---
id: 20260514-mimo-api-runtime-home
name: Mimo API Runtime Home
slug: mimo-api-runtime-home
cwd: /home/loviya
summary: Create and repair a Xiaomi MiMo-oriented Codex runtime home named .codex-api-mimo and launcher codex-api-mimo.
tags:
  - codex
  - api-runtime
  - mimo
priority: normal
---

# Mimo API Runtime Home

## Current Snapshot

- status: 已完成
- goal: Finish and verify a separate Xiaomi MiMo-oriented Codex runtime home launched by `codex-api-mimo`.
- blocker: none
- next: none
- updated: 2026-05-16 13:52:47 +0800

## Key Results

- Created `/home/loviya/.codex-api-mimo` as an independent runtime home.
- Added shared symlinks for `AGENTS.md`, `continue.md`, `worklogs`, `skills`, `rules`, `memories`, `vendor_imports`, and `plugins`.
- Kept account/runtime state local to `.codex-api-mimo`: `config.toml`, `mimo.env`, `installation_id`, `sessions/`, `log/`, `tmp/`, `.tmp/`, `cache/`, and future sqlite/log/history files.
- Added `/home/loviya/.codex-api-mimo/codex-api-mimo` and `/home/loviya/.local/bin/codex-api-mimo`.
- Added `/home/loviya/.codex-api-mimo/mimo_responses_proxy.py`, converting Codex Responses API calls to OpenAI-compatible Chat Completions calls.
- Originally configured Xiaomi MiMo settings without recording the API key in this worklog; these were superseded on 2026-05-16:
  - endpoint: `https://api.xiaomimimo.com/v1/chat/completions`
  - model: `xiaomi/mimo-v2-flash`
  - local proxy: `http://127.0.0.1:18793/v1`
- Added `codex-api-mimo` aliases to `/home/loviya/.bashrc` and `/home/loviya/.zshrc`.
- Updated `/home/loviya/.codex/AGENTS.md` so `.codex-api-mimo` is documented as a Xiaomi MiMo-specific API runtime home.
- Verified `codex-api-mimo --version` returns `codex-cli 0.130.0`.
- Verified the runtime symlink layout and AGENTS/bash/zsh references with targeted reads.
- Fixed the local Responses streaming proxy so Codex CLI no longer reports `OutputTextDelta without active item`.
- Verified live MiMo access with `codex-api-mimo exec --skip-git-repo-check --sandbox read-only "只回复 ok"` after running outside the sandbox so the local proxy could bind and reach the network.
- Confirmed MiMo session/runtime artifacts are written under `/home/loviya/.codex-api-mimo`, including `sessions/`, `state_5.sqlite`, and `logs_2.sqlite`.
- Fixed the MiMo proxy so Codex tool calls are forwarded through Chat Completions `tools` and returned as Responses `function_call` items.
- Added `enable_thinking: false` to upstream MiMo requests because MiMo rejects tool-result follow-up turns in thinking mode unless `reasoning_content` is replayed.
- Verified `codex-api-mimo exec --skip-git-repo-check --sandbox read-only "请使用 shell 工具运行 pwd，然后只回复 pwd 的输出。"` actually executed `/usr/bin/bash -lc pwd` and returned `/home/loviya`.
- Updated `/home/loviya/.codex-api-mimo/codex-api-mimo` to start the local proxy with `setsid -f`, so it remains listening after `codex exec` exits.
- Updated the configured upstream MiMo endpoint and default model to the current OpenAI-compatible documentation:
  - endpoint: `https://api.mimo-v2.com/v1/chat/completions`
  - model: `mimo-v2.5-pro`
- Rotated `MIMO_API_KEY` after decrypting the user-provided token with CryptoJS `RabbitLegacy` and passphrase `linux.do`; the worklog intentionally does not record the plaintext key.
- Backed up `/home/loviya/.codex-api-mimo/mimo.env` before rotation:
  - `/home/loviya/.codex-api-mimo/mimo.env.bak-20260516-134543`
  - `/home/loviya/.codex-api-mimo/mimo.env.bak-20260516-134636-encrypted`
