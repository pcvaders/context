# Model Context Protocol (MCP)

> Open standard by Anthropic enabling LLM agents to connect to external tools, data sources, and services via a unified server/client protocol.

**Full name**: Model Context Protocol  
**Author**: Anthropic  
**Spec**: https://modelcontextprotocol.io  
**Released**: 2024-11 (as of 2026-05)

## What it is

MCP is a JSON-RPC protocol that standardises how AI agents discover and call external capabilities. Instead of each tool having a bespoke integration, any MCP-compliant server exposes tools, resources, and prompts that any MCP-compliant client (Claude Code, Claude Desktop, Cursor, etc.) can consume.

```
Client (Claude Code)
  ↔ MCP protocol (stdio / SSE)
    ↔ MCP Server (smart-connections, homeassistant, notebooklm, etc.)
      ↔ Underlying service / data
```

## Key Concepts

| Term | Meaning |
|---|---|
| **Tool** | Function the LLM can call (e.g. `semantic_search`) |
| **Resource** | Data the LLM can read (e.g. vault notes) |
| **Prompt** | Reusable prompt template exposed by server |
| **Server** | Process exposing tools/resources via MCP protocol |
| **Client** | LLM host that connects to servers (Claude Code, Claude Desktop) |

## Transport types

- **stdio** — server runs as subprocess, communication via stdin/stdout (most common for local)
- **SSE** — HTTP server-sent events (for remote/network servers)

## Active MCP Servers (voyager1, as of 2026-05)

| Server | Purpose | Config |
|---|---|---|
| `smart-connections` | Semantic search over Obsidian vault | `~/.mcp.json` (disabled — enable via SwiftBar) |
| `homeassistant` | Home automation control | `claude_desktop_config.json` |
| `mempalace` | Persistent memory / knowledge graph | `claude_desktop_config.json` |
| `notebooklm-mcp` | NotebookLM notebook access | `claude_desktop_config.json` |

## Claude Desktop Config Race Condition

Claude Desktop rewrites `claude_desktop_config.json` from memory when it quits — any manual edits during a session are overwritten. Workaround: use `claude_desktop_config.disabled.json` for parked servers; SwiftBar `mcp-toggle` plugin moves entries between files and quits Claude before editing.

## Related

- [[smart-connections-mcp]] — MCP server for Obsidian semantic search
- [[claude-code]] — primary MCP client in this environment
- [[skill-ecosystem]] — MCP servers complement skill plugins
