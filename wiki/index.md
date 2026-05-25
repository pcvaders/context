# AI Agentic Wiki — Index

> Master index of all wiki pages. Updated as new pages are created.

## Structure

- **[[concepts/]]** — Fundamental ideas: RAG, MCP, context windows, agent memory, semantic search, embeddings, etc.
- **[[entities/]]** — Tools, models, people, orgs: Claude Code, Karpathy, Smart Connections, Obsidian, etc.
- **[[sources/]]** — Summaries of ingested sources: papers, gists, articles, repos
- **[[syntheses/]]** — Cross-cutting analysis: comparisons, frameworks, emergent patterns

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

## Entities

| Page | Summary |
|---|---|
| [[claude-code]] | Anthropic's agentic coding tool — recommended LLM writer for wiki pattern |
| [[karpathy-andrej]] | AI researcher, OpenAI co-founder, creator of LLM Wiki pattern |
| [[obsidian]] | Markdown IDE — reading interface for this vault |
| [[smart-connections-mcp]] | ~~MCP server~~ DEPRECATED 2026-05-22 — replaced by [[semantic-clip]] |
| [[semantic-clip]] | Node.js CLI — local semantic search via `.smart-env` vecs, zero MCP overhead |
| [[julius-brussee]] | Creator of caveman token compression skill and ecosystem |

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
| [[claude-skills-agent-discovery-feb2026]] | Feb 2026 Skills ecosystem discovery: Agent Skills timeline, SKILL.md format, Skills vs NotebookLM, mobile gap |
| [[ai-infrastructure-stack-mar2026]] | Mar 2026 AI stack convergence: inference cost management, Aug-Sep 2025 degradation incident, OpenClaw, TurboQuant, ARM AGI CPU |
| [[djbrightone-spotify-skill-may2026]] | Spotify Monday workflow skill: 6-step pipeline, two-app architecture, launchd setup pattern, root cause of automation never firing |

## Syntheses

| Page | Summary |
|---|---|
| [[rag-vs-llm-wiki]] | Comparison of RAG and LLM Wiki knowledge architectures |

---

Last updated: 2026-05-25 15:06 UTC
