---
id: 20260511-codex-api-runtime-home
name: Codex API Runtime Home
slug: codex-api-runtime-home
cwd: /home/loviya/notes/obsidian_notes
summary: 已新增 `/home/loviya/.codex-api` as a separate Codex runtime home for API-management work while sharing managed knowledge paths.
tags:
  - codex
  - api
  - runtime-home
priority: normal
---

# Codex API Runtime Home

## 当前快照

- 状态: 已完成
- 目标: 创建一个专门用于 API 管理的 Codex runtime home。
- 阻塞: 无
- 下一步: 无
- 更新时间: 2026-05-11 20:47:39 +0800

## 关键结果

- `/home/loviya/.codex-api` 作为 API 管理专用 Codex home。
- 已保留并复用既有 API 相关文件：`relay.env`、`deepseek.env`、`codex-deepseek`。
- 已确认 shell 入口：`alias codex-api='source $HOME/.codex-api/relay.env; CODEX_HOME=$HOME/.codex-api codex'`。
- 共享软链接：
  - `AGENTS.md -> /home/loviya/.codex/AGENTS.md`
  - `continue.md -> /home/loviya/.codex/continue.md`
  - `worklogs -> /home/loviya/.codex/worklogs`
  - `skills -> /home/loviya/.codex/skills`
  - `rules -> /home/loviya/.codex/rules`
  - `memories -> /home/loviya/.codex/memories`
  - `vendor_imports -> /home/loviya/.codex/vendor_imports`
  - `plugins -> /home/loviya/.codex-shared/plugins`
- 本地隔离项包括 `config.toml`、`history.jsonl`、`installation_id`、`sessions/`、sqlite state/log files、`log/`、`tmp/`、`.tmp/`、`cache/`。
- 已更新 `/home/loviya/.codex/AGENTS.md`，把 `.codex-api` 纳入多账号布局规则。
- 替换本地 `skills/` 和 `memories/` 目录前，备份到 `/tmp/codex-shared-backup-20260511-codex-api/`。

## Add API-Specific Codex Runtime Home

- 更新时间: 2026-05-11 20:47:39 +0800
- 工作目录: `/home/loviya/notes/obsidian_notes`
- 来源指令: `在创建一个,专门用于管理api的`
- 问题:
  - 用户需要在既有 `.codex-a`、`.codex-b` 多账号布局之外，增加一个 API 管理专用 Codex home。
- 改进:
  - 创建并规范化 `/home/loviya/.codex-api`，让共享知识路径与 A/B 保持一致，同时保留 API home 自己的运行态、配置和日志。
  - 修正已有 `.codex-api/skills` 与 `.codex-api/memories` 本地目录，把它们备份后替换成顶层共享软链接。
  - 更新共享 `AGENTS.md`，使后续会话知道 `.codex-api` 是正式 runtime home。
- 结果:
  - `codex-api` 入口可使用独立 `CODEX_HOME` 管理 API 工作。
- 下一步:
  - 无。
