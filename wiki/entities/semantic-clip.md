> Local CLI tool that replaces smart-connections-mcp — reads pre-computed `.smart-env/` embeddings directly for zero-network, zero-MCP semantic vault search.

# semantic-clip

## What it is

Node.js CLI binary that performs semantic search over the Obsidian vault using the same pre-computed `TaylorAI/bge-micro-v2` vector embeddings that Smart Connections writes to `.smart-env/multi/*.ajson`. No MCP server, no network, no session token overhead.

## Why it was built

[[smart-connections-mcp]] ran at every Claude Code session start — loading a Python MCP server into context before the user typed anything. No native UI existed to disable individual MCPs (root cause of the [[swiftbar-mcp-toggle]] project). `semantic-clip` eliminates the server entirely by reading the same data directly.

## How it works

1. Reads all `.ajson` files from `.smart-env/multi/`
2. Parses pre-computed 384-dim vectors (format: bare `"key": {...},` — strip trailing comma, wrap in `{}`)
3. Embeds query using `@xenova/transformers` + `TaylorAI/bge-micro-v2` (ONNX, quantized)
4. Cosine similarity against all stored vecs
5. Returns top-3 matches — file path + summary/first 300 chars

## Location

```
/Users/voyager1/Library/Mobile Documents/.../Obsidian Vault AI/semantic-clip.js
~/.local/bin/semantic-clip  (symlink)
/opt/homebrew/bin/semantic-clip  (npm link)
```

## Usage

```bash
semantic-clip "rag architecture"
semantic-clip "token budget contract" | pbcopy
semantic-clip "paperpress dedup" > context.txt
```

## Role in three-tier smart-clip stack

`smart-clip` calls tiers in order — first match wins:

| Tier | Tool | Method | Network |
|---|---|---|---|
| 1 | `wiki-clip` | Keyword match, Paperpress frontmatter | Zero |
| 2 | `semantic-clip` | Vector cosine sim, local `.smart-env` vecs | Zero |
| 3 | `nlm query` | NotebookLM AI semantic answer | Cloud |

## Key implementation detail

`.ajson` format is NOT standard JSON — each file is a bare `"smart_sources:path": {...},` with trailing comma. Must strip comma and wrap in `{}` before `JSON.parse()`. Vecs are 384-dim floats under `embeddings["TaylorAI/bge-micro-v2"].vec`.

## Dependencies

- `@xenova/transformers` — ONNX model runner, downloads `TaylorAI/bge-micro-v2` on first run (~23MB cached)
- No Python, no MCP, no network after first model download

## Related

- [[smart-connections-mcp]] — the MCP server this replaces (DEPRECATED)
- [[smart-connections]] — the Obsidian plugin whose `.smart-env/` embeddings this reads
- [[wiki-clip]] — Tier 1 keyword search CLI
- [[smart-clip]] — three-tier wrapper that orchestrates all tiers
- [[obsidian-agent-bridge]] — parent project

(as of 2026-05)
