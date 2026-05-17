---
id: 20260517-zsh-startup-performance
name: Zsh Startup Performance
slug: zsh-startup-performance
cwd: /home/loviya
summary: Diagnose why zsh feels much slower than bash after migration and optimize startup if safe.
tags:
  - zsh
  - shell
  - performance
priority: normal
---

# Zsh Startup Performance

## Current Snapshot

- status: 已完成
- goal: 找出 zsh 比 bash 慢很多的主要原因，并在不破坏现有功能的前提下优化启动速度。
- blocker: 无。
- next: 无。
- updated: 2026-05-17 17:57:00 +0800

## Key Results

- zsh 裸启动很快；慢点来自启动配置，不是 zsh 本体。
- `zprof` 显示 `nvm` 是主因：`.zshrc` 中 `source nvm.sh` 和 `nvm use 22` 占用约 0.7 秒。
- `.zprofile` 也重复加载 nvm，登录终端可能比非登录交互 shell 更慢。
- 已把 zsh 中 nvm 初始化改成懒加载：默认 Node 22 路径直接加入 PATH，真正运行 `nvm` 时再 source `nvm.sh`。
- 验证后 `zsh -ic exit` 从约 `1.28s` 降到约 `0.07s`；PTY 下约 `0.08s`。
- `node -v` 为 `v22.22.2`，`npm -v` 为 `10.9.7`，`nvm` 仍是可用 shell function。
- 用户指出应放入 `codex_notes`；已删除误放的 `/home/loviya/obnotes/codex/2026-05-17-zsh-nvm-startup-optimization.md`，并改存到 `/home/loviya/.codex/codex_notes/requested/2026-05-17-zsh-nvm-startup-optimization.md`。

## Decisions

- 不恢复已完成的 `20260515-zsh-full-migration`；本次性能排查作为新的工作流记录。
- 不在 zsh 启动时执行 `nvm use 22`；用固定 Node 22 bin 路径保障默认 Node 可用。
- 保留 Oh My Zsh 和 Powerlevel10k；它们在 profile 中不是主要耗时来源。

## Diagnose Zsh Startup Slowness

- updated: 2026-05-17 17:45:04 +0800
- cwd: `/home/loviya`
- source instruction: `我发现现在使用zsh比bash慢很多`
- problem:
  - 用户反馈迁移到 zsh 后交互体验明显比 bash 慢。
  - 需要区分是 zsh 本身慢，还是 `.zshrc` 中插件、补全、prompt、外部命令或环境管理器初始化拖慢。
- improvement:
  - 先测量裸 shell、普通交互 shell 和带配置调试的启动耗时。
  - 再根据热点做最小化修改。
- result:
  - 已修改 `/home/loviya/.zshrc` 和 `/home/loviya/.zprofile`，将 nvm 改为懒加载。
  - 无 TTY 的 Codex 测试仍会打印 Powerlevel10k `gitstatus failed to initialize`，但 PTY 验证正常；这是测试环境问题，不是真实终端启动失败。
- next:
  - 无。
