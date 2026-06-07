---
id: 20260607-obnotes-sync-diagnosis
name: obnotes 远程同步问题诊断
slug: obnotes-sync-diagnosis
cwd: /home/loviya/notes/obsidian_notes
summary: 检查 ~/obnotes 与远程仓库同步异常，重点核对 Git remote、branch upstream、本地修改和远端可达性。
tags: [obnotes, obsidian_notes, git, sync, github]
---

# obnotes 远程同步问题诊断

## Current Snapshot

- workflow id: 20260607-obnotes-sync-diagnosis
- current status: 已完成
- current goal: 检测 `/home/loviya/obnotes` 与远程仓库同步出现的问题
- current blocker: 暂无
- next step: 用户确认后可修复 remote/upstream，并单独处理坏掉的 `rust-by-practice` gitlink
- tags: obnotes, obsidian_notes, git, sync, github
- summary: `~/obnotes` 指向 `/home/loviya/notes/obsidian_notes`；同步异常主因是当前 Git remote 被配置为 `git@github.com:submergepsc/oiwiki_changed_frontend.git`，但旧 worklog 记录该 vault 的正确远端曾是 `git@github.com:submergepsc/obsidian_notes.git`。当前 `main` 没有 upstream；另有一个坏掉的 `rust-by-practice` gitlink/submodule 会导致 submodule 检查失败。

## Findings

- `/home/loviya/obnotes` 是符号链接，目标为 `/home/loviya/notes/obsidian_notes`。
- `git status --short --branch` 输出 `## main`，没有显示 `...origin/main`，说明 `main` 没有配置 upstream。
- 当前 `.git/config` 只有：
  - `remote.origin.url git@github.com:submergepsc/oiwiki_changed_frontend.git`
  - `remote.origin.fetch +refs/heads/*:refs/remotes/origin/*`
- 历史 worklog `/home/loviya/.codex/worklogs/2026-04-H2/20260429-obnotes-github-batch-upload.md` 记录当时正确远端为 `git@github.com:submergepsc/obsidian_notes.git`，最终推送到 `origin/main`。
- 当前工作树非干净：
  - modified submodule: `25_2/rust/rust-by-practice`
  - modified worklog files from this diagnosis under `codex/codex_worklogs/`
  - modified file: `ubuntu使用/ubuntu软件使用介绍/ubuntu磁盘管理工具.md`
- `git ls-remote --heads origin` 返回当前错误远端 `oiwiki_changed_frontend.git` 的 `main=f9848bae...`，提交信息是 `oiwiki_init`。
- `git ls-remote --heads git@github.com:submergepsc/obsidian_notes.git` 返回正确候选远端 `main=f4defade...`。
- 本地 `main=b9db8123`，正确候选远端 `f4defade` 是本地 `main` 的祖先；本地比该远端多 7 个提交。
- 当前 `origin/main=f9848bae`，`git rev-list --left-right --count main...origin/main` 为 `37 1`，说明本地 `main` 和错误远端 `origin/main` 不是正常同步关系。
- `.git/config` 修改时间为 `2026-06-04 23:18:50 +0800`；`.zsh_history` 显示 `2026-06-04 23:14-23:20` 附近有多条 `oiwiki_changed_frontend` 的 `git remote add/set-url` 与 `git push --force` 操作，和 remote 被改错的时间一致。
- `25_2/rust/rust-by-practice` 在主仓库索引中是 `160000` gitlink，但根目录没有 `.gitmodules` 对应条目，`git submodule status --recursive` 报 `fatal: no submodule mapping found in .gitmodules for path '25_2/rust/rust-by-practice'`。
- Obsidian Git 配置中 `pullBeforePush=true`、`syncMethod=merge`、`autoPullOnBoot=false`、`updateSubmodules=false`。在 remote 指错和 upstream 缺失的情况下，插件的同步/手动 pull/push 会围绕错误 remote 失败或出现异常提示。

## Conclusion

- 主因：`/home/loviya/notes/obsidian_notes` 的 `origin` 被改成了 `git@github.com:submergepsc/oiwiki_changed_frontend.git`，不是 obnotes/obsidian_notes 的远程仓库。
- 次因：`main` 没有配置 upstream，所以裸 `git push` / 部分插件同步逻辑没有明确追踪目标。
- 额外风险：`25_2/rust/rust-by-practice` 是无 `.gitmodules` 映射的 gitlink，会导致 submodule 命令失败；如果同步插件或脚本检查 submodule，会单独报错。
- 推荐修复方向：先把 `origin` 改回 `git@github.com:submergepsc/obsidian_notes.git`，再为 `main` 设置 upstream；之后再决定 `rust-by-practice` 是补 `.gitmodules`、取消 gitlink 改为普通目录，还是从主仓库移除跟踪。

## Large Content Audit

- 工作区总大小约 `10G`，其中 `.git` 约 `1.5G`。
- `25_1/` 磁盘占用约 `5.9G`，但当前 HEAD 中 `25_1` 已跟踪文件为 `0`，且 `.gitignore` 有 `25_1/`；因此它目前不应被上传，除非以后强制添加。
- 当前 HEAD 已跟踪内容按顶层目录估算：
  - `25_2`: `1305.3M`
  - `crawl`: `519.9M`
  - `tools`: `75.8M`
  - `.obsidian`: `71.6M`
  - `homework`: `28.0M`
