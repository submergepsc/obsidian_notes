---
id: 20260524-a3f2-plot3-pos-throughput-panels
name: Plot3 POS Throughput Panels
slug: plot3-pos-throughput-panels
cwd: /home/loviya/code/rwa_plots
summary: 将 plot_3_throught.py 的 POS 吞吐量图按吞吐量范围分组绘制为 2-3 个子图，类似 POW 的分面效果。
tags:
  - rwa_plots
  - plot3
  - throughput
  - pos
priority: normal
---

# Plot3 POS Throughput Panels

## 当前快照

- 状态: 已完成
- 目标: 修改 `plot_3_throught.py`，把 POS throughput 五条曲线按吞吐量大小范围分组，绘制成 2 或 3 个子图，参考现有 POW 分面风格。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-24 12:17:30 +0800
- CODEX_HOME: 空；本轮仅在 repo 与共享 worklog 记录状态，未使用账户专属运行态。

## 本轮记录

- 来源指令: 用户要求 `plot_3_throught.py` 的 POS 吞吐量图按照吞吐量范围把五个绘图函数分类，绘制类似 POW 部分的多个图，但只要两个或者三个。
- 初步观察:
  - 工作目录是 `/home/loviya/code/rwa_plots`。
  - `plot_3_throught.py` 中 POW 当前为每协议一行的横向 boxplot；POS 当前为单张 throughput time-series。
  - `git status --short` 显示已有用户变更 `README.md`，本轮不触碰。
  - POS 平滑 TPS 大致分层: FastOracle 约 13 TPS，DAON 约 3.3 TPS，Sen. 约 1.4 TPS，DECEN. 约 1.0 TPS，Deep. 约 0.4 TPS。

## 命令

- `git status --short`
- `sed -n '1,260p' plot_3_throught.py`
- `sed -n '261,620p' plot_3_throught.py`
- `python3 - <<'PY' ... total_handled_num_pos.csv TPS range summary ... PY`

## 结果

- 已修改 `plot_3_throught.py` 的 POS 分支：根据每个协议平滑 throughput 的 90 分位值自动分到 `High`、`Mid`、`Low` 三个共享时间轴子图。
- 当前 POS 分组结果：`FastOracle` 在 High，`DAON` 在 Mid，`Deep.` / `Sen.` / `DECEN.` 在 Low。
- 保留完成点竖线、FastOracle 完成圈注和 `All requests have been handled` 注释；y 轴按每组范围自动取整，避免低 TPS 曲线被 FastOracle 压扁。
- 已重新生成 `figures/03_throughput/throughput_stability_pos.pdf`。运行完整脚本时 `throughput_stability_pow.pdf` 也被重写，但 POW 绘图分支未做行为性修改，渲染检查保持原箱线图布局。
- 注意：工作区原本已有用户改动 `README.md`，本轮没有修改该文件。

## 验证

- `.venv/bin/python -m py_compile plot_3_throught.py` 通过。
- `MPLCONFIGDIR=/tmp/matplotlib-cache .venv/bin/python plot_3_throught.py` 成功生成 POS/POW throughput PDF。
- `pdftoppm -png -singlefile figures/03_throughput/throughput_stability_pos.pdf /tmp/plot3_pos_grouped_check2` 渲染检查通过：POS 为三行 High/Mid/Low 分面，图例和注释没有遮住主要曲线。
- `pdftoppm -png -singlefile figures/03_throughput/throughput_stability_pow.pdf /tmp/plot3_pow_check_after_pos_group` 渲染检查通过：POW 仍是五行横向 boxplot。
