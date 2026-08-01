# Buzz.app Agent Harness Config (0.5.0)

How to wire Buzz agents to external ACP backends, and the traps. Verified 2026-07-29 on Buzz v0.5.0. Full identity rotation done 2026-07-29 — all agents rebuilt post-wipe.

Live agents (post-rotation, all verified responsive):

| Agent | Harness | Model | Notes |
|---|---|---|---|
| Honey | Gemini CLI (Vertex) — custom | auto | gcloud ADC, no env vars needed |
| Fizz | OpenCode | `ollama/gpt-oss:120b-cloud` | free tier |
| Claude | Claude Code (`claude` harness) | opus | CLI subscription, no API key |
| Bumble | OpenCode | `ollama/gpt-oss:120b-cloud` | **nemotron BANNED** — see [[bumble-credential-hunt-incident]] |

Setup helper: `~/projects/Agency-Agents-AutoSkill-Loop-Engineering/scripts/setup-buzz-agents.sh`.

## What is and isn't hand-editable

State file: `~/Library/Application Support/xyz.block.buzz.app/agents/managed-agents.json`.

- **Harness selection: GUI only.** Buzz reconciles `agent_command` back to the default `buzz-agent` harness on launch, so patching that field externally is silently discarded. Use Edit agent → *Customize for this agent* → Agent harness.
- **Non-secret fields: safe to hand-edit while the agent is stopped** — `agent_args`, env var names. The GUI reads and writes the same file. Fizz was stuck double-appending `acp acp` until leftover `agent_args` were cleared this way.
- Quit Buzz (or stop the agent) before editing; the app writes from memory on exit.

## Registering a custom harness

Settings (⌘,) → Agents → *Agent runtimes* → **Add runtimes** → **Custom harness**. Fields: Name, auto-derived ID, Command (absolute path), Arguments (one row each), Env vars, Docs URL. Saved harnesses appear in the **per-agent harness dropdown**, not in the global "Ready" list.

Worked example — Gemini CLI on Vertex:
- Command `/opt/homebrew/bin/gemini`, args `--acp` and `--skip-trust`
- Env `GOOGLE_GENAI_USE_VERTEXAI=true`, `GOOGLE_CLOUD_PROJECT=cloud-vertex-gemini`, `GOOGLE_CLOUD_LOCATION=global`
- `--skip-trust` is required: a headless spawn can't answer the trusted-folder prompt.

## Critical: Channel Subscription

`buzz-acp` runs in `subscribe=Mentions` mode. **An agent with no channels logs `discovered 0 channel(s)` and sits idle forever — DMs alone are not enough.**

Fix: Agents → [agent] profile → Channels tab → Add to channel → `#general`  
"Running agents pick up new channels automatically via membership notifications" — no restart needed after adding.

All agents must be added to at least one channel post-setup or post-rotation.

## Post-Rotation Re-setup Order

After a Buzz identity rotation (Sign Out wipes all agent data and pubkeys):

1. Re-register custom harnesses via Settings → Agents → Agent runtimes → Add runtime → Custom harness (OpenCode, Gemini CLI) — they disappear on rotation.
2. Configure each agent's harness + model via GUI (agent_command is GUI-only, hand-edits are discarded).
3. Add all agents to #general via Channels tab — otherwise they sit idle.
4. Verify each agent responds to an @mention in #general.

## Gotchas

- **PATH detection:** Buzz only finds CLIs on its own PATH. `~/.opencode/bin/opencode` showed "not installed" until symlinked to `~/.local/bin/opencode`; then *Check again* flipped it to Ready.
- **Env-var UI bug:** typing `_` mid-field in the per-agent Environment-variable box sometimes inserts a blank row instead of the character. Verify every env edit in `managed-agents.json`; don't trust the displayed text.
- **New agents can't be minted headless** — each carries a nostr pubkey plus an owner-signed `auth_tag`, and only Buzz holds the owner key (keychain `buzz-desktop`). Create via GUI, or via an agent's `buzz agents draft-create` / `draft-update` tools, which land as drafts needing owner approval.
- **`requirements=2` / "setup-listener mode"** in the harness log means the agent has no provider+model resolved — it's the generic Buzz Agent harness waiting on config, not a broken binary.
- Gemini CLI free-tier OAuth is retired (`UNSUPPORTED_CLIENT`); Vertex ADC is the only path — see [[renderzero-vertex-patch]].
- **Never add `BUZZ_PRIVATE_KEY` to any agent env** — harness withholds it by design; handing it to a free-tier model caused the [[bumble-credential-hunt-incident]].
