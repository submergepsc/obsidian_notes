---
id: 20260428-opencli-setup
name: opencli setup
slug: opencli-setup
cwd: /home/loviya
summary: Installed and configured @jackwener/opencli for bash usage.
tags:
  - opencli
  - npm
  - bash
priority: medium
---

# opencli setup

## Sessions

## 安装并配置 @jackwener/opencli
- updated: 2026-04-28 14:33:11 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `none`
- source instruction: `npm install -g @jackwener/opencli,帮我配置完这个`
- context: 新建 `opencli setup` 工作流。
- status: 已完成
- problem:
  - goal: 安装并配置 `@jackwener/opencli`。
- result:
  - 已通过 `npm install -g @jackwener/opencli` 安装 `opencli` 1.7.8；生成并接入 bash completion；确认 `opencli --version`、`opencli list -f json` 可用；已 sparse clone 官方仓库并准备扩展目录 `/home/loviya/apps/opencli-source/extension`；最终 `opencli doctor` 通过，daemon 运行在 19825，Browser Bridge extension 已连接。
- next: 无。
- tags: opencli, npm, bash, browser-extension
## 避免 opencli bash completion 影响多个 AI agent 的 s...
- updated: 2026-04-28 14:42:55 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `none`
- source instruction: `我会使用非常多个aiagent,你这个~/.bash_completion会误导其他的ai`
- context: 继续修正 OpenCLI shell 配置。
- status: 已完成
- problem:
  - goal: 避免 opencli bash completion 影响多个 AI agent 的 shell 判断。
- result:
  - 已从 `/home/loviya/.bashrc` 移除 `~/.bash_completion.d/opencli` 的 source 行，并删除 `/home/loviya/.bash_completion.d/opencli` 文件；验证 `opencli` 命令仍为 1.7.8，且 bash 中不再注册 `opencli` completion。
- next: 无。
- tags: opencli, bash, completion, ai-agent
