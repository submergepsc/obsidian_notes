---
id: 20260520-codex-api-mimo-pay-self-upstream-fix
name: codex-api-mimo-pay-self 上游 502 修复
slug: codex-api-mimo-pay-self-upstream-fix
cwd: /home/loviya
summary: "定位并修复 codex-api-mimo-pay-self：本机 18793 代理 health 正常但上游 MiMo 请求 502，切回可用备份 key 和旧域名后最小 Codex 请求返回 ok。"
tags:
  - codex-api
  - mimo
  - proxy
  - api
---

# Current Snapshot

- workflow id: 20260520-codex-api-mimo-pay-self-upstream-fix
- current status: 已完成
- current goal: 查清并修复当前 `codex-api-mimo-pay-self` 502。
- current blocker: 无。
- next step: 无；如再次 502，先检查 `mimo.env` 的上游域名和 key 形态。
- tags: codex-api, mimo, proxy, api
- summary: `127.0.0.1:18793/health` 正常但 `/v1/responses` 失败；新域名 `api.mimo-v2.com` 在本机 TLS 失败，当前 `tp-cp...` key 对旧域名 401。备份 `sk-c6...` key + 旧域名 `api.xiaomimimo.com` 验证 200。已恢复该组合并重启代理，`codex-api-mimo-pay-self exec ... "只回复 ok"` 成功。

## Key Results

- 当前 `codex-api-mimo-pay-self` 是 `/home/loviya/.codex-api-mimo-pay-self` 链路，不是 `/home/loviya/.codex-api-mimo-free-self` 的 mimi3/8000 链路。
- 本机代理：`127.0.0.1:18793`，脚本 `/home/loviya/.codex-api-mimo-pay-self/mimo_responses_proxy.py`。
- 问题现象：health 返回 `{"ok": true}`，但真实请求连续 502，脱敏错误摘要为 `SSL: UNEXPECTED_EOF_WHILE_READING`。
- 网络测试：`api.mimo-v2.com` TLS 失败；`api.xiaomimimo.com` TLS 正常，HEAD 返回 405，说明端点可达。
- 当前坏 key 形态：`tp-cp...`，对旧域名最小请求返回 401。
- 可用备份 key 形态：`sk-c6...`，对旧域名 + `mimo-v2.5-pro` 最小 Chat Completions 请求返回 200 和 `ok`。

## Changes

- 备份坏配置：`/home/loviya/.codex-api-mimo-pay-self/mimo.env.bak-20260520-0059-broken`。
- 恢复 key 来源：`/home/loviya/.codex-api-mimo-pay-self/mimo.env.bak-20260516-134543`。
- 修改 `/home/loviya/.codex-api-mimo-pay-self/mimo.env`：
  - `MIMO_CHAT_COMPLETIONS_URL=https://api.xiaomimimo.com/v1/chat/completions`
  - `MIMO_MODEL=mimo-v2.5-pro`
  - key 使用已验证可用的备份 key；不在日志中记录完整值。
- 停止旧 `mimo_responses_proxy.py`，让 `/home/loviya/.local/bin/codex-api-mimo-pay-self` 按新 env 拉起新代理。
- 更新 note：`/home/loviya/.codex/codex_notes/requested/2026-05-20-codex-api-mimo-pay-self-vs-ds-config.md`。

## Verification

- `curl -fsS http://127.0.0.1:18793/health` 返回 `{"ok": true}`。
- 新代理进程：`python3 /home/loviya/.codex-api-mimo-pay-self/mimo_responses_proxy.py`。
- `/home/loviya/.local/bin/codex-api-mimo-pay-self exec --skip-git-repo-check --sandbox read-only "只回复 ok"` 成功返回 `ok`。
- 代理日志出现新的 `POST /v1/responses HTTP/1.1` `200`。
