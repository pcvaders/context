---
title: design-extract (designlang) — Manavarya09
date: 2026-05-20
summary: "CLI + MCP server that extracts a complete design system from any URL — DTCG tokens, Tailwind config, Figma variables, WCAG audit."
tags: [design, mcp, cli, tooling]
---

> CLI + MCP server that extracts a website's complete design system — DTCG tokens, Tailwind config, Figma variables, motion tokens, WCAG audit — with one command.

# Source — Manavarya09/design-extract (designlang)

**Author**: Manav Arya Singh (Manavarya09)
**URL**: https://github.com/Manavarya09/design-extract
**npm**: `designlang`
**Type**: GitHub repo / CLI tool / MCP server / Claude Code plugin
**Clipped**: 2026-05-20
**Ingested**: 2026-05-20

---

## One-line thesis

`npx designlang <url>` → headless Playwright crawl → 17+ output files: DTCG tokens, Tailwind config, shadcn theme, Figma variables, motion tokens, typed React component anatomy, brand voice, WCAG audit, paste-ready LLM prompts, and a shareable grade report.

## Key takeaways

- **One command** covers what most extractors don't: layout patterns, responsive behavior (4 breakpoints), hover/focus/active state transitions, multi-page consistency, drift checks, WCAG remediation palette
- **17+ output files** per run including `*-design-tokens.json` (W3C DTCG), `*-tailwind.config.js`, `*-shadcn-theme.css`, `*-figma-variables.json`, `*-anatomy.tsx`, `*-motion-tokens.json`, `*-voice.json`
- **MCP server** (`designlang mcp`) — exposes tokens, regions, components, contrast pairs to Claude Code/Cursor/Windsurf
- **Claude Code plugin** — `/plugin install Manavarya09/design-extract` → 5 slash commands: `/extract`, `/grade`, `/battle`, `/remix`, `/pack`
- **Agent skill** — `npx skills add Manavarya09/design-extract` for 40+ agents
- **Design grading** (`designlang grade`) — shareable HTML report card, letter grade A-F across 8 dimensions
- **Battle mode** (`designlang battle stripe.com vercel.com`) — head-to-head design comparison
- **Remix** (`designlang remix <url> --as cyberpunk`) — restyle in 6 vocabularies
- **Pair** (`designlang pair <A> <B>`) — fuse two design systems across 7 axes
- **CI-ready**: `drift`, `lint`, `visual-diff` all exit non-zero on failure

## Multi-platform output

`--platforms web,ios,android,flutter,wordpress,all` emits platform-specific token files (SwiftUI, Compose, Flutter, WP block theme).

## Surfaces

| Surface | How |
|---|---|
| CLI | `npx designlang <url>` |
| MCP server | `npx designlang mcp` (stdio) |
| Claude Code plugin | `/plugin install Manavarya09/design-extract` |
| VS Code extension | `vscode-extension/` |
| Figma plugin | URL → Figma Variables collection |
| Chrome extension | One-click from any tab |
| GitHub Action | Design regression guard on PRs |
| Raycast extension | Extract/score from launcher |

## Relevance to this vault

- Demonstrates MCP-as-tool-wrapper pattern (wraps Playwright extraction, exposes via MCP)
- Claude Code plugin architecture example
- Not directly used in wiki workflow — design tooling, not knowledge tooling

## Related concepts

- [[claude-code-skills]] — plugin/skill install pattern
- [[mcp]] — MCP server pattern

## Related entities

- [[claude-code]] — primary agent target

(as of 2026-05)
