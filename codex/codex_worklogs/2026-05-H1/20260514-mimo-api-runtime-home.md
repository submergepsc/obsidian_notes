---
id: 20260514-mimo-api-runtime-home
name: Mimo API Runtime Home
slug: mimo-api-runtime-home
cwd: /home/loviya
summary: 创建并修复面向小米 MiMo 的 Codex runtime home `.codex-api-mimo-pay-self` 和启动器 `codex-api-mimo-pay-self`。
tags:
  - codex
  - api-runtime
  - mimo
priority: normal
---

# Mimo API Runtime Home

## 当前快照

- 状态: 已完成
- 目标: 完成并验证由 `codex-api-mimo-pay-self` 启动的独立小米 MiMo Codex runtime home。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-16 13:52:47 +0800

## 关键结果

- 已创建 `/home/loviya/.codex-api-mimo-pay-self` as an independent runtime home.
- 已新增 shared symlinks for `AGENTS.md`, `continue.md`, `worklogs`, `skills`, `rules`, `memories`, `vendor_imports`, and `plugins`.
- Kept account/runtime state local to `.codex-api-mimo-pay-self`: `config.toml`, `mimo.env`, `installation_id`, `sessions/`, `log/`, `tmp/`, `.tmp/`, `cache/`, and future sqlite/log/history files.
- 已新增 `/home/loviya/.codex-api-mimo-pay-self/codex-api-mimo-pay-self` and `/home/loviya/.local/bin/codex-api-mimo-pay-self`.
- 已新增 `/home/loviya/.codex-api-mimo-pay-self/mimo_responses_proxy.py`, converting Codex Responses API calls to OpenAI-compatible Chat Completions calls.
- Originally configured Xiaomi MiMo settings 不带 recording the API key in this worklog; these were superseded on 2026-05-16:
  - endpoint: `https://api.xiaomimimo.com/v1/chat/completions`
  - model: `xiaomi/mimo-v2-flash`
  - local proxy: `http://127.0.0.1:18793/v1`
- 已新增 `codex-api-mimo-pay-self` aliases to `/home/loviya/.bashrc` and `/home/loviya/.zshrc`.
- 已更新 `/home/loviya/.codex/AGENTS.md` so `.codex-api-mimo-pay-self` is documented as a Xiaomi MiMo-specific API runtime home.
- Verified `codex-api-mimo-pay-self --version` 返回 `codex-cli 0.130.0`.
- Verified the runtime symlink layout and AGENTS/bash/zsh references 带 targeted reads.
- 已修复 the local Responses streaming proxy so Codex CLI no longer reports `OutputTextDelta 不带 active item`.
- Verified live MiMo access 带 `codex-api-mimo-pay-self exec --skip-git-repo-check --sandbox read-only "只回复 ok"` after running outside the sandbox so the local proxy could bind and reach the network.
- 已确认 MiMo session/runtime artifacts are written under `/home/loviya/.codex-api-mimo-pay-self`, including `sessions/`, `state_5.sqlite`, and `logs_2.sqlite`.
- 已修复 the MiMo proxy so Codex tool calls are forwarded through Chat Completions `tools` and 返回 as Responses `function_call` items.
- 已新增 `enable_thinking: false` to upstream MiMo requests 因为 MiMo rejects tool-result follow-up turns in thinking mode unless `reasoning_content` is replayed.
- Verified `codex-api-mimo-pay-self exec --skip-git-repo-check --sandbox read-only "请使用 shell 工具运行 pwd，然后只回复 pwd 的输出。"` actually executed `/usr/bin/bash -lc pwd` and 返回 `/home/loviya`.
- 已更新 `/home/loviya/.codex-api-mimo-pay-self/codex-api-mimo-pay-self` to start the local proxy 带 `setsid -f`, so it remains listening after `codex exec` exits.
- 已更新 the configured upstream MiMo endpoint and default model to the current OpenAI-compatible documentation:
  - endpoint: `https://api.mimo-v2.com/v1/chat/completions`
  - model: `mimo-v2.5-pro`
- Rotated `MIMO_API_KEY` after decrypting the user-provided token 带 CryptoJS `RabbitLegacy` and passphrase `linux.do`; the worklog intentionally does not record the plaintext key.
- Backed up `/home/loviya/.codex-api-mimo-pay-self/mimo.env` before rotation:
  - `/home/loviya/.codex-api-mimo-pay-self/mimo.env.bak-20260516-134543`
  - `/home/loviya/.codex-api-mimo-pay-self/mimo.env.bak-20260516-134636-encrypted`
