---
title: "Session startup triggers not activating"
date: "2026-05-30"
uuid: "cf71fd4b-5496-483c-a051-9ac74151b903"
source: "claude-chat-export"
messages: 2
---

# Session startup triggers not activating

**Date**: 2026-05-30  
**Messages**: 1 human / 1 assistant  
**UUID**: `cf71fd4b-5496-483c-a051-9ac74151b903`  

## Conversation

### **Human**

hey chat

### **Claude**

Hey! Wiki's loaded. Here's where things stand:

**Last entry — [2026-05-22] ARCHITECTURE: vault CLI + dual wiki + NLM automation**
You consolidated everything behind a single `vault` command, stood up a parallel `wiki-personal/` vault, and automated the NotebookLM sync so the AI wiki now pushes to NLM as six auto-managed bundles (Concepts, Entities, Sources, Syntheses, Home Assistant, Log+Index) — replacing the old eight hand-managed sources.

**Open items still hanging:**
- Ingest `semantic-clip.js` itself as a source page (`sources/semantic-clip.md`)
- Create entity pages for `wiki-clip` and `smart-clip` (referenced but undocumented)
- Log two new skills that appeared 2026-05-22: `obsidian-wiki-memory` and `interlinked`
- Embedding delta health issue: only 25 `.ajson` files vs 57 wiki pages — Smart Connections hasn't finished indexing the full vault (target delta ≤ 5)

One thing worth flagging: there are several entries all stamped `2026-05-22`, so "last entry" is a bit ambiguous in ordering — the CLI/dual-wiki one sits at the bottom of the file, so I'm treating it as most recent.

Where do you want to go from here?
- **Ingest** a new source
- **Query** the wiki (or general AI/agent/tooling question)
- **Lint** pass — feels overdue given the orphan-link and embedding-delta notes

What's the move?
