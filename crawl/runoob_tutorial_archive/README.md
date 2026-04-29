# Runoob Scraper

这个目录下的 `runoob_scraper.py` 用来抓取菜鸟教程页面，并保存为三份内容：

- `html/`: 原始 HTML
- `text/`: 提取后的纯文本
- `meta/`: 页面元数据

默认行为：

- 从 `https://www.runoob.com/sitemap` 开始抓
- 只抓取 `runoob.com` 站内页面
- 默认每次请求间隔 `1` 秒
- 默认排除一些明显不属于教程正文的路径
- 支持通过 `state.json` 断点续跑

## 常用命令

先试抓少量页面：

```bash
python3 runoob_scraper.py --max-pages 20 --drop-query --resume
```

抓取更多教程页，并限制在教程相关 URL：

```bash
python3 runoob_scraper.py \
  --include-regex '/(python|java|sql|linux|git|docker|react|vue)/' \
  --drop-query \
  --resume
```

完整抓取站点地图能发现的大量页面：

```bash
python3 runoob_scraper.py --drop-query --resume
```

## 输出结构

默认输出到 `runoob_archive/`：

```text
runoob_archive/
  html/
  text/
  meta/
  state.json
```

## 说明

- 这个脚本使用 `requests` + Python 标准库，不依赖 `bs4`
- 提取出的 `text` 是通用清洗结果，不是精细排版版 Markdown
- 如果只想抓某一门教程，可以改 `--start-url`，例如：

```bash
python3 runoob_scraper.py \
  --start-url https://www.runoob.com/python3/python3-tutorial.html \
  --include-regex '/python3/' \
  --drop-query \
  --resume
```
