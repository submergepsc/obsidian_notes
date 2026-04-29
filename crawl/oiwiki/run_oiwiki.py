import argparse
import json
import re
import time
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse
from xml.etree import ElementTree

import html2text
import requests
from bs4 import BeautifulSoup, NavigableString
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


BASE_URL = "https://oi-wiki.org/"
DEFAULT_OUTPUT_DIR = "docs"
DEFAULT_TIMEOUT = 20
DEFAULT_DELAY = 0.2
DEFAULT_MAX_PAGES = 5000
DEFAULT_SAVE_EVERY = 10
OUTPUT_ENCODING = "utf-8-sig"
ASSET_SUFFIXES = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".webp",
    ".ico",
    ".css",
    ".js",
    ".json",
    ".xml",
    ".pdf",
    ".zip",
    ".rar",
    ".7z",
    ".mp4",
    ".mp3",
)
SKIP_PATH_PREFIXES = (
    "/assets/",
    "/javascripts/",
    "/stylesheets/",
    "/images/",
    "/tags/",
)


def create_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        }
    )
    retry = Retry(
        total=4,
        connect=4,
        read=4,
        backoff_factor=0.8,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET", "HEAD"]),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    scheme = "https"
    netloc = parsed.netloc.lower()
    path = parsed.path or "/"
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/") + "/"
    return f"{scheme}://{netloc}{path}"


def is_content_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.netloc not in {"oi-wiki.org", "www.oi-wiki.org"}:
        return False

    path = (parsed.path or "/").lower()
    if any(path.startswith(prefix) for prefix in SKIP_PATH_PREFIXES):
        return False
    if path.endswith(ASSET_SUFFIXES):
        return False
    return True


def url_to_file_path(url: str, output_dir: Path) -> Path:
    parsed = urlparse(url)
    path = parsed.path.strip("/")

    if not path:
        safe = "index"
    else:
        safe = path.replace("/", "__")

    safe = re.sub(r'[<>:"\\|?*]+', "_", safe)
    return output_dir / f"{safe}.md"


def fetch_text(session: requests.Session, url: str, timeout: int) -> str:
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text


def load_sitemap_urls(session: requests.Session, timeout: int) -> list[str]:
    candidates = [
        urljoin(BASE_URL, "sitemap.xml"),
        urljoin(BASE_URL, "sitemap_index.xml"),
    ]
    found_urls: list[str] = []

    for sitemap_url in candidates:
        try:
            xml_text = fetch_text(session, sitemap_url, timeout)
        except requests.RequestException:
            continue

        try:
            root = ElementTree.fromstring(xml_text)
        except ElementTree.ParseError:
            continue

        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        loc_nodes = root.findall(".//sm:loc", ns)
        if not loc_nodes:
            loc_nodes = root.findall(".//loc")

        for node in loc_nodes:
            if node.text:
                normalized = normalize_url(node.text.strip())
                if is_content_url(normalized):
                    found_urls.append(normalized)

        if found_urls:
            break

    return sorted(set(found_urls))


def extract_links(page_url: str, soup: BeautifulSoup) -> set[str]:
    links: set[str] = set()
    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
            continue
        try:
            full_url = normalize_url(urljoin(page_url, href))
        except ValueError:
            continue
        if is_content_url(full_url):
            links.add(full_url)
    return links


def clean_content_node(content: BeautifulSoup, page_url: str, session: requests.Session, image_dir: Path) -> None:
    for node in content.select(
        ".md-source-file, .md-content__button, .mdx-badge, .admonition-title > .twemoji"
    ):
        node.decompose()

    for anchor in content.select("a.headerlink"):
        anchor.decompose()

    for code_block in content.find_all("pre"):
        code_text = code_block.get_text("\n", strip=False).strip("\n")
        if not code_text.strip():
            continue
        fenced = NavigableString(f"\n```text\n{code_text}\n```\n")
        code_block.replace_with(fenced)

    image_dir.mkdir(parents=True, exist_ok=True)
    for img in content.find_all("img"):
        src = img.get("src")
        if not src:
            continue

        img_url = urljoin(page_url, src)
        parsed = urlparse(img_url)
        filename = Path(parsed.path).name
        if not filename:
            continue

        local_path = image_dir / filename
        if not local_path.exists():
            try:
                response = session.get(img_url, timeout=15)
                response.raise_for_status()
                local_path.write_bytes(response.content)
            except requests.RequestException:
                continue

        img["src"] = f"./images/{filename}"


def html_to_markdown(content: BeautifulSoup) -> str:
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    converter.body_width = 0
    converter.bypass_tables = False
    converter.wrap_links = False
    converter.wrap_list_items = False
    converter.mark_code = False
    converter.wrap_code = False

    markdown = converter.handle(str(content))
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"
    return markdown


def extract_main_content(soup: BeautifulSoup) -> BeautifulSoup | None:
    selectors = [
        "article.md-content__inner.md-typeset",
        "article.md-content__inner",
        "main article",
        "main",
    ]
    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            return node
    return None


def scrape_page(
    session: requests.Session,
    url: str,
    output_dir: Path,
    timeout: int,
) -> tuple[bool, Path | None, set[str]]:
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    response.encoding = "utf-8"
    final_url = normalize_url(response.url)
    soup = BeautifulSoup(response.text, "html.parser")

    content = extract_main_content(soup)
    links = extract_links(final_url, soup)
    if content is None:
        return False, None, links

    title = soup.title.get_text(strip=True) if soup.title else final_url
    image_dir = output_dir / "images"
    clean_content_node(content, final_url, session, image_dir)
    markdown_body = html_to_markdown(content)
    markdown = f"# {title}\n\n- Source: {final_url}\n\n{markdown_body}"

    file_path = url_to_file_path(final_url, output_dir)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(markdown, encoding=OUTPUT_ENCODING)
    return True, file_path, links


def build_state_path(output_dir: Path) -> Path:
    return output_dir / "_crawl_state.json"


def build_index_path(output_dir: Path) -> Path:
    return output_dir / "_crawl_index.json"


def save_progress(
    state_path: Path,
    start_url: str,
    queue: deque[str],
    visited: set[str],
    saved_files: list[dict[str, str]],
    skipped: list[str],
) -> None:
    state = {
        "start_url": start_url,
        "queue": list(queue),
        "visited": sorted(visited),
        "saved_files": saved_files,
        "skipped_urls": skipped,
        "updated_at": int(time.time()),
    }
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding=OUTPUT_ENCODING)


