> Local-first markdown note-taking app — the reading interface for this LLM Wiki.

# Obsidian

## What it is

Obsidian is a local-first note-taking application built around plain markdown files stored in a vault on your own machine (or synced storage). Notes are linked via `[[wikilinks]]`, visualised as a graph, and extended via a large community plugin ecosystem.

## Role in this vault

In [[karpathy-andrej]]'s framing: **Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase.**

- Human reads and navigates the wiki in Obsidian
- Claude writes and maintains the wiki pages
- Obsidian's graph view shows the knowledge network
- Wikilinks resolve automatically across the vault

## Key features for this setup

- **`[[wikilinks]]`** — bidirectional links between pages, auto-completing as you type
- **Graph view** — visual map of the entire knowledge network
- **Backlinks panel** — see every page that links to the current one
- **Local vault** — files are plain markdown, readable by any agent or tool
- **Community plugins** — extends the vault with semantic search, templates, dashboards

## Relevant plugins

See `obsidian-starter-pack.md` in the vault root for the full validated list (May 2026).

Key plugins for this setup:
- [[smart-connections]] — semantic search layer
- Dataview — query vault as a database
- Templater — consistent page structure
- Tasks + Kanban — dispatch workflow tracking

## Vault path (this wiki)

`/Users/voyager1/Library/CloudStorage/GoogleDrive-pcgamesplay1@gmail.com/My Drive/Obsidian/Obsidian Vault AI`

## Version

1.12.7 (Installer 1.12.4) — as of 2026-05

## Related

- [[llm-wiki]], [[smart-connections]], [[karpathy-andrej]], [[claude-code]]

(as of 2026-05)
