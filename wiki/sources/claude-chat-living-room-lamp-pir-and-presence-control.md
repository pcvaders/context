---
title: "Living room lamp PIR and presence control"
date: "2026-04-14"
uuid: "0c342e74-092e-4433-8454-7c3e93e179d2"
source: "claude-chat-export"
messages: 8
---

# Living room lamp PIR and presence control

**Date**: 2026-04-14  
**Messages**: 4 human / 4 assistant  
**UUID**: `0c342e74-092e-4433-8454-7c3e93e179d2`  

## Conversation

### **Human**

can you check the new automation: Living Room Lamp - PIR & Presence Control it did not switch the tv or lamp on when i enabled it.

### **Claude**

I'll help you troubleshoot that automation. Let me first load the Home Assistant tools and then check the automation configuration and execution history.
Now let me find your automation and check what's happening:
Good news! I've checked your automation and here's what I found:

**The automation IS working correctly!** ✅

Looking at the most recent execution trace (at 9:04 PM tonight), the automation:
1. ✅ Triggered when motion was detected on your PIR sensor
2. ✅ Checked the light level (1258 lux, below the 2550 threshold)  
3. ✅ **Successfully turned on the lamp** (`switch.double_gang_1_mums_switch_2`)
4. ✅ Checked the time (after 12:15 PM)
5. ✅ **Successfully turned on the TV** (`switch.basement_tv_mains_p`)

Both switches are currently showing as **"on"** in Home Assistant and were last changed at exactly the time the automation ran.

**However, the issue you're experiencing might be:**

1. **Physical devices not responding** - The switches in Home Assistant are turning "on", but the actual TV or lamp might not be responding because:
   - The TV might be unplugged or in standby mode
   - The lamp bulb might be off or disconnected
   - There might be a power issue with the devices

2. **"Enabling" doesn't trigger immediately** - When you enable an automation, it doesn't run the actions immediately. It only triggers when:
   - Motion is detected (PIR turns on)
   - OR it's 10:45 AM on a Sunday
   - OR no presence is detected for 2 minutes (which turns things OFF)

3. **Check if the physical devices are working** - Try manually turning them on through Home Assistant to see if they respond.

Would you like me to help you test the switches manually or investigate further?

### **Human**

Yes, as today the tv did not turn on until after 13:20 and not 12:15 and people were present

### **Claude**

Let me check the automation execution history from today to see what happened around 12:15 PM and 1:20 PM.
I found the problem! The automation **is working as designed**, but the design has a flaw for your use case. Here's what's happening:

## The Issue

**Today at 1:00 PM (13:00 local time):**
1. ✅ Motion detected → TV turned ON (correctly, after 12:15 PM)
2. ⏱️ At 1:02 PM - Motion stopped (people sitting still watching TV)
3. ❌ At 1:04 PM - Automation turned TV OFF (after 2 minutes of no motion)
4. 👤 People were still there, but not moving enough to trigger the PIR sensor

**Then at 1:19 PM:**
- Motion detected again → TV turned back ON

## The Root Cause

The automation turns **everything off** after 2 minutes of no motion, regardless of the time of day. This works fine at night, but during the day when people are watching TV, they sit still and don't trigger the motion sensor continuously.

**PIR motion sensors only detect movement** - they can't tell if someone is sitting still in a chair watching TV.

## Solutions

I can fix this with a few options:

### **Option 1: Don't turn TV off during daytime hours** (Recommended)
Only turn the TV off automatically late at night or early morning when nobody should be watching:

```yaml
- If no motion for 2 minutes AND time is before 7 AM or after 11 PM → turn TV off
- Otherwise → leave TV on
```

### **Option 2: Longer delay during daytime**
Keep a short 2-minute delay at night, but use a much longer delay (like 30 minutes) during the day.

### **Option 3: Add a separate "TV off" button/automation**
Let motion turn the TV ON automatically, but require manual turn-off or a bedtime automation.

**Which approach would you prefer?** I can update the automation right now.

### **Human**

can you add the Human Sensor Ground (24GHz mmWave human presence sensor (MTD285-ZB)) into the Automation and that should then fix the problem.

### **Claude**

Perfect solution! A mmWave presence sensor will detect people even when they're sitting still watching TV, which is exactly what you need. Let me find that sensor and add it to the automation.
Perfect! I found the presence sensor: `binary_sensor.human_sensor_ground_presence`. Now I'll update the automation to check BOTH sensors before turning things off. This way, even if the PIR doesn't detect motion (people sitting still), the presence sensor will prevent the automation from turning off the TV and lamp.
Perfect! ✅ **The automation has been successfully updated!**

