---
id: 20260507-run-all-plots-continue
name: Continue run_all_plots.py Workflow
slug: run-all-plots-continue
cwd: /home/loviya/code/RWAExpResults
summary: Continued the run_all_plots.py line of work, verified the full plotting pipeline in the project venv, and captured the remaining warning cleanup step.
tags:
  - rwa-exp-results
  - plotting
  - run-all-plots
priority: normal
---

# Continue run_all_plots.py Workflow

## Current Snapshot

- status: 已完成
- goal: Keep the full plotting pipeline stable and warning-free through `run_all_plots.py`.
- blocker: 无。
- next: 无；Plot 5 scalability figures now also use a logarithmic x-axis.
- updated: 2026-05-08 00:00:08 +0800

## Key Results

- Verified `source .venv/bin/activate && python3 run_all_plots.py` completes successfully.
- Confirmed all target plot scripts execute in sequence: `plot_2_queue.py`, `plot_3_throught.py`, `plot_4_certifycate.py`, `plot_5_scalability.py`.
- Observed one non-fatal warning from Matplotlib 3.9+ about `boxplot(labels=...)` deprecation in `plot_3_throught.py`.
- Reduced Plot 5 axis label, tick label, and legend font sizes so the embedded figure text is closer to surrounding paper text.
- Increased Plot 5 text slightly from the too-small baseline after reviewing the embedded paper screenshot.
- Regenerated `figures/05_scalability/pos_quantity_vs_time.pdf` and `figures/05_scalability/pow_quantity_vs_time.pdf`.
- Converted large tick labels in all `run_all_plots.py` target scripts from `k`/plain large integers to compact scientific notation.
- Updated Plot 2 POS queue figure to remove the inset and use a logarithmic x-axis.
- Reduced Plot 2 POS log x-axis tick density so labels no longer overlap in the paper-sized PDF.
- Cropped Plot 2 POS log x-axis to start at `0.1` min to reduce left-side whitespace.
- Extended Plot 2 POS right boundary so Deep. is no longer truncated.
- Reworked Plot 2 POW queue figure from a broken-axis layout to the same single log x-axis style as POS.
- Cropped Plot 2 log x-axes to start at `1` min to reduce remaining left-side whitespace.
- Corrected Plot 5 scalability x-axis to use a logarithmic scale as requested.
- Investigated whether Plot 2 PoW had previously been a cumulative-style figure; current `plot_2_queue.py` uses `total_q_len_pow.csv` and draws queue length, while the closest cumulative trace is the disabled `plot_cumulative_workload` function in `plot_full_8_analysis.py`.
- Reduced Plot 5 marker sizes and increased marker density for the POS/POW cumulative latency figures.

## Continue run_all_plots.py Execution

- updated: 2026-05-07 22:03:00 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `继续run_all_plots.py工作`
- problem:
  - Needed to continue the existing plotting workflow and verify current executability end-to-end.
- improvement:
  - Ran the full pipeline inside the project venv with `source .venv/bin/activate && python3 run_all_plots.py`.
  - Checked the current script list in `run_all_plots.py` and runtime output.
- result:
  - Pipeline succeeds with exit code 0 and regenerates plot outputs.
  - One deprecation warning remains and can be cleaned without behavior change.
- next:
  - If requested, patch `plot_3_throught.py` to use `tick_labels` and re-run `run_all_plots.py` for a warning-free baseline.

## Plot 5 Text Should Match Surrounding Paper Text

- updated: 2026-05-07 14:25:02 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `这个图片中的所有文字大小调整成周围的文字一样大`
- problem:
  - In the paper screenshot, Plot 5 axis labels, tick labels, and legend text were visually larger than the surrounding body text.
- improvement:
  - Changed `AXIS_LABEL_SIZE` from 30 to 20, `TICK_LABEL_SIZE` from 26 to 18, and `LEGEND_FONT_SIZE` from 24 to 18 in `plot_5_scalability.py`.
  - Re-ran `python3 plot_5_scalability.py` inside the project virtualenv.
  - Re-ran `python3 run_all_plots.py` inside the project virtualenv to verify the full plotting pipeline still succeeds.
- result:
  - Regenerated both Plot 5 PDFs under `figures/05_scalability/`.
  - Full plot pipeline completed successfully; the existing Matplotlib `labels` deprecation warning in `plot_3_throught.py` remains non-fatal and unrelated to this font-size change.
- next:
  - 无；if the embedded PDF preview still looks off, fine-tune the three Plot 5 font constants again from the new baseline.

## Plot 5 Markers Should Be Smaller And Denser

