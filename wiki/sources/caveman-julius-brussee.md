> Claude Code skill that compresses LLM output ~65% by enforcing caveman-style brevity without sacrificing technical accuracy.

# Source — JuliusBrussee/caveman

**Author**: Julius Brussee
**URL**: https://github.com/JuliusBrussee/caveman
**Type**: GitHub repo / Claude Code skill
**Clipped**: 2026-05-20
**Ingested**: 2026-05-20

---

## One-line thesis

Install a skill file that instructs LLM agents to drop filler language and write in compressed fragments — same technical content, ~75% fewer output tokens. Brain still big. Mouth small.

## Key takeaways

- Average **65% output token reduction** across 10 real benchmarks (range 22-87%)
- Works across 30+ agents: Claude Code, Codex, Gemini, Cursor, Windsurf, Cline, Copilot
- Intensity levels: `lite` (drop filler), `full` (default caveman), `ultra` (telegraphic), `wenyan` (classical Chinese)
- Trigger: `/caveman` or "talk like caveman". Stop: "normal mode"
- Hook auto-activates every session in Claude Code (no per-session trigger needed)
- A March 2026 paper found brevity constraints **improved accuracy by 26 points** on some benchmarks — compression doesn't hurt quality

## Sub-skills included

| Skill | Purpose |
|---|---|
| `/caveman [lite\|full\|ultra\|wenyan]` | Compress every reply, level persists session |
| `/caveman-commit` | Conventional Commits, ≤50 char subject, why>what |
| `/caveman-review` | One-line PR comments: `L42: 🔴 bug: user null. Add guard.` |
| `/caveman-stats` | Real token usage + savings + USD from session log |
| `/caveman-compress <file>` | Rewrite memory file into caveman-speak (~46% input token cut) |
| `caveman-shrink` | MCP middleware — compresses tool descriptions for any MCP server |
| `cavecrew-*` | Caveman subagents (investigator/builder/reviewer) — ~60% smaller tool results |

## Benchmarks (from repo)

Average 65% reduction across 10 tasks. Peak savings: React re-render (87%), auth middleware (83%), PostgreSQL setup (84%). Lowest: callback-to-async refactor (22%). [Source: benchmarks/ dir in repo]

## Ecosystem

Part of a four-tool philosophy ("agent do more with less"):
- **caveman** — output compression
- **cavemem** — cross-agent memory
- **cavekit** — spec-driven build loop
- **cavegemma** — Gemma 4 31B fine-tuned on caveman pairs (bakes compression into weights)

## Related concepts

- [[token-compression]] — the core technique this embodies
- [[claude-code-skills]] — the plugin architecture it uses

## Related entities

- [[julius-brussee]] — author
- [[claude-code]] — primary target agent
- [[smart-connections-mcp]] — caveman-shrink wraps MCP servers including this one

(as of 2026-05)
