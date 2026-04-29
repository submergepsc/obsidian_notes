import os
import re
import requests
from bs4 import BeautifulSoup
import html2text
import urllib3
from urllib.parse import urljoin, urlparse
from collections import deque
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ================= 配置与拦截区 =================
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.environ['http_proxy'] = ''
os.environ['https_proxy'] = ''
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

proxies = {"http": None, "https": None}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# ================= 核心逻辑区 =================
def normalize_url(url):
    parsed = urlparse(url)
    path = parsed.path or '/'
    if path != '/' and path.endswith('/'):
        path = path.rstrip('/')
    return f"https://{parsed.netloc}{path}"


def is_linux_doc_url(url):
    parsed = urlparse(url)
    if parsed.netloc != 'www.runoob.com':
        return False

    path = parsed.path or '/'
    if not path.startswith('/linux'):
        return False

    # 排除资源文件。
    blocked_suffixes = (
        '.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.ico',
        '.css', '.js', '.json', '.xml', '.pdf', '.zip', '.rar'
    )
    lower_path = path.lower()
    return not lower_path.endswith(blocked_suffixes)


def url_to_markdown_filename(url):
    parsed = urlparse(url)
    path = parsed.path.strip('/')

    if not path:
        path = 'index'

    if path.endswith('.html'):
        path = path[:-5]

    safe_name = path.replace('/', '__').replace('\\', '__')
    safe_name = re.sub(r'[<>:"|?*]+', '_', safe_name)
    return f"{safe_name}.md"


