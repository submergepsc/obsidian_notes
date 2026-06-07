---
id: 20260517-4f91-rwa-plot-scheme-names
name: RWA Plot Scheme Names
slug: rwa-plot-scheme-names
cwd: /home/loviya/code/RWAExpResults
summary: 已统一 the five scheme display names across the RWAExpResults plotting scripts and regenerated the figure PDFs.
tags:
  - RWAExpResults
  - plotting
  - scheme-names
priority: normal
---

# RWA Plot Scheme Names

## 当前快照

- 状态: 已完成
- 目标: 使用the scheme names from the provided reference figure across the plotting scripts in this session.
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-17 17:38:18 +0800

## 关键结果

- 已统一 scheme labels as:
  - `seenfeed` -> `Sen.[11]`
  - `daon` -> `DAON[12]`
  - `decentruth` -> `DECEN.[13]`
  - `deepthought` -> `Deep.[14]`
  - `committee` -> `FastOracle[15]`
- 已更新 `plot_1_stacked_bars.py`, `plot_2_queue.py`, `plot_3_throught.py`, `plot_4_certifycate.py`, and `plot_5_scalability.py`.
- Rebuilt the figure PDFs under `figures/01_breakdown`, `figures/02_queue`, `figures/03_throughput`, `figures/04_certificate`, and `figures/05_scalability`.
- 已修复 the incomplete `LogLocator(base=10.0, subs=(2.0, 5.` line in `plot_2_queue.py` so the plotting suite can run.
- Later removed citation brackets and numbers from the scheme labels, leaving `Sen.`, `DAON`, `DECEN.`, `Deep.`, and `FastOracle`.

## 命令

- `.venv/bin/python -m py_compile plot_1_stacked_bars.py plot_2_queue.py plot_3_throught.py plot_4_certifycate.py plot_5_scalability.py`
- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python plot_1_stacked_bars.py`
- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python run_all_plots.py`

## 解释Why `pa` Is Unavailable In Current 命令 环境

- 更新时间: 2026-05-17 16:02:59 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `当前环境pa为什么没用`
- 问题:
  - `pa` exists as an alias in `/home/loviya/.bashrc` and `/home/loviya/.zshrc`, but the current Codex command environment is non-interactive and reported `pa not found`.
  - `VIRTUAL_ENV` is empty, and `python` is not on PATH in this environment; the project interpreter is available as `.venv/bin/python`.
- 改进:
  - Verified the alias definitions and the project virtualenv directly.
- 结果:
  - 使用the direct command in non-interactive contexts: `MPLCONFIGDIR=/tmp/matplotlib-cache /home/loviya/code/RWAExpResults/.venv/bin/python /home/loviya/code/RWAExpResults/run_all_plots.py`.
- 下一步:
  - If the user wants `pa` to work everywhere, create a real executable wrapper in `~/.local/bin/pa` 而不是 relying on shell aliases.

## Remove Citation Numbers From Plot Scheme Labels

- 更新时间: 2026-05-17 16:04:42 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `对了之前修改方案名称的时候,吧中括号和里面的数字删掉`
- 问题:
  - The previously standardized labels included citation suffixes such as `[11]` and `[15]`, but the user now wants those removed.
- 改进:
  - 已更新 the same five plotting scripts so labels are `Sen.`, `DAON`, `DECEN.`, `Deep.`, and `FastOracle`.
  - Rebuilt all affected PDFs.
- 结果:
  - `py_compile` passes for the five plotting scripts.
  - Regenerated PDFs were written at 2026-05-17 16:04 +0800.
- 下一步:
  - 无

## Verify Plot 3 Throughput Labels

- 更新时间: 2026-05-17 16:05:35 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `对了plot3还没有修改`
- 问题:
  - User reported plot3 may not have been updated.
- 改进:
  - 已检查 `plot3.py` and `plot_3_throught.py`.
  - Verified generated `figures/03_throughput/throughput_stability_pos.pdf` and `throughput_stability_pow.pdf` 带 `pdftotext`.
- 结果:
  - `plot3.py` is an empty 0-line file.
  - The active throughput script `plot_3_throught.py` and both generated throughput PDFs use `FastOracle`, `Deep.`, `Sen.`, `DECEN.`, and `DAON` 带 no bracketed citation numbers.
- 下一步:
  - If the user means another plot3 artifact, identify the exact file path or preview source.

## Simplify Plot 4 Certificate X-Axis Ticks

