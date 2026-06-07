---
id: 20260514-feishu-wiki-jc4q-crawl
name: Feishu Wiki JC4q Crawl
slug: feishu-wiki-jc4q-crawl
cwd: /home/loviya/notes/obsidian_notes/25_2/os/class/11w
summary: 将飞书 wiki 页面 `JC4qwwvWtiaXV0k15wvc5Dcln8I` 抓取到 Obsidian crawl 目录。
tags:
  - feishu
  - wiki
  - crawl
  - obsidian
priority: normal
---

# Feishu Wiki JC4q Crawl

## 当前快照

- 状态: 已完成
- 目标: 把 `https://ycnw11in464y.feishu.cn/wiki/JC4qwwvWtiaXV0k15wvc5Dcln8I` 的内容爬到 `~/obnotes/crawl/`。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-14 20:39:58 +0800

## 关键结果

- 归档目录：`/home/loviya/obnotes/crawl/feishu-wiki-JC4qwwvWtiaXV0k15wvc5Dcln8I/`
- Markdown 导出：`第二周实验：Linux常用命令与ARM汇编语言.md`，425 行。
- 原始页面和登录跳转后 Cookie：`page.html`、`cookies.txt`。
- 元数据：`metadata/client_vars.json`、`metadata/server_data.json`、`metadata/images.json`。
- 图片资源：`assets/WlsmbZWUKohBqKx4qTKccrOLnne.png`、`assets/AjsKbYm6vo64SzxAoPScVnM8nvc.png`。
- 可重跑脚本：`extract_feishu_doc.py`。

## 决策

- 按爬取工作区规则，新飞书目标使用独立目录 `~/obnotes/crawl/feishu-wiki-JC4qwwvWtiaXV0k15wvc5Dcln8I/`，不混入 5 月 9 日的 `EKAN...` 归档。
- 该页面的 SSR HTML 已包含文档 `block_map`，因此直接从保存的 HTML 解析并转换 Markdown，而不是依赖浏览器导出。

## 抓取飞书文档页面并转换为 Markdown

- 更新时间: 2026-05-14 20:39:58 +0800
- 工作目录: `/home/loviya/notes/obsidian_notes/25_2/os/class/11w`
- 来源指令: `https://ycnw11in464y.feishu.cn/wiki/JC4qwwvWtiaXV0k15wvc5Dcln8I帮我吧这个内容爬下来,放到之前的obnotes/crawl里面`
- 问题:
  - 用户需要把飞书 wiki 文档内容保存到此前约定的 Obsidian crawl 目录。
  - 旧飞书归档 workflow 是另一个 wiki token 且已完成，不能混用目录。
- 改进:
  - 新建自包含目录，保存页面 HTML 和 cookies。
  - 从 SSR `clientVars` 中提取 `block_map`，生成 Markdown 和 JSON 元数据。
  - 使用飞书 box stream 下载接口保存文档内两张图片。
- 结果:
  - 已生成可读 Markdown、图片、README、原始 HTML、Cookie、元数据和可重跑提取脚本。
  - 脚本语法检查通过；网络图片下载需要沙箱外权限，已通过批准后完成。
- 下一步:
  - 无。
