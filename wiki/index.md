# AI Agentic Wiki — Index

> Master index of all wiki pages. Updated as new pages are created.

## Structure

- **[[concepts/]]** — Fundamental ideas: RAG, MCP, context windows, agent memory, semantic search, embeddings, etc.
- **[[entities/]]** — Tools, models, people, orgs: Claude Code, Karpathy, Smart Connections, Obsidian, etc.
- **[[sources/]]** — Summaries of ingested sources: papers, gists, articles, repos
- **[[syntheses/]]** — Cross-cutting analysis: comparisons, frameworks, emergent patterns
- **[[pinokio/]]** — Pinokio launcher + Windows 11 local AI stack

## Concepts

| Page | Summary |
|---|---|
| [[llm-wiki]] | Pattern: LLM builds persistent wiki layer over raw sources instead of re-deriving per query |
| [[rag]] | Retrieval-Augmented Generation — contrast with LLM Wiki |
| [[ingest]] | Operation: read source → update wiki pages → cross-link → log |
| [[query]] | Operation: answer from wiki, file good answers back as pages |
| [[lint]] | Operation: find orphans, contradictions, stale claims |
| [[token-compression]] | Techniques to cut LLM output tokens without losing accuracy |
| [[claude-code-skills]] | Claude Code plugin/skill system — markdown files extending agent behavior |
| [[ai-cost-observability]] | Tools + practices for measuring and optimizing AI token spend |
| [[skill-ecosystem]] | 4-marketplace Claude Code skill stack: superpowers, antigravity, karpathy, caveman |
| [[agent-native-cli]] | Design pattern for LLM-consumable CLIs: auto-JSON, typed exit codes, --compact, SQLite |
| [[claude-ai-context-loading]] | Project Instructions / CLAUDE.md / hooks pattern for persistent context across Claude surfaces |
| [[mcp]] | Model Context Protocol — Anthropic standard for tool/resource exposure to LLM agents |

## Entities

| Page | Summary |
|---|---|
| [[claude-code]] | Anthropic's agentic coding tool — recommended LLM writer for wiki pattern |
| [[karpathy-andrej]] | AI researcher, OpenAI co-founder, creator of LLM Wiki pattern |
| [[obsidian]] | Markdown IDE — reading interface for this vault |
| [[smart-connections-mcp]] | ~~MCP server~~ DEPRECATED 2026-05-22 — replaced by [[semantic-clip]] |
| [[semantic-clip]] | Node.js CLI — local semantic search via `.smart-env` vecs, zero MCP overhead |
| [[julius-brussee]] | Creator of caveman token compression skill and ecosystem |
| [[litellm-proxy]] | LiteLLM proxy — unified OpenAI-compatible gateway routing to multiple LLM backends |

## Pinokio / Windows 11

| Page | Summary |
|---|---|
| [[pinokio/pinokio]] | One-click AI app launcher — manages local AI tools, Python envs, model downloads |
| [[pinokio/Windows 11/windows-11]] | Windows 11 Pro host — specs, local AI stack (Ollama + Hermes + Open WebUI) |
| [[pinokio/Windows 11/claude-code-sync]] | Guide: mirror Mac Claude Code setup to Windows 11 — skills, hooks, commands, settings.json |

## Sources

| Page | Summary |
|---|---|
| [[karpathy-llm-wiki-gist]] | April 2026 gist defining three-layer LLM Wiki architecture |
| [[dan6684-smart-connections-mcp]] | MCP server exposing Obsidian Smart Connections to Claude Code |
| [[caveman-julius-brussee]] | Claude Code skill — ~65% output token compression via caveman brevity |
| [[codeburn-getagentseal]] | TUI + menu bar for token cost observability across 19+ AI coding tools |
| [[design-extract-manavarya09]] | CLI + MCP server extracting website design systems — DTCG tokens, Tailwind, Figma vars |
| [[cloakbrowser-cloakhq]] | Stealth Chromium fork — drop-in Playwright replacement, passes bot detection (stub) |
| [[antigravity-awesome-skills]] | Community library of 1,431 Claude Code skills in 37 curated bundles across 9 categories |
| [[karpathy-guidelines-source]] | Karpathy coding guidelines plugin — 4 rules: think first, simplicity, surgical, goal-driven |
| [[vault-setup-session]] | Founding session: Obsidian vault structure, nested vault discovery, Smart Connections MCP setup |
| [[mcp-connector-management]] | MCP toggle patterns: disabled.json, SwiftBar plugin, Claude Desktop config race condition |
| [[cli-printing-press]] | Agent-driven Go CLI + MCP server generator from any API spec — printing-press v4.9.0 |
| [[claude-mobile-sync-issues-2026-05]] | Mobile sync root causes, GitHub bridge, daemon bug fix, Claude desktop redesign notes (May 2026) |

## Syntheses

| Page | Summary |
|---|---|
| [[rag-vs-llm-wiki]] | Comparison of RAG and LLM Wiki knowledge architectures |
| [[skill-selection-guide]] | Task→skill mapping, workflow phase map, anti-patterns for Claude Code skill selection |

---

Last updated: 2026-05-31 00:19 UTC
