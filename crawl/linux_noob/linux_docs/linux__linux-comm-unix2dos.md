# Linux unix2dos 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

`unix2dos` 是一个用于将 Unix/Linux 格式的文本文件转换为 DOS/Windows 格式的实用工具。它主要处理文本文件中的行结束符（line endings）问题。

在 Unix/Linux 系统中，文本文件的每行以 **换行符（LF，`n`）** 结尾；而在 Windows 系统中，每行以 **回车符+换行符（CRLF，`rn`）** 结尾。这种差异可能导致在不同系统间共享文本文件时出现格式问题。

* * *

## 为什么需要 unix2dos

当你在以下场景工作时，可能需要使用 unix2dos：

  1. **跨平台协作** ：在 Linux 上编写的脚本或配置文件需要在 Windows 上使用时
  2. **文件传输** ：通过 FTP 或其他方式将文件从 Unix 系统传输到 Windows 系统
  3. **工具兼容性** ：某些 Windows 工具（如记事本）无法正确显示只有 LF 的行尾



* * *

## 安装 unix2dos

大多数 Linux 发行版默认不安装 unix2dos，但可以通过包管理器轻松安装：

### Debian/Ubuntu 系统

## 实例

```bash
sudo apt-get update sudo apt-get install dos2unix
```


### CentOS/RHEL 系统

```bash
sudo yum install dos2unix
```


### 注意

`unix2dos` 和 `dos2unix` 通常包含在同一个软件包中，安装 `dos2unix` 包会同时安装这两个工具。

* * *

## 基本语法

```bash
unix2dos [选项] 文件...
```


### 常用选项

选项 | 描述  
---|---  
`-b` 或 `--keep-bom` | 保留 UTF-8 字节顺序标记（BOM）  
`-c` 或 `--convmode` | 转换模式（ascii, 7bit, iso, mac）  
`-f` 或 `--force` | 强制转换二进制文件  
`-h` 或 `--help` | 显示帮助信息  
`-k` 或 `--keepdate` | 保持文件时间戳不变  
`-L` 或 `--license` | 显示软件许可证  
`-l` 或 `--newline` | 仅添加换行符  
`-m` 或 `--add-bom` | 添加 UTF-8 字节顺序标记  
`-n` 或 `--newfile` | 写入新文件（不修改原文件）  
`-o` 或 `--oldfile` | 写入原文件（默认行为）  
`-q` 或 `--quiet` | 静默模式，不显示警告  
`-V` 或 `--version` | 显示版本信息  
  
* * *

## 使用示例

### 示例 1：基本转换

将 Unix 格式的文件转换为 DOS 格式：

```bash
unix2dos file.txt
```


这会将 `file.txt` 的行尾从 LF 转换为 CRLF，直接修改原文件。

### 示例 2：保留原文件并创建新文件

如果你想保留原始文件并创建一个转换后的新文件：

```bash
unix2dos -n unixfile.txt dosfile.txt
```


### 示例 3：批量转换多个文件

使用通配符转换多个文件：

```bash
unix2dos *.txt
```


### 示例 4：递归转换目录中的所有文件

结合 `find` 命令递归处理目录：

```bash
find . -name "*.sh" -exec unix2dos {} ;
```


### 示例 5：保持文件时间戳不变

转换文件但不修改其时间戳：

```bash
unix2dos -k file.txt
```


* * *

## 实际应用场景

### 场景 1：Shell 脚本在 Windows 上运行

假设你编写了一个 Linux shell 脚本，但需要在 Windows 的 Git Bash 或 WSL 中运行：

```bash
unix2dos script.sh
```


### 场景 2：配置文件跨平台使用

当你的应用程序配置文件需要在 Windows 和 Linux 上共享时：

```bash
unix2dos config.properties
```


### 场景 3：与 Windows 用户共享文档

将 Markdown 文件转换为 Windows 格式以便同事用记事本编辑：

```bash
unix2dos README.md
```


* * *

## 注意事项

  1. **二进制文件** ：避免对二进制文件（如图片、压缩包）使用 unix2dos，除非你明确知道自己在做什么（可使用 `-f` 强制转换）
  2. **备份文件** ：直接修改原文件时，建议先备份重要文件
  3. **UTF-8 BOM** ：Windows 有时需要 BOM 来正确识别 UTF-8 编码，可使用 `-m` 选项添加
  4. **反向转换** ：如果需要将 DOS 格式转换为 Unix 格式，使用 `dos2unix` 命令



* * *

## 常见问题解答

### Q1：如何检查文件的换行符类型？

使用 `file` 命令：

```bash
file filename.txt
```


或使用 `cat` 显示特殊字符：

```bash
cat -A filename.txt
```


Unix 格式会显示 `$` 在行尾，DOS 格式会显示 `^M$`。

### Q2：转换后文件大小有变化吗？

是的，因为每行多了一个回车符（CR），文件通常会略微变大。

### Q3：为什么我的脚本在 Windows 上执行报错？

可能是因为行尾格式不正确，尝试用 unix2dos 转换后再执行。

### Q4：如何在脚本中自动检测和转换？

可以结合 `file` 命令和条件判断：

## 实例

```bash
if file filename.txt | grep -q "CRLF" ; then echo "File is already in DOS format" else unix2dos filename.txt fi
```


* * *

## 总结

`unix2dos` 是一个简单但强大的工具，解决了跨平台文本文件格式兼容性问题。通过本文的学习，你应该能够：

  1. 理解 Unix 和 DOS/Windows 行尾格式的区别
  2. 正确安装和使用 unix2dos 命令
  3. 处理各种文件转换场景
  4. 避免常见的转换错误



记住，在跨平台协作环境中，保持文本文件格式的一致性可以避免许多不必要的问题。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
