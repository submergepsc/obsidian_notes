---
requested_by_user: true
importance: user-requested
review_priority: high
tags: [user-requested, important, obnotes, git, github, sync]
---

# obnotes push 失败根因

## 结论

`git push` 失败或看起来异常庞大，通常不是最后一个 commit 的改动太大，而是本地相对远端多出的历史对象里已经包含了大文件。

这次 `~/obnotes` 排查里，主要有四个问题叠加：

1. `origin` 一度指错仓库，指到了 `git@github.com:submergepsc/oiwiki_changed_frontend.git`。
2. `main` 一度没有正确 upstream，导致同步目标不明确。
3. 本地历史里包含了超过 GitHub `100MB` 限制的大文件，例如 `Packet_Tracer821_*.{dmg,exe}` 和两份 `小林coding-图解网络` PDF。
4. `25_2/rust/rust-by-practice` 是嵌套 Git 仓库，但主仓库没有对应 `.gitmodules` 映射，会制造坏 gitlink/submodule 状态。

## 可复用判断

- `git status --short --branch` 如果只显示 `## main`，通常说明没有正确 upstream。
- `git rev-list --objects origin/main..main | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)'` 可以直接看待推送范围里的大 blob。
- `git ls-remote origin refs/heads/main` 可以确认远端 `main` 当前实际指向。
- `git submodule status --recursive` 如果报 `no submodule mapping found`，说明有坏 gitlink 或嵌套仓库被误纳入主仓库。

## 安全覆盖远端

1. 先把当前本地分支打一个备份分支。
2. `git reset --mixed origin/main`，把本地提交拆回工作区。
3. 把大文件和嵌套仓库从暂存区排除，必要时补 `.gitignore`。
4. 重新 `git add` 需要同步的内容，确认没有超过 `100MB` 的文件。
5. 正常 `git commit`，再 `git push origin main`。

## 注意

- `.gitignore` 只能阻止未来未跟踪文件被添加，不能自动从历史里删除已经提交过的大对象。
- 如果大文件已经进入提交历史，直接 `force push` 也可能仍然会被 GitHub 拒绝。
- 如果目标只是让远端跟本地一致，优先做一次干净同步提交，而不是硬推原始脏历史。
