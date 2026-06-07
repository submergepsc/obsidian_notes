---
id: 20260516-a17c9d-session-standby
name: Session Standby
slug: session-standby
cwd: /home/loviya
summary: 新 API 调用 Codex 会话的启动记录；暂时没有具体任务。
tags:
  - startup
  - standby
priority: normal
---

# 会话待命

## 当前快照

- 状态: 已完成
- 目标: 等待用户给出具体任务，不把本次会话误接到无关的未完成工作流。
- 阻塞: API runtime home is `/home/loviya/.codex-b`, while the global policy expects API sessions to use `/home/loviya/.codex-api`, `/home/loviya/.codex-api-ds`, or `/home/loviya/.codex-api-mimo-pay-self`.
- 下一步: 无。
- 更新时间: 2026-05-16 11:51:47 +0800

## 启动 会话 已创建 Without Task Attachment

- 更新时间: 2026-05-16 11:45:14 +0800
- 工作目录: `/home/loviya`
- 来源指令: `hi`
- 问题:
  - The current instruction is only a greeting, and the recent unfinished workflows in `/home/loviya` do not have a strong task-thread match.
  - The API runtime home check reported `/home/loviya/.codex-b`, which does not match the expected API runtime homes from the global policy.
- 改进:
  - 已创建 a minimal standalone workflow so future concrete work can either continue this session or start a better-named task workflow 不带 corrupting unrelated worklogs.
- 结果:
  - Shared worklog bookkeeping is active for this session.
- 下一步:
  - Ask the user for the concrete task.
