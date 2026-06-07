---
id: 20260519-codex-api-mimo-free-self-recheck
name: codex-api-mimo-free-self 复查与本地修复
slug: codex-api-mimo-free-self-recheck
cwd: /home/loviya
summary: "复查并修复 codex-api-mimo-free-self：修正 wrapper 目录，清理坏 ALL_PROXY，重启 Pinggy 和 mimi3，active_clients 已恢复为 1。"
tags: [codex-api, mimo1, mimi3, gateway, proxy]
---

# codex-api-mimo-free-self 复查与本地修复

## Current Snapshot

- workflow id: `20260519-codex-api-mimo-free-self-recheck`
- current status: `已完成`
- current goal: 让 `codex-api-mimo-free-self` 可用。
- current blocker: 无。
- next step: 无。
- tags: codex-api, mimo1, mimi3, gateway, proxy
- summary: 已将 `/home/loviya/.codex-api-mimo-free-self/codex-api-mimo-free-self` 默认目录从不存在的 `/home/loviya/code/mimo3` 改为真实 `/home/loviya/code/mimi3`；停止继承 `ALL_PROXY=socks://127.0.0.1:7897/` 的旧 8000 进程；启动新 Pinggy 隧道并更新 `.env`；重启 `mimi3-gateway` 后 `active_clients=1`，最小 `/v1/responses` 请求成功返回。

## Key Results

- `codex-api-mimo-free-self` 命令入口可执行：`codex-cli 0.131.0`。
- `CODEX_HOME=/home/loviya/.codex-api-mimo-free-self codex debug models` 可解析 `mimo-v2.5-pro`。
- 真实网络命名空间中 8000 正常监听，进程为新启动的 `/home/loviya/code/mimi3/.venv/bin/python main.py`。
- 新进程环境已清掉 `ALL_PROXY/all_proxy=socks://...`，保留 `HTTP_PROXY/HTTPS_PROXY=http://127.0.0.1:7897/`。
- 新 Pinggy 地址：`https://mabkv-58-249-112-20.run.pinggy-free.link`。
- `/home/loviya/code/mimi3/.env` 已更新为 `WS_TUNNEL_URL=wss://mabkv-58-249-112-20.run.pinggy-free.link/ws`。
- 当前 tmux 会话：
  - `tmux -L codex-mimo2`: `pinggy-mimi3`
  - `tmux -L codex-mimo2`: `mimi3-gateway`
- 最新状态：远端 bridge 回连成功，日志显示 `内网节点已接入`，`active_clients=1`。

## Changes

- 修改 `/home/loviya/.codex-api-mimo-free-self/codex-api-mimo-free-self`
  - 默认 `MIMO3_DIR` 改为 `/home/loviya/code/mimi3`。
  - 启动 mimi3 时清理 `ALL_PROXY/all_proxy` 的 `socks://` 形式，避免 `httpx` 报 `Unknown scheme for proxy URL`。
  - 本地代理端口不可用时会清理代理环境，避免死代理传给 mimi3。
- 修改 `/home/loviya/code/mimi3/.env`
  - `WS_TUNNEL_URL` 更新为新的 Pinggy 隧道地址。

## Verification

- `bash -n /home/loviya/.codex-api-mimo-free-self/codex-api-mimo-free-self`：通过。
- `ss -ltnp`：`0.0.0.0:8000` 由 `python` 监听。
- `curl http://127.0.0.1:8000/api/system/status`：返回 `{"active_clients":1}`。
- `curl http://127.0.0.1:8000/v1/models`：返回 `mimo-v2.5-pro` 等模型。
- `/home/loviya/.local/bin/codex-api-mimo-free-self --version`：返回 `codex-cli 0.131.0`。
- `curl http://127.0.0.1:8000/v1/responses ...`：成功返回 `pong` 流式响应。

## Commands

- 停止旧进程：`pkill -TERM -f '/home/loviya/code/mimi3/.venv/bin/python main.py'`。
- 重启网关：`tmux -L codex-mimo2 new-session -d -s mimi3-gateway ... /home/loviya/code/mimi3/.venv/bin/python main.py`。
- 启动新隧道：`tmux -L codex-mimo2 new-session -d -s pinggy-mimi3 ... a.pinggy.io`。
