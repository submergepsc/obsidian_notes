# OI Wiki crawler

抓取 `https://oi-wiki.org/` 站内页面，并把正文保存为本地 Markdown 文件。

## 安装依赖

```powershell
pip install -r requirements.txt
```

## 运行

```powershell
python run_oiwiki.py --output-dir docs
```

常用参数：

- `--max-pages 200`：限制最多抓取页面数
- `--delay 0.5`：每次请求之间暂停 0.5 秒
- `--timeout 30`：单次请求超时时间
- `--save-every 5`：每处理 5 页保存一次断点
- `--fresh`：忽略已有断点，从头开始抓取

## 断点续爬

程序默认会把抓取状态保存到 `docs/_crawl_state.json`，断电或中断后再次执行同一命令会自动继续。

```powershell
python run_oiwiki.py --output-dir docs
```

如果断点队列已经为空，程序会重新读取 sitemap，并只把尚未访问过的新页面加入队列。

如果你要彻底重跑，显式加上：

```powershell
python run_oiwiki.py --output-dir docs --fresh
```

## 输出

- `docs/*.md`：抓到的 Markdown 页面
- `docs/images/*`：下载到本地的图片
- `docs/_crawl_index.json`：抓取索引和统计信息
- `docs/_crawl_state.json`：断点续爬状态文件

## 生成离线 HTML

```powershell
python build_oiwiki_html.py
```

默认会读取 `docs/`，并把离线 HTML 归档生成到当前 crawl 项目内：

```text
oiwiki_archive/
```

主要入口：

- `oiwiki_archive/index.html`：归档首页
- `oiwiki_archive/html/index.html`：HTML 总索引
- `oiwiki_archive/html/all-pages.html`：全部页面索引
- `oiwiki_archive/html/<group>/index.html`：栏目索引
- `oiwiki_archive/search_index.json`：搜索索引

当前 HTML 归档包含全站搜索、栏目筛选、页内目录、同栏目导航、上一篇/下一篇文章导航，以及对 Markdown 表格的横向滚动渲染。首页左侧主题导航支持进入栏目索引或原地展开页面列表；栏目索引页使用扁平页面列表，不再为单页 subgroup 生成小节。

OI Wiki 站内页面和图片应保持本地化：重建后不应出现指向 `oi-wiki.org` 的在线 `href` 或 `src`。外部参考链接、题库链接、GitHub 链接等仍保留原始 HTTP/HTTPS 链接。
