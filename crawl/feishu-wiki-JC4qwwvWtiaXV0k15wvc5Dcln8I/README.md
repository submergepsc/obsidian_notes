# Feishu Wiki Crawl

- source: https://ycnw11in464y.feishu.cn/wiki/JC4qwwvWtiaXV0k15wvc5Dcln8I
- title: 第二周实验：Linux常用命令与ARM汇编语言
- crawled at: 2026-05-14 20:40 +0800
- Markdown export: `第二周实验：Linux常用命令与ARM汇编语言.md`
- captured page: `page.html`
- captured cookies: `cookies.txt`
- assets: `assets/`
- metadata: `metadata/`

## Contents

- `metadata/client_vars.json`: parsed Feishu SSR client payload containing `block_map`.
- `metadata/server_data.json`: parsed Feishu page metadata.
- `metadata/images.json`: downloaded image token, filename, and byte-size manifest.
- `extract_feishu_doc.py`: repeatable extractor for the saved `page.html`.

## Notes

The page was accessible through the public SSR HTML response. The extractor converts the embedded Feishu document blocks to Markdown and downloads the two embedded images through the Feishu box stream endpoint.