- updated: 2026-05-08 00:00:08 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `把图标上的点放小一点,密一点`
- problem:
  - Plot 5 line markers were visually too large and too sparse in the embedded paper view.
- improvement:
  - Changed the sampling interval in `plot_5_scalability.py` from `2000` to `500`.
  - Reduced marker sizes from `24/18` to `9/6` for FastOracle/other schemes.
  - Reduced line widths from `7/4` to `4/2.5` to match the smaller markers.
- result:
  - Regenerated `figures/05_scalability/pos_quantity_vs_time.pdf` and `figures/05_scalability/pow_quantity_vs_time.pdf`.
  - Render check showed smaller and denser markers.
- next:
  - 无。

## Plot 5 Text Should Be Slightly Larger

- updated: 2026-05-07 14:36:01 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `当前效果是有点点差 ,字体再调整大一点`
- problem:
  - The previous Plot 5 text baseline (`20/18/18`) looked slightly too small in the paper screenshot.
- improvement:
  - Increased `AXIS_LABEL_SIZE` to 22, `TICK_LABEL_SIZE` to 20, and `LEGEND_FONT_SIZE` to 20 in `plot_5_scalability.py`.
  - Regenerated Plot 5 PDFs and re-ran the full `run_all_plots.py` pipeline in the project virtualenv.
- result:
  - `figures/05_scalability/pos_quantity_vs_time.pdf` and `figures/05_scalability/pow_quantity_vs_time.pdf` were updated at 2026-05-07 14:35 +0800.
  - Full plotting pipeline completed successfully.
- next:
  - 无。

## Plot 5 X Axis Should Also Be Logarithmic

- updated: 2026-05-07 18:09:29 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `对了我让你吧这个换成对数轴,x轴,你怎么没有更换`
- problem:
  - Plot 2 had been changed to a log x-axis, but Plot 5 scalability figures were still using a linear processed-request x-axis.
- improvement:
  - Added `ax.set_xscale("log")` to `plot_5_scalability.py`.
  - Set Plot 5 x-axis ticks to `1`, `10`, `100`, `1e3`, and `1e4`.
  - Changed Plot 5 sampled x-values to start at `1` because log axes cannot display `0`.
- result:
  - Regenerated `figures/05_scalability/pos_quantity_vs_time.pdf` and `figures/05_scalability/pow_quantity_vs_time.pdf`.
  - Verified `source .venv/bin/activate && python3 run_all_plots.py` completes successfully.
- next:
  - 无。

## Plot 2 POW Cumulative Figure Memory Check

- updated: 2026-05-07 23:45:14 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `不行这个我记得plot2的pow图最后绘制的是某种程度的累计的图,你记得吗`
- problem:
  - Needed to determine whether Plot 2 PoW was previously a cumulative-style figure instead of a queue-length figure.
- investigation:
  - Checked `plot_2_queue.py`; it reads `total_q_len_pow.csv` and labels the y-axis `Queue Length`.
  - Checked legacy output names under `figs_pow_*`; queue outputs include `queue_log_dynamics.pdf` and `queue_decay_kde.pdf`, not a cumulative handled-count figure.
  - Found a disabled `plot_cumulative_workload` function in `plot_full_8_analysis.py` that would have used `total_handled_num_pow.csv` to draw `Cumulative Workload Progress` / `Completion Percentage (%)`.
- result:
  - The current formal Plot 2 PoW is queue length dynamics, but the remembered cumulative-style figure likely refers to the disabled cumulative workload/progress plot rather than `plot_2_queue.py`.
- next:
  - Decide whether Plot 2 should be changed to that cumulative workload/progress concept or keep queue length to match the paper caption.

## Plot 2 Log X Axis Should Start At 1

- updated: 2026-05-07 18:05:22 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `感觉还是不够,从1开始吧`
- problem:
  - Starting at `0.1` still left more early-time space than desired.
- improvement:
  - Set the shared queue plot x-axis left limit to `1`.
  - Changed major ticks to `1`, `10`, `100`, `1e3`, and `1e4`.
- result:
  - Regenerated Plot 2 POS and POW PDFs.
  - Verified `source .venv/bin/activate && python3 run_all_plots.py` completes successfully.
- next:
  - 无。

## Plot 2 POW Should Use Log X Axis Without Broken Axis

- updated: 2026-05-07 15:27:50 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `对了  对于pos的部分,取消短轴,和pos一样使用对数轴`
- problem:
  - The POW queue figure still used a broken x-axis layout, while the POS queue figure had already moved to a single logarithmic x-axis.
