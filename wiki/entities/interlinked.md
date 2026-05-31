> Claude Code skill that activates the AI LLM Wiki assistant persona — handles INGEST, QUERY, and LINT operations on the vault.

## interlinked

**Type:** Claude Code skill (`~/.claude/skills/interlinked.md`)
**Plugin:** User-defined (PCGamesplay1/Claude-skills)
**Appears in:** Skill list as `interlinked`

## What it does

Activates the wiki maintainer role for the AI Agentic knowledge base. Three operations:

| Operation | Trigger | What happens |
|-----------|---------|--------------|
| **INGEST** | "interlinked [source]" | Source → summary page → update concept/entity pages → cross-link → index + log |
| **QUERY** | Any AI/agent question | Wiki-first answer, supplements with general knowledge (labelled) |
| **LINT** | "lint the wiki" | Finds orphans, missing pages, contradictions, stale claims |

Follows Karpathy LLM Wiki pattern: raw sources immutable, wiki layer maintained by Claude.

## Session start behaviour

1. Regenerates `wiki/index.html` via `generate_wiki_index.py`
2. Reads `wiki/log.md` for last operation + open items
3. Surfaces status and offers next operation

## Related

- [[obsidian-wiki-memory]] — the memory-load counterpart skill
- [[llm-wiki]] — the vault it maintains
- [[claude-code-skills]] — the skill ecosystem
- [[wiki-clip]], [[smart-clip]] — search tools used during QUERY

## Log

- 2026-05-22: skill created alongside obsidian-wiki-memory
- 2026-05-31: first documented in wiki (this entry)
