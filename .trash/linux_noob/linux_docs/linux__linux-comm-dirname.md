# Linux dirname 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 什么是 dirname 命令

`dirname` 是 Linux/Unix 系统中一个简单但实用的命令行工具，用于从文件路径中提取目录部分。它可以帮助你快速获取路径中的父目录，而无需手动解析字符串。

### 基本功能

  * 输入：一个文件路径字符串
  * 输出：该路径的目录部分（即去掉最后一个斜杠后的内容）



* * *

## 命令语法

```bash
dirname [选项] 文件名...
```


### 参数说明

  * **文件名** ：可以是一个或多个文件路径（支持绝对路径和相对路径）
  * **...**：表示可以同时处理多个文件路径



### 选项参数

虽然大多数情况下 `dirname` 不需要选项，但 GNU 版本支持以下标准选项：

选项 | 说明  
---|---  
`-z` | 使用 NUL 字符（\0）分隔输出，而不是换行符  
`--help` | 显示帮助信息  
`--version` | 显示版本信息  
  
* * *

## 工作原理

`dirname` 命令通过以下步骤处理路径：

  1. 删除路径末尾的所有斜杠（/）
  2. 删除最后一个斜杠及其后的所有字符
  3. 如果结果为空，则输出 "."（当前目录）



### 处理流程图

![](./images/linux-comm-dirname-runoob.png)

* * *

## 使用示例

### 基础用法

## 实例

```bash
$ dirname / home / user / docs / file.txt / home / user / docs $ dirname relative / path / to / file relative / path / to
```


### 处理多个文件

## 实例

```bash
$ dirname / a / b / c.txt / x / y / z.txt / a / b / x / y
```


### 特殊路径处理

## 实例

```bash
$ dirname / usr / bin / # 注意末尾斜杠 / usr $ dirname file.txt # 只有文件名 . $ dirname / # 根目录 /
```


### 在脚本中使用

## 实例

```bash
#!/bin/bash # 获取脚本所在目录 SCRIPT_DIR =$ ( dirname "$0" ) echo "脚本目录: $SCRIPT_DIR " # 获取配置文件路径的目录 CONFIG_PATH = "/etc/app/config.cfg" CONFIG_DIR =$ ( dirname " $CONFIG_PATH " ) echo "配置目录: $CONFIG_DIR "
```


* * *

## 常见应用场景

### 1\. 获取脚本所在目录

## 实例

```bash
#!/bin/bash # 获取脚本所在绝对路径 SCRIPT_DIR =$ ( dirname " $(readlink -f "$0") " ) echo "脚本所在目录: $SCRIPT_DIR "
```


### 2\. 构建相对路径

## 实例

```bash
# 假设我们知道文件在某个目录的子目录中 BASE_DIR = "/var/log" FULL_PATH = " $BASE_DIR /app/error.log" # 获取日志目录 LOG_DIR =$ ( dirname " $FULL_PATH " )
```


### 3\. 与 basename 配合使用

## 实例

```bash
# 分解完整路径 FULL_PATH = "/home/user/docs/report.pdf" DIR =$ ( dirname " $FULL_PATH " ) FILE =$ ( basename " $FULL_PATH " ) echo "目录: $DIR " echo "文件名: $FILE "
```


* * *

## 注意事项

**符号链接** ：`dirname` 不会解析符号链接，如需解析，可结合 `readlink` 使用

## 实例

```bash
dirname " $(readlink -f "/path/with/symlink") "
```


**空格处理** ：路径包含空格时，确保使用引号

## 实例

```bash
dirname "/path/with spaces/file.txt"
```


**相对路径** ：输出结果会保持相对路径形式

## 实例

```bash
$ dirname .. / parent / file.txt .. / parent
```


**空输入** ：如果没有提供参数，GNU 版本会输出 "."，但这不是 POSIX 标准行为

* * *

## 与类似命令对比

命令 | 功能 | 示例输入 | 示例输出  
---|---|---|---  
`dirname` | 提取目录部分 | /a/b/c.txt | /a/b  
`basename` | 提取文件名部分 | /a/b/c.txt | c.txt  
`realpath` | 获取绝对路径（解析符号链接） | ../file | /full/path/to/file  
  
* * *

## 实践练习

创建一个测试文件并获取其目录路径

## 实例

```bash
touch / tmp / testfile dirname / tmp / testfile
```


编写一个脚本，显示它自身所在的目录

## 实例

```bash
#!/bin/bash echo "本脚本位于: $(dirname "$0") "
```


尝试处理包含空格和特殊字符的路径

## 实例

```bash
mkdir -p "/tmp/my dir" touch "/tmp/my dir/special file.txt" dirname "/tmp/my dir/special file.txt"
```


* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