- Git 历史中大于 `10MiB` 的 blob 共 `9` 个，总计约 `1150.4MiB`；其中多个超过 GitHub 普通仓库单文件 `100MiB` 限制，推送会失败或不适合直接上传。
- 已跟踪且明显不适合普通 Git 上传的大文件：
  - `25_2/cn/组网实验预备-软件安装与注册/Packet_Tracer821_MacOS.dmg`，约 `257MiB`
  - `25_2/cn/计算机网络：自顶向下方法（原书第8版） (...).pdf`，约 `251MiB`
  - `25_2/cn/组网实验预备-软件安装与注册/Packet_Tracer821_Win_x64.exe`，约 `227MiB`
  - `25_2/cn/课件/小林coding-图解网络/图解网络-小林coding-亮白风格-v4.0.pdf`，约 `156MiB`
  - `25_2/cn/课件/小林coding-图解网络/图解网络-小林coding-暗黑风格-v4.0.pdf`，约 `156MiB`
  - `25_2/cn/组网实验预备-软件安装与注册/SSE208-组网课程软件安装.pptx`，约 `42MiB`
  - `.obsidian/plugins/image-upload-toolkit/main.js`，约 `16MiB`
  - `25_2/cn/课件/实验3-网络编程/SSE208-实验3-实验要求-网络编程.docx`，约 `11MiB`
- 磁盘上还有很多 ignored 大文件和环境目录，当前不会上传：`25_1/` 下若干 `.exe/.msi/.zip/.rar/.dmg/.pkl`，`crawl/oiwiki/.venv/`，`25_1/人工智能与大模型实验/.conda/` 等。
- 可考虑的清理方向：把上述已跟踪大安装包、教材 PDF 和成对重复 PDF 从 Git 历史中剥离或迁移到 Git LFS/外部存储；只在 Git 中保留索引说明或下载来源。

## 2026-06-07 `.gitignore` Update

- 用户要求把不必要上传/大内容写入 `.gitignore`。
- 已修改 `/home/loviya/notes/obsidian_notes/.gitignore`，新增规则：
  - 常见大二进制/安装包：`*.rar`、`*.7z`、`*.iso`、`*.dmg`、`*.exe`、`*.msi`、`*.pkg`、`*.deb`、`*.AppImage`
  - 数据/模型文件：`*.pkl`、`*.onnx`、`*.pt`、`*.pth`、`*.safetensors`
  - 本地环境和构建产物：`.conda/`、`node_modules/`、`dist/`、`build/`、`target/`、对象文件/动态库等
  - 已发现的大型课程资源定点规则：Packet Tracer 安装包、`计算机网络：自顶向下方法*.pdf`、`小林coding-图解网络/*.pdf`
- 验证：`git check-ignore --no-index -v ...` 能命中 `Packet_Tracer821_MacOS.dmg`、`Packet_Tracer821_Win_x64.exe`、自顶向下方法 PDF、小林 coding PDF。
- 注意：这些规则只能阻止未来误添加；已被 Git 跟踪的大文件仍需要后续 `git rm --cached` 或历史清理才能真正从上传内容中移除。
- 本轮观察到 `origin` 已为 `git@github.com:submergepsc/obsidian_notes.git`，`main` 已追踪 `origin/main` 且本地 ahead 9；该 remote/upstream 修复不是本轮执行。

## 2026-06-07 Push Size Explanation

- 用户执行 `git push origin main` 时看到 `5161` 个对象和 `5042` 个压缩对象，询问为什么最新提交只有 `7 files changed` 但 push 仍很庞大。
- 结论：push 发送的是 `origin/main..main` 范围内远端没有的所有对象，不是只发送最后一个 commit 的 diff。
- 当前 `main` 相对 `origin/main` ahead `9` 个提交；`git rev-list --objects origin/main..main` 显示新 blob 共 `4787` 个，总大小约 `1329.3MiB`。
- 其中大于 `10MiB` 的 blob 有 `7` 个，总计约 `1099.0MiB`，包括 Packet Tracer 安装包、网络教材 PDF、小林 coding PDF 和大 pptx/docx。
- `.gitignore` 只阻止未来未跟踪文件被添加；已经进入这 9 个本地提交的 blob 仍会被 push。

## Commands

- `ls -ld /home/loviya/obnotes /home/loviya/notes /home/loviya/notes/obsidian_notes`
- `git -C /home/loviya/notes/obsidian_notes status --short --branch`
- `git -C /home/loviya/notes/obsidian_notes remote -v`
- `git -C /home/loviya/notes/obsidian_notes config --show-origin --get-regexp '^(remote|branch)\.'`
- `git -C /home/loviya/notes/obsidian_notes ls-remote --heads origin`
- `git -C /home/loviya/notes/obsidian_notes ls-remote --heads git@github.com:submergepsc/obsidian_notes.git`
- `git -C /home/loviya/notes/obsidian_notes rev-list --left-right --count main...origin/main`
- `git -C /home/loviya/notes/obsidian_notes submodule status --recursive`
- `du -h -d 2 /home/loviya/notes/obsidian_notes | sort -h | tail -40`
- `git -C /home/loviya/notes/obsidian_notes count-objects -vH`
- `git ls-tree -r -l HEAD | awk ...`
- `git rev-list --objects --all | git cat-file --batch-check=...`
- `git check-ignore --no-index -v ...`
