# PIR First Floor Lights Troubleshooting Session [26]

> Session building the 4-sensor corridor system and diagnosing why new automation refused to work — turned out automation was simply turned off.

**Date**: 2026-05 (approx)  
**Source**: Claude.ai conversation [26]  
**Topic**: New 1st floor PIR lights automation not triggering

## 4-Sensor Corridor Coverage

Expanded coverage to 4 PIR sensors (was 3):

| Entity | Zone |
|---|---|
| `binary_sensor.pir_light_gnd_corridor` | Ground floor corridor |
| `binary_sensor.pir_front_door_corridor_2` | Front door corridor |
| `binary_sensor.pir_top_of_stairs_1st_floor` | 1st floor stairs |
| `binary_sensor.pir_2nd_floor_stairs` | 2nd floor stairs |

Group helper `binary_sensor.corridor_pir_sensors` created containing all 4 — used as single entity in automation.

## Root Cause: Automation Was Turned Off

Lights not working after automation rebuild. `ha_get_automation_traces` showed no traces after expected trigger time — confirmed automation state was `off`. Re-enabled via `ha_config_set_automation`.

**Lesson**: check automation enabled state FIRST when lights refuse to work. No error, no trace, no clue from history alone.

## Final Configuration

```yaml
trigger:
  # any of 4 PIR sensors going on
  entity_id:
    - binary_sensor.pir_light_gnd_corridor
    - binary_sensor.pir_front_door_corridor_2
    - binary_sensor.pir_top_of_stairs_1st_floor
    - binary_sensor.pir_2nd_floor_stairs
  to: "on"

condition:
  - condition: or   # either sensor below 800 lx
    conditions:
      - numeric_state entity_id: sensor.pir_front_door_illuminance below: 800
      - numeric_state entity_id: sensor.pir_top_of_stairs_illuminance below: 800

action:
  - light.turn_on
  - wait_for_trigger: all 4 sensors off for: seconds: 30
  - light.turn_off
```

Timer: **30 seconds** after all sensors clear (reduced from 60s).

## Related

- [[pir-automation]] — canonical patterns, diagnostic order
- [[pir-lights-issue-25]] — prior session, same system
- [[pir-corridor-troubleshooting-23]] — original corridor session
