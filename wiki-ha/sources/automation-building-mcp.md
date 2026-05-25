# Automation Building via MCP

> 207-message extended session building Home Assistant automations via Claude Desktop MCP tools in Extended Mode — ground floor + first floor PIR, presence detection, living room lamp.

**Date**: 2026-03-23  
**Duration**: 207 messages  
**Mode**: Claude Desktop + ha-mcp in Extended Mode  
**Outcome**: Multi-floor PIR automation suite built

## What was built

- Ground floor PIR automation suite
- First floor corridor lights (PIR-triggered)
- Living room lamp + PIR + presence combo
- Dashboard cards for automation control

## MCP-driven automation workflow

Claude used ha-mcp tools to:
1. Read existing entity states and automation configs
2. Draft automations in YAML
3. Call HA service to create/update automations via API
4. Verify by reading back entity states

This is the core ha-mcp value: **natural language → working automations** without touching HA UI.

## Patterns established

See [[pir-automation]] for extracted patterns.

Key automation approaches:
- `wait_for_trigger` for restart-resilient cooldown
- Time window conditions (sunset-based)
- Multi-sensor AND conditions across floors

## Multi-session continuity

At 207 messages, session ran into context limits. Patterns:
- Claude summarised automation state before context window full
- New session resumed using `HOME_ASSISTANT_SKILL.md` as context injection

## Related

- [[ha-mcp]] — tool used
- [[pir-automation]] — patterns extracted
- [[aqara-sensors]] — sensors automated
- [[ha-instance]] — target system
