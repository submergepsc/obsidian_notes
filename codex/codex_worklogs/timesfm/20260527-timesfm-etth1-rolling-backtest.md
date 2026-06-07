---
id: 20260527-timesfm-etth1-rolling-backtest
name: TimesFM ETTh1 rolling backtest
slug: timesfm-etth1-rolling-backtest
cwd: /home/loviya/code/timesfm
summary: Convert quickrun ETTh1 single-window forecast into a rolling backtest benchmark.
tags:
  - timesfm
  - etth1
  - quickrun
  - backtest
---

# Current Snapshot

- workflow id: 20260527-timesfm-etth1-rolling-backtest
- current status: 已完成
- current goal: 将 quickrun/run_timesfm_etth1.py 从单窗口预测改成多窗口 rolling backtest，并保留汇总指标、逐窗口预测和示例图。
- current blocker: none
- next step: none
- tags: timesfm, etth1, quickrun, backtest
- summary: 读取项目后确认 quickrun 当前只评估最后一个 96h 窗口；本轮将扩展为多窗口回测以提高结果可信度。

# Progress

## 2026-05-27 21:16 +0800

- 用户同意将 quickrun ETTh1 实验推进为 rolling backtest。
- 当前仓库状态: 只有 quickrun/ 未跟踪；本轮开始前未修改源码。
- 计划编辑: quickrun/run_timesfm_etth1.py。

## 2026-05-27 21:21 +0800

- 已将 quickrun/run_timesfm_etth1.py 改为 8 个非重叠窗口的 rolling backtest。
- 新增 SeasonalNaive_168h baseline，保留 SeasonalNaive_24h。
- 输出:
  - quickrun/results/metrics.csv: 汇总指标，3 个模型。
  - quickrun/results/per_window_metrics.csv: 8 个窗口 x 3 个模型。
  - quickrun/results/forecast_values.csv: 8 x 96 = 768 行逐小时预测。
  - quickrun/results/timesfm_forecast.png: 最后一个窗口可视化。
- 验证:
  - python -m py_compile quickrun/run_timesfm_etth1.py 通过。
  - python quickrun/run_timesfm_etth1.py 通过。
- 结果摘要:
  - SeasonalNaive_24h: MAE 1.906902, RMSE 2.492032。
  - SeasonalNaive_168h: MAE 1.852737, RMSE 2.473503。
  - TimesFM_2.5_200M: MAE 1.252056, RMSE 1.757624, P10-P90 coverage 0.805990。
- 过程中修复一个 NumPy 兼容问题: 当前环境没有 np.trapz，因此改为 np.trapezoid 或手写 trapezoid fallback。
- 过程中将 MPLCONFIGDIR 指向 /tmp/timesfm-matplotlib，避免 Matplotlib 尝试写 /home/loviya/.config/matplotlib。
