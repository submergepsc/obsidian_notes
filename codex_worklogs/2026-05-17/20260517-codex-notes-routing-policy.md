---
id: 20260517-codex-notes-routing-policy
name: Codex Notes Routing Policy
slug: codex-notes-routing-policy
cwd: /home/loviya
summary: Clarify that all notes requests should write to codex_notes instead of the legacy obnotes/codex result archive.
tags:
  - codex
  - notes
  - policy
priority: normal
---

# Codex Notes Routing Policy

## Current Snapshot

- status: 已完成
- goal: 防止以后把用户要求写 notes 的内容误放到 `~/obnotes/codex/`。
- blocker: 无。
- next: 无。
- updated: 2026-05-17 18:05:00 +0800

## Key Results

- 已更新 `/home/loviya/.codex/AGENTS.md`。
- 新规则：凡是用户说 `notes`、`笔记`、`记到 notes`、`写到 notes`、durable notes、reusable notes，统一写入 `~/.codex/codex_notes/`。
- 用户主动要求生成笔记时，写入 `~/.codex/codex_notes/requested/`，并使用 `requested_by_user: true`、`importance: user-requested`、`review_priority: high` 等元数据。
- `~/obnotes/codex/` 降为 legacy result archive，除非用户明确给出该路径或明确要求写到那里，否则不再作为 note 请求的默认目标。

## Route All Notes Into Codex Notes

- updated: 2026-05-17 18:05:00 +0800
- cwd: `/home/loviya`
- source instruction: `为了防止以后搞错,所有的notes都是写道codex_notes里面去的`
- problem:
  - 先前把用户要求“写到 notes”误解为写入 `~/obnotes/codex/`。
  - AGENTS.md 中 `Important Result Notes` 和 `Codex Notes Knowledge Base` 两套位置容易混淆。
- improvement:
  - 将 notes 请求的默认路由明确为 `~/.codex/codex_notes/`。
  - 将用户主动要求的笔记明确路由到 `~/.codex/codex_notes/requested/`。
- result:
  - 后续不会再把普通 notes 请求写到 `~/obnotes/codex/`。
- next:
  - 无。
