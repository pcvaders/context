# Agent-Native CLI Design

> Design pattern for CLI tools optimised for LLM agent consumption — auto-JSON output, typed exit codes, --compact mode, stdin piping, and local SQLite persistence.

## The problem

Standard CLIs are designed for humans: coloured output, interactive prompts, prose error messages. When an LLM agent calls a CLI, these patterns waste tokens and break parsing.

## Agent-native conventions

### Output

| Pattern | How |
|---|---|
| Auto-JSON when piped | `if !isatty(stdout) { outputJSON() }` — no `--json` flag needed |
| `--compact` flag | Strips verbose fields, 60-80% token reduction |
| `--select fields` | Output only requested fields |
| `--csv` | Structured tabular output |
| `--no-input` | Fail fast instead of interactive prompt |

### Exit codes (typed)

| Code | Meaning |
|---|---|
| `0` | Success |
| `2` | Usage error (bad flags/args) |
| `3` | Not found |
| `4` | Auth failure |
| `5` | API/upstream error |
| `7` | Rate limited |

Agent can branch on exit code without parsing stderr.

### Exploration

- `--dry-run` — show what would happen without side effects
- `--stdin` — accept piped JSON/IDs as input
- Subcommands discoverable via `--help`

## Five rungs of quality

CLI Printing Press uses a 5-rung creativity ladder:

| Rung | Feature |
|---|---|
| 1-2 | API wrapper + output formatting |
| 3 | Local SQLite persistence + FTS5 search |
| 4 | Domain analytics (stale issues, orphans, leaderboards) |
| 5 | Behavioural insights (health scores, duplicates, trends) |

Rung 3+ enables **offline queries** — agent can query local cache at 50ms vs 200-500ms API round-trip.

## NOI — Non-Obvious Insight

Every API has a hidden purpose beyond its intended use. Identifying the NOI shapes which commands get built:

> "Linear isn't just an issue tracker. It's a team behavior observatory."  
> "Spotify isn't just a music player. It's a taste-graph time machine."

NOI drives Rung 4-5 feature design — the commands humans wouldn't think to build.

## Related

- [[cli-printing-press]] — tool that generates agent-native CLIs
- [[token-compression]] — complementary approach (compress LLM output)
- [[ai-cost-observability]] — measuring token cost of CLI interactions
- [[mcp]] — alternative/complement: MCP servers vs CLI binaries for agent tool use
