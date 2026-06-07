---
id: 20260525-c2e7-plot5-scientific-ticks
name: Plot5 Scientific Ticks
slug: plot5-scientific-ticks
cwd: /home/loviya/code/rwa_plots
summary: 调整 plot_5_scalability.py，让 quantity_vs_time 图的 x/y 轴刻度都使用科学计数法。
tags:
  - rwa_plots
  - plot5
  - scalability
  - ticks
---

# Current Snapshot

- workflow id: 20260525-c2e7-plot5-scientific-ticks
- current status: 已完成
- current goal: 将 `figures/05_scalability/*_quantity_vs_time.pdf` 对应的 x/y 轴刻度改为科学计数法。
- current blocker: 无
- next step: 无
- tags: rwa_plots, plot5, scalability, ticks
- summary: 已将 `plot_5_scalability.py` 的 `k_formatter` 替换为紧凑科学计数法 formatter，并同时应用到 x/y 轴。已重新生成 `figures/05_scalability/pow_quantity_vs_time.pdf` 和 `pos_quantity_vs_time.pdf`。

# Session Notes

- 2026-05-25 13:32:48 +0800: 用户要求“这个字体的x,y轴都改成科学记数法”，截图对应 Plot5 scalability 的 `pow_quantity_vs_time.pdf`。
- 2026-05-25 13:34:55 +0800: 修改 `plot_5_scalability.py`，新增 `scientific_formatter`，输出如 `5e3`, `1e4`, `1.5e4`, `2e4`；`0` 保持为 `0`。x/y 轴均使用该 formatter。

# Verification

- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python -m py_compile plot_5_scalability.py` 通过。
- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python plot_5_scalability.py` 通过，重新生成 PoW 和 PoS Plot5 PDF。
- `pdftotext figures/05_scalability/pow_quantity_vs_time.pdf -` 显示 x/y 刻度均为科学计数法，包含 `5e3`, `1e4`, `1.5e4`, `2e4`, `1.6e4` 等；不再显示 `5k`。
- `pdftotext figures/05_scalability/pos_quantity_vs_time.pdf -` 同样显示科学计数法刻度。
- `pdftoppm -png -singlefile figures/05_scalability/pow_quantity_vs_time.pdf /tmp/plot5_pow_scientific_ticks_check` 渲染预览通过。
