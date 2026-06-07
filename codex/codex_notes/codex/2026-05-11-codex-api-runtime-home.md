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

`/home/loviya/.codex-api` 是 API 管理工作的专用 Codex runtime home。

Use:

```bash
codex-api
```

shell alias 会加载 `/home/loviya/.codex-api/relay.env`，并用以下方式启动 Codex：

```bash
CODEX_HOME=$HOME/.codex-api codex
```

共享路径沿用 `.codex-a` 和 `.codex-b` 的布局：`AGENTS.md`、`continue.md`、`worklogs`、`skills`、`rules`、`memories`、`vendor_imports` 和 `plugins`。

账户/runtime 专属文件保留在 `.codex-api` 本地：`auth.json`、`config.toml`、`history.jsonl`、`installation_id`、`sessions/`、sqlite state/log files、`log/`、`tmp/`、`.tmp/`、`cache/` 和 `models_cache.json`。

`.codex-api` 中保留的既有 API 相关文件包括 `relay.env`、`deepseek.env` 和 `codex-deepseek`。

持久策略来源是 `/home/loviya/.codex/AGENTS.md` 中的多账户 Codex 布局规则。
