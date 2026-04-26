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

如果你要彻底重跑，显式加上：

```powershell
python run_oiwiki.py --output-dir docs --fresh
```

## 输出

- `docs/*.md`：抓到的 Markdown 页面
- `docs/images/*`：下载到本地的图片
- `docs/_crawl_index.json`：抓取索引和统计信息
- `docs/_crawl_state.json`：断点续爬状态文件
