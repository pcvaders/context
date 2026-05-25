# Zigbee Migration Troubleshooting

> 109-message session recovering Zigbee2MQTT and ZHA after NVMe/SSD storage migration from Lenovo M70Q Gen2 to M70Q I7.

**Date**: 2026-04-01  
**Duration**: 109 messages  
**Outcome**: ✅ Zigbee fully recovered

## Root cause

USB device paths (`/dev/ttyUSBx`) are assigned dynamically. After hardware migration, the Sonoff Zigbee dongle was assigned a different port number. Zigbee2MQTT config pointed to old path → coordinator not found → all Zigbee entities unavailable.

## Fix

Replace dynamic path with persistent serial-by-id path:

```yaml
# zigbee2mqtt/configuration.yaml
serial:
  port: /dev/serial/by-id/usb-ITead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_<serial>-if00-port0
```

Find available serial IDs:
```bash
ls /dev/serial/by-id/
```

## Diagnostic steps used

1. Check if dongle visible: `ls /dev/ttyUSB*`
2. Check Zigbee2MQTT logs in HA add-on
3. Test port directly: `minicom -D /dev/ttyUSB0 -b 115200`
4. Cross-check ZHA for same port conflict (Z2M and ZHA cannot share coordinator)

## Lessons

- Always use `/dev/serial/by-id/` paths for USB devices in HA/Z2M
- Never run both Z2M and ZHA on same coordinator — port conflict
- After migration: check all add-ons with USB device access (Z2M, ZHA, Bluetooth)

## Related

- [[sonoff-zigbee-dongle]] — the hardware
- [[zigbee]] — Zigbee stack
- [[proxmox-host]] — hardware that was migrated
