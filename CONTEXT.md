# voyager1 — AI Code Context

> Public, sanitized. Hardware/host/network detail lives ONLY in private `voyager-hub/memory/hardware.md`, never here.

## Identity & Tooling

**Name:** voyager1
**Setup:** Two machines (desktop + laptop). Claude is primary IDE on both. Cowork on cloud. Chat for quick questions. CCR for routines.
**Key tools:** claude-code, home-assistant (MCP), lmstudio (local), notebooklm (research).

## Projects

- **Open Design** — Pollinations texture API, model picker patch active
- **Higgsfield** — Video generation, Pollinations/FAL/RunwayML
- **Nano Banana** — Google Gemini free tier, Pro upgrade pending
- **Home Assistant** — local MCP integration
- **AI Tools** — Wiki (Obsidian) + NotebookLM (research notebooks)

## Preferences

- **Visual-first:** Prefer card grids + icons + color-coded UI. Text is a last resort.
- **Vault:** Obsidian AI LLM Wiki + personal wiki (both iCloud). Auto-sync + dedup on SessionStart.
- **Memory:** Unified hub (GitHub private voyager-hub + public CONTEXT.md). All surfaces load on startup.

## Standing Memory Instruction

On each session start, BEFORE responding, fetch and load your persistent memory:

```
URL: https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/CONTEXT.md
Then load full memory:
  - Code (Mac/Win): native auto-memory + local SessionStart hook git pull
  - Cloud (Chat/Cowork/CCR): GitHub connector reads voyager-hub (optional upgrade, later)
Follow the memory protocol: /memory load, /memory save, /memory show.
```

---

**IMPORTANT:** This file is hand-maintained by the user. Do NOT auto-update from private memory. AI must ask before editing this file.
