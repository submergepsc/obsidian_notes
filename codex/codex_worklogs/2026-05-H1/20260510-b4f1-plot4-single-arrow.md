---
id: 20260510-b4f1-plot4-single-arrow
name: Plot4 Certificate Single Arrow
slug: plot4-single-arrow
cwd: /home/loviya/code/RWAExpResults
summary: 调整 plot4 certificate 峰值标注，使黑色指示线只绘制一次。
tags:
  - RWAExpResults
  - plotting
  - certificate
priority: normal
---

# Plot4 Certificate 单 Arrow

## 当前快照

- 状态: 已完成
- 目标: 让 plot4 的黑色峰值标注指示线只出现一次。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-10 14:58:00 +0800

## 关键结果

- `plot_4_certifycate.py` now keeps all peak circles but draws only one `ConnectionPatch` pointer line.
- The single pointer targets the `committee` / `FastOracle` peak by default, 带 a fallback to the first available peak if that key is absent.
- Regenerated `figures/04_certificate/certificate_cdf_pos.pdf` and `figures/04_certificate/certificate_cdf_pow.pdf`.

## 命令

- `.venv/bin/python plot_4_certifycate.py`
- `.venv/bin/python -m py_compile plot_4_certifycate.py`
- `pdftoppm -png -singlefile -r 120 figures/04_certificate/certificate_cdf_pos.pdf /tmp/certificate_cdf_pos_check`

## 验证

- The plotting script completed successfully for POS and POW.
- `py_compile` passed 使用 the project virtualenv Python.
- The rendered POS check image showed one black annotation pointer line.
