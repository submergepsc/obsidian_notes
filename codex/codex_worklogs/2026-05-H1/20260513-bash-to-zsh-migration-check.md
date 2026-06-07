---
id: 20260513-bash-to-zsh-migration-check
name: Bash To Zsh Migration Check
slug: bash-to-zsh-migration-check
cwd: /home/loviya/notes/obsidian_notes/25_2/cn
summary: 已检查 current Bash-to-Zsh migration status and identified the remaining switch-over work.
tags:
  - shell
  - zsh
  - bash
  - migration
priority: normal
---

# Bash 到 Zsh 迁移检查

## 当前快照

- 状态: 已完成
- 目标: 检查how far the Bash configuration has been migrated to Zsh.
- 阻塞: 无。
- 下一步: 如果用户要实际切换，先补齐剩余 Zsh 缺口，再运行 `chsh -s /usr/bin/zsh loviya`。
- 更新时间: 2026-05-13 22:55:00 +0800

## 关键结果

- `zsh` is installed at `/usr/bin/zsh`.
- `/home/loviya/.zshrc` exists and was last modified on 2026-05-12 11:51:04 +0800.
- 账号登录 shell 仍是 `/usr/bin/bash`，因此系统级切换尚未完成。
- `.zshrc` already contains a migrated configuration block covering most aliases, functions, environment variables, nvm, fcitx, OpenClaw zsh completion, Powerlevel10k, and tmux startup.
- `.zshrc` passes `zsh -n`.
- In the sandboxed check, sourcing `.zshrc` reported write failures for Oh My Zsh cache files 因为 the home cache path was read-only in this Codex environment; this is likely sandbox-specific.

## 剩余缺口

- Bash has `cdos` and `cdcn`; Zsh currently has `os` but not `cdos` or `cdcn`.
- `.zshrc` tries to source `~/.fzf.zsh`, but that file does not exist. The fzf zsh integration files exist under `~/.fzf/shell/`.
- `.profile` still has Bash/NVM/Fcitx login-shell setup. Zsh login behavior should be checked before relying on `.zshrc` alone for graphical or login sessions.
- The default shell has not been changed 带 `chsh`.
- The shell config still contains an explicit API key export and should be cleaned up into a dedicated env file before broader reuse.

## 命令

- `getent passwd loviya`
- `command -v zsh bash chsh fzf starship zoxide direnv`
- `sed -n '1,260p' /home/loviya/.bashrc`
- `sed -n '1,320p' /home/loviya/.zshrc`
- `zsh -n /home/loviya/.zshrc`
- `zsh -ic 'echo ZSH_OK; alias rb; alias os; whence -w ob q lsn pandoc_pdf py dec2hex'`
- `find /home/loviya/.fzf -maxdepth 3 -type f | sort`

