import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime
import os
import time
from spotipy.exceptions import SpotifyException

# ── Credentials ────────────────────────────────────────────────────────────────
CLIENT_ID_APP1     = '***REMOVED***'   # release_radar, remix, edm
CLIENT_SECRET_APP1 = '***REMOVED***'
CLIENT_ID_APP2     = '***REMOVED***'   # dnb, rnb
CLIENT_SECRET_APP2 = '***REMOVED***'
REDIRECT_URI       = 'http://127.0.0.1:8888/callback'
SCOPE              = (
    "playlist-modify-public playlist-modify-private "
    "playlist-read-private playlist-read-collaborative"
)

# ── Playlist IDs ───────────────────────────────────────────────────────────────
# Release Radar: Spotify blocks API access to personalised playlists.
# Step 1 will attempt to read it — if Spotify allows it, the copy is auto-refreshed.
# If blocked (404/403), Step 1 skips gracefully and Steps 2–6 run on the existing copy.
# Manual fallback: Spotify app → Release Radar → Select All → Add to playlist → Release Radar Copy
RELEASE_RADAR_ID      = '37i9dQZEVXboEoTOVLo0jR'
RELEASE_RADAR_COPY_ID = '5eY6y3BV1LU6fQoAfNRKsl'
DNB_REF_1             = '0yybc8ObzsQyoAE55ILZGt'   # user DNB reference
DNB_REF_2             = '5Ik2wnYMLvpqhvdklDBVR0'   # promoter DNB reference (read-only)
RNB_REF               = '1cuMaxb31EuQdg8jMp6yqv'
EDM_REF               = '1PxHGM0mEwWroAfak61dY4'   # Armada New Releases (read-only)

ADDED_REMIXES_FILE = 'added_remixes.txt'
LOG_FILE = f"workflow_log_{datetime.date.today().strftime('%Y-%m-%d')}.txt"

# ── WORKFLOW ORDER ─────────────────────────────────────────────────────────────
# Step 1 — Attempt to sync Release Radar Copy from Release Radar.
#           READ-FIRST: only erases copy if Release Radar is accessible.
#           If Spotify blocks access, skips gracefully — copy retains last content.
#           Manual fallback: add this week's Release Radar to Copy before running.
# Step 2 — Release Radar remix finder (runs on whatever is in Copy)
# Step 3 — Broad remix search (separate, uses added_remixes.txt for dedup)
# Step 4 — DNB new releases (merged: user ref + promoter ref)
# Step 5 — R&B new releases
# Step 6 — EDM new releases (Armada Music roster)

# ── Logging ───────────────────────────────────────────────────────────────────
def log(msg):
    print(msg)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(msg + '\n')

# ── Shared helpers ────────────────────────────────────────────────────────────
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
            log(f"Unexpected: {ex}")
            time.sleep(2)
    raise Exception("Max retries exceeded")

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def is_english(track):
    markets = track.get('available_markets', [])
    return 'GB' in markets or 'US' in markets

def get_isrc(track):
    return track.get('external_ids', {}).get('isrc', '')

def get_all_playlist_tracks(sp, playlist_id):
    items, offset = [], 0
    while True:
        r = safe_call(sp.playlist_items, playlist_id, offset=offset, limit=100)
        batch = r.get('items', [])
        if not batch:
            break
        items.extend(batch)
        offset += len(batch)
        if not r.get('next'):
            break
    return items

