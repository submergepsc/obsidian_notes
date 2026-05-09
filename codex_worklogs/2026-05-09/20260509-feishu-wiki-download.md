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

- status: 进行中
- goal: 下载 `https://ycnw11in464y.feishu.cn/wiki/EKANwPkB8iXXm4kCS9ac926Oncc` 可访问的所有文件。
- blocker: 尚未确认飞书 wiki 页面是否公开可访问，以及是否需要登录 Cookie/API token。
- next: 探测分享页和接口响应，若可访问则枚举并下载文件到 `~/obnotes/crawl/feishu-wiki-EKANwPkB8iXXm4kCS9ac926Oncc/`。
- updated: 2026-05-09 21:07:10 +0800

## Key Results

- 下载目标目录：`/home/loviya/obnotes/crawl/feishu-wiki-EKANwPkB8iXXm4kCS9ac926Oncc/`。

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
  - 待探测。
- next:
  - 使用 HTTP 请求保存页面响应并分析是否需要用户提供登录凭据。
