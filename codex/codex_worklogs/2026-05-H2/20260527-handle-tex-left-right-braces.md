---
id: 20260527-handle-tex-left-right-braces
name: handle_tex left right 大括号修复
slug: handle-tex-left-right-braces
cwd: /home/loviya
summary: "补强 handle_tex：将 LaTeX 中错误的 \\left{ / \\right} 自动修正为 \\left\\{ / \\right\\}。"
tags: [shell, text-cleanup, obsidian, tex]
---

# handle_tex left right 大括号修复

## Current Snapshot

- workflow id: 20260527-handle-tex-left-right-braces
- current status: 已完成
- current goal: 根据 Obsidian 渲染失败案例，修改 `/home/loviya/.self_def/bin/handle_tex`，自动修正 `\left{` / `\right}`。
- current blocker: none
- next step: none
- tags: shell, text-cleanup, obsidian, tex
- summary: 已在 `transform_text` 入口将 `\left{`、`\left {` 统一转为 `\left\{`，将 `\right}`、`\right }` 统一转为 `\right\}`；已正确的 `\left\{...\right\}` 不会重复转义。

## Changes

- 修改 `/home/loviya/.self_def/bin/handle_tex`。
- 新增全局预处理：
  - `$text =~ s/\\left[ \t]*\{/\\left\\{/g;`
  - `$text =~ s/\\right[ \t]*\}/\\right\\}/g;`
- 帮助文本新增该规则。

## Verification

- `perl -c /home/loviya/.self_def/bin/handle_tex`：通过。
- stdin 样例验证：多行指示函数中的 `\left{ ... \right}` 输出为 `\left\{ ... \right\}`。
- stdin 样例验证：`\left {z \ge y\right }` 输出为 `\left\{z \ge y\right\}`。
- stdin 样例验证：已有 `\left\{z \ge y\right\}` 保持不变。
