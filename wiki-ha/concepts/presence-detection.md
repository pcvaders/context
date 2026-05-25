# Presence Detection

> Distinguishing between motion (PIR) and occupancy (presence) in Home Assistant — key to avoiding lights turning off while someone is still in the room.

## PIR vs Presence sensors

| | PIR (motion) | Presence (mmWave) |
|---|---|---|
| Detects | Movement | Static occupancy |
| False negatives | Yes — still person = no trigger | Rare |
| Cooldown | 60s+ before `off` | Near-instant |
| Aqara model | PIR sensor | FP2 |
| Sonoff model | — | SNZB-06P (5.8GHz mmWave) |
| Use case | Entry trigger | Room occupancy |
| Power requirement | Battery OK | Mains required (as of 2026-05) |

**Critical (2026-05):** mmWave/radar presence sensors (Aqara FP2, Sonoff SNZB-06P) require mains power to scan reliably. Battery-powered variants exhibit ghost detection — reporting `detected` for 60+ min after last true presence, or `unavailable` after power migration. Only deploy mains-powered presence sensors in automations.

## Problem: lights off while occupied

PIR sensors report `occupancy: off` after cooldown even if person is still. Fix options:
1. Use FP2 presence sensor as primary, PIR as secondary
2. Extend cooldown via automation `for:` condition
3. Use phone/device tracker as secondary presence signal (HA Companion app)

## iPhone presence via HA Companion

HA Companion app on iPhone 12 Pro Max provides:
- Home/away detection (zone-based)
- WiFi SSID-based presence
- BLE detection (if HA Bluetooth integration active)

Best for: whole-home away mode, not room-level presence.

## Related

- [[pir-automation]] — automation patterns using presence
- [[aqara-sensors]] — sensor hardware
- [[ha-instance]] — HA Companion app integration
