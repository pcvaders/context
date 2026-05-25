> Investigation and fixes for Claude.ai mobile sync failures and Mac desktop issues, 2026-05-22.

# Source: Claude.ai Mobile Sync & Mac Desktop Issues (May 2026)

**Origin**: Notes from Claude.ai mobile debugging session  
**Date**: 2026-05-22  
**Status**: GitHub bridge fix verified working ✓

---

## Problem 1: Mobile Not Syncing

**Symptom**: No conversations on mobile after restart. History blank. UI always 1 day behind.

**Root causes:**
- macOS sleep/wake bug in Claude Code daemon — clock jumps treated as idle time → background sessions disappeared
- Claude.ai mobile app not reflecting recent conversations
- No hook system in Claude.ai for auto-loading context at session start

**Fix**: Update Claude Code (May 2026 release patched daemon reconnect bug). Force quit + reopen mobile app after update.

> `brew upgrade claude` — or update via desktop app

summary: "Investigation and fixes for Claude.ai mobile sync failures and Mac desktop daemon issues, 2026-05-22."
---

## Problem 2: Wiki Not Accessible from Claude.ai

See [[mcp-connector-management]] and log entry `[2026-05-22] ARCHITECTURE — GitHub bridge`.

**Solution confirmed working**: Push `wiki/index.md` + `wiki/log.md` to public GitHub → Claude.ai WebFetch raw URLs. No auth, no MCP.

---

## Problem 3: No Auto-load on Session Start

Claude.ai has no hook system. Workarounds:

| Surface | Mechanism | Notes |
|---|---|---|
| Claude.ai Projects | Project Instructions | Runs at start of every conversation in project |
| Cowork | `CLAUDE.md` in project root | Read every session automatically |
| Claude Code | Hooks system | `SessionStart` hook, most powerful |

**Pattern**: Add wiki fetch instructions to Project Instructions / CLAUDE.md so Claude.ai/Cowork auto-fetches the GitHub raw URLs each session start.

---

## Mac Desktop App — May 2026 Redesign

Major release (as of 2026-05) [unsourced — from mobile session notes, verify against release notes]:

- New session sidebar — parallel task management
- Drag-and-drop workspace layout
- Integrated terminal + file editor
- SSH support on Mac [unsourced — previously stated Linux only]
- CLI plugin parity — desktop plugins work same as terminal
- Three view modes: Verbose / Normal / Summary [unsourced]
- Usage button — shows context window + session token usage
- **Bug fixed**: background sessions disappearing after macOS sleep/wake (daemon clock jump detection)
- **Bug fixed**: daemon not exiting cleanly after `brew upgrade`

---

## Cross-links
- [[claude-code]] — entity page, update with redesign notes
- [[mcp-connector-management]] — MCP access limitations
- [[semantic-clip]] — iCloud workaround context

## Notes
Source is mobile session notes — feature claims marked [unsourced] should be verified against official release notes before treating as authoritative.
