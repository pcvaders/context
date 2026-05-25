# MCP Connector Management Session

> 36-message session establishing MCP enable/disable patterns — per-conversation toggles on claude.ai, SwiftBar plugin for Claude Desktop config management, disabled.json pattern.

**Date**: 2026-05-20  
**Duration**: 36 messages  
**Outcome**: ✅ SwiftBar MCP toggle plugin operational

## Problems solved

**Problem 1**: MCP servers consuming too many tokens — needed per-session control  
**Solution**: claude.ai has per-conversation connector toggles via "+" → Connectors. Enable/disable per conversation without removing.

**Problem 2**: Claude Desktop config race condition — manual edits to `claude_desktop_config.json` overwritten when Claude quits (app rewrites from memory)  
**Solution**: `claude_desktop_config.disabled.json` pattern — park disabled MCPs in separate file Claude never touches. SwiftBar plugin moves entries between files, quits Claude before editing, restarts after.

**Problem 3**: Smart Connections MCP path wrong — pointed to parent vault directory  
**Solution**: Corrected `OBSIDIAN_VAULT_PATH` to `Obsidian Vault Icloud/Obsidian Vault AI`

## SwiftBar plugin pattern

`mcp-toggle.30s.py` in `~/Library/Application Support/SwiftBar/Plugins/`:
- Reads both `claude_desktop_config.json` + `disabled.json`
- Shows `MCP N/M` in menu bar
- Toggle action: quit Claude → move entry between files → restart Claude
- Prevents config overwrite race condition

## Key insight: config race condition

Claude Desktop holds MCP config in memory. On quit, writes memory state to disk. Any file edits made while Claude is running are overwritten. Must quit Claude before editing either config file.

## Related

- [[mcp]] — protocol being managed
- [[claude-code]] — Claude Code vs Claude Desktop config differences
