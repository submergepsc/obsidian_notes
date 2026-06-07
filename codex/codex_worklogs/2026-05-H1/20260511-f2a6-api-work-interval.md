---
id: 20260511-f2a6-api-work-interval
name: API Work Interval Runtime Home
slug: api-work-interval
cwd: /home/loviya
summary: 确认当前会话由 API 调用，并建立 API runtime home 规则。
tags:
  - codex
  - api
  - runtime-home
priority: normal
---

# API Work Interval Runtime Home

## 当前快照

- 状态: 已完成
- 目标: 建立专用 API 工作区间，并确认当前会话是否由 API 调用。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-11 21:25:29 +0800

## 关键结果

- 已确认 the active environment uses `CODEX_HOME=/home/loviya/.codex-api`.
- Verified `/home/loviya/.codex-api` already exists as an API dedicated runtime home 带 account-specific runtime files and selected shared content symlinks.
- 已更新 `/home/loviya/.codex/AGENTS.md` so API-invoked sessions must verify and use `/home/loviya/.codex-api` as their dedicated API work interval/runtime home.

## API Runtime Home Rule Was Made Explicit

- 更新时间: 2026-05-11 21:25:29 +0800
- 工作目录: `/home/loviya`
- 来源指令: `建立一个新的api专用的工作区间,你知道当前是调用的api吗`
- 问题:
  - The API runtime home existed, but the startup rules did not explicitly say API-invoked sessions must verify and use it as the API work interval.
- 改进:
  - 已新增 a durable rule to `AGENTS.md` requiring API sessions to use `CODEX_HOME=/home/loviya/.codex-api` and report a mismatch before account-specific runtime changes.
- 结果:
  - Current and future API sessions have an explicit API work interval rule.
- 下一步:
  - 无