def create_http_session():
    session = requests.Session()
    session.trust_env = False
    session.headers.update(headers)

    retry = Retry(
        total=3,
        connect=3,
        read=3,
        backoff_factor=0.6,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET", "HEAD"]),
        raise_on_status=False
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def build_fallback_urls(url):
    parsed = urlparse(url)
    candidates = [url]

    if parsed.scheme == 'https':
        candidates.append(f"http://{parsed.netloc}{parsed.path or '/'}")

    return candidates


def fetch_page(url, session, timeout=15):
    last_error = None
    for candidate in build_fallback_urls(url):
        try:
            response = session.get(candidate, timeout=timeout, verify=False, proxies=proxies)
            response.raise_for_status()
            response.encoding = 'utf-8'
            return response, normalize_url(response.url)
        except requests.exceptions.RequestException as e:
            last_error = e

    raise last_error


def extract_markdown_from_content(soup, content_div, page_url, output_root, session):
    # ================= 🛠️ 格式修复终极手术区 =================

    # 【终极修复 1：代码块】
    # 覆盖常见代码容器：菜鸟教程的 div.example_code/div.hl-main 以及通用 pre。
    code_candidates = content_div.select('div.example_code, div.hl-main, pre')

    for code_node in code_candidates:
        # 跳过嵌套在其他代码容器中的节点，避免重复包裹。
        parent = code_node.parent
        is_nested = False
        while parent and parent != content_div:
            classes = parent.get('class', []) if hasattr(parent, 'get') else []
            if parent.name == 'pre' or 'example_code' in classes or 'hl-main' in classes:
                is_nested = True
                break
            parent = parent.parent
        if is_nested:
            continue

        # separator='\n' 保留换行；strip=False 保留缩进。
        raw_code = code_node.get_text(separator='\n', strip=False).strip('\n')
        if not raw_code.strip():
            continue

        # 统一输出 Markdown 围栏代码块。
        formatted_code = f"\n```bash\n{raw_code}\n```\n"
        new_node = soup.new_string(formatted_code)
        code_node.replace_with(new_node)

    # 【修复 2: 局部代码 (行内代码)】
    # 找到所有 <span class="marked"> 替换为 <code>
    for marked_span in content_div.find_all('span', class_='marked'):
        code_tag = soup.new_tag('code')
        code_tag.string = marked_span.get_text()
        marked_span.replace_with(code_tag)

    # --- 图片本地化处理引擎 ---
    img_dir = os.path.join(output_root, 'images')
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    for img_tag in content_div.find_all('img'):
        img_src = img_tag.get('src')
        if not img_src:
            continue

        if img_src.startswith('//'):
            img_url = 'https:' + img_src
        else:
            img_url = urljoin(page_url, img_src)

        img_filename = img_url.split('/')[-1].split('?')[0]
        if not img_filename:
            continue

        local_img_path = os.path.join(img_dir, img_filename)

        if not os.path.exists(local_img_path):
            try:
                img_response = session.get(
                    img_url,
                    timeout=10,
                    verify=False,
                    proxies=proxies
                )
                if img_response.status_code == 200:
                    with open(local_img_path, 'wb') as f:
                        f.write(img_response.content)
            except Exception:
                pass

        img_tag['src'] = f"./images/{img_filename}"
    # --------------------------

    # ================= ⚙️ 渲染引擎配置增强 =================
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.bypass_tables = False
    h.body_width = 0  # 禁用自动换行

    # 关闭 [code]...[/code] 标记输出，保留我们手动注入的 ``` 围栏。
    h.wrap_code = False
    h.mark_code = False
    # =======================================================

    markdown_content = h.handle(str(content_div))
    return normalize_inline_fenced_blocks(markdown_content)


def normalize_inline_fenced_blocks(markdown_text):
    # 先把 [code]...[/code] 兜底转换为 bash 围栏代码块。
    markdown_text = re.sub(
        r'\[code\]\s*(.*?)\s*\[/code\]',
        lambda m: f"```bash\n{m.group(1).strip()}\n```",
        markdown_text,
        flags=re.DOTALL
    )

    # 把单行的 ```bash command ``` 规范化为三行围栏代码块。
    pattern = re.compile(r'^\s*```([a-zA-Z0-9_+-]+)\s+(.+?)\s*```\s*$')
    normalized_lines = []

    for line in markdown_text.splitlines():
        match = pattern.match(line)
        if match:
            language = match.group(1)
            code = match.group(2)
            normalized_lines.extend([f"```{language}", code, "```", ""])
        else:
            normalized_lines.append(line)

    return "\n".join(normalized_lines).rstrip() + "\n"


def scrape_single_page(page_url, soup, output_root, session):
    try:
        content_div = soup.find('div', class_='article-intro')

        if content_div:
            if not os.path.exists(output_root):
                os.makedirs(output_root)

            markdown_content = extract_markdown_from_content(soup, content_div, page_url, output_root, session)
            output_path = os.path.join(output_root, url_to_markdown_filename(page_url))

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            return True, output_path
        else:
            return False, None
    except Exception as e:
        print(f"   [Error] 抓取异常: {e}")
        return False, None


def collect_links(page_url, soup):
    links = set()
    for a_tag in soup.find_all('a', href=True):
        href = a_tag.get('href', '').strip()
        if not href:
            continue

        if href.startswith(('#', 'javascript:', 'mailto:', 'tel:')):
            continue

        try:
            full_url = urljoin(page_url, href)
        except ValueError:
            continue

        normalized = normalize_url(full_url)

        if is_linux_doc_url(normalized):
            links.add(normalized)

    return links


def crawl_linux_docs(start_url, output_root, max_pages=500):
    visited = set()
    queue = deque([normalize_url(start_url)])
    success_count = 0
    failed_count = 0
    saved_files = []
    session = create_http_session()

    if not os.path.exists(output_root):
        os.makedirs(output_root)

    while queue and len(visited) < max_pages:
        current_url = queue.popleft()
        if current_url in visited:
            continue

        visited.add(current_url)
        print(f"\n[{len(visited)}] 抓取: {current_url}")

        try:
            response, final_url = fetch_page(current_url, session)
            soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            failed_count += 1
            print(f"   [Error] 页面请求失败: {e}")
            continue

        success, output_path = scrape_single_page(final_url, soup, output_root, session)
        if success and output_path:
            success_count += 1
            saved_files.append(output_path)
            print(f"   [OK] 已保存: {output_path}")
        else:
            failed_count += 1
            print("   [Skip] 未找到 article-intro，已跳过")

        for link in collect_links(final_url, soup):
            if link not in visited:
                queue.append(link)

    index_path = os.path.join(output_root, '_crawl_index.txt')
    with open(index_path, 'w', encoding='utf-8') as f:
        for path in saved_files:
            f.write(path + '\n')

    print("\n===== 抓取完成 =====")
    print(f"成功: {success_count}")
    print(f"失败/跳过: {failed_count}")
    print(f"访问页面数: {len(visited)}")
    print(f"索引文件: {index_path}")


# ================= 批量抓取执行区 =================
if __name__ == "__main__":
    START_URL = "https://www.runoob.com/linux"
    OUTPUT_DIR = "linux_docs"
    MAX_PAGES = 500

    print(f"🚀 开始批量抓取: {START_URL}")
    crawl_linux_docs(START_URL, OUTPUT_DIR, max_pages=MAX_PAGES)