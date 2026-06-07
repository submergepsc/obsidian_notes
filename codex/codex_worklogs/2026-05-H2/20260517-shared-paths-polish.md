---
id: 20260517-shared-paths-polish
name: Shared Paths Polish
slug: shared-paths-polish
cwd: /home/loviya
summary: 将 `AGENTS.md` 中冗长的 shared-path 列表改成紧凑表格。
tags:
  - codex
  - agents
  - layout
  - polish
priority: normal
---

# Shared Paths Polish

## 当前快照

- 状态: 已完成
- 目标: 把 `AGENTS.md` 里的 shared paths 长列表改成更紧凑、更易读的格式。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-17 18:52:00 +0800

## 关键结果

- `Shared paths` 从 8 行重复长列表改成了表格。
- 只保留一条 “Applied under” 说明，避免每行重复 `.codex-a/.codex-b/...`。
- 语义不变，视觉上更干净。

## 决策

- 对这种“同一目标、多个前缀”的内容，优先用表格表达，而不是展开成一串重复条目。

## Polish Shared Paths

- 更新时间: 2026-05-17 18:52:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `Shared paths ... 这一部分内容太难看了,润色一下修改一下`
- 问题:
  - Shared paths 里每一行都重复同样的 5 个前缀，阅读噪音太高。
- 改进:
  - 改成两列 Markdown 表格，只列路径组和共享目标。
- 结果:
  - `AGENTS.md` 更紧凑，也更适合启动时快速扫描。
- 下一步:
  - 无。
