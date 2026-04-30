---
created: 2026-04-27 11:10:00 +0800
topic: codex-log-management
---

# codex log management

## Current setup

- Codex 原生共享状态目录：`~/.codex/`
- 原生日志仍然主要在：`~/.codex/log/codex-tui.log`
- 原生会话/状态文件还包括：`history.jsonl`、`session_index.jsonl`、`logs_2.sqlite`、`state_5.sqlite`
- 这些文件是全局共享的，不会按窗口自动拆成独立日志

## Added worklog layer

- 新增工作日志根目录：`~/.codex/worklogs/`
- 日志按日期分目录：`~/.codex/worklogs/YYYY-MM-DD/`
- 每个独立工作流对应一个 Markdown 文件：`~/.codex/worklogs/YYYY-MM-DD/<Name>.md`
- `<Name>` 会先做清洗，空格会转成 `-`，路径分隔符会被替换掉

## Launcher

- 启动器脚本：`~/.local/bin/codex-worklog`
- 快捷别名：`cwl`
- 原版 `codex` 命令没有被覆盖，只是额外加了一层包装

## Behavior

- 启动时先列出当天已有工作流
- 如果手动传入名字，就直接使用
- 如果不传名字，默认值优先取当前 Git 仓库名
- 如果当前目录不在 Git 仓库里，则退回当前目录名
- 如果当天该名字的日志文件不存在，就创建
- 如果已存在，就在同一文件下追加一段新的 `Sessions` 记录
- 创建/追加后会自动打开日志文件
- 自动打开优先使用 `code`，没有则退回 `xdg-open`

## Environment

- 当前会导出：`CODEX_WORKLOG_PATH`
- 这个变量指向本次窗口对应的日志文件路径
- 可用 `CODEX_WORKLOG_NO_OPEN=1` 临时关闭自动打开日志文件的行为

## Recommended usage

```bash
cwl
```

```bash
cwl --name obsidian-sync
```

```bash
CODEX_WORKLOG_NO_OPEN=1 cwl
```

## Practical meaning

- Codex 原生日志继续负责底层统一记录
- `worklogs` 这一层负责按“窗口 / 工作流”做人工可读的任务记录
- 这样可以同时保留全局调试日志和多窗口独立工作笔记

## Problems And Improvements Notes

## 接续工作流状态更新
- updated: 2026-04-27 11:51:46 CST

#### Background

- 用户最初希望进入 `~/notes/obsidian/codex` 工作，但实际存在的目录是 `~/notes/obsidian_notes`
- 后续定位到需要整理的是 `~/notes/obsidian_notes/codex/runoob_archive/` 这套离线归档索引
- 原始索引的问题有两层：
  - 根索引里的各个 group，例如 `js`、`python3`、`sql`、`docker` 等，全部平铺在同一级
  - 每个 group 页内部通常也是单一长列表，缺少进一步的细分入口

#### Investigation

- 检查了 `runoob_archive` 当前结构，确认首页索引、各 group 索引以及 `meta/`、`text/`、`html/` 目录之间的关系
- 通过代码搜索定位到索引生成逻辑集中在 `~/notes/obsidian_notes/codex/runoob_scraper.py`
- 确认 `build_index_pages()` 会基于 `meta/*.json` 重新生成：
  - 根索引 `runoob_archive/index.html`
  - `html/index.html`
  - 每个 group 下的 `html/<group>/index.html`
- 评估后决定直接改索引生成器，而不是手工修改生成后的 HTML，因为这样后续重建时不会丢失结构调整

#### Index restructuring

- 为每条页面记录增加 `subgroup` 分类字段，按标题、slug、URL 关键词自动归类
- 当前页内分类规则包括：
  - `入门`
  - `参考`
  - `实例`
  - `练习`
  - `测验`
  - `面试`
  - `AI / 工具`
  - `专题`
- 根索引进一步增加按 group 归类的主题层级，把原本平铺的 group 组织成更高一层的大类
- 当前主题大类包括：
  - `前端开发`
  - `后端与编程语言`
  - `数据与数据库`
  - `AI 与 Agent`
  - `工具链与工程`
  - `网络协议与标准`
  - `站点与杂项`
  - `未分类`

#### Navigation and layout

