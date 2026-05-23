> How to mirror a Mac Claude Code setup onto Windows 11 — CLAUDE.md, skills, commands, hooks, MCP, and the AI LLM Wiki loader.

# Claude Code: Mac → Windows 11 Sync

## What lives where

| Item | Mac path | Windows path |
|------|----------|--------------|
| Global config | `~/.claude/settings.json` | `C:\Users\PCG1\.claude\settings.json` |
| Global instructions | `~/.claude/CLAUDE.md` | `C:\Users\PCG1\.claude\CLAUDE.md` |
| Skills folder | `~/.claude/skills/` | `C:\Users\PCG1\.claude\skills\` |
| Commands folder | `~/.claude/commands/` | `C:\Users\PCG1\.claude\commands\` |
| Hooks folder | `~/.claude/hooks/` | `C:\Users\PCG1\.claude\hooks\` |
| Project memory | `~/.claude/projects/<slug>/memory/` | `C:\Users\PCG1\.claude\projects\<slug>\memory\` |
| Credentials | `~/.claude/.credentials.json` | `C:\Users\PCG1\.claude\.credentials.json` |

---

## Current Mac state (2026-05-23)

### Skills (`~/.claude/skills/`)

| Skill | Notes |
|-------|-------|
| `caveman` | ~65% output token compression |
| `cavecrew` | compressed subagent delegation |
| `caveman-commit` | commit message helper |
| `caveman-compress` | manual compression |
| `caveman-help` | caveman docs |
| `caveman-review` | code review |
| `caveman-stats` | token savings stats |
| `obsidian-wiki-memory` | Obsidian vault router |
| `gepeto` | Pinokio launcher dev guide ✓ Windows has |
| `pinokio` | Pinokio runtime control ✓ Windows has |
| `paperpress-cli` | Paperpress vault publishing |
| `screenwriter` | screenwriting helper |
| `higgsfield-*` | Higgsfield AI image tools |

### Commands (`~/.claude/commands/`)

| File | Slash command | Notes |
|------|---------------|-------|
| `aillmwiki.md` | `/aillmwiki` | AI LLM Wiki assistant mode |
| `interlinked.md` | `/interlinked` | semantic wiki search via `semantic-clip` |
| `vault.md` | `/vault` | vault management shortcuts |

> **Note:** `aillmwiki` is a command (not a skill). It lives in `commands/`, not `skills/`.

### Hooks (`~/.claude/hooks/`)

| File | Event | Notes |
|------|-------|-------|
| `caveman-activate.js` | SessionStart | writes caveman flag, emits ruleset |
| `caveman-config.js` | — | shared config (required by all JS hooks) |
| `caveman-mode-tracker.js` | UserPromptSubmit | tracks mode changes |
| `caveman-stats.js` | — | stats helper |
| `caveman-statusline.sh` | statusLine | Mac (bash) |
| `caveman-statusline.ps1` | statusLine | **Windows (PowerShell) — already written** |
| `skill-enforcer.py` | PreToolUse | blocks Bash/Edit/Write if no skill invoked |
| `skill-tracker.py` | PostToolUse | writes skill-invoked flag |
| `wiki-index-regenerate.py` | PostToolUse | regenerates wiki index — Mac paths, skip on Windows |
| `package.json` | — | `{"type":"commonjs"}` — required for JS hooks |

### Active hooks (Mac `settings.json`)

- **SessionStart**: `caveman-activate.js` + `optimize-vault.js` (async vault dedup, iCloud path)
- **UserPromptSubmit**: `caveman-mode-tracker.js`
- **PreToolUse** `Bash|Edit|Write`: `skill-enforcer.py`
- **PostToolUse**: `wiki-index-regenerate.py` + `skill-tracker.py`

### CLAUDE.md

Currently empty on Mac. Nothing to copy — create a Windows-specific one.

---

## Step-by-step sync

### 1. Prerequisites — install on Windows

```powershell
winget install OpenJS.NodeJS
winget install Python.Python.3
```

Verify:
```powershell
node --version
python --version
```

### 2. Copy skills

On Mac, zip and transfer via iCloud or USB:

```bash
cd ~/.claude && zip -r claude-skills.zip skills/
```

Extract to `C:\Users\PCG1\.claude\skills\` on Windows.

Priority skills (minimum viable set):
- `skills/caveman/`
- `skills/cavecrew/`
- `skills/obsidian-wiki-memory/`

### 3. Copy commands

```bash
cd ~/.claude && zip -r claude-commands.zip commands/
```

Extract to `C:\Users\PCG1\.claude\commands\`.

Commands are plain markdown — no path rewriting needed.

### 4. Copy hooks

```bash
cd ~/.claude && zip -r claude-hooks.zip hooks/
```

Extract to `C:\Users\PCG1\.claude\hooks\`.

**Required files:**

| File | Cross-platform? |
|------|----------------|
| `caveman-activate.js` | ✓ yes |
| `caveman-config.js` | ✓ yes |
| `caveman-mode-tracker.js` | ✓ yes |
| `caveman-stats.js` | ✓ yes |
| `caveman-statusline.ps1` | ✓ Windows-native |
| `skill-enforcer.py` | ✓ yes (uses `tempfile.gettempdir()`) |
| `skill-tracker.py` | ✓ yes (uses `tempfile.gettempdir()`) |
| `package.json` | ✓ yes |
| `wiki-index-regenerate.py` | ✗ skip — Mac paths hardcoded |
| `caveman-statusline.sh` | ✗ skip — bash only |

### 5. Deploy settings.json

Use the ready-made template: `[[windows-settings]]` (same folder as this file).

Place at `C:\Users\PCG1\.claude\settings.json`.

**Do NOT copy Mac's `settings.json` directly** — Node path (`/opt/homebrew/...`) and statusLine command are Mac-only.

Key differences:

| | Mac | Windows |
|--|-----|---------|
| Node path | `/opt/homebrew/Cellar/node/.../bin/node` | `node` |
| Python | `python3` | `python` |
| StatusLine | `bash "...caveman-statusline.sh"` | `powershell -NoProfile -File "...caveman-statusline.ps1"` |
| `optimize-vault.js` | included | optional — add if iCloud installed |
| `wiki-index-regenerate.py` | PostToolUse | **omit** |

**Optional — add vault dedup to SessionStart if iCloud for Windows is installed:**

```json
{
  "type": "command",
  "command": "node \"C:\\Users\\PCG1\\iCloudDrive\\iCloud~md~obsidian\\Obsidian Vault Icloud\\Obsidian Vault AI\\optimize-vault.js\" 2>NUL",
  "timeout": 15,
  "statusMessage": "Optimizing vault...",
  "async": true
}
```

### 6. Create CLAUDE.md

Mac's `CLAUDE.md` is empty. Create `C:\Users\PCG1\.claude\CLAUDE.md`:

```markdown
## AI LLM Wiki

