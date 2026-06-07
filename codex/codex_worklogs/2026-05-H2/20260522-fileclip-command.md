---
id: 20260522-fileclip-command
name: fileclip 文件内容到剪贴板命令
slug: fileclip-command
cwd: /home/loviya
summary: 新增 fileclip 命令，将指定文件内容写入 CopyQ 历史并同步为系统剪贴板。
tags:
  - clipboard
  - copyq
  - shell
---

# Current Snapshot

- workflow id: 20260522-fileclip-command
- current status: 已完成
- current goal: 提供一个命令，把某个文件的内容复制到系统剪贴板。
- current blocker: 无
- next step: 无
- tags: clipboard, copyq, shell
- summary: 已新增 `/home/loviya/.local/bin/fileclip`，语法检查、帮助输出、PATH 解析和 CopyQ 真实写入读回均通过。

# Key Results

- 发现本机已有 CopyQ 结论：`copyq --start-server add -` 写入历史，随后 `copyq --start-server select 0` 同步系统剪贴板。
- 当前 PATH 包含 `/home/loviya/.local/bin`，zsh 配置也会加入该目录。

# Commands

- 搜索历史 worklog：`rg -n "剪切板|clipboard|copyq|文件内容" ~/.codex/worklogs/INDEX.md ~/.codex/worklogs`
- 检查入口：`rg -n "alias |function |fpath|source|copyq|clipboard|clip" ~/.zshrc ~/.bashrc ~/.profile ~/.local/bin ~/bin`

# Artifacts

- `/home/loviya/.local/bin/fileclip`

# Verification

- `sh -n /home/loviya/.local/bin/fileclip` 通过。
- `/home/loviya/.local/bin/fileclip --help` 正常输出用法。
- `command -v fileclip` 解析为 `/home/loviya/.local/bin/fileclip`。
- 使用临时文件执行真实写入，`copyq --start-server read 0` 读回内容与测试文件一致。

# Notes

- 用户明确要求“写入notes”；已新增 requested note：`/home/loviya/.codex/codex_notes/requested/2026-05-22-fileclip-file-to-clipboard.md`。
- 已更新 notes 总索引和 requested 索引。
