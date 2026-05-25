> A pattern for building personal knowledge bases where the LLM incrementally builds and maintains a persistent wiki rather than re-deriving knowledge from raw documents on every query.

# LLM Wiki

## Definition

The LLM Wiki is a knowledge architecture pattern where an LLM acts as the writer and maintainer of a structured, interlinked set of markdown files — the wiki layer — that sits between raw sources and the human reader.

The key insight: **knowledge is compiled once and kept current**, not re-discovered from scratch on every query. The wiki is a persistent, compounding artifact.

## The Three Layers

1. **Raw sources** — immutable curated collection (articles, papers, gists, transcripts). Never modified.
2. **Wiki layer** — LLM-generated markdown files. Summaries, entity pages, concept pages, synthesis. The LLM owns this entirely.
3. **Schema** — a CLAUDE.md or AGENTS.md file telling the LLM how the wiki is structured and what workflows to follow.

## The Three Operations

- [[ingest]] — read a new source, update wiki pages, cross-link
- [[query]] — answer questions from the wiki, file answers back as new pages
- [[lint]] — periodic health check, fix contradictions and orphan pages

## Contrast with RAG

| | RAG | LLM Wiki |
|---|---|---|
| Knowledge model | Re-derived on every query | Compiled once, kept current |
| Cross-references | Re-assembled at query time | Already there |
| Contradictions | Surface at query time (if at all) | Flagged during ingest |
| Compounding | None | Every ingest deepens the wiki |
| Maintenance cost | Low upfront, high per-query | High upfront (ingest), low per-query |

See [[rag]] for full contrast.

## Practical Setup

- [[obsidian]] as the IDE — reading interface, backlinks, graph view
- [[claude-code]] or Claude.ai as the programmer — writes and maintains the wiki
- The wiki is the codebase — persistent artifact that grows over time

## Indexing Strategy

**[[index.md]]** — content-oriented catalog. One-line summary per page, organised by category. Updated on every ingest. Effective at moderate scale (~100 sources, hundreds of pages) without needing embedding-based RAG.

**[[log.md]]** — append-only chronological record. Every operation logged with agent, status, pages touched, next step. The dispatch continuity anchor.

## Use Cases

- Personal knowledge (goals, health, psychology, self-improvement)
- Research (building an evolving thesis across many papers)
- Books (companion wiki with characters, themes, plot threads)
- Business/team (internal wiki fed by Slack, transcripts, documents)
- Competitive analysis, due diligence, trip planning, course notes

## Sources

- [[karpathy-llm-wiki-gist]] — original idea file (April 2026)

## Related

- [[rag]], [[ingest]], [[query]], [[lint]], [[karpathy-andrej]], [[obsidian]], [[claude-code]]

(as of 2026-05)
