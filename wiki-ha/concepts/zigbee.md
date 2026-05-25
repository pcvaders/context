# Zigbee

> Low-power mesh radio protocol for smart home devices — implemented in HA via Zigbee2MQTT (primary) and ZHA, using a Sonoff USB coordinator dongle.

## Stack in use

```
Aqara/other Zigbee devices
  ↔ Sonoff Zigbee USB dongle (coordinator)
    ↔ Zigbee2MQTT (bridge software)
      ↔ Mosquitto MQTT broker
        ↔ Home Assistant
```

ZHA also configured as secondary integration.

## Zigbee2MQTT vs ZHA

| | Zigbee2MQTT | ZHA |
|---|---|---|
| Config | External (YAML + MQTT) | Built into HA |
| Device support | Broader, faster updates | Native HA integration |
| Flexibility | Higher | Simpler |

## Critical: USB port persistence

After hardware migration, `/dev/ttyUSBx` paths change. Always use:

```yaml
serial:
  port: /dev/serial/by-id/usb-ITead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_<serial>-if00-port0
```

Never use `/dev/ttyUSB0` — breaks on reboot or hardware change.

## Device pairing

Aqara sensors: hold reset until LED flashes blue 3×, then Z2M detects within 60s.

## Related

- [[sonoff-zigbee-dongle]] — coordinator hardware
- [[mqtt]] — transport layer
- [[zigbee-migration]] — migration troubleshooting
- [[aqara-sensors]] — devices on the network
