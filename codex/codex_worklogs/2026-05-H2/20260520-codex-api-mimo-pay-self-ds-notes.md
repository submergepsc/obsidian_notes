---
id: 20260520-codex-api-mimo-pay-self-ds-notes
name: codex-api-mimo-pay-self 与 ds 配置链路 notes
slug: codex-api-mimo-pay-self-ds-notes
cwd: /home/loviya
summary: 按用户要求将 codex-api-mimo-pay-self 配置链路写入 codex_notes，并与 codex-api-ds 配置做比较。
tags:
  - notes
  - codex-api-mimo-pay-self
  - codex-api-ds
  - provider-config
---

# codex-api-mimo-pay-self 与 ds 配置链路 notes

## Current Snapshot

- workflow id: 20260520-codex-api-mimo-pay-self-ds-notes
- current status: 已完成
- current goal: 新增用户请求 note，记录 codex-api-mimo-pay-self 配置链路并对比 codex-api-ds。
- current blocker: 无
- next step: 无
- tags: notes, codex-api-mimo-pay-self, codex-api-ds, provider-config
- summary: 已读取现有 mimo/ds notes 和当前 `/home/loviya/.codex-api-mimo-pay-self`、`/home/loviya/.codex-api-mimo-free-self` 配置，确认 `codex-api-mimo-pay-self` 走 18793 Responses 代理，`codex_api_mimo_free_self` 走 8000 mimi3 网关。

## Key Results

- 新增 note: `requested/2026-05-20-codex-api-mimo-pay-self-vs-ds-config.md`。
- note 只记录脱敏链路、配置键、端口、模型名和验证命令，不记录真实 key 或上游 URL。

## Verification

- 已更新 `~/.codex/codex_notes/INDEX.md`。
- 已更新 `~/.codex/codex_notes/requested/INDEX.md`。
- 已更新 `~/.codex/worklogs/INDEX.md`。
- 下一步：最终检查 note frontmatter、索引链接和敏感信息脱敏。
