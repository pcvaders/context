> Last updated: 2026-05-31. Full current Mac state.

# Claude Code: Mac → Windows 11 Sync

## Auto-sync on session start

**Yes — fully automatic.** Once set up, every new Claude Code session on Win11:
1. `session-start.ps1` fires → `git pull voyager-hub` → latest CONTEXT.md + memory loaded
2. Memory nodes available immediately
3. Wiki readable via GitHub raw URLs (always current)

No manual steps after initial setup.

## What lives where

| Item | Mac | Windows |
|---|---|---|
| Global config | `~/.claude/settings.json` | `C:\Users\PCG1\.claude\settings.json` |
| Skills | `~/.claude/skills/` | `C:\Users\PCG1\.claude\skills\` |
| Hooks | `~/.claude/hooks/` | `C:\Users\PCG1\.claude\hooks\` |
| Commands | `~/.claude/commands/` | `C:\Users\PCG1\.claude\commands\` |
| voyager-hub | `~/voyager-hub/` | `C:\Users\PCG1\voyager-hub\` |
| Projects | `~/projects/` | `C:\Users\PCG1\projects\` |

## Current Mac skills (2026-05-31)

Copy all except `tests/`:
caveman · cavecrew · caveman-commit · caveman-compress · caveman-help · caveman-review · caveman-stats · gepeto · higgsfield-generate · higgsfield-marketplace-cards · higgsfield-product-photoshoot · higgsfield-soul-id · memory.md · memory-reconcile-subagent.md · obsidian-wiki-memory · pinokio · screenwriter · topview

## Current hooks

| File | Win11? |
|---|---|
| `caveman-activate.js` | ✅ |
| `caveman-config.js` | ✅ |
| `caveman-mode-tracker.js` | ✅ |
| `caveman-stats.js` | ✅ |
| `caveman-statusline.ps1` | ✅ |
| `skill-enforcer.py` | ✅ |
| `skill-tracker.py` | ✅ |
| `skill-recommender.py` | ✅ |
| `roi-post-session.py` | ✅ |
| `package.json` | ✅ |
| `session-start.sh` | ❌ skip (Mac bash) |
| `caveman-statusline.sh` | ❌ skip (Mac bash) |
| `wiki-index-regenerate.py` | ❌ skip (Mac paths) |

**Create `session-start.ps1`** — see windows-settings.json folder.

## Setup steps

### 1. Prerequisites
```powershell
winget install OpenJS.NodeJS
winget install Python.Python.3
winget install Git.Git
node --version && python --version && git --version
```

### 2. Clone voyager-hub (ONE TIME)
```powershell
git clone https://github.com/PCGamesplay1/voyager-hub.git C:\Users\PCG1\voyager-hub
```

### 3. Clone wiki + projects (ONE TIME)
```powershell
mkdir C:\Users\PCG1\projects
git clone https://github.com/PCGamesplay1/Claude-skills.git C:\Users\PCG1\projects\claude-skills
```

### 4. Copy skills + hooks from Mac
```bash
cd ~/.claude
zip -r /tmp/claude-skills.zip skills/
zip -r /tmp/claude-hooks.zip hooks/
zip -r /tmp/claude-commands.zip commands/
```
Transfer ZIPs → extract to Win11 paths.

### 5. Create `session-start.ps1`
```powershell
# C:\Users\PCG1\.claude\hooks\session-start.ps1
$ErrorActionPreference = "SilentlyContinue"
Write-Output "[SessionStart] Memory reconcile starting..."
$hub = "C:\Users\PCG1\voyager-hub"
if (Test-Path $hub) {
    Set-Location $hub
    git pull origin main 2>&1 | Out-Null
    Write-Output "[SessionStart] voyager-hub pulled"
} else {
    Write-Output "[SessionStart] WARNING: voyager-hub not found — clone it first"
}
$mem = "C:\Users\PCG1\.claude\projects\-Users-PCG1\memory"
if (Test-Path $mem) {
    $n = (Get-ChildItem $mem -Filter "*.md").Count
    Write-Output "[SessionStart] Auto-memory: $n nodes available"
}
Write-Output "[SessionStart] Done"
```

### 6. Deploy settings.json
Use `windows-settings.json` (same folder). Place at `C:\Users\PCG1\.claude\settings.json`.

### 7. Create CLAUDE.md
```markdown
# Claude Code — Win11

## Memory bootstrap
voyager-hub auto-pulled each session.
CONTEXT.md: C:\Users\PCG1\voyager-hub\memory\CONTEXT.md

## AI LLM Wiki
https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/index.md
Local: C:\Users\PCG1\projects\claude-skills\wiki\

## Active projects
- Isle of Dogs: C:\Users\PCG1\projects\claude-skills\isle-of-dogs\CLAUDE.md
- ComfyUI: PRIMARY target — RTX 5070ti
  Install: comfy-cli + LTX 2.3 + Cameraman IC-LoRA
  Pipeline: wiki/concepts/higgsfield-comfyui-pipeline-architecture.md

## Paths
Home: C:\Users\PCG1 | Python: python | Node: node | Shell: PowerShell
```

### 8. Restart Claude Code
Session should show:
```
[SessionStart] voyager-hub pulled
[SessionStart] Auto-memory: N nodes available
CAVEMAN MODE ACTIVE
```

## Win11 differences

| | Mac | Windows |
|---|---|---|
| Python | `python3` | `python` |
| Node | `/opt/homebrew/.../node` | `node` |
| Home | `~` | `C:\Users\PCG1` |
| Shell | bash | PowerShell |
| iCloud | `~/Library/Mobile Documents/...` | `C:\Users\PCG1\iCloudDrive\...` |

## Related
[[claude-code]] · [[windows-11]] · [[pinokio]] · [[isle-of-dogs-project]] · [[comfyui]]
