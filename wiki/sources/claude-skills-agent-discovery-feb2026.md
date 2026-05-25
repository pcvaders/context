---
title: Claude Agent Skills — Discovery Session (Feb 2026)
summary: "Feb 2026 exploration of Agent Skills ecosystem: official announcement, SKILL.md format, open standard, Skills vs NotebookLM comparison, mobile gap, Apple/Gemini deal context."
tags: [skills, agents, anthropic, notebooklm, apple]
source-type: claude-ai-export
export-id: b7ae9ea3
conversation: "Claude's Skills function and AI agents"
date: 2026-02-23
---

# Claude Agent Skills — Discovery Session (Feb 2026)

> Source: Claude.ai export `b7ae9ea3`, conversation "Claude's Skills function and AI agents" (94 msgs, 2026-02-23). User's first deep exploration of Agent Skills before the voyager1 skill stack was built.

## Key Facts

### Timeline

| Date | Event |
|---|---|
| Oct 2025 | Agent Skills officially announced by Anthropic |
| Dec 2025 | Agent Skills released as open standard (similar to MCP release model) |
| Feb 2026 | This discovery session (predates voyager1 skill stack setup) |
| May 2026 | voyager1 installs 4-marketplace skill stack (see [[skill-ecosystem]]) |

### Official Resources

- `github.com/anthropics/skills` — Anthropic's public pre-built example skills (creative, design, dev, enterprise, doc processing)
- `agentskills.io` — open standard spec, guides, tutorials
- `github.com/agentskills/agentskills` — community repository
- `template-skill` folder in anthropics/skills — starting point for custom skills

### Two Different Things Called "Skills"

1. **Agent Skills (official product)** — SKILL.md + instructions + scripts + resources. Agents load domain-specific expertise on demand. Announced Oct 2025.
2. **Internal document-generation skills** — legacy internal tools for producing Word docs, PDFs, PPTs. Pre-date Agent Skills. Different system.

Confusion was common at time of this conversation. Agent Skills = the right framing.

## Skills vs NotebookLM

| Dimension | NotebookLM | Agent Skills |
|---|---|---|
| Mode | **Consumption** — understand and query knowledge | **Execution** — act on knowledge |
| Reuse | Per-project rebuild | Reusable across sessions/agents |
| Output | Answers, summaries, audio | Work product (completed tasks) |
| Integration | Google Workspace | Claude Code, Claude.ai, dev platform |

Key insight from session: *"The skill doesn't just know how to fill out a legal contract — it fills it out."*

## Expert-Tool Mismatch Problem

Identified as the main barrier to ecosystem growth:

- Skills format (Markdown + YAML + GitHub) filters out ~95% of potential contributors
- Most valuable domain expertise sits with non-developers (nurses, accountants, tradespeople)
- GUI gap on mobile = unreachable population
- Apple App Store politics compound the problem (30% cut, arbitrary rejection, Apple Intelligence conflict of interest)

## Autonomous Agent Hype Cycle Warning

Session documented a pattern (relevant to evaluating AI agent tools):

1. Launch with dramatic "take over your life admin" claims
2. Tech press coverage without scrutiny
3. Millions of users onboarded
4. Large token burn on tasks that don't complete reliably
5. Quiet failure while founders raise on user numbers (not results)

Token cost issue: systems make API calls users never see — every failed attempt, every retry costs money. When the agent fails, costs are hidden from users.

## Apple/Gemini Context (Jan 2026)

Apple announced Jan 12 2026: multi-year deal with Google to use Gemini model for AI features including upgraded Siri. ~$1 billion/year. Siri jumps from 150B to 1.2T parameters.

Apple considered Anthropic and OpenAI before choosing Google.

Apple historical pattern (leverage → replace):
- Google Maps → Apple Maps
- Intel chips → Apple Silicon (M1)
- Google Search revenue ($20B/year) → building own search index in background

Implication: Apple may eventually replace Gemini once they've learned the space.

## Links

- [[skill-ecosystem]] — installed stack as of May 2026
- [[claude-code-skills]] — concept page for skills mechanism
- [[karpathy-guidelines-source]] — Karpathy guidelines skill
- [[antigravity-awesome-skills]] — community skills library
