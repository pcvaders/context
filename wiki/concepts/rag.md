> Traditional retrieval-augmented generation — the pattern the LLM Wiki replaces.

# RAG (Retrieval-Augmented Generation)

## Definition

RAG is a technique for grounding LLM responses in specific documents. At query time, relevant chunks are retrieved from a vector database and injected into the LLM's context window alongside the question.

## How it works

1. Documents are chunked and embedded into a vector database (e.g. Pinecone, Chroma, Weaviate)
2. At query time, the question is embedded and semantically similar chunks are retrieved
3. Retrieved chunks are injected into the LLM prompt as context
4. The LLM generates an answer grounded in the retrieved content

## The core problem

**RAG rediscovers knowledge from scratch on every query.** Nothing accumulates. Ask a question requiring synthesis of five documents, and the LLM re-finds and re-pieces together fragments every time.

- Cross-references must be re-assembled at query time
- Contradictions surface at query time (if at all)
- Every session starts from zero
- Knowledge does not compound

## Examples of RAG systems

- NotebookLM (Google)
- ChatGPT file uploads
- Most enterprise "chat with your docs" tools
- The original Pinecone memory system (what this vault replaced)

## Contrast with LLM Wiki

| | RAG | [[llm-wiki]] |
|---|---|---|
| Knowledge model | Re-derived every query | Compiled once, kept current |
| Cross-references | Re-assembled at query time | Already in wiki pages |
| Contradictions | Surface at query time | Flagged during [[ingest]] |
| Compounding | None | Every ingest deepens the wiki |
| Maintenance | Low upfront, high per-query | High upfront, low per-query |
| Requires vector DB | Yes | No |

## When RAG is still appropriate

- Very large document sets (thousands of files) where full wiki compilation is impractical
- Real-time document search where freshness matters more than synthesis
- When you need verbatim retrieval rather than synthesised knowledge

## Sources

- [[karpathy-llm-wiki-gist]] — Karpathy's framing of the RAG problem

## Related

- [[llm-wiki]], [[ingest]], [[smart-connections]], [[pinecone]]

(as of 2026-05)
