> Pattern for loading persistent context at session start across Claude surfaces — Project Instructions, CLAUDE.md, hooks.

# Claude.ai Context Loading

## Problem

Claude.ai has no hook system. Each new conversation starts blank. For a wiki assistant, this means:
- No auto-fetch of wiki state
- User must paste context or re-explain every session
- Claude.ai mobile → always behind Claude Code sessions

## Solutions by surface

| Surface | Mechanism | Auto-runs | Scope |
|---|---|---|---|
| **Claude.ai Projects** | Project Instructions | ✓ every conversation | All convos in that project |
| **Cowork** | `CLAUDE.md` in project root | ✓ every session | That project |
| **Claude Code (terminal)** | `SessionStart` hook | ✓ every session | Configurable globally/project |
| **Claude Code (terminal)** | `~/.claude/CLAUDE.md` | ✓ every session | Global |

## Pattern: GitHub raw URL fetch

Embed in Project Instructions or CLAUDE.md:

```
At the start of this conversation, fetch:
https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/index.md
https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/log.md
```

Claude.ai will WebFetch these at conversation start → live wiki state loaded with no manual action.

## Pattern: Claude Code SessionStart hook

More powerful — runs shell commands, not just fetches:

```bash
# ~/.claude/hooks/session-start.sh
wiki-clip summary   # keyword search warm-up
vault index         # regenerate wiki front page
```

Configured via `~/.claude/settings.json` hooks block.

## Limitations

- Claude.ai Project Instructions: character limit applies; can't embed full wiki, only fetch pointers
- WebFetch in Project Instructions: not guaranteed to trigger on every surface (verify per Claude.ai version)
- Cowork CLAUDE.md: read at session start, but very long files hurt context efficiency

## Related

- [[claude-code]] — hooks architecture
- [[llm-wiki]] — why persistent context matters
- [[mcp-connector-management]] — why direct iCloud access isn't available on Claude.ai

(as of 2026-05)