- 已新增 a requested `codex_notes` entry documenting the RabbitLegacy decrypt/encrypt procedure 不带 recording real secrets:
  - `/home/loviya/.codex/codex_notes/requested/2026-05-16-cryptojs-rabbitlegacy-secret-decrypt-encrypt.md`

## Create Mimo-Specific Codex Runtime

- 更新时间: 2026-05-15 00:50:02 +0800
- 工作目录: `/home/loviya`
- 来源指令: `我给你一个mimo的api,可以新建一个.codex-api-mimo-pay-self的codex环境吗`
- 问题:
  - 用户需要 a new Codex runtime home dedicated to Mimo API use, analogous to the existing DeepSeek-specific `.codex-api-ds`.
- 改进:
  - Built `.codex-api-mimo-pay-self` 带 isolated runtime state, shared managed content symlinks, a launcher, shell aliases, and a local Responses-to-Chat-Completions proxy.
- 结果:
  - The environment is configured and structurally verified, but live request validation was not completed before the user paused for the night.
- 下一步:
  - Validate the live MiMo request path 带 `codex-api-mimo-pay-self exec --skip-git-repo-check --sandbox read-only "只回复 ok"`.

## Resume From API 启动 问候

- 更新时间: 2026-05-15 09:47:11 +0800
- 工作目录: `/home/loviya`
- 来源指令: `hi`
- 问题:
  - The session started through the API 带 `CODEX_HOME` empty, which does not match the expected dedicated API runtime homes.
  - The current directory matched an unfinished workflow, but the user provided only a greeting and no explicit instruction to run the pending live MiMo validation.
- 改进:
  - Resumed this workflow for continuity and recorded the runtime-home mismatch before account-specific runtime changes.
- 结果:
  - No MiMo API validation command was run in response to the greeting alone.
- 下一步:
  - If requested, validate the live MiMo request path 带 `codex-api-mimo-pay-self exec --skip-git-repo-check --sandbox read-only "只回复 ok"`.

## Validate 实时 Mimo Codex API Path

- 更新时间: 2026-05-15 09:56:24 +0800
- 工作目录: `/home/loviya`
- 来源指令: `继续完成我的mimo的codexapi接入`
- 问题:
  - The first validation attempt inside the sandbox failed 因为 the local proxy could not bind to `127.0.0.1:18793`.
  - The first host-side validation reached MiMo but Codex CLI logged `OutputTextDelta 不带 active item`, caused by an incomplete streamed Responses event shape.
- 改进:
  - 已更新 `/home/loviya/.codex-api-mimo-pay-self/mimo_responses_proxy.py` to include `content: []` on `response.output_item.added` and `item_id` on content/delta/done events.
  - Re-ran the live validation command outside the sandbox so the local proxy could bind and make the upstream MiMo request.
- 结果:
  - `codex-api-mimo-pay-self exec --skip-git-repo-check --sandbox read-only "只回复 ok"` completed successfully 带 provider `mimo`, model `xiaomi/mimo-v2-flash`, and no streaming parser error.
  - Runtime/session files were created under `/home/loviya/.codex-api-mimo-pay-self`, confirming account-home isolation for this launcher.
- 下一步:
  - 无

## Repair Mimo Tool-Call Loop

- 更新时间: 2026-05-15 11:20:51 +0800
- 工作目录: `/home/loviya`
- 来源指令: `我是要你帮我修改.codex-api-mimo-pay-self`
- 问题:
  - `codex-api-mimo-pay-self` could answer simple prompts, but for file-editing work it kept returning plan text such as "I will read the file" and never executed shell or patch tools.
  - The MiMo Responses proxy converted requests to plain Chat Completions messages but did not forward Codex `tools`, so the upstream model had no native way to call `exec` or `apply_patch`.
  - After adding tool forwarding, MiMo rejected the tool-result follow-up turn 带 `The reasoning_content in the thinking mode must be passed back to the API.`
- 改进:
  - 已更新 `/home/loviya/.codex-api-mimo-pay-self/mimo_responses_proxy.py` to convert Responses `tools` into Chat Completions `tools` 带 `tool_choice: auto`.
  - Converted upstream Chat Completions `tool_calls` back into Responses `function_call` output items for Codex CLI.
  - Converted Responses `function_call` and `function_call_output` history back into assistant/tool Chat Completions messages.
  - 已新增 `enable_thinking: false` to MiMo upstream requests so tool-result follow-up turns are accepted.
  - Kept a fallback cache for `reasoning_content` by tool call ID in case thinking mode is re-enabled later.
  - 已更新 the launcher to start the proxy 带 `setsid -f` 而不是 a shell background job, avoiding proxy shutdown after one-off `codex exec` validation.
