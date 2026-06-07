---
id: 20260527-obsidian-latex-advanced-note
name: Obsidian LaTeX 进阶笔记重写
slug: obsidian-latex-advanced-note
cwd: /home/loviya/notes/obsidian_notes/25_2/AI2
summary: "将 obsidian使用/数学公式渲染.md 从入门笔记改写为更完整的 Obsidian LaTeX/MathJax 进阶手册。"
tags: [obsidian, latex, mathjax, notes]
---

# Obsidian LaTeX 进阶笔记重写

## Current Snapshot

- workflow id: 20260527-obsidian-latex-advanced-note
- current status: 已完成
- current goal: 重写 `/home/loviya/notes/obsidian_notes/obsidian使用/数学公式渲染.md`，改成完整、全面、进阶的 Obsidian LaTeX 使用手册。
- current blocker: none
- next step: none
- tags: obsidian, latex, mathjax, notes
- summary: 已将原约 866 行基础笔记整体重写为约 2127 行进阶手册，覆盖 Obsidian 数学公式边界、MathJax/TeX 心智模型、常用符号、多行对齐、矩阵、分段函数、概率统计、机器学习/时间序列公式、表格/列表/Callout 用法、AI 输出清理、排错和可复制模板。

## Changes

- 重写 `/home/loviya/notes/obsidian_notes/obsidian使用/数学公式渲染.md`。
- 新增 24 个主章节和目录。
- 增补进阶内容：`\left...\right` 定界符、`aligned`、`cases`、矩阵、数组、公式编号、统计概率、机器学习/时间序列常用公式、Obsidian 表格/列表/Callout 场景、宏与模板、AI 复制清理规则。
- 修正 Markdown 表格中容易破表的竖线示例，使用 `\lvert...\rvert`、`\lVert...\rVert` 等更稳写法。

## Verification

- `wc -l`：目标文件 2127 行。
- `rg` 定点检查：目录、24 个主章节、常见渲染错误、AI 输出清理、参考链接等关键章节存在。
- `rg -c '^```'`：代码 fence 数量为 274，是偶数，未发现明显未闭合代码块。
- 定点检查表格中的绝对值/范数示例，已避免裸 `|` 破坏 Markdown 表格。

## Notes

- 参考官方 Obsidian 帮助页确认 Obsidian 的数学表达式使用 MathJax，核心写法是 `$...$` 与 `$$...$$`。
- 参考 MathJax 官方 supported macros 文档，避免把完整 LaTeX 排版系统能力误写成 Obsidian 一定可用。