- 更新时间: 2026-05-17 16:14:16 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `对于plot4的部分,x轴的指数的stick太乱了`
- 问题:
  - `plot_4_certifycate.py` used scientific-format x-axis ticks, producing cluttered labels such as `2.5e3`, `7.5e3`, and `1.2e4`.
- 改进:
  - 已新增 a `format_seconds_k` formatter.
  - Set the x-axis major locator to `MultipleLocator(5000)` so plot4 uses clean ticks such as `0`, `5k`, `10k`, and `15k`.
- 结果:
  - `plot_4_certifycate.py` compiles.
  - Regenerated `figures/04_certificate/certificate_cdf_pos.pdf` and `certificate_cdf_pow.pdf`.
  - `pdftotext` verification shows the x-axis no longer uses mixed scientific notation.
- 下一步:
  - 无

## 使用Scientific Notation For Plot 4 Ticks

- 更新时间: 2026-05-17 16:15:14 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `不行所有的都是用科学记数法,不需要k`
- 问题:
  - The prior plot4 x-axis cleanup used `k` labels, but the user wants scientific notation.
- 改进:
  - Kept sparse major ticks every 5000 seconds.
  - 已修改 the x-axis formatter back to `format_scientific`, so ticks render as `5e3`, `1e4`, and `1.5e4`.
- 结果:
  - `plot_4_certifycate.py` compiles.
  - Regenerated both plot4 certificate PDFs.
  - `pdftotext` verification shows scientific labels and no `k` suffixes.
- 下一步:
  - 无

## Align Plots 3, 2, And 4 For Three-列 图 布局

- 更新时间: 2026-05-17 16:19:13 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `3,2,4这几张图片是放到一起的,你看能否把这几个图片调整一下`
- 问题:
  - The throughput, queue, and certificate PDFs are used together as three subfigures, but their original page sizes, crop behavior, font sizes, and marker sizes were inconsistent.
- 改进:
  - 已统一 `plot_2_queue.py`, `plot_3_throught.py`, and `plot_4_certifycate.py` to a shared `8x6` / `576 x 432 pt` PDF page size.
  - Reduced plot2's very large font and marker sizes for a three-column layout.
  - 已删除 plot4's tight PDF crop so it keeps the same aspect ratio as plot2 and plot3.
  - Tuned plot3's font sizes, line widths, legend, and annotation sizes to fit better as a subfigure.
- 结果:
  - Regenerated `figures/02_queue`, `figures/03_throughput`, and `figures/04_certificate` pos/pow PDFs.
  - Verified all six PDFs have `Page size: 576 x 432 pts`.
  - 已创建 a temporary POS montage at `/tmp/rwa_pos_324_montage.png` for visual inspection.
- 下一步:
  - 无

## Match Plot 2 And Plot 4 Marker Sizes To Plot 5

- 更新时间: 2026-05-17 16:22:13 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `不行,2,4的标记都不行,标点改成5一样大,然后`
- 问题:
  - Plot2 and plot4 marker sizes were reduced for the three-column layout, but the user wants their markers to match plot5.
  - The instruction ended after `然后`, so only the explicit marker-size change was applied.
- 改进:
  - Set plot2's real and legend marker sizes to `24` for FastOracle and `18` for other schemes.
  - Set plot4's `MARKER_SIZE_OURS = 24` and `MARKER_SIZE_OTHERS = 18`.
- 结果:
  - `plot_2_queue.py` and `plot_4_certifycate.py` compile.
  - Regenerated `figures/02_queue` and `figures/04_certificate` pos/pow PDFs.
  - Verified the regenerated PDFs still use `576 x 432 pts`.
- 下一步:
  - Wait for the user's continuation after `然后` if there is another desired adjustment.

## 修复 Plot 4 Annotation Arrow Start And Text Box Size

- 更新时间: 2026-05-17 16:24:32 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `然后plot4中箭头执行的start部分位置不对,文本框也太小了`
- 问题:
  - Plot4's arrow tail used a hard-coded x offset, so it did not reliably start from the text box.
  - The annotation text box became too small after the three-column layout tuning.
- 改进:
  - Enlarged the annotation text to 18 pt and increased the box padding.
  - 已新增 text-box edge calculation in display coordinates, then converted that edge point back to data coordinates for the arrow tail.
  - Enlarged peak highlight circles so they fit the marker sizes matched to plot5.
- 结果:
  - `plot_4_certifycate.py` compiles.
  - Regenerated `figures/04_certificate/certificate_cdf_pos.pdf` and `certificate_cdf_pow.pdf`.
  - Verified page size remains `576 x 432 pts` and rendered a PNG preview at `/tmp/rwa_plot4_pos_after_arrow.png`.
