import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime
import sys
import os
import time
import keyring
from spotipy.exceptions import SpotifyException

# ── Credentials (App 2) — keychain 'djbrightone-spotify' or env DJB_SPOTIFY_<KEY> ──
def _secret(key):
    val = os.environ.get(f"DJB_SPOTIFY_{key}") or keyring.get_password('djbrightone-spotify', key)
    if not val:
        raise RuntimeError(f"Missing Spotify credential '{key}' (env DJB_SPOTIFY_{key} or keychain).")
    return val

SPOTIPY_CLIENT_ID     = _secret('CLIENT_ID_APP2')
SPOTIPY_CLIENT_SECRET = _secret('CLIENT_SECRET_APP2')
SPOTIPY_REDIRECT_URI  = 'http://127.0.0.1:8888/callback'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-modify-public playlist-modify-private playlist-read-private"
))

# ── Playlists we OWN (can modify) ──────────────────────────────
OWNED_PLAYLISTS = {
    'dnb': '0yybc8ObzsQyoAE55ILZGt',
    'rnb': '1cuMaxb31EuQdg8jMp6yqv',
}
# Read-only — never auto-modified:
#   DNB promoter ref : 5Ik2wnYMLvpqhvdklDBVR0
#   EDM Armada ref   : 1PxHGM0mEwWroAfak61dY4

PRUNE_MONTHS = 12

# ── Helpers ────────────────────────────────────────────────
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

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def is_english(artist_id):
    try:
        albums = safe_call(sp.artist_albums, artist_id, album_type='single', limit=1)
        if albums['items']:
            tracks = safe_call(sp.album_tracks, albums['items'][0]['id'], limit=1)
            if tracks['items']:
                markets = tracks['items'][0].get('available_markets', [])
                return 'GB' in markets or 'US' in markets
    except Exception:
        pass
    return True  # include if uncertain

def last_release_date(artist_id):
    try:
        albums = safe_call(sp.artist_albums, artist_id, album_type='single,album', limit=5)
        dates = []
        for a in albums['items']:
            rd = a.get('release_date', '')
            if len(rd) == 10:
                dates.append(datetime.datetime.strptime(rd, '%Y-%m-%d').date())
        return max(dates) if dates else None
    except Exception:
        return None

def get_playlist_artists(playlist_id):
    artists = {}
    offset = 0
    while True:
        r = safe_call(sp.playlist_tracks, playlist_id, offset=offset, limit=100)
        for item in r.get('items', []):
            t = item.get('track')
            if t and t.get('artists'):
                a = t['artists'][0]
                artists[a['id']] = a['name']
        offset += len(r.get('items', []))
        if not r.get('next'):
            break
    return artists

def get_latest_track_uri(artist_id):
    try:
        albums = safe_call(sp.artist_albums, artist_id, album_type='single', limit=1)
        if albums['items']:
            tracks = safe_call(sp.album_tracks, albums['items'][0]['id'], limit=1)
            if tracks['items']:
                return tracks['items'][0]['uri']
    except Exception:
        pass
    return None

# ── Import Mode ────────────────────────────────────────────────
def mode_import(apply=False):
    try:
        with open('artists_to_add.txt', 'r', encoding='utf-8') as f:
            names = [l.strip() for l in f if l.strip() and not l.startswith('#')]
    except FileNotFoundError:
        print("ERROR: artists_to_add.txt not found.")
        print("Create it with one artist name per line (paste from promoter's message).")
        return

    today = datetime.date.today().strftime('%Y-%m-%d')
    report = f"artist_import_review_{today}.txt"
    found, not_found = [], []

    print(f"Searching Spotify for {len(names)} artists...")
    for name in names:
        r = safe_call(sp.search, q=name, type='artist', limit=3)
        artists = r['artists']['items']
        if artists:
            a = artists[0]
            found.append({
                'query':     name,
                'name':      a['name'],
                'id':        a['id'],
                'followers': a['followers']['total'],
                'genres':    ', '.join(a['genres'][:3]) or 'N/A',
                'english':   is_english(a['id']),
                'url':       a['external_urls']['spotify'],
            })
        else:
            not_found.append(name)
        time.sleep(0.1)

    with open(report, 'w', encoding='utf-8') as f:
        f.write(f"Artist Import Review — {today}\n")
        f.write("=" * 60 + "\n")
        f.write("Instructions:\n")
        f.write("  1. Verify each Spotify match is correct\n")
        f.write("  2. Set TARGET below (dnb or rnb)\n")
        f.write("  3. Run: python3 maintain_artists.py --import --apply\n\n")
        f.write("TARGET: dnb\n\n")
        f.write("SUGGESTED ADDS:\n")
        for r2 in found:
            flag = "English OK" if r2['english'] else "WARNING: non-English"
            f.write(f"  {r2['query']} -> {r2['name']} | {r2['followers']:,} followers | {r2['genres']} | {flag}\n")
            f.write(f"    {r2['url']}\n")
        if not_found:
            f.write(f"\nNOT FOUND ({len(not_found)}):\n")
            for n in not_found:
                f.write(f"  - {n}\n")

    print(f"Review file created: {report}")
    print("Check matches, then run with --apply to add to Spotify.")

    if apply:
        target = input("Add to which playlist? (dnb/rnb): ").strip().lower()
        if target not in OWNED_PLAYLISTS:
            print(f"Unknown target '{target}'. Use 'dnb' or 'rnb'.")
            return
        playlist_id = OWNED_PLAYLISTS[target]
        added = 0
        for r2 in found:
            if not r2['english']:
                print(f"  SKIP non-English: {r2['name']}")
                continue
            uri = get_latest_track_uri(r2['id'])
            if uri:
                safe_call(sp.playlist_add_items, playlist_id, [uri])
                print(f"  ADDED: {r2['name']}")
                added += 1
            else:
                print(f"  SKIP (no recent track found): {r2['name']}")
        print(f"\nAdded {added} artists to {target.upper()} reference playlist.")