def load_progress(
    state_path: Path,
) -> tuple[str | None, deque[str], set[str], list[dict[str, str]], list[str]]:
    if not state_path.exists():
        return None, deque(), set(), [], []

    data = json.loads(state_path.read_text(encoding="utf-8-sig"))
    return (
        data.get("start_url"),
        deque(data.get("queue", [])),
        set(data.get("visited", [])),
        data.get("saved_files", []),
        data.get("skipped_urls", []),
    )


def write_index(
    index_path: Path,
    start_url: str,
    queue: deque[str],
    visited: set[str],
    saved_files: list[dict[str, str]],
    skipped: list[str],
) -> None:
    index_path.write_text(
        json.dumps(
            {
                "start_url": start_url,
                "visited_count": len(visited),
                "queued_count": len(queue),
                "saved_count": len(saved_files),
                "skipped_count": len(skipped),
                "saved_files": saved_files,
                "skipped_urls": skipped,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding=OUTPUT_ENCODING,
    )


def repair_existing_files(output_dir: Path, timeout: int, delay: float) -> None:
    state_path = build_state_path(output_dir)
    saved_start_url, queue, visited, saved_files, skipped = load_progress(state_path)
    if not saved_files:
        print("没有找到已保存页面，跳过修复。")
        return

    session = create_session()
    repaired = 0
    failed = 0

    for item in saved_files:
        url = item.get("url")
        if not url:
            continue
        print(f"[REPAIR {repaired + failed + 1}/{len(saved_files)}] {url}")
        try:
            success, file_path, _ = scrape_page(session, url, output_dir, timeout)
        except requests.RequestException as exc:
            print(f"   [ERROR] 请求失败: {exc}")
            failed += 1
            continue
        except Exception as exc:
            print(f"   [ERROR] 解析失败: {exc}")
            failed += 1
            continue

        if success and file_path is not None:
            item["file"] = str(file_path)
            repaired += 1
            print(f"   [OK] 已修复 {file_path}")
        else:
            failed += 1
            print("   [SKIP] 未找到正文区域")

        if delay > 0:
            time.sleep(delay)

    save_progress(
        state_path,
        saved_start_url or BASE_URL,
        queue,
        visited,
        saved_files,
        skipped,
    )
    write_index(
        build_index_path(output_dir),
        saved_start_url or BASE_URL,
        queue,
        visited,
        saved_files,
        skipped,
    )
    print(f"修复完成: 成功 {repaired}，失败 {failed}")


def crawl_site(
    start_url: str,
    output_dir: Path,
    timeout: int,
    delay: float,
    max_pages: int,
    save_every: int,
    fresh: bool,
) -> None:
    session = create_session()
    output_dir.mkdir(parents=True, exist_ok=True)
    state_path = build_state_path(output_dir)
    index_path = build_index_path(output_dir)

    if fresh:
        saved_start_url, queue, visited, saved_files, skipped = None, deque(), set(), [], []
    else:
        saved_start_url, queue, visited, saved_files, skipped = load_progress(state_path)

    if queue or visited or saved_files or skipped:
        start_url = saved_start_url or start_url
        print(
            f"检测到断点状态，继续抓取: visited={len(visited)}, "
            f"queued={len(queue)}, saved={len(saved_files)}"
        )
        if not queue:
            sitemap_urls = load_sitemap_urls(session, timeout)
            new_urls = [url for url in sitemap_urls if url not in visited]
            queue.extend(new_urls)
            if new_urls:
                print(f"从 sitemap 发现新页面: {len(new_urls)}")
                save_progress(state_path, start_url, queue, visited, saved_files, skipped)
                write_index(index_path, start_url, queue, visited, saved_files, skipped)
            elif sitemap_urls:
                print("sitemap 中没有发现新页面。")
            else:
                print("未能读取 sitemap，按现有断点继续。")
    else:
        sitemap_urls = load_sitemap_urls(session, timeout)
        queue = deque(sitemap_urls or [normalize_url(start_url)])
        visited = set()
        saved_files = []
        skipped = []
        save_progress(state_path, start_url, queue, visited, saved_files, skipped)

    processed_since_save = 0

    while queue and len(visited) < max_pages:
        current_url = queue.popleft()
        if current_url in visited:
            continue
        visited.add(current_url)

        print(f"[{len(visited)}] 抓取 {current_url}")
        try:
            success, file_path, links = scrape_page(session, current_url, output_dir, timeout)
        except requests.RequestException as exc:
            print(f"   [ERROR] 请求失败: {exc}")
            skipped.append(current_url)
            processed_since_save += 1
            if processed_since_save >= save_every:
                save_progress(state_path, start_url, queue, visited, saved_files, skipped)
                write_index(index_path, start_url, queue, visited, saved_files, skipped)
                processed_since_save = 0
            continue
        except Exception as exc:
            print(f"   [ERROR] 解析失败: {exc}")
            skipped.append(current_url)
            processed_since_save += 1
            if processed_since_save >= save_every:
                save_progress(state_path, start_url, queue, visited, saved_files, skipped)
                write_index(index_path, start_url, queue, visited, saved_files, skipped)
                processed_since_save = 0
            continue

        if success and file_path is not None:
            print(f"   [OK] 保存到 {file_path}")
            saved_files.append({"url": current_url, "file": str(file_path)})
        else:
            print("   [SKIP] 未找到正文区域")
            skipped.append(current_url)

        for link in sorted(links):
            if link not in visited and link not in queue:
                queue.append(link)

        processed_since_save += 1
        if processed_since_save >= save_every:
            save_progress(state_path, start_url, queue, visited, saved_files, skipped)
            write_index(index_path, start_url, queue, visited, saved_files, skipped)
            processed_since_save = 0

        if delay > 0:
            time.sleep(delay)

    save_progress(state_path, start_url, queue, visited, saved_files, skipped)
    write_index(index_path, start_url, queue, visited, saved_files, skipped)

    print("\n===== 抓取完成 =====")
    print(f"访问页面数: {len(visited)}")
    print(f"待抓页面数: {len(queue)}")
    print(f"保存页面数: {len(saved_files)}")
    print(f"跳过页面数: {len(skipped)}")
    print(f"索引文件: {index_path}")
    print(f"断点文件: {state_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="抓取 oi-wiki.org 全站内容到本地 Markdown")
    parser.add_argument("--start-url", default=BASE_URL, help="起始 URL，默认首页")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="输出目录")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="单次请求超时秒数")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY, help="请求之间的间隔秒数")
    parser.add_argument("--max-pages", type=int, default=DEFAULT_MAX_PAGES, help="最多抓取页面数")
    parser.add_argument("--save-every", type=int, default=DEFAULT_SAVE_EVERY, help="每处理多少页保存一次断点")
    parser.add_argument("--fresh", action="store_true", help="忽略已有断点状态，从头开始抓取")
    parser.add_argument("--repair-existing", action="store_true", help="先按已保存页面列表修复本地文件")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.repair_existing:
        repair_existing_files(
            output_dir=Path(args.output_dir),
            timeout=args.timeout,
            delay=args.delay,
        )
        return

    crawl_site(
        start_url=args.start_url,
        output_dir=Path(args.output_dir),
        timeout=args.timeout,
        delay=args.delay,
        max_pages=args.max_pages,
        save_every=max(1, args.save_every),
        fresh=args.fresh,
    )


if __name__ == "__main__":
    main()