# ── Step 1: Attempt to sync Release Radar Copy ────────────────────────────────
# READ-FIRST design: fetch Release Radar tracks before touching the copy.
# If Spotify blocks access (404/403), the copy is left untouched and the workflow
# continues with whatever the user has already added manually.
def sync_release_radar(sp):
    log("\n=== STEP 1: Release Radar Sync (attempt) ===")

    log(f"Attempting to read Release Radar ({RELEASE_RADAR_ID})...")
    try:
        rr_items = get_all_playlist_tracks(sp, RELEASE_RADAR_ID)
        rr_uris = [i['track']['uri'] for i in rr_items if i.get('track')]
    except SpotifyException as e:
        if e.http_status in (403, 404):
            log(
                f"  Spotify blocked access to Release Radar (HTTP {e.http_status}) — "
                "this is expected for personalised playlists.\n"
                "  Skipping auto-sync. Copy retains its current content.\n"
                "  Manual update: Spotify app → Release Radar → Select All → "
                "Add to playlist → Release Radar Copy."
            )
            return
        raise
    except Exception as e:
        log(f"  Could not read Release Radar: {e}\n  Skipping auto-sync.")
        return

    if not rr_uris:
        log("  Release Radar appears empty — skipping sync.")
        return

    log(f"  Read {len(rr_uris)} tracks from Release Radar. Refreshing copy...")
    existing = get_all_playlist_tracks(sp, RELEASE_RADAR_COPY_ID)
    existing_uris = [i['track']['uri'] for i in existing if i.get('track')]
    for chunk in chunks(existing_uris, 100):
        safe_call(sp.playlist_remove_all_occurrences_of_items, RELEASE_RADAR_COPY_ID, chunk)
    log(f"  Erased {len(existing_uris)} old tracks.")

    for chunk in chunks(rr_uris, 100):
        safe_call(sp.playlist_add_items, RELEASE_RADAR_COPY_ID, chunk)
    log(f"  Done. {len(rr_uris)} tracks copied. Release Radar Copy is ready.")

# ── Step 2: Release Radar Remix Finder ───────────────────────────────────────
def release_radar_remixes(sp):
    log("\n=== STEP 2: Release Radar Remix Finder ===")
    today = datetime.date.today().strftime('%Y-%m-%d')
    seen_isrcs, track_ids = set(), []

    copy_items = get_all_playlist_tracks(sp, RELEASE_RADAR_COPY_ID)
    if not copy_items:
        log("  Release Radar Copy is empty — nothing to scan.")
        log("  Add this week's Release Radar to the copy manually and re-run if needed.")
        return

    for item in copy_items:
        track = item.get('track')
        if not track or 'remix' not in track['name'].lower():
            continue
        if not is_english(track):
            continue
        code = get_isrc(track)
        if code and code in seen_isrcs:
            log(f"  SKIP dupe ISRC: {track['name']}")
            continue
        if code:
            seen_isrcs.add(code)
        track_ids.append(track['id'])

    if track_ids:
        uid = safe_call(sp.current_user)['id']
        name = f"\U0001f3a7 Release Radar Remixes - {today}"
        pl = safe_call(sp.user_playlist_create, uid, name, public=True)
        for chunk in chunks(track_ids, 100):
            safe_call(sp.playlist_add_items, pl['id'], chunk)
        log(f"  Created '{name}' — {len(track_ids)} remixes.")
    else:
        log("  No remixes found in Release Radar Copy.")

