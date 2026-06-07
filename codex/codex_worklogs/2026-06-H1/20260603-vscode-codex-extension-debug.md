---
id: 20260603-vscode-codex-extension-debug
name: VS Code Codex 插件不可用排查
slug: vscode-codex-extension-debug
cwd: /home/loviya
summary: 排查 VS Code 中 openai.chatgpt/Codex 插件不可用问题，重点看扩展版本、app-server 进程、日志和账户状态。
tags:
  - vscode
  - codex
  - openai-chatgpt
  - extension
---

# Current Snapshot

- workflow id: 20260603-vscode-codex-extension-debug
- current status: 待继续
- current goal: 找出 VS Code 的 Codex 插件无法使用的原因，并尽量恢复可用。
- current blocker: 需要用户在 VS Code 里执行 `Developer: Reload Window` 或重启 VS Code，确认 Codex 插件是否恢复。
- next step: 用户 reload VS Code 后测试 Codex；若仍失败，读取新生成的 `openai.chatgpt/Codex.log` 和新 app-server 进程版本。
- tags: vscode, codex, openai-chatgpt, extension
- summary: 已确认 `openai.chatgpt@26.5601.21317` 是当前 VS Code 扩展索引版本；旧目录 `26.527`、`26.601` 被 `.obsolete` 标记但曾各自残留一个 `codex app-server`。已停止这两个旧 app-server；当前只剩终端里的 Codex CLI 进程。网络方面，`chatgpt.com/backend-api/...` 当前可达，但 `ab.chatgpt.com` 仍 TLS 失败/403，旧日志里大量 `fetch failed` 和 `failed to list apps` 与网络波动或代理环境有关。

# Log

## 2026-06-03 17:10 +0800

- 专属日志: `/home/loviya/.config/Code/logs/20260603T100013/window*/exthost/openai.chatgpt/Codex.log`。
- 日志结论: Codex 扩展能激活并 spawn app-server；旧日志中反复出现 `failed to list apps: Failed to send request`、`fetch failed`，目标包括 `chatgpt.com/backend-api/wham/apps`、`chatgpt.com/backend-api/codex/models` 和 `ab.chatgpt.com`。
- 版本结论: 16:08 VS Code 安装了 `openai.chatgpt-26.5601.21317-linux-x64` 并把 `26.601` 标记 obsolete，但 16:06 已启动的 `26.601` app-server 仍在跑；早上 `26.527` app-server 也残留。
- 网络结论: 当前 shell 显式测试显示 `chatgpt.com/backend-api/wham/apps` 不走代理可达，返回 HTTP 405（方法不匹配但网络通）；`ab.chatgpt.com` 仍 TLS 失败；`api.github.com/repos/openai/plugins` 可达。
- 环境结论: 当前 shell 有 `HTTP_PROXY/HTTPS_PROXY/ALL_PROXY` 和 `CODEX_HOME=/home/loviya/.codex-a`；VS Code 主进程未检出这些 proxy/CODEX_HOME 变量。
- 处理: 已停止两个 VS Code OpenAI 插件遗留 app-server：`openai.chatgpt-26.527.../codex app-server` 和 `openai.chatgpt-26.601.../codex app-server`。
- 验证: `pgrep -a -u loviya codex` 只剩当前终端 Codex CLI，不再有 VS Code 扩展目录中的 app-server。
- 待测: 用户在 VS Code 执行 `Developer: Reload Window` 或重启 VS Code 后，再打开 Codex sidebar 测试。

## 2026-06-03 16:13 +0800

- 来源指令: 用户反馈“检查一下为什么我的 vscode 的 codex 插件没法使用”。
- 历史搜索: `MEMORY.md` 未找到相关记忆；worklog 只找到 Codex apps MCP 启动告警和泛 VS Code 记录，无明确同类插件故障。
- 当前扩展: `code --list-extensions --show-versions` 显示 `openai.chatgpt@26.5601.21317` 已安装。
- 当前扩展目录: `/home/loviya/.vscode/extensions` 中同时存在 `openai.chatgpt-26.527.60818-linux-x64`、`openai.chatgpt-26.5601.21317-linux-x64`、`openai.chatgpt-26.601.21317-linux-x64`。
- 当前进程: VS Code 主窗口正在运行；同时看到 `codex app-server` 进程来自 `26.527` 和 `26.601` 两个不同扩展目录。
- 初步判断: 当前不是“插件没装”，更像扩展版本和 app-server 运行态不一致，或登录/服务状态错误。
