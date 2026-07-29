# Buzz.app Agent Harness Config (0.5.0)

How to wire Buzz agents to external ACP backends, and the traps. Verified 2026-07-29 on Buzz v0.5.0.

Live agents: **Honey** → Gemini CLI (Vertex custom harness, model Auto) · **Fizz** → OpenCode (`ollama/gpt-oss:120b-cloud`, free) · **Claude** → Claude Code (opus, CLI subscription, no API key) · **Bumble** → Hermes Agent, **stopped on purpose** (see [[bumble-credential-hunt-incident]]).

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

## Gotchas

- **PATH detection:** Buzz only finds CLIs on its own PATH. `~/.opencode/bin/opencode` showed "not installed" until symlinked to `~/.local/bin/opencode`; then *Check again* flipped it to Ready.
- **Env-var UI bug:** typing `_` mid-field in the per-agent Environment-variable box sometimes inserts a blank row instead of the character. Verify every env edit in `managed-agents.json`; don't trust the displayed text.
- **New agents can't be minted headless** — each carries a nostr pubkey plus an owner-signed `auth_tag`, and only Buzz holds the owner key (keychain `buzz-desktop`). Create via GUI, or via an agent's `buzz agents draft-create` / `draft-update` tools, which land as drafts needing owner approval.
- **`requirements=2` / "setup-listener mode"** in the harness log means the agent has no provider+model resolved — it's the generic Buzz Agent harness waiting on config, not a broken binary.
- Gemini CLI free-tier OAuth is retired (`UNSUPPORTED_CLIENT`); Vertex ADC is the only path — see [[renderzero-vertex-patch]].
