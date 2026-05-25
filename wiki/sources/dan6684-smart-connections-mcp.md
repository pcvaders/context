> MCP server that exposes Obsidian Smart Connections vector database to Claude Code via semantic search.

# Source — dan6684/smart-connections-mcp

**Author**: dan6684
**URL**: https://github.com/dan6684/smart-connections-mcp
**Type**: GitHub repository / MCP server
**Language**: Python
**License**: MIT
**Stars**: 3 | **Forks**: 1
**Ingested**: 2026-05-20

---

## One-line thesis

Exposes the Smart Connections vector database already computed by Obsidian to Claude Code via MCP — no re-embedding needed. Solves the problem of Claude agents not being able to read vault markdown files directly.

## What it does

Three core tools exposed via MCP:
- `semantic_search` — find notes by meaning across the vault
- `find_related` — discover semantically similar notes to a given note
- `get_context_blocks` — build targeted text blocks for complex queries

## Why it matters for this vault

Solves the clippings problem: Claude Code (and Cowork dispatch) can search the vault semantically without the user having to paste content manually. Dispatch workflows can find relevant pages, check for contradictions, and resume from log.md — all via semantic search.

## Install method

```bash
git clone https://github.com/dan6684/smart-connections-mcp.git ~/smart-connections-mcp
cd ~/smart-connections-mcp
./install.sh
```

## MCP config

```json
{
  "mcpServers": {
    "smart-connections": {
      "command": "/Users/YOUR_USERNAME/smart-connections-mcp/.venv/bin/python",
      "args": ["/Users/YOUR_USERNAME/smart-connections-mcp/server.py"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "/path/to/your/obsidian/vault"
      }
    }
  }
}
```

**Important**: Use the virtual environment Python, not system Python.

## Prerequisites

- Smart Connections plugin installed and indexed in Obsidian (must run first)
- Python installed on the machine
- Claude Code running in VS Code

## Key notes

- Keep this repo separate from the Obsidian vault (per DEPLOYMENT.md)
- If timeout issues occur, see TROUBLESHOOTING.md in the repo
- Reads `.smart-env/` files Smart Connections already computed — no re-indexing

## Alternative forks

- `msdanyg/smart-connections-mcp` — TypeScript, adds knowledge graph traversal
- `gogogadgetbytes/smart-connections-mcp` — Node.js, read-only, security-focused

## Related

- [[smart-connections]] — the Obsidian plugin this server exposes
- [[claude-code]] — the MCP client
- [[mcp]] — the protocol
- [[obsidian]] — the vault

(as of 2026-05)
