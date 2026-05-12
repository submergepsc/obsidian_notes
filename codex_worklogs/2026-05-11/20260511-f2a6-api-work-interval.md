---
id: 20260511-f2a6-api-work-interval
name: API Work Interval Runtime Home
slug: api-work-interval
cwd: /home/loviya
summary: Confirmed the current session is API-invoked and established the API runtime home rule.
tags:
  - codex
  - api
  - runtime-home
priority: normal
---

# API Work Interval Runtime Home

## Current Snapshot

- status: 已完成
- goal: Establish a dedicated API work interval and confirm whether the current session is API-invoked.
- blocker: none
- next: none
- updated: 2026-05-11 21:25:29 +0800

## Key Results

- Confirmed the active environment uses `CODEX_HOME=/home/loviya/.codex-api`.
- Verified `/home/loviya/.codex-api` already exists as an API dedicated runtime home with account-specific runtime files and selected shared content symlinks.
- Updated `/home/loviya/.codex/AGENTS.md` so API-invoked sessions must verify and use `/home/loviya/.codex-api` as their dedicated API work interval/runtime home.

## API Runtime Home Rule Was Made Explicit

- updated: 2026-05-11 21:25:29 +0800
- cwd: `/home/loviya`
- source instruction: `建立一个新的api专用的工作区间,你知道当前是调用的api吗`
- problem:
  - The API runtime home existed, but the startup rules did not explicitly say API-invoked sessions must verify and use it as the API work interval.
- improvement:
  - Added a durable rule to `AGENTS.md` requiring API sessions to use `CODEX_HOME=/home/loviya/.codex-api` and report a mismatch before account-specific runtime changes.
- result:
  - Current and future API sessions have an explicit API work interval rule.
- next:
  - none
