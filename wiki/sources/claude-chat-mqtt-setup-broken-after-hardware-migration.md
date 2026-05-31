---
title: "MQTT setup broken after hardware migration"
date: "2026-03-31"
uuid: "0bdfc087-65fb-43fb-b021-680c51532a25"
source: "claude-chat-export"
messages: 14
---

# MQTT setup broken after hardware migration

> **Conversation Overview**
>
> The person migrated an NVMe and SSD from a Lenovo M70Q Tiny Gen2 into a Lenovo M70Q Tiny I7 and encountered issues with their Home Assistant MQTT setup afterward. The core problem turned out to be that the Sonoff Zigbee 3.0 USB Dongle Plus V2 was no longer being recognized by Zigbee2MQTT after the hardware swap, as the device path had changed from its previous assignment to `/dev/ttyUSB1`.
>
> Claude walked through diagnosing the issue by checking `/dev/serial/by-id/` for the dongle, and the person confirmed it was visible in the HA Hardware list with the full ID path: `/dev/serial/by-id/usb-Itead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_V2_6024afc48fc2ef11a6eac6138148b910-if00-port0`. The recommended fix was to update the Zigbee2MQTT add-on configuration to use this stable by-id path rather than the volatile `ttyUSBx` assignment, preventing recurrence after future reboots. The conversation ended before confirmation that the fix resolved the issue. The person also noted that a direct MCP link Claude had was broken during the session, meaning Claude could not access the HA instance directly and relied on the person providing device information manually.
>

**Date**: 2026-03-31  
**Messages**: 8 human / 6 assistant  
**UUID**: `0bdfc087-65fb-43fb-b021-680c51532a25`  

## Conversation

### **Human**

So I moved the NVME and SSD from the M70Q TIny Gen2 into a M70Q Tiny I7 and now things seem a bit broken especially the MQTT setup

### **Claude**

Let me help you troubleshoot the drive migration issues. Moving drives between different hardware generations can cause several problems.

What's broken with the MQTT setup specifically? A few things to check:
While you answer those — the most common issues after a hardware swap like this are:

**Network/IP related** — The new machine likely got a different MAC address, so if your router assigns IPs by MAC, the machine now has a different IP. Any MQTT clients hardcoded to the old IP will fail to connect.

**Driver issues** — The Gen2 vs the I7 variant may have different chipsets (especially network and storage controllers). If the OS booted but with missing/wrong drivers, network interfaces may be named differently (e.g. `enp3s0` → `enp2s0`).

**Hardware ID changes** — Things like SSL certificates or license-bound configs tied to machine identifiers (hostname, MAC, etc.) may have broken.

**Service not starting** — If the broker service depends on a network interface that's now named differently, it may fail silently at boot.

What does the MQTT broker log say when you try to start it?

### **Human**

Q: What symptoms are you seeing with MQTT? (Select all that apply)
A: Sonoff USB -P not showing up now

Q: What OS / MQTT broker are you running?
A: Home Assistant (Mosquitto add-on)

### **Claude**

Ah, so the real issue is the **Sonoff Zigbee USB dongle not being recognized** — MQTT itself is probably fine, it's just that the Zigbee integration has lost its device.

This is a classic USB device path change after a hardware migration. Here's what's likely happening and how to fix it:

---

**The Problem**

The Sonoff Zigbee USB dongle (Sonoff Zigbee 3.0 USB Dongle Plus) was previously mapped to something like `/dev/ttyUSB0` or `/dev/ttyACM0`, but on the new hardware it may be on a different path — or the serial port isn't being passed through correctly to the HA add-on.

---

**Step-by-step fix**

**1. Check if the OS even sees the dongle**

[REDACTED:ssh_uri] into your Home Assistant host and run:
```bash
ls /dev/serial/by-id/
```
You should see something like:
```
usb-ITead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_...
```
If nothing shows up, the OS isn't detecting it at all — try a different USB port, preferably USB 2.0 (the dongle can be finicky on USB 3.0).

**2. If it shows up there, update the device path in Zigbee2MQTT**

In your `zigbee2mqtt` configuration (usually at `/config/zigbee2mqtt/configuration.yaml`), check the serial section:
```yaml
serial:
  port: /dev/ttyUSB0
```
Change it to use the stable by-id path instead:
```yaml
serial:
  port: /dev/serial/by-id/usb-ITead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_XXXX
```
This survives reboots and hardware changes much better than `ttyUSB0`.

**3. Check the Zigbee2MQTT add-on config in HA**

Go to **Settings → Add-ons → Zigbee2MQTT → Configuration** and make sure the serial port listed there matches what you found in step 1.

---

**Quick question** — are you running Zigbee2MQTT as the add-on, or are you using the built-in ZHA integration? That'll affect exactly where to make the fix.

### **Human**

are you still connecteed?

### **Human**

are you still connecteed?

### **Human**

are you still connecteed?

### **Claude**

Yes, still here! Did you get a chance to check if the dongle shows up with that `ls /dev/serial/by-id/` command?

### **Human**

I meant connected to HA, so you can check

### **Claude**

I don't have a direct connection to your Home Assistant instance — I can only see what you share with me in the chat. I'm not able to [REDACTED:ssh_uri] in or access your HA dashboard directly.

To help you troubleshoot, you'd need to paste the output of commands or logs here. The quickest things to grab would be:

1. **[REDACTED:ssh_uri] into HA host and run:**
   ```bash
   ls /dev/serial/by-id/
   ```

2. **Or from the HA UI:** Settings → System → Hardware → and look for any serial/USB devices listed there.

Paste whatever you see and we'll go from there!

### **Human**

Okay so now your direct mcp link is also broken. Its there in the Hardware list: `/dev/ttyUSB1`
ID: `/dev/serial/by-id/usb-Itead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_V2_6024afc48fc2ef11a6eac6138148b910-if00-port0`

### **Claude**

Great, the dongle is detected! The issue is it's now on `ttyUSB1` instead of whatever it was before (probably `ttyUSB0`).

**Fix it now:**

Go to your Zigbee2MQTT add-on configuration and update the serial port to use the stable by-id path:

```yaml
serial:
  port: /dev/serial/by-id/usb-Itead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_V2_6024afc48fc2ef11a6eac6138148b910-if00-port0
```

Using the full by-id path instead of `ttyUSB1` means it won't break again if the port number changes on the next reboot.

**To do this in HA:**
1. Go to **Settings → Add-ons → Zigbee2MQTT**
2. Click the **Configuration** tab
3. Find the `serial` → `port` field and paste that full path in
4. Save and restart the add-on

Once it restarts, your Zigbee devices should come back online and MQTT messages should start flowing again. Let me know what you see in the logs after the restart!

### **Human**

quickly summarise this chat

### **Claude**

You migrated the NVMe and SSD from a **Lenovo M70Q Tiny Gen2** to an **M70Q Tiny I7**, which caused your **Sonoff Zigbee USB dongle** to stop being recognised — breaking your Zigbee2MQTT/MQTT setup in Home Assistant.

**Fix:** The dongle moved from `ttyUSB0` to `ttyUSB1`, so the solution is to update the serial port in Zigbee2MQTT to use the stable by-id path:
```
/dev/serial/by-id/usb-Itead_Sonoff_Zigbee_3.0_USB_Dongle_Plus_V2_6024afc48fc2ef11a6eac6138148b910-if00-port0
```

Still waiting to hear if the add-on restart fixed it!
