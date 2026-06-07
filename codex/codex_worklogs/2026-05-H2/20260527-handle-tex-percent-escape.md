---
id: 20260527-handle-tex-percent-escape
name: handle_tex percent 全局转义
slug: handle-tex-percent-escape
cwd: /home/loviya
summary: "按用户要求在 handle_tex 中对每个输入文本应用 s/%/\\%/g。"
tags: [shell, text-cleanup, obsidian, tex]
---

# handle_tex percent 全局转义

## Current Snapshot

- workflow id: 20260527-handle-tex-percent-escape
- current status: 已完成
- current goal: 修改 `/home/loviya/.self_def/bin/handle_tex`，对每个处理文本应用 `s/%/\\%/g`。
- current blocker: none
- next step: none
- tags: shell, text-cleanup, obsidian, tex
- summary: 已在 `transform_text` 入口对完整输入执行 `%` 到 `\%` 的全局替换，覆盖文件、目录递归处理和 stdin 过滤器模式。

## Changes

- 修改 `/home/loviya/.self_def/bin/handle_tex`。
- 在 `transform_text` 开头新增 `$text =~ s/%/\\%/g;`。
- 帮助文本新增“将所有文本中的 % 转换为 \%”。
- 该规则先于数学块、行内公式、代码 fence 等其它转换执行，因此 fenced code block 内的 `%` 也会被转义。

## Verification

- `perl -c /home/loviya/.self_def/bin/handle_tex`：通过。
- stdin 样例验证普通文本、`$$` 数学块、fenced code block 内的 `%` 均输出为 `\%`。
- `handle_tex --help`：确认帮助文本包含 percent 转义规则。
