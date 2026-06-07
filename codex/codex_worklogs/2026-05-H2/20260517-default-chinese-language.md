---
id: 20260517-default-chinese-language
name: 默认中文语言规则
slug: default-chinese-language
cwd: /home/loviya
summary: 将 Codex 的默认人类可读输出和 worklog 语言改为简体中文。
tags:
  - codex
  - agents
  - language
  - worklog
---

# 默认中文语言规则

## 当前快照

- 工作流 ID: `20260517-default-chinese-language`
- 当前状态: `已完成`
- 当前目标: 修改全局 `AGENTS.md`，让系统默认使用简体中文记录和回复。
- 当前阻塞: 无。
- 下一步: 无。
- 标签: codex, agents, language, worklog
- 摘要: 已在全局规则中增加 `Language Defaults`，规定面向用户的回复、worklog、durable notes、摘要、决策和操作说明默认使用简体中文；代码、命令、路径、配置键、标识符、API 名称、模型名、引用输出和错误信息保持原语言。

## 关键结果

- 在 `/home/loviya/.codex/AGENTS.md` 靠前位置新增 `Language Defaults` 小节。
- 规则覆盖用户可见回复、worklog 内容、durable notes、summary、decisions 和 operational explanations。
- 保留技术内容原文，避免把代码、命令、配置键、错误信息等翻译后造成歧义。

## 决策

- 采用全局默认中文，而不是只修改 `Worklogs` 小节，因为用户要求是“系统的语言默认是中文”。
- 用户明确要求其他语言时，单次任务或指定 artifact 仍按用户语言执行。

## 验证

- 已用 `rg -n "语言默认值|默认中文|简体中文" /home/loviya/.codex/AGENTS.md /home/loviya/.codex/worklogs/2026-05-17/20260517-default-chinese-language.md /home/loviya/.codex/worklogs/INDEX.md` 验证。
