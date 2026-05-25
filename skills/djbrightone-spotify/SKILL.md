---
name: djbrightone-spotify
description: "DJ Brightone's weekly Spotify workflow. Use when asked to run the Monday workflow, import a promoter's artist list, prune inactive artists, or manage the DNB/R&B/EDM reference playlists. All scripts live in Google Drive spotify-remix folder."
license: Private
---

# djbrightone Spotify Skill

Weekly automated Spotify workflow for DJ Brightone. Scripts live in this repo under `skills/djbrightone-spotify/scripts/`. Runtime state (`.cache`, `added_remixes.txt`, dated output folders) lives in Google Drive at `My Drive/spotify-remix/`.

---

## Monday Workflow

Runs automatically every Monday at 14:00 local time via launchd. To trigger manually:

```bash
cd "/Users/voyager1/Library/CloudStorage/GoogleDrive-pcgamesplay1@gmail.com/My Drive/spotify-remix"
python3 ~/claude-skills/skills/djbrightone-spotify/scripts/run_monday_workflow.py
```

**Order of operations:**
1. Attempt to sync Release Radar Copy from Release Radar — read-first: only erases and refills if Spotify allows API access. If blocked (Spotify intentionally restricts personalised playlists), skips gracefully and Steps 2–6 still run on the existing copy.
2. Extract remixes from Release Radar Copy (ISRC dedup, English-only via UK/US market)
3. Broad remix search across Spotify (dedup via `added_remixes.txt`, English-only)
4. DNB new releases (merged: user ref + promoter ref)
5. R&B new releases
6. EDM new releases (Armada Music roster via Armada New Releases playlist)

**Release Radar limitation:** Spotify blocks API access to "Made for You" personalised playlists (Release Radar, Discover Weekly, etc.). Step 1 attempts access but will likely be blocked. When it is, the copy is left untouched — it is never erased unless a successful read confirms Release Radar is accessible.

**Manual update (takes ~2 min, do before running):**
1. Spotify app → Release Radar → `...` → Select All → Add to playlist → **Release Radar Copy**
2. Then run `python3 run_monday_workflow.py` — Steps 2–6 handle the rest automatically

**Playlist IDs:**

| Name | ID | Owner |
|---|---|---|
| Release Radar | `37i9dQZEVXboEoTOVLo0jR` | Spotify |
| Release Radar Copy | `5eY6y3BV1LU6fQoAfNRKsl` | User |
| DNB user ref | `0yybc8ObzsQyoAE55ILZGt` | User (editable) |
| DNB promoter ref | `5Ik2wnYMLvpqhvdklDBVR0` | Promoter (read-only) |
| R&B ref | `1cuMaxb31EuQdg8jMp6yqv` | User (editable) |
| EDM ref (Armada) | `1PxHGM0mEwWroAfak61dY4` | Armada Music (read-only) |

---

## Artist Maintenance

Run manually — human-triggered only. Never runs as part of Monday automation.

### Import promoter's artist list

1. Paste artist names (one per line) into `artists_to_add.txt` in the spotify-remix folder
2. Generate review: `python3 ~/claude-skills/skills/djbrightone-spotify/scripts/maintain_artists.py --import`
3. Open `artist_import_review_YYYY-MM-DD.txt` — verify each Spotify match is correct
4. Apply: `python3 ~/claude-skills/skills/djbrightone-spotify/scripts/maintain_artists.py --import --apply`

Non-English artists are filtered automatically (no UK/US market availability).

### Prune inactive artists (12-month threshold)

```bash
python3 ~/claude-skills/skills/djbrightone-spotify/scripts/maintain_artists.py --prune           # generate internal report
python3 ~/claude-skills/skills/djbrightone-spotify/scripts/maintain_artists.py --prune --apply   # remove flagged artists
```

Only affects owned playlists (DNB user ref, R&B). Promoter and Armada playlists are never auto-modified.

---

## EDM Reference

Currently seeded from Armada Music's official **Armada New Releases** playlist (`1PxHGM0mEwWroAfak61dY4`), covering the full Armada roster including Armin van Buuren.

When promoter's dedicated EDM playlist is confirmed, update `EDM_REF` in `run_monday_workflow.py` and `REFERENCE_PLAYLIST_ID` in `spotifyedm.py`.

---

## launchd Setup (one-time, on Mac)

First clone the repo if not already done:
```bash
git clone https://github.com/pcgamesplay1/claude-skills.git ~/claude-skills
```

Then load the plist:
```bash
cp ~/claude-skills/skills/djbrightone-spotify/scripts/com.djbrightone.spotify.monday.plist \
   ~/Library/LaunchAgents/

launchctl load ~/Library/LaunchAgents/com.djbrightone.spotify.monday.plist
```

To update scripts in future: `cd ~/claude-skills && git pull` — no file management needed.

Verify it loaded:
```bash
launchctl list | grep djbrightone
```

View live logs:
```bash
tail -f ~/Library/Logs/djbrightone-spotify.log
```

**BST note:** launchd uses local time. UK is UTC in winter, UTC+1 in summer (BST: late March–late October). Change `Hour` in the plist from `14` to `13` during BST if strict 14:00 UTC is required.

---

## Credentials

| App | Client ID prefix | Scripts |
|---|---|---|
| App 1 | `5e329e33...` | release_radar, remix, EDM |
| App 2 | `168ae63f...` | DNB, R&B, maintain_artists |

Two separate Spotify developer apps are used to stay within Spotify's dev mode limits.
