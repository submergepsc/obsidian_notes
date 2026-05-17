---
id: 20260516-a17c9d-session-standby
name: Session Standby
slug: session-standby
cwd: /home/loviya
summary: Startup bookkeeping for a new API-invoked Codex session with no concrete task yet.
tags:
  - startup
  - standby
priority: normal
---

# Session Standby

## Current Snapshot

- status: 已完成
- goal: Wait for a concrete user task without attaching this session to an unrelated unfinished workflow.
- blocker: API runtime home is `/home/loviya/.codex-b`, while the global policy expects API sessions to use `/home/loviya/.codex-api`, `/home/loviya/.codex-api-ds`, or `/home/loviya/.codex-api-mimo`.
- next: none
- updated: 2026-05-16 11:51:47 +0800

## Startup Session Created Without Task Attachment

- updated: 2026-05-16 11:45:14 +0800
- cwd: `/home/loviya`
- source instruction: `hi`
- problem:
  - The current instruction is only a greeting, and the recent unfinished workflows in `/home/loviya` do not have a strong task-thread match.
  - The API runtime home check reported `/home/loviya/.codex-b`, which does not match the expected API runtime homes from the global policy.
- improvement:
  - Created a minimal standalone workflow so future concrete work can either continue this session or start a better-named task workflow without corrupting unrelated worklogs.
- result:
  - Shared worklog bookkeeping is active for this session.
- next:
  - Ask the user for the concrete task.
