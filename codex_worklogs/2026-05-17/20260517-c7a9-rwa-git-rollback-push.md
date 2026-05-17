---
id: 20260517-c7a9-rwa-git-rollback-push
name: RWA Git Rollback Push
slug: rwa-git-rollback-push
cwd: /home/loviya/code/RWAExpResults
summary: Created local Git rollback checkpoints for RWAExpResults and fixed the failed push to origin main by pushing master:main.
tags:
  - RWAExpResults
  - git
  - rollback
  - push
priority: normal
---

# RWA Git Rollback Push

## Current Snapshot

- status: 已完成
- goal: Record the current RWAExpResults Git state for rollback and push it to GitHub main.
- blocker: none
- next: none
- updated: 2026-05-17 17:16:00 +0800

## Key Results

- Created empty rollback anchor commit `d16fb74` with message `chore: checkpoint current state for rollback`.
- Created change commit `845a8f1` with message `chore: record current plot changes for rollback` for `plot_3_throught.py` and two throughput PDFs.
- Created docs commit `3df9370` with message `docs: record plot script structure` for `README_plot_all.md`.
- Fixed the user's failed `git push --force origin main` by pushing the local `master` branch to remote `main` with `git push --force origin master:main`.
- Remote `origin/main` now points to `3df9370ef4fad1abecc265408df3808535f90d4f`.

## Commands

- `git commit --allow-empty -m "chore: checkpoint current state for rollback"`
- `git add figures/03_throughput/throughput_stability_pos.pdf figures/03_throughput/throughput_stability_pow.pdf plot_3_throught.py`
- `git commit -m "chore: record current plot changes for rollback"`
- `git add README_plot_all.md`
- `git commit -m "docs: record plot script structure"`
- `git push --force origin master:main`

## Push Error Resolution

- updated: 2026-05-17 17:16:00 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `当前 更改记录一下git日志方便回滚`; `git push --force origin main ... 解决一下`
- problem:
  - Local branch was `master`, so `git push --force origin main` failed because there was no local `main` source ref.
  - `origin/main` existed as a different remote branch at `bd4e289 Initial commit`.
- improvement:
  - Used an explicit source:destination refspec: `master:main`.
  - Forced the remote `main` branch to the current local rollback checkpoint history.
- result:
  - GitHub accepted the forced update: `master -> main`.
  - `origin/main` now tracks local commit `3df9370`.
- next:
  - None for the push fix. Check `git status` before any later commit because the working tree still shows many tracked modified files after this push.
