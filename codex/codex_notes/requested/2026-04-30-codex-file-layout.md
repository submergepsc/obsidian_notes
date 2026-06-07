---
date: 2026-04-30
area: requested
problem: "记录当前 Codex 与 Obsidian 文件布局"
source_worklog: "log-management"
status: solved
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - file-layout
---

# 当前 Codex 文件布局

## 目的

本 note 记录当前 Codex homes 和 Obsidian 支撑的 note storage 目录布局。它是用户明确要求保存的 note，因此放在
`codex_notes/requested/`.

## 主要路径

```text
/home/loviya/.codex        # main Codex home and shared content center
/home/loviya/.codex-a      # account A runtime home
/home/loviya/.codex-b      # account B runtime home
/home/loviya/.codex-api    # API/relay runtime home
/home/loviya/obnotes       # symlink to /home/loviya/notes/obsidian_notes
```

## 共享笔记路径

```text
~/.codex/worklogs    -> ~/obnotes/codex_worklogs
~/.codex/codex_notes -> ~/obnotes/codex_notes
~/.codex/.obsidian   -> ~/obnotes/.obsidian
```

`codex_worklogs/` 保存原始 workflow 记录。`codex_notes/` 保存问题解决后写入的更短知识 note。

## 主 `.codex`

`~/.codex` 同时是主账户 home 和共享内容中心。

账户专属 runtime 文件保留在本地：

```text
auth.json
config.toml
sessions/
log/
state_5.sqlite*
logs_2.sqlite*
history.jsonl
session_index.jsonl
```

共享或由 Obsidian 支撑的内容：

```text
AGENTS.md
continue.md
skills/
rules/
memories/
vendor_imports/
worklogs -> ~/obnotes/codex_worklogs
codex_notes -> ~/obnotes/codex_notes
.obsidian -> ~/obnotes/.obsidian
```

## `.codex-a` 与 `.codex-b`

这些是账户专属 runtime homes。它们各自保留自己的 identity 和 session state：

```text
auth.json
config.toml
sessions/
log/
state_5.sqlite*
logs_2.sqlite*
history.jsonl
```

它们通过符号链接共享托管内容：

```text
AGENTS.md      -> ~/.codex/AGENTS.md
continue.md    -> ~/.codex/continue.md
worklogs       -> ~/.codex/worklogs -> ~/obnotes/codex_worklogs
skills         -> ~/.codex/skills
rules          -> ~/.codex/rules
memories       -> ~/.codex/memories
vendor_imports -> ~/.codex/vendor_imports
plugins        -> ~/.codex-shared/plugins
```

Shell aliases：

```bash
codex-a='CODEX_HOME=$HOME/.codex-a codex'
codex-b='CODEX_HOME=$HOME/.codex-b codex'
```

## `.codex-api`

`~/.codex-api` 是 API/relay Codex home，基本独立于共享账户布局。

重要文件：

```text
config.toml
deepseek.env
relay.env
codex-deepseek
sessions/
log/
state_5.sqlite*
logs_2.sqlite
skills/
memories/
```

当前默认 provider：

```toml
model = "claude-opus-4-1-20250805"
model_provider = "relay"
```

Shell alias：

```bash
codex-api='source $HOME/.codex-api/relay.env; CODEX_HOME=$HOME/.codex-api codex'
```

## 规则

- Runtime identity、auth、sessions、sqlite state、logs 和 caches 保持账户专属。
- 共享指令和可复用内容位于主 `~/.codex` 下。
- 原始 Markdown notes 位于 Obsidian：
  - `~/obnotes/codex_worklogs`
  - `~/obnotes/codex_notes`
- `~/.codex` 保留稳定的 symlink paths，确保 Codex tools 继续可用。

## 注意事项

- `codex_worklogs/` 可能包含路径、命令输出和操作上下文。公开同步或 Git 发布前需要检查。
- `codex_notes/requested/` 用于用户明确要求保存的 notes，可能比自动主题 notes 保留更多特定回答内容。
