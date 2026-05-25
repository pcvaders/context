#!/usr/bin/env bash
# agent-commit.sh — secure wrapper for external agent git commits
#
# Usage: agent-commit.sh <agent_name> <task_type> <roi_score> <file1> [file2 ...]
#
# Enforces:
#   - Agent identity (External Agent / agents@voyager1.local)
#   - Deploy key authentication (id_ed25519_agents)
#   - File whitelist: only proposals/ inside agent-proposals repo
#   - Blocks sensitive path writes
#   - Structured audit log entry per commit

set -euo pipefail

REPO="$HOME/agent-proposals"
LOG="$REPO/logs/agent-activity.log"
DEPLOY_KEY="$HOME/.ssh/id_ed25519_agents"
AGENT_NAME="${1:-unknown}"
TASK_TYPE="${2:-general}"
ROI_SCORE="${3:-0}"
shift 3 2>/dev/null || { echo "Usage: agent-commit.sh <agent> <task> <roi> <file...>" >&2; exit 1; }

FILES=("$@")
NOW=$(date -u '+%Y-%m-%d %H:%M UTC')
STATUS="ok"

# ── Blocked paths ─────────────────────────────────────────────────────────────
BLOCKED_PATTERNS=(
    "$HOME/.claude"
    "$HOME/Library/LaunchAgents"
    "$HOME/Library/Application Support/Claude"
    "$HOME/claude-skills"
    "/Library/Mobile Documents"
)

for file in "${FILES[@]}"; do
    abs=$(realpath "$file" 2>/dev/null || echo "$file")
    for blocked in "${BLOCKED_PATTERNS[@]}"; do
        if [[ "$abs" == "$blocked"* ]]; then
            echo "[BLOCKED] $agent_name attempted write to protected path: $abs" >&2
            STATUS="blocked"
            printf '[%s] agent=%s task=%s roi=%s files=0 status=blocked path=%s\n' \
                "$NOW" "$AGENT_NAME" "$TASK_TYPE" "$ROI_SCORE" "$abs" >> "$LOG"
            exit 2
        fi
    done
    # Must be inside proposals/
    if [[ "$abs" != "$REPO/proposals/"* ]]; then
        echo "[BLOCKED] File outside proposals/: $abs" >&2
        STATUS="blocked"
        printf '[%s] agent=%s task=%s roi=%s files=0 status=blocked path=%s\n' \
            "$NOW" "$AGENT_NAME" "$TASK_TYPE" "$ROI_SCORE" "$abs" >> "$LOG"
        exit 2
    fi
done

# ── Commit ────────────────────────────────────────────────────────────────────
cd "$REPO"

export GIT_SSH_COMMAND="ssh -i $DEPLOY_KEY -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
export GIT_CONFIG_GLOBAL="$HOME/.gitconfig-agents"
export GIT_AUTHOR_NAME="External Agent"
export GIT_AUTHOR_EMAIL="agents@voyager1.local"
export GIT_COMMITTER_NAME="External Agent"
export GIT_COMMITTER_EMAIL="agents@voyager1.local"

for file in "${FILES[@]}"; do
    git add "$file"
done

COMMIT_MSG="[${AGENT_NAME}] ${TASK_TYPE} | roi=${ROI_SCORE} | $(date -u '+%Y-%m-%d %H:%M UTC')"
git commit -m "$COMMIT_MSG"

FILE_COUNT="${#FILES[@]}"
printf '[%s] agent=%s task=%s roi=%s files=%d status=%s\n' \
    "$NOW" "$AGENT_NAME" "$TASK_TYPE" "$ROI_SCORE" "$FILE_COUNT" "$STATUS" >> "$LOG"

echo "Committed: $COMMIT_MSG"

# Push via human only — deploy key is read-only
# To push: git -C ~/agent-proposals push
