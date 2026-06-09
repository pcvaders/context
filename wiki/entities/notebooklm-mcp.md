> NotebookLM MCP setup for Claude Code and Cowork (Claude Desktop) — auth via saved Google session.

# NotebookLM MCP

**Package:** `notebooklm-mcp-cli` (PyPI + CLI wrapper)
**CLI:** `nlm` at `/Users/voyager1/.local/bin/nlm`
**MCP binary:** `notebooklm-mcp` at `/Users/voyager1/.local/bin/notebooklm-mcp`
**Auth:** Google account `pcgamesplay1@gmail.com`, 43 cookies, headless Chrome profile

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
