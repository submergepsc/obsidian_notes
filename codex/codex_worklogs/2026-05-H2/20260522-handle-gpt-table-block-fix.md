---
id: 20260522-handle-gpt-table-block-fix
name: handle_gpt_text Markdown 表格处理修复
slug: handle-gpt-table-block-fix
cwd: /home/loviya
summary: 修复 /home/loviya/handle_gpt_text.sh 对 Markdown 表格块的处理，保留表格并在表格块前后补空行。
tags:
  - shell
  - text-cleanup
  - markdown
  - handle-gpt
---

# Current Snapshot

- workflow id: 20260522-handle-gpt-table-block-fix
- current status: 已完成
- current goal: 修复 `/home/loviya/handle_gpt_text.sh` 无法正常处理 Markdown 表格的问题，尤其是 `|文件|作用|` / `|---|---|` / `` `book.toml` `` 这种表格。
- current blocker: 无
- next step: 无
- tags: shell, text-cleanup, markdown, handle-gpt
- summary: 已将脚本改为 Perl `-ne` 持久状态处理：删除空行和单独 `---`，保留 Markdown 表格块，并在表格块前后补一个空行。

# Findings

- `/home/loviya/handle_gpt_text.sh` 是 `handle_gpt` alias 的目标。
- 当前 Perl 片段中 `my $printed=0; my $pre_in_table=0;` 位于逐行循环内部，每行都会重置。
- 用户给出的表格行应被识别为一个连续 Markdown 表格块，不能因为 `|---|---|` 或反引号内容导致错误处理。

# Artifacts

- `/home/loviya/handle_gpt_text.sh`

# Changes

- 修改 `/home/loviya/handle_gpt_text.sh` 的 Perl 清理逻辑：
  - 从逐行重置状态的 `-pe` 改为 `-ne`，在 `BEGIN` 中维护 `$printed`、`$in_table`、`$pending_blank`。
  - 单独一行 `---` 仍被删除。
  - 空行仍被删除，再由脚本按表格块边界补必要空行。
  - `^\s*\|.*\|\s*$` 识别为 Markdown 表格行，连续表格行作为一个表格块保留。

# Verification

- `bash -n /home/loviya/handle_gpt_text.sh` 通过。
- 使用用户样例验证：`|文件|作用|`、`|---|---|`、``|`book.toml`|配置书名、作者、输出、主题与插件等|`` 均保留。
- 额外验证：单独 `---` 被删除，但表格分隔行 `|---|---|` 保留；表格块前后各有一个空行。

# Follow-up: 标题后表格不插空行

- 用户补充：如果上一行含有 `#` 是标题，标题和表格之间不需要插入空行。
- 已在 `/home/loviya/handle_gpt_text.sh` 增加 `$last_was_heading` 状态。
- 新规则：进入表格块时，如果上一条输出行是 `^\s*#` 标题，则不调用 `emit_blank()`；正文后进入表格仍补空行。
- 验证：`bash -n /home/loviya/handle_gpt_text.sh` 通过；样例中 `# 文件列表` 后表格紧跟显示，正文后表格仍保留空行。
