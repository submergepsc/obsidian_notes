---
title: 小技巧 Tips
created: 2026-05-22
updated: 2026-05-24
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - tips
  - shell
  - battery
  - lenovo
  - ubuntu
---

# 小技巧 Tips

## 目录

- [复制文件内容到剪贴板](#复制文件内容到剪贴板)
- [替换文件或目录中的文本](#替换文件或目录中的文本)
- [Ubuntu 关闭 Lenovo 80% 充电保护](#ubuntu-关闭-lenovo-80-充电保护)

## 复制文件内容到剪贴板

把某个文件内容复制到系统剪贴板：

```sh
fileclip /path/to/file
```

脚本位置：`/home/loviya/.local/bin/fileclip`

它优先使用 CopyQ，既写入 CopyQ 历史，也同步为系统剪贴板。

## 替换文件或目录中的文本

只替换单个文件：

```sh
perl -pi -e 's#旧名称#新名称#g' /path/to/file
```

递归替换当前目录下所有包含目标文本的文件，先查看会改哪些文件：

```sh
rg -l '旧名称' .
```

确认后执行：

```sh
rg -l -0 '旧名称' . | xargs -0 perl -pi -e 's#旧名称#新名称#g'
```

示例：

```sh
rg -l -0 'in_tabel' . | xargs -0 perl -pi -e 's#in_tabel#pre_in_table#g'
```

注意：`.` 是目录，不能直接作为 `perl -pi` 的目标文件；要传具体文件，或用 `rg -l` 找出文件列表再传给 `perl`。

## Ubuntu 关闭 Lenovo 80% 充电保护

Lenovo Ideapad/小新一类机器在 Ubuntu 里 80% 左右停充，通常是 `ideapad_acpi` 的电池养护模式：

```bash
cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

含义：`1` 是开启养护/80% 停充，`0` 是关闭。

关闭停充、允许充到 100%：

```bash
echo 0 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

重新开启养护模式：

```bash
echo 1 | sudo tee /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode
```

如果路径不存在，先找实际接口：

```bash
find /sys -name conservation_mode 2>/dev/null
```
