# Pinecone

> Managed vector database service — primary alternative to local embeddings for RAG pipelines at scale.

**URL**: https://pinecone.io  
**Type**: Cloud service, vector database  
**Relevance**: Referenced as RAG infrastructure contrast vs LLM Wiki pattern

## What it does

Pinecone stores and queries high-dimensional vector embeddings at scale. Used in production RAG systems where:
- Corpus is too large for local embedding (millions of docs)
- Low-latency retrieval at query time is required
- Multiple clients need shared index access

## Contrast with LLM Wiki

RAG + Pinecone = retrieve chunks per query, re-synthesize each time.  
LLM Wiki = pre-synthesized wiki pages, semantic search over structured knowledge.

See [[rag-vs-llm-wiki]] for full comparison.

## Related

- [[rag]] — retrieval pattern Pinecone supports
- [[rag-vs-llm-wiki]] — architectural comparison
- [[smart-connections]] — local alternative (Obsidian vault, no cloud)
