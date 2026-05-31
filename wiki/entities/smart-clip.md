> Three-tier local search orchestrator: keyword → semantic → NotebookLM fallback over the AI LLM Wiki vault.

## smart-clip

**Type:** CLI tool (local bash alias)
**Layer:** Tier 3 orchestrator
**Calls:** [[wiki-clip]] → [[semantic-clip]] → NotebookLM fallback

## What it does

Runs a progressive search pipeline over the vault:

| Tier | Tool | Method | Speed |
|------|------|---------|-------|
| 1 | [[wiki-clip]] | Keyword / frontmatter | Instant |
| 2 | [[semantic-clip]] | Vector embeddings (.smart-env/) | Fast |
| 3 | NotebookLM | LLM-backed notebook search | Slow / cloud |

Escalates to the next tier only if the previous returns insufficient results. Tier 3 (NotebookLM) requires the NLM MCP to be enabled.

## Usage

```bash
smart-clip "query string"
```

## When to use

Default search command for vault queries when you don't know which tier will have the answer. wiki-clip and semantic-clip can be called directly for speed.

## Related

- [[wiki-clip]] — Tier 1 keyword search
- [[semantic-clip]] — Tier 2 vector search
- [[llm-wiki]] — the vault it searches

## Log

- 2026-05-22: first referenced in vault CLI setup alongside wiki-clip and semantic-clip
