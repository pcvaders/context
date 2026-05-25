---
title: Aqara High Human Sensor — Occupancy Delay Diagnosis (Mar 2026)
summary: "Occupancy took 15 min to clear: ZHA write-back bug, parameters revert to default on re-pair. Sonoff USB-P ordered for Z2M migration. PIR automation fix: HA UI leaves stale entity refs on edit."
tags: [aqara, zigbee, zha, pir, automation, occupancy]
source-type: claude-ai-export
export-id: eec88378
conversation: "Aqara sensor occupancy delay issue"
date: 2026-03-25
---

# Aqara High Human Sensor — Occupancy Delay Diagnosis (Mar 2026)

> Source: Claude.ai export `eec88378`, conversation "Aqara sensor occupancy delay issue" (28 msgs, 2026-03-25).

## Sensor Details

**Entity**: `binary_sensor.aqara_high_human_sensor_occupancy` (GND Floor)
- Battery: 100% (CR16xx cell, healthy)
- Default detection interval: 120s
- Default sensitivity: 60s
- ZHA (not Z2M) at time of this session

## Symptom: 15-Minute Occupancy Clear Delay

**Root cause**: Default parameters set to long intervals.

**ZHA write-back problem** — when you set Zigbee `number` entity values via ZHA, the sensor doesn't reliably accept them:
- Commands dispatched but sensor shows old values on verify
- Parameters revert on re-pair or HA restart
- This is a **known ZHA quirk with Zigbee number entities** — ZHA doesn't have reliable write-back for all sensor config attributes

## Fix: Z2M Migration (Sonoff USB-P)

ZHA couldn't reliably write sensor parameters. Solution: migrate Aqara to Zigbee2MQTT:

- **Sonoff USB-E** → stays on ZHA, runs existing paired devices
- **Sonoff USB-P** (external antenna, ordered Mar 2026) → runs Z2M

ZHA and Z2M can run **side by side permanently** — each needs its own dedicated USB dongle. No conflict, no decommission required. HA treats both as separate integrations.

Z2M gives full control over sensor parameters including detection intervals, sensitivity, all config attributes that ZHA doesn't expose or won't write back.

## PIR Automation Fix — HA UI Stale Reference Bug

Session also resolved a PIR automation bug: lights stuck on because PIR sensor showing "Unknown" state.

**Critical HA gotcha**: When editing an automation via the UI, HA only updates what you explicitly touch. **Old entity references in other steps silently persist.**

Example: replaced `binary_sensor.pir_stairs_corridor` with `binary_sensor.pir_top_of_stairs_1st_floor`. After editing trigger, the condition/action steps still referenced the old entity. Automation broken.

Fix: after any sensor replacement, verify ALL steps in the automation reference the new entity — not just the step you edited.

Diagnosis command: check automation config after edit:
```yaml
# In Claude Code / ha-mcp: read automation and grep for old entity ID
```

## Interlinked Keyword Origin

In this session (Mar 2026), "Interlinked" was established as the master keyword triggering:
1. Session summary (compact, key points)
2. Updated HOME_ASSISTANT_SKILL.md output ready for download

This predates the AI LLM wiki "Interlinked" usage. The pattern originated in HA sessions.

## Links

- [[aqara-sensors]] — Aqara sensor entity list
- [[pir-automation]] — PIR automation patterns
- [[zigbee-migration]] — Sonoff USB port migration
- [[aqara-pir-setup]] — original Aqara setup session
