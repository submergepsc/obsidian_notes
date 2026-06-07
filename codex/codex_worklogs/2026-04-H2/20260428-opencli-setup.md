---
id: 20260428-opencli-setup
name: opencli setup
slug: opencli-setup
cwd: /home/loviya
summary: 已安装 and configured @jackwener/opencli for bash usage.
tags:
  - opencli
  - npm
  - bash
priority: medium
---

# opencli setup

## 会话

## 安装并配置 @jackwener/opencli
- 更新时间: 2026-04-28 14:33:11 +0800
- 工作目录: `/home/loviya`
- 主机: `nibaba`
- tmux: `无`
- 来源指令: `npm install -g @jackwener/opencli,帮我配置完这个`
- 上下文: 新建 `opencli setup` 工作流。
- 状态: 已完成
- 问题:
  - 目标: 安装并配置 `@jackwener/opencli`。
- 结果:
  - 已通过 `npm install -g @jackwener/opencli` 安装 `opencli` 1.7.8；生成并接入 bash completion；确认 `opencli --version`、`opencli list -f json` 可用；已 sparse clone 官方仓库并准备扩展目录 `/home/loviya/apps/opencli-source/extension`；最终 `opencli doctor` 通过，daemon 运行在 19825，Browser Bridge extension 已连接。
- 下一步: 无。
- 标签: opencli, npm, bash, browser-extension
## 避免 opencli bash completion 影响多个 AI agent 的 s...
- 更新时间: 2026-04-28 14:42:55 +0800
- 工作目录: `/home/loviya`
- 主机: `nibaba`
- tmux: `无`
- 来源指令: `我会使用非常多个aiagent,你这个~/.bash_completion会误导其他的ai`
- 上下文: 继续修正 OpenCLI shell 配置。
- 状态: 已完成
- 问题:
  - 目标: 避免 opencli bash completion 影响多个 AI agent 的 shell 判断。
- 结果:
  - 已从 `/home/loviya/.bashrc` 移除 `~/.bash_completion.d/opencli` 的 source 行，并删除 `/home/loviya/.bash_completion.d/opencli` 文件；验证 `opencli` 命令仍为 1.7.8，且 bash 中不再注册 `opencli` completion。
- 下一步: 无。
- 标签: opencli, bash, completion, ai-agent