- 首页结构从“一个 groups 区块 + 一个 pages 区块”改成“主题大类分段展示”
- 每个大类下会显示：
  - 该类总页数
  - 该类 group 数
  - group 卡片预览
- 每个 group 卡片会显示：
  - group 名称
  - 该组页面数
  - 前几个页内子类的数量摘要
  - 若干示例页面链接
- 组页索引改成：
  - 顶部给出页内子类总数
  - 先列出分类导航
  - 再分 section 展示每个子类下的页面

#### Sidebar work

- 给索引模板 `_wrap_index_html()` 增加双栏布局
- 左侧增加固定侧栏，右侧保留正文内容
- 首页左侧加入 `主题导航`
- 组页左侧加入 `页内导航`
- 侧栏使用 `details/summary` 结构，支持展开和折叠
- 首页侧栏从“全部默认展开”调整为“只展开第一个主题大类，其余默认折叠”
- 组页侧栏仍默认展开，减少额外点击
- 给侧栏卡片增加：
  - `max-height: calc(100vh - 40px)`
  - `overflow: auto`
  以实现左侧导航独立滚动

#### Files and paths involved

- 主要修改文件：
  - `~/notes/obsidian_notes/codex/runoob_scraper.py`
- 重新生成的主要输出：
  - `~/notes/obsidian_notes/codex/runoob_archive/index.html`
  - `~/notes/obsidian_notes/codex/runoob_archive/html/index.html`
  - `~/notes/obsidian_notes/codex/runoob_archive/html/<group>/index.html`
- 本次重建过程中也补出了少量之前未生成的 group 索引页，例如：
  - `python-qt`
  - `regex`
  - `sass`

#### Verification

- 多次执行 `python3 runoob_scraper.py --build-index-only` 重建索引页
- 使用 `python3 -m py_compile ~/notes/obsidian_notes/codex/runoob_scraper.py` 做语法校验
- 通过检查生成后的首页和组页 HTML，确认：
  - 主题大类标题已实际写入首页
  - 首页左侧 `主题导航` 已生效
  - 组页左侧 `页内导航` 已生效
  - 首页侧栏默认只有第一个大类展开
  - 侧栏支持独立滚动

#### Worklog check

- 期间确认了 `~/.codex/worklogs/` 目录已经创建
- 当前存在的内容包括：
  - `~/.codex/worklogs/2026-04-27/`
  - `~/.codex/worklogs/2026-04-27/log-management.md`
- 用户额外要求把当前工作同步记录到这个日志文件中，本段即为更详细的补充记录

## 接续工作流状态更新
- updated: 2026-04-27 17:55:20 +0800

#### Day boundary rule

- 新增统一约定：Codex worklog 不按自然日 `00:00` 切分
- 正式改为按本地时间 `04:00` 切分工作日
- 也就是“当天 `04:00` 到次日 `04:00`”视为同一天的工作
- 凌晨 `00:00` 到 `03:59` 的持续工作，应继续写入前一天目录，而不是新建当天目录

#### Applied changes

- 已更新 `~/.local/bin/codex-worklog`
- 当前启动器目录计算改为基于 `date -d '4 hours ago' +%F`
- 已更新全局说明文件 `~/.codex/worklogs/README.md`
- 已写入 `~/.codex/agnets.md`

#### Intended effect

- 避免夜间连续工作被 `00:00` 硬切成两个日期目录
- 让单次长会话、跨午夜修复、深夜整理类工作保持在同一条 worklog 线程里

## 接续工作流状态更新
- updated: 2026-04-27 18:02:00 +0800

#### Startup and handoff rule

- 新增全局规则文件：`~/.codex/AGENTS.md`
- 该文件单独定义了 `Worklog Module`
- 目标是让每次进入 Codex 终端时，先读取统一规则，再决定是接续旧工作流还是新建

#### Wrapper behavior change

- `~/.local/bin/codex-worklog` 现在会在启动时打印并读取 `~/.codex/AGENTS.md`
- 会根据当前输入指令或传入的 prompt 文本，搜索最近 worklog
- 如果检测到相近且疑似未完成的工作流，会给出候选，优先接续
- 如果没有合适候选，仍然按原方式新建 worklog
- 新的 session 模板中增加了 `当前状态：进行中`

#### Shell entrypoint change

