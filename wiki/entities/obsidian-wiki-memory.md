> Claude Code skill that loads the AI LLM Wiki vault context into any session at startup via smart-clip search.

## obsidian-wiki-memory

**Type:** Claude Code skill (`~/.claude/skills/obsidian-wiki-memory.md`)
**Plugin:** User-defined (PCGamesplay1/Claude-skills)
**Appears in:** Skill list as `obsidian-wiki-memory`

## What it does

When invoked, loads relevant vault context into the active Claude Code session:
- Fetches `wiki/index.md` and `wiki/log.md` for orientation
- Enables `/memory load`, `/memory save`, `/memory show` commands
- Bridges Claude Code sessions to the persistent Obsidian AI LLM Wiki

Part of the unified memory system (Plan 2, 2026-05-30): local auto-memory + vault + voyager-hub private repo.

## Usage

```
/skill obsidian-wiki-memory
```

Or invoked via SessionStart hook automatically.

## Related

- [[interlinked]] — the wiki maintenance skill (ingest/lint/query)
- [[llm-wiki]] — the vault it loads
- [[claude-code-skills]] — the skill ecosystem

## Log

- 2026-05-22: skill created, noted as open item in wiki log
- 2026-05-30: unified memory system built around it (Plan 2)
