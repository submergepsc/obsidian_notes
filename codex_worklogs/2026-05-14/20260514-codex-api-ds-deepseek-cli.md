---
id: 20260514-codex-api-ds-deepseek-cli
name: Codex API DS DeepSeek CLI
slug: codex-api-ds-deepseek-cli
cwd: /home/loviya
summary: Create an isolated DeepSeek-oriented Codex runtime home and launcher named codex-api-ds.
tags:
  - codex
  - deepseek
  - runtime-home
  - cli
priority: normal
---

# Codex API DS DeepSeek CLI

## Current Snapshot

- status: 已完成
- goal: Provide `codex-api-ds` that starts Codex with `/home/loviya/.codex-api-ds` and routes requests to DeepSeek.
- blocker: none
- next: none
- updated: 2026-05-15 00:25:52 +0800

## Key Results

- Created `/home/loviya/.codex-api-ds` as an independent runtime home.
- Shared only managed content paths from `/home/loviya/.codex`: `AGENTS.md`, `continue.md`, `worklogs`, `skills`, `rules`, `memories`, `vendor_imports`, and shared plugins.
- Added `/home/loviya/.local/bin/codex-api-ds` and `/home/loviya/.codex-api-ds/codex-api-ds`.
- Stored the DeepSeek key in `/home/loviya/.codex-api-ds/deepseek.env` with `600` permissions.
- Added `/home/loviya/.codex-api-ds/deepseek_responses_proxy.py` because Codex 0.130 uses the Responses API while DeepSeek exposes Chat Completions.
- Configured `/home/loviya/.codex-api-ds/config.toml` to use `model_provider = "deepseek"`, `model = "deepseek-chat"`, and the local compatibility endpoint `http://127.0.0.1:18792/v1`.
- Updated `/home/loviya/.codex/AGENTS.md` so `.codex-api-ds` is documented as a DeepSeek-specific API runtime home.

## Verification

- `codex-api-ds --version` returned `codex-cli 0.130.0`.
- Direct DeepSeek Chat Completions validation with the new key returned HTTP 200 and `ok`.
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "只回复 ok"` completed successfully through the compatibility proxy and returned `ok`.
- The local proxy runs in tmux session `codex-ds-proxy` on `127.0.0.1:18792`.

## Notes

- Do not write API keys into worklogs, `continue.md`, or codex notes.
- Port `18791` was already occupied by `openclaw-gateway`, so the DeepSeek compatibility proxy uses `18792`.
