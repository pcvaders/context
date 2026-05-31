---
title: "Token usage analyzer"
date: "2026-05-19"
uuid: "2b0216dc-6534-469b-9e42-6c0cd3e28b45"
source: "claude-chat-export"
messages: 4
---

# Token usage analyzer

**Date**: 2026-05-19  
**Messages**: 2 human / 2 assistant  
**UUID**: `2b0216dc-6534-469b-9e42-6c0cd3e28b45`  

## Conversation

### **Human**

/token-usage-analyzer

### **Claude**

📊 Usage Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**💬 MESSAGE USAGE (RATE LIMIT)**

| | |
|---|---|
| Messages sent (this session) | **1** |
| Plan | Pro / Paid (unlimited standard messages) |
| Status | ✅ No rate limit concern |

You're on a paid plan — standard message rate limits don't apply the way they do on the free tier. (Opus-class usage has separate limits, but Sonnet is unrestricted.)

---

**⚡ TOKEN USAGE (CONTEXT WINDOW)**

No `system_warning` token marker is present in context, which means usage is well within the healthy range. Based on what's loaded:

| Component | Est. Tokens |
|---|---|
| System prompt + instructions | ~22–25k |
| userMemories | ~1.5k |
| Available skills metadata | ~1k |
| Loaded skill (token-usage-analyzer) | ~1.5k |
| Conversation so far (1 exchange) | ~0.5k |
| **Estimated total** | **~27k** |
| **Context window** | **1,000,000** |
| **Estimated remaining** | **~973k (97%)** |

---

**🎯 Status**

- **Messages**: ✅ Fresh session, no concerns
- **Context window**: ✅ Very healthy — 97%+ available
- **Recommendation**: You've got plenty of runway. Long agentic tasks, large documents, or extended back-and-forth are all fine here.

### **Human**

now how do i setup an automated task for you?

### **Claude**

There are two main paths depending on what you want to automate. Here's the breakdown:

---

## Option 1: Claude Cowork (Desktop App — No Code)

The easiest route. Scheduled tasks in Cowork let you write a prompt once, tell Claude how often to run it, and it handles the rest — hourly, daily, weekly, weekdays only, or on demand. Available for all paid plans (Pro, Max, Team, Enterprise).

**How to set it up:**
1. Install/update **Claude Desktop** (make sure it's fully up to date)
2. Open Cowork and type `/schedule`
3. Claude walks you through a few questions, usually with options to choose from — confirm, and the task is scheduled.

**Key caveat:** Scheduled tasks only run while your computer is awake and Claude Desktop is open. If your machine sleeps during the scheduled time, the task runs when you wake up.

Also worth noting: Cowork is currently macOS only — the Windows version is expected by mid-2026.

---

## Option 2: Cloud Scheduled Tasks (No Machine Required)

You can schedule tasks to run automatically by heading to `claude.ai/code/scheduled` on the web. These tasks run on Anthropic's cloud infrastructure, so they don't depend on your local machine being awake or the desktop app being open at all.

Cloud scheduled tasks work with connectors you've connected to your Claude account — things like Gmail, Slack, Notion, etc. Which is relevant to you given your Gmail connector is already hooked up.

---

## What's the difference?

| | Cowork (Desktop) | Cloud Tasks |
|---|---|---|
| Needs machine on | ✅ Yes | ❌ No |
| Local file access | ✅ Yes | ❌ No |
| Works with connectors | ✅ Yes | ✅ Yes |
| Setup | `/schedule` command | claude.ai/code/scheduled |

Given your technical background and the Gmail unsubscriber project you've been planning, cloud scheduled tasks + your Gmail connector could be a powerful combo. Want to explore a specific automation?
