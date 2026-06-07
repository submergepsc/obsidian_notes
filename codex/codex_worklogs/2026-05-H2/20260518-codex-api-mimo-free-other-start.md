---
id: 20260518-codex-api-mimo-free-other-start
name: Codex API Mimo2 Start
slug: codex-api-mimo-free-other-start
cwd: /home/loviya
summary: 启动用户所称“之前的 codex-api-mimo-free-other”，核实现有配置实际为 mimi3 本地网关和 codex-api-mimo-free-self。
tags:
  - codex-api
  - mimo
  - mimo2api
  - mimi3
  - startup
---

# Codex API Mimo2 Start

## 当前快照

- 工作流 ID: 20260518-codex-api-mimo-free-other-start
- 当前状态: 已完成
- 当前目标: 启动用户所称“之前的 codex-api-mimo-free-other”相关服务，确认可用入口
- 当前阻塞: none；但本机不存在独立 `/home/loviya/.codex-api-mimo-free-other` 或 `codex-api-mimo-free-other` 启动器，实际恢复的是 `mimo2api`/`mimi3` 网关和既有 `codex_api_mimo_free_self` 入口
- 下一步: none
- 标签: codex-api, mimo, mimo2api, mimi3, startup
- 摘要: 已在 `tmux -L codex-mimo2` 下启动 `pinggy-mimi3` 和 `mimi3-gateway`，本机 API `http://127.0.0.1:8000/v1` 可用，`active_clients=1`；已通过本地 `model_catalog_json` 让 Codex 正确识别 `mimo-v2.5-pro`。

## 关键结果

- 已确认存在 `/home/loviya/.codex-api-mimo-pay-self` 和 `/home/loviya/.codex-api-mimo-free-self`，未发现 `/home/loviya/.codex-api-mimo-free-other`。
- 持久 note `/home/loviya/.codex/codex_notes/requested/2026-05-18-mimi3-codex-api-mimo-free-self-local-gateway.md` 说明 `mimo2api` 是 `/home/loviya/code/mimi3` 内的本地网关模块，不是独立 `codex-api-mimo-free-other` home。
- `codex_api_mimo_free_self` 启动器使用 `CODEX_HOME=/home/loviya/.codex-api-mimo-free-self`，访问 `http://127.0.0.1:8000/v1`。
- `curl http://127.0.0.1:8000/api/system/status` 当前失败，说明本地 `mimi3` 网关尚未运行。
- 2026-05-18 11:04 启动新 Pinggy 隧道，地址为 `https://fwhbw-2409-895a-2228-6f-d118-c26a-5833-6948.run.pinggy-free.link`。
- 已更新 `/home/loviya/code/mimi3/.env` 的 `WS_TUNNEL_URL` 为 `wss://fwhbw-2409-895a-2228-6f-d118-c26a-5833-6948.run.pinggy-free.link/ws`。
- 已在 `tmux -L codex-mimo2` 下启动两个会话：`pinggy-mimi3` 和 `mimi3-gateway`。
- 2026-05-18 11:07 验证 `curl -fsS http://127.0.0.1:8000/api/system/status` 返回 `{"active_clients":1}`。
- 2026-05-18 11:05 验证 `curl -fsS http://127.0.0.1:8000/v1/models` 返回模型列表，包含 `mimo-v2.5-pro`。
- 2026-05-18 11:39 用户报告 Codex TUI 告警 `Model metadata for mimo-v2.5-pro not found`。
- 已在 `/home/loviya/.codex-api-mimo-free-self/config.toml` 增加 `model_context_window = 1048576` 和 `model_auto_compact_token_limit = 900000`，匹配网关 `/v1/models` 返回的上下文规模。
- 单独的 `model_context_window` 不足以消除告警；Codex 0.130.0 需要通过 `model_catalog_json` 为未知 slug 提供完整模型 catalog。
- 已新增 `/home/loviya/.codex-api-mimo-free-self/model_catalog.json`，并在 `/home/loviya/.codex-api-mimo-free-self/config.toml` 添加 `model_catalog_json = "/home/loviya/.codex-api-mimo-free-self/model_catalog.json"`。
- 验证 `CODEX_HOME=/home/loviya/.codex-api-mimo-free-self codex debug models` 能解析并只返回 `mimo-v2.5-pro`。
- 验证命令 `CODEX_HOME=/home/loviya/.codex-api-mimo-free-self MIMO1_API_KEY=mimo-local codex exec -m mimo-v2.5-pro --skip-git-repo-check --sandbox read-only --json "只回复 ok"` 成功返回 `ok`，未再出现 metadata 告警。
- 验证期间远端 Claw 节点一度断开导致 503/502，随后自动重连恢复；这是网关节点稳定性问题，不是 metadata 配置问题。

## 命令

- `rg` 搜索 `mimo2|codex-api-mimo-free-other|api-mimo2`：仅命中持久 note 中的 `mimo2api`。
- `find /home/loviya -maxdepth 2 -name '*mimo2*'`：未发现 `mimo2` 账户 home 或启动器。
- `curl -fsS http://127.0.0.1:8000/api/system/status`：连接失败。
- `tmux -L codex-mimo2 new-session -d -s pinggy-mimi3 ...`：启动 Pinggy 临时隧道。
- `tmux -L codex-mimo2 new-session -d -s mimi3-gateway ... .venv/bin/python main.py`：启动本机网关。
- `ss -ltnp | rg ':8000|State'`：确认 `python` 进程监听 `0.0.0.0:8000`。
- `codex exec -m mimo-v2.5-pro ... "只回复 ok"`：验证 metadata 告警消失和模型调用成功。
