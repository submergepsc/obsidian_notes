---
id: 20260527-handle-tex-obsidian-math
name: handle_tex Obsidian 数学块修复
slug: handle-tex-obsidian-math
cwd: /home/loviya
summary: 新增 `~/.self_def/bin/handle_tex`，用于把 GPT 复制文本里的 TeX 数学块分隔符转换为 Obsidian 兼容格式。
tags:
  - shell
  - text-cleanup
  - obsidian
  - tex
---

# handle_tex Obsidian 数学块修复

## Current Snapshot

- workflow id: 20260527-handle-tex-obsidian-math
- current status: 已完成
- current goal: 在 `~/.self_def/bin` 新增 `handle_tex`，处理 GPT 文本复制到 Obsidian 后出现的 TeX 分隔符兼容问题。
- current blocker: 无
- next step: 无
- tags: shell, text-cleanup, obsidian, tex
- summary: 已新增并补强 `/home/loviya/.self_def/bin/handle_tex`，可处理文件、目录或 stdin，将独立成行的 `[`/`]`、`\[`/`\]`、以及 GPT 复制文本中常见的 `# [`/`## [` 数学块开头转换为 Obsidian 的 `$$`；同时处理 `\(...\)` 行内公式和列表项开头的 `(t)：` / `(\hat{y}_{t+h})：` 变量标签。

## Notes

- 当前 `CODEX_HOME=/home/loviya/.codex-b`，cwd 为 `/home/loviya`。
- 常规 sandbox 命令失败，错误为 bubblewrap 不能 enforce `/home/loviya/.codex-b/memories/.git` 的 read-only path；本轮本机检查和验证使用 escalation 执行。
- `apply_patch` 也受同一 sandbox 初始化错误影响，无法读取 symlink 后的 worklog 文件；本轮改用提升权限的本机写入命令落盘，并记录该偏离。
- 旧 worklog 中有 `/home/loviya/handle_gpt_text.sh` 的历史，但该文件当前不存在；本轮按用户要求创建独立 `~/.self_def/bin/handle_tex`。

## Artifacts

- `/home/loviya/.self_def/bin/handle_tex`
- `/tmp/handle_tex_sample.md`：验证样例输出文件。
- `/tmp/handle_tex_stdin.md`：stdin 模式验证样例。

## Changes

- 新增 Perl 脚本 `handle_tex`，无外部依赖。
- 支持 `handle_tex 文件或文件夹 [...]` 原地处理；目录会递归处理普通文本文件，并跳过含 NUL 的二进制文件。
- 支持 `handle_tex < input.md > output.md` 作为过滤器使用。
- 处理规则：
  - 独立成行的 `[` / `]` 数学块转为 `$$` / `$$`。
  - 独立成行的 `\[` / `\]` 数学块转为 `$$` / `$$`。
  - 单行 `\[ ... \]` 转为多行 `$$ ... $$`。
  - 行内 `\( ... \)` 转为 `$...$`。
  - fenced code block 内内容保持不变。
- 文件写回使用同目录临时文件替换，并保留原权限；脚本权限为 `0755`。

## Verification

- `perl -c /home/loviya/.self_def/bin/handle_tex` 通过。
- `/home/loviya/.self_def/bin/handle_tex --help` 输出中文帮助正常，无 mojibake。
- 用用户给出的 MAE 样例验证：三组独立 `[`/`]` 数学块均转换为 `$$`，行内 `\(y = 100\)` 转为 `$y = 100$`，代码块内 `[`/`]` 保持不变。
- stdin 模式验证：`\[` / `\]` 块输出为 `$$` 块。
- 错误路径验证：不存在的路径返回非零并输出 `错误：不是文件或文件夹`。


## Follow-up: 支持标题前缀数学块

- 用户补充样例：`# [` 开头的 MASE 公式块没有被转换。
- 已扩展 `open_delim()`：当一行只有 Markdown heading prefix 加数学块开头时，例如 `# [`、`## [` 或 `# \[ `，视为数学块开头，并在输出中丢弃多余 heading prefix，生成普通 `$$` 块。
- 保持闭合分隔符规则不变，仍要求独立成行的 `]` 或 `\]`，避免误伤普通标题或链接文本。
- 同步更新 `--help` 文案，说明支持 `# [ ... ]`。
- 验证：
  - `perl -c /home/loviya/.self_def/bin/handle_tex` 通过。
  - 用户 MASE 样例已输出为 `$$ ... $$`。
  - 混合回归样例中普通 `# 普通标题` 保持不变，fenced code block 内 `# [` 保持不变，`## [` 数学块转为 `$$`。


## Follow-up: 支持列表项开头括号公式

- 用户补充样例：`- (t)：当前时间点；`、`- (h)：预测距离；`、`- (\hat{y}_{t+h})：预测值；` 没有被转换。
- 已新增 `convert_list_label_math()`：只处理 Markdown 列表项开头且紧跟冒号的括号标签，例如 `- (t)：`、`- (\hat{y}_{t+h})：`、`1. (MAE):`。
- 加入 `looks_like_math_expr()` 判断，要求括号内像 TeX/变量；中文普通标签如 `- (普通说明)：` 不会转换。
- 规则运行在 fenced code block 外，代码块内列表文本保持不变。
- 验证：
  - `perl -c /home/loviya/.self_def/bin/handle_tex` 通过。
  - 用户三行样例输出为 `- $t$：`、`- $h$：`、`- $\hat{y}_{t+h}$：`。
  - 回归样例确认 `# [` 数学块、`\(y = 100\)` 行内公式和新列表项规则可同时工作。
