---
id: 20260525-a9c3-plot3-pow-deep-yticks
name: Plot3 POW Deep Y Ticks
slug: plot3-pow-deep-yticks
cwd: /home/loviya/code/rwa_plots
summary: 调整 plot_3_throught.py 的 PoW Deep. 底部分面 y 轴刻度，去掉 0.05 和 0.15。
tags:
  - rwa_plots
  - plot3
  - throughput
  - pow
---

# Current Snapshot

- workflow id: 20260525-a9c3-plot3-pow-deep-yticks
- current status: 已完成
- current goal: 继续修改 `plot_3_throught.py` 的 PoW 部分，让下方 Deep. 面板 y 轴刻度不显示 `0.05` 和 `0.15`。
- current blocker: 无
- next step: 无
- tags: rwa_plots, plot3, throughput, pow
- summary: 已在 PoW 分面绘图循环中为下方 Deep. 面板单独设置 `0.10` 的 y tick 步长；其它 PoW 面板继续使用自动步长。已重新生成 `figures/03_throughput/throughput_stability_pow.pdf`。

# Session Notes

- 2026-05-25 13:25:36 +0800: 用户要求“继续修改plot3的pow部分,下面的deep把y轴的刻度改一下,删掉0.05,0.15”。已确认上一轮 `plot3-pow-deep-split` workflow 为已完成，本轮创建新 workflow。
- 2026-05-25 13:27:22 +0800: 修改 `plot_3_throught.py`，新增 `POW_DEEP_Y_TICK_STEP = 0.10`，并在 PoW 分面循环中仅对 `[POW_DEEP_KEY]` 面板使用该步长。为保持文件一致性，将脚本行尾统一回原有 CRLF。

# Verification

- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python -m py_compile plot_3_throught.py` 通过。
- 只调用 `plot_throughput_stability('pow', target_dir)`，重新生成 `figures/03_throughput/throughput_stability_pow.pdf`。
- `pdftotext figures/03_throughput/throughput_stability_pow.pdf -` 显示 Deep. 面板 y 轴刻度为 `0.00`, `0.10`, `0.20`，未出现 `0.05` 或 `0.15`。
