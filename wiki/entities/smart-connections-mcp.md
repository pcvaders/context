> ~~MCP server that bridges Obsidian Smart Connections embeddings to Claude Code.~~ **DEPRECATED (2026-05-22) — replaced by [[semantic-clip]] CLI. MCP disabled in `~/.claude/settings.json`. Do not use MCP tools.**

# smart-connections-mcp

## What it is

A Python MCP server that exposes the Smart Connections vector database (already computed by Obsidian) to Claude Code and other MCP clients. No re-embedding needed — it reads `.smart-env/` files directly.

## Why it exists

Claude agents (Claude Code, Cowork dispatch) cannot read markdown files from Google Drive or local vaults directly via the Drive API. This MCP server solves that by giving agents semantic search over the entire vault.

## Three tools exposed

| Tool | What it does |
|---|---|
| `semantic_search` | Find notes by meaning — natural language query returns ranked vault pages |
| `find_related` | Given a note path, find semantically similar notes |
| `get_context_blocks` | Build targeted text blocks from multiple notes for complex queries |

## Role in this vault

- Solves the **clippings problem** — dispatch can find GitHub references and clippings semantically without manual pasting
- Enables **Cowork dispatch** to search log.md, dispatch-state.md, and wiki pages programmatically
- Connects Claude Code directly to the vault for autonomous ingest and lint operations

## Prerequisites

1. Smart Connections plugin installed in Obsidian ✅ (Phase 2 step 1)
2. Smart Connections has completed its first index pass (`.smart-env/` folder exists in vault)
3. Python installed on machine
4. Claude Code running in VS Code ✅

## Install

```bash
# Clone to home directory (keep separate from vault)
git clone https://github.com/dan6684/smart-connections-mcp.git ~/smart-connections-mcp
cd ~/smart-connections-mcp
./install.sh
```

## MCP config (add to Claude Code .mcp.json)

```json
{
  "mcpServers": {
    "smart-connections": {
      "command": "/Users/voyager1/smart-connections-mcp/.venv/bin/python",
      "args": ["/Users/voyager1/smart-connections-mcp/server.py"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "/Users/voyager1/Library/CloudStorage/GoogleDrive-pcgamesplay1@gmail.com/My Drive/Obsidian/Obsidian Vault AI"
      }
    }
  }
}
```

**Critical**: Use `.venv/bin/python` not system Python.

## Verify install

```bash
claude mcp list
# Expected: smart-connections: .venv/bin/python server.py - ✓ Connected
```

## Status (May 2026) — DEPRECATED

**Disabled 2026-05-22.** Root cause: MCP server loads at every session start, consuming tokens before user types a single character. No native Claude Code UI to disable per-MCP. Workaround was SwiftBar toggle — but full replacement preferred.

**Replacement: [[semantic-clip]]** — Node.js CLI that reads same `.smart-env/` pre-computed vectors directly. Zero MCP overhead, zero network, same 384-dim `TaylorAI/bge-micro-v2` embeddings. Drop-in semantic search via `semantic-clip "query" | pbcopy`.

`disabledMcpjsonServers: ["smart-connections"]` set in `~/.claude/settings.json`.

3 stars, 1 fork, MIT license. Small but functional. The approach (reading pre-computed embeddings) is sound even if the packaging is minimal. See also `msdanyg` fork for TypeScript alternative with knowledge graph support.

## Related

- [[smart-connections]] — the Obsidian plugin whose embeddings this server reads
- [[claude-code]] — the MCP client
- [[mcp]] — the protocol
- [[obsidian]] — the vault
- [[dan6684-smart-connections-mcp]] — source page

(as of 2026-05)
