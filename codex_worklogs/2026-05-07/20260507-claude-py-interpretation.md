---
id: 20260507-claude-py-interpretation
name: Claude Python File Interpretation
slug: claude-py-interpretation
cwd: /home/loviya/claude
summary: 解读 /home/loviya/claude/claude.py 的用途、结构、执行流程和风险点。
tags:
  - python
  - claude
  - code-reading
priority: normal
---

# Claude Python File Interpretation

## Current Snapshot

- status: 已完成
- goal: 解读 `claude.py` 的代码行为和风险。
- blocker: 无。
- next: 无。
- updated: 2026-05-07 12:10:44 +0800

## Key Results

- `claude.py` 是一个 Claude Code CLI 补丁器，用于定位已安装的 Claude Code 可执行文件和 npm shim。
- 脚本通过字节级等长替换清空内置提示词/限制片段，并改写 Windows npm shim 以自动追加 `~/.claude/override.md`。
- 支持 TUI、`--status`、`--apply`、`--revert` 四类入口；运行 `--apply` 会修改安装目录中的实际可执行文件和 shim。

## Code Interpretation Request

- updated: 2026-05-07 12:10:44 +0800
- cwd: `/home/loviya/claude`
- source instruction: `解读一下这个python文件`
- problem:
  - 用户需要理解当前目录唯一 Python 文件 `claude.py` 的作用和风险。
- result:
  - 已阅读文件主体，包括路径检测、补丁定位、shim 注入、状态展示、应用和回滚流程。
- next:
  - 无。
