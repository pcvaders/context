# Vault Setup Session

> Founding session establishing the AI LLM Wiki vault structure, MCP connections, and wiki folder layout in Obsidian iCloud vault.

**Date**: 2026-05-20  
**Duration**: 98 messages  
**Outcome**: ✅ Vault operational with Smart Connections MCP

## Key decisions made

**Obsidian over Pinecone**: User had Obsidian already — vault stores session memories as `.md` files, readable/linkable/graphable. No external account needed. Trade-off: no vector search at scale, but Smart Connections fills that gap locally.

**Nested vault structure discovered**:
```
Obsidian Vault Icloud/        ← iCloud root
├── Obsidian Vault AI/        ← AI wiki vault
└── Obsidian Vault Personal/  ← personal vault
```
MCP path must point to `Obsidian Vault AI` not parent.

**Wiki folder layout**:
```
wiki/
├── concepts/   ← fundamental ideas
├── entities/   ← tools, people, orgs
├── sources/    ← ingested source summaries
├── syntheses/  ← cross-cutting analysis
├── index.md
└── log.md
```

## MCP setup outcome

`smart-connections-mcp` connected to `Obsidian Vault AI` vault. Path corrected from parent directory to correct subfolder. Smart Connections semantic search operational.

## Related

- [[smart-connections-mcp]] — MCP server set up in this session
- [[obsidian]] — vault host
- [[llm-wiki]] — pattern being implemented
- [[mcp]] — protocol used