- 已把交互式 shell 中的 `codex` alias 到 `codex-worklog`
- 这样直接输入 `codex ...` 时，也会先经过 worklog 判断流程，而不再只靠 `cwl`
- 另外已在 `~/.bashrc` 中加入 `codex_read_agents`，使每次打开交互式终端时都会先读取 `~/.codex/AGENTS.md`

## 接续工作流状态更新
- updated: 2026-04-27 18:10:00 +0800

#### Workflow state machine

- 给 worklog 规则补充了显式状态值：
  - `进行中`
  - `待继续`
  - `阻塞`
  - `已完成`
  - `已搁置`
- 其中 `进行中` / `待继续` / `阻塞` 会被当作未完成工作流
- `已完成` / `已搁置` 默认不会再被自动接续

#### Query table

- 新增 `~/.codex/worklogs/INDEX.md` 作为总览查询表
- 启动器每次创建或续写 worklog 后都会自动刷新这个表
- 当前表格列包括：
  - workday
  - workflow
  - status
  - updated
  - cwd
  - next step
  - file

#### Matching improvement

- 工作流接续判断不再只看“是否出现完成字样”
- 现在优先读取最新 `当前状态`
- 同时把当前仓库上下文纳入匹配打分，减少跨项目误接续
## 接续工作流状态更新
- updated: 2026-04-27 18:06:48 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `/tmp/tmux-1000/default,5457,0`
- status: 进行中
## 接续工作流状态更新
- updated: 2026-04-27 18:07:52 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `/tmp/tmux-1000/default,5457,0`
- status: 进行中
## 接续工作流状态更新
- updated: 2026-04-27 18:08:17 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `/tmp/tmux-1000/default,5457,0`
- status: 进行中
## 解释 Obsidian/终端命令打开两个页面的原因
- updated: 2026-04-28 12:01:09 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `none`
- source instruction: `为什么现在obsidian输入这个命令行会打开两个页面`
- context: 根据 Obsidian、命令行、worklog 启动器上下文，接续 `log-management`。
- status: 进行中
- problem:
  - goal: 解释 Obsidian/终端命令打开两个页面的原因。
  - blocker: 用户未明确具体命令，需按 `ob` 与 `codex-worklog/cwl` 两种可能分别说明。
- result:
  - 已定位 `codex-worklog` 会自动打开 worklog；Obsidian 配置中 `/home/loviya/.codex` vault 处于 `open: true`，因此 Obsidian 启动时可能恢复第二个 vault/窗口。
- next: 如需消除双开，确认要改 Obsidian vault 恢复状态还是关闭 worklog 自动打开。
- tags: obsidian, codex-worklog, terminal, startup
## 恢复 ob 打开主 Obsidian vault 的正常行为
- updated: 2026-04-28 12:08:00 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `none`
- source instruction: `把我正常的工作流恢复`
- context: 继续 `log-management` 中的 Obsidian 启动恢复问题。
- status: 进行中
- problem:
  - goal: 恢复 `ob` 打开主 Obsidian vault 的正常行为。
- result:
  - 已将 `/home/loviya/bin/ob` 改为 `exec obsidian "$HOME/notes/obsidian_notes"`，并把 Obsidian 状态切换为 `obsidian_notes` vault `open: true`、`.codex` vault 不再标记打开。
- next: 用户可运行 `ob` 验证是否只打开 `/home/loviya/notes/obsidian_notes`；若 Obsidian 再次写回 `.codex` 为打开状态，再改为 URI/protocol 方式。
- tags: obsidian, ob, vault, startup
## 确认交互式 shell 中 ob 的真实解析结果，并撤回无关改动
- updated: 2026-04-28 12:10:00 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `none`
- source instruction: `你搞错了,ob是我设置的alias`
- context: 修正上一条对 `ob` 入口的判断。
- status: 进行中
- problem:
  - goal: 确认交互式 shell 中 `ob` 的真实解析结果，并撤回无关改动。
- result:
  - 交互式 `bash -ic` 确认 `ob` 是 `.bashrc` 中的 alias：`obsidian "$HOME/notes/obsidian_notes"`；已撤回对 `/home/loviya/bin/ob` 的改动，仅保留 Obsidian vault 状态修复。
