# wiki/sync.sh — Known Issues (Mac Claude Code)

> Reviewed 2026-05-25. Four bugs found in the updated sync.sh. None cause errors (guards prevent crashes) but three cause silent data loss — wiki-ha, stats, and off-branch pushes will silently do nothing useful.

---

## Issue 1 — `wiki-ha/` will never sync (SILENT)

**Line 44:** `wiki-ha` is in the rsync loop, so it looks for `$VAULT/wiki/wiki-ha/`.
The actual path is `$VAULT/wiki-ha/` — a sibling of `wiki/`, not inside it.
The `[ -d ]` guard silently skips it. No error, no sync.

**Fix needed in `sync.sh`:**
```bash
# After the main rsync loop, add:
WIKI_HA_SRC="$VAULT/wiki-ha"
if [ -d "$WIKI_HA_SRC" ]; then
  mkdir -p "$REPO_ROOT/wiki-ha"
  rsync -a --delete \
    --include='*/' \
    --include='*.md' \
    --exclude='*' \
    "$WIKI_HA_SRC/" "$REPO_ROOT/wiki-ha/"
  echo "  synced: wiki-ha/ (from vault root)"
fi
```
Also change `git add wiki/` → `git add wiki/ wiki-ha/` on line 91.

---

## Issue 2 — Push goes to current branch, not `main` (SILENT)

**Line 95:** `git push -u origin "$(git rev-parse --abbrev-ref HEAD)"`
If you run `vault github sync` while on a feature branch, the wiki content is pushed to that branch. Claude.ai raw URLs point to `main` — so the update is invisible.

**Fix needed in `sync.sh`:**
```bash
# Replace the push block with:
CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
if [ "$CURRENT_BRANCH" != "main" ]; then
  echo "WARNING: Not on main (on '$CURRENT_BRANCH'). Pushing wiki commit to main via temp merge."
  git push -u origin "$CURRENT_BRANCH"
  echo "NOTE: Claude.ai reads from main — run 'git checkout main && git merge $CURRENT_BRANCH && git push' to publish."
else
  git push -u origin main
fi
```
Or simpler: always stash, switch to main, cherry-pick the commit, push, switch back.

---

## Issue 3 — `wiki/stats/` not synced

`wiki/stats/` (baseline files, nlm-sync-state.json, snapshots) is not in the rsync loop.
Low priority — Claude.ai doesn't need stats — but means stats data is never in the repo and can't be recovered from GitHub.

**Fix needed in `sync.sh`:** Add `stats` to the rsync loop (line 44):
```bash
for subdir in concepts entities sources syntheses stats; do
```
(Remove `wiki-ha` from this loop per Issue 1.)

---

## Issue 4 — `generate_wiki_index.py` path not confirmed

**Line 35:** Assumed at `$VAULT/generate_wiki_index.py`.
If it lives elsewhere (e.g. `$VAULT/scripts/generate_wiki_index.py`) it silently skips — index won't be regenerated before sync.

**Action needed:** On Mac, run `find "$VAULT" -name "generate_wiki_index.py"` once to confirm the actual path, then hardcode or update the GENERATOR variable in sync.sh if it differs.

---

## Outstanding automation gaps (not sync.sh bugs)

These require changes to `~/.claude/settings.json` on Mac — not to sync.sh:

| Gap | Fix |
|-----|-----|
| sync.sh runs manually only | Add `StopHook` to `~/.claude/settings.json`: `bash ~/path/to/wiki/sync.sh` |
| NLM not synced after sessions | Add `vault ingest nlm` to same StopHook |
| Web sessions start blind | Add `curl` of raw GitHub index.md/log.md to SessionStart hook |

---

## Priority order

1. **Issue 2** (branch push) — fix first or all syncs go nowhere useful
2. **Issue 1** (wiki-ha) — fixes HA wiki appearing in repo
3. **StopHook** — makes sync automatic after every Mac session
4. **Issue 3** (stats) — low priority
5. **Issue 4** (generator path) — verify once manually
