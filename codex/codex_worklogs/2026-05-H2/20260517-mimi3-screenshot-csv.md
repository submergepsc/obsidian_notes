---
id: 20260517-mimi3-screenshot-csv
name: Mimi3 Screenshot CSV
slug: mimi3-screenshot-csv
cwd: /home/loviya/code/mimi3
summary: 根据用户截图在 mimi3 工作区创建一个两列表格 CSV，避免补全截断 token。
tags:
  - mimi3
  - csv
  - screenshot
---

## 当前快照

- 工作流 ID: `20260517-mimi3-screenshot-csv`
- 当前状态: `已完成`
- 当前目标: 根据截图创建 CSV 表格文件，并生成 `name=value; ...` 字符串输出文件。
- 当前阻塞: none
- 下一步: none
- 标签: `mimi3`, `csv`, `screenshot`
- 摘要: 已新增 `image_table.csv`、`csv_to_string.py` 和 `image_table_string.txt`；脚本读取 `名称`/`值` 两列并输出类似 `serviceToken="..."; userId=...` 的字符串文件。后续修正了 CSV 双引号处理，保留第二列原本用 CSV 引号包住的值。

## 关键结果

- 新增 `/home/loviya/code/mimi3/image_table.csv`。
- 新增 `/home/loviya/code/mimi3/csv_to_string.py`。
- 运行脚本生成 `/home/loviya/code/mimi3/image_table_string.txt`。
- 修正 `/home/loviya/code/mimi3/csv_to_string.py`：读取原始 CSV 行判断第二列是否以 `"` 开头，生成字符串时对这类值补回一层双引号。
- CSV 行来自截图可见内容：`cUserId`、`serviceToken`、`uLocale`、`userId`、`xiaomichat...`。
- 对 `serviceToken` 等可疑敏感字段只保存截图可见的截断内容。

## 验证

- 使用 `sed -n '1,20p' image_table.csv` 复查 CSV 文件内容。
- 使用 `python3 csv_to_string.py` 生成输出，命令打印了一行格式化字符串。
- 使用 `sed -n '1,5p' image_table_string.txt` 复查输出文件。
- 使用 `python3 -m py_compile csv_to_string.py` 验证脚本语法通过。
- 2026-05-18 00:04 CST 再次运行脚本，确认 `serviceToken` 和 `xiaomichatbot_ph` 输出为双引号包裹，`userId` 不带双引号；未把完整 token 写入 worklog。