- next: 用户运行 `ob` 验证；若仍打开 `.codex`，继续检查 Obsidian 单实例/URI 打开策略。
- tags: obsidian, alias, bashrc
## 把 ob 从 alias 改成可处理路径的 Bash 函数
- updated: 2026-04-28 12:18:00 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `none`
- source instruction: `在~/.bashrc 增加一个ob(){}来帮我处理打开的问题`
- context: 继续处理 Obsidian CLI 路径打开问题。
- status: 进行中
- problem:
  - goal: 把 `ob` 从 alias 改成可处理路径的 Bash 函数。
- result:
  - 已将 `.bashrc` 中的 `ob` alias 替换为函数；默认打开 `/home/loviya/notes/obsidian_notes`，`ob ~/.codex` / `ob codex` 会转为 `obsidian://open?path=/home/loviya/.codex`，避免 Obsidian CLI 把路径当命令。
- next: 新终端或执行 `source ~/.bashrc` 后，运行 `ob`、`ob ~/.codex` 验证。
- tags: obsidian, bashrc, function, uri
## 让空参数 ob 显式默认打开主 vault
- updated: 2026-04-28 12:20:00 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `none`
- source instruction: `增加一些默认的,如果是空的自动执行 ob ~/notes/obsidian_notes`
- context: 继续完善 `.bashrc` 中的 `ob` 函数默认行为。
- status: 进行中
- problem:
  - goal: 让空参数 `ob` 显式默认打开主 vault。
- result:
  - 已把 `ob` 函数改成显式判断空参数；无参数时打开 `/home/loviya/notes/obsidian_notes`，并新增 `note`、`main` 默认关键词指向主 vault。
- next: 新终端或执行 `source ~/.bashrc` 后验证 `ob`、`ob notes`、`ob codex`。
- tags: obsidian, bashrc, defaults
## 让后续网页爬取、站点镜像、教程归档、离线 HTML 生成默认进入 ~/obnotes/c...
- updated: 2026-04-28 14:33:49 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `unavailable`
- source instruction: `把以后涉及到爬取网页工作区的都自动定向到这个crawl目录下面`
- context: 继续全局 Codex 工作区和 Obsidian vault 路径规范整理。
- status: 已完成
- problem:
  - goal: 让后续网页爬取、站点镜像、教程归档、离线 HTML 生成默认进入 `~/obnotes/crawl/`。
  - blocker: 无。
- result:
  - 已在 `~/.codex/AGENTS.md` 新增 `Workspace Routing` 规则：网页爬取、站点镜像、教程归档、离线 HTML、下载资源、状态文件和爬虫脚本默认放到 `~/obnotes/crawl/`；每个爬取目标使用自包含目录；不得默认散落到 `~/obnotes/` 根目录、`~/` 或无关项目目录。同步更新 `~/.codex/continue.md`。
- next: 无；未来新增爬取目标时，默认创建或复用 `~/obnotes/crawl/<slug>/`。
- tags: codex, crawl, obsidian, workspace
## 解释 obsidian 直接启动和 ob 默认 vault 不一致的原因
- updated: 2026-04-28 13:59:46 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `none`
- source instruction: `obsidian为什么不能直接启动obsidian；ob为什么打开的不是obsidian_notes默认文件夹`
- context: 继续排查 Obsidian/`ob` 启动路径遗留问题。
- status: 进行中
- problem:
  - goal: 解释 `obsidian` 直接启动和 `ob` 默认 vault 不一致的原因。
- result:
  - 确认 `obsidian` 是 `~/.local/bin/obsidian` 包装脚本，指向 `/home/loviya/apps/obsidian-1.12.7/obsidian`；bash 交互式 `ob` 是 `.bashrc` 函数，默认目标为 `/home/loviya/notes/obsidian_notes`；但 PATH 中还存在 `/home/loviya/bin/ob`，zsh 未定义同名函数，只会走脚本。`obsidian` 无参数启动只恢复 Obsidian 自己记录的上次 vault/session，不等于强制打开默认 vault。
- next: 如需修复，应统一 bash/zsh 的 `ob` 定义，并考虑把 `ob` 改为 `obsidian://open?path=...` 方式强制打开目标 vault。
- tags: obsidian, ob, bashrc, zshrc, launcher
## 只修改 bash 下的 ob 启动逻辑
- updated: 2026-04-28 14:03:53 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `none`
- source instruction: `ok`
- context: 继续 `ob` bash 函数修复。
- status: 进行中
- problem:
  - goal: 只修改 bash 下的 `ob` 启动逻辑。
