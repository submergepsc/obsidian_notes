---
id: 20260517-c7a9-rwa-git-rollback-push
name: RWA Git Rollback Push
slug: rwa-git-rollback-push
cwd: /home/loviya/code/RWAExpResults
summary: 已创建 local Git rollback checkpoints for RWAExpResults and fixed the failed push to origin main by pushing master:main.
tags:
  - RWAExpResults
  - git
  - rollback
  - push
priority: normal
---

# RWA Git 回滚 推送

## 当前快照

- 状态: 已完成
- 目标: 记录the current RWAExpResults Git state for rollback and push it to GitHub main.
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-17 17:16:00 +0800

## 关键结果

- 已创建 empty rollback anchor commit `d16fb74` 带 message `chore: checkpoint current state for rollback`.
- 已创建 change commit `845a8f1` 带 message `chore: record current plot changes for rollback` for `plot_3_throught.py` and two throughput PDFs.
- 已创建 docs commit `3df9370` 带 message `docs: record plot script structure` for `README_plot_all.md`.
- 已修复 the user's failed `git push --force origin main` by pushing the local `master` branch to remote `main` 带 `git push --force origin master:main`.
- Remote `origin/main` now points to `3df9370ef4fad1abecc265408df3808535f90d4f`.

## 命令

- `git commit --allow-empty -m "chore: checkpoint current state for rollback"`
- `git add figures/03_throughput/throughput_stability_pos.pdf figures/03_throughput/throughput_stability_pow.pdf plot_3_throught.py`
- `git commit -m "chore: record current plot changes for rollback"`
- `git add README_plot_all.md`
- `git commit -m "docs: record plot script structure"`
- `git push --force origin master:main`

## 推送 Error Resolution

- 更新时间: 2026-05-17 17:16:00 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `当前 更改记录一下git日志方便回滚`; `git push --force origin main ... 解决一下`
- 问题:
  - Local branch was `master`, so `git push --force origin main` failed 因为 there was no local `main` source ref.
  - `origin/main` existed as a different remote branch at `bd4e289 Initial commit`.
- 改进:
  - Used an explicit source:destination refspec: `master:main`.
  - Forced the remote `main` branch to the current local rollback checkpoint history.
- 结果:
  - GitHub accepted the forced update: `master -> main`.
  - `origin/main` now tracks local commit `3df9370`.
- 下一步:
  - 无 for the push fix. Check `git status` before any later commit 因为 the working tree still shows many tracked modified files after this push.
