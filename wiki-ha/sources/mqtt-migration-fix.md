# MQTT Migration Fix

> 14-message session recovering MQTT broker after Lenovo hardware migration caused Mosquitto to lose its configuration.

**Date**: 2026-03-31  
**Duration**: 14 messages  
**Outcome**: ✅ MQTT restored, all Zigbee entities back online

## Root cause

Hardware migration (M70Q Gen2 → M70Q I7) caused Mosquitto add-on to lose stored credentials. Zigbee2MQTT could not authenticate to broker.

## Fix steps

1. Open HA → Settings → Add-ons → Mosquitto broker
2. Check/reset Mosquitto user credentials
3. Update Zigbee2MQTT `configuration.yaml` with matching credentials:

```yaml
mqtt:
  server: mqtt://localhost
  user: <mosquitto-user>
  password: <mosquitto-password>
```

4. Restart Zigbee2MQTT add-on
5. Verify entities appear in HA

## Prevention

Before any hardware migration:
- Export Mosquitto config and credentials
- Note Zigbee2MQTT MQTT credentials
- Backup full HA config snapshot

## Related

- [[mqtt]] — MQTT concept page
- [[zigbee]] — downstream consumer of MQTT
- [[proxmox-host]] — migrated hardware
