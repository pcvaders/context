> CLI keyword search tool over AI LLM Wiki + Claude Skills frontmatter (Tier 1 of smart-clip pipeline).

## wiki-clip

**Type:** CLI tool (local bash alias)
**Layer:** Tier 1 — keyword search (fast, no embeddings required)
**Part of:** [[smart-clip]] three-tier search pipeline

## What it does

Searches frontmatter fields (`title`, `summary`, `tags`) across:
- `wiki/` markdown pages (concepts, entities, sources, syntheses)
- Claude Skills files (`.claude/skills/`)
- ChatLogs / session logs

Returns ranked matches by keyword frequency. No vector model required — runs instantly from shell.

## Usage

```bash
wiki-clip "query string"
```

## When to use

Use wiki-clip when:
- Query maps cleanly to known titles or tags
- Speed matters (Tier 1 returns instantly)
- [[smart-clip]] Tier 1 step (auto-called before semantic escalation)

## Related

- [[smart-clip]] — orchestrates wiki-clip → semantic-clip → NotebookLM
- [[semantic-clip]] — Tier 2 vector search (escalation path)
- [[llm-wiki]] — the knowledge base it searches

## Log

- 2026-05-22: first referenced in vault CLI setup
