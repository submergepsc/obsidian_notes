---
id: 20260515-mdbook-playpen-editor-fix
name: Fix mdBook Playpen Editor Field
slug: mdbook-playpen-editor-fix
cwd: /home/loviya/notes/obsidian_notes/rust/rust-by-practice
summary: 已删除 the obsolete mdBook playpen editor field from the rust-by-practice Chinese book config.
tags:
  - rust
  - mdbook
  - rust-by-practice
priority: normal
---

# 修复 mdBook Playpen Editor Field

## 当前快照

- 状态: 已完成
- 目标: 移除新版 mdBook 不接受的配置字段。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-15 14:12:32 +0800

## 关键结果

- 已删除 `editor = "ace"` from `/home/loviya/notes/obsidian_notes/rust/rust-by-practice/zh-CN/book.toml`.
- Verified `mdbook build zh-CN` completes successfully.

## 修复 Obsolete mdBook Editor Field

- 更新时间: 2026-05-15 14:12:32 +0800
- 工作目录: `/home/loviya/notes/obsidian_notes/rust/rust-by-practice`
- 来源指令: `改一下`
- 问题:
  - Newer `mdbook` versions reject the old `editor` field under `[output.html.playpen]`.
- 改进:
  - 已删除 only the unsupported field and left the existing `editable = true` setting intact.
- 结果:
  - The Chinese mdBook build now succeeds 不带 the `unknown field editor` error.
- 下一步:
  - 无
