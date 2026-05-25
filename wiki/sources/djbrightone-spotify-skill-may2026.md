---
title: djbrightone-spotify Skill — Setup & Launchd Automation (May 2026)
summary: "May 2026 Spotify Monday workflow setup, launchd plist automation, two-app Spotipy architecture, diagnosis of why automation never fired (wrong python path + never installed to LaunchAgents)."
tags: [spotify, launchd, automation, macos, spotipy, skills]
source-type: manual-session-notes
date: 2026-05-25
---

# djbrightone-spotify Skill — Setup & Launchd Automation (May 2026)

> Manual notes from Claude Code session 2026-05-25. Source: `~/claude-skills/skills/djbrightone-spotify/`. Not in any Claude.ai export — this session occurred in Claude Code directly.

## Skill Location

```
~/claude-skills/skills/djbrightone-spotify/
├── SKILL.md                    # full skill documentation
└── scripts/
    ├── run_monday_workflow.py  # main 6-step pipeline (13,463 bytes)
    └── com.djbrightone.spotify.monday.plist  # launchd plist (source of truth)
```

Installed plist: `~/Library/LaunchAgents/com.djbrightone.spotify.monday.plist`

## What the Workflow Does

6-step pipeline run every Monday at 14:00 BST:

| Step | Action |
|---|---|
| 1 | Release Radar sync (gracefully skips if Spotify blocks 404/403) |
| 2 | Release Radar remix finder (ISRC dedup, English-only UK/US market) |
| 3 | Broad remix search (dedup via `added_remixes.txt`) |
| 4 | DNB new releases (merged user ref + promoter ref) |
| 5 | R&B new releases |
| 6 | EDM new releases (Armada Music roster) |

First manual run result (2026-05-25 15:15 UTC): 17 Release Radar remixes, 5 new broad remixes, 18 DNB tracks, 9 R&B tracks, 98 EDM tracks.

## Two-App Architecture

Two Spotify developer apps to stay within dev mode rate limits:

| App | Client ID prefix | Used for |
|---|---|---|
| App1 | 5e329e33 | Remix finder, EDM searches |
| App2 | 168ae63f | DNB + R&B searches |

## Working Directory

`/Users/voyager1/Library/CloudStorage/GoogleDrive-pcgamesplay1@gmail.com/My Drive/spotify-remix/`

State files (`added_remixes.txt`, logs, dated output folders) persist in Google Drive.

## Launchd Schedule

```xml
<key>StartCalendarInterval</key>
<dict>
    <key>Weekday</key><integer>1</integer>  <!-- Monday -->
    <key>Hour</key><integer>14</integer>    <!-- 14:00 local time -->
    <key>Minute</key><integer>0</integer>
</dict>
```

UK timezone note: fires at 14:00 BST (13:00 UTC) in summer, 14:00 UTC in winter.

Logs: `~/Library/Logs/djbrightone-spotify.log` (stdout) and `-error.log` (stderr).

## Root Cause Diagnosis (Why It Never Fired)

**Two compounding failures:**

1. **Wrong Python path** — plist used `/usr/bin/python3` which has no spotipy installed. Fix: `/opt/miniconda3/bin/python3`.

2. **Never installed** — plist was created in Claude.ai web session on May 21 2026, saved to Google Drive and GitHub, but never `cp`'d to `~/Library/LaunchAgents/` and never `launchctl load`'d.

The "missing chat" was not missing — it was a Claude.ai web session (not Claude Code). Web sessions are separate from Claude Code; no shared history.

**Fix applied 2026-05-25:**
```bash
# Fix python path in plist (already done — commit 9d734ea in ~/claude-skills)
git pull  # get updated plist

# Install
cp ~/claude-skills/skills/djbrightone-spotify/scripts/com.djbrightone.spotify.monday.plist \
   ~/Library/LaunchAgents/

# Load
launchctl load ~/Library/LaunchAgents/com.djbrightone.spotify.monday.plist

# Verify
launchctl list | grep djbrightone

# Manual run (since 14:00 already passed for today)
cd "/Users/voyager1/Library/CloudStorage/GoogleDrive-.../My Drive/spotify-remix"
/opt/miniconda3/bin/python3 ~/claude-skills/skills/djbrightone-spotify/scripts/run_monday_workflow.py
```

**Broken venv** (`myenv/`): Created by jamesflood user on different machine, points to missing homebrew python3.12. Not used — miniconda used instead.

## LaunchAgents Pattern (macOS Automation)

For any macOS scheduled task via launchd:

1. Create plist in repo (source of truth)
2. `cp` to `~/Library/LaunchAgents/`
3. `launchctl load <path>` (only needed once)
4. `launchctl list | grep <label>` to verify

Reload after changes:
```bash
launchctl unload ~/Library/LaunchAgents/<label>.plist
launchctl load ~/Library/LaunchAgents/<label>.plist
```

Python path: always use `/opt/miniconda3/bin/python3` (has all packages), not `/usr/bin/python3` (system Python, bare).

## GitHub Repo

`PCGamesplay1/Claude-skills` — plist at `skills/djbrightone-spotify/scripts/com.djbrightone.spotify.monday.plist`

Commit 9d734ea: python path fix (not yet pushed as of 2026-05-25).

## Links

- [[claude-code-skills]] — skill system overview
- [[skill-ecosystem]] — voyager1 skill stack
