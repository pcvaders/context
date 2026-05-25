# Sonoff Zigbee Dongle

> Sonoff Zigbee USB coordinator used with Zigbee2MQTT — required USB port remapping after Proxmox host hardware migration.

**Model**: Sonoff Zigbee 3.0 USB Dongle Plus  
**Protocol**: Zigbee coordinator  
**Integration**: Zigbee2MQTT (primary), ZHA (secondary)

## Port mapping issue after migration

When NVMe/SSD migrated from Lenovo M70Q Gen2 to M70Q I7, the USB port mapping changed. Zigbee2MQTT lost its serial device because `/dev/ttyUSB0` became `/dev/ttyUSB1` (or similar).

**Fix**: Use persistent USB device path by serial ID instead of `/dev/ttyUSBx`.

```yaml
# zigbee2mqtt configuration.yaml
serial:
  port: /dev/serial/by-id/usb-ITead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_<serial>-if00-port0
```

Find the ID with:
```bash
ls /dev/serial/by-id/
```

This path persists across reboots and hardware changes regardless of which USB port the dongle is plugged into.

## Related

- [[zigbee]] — Zigbee stack overview
- [[zigbee-migration]] — 109-msg troubleshooting session
- [[ha-instance]] — host HA installation
