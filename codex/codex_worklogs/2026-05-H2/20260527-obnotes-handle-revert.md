---
id: 20260527-obnotes-handle-revert
name: obnotes handle 最近修改回滚
slug: obnotes-handle-revert
cwd: /home/loviya/notes/obsidian_notes
summary: "调查并回滚用户刚在 obnotes 内运行 handle 命令后最近 5 分钟触碰的文件。"
tags: [obnotes, obsidian, git, rollback, handle]
---

# obnotes handle 最近修改回滚

## Current Snapshot

- workflow id: 20260527-obnotes-handle-revert
- current status: 已完成
- current goal: 回滚 `~/obnotes` 中 `2026-05-27 15:36:05 +0800` 之后由 handle 命令触碰的文件
- current blocker: none
- next step: none
- tags: obnotes, obsidian, git, rollback, handle
- summary: 已确认 `/home/loviya/obnotes` 指向 `/home/loviya/notes/obsidian_notes`，该目录是 git 仓库；最近窗口内现存文件集中在 `.obsidian` 和 `obsidian使用`。

## Key Results

- 固定调查窗口：`2026-05-27 15:36:05 +0800` 之后，避免后续恢复操作把新 mtime 混入原始清单。
- `find` 结果显示最近现存文件主要为 `.obsidian` 主题/插件/配置文件，以及 `obsidian使用` 下 8 个 Markdown 文件。
- `git status` 中存在大量更早的历史改动，不能整仓库重置；恢复必须按固定窗口筛选。

## Commands

- `find /home/loviya/notes/obsidian_notes -path '*/.git/*' -prune -o -type f -newermt '2026-05-27 15:36:05 +0800' ...`
- `git -C /home/loviya/notes/obsidian_notes status --short`
- `git -C /home/loviya/notes/obsidian_notes diff --name-status`

## Restore Result

- 已将固定窗口内 51 个 git 跟踪文件执行 `git restore --worktree`。
- 恢复前 diff 已备份到 `/tmp/obnotes-handle-revert-20260527-1544.diff`，大小约 8.17 MB。
- 验证：对这 51 个路径执行 `git status --short -- <paths>` 和 `git diff --name-only -- <paths>`，输出均为空。
- 固定窗口内没有未跟踪文件需要删除；`.obsidian/workspace.json` 是 `.gitignore` 忽略的 Obsidian 运行态文件，且之后仍被 Obsidian 写入，没有可用 git 版本可恢复。
- 仓库仍有其他历史未提交改动；未执行整仓库 reset。
