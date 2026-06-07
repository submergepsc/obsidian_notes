---
id: 20260522-fzf-path-widget-fix
name: fzf PATH 与 Ctrl-R widget 修复
slug: fzf-path-widget-fix
cwd: /home/loviya
summary: 修复 zsh 中 fzf-history-widget 已绑定但 fzf 二进制不在 PATH 导致 Ctrl-R 报 command not found 的问题。
tags:
  - zsh
  - fzf
  - shell
---

## Current Snapshot

- workflow id: 20260522-fzf-path-widget-fix
- current status: 已完成
- current goal: 诊断并修复 `fzf-history-widget: command not found: fzf`
- current blocker: 无
- next step: 无
- tags: zsh, fzf, shell
- summary: `fzf` 二进制位于 `/home/loviya/.fzf/bin/fzf`，但启动配置没有在加载 key bindings 前确保该目录进入 `PATH`；已更新 `/home/loviya/.zshrc`。

## Key Results

- `command -v fzf` 在原检查中为空，`type fzf` 显示 `fzf not found`。
- `find /home/loviya -maxdepth 5 -type f -name fzf` 找到 `/home/loviya/.fzf/bin/fzf`。
- `/home/loviya/.fzf.zsh` 不存在，`.zshrc` 走 `~/.fzf/shell/key-bindings.zsh` 分支，因此 widget 被加载但二进制目录没有进入 `PATH`。

## Changes

- 修改 `/home/loviya/.zshrc`：在 fzf key-bindings 加载前，如果 `$HOME/.fzf/bin/fzf` 可执行，则把 `$HOME/.fzf/bin` 加到 `PATH`。
- 修改 `/home/loviya/.zshrc`：最终 `Ctrl-R` 绑定增加 `${+commands[fzf]}` 条件，避免在 `fzf` 不可用时绑定到会报错的 widget。

## Verification

- `zsh -ic 'command -v fzf; whence -w fzf-history-widget; bindkey "^R"'` 使用 TTY 验证：
  - `/home/loviya/.fzf/bin/fzf`
  - `fzf-history-widget: function`
  - `"^R" fzf-history-widget`
