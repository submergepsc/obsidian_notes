import argparse
import json
import os
import re
import shutil
from dataclasses import dataclass, field
from html import escape
from pathlib import Path
from urllib.parse import urljoin, urlparse


BASE_URL = "https://oi-wiki.org/"
DEFAULT_SOURCE_DIR = Path("docs")
DEFAULT_OUTPUT_DIR = Path("oiwiki_archive")


@dataclass
class Entry:
    title: str
    url: str
    md_path: Path
    html_path: Path
    group: str
    subgroup: str
    source_path: str
    headings: list[tuple[int, str, str]] = field(default_factory=list)


def slugify(value: str) -> str:
    parts: list[str] = []
    for char in value.lower():
        if char.isascii() and char.isalnum():
            parts.append(char)
        elif char in {" ", "-", "_", "/", "."}:
            parts.append("-")
        else:
            parts.append(f"{ord(char):x}")
    slug = re.sub(r"-+", "-", "".join(parts)).strip("-")
    return slug or "page"


def clean_title(title: str) -> str:
    title = title.strip().lstrip("\ufeff")
    title = re.sub(r"\s+-\s+OI Wiki$", "", title)
    return title.strip() or "Untitled"


def title_from_markdown(md_path: Path) -> str:
    try:
        for line in md_path.read_text(encoding="utf-8-sig").splitlines():
            if line.startswith("# "):
                return clean_title(line[2:])
    except UnicodeDecodeError:
        for line in md_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return clean_title(line[2:])
    return clean_title(md_path.stem.replace("__", " / ").replace("-", " "))


def strip_crawl_preamble(md_text: str) -> str:
    return re.sub(r"^\ufeff?# .+? - OI Wiki\s*\n\s*- Source: https?://oi-wiki\.org/\S*\s*\n+", "", md_text, count=1)


def url_parts(url: str) -> list[str]:
    path = urlparse(url).path.strip("/")
    return [part for part in path.split("/") if part]


def group_from_url(url: str) -> str:
    parts = url_parts(url)
    return parts[0] if parts else "home"


def subgroup_from_url(url: str) -> str:
    parts = url_parts(url)
    if len(parts) >= 2:
        return parts[1]
    return "overview"


def category_for_group(group: str) -> str:
    rules = {
        "入门与语言": {"home", "intro", "lang", "basic", "contest"},
        "搜索与枚举": {"search"},
        "数据结构": {"ds"},
        "图论": {"graph"},
        "动态规划": {"dp"},
        "数学": {"math", "geometry"},
        "字符串": {"string"},
        "工具与杂项": {"tools", "misc", "topic", "edit-landing"},
    }
    for category, groups in rules.items():
        if group in groups:
            return category
    return "其他"


def group_label(group: str) -> str:
    labels = {
        "home": "首页",
        "intro": "OI Wiki 介绍",
        "lang": "编程语言",
        "basic": "基础知识",
        "contest": "赛事与实践",
        "search": "搜索",
        "ds": "数据结构",
        "graph": "图论",
        "dp": "动态规划",
        "math": "数学",
        "geometry": "计算几何",
        "string": "字符串",
        "tools": "工具",
        "misc": "杂项",
        "topic": "专题",
        "edit-landing": "编辑说明",
    }
    return labels.get(group, group)


def subgroup_label(subgroup: str) -> str:
    labels = {
        "overview": "概览",
        "opt": "优化",
        "flow": "网络流",
        "graph-matching": "图匹配",
        "tree": "树相关",
        "number-theory": "数论",
        "linear-algebra": "线性代数",
        "combinatorics": "组合数学",
        "game-theory": "博弈论",
        "poly": "多项式",
        "numerical": "数值算法",
        "probability": "概率",
        "csl": "C++ 标准库",
        "pb-ds": "PBDS",
        "editor": "编辑器",
        "judger": "评测工具",
        "testlib": "Testlib",
    }
    return labels.get(subgroup, subgroup)


def html_file_for_url(url: str) -> Path:
    parts = url_parts(url)
    if not parts:
        return Path("html/home/home.html")
    group = parts[0]
    stem = "__".join(parts[1:]) if len(parts) > 1 else "overview"
    return Path("html") / group / f"{slugify(stem)}.html"


def rel_link(current_path: Path, target_path: Path) -> str:
    return Path(os.path.relpath(target_path, current_path.parent)).as_posix()


