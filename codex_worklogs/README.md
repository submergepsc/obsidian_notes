---
created: 2026-04-27 11:14:00 +0800
type: guide
scope: codex-worklogs
---

# codex worklogs guide

这个文件是 `~/.codex/worklogs/` 的长期指导文件。
目标不是记录某一次具体工作，而是规范以后所有 Codex 窗口、工作流、日志文件的写法。

全局启动和接续规则另外定义在：

- `~/.codex/AGENTS.md`

## Directory rule

- 所有 Codex 工作日志统一放在：`~/.codex/worklogs/`
- 每个工作日一个目录：`~/.codex/worklogs/YYYY-MM-DD/`
- 每个独立工作流一个文件：`~/.codex/worklogs/YYYY-MM-DD/<Workflow-ID>.md`
- `Workflow-ID` 推荐格式：`YYYYMMDD-<short-hash>-<slug>`
- `slug` 应该表达“这一个任务线程正在推进的事情”，不要过于宽泛

这里的“工作日”不是自然日零点切分，而是固定采用：

- 当天 `04:00` 到次日 `03:59` 视为同一个工作日
- 也就是说，凌晨 `00:30`、`01:20`、`03:40` 的工作，仍归到前一天的 worklog 目录
- 到 `04:00` 后，才切换到新的 `YYYY-MM-DD` 目录

## Naming rule

推荐优先按“仓库/主题 + 任务”命名 slug，例如：

- `obsidian_notes-sync`
- `obsidian_notes-log-system`
- `leetcode-debug`
- `ubuntu-input-fix`

避免使用：

- `test`
- `new`
- `temp`
- `aaa`
- `untitled`

如果当前 session 的任务已经明显切换，不要继续复用旧 workflow，应该新开一个工作流文件。

## Session rule

同一个 `<Name>.md` 可以记录多次进入同一工作流的会话。
每次重新进入该工作流时，都在同一文件下追加新的 `Sessions` 记录。

适合继续追加的情况：

- 还是同一个仓库
- 还是同一个问题
- 只是中断后继续做

适合新建文件的情况：

- 任务目标已经变了
- 仓库变了
- 当前窗口承担的是另一条独立工作线

## Launcher rule

推荐统一通过下面命令启动：

```bash
cwl
```

或者：

```bash
cwl --name obsidian_notes-sync
```

这个启动器会：

- 先读取 `~/.codex/AGENTS.md`
- 先列出当天已有工作流
- 根据当前任务描述和 repo/cwd 判断是否应接续之前未完成的工作流
- 如果没有显式任务描述，优先从当前 repo/cwd 的未完成 workflow 中恢复
- 根据 worklog 里的显式状态字段判断哪些工作流仍然未完成
- 对超过 3 天未更新的未完成 workflow，默认按 `已搁置` 处理
- 新建 workflow 时自动生成唯一 ID
- 默认使用当前 Git 仓库名或当前目录名作为 slug，不再无条件询问 `name`
- 自动创建或追加对应的日志文件
- 自动刷新 `~/.codex/worklogs/INDEX.md` 查询总表
- 自动打开该日志文件
- 然后再启动真正的 `codex`

这条规则的实际执行标准是：

- 每个新的 Codex session 都应当在启动时绑定一个 workflow
- 如果当前窗口没有合适的日志文件，就立即创建
- 如果当前窗口只是继续同一任务，就复用已有日志文件
- 不要先开工、最后才补日志；建立 worklog 应视为窗口启动的一部分

## What the worklog is for

`worklogs` 的作用是记录“人工可读的工作流”。
它和 Codex 原生底层日志不是一回事。

分工如下：

- Codex 原生日志：负责底层运行、会话、调试信息
- `worklogs`：负责人能读懂的任务轨迹、窗口分工、上下文延续

## Recommended usage habit

每开一个新的 Codex 窗口，都先判断：

1. 这是继续已有工作流，还是新的工作流？
2. 这个窗口的任务名应该叫什么？
3. 这次进入后，日志里要补什么说明？

推荐在每次开始工作后，尽快在该日志文件的 `note:` 下补充：

- 当前状态
- 当前目标
- 当前阻塞点
- 下一步准备做什么
- 标签
- 摘要

在一次有实质内容的工作结束前，建议至少补一段简短 session update，说明：

- 这次改了什么
- 影响了哪些文件或目录
- 做了哪些验证
- 是否还有后续待办或未解决问题

## Minimal standard

以后所有 Codex 工作日志，至少满足以下标准：

- 有明确 `<Name>`
- 有唯一 `Workflow-ID`
- 有正确日期目录
- 日期目录按 `04:00 -> 次日 04:00` 的工作日边界计算
- 一次 session 只绑定一个 active workflow
- 同任务可续写，不同任务要拆分
- 不再把多个完全无关的任务混在一个文件里
- 最新 session 应有明确 `当前状态`

进一步的操作标准：

- one session, one active workflow
- one distinct task thread, one log file
- worklog 要足够清晰，让人不看 Codex 内部日志也能理解这次工作的大意
- 如果仓库内已经存在 `AGENTS.md`，应同时遵守其中对 worklog 和收尾步骤的补充要求

推荐使用的状态值：

- `进行中`
- `待继续`
- `阻塞`
- `已完成`
- `已搁置`

其中：

- `进行中`、`待继续`、`阻塞` 会被视为未完成工作流
- `已完成`、`已搁置` 默认不会作为接续候选

## Generated output rule

如果某个仓库存在“源码/生成器 + 生成产物”的关系，那么 worklog 除了记录代码修改，还应记录产物是否已经同步刷新。

典型情况：

- 修改了索引生成器
- 修改了站点导航模板
- 修改了分组/分类逻辑
- 修改了会影响最终可浏览页面的布局或结构

这类工作结束前，应该把“是否已重建产物、是否已做快速校验”记进 worklog，而不是只记录源码变更。

以 `obsidian_notes/runoob_tutorial_archive/runoob_archive` 为例，常见收尾动作是：

```bash
cd /home/loviya/notes/obsidian_notes/runoob_tutorial_archive && python3 runoob_scraper.py --build-index-only
```

如果生成器 Python 代码也变了，再补：

```bash
python3 -m py_compile /home/loviya/notes/obsidian_notes/runoob_tutorial_archive/runoob_scraper.py
```

目的不是增加流程，而是避免“代码改了，但生成页面还是旧的”这种脱节状态。

## Environment note

当前启动器会导出：

- `CODEX_WORKLOG_PATH`

这个变量表示“当前窗口对应的工作日志文件路径”。
如果后面要做自动写入、状态同步、日志索引，可以继续基于这个变量扩展。