- result:
  - 已将 `/home/loviya/.bashrc` 中 `ob` 函数最后的裸路径启动改为 `command obsidian "obsidian://open?path=$target"`，让 `ob` 更强制地打开解析后的目标路径；未修改 zsh 配置。
- next: 执行 `source ~/.bashrc` 或开新 bash 后运行 `ob` 验证是否打开 `/home/loviya/notes/obsidian_notes`。
- tags: obsidian, ob, bashrc
## 确认 cwl 的含义和当前会话内的安全处理方式
- updated: 2026-04-29 15:20:46 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `none`
- source instruction: `cwl`
- context: 用户输入短关键词 `cwl`；按启动规则先匹配 worklog，接续记录 `codex-worklog` / `cwl` 启动器相关 workflow。
- status: 进行中
- problem:
  - goal: 确认 `cwl` 的含义和当前会话内的安全处理方式。
  - blocker: 当前已经在 Codex 会话中，不应再直接启动嵌套 `codex-worklog -> codex` 进程。
- result:
  - 已确认 `cwl` 是 `~/.local/bin/codex-worklog` 的入口/别名语义；该脚本会读取 AGENTS、选择或创建 worklog、刷新 `INDEX.md` 和 continue 摘要，然后 `exec codex`。在当前已运行的 Codex 内不递归启动。
- next: 如需新开 Codex workflow，应在外层 shell 运行 `cwl`、`cwl --task "..."` 或 `cwl --name <slug>`；当前会话只做说明和日志记录。
- tags: codex-worklog, cwl, launcher
## 在全局 AGENTS.md 中增加重要结果写入 Obsidian vault 的规则
- updated: 2026-04-29 22:06:43 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `unknown`
- source instruction: `更改一下agents.md,对于比较重要的结果,把worklog写入到~/obnotes/codex文件夹下面去,不需要你询问,我会告诉你`
- context: 继续全局 Codex worklog/Obsidian 记录规则维护。
- status: 已完成
- problem:
  - goal: 在全局 `AGENTS.md` 中增加重要结果写入 Obsidian vault 的规则。
  - blocker: 无。
- result:
  - 已在 `/home/loviya/.codex/AGENTS.md` 的 Worklog Module 中新增 `Important Result Notes`：`~/obnotes/codex/` 是重要 Codex 结果的用户可读笔记位置；不替代强制 workflow log；用户明确要求保存重要结果时无需再次确认，直接创建目录并写入整理后的 Markdown，失败时按权限规则申请升级或报告路径。
- next: 无；后续当用户明确说明重要结果需要保留时，直接写整理后的 Markdown 到 `~/obnotes/codex/`，同时常规 worklog 仍写入 `~/.codex/worklogs/`。
- tags: codex, agents, worklog, obsidian
## 修正 worklog 只像历史会话记录的问题，让 worklog 更适合作为状态和结论入...
- updated: 2026-04-29 22:10:36 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `unknown`
- source instruction: `我发先你当前的worklog的内容完全就是记录历史会话`
- context: 继续全局 Codex worklog 质量规则维护。
- status: 已完成
- problem:
  - goal: 修正 worklog 只像历史会话记录的问题，让 worklog 更适合作为状态和结论入口。
  - blocker: 无。
- result:
  - 已修改 `/home/loviya/.codex/AGENTS.md` 的 `Logging Standard`：worklog 不应只是按时间追加的会话历史；必须把当前状态、可复用结论、决策、命令、产物和开放问题放在顶部结构化区域，session blocks 仍保留但应简洁。
- next: 后续新建或更新 worklog 时，应维护顶部 `Current Snapshot`、`Key Results`、`Decisions` 等结构；会话历史只作为简短审计记录。
- tags: codex, agents, worklog, structure
## 你改成这样,所有的worklog只记录这个工作流中提出的问题和改进措施,也就是记录笔记...

- updated: 2026-04-29 22:39:52 +0800
- cwd: `/home/loviya`
- source instruction: `你改成这样,所有的worklog只记录这个工作流中提出的问题和改进措施,也就是记录笔记,而不是记录会话,并且每个标题都是用总结的会话内容,而不是时间`
- problem:
  - 旧规则仍保留 `Session History` 和时间标题模板，容易让 worklog 继续变成会话流水。
