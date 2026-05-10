---
id: 20260509-feishu-wiki-download
name: Feishu Wiki File Download
slug: feishu-wiki-download
cwd: /home/loviya
summary: Download all files reachable from a Feishu wiki URL into a self-contained crawl directory.
tags:
  - feishu
  - wiki
  - crawl
  - download
priority: normal
---

# Feishu Wiki File Download

## Current Snapshot

- status: 已完成
- goal: 下载 `https://ycnw11in464y.feishu.cn/wiki/EKANwPkB8iXXm4kCS9ac926Oncc` 可访问的直接文件。
- blocker: 无；飞书文档页面节点不是直接 PDF 文件，已记录链接和元数据。
- next: 无；如需把 9 个飞书文档页面也导出为 PDF/Word，需要登录态或进一步确认导出权限。
- updated: 2026-05-09 21:56:00 +0800

## Key Results

- 下载目标目录：`/home/loviya/obnotes/crawl/feishu-wiki-EKANwPkB8iXXm4kCS9ac926Oncc/`。
- 已下载 16 个 PDF 到 `downloads/`，合计约 40M。
- 已保存清单：`metadata/downloaded_pdfs.tsv`、`metadata/all_nodes.tsv`、`metadata/doc_nodes.tsv`。
- 飞书 wiki 树中另有 9 个 `obj_type=22` 页面节点，已记录链接但不是直接二进制文件。

## Decisions

- 按全局规则，网页/资料抓取归档放在 `~/obnotes/crawl/` 下，每个目标使用独立目录。

## 探测飞书 Wiki 链接并下载可访问文件

- updated: 2026-05-09 21:07:10 +0800
- cwd: `/home/loviya`
- source instruction: `我想要把https://ycnw11in464y.feishu.cn/wiki/EKANwPkB8iXXm4kCS9ac926Oncc这个地址的所有文件下载下来`
- problem:
  - 需要下载飞书 wiki 地址的所有文件，但尚不知道页面权限、文件枚举方式和下载接口。
- improvement:
  - 先创建自包含 crawl 目录，再探测公开页面、页面脚本和可能的附件接口。
- result:
  - 通过匿名会话访问到页面 HTML，定位 `space_id=7612526296744135617`、`wiki_token=EKANwPkB8iXXm4kCS9ac926Oncc`、当前 PDF 对象 `obj_token=CTPfbdHGgorfbpxCyoTc2DTKnOg`。
  - 使用 `/space/api/wiki/v2/tree/get_info/` 枚举知识库树，发现 16 个 PDF 文件节点、9 个飞书文档页面节点、1 个根占位节点。
  - 使用 `/space/api/box/stream/download/all/<obj_token>/?mount_node_token=<wiki_token>&mount_point=wiki` 下载 16 个 PDF 到 `downloads/`。
  - 生成 `README.md` 和 metadata 清单，便于核对下载位置与未直接下载的页面链接。
- next:
  - 无；若用户还需要导出 9 个飞书文档页面，需要继续尝试导出接口或提供已登录浏览器 Cookie。
