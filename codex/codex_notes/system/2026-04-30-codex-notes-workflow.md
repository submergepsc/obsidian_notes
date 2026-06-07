---
date: 2026-04-30
area: system
problem: "创建从已解决 Codex worklog 结果沉淀出的压缩知识层"
source_worklog: "20260429-mima-md-search"
status: solved
---

# Codex 笔记 工作流

## 问题

Worklogs 适合保存 workflow 状态、续接决策、阻塞点和详细操作历史，但对长期知识检索来说太冗长。
用户需要一个单独目录，只保存问题解决后的压缩知识。

## 结果

创建 `~/obnotes/codex_notes/` 作为面向 Obsidian 的持久知识目录，并链接到共享 Codex home：

```text
/home/loviya/.codex/codex_notes -> /home/loviya/obnotes/codex_notes
```

Notes 按已解决问题和主题区域组织，不按原始 session transcript 组织。
	
## 流程

后续 Codex 工作结束后使用这条规则：

1. 先在 `~/.codex/worklogs/` 下写入或更新强制 worklog。
2. 当用户问题解决后，判断结果是否具有可复用知识价值。
3. 如果有，写一条简短 note 到 `~/.codex/codex_notes/<area>/`。
4. 在 `~/.codex/codex_notes/INDEX.md` 添加一行索引。

推荐 note 路径：

```text
~/.codex/codex_notes/<area>/YYYY-MM-DD-<problem-slug>.md
```

## 组织方式

- `system/`：Codex workflow、note 策略和跨领域设置。
- `codex/`：Codex CLI、resume、providers、accounts、config。
- `terminal/`：shell、tmux、history 和命令行工作流。
- `obsidian/`：Obsidian vault、`ob` helper 和 note storage。

只有当已解决问题不适合现有分组时，才新增主题目录。

## 注意事项

- 不要复制 secrets、credentials、tokens、private keys 或账户内容。
- 不要把整个 worklog 复制进 notes。
- 不要为未完成调查写 note。
- Notes 可以链接到 worklogs，但 note 本身应能独立理解。

## 来源

- Worklog: `/home/loviya/.codex/worklogs/2026-04-29/20260429-mima-md-search.md`
