> Anthropic's agentic coding tool — one of the recommended LLM writers for this wiki pattern.

# Claude Code

## What it is

Claude Code is Anthropic's command-line agentic coding tool. It runs in the terminal (and VS Code), reads and writes files directly, executes bash commands, and operates with a high degree of autonomy on multi-step tasks.

## Role in LLM Wiki

In [[karpathy-andrej]]'s pattern, Claude Code is the recommended "programmer" that writes and maintains the wiki layer. It can:

- Read source files from `raw/`
- Create and update markdown pages across the vault
- Run lint checks across the full wiki
- Execute multi-step ingest workflows autonomously

## Relationship to this project

This vault is currently being maintained via **Claude.ai Projects** (chat interface) rather than Claude Code directly. Claude.ai Projects use Project Instructions as the schema (equivalent to CLAUDE.md in Claude Code). Both approaches follow the same LLM Wiki pattern.

Claude Code becomes more relevant when:
- Connecting to Obsidian vault via [[semantic-clip]] CLI (replaces smart-connections-mcp — DEPRECATED 2026-05-22)
- Running autonomous Cowork dispatch workflows
- Bulk ingesting many sources in one session

## Cowork dispatch integration

Claude Code + Cowork dispatch is the planned automation layer for this vault. The `log.md` + `dispatch-state.md` pattern ensures dispatch can resume mid-workflow without relying on Claude's memory persistence.

See project instructions for dispatch continuity design.

## Skills and plugins

Claude Code's skill system extends agent behavior via markdown files in `~/.claude/skills/` and `~/.claude/commands/`. See [[claude-code-skills]] for full architecture.

Notable skills active in this environment:
- **caveman** ([[julius-brussee]]) — ~65% output token compression, auto-activates every session via hook
- **cavecrew** — compressed subagent delegation (investigator/builder/reviewer)
- **aillmwiki** — this wiki's assistant mode (voyager1 custom)

## Desktop App — May 2026 redesign

Major release (as of 2026-05) per [[claude-mobile-sync-issues-2026-05]]:
- Session sidebar for parallel task management
- Drag-and-drop workspace layout
- Integrated terminal + file editor  
- Three view modes: Verbose / Normal / Summary [unsourced — verify against release notes before treating as authoritative]
- Usage button showing context window + session token usage
- CLI plugin parity — desktop plugins work same as terminal

## Daemon bugs fixed (May 2026)

- **Sleep/wake bug**: macOS clock jumps were treated as elapsed idle time → background sessions disappeared. Now detects clock jumps correctly.
- **brew upgrade cleanup**: daemon was not exiting cleanly after `brew upgrade`. Fixed.

Fix: `brew upgrade claude` or update via desktop app.

## Version note

Running in VS Code as of 2026-05. [unsourced — user to confirm version]

## Related

- [[llm-wiki]], [[karpathy-andrej]], [[obsidian]], [[claude-code-skills]], [[token-compression]], [[skill-ecosystem]], [[claude-ai-context-loading]]

(as of 2026-05)
