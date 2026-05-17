---
id: 20260515-zsh-full-migration
name: Zsh Full Migration
slug: zsh-full-migration
cwd: /home/loviya
summary: 将 Bash 中仍未覆盖的交互功能迁移到 zsh，补齐登录 shell、fzf、reload alias 和 API 环境清理。
tags:
  - zsh
  - bash
  - shell
priority: normal
---

# Zsh Full Migration

## Current Snapshot

- status: 已完成
- goal: 全面进入 zsh，完成 Bash 功能迁移。
- blocker: 无。
- next: 无。
- updated: 2026-05-17 16:04:16 +0800

## Key Results

- 默认登录 shell 已从 `/usr/bin/bash` 切换到 `/usr/bin/zsh`。
- `.zshrc` 已补齐 Bash 中剩余的 `cdos`、`cdcn`、`aagcc`、`help`、`cdls`。
- `.zshrc` 已补齐 `.profile` 里的 `~/bin` PATH 入口。
- `rb` 和 `reload_bashrc` 已改为 reload zsh，避免迁移后误回 Bash 配置。
- 已验证 zsh 能加载补齐的别名和函数，并能使用 Node 22 与 Cargo。
- 新增 `.zprofile`，让 zsh 登录 shell 也初始化 `~/bin`、`~/.local/bin`、Fcitx、NVM/Node 22。
- `.zshrc` 的 fzf 集成改为在真实 TTY 下加载，并回退到 `~/.fzf/shell/{completion,key-bindings}.zsh`。
- `sb` 在 zsh 中已改为 `source ~/.zshrc`。
- 已从 `.bashrc` 和 `.zshrc` 移除交互启动时的 `OPENAI_*` 直接导出，Codex API alias 继续使用专用 relay env。
- PTY 条件下已验证 fzf zsh completion 和 `fzf-file-widget` 会注册。

## Decisions

- 保留现有 Oh My Zsh 和 Powerlevel10k 配置，在当前 `.zshrc` 的 Bash migration 区块内补齐缺失功能。
- 不删除 `.bashrc`，将其作为回退配置保留。
- fzf 的 zsh key binding 依赖 ZLE，只在真实 TTY 里加载；非 TTY 脚本检查不需要加载按键绑定。

## Finish Remaining Zsh Migration Gaps

- updated: 2026-05-17 16:01:57 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `bash向zsh迁移还是不完整,继续检查改正`
- problem:
  - 上次 worklog 已标记完成，但 zsh 仍未覆盖登录 shell 的 `.profile` 初始化路径。
  - `.zshrc` 只尝试 source 不存在的 `~/.fzf.zsh`，没有使用实际存在的 `~/.fzf/shell/` zsh 集成。
  - zsh 中的 `sb` 仍指向 `source ~/.bashrc`，会把迁移后的会话拉回 Bash 配置。
  - `.bashrc` 和 `.zshrc` 仍有交互启动时的 `OPENAI_*` 直接导出。
  - 当前 API 会话的 `CODEX_HOME` 是 `/home/loviya/.codex-b`，与 API 会话应使用的 `/home/loviya/.codex-api` 不一致；本次未修改 Codex 账户运行态文件。
- improvement:
  - 新增 `/home/loviya/.zprofile`，补齐登录 zsh 的 PATH、Fcitx、NVM/Node 22 初始化。
  - 更新 `/home/loviya/.zshrc`：fzf 在真实 TTY 下加载 zsh completion 和 key bindings；`sb` 改为 reload `.zshrc`。
  - 从 `/home/loviya/.bashrc` 和 `/home/loviya/.zshrc` 移除交互配置里的 `OPENAI_*` 直接导出，保留 `codex-api` alias 的 relay env 入口。
- result:
  - `zsh -n ~/.zshrc` 和 `zsh -n ~/.zprofile` 通过。
  - 干净环境下 `zsh -lic` 验证 `ob`、`q`、`lsn`、`pandoc_pdf`、`py`、`dec2hex`、`cdls`、`aagcc`、Node 22、Cargo 都可用。
  - PTY 条件下验证 fzf zsh completion 和 `fzf-file-widget` 都会注册。
  - 干净环境下 Bash fallback 不再从 `.bashrc` 导出 `OPENAI_*`。
  - Codex 无 TTY 检查仍会因 sandbox 对 `~/.zcompdump-*` 的写限制出现 Oh My Zsh compdump 提示；这属于当前工具沙箱限制，不是 zsh 配置语法错误。
- next:
  - 无。

## Complete Bash Function Migration To Zsh

- updated: 2026-05-15 15:52:00 +0800
- cwd: `/home/loviya`
- source instruction: `我现在要全面进入使用zsh,完成bash所有功能迁移`
- problem:
  - 当前默认登录 shell 仍是 `/usr/bin/bash`。
  - `.zshrc` 已覆盖大多数 Bash 功能，但缺少 Bash 末尾新增的 `cdos`、`cdcn`、`aagcc`、`help`、`cdls`。
  - `.profile` 中的 `~/bin` PATH 补充未在 zsh 交互配置中体现。
- improvement:
  - 在 `.zshrc` 中补齐缺失别名、函数和 PATH。
  - 验证 zsh 配置加载。
  - 将用户默认登录 shell 改为 zsh。
- result:
  - `/home/loviya/.zshrc` 已补齐缺失功能。
  - `getent passwd loviya | cut -d: -f7` 返回 `/usr/bin/zsh`。
  - `zsh -n ~/.zshrc` 通过。
  - `zsh -lic` 验证 `rb`、`cdos`、`aagcc`、`help`、`cdls`、Node 22、Cargo 均可用。
  - 无 TTY 测试中 Powerlevel10k gitstatus 会报初始化警告，但不影响配置加载；真实终端通常不会以这种方式启动。
- next:
  - 新开终端后使用 zsh；旧终端可执行 `exec zsh`。
