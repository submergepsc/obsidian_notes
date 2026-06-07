---
id: 20260515-api-relay-station-collection
name: API Relay Station Collection
slug: api-relay-station-collection
cwd: /home/loviya
summary: 从 GitHub relayAPI 仓库和 Veridrop 检测工具收集中文 AI API 中转站信息，整理成结构化列表
tags:
  - api
  - relay
  - proxy
  - claude
  - openai
  - 中转站
priority: normal
---

# API Relay Station Collection

## 当前快照

- 状态: 已完成
- 目标: 收集网上所有可用的 AI API 中转站（私有/第三方中转）
- 阻塞: 无。
- 下一步: 用户提供 Copilot API Key 后配置 OpenClaw
- 更新时间: 2026-05-15 19:30:00 +0800

## 关键结果

- 从 GitHub [relayAPI](https://github.com/zzsting88/relayAPI) 仓库获取了完整的 AI API 中转站推荐与评测列表
- 从 [Veridrop](https://github.com/canarybyte/veridrop) 获取了中转站真伪检测工具的说明
- 整理了约 20+ 个中转站的结构化信息（按编程类/综合类分类）
- 记录了各站点的价格参考、特点和安全建议

## 产物

- 整理后的列表: `~/obnotes/crawl/api-proxy-list/README.md`
- relayAPI 原始参考: `~/obnotes/crawl/api-proxy-list/relayAPI_reference.md`
- Veridrop 原始参考: `~/obnotes/crawl/api-proxy-list/veridrop_reference.md`

## Discoveries

- 发现 `relayAPI` 仓库（zzsting88）是目前最新最全的中转站评测汇总
- Veridrop 提供 Claude thinking 签名验证的中转站真伪检测
- 禾维AI提供实时中转站价格排行榜

## 待确认问题

- 用户想用 Copilot API Key 还是普通的中转站 API Key 来配置 Claude Code？
