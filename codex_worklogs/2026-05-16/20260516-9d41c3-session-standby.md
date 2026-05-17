---
id: 20260516-9d41c3-session-standby
name: Session Standby
slug: session-standby
cwd: /home/loviya
summary: Startup bookkeeping for a greeting-only Codex API session with no concrete task yet.
tags:
  - startup
  - standby
priority: normal
---

# Session Standby

## Current Snapshot

- status: 已完成
- goal: Wait for a concrete user task without attaching this session to an unrelated unfinished workflow.
- blocker: API runtime home is `/home/loviya/.codex-a`, while the global policy expects API sessions to use `/home/loviya/.codex-api`, `/home/loviya/.codex-api-ds`, or `/home/loviya/.codex-api-mimo`.
- next: none
- updated: 2026-05-16 13:56:30 +0800

## Greeting Did Not Match An Unfinished Workflow

- updated: 2026-05-16 13:56:30 +0800
- cwd: `/home/loviya`
- source instruction: `hi`
- problem:
  - The instruction is only a greeting, while recent `/home/loviya` workflows cover distinct task threads.
  - The API runtime home check reported `/home/loviya/.codex-a`, which does not match the expected API runtime homes from the global policy.
- improvement:
  - Created a minimal standalone startup record and left unrelated unfinished workflows untouched.
  - Avoided account-specific runtime changes because the runtime home does not match the API-session policy.
- result:
  - Startup bookkeeping is complete for this session.
- next:
  - Wait for the user's concrete task.
