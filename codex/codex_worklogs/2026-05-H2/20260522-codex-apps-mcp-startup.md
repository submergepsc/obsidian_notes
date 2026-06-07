---
id: 20260522-codex-apps-mcp-startup
name: Codex apps MCP 启动失败处理
slug: codex-apps-mcp-startup
cwd: /home/loviya
summary: 处理普通账户 .codex-b 启动时内置 codex_apps MCP 访问 chatgpt.com/backend-api/wham/apps 失败导致的启动告警。
tags:
  - codex
  - mcp
  - codex-b
  - config
---

## Current Snapshot

- workflow id: `20260522-codex-apps-mcp-startup`
- current status: `已完成`
- current goal: 消除当前 `/home/loviya/.codex-b` 启动时 `codex_apps` MCP startup incomplete 告警
- current blocker: 无
- next step: 无；新启动 Codex 会读取 `/home/loviya/.codex-b/config.toml` 中的 `features.apps=false`
- tags: `codex`, `mcp`, `codex-b`, `config`
- summary: `codex mcp list` 显示没有用户配置的外部 MCP；`codex features list` 显示 `apps` 为 stable 且当前 true。日志中 `codex_apps` 访问 `https://chatgpt.com/backend-api/wham/apps` 多次失败，曾返回 Cloudflare HTML 或 HTTP request failed。

## Session Notes

- 当前账户：`CODEX_HOME=/home/loviya/.codex-b`。
- 当前 `/home/loviya/.codex-b/config.toml` 没有显式 `[mcp_servers]` 或 `codex_apps` 配置。
- `codex mcp list` 输出没有外部 MCP server，说明 `codex_apps` 来自 Codex 内置 Apps 功能。
- 诊断结论：启动告警不是用户自定义 MCP 配置错误；它来自内置 `apps` feature 尝试连接 ChatGPT Apps endpoint 失败。

## Commands

- `codex features list`: `apps stable true`，`enable_mcp_apps under development false`。
- `codex mcp list`: 无外部 MCP server。
- `rg -n "codex_apps|wham|MCP startup|mcp_servers" ...`: 当前账户日志存在历史和近期 `codex_apps` handshake/HTTP 失败。

## Key Results

- 已执行 `codex features disable apps`，写入 `/home/loviya/.codex-b/config.toml`。
- 验证 `/home/loviya/.codex-b/config.toml` 已包含 `[features] apps = false`。
- 验证 `codex features list` 中 `apps stable false`。
- 验证 `codex mcp list` 仍显示无外部 MCP server，未改动用户 MCP 配置。
- 未发起模型 live call；本次验证是配置级验证。
