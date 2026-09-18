> `davinci-tools.html` dashboard wired to a 284-tool `cutmaster_ai` backend; verified end-to-end via a real DaVinci Resolve timeline cut on 2026-06-13. Known gap: ffmpeg not on PATH.

# Cutmaster AI — DaVinci Tools Dashboard

## What it is
A dashboard (`davinci-tools.html`) driving a 284-tool `cutmaster_ai` backend for DaVinci Resolve automation. Pipeline: Deepgram STT → preset detection → build → execute.

## Verified
End-to-end pipeline confirmed working via a real DaVinci Resolve timeline cut, 2026-06-13 — not just a dry-run/API-success check.

## Known gap
`ffmpeg` is not on PATH for normal launches. Current workaround borrows AutoCut's bundled ffmpeg binary. Not a proper fix.

## Status
Working, but: (1) `ffmpeg` PATH gap unresolved, (2) work was uncommitted as of the source session — verify git state before assuming this is saved.

## Related
- Git hosting for this project moved to Codeberg/Forgejo after a GitHub account suspension — see [[cutmaster-ai-git-hosting]]
