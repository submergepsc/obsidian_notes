---
id: 20260517-agents-md-cleanup
name: AGENTS Md Cleanup
slug: agents-md-cleanup
cwd: /home/loviya
summary: 删除 `AGENTS.md` 中的冗余说明，只保留影响 Codex 行为的规则。
tags:
  - codex
  - agents
  - policy
  - cleanup
priority: normal
---

# AGENTS Md 清理

## 当前快照

- 状态: 已完成
- 目标: 压缩 `/home/loviya/.codex/AGENTS.md`，去掉重复解释和冗余转述，只保留会影响行为的规则。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-17 18:45:00 +0800

## 关键结果

- `AGENTS.md` 已改成更短的规则清单风格。
- 删除了多处重复的中英复述，保留了启动、账号布局、worklog、notes、维护这几类关键规则。
- 已验证新版本还保留了 `codex/codex_worklogs` 和 `codex/codex_notes` 的路径说明，以及长工作流快照压缩规则。

## 决策

- 以后 `AGENTS.md` 只保留可执行规则，不再把同一条规则做多次中文解释。
- 目录路径统一写成 `~/obnotes/codex/...`，避免再回到旧的根目录布局。

## Simplify AGENTS.md

- 更新时间: 2026-05-17 18:45:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `我发现agents.md里面不少废话,整理一下`
- 问题:
  - 原 `AGENTS.md` 里有大量重复表述、长段说明和同义复写，阅读成本高。
- 改进:
  - 直接重写为精简版规则清单，把重复解释压缩掉。
- 结果:
  - `AGENTS.md` 更短，更适合作为启动时的规则索引。
- 下一步:
  - 无。
