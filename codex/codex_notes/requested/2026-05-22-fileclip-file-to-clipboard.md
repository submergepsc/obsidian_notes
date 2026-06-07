---
title: fileclip 文件内容复制到剪贴板
created: 2026-05-22
updated: 2026-05-22
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - clipboard
  - copyq
  - shell
source_worklog: 20260522-fileclip-command
---

# fileclip 文件内容复制到剪贴板

## 结论

本机已有命令：`/home/loviya/.local/bin/fileclip`

用法：

```sh
fileclip /path/to/file
```

效果：把指定普通文件的内容复制到系统剪贴板。脚本优先使用 CopyQ：

```sh
copyq --start-server add - <"$file"
copyq --start-server select 0
```

这样既写入 CopyQ 历史，又把最新项设为系统剪贴板。

## 回退逻辑

如果 `copyq` 不可用，脚本按顺序尝试：

1. `wl-copy`
2. `xclip -selection clipboard`

如果这些工具都不可用，会报错：`fileclip: no clipboard tool found; install copyq, wl-clipboard, or xclip`

## 验证方式

语法检查：

```sh
sh -n /home/loviya/.local/bin/fileclip
```

确认 PATH：

```sh
command -v fileclip
```

真实 CopyQ 读回验证示例：

```sh
printf '%s\n' hello >/tmp/fileclip-test.txt
fileclip /tmp/fileclip-test.txt
copyq --start-server read 0
```

预期读回 `/tmp/fileclip-test.txt` 的内容。

## 注意

- 只接受一个参数，并要求目标是可读的普通文件。
- 内容按文件原样通过 stdin 送入剪贴板工具，不做文本加工。
- 如果复制的是敏感文件，内容会进入 CopyQ 历史；需要时手动清理 CopyQ 历史。
