---
id: 20260428-oiwiki-crawl
name: oiwiki crawl
slug: oiwiki-crawl
cwd: /home/loviya/notes/obsidian_notes/crawl/oiwiki
summary: OI Wiki Markdown crawl and self-contained offline HTML archive completed.
tags:
  - oiwiki
  - crawl
  - obsidian
priority: medium
---

# oiwiki crawl

## Sessions

## 从 docs/_crawl_state.json 续爬 OI Wiki，并保证本地 Ma...
- updated: 2026-04-28 12:57:52 +0800
- cwd: `/home/loviya/notes/obsidian_notes/crawl/oiwiki`
- host: `nibaba`
- tmux: ``
- source instruction: `继续爬取oiwiki的工作流`
- context: 未在旧 worklog 中找到直接的 `oiwiki` 记录；根据 `/home/loviya/notes/obsidian_notes/crawl/oiwiki` 中的爬虫和断点创建本工作流。
- status: 已完成
- problem:
  - goal: 从 `docs/_crawl_state.json` 续爬 OI Wiki，并保证本地 Markdown 内容可用。
  - blocker: 无。
- result:
  - 创建本地 `.venv` 并安装 `requests`、`beautifulsoup4`、`html2text`。先从断点把队列从 `visited=320, saved=236, queue=133` 续到 `visited=453, saved=369, queue=0`；随后把历史 `skipped_urls=84` 重新入队并成功补齐，得到 `visited=453, saved=453, queue=0, skipped=0`。最后运行 `--repair-existing` 重抓 453 个已保存页面，修复旧文件乱码和索引中旧路径格式。最终 `docs/_crawl_index.json` 为 `visited_count=453, queued_count=0, saved_count=453, skipped_count=0`，`docs/` 有 453 个 Markdown 文件、`docs/images/` 有 616 个资源文件。
- next: 无；如未来更新 OI Wiki，可在本目录运行 `.venv/bin/python run_oiwiki.py --output-dir docs` 继续增量抓取，必要时再运行 `--repair-existing`。
- tags: oiwiki, crawl, obsidian
## 让已完成队列的续爬也能发现 sitemap 中后续新增页面，并执行一次增量检查
- updated: 2026-04-28 14:03:36 +0800
- cwd: `/home/loviya/notes/obsidian_notes/crawl/oiwiki`
- host: `nibaba`
- tmux: `unavailable`
- source instruction: `继续爬取oiwiki的工作`
- context: 用户明确要求继续 `oiwiki` 爬取，接续已完成的同一 workflow。
- status: 已完成
- problem:
  - goal: 让已完成队列的续爬也能发现 sitemap 中后续新增页面，并执行一次增量检查。
  - blocker: 无。
- result:
  - 已修改 `run_oiwiki.py`：当断点存在且队列为空时，会重新读取 sitemap，并把尚未访问的新 URL 加入队列。同步更新 README 续爬说明。语法校验 `.venv/bin/python -m py_compile run_oiwiki.py` 通过。实际运行 `.venv/bin/python run_oiwiki.py --output-dir docs` 后，sitemap 可读取但没有发现新页面；最终仍为 `visited=453, queued=0, saved=453, skipped=0`，`docs/` 中 Markdown 文件 453 个，`docs/images/` 资源 616 个。
- next: 无；之后继续运行 `.venv/bin/python run_oiwiki.py --output-dir docs` 即可自动检查 sitemap 新页面。
- tags: oiwiki, crawl, obsidian
## 仿照菜鸟教程归档，为 OI Wiki 生成 vault 根目录下的离线 HTML 归档和...
- updated: 2026-04-28 14:24:49 +0800
- cwd: `/home/loviya/notes/obsidian_notes/crawl/oiwiki`
- host: `nibaba`
- tmux: `unavailable`
- source instruction: `仿照爬取的菜鸟教程的内容,做一个离线 html，并且索引这些都要齐全`
- context: 用户明确要求继续 OI Wiki，并更正目标位置为 `/home/loviya/notes/obsidian_notes` vault 内。
- status: 已完成
- problem:
  - goal: 仿照菜鸟教程归档，为 OI Wiki 生成 vault 根目录下的离线 HTML 归档和完整索引。
  - blocker: 无。
