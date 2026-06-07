---
id: 20260521-ctrl-r-fzf-zsh-fix
name: Ctrl+r fzf zsh 绑定修复
slug: ctrl-r-fzf-zsh-fix
cwd: /home/loviya
summary: 调整 zsh 中 fzf key bindings 的加载条件，让交互式 shell 稳定绑定 Ctrl+r 到 fzf-history-widget。
tags:
  - zsh
  - fzf
  - history
  - ctrl-r
---

# Ctrl+r fzf zsh 绑定修复

## Current Snapshot

- workflow id: 20260521-ctrl-r-fzf-zsh-fix
- current status: 已完成
- current goal: 修复/加固 zsh 下 Ctrl+r 历史搜索，确保交互式 shell 使用 fzf
- current blocker: none
- next step: none
- tags: zsh, fzf, history, ctrl-r
- summary: 已将 fzf 加载条件加固为交互式且 stdin/stdout 均为 TTY；真实 PTY 下 `Ctrl+r` 绑定到 `fzf-history-widget`，非 TTY 检查不再加载 fzf。

## Verification

- `sed -n '104,116p' ~/.zshrc`：确认 fzf 加载条件为 `[[ -o interactive && -t 0 && -t 1 ]]`。
- PTY `zsh -ic 'bindkey "^R"; whence -w fzf-history-widget'`：返回 `"^R" fzf-history-widget` 和 `fzf-history-widget: function`。
- 非 TTY `zsh -ic`：不加载 fzf，`Ctrl+r` 回退原生历史搜索，避免无界面环境加载 fzf key bindings。
- `zsh -n ~/.zshrc`：语法检查通过。

## Notes

- 真实终端里 `Ctrl+r` 使用 fzf；脚本式/非 TTY 检查里看到 zsh 原生绑定是预期行为。
- 非 TTY 下仍可能出现 Powerlevel10k/gitstatus 初始化提示，这是独立问题，不属于 Ctrl+r/fzf 绑定。

## Follow-up

- Ctrl+r 历史窗口已配置为 `--height 100%`，输入如 `ls` 时可在满高 fzf 列表中滚动查看所有匹配项。
- PTY 验证：`FZF_CTRL_R_OPTS=--height 100%`，`^R` 绑定为 `fzf-history-widget`。
