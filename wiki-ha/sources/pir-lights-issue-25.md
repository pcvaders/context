# PIR Lights First Floor Issue Session [25]

> Session diagnosing lights staying on — wait-for-trigger was monitoring one sensor instead of all, allowing any single sensor going off to start the countdown.

**Date**: 2026-05 (approx)  
**Source**: Claude.ai conversation [25]  
**Topic**: 1st floor lights refusing to turn off

## Problem

Lights stuck ON after motion cleared. Root cause: `wait_for_trigger` was watching sensor list but starting countdown when ANY ONE sensor went `off`, not waiting for ALL sensors to be `off`.

## Fix Applied

Changed wait-for-trigger to require all three sensors off for 1 minute:

```yaml
wait_for_trigger:
  - platform: state
    entity_id:
      - binary_sensor.pir_front_door_corridor_2
      - binary_sensor.pir_top_of_stairs_1st_floor
      - binary_sensor.pir_2nd_floor_stairs
    to: "off"
    for:
      minutes: 1
```

Also corrected: lux threshold had been accidentally reset to 1000 lx during prior edit — restored to 800 lx.

## Secondary finding: Sonoff ghost detection

`binary_sensor.sonoff_snzb_06p_human_sensor_2` (Living Room) showed `detected` for 60+ minutes despite having no mains power connected. Cause: sensor retained last known state. Fix: removed from Ground Floor Automation 3. Sensor needs re-pairing when properly powered.

## Token usage discussion

This session surfaced a key insight: skill files uploaded at conversation start persist in context for the entire conversation — they are not "re-read" per message, they accumulate token cost continuously. Better pattern: use Claude Code project-level skill files accessed via `Skill` tool, not uploaded documents.

## Related

- [[pir-automation]] — diagnostic order and all-sensors-off wait pattern
- [[presence-detection]] — ghost detection / mains power requirement
- [[pir-corridor-troubleshooting-23]] — prior session, same system
