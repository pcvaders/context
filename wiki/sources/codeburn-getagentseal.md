---
title: Codeburn (getagentseal)
date: 2026-05-20
summary: "TUI dashboard tracking token cost and performance across 19+ AI coding tools — offline, no proxy, reads local session files."
tags: [tooling, cost, observability, claude-code]
---

> Interactive TUI + menu bar for tracking token cost and performance across 19+ AI coding tools — reads session data locally, no proxy, no API key.

# Source — getagentseal/codeburn

**Author**: AgentSeal (iamtoruk)
**URL**: https://github.com/getagentseal/codeburn
**Type**: GitHub repo / CLI tool
**Clipped**: 2026-05-20
**Ingested**: 2026-05-20

---

## One-line thesis

`npm install -g codeburn` → TUI dashboard that reads local session files from Claude Code, Codex, Cursor, Gemini CLI, and 16+ more agents, prices every API call via LiteLLM, and breaks spend by task type, model, project, and tool — all offline.

## Key takeaways

- **19+ providers supported** (as of 2026-05): Claude Code, Claude Desktop, Codex, Cursor, Gemini CLI, Cline, Roo Code, OpenCode, OpenClaw, Pi, Mistral Vibe, Kiro, GitHub Copilot, IBM Bob, Kimi Code CLI, KiloCode, Qwen, Droid, Crush, Goose, Antigravity
- **Zero network dependency for data** — reads JSONL/SQLite/JSON session files directly from disk
- **LiteLLM pricing** — fetched + cached 24h at `~/.cache/codeburn/`; hardcoded fallbacks for Claude + GPT models
- **13 task categories** — classified deterministically from tool usage patterns (no LLM calls)
- **One-shot rate** — detects Edit/Bash/Edit retry cycles; shows % of edits that succeeded first try
- **Yield analysis** (`codeburn yield`) — correlates sessions with git commits to surface productive vs abandoned spend
- **Optimize** (`codeburn optimize`) — scans `~/.claude/` for waste: unused MCPs, bloated CLAUDE.md, low Read:Edit ratio, uncapped bash output
- **Compare** (`codeburn compare`) — side-by-side model performance: cost/call, cost/edit, cache hit %, one-shot rate
- **macOS menu bar** (`codeburn menubar`) — native Swift/SwiftUI app, shows today's spend, auto-refreshes 30s
- **Multi-config Claude** — `CLAUDE_CONFIG_DIRS=~/.claude-work:~/.claude-personal` merges multiple accounts

## Task categories (13)

Coding, Debugging, Feature Dev, Refactoring, Testing, Exploration, Planning, Delegation, Git Ops, Build/Deploy, Brainstorming, Conversation, General — classified from tool names and message keywords.

## Key commands

```bash
codeburn                     # 7-day TUI dashboard
codeburn today               # today
codeburn optimize            # waste scan + fixes
codeburn compare             # model comparison
codeburn yield               # productive vs abandoned spend
codeburn menubar             # install + launch menu bar app
codeburn models --by-task    # per-model per-task-type breakdown
```

## Dashboard signals (interpretation guide from repo)

| Signal | Meaning |
|---|---|
| Cache hit < 80% | Context not stable, or caching misconfigured |
| Many `Read` calls | Agent re-reading same files, missing context |
| Low 1-shot rate | Retry loops, agent struggling with edits |
| Opus dominating small turns | Overpowered model |
| Bash dominated by `git status`/`ls` | Agent exploring not executing |
| Conversation category dominant | Agent talking not doing |

## How data is read

- **Claude Code**: JSONL at `~/.claude/projects/<path>/<session-id>.jsonl`
- **Codex**: JSONL at `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`
- **Cursor**: SQLite at `~/Library/Application Support/Cursor/User/globalStorage/state.vscdb`
- **Gemini CLI**: JSON files at `~/.gemini/tmp/<project>/chats/session-*.json`
- **OpenCode**: SQLite at `~/.local/share/opencode/opencode*.db`

## Relevance to this vault

Direct observability layer for the LLM Wiki workflow. `codeburn optimize` surfaces wasted tokens in CLAUDE.md and unused MCPs — directly actionable for vault maintenance efficiency.

## Related concepts

- [[ai-cost-observability]] — the category this tool exemplifies
- [[token-compression]] — complementary: caveman reduces tokens, codeburn measures them

## Related entities

- [[claude-code]] — primary supported provider

(as of 2026-05)