Vault: C:\Users\PCG1\iCloudDrive\iCloud~md~obsidian\Obsidian Vault Icloud\Obsidian Vault AI

Sections:
- wiki/concepts/ — AI/LLM concepts
- wiki/entities/ — tools, models, people
- wiki/syntheses/ — cross-cutting analysis
- wiki/agents/claude-primary/inbox/ — active context

Use /aillmwiki for full wiki assistant mode.
```

### 7. Plugins

Plugins auto-install when Claude Code restarts with the new `settings.json` (which includes `extraKnownMarketplaces`). Or install manually:

```
claude plugins install caveman@caveman
claude plugins install karpathy-skills@karpathy-skills
claude plugins install antigravity-awesome-skills@antigravity-awesome-skills
```

---

## Quick checklist

- [ ] `node` in PATH
- [ ] `python` in PATH
- [ ] `skills/caveman/` copied
- [ ] `skills/cavecrew/` copied
- [ ] `skills/obsidian-wiki-memory/` copied
- [ ] `skills/gepeto/` ✓ present
- [ ] `skills/pinokio/` ✓ present
- [ ] `commands/aillmwiki.md` copied
- [ ] `commands/interlinked.md` copied
- [ ] `commands/vault.md` copied
- [ ] `hooks/caveman-activate.js` copied
- [ ] `hooks/caveman-config.js` copied
- [ ] `hooks/caveman-mode-tracker.js` copied
- [ ] `hooks/skill-enforcer.py` copied
- [ ] `hooks/skill-tracker.py` copied
- [ ] `hooks/package.json` copied
- [ ] `hooks/caveman-statusline.ps1` ✓ present
- [ ] `settings.json` deployed from `[[windows-settings]]` template
- [ ] `CLAUDE.md` created
- [ ] Claude Code restarted → plugins auto-installed

---

## Windows-specific differences

| Behavior | Mac | Windows |
|----------|-----|---------|
| Shell in hooks | `bash -c "..."` | `powershell -NoProfile -Command "..."` |
| Path separator | `/` | `\` (escape as `\\` in JSON) |
| Home dir | `~` | `C:\Users\PCG1` |
| Hook env vars | `$HOME` | `$env:USERPROFILE` |
| Node location | Homebrew absolute path | `node` from PATH |
| Python command | `python3` | `python` |
| iCloud Drive | `~/Library/Mobile Documents/...` | `C:\Users\PCG1\iCloudDrive\...` |
| Temp dir (flag files) | `/var/folders/.../T/` | `C:\Users\PCG1\AppData\Local\Temp` |

---

## Related

- [[claude-code]]
- [[windows-11]]
- [[pinokio]]
- [[aillmwiki]]
- [[windows-settings]]
