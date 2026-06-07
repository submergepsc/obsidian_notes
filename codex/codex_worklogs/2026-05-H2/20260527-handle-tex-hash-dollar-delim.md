---
id: 20260527-handle-tex-hash-dollar-delim
name: handle_tex hash dollar 分隔符清理
slug: handle-tex-hash-dollar-delim
cwd: /home/loviya
summary: "补强 handle_tex：独立成行的 # $$、## $$、#$$ 等数学块分隔符统一清理为 $$。"
tags: [shell, text-cleanup, obsidian, tex]
---

# handle_tex hash dollar 分隔符清理

## Current Snapshot

- workflow id: 20260527-handle-tex-hash-dollar-delim
- current status: 已完成
- current goal: 修改 `/home/loviya/.self_def/bin/handle_tex`，只要独立 `$$` 分隔符行前面带 `#`，就删除前面的所有 `#`。
- current blocker: none
- next step: none
- tags: shell, text-cleanup, obsidian, tex
- summary: 已让 `# $$`、`## $$`、`#$$`、缩进后的 `### $$` 等行在处理后输出为原缩进加 `$$`；fenced code block 内保持不处理。

## Changes

- 修改 `/home/loviya/.self_def/bin/handle_tex`。
- `is_display_math_delim` 现在识别独立成行的 hash 前缀 `$$` 分隔符。
- 新增 `normalize_display_math_delim`，输出时删除 `$$` 前所有 `#` 和中间空格，只保留原缩进与 `$$`。
- 顺手修复 `normalize_display_math_line` 中一个 Perl 正则字符类转义问题；否则当前脚本会在 `perl -c` 阶段报 `Unmatched [`。
- 帮助文本已补充该规则。

## Verification

- `perl -c /home/loviya/.self_def/bin/handle_tex`：通过。
- stdin 样例验证：`# $$`、`## $$`、`#$$`、缩进后的 `### $$` 均输出为 `$$`，保留原缩进。
- stdin 样例验证：fenced code block 内的 `# $$` 保持原样，代码块外正常清理。