def load_entries(source_dir: Path, output_dir: Path) -> list[Entry]:
    index_path = source_dir / "_crawl_index.json"
    if not index_path.exists():
        raise FileNotFoundError(f"Missing crawl index: {index_path}")

    index = json.loads(index_path.read_text(encoding="utf-8-sig"))
    entries: list[Entry] = []
    for item in index.get("saved_files", []):
        url = item.get("url", "")
        file_value = item.get("file", "")
        if not url or not file_value:
            continue
        md_path = Path(file_value)
        if not md_path.is_absolute():
            md_path = source_dir.parent / md_path
        if not md_path.exists():
            continue
        html_rel = html_file_for_url(url)
        entries.append(
            Entry(
                title=title_from_markdown(md_path),
                url=url,
                md_path=md_path,
                html_path=output_dir / html_rel,
                group=group_from_url(url),
                subgroup=subgroup_from_url(url),
                source_path=Path(file_value).as_posix(),
            )
        )
    return sorted(entries, key=lambda entry: (entry.group, entry.subgroup, entry.title.lower(), entry.url))


def inline_markdown(
    text: str,
    current_path: Path,
    output_dir: Path,
    url_to_entry: dict[str, Entry],
    page_url: str = "",
) -> str:
    placeholders: list[str] = []

    def placeholder_token(index: int) -> str:
        return f"@@OIHTML{index}@@"

    def stash(value: str) -> str:
        placeholders.append(value)
        return placeholder_token(len(placeholders) - 1)

    def image_repl(match: re.Match[str]) -> str:
        alt = escape(match.group(1), quote=True)
        src = match.group(2).strip()
        if src.startswith("./images/"):
            target = output_dir / "assets" / "images" / src.removeprefix("./images/")
            src = rel_link(current_path, target)
        return stash(f'<img src="{escape(src, quote=True)}" alt="{alt}">')

    def link_repl(match: re.Match[str]) -> str:
        label = inline_markdown(match.group(1), current_path, output_dir, url_to_entry, page_url)
        for index, html in enumerate(placeholders):
            label = label.replace(placeholder_token(index), html)
        href = match.group(2).strip()
        title = ""
        if " " in href and href.endswith('"'):
            href, raw_title = href.rsplit(" ", 1)
            title = raw_title.strip('"')
        target_url = normalize_oiwiki_url(href)
        if target_url not in url_to_entry and page_url and is_local_href(href):
            target_url = normalize_oiwiki_url(urljoin(page_url, href))
        if target_url in url_to_entry:
            href = rel_link(current_path, url_to_entry[target_url].html_path)
        elif href.startswith("./images/"):
            href = rel_link(current_path, output_dir / "assets" / "images" / href.removeprefix("./images/"))
        title_attr = f' title="{escape(title, quote=True)}"' if title else ""
        return stash(f'<a href="{escape(href, quote=True)}"{title_attr}>{label}</a>')

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", image_repl, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, text)
    text = escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    for index, html in enumerate(placeholders):
        text = text.replace(placeholder_token(index), html)
    return text


def normalize_oiwiki_url(href: str) -> str:
    parsed = urlparse(href)
    if parsed.scheme in {"http", "https"} and parsed.netloc == urlparse(BASE_URL).netloc:
        path = parsed.path or "/"
        if path != "/" and not path.endswith("/"):
            path = f"{path}/"
        return f"{BASE_URL.rstrip('/')}{path}"
    return href


def is_local_href(href: str) -> bool:
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc:
        return False
    return not href.startswith(("#", "mailto:", "tel:", "javascript:", "data:"))


def heading_id(text: str, used: set[str]) -> str:
    base = slugify(re.sub(r"<[^>]+>", "", text))
    candidate = base
    counter = 2
    while candidate in used:
        candidate = f"{base}-{counter}"
        counter += 1
    used.add(candidate)
    return candidate


def is_table_row(line: str) -> bool:
    stripped = line.strip()
    return "|" in stripped and not stripped.startswith("```")


def is_table_separator(line: str) -> bool:
    if not is_table_row(line):
        return False
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
        if stripped.endswith("|"):
            stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def render_table(
    table_lines: list[str],
    current_path: Path,
    output_dir: Path,
    url_to_entry: dict[str, Entry],
    page_url: str,
) -> str:
    header = split_table_row(table_lines[0])
    body_rows = [split_table_row(line) for line in table_lines[2:]]
    width = len(header)

    def render_cells(cells: list[str], tag: str) -> str:
        normalized = cells[:width] + [""] * max(0, width - len(cells))
        return "".join(
            f"<{tag}>{inline_markdown(cell, current_path, output_dir, url_to_entry, page_url)}</{tag}>"
            for cell in normalized
        )

    rows = "".join(f"<tr>{render_cells(cells, 'td')}</tr>" for cells in body_rows)
    return (
        '<div class="table-scroll"><table>'
        f"<thead><tr>{render_cells(header, 'th')}</tr></thead>"
        f"<tbody>{rows}</tbody>"
        "</table></div>"
    )


