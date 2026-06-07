---
id: 20260524-b7e2-plot3-pow-deep-split
name: Plot3 POW Deep Split
slug: plot3-pow-deep-split
cwd: /home/loviya/code/rwa_plots
summary: 修改 plot_3_throught.py 的 PoW throughput 图为两个折线分面：Deep. 单独显示，FastOracle/Sen./DAON 组合显示，DECEN. 不纳入 PoW 图。
tags:
  - rwa_plots
  - plot3
  - throughput
  - pow
---

# Current Snapshot

- workflow id: 20260524-b7e2-plot3-pow-deep-split
- current status: 已完成
- current goal: 只修改 `plot_3_throught.py` 的 PoW 部分，把 Deep. 单独分出来，其余有效协议组合为吞吐量折线图，并忽略 DECEN.。
- current blocker: 无
- next step: 无
- tags: rwa_plots, plot3, throughput, pow
- summary: PoW 图已从五行 boxplot 改为两个 throughput time-series 分面；上方面板为 FastOracle/Sen./DECEN./DAON，横轴独立收紧到约 240 分钟且 DECEN. 不参与范围计算；下方面板为 Deep.，保留 0-366 分钟视图且不显示面板内标题。

# Session Notes

- 2026-05-24 19:16:59 +0800: 用户要求“只用修改plot3的pow部分，把deep单独分出来做一个部分，剩下的都组合到一起”。初始理解为两个 boxplot 分面。
- 用户随后纠正：PoW 应改成“这样的吞吐量的图”，即 throughput over time 折线图，不是箱线图。
- 首版折线使用逐采样 `diff/dt`，造成 FastOracle 瞬时尖峰把 y 轴拉到 300+，刻度拥挤。
- 迭代后改为按 `minute_bin` 统计每分钟处理量 / 60，沿用原 boxplot 的吞吐量口径，避免瞬时尖峰。
- 用户继续要求“DECEN. 不用考虑，不用共享 x 轴，展开一点上面的”。先误解为去掉 DECEN.，后续用户澄清“DECEN. 加回去，只是不考虑这个方案的范围”。最终 PoW 分支改为 `POW_RANGE_IGNORED_KEYS = {"decentruth"}`，即 DECEN. 仍绘制和出现在图例中，但不参与上方面板 xlim 计算。
- 用户要求删除右上角的 Deep.，已删除下方面板内部右上角 `Deep.` 标题；图例中的 `Deep.` 保留。
- 本轮只保留 `plot_3_throught.py` 与 `figures/03_throughput/throughput_stability_pow.pdf` 修改；意外出现的 POS PDF modified 已还原。

# Verification

- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python -m py_compile plot_3_throught.py` 通过。
- 只调用 `plot_throughput_stability('pow', target_dir)` 重新生成 `figures/03_throughput/throughput_stability_pow.pdf`。
- `pdftoppm -png -singlefile figures/03_throughput/throughput_stability_pow.pdf /tmp/plot3_pow_no_deep_panel_label_check` 渲染检查通过：上方面板含 FastOracle/Sen./DECEN./DAON 且展开到 0-240 min，下方面板单独显示 Deep. 曲线但无面板内 `Deep.` 标题。
