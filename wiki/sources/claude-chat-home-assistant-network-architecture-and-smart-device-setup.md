---
title: "Home Assistant network architecture and smart device setup"
date: "2026-02-24"
uuid: "abfc110f-4ea7-464c-993d-c454e53756b2"
source: "claude-chat-export"
messages: 6
---

# Home Assistant network architecture and smart device setup

**Date**: 2026-02-24  
**Messages**: 4 human / 2 assistant  
**UUID**: `abfc110f-4ea7-464c-993d-c454e53756b2`  

## Conversation

### **Human**

can you draw me a complete network of how a Homeassistant server would work with recommended smart switches, hubs, extensions etc

### **Claude**

Here's your interactive Home Assistant network diagram! **Hover over any node** to get detailed info and product recommendations.

The diagram covers the full recommended ecosystem:

**Core infrastructure** — Router (UniFi/TP-Link), HA Server (Raspberry Pi 5/NUC), MQTT Broker (Mosquitto add-on), and optional NAS for backups/Frigate NVR.

**Protocols & hubs:**
- **Zigbee** via Sonoff USB dongle + ZHA/Zigbee2MQTT — best for bulbs, sensors, switches
- **Z-Wave 800** via Zooz stick — best for locks, in-wall dimmers, reliable through walls
- **Matter/Thread** via HomePod mini or Nest Hub Max as border router — future-proof, no hub lock-in
- **WiFi/ESPHome** — Shelly devices and DIY ESP32 sensors, all fully local

**End devices** span smart bulbs, motion sensors, door sensors, in-wall switches/dimmers, smart locks, thermostats, plugs with energy monitoring, and Matter devices.

**Cloud** is entirely optional — Nabu Casa ($65/yr) for remote access, or keep everything 100% local.

### **Human**

Great, I have a human presence sensor that I want to setup for lights and power but I want to setup an automation for it and use a PIR sensor to also confirm a presence, how can i do this?

### **Claude**

Great use case! Combining a **human presence sensor** (mmWave radar, like Aqara FP2 or LD2410) with a **PIR sensor** gives you the best of both worlds:

- **mmWave** = detects stationary presence (sitting, sleeping) but can have false positives
- **PIR** = confirms movement, very reliable trigger, eliminates false positives

Here are a few automation strategies depending on your goal:

---

**Strategy 1 — AND Logic (both must agree)**
Best for: Lights that should only turn on when someone is *definitely* there.

```yaml
trigger:
  - platform: state
    entity_id: binary_sensor.pir_sensor
    to: "on"
condition:
  - condition: state
    entity_id: binary_sensor.presence_sensor
    state: "on"
action:
  - service: light.turn_on
    target:
      entity_id: light.room_lights
```
PIR triggers → presence sensor must also confirm → lights on. Reduces false positives significantly.

---

**Strategy 2 — OR for ON, AND for OFF (recommended)**
Best for: Lights that turn on quickly, but only turn off when *both* agree nobody is there.

```yaml
# TURN ON - either sensor triggers
trigger:
  - platform: state
    entity_id:
      - binary_sensor.pir_sensor
      - binary_sensor.presence_sensor
    to: "on"
action:
  - service: light.turn_on
    target:
      entity_id: light.room_lights

# TURN OFF - both must be clear + timeout
trigger:
  - platform: state
    entity_id: binary_sensor.presence_sensor
    to: "off"
    for:
      minutes: 2
condition:
  - condition: state
    entity_id: binary_sensor.pir_sensor
    state: "off"
action:
  - service: light.turn_off
    target:
      entity_id: light.room_lights
```

---

**Strategy 3 — Helper-based with input_boolean (most robust)**
Use a virtual `input_boolean.room_occupied` that both sensors feed into, then your light/power automations just watch that single helper. This is the cleanest approach for multiple devices in the same room.

```yaml
# Set occupied when either fires
trigger:
  - platform: state
    entity_id:
      - binary_sensor.pir_sensor
      - binary_sensor.presence_sensor
    to: "on"
action:
  - service: input_boolean.turn_on
    entity_id: input_boolean.room_occupied

# Clear only when BOTH are off for 5 minutes
trigger:
  - platform: template
    value_template: >
      {{ is_state('binary_sensor.pir_sensor', 'off') and
         is_state('binary_sensor.presence_sensor', 'off') }}
    for:
      minutes: 5
action:
  - service: input_boolean.turn_off
    entity_id: input_boolean.room_occupied
```

Then all your lights and smart plugs just automate off `input_boolean.room_occupied`.

---

**My recommendation for you:** Use **Strategy 3** — it scales well if you add more devices later (a TV, a fan, a desk lamp) and you only have one place to tune the timeout. Would you like me to build out the full automation YAML including the smart plug/power switching as well, or set it up for a specific room?

### **Human**

i am just trying to work out how to enable claude in home assistant, so its easier for you

### **Human**

okay so how do I use this code in Home Assistant?
