---
title: Karpathy LLM Wiki Gist
date: 2026-05-19
summary: "Karpathy's April 2026 gist proposing persistent LLM-maintained wikis as an alternative to RAG — the founding pattern for this vault."
tags: [karpathy, llm-wiki, rag, methodology]
---

> One source that defines the entire pattern this wiki is built on.

# Source — Karpathy LLM Wiki Gist

**Author**: Andrej Karpathy
**Date**: April 4, 2026
**URL**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
**Type**: Idea file / concept gist
**Ingested**: 2026-05-19

---

## One-line thesis

Instead of re-deriving knowledge from raw documents on every query (RAG), the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that compounds knowledge over time.

## Key takeaways

- The wiki is a **persistent, compounding artifact** — not a log, not a search index
- Knowledge is compiled once and kept current, not re-discovered on every query
- The LLM owns the wiki layer entirely — humans read it, LLMs write it
- Three operations drive everything: [[ingest]], [[query]], [[lint]]
- [[index.md]] and [[log.md]] are the two structural anchors

## Scope

Describes three-layer architecture (raw sources, wiki layer, schema), three operations (ingest, query, lint), indexing strategy, use cases, and philosophical contrast with RAG.

## Related concepts

- [[llm-wiki]] — the core pattern
- [[rag]] — what this replaces
- [[ingest]] — first operation
- [[query]] — second operation
- [[lint]] — third operation

## Related entities

- [[karpathy-andrej]] — author
- [[obsidian]] — recommended reading interface
- [[claude-code]] — recommended writing agent
