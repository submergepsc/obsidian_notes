---
id: 20260507-plot3-pow-throughput-timeseries
name: Plot 3 POW Throughput Time Series
slug: plot3-pow-throughput-timeseries
cwd: /home/loviya/code/RWAExpResults
summary: 已诊断 the Plot 3 PoW throughput panel as a boxplot replacement and restored it to a committed-style broken-axis throughput time series.
tags:
  - RWAExpResults
  - plots
  - throughput
priority: normal
---

# Plot 3 POW Throughput Time Series

## 当前快照

- 状态: 已完成
- 目标: 解释并fix the broken-looking PoW throughput panel in Plot 3.
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-07 23:12:22 +0800

## 关键结果

- 已确认 that `plot_3_throught.py` had replaced the PoW throughput stability time-series branch 带 a protocol boxplot.
- The previous intended figure type was a throughput stability plot; committed history used a PoW throughput line plot 带 a vertical broken y-axis.
- Restored `figures/03_throughput/throughput_stability_pow.pdf` to a broken-axis throughput time-series plot 带 `Time (min)` on the x-axis.
- Regenerated both Plot 3 PDFs 带 `python3 plot_3_throught.py` and render-checked the PoW PDF.
- 后续 investigation found no explicit user instruction requesting a boxplot. Git history shows committed versions used PoW throughput line/broken-axis plots, while the boxplot only existed in the uncommitted working tree before the 2026-05-07 14:50 scientific-notation cleanup.
- Per follow-up request, changed the PoW panel back from the temporary log-time single-axis line plot to the committed-style vertical broken-axis throughput line plot.
- Cropped the PoW throughput x-axis to keep only the left-side `0-240 min` range.
- Set the lower broken-axis y range to `0-80 TPS`.

## POW Throughput Panel Was A Boxplot

- 更新时间: 2026-05-07 23:03:33 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `这个plot3的pow的部分的图片怎么回事,之前想要绘制称什么图片来着`
- 问题:
  - The PoW throughput subfigure was showing a nearly empty category-axis plot 因为 the script used a boxplot branch for PoW.
  - 这与论文中按时间跟踪吞吐量的描述冲突。
- 改进:
  - 已修改 the PoW branch back to a throughput stability time series and used a log-scaled time axis to handle the long PoW duration.
- 结果:
  - `throughput_stability_pow.pdf` now shows throughput curves over time rather than a collapsed boxplot.
- 下一步:
  - 无。

## POW Lower Broken-Axis Segment Should Be 0 To 80 TPS

- 更新时间: 2026-05-07 23:12:22 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `高度下一段是0-80`
- 问题:
  - The lower segment of the PoW broken y-axis still used a taller range than needed.
- 改进:
  - 已修改 the lower axis to `ax2.set_ylim(-2, 80)` and ticks to `[0, 20, 40, 60, 80]`.
  - Regenerated and render-checked `figures/03_throughput/throughput_stability_pow.pdf`.
- 结果:
  - The lower throughput segment now focuses on `0-80 TPS`.
- 下一步:
  - 无。

## POW Throughput Should Keep Only 0 To 240 Minutes

- 更新时间: 2026-05-07 23:11:10 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `只保留左侧的240以内的就行`
- 问题:
  - The PoW throughput panel still showed the later right-side range beyond 240 minutes.
- 改进:
  - 已新增 `POW_X_MAX_MINUTES = 240` and used it as the PoW broken-axis x-axis right limit.
  - Regenerated `figures/03_throughput/throughput_stability_pow.pdf` and render-checked that the final x tick is 240.
- 结果:
  - Plot 3 PoW now keeps only the `0-240 min` region.
- 下一步:
  - 无。

## POW Throughput Should Match Committed Broken-Axis Style

- 更新时间: 2026-05-07 23:08:44 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `git log 里的已提交版本：plot_3_throught.py 从 2026-01-15 到 2026-04-12 的提交里，PoW 都是 throughput 折线/断轴图，没有箱线图。改回去`
- 问题:
  - The immediate fix had restored a time-series plot, but used a single log-scaled x-axis rather than the committed vertical broken-axis style.
- 改进:
  - Replaced the PoW single-axis log plot 带 a two-row shared-x broken-axis line plot.
  - 已删除 now-unused log-axis and boxplot-related imports from `plot_3_throught.py`.
  - Regenerated `figures/03_throughput/throughput_stability_pow.pdf` and render-checked it.
- 结果:
  - Plot 3 PoW is now a throughput line plot 带 a vertical broken y-axis, matching the figure type used in committed history.
- 下一步:
  - 无。

## Boxplot Requirement Was Not 已找到

- 更新时间: 2026-05-07 23:05:04 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `这个箱线图的要求什么时候提的`
- 问题:
  - Needed to identify whether the PoW throughput boxplot came from an explicit requirement.
- investigation:
  - Searched worklogs for `箱线图`, `boxplot`, `violin`, `Plot 3`, and throughput references.
  - 已检查 git 历史 for `plot_3_throught.py`; committed versions from 2026-01-15 through 2026-04-12 used PoW throughput line/broken-axis logic, not a boxplot.
  - 已找到 the earliest worklog mention at 2026-05-07 14:50:18 +0800, where an existing `boxplot(labels=...)` call was only updated to `tick_labels` during scientific-notation cleanup.
- 结果:
  - 没有明确的 boxplot requirement was found in the local worklogs or git history.
  - The boxplot appears to have been an uncommitted experimental or accidental replacement rather than a requested figure type.
- 下一步:
  - 无。
