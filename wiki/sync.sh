#!/usr/bin/env bash
# Syncs key wiki files from the iCloud/Obsidian vault into this repo's wiki/ directory,
# then commits and pushes so Claude.ai can read the latest content via raw GitHub URLs.
#
# Usage (run from Claude Code or terminal):
#   bash wiki/sync.sh [VAULT_PATH]
#
# Default vault path assumes the standard iCloud Drive / Obsidian location on macOS.
# Override by passing a path as the first argument.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_DIR="$REPO_ROOT/wiki"
VAULT_PATH="${1:-$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents}"

# ---------------------------------------------------------------------------
# Find the vault — adjust VAULT_SUBDIR to match your Obsidian vault name
# ---------------------------------------------------------------------------
VAULT_SUBDIR="${VAULT_SUBDIR:-AI-LLM-Wiki}"   # change to your vault folder name
VAULT="$VAULT_PATH/$VAULT_SUBDIR"

if [ ! -d "$VAULT" ]; then
  echo "ERROR: Vault not found at: $VAULT"
  echo "Set VAULT_SUBDIR env var to your Obsidian vault folder name, or pass the full path as \$1."
  exit 1
fi

echo "Syncing from: $VAULT"

# ---------------------------------------------------------------------------
# Copy files — add more entries here as the wiki grows
# ---------------------------------------------------------------------------
copy_if_exists() {
  local src="$VAULT/$1"
  local dst="$WIKI_DIR/$2"
  if [ -f "$src" ]; then
    cp "$src" "$dst"
    echo "  copied: $1 → wiki/$2"
  else
    echo "  skip (not found): $1"
  fi
}

copy_if_exists "index.md"   "index.md"
copy_if_exists "log.md"     "log.md"

# ---------------------------------------------------------------------------
# Stamp the sync timestamp in index.md
# ---------------------------------------------------------------------------
TIMESTAMP="$(date -u '+%Y-%m-%d %H:%M UTC')"
sed -i.bak "s|> \*\*Last synced\*\*:.*|> **Last synced**: $TIMESTAMP|" "$WIKI_DIR/index.md"
rm -f "$WIKI_DIR/index.md.bak"

# ---------------------------------------------------------------------------
# Commit and push
# ---------------------------------------------------------------------------
cd "$REPO_ROOT"
git add wiki/
git diff --cached --quiet && echo "Nothing changed, skipping commit." && exit 0

git commit -m "wiki: sync from iCloud vault ($TIMESTAMP)"
git push -u origin "$(git rev-parse --abbrev-ref HEAD)"

echo ""
echo "Done. Claude.ai can now read the latest wiki at:"
echo "  https://raw.githubusercontent.com/pcgamesplay1/claude-skills/main/wiki/index.md"
echo "  https://raw.githubusercontent.com/pcgamesplay1/claude-skills/main/wiki/log.md"
