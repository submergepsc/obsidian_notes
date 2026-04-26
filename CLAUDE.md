# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository shape

This is an Obsidian vault, not a conventional application repository. Most tracked files are Markdown knowledge notes plus Obsidian configuration under `.obsidian/`.

Key areas:
- `.obsidian/` — vault configuration, plugin data, workspace state, hotkeys, themes. These files change frequently during normal Obsidian use.
- `templates/` — Templater snippets used by Obsidian. `insert_date.md` inserts frontmatter date; `insert_true_date.md` inserts a raw timestamp string.
- `tools/`, `learning/`, `obsidian使用/`, `25_1/`, `25_2/`, `日记/` — content collections and notes. Treat these primarily as authored documents, not code modules.
- `crawl/` — the main code-bearing area. `crawl/run_noob.py` crawls Runoob Linux docs, converts page content to Markdown, localizes images into `crawl/linux_docs/images/`, and writes an index file.
- `copilot/` — saved Copilot conversations and custom prompt templates.
- `.trash/` — deleted or intermediate vault content; usually noisy and not a good place to make intentional edits unless the user asks.
- `fastoracle_temp` — symlink to an external desktop folder; be careful when editing anything through it.

## Working assumptions

- There is no root `README.md`, `CLAUDE.md`, `.cursorrules`, or `.github/copilot-instructions.md` in this vault.
- There is no unified build/lint/test system at the repository root: no root `package.json`, `pyproject.toml`, or `requirements.txt` were found.
- Git is used as a vault backup mechanism. Obsidian Git is configured to auto-commit with message `vault backup: {{date}}` and auto-pull on boot, so workspace/config files often appear modified.

## Common commands

### Git / repository inspection
```bash
git status --short
git diff -- <path>
git log --oneline -n 10
```

### Obsidian-specific context
There is no CLI build step for the vault itself. Most changes are direct edits to Markdown or Obsidian JSON config.

Templater is configured to use:
- `templates/insert_date.md`
- `templates/insert_true_date.md`

### Python crawler
The only obvious executable project script is `crawl/run_noob.py`.

Run from the repository root:
```bash
python crawl/run_noob.py
```

The script imports these packages:
```bash
pip install requests beautifulsoup4 html2text urllib3
```

Run from inside `crawl/` if you want output paths like `linux_docs/` to stay local to that folder:
```bash
cd crawl && python run_noob.py
```

There is no discovered first-party automated test suite for the crawler or the vault.

## Architecture notes

### Obsidian vault behavior
- This repo is content-first. Most edits should preserve existing wiki-links, relative Markdown links, and user-authored note structure.
- `.obsidian/workspace*.json`, `.obsidian/hotkeys.json`, and plugin `data.json` files are user-stateful and can change independently of intentional feature work. Avoid “cleaning them up” unless the task is explicitly about Obsidian configuration.
- `.stignore` currently ignores only `.git` and `.gitignore`, suggesting the vault may also be synced by another file-sync tool.

### Crawler flow (`crawl/run_noob.py`)
High-level pipeline:
1. Disable proxy env vars and requests proxy inheritance.
2. Build a retrying `requests.Session`.
3. Start from `https://www.runoob.com/linux`.
4. Breadth-first crawl only pages under `www.runoob.com/linux` while excluding static assets.
5. Extract `div.article-intro` from each page.
6. Convert HTML to Markdown with custom normalization for fenced code blocks and inline code.
7. Download referenced images into `images/` beside generated docs and rewrite image links to local paths.
8. Save each page as a sanitized Markdown filename and record outputs in `_crawl_index.txt`.

Important implementation details:
- URL normalization forces canonical HTTPS-style document URLs.
- The crawler assumes Runoob page content lives in `div.article-intro`; if scraping breaks, check site structure first.
- Output paths are relative to the current working directory because `OUTPUT_DIR = "linux_docs"` is a relative path in `__main__`.

## Practical guidance for future edits

- For note reorganization tasks, expect many files to be Markdown-only and linked by Obsidian wiki-links.
- Before changing or deleting files under `.obsidian/`, confirm the task is about vault behavior rather than incidental UI state.
- Before running the crawler, verify the intended working directory so generated files land in the expected place.
- Ignore vendored `.venv` content under coursework folders unless the user explicitly asks to work there; searches can easily get polluted by those files.
