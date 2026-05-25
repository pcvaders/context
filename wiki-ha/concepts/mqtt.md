# MQTT

> Mosquitto MQTT broker running on Proxmox — message bus between Zigbee2MQTT and Home Assistant; required reconfiguration after hardware migration.

**Broker**: Mosquitto  
**Host**: Proxmox (same machine as HA)  
**Port**: 1883 (local), 8883 (TLS)

## Role in stack

```
Zigbee2MQTT → MQTT topics → Mosquitto → HA MQTT integration → entities
```

All Zigbee device state flows through MQTT. Loss of broker = loss of all Zigbee devices in HA.

## Migration fix (Lenovo M70Q Gen2 → I7)

After hardware migration, MQTT broker lost config. Symptoms:
- All Zigbee entities unavailable in HA
- Zigbee2MQTT logs showing connection refused to broker
- HA MQTT integration showing disconnected

Fix checklist:
1. Verify Mosquitto add-on is running in HA
2. Check Mosquitto config — credentials may have reset
3. Verify Zigbee2MQTT `configuration.yaml` has correct broker host/port/credentials
4. Restart Z2M after fixing credentials

## Related

- [[zigbee]] — primary MQTT consumer
- [[mqtt-migration-fix]] — migration session source
- [[ha-instance]] — host system