- Added a requested `codex_notes` entry documenting the RabbitLegacy decrypt/encrypt procedure without recording real secrets:
  - `/home/loviya/.codex/codex_notes/requested/2026-05-16-cryptojs-rabbitlegacy-secret-decrypt-encrypt.md`

## Create Mimo-Specific Codex Runtime

- updated: 2026-05-15 00:50:02 +0800
- cwd: `/home/loviya`
- source instruction: `我给你一个mimo的api,可以新建一个.codex-api-mimo的codex环境吗`
- problem:
  - The user wanted a new Codex runtime home dedicated to Mimo API use, analogous to the existing DeepSeek-specific `.codex-api-ds`.
- improvement:
  - Built `.codex-api-mimo` with isolated runtime state, shared managed content symlinks, a launcher, shell aliases, and a local Responses-to-Chat-Completions proxy.
- result:
  - The environment is configured and structurally verified, but live request validation was not completed before the user paused for the night.
- next:
  - Validate the live MiMo request path with `codex-api-mimo exec --skip-git-repo-check --sandbox read-only "只回复 ok"`.

## Resume From API Startup Greeting

- updated: 2026-05-15 09:47:11 +0800
- cwd: `/home/loviya`
- source instruction: `hi`
- problem:
  - The session started through the API with `CODEX_HOME` empty, which does not match the expected dedicated API runtime homes.
  - The current directory matched an unfinished workflow, but the user provided only a greeting and no explicit instruction to run the pending live MiMo validation.
- improvement:
  - Resumed this workflow for continuity and recorded the runtime-home mismatch before account-specific runtime changes.
- result:
  - No MiMo API validation command was run in response to the greeting alone.
- next:
  - If requested, validate the live MiMo request path with `codex-api-mimo exec --skip-git-repo-check --sandbox read-only "只回复 ok"`.

## Validate Live Mimo Codex API Path

- updated: 2026-05-15 09:56:24 +0800
- cwd: `/home/loviya`
- source instruction: `继续完成我的mimo的codexapi接入`
- problem:
  - The first validation attempt inside the sandbox failed because the local proxy could not bind to `127.0.0.1:18793`.
  - The first host-side validation reached MiMo but Codex CLI logged `OutputTextDelta without active item`, caused by an incomplete streamed Responses event shape.
- improvement:
  - Updated `/home/loviya/.codex-api-mimo/mimo_responses_proxy.py` to include `content: []` on `response.output_item.added` and `item_id` on content/delta/done events.
  - Re-ran the live validation command outside the sandbox so the local proxy could bind and make the upstream MiMo request.
- result:
  - `codex-api-mimo exec --skip-git-repo-check --sandbox read-only "只回复 ok"` completed successfully with provider `mimo`, model `xiaomi/mimo-v2-flash`, and no streaming parser error.
  - Runtime/session files were created under `/home/loviya/.codex-api-mimo`, confirming account-home isolation for this launcher.
- next:
  - none

## Repair Mimo Tool-Call Loop

- updated: 2026-05-15 11:20:51 +0800
- cwd: `/home/loviya`
- source instruction: `我是要你帮我修改.codex-api-mimo`
- problem:
  - `codex-api-mimo` could answer simple prompts, but for file-editing work it kept returning plan text such as "I will read the file" and never executed shell or patch tools.
  - The MiMo Responses proxy converted requests to plain Chat Completions messages but did not forward Codex `tools`, so the upstream model had no native way to call `exec` or `apply_patch`.
  - After adding tool forwarding, MiMo rejected the tool-result follow-up turn with `The reasoning_content in the thinking mode must be passed back to the API.`
- improvement:
  - Updated `/home/loviya/.codex-api-mimo/mimo_responses_proxy.py` to convert Responses `tools` into Chat Completions `tools` with `tool_choice: auto`.
  - Converted upstream Chat Completions `tool_calls` back into Responses `function_call` output items for Codex CLI.
  - Converted Responses `function_call` and `function_call_output` history back into assistant/tool Chat Completions messages.
  - Added `enable_thinking: false` to MiMo upstream requests so tool-result follow-up turns are accepted.
  - Kept a fallback cache for `reasoning_content` by tool call ID in case thinking mode is re-enabled later.
  - Updated the launcher to start the proxy with `setsid -f` instead of a shell background job, avoiding proxy shutdown after one-off `codex exec` validation.
