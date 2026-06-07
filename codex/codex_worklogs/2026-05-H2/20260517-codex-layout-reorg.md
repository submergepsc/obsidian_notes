---
id: 20260517-codex-layout-reorg
name: Codex Layout Reorg
slug: codex-layout-reorg
cwd: /home/loviya
summary: 将 codex worklogs 和 codex_notes 移到 `codex/` 根目录下，并更新所有路径设置和软链接。
tags:
  - codex
  - layout
  - worklogs
  - notes
  - policy
priority: normal
---

# Codex 布局 Reorg

## 当前快照

- 状态: 已完成
- 目标: 将 `codex_worklogs` 和 `codex_notes` 统一移动到 `~/obnotes/codex/` 目录下，并同步更新路径设置。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-17 18:37:00 +0800

## 关键结果

- 已把 `~/obnotes/codex_worklogs/` 移动为 `~/obnotes/codex/codex_worklogs/`。
- 已把 `~/obnotes/codex_notes/` 移动为 `~/obnotes/codex/codex_notes/`。
- 已将 `~/.codex/worklogs` 和 `~/.codex/codex_notes` 重新指向新的 `codex/` 子目录。
- 已更新 `/home/loviya/.codex/AGENTS.md`、`codex/codex_notes/README.md`、`codex/codex_worklogs/README.md` 中的路径说明。

## 决策

- 保留 `~/obnotes/codex/` 作为 Codex 内容根目录。
- 让 `codex_notes` 与 `codex_worklogs` 继续保留原名，但放到 `codex/` 之下，避免改动太多既有逻辑。
- 直接结果笔记可以继续放在 `~/obnotes/codex/` 根目录，`codex_notes` 和 `codex_worklogs` 负责结构化沉淀。

## Rehome Codex Storage Under Codex Root

- 更新时间: 2026-05-17 18:37:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `整理一下codex的结构,把obnotes/codex_worklog和codex_notes都放到codex目录里面,并且更新所有相关的路径设置`
- 问题:
  - `codex_worklogs` 和 `codex_notes` 还散落在 `~/obnotes/` 根下，路径层级不统一。
  - `.codex` 里的共享链接仍然指向旧路径。
- 改进:
  - 统一迁入 `~/obnotes/codex/codex_worklogs` 与 `~/obnotes/codex/codex_notes`。
  - 同步更新 AGENTS、README 和软链接目标。
- 结果:
  - Codex 相关内容现在统一收纳到 `codex/` 根目录下。
- 下一步:
  - 无。