- 结果:
  - `python3 -m py_compile /home/loviya/.codex-api-mimo-pay-self/mimo_responses_proxy.py` succeeds.
  - Live validation outside the sandbox shows Codex executing `/usr/bin/bash -lc pwd` through MiMo and returning `/home/loviya`.
  - `ss -ltnp` confirms `python3 /home/loviya/.codex-api-mimo-pay-self/mimo_responses_proxy.py` remains listening on `127.0.0.1:18793` after validation.
- 下一步:
  - 无

## Sync Mimo Endpoint And Model ID

- 更新时间: 2026-05-16 12:46:20 +0800
- 工作目录: `/home/loviya`
- 来源指令: `查看一下codex-api-mimo-pay-self的配置,这个有什么问题没有`
- 问题:
  - `/home/loviya/.codex-api-mimo-pay-self/mimo.env` still used `https://api.xiaomimimo.com/v1/chat/completions`.
  - `/home/loviya/.codex-api-mimo-pay-self/config.toml` and `mimo.env` still used `xiaomi/mimo-v2-flash`, while the current MiMo OpenAI-compatible model IDs are unprefixed, such as `mimo-v2.5-pro`.
  - The user's Trae screenshot showed a 400 `Param Incorrect` error while 使用 the older domain.
- 改进:
  - 已更新 `MIMO_CHAT_COMPLETIONS_URL` to `https://api.mimo-v2.com/v1/chat/completions`.
  - 已更新 the Codex default MiMo model to `mimo-v2.5-pro`.
  - Kept Codex itself on the local Responses proxy at `http://127.0.0.1:18793/v1`, 因为 Codex needs Responses API compatibility and MiMo exposes Chat Completions upstream.
- 结果:
  - `python3 -m py_compile /home/loviya/.codex-api-mimo-pay-self/mimo_responses_proxy.py` succeeds.
  - Targeted reads confirmed the new endpoint and model are written.
- 下一步:
  - For Trae, use OpenAI Chat Completions 带 base URL `https://api.mimo-v2.com/v1` and model `mimo-v2.5-pro`.

## Rotate Mimo API Key From Encrypted Token

- 更新时间: 2026-05-16 13:46:06 +0800
- 工作目录: `/home/loviya`
- 来源指令: `上面给的密匙是加密的`
- 问题:
  - The first replacement wrote the encrypted token directly into `MIMO_API_KEY`, which is not usable as an API key.
  - The source token was encrypted 带 Rabbit-compatible tooling and passphrase `linux.do`.
- 改进:
  - Preserved the previous usable `mimo.env` backup as `/home/loviya/.codex-api-mimo-pay-self/mimo.env.bak-20260516-134543`.
  - Preserved the intermediate encrypted-token file as `/home/loviya/.codex-api-mimo-pay-self/mimo.env.bak-20260516-134636-encrypted`.
  - Used the locally installed `crypto-js` package and `RabbitLegacy` decryptor to derive the plaintext token, then wrote only the plaintext token into `MIMO_API_KEY`.
- 结果:
  - `/home/loviya/.codex-api-mimo-pay-self/mimo.env` now contains the decrypted MiMo token.
  - Verification confirmed `mimo.env` and both backups have `600` permissions.
  - Verification confirmed the active key is single-line, length 51, and has the expected token prefix 不带 printing the full secret.
- 下一步:
  - 无

## Preserve RabbitLegacy Secret Handling 流程

- 更新时间: 2026-05-16 13:52:47 +0800
- 工作目录: `/home/loviya`
- 来源指令: `把这个解密和加密的知识和过程,写到notes里面`
- 问题:
  - The RabbitLegacy compatibility detail is easy to lose if it remains only in chat history.
  - A durable note should be reusable while avoiding plaintext secrets and the specific encrypted token.
- 改进:
  - 已新增 `/home/loviya/.codex/codex_notes/requested/2026-05-16-cryptojs-rabbitlegacy-secret-decrypt-encrypt.md`.
  - 已更新 `/home/loviya/.codex/codex_notes/INDEX.md`.
  - Included placeholder-based decrypt, metadata-only verification, encrypt, and round-trip examples.
- 结果:
  - The requested note is available through the Obsidian-backed `codex_notes` symlink.
  - Secret checks confirmed the note does not contain the real encrypted token prefix or decrypted token prefix.
- 下一步:
  - 无
