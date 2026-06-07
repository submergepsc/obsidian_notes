---
id: 20260511-b3e7-plot4-red-left-arrow
name: Plot4 Red Left Arrow
slug: plot4-red-left-arrow
cwd: /home/loviya/code/RWAExpResults
summary: 已更新 plot4 certificate annotation arrow to be red, thicker, and start from the left side of the text box.
tags:
  - RWAExpResults
  - plot4
  - figure
priority: normal
---

# Plot4 Red Left Arrow

## 当前快照

- 状态: 已完成
- 目标: 调整 plot4 峰值标注箭头的样式和位置。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-11 19:28:00 +0800

## 关键结果

- 已更新 `plot_4_certifycate.py` so the peak annotation arrow starts near the left side of the text box.
- 已修改 the arrow color to `#d62728`, increased line width to `3.0`, and set `mutation_scale=18`.
- Regenerated `figures/04_certificate/certificate_cdf_pos.pdf` and `figures/04_certificate/certificate_cdf_pow.pdf`.
- Rendered `certificate_cdf_pow.pdf` to `/tmp/certificate_cdf_pow_check.png` for visual verification.

## 命令

- `python3 plot_4_certifycate.py`
- `pdftoppm -png -singlefile figures/04_certificate/certificate_cdf_pow.pdf /tmp/certificate_cdf_pow_check`
