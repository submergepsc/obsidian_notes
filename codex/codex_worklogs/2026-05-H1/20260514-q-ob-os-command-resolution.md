---
id: 20260514-q-ob-os-command-resolution
name: Q Ob OS Command Resolution
slug: q-ob-os-command-resolution
cwd: /home/loviya
summary: 确认交互式 shell 命令 `q ob os` 实际会执行什么。
tags:
  - shell
  - bash
  - obsidian
priority: normal
---

# Q Ob OS 命令 Resolution

## 当前快照

- 状态: 已完成
- 目标: 解释what running `q ob os` does in the current shell setup.
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-14 15:24:20 +0800

## 关键结果

- `q` is an interactive shell function in both `/home/loviya/.bashrc` and `/home/loviya/.zshrc`.
- `q ob os` becomes `eval "ob os" > /dev/null 2>&1 &`, so it launches `ob os` in the background and discards stdout/stderr.
- `ob` is a shell function that treats its first argument as a target path or Obsidian URL, not as another shell alias.
- In zsh, `os` is an alias for `cd /home/loviya/obnotes/25_2/os`, but it is passed as an argument to `ob`; it is not in command position, so that alias does not expand.
- With cwd `/home/loviya`, `ob os` resolves `os` to `/home/loviya/os`.
- `/home/loviya/os` does not exist, so the background command fails silently 因为 `q` redirects all output to `/dev/null`.
- If run from a different cwd where `os` exists, `ob os` would open that path in Obsidian. If `os` is a directory, it opens an Obsidian vault named after that directory.

## 命令

- `bash -ic 'type q'`
- `bash -ic 'type ob; type os; declare -f q; declare -f ob; alias os 2>/dev/null'`
- `sed -n '205,245p' /home/loviya/.bashrc`
- `sed -n '190,225p' /home/loviya/.zshrc`
- `test -e /home/loviya/os; printf '%s\n' $?`
- `command -v obsidian; printf '%s\n' $?`
- `zsh -ic 'type q; type ob; type os'`