- result:
  - 新增 `build_oiwiki_html.py`，默认读取 `crawl/oiwiki/docs`，输出到 `/home/loviya/notes/obsidian_notes/oiwiki_archive`。生成内容包括 `index.html`、`html/index.html`、`html/all-pages.html`、16 个栏目索引、465 篇文章 HTML、`search_index.json`、`_manifest.json` 和 `assets/images`。检查中发现旧爬虫误跳过 `/search/` 算法栏目，已从 `SKIP_PATH_PREFIXES` 移除 `/search/`，续爬补齐 12 页，最终 crawl 统计为 `visited=465, queued=0, saved=465, skipped=0`。重新生成 HTML 后 manifest 为 `pages=465, groups=16, assets=635`，HTML 文件 483 个，资源 635 个，搜索索引 465 条；NUL 占位符检查为 0。剩余本地引用检查中的 58 项为 Markdown 示例链接或数学文本被简易解析器误判，不影响归档索引和已抓页面跳转。
- next: 无；如需重建，进入 `crawl/oiwiki` 运行 `.venv/bin/python build_oiwiki_html.py`。
- tags: oiwiki, crawl, html, obsidian
## 把 vault 根目录的 oiwiki_archive 收进 crawl/oiwiki...
- updated: 2026-04-28 14:31:32 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `unavailable`
- source instruction: `把~/obnotes/oiwiki_archive和~/obnotes/crawl/oiwiki合并,存到crawl里面`
- context: 继续 OI Wiki 归档路径整理。
- status: 已完成
- problem:
  - goal: 把 vault 根目录的 `oiwiki_archive` 收进 `crawl/oiwiki` 项目目录。
  - blocker: 无。
- result:
  - 已将 `/home/loviya/obnotes/oiwiki_archive` 移动到 `/home/loviya/obnotes/crawl/oiwiki/oiwiki_archive`。同步把 `build_oiwiki_html.py` 默认输出从 `../../oiwiki_archive` 改成 `oiwiki_archive`，并更新 README。校验 `.venv/bin/python -m py_compile build_oiwiki_html.py run_oiwiki.py` 通过；旧路径不存在，新入口、manifest 和 483 个 HTML 文件存在。
- next: 无；归档入口已改为 `/home/loviya/obnotes/crawl/oiwiki/oiwiki_archive/index.html`。
- tags: oiwiki, crawl, html, obsidian
## 优化 oiwiki_archive 本地 HTML 阅读和导航体验，并保持可重建
- updated: 2026-04-28 21:29:16 +0800
- cwd: `/home/loviya/notes/obsidian_notes/crawl/oiwiki`
- host: `nibaba`
- tmux: `/tmp/tmux-1000/default,5441,2`
- source instruction: `你继续调整~/obnotes/crawl/oiwiki的工作流,优化这个本地网页`
- context: 用户明确要求继续 `~/obnotes/crawl/oiwiki` 的 OI Wiki workflow，接续本文件。
- status: 已完成
- problem:
  - goal: 优化 `oiwiki_archive` 本地 HTML 阅读和导航体验，并保持可重建。
  - blocker: 无。
- result:
  - 已优化 `build_oiwiki_html.py` 并重新生成归档：新增 Markdown 表格渲染和横向滚动样式，保守处理含原始 `|` 的公式表格行；文章页新增上一篇/下一篇导航；搜索支持多关键词匹配和 `?q=` 初始查询；文章宽度、表格、移动端导航样式同步优化。更新 README 说明。校验 `.venv/bin/python -m py_compile build_oiwiki_html.py` 通过；重建结果为 `pages=465, groups=16, assets=635`，HTML 文件 484 个，归档目录约 95M。
