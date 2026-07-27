---
title: Obsidian-Agent Bridge ("The Bridge")
type: entity
created: 2026-07-14
updated: 2026-07-14
status: active
tags: [bridge, recall, skills, agents]
---

> summary: The connective layer between the Obsidian vault and AI agents — recall CLI (3 corpora), clip tools, skills, and hooks, with honest-absence guarantees.

# Obsidian-Agent Bridge ("The Bridge")

The connective tissue between the [[obsidian]] vault and every AI agent: it turns the wiki + memory into agent-readable/writable knowledge with honest-absence guarantees.

## Components

**recall** — the front door. One CLI (`~/.local/bin/recall` → `~/projects/homelab/recall/recall.sh`) fanning out in parallel to three distinct corpora:

| Arm | Tool | Gate |
|---|---|---|
| CONCEPT | `vault smart` — 3 tiers: [[wiki-clip]] keyword → [[semantic-clip]] (z ≥ 1.85) → NotebookLM | z-score floor |
| CODE | `graphify query` — per-project AST graph (`graphify-out/graph.json`) | none (nearest-neighbour) |
| LIBRARY | `memorwise query` — CT105 `:4747`, ~1,133 sources | 0.40 score floor |

Honest absence is a first-class answer on every gated arm (`[no confident match]`, `[no matches in <arm>]`) — never gap-fill. Hub-backed variant: `http://<hub-lan-ip>:8090/recall?q=…` (24/7, CT107; LAN address in [[homelab]]).

**Clip tools:** [[wiki-clip]] (zero-cost keyword/frontmatter), [[semantic-clip]] (local ONNX bge-micro-v2, ~23MB, no network), `nlm` ([[notebooklm-mcp]], paid, Tier-3 only).

**Skills enforcing wiki-first behavior:** `recall`, [[interlinked]] (ingest/query/lint), [[obsidian-wiki-memory]] (session-start vault context).

**Hooks:** SessionStart loads brain context + rules; Stop syncs `~/.claude` memory → homelab-brain (`memory/mac-m3/`) + session ledger.

## See also

Full system map: `wiki-ha/syntheses/local-ai-system-overview-2026-07.md` (personal tier, local only) · Hub: [[homelab]] · Being generalized for new users as the **brain-appliance** (spec `~/projects/brain-appliance/docs/superpowers/specs/2026-07-14-brain-appliance-v1-design.md`, where the Bridge becomes `brainctl` on PyPI + HTTP API).
