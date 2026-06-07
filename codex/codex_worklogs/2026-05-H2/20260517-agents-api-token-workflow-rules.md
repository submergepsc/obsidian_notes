---
id: 20260517-agents-api-token-workflow-rules
name: AGENTS API Token Workflow Rules
slug: agents-api-token-workflow-rules
cwd: /home/loviya
summary: 扩展全局 AGENTS.md，补充 API 调用、token 消耗、工作流生命周期和执行验证规则。
tags:
  - agents
  - codex
  - workflow
  - api
  - token-budget
---

# AGENTS API Token 工作流 规则

## 当前快照

- 工作流 ID: `20260517-agents-api-token-workflow-rules`
- 当前状态: `已完成`
- 当前目标: 扩展 `/home/loviya/.codex/AGENTS.md`，让其覆盖 API 调用隔离、token/上下文消耗、工作流生命周期、日志和验证规则。
- 当前阻塞: 无。
- 下一步: 无。
- 标签: agents, codex, workflow, api, token-budget
- 摘要: 用户认为当前 AGENTS.md 过于简略，要求从 API 调用、token 消耗、完善工作流等角度扩展。

## 关键结果

- 已确认 `/home/loviya/AGENTS.md` 不存在；当前生效文件为 `/home/loviya/.codex/AGENTS.md`。
- 已新增规则章节：`API Invocation`、`Token and Context Budget`、`Execution Workflow`。
- 已扩展 `Startup`、`Account Layout`、`Worklogs`、`Maintenance` 相关规则。

## 命令

- `sed -n '1,320p' /home/loviya/.codex/AGENTS.md`
- `sed -n '1,220p' /home/loviya/.codex/worklogs/INDEX.md`
- `rg -n "AGENTS|agents|工作流|workflow|token|api|API" /home/loviya/.codex/worklogs`

## 验证

- `rg -n "API Invocation|Token and Context Budget|Execution Workflow|Cost and Rate Discipline|Lifecycle|Provider Compatibility|CODEX_HOME|secret|worklog path" /home/loviya/.codex/AGENTS.md`
- `sed -n '1,260p' /home/loviya/.codex/AGENTS.md`
- 验证结果：新增章节和关键规则均已写入 `/home/loviya/.codex/AGENTS.md`。