- next: 无；归档入口仍为 `/home/loviya/obnotes/crawl/oiwiki/oiwiki_archive/index.html`，重建命令为 `.venv/bin/python build_oiwiki_html.py`。
- tags: oiwiki, crawl, html, obsidian, offline-archive
## 保留外站 HTTP/HTTPS 链接，但将所有 oi-wiki.org 站内导航改成本地...
- updated: 2026-04-28 21:39:35 +0800
- cwd: `/home/loviya/notes/obsidian_notes/crawl/oiwiki`
- host: `nibaba`
- tmux: `/tmp/tmux-1000/default,5441,2`
- source instruction: `外部的链接仍然作为http的导航留着,所有oiwiki中存在的内容都下载到本地`
- context: 继续 OI Wiki 离线 HTML 本地化调整。
- status: 已完成
- problem:
  - goal: 保留外站 HTTP/HTTPS 链接，但将所有 `oi-wiki.org` 站内导航改成本地文件，并确认站内内容已抓全。
  - blocker: 无。
- result:
  - 运行 `.venv/bin/python run_oiwiki.py --output-dir docs` 检查 sitemap，未发现新增页面，统计保持 `visited=465, queued=0, saved=465, skipped=0`。修改 `build_oiwiki_html.py`：按域名归一化 `https://oi-wiki.org`、`https://oi-wiki.org/` 和带 query 的站内链接到本地 HTML；去掉文章正文中的抓取 Source 前导元信息，文章顶部只显示本地源文件；搜索数据改用本地源文件路径，不再嵌入原始 OI Wiki URL。重新生成后 `pages=465, groups=16, assets=635`，HTML 文件 484 个；检查确认归档中无 `href/src` 指向 `oi-wiki.org`，外部站点链接仍保留 HTTP/HTTPS。
- next: 无；未来重建后可用 `rg -n 'href="https?://oi-wiki\\.org|src="https?://oi-wiki\\.org' oiwiki_archive --glob '*.html' --glob '*.json'` 检查。
- tags: oiwiki, crawl, html, local-links, offline-archive
## 去掉首页、总索引、全部页面索引中无用的线上 URL 展示文本
- updated: 2026-04-28 21:45:19 +0800
- cwd: `/home/loviya/notes/obsidian_notes/crawl/oiwiki`
- host: `nibaba`
- tmux: `/tmp/tmux-1000/default,5441,2`
- source instruction: `index页面存在很多https的显示内容,我根本不会去打开,没必要显示这些,全部删掉或者隐藏`
- context: 继续 OI Wiki 离线 HTML 索引页展示精简。
- status: 已完成
- problem:
  - goal: 去掉首页、总索引、全部页面索引中无用的线上 URL 展示文本。
  - blocker: 无。
- result:
  - 已修改 `build_oiwiki_html.py`，移除 `all-pages.html` 和栏目索引中每条页面下方显示的原始 `https://oi-wiki.org/...`；搜索结果不再展示源文件或 URL；首页搜索占位文案移除 URL 字样；内嵌搜索数据不再携带 source 字段。重新生成归档后，检查 `index.html`、`html/index.html`、`html/all-pages.html` 均无 `https://oi-wiki.org`、无 `<code>https://...` 展示项、无旧 URL 占位文案；全归档仍无 `href/src` 指向 `oi-wiki.org`。
- next: 无。
- tags: oiwiki, html, index, local-links
## 左侧悬浮导航支持进入栏目页或原地展开页面；删除单页 subgroup 小节
- updated: 2026-04-28 21:51:47 +0800
- cwd: `/home/loviya/notes/obsidian_notes/crawl/oiwiki`
- host: `nibaba`
- tmux: `unavailable`
- source instruction: `左侧的悬浮窗口不是不展开,改成可选是否进去或者展开`
- context: 继续 OI Wiki 离线 HTML 导航体验调整。
- status: 已完成
- problem:
  - goal: 左侧悬浮导航支持进入栏目页或原地展开页面；删除单页 subgroup 小节。
  - blocker: 无。
- result:
  - 修改 `build_oiwiki_html.py`：首页左侧主题导航变为 category -> group -> page 的多层 details；group summary 保留栏目索引链接，展开后直接列出页面链接；栏目索引页改成扁平页面列表，不再按 subgroup 生成 `iterative (1)` 等小节。同步更新 README。重新生成归档，校验 py_compile 和 build 通过；仍无 `href/src` 指向 `oi-wiki.org`，HTML 文件 484 个。
- next: 无。
- tags: oiwiki, html, sidebar, navigation
