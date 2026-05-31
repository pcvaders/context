---
title: "Integrating Claude with home assistant"
date: "2026-03-24"
uuid: "ae994a0f-b5c2-4855-b10b-304bdefc9572"
source: "claude-chat-export"
messages: 4
---

# Integrating Claude with home assistant

> **Conversation Overview**
>
> The person is exploring how to integrate Claude AI into their Home Assistant smart home setup, with a focus on using their mobile phone (iPhone 12 Pro Max with the HA Companion app). The conversation covered two main integration approaches: the official Anthropic integration built into Home Assistant (the simpler, recommended starting point) and the more advanced MCP (Model Context Protocol) server add-on approach.
>
> Claude walked through the official Anthropic integration setup process, including navigating to Settings → Devices & Services, obtaining an API key from the Anthropic portal, and configuring Claude as a voice assistant accessible via the Assist feature in the iPhone HA Companion app. Claude noted the pay-per-use cost consideration for the API.
>
> The person then revealed they are running Home Assistant on a Proxmox server, shifting the conversation toward the MCP setup path. Claude clarified it does not have live visibility into the person's Proxmox environment, but can assist if given details about their configuration. Claude asked clarifying questions about whether HA is running as a VM, LXC container, or Docker on Proxmox, and which MCP deployment approach they prefer. Claude also noted that the MCP approach would allow controlling the home directly through Claude.ai or the Claude app, bypassing the HA Assist interface entirely. The conversation ended with those questions pending, so the MCP setup has not yet been completed.
>

**Date**: 2026-03-24  
**Messages**: 2 human / 2 assistant  
**UUID**: `ae994a0f-b5c2-4855-b10b-304bdefc9572`  

## Conversation

### **Human**

So let’s see if there is any way to integrate Claude into home assistant using a mobile phone

### **Claude**

Great news — there are actually several solid options, ranging from dead simple to more advanced. Here's a breakdown tailored to your setup (iPhone 12 Pro Max with the HA Companion app):

---

## Option 1 — Official Anthropic Integration (Easiest, Recommended First)

This is built directly into Home Assistant and is the most straightforward path.

The Anthropic integration adds a conversation agent powered by Claude (e.g. Claude Sonnet) in Home Assistant. Controlling HA is done by providing Claude access to the Assist API. You can control what devices and entities it can access from the exposed entities page.

**How to set it up:**

Go to Settings → Devices & Services → Add Integration → search for Anthropic → follow the on-screen instructions. You'll need an API key from Anthropic — log into the Anthropic portal, enable billing, then visit the API Keys page to get your key.

Then to use it from your iPhone:

Go to Settings → Voice Assistants → Add Assistant, give it a name, and pick Claude as the conversation agent. You can then use it through the Assist feature in the HA Companion app on your phone.

⚠️ **Cost note:** This uses the Anthropic API which is pay-per-use. Monitor usage in the Anthropic portal — for typical home automation queries it's very cheap, but worth keeping an eye on.

---

## Option 2 — MCP Server Add-on (More Powerful)

There's a Home Assistant add-on that bridges HA with Claude via the Model Context Protocol (MCP). It provides real-time updates of smart home states via a persistent WebSocket connection, and access to over 40 distinct operations for querying states, calling services, monitoring events, and more.

This approach is more powerful but more complex to set up — better suited once you're comfortable with Option 1.

---

## What You'd Be Able to Do From Your Phone

Once set up via Option 1, through the HA Companion app on your iPhone you could:

- Ask Claude to **turn on/off specific devices** ("Turn on the Reading Lamp")
- Ask about **sensor states** ("Is anyone in the bedroom right now?")
- Ask Claude to **explain or modify automations** in plain English
- Use it as a **voice assistant** via the Assist button in the app

---

## Practical Suggestion for You

Given your setup, I'd go with **Option 1** first — it's built-in, stable, and actively maintained (it's been receiving updates in recent HA releases). Once the Anthropic integration is added and Claude is set as your Voice Assistant, you can press the Assist microphone button in your iPhone HA app and talk to Claude directly about your home.

Want help writing a good **system prompt** to give Claude context about your property layout, sensors, and automations so it can respond intelligently? That would make a big difference in how useful it is.

### **Human**

So can you see my setup with Proxmox and setting up the MCP?

### **Claude**

I don't have visibility into your Proxmox setup or any live connection to your system — I can only see what's in your Home Assistant skill document that's loaded in this project.

That said, I can absolutely **help you set up the MCP server** if you tell me a bit about your environment. A few questions to get oriented:
While you answer those — one important thing to know upfront:

The **MCP approach** for connecting Claude to HA works differently from the built-in Anthropic integration. Rather than Claude living *inside* HA, the MCP server exposes your HA to Claude (e.g. via Claude.ai or the Claude app on your iPhone) so Claude can query states and call services directly.

This means you'd potentially be able to have a conversation **right here in Claude** and control your home — including your specific sensors, automations, and devices from your skill doc — without needing the HA Assist interface at all.

Let me know your setup and we'll work through it step by step.
