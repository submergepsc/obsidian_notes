# Linux basename 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 什么是 basename 命令

`basename` 是 Linux 系统中一个简单但实用的命令行工具，用于从文件路径中提取文件名部分。它就像是一个路径解析器，能够剥离目录信息，只保留最后的文件名。

**类比理解** ：想象你有一个完整的邮寄地址（如"中国/北京市/海淀区/中关村大街1号"），`basename` 的功能就是只提取最后的"中关村大街1号"部分。

* * *

## basename 命令的基本语法

```bash
basename [选项] 路径 [后缀]
```


### 参数说明

  1. **路径** （必需）：要处理的完整路径字符串
  2. **后缀** （可选）：如果指定，会从结果中移除这个后缀



### 常用选项

选项 | 说明  
---|---  
`-a` | 支持多个路径作为参数  
`-s 后缀` | 移除指定的后缀（等同于在命令末尾加后缀参数）  
`-z` | 使用空字符分隔输出结果（而不是换行符）  
  
* * *

## 基础用法示例

### 示例1：基本文件名提取

## 实例

```bash
$ basename / home / user / documents / report.txt report.txt
```


### 示例2：移除文件扩展名

## 实例

```bash
$ basename / home / user / documents / report.txt .txt report
```


### 示例3：处理多个文件（使用 -a 选项）

## 实例

```bash
$ basename -a / path / to / file1.txt / another / path / file2.log file1.txt file2.log
```


* * *

## 实际应用场景

### 场景1：批量处理文件扩展名

## 实例

```bash
for file in * .jpg; do mv " $file " " $(basename "$file" .jpg) .png" done
```


**解释** ：这个脚本会将当前目录下所有 .jpg 文件重命名为 .png 文件，只修改扩展名而保留原文件名。

### 场景2：在脚本中获取当前脚本名称

## 实例

```bash
#!/bin/bash SCRIPT_NAME =$ ( basename "$0" ) echo "正在运行脚本: $SCRIPT_NAME "
```


### 场景3：与 find 命令结合使用

## 实例

```bash
find / var / log -name "*.log" -exec basename { } \;
```


**作用** ：找出 /var/log 目录下所有 .log 文件并只显示文件名（不含路径）

* * *

## 常见问题解答

### Q1: basename 和 dirname 有什么区别？

命令 | 功能 | 示例输入 | 示例输出  
---|---|---|---  
`basename` | 提取路径最后部分 | /a/b/c.txt | c.txt  
`dirname` | 提取目录部分 | /a/b/c.txt | /a/b  
  
### Q2: 为什么我的 basename 命令不起作用？

常见原因：

  1. 路径中包含特殊字符（如空格）但未加引号

     * **错误** ：`basename /path/with spaces/file`
     * **正确** ：`basename "/path/with spaces/file"`
  2. 在脚本中使用变量时未加引号

     * **错误** ：`basename $filepath`
     * **正确** ：`basename "$filepath"`



* * *

## 进阶技巧

### 技巧1：处理多个后缀

## 实例

```bash
$ basename archive.tar.gz .gz archive.tar $ basename archive.tar.gz .tar.gz archive
```


### 技巧2：在管道中使用

## 实例

```bash
echo "/usr/local/bin/python" | xargs basename
```


输出：`python`

### 技巧3：结合参数扩展的替代方案

在 Bash 中，你也可以使用参数扩展实现类似功能：

## 实例

```bash
path = "/home/user/file.txt" filename = " ${path##*/} " # 等同于 basename echo " $filename "
```


* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
