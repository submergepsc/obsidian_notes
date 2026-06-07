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

# API 工作区间 Runtime Home

## 结果

本机通过 API 调用的 Codex 会话应使用 `/home/loviya/.codex-api` 作为专用 API 工作区间/runtime home。

## 验证

- Check `CODEX_HOME`.
- API 会话的预期值：`/home/loviya/.codex-api`。
- 如果实际值不同，在修改账户专属运行态前先报告不一致。

## 布局

- 共享策略和托管内容仍通过选定符号链接来自 `/home/loviya/.codex`。
- Runtime identity、日志、sessions、cache、history、sqlite state 和账户专属 config 保留在 `/home/loviya/.codex-api` 下。

## 来源

- Worklog: `/home/loviya/.codex/worklogs/2026-05-11/20260511-f2a6-api-work-interval.md`