- 下一步:
  - 无

## Match Plot 3 PoW Throughput Boxplot Axis Style

- 更新时间: 2026-05-17 17:01:47 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `这个还记得之前吞吐量的图吗,把plot3的pow改成pos的样式,根据大小的不同,改成`
- 问题:
  - Plot3 PoW used automatic per-panel x-axis ticks, which produced duplicate/awkward labels such as repeated `15` on the `Sen.` row.
- 改进:
  - 已新增 `POW_AXIS_CONFIG` in `plot_3_throught.py` for fixed per-scheme x-axis ranges and tick labels:
    `FastOracle` 13/33/53/72, `Deep.` 0.01/0.04/0.06/0.09, `Sen.` 13/14/15, `DECEN.` 9.0/9.6/10/11, and `DAON` 0.00/13/25/38.
- 结果:
  - `plot_3_throught.py` compiles.
  - Regenerated `figures/03_throughput/throughput_stability_pos.pdf` and `throughput_stability_pow.pdf`.
  - Verified PoW PDF remains `576 x 432 pts` and rendered a PNG preview at `/tmp/rwa_plot3_pow_fixed.png`.
- 下一步:
  - 无

## Document Plot All File Structure

- 更新时间: 2026-05-17 17:05:50 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `把plot_all的四个文件的所有有关文件的文件结构介绍一下,生成readme文件`
- 问题:
  - The four scripts run by `run_all_plots.py` have related input CSVs, output PDFs, upstream generation scripts, and LaTeX references spread across the project.
- 改进:
  - 已新增 `README_plot_all.md` in the project root.
  - Documented `run_all_plots.py`, `plot_2_queue.py`, `plot_3_throught.py`, `plot_4_certifycate.py`, `plot_5_scalability.py`, their direct inputs, outputs, upstream scripts, and common maintenance points.
- 结果:
  - README was verified 带 targeted `rg` and `sed` reads.
- 下一步:
  - 无

## Rewrite 项目 README For Active Plotting 工作流

- 更新时间: 2026-05-17 17:31:17 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `README.md重新写,需要完整介绍整个文件,(不包括实际上很多没有用到或者之前已经废弃的一些文件,),像csv怎么使用的,怎么被文件之间相互调用的,文件之间生成的内容等,结构等,这个readme不是写光一个run_all_plots.py`
- 问题:
  - The previous README focused too narrowly on `run_all_plots.py` and the four scripts it runs.
  - It did not fully explain the active project structure, plot1, CSV roles, generated PDFs, LaTeX references, and upstream generation scripts.
- 改进:
  - Rewrote `README.md` as a project-level active workflow document.
  - Covered `main.tex`, `figure -> figures`, `plot_1_stacked_bars.py` through `plot_5_scalability.py`, `run_all_plots.py`, root CSV inputs, generated figures, upstream scripts, and files excluded from the main workflow.
- 结果:
  - Verified the new README 带 targeted `rg` and `sed` reads.
- 下一步:
  - 无

## Remove External LaTeX Ownership From README

- 更新时间: 2026-05-17 17:38:18 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `对了再次修改一下readme内容,里面涉及到的latex内容不要说,这个main.tex不是我负责的部分,不要当成我自己的`
- 问题:
  - README described `main.tex`, `figure -> figures`, and LaTeX references, which incorrectly implied ownership of an external document/paper source.
- 改进:
  - 已删除 `main.tex`, `main.pdf`, `figure -> figures`, `figure/...`, and LaTeX reference sections from `README.md`.
  - Rephrased the workflow to stop at generated PDFs under `figures/`.
  - Described external report/paper integration only generically as outside this plotting workflow.
- 结果:
  - Verified 带 `rg` that no `main.tex`, `main.pdf`, `LaTeX`, `figure -> figures`, or `figure/...` references remain in `README.md`.
- 下一步:
  - 无

## Standardize Plot Scheme Names

- 更新时间: 2026-05-17 16:00:52 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `整个会话会涉及到4各绘图函数,,每个基本都是五个方案,这无法方案的命名以这个方案为准`
- 问题:
  - The plotting scripts used inconsistent old labels such as `Seen.`, `Decen.`, `Daon.`, `Deep.`, and `FastOracle`.
- 改进:
  - Replaced those labels 带 the citation-bearing names from the provided figure.
  - Included `plot_1_stacked_bars.py` 因为 the reference image is the latency stacked-bar figure.
- 结果:
  - All targeted scripts compile, and all regenerated PDFs use the new labels.
- 下一步:
  - 无