- improvement:
  - Removed the POW broken-axis subplot construction and break markers from `plot_2_queue.py`.
  - Drew POW on one axis with the same log x-axis formatter and tick family used by POS.
  - Extended POW right boundary to cover the full active queue duration, including Deep.
- result:
  - Regenerated `figures/02_queue/queue_dynamics_pow.pdf`.
  - Verified `source .venv/bin/activate && python3 run_all_plots.py` completes successfully.
- next:
  - 无。

## Plot 2 POS Should Include Full Deep Processing

- updated: 2026-05-07 15:22:58 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `对了对于deep的方案,把整个处理的过程也要绘制出来,当前的图片截断了`
- problem:
  - POS queue figure was still cropped around the faster schemes, so the slower Deep. queue decay was cut off.
- improvement:
  - Changed POS crop calculation to include all protocols' active queue duration instead of excluding `deepthought`.
  - Set the POS right boundary to at least `1200` min so Deep. completion and the `1e3` log tick have visual margin.
- result:
  - Regenerated `figures/02_queue/queue_dynamics_pos.pdf` with the full Deep. processing curve.
  - Verified `source .venv/bin/activate && python3 run_all_plots.py` completes successfully.
- next:
  - 无。

## Plot 2 POS Log Axis Should Start At 0.1

- updated: 2026-05-07 15:17:34 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `我觉得左侧留空太多,可以从0.1开始绘制`
- problem:
  - Starting the POS log x-axis at the earliest positive time left too much empty space on the left side.
- improvement:
  - Set POS x-axis left limit to `0.1`.
  - Changed POS major ticks to `0.1`, `1`, `10`, and `100`.
- result:
  - Regenerated `figures/02_queue/queue_dynamics_pos.pdf`.
  - Verified `source .venv/bin/activate && python3 run_all_plots.py` completes successfully.
- next:
  - 无。

## Plot 2 POS Log Tick Spacing Should Be Readable

- updated: 2026-05-07 15:12:29 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `根据当前的效果调整一下x轴的刻度间距`
- problem:
  - The initial POS log x-axis tick set was too dense and labels overlapped in the PDF preview.
- improvement:
  - Changed POS x-axis major ticks to `0.02`, `0.2`, `2`, `20`, and `200`.
  - Kept minor log grid lines while hiding minor tick labels.
- result:
  - Regenerated `figures/02_queue/queue_dynamics_pos.pdf`.
  - Verified `source .venv/bin/activate && python3 run_all_plots.py` completes successfully.
- next:
  - 无。

## Plot 2 POS Queue Should Use Log X Axis Without Inset

- updated: 2026-05-07 15:07:28 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `先修改一下plot2,并且pos的子窗口不需要了,x轴换成对数轴`
- problem:
  - The POS queue figure still had an inset zoom window, and the linear x-axis compressed early-time behavior.
- improvement:
  - Removed the POS inset window code and its `inset_axes` / `mark_inset` imports from `plot_2_queue.py`.
  - Changed the POS queue x-axis to a true log scale with the left limit set to the smallest positive time value.
  - Replaced dense default log ticks with a fixed readable set: `0.02`, `0.1`, `0.5`, `2`, `10`, `50`, and `200`.
- result:
  - Regenerated `figures/02_queue/queue_dynamics_pos.pdf` and `figures/02_queue/queue_dynamics_pow.pdf`.
  - Verified `source .venv/bin/activate && python3 run_all_plots.py` completes successfully.
- next:
  - 无。

## Plot Tick Labels Should Use Scientific Notation

- updated: 2026-05-07 14:50:18 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `对了,你把所有的以k结尾的单位和所有的大于1000的数字,都使用科学记数法来表示,所有的run_all_plots.py 的文件`
- problem:
  - Several generated figures used `k` suffixes such as `2k`/`20k`, while others could show plain large integers above 1000.
- improvement:
  - Added compact scientific-notation tick formatters to `plot_2_queue.py`, `plot_3_throught.py`, `plot_4_certifycate.py`, and `plot_5_scalability.py`.
  - Replaced Plot 2 queue `k` formatter with `1e3`/`2e4` style output.
  - Replaced Plot 5 scalability `k` formatter and applied the same formatter to both x and y axes.
  - Applied the formatter to Plot 4 certificate x/y axes and Plot 3 throughput y axes.
  - Updated `plot_3_throught.py` boxplot argument from deprecated `labels` to `tick_labels`.
- result:
  - `source .venv/bin/activate && python3 run_all_plots.py` completed successfully.
  - `pdftotext` checks found scientific notation in updated PDFs and no remaining `k` tick labels in the generated outputs.
- next:
  - 无。
