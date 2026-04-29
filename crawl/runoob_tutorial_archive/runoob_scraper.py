#!/usr/bin/env python3
from __future__ import annotations

import argparse
from html import escape
import json
import os
import re
import sys
import time
from collections import deque
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse, urlunparse

import requests


DEFAULT_START_URL = "https://www.runoob.com/sitemap"
DEFAULT_DOMAIN = "www.runoob.com"
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36 runoob-archiver/1.0"
)
NON_HTML_SUFFIXES = {
    ".7z",
    ".apk",
    ".avi",
    ".bmp",
    ".css",
    ".csv",
    ".doc",
    ".docx",
    ".epub",
    ".gif",
    ".gz",
    ".ico",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".m4a",
    ".mkv",
    ".mov",
    ".mp3",
    ".mp4",
    ".pdf",
    ".png",
    ".ppt",
    ".pptx",
    ".rar",
    ".rss",
    ".svg",
    ".tar",
    ".tgz",
    ".txt",
    ".wav",
    ".webm",
    ".webp",
    ".xml",
    ".xz",
    ".zip",
}


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.title: str = ""
        self._in_title = False
        self._title_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            attr_map = dict(attrs)
            href = attr_map.get("href")
            if href:
                self.links.append(href.strip())
        elif tag == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
            self.title = "".join(self._title_parts).strip()

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)


class HrefExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        attr_map = dict(attrs)
        href = attr_map.get("href")
        if href:
            self.hrefs.append(href.strip())


