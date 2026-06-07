---
date: 2026-05-17
area: system
importance: normal
tags:
  - codex
  - layout
  - worklogs
  - notes
  - symlink
source_worklog: 20260517-codex-layout-reorg
---

# Codex 布局重组

## 决策

保持 Codex 存储统一位于 `~/obnotes/codex/` 下：

- `~/obnotes/codex/codex_worklogs/`
- `~/obnotes/codex/codex_notes/`

共享 `.codex` 路径应指向这些位置。

## 原因

这样可以把所有 Codex 管理内容放在同一个父目录下，同时保留既有的 `codex_worklogs` 和 `codex_notes` 名称。

## 已更新路径

- `~/.codex/worklogs` -> `~/obnotes/codex/codex_worklogs/`
- `~/.codex/codex_notes` -> `~/obnotes/codex/codex_notes/`
- `/home/loviya/.codex/AGENTS.md`
- `codex/codex_worklogs/README.md`
- `codex/codex_notes/README.md`
