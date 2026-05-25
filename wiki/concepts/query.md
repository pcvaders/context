> Asking questions against the wiki and filing good answers back as new pages.

# Query

## Definition

Query is the second of three core [[llm-wiki]] operations. It is the process of asking questions against the compiled wiki and synthesising answers from existing pages — with citations.

## Process

1. Check `log.md` for recent context and active workflows
2. Search wiki pages relevant to the question
3. Synthesise an answer with citations to specific pages
4. Label clearly when supplementing from general knowledge vs wiki content
5. If a gap exists, note it: *"This isn't in the wiki yet — want me to create a page?"*
6. Substantial answers can be filed back as new `wiki/syntheses/` pages

## Key insight

**Good answers compound.** When a query produces a useful synthesis — a comparison, an analysis, a pattern across multiple sources — that answer should be filed back into the wiki as a new page. It doesn't disappear into chat history.

Examples of answers worth filing back:
- Comparisons: `wiki/syntheses/rag-vs-llm-wiki.md`
- Patterns: `wiki/syntheses/agent-memory-patterns.md`
- Analyses: `wiki/syntheses/why-pinecone-is-overkill.md`

## Answer from wiki first

Always check what's compiled in the wiki before generating from general knowledge. Label the source:
- *"From the wiki: ..."*
- *"From general knowledge (not yet in wiki): ..."*

## Related

- [[llm-wiki]], [[ingest]], [[lint]], [[syntheses]]

(as of 2026-05)
