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

## Summary contract — REQUIRED on every page

Every page indexed by `generate_wiki_index.py` (concepts, entities, sources,
syntheses, incidents, pinokio) MUST carry a summary in one of two forms:

1. **`summary:` in YAML frontmatter** — preferred for generated pages such as
   `sources/claude-chat-*`, because a script can write it:

   ```
   ---
   title: "Aqara motion sensor setup"
   summary: "Established that the Aqara High Human Sensor is PIR-based, not mmWave."
   ---
   ```

2. **A `>` blockquote directly under the H1**, before the first `## ` heading —
   the hand-written form used by concepts and entities.

A blockquote *below* the first `## ` heading is body content, not a summary.
The index treats it as body content and ignores it. Do not rely on it.

Check the whole vault with:

```
python3 lint_summaries.py --by-section
```

It exits non-zero if any indexed page lacks a summary, so it can gate an ingest.
It shares `extract_summary()` with the index generator, so the lint count and
the index can never disagree.

**Known gap (as of 2026-09):** the `claude-chat-*` export path does not write
`summary:`. Fix the exporter to emit the frontmatter key — do not hand-patch
individual files. See log.md [2026-09-18] P3.

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

- [[llm-wiki]], [[query]], [[lint]], [[log]], [[index]]

(as of 2026-05)
