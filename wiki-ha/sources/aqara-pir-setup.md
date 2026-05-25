# Aqara PIR Setup Session

> 42-message session setting up Aqara motion sensors and building floor-by-floor automation in Home Assistant.

**Date**: 2026-03-25  
**Duration**: 42 messages  
**Outcome**: ✅ Ground + first floor PIR automations working

## Topics covered

- Aqara PIR pairing via Zigbee2MQTT
- Occupancy delay quirk and workaround
- First floor corridor lights automation
- Dashboard visibility for PIR states

## Key findings

Aqara PIR reports occupancy `on` immediately on motion, but holds for ~60 seconds before reporting `off`. This caused lights staying on too long. Workaround: add `for: 30s` on the `off` trigger.

## Related

- [[aqara-sensors]] — sensor entity page
- [[pir-automation]] — automation patterns
- [[zigbee]] — Zigbee stack
