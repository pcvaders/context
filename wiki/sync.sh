#!/usr/bin/env bash
# Syncs key wiki files from the iCloud/Obsidian vault into this repo's wiki/ and
# wiki-personal/ directories, then commits and pushes so Claude.ai can read the
# latest content via raw GitHub URLs.
#
# Usage (run from Claude Code or terminal):
#   bash wiki/sync.sh [VAULT_PATH]
#
# Default vault path assumes the standard iCloud Drive / Obsidian location on macOS.
# Override by passing a path as the first argument.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_DIR="$REPO_ROOT/wiki"
PERSONAL_DIR="$REPO_ROOT/wiki-personal"
VAULT_PATH="${1:-$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents}"

# ---------------------------------------------------------------------------
# Find the vault — adjust VAULT_SUBDIR to match your Obsidian vault name
# ---------------------------------------------------------------------------
VAULT_SUBDIR="${VAULT_SUBDIR:-Obsidian Vault Icloud/Obsidian Vault AI}"
WIKI_SRC="$VAULT_PATH/$VAULT_SUBDIR/wiki"
PERSONAL_SRC="$VAULT_PATH/$VAULT_SUBDIR/wiki-personal"
VAULT="$VAULT_PATH/$VAULT_SUBDIR"

if [ ! -d "$WIKI_SRC" ]; then
  echo "ERROR: Wiki source not found at: $WIKI_SRC"
  echo "Set VAULT_SUBDIR env var (relative to iCloud Obsidian base), or pass full vault path as \$1."
  exit 1
fi

echo "Syncing AI wiki from:       $WIKI_SRC"
echo "Syncing personal wiki from: $PERSONAL_SRC"

# ---------------------------------------------------------------------------
# Regenerate wiki index from vault if generator script exists
# ---------------------------------------------------------------------------
GENERATOR="$VAULT/generate_wiki_index.py"
if [ -f "$GENERATOR" ]; then
  echo "  Running generate_wiki_index.py..."
  python3 "$GENERATOR" || echo "  WARNING: index generator failed, continuing with existing index"
fi

# ---------------------------------------------------------------------------
# Rsync full wiki subdirectories (.md files only, mirrors deletions)
# ---------------------------------------------------------------------------
for subdir in concepts entities sources syntheses stats; do
  if [ -d "$WIKI_SRC/$subdir" ]; then
    mkdir -p "$WIKI_DIR/$subdir"
    rsync -a --delete \
      --include='*/' \
      --include='*.md' \
      --exclude='*' \
      "$WIKI_SRC/$subdir/" "$WIKI_DIR/$subdir/"
    echo "  synced: $subdir/"
  fi
done

# NOTE: wiki-ha/ is PERSONAL tier (homelab/network) — NEVER synced to this public
# repo (security classification, 2026-05-30). It lives only locally + in the private
# voyager-hub. Do not re-add a wiki-ha sync block here.

# ---------------------------------------------------------------------------
# Copy helpers
# ---------------------------------------------------------------------------
copy_if_exists() {
  local src="$1"
  local dst="$2"
  mkdir -p "$(dirname "$dst")"
  if [ -f "$src" ]; then
    cp "$src" "$dst"
    echo "  copied: $(basename "$src") → $(realpath --relative-to="$REPO_ROOT" "$dst")"
  else
    echo "  skip (not found): $src"
  fi
}

# AI wiki root files
copy_if_exists "$WIKI_SRC/index.md"  "$WIKI_DIR/index.md"
copy_if_exists "$WIKI_SRC/log.md"    "$WIKI_DIR/log.md"

# NOTE: wiki-personal/ is PERSONAL tier — NEVER synced to this public repo
# (security classification, 2026-05-30). Local + private voyager-hub only.

# Pinokio / Windows 11 guides (path-normalised: "Windows 11" → "windows-11")
mkdir -p "$WIKI_DIR/pinokio/windows-11"
copy_if_exists "$WIKI_SRC/pinokio/Windows 11/claude-code-sync.md"   "$WIKI_DIR/pinokio/windows-11/claude-code-sync.md"
copy_if_exists "$WIKI_SRC/pinokio/Windows 11/windows-settings.json" "$WIKI_DIR/pinokio/windows-11/windows-settings.json"

# ---------------------------------------------------------------------------
# Stamp the sync timestamp in index.md (handles both footer variants)
# ---------------------------------------------------------------------------
TIMESTAMP="$(date -u '+%Y-%m-%d %H:%M UTC')"
sed -i.bak "s|^Last updated:.*|Last updated: $TIMESTAMP|" "$WIKI_DIR/index.md"
sed -i.bak "s|> \*\*Last synced\*\*:.*|> **Last synced**: $TIMESTAMP|" "$WIKI_DIR/index.md"
rm -f "$WIKI_DIR/index.md.bak"
if [ -f "$PERSONAL_DIR/index.md" ]; then
  sed -i.bak "s|> \*\*Last synced\*\*:.*|> **Last synced**: $TIMESTAMP|" "$PERSONAL_DIR/index.md"
  rm -f "$PERSONAL_DIR/index.md.bak"
fi

# ---------------------------------------------------------------------------
# Commit and push — warn if not on main (Claude.ai reads from main only)
# ---------------------------------------------------------------------------
cd "$REPO_ROOT"
CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"

# ---------------------------------------------------------------------------
# SECURITY GATE — scan AI-tier wiki/ before any PUBLIC push. Fail closed.
# Personal tiers (wiki-ha, wiki-personal) are not synced here at all.
# ---------------------------------------------------------------------------
SCANNER="$HOME/projects/secret_scan.py"
if [ -f "$SCANNER" ]; then
  echo "Running secret scan on wiki/ before public push..."
  if ! python3 "$SCANNER" "$WIKI_DIR"; then
    echo ""
    echo "ABORT: secret scan found issues (or a file was unreadable). Nothing pushed."
    echo "Fix the flagged file(s) above, then re-run. This is the public-repo gate."
    exit 1
  fi
  echo "  scan clean."
else
  echo "ABORT: secret scanner not found at $SCANNER — refusing to push to PUBLIC repo unscanned."
  exit 1
fi

git add wiki/
git diff --cached --quiet && echo "Nothing changed, skipping commit." && exit 0

git commit -m "wiki: sync from iCloud vault ($TIMESTAMP)"

if [ "$CURRENT_BRANCH" != "main" ]; then
  echo "WARNING: Not on main (on '$CURRENT_BRANCH')."
  echo "Pushing to current branch — run 'git checkout main && git merge $CURRENT_BRANCH && git push' to publish to Claude.ai."
  git push -u origin "$CURRENT_BRANCH"
else
  git push -u origin main
fi

echo ""
echo "Done. Claude.ai can now read the latest AI wiki at:"
echo "  https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/index.md"
echo "  https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/log.md"
echo "  (Personal tiers wiki-ha/ and wiki-personal/ are intentionally NOT public.)"
