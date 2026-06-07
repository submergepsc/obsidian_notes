---
id: 20260527-plot3-pow-legend-panel
name: Plot3 POW Legend Panel
slug: plot3-pow-legend-panel
cwd: /home/loviya/code/rwa_plots
summary: 调整 plot3 PoW 吞吐量图的上下分面 legend 字号和下方 Deep. 分面高度。
tags:
  - rwa_plots
  - plot3
  - throughput
  - pow
---

## Current Snapshot

- workflow id: 20260527-plot3-pow-legend-panel
- current status: 已完成
- current goal: 将 `plot_3_throught.py` 中 PoW 图上方组合分面和下方 Deep. 分面的 legend 字号统一放大，并适当增大下方 Deep. 分面高度。
- current blocker: 无
- next step: 无
- tags: rwa_plots, plot3, throughput, pow
- summary: 已将 `plot_3_throught.py` 的 PoW 分面 legend 字号改为 `POW_PANEL_LEGEND_FONT_SIZE = 21`，Deep. 下方面板高度比例改为 `POW_DEEP_PANEL_HEIGHT_RATIO = 1.6`，分面间距改为 `0.24`，并只重新生成 `figures/03_throughput/throughput_stability_pow.pdf`。当前 `CODEX_HOME` 为空，按启动规则记录但本任务不依赖账户专属状态。

## Session Log

- 2026-05-27 18:07:53 +0800: 用户要求把 plot3 的 PoW 图 legend 调整到与 PoW 字体一样大小，Deep. 也一样，并把下面的 Deep. 分面稍微调大。
- 已检查当前工作区：`plot_3_throught.py`、plot2/plot3 PDF 等已有未提交改动；本轮只改 plot3 PoW 相关参数并保留既有改动。
- 2026-05-27 18:11:45 +0800: 修改 `plot_3_throught.py`：新增 `POW_PANEL_LEGEND_FONT_SIZE = 21`、`POW_DEEP_PANEL_HEIGHT_RATIO = 1.6`，将 `POW_PANEL_HSPACE` 从 `0.30` 调为 `0.24`，并让 PoW 分面 legend 使用该字号常量。
- 只调用 `plot_throughput_stability('pow', target_dir)`，重新生成 `figures/03_throughput/throughput_stability_pow.pdf`，避免重写 POS 图。

## Verification

- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python -m py_compile plot_3_throught.py` 通过。
- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python -c "... plot_throughput_stability('pow', target_dir)"` 通过，输出 `figures/03_throughput/throughput_stability_pow.pdf`。
- `pdftoppm -png -singlefile figures/03_throughput/throughput_stability_pow.pdf /tmp/plot3_pow_after_legend` 渲染检查通过：上下两个 legend 字号一致变大，Deep. 分面高度更宽裕且未裁切。
- `pdftotext figures/03_throughput/throughput_stability_pow.pdf -` 确认文本仍包含 `FastOracle`, `Sen.`, `DECEN.`, `DAON`, `Deep.`, `Time (min)`。
