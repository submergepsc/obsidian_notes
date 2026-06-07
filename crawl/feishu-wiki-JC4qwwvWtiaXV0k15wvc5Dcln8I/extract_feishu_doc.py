#!/usr/bin/env python3
"""Extract a public Feishu doc SSR payload into local Markdown."""

from __future__ import annotations

import json
import re
import urllib.request
from http.cookiejar import MozillaCookieJar
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PAGE_HTML = BASE_DIR / "page.html"
COOKIES = BASE_DIR / "cookies.txt"
METADATA_DIR = BASE_DIR / "metadata"
ASSETS_DIR = BASE_DIR / "assets"
WIKI_TOKEN = "JC4qwwvWtiaXV0k15wvc5Dcln8I"
SOURCE_URL = f"https://ycnw11in464y.feishu.cn/wiki/{WIKI_TOKEN}"


def find_balanced_arg(source: str, marker: str) -> str:
    start = source.index(marker) + len(marker)
    depth = 0
    in_string = False
    escaped = False
    for index, char in enumerate(source[start:], start):
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char in "({[":
            depth += 1
        elif char in ")}]":
            if depth == 0:
                return source[start:index]
            depth -= 1
    raise ValueError(f"Could not find balanced argument for {marker!r}")


def extract_text(block_data: dict) -> str:
    text_data = block_data.get("text") or {}
    attributed = text_data.get("initialAttributedTexts") or {}
    text_map = attributed.get("text") or {}
    return "".join(text_map[key] for key in sorted(text_map, key=lambda item: int(item)))


def markdown_escape(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").rstrip()


def image_filename(image: dict, token: str) -> str:
    suffix = {
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/gif": ".gif",
        "image/webp": ".webp",
    }.get(image.get("mimeType"), Path(image.get("name", "")).suffix or ".bin")
    return f"{token}{suffix}"


def render_block(block_id: str, block_map: dict, depth: int = 0) -> list[str]:
    block = block_map.get(block_id)
    if not block:
        return []
    data = block.get("data", {})
    block_type = data.get("type", "")
    text = markdown_escape(extract_text(data))
    lines: list[str] = []

    if block_type == "page":
        pass
    elif block_type == "heading1":
        lines.append(f"# {text}" if text else "#")
    elif block_type == "heading2":
        lines.append(f"## {text}" if text else "##")
    elif block_type == "heading3":
        lines.append(f"### {text}" if text else "###")
    elif block_type == "text":
        if text:
            lines.append(text)
    elif block_type == "code":
        language = (data.get("language") or "").lower()
        lines.append(f"```{language}")
        lines.extend(text.splitlines())
        lines.append("```")
    elif block_type == "ordered":
        prefix = "  " * depth + "1. "
        lines.append(prefix + text)
    elif block_type == "bullet":
        prefix = "  " * depth + "- "
        lines.append(prefix + text)
    elif block_type == "divider":
        lines.append("---")
    elif block_type == "image":
        image = data.get("image") or {}
        token = image.get("token", block_id)
        filename = image_filename(image, token)
        alt = image.get("name") or token
        lines.append(f"![{alt}](assets/{filename})")
    elif block_type == "callout":
        lines.append("> [!note]")
    elif text:
        lines.append(text)
    else:
        lines.append(f"<!-- Unsupported Feishu block type: {block_type} ({block_id}) -->")

    child_depth = depth + 1 if block_type in {"ordered", "bullet"} else depth
    for child_id in data.get("children") or []:
        child_lines = render_block(child_id, block_map, child_depth)
        if child_lines:
            if lines and lines[-1] != "":
                lines.append("")
            lines.extend(child_lines)
    return lines


def download_images(block_map: dict) -> list[dict]:
    ASSETS_DIR.mkdir(exist_ok=True)
    cookie_jar = MozillaCookieJar()
    if COOKIES.exists():
        cookie_jar.load(COOKIES, ignore_discard=True, ignore_expires=True)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    downloaded = []
    for block_id, block in block_map.items():
        data = block.get("data", {})
        if data.get("type") != "image":
            continue
        image = data.get("image") or {}
        token = image.get("token")
        if not token:
            continue
        filename = image_filename(image, token)
        url = (
            "https://ycnw11in464y.feishu.cn/space/api/box/stream/download/all/"
            f"{token}/?mount_node_token={WIKI_TOKEN}&mount_point=wiki"
        )
        output = ASSETS_DIR / filename
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with opener.open(request, timeout=30) as response:
            output.write_bytes(response.read())
        downloaded.append(
            {
                "block_id": block_id,
                "token": token,
                "filename": f"assets/{filename}",
                "bytes": output.stat().st_size,
                "mime_type": image.get("mimeType"),
            }
        )
    return downloaded


def main() -> None:
    html = PAGE_HTML.read_text(encoding="utf-8")
    client_vars = json.loads(find_balanced_arg(html, "clientVars: Object("))
    server_data = json.loads(find_balanced_arg(html, "window.SERVER_DATA = Object("))
    block_map = client_vars["data"]["block_map"]
    root_id = server_data["meta"]["token"]
    title = server_data["meta"]["title"]

    METADATA_DIR.mkdir(exist_ok=True)
    (METADATA_DIR / "client_vars.json").write_text(
        json.dumps(client_vars, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (METADATA_DIR / "server_data.json").write_text(
        json.dumps(server_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    lines = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"source: {SOURCE_URL}",
        f"wiki_token: {WIKI_TOKEN}",
        f"obj_token: {root_id}",
        "---",
        "",
    ]
    root = block_map[root_id]["data"]
    for child_id in root.get("children") or []:
        block_lines = render_block(child_id, block_map)
        if block_lines:
            if lines and lines[-1] != "":
                lines.append("")
            lines.extend(block_lines)
    lines.append("")
    (BASE_DIR / f"{title}.md").write_text("\n".join(lines), encoding="utf-8")

    images = download_images(block_map)
    (METADATA_DIR / "images.json").write_text(
        json.dumps(images, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"extracted {len(block_map)} blocks, {len(images)} images")


if __name__ == "__main__":
    main()