def table_width(line: str) -> int:
    return len(split_table_row(line))


def render_markdown(
    md_text: str,
    current_path: Path,
    output_dir: Path,
    url_to_entry: dict[str, Entry],
    page_url: str,
) -> tuple[str, list[tuple[int, str, str]]]:
    lines = md_text.lstrip("\ufeff").splitlines()
    html_parts: list[str] = []
    headings: list[tuple[int, str, str]] = []
    used_ids: set[str] = set()
    paragraph: list[str] = []
    list_stack: list[str] = []
    in_code = False
    code_lang = ""
    code_lines: list[str] = []
    in_quote = False
    quote_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            joined = " ".join(line.strip() for line in paragraph).strip()
            if joined:
                html_parts.append(f"<p>{inline_markdown(joined, current_path, output_dir, url_to_entry, page_url)}</p>")
            paragraph = []

    def close_lists() -> None:
        while list_stack:
            html_parts.append(f"</{list_stack.pop()}>")

    def flush_quote() -> None:
        nonlocal in_quote, quote_lines
        if in_quote:
            inner = " ".join(line.strip() for line in quote_lines).strip()
            html_parts.append(f"<blockquote>{inline_markdown(inner, current_path, output_dir, url_to_entry, page_url)}</blockquote>")
            in_quote = False
            quote_lines = []

    index = 0
    while index < len(lines):
        raw_line = lines[index]
        index += 1
        line = raw_line.rstrip()
        fence = re.match(r"^```(.*)$", line)
        if fence:
            flush_paragraph()
            close_lists()
            flush_quote()
            if in_code:
                html_parts.append(
                    f'<pre><code class="language-{escape(code_lang, quote=True)}">'
                    f"{escape(chr(10).join(code_lines))}</code></pre>"
                )
                in_code = False
                code_lang = ""
                code_lines = []
            else:
                in_code = True
                code_lang = fence.group(1).strip().split(" ")[0]
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not line.strip():
            flush_paragraph()
            close_lists()
            flush_quote()
            continue

        if line.startswith(">"):
            flush_paragraph()
            close_lists()
            in_quote = True
            quote_lines.append(line.lstrip("> "))
            continue
        flush_quote()

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            close_lists()
            level = len(heading.group(1))
            text = clean_title(heading.group(2))
            rendered_text = inline_markdown(text, current_path, output_dir, url_to_entry, page_url)
            anchor = heading_id(text, used_ids)
            headings.append((level, text, anchor))
            html_parts.append(f'<h{level} id="{escape(anchor)}">{rendered_text}</h{level}>')
            continue

        if index < len(lines) and is_table_row(line) and is_table_separator(lines[index]):
            flush_paragraph()
            close_lists()
            width = table_width(line)
            table_lines = [line, lines[index].rstrip()]
            index += 1
            while index < len(lines) and is_table_row(lines[index]) and table_width(lines[index]) == width:
                table_lines.append(lines[index].rstrip())
                index += 1
            if len(table_lines) > 2:
                html_parts.append(render_table(table_lines, current_path, output_dir, url_to_entry, page_url))
            else:
                paragraph.append(line)
            continue

        item = re.match(r"^\s*[-*]\s+(.+)$", line)
        ordered = re.match(r"^\s*\d+[.)]\s+(.+)$", line)
        if item or ordered:
            flush_paragraph()
            tag = "ol" if ordered else "ul"
            if list_stack != [tag]:
                close_lists()
                html_parts.append(f"<{tag}>")
                list_stack.append(tag)
            value = (ordered or item).group(1)
            html_parts.append(f"<li>{inline_markdown(value, current_path, output_dir, url_to_entry, page_url)}</li>")
            continue

        if re.match(r"^\s*[-*_]{3,}\s*$", line):
            flush_paragraph()
            close_lists()
            html_parts.append("<hr>")
            continue

        paragraph.append(line)

    flush_paragraph()
    close_lists()
    flush_quote()
    if in_code:
        html_parts.append(f"<pre><code>{escape(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(html_parts), headings


def build_group_map(entries: list[Entry]) -> dict[str, list[Entry]]:
    group_map: dict[str, list[Entry]] = {}
    for entry in entries:
        group_map.setdefault(entry.group, []).append(entry)
    return group_map


def build_subgroup_map(entries: list[Entry]) -> dict[str, list[Entry]]:
    subgroup_map: dict[str, list[Entry]] = {}
    for entry in entries:
        subgroup_map.setdefault(entry.subgroup, []).append(entry)
    return subgroup_map


def build_category_map(group_map: dict[str, list[Entry]]) -> dict[str, list[tuple[str, list[Entry]]]]:
    category_map: dict[str, list[tuple[str, list[Entry]]]] = {}
    for group, group_entries in group_map.items():
        category_map.setdefault(category_for_group(group), []).append((group, group_entries))
    return category_map


def render_search_block(title: str, placeholder: str) -> str:
    return (
        '<section class="search-panel">'
        f"<h2>{escape(title)}</h2>"
        '<div class="search-controls">'
        '<label><span>栏目</span><select id="archive-search-group"><option value="">全部栏目</option></select></label>'
        f'<input id="archive-search-input" type="search" placeholder="{escape(placeholder, quote=True)}" autocomplete="off">'
        '<button id="archive-search-clear" type="button">清空</button>'
        "</div>"
        '<p id="archive-search-status" class="search-status">输入标题、栏目或分类关键词。</p>'
        '<ol id="archive-search-results" class="search-results" hidden></ol>'
        "</section>"
    )


def search_items(entries: list[Entry], current_path: Path) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for entry in entries:
        items.append(
            {
                "title": entry.title,
                "group": group_label(entry.group),
                "subgroup": subgroup_label(entry.subgroup),
                "href": rel_link(current_path, entry.html_path),
            }
        )
    return items


def wrap_page(title: str, subtitle: str, body: str, sidebar: str, search_data: list[dict[str, str]]) -> str:
    payload = json.dumps(search_data, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f7f8;
      --panel: #ffffff;
      --ink: #17202a;
      --muted: #5f6c7b;
      --line: #d9e1e8;
      --accent: #0f766e;
      --accent-soft: #d9f3ef;
      --code-bg: #111827;
      --code-ink: #e5e7eb;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: "Noto Sans SC", "Source Han Sans SC", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.65;
    }}
    main {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 24px 20px 56px;
    }}
    .layout {{
      display: grid;
      grid-template-columns: 300px minmax(0, 1fr);
      gap: 20px;
      align-items: start;
    }}
    header, section, article, .sidebar-card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    header {{
      padding: 20px 22px;
      margin-bottom: 20px;
    }}
    header h1 {{
      margin: 0 0 6px;
      font-size: 1.75rem;
      line-height: 1.25;
    }}
    header p, p {{
      color: var(--muted);
    }}
    aside {{
      position: sticky;
      top: 16px;
    }}
    .sidebar-card {{
      padding: 16px;
      max-height: calc(100vh - 32px);
      overflow: auto;
    }}
    .sidebar-card h2, section h2 {{
      margin: 0 0 10px;
      font-size: 1.05rem;
    }}
    a {{
      color: var(--accent);
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    .sidebar-list, .sidebar-sublist {{
      list-style: none;
      margin: 0;
      padding: 0;
    }}
    .sidebar-sublist {{
      margin-top: 8px;
      padding-left: 12px;
      border-left: 1px dashed var(--line);
    }}
    .sidebar-list li {{
      margin: 0 0 9px;
      padding-bottom: 9px;
      border-bottom: 1px solid var(--line);
    }}
    .sidebar-sublist li {{
      border: 0;
      padding-bottom: 0;
      margin-bottom: 7px;
    }}
    .sidebar-list span, .meta {{
      color: var(--muted);
      font-size: 0.9rem;
    }}
    .sidebar-row {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 10px;
    }}
    .sidebar-row a {{
      min-width: 0;
      overflow-wrap: anywhere;
    }}
    .sidebar-row span {{
      flex: 0 0 auto;
    }}
    details summary {{
      cursor: pointer;
      font-weight: 600;
    }}
    .content > section, article {{
      padding: 20px 22px;
      margin-bottom: 18px;
    }}
    article {{
      max-width: 980px;
    }}
    .group-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 14px;
    }}
    .group-card {{
      min-width: 0;
    }}
    .page-list li, .group-card li, .search-results li {{
      margin: 7px 0;
    }}
    .article-nav {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
      gap: 12px;
      margin: 0 0 18px;
    }}
    .article-nav a {{
      display: block;
      min-width: 0;
      padding: 12px 14px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      overflow-wrap: anywhere;
    }}
    .article-nav a:last-child {{
      text-align: right;
    }}
    .search-controls {{
      display: grid;
      grid-template-columns: 180px minmax(0, 1fr) auto;
      gap: 10px;
      align-items: end;
    }}
    .search-controls label {{
      display: grid;
      gap: 4px;
      color: var(--muted);
      font-size: 0.92rem;
    }}
    input, select, button {{
      min-height: 42px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      font: inherit;
      padding: 8px 10px;
    }}
    button {{
      background: var(--accent-soft);
      color: var(--accent);
      cursor: pointer;
      font-weight: 600;
    }}
    mark {{
      background: #f5d76e;
      color: #17202a;
      border-radius: 3px;
      padding: 0 2px;
    }}
    article h1, article h2, article h3, article h4 {{
      line-height: 1.35;
      scroll-margin-top: 20px;
    }}
    article img {{
      max-width: 100%;
      height: auto;
      vertical-align: middle;
    }}
    .table-scroll {{
      overflow: auto;
      margin: 1em 0;
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 680px;
      background: var(--panel);
    }}
    th, td {{
      padding: 8px 10px;
      border: 1px solid var(--line);
      vertical-align: top;
      text-align: left;
    }}
    th {{
      background: #eef7f6;
      color: #123c39;
      font-weight: 700;
    }}
    pre {{
      overflow: auto;
      padding: 14px;
      border-radius: 8px;
      background: var(--code-bg);
      color: var(--code-ink);
    }}
    code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.92em;
      word-break: break-word;
    }}
    p code, li code {{
      background: #eef2f7;
      color: #1f2937;
      border-radius: 4px;
      padding: 0.1em 0.3em;
    }}
    blockquote {{
      margin: 1em 0;
      padding: 0.2em 1em;
      border-left: 4px solid var(--accent);
      background: #f0fdfa;
      color: #334155;
    }}
    @media (max-width: 900px) {{
      .layout {{
        grid-template-columns: 1fr;
      }}
      aside {{
        position: static;
      }}
      .search-controls {{
        grid-template-columns: 1fr;
      }}
      .article-nav {{
        grid-template-columns: 1fr;
      }}
      .article-nav a:last-child {{
        text-align: left;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>{escape(title)}</h1>
      <p>{escape(subtitle)}</p>
    </header>
    <div class="layout">
      <aside>{sidebar}</aside>
      <div class="content">{body}</div>
    </div>
  </main>
  <script id="archive-search-data" type="application/json">{payload}</script>
  <script>
    (() => {{
      const input = document.getElementById("archive-search-input");
      const results = document.getElementById("archive-search-results");
      const status = document.getElementById("archive-search-status");
      const clearButton = document.getElementById("archive-search-clear");
      const groupSelect = document.getElementById("archive-search-group");
      const dataNode = document.getElementById("archive-search-data");
      if (!input || !results || !status || !clearButton || !groupSelect || !dataNode) return;
      let items = [];
      try {{ items = JSON.parse(dataNode.textContent || "[]"); }} catch (_error) {{ return; }}
      const escapeHtml = (value) => value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
      const highlight = (value, query) => {{
        if (!query) return escapeHtml(value);
        const source = value.toLowerCase();
        const needle = query.toLowerCase();
        let cursor = 0;
        let html = "";
        while (cursor < value.length) {{
          const index = source.indexOf(needle, cursor);
          if (index === -1) {{
            html += escapeHtml(value.slice(cursor));
            break;
          }}
          html += escapeHtml(value.slice(cursor, index));
          html += `<mark>${{escapeHtml(value.slice(index, index + needle.length))}}</mark>`;
          cursor = index + needle.length;
        }}
        return html;
      }};
      const groups = [...new Set(items.map((item) => item.group))].sort((a, b) => a.localeCompare(b, "zh-CN"));
      for (const group of groups) {{
        const option = document.createElement("option");
        option.value = group;
        option.textContent = group;
        groupSelect.append(option);
      }}
      const render = () => {{
        const query = input.value.trim().toLowerCase();
        const tokens = query.split(/\\s+/).filter(Boolean);
        const selectedGroup = groupSelect.value;
        const scoped = selectedGroup ? items.filter((item) => item.group === selectedGroup) : items;
        if (!query) {{
          results.hidden = true;
          results.innerHTML = "";
          status.textContent = selectedGroup ? `${{selectedGroup}} 下可搜索 ${{scoped.length}} 个页面。` : `可搜索 ${{items.length}} 个页面。`;
          return;
        }}
        const matches = scoped
          .filter((item) => {{
            const haystack = [item.title, item.group, item.subgroup].join(" ").toLowerCase();
            return tokens.every((token) => haystack.includes(token));
          }})
          .sort((a, b) => a.title.localeCompare(b.title, "zh-CN"));
        results.hidden = matches.length === 0;
        results.innerHTML = matches.slice(0, 100).map((item) =>
          `<li><a href="${{item.href}}">${{highlight(item.title, query)}}</a><div class="meta">${{highlight(item.group, query)}} / ${{highlight(item.subgroup, query)}}</div></li>`
        ).join("");
        status.textContent = matches.length ? `匹配 ${{matches.length}} 个页面，显示前 ${{Math.min(matches.length, 100)}} 个。` : "没有匹配结果。";
      }};
      input.addEventListener("input", render);
      groupSelect.addEventListener("change", render);
      clearButton.addEventListener("click", () => {{
        input.value = "";
        groupSelect.value = "";
        input.focus();
        render();
      }});
      document.addEventListener("keydown", (event) => {{
        if (event.key === "/" && event.target !== input) {{
          event.preventDefault();
          input.focus();
        }}
        if (event.key === "Escape" && document.activeElement === input) {{
          input.value = "";
          render();
        }}
      }});
      const params = new URLSearchParams(window.location.search);
      const initialQuery = params.get("q");
      if (initialQuery) input.value = initialQuery;
      render();
    }})();
  </script>
</body>
</html>
"""


def render_root_index(entries: list[Entry], output_dir: Path, current_path: Path) -> str:
    group_map = build_group_map(entries)
    category_map = build_category_map(group_map)
    order = ["入门与语言", "搜索与枚举", "数据结构", "图论", "动态规划", "数学", "字符串", "工具与杂项", "其他"]
    sidebar_items: list[str] = []
    sections: list[str] = []
    for index, category in enumerate(order):
        groups = category_map.get(category, [])
        if not groups:
            continue
        groups = sorted(groups, key=lambda item: (-len(item[1]), group_label(item[0])))
        anchor = slugify(category)
        nested_items: list[str] = []
        for group, group_entries in groups:
            page_links = "".join(
                f'<li><a href="{escape(rel_link(current_path, entry.html_path))}">{escape(entry.title)}</a></li>'
                for entry in sorted(group_entries, key=lambda item: item.title.lower())
            )
            nested_items.append(
                '<li><details>'
                f'<summary><span class="sidebar-row"><a href="{escape(rel_link(current_path, output_dir / "html" / group / "index.html"))}">{escape(group_label(group))}</a> <span>{len(group_entries)}</span></span></summary>'
                f'<ul class="sidebar-sublist">{page_links}</ul>'
                '</details></li>'
            )
        nested = "".join(nested_items)
        sidebar_items.append(
            f'<li><details{" open" if index == 0 else ""}><summary><a href="#{escape(anchor)}">{escape(category)}</a> <span>{len(groups)}</span></summary><ul class="sidebar-sublist">{nested}</ul></details></li>'
        )
        cards = []
        for group, group_entries in groups:
            samples = "".join(
                f'<li><a href="{escape(rel_link(current_path, entry.html_path))}">{escape(entry.title)}</a></li>'
                for entry in sorted(group_entries, key=lambda item: item.title.lower())[:8]
            )
            cards.append(
                f'<section class="group-card"><h2><a href="{escape(rel_link(current_path, output_dir / "html" / group / "index.html"))}">{escape(group_label(group))}</a></h2>'
                f'<p>{len(group_entries)} pages / {len(build_subgroup_map(group_entries))} subgroups</p><ul>{samples}</ul></section>'
            )
        total = sum(len(group_entries) for _, group_entries in groups)
        sections.append(f'<section id="{escape(anchor)}"><h2>{escape(category)}</h2><p>{total} pages / {len(groups)} groups</p><div class="group-grid">{"".join(cards)}</div></section>')

    sidebar = f'<nav class="sidebar-card"><h2>主题导航</h2><ul class="sidebar-list">{"".join(sidebar_items)}</ul></nav>'
    body = (
        render_search_block("全站搜索", "搜索页面标题、栏目或分类")
        + f'<section><h2>完整索引</h2><p><a href="{escape(rel_link(current_path, output_dir / "html" / "all-pages.html"))}">查看全部 {len(entries)} 个页面</a></p></section>'
        + "".join(sections)
    )
    return wrap_page("OI Wiki Archive", f"离线 HTML 索引，{len(entries)} 个页面，{len(group_map)} 个栏目。", body, sidebar, search_items(entries, current_path))


def render_all_pages(entries: list[Entry], output_dir: Path, current_path: Path) -> str:
    items = "".join(
        f'<li><a href="{escape(rel_link(current_path, entry.html_path))}">{escape(entry.title)}</a> <span>{escape(group_label(entry.group))} / {escape(subgroup_label(entry.subgroup))}</span></li>'
        for entry in sorted(entries, key=lambda item: (group_label(item.group), subgroup_label(item.subgroup), item.title.lower()))
    )
    sidebar = (
        '<nav class="sidebar-card"><h2>索引</h2><ul class="sidebar-list">'
        f'<li><a href="{escape(rel_link(current_path, output_dir / "index.html"))}">归档首页</a></li>'
        f'<li><a href="{escape(rel_link(current_path, output_dir / "html" / "index.html"))}">HTML 总索引</a></li>'
        "</ul></nav>"
    )
    body = render_search_block("全量搜索", "搜索全部页面") + f'<section><h2>全部页面 ({len(entries)})</h2><ol class="page-list">{items}</ol></section>'
    return wrap_page("OI Wiki 全部页面", "按栏目和标题排序的完整页面清单。", body, sidebar, search_items(entries, current_path))


def render_group_index(group: str, entries: list[Entry], output_dir: Path, current_path: Path) -> str:
    sorted_entries = sorted(entries, key=lambda item: (subgroup_label(item.subgroup), item.title.lower()))
    nav_items = "".join(
        f'<li><a href="{escape(rel_link(current_path, entry.html_path))}">{escape(entry.title)}</a></li>'
        for entry in sorted_entries
    )
    page_items = "".join(
        f'<li><a href="{escape(rel_link(current_path, entry.html_path))}">{escape(entry.title)}</a></li>'
        for entry in sorted_entries
    )

    sidebar = (
        '<nav class="sidebar-card"><h2>页内导航</h2><ul class="sidebar-list">'
        f'<li><a href="{escape(rel_link(current_path, output_dir / "index.html"))}">归档首页</a></li>'
        f'<li><a href="{escape(rel_link(current_path, output_dir / "html" / "all-pages.html"))}">全部页面</a></li>'
        f'<li><details open><summary>本栏目页面 <span>{len(entries)}</span></summary><ul class="sidebar-sublist">{nav_items}</ul></details></li>'
        "</ul></nav>"
    )
    body = render_search_block("栏目搜索", f"搜索 {group_label(group)} 下的页面") + f'<section><h2>{escape(group_label(group))} ({len(entries)})</h2><ol class="page-list">{page_items}</ol></section>'
    return wrap_page(f"{group_label(group)} - OI Wiki", f"{len(entries)} 个页面。", body, sidebar, search_items(entries, current_path))


def render_article(entry: Entry, entries: list[Entry], output_dir: Path, url_to_entry: dict[str, Entry]) -> str:
    raw = entry.md_path.read_text(encoding="utf-8-sig")
    raw = strip_crawl_preamble(raw)
    article_html, headings = render_markdown(raw, entry.html_path, output_dir, url_to_entry, entry.url)
    entry.headings = headings
    group_entries = sorted([item for item in entries if item.group == entry.group], key=lambda item: item.title.lower())
    current_index = group_entries.index(entry)
    previous_entry = group_entries[current_index - 1] if current_index > 0 else None
    next_entry = group_entries[current_index + 1] if current_index + 1 < len(group_entries) else None
    group_links = "".join(
        f'<li><a href="{escape(rel_link(entry.html_path, item.html_path))}">{escape(item.title)}</a></li>'
        for item in group_entries
    )
    heading_links = "".join(
        f'<li><a href="#{escape(anchor)}">{escape(text)}</a></li>'
        for level, text, anchor in headings
        if level <= 3
    )
    sidebar = (
        '<nav class="sidebar-card"><h2>页面导航</h2><ul class="sidebar-list">'
        f'<li><a href="{escape(rel_link(entry.html_path, output_dir / "index.html"))}">归档首页</a></li>'
        f'<li><a href="{escape(rel_link(entry.html_path, output_dir / "html" / entry.group / "index.html"))}">{escape(group_label(entry.group))} 索引</a></li>'
        f'<li><details open><summary>本文目录</summary><ul class="sidebar-sublist">{heading_links}</ul></details></li>'
        f'<li><details><summary>同栏目页面</summary><ul class="sidebar-sublist">{group_links}</ul></details></li>'
        "</ul></nav>"
    )
    previous_link = (
        f'<a href="{escape(rel_link(entry.html_path, previous_entry.html_path))}"><span class="meta">上一篇</span><br>{escape(previous_entry.title)}</a>'
        if previous_entry
        else "<span></span>"
    )
    next_link = (
        f'<a href="{escape(rel_link(entry.html_path, next_entry.html_path))}"><span class="meta">下一篇</span><br>{escape(next_entry.title)}</a>'
        if next_entry
        else "<span></span>"
    )
    article_nav = f'<nav class="article-nav">{previous_link}{next_link}</nav>'
    body = (
        f"{article_nav}"
        "<article>"
        f'<p class="meta">本地源文件：<code>{escape(entry.source_path)}</code></p>'
        f"{article_html}</article>"
        f"{article_nav}"
    )
    return wrap_page(entry.title, f"{group_label(entry.group)} / {subgroup_label(entry.subgroup)}", body, sidebar, search_items(entries, entry.html_path))


def copy_assets(source_dir: Path, output_dir: Path) -> int:
    image_source = source_dir / "images"
    image_target = output_dir / "assets" / "images"
    if not image_source.exists():
        return 0
    image_target.mkdir(parents=True, exist_ok=True)
    count = 0
    for path in image_source.iterdir():
        if path.is_file():
            shutil.copy2(path, image_target / path.name)
            count += 1
    return count


def build_archive(source_dir: Path, output_dir: Path) -> dict[str, int]:
    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    entries = load_entries(source_dir, output_dir)
    if not entries:
        raise RuntimeError(f"No pages found under {source_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "html").mkdir(parents=True, exist_ok=True)
    copied_assets = copy_assets(source_dir, output_dir)
    url_to_entry = {entry.url: entry for entry in entries}

    for entry in entries:
        entry.html_path.parent.mkdir(parents=True, exist_ok=True)
        entry.html_path.write_text(render_article(entry, entries, output_dir, url_to_entry), encoding="utf-8")

    group_map = build_group_map(entries)
    for group, group_entries in group_map.items():
        group_index = output_dir / "html" / group / "index.html"
        group_index.parent.mkdir(parents=True, exist_ok=True)
        group_index.write_text(render_group_index(group, group_entries, output_dir, group_index), encoding="utf-8")

    root_index = output_dir / "index.html"
    root_index.write_text(render_root_index(entries, output_dir, root_index), encoding="utf-8")
    html_index = output_dir / "html" / "index.html"
    html_index.write_text(render_root_index(entries, output_dir, html_index), encoding="utf-8")
    all_pages = output_dir / "html" / "all-pages.html"
    all_pages.write_text(render_all_pages(entries, output_dir, all_pages), encoding="utf-8")

    search_payload = [
        {
            "title": entry.title,
            "group": entry.group,
            "group_label": group_label(entry.group),
            "subgroup": entry.subgroup,
            "subgroup_label": subgroup_label(entry.subgroup),
            "html": Path(os.path.relpath(entry.html_path, output_dir)).as_posix(),
            "source": entry.source_path,
        }
        for entry in entries
    ]
    (output_dir / "search_index.json").write_text(json.dumps(search_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest = {
        "source_dir": source_dir.as_posix(),
        "pages": len(entries),
        "groups": len(group_map),
        "assets": copied_assets,
        "entry": "index.html",
    }
    (output_dir / "_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"pages": len(entries), "groups": len(group_map), "assets": copied_assets}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build an offline OI Wiki HTML archive from crawled Markdown.")
    parser.add_argument("--source-dir", default=str(DEFAULT_SOURCE_DIR), help="Crawled Markdown directory.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="HTML archive output directory.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_archive(Path(args.source_dir), Path(args.output_dir))
    print(
        "HTML archive generated: "
        f"pages={result['pages']}, groups={result['groups']}, assets={result['assets']}"
    )


if __name__ == "__main__":
    main()