class TextExtractor(HTMLParser):
    BLOCK_TAGS = {
        "article",
        "aside",
        "blockquote",
        "br",
        "div",
        "dt",
        "dd",
        "fieldset",
        "figcaption",
        "figure",
        "footer",
        "form",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "hr",
        "li",
        "main",
        "nav",
        "ol",
        "p",
        "pre",
        "section",
        "table",
        "td",
        "th",
        "tr",
        "ul",
    }
    SKIP_TAGS = {"script", "style", "noscript", "svg", "canvas"}
    SKIP_ATTR_KEYWORDS = {
        "breadcrumb",
        "comment",
        "copyright",
        "footer",
        "header",
        "menu",
        "nav",
        "notice",
        "sidebar",
        "toolbar",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self._skip_depth > 0:
            self._skip_depth += 1
            return

        if tag in self.SKIP_TAGS or self._should_skip_attrs(attrs):
            self._skip_depth = 1
            return

        if tag == "br":
            self.parts.append("\n")
        elif tag in self.BLOCK_TAGS:
            self.parts.append("\n\n")

    def handle_endtag(self, tag: str) -> None:
        if self._skip_depth > 0:
            self._skip_depth -= 1
            return

        if tag in self.BLOCK_TAGS:
            self.parts.append("\n\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth > 0:
            return
        text = data.strip()
        if text:
            self.parts.append(text)
            self.parts.append(" ")

    def _should_skip_attrs(self, attrs: list[tuple[str, str | None]]) -> bool:
        for key, value in attrs:
            if key not in {"id", "class", "role"} or not value:
                continue
            lowered = value.lower()
            if any(keyword in lowered for keyword in self.SKIP_ATTR_KEYWORDS):
                return True
        return False

    def get_text(self) -> str:
        text = "".join(self.parts)
        text = unescape(text)
        text = text.replace("\xa0", " ")
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


class LocalLinkRewriter(HTMLParser):
    URL_ATTRS = {"href", "src", "action"}

    def __init__(self, rewrite_attr) -> None:
        super().__init__(convert_charrefs=False)
        self.rewrite_attr = rewrite_attr
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.parts.append(self._render_tag(tag, attrs, closed=False))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.parts.append(self._render_tag(tag, attrs, closed=True))

    def handle_endtag(self, tag: str) -> None:
        self.parts.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def handle_comment(self, data: str) -> None:
        self.parts.append(f"<!--{data}-->")

    def handle_decl(self, decl: str) -> None:
        self.parts.append(f"<!{decl}>")

    def handle_entityref(self, name: str) -> None:
        self.parts.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        self.parts.append(f"&#{name};")

    def handle_pi(self, data: str) -> None:
        self.parts.append(f"<?{data}>")

    def unknown_decl(self, data: str) -> None:
        self.parts.append(f"<![{data}]>")

    def _render_tag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
        closed: bool,
    ) -> str:
        rendered = [f"<{tag}"]
        for key, value in attrs:
            if value is None:
                rendered.append(f" {key}")
                continue
            if key.lower() in self.URL_ATTRS:
                value = self.rewrite_attr(key.lower(), value)
            escaped = escape(value, quote=True)
            rendered.append(f' {key}="{escaped}"')
        rendered.append(" />" if closed else ">")
        return "".join(rendered)

    def get_html(self) -> str:
        return "".join(self.parts)


@dataclass
class PageResult:
    url: str
    title: str
    links: list[str]
    text: str
    status_code: int
    content_type: str
    html: str


class RunoobScraper:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.output_dir = Path(args.output).resolve()
        self.state_file = self.output_dir / "state.json"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        (self.output_dir / "html").mkdir(exist_ok=True)
        (self.output_dir / "text").mkdir(exist_ok=True)
        (self.output_dir / "meta").mkdir(exist_ok=True)

        self.session = requests.Session()
        self.session.headers.update({"User-Agent": args.user_agent})
        self.allowed_hosts = {
            host.strip().lower()
            for host in args.allowed_host
            if host.strip()
        }
        self.include_patterns = [re.compile(p) for p in args.include_regex]
        self.exclude_patterns = [re.compile(p) for p in args.exclude_regex]

        self.visited: set[str] = set()
        self.failed: dict[str, str] = {}
        self.queue: deque[str] = deque()
        self.saved_count = 0
        self.skip_count = 0

    def run(self) -> int:
        if self.args.backfill_missing_only:
            missing_urls = self.collect_missing_link_urls()
            for url in reversed(missing_urls):
                self.queue.appendleft(url)
            print(f"Queued {len(missing_urls)} missing target URLs")
            return self._crawl_queue()

        if self.args.build_index_only:
            generated = self.build_index_pages()
            print(f"Built {generated} index page(s)")
            return 0

        if self.args.rewrite_only:
            rewritten = self.rewrite_saved_html()
            print(f"Rewritten local links for {rewritten} saved pages")
            return 0

        self._load_state()
        if not self.queue:
            for url in self.args.start_url:
                normalized = self.normalize_url(url, base_url=None)
                if normalized:
                    self.queue.append(normalized)

        return self._crawl_queue()

    def _crawl_queue(self) -> int:
        while self.queue:
            if self.args.max_pages and self.saved_count >= self.args.max_pages:
                print(f"Reached max pages limit: {self.args.max_pages}")
                break

            url = self.queue.popleft()
            if url in self.visited:
                continue

            try:
                result = self.fetch_page(url)
            except Exception as exc:  # noqa: BLE001
                self.failed[url] = str(exc)
                print(f"[ERROR] {url} -> {exc}", file=sys.stderr)
                self.visited.add(url)
                self._save_state()
                self._sleep()
                continue

            self.visited.add(url)

            if result:
                self._save_page(result)
                self.saved_count += 1
                print(f"[OK] {result.url}")

                for href in result.links:
                    normalized = self.normalize_url(href, base_url=result.url)
                    if not normalized:
                        continue
                    if normalized in self.visited or normalized in self.queue:
                        continue
                    self.queue.append(normalized)
            else:
                self.skip_count += 1
                print(f"[SKIP] {url}")

            self._save_state()
            self._sleep()

        self.build_index_pages()
        self._save_state()
        print(
            "Done. "
            f"saved={self.saved_count} skipped={self.skip_count} "
            f"visited={len(self.visited)} queued={len(self.queue)} failed={len(self.failed)}"
        )
        return 0

    def collect_missing_link_urls(self) -> list[str]:
        html_root = self.output_dir / "html"
        meta_root = self.output_dir / "meta"
        if not html_root.exists() or not meta_root.exists():
            return []

        page_url_map: dict[Path, str] = {}
        for meta_path in meta_root.rglob("*.json"):
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                continue
            page_url = meta.get("url")
            if not page_url:
                continue
            html_rel = meta_path.relative_to(meta_root).with_suffix(".html")
            page_url_map[html_root / html_rel] = page_url

        missing_urls: list[str] = []
        seen: set[str] = set()
        for html_path, page_url in page_url_map.items():
            if not html_path.exists():
                continue
            try:
                html = html_path.read_text(encoding="utf-8")
            except Exception:  # noqa: BLE001
                continue

            extractor = HrefExtractor()
            extractor.feed(html)
            for href in extractor.hrefs:
                remote_url = self.normalize_url(href, base_url=page_url)
                if not remote_url:
                    continue
                local_target = self.output_dir / "html" / self._relative_path_for_url(remote_url).with_suffix(".html")
                if local_target.exists():
                    continue
                if remote_url in seen:
                    continue
                seen.add(remote_url)
                missing_urls.append(remote_url)

        return missing_urls

    def fetch_page(self, url: str) -> PageResult | None:
        response = self.session.get(url, timeout=self.args.timeout)
        response.raise_for_status()

        content_type = response.headers.get("content-type", "")
        if "text/html" not in content_type.lower():
            return None

        html = response.text
        link_extractor = LinkExtractor()
        link_extractor.feed(html)

        text_extractor = TextExtractor()
        text_extractor.feed(html)

        return PageResult(
            url=url,
            title=link_extractor.title,
            links=link_extractor.links,
            text=text_extractor.get_text(),
            status_code=response.status_code,
            content_type=content_type,
            html=html,
        )

    def normalize_url(self, raw_url: str, base_url: str | None) -> str | None:
        if not raw_url:
            return None
        raw_url = raw_url.strip()
        if raw_url.startswith(("#", "javascript:", "mailto:", "tel:")):
            return None

        joined = urljoin(base_url or "", raw_url)
        parsed = urlparse(joined)

        if parsed.scheme not in {"http", "https"}:
            return None
        if parsed.netloc.lower() not in self.allowed_hosts:
            return None
        if self._has_non_html_suffix(parsed.path):
            return None

        cleaned = parsed._replace(fragment="", params="")
        if self.args.drop_query:
            cleaned = cleaned._replace(query="")

        normalized = urlunparse(cleaned)
        if not self._passes_filters(normalized):
            return None
        return normalized

    def _passes_filters(self, url: str) -> bool:
        if self.include_patterns and not any(p.search(url) for p in self.include_patterns):
            return False
        if any(p.search(url) for p in self.exclude_patterns):
            return False
        return True

    def _has_non_html_suffix(self, path: str) -> bool:
        suffix = Path(path.lower()).suffix
        return suffix in NON_HTML_SUFFIXES

    def _save_page(self, result: PageResult) -> None:
        relative = self._relative_path_for_url(result.url)
        html_path = self.output_dir / "html" / relative.with_suffix(".html")
        text_path = self.output_dir / "text" / relative.with_suffix(".txt")
        meta_path = self.output_dir / "meta" / relative.with_suffix(".json")

        html_path.parent.mkdir(parents=True, exist_ok=True)
        text_path.parent.mkdir(parents=True, exist_ok=True)
        meta_path.parent.mkdir(parents=True, exist_ok=True)

        local_html = self._rewrite_html_for_local(result.url, result.html, html_path)
        html_path.write_text(local_html, encoding="utf-8")
        text_path.write_text(self._build_text_payload(result), encoding="utf-8")
        meta = {
            "url": result.url,
            "title": result.title,
            "status_code": result.status_code,
            "content_type": result.content_type,
            "saved_at": int(time.time()),
            "link_count": len(result.links),
        }
        meta_path.write_text(
            json.dumps(meta, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def rewrite_saved_html(self) -> int:
        count = 0
        for meta_path in (self.output_dir / "meta").rglob("*.json"):
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            page_url = meta.get("url")
            if not page_url:
                continue

            relative = meta_path.relative_to(self.output_dir / "meta").with_suffix(".html")
            html_path = self.output_dir / "html" / relative
            if not html_path.exists():
                continue

            html = html_path.read_text(encoding="utf-8")
            rewritten = self._rewrite_html_for_local(page_url, html, html_path)
            html_path.write_text(rewritten, encoding="utf-8")
            count += 1
        return count

    def build_index_pages(self) -> int:
        meta_root = self.output_dir / "meta"
        if not meta_root.exists():
            return 0

        entries: list[dict[str, str]] = []
        for meta_path in sorted(meta_root.rglob("*.json")):
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                continue
            url = meta.get("url", "")
            title = meta.get("title", "") or url
            if not url:
                continue
            html_rel = meta_path.relative_to(meta_root).with_suffix(".html")
            entries.append(
                {
                    "title": title,
                    "url": url,
                    "group": html_rel.parts[0] if len(html_rel.parts) > 1 else "root",
                    "subgroup": self._classify_entry(title, url, html_rel),
                    "html_rel": html_rel.as_posix(),
                }
            )

        if not entries:
            return 0

        group_map: dict[str, list[dict[str, str]]] = {}
        for entry in entries:
            group_map.setdefault(entry["group"], []).append(entry)

        html_root = self.output_dir / "html"
        generated = 0

        root_index_path = self.output_dir / "index.html"
        root_index_path.write_text(
            self._render_root_index(entries, group_map),
            encoding="utf-8",
        )
        generated += 1

        html_index_path = html_root / "index.html"
        html_index_path.parent.mkdir(parents=True, exist_ok=True)
        html_index_path.write_text(
            self._render_root_index(
                entries,
                group_map,
                base_dir=html_root,
                current_path=html_index_path,
            ),
            encoding="utf-8",
        )
        generated += 1

        for group, group_entries in sorted(group_map.items()):
            group_dir = html_root / group
            group_dir.mkdir(parents=True, exist_ok=True)
            group_index_path = group_dir / "index.html"
            group_index_path.write_text(
                self._render_group_index(
                    group,
                    group_entries,
                    base_dir=html_root,
                    current_path=group_index_path,
                ),
                encoding="utf-8",
            )
            generated += 1

        return generated

    def _build_text_payload(self, result: PageResult) -> str:
        sections = [f"URL: {result.url}"]
        if result.title:
            sections.append(f"Title: {result.title}")
        sections.append("")
        sections.append(result.text)
        return "\n".join(sections).strip() + "\n"

    def _classify_entry(self, title: str, url: str, html_rel: Path) -> str:
        cleaned_title = self._clean_title(title).lower()
        slug = html_rel.stem.lower()
        joined = f"{cleaned_title} {slug} {url.lower()}"

        if "fitten-code" in slug or "ai 编程助手" in cleaned_title or "ai agent" in joined:
            return "AI / 工具"
        if any(keyword in joined for keyword in ("quiz", "测验", "考试", "test")):
            return "测验"
        if any(keyword in joined for keyword in ("example", "examples", "实例", "案例", "demo")):
            return "实例"
        if any(keyword in joined for keyword in ("interview", "面试")):
            return "面试"
        if any(keyword in joined for keyword in ("exercise", "练习", "习题")):
            return "练习"
        if any(keyword in joined for keyword in ("install", "setup", "intro", "tutorial", "环境", "入门", "基础", "概述", "简介", "教程")):
            return "入门"
        if any(
            keyword in joined
            for keyword in (
                "reference",
                "references",
                "ref",
                "tag",
                "tags",
                "attr",
                "attrs",
                "attribute",
                "attributes",
                "api",
                "func-",
                "function",
                "functions",
                "method",
                "methods",
                "property",
                "properties",
                "object",
                "objects",
                "event",
                "events",
                "operator",
                "operators",
                "element",
                "elements",
                "参考",
                "手册",
                "速查",
            )
        ):
            return "参考"
        return "专题"

    def _build_subgroup_map(self, entries: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
        subgroup_map: dict[str, list[dict[str, str]]] = {}
        for entry in entries:
            subgroup_map.setdefault(entry["subgroup"], []).append(entry)
        return subgroup_map

    def _classify_group(self, group: str) -> str:
        category_rules = [
            (
                "前端开发",
                {
                    "html",
                    "css",
                    "css3",
                    "cssref",
                    "js",
                    "jsref",
                    "jquery",
                    "jqueryui",
                    "jquerymobile",
                    "angularjs",
                    "angularjs2",
                    "react",
                    "vue",
                    "vue2",
                    "vue3",
                    "nextjs",
                    "tailwindcss",
                    "bootstrap",
                    "bootstrap4",
                    "bootstrap5",
                    "foundation",
                    "font-awesome",
                    "svg",
                    "chartjs",
                    "echarts",
                    "highcharts",
                    "googleapi",
                    "googleAPI",
                    "html5",
                    "htmldom",
                    "dom",
                    "ajax",
                    "ajx",
                    "json",
                    "web",
                    "browsers",
                    "charsets",
                    "tags",
                },
            ),
            (
                "后端与编程语言",
                {
                    "python",
                    "python3",
                    "java",
                    "php",
                    "ruby",
                    "go",
                    "rust",
                    "c",
                    "cprogramming",
                    "cplusplus",
                    "cpp",
                    "csharp",
                    "scala",
                    "kotlin",
                    "lua",
                    "perl",
                    "r",
                    "typescript",
                    "nodejs",
                    "jsp",
                    "servlet",
                    "asp",
                    "aspnet",
                    "vbscript",
                },
            ),
            (
                "数据与数据库",
                {
                    "sql",
                    "mysql",
                    "postgresql",
                    "mongodb",
                    "redis",
                    "memcached",
                    "Memcached",
                    "sqlite",
                    "pandas",
                    "numpy",
                    "matplotlib",
                    "data-structures",
                    "schema",
                    "ml",
                    "tensorflow",
                    "sklearn",
                    "scipy",
                    "pytorch",
                    "opencv",
                    "nlp",
                    "restfulapi",
                },
            ),
            (
                "AI 与 Agent",
                {
                    "ai-agent",
                    "claude-code",
                    "codex",
                    "opencode",
                    "ollama",
                    "skills",
                    "coder-learn-path",
                    "quality",
                },
            ),
            (
                "工具链与工程",
                {
                    "docker",
                    "linux",
                    "git",
                    "maven",
                    "vscode",
                    "eclipse",
                    "pycharm",
                    "selenium",
                    "playwright",
                    "flutter",
                    "ionic",
                    "ios",
                    "jupyter-notebook",
                    "markdown",
                    "design-pattern",
                    "python-design-pattern",
                    "cmake",
                    "qt",
                    "python-qt",
                    "openclaw",
                    "swagger",
                    "sass",
                    "svn",
                },
            ),
            (
                "网络协议与标准",
                {
                    "xml",
                    "xsl",
                    "xslfo",
                    "xpath",
                    "xquery",
                    "xlink",
                    "w3c",
                    "wsdl",
                    "webservices",
                    "soap",
                    "rss",
                    "np",
                    "tcpip",
                    "http",
                    "regexp",
                    "regex",
                    "rdf",
                    "dtd",
                },
            ),
            (
                "站点与杂项",
                {
                    "aboutus",
                    "archives",
                    "browser-history",
                    "commentslist",
                    "disclaimer",
                    "hosting",
                    "index",
                    "manual",
                    "quiz",
                    "runoob-app",
                    "sitemap",
                    "w3cnote",
                    "chmproblem",
                    "dash",
                    "firebug",
                    "appml",
                },
            ),
        ]
        for category, groups in category_rules:
            if group in groups:
                return category
        return "未分类"

    def _build_category_map(
        self,
        group_map: dict[str, list[dict[str, str]]],
    ) -> dict[str, list[tuple[str, list[dict[str, str]]]]]:
        category_map: dict[str, list[tuple[str, list[dict[str, str]]]]] = {}
        for group, group_entries in group_map.items():
            category = self._classify_group(group)
            category_map.setdefault(category, []).append((group, group_entries))
        return category_map

    def _sorted_subgroups(
        self,
        subgroup_map: dict[str, list[dict[str, str]]],
    ) -> list[tuple[str, list[dict[str, str]]]]:
        order = {
            "入门": 0,
            "参考": 1,
            "实例": 2,
            "练习": 3,
            "测验": 4,
            "面试": 5,
            "AI / 工具": 6,
            "专题": 7,
        }
        return sorted(
            subgroup_map.items(),
            key=lambda item: (order.get(item[0], 99), -len(item[1]), item[0]),
        )

    def _build_search_items(
        self,
        entries: list[dict[str, str]],
        current_path: Path | None,
        base_dir: Path | None = None,
    ) -> list[dict[str, str]]:
        search_items: list[dict[str, str]] = []
        for entry in entries:
            target_path = (base_dir / entry["html_rel"]) if base_dir else Path("html") / entry["html_rel"]
            search_items.append(
                {
                    "title": self._clean_title(entry["title"]),
                    "group": entry["group"],
                    "subgroup": entry["subgroup"],
                    "url": entry["url"],
                    "href": self._link_href(current_path, target_path),
                }
            )
        return search_items

    def _render_search_block(self, title: str, placeholder: str) -> str:
        return (
            '<section class="search-panel">'
            f"<h2>{escape(title)}</h2>"
            "<div class=\"search-controls\">"
            '<label class="search-select-wrap" for="archive-search-group">'
            '<span>分组</span>'
            '<select id="archive-search-group" class="search-select">'
            '<option value="">全部分组</option>'
            "</select>"
            "</label>"
            f'<input id="archive-search-input" class="search-input" type="search" placeholder="{escape(placeholder)}" autocomplete="off">'
            '<button id="archive-search-clear" class="search-clear" type="button">清空</button>'
            "</div>"
            '<p class="search-hint">支持标题、分组、分类、URL 关键词，按 <kbd>/</kbd> 聚焦，按 <kbd>Esc</kbd> 清空，搜索状态会写入地址栏。</p>'
            '<p id="archive-search-status" class="search-status">输入标题、分组、分类或 URL 关键词。</p>'
            '<ol id="archive-search-results" class="search-results" hidden></ol>'
            "</section>"
        )

    def _render_root_index(
        self,
        entries: list[dict[str, str]],
        group_map: dict[str, list[dict[str, str]]],
        base_dir: Path | None = None,
        current_path: Path | None = None,
    ) -> str:
        category_map = self._build_category_map(group_map)
        total = len(entries)
        category_sections = []
        sidebar_items = []

        category_order = [
            "前端开发",
            "后端与编程语言",
            "数据与数据库",
            "AI 与 Agent",
            "工具链与工程",
            "网络协议与标准",
            "站点与杂项",
            "未分类",
        ]
        ordered_categories = sorted(
            category_map.items(),
            key=lambda item: (
                category_order.index(item[0]) if item[0] in category_order else len(category_order),
                -sum(len(group_entries) for _, group_entries in item[1]),
                item[0],
            ),
        )

        for index, (category, grouped_items) in enumerate(ordered_categories):
            group_cards = []
            sorted_groups = sorted(grouped_items, key=lambda item: (-len(item[1]), item[0]))
            total_in_category = sum(len(group_entries) for _, group_entries in sorted_groups)
            category_anchor = f"category-{self._slugify(category)}"
            nested_group_items = []
            for group, group_entries in sorted_groups:
                sample = group_entries[:6]
                subgroup_map = self._build_subgroup_map(group_entries)
                group_href = self._link_href(
                    current_path=current_path,
                    target_path=(base_dir / group / "index.html") if base_dir else Path(f"html/{group}/index.html"),
                )
                nested_group_items.append(
                    f'<li><a href="{escape(group_href)}">{escape(group)}</a> <span>{len(group_entries)} pages</span></li>'
                )
                subgroup_badges = " / ".join(
                    f"{subgroup} {len(items)}"
                    for subgroup, items in self._sorted_subgroups(subgroup_map)[:4]
                )
                previews = "".join(
                    f'<li><a href="{escape(self._link_href(current_path, (base_dir / e["html_rel"]) if base_dir else Path("html") / e["html_rel"]))}">{escape(self._clean_title(e["title"]))}</a></li>'
                    for e in sample
                )
                group_cards.append(
                    (
                        f"<section class=\"group-card\">"
                        f"<h2><a href=\"{escape(group_href)}\">{escape(group)}</a></h2>"
                        f"<p>{len(group_entries)} pages</p>"
                        f"<p>{escape(subgroup_badges)}</p>"
                        f"<ul>{previews}</ul>"
                        f"</section>"
                    )
                )
            category_sections.append(
                f'<section id="{escape(category_anchor)}">'
                f"<h2>{escape(category)}</h2>"
                f"<p>{total_in_category} pages / {len(sorted_groups)} groups</p>"
                f"<div class=\"group-grid\">{''.join(group_cards)}</div>"
                "</section>"
            )
            sidebar_items.append(
                "<li>"
                f"<details{' open' if index == 0 else ''}>"
                f"<summary><a href=\"#{escape(category_anchor)}\">{escape(category)}</a>"
                f" <span>{len(sorted_groups)} groups</span></summary>"
                f"<ul class=\"sidebar-sublist\">{''.join(nested_group_items)}</ul>"
                "</details>"
                "</li>"
            )

        search_block = self._render_search_block("全站搜索", "搜索页面标题、分组、分类或原始 URL")
        return self._wrap_index_html(
            title="Runoob Archive",
            subtitle=f"Offline mirror index. Total pages: {total}, groups: {len(group_map)}",
            sidebar=(
                "<nav class=\"sidebar-card\">"
                "<h2>主题导航</h2>"
                f"<ul class=\"sidebar-list\">{''.join(sidebar_items)}</ul>"
                "</nav>"
            ),
            body=search_block + "".join(category_sections),
            search_items=self._build_search_items(entries, current_path, base_dir),
        )

    def _render_group_index(
        self,
        group: str,
        entries: list[dict[str, str]],
        base_dir: Path,
        current_path: Path,
    ) -> str:
        subgroup_map = self._build_subgroup_map(entries)
        nav_items = []
        sections = []
        for subgroup, subgroup_entries in self._sorted_subgroups(subgroup_map):
            anchor = f"subgroup-{self._slugify(subgroup)}"
            nav_items.append(
                f'<li><a href="#{escape(anchor)}">{escape(subgroup)}</a> <span>{len(subgroup_entries)} pages</span></li>'
            )
            items = []
            for entry in sorted(subgroup_entries, key=lambda item: self._clean_title(item["title"]).lower()):
                href = self._link_href(current_path, base_dir / entry["html_rel"])
                items.append(
                    f'<li><a href="{escape(href)}">{escape(self._clean_title(entry["title"]))}</a>'
                    f' <code>{escape(entry["url"])}</code></li>'
                )
            sections.append(
                f'<section id="{escape(anchor)}"><h2>{escape(subgroup)} ({len(subgroup_entries)})</h2>'
                f'<ol class="page-list">{"".join(items)}</ol></section>'
            )

        home_href = self._link_href(current_path, base_dir / "index.html")
        root_href = self._link_href(current_path, self.output_dir / "index.html")
        body = (
            f'<p><a href="{escape(home_href)}">HTML index</a> | '
            f'<a href="{escape(root_href)}">Archive home</a></p>'
            f'{self._render_search_block("组内搜索", "搜索当前分组下的页面标题、分类或 URL")}'
            f'<section><h2>{escape(group)} ({len(entries)})</h2>'
            f'<p>二级分类：{len(subgroup_map)} 个</p>'
            f'<ul class="page-list">{"".join(nav_items)}</ul></section>'
            f'{"".join(sections)}'
        )
        return self._wrap_index_html(
            title=f"{group} index",
            subtitle=f"Offline pages under {group}",
            sidebar=(
                "<nav class=\"sidebar-card\">"
                "<h2>页内导航</h2>"
                "<ul class=\"sidebar-list\">"
                "<li><details open><summary>分类目录</summary>"
                f"<ul class=\"sidebar-sublist\">{''.join(nav_items)}</ul>"
                "</details></li>"
                "</ul>"
                "</nav>"
            ),
            body=body,
            search_items=self._build_search_items(entries, current_path, base_dir),
        )

    def _wrap_index_html(
        self,
        title: str,
        subtitle: str,
        body: str,
        sidebar: str = "",
        search_items: list[dict[str, str]] | None = None,
    ) -> str:
        search_payload = json.dumps(search_items or [], ensure_ascii=False)
        search_script = """
  <script id="archive-search-data" type="application/json">__SEARCH_DATA__</script>
  <script>
    (() => {
      const input = document.getElementById("archive-search-input");
      const results = document.getElementById("archive-search-results");
      const status = document.getElementById("archive-search-status");
      const clearButton = document.getElementById("archive-search-clear");
      const groupSelect = document.getElementById("archive-search-group");
      const dataNode = document.getElementById("archive-search-data");
      if (!input || !results || !status || !clearButton || !groupSelect || !dataNode) {
        return;
      }

      let items = [];
      try {
        items = JSON.parse(dataNode.textContent || "[]");
      } catch (_error) {
        status.textContent = "搜索索引加载失败。";
        return;
      }

      const syncHash = (query, group) => {
        const params = new URLSearchParams();
        if (query) {
          params.set("search", query);
        }
        if (group) {
          params.set("group", group);
        }
        const nextHash = params.toString();
        const target = nextHash ? `#${nextHash}` : window.location.pathname + window.location.search;
        if (nextHash) {
          history.replaceState(null, "", `#${nextHash}`);
          return;
        }
        history.replaceState(null, "", target);
      };

      const parseHashState = () => {
        const raw = window.location.hash.startsWith("#") ? window.location.hash.slice(1) : "";
        const params = new URLSearchParams(raw);
        return {
          query: params.get("search") || "",
          group: params.get("group") || "",
        };
      };

      const populateGroups = () => {
        const groups = [...new Set(items.map((item) => item.group))].sort((left, right) =>
          left.localeCompare(right, "zh-CN")
        );
        for (const group of groups) {
          const option = document.createElement("option");
          option.value = group;
          option.textContent = group;
          groupSelect.append(option);
        }
      };

      const renderResults = (matches, query) => {
        const selectedGroup = groupSelect.value;
        if (!query) {
          results.hidden = true;
          results.innerHTML = "";
          status.textContent = selectedGroup
            ? `当前分组 ${selectedGroup} 下可搜索 ${items.filter((item) => item.group === selectedGroup).length} 个页面。`
            : `可搜索 ${items.length} 个页面。`;
          return;
        }

        if (!matches.length) {
          results.hidden = true;
          results.innerHTML = "";
          status.textContent = selectedGroup
            ? `分组 ${selectedGroup} 下没有匹配“${query}”的结果。`
            : `没有匹配“${query}”的结果。`;
          return;
        }

        results.hidden = false;
        results.innerHTML = matches
          .slice(0, 80)
          .map((item) => (
            `<li><a href="${item.href}">${highlight(item.title, query)}</a><span>${highlight(item.group, query)} / ${highlight(item.subgroup, query)}</span><code>${highlight(item.url, query)}</code></li>`
          ))
          .join("");
        const suffix = matches.length > 80 ? `，显示前 80 条 / 共 ${matches.length} 条` : `，共 ${matches.length} 条`;
        status.textContent = selectedGroup
          ? `在 ${selectedGroup} 中搜索“${query}”${suffix}。`
          : `搜索“${query}”${suffix}。`;
      };

      const escapeHtml = (value) =>
        value
          .replaceAll("&", "&amp;")
          .replaceAll("<", "&lt;")
          .replaceAll(">", "&gt;")
          .replaceAll('"', "&quot;");

      const highlight = (value, query) => {
        if (!query) {
          return escapeHtml(value);
        }
        const source = value.toLowerCase();
        const needle = query.toLowerCase();
        let cursor = 0;
        let html = "";
        while (cursor < value.length) {
          const index = source.indexOf(needle, cursor);
          if (index === -1) {
            html += escapeHtml(value.slice(cursor));
            break;
          }
          html += escapeHtml(value.slice(cursor, index));
          html += `<mark>${escapeHtml(value.slice(index, index + needle.length))}</mark>`;
          cursor = index + needle.length;
        }
        return html;
      };

      const scoreItem = (item, query) => {
        const title = item.title.toLowerCase();
        const group = item.group.toLowerCase();
        const subgroup = item.subgroup.toLowerCase();
        const url = item.url.toLowerCase();
        let score = 0;
        if (title === query) score += 120;
        if (title.startsWith(query)) score += 80;
        if (title.includes(query)) score += 40;
        if (group === query) score += 36;
        if (group.startsWith(query)) score += 24;
        if (group.includes(query)) score += 12;
        if (subgroup === query) score += 18;
        if (subgroup.includes(query)) score += 8;
        if (url.includes(query)) score += 6;
        return score;
      };

      const runSearch = () => {
        const query = input.value.trim().toLowerCase();
        const selectedGroup = groupSelect.value;
        const scopedItems = selectedGroup ? items.filter((item) => item.group === selectedGroup) : items;
        syncHash(input.value.trim(), selectedGroup);
        if (!query) {
          renderResults([], "");
          return;
        }

        const matches = scopedItems
          .filter((item) =>
            [item.title, item.group, item.subgroup, item.url].some((field) => field.toLowerCase().includes(query))
          )
          .sort((left, right) => {
            const scoreDiff = scoreItem(right, query) - scoreItem(left, query);
            if (scoreDiff !== 0) {
              return scoreDiff;
            }
            return left.title.localeCompare(right.title, "zh-CN");
          });
        renderResults(matches, input.value.trim());
      };

      input.addEventListener("input", runSearch);
      groupSelect.addEventListener("change", runSearch);
      clearButton.addEventListener("click", () => {
        input.value = "";
        groupSelect.value = "";
        input.focus();
        syncHash("", "");
        renderResults([], "");
      });
      document.addEventListener("keydown", (event) => {
        if (event.key === "/" && event.target !== input) {
          event.preventDefault();
          input.focus();
          input.select();
          return;
        }
        if (event.key === "Escape" && document.activeElement === input) {
          input.value = "";
          renderResults([], "");
        }
      });
      populateGroups();
      const initialState = parseHashState();
      if (initialState.group && [...groupSelect.options].some((option) => option.value === initialState.group)) {
        groupSelect.value = initialState.group;
      }
      if (initialState.query) {
        input.value = initialState.query;
      }
      window.addEventListener("hashchange", () => {
        const state = parseHashState();
        if (state.group !== groupSelect.value && [...groupSelect.options].some((option) => option.value === state.group)) {
          groupSelect.value = state.group;
        }
        if (state.query !== input.value) {
          input.value = state.query;
        }
        runSearch();
      });
      runSearch();
    })();
  </script>""".replace("__SEARCH_DATA__", search_payload)
        return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f4efe6;
      --panel: #fffaf1;
      --ink: #1f2937;
      --muted: #6b7280;
      --line: #d6c7ae;
      --accent: #9a3412;
      --accent-soft: #f3dfc1;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Noto Serif SC", "Source Han Serif SC", serif;
      background:
        radial-gradient(circle at top left, #fff6dd 0, transparent 28rem),
        linear-gradient(180deg, #f7f1e7 0%, #efe5d6 100%);
      color: var(--ink);
    }}
    main {{
      max-width: 1380px;
      margin: 0 auto;
      padding: 32px 20px 64px;
    }}
    .layout {{
      display: grid;
      grid-template-columns: 280px minmax(0, 1fr);
      gap: 24px;
      align-items: start;
    }}
    aside {{
      position: sticky;
      top: 20px;
    }}
    h1, h2 {{ margin: 0 0 12px; }}
    p {{ color: var(--muted); }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    header {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 24px;
      box-shadow: 0 10px 30px rgba(84, 51, 16, 0.08);
      margin-bottom: 24px;
    }}
    section {{
      background: rgba(255, 250, 241, 0.9);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 20px;
      margin-bottom: 20px;
    }}
    .group-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
    }}
    .search-panel {{
      background: rgba(255, 250, 241, 0.95);
    }}
    .search-controls {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-bottom: 12px;
      align-items: end;
    }}
    .search-select-wrap {{
      display: grid;
      gap: 6px;
      color: var(--muted);
      font-size: 0.95em;
    }}
    .search-select {{
      min-width: 140px;
      padding: 12px 14px;
      border: 1px solid var(--line);
      border-radius: 12px;
      background: #fffdf8;
      color: var(--ink);
      font: inherit;
    }}
    .search-input {{
      flex: 1 1 320px;
      min-width: 0;
      padding: 12px 14px;
      border: 1px solid var(--line);
      border-radius: 12px;
      background: #fffdf8;
      color: var(--ink);
      font: inherit;
    }}
    .search-input:focus {{
      outline: 2px solid rgba(154, 52, 18, 0.18);
      border-color: var(--accent);
    }}
    .search-select:focus {{
      outline: 2px solid rgba(154, 52, 18, 0.18);
      border-color: var(--accent);
    }}
    .search-clear {{
      padding: 12px 16px;
      border: 1px solid var(--line);
      border-radius: 12px;
      background: var(--accent-soft);
      color: var(--accent);
      font: inherit;
      cursor: pointer;
    }}
    .search-status {{
      margin: 0 0 12px;
    }}
    .search-hint {{
      margin: 0 0 10px;
      font-size: 0.95em;
    }}
    .search-results {{
      margin: 0;
      padding-left: 20px;
    }}
    .search-results li {{
      margin: 10px 0;
      line-height: 1.5;
    }}
    .search-results span,
    .search-results code {{
      display: block;
      margin-top: 4px;
    }}
    mark {{
      background: #f8d689;
      color: #7c2d12;
      padding: 0 0.15em;
      border-radius: 0.2em;
    }}
    kbd {{
      display: inline-block;
      min-width: 1.6em;
      padding: 0.1em 0.4em;
      border: 1px solid var(--line);
      border-bottom-width: 2px;
      border-radius: 0.45em;
      background: #fffdf8;
      color: var(--ink);
      font: 0.9em/1.4 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      text-align: center;
    }}
    .group-card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 16px;
    }}
    .sidebar-card {{
      background: rgba(255, 250, 241, 0.96);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 18px;
      box-shadow: 0 10px 30px rgba(84, 51, 16, 0.08);
      max-height: calc(100vh - 40px);
      overflow: auto;
    }}
    .sidebar-list {{
      list-style: none;
      margin: 0;
      padding: 0;
    }}
    .sidebar-sublist {{
      list-style: none;
      margin: 10px 0 0;
      padding: 0 0 0 12px;
      border-left: 1px dashed var(--line);
    }}
    .sidebar-list li {{
      margin: 0 0 10px;
      line-height: 1.5;
      padding-bottom: 10px;
      border-bottom: 1px dashed var(--line);
    }}
    .sidebar-list li:last-child {{
      margin-bottom: 0;
      padding-bottom: 0;
      border-bottom: 0;
    }}
    .sidebar-list span {{
      color: var(--muted);
      font-size: 0.9em;
      margin-left: 8px;
    }}
    .sidebar-list details {{
      display: block;
    }}
    .sidebar-list summary {{
      cursor: pointer;
      font-weight: 600;
      list-style: none;
    }}
    .sidebar-list summary::-webkit-details-marker {{
      display: none;
    }}
    .sidebar-list summary::before {{
      content: "▸";
      display: inline-block;
      margin-right: 8px;
      color: var(--accent);
      transition: transform 0.15s ease;
    }}
    .sidebar-list details[open] > summary::before {{
      transform: rotate(90deg);
    }}
    .sidebar-sublist li {{
      margin: 8px 0 0;
      padding: 0;
      border: 0;
    }}
    .group-card ul, .page-list {{
      margin: 0;
      padding-left: 20px;
    }}
    .group-card li, .page-list li {{
      margin: 6px 0;
      line-height: 1.5;
    }}
    .page-list span {{
      color: var(--muted);
      font-size: 0.9em;
      margin-left: 8px;
    }}
    code {{
      color: var(--muted);
      font-size: 0.85em;
      word-break: break-all;
    }}
    @media (max-width: 960px) {{
      .layout {{
        grid-template-columns: 1fr;
      }}
      aside {{
        position: static;
      }}
      .search-controls {{
        flex-direction: column;
        align-items: stretch;
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
      <div>{body}</div>
    </div>
  </main>
{search_script}
</body>
</html>
"""

    def _clean_title(self, title: str) -> str:
        return re.sub(r"\s+\|\s+菜鸟教程$", "", title).strip()

    def _slugify(self, value: str) -> str:
        parts: list[str] = []
        for char in value.lower():
            if char.isascii() and char.isalnum():
                parts.append(char)
            elif char in {" ", "/", "-", "_"}:
                parts.append("-")
            else:
                parts.append(f"{ord(char):x}")
        slug = re.sub(r"-+", "-", "".join(parts)).strip("-")
        return slug or "group"

    def _link_href(self, current_path: Path | None, target_path: Path) -> str:
        if current_path is None:
            return target_path.as_posix()
        return Path(os.path.relpath(target_path, current_path.parent)).as_posix()

    def _relative_path_for_url(self, url: str) -> Path:
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        if not path:
            path = "index"
        elif path.endswith("/"):
            path = f"{path}index"

        relative = Path(path)
        if not relative.suffix:
            relative = relative / "index"
        return relative

    def _rewrite_html_for_local(self, page_url: str, html: str, html_path: Path) -> str:
        rewriter = LocalLinkRewriter(
            lambda attr, value: self._rewrite_attr_value(attr, value, page_url, html_path)
        )
        rewriter.feed(html)
        return rewriter.get_html()

    def _rewrite_attr_value(
        self,
        attr_name: str,
        raw_value: str,
        page_url: str,
        html_path: Path,
    ) -> str:
        normalized = self.normalize_url(raw_value, base_url=page_url)
        if not normalized:
            return raw_value

        target_path = self.output_dir / "html" / self._relative_path_for_url(normalized).with_suffix(".html")
        relative_path = Path(
            target_path.relative_to(target_path.anchor) if target_path.is_absolute() else target_path
        )
        current_parent = html_path.parent
        local_href = Path(
            current_parent.relative_to(current_parent.anchor) if current_parent.is_absolute() else current_parent
        )
        rel = Path(os.path.relpath(str(relative_path), str(local_href))).as_posix()

        if attr_name == "action" and not rel:
            return "./"
        return rel or "./"

    def _sleep(self) -> None:
        if self.args.delay > 0:
            time.sleep(self.args.delay)

    def _load_state(self) -> None:
        if not self.args.resume or not self.state_file.exists():
            return
        data = json.loads(self.state_file.read_text(encoding="utf-8"))
        self.visited = set(data.get("visited", []))
        self.failed = dict(data.get("failed", {}))
        self.queue = deque(data.get("queue", []))
        self.saved_count = int(data.get("saved_count", 0))
        self.skip_count = int(data.get("skip_count", 0))
        print(
            "Loaded state: "
            f"visited={len(self.visited)} queued={len(self.queue)} failed={len(self.failed)}"
        )

    def _save_state(self) -> None:
        data = {
            "visited": sorted(self.visited),
            "failed": self.failed,
            "queue": list(self.queue),
            "saved_count": self.saved_count,
            "skip_count": self.skip_count,
        }
        self.state_file.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "抓取菜鸟教程页面并保存为 html/text/meta。"
            "默认从站点地图开始，支持断点续跑。"
        )
    )
    parser.add_argument(
        "--start-url",
        action="append",
        default=[DEFAULT_START_URL],
        help="起始页面，可重复传入多个。默认是站点地图。",
    )
    parser.add_argument(
        "--allowed-host",
        action="append",
        default=[DEFAULT_DOMAIN, "runoob.com", "m.runoob.com"],
        help="允许抓取的域名，可重复传入多个。",
    )
    parser.add_argument(
        "--output",
        default="runoob_archive",
        help="输出目录，默认 runoob_archive。",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="每次请求之间的等待秒数，默认 1.0。",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=20.0,
        help="单次请求超时秒数，默认 20。",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=0,
        help="最多抓取多少个页面，0 表示不限。",
    )
    parser.add_argument(
        "--drop-query",
        action="store_true",
        help="抓取时去掉 URL query，减少重复页面。",
    )
    parser.add_argument(
        "--include-regex",
        action="append",
        default=[],
        help="只抓取匹配该正则的 URL，可重复传入。",
    )
    parser.add_argument(
        "--exclude-regex",
        action="append",
        default=[
            r"/try/",
            r"/wp-content/",
            r"/wp-admin/",
            r"/shoppinglist",
            r"/feedback",
            r"/bookmark",
            r"/note/",
            r"/w3cnote/",
        ],
        help="排除匹配该正则的 URL，可重复传入。",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="从 output/state.json 断点续跑。",
    )
    parser.add_argument(
        "--rewrite-only",
        action="store_true",
        help="不联网，直接重写已保存 HTML 中的站内链接为本地相对路径。",
    )
    parser.add_argument(
        "--build-index-only",
        action="store_true",
        help="不联网，基于已保存 meta 生成本地索引页。",
    )
    parser.add_argument(
        "--backfill-missing-only",
        action="store_true",
        help="扫描已保存页面中的本地断链目标，并按缺失 URL 回填抓取。",
    )
    parser.add_argument(
        "--user-agent",
        default=DEFAULT_USER_AGENT,
        help="自定义 User-Agent。",
    )
    return parser.parse_args(list(argv))


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    scraper = RunoobScraper(args)
    return scraper.run()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
