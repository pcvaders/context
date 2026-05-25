> Tools and practices for measuring, attributing, and optimizing token spend across AI coding agents.

# AI Cost Observability

## Definition

AI cost observability is the practice of instrumenting LLM agent workflows to surface where tokens are consumed, what tasks they're spent on, and whether the spend was productive. Analogous to APM (application performance monitoring) for traditional software.

## Why it matters

- AI coding tool costs compound quickly across sessions, projects, models, and agents
- Spend is invisible without tooling — no built-in breakdown of "how much did that feature cost?"
- Waste patterns (re-reading files, retry loops, unused MCPs, bloated CLAUDE.md) are only detectable retrospectively
- Model choice has large cost impact; observability enables empirical comparison

## Key metrics

| Metric | What it shows |
|---|---|
| Cost per session | Overall spend, comparable across projects |
| Cache hit rate | Context stability; < 80% suggests config issues |
| One-shot rate | % of edits succeeding without retry; proxy for model effectiveness |
| Task category breakdown | Where tokens actually go (coding vs exploring vs conversation) |
| Yield | Correlation of sessions with landed commits — productive vs abandoned spend |

## Tooling (as of 2026-05)

| Tool | Coverage | Storage |
|---|---|---|
| [[codeburn-getagentseal|codeburn]] | 19+ agents | Local JSONL/SQLite reads, no proxy |
| `caveman-stats` (sub-skill of [[caveman-julius-brussee|caveman]]) | Claude Code only | Session log |


## Optimize patterns (from codeburn)

Common waste signals and fixes:

- **Low Read:Edit ratio** → agent editing without reading, causes retries → add context explicitly
- **Uncapped bash output** → set `BASH_MAX_OUTPUT_LENGTH` → cuts context waste
- **Unused MCP servers** → each pays tool-schema overhead every session → prune unused
- **Bloated CLAUDE.md** → compress with `caveman-compress` (see [[token-compression]])
- **Ghost skills/commands** → defined but never invoked → archive to reduce load
- **Files re-read across sessions** → consolidate into CLAUDE.md or project context

## Relationship to token compression

Observability and compression are complementary:
- **[[token-compression]]** reduces tokens spent (proactive)
- **AI cost observability** measures tokens spent and finds waste (retrospective)

Run `codeburn optimize` to find waste → fix with `caveman-compress`, config tweaks → re-measure.

## Related

- [[token-compression]], [[codeburn-getagentseal]], [[claude-code]], [[claude-code-skills]]

(as of 2026-05)