- improvement:
  - 已修改 `/home/loviya/.codex/AGENTS.md` 的 `Logging Standard`，明确 worklog 是 notes file，不是 session transcript。
  - 要求所有条目标题概括问题、改进或结果，不使用纯时间标题。
  - 时间、cwd、host、instruction 只能作为条目元数据，不作为标题。
  - 新模板改为 `problem`、`improvement`、`result`、`next`。
- result:
  - 后续 worklog 应只记录工作流中提出的问题、对应改进措施、结论、命令、产物和下一步。
  - 历史审计信息只能作为简短元数据存在，不能成为主体结构。
- next:
  - 新建或继续 workflow 时，按内容摘要标题写笔记条目。

## 全面转换现有 Worklog 为问题和改进笔记

- updated: 2026-04-29 23:38:39 +0800
- cwd: `/home/loviya`
- source instruction: `按照这个要求全面改一下worklog`
- problem:
  - 现有 worklog 文件中仍有大量纯时间标题和旧式 `note` 会话字段，不符合“只记录问题和改进措施”的笔记要求。
- improvement:
  - 已备份原始 worklogs 到 `/tmp/worklogs-before-note-structure-20260429-2239`。
  - 已批量处理 15 个 workflow 文件，排除 `INDEX.md` 和 `README.md`。
  - 将 `### <时间>` 标题转换为概括内容的 `## <问题/目标摘要>` 标题。
  - 将时间改为条目元数据 `updated:`。
  - 将旧的 `note:`、`当前状态`、`当前目标`、`当前阻塞`、`摘要`、`下一步` 字段转换为 `context`、`status`、`problem`、`result`、`next`、`tags`。
- result:
  - `rg '^### [0-9]{4}-[0-9]{2}-[0-9]{2}|^- note:|^## (记录问题和改进|Session update|[0-9]{4}-[0-9]{2}-[0-9]{2})' ~/.codex/worklogs -g '*.md'` 已无匹配。
  - 现有 worklogs 已从会话流水结构迁移为问题/改进笔记结构。
- next:
  - 后续新增或更新 workflow 时，继续使用内容摘要标题和 `problem/improvement/result/next` 笔记字段。

## 增加 codex_notes 作为已解决问题的凝练知识库

- updated: 2026-04-30 17:37:00 +0800
- cwd: `/home/loviya`
- source instruction: `在~/.codex下面写一个codex_notes的目录链接,指向~/obnotes/codex_notes/这个目录,然后这个目录里面的内容是同步worklog里面的内容...只有在解决了问题之后才进行记录`
- problem:
  - worklog 负责记录工作流状态、问题、改进和过程信息，但长期复用时仍偏详细；用户需要一个更凝练的知识库，只保存已经解决的问题和可复用结论。
- improvement:
  - 创建 `/home/loviya/obnotes/codex_notes/`，并在 `/home/loviya/.codex/codex_notes` 建立软链接指向该目录。
  - 新增 `README.md`、`INDEX.md`、`_templates/problem-note.md` 和首条笔记 `system/2026-04-30-codex-notes-workflow.md`。
  - 在 `/home/loviya/.codex/AGENTS.md` 新增 `Codex Notes Knowledge Base` 规则，明确 `codex_notes` 只在问题解决后记录，并且不能替代 worklog。
- result:
  - 以后 Codex 仍先维护 `~/.codex/worklogs/`；当问题解决且有可复用价值时，再写一条短笔记到 `~/.codex/codex_notes/<area>/YYYY-MM-DD-<slug>.md` 并更新 `INDEX.md`。
  - 目录建议为 `system/`、`codex/`、`terminal/`、`obsidian/`，必要时再新增 topic。
- next:
  - 后续解决问题后，按 `codex_notes` 规则沉淀比 worklog 更短的知识笔记。
- tags: codex, worklog, notes, obsidian, knowledge-base

## 将 worklogs 原始文件迁移到 Obsidian vault

- updated: 2026-04-30 17:45:00 +0800
- cwd: `/home/loviya`
- source instruction: `ok,执行worklog的存放`
- problem:
  - 用户希望 worklog 作为笔记资产也由常用 Obsidian vault 管理，而不是原始文件长期放在 `.codex` 运行目录里。
