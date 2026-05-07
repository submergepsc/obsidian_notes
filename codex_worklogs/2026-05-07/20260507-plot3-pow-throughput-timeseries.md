---
id: 20260507-plot3-pow-throughput-timeseries
name: Plot 3 POW Throughput Time Series
slug: plot3-pow-throughput-timeseries
cwd: /home/loviya/code/RWAExpResults
summary: Diagnosed the Plot 3 PoW throughput panel as a boxplot replacement and restored it to a committed-style broken-axis throughput time series.
tags:
  - RWAExpResults
  - plots
  - throughput
priority: normal
---

# Plot 3 POW Throughput Time Series

## Current Snapshot

- status: 已完成
- goal: Explain and fix the broken-looking PoW throughput panel in Plot 3.
- blocker: 无。
- next: 无。
- updated: 2026-05-07 23:12:22 +0800

## Key Results

- Confirmed that `plot_3_throught.py` had replaced the PoW throughput stability time-series branch with a protocol boxplot.
- The previous intended figure type was a throughput stability plot; committed history used a PoW throughput line plot with a vertical broken y-axis.
- Restored `figures/03_throughput/throughput_stability_pow.pdf` to a broken-axis throughput time-series plot with `Time (min)` on the x-axis.
- Regenerated both Plot 3 PDFs with `python3 plot_3_throught.py` and render-checked the PoW PDF.
- Follow-up investigation found no explicit user instruction requesting a boxplot. Git history shows committed versions used PoW throughput line/broken-axis plots, while the boxplot only existed in the uncommitted working tree before the 2026-05-07 14:50 scientific-notation cleanup.
- Per follow-up request, changed the PoW panel back from the temporary log-time single-axis line plot to the committed-style vertical broken-axis throughput line plot.
- Cropped the PoW throughput x-axis to keep only the left-side `0-240 min` range.
- Set the lower broken-axis y range to `0-80 TPS`.

## POW Throughput Panel Was A Boxplot

- updated: 2026-05-07 23:03:33 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `这个plot3的pow的部分的图片怎么回事,之前想要绘制称什么图片来着`
- problem:
  - The PoW throughput subfigure was showing a nearly empty category-axis plot because the script used a boxplot branch for PoW.
  - This conflicted with the paper text, which describes throughput tracked over time.
- improvement:
  - Changed the PoW branch back to a throughput stability time series and used a log-scaled time axis to handle the long PoW duration.
- result:
  - `throughput_stability_pow.pdf` now shows throughput curves over time rather than a collapsed boxplot.
- next:
  - 无。

## POW Lower Broken-Axis Segment Should Be 0 To 80 TPS

- updated: 2026-05-07 23:12:22 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `高度下一段是0-80`
- problem:
  - The lower segment of the PoW broken y-axis still used a taller range than needed.
- improvement:
  - Changed the lower axis to `ax2.set_ylim(-2, 80)` and ticks to `[0, 20, 40, 60, 80]`.
  - Regenerated and render-checked `figures/03_throughput/throughput_stability_pow.pdf`.
- result:
  - The lower throughput segment now focuses on `0-80 TPS`.
- next:
  - 无。

## POW Throughput Should Keep Only 0 To 240 Minutes

- updated: 2026-05-07 23:11:10 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `只保留左侧的240以内的就行`
- problem:
  - The PoW throughput panel still showed the later right-side range beyond 240 minutes.
- improvement:
  - Added `POW_X_MAX_MINUTES = 240` and used it as the PoW broken-axis x-axis right limit.
  - Regenerated `figures/03_throughput/throughput_stability_pow.pdf` and render-checked that the final x tick is 240.
- result:
  - Plot 3 PoW now keeps only the `0-240 min` region.
- next:
  - 无。

## POW Throughput Should Match Committed Broken-Axis Style

- updated: 2026-05-07 23:08:44 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `git log 里的已提交版本：plot_3_throught.py 从 2026-01-15 到 2026-04-12 的提交里，PoW 都是 throughput 折线/断轴图，没有箱线图。改回去`
- problem:
  - The immediate fix had restored a time-series plot, but used a single log-scaled x-axis rather than the committed vertical broken-axis style.
- improvement:
  - Replaced the PoW single-axis log plot with a two-row shared-x broken-axis line plot.
  - Removed now-unused log-axis and boxplot-related imports from `plot_3_throught.py`.
  - Regenerated `figures/03_throughput/throughput_stability_pow.pdf` and render-checked it.
- result:
  - Plot 3 PoW is now a throughput line plot with a vertical broken y-axis, matching the figure type used in committed history.
- next:
  - 无。

## Boxplot Requirement Was Not Found

- updated: 2026-05-07 23:05:04 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `这个箱线图的要求什么时候提的`
- problem:
  - Needed to identify whether the PoW throughput boxplot came from an explicit requirement.
- investigation:
  - Searched worklogs for `箱线图`, `boxplot`, `violin`, `Plot 3`, and throughput references.
  - Checked git history for `plot_3_throught.py`; committed versions from 2026-01-15 through 2026-04-12 used PoW throughput line/broken-axis logic, not a boxplot.
  - Found the earliest worklog mention at 2026-05-07 14:50:18 +0800, where an existing `boxplot(labels=...)` call was only updated to `tick_labels` during scientific-notation cleanup.
- result:
  - No explicit boxplot requirement was found in the local worklogs or git history.
  - The boxplot appears to have been an uncommitted experimental or accidental replacement rather than a requested figure type.
- next:
  - 无。