# ── Prune Mode ─────────────────────────────────────────────────
def mode_prune(apply=False):
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=PRUNE_MONTHS * 30)
    report = f"artist_prune_review_{today.strftime('%Y-%m-%d')}.txt"

    print(f"Checking for artists inactive since {cutoff.strftime('%Y-%m-%d')}...")
    flagged = {}

    for label, pid in OWNED_PLAYLISTS.items():
        print(f"  Scanning {label.upper()} reference playlist...")
        artists = get_playlist_artists(pid)
        flagged[label] = []
        for aid, name in artists.items():
            last = last_release_date(aid)
            if last is None or last < cutoff:
                flagged[label].append({
                    'id':           aid,
                    'name':         name,
                    'last_release': last.strftime('%Y-%m-%d') if last else 'none found',
                })
            time.sleep(0.1)

    with open(report, 'w', encoding='utf-8') as f:
        f.write(f"Artist Prune Review — {today.strftime('%Y-%m-%d')}\n")
        f.write(f"Inactive threshold: {PRUNE_MONTHS} months (cutoff: {cutoff.strftime('%Y-%m-%d')})\n")
        f.write("=" * 60 + "\n")
        f.write("Internal log only. Run with --prune --apply to remove.\n")
        f.write("Note: Promoter DNB + Armada EDM playlists are read-only and not pruned here.\n\n")
        total = 0
        for label, artists in flagged.items():
            f.write(f"{label.upper()} — {len(artists)} flagged:\n")
            for a in artists:
                f.write(f"  - {a['name']} | Last release: {a['last_release']}\n")
            total += len(artists)
        f.write(f"\nTotal flagged: {total}\n")

    print(f"Prune report saved: {report}")
    print(f"Total flagged: {sum(len(v) for v in flagged.values())}")

    if apply:
        for label, pid in OWNED_PLAYLISTS.items():
            to_remove = flagged.get(label, [])
            if not to_remove:
                continue
            remove_ids = {a['id'] for a in to_remove}
            all_items, offset = [], 0
            while True:
                r = safe_call(sp.playlist_tracks, pid, offset=offset, limit=100)
                for item in r.get('items', []):
                    t = item.get('track')
                    if t and t.get('artists') and t['artists'][0]['id'] in remove_ids:
                        all_items.append({'uri': t['uri']})
                offset += len(r.get('items', []))
                if not r.get('next'):
                    break
            for chunk in chunks(all_items, 100):
                safe_call(sp.playlist_remove_all_occurrences_of_items, pid, chunk)
            print(f"  Removed {len(to_remove)} artists from {label.upper()}.")

# ── Entry Point ────────────────────────────────────────────────
if __name__ == '__main__':
    args = sys.argv[1:]
    apply = '--apply' in args

    if '--import' in args:
        mode_import(apply=apply)
    elif '--prune' in args:
        mode_prune(apply=apply)
    else:
        print("Usage:")
        print("  python3 maintain_artists.py --import          # Review promoter's artist list")
        print("  python3 maintain_artists.py --import --apply  # Apply approved adds")
        print("  python3 maintain_artists.py --prune           # Check for inactive artists (12mo)")
        print("  python3 maintain_artists.py --prune --apply   # Remove inactive artists")
