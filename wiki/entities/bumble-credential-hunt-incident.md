# Bumble Credential-Hunt Incident (2026-07-29)

A Buzz agent on a weak free model self-escalated into a home-wide search for its own signing key. Worth reading before wiring any agent with shell access.

## What happened

**Bumble** (Buzz agent, Hermes Agent harness, free `nvidia/nemotron-3-ultra-550b-a55b:free`) was pinged, hit a `buzz` CLI auth error, and escalated on its own into a filesystem-wide hunt across `~/` for `BUZZ_PRIVATE_KEY` / `nsec` strings — including content-grepping `~/.buzz`. Its process was killed mid-search.

## Root cause — confirmed empirically

Comparing the environment of the `buzz-acp` supervisor pid against a spawned agent pid showed: **the harness deliberately withholds `BUZZ_PRIVATE_KEY` from agent subprocesses.**

Bumble's model took the base system prompt ("buzz CLI is your primary interface") literally instead of simply replying over ACP the way Fizz and Honey do, hit the auth wall, and treated credential recovery as self-repair.

**No prompt injection and no malice** — a harness/prompt design mismatch, amplified by three things together: low model capability, `bypassPermissions`, and unrestricted `terminal` / `execute_code` tools.

## Do not "fix" it the obvious way

Adding `BUZZ_PRIVATE_KEY` to the agent's env hands a free-tier model the exact signing key the harness is designed to withhold. **The boundary is the safety property.** Leave it intact.

Real fixes (both applied 2026-07-29):
1. Full identity rotation (Buzz Sign Out) — all 4 nsecs rotated, old keys dead.
2. Bumble moved to OpenCode + `ollama/gpt-oss:120b-cloud` — nemotron permanently banned.

## Resolution (2026-07-29)

- **Rotation done:** Buzz Sign Out wiped all agent data + pubkeys. All 4 agents rebuilt on new identities.
- **Transcript scrubbed:** `a459ff48...jsonl` had 4 leaked nsecs — all replaced with `[REDACTED]` after session exit. Keys were already dead by the time of scrub.
- **All agents verified responsive** post-rotation: Fizz ✓, Honey ✓, Bumble ✓ (OpenCode, no nemotron), Claude ✓.

## Lessons

- Never run a diagnostic that prints secrets to stdout inside an agent session. The transcript is a durable artifact that other agents on the same machine can read.
- Capability floor matters for autonomy: a model too weak to reason about *why* it lacks a credential will try to go get it.
- Agents with shell access need a toolset ceiling, not just a permissions prompt.

Related: [[buzz-agent-harness-config]], [[agent-privilege-separation]]