- result:
  - `python3 -m py_compile /home/loviya/.codex-api-mimo/mimo_responses_proxy.py` succeeds.
  - Live validation outside the sandbox shows Codex executing `/usr/bin/bash -lc pwd` through MiMo and returning `/home/loviya`.
  - `ss -ltnp` confirms `python3 /home/loviya/.codex-api-mimo/mimo_responses_proxy.py` remains listening on `127.0.0.1:18793` after validation.
- next:
  - none

## Sync Mimo Endpoint And Model ID

- updated: 2026-05-16 12:46:20 +0800
- cwd: `/home/loviya`
- source instruction: `查看一下codex-api-mimo的配置,这个有什么问题没有`
- problem:
  - `/home/loviya/.codex-api-mimo/mimo.env` still used `https://api.xiaomimimo.com/v1/chat/completions`.
  - `/home/loviya/.codex-api-mimo/config.toml` and `mimo.env` still used `xiaomi/mimo-v2-flash`, while the current MiMo OpenAI-compatible model IDs are unprefixed, such as `mimo-v2.5-pro`.
  - The user's Trae screenshot showed a 400 `Param Incorrect` error while using the older domain.
- improvement:
  - Updated `MIMO_CHAT_COMPLETIONS_URL` to `https://api.mimo-v2.com/v1/chat/completions`.
  - Updated the Codex default MiMo model to `mimo-v2.5-pro`.
  - Kept Codex itself on the local Responses proxy at `http://127.0.0.1:18793/v1`, because Codex needs Responses API compatibility and MiMo exposes Chat Completions upstream.
- result:
  - `python3 -m py_compile /home/loviya/.codex-api-mimo/mimo_responses_proxy.py` succeeds.
  - Targeted reads confirmed the new endpoint and model are written.
- next:
  - For Trae, use OpenAI Chat Completions with base URL `https://api.mimo-v2.com/v1` and model `mimo-v2.5-pro`.

## Rotate Mimo API Key From Encrypted Token

- updated: 2026-05-16 13:46:06 +0800
- cwd: `/home/loviya`
- source instruction: `上面给的密匙是加密的`
- problem:
  - The first replacement wrote the encrypted token directly into `MIMO_API_KEY`, which is not usable as an API key.
  - The source token was encrypted with Rabbit-compatible tooling and passphrase `linux.do`.
- improvement:
  - Preserved the previous usable `mimo.env` backup as `/home/loviya/.codex-api-mimo/mimo.env.bak-20260516-134543`.
  - Preserved the intermediate encrypted-token file as `/home/loviya/.codex-api-mimo/mimo.env.bak-20260516-134636-encrypted`.
  - Used the locally installed `crypto-js` package and `RabbitLegacy` decryptor to derive the plaintext token, then wrote only the plaintext token into `MIMO_API_KEY`.
- result:
  - `/home/loviya/.codex-api-mimo/mimo.env` now contains the decrypted MiMo token.
  - Verification confirmed `mimo.env` and both backups have `600` permissions.
  - Verification confirmed the active key is single-line, length 51, and has the expected token prefix without printing the full secret.
- next:
  - none

## Preserve RabbitLegacy Secret Handling Procedure

- updated: 2026-05-16 13:52:47 +0800
- cwd: `/home/loviya`
- source instruction: `把这个解密和加密的知识和过程,写到notes里面`
- problem:
  - The RabbitLegacy compatibility detail is easy to lose if it remains only in chat history.
  - A durable note should be reusable while avoiding plaintext secrets and the specific encrypted token.
- improvement:
  - Added `/home/loviya/.codex/codex_notes/requested/2026-05-16-cryptojs-rabbitlegacy-secret-decrypt-encrypt.md`.
  - Updated `/home/loviya/.codex/codex_notes/INDEX.md`.
  - Included placeholder-based decrypt, metadata-only verification, encrypt, and round-trip examples.
- result:
  - The requested note is available through the Obsidian-backed `codex_notes` symlink.
  - Secret checks confirmed the note does not contain the real encrypted token prefix or decrypted token prefix.
- next:
  - none
