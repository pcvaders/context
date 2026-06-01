import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime
import os
import time
import keyring
from spotipy.exceptions import SpotifyException

# ── Credentials (App 1) — keychain 'djbrightone-spotify' or env DJB_SPOTIFY_<KEY> ──
def _secret(key):
    val = os.environ.get(f"DJB_SPOTIFY_{key}") or keyring.get_password('djbrightone-spotify', key)
    if not val:
        raise RuntimeError(f"Missing Spotify credential '{key}' (env DJB_SPOTIFY_{key} or keychain).")
    return val

SPOTIPY_CLIENT_ID     = _secret('CLIENT_ID_APP1')
SPOTIPY_CLIENT_SECRET = _secret('CLIENT_SECRET_APP1')
SPOTIPY_REDIRECT_URI  = 'http://127.0.0.1:8888/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-modify-public playlist-modify-private playlist-read-private"
))

# ── Reference: Armada New Releases (official Armada Music playlist) ──
REFERENCE_PLAYLIST_ID = '1PxHGM0mEwWroAfak61dY4'
# TODO: Replace with promoter's dedicated EDM playlist ID when confirmed

USERNAME = sp.current_user()['id']
TODAY    = datetime.date.today()
FOLDER   = TODAY.strftime("%Y-%m-%d_EDM")
os.makedirs(FOLDER, exist_ok=True)

def safe_call(func, *args, **kwargs):
    for attempt in range(5):
        try:
            return func(*args, **kwargs)
        except SpotifyException as e:
            if e.http_status == 429:
                time.sleep(int(e.headers.get("Retry-After", 5)))
            elif 500 <= e.http_status < 600:
                time.sleep(2 ** attempt)
            else:
                raise
        except Exception as ex:
            print(f"Unexpected error: {ex}")
            time.sleep(2)
    raise Exception("Max retries exceeded")

def chunk_list(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

def get_recent_releases(artist_ids):
    cutoff = TODAY - datetime.timedelta(days=7)
    album_ids = []
    for aid in artist_ids:
        albums = safe_call(sp.artist_albums, aid, album_type='single')
        for album in albums['items']:
            rd = album.get('release_date', '')
            if len(rd) == 10:
                if datetime.datetime.strptime(rd, '%Y-%m-%d').date() >= cutoff:
                    album_ids.append(album['id'])

    print(f"Found {len(album_ids)} recent singles.")
    new_tracks = []
    for batch in chunk_list(album_ids, 20):
        objs = safe_call(sp.albums, batch)['albums']
        for album in objs:
            if album and 'tracks' in album:
                new_tracks.extend(album['tracks']['items'])
        time.sleep(0.25)
    return new_tracks

print("Fetching Armada Music reference playlist artists...")
ref_tracks = safe_call(sp.playlist_tracks, REFERENCE_PLAYLIST_ID)['items']
artist_ids = list({t['track']['artists'][0]['id'] for t in ref_tracks if t.get('track')})
print(f"Found {len(artist_ids)} unique artists.")

print("Checking for new releases in the past 7 days...")
new_tracks = get_recent_releases(artist_ids)

if new_tracks:
    track_ids = [t['id'] for t in new_tracks if t.get('id')]
    playlist_name = TODAY.strftime("%Y-%m-%d EDM")
    new_playlist = safe_call(sp.user_playlist_create, USERNAME, playlist_name, public=False)
    for chunk in chunk_list(track_ids, 100):
        safe_call(sp.playlist_add_items, new_playlist['id'], chunk)
    print(f"{len(track_ids)} new EDM tracks added to '{playlist_name}'.")
else:
    print("No new EDM tracks found this week.")
