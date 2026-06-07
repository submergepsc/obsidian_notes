# Codex 笔记 知识库

`codex_notes` 是从已解决 Codex 工作中沉淀出的压缩知识层。

它不是 transcript，也不替代 `~/.codex/worklogs`。
Worklogs 保存 workflow 状态和操作历史；`codex_notes` 保存问题解决后的可复用结论。

在本机，`~/.codex/codex_notes` 是指向
`~/obnotes/codex/codex_notes/` 的符号链接。

## 写入策略

- 只在问题已经解决或形成稳定决策后写 note。
- 按已解决的问题组织 notes，不按聊天会话组织。
- 每条 note 应比来源 worklog 更短、更干净。
- 如果用户明确要求把特定内容写成 notes，把对应 note 写入 `requested/` 并保留用户指定重点。
- 用户明确要求写入的 notes 必须在 frontmatter 中明显标记：
  `requested_by_user: true`, `importance: user-requested`,
  `review_priority: high`，并让 tags 包含 `user-requested` 和 `important`。
- 优先记录命令、路径、决策、注意事项和可复用流程。
- 不要把 secrets、credentials、tokens、private keys 或原始账户内容复制进 notes。
- 有用时链接回来源 worklog。

## 目录结构

- `INDEX.md`：人工可读的压缩 notes 索引。
- `_templates/problem-note.md`：note 模板。
- `system/`：Codex workflow、note 策略和跨领域设置。
- `codex/`：Codex CLI、resume、providers、accounts、config。
- `terminal/`：shell、tmux、history 和命令行工作流。
- `obsidian/`：Obsidian vault、`ob` helper 和 note storage。
- `requested/`：用户明确要求从特定回答、解释或上下文块保存的 notes。

当已解决问题不适合现有分类时，再新增主题目录。
