# PIR Corridor Troubleshooting Session [23]

> Session diagnosing 1st floor corridor PIR automation failure — illuminance threshold mismatch and Sonoff SNZB-06P sensor integration.

**Date**: 2026-05 (approx)  
**Source**: Claude.ai conversation [23]  
**Topic**: PIR 1st floor corridor automation not triggering or staying on too long

## Problem

Corridor lights not triggering reliably. Investigation revealed:
- Automation only checked `pir_front_door_illuminance` — not the Top of Stairs sensor
- Threshold was 1000 lx — changed to 800 lx for both sensors
- Single-sensor illuminance check caused missed triggers when approach came from stairs side

## Fix Applied

Changed illuminance condition from single-sensor to OR condition:

```yaml
condition:
  - condition: or
    conditions:
      - condition: numeric_state
        entity_id: sensor.pir_front_door_illuminance
        below: 800
      - condition: numeric_state
        entity_id: sensor.pir_top_of_stairs_1st_floor_illuminance
        below: 800
```

## Secondary work: Sonoff SNZB-06P

**Added** `binary_sensor.sonoff_snzb_06p_human_sensor_2` (Living Room) to Ground Floor Automation 3:
- Mains-powered, 5.8GHz mmWave, 15s presence timeout
- Added to: motion trigger, no-presence trigger, no-presence condition

**Old sensor flagged**: `binary_sensor.human_sensor` (SNZB-06P, Main Bedroom) — unavailable, faulty, needs ZHA removal.

Manual ZHA removal path: Settings → Devices & Services → ZHA → find device → Delete.

## Diagnostic lesson

`ha_get_automation_traces` should be first diagnostic tool before pulling history. Traces show:
- Exactly which trigger fired
- Which conditions passed/failed
- Which branch executed

Agreed protocol for all future HA sessions:
1. `ha_get_automation_traces`
2. `ha_config_get_automation`
3. `ha_get_states`
4. `ha_get_history` (narrow, only if needed)

## Related

- [[pir-automation]] — patterns and multi-sensor logic
- [[presence-detection]] — mmWave power requirement
- [[aqara-pir-setup]] — Aqara sensor configuration
