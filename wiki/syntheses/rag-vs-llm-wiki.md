> RAG re-derives knowledge from scratch on every query; the LLM Wiki compiles it once and keeps it current.

# RAG vs LLM Wiki

## The Core Difference

The fundamental difference is **when knowledge is assembled**.

**RAG** assembles knowledge at query time — every time you ask a question, it retrieves relevant chunks from a vector database and re-pieces them together. Nothing accumulates between queries. Ask the same question tomorrow and it rediscovers the same fragments from scratch.

**LLM Wiki** assembles knowledge at ingest time — when a new source arrives, the LLM reads it, extracts what matters, and permanently weaves it into the wiki. Cross-references are already there. Contradictions are already flagged. The next query finds a pre-compiled answer, not raw fragments.

## Comparison

| | RAG | LLM Wiki |
|---|---|---|
| Knowledge model | Re-derived every query | Compiled once, kept current |
| Cross-references | Re-assembled at query time | Already in wiki pages |
| Contradictions | Surface at query time (if at all) | Flagged during [[ingest]] |
| Compounding | None | Every ingest deepens the wiki |
| Maintenance cost | Low upfront, high per-query | High upfront, low per-query |
| Requires vector DB | Yes | No |
| Best for | Large doc sets, verbatim retrieval | Synthesised knowledge, compounding insight |

## Karpathy's Framing

The cost is paid upfront in maintenance ([[ingest]], [[lint]]), but queries become faster, more accurate, and more cumulative. Knowledge compounds rather than evaporates into chat history.

## When RAG Is Still Appropriate

- Very large document sets (thousands of files) where full wiki compilation is impractical
- Real-time document search where freshness matters more than synthesis
- When verbatim retrieval is needed rather than synthesised knowledge

## Why This Vault Chose LLM Wiki

The original memory system (wrap-up/recall skills) was RAG-flavoured — session summaries stored in Pinecone, retrieved semantically at query time. The LLM Wiki pattern was chosen because:

1. Knowledge compounds — each ingest deepens the wiki rather than adding to a flat index
2. No vector DB required — Obsidian + Smart Connections handles search locally
3. Contradictions are surfaced explicitly during ingest, not discovered accidentally at query time
4. Cowork dispatch can resume from `log.md` — no reliance on embedding freshness

## Sources

- [[karpathy-llm-wiki-gist]] — original framing
- [[rag]] — full RAG concept page
- [[llm-wiki]] — full LLM Wiki concept page

## Related

- [[ingest]], [[query]], [[lint]], [[smart-connections]], [[obsidian]]

*Filed from query: "How does the LLM Wiki differ from RAG?" — 2026-05-19*
(as of 2026-05)
