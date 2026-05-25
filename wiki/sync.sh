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
VAULT_SUBDIR="${VAULT_SUBDIR:-Obsidian Vault Icloud/Obsidian Vault AI}"
WIKI_SRC="$VAULT_PATH/$VAULT_SUBDIR/wiki"
VAULT="$VAULT_PATH/$VAULT_SUBDIR"

if [ ! -d "$WIKI_SRC" ]; then
  echo "ERROR: Wiki source not found at: $WIKI_SRC"
  echo "Set VAULT_SUBDIR env var (relative to iCloud Obsidian base), or pass full vault path as \$1."
  exit 1
fi

echo "Syncing from: $WIKI_SRC"

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
for subdir in concepts entities sources syntheses wiki-ha; do
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

# ---------------------------------------------------------------------------
# Copy root wiki files and path-normalised subdirectories
# ---------------------------------------------------------------------------
copy_if_exists() {
  local src="$WIKI_SRC/$1"
  local dst="$WIKI_DIR/$2"
  mkdir -p "$(dirname "$dst")"
  if [ -f "$src" ]; then
    cp "$src" "$dst"
    echo "  copied: $1 → wiki/$2"
  else
    echo "  skip (not found): $1"
  fi
}

copy_if_exists "index.md"   "index.md"
copy_if_exists "log.md"     "log.md"

# Pinokio / Windows 11 guides (path-normalised: "Windows 11" → "windows-11")
mkdir -p "$WIKI_DIR/pinokio/windows-11"
copy_if_exists "pinokio/Windows 11/claude-code-sync.md"  "pinokio/windows-11/claude-code-sync.md"
copy_if_exists "pinokio/Windows 11/windows-settings.json" "pinokio/windows-11/windows-settings.json"

# ---------------------------------------------------------------------------
# Stamp the sync timestamp in index.md (handles both footer variants)
# ---------------------------------------------------------------------------
TIMESTAMP="$(date -u '+%Y-%m-%d %H:%M UTC')"
sed -i.bak "s|^Last updated:.*|Last updated: $TIMESTAMP|" "$WIKI_DIR/index.md"
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
