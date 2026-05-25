> Adding a new source to the wiki and integrating its knowledge into existing pages.

# Ingest

## Definition

Ingest is the first of three core [[llm-wiki]] operations. It is the process of reading a new raw source and permanently weaving its knowledge into the wiki — updating existing pages, creating new ones, and cross-linking everything.

## Process

1. Read the source fully — treat it as immutable, never modify `raw/`
2. Create or update a `wiki/sources/` page summarising the source
3. For each key concept or entity: update the relevant page or create it if missing
4. Add `[[wikilinks]]` between related pages
5. Flag any contradictions with existing wiki content explicitly
6. Update `wiki/index.md`
7. Append to `wiki/log.md` with agent, status, pages touched, next step

## Scale

One ingest typically touches **5–15 wiki pages**. Be specific, not exhaustive. The goal is to deepen the wiki, not sprawl it.

## Quality rules

- Specifics beat summaries — name actual concepts, decisions, people
- Prefer updating existing pages over creating new ones
- Never fabricate citations — mark unsourced claims `[unsourced]`
- Flag contradictions explicitly — do not silently blend conflicting claims
- Date-stamp any claim that could go stale: `(as of YYYY-MM)`

## Dispatch continuity

After every ingest:
- Update `log.md` with **Status** and **Next step**
- Update `agents/[agent-name]/dispatch-state.md` with current progress
- This allows any subsequent dispatch call to resume exactly where it stopped

## Related

- [[llm-wiki]], [[query]], [[lint]], [[log.md]], [[index.md]]

(as of 2026-05)
