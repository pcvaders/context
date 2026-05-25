# PIR Automation

> Patterns for Home Assistant automations triggered by PIR motion sensors — covering trigger design, cooldown handling, multi-floor logic, and HA restart resilience.

## Deployment (voyager1, as of 2026-05)

- Ground floor — multiple PIR zones
- 1st floor corridor — 4-sensor system: `pir_light_gnd_corridor`, `pir_front_door_corridor_2`, `pir_top_of_stairs_1st_floor`, `pir_2nd_floor_stairs`
- Living room — lamp + PIR + presence combo (Sonoff SNZB-06P removed after ghost detection)

## Reliable automation pattern

Use `wait_for_trigger` with timeout instead of `delay` — survives HA restarts:

```yaml
automation:
  trigger:
    - platform: state
      entity_id: binary_sensor.pir_corridor
      to: "on"
  action:
    - service: light.turn_on
      target:
        entity_id: light.corridor
    - wait_for_trigger:
        - platform: state
          entity_id: binary_sensor.pir_corridor
          to: "off"
      timeout: "00:02:00"
      continue_on_timeout: true
    - service: light.turn_off
      target:
        entity_id: light.corridor
```

**Why `wait_for_trigger` not `delay`**: `delay` is cancelled if HA restarts mid-automation. `wait_for_trigger` resumes correctly.

## Cooldown problem

Aqara PIR sensors hold `occupancy: on` for 60s after last motion. If you need faster response, combine with presence sensor or add `for:` condition:

```yaml
trigger:
  - platform: state
    entity_id: binary_sensor.pir_corridor
    to: "off"
    for: "00:00:30"   # wait 30s of no motion before turning off
```

## Multi-sensor all-off wait (critical pattern)

**Bug pattern:** waiting for ONE sensor to go off before starting countdown — lights never turn off if other sensors still active.

Correct: wait for ALL sensors off for N seconds before turning off:

```yaml
wait_for_trigger:
  - platform: state
    entity_id:
      - binary_sensor.pir_gnd_corridor
      - binary_sensor.pir_front_door_corridor_2
      - binary_sensor.pir_top_of_stairs_1st_floor
      - binary_sensor.pir_2nd_floor_stairs
    to: "off"
    for:
      seconds: 30
```

Alternative: create a binary sensor group helper with all sensors, use group as single entity in automation — cleaner for 4+ sensors.

## Illuminance threshold (OR logic)

Check illuminance for ALL sensors in coverage area — use OR condition so either low-light reading triggers:

```yaml
condition:
  - condition: or
    conditions:
      - condition: numeric_state
          entity_id: sensor.pir_front_door_illuminance
          below: 800
      - condition: numeric_state
          entity_id: sensor.pir_top_of_stairs_illuminance
          below: 800
```

Threshold 800 lx calibrated for UK corridor (as of 2026-05). Check solar noon reading to tune.

## Multi-floor / multi-sensor AND condition

```yaml
condition:
  - condition: and
    conditions:
      - condition: state
        entity_id: binary_sensor.pir_ground
        state: "off"
      - condition: state
        entity_id: binary_sensor.pir_first_floor
        state: "off"
```

## Automation enabled state — first diagnostic check

Lights refusing to work = check automation is ENABLED before all else. Automations can be turned off silently via UI with no visible indicator in the automation trace list.

```bash
# Via ha_config_get_automation — check state: field
# Via ha_get_automation_traces — no traces after expected trigger = likely disabled
```

## Diagnostic order

1. `ha_get_automation_traces` — see exactly what fired, what condition passed/failed
2. `ha_config_get_automation` — check config is correct and state is not `off`
3. `ha_get_states` — check live sensor states
4. `ha_get_history` (narrow window) — only if traces don't tell full story

## Time window condition

Lights only trigger between sunset and 23:00:

```yaml
condition:
  - condition: sun
    after: sunset
  - condition: time
    before: "23:00:00"
```

## Related

- [[aqara-sensors]] — sensor hardware
- [[presence-detection]] — presence vs motion distinction
- [[aqara-pir-setup]] — setup session
- [[pir-corridor-troubleshooting-23]] — session 23: illuminance fix + Sonoff SNZB-06P add
- [[pir-lights-issue-25]] — session 25: all-sensors-off wait fix
- [[pir-lights-troubleshooting-26]] — session 26: 4-sensor expansion + timer fix
