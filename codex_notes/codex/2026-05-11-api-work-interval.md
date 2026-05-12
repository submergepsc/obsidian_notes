---
title: API Work Interval Runtime Home
date: 2026-05-11
area: codex
importance: normal
requested_by_user: false
tags:
  - codex
  - api
  - runtime-home
source_worklog: /home/loviya/.codex/worklogs/2026-05-11/20260511-f2a6-api-work-interval.md
---

# API Work Interval Runtime Home

## Result

API-invoked Codex sessions on this machine should use `/home/loviya/.codex-api` as the dedicated API work interval/runtime home.

## Verification

- Check `CODEX_HOME`.
- Expected value for API sessions: `/home/loviya/.codex-api`.
- If the value differs, report the mismatch before changing account-specific runtime state.

## Layout

- Shared policy and managed content still come from `/home/loviya/.codex` through selected symlinks.
- Runtime identity, logs, sessions, caches, history, sqlite state, and account-specific config stay under `/home/loviya/.codex-api`.

## Source

- Worklog: `/home/loviya/.codex/worklogs/2026-05-11/20260511-f2a6-api-work-interval.md`
