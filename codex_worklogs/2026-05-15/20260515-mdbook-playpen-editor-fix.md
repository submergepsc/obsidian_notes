---
id: 20260515-mdbook-playpen-editor-fix
name: Fix mdBook Playpen Editor Field
slug: mdbook-playpen-editor-fix
cwd: /home/loviya/notes/obsidian_notes/rust/rust-by-practice
summary: Removed the obsolete mdBook playpen editor field from the rust-by-practice Chinese book config.
tags:
  - rust
  - mdbook
  - rust-by-practice
priority: normal
---

# Fix mdBook Playpen Editor Field

## Current Snapshot

- status: 已完成
- goal: Remove the mdBook configuration field that newer mdBook versions reject.
- blocker: none
- next: none
- updated: 2026-05-15 14:12:32 +0800

## Key Results

- Removed `editor = "ace"` from `/home/loviya/notes/obsidian_notes/rust/rust-by-practice/zh-CN/book.toml`.
- Verified `mdbook build zh-CN` completes successfully.

## Fix Obsolete mdBook Editor Field

- updated: 2026-05-15 14:12:32 +0800
- cwd: `/home/loviya/notes/obsidian_notes/rust/rust-by-practice`
- source instruction: `改一下`
- problem:
  - Newer `mdbook` versions reject the old `editor` field under `[output.html.playpen]`.
- improvement:
  - Removed only the unsupported field and left the existing `editable = true` setting intact.
- result:
  - The Chinese mdBook build now succeeds without the `unknown field editor` error.
- next:
  - none
