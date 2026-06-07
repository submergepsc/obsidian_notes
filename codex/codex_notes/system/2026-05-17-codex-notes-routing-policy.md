---
date: 2026-05-17
area: system
importance: normal
tags:
  - codex
  - notes
  - routing
  - policy
source_worklog: 20260517-codex-notes-routing-policy
---

# Codex 笔记 路由策略

## 决策

所有提到 `notes`、`笔记`、`记到 notes`、`写到 notes`、durable notes 或 reusable notes 的用户请求，都应写入 `~/.codex/codex_notes/`。

如果用户明确要求从特定内容制作或保留 note，写入：

```text
~/.codex/codex_notes/requested/
```

## 用户请求 笔记 的必需元数据

用户明确要求保存的 notes 必须包含以下 frontmatter：

```yaml
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
```

`~/.codex/codex_notes/INDEX.md` 中对应行应显示 `user-requested/high`。

## 旧位置

`~/obnotes/codex/` 是旧结果归档位置。普通 notes 请求不要写到这里。只有当用户明确给出这个精确路径，或明确要求写到 `~/obnotes/codex/` 下时，才使用它。

## 权威来源

持久策略写在 `/home/loviya/.codex/AGENTS.md` 的 notes 相关章节中。
