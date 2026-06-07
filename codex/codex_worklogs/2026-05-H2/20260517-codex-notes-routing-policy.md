---
id: 20260517-codex-notes-routing-policy
name: Codex Notes Routing Policy
slug: codex-notes-routing-policy
cwd: /home/loviya
summary: 明确所有 notes 请求应写入 `codex_notes`，不再默认写入旧的 `obnotes/codex` 结果归档。
tags:
  - codex
  - notes
  - policy
priority: normal
---

# Codex 笔记 Routing 策略

## 当前快照

- 状态: 已完成
- 目标: 防止以后把用户要求写 notes 的内容误放到 `~/obnotes/codex/`。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-17 18:05:00 +0800

## 关键结果

- 已更新 `/home/loviya/.codex/AGENTS.md`。
- 新规则：凡是用户说 `notes`、`笔记`、`记到 notes`、`写到 notes`、durable notes、reusable notes，统一写入 `~/.codex/codex_notes/`。
- 用户主动要求生成笔记时，写入 `~/.codex/codex_notes/requested/`，并使用 `requested_by_user: true`、`importance: user-requested`、`review_priority: high` 等元数据。
- `~/obnotes/codex/` 降为 legacy result archive，除非用户明确给出该路径或明确要求写到那里，否则不再作为 note 请求的默认目标。

## Route All 笔记 Into Codex 笔记

- 更新时间: 2026-05-17 18:05:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `为了防止以后搞错,所有的notes都是写道codex_notes里面去的`
- 问题:
  - 先前把用户要求“写到 notes”误解为写入 `~/obnotes/codex/`。
  - AGENTS.md 中 `Important Result Notes` 和 `Codex Notes Knowledge Base` 两套位置容易混淆。
- 改进:
  - 将 notes 请求的默认路由明确为 `~/.codex/codex_notes/`。
  - 将用户主动要求的笔记明确路由到 `~/.codex/codex_notes/requested/`。
- 结果:
  - 后续不会再把普通 notes 请求写到 `~/obnotes/codex/`。
- 下一步:
  - 无。
