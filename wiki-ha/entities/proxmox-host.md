# Proxmox Host

> Lenovo M70Q Tiny I7 running Proxmox — hosts the Home Assistant VM and associated services.

**Hardware**: Lenovo M70Q Tiny I7  
**Previous**: Lenovo M70Q Tiny Gen2 (storage migrated)  
**Hypervisor**: Proxmox VE

## Migration history

NVMe (OS) and SSD (data) migrated from M70Q Gen2 to M70Q I7. Migration caused two downstream issues:
1. MQTT broker lost config → fixed via [[mqtt-migration-fix]]
2. Sonoff Zigbee USB dongle changed port mapping → fixed via [[zigbee-migration]]

## Related

- [[ha-instance]] — VM running on this host
- [[zigbee-migration]] — USB port issue post-migration
- [[mqtt-migration-fix]] — MQTT issue post-migration
