---
title: "Cowork task setup with missing folders"
date: "2026-05-20"
uuid: "530c7728-37ac-48d8-b906-c99e70f094c2"
source: "claude-chat-export"
messages: 2
---

# Cowork task setup with missing folders

**Date**: 2026-05-20  
**Messages**: 1 human / 1 assistant  
**UUID**: `530c7728-37ac-48d8-b906-c99e70f094c2`  

## Conversation

### **Human**

i am trying to setup a task in cowork, to use this project and search for clippings but i cannot see any folders etc here?

### **Claude**

I see the issue — **the vault structure doesn't exist yet**. Before you set up Cowork, we need to create it.

Let me clarify a few things:

1. **Vault location**: Is `~/Documents/AIAgenticVault` the path you want to use, or do you prefer somewhere else?

2. **What are "clippings"?** Do you mean:
   - Saved articles/web pages you want to ingest into the wiki?
   - Notes or highlights from books/papers?
   - Links you've collected?

3. **What should Cowork do?** When you say "search for clippings," do you want Cowork to:
   - Monitor a specific folder for new files and notify you?
   - Help you ingest them one by one into the wiki?
   - Index them for quick lookup?

Once I know this, I can:
- **Create the folder structure** (wiki/, raw/, claude-sessions/)
- **Set up a clippings input folder** (e.g., `raw/clippings/`) where you drop things
- **Guide you through Cowork setup** to automate the ingest workflow

**Quick start**: If you want me to just create the vault now at `~/Documents/AIAgenticVault`, I can do that with bash. Confirm the path and I'll set it up, then we'll wire up Cowork.
