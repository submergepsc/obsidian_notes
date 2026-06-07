---
id: 20260527-handle-tex-inline-math-cleanup
name: handle_tex 行内数学与 cases 清理
slug: handle-tex-inline-math-cleanup
cwd: /home/loviya
summary: "根据 Obsidian 截图补强 handle_tex：处理普通括号数学、已有 $$ 块内部残留和 cases 间距写法。"
tags: [shell, text-cleanup, obsidian, tex]
---

# handle_tex 行内数学与 cases 清理

## Current Snapshot

- workflow id: 20260527-handle-tex-inline-math-cleanup
- current status: 已完成
- current goal: 修复 `/home/loviya/.self_def/bin/handle_tex`，让截图中的 Quantile Loss 段落和 cases 公式能被更完整转换。
- current blocker: none
- next step: none
- tags: shell, text-cleanup, obsidian, tex
- summary: 发现现有脚本只处理 `\(...\)` 和数学块边界，未处理普通 `(y)`/`(\tau)`、已有 `$$` 块内部残留，以及 `\[6pt]` 这类 cases 行距误写。

## Findings

- 脚本路径：`/home/loviya/.self_def/bin/handle_tex`。
- 截图对应文件：`/home/loviya/notes/obsidian_notes/25_2/AI2/crps和quantile loss.md`。
- 典型残留：段落中的 `(y)`、`(\tau)`、`(\hat{q}_{\tau})` 未转行内数学；`cases` 内部的 `\[6pt]` 应为 `\\[6pt]`。

## Changes

- 修改 `/home/loviya/.self_def/bin/handle_tex`。
- 新增普通段落/表格中的裸括号数学转换，例如 `(y)`、`(\tau)`、`(\hat{q}_{\tau})`、`(2)` 转为 `$...$`。
- 新增已有 `$$` 数学块状态跟踪，块内部不再走普通行内转换，但会清理 GPT 复制残留。
- 新增数学块内部清理：`\[6pt]`、`\[4pt]` 等行距写法转为 `\\[6pt]`、`\\[4pt]`；行尾单反斜杠转为 `\\`。
- 单行 `\[ ... \]` 仍转为多行 `$$ ... $$`，并避免误把公式内部括号再转成 `$...$`。
- 代码 fence 内内容保持不处理。
- 修改前脚本备份：`/tmp/handle_tex.20260527-1600.bak`。

## Verification

- `perl -c /home/loviya/.self_def/bin/handle_tex` 通过。
- `handle_tex --help` 输出包含新规则。
- stdin 回归样例通过：截图中的 `(y)`、`(\tau)`、`(\hat{q}_{\tau})`、表格 `|P10|(\hat{q}_{0.1})|`、`(2)` 均转换为 `$...$`；代码块内不变。
- stdin 回归样例确认 `\[ L_{\tau}(y,\hat{q}_{\tau}) \]` 转为 `$$` 块后，不再误处理公式内部括号。
- 真实文件临时副本 `/tmp/crps-quantile-handle-tex-test.md` 验证通过；未批量修改原始 `obnotes` 笔记。

## Notes

- 本轮仍遇到常规 sandbox/bubblewrap 对 `/home/loviya/.codex-b/memories/.git` 的初始化错误；读写和验证均使用 escalation。
- `apply_patch` 在此环境会被同一 sandbox 问题阻断，本轮使用定点 Python patch 修改脚本。
