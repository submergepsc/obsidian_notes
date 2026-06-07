---
id: 20260517-mimi3-service-start
name: mimi3 service start and codex_api_mimo_free_self
slug: mimi3-service-start
cwd: /home/loviya/code/mimi3
summary: 启动 mimi3 网关，打通 Claw 节点，并新增 codex_api_mimo_free_self 本地 Codex API 启动器。
tags:
  - mimi3
  - service-start
  - codex-api
  - mimo
---

## 当前快照

- 工作流 ID: 20260517-mimi3-service-start
- 当前状态: 已完成
- 当前目标: 让 mimi3 网关可用，并创建 `codex_api_mimo_free_self` 通过本地 mimi3 `/v1/responses` 作为 Codex API provider。
- 当前阻塞: none
- 下一步: none
- 标签: mimi3, service-start, codex-api, mimo
- 摘要: 本地服务 `http://127.0.0.1:8000` 可用，Pinggy 隧道 `https://ugwzo-104-234-0-177.run.pinggy-free.link` 已连通，`active_clients=1`。新增 `/home/loviya/.codex-api-mimo-free-self` 和 `/home/loviya/.local/bin/codex_api_mimo_free_self`。2026-05-18 按用户纠偏增强记录规则：worklog 记录具体会话解决流程，notes 保留最终复用结论，并新增 requested notes 专用索引。

## 关键结果

- 已创建 project `.venv` and installed runtime dependencies via `requirements.txt`.
- 已新增 `requirements.txt` and `.gitignore` runtime ignores for gateway db/lock files.
- Imported one Xiaomi AI Studio credential into `users/`; account status reached `AVAILABLE`.
- Set `.env` `WS_TUNNEL_URL=wss://ugwzo-104-234-0-177.run.pinggy-free.link/ws`.
- 已开始 `mimi3` 带 proxy env vars unset to avoid `httpx` `socks://` scheme errors.
- 已创建 `codex_api_mimo_free_self` launcher 使用 `CODEX_HOME=/home/loviya/.codex-api-mimo-free-self` and provider `base_url=http://127.0.0.1:8000/v1`, `wire_api=responses`, model `mimo-v2.5-pro`.

## 命令

- `curl http://127.0.0.1:8000/api/system/status` 返回 `active_clients=1`.
- `curl https://ugwzo-104-234-0-177.run.pinggy-free.link/api/system/status` 返回 `active_clients=1`.
- `codex_api_mimo_free_self --version` should delegate to the installed `codex` binary.

## 产物

- `/home/loviya/.codex-api-mimo-free-self/config.toml`
- `/home/loviya/.codex-api-mimo-free-self/codex-api-mimo-free-self`
- `/home/loviya/.local/bin/codex_api_mimo_free_self`
- `/home/loviya/.local/bin/codex-api-mimo-free-self`
- `/home/loviya/.codex/codex_notes/requested/2026-05-18-mimi3-codex-api-mimo-free-self-local-gateway.md`
- `/home/loviya/.codex/codex_notes/requested/INDEX.md`

## 决策

- 2026-05-18: 用户明确纠偏记录策略：不要让 notes 承担完整过程记录；worklog 应更详细地保存每个会话的解决流程、尝试路径、失败原因、配置变化和验证结果，notes 反而要更简洁，只沉淀最终结果和可复用命令。
- 2026-05-18: 已将该策略写入 `/home/loviya/.codex/AGENTS.md` 的 Worklogs/Notes 规则，并为 `codex_notes/requested/` 新增专用 `INDEX.md`。全局 `codex_notes/INDEX.md` 仍作为全量索引。
