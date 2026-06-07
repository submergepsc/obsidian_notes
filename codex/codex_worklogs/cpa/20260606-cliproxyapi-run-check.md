---
id: 20260606-cliproxyapi-run-check
name: CLIProxyAPI 本机运行检查
slug: cliproxyapi-run-check
cwd: /home/loviya/cpa
summary: "检查本机 /home/loviya/cpa 的 CLIProxyAPI 二进制、配置模板、认证目录和运行方式，并尽量启动验证。"
tags:
  - cpa
  - cliproxyapi
  - api-proxy
---

# Current Snapshot

- workflow id: 20260606-cliproxyapi-run-check
- current status: 已完成
- current goal: 帮用户确认本机 `/home/loviya/cpa` 的 CLIProxyAPI 能否运行，并给出可用启动/配置方式。
- current blocker: 无。
- next step: none；如需继续，可把 OpenAI-compatible 客户端指向 `http://127.0.0.1:8317/v1`。
- tags: cpa, cliproxyapi, api-proxy
- summary: `/home/loviya/cpa` 是独立二进制目录，不是 Git repo；已创建本地安全配置 `/home/loviya/cpa/config.yaml`，后台服务运行在 `tmux -L cpa` 的 `cli-proxy-api` 会话中，监听 `127.0.0.1:8317`；Codex auth 已加载，`gpt-5.4-mini` 最小请求返回成功。

# Log

## 2026-06-06 17:24 +0800

- 来源指令: 用户确认需要处理 `CLIProxyAPI`，按“检查并尽量跑起来”执行。
- 初始发现:
  - `/home/loviya/cpa` 非 Git 仓库。
  - 目录内有可执行文件 `cli-proxy-api`，大小约 40 MiB。
  - README_CN 描述它是为 OpenAI/Gemini/Claude/Codex/Grok 兼容 API 提供代理服务器的工具，并支持 OpenAI Codex 与 Claude Code OAuth。
- 下一步: 检查配置模板、命令帮助、认证目录和本机端口占用。

## 2026-06-06 17:28 +0800

- 命令帮助: `cli-proxy-api --help` 显示版本 `7.1.19`，支持 `-codex-login`、`-codex-device-login`、`-claude-login`、`-login`、`-tui`、`-standalone`、`-local-model` 和 `-config`。
- 配置模板: 默认端口 `8317`，默认 `auth-dir: ~/.cli-proxy-api`，管理 API 的 `secret-key` 留空会禁用 `/v0/management`。
- 本地状态:
  - 未发现已有 `~/.cli-proxy-api` 认证目录；短跑启动时已创建该目录。
  - 未发现既有 `cli-proxy-api` 进程。
  - 端口 `8317` 原本未占用。
- 新增配置: 写入 `/home/loviya/cpa/config.yaml`，只绑定 `127.0.0.1:8317`，TLS 关闭，远程管理关闭，control panel 关闭，使用 `/home/loviya/.cli-proxy-api` 作为认证目录。未写入任何真实上游凭据。
- 验证:
  - sandbox 内启动失败，错误是 `listen tcp 127.0.0.1:8317: socket: operation not permitted`，属于 sandbox 本地监听限制。
  - 宿主机权限短跑验证成功，`timeout` 到时退出前已打印 `API server started successfully on: 127.0.0.1:8317`。
  - 已用 `tmux -L cpa new-session -d -s cli-proxy-api ...` 启动常驻服务。
  - `ss -ltnp` 确认 `cli-proxy-api` 监听 `127.0.0.1:8317`。
  - 不带 API key 访问 `/v1/models` 返回 `401 Missing API key`。
  - 带本地配置 key 访问 `/v1/models` 返回 `200` 和空模型列表，符合当前无上游账号状态。
- 当前结论: CPA 服务本体已经可用；要真正调用模型，需要下一步登录 Codex/Claude/Gemini 或在配置里添加上游 API key。

## 2026-06-06 17:30 +0800

- 用户中断 Codex device-code 登录流程，转而要求打开 CPA 网页。
- 状态确认:
  - `cli-proxy-api` 进程仍在运行，监听 `127.0.0.1:8317`。
  - `GET /` 返回 API 状态 JSON：包含 `POST /v1/chat/completions`、`POST /v1/completions`、`GET /v1/models`。
  - `/v0/management/` 返回 404，因为当前配置 `remote-management.secret-key` 留空且 `disable-control-panel: true`，管理面板关闭。
- 操作: 已执行 `xdg-open http://127.0.0.1:8317/` 打开本地 CPA 服务页。
- 下一步: 若用户需要图形管理面板，需要修改配置启用 Management API 和 control panel，并重启 CPA 服务。

## 2026-06-06 17:34 +0800

- 用户要求检查当前情况。
- 运行态:
  - `cli-proxy-api` 进程仍在运行，PID `861176`。
  - `ss -ltnp` 确认监听 `127.0.0.1:8317`。
  - `tmux -L cpa list-sessions` 确认 `cli-proxy-api` 会话存在。
- 认证状态:
  - `/home/loviya/.cli-proxy-api/` 下已有 1 个 Codex auth JSON 文件。
  - CPA 日志记录 `auth file changed (CREATE)`，说明服务已检测到该认证文件。
- 模型与调用验证:
  - 带本地 API key 请求 `/v1/models` 返回 200，模型列表不为空。
  - `gpt-5.3-codex` 最小请求失败，原因是当前 ChatGPT 账号不支持该 Codex 专用模型。
  - `gpt-5.4-mini` 最小请求成功，返回 `OK`；说明 CPA -> Codex/ChatGPT 上游链路可用。
- 当前结论: 本地 CPA 已可作为 OpenAI-compatible API 使用；建议默认先用 `gpt-5.4-mini` 或模型列表中的通用 GPT 模型。

## 2026-06-06 17:38 +0800

- 用户要求立即启用 CPA 网页管理面板，并提供管理密码。
- 配置变更:
  - `/home/loviya/cpa/config.yaml` 已启用 `remote-management.secret-key`。
  - `remote-management.disable-control-panel` 已改为 `false`。
  - `allow-remote` 保持 `false`，因此管理入口仍只允许本机访问。
  - 未在 worklog 中记录管理密码明文。
- 服务操作:
  - 已重启 `tmux -L cpa` 下的 `cli-proxy-api` 会话。
  - 重启后 PID 为 `890786`，监听 `127.0.0.1:8317`。
  - 日志显示 management asset 已通过 fallback 页面下载并更新成功。
- 面板入口:
  - 测试 `/management.html` 返回 `200 text/html`。
  - 已执行 `xdg-open http://127.0.0.1:8317/management.html` 打开管理面板。

## 2026-06-06 17:40 +0800

- 用户要求在 zsh 里设置 `cpa` function，用 `cpa` 命令直接打开管理面板。
- 检查: 未发现已有同名 `cpa` alias/function。
- 变更: 在 `/home/loviya/.zshrc` 添加 `cpa()`，执行 `xdg-open http://127.0.0.1:8317/management.html`。
- 验证: `zsh -ic 'whence -f cpa'` 能加载并显示该函数；非完整交互验证中 Powerlevel10k/gitstatus 有初始化提示，不影响函数定义。
