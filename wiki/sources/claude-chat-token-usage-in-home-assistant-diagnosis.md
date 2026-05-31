---
title: "Token usage in home assistant diagnosis"
date: "2026-04-09"
uuid: "4359ca94-6efe-4233-b18e-537b348d489a"
source: "claude-chat-export"
messages: 4
---

# Token usage in home assistant diagnosis

**Date**: 2026-04-09  
**Messages**: 2 human / 2 assistant  
**UUID**: `4359ca94-6efe-4233-b18e-537b348d489a`  

## Conversation

### **Human**

can you show me how we used up all of my tokens after just a home assistant diagnosis?

### **Claude**

I can see the concern, but I want to clarify what you're seeing. Looking at my token budget indicator, I have **190,000 tokens available** for this conversation - that's my budget for processing and responding, not something you've used up.

What likely happened is:

1. **System prompt overhead**: Every conversation with me starts with extensive background instructions (you can see hints of this in the XML tags like `<claude_info>`, `<claude_behavior>`, available tools, skills, etc.). This context takes up a significant portion of tokens before we even begin talking.

2. **Tool definitions**: All the available tools (web search, Google Drive, Canva, weather, etc.) are loaded into context with their full schemas, which consumes many tokens.

3. **Conversation history**: If you had a Home Assistant discussion, that entire conversation is being kept in context so I can reference it.

The token budget you're seeing is **mine to work with** for this session - it's not a charge to you. If we were close to exhausting this budget, I would let you know and we might need to start a fresh conversation.

**Could you share more about what made you think the tokens were "used up"?** Did you see a specific warning or limit message? That would help me understand if there's an actual issue or if this is just about the budget display.

### **Human**

Each time I asked for HA PIR light diagnostics they are used up immediately

### **Claude**

Ah, I see what's happening! When you ask for Home Assistant diagnostics, I'm likely calling the `view` tool to read skill files or configuration information, and those files can be **very large** - easily tens of thousands of tokens each.

Here's what's probably consuming tokens so quickly:

1. **Skills being loaded**: If I'm reading `/mnt/skills/` documentation files to help with Home Assistant, some of those can be 20k-50k+ tokens per file
2. **Configuration files**: Home Assistant configs can be massive if you have many devices/automations
3. **Multiple tool calls**: Each diagnostic request might trigger several `view` operations
4. **Full conversation context**: Everything from previous messages stays in memory

**To help diagnose this better, could you tell me:**
- Were you asking me to read specific Home Assistant YAML files?
- Did I call any tools like `view` multiple times?
- Was I loading skills before responding?

**A workaround**: If you need to do multiple Home Assistant diagnostics, try:
- Start a fresh conversation for each separate issue
- Ask me to focus on just one specific automation/sensor at a time
- Copy/paste just the relevant YAML snippet instead of having me read entire config files

Would you like to try another PIR light diagnostic now, and I can be more careful about which files I read?
