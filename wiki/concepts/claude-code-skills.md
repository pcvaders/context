> The plugin/skill system for Claude Code — markdown files that load additional behaviors, workflows, and slash commands into the agent.

# Claude Code Skills

## Definition

Claude Code skills (also called plugins in some contexts) are markdown files dropped into `~/.claude/skills/` or agent-specific directories. When invoked, the file content is loaded into the agent's context and followed as instructions. They extend Claude Code without modifying the model.

## How they work

1. Skill file installed to `~/.claude/skills/<plugin>/<SKILL.md>` (or equivalent per agent)
2. User triggers: `/skillname` or natural language ("talk like caveman")
3. Claude Code reads the skill file, follows its instructions for the session
4. Some skills use hooks to auto-activate every session (no trigger needed)

## Slash commands

Skills expose custom slash commands. Examples:
- `/caveman` — activate token compression mode
- `/caveman-commit` — generate commit message
- `/cavecrew` — decision guide for subagent delegation
- `/aillmwiki` — AI LLM wiki assistant mode

Custom slash commands live in `~/.claude/commands/*.md`. Skill slash commands may differ per implementation.

## Auto-activation

Claude Code supports hook-based auto-activation. Skills can write a flag file at session start that Claude reads, activating the skill from message one without user trigger. Used by: caveman (always-on compression), aillmwiki (session-start status check).

## Installation

```bash
# One-liner (caveman example)
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash

# Manual: drop skill file in correct dir
~/.claude/skills/<name>/SKILL.md    # Claude Code
~/.claude/commands/<name>.md        # Slash commands
```

## Notable skills (in this vault's context)

| Skill | Source | Purpose |
|---|---|---|
| caveman | [[julius-brussee]] | Output token compression |
| cavecrew | [[julius-brussee]] | Compressed subagent delegation |
| aillmwiki | voyager1 | LLM wiki assistant mode |

## Multi-agent support

Same skill file pattern extends to Codex, Gemini, Cursor, Windsurf, Cline, Copilot (30+). Install scripts detect which agents are present and place files appropriately.

## Related

- [[claude-code]], [[token-compression]], [[caveman-julius-brussee]]

(as of 2026-05)
