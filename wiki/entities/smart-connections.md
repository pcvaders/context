# Smart Connections

> Obsidian plugin providing AI-powered semantic search and note linking via local embeddings; exposed to Claude Code via the smart-connections-mcp server.

**Plugin**: https://github.com/brianpetro/jsbrains  
**MCP wrapper**: [[smart-connections-mcp]]  
**Type**: Obsidian plugin + MCP server

## What it does

Smart Connections indexes all vault notes as vector embeddings and provides:
- Semantic similarity search across notes
- Related note suggestions in a side panel
- Context block retrieval (RAG-quality chunks)
- Exposed via MCP: `semantic_search`, `find_related`, `get_context_blocks`

## Role in this vault

Primary discovery layer for the AI LLM Wiki. When asked a QUERY, Claude Code searches the vault semantically rather than grepping filenames. Enables wiki pages to surface by meaning, not just keyword match.

## Embedding model

Uses `TaylorAI/bge-micro-v2` (local HuggingFace model). Downloads anonymously — no auth token required. (as of 2026-05)

## Related

- [[smart-connections-mcp]] — MCP server wrapper
- [[mcp]] — protocol used to expose Smart Connections to Claude Code
- [[obsidian]] — host application
- [[llm-wiki]] — pattern that depends on semantic search for QUERY operation
