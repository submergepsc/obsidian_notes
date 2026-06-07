---
id: 20260518-codex-api-mimo-free-self-restart
name: codex-api-mimo-free-self 启动
slug: codex-api-mimo-free-self-restart
cwd: /home/loviya/code/mimi3
summary: 按用户要求启动 codex-api-mimo-free-self 依赖的本机 mimi3 网关与 Pinggy 隧道，并验证 Codex API 入口。
tags:
  - codex-api
  - mimo1
  - mimi3
  - startup
---

# codex-api-mimo-free-self 启动

## Current Snapshot

- workflow id: `20260518-codex-api-mimo-free-self-restart`
- current status: `已完成`
- current goal: 启动 `codex-api-mimo-free-self` 可用所需的 `mimi3` 本机网关和 Pinggy 回连隧道。
- current blocker: Claw 云端实例创建失败，`active_clients=0`；`codex-api-mimo-free-self` 已启动但实际请求需等待后端节点接入。
- next step: 如需真实模型调用，处理 Claw 账户/云端实例 `DESTROYED` 问题，或等待网关自动重试。
- tags: `codex-api`, `mimo1`, `mimi3`, `startup`
- summary: 已启动 `pinggy-mimi3`、`mimi3-gateway` 和 `codex-api-mimo-free-self` 三个 tmux 会话；本机 8000 监听，`/v1/models` 可用，Codex UI 已进入 `mimo-v2.5-pro`。当前 `active_clients=0`，日志显示 Claw 创建状态为 `DESTROYED` 并持续重试。

## Key Results

- Pinggy 新地址：`https://macmh-38-207-136-179.run.pinggy-free.link`
- `.env` 已更新：`WS_TUNNEL_URL=wss://macmh-38-207-136-179.run.pinggy-free.link/ws`
- tmux server：`tmux -L codex-mimo2`
- tmux sessions:
  - `pinggy-mimi3`
  - `mimi3-gateway`
  - `codex-api-mimo-free-self`
- `codex-api-mimo-free-self` 已启动到交互界面，model 为 `mimo-v2.5-pro`，目录为 `/home/loviya/code/mimi3`。

## Commands

- `rg -n "codex-api-mimo-free-self|codex_api_mimo_free_self|mimo1|mimi3" ...`：定位到 requested note 和旧 worklog。
- `ss -ltnp`：启动前没有 8000 监听。
- `tmux -L codex-mimo2 list-sessions`：启动前无该 tmux server。
- `tmux -L codex-mimo2 new-session -d -s pinggy-mimi3 ...`：启动 Pinggy 隧道。
- `tmux -L codex-mimo2 capture-pane -pt pinggy-mimi3 -S -200`：获取新地址 `https://macmh-38-207-136-179.run.pinggy-free.link`。
- `tmux -L codex-mimo2 new-session -d -s mimi3-gateway ... .venv/bin/python main.py`：启动本机网关。
- `ss -ltnp`：确认 `python` 监听 `0.0.0.0:8000`。
- `curl -fsS http://127.0.0.1:8000/api/system/status`：返回 `{"active_clients":0}`。
- `curl -fsS http://127.0.0.1:8000/v1/models`：返回 `mimo-v2.5-pro` 等模型列表。
- `/home/loviya/.local/bin/codex_api_mimo_free_self --version`：返回 `codex-cli 0.130.0`。
- `CODEX_HOME=/home/loviya/.codex-api-mimo-free-self codex debug models`：成功解析 `mimo-v2.5-pro`。
- `tmux -L codex-mimo2 new-session -d -s codex-api-mimo-free-self ... codex_api_mimo_free_self`：启动 Codex API mimo1 交互界面。
- `tmux -L codex-mimo2 capture-pane -pt codex-api-mimo-free-self -S -80`：界面已启动，提示 `mimi3 当前没有在线 Claw 节点`，model 为 `mimo-v2.5-pro`。
