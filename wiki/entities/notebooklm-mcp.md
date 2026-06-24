> NotebookLM MCP setup for Claude Code and Cowork (Claude Desktop) — auth via saved Google session.

# NotebookLM MCP

**Package:** `notebooklm-mcp-cli` 0.6.10 (PyPI, uv tool)
**CLI:** `nlm` at `/Users/voyager1/.local/bin/nlm`
**MCP binary:** `notebooklm-mcp` at `/Users/voyager1/.local/bin/notebooklm-mcp`
**Token store:** `~/.notebooklm-mcp-cli/profiles/<profile>/`

## Two accounts (as of 2026-06)

- **pcvaders@gmail.com** = `default` profile. Cowork + Claude Code MCP use this. Primary account (28 notebooks).
- **pcgamesplay1@gmail.com** = `pcgamesplay1` profile. Owns the memory notebooks.

Memory notebooks owned by pcgamesplay1, **shared to pcvaders as editor**:
- `38bfb58a-...` "AI Code Style Guide & Skills 2026" — shared ✓
- `64447237-...` personal wiki — pending share

```bash
nlm login switch pcvaders        # set active account (CLI + MCP)
nlm login profile list
nlm login -p pcgamesplay1 --force # re-auth a profile (Chrome)
```

**GOTCHA:** `nlm login --clear` often captures only 20-22 cookies (partial → "Authentication expired" on first call). Full session ≈ 43. If auth expires right after login, re-run `nlm login -p <profile> --force` WITHOUT `--clear`.

## Setup Status (as of 2026-06)

| Client | Config | Status |
|---|---|---|
| Claude Code | user scope via `claude mcp` | ✓ Connected |
| Cowork / Claude Desktop | `~/Library/Application Support/Claude/claude_desktop_config.json` → `mcpServers` | Requires app restart |

## How to wire a new client

```bash
# Supported clients (nlm knows about these)
nlm setup add claude-code
nlm setup add gemini
nlm setup add cursor

# Claude Desktop / Cowork — nlm doesn't support "claude-desktop"
# Add manually to ~/Library/Application Support/Claude/claude_desktop_config.json:
# "mcpServers": { "notebooklm-mcp": { "command": "notebooklm-mcp", "args": [] } }
```

## Re-auth if cookies expire

```bash
nlm doctor          # check status
nlm setup add claude-code --force  # re-run auth flow
```

## Key notebooks

- **AI Code Style Guide & Skills 2026** — ID `38bfb58a-0da8-4702-bae9-2979866f413c` — Claude's persistent memory, fed from Obsidian wiki
- **Claude AI Memory** — ID `ebbf4879-e677-4756-9b70-be71ff1bd558` — legacy, mostly empty

## Why MCP doesn't auto-sync across instances

Each Claude surface (claude.ai, Claude Code, Cowork) has its own MCP config. claude.ai uses Anthropic-hosted connectors (no local MCP). Claude Code and Cowork need local setup.

See also: [[obsidian-wiki-memory]], [[smart-clip]]