# ── Step 3: Broad Remix Search ────────────────────────────────────────────────
def broad_remix_search(sp):
    log("\n=== STEP 3: Broad Remix Search ===")
    today = datetime.date.today()
    last_week = (today - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

    previously_added = set()
    if os.path.exists(ADDED_REMIXES_FILE):
        with open(ADDED_REMIXES_FILE, 'r', encoding='utf-8') as f:
            previously_added = {l.strip() for l in f if l.strip()}

    found = []
    for offset in range(0, 1000, 50):
        r = safe_call(sp.search, q="remix", type="track", limit=50, offset=offset)
        tracks = r['tracks']['items']
        if not tracks:
            break
        for t in tracks:
            if 'remix' not in t['name'].lower():
                continue
            if t['album']['release_date'] < last_week:
                continue
            if not is_english(t):
                continue
            if t['id'] not in previously_added:
                found.append(t['id'])

    unique = list(set(found))
    if unique:
        uid = safe_call(sp.current_user)['id']
        name = f"New Remixes - {today.strftime('%Y-%m-%d')}"
        pl = safe_call(sp.user_playlist_create, uid, name, public=True)
        safe_call(sp.playlist_add_items, pl['id'], unique)
        with open(ADDED_REMIXES_FILE, 'a', encoding='utf-8') as f:
            f.write('\n'.join(unique) + '\n')
        log(f"  Created '{name}' — {len(unique)} new remixes.")
    else:
        log("  No new remixes found.")

# ── Steps 4–6: Genre New Releases ─────────────────────────────────────────────
def genre_releases(sp, genre_name, ref_playlist_ids, folder_tag):
    log(f"\n=== {genre_name} New Releases ===")
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=7)

    artist_ids = set()
    for pid in ref_playlist_ids:
        if not pid:
            continue
        try:
            for item in get_all_playlist_tracks(sp, pid):
                t = item.get('track')
                if t and t.get('artists'):
                    artist_ids.add(t['artists'][0]['id'])
        except Exception as e:
            log(f"  Could not read playlist {pid}: {e}")

    log(f"  {len(artist_ids)} unique artists across {len([p for p in ref_playlist_ids if p])} playlist(s).")

    album_ids = []
    for aid in artist_ids:
        try:
            r = safe_call(sp.artist_albums, aid, album_type='single')
            for album in r['items']:
                rd = album.get('release_date', '')
                if len(rd) == 10:
                    if datetime.datetime.strptime(rd, '%Y-%m-%d').date() >= cutoff:
                        album_ids.append(album['id'])
        except Exception as e:
            log(f"  Error on artist {aid}: {e}")

    new_tracks = []
    for batch in chunks(album_ids, 20):
        objs = safe_call(sp.albums, batch)['albums']
        for album in objs:
            if album and 'tracks' in album:
                new_tracks.extend(album['tracks']['items'])
        time.sleep(0.25)

    if new_tracks:
        track_ids = [t['id'] for t in new_tracks if t.get('id')]
        uid = safe_call(sp.current_user)['id']
        name = today.strftime(f"%Y-%m-%d {genre_name}")
        pl = safe_call(sp.user_playlist_create, uid, name, public=False)
        for chunk in chunks(track_ids, 100):
            safe_call(sp.playlist_add_items, pl['id'], chunk)
        os.makedirs(today.strftime(f"%Y-%m-%d_{folder_tag}"), exist_ok=True)
        log(f"  Created '{name}' — {len(track_ids)} tracks.")
    else:
        log(f"  No new {genre_name} releases found.")

# ── Main ───────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    log(f"\n{'='*55}")
    log(f"djbrightone Monday Workflow — {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} UTC")
    log(f"{'='*55}")
    log("Step 1 attempts Release Radar auto-sync. If Spotify blocks it, Steps 2-6 still run.")

    sp1 = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID_APP1, client_secret=CLIENT_SECRET_APP1,
        redirect_uri=REDIRECT_URI, scope=SCOPE
    ))
    sp2 = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID_APP2, client_secret=CLIENT_SECRET_APP2,
        redirect_uri=REDIRECT_URI, scope=SCOPE
    ))

    steps = [
        ("Step 1 — Release Radar Sync",    lambda: sync_release_radar(sp1)),
        ("Step 2 — Release Radar Remixes", lambda: release_radar_remixes(sp1)),
        ("Step 3 — Broad Remix Search",    lambda: broad_remix_search(sp1)),
        ("Step 4 — DNB New Releases",      lambda: genre_releases(sp2, "DNB", [DNB_REF_1, DNB_REF_2], "DNB")),
        ("Step 5 — R&B New Releases",      lambda: genre_releases(sp2, "R&B", [RNB_REF], "RNB")),
        ("Step 6 — EDM New Releases",      lambda: genre_releases(sp1, "EDM", [EDM_REF], "EDM")),
    ]

    for step_name, fn in steps:
        try:
            fn()
        except Exception as e:
            log(f"ERROR in {step_name}: {e}")

    log(f"\nWorkflow complete — {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} UTC")

    # Record pipeline ROI (non-blocking, best-effort)
    try:
        import subprocess, sys
        roi_script = os.path.join(
            os.path.expanduser("~"),
            "Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Vault Icloud/Obsidian Vault AI/roi_evaluator.py"
        )
        if os.path.exists(roi_script):
            subprocess.Popen(
                [sys.executable, roi_script, "--pipeline", "spotify-monday"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
    except Exception:
        pass
