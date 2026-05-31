---
title: "semantic-clip.js source"
date: 2026-05-31
summary: "Node.js CLI for local semantic search over Smart Connections embeddings — zero MCP, zero network, cosine similarity over .smart-env/multi/*.ajson."
tags: [semantic-search, cli, embeddings, smart-connections, obsidian, vault]
---

> Source file: `semantic-clip.js` — Node.js local semantic search CLI over pre-computed vault embeddings.

## Source

**File:** `$VAULT/semantic-clip.js`
**Symlink:** `~/.local/bin/semantic-clip`
**Language:** Node.js (CommonJS + ES module import for `@xenova/transformers`)
**Lines:** 114
**Ingested:** 2026-05-31

## What it does

Reads all pre-computed `.ajson` embedding files from `.smart-env/multi/`, embeds the query using `TaylorAI/bge-micro-v2` (ONNX, local), and returns top-3 cosine similarity matches with file path + summary.

## Key implementation details

- **`.ajson` format quirk:** each file is a bare `"key": {...},` (not valid JSON). Must strip trailing comma and wrap in `{}` before `JSON.parse()`.
- **Vector key:** `embeddings["TaylorAI/bge-micro-v2"].vec` — 384-dim float array.
- **Cosine similarity:** manual dot-product / magnitude calc (no external math lib).
- **Summary extraction:** tries frontmatter `summary:` field first, falls back to first 300 chars of body (strips frontmatter block).
- **Model noise suppression:** temporarily overrides `console.warn` during model load to keep output clean.

## Dependencies

| Package | Role |
|---------|------|
| `@xenova/transformers` | ONNX model runner, downloads `TaylorAI/bge-micro-v2` ~23MB on first run |
| Node.js stdlib (`fs`, `path`) | File I/O only |

No Python, no MCP server, no network after first model download.

## Embedding delta issue (as of 2026-05-31)

Only 25 `.ajson` files vs 74 wiki pages — Smart Connections hasn't finished indexing the full vault. Run Smart Connections from Obsidian to trigger re-index before semantic-clip returns full coverage.

## Related

- [[semantic-clip]] — entity page (what it is, usage, role in stack)
- [[smart-clip]] — three-tier orchestrator that calls this as Tier 2
- [[wiki-clip]] — Tier 1 keyword counterpart
- [[smart-connections]] — the Obsidian plugin whose `.smart-env/` data this reads