## What Changed

I added the **Human Sensor Ground (mmWave presence sensor)** as an additional check before turning things off. Here's how it now works:

### Current Behavior:
1. **Turn ON** when PIR detects motion (unchanged)
   - Lamp turns on if light level is low
   - TV turns on if it's after 12:15 PM

2. **Turn OFF** - **NEW LOGIC** ⭐
   - Waits for PIR to show no motion for 2 minutes
   - **THEN checks if the presence sensor also shows no presence**
   - **Only turns off if BOTH sensors show no one is there**

### Why This Fixes Your Problem

**Before:** At 1:04 PM today, the PIR didn't detect motion for 2 minutes (people sitting still watching TV) → TV turned off

**Now:** Even if the PIR doesn't detect motion, the mmWave presence sensor will still detect people sitting on the couch → TV stays on! 

The mmWave sensor detects presence even when people aren't moving, so the automation won't turn off the TV/lamp while someone is still in the room watching.

**The automation is ready to test** - next time someone is watching TV and sitting still, the presence sensor should keep everything on! 🎉

### **Human**

Okay the New Human Sensor and the TV are working, but the light came on this morning and then has stayed off even now when its well below the lx, can you diagnose and repair

### **Claude**

I'll diagnose the lamp issue. Let me check the current states and recent automation activity.
**Found the problem!** 

Looking at the automation trace from 3:59 PM (15:59 UTC):

## What Happened

1. ✅ Motion was detected → Automation triggered
2. ❌ **Lux was 2846** (ABOVE the 2550 threshold) → **Lamp didn't turn on**
3. ✅ TV turned on (correctly, as it was after 12:15 PM)

## The Current Situation

**Right now:**
- Lux is **1438** (well below 2550 - lamp SHOULD be on) ✅
- PIR is **"on"** (still detecting presence) ✅
- Presence sensor is **"on"** ✅
- Lamp is **OFF** ❌

## The Root Cause

**The automation only checks lux when motion is NEWLY detected** (when PIR changes from "off" to "on"). 

Here's the sequence:
1. At 3:59 PM - Motion detected, but it was still bright outside (lux 2846) → Lamp stayed off
2. Later - Sun set, lux dropped to 1438 (dark enough for lamp)
3. **But the PIR has been continuously "on"** since 3:59 PM (people present)
4. **No new motion trigger** = automation doesn't re-check the lux level

## The Fix

I need to add a **lux-based trigger** so the lamp turns on automatically when it gets dark enough, even if motion was already detected earlier:
Perfect! ✅ **The automation has been fixed!** Now let me turn on the lamp manually since you're currently in the dark:
## ✅ **Fixed and Lamp is Now ON!**

### What Was Wrong

**The Problem:** The automation only checked the light level (lux) when **NEW motion** was detected. Here's what happened today:

1. **3:59 PM** - Motion detected, but lux was **2846** (still bright outside) → Lamp stayed off ✓
2. **Later** - Sun set, lux dropped to **1438** (dark enough for lamp)
3. **But** - People were already present, so PIR stayed continuously "on"
4. **No new motion trigger** → Automation never rechecked the lux → **Lamp stayed off** ❌

### The Fix - Added Lux-Based Trigger

I added a **4th trigger** that monitors the light sensor:

**New Trigger:**
- **When lux drops below 2000** (it gets dark enough)
- **AND** someone is present (PIR or mmWave sensor detects presence)
- **Then** turn on the lamp automatically

### How It Works Now

**4 Ways the Automation Can Trigger:**

1. **Motion detected** → Check lux, turn on lamp if dark enough
2. **Gets dark** (lux drops below 2000) → Check if anyone present, turn on lamp ✅ **NEW**
3. **No presence for 2 min** → Turn off lamp AND TV (only if both sensors show no one)
4. **Sunday 10:45 AM** → Turn on TV

### What This Fixes

- ✅ Lamp will now turn on automatically when it gets dark, even if motion was detected earlier when it was still bright
- ✅ Lamp will still turn on when motion is detected (if dark enough)
- ✅ Lamp won't turn off while people are sitting still (thanks to mmWave sensor)

The lamp should work perfectly now! 🎉