- improvement:
  - 将现有 worklog 内容复制/迁移到 `/home/loviya/obnotes/codex_worklogs`。
  - 原 `/home/loviya/.codex/worklogs` 已改名为备份目录 `/home/loviya/.codex/worklogs.backup-before-obnotes-link-20260430-174333`。
  - 新建软链接 `/home/loviya/.codex/worklogs -> /home/loviya/obnotes/codex_worklogs`。
  - 更新 `/home/loviya/.codex/AGENTS.md` 的 Output Location，说明 worklog 稳定入口仍是 `~/.codex/worklogs`，原始 Markdown 文件实际位于 `~/obnotes/codex_worklogs/`。
- result:
  - `readlink -f ~/.codex/worklogs` 解析为 `/home/loviya/notes/obsidian_notes/codex_worklogs`。
  - `find -L ~/.codex/worklogs -maxdepth 2 -type f | wc -l` 返回 21。
  - 迁移前后文件名列表和 `diff -qr` 对比一致。
- next:
  - 后续 Codex 继续按 `~/.codex/worklogs` 读写；用户可在 Obsidian 中通过 `codex_worklogs/` 查看原始工作流记录。
- tags: codex, worklog, obsidian, symlink, migration

## 为用户指定笔记增加 requested 分区

- updated: 2026-04-30 17:54:00 +0800
- cwd: `/home/loviya`
- source instruction: `对于codex_notes的内容,我经常需要特别制定做笔记的内容,对于这部分内容特别分区,比如上面的内容`
- problem:
  - `codex_notes` 同时需要承载自动从已解决问题提炼的知识，以及用户明确指定“把这部分内容做笔记”的材料；两者来源和保真度不同，混在同一分区会降低可读性。
- improvement:
  - 新增 `/home/loviya/obnotes/codex_notes/requested/` 分区，专门保存用户明确指定的笔记内容。
  - 更新 `codex_notes/README.md` 和 `/home/loviya/.codex/AGENTS.md`，规定用户明确要求对某段回答/上下文做笔记时写入 `requested/`。
  - 新增用户指定笔记 `/home/loviya/obnotes/codex_notes/requested/2026-04-30-codex-file-layout.md`，记录当前 `.codex`、`.codex-a`、`.codex-b`、`.codex-api` 与 Obsidian 目录结构。
  - 更新 `codex_notes/INDEX.md`。
- result:
  - 自动知识沉淀仍按主题放入 `system/`、`codex/`、`terminal/`、`obsidian/`。
  - 用户指定的“上面内容做笔记”统一进入 `requested/`，可保留更多指定内容重点，但仍去除密钥、冗余会话和敏感细节。
- next:
  - 后续用户说“把上面的内容做笔记/记录下来/这部分特别记一下”时，优先写入 `~/.codex/codex_notes/requested/`。
- tags: codex, notes, requested, obsidian

## 将动态维护 AGENTS.md 写成强制流程

- updated: 2026-04-30 18:01:44 +0800
- cwd: `/home/loviya`
- source instruction: `涉及到目录结构和工作流改变的部分,全部都要写回agents.md并且确认...这个动态修改agents.md的流程,也要写入agents.md`
- problem:
  - 目录结构、软链接、工作流规则和记录位置的变更如果只存在于会话或 worklog 中，后续 Codex 启动时可能不会遵守最新约定。
  - 用户要求这种动态维护规则本身也成为 AGENTS.md 的持久规则。
- improvement:
  - 在 `/home/loviya/.codex/AGENTS.md` 中新增 `Dynamic AGENTS.md Maintenance` 小节。
  - 明确目录结构、Obsidian 存储、软链接拓扑、workflow lifecycle、startup/resume、note/write location、account-home sharing、verification steps 等变化都必须同回合写回 AGENTS。
  - 明确写完 AGENTS 后必须用 `rg` 或 `sed` 做 targeted verification。
- result:
  - 已验证 `rg -n "Dynamic AGENTS.md Maintenance|must be written back|目录结构、软链接、工作流规则" ~/.codex/AGENTS.md` 能命中新规则。
- next:
  - 后续结构/流程规则变更必须先改 AGENTS.md 并确认，再在 final 中报告。
- tags: codex, agents, workflow, policy
