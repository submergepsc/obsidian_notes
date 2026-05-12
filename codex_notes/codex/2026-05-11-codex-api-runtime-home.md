---
title: Codex API Runtime Home
date: 2026-05-11
area: codex
importance: normal
requested_by_user: false
tags:
  - codex
  - api
  - runtime-home
source_worklog: /home/loviya/.codex/worklogs/2026-05-11/20260511-codex-api-runtime-home.md
---

# Codex API Runtime Home

`/home/loviya/.codex-api` is the dedicated Codex runtime home for API-management work.

Use:

```bash
codex-api
```

The shell alias loads `/home/loviya/.codex-api/relay.env` and starts Codex with:

```bash
CODEX_HOME=$HOME/.codex-api codex
```

Shared paths mirror `.codex-a` and `.codex-b`: `AGENTS.md`, `continue.md`, `worklogs`, `skills`, `rules`, `memories`, `vendor_imports`, and `plugins`.

Account/runtime-specific files stay local to `.codex-api`: `auth.json`, `config.toml`, `history.jsonl`, `installation_id`, `sessions/`, sqlite state/log files, `log/`, `tmp/`, `.tmp/`, `cache/`, and `models_cache.json`.

Existing API-related files retained in `.codex-api` include `relay.env`, `deepseek.env`, and `codex-deepseek`.

The durable policy source is `/home/loviya/.codex/AGENTS.md`, under `Multi-Account Codex Layout`.
