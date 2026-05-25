# Aqara Sensors

> Aqara PIR motion and presence sensors deployed across voyager1's home — used for floor-by-floor automation triggers in Home Assistant.

**Brand**: Aqara  
**Protocol**: Zigbee (via Zigbee2MQTT)  
**Deployment**: Ground floor, first floor corridor, living room (as of 2026-05)

## Sensor types in use

| Sensor | Type | Known issue |
|---|---|---|
| Aqara PIR | Motion (binary) | Occupancy delay — stays `on` for 60s+ after motion stops |
| Aqara presence | FP2 mmWave presence | More accurate, no cooldown delay |

## Known quirks

**Occupancy delay**: Standard Aqara PIR sensors have a built-in cooldown before reporting `occupancy: false`. Workaround: use presence sensors or adjust automation trigger to `state` not `device_tracker`.

**Setup gotcha**: Sensors must be paired with Zigbee2MQTT coordinator in pairing mode — hold reset button until LED flashes blue 3×.

## Automation patterns

- **PIR → lights on**: trigger on `occupancy: true`, condition checks time window
- **No motion → lights off**: use `wait_for_trigger` with timeout rather than `delay` (survives HA restart)
- **Multi-sensor AND**: combine ground + first floor PIR in single automation via condition group

## Related

- [[pir-automation]] — automation patterns
- [[presence-detection]] — occupancy vs motion concepts
- [[zigbee]] — Zigbee stack they run on
- [[aqara-pir-setup]] — setup session source
