# Linux dos2unix 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

dos2unix 是一个用于将文本文件从 DOS/Windows 格式转换为 Unix/Linux 格式的实用工具。它主要解决不同操作系统间换行符差异导致的问题。

**核心功能** ：

  * 将 DOS/Windows 格式的文本文件（CRLF 换行符）转换为 Unix/Linux 格式（LF 换行符）
  * 处理文件编码问题（可选）
  * 批量转换多个文件



* * *

## 为什么需要 dos2unix

### 换行符差异

不同操作系统使用不同的换行符：

  * **Windows/DOS** ：使用回车+换行（CRLF，即 `rn`）
  * **Unix/Linux** ：仅使用换行（LF，即 `n`）
  * **Mac OS（旧版本）** ：使用回车（CR，即 `r`）



### 问题表现

当 Windows 创建的文本文件在 Linux 系统打开时：

  * 可能出现 `^M` 字符（在 vi 中可见）
  * 脚本文件可能无法正常执行
  * 某些工具（如 grep、awk）可能无法正确处理文本



* * *

## 安装 dos2unix

大多数 Linux 发行版默认不安装 dos2unix，需要手动安装：

### Ubuntu/Debian

## 实例

```bash
sudo apt-get update sudo apt-get install dos2unix
```


### CentOS/RHEL

```bash
sudo yum install dos2unix
```


### 验证安装

```bash
dos2unix --version
```


* * *

## 基本语法

```bash
dos2unix [选项] 文件...
```


### 常用选项

选项 | 描述  
---|---  
`-k` | 保留文件时间戳不变  
`-f` | 强制转换，忽略二进制文件检查  
`-q` | 静默模式，不显示警告信息  
`-o` | 覆盖原始文件（默认行为）  
`-n` | 新文件模式，保留原文件，输出到新文件  
`-c` | 转换编码（需配合 `-e` 选项使用）  
`-e` | 指定目标编码（如 `-e utf8`）  
`-b` | 创建备份文件（添加 `.bak` 后缀）  
  
* * *

## 使用示例

### 1\. 基本转换

```bash
dos2unix file.txt
```


这将直接修改 file.txt 文件

### 2\. 保留原文件

```bash
dos2unix -n file.txt newfile.txt
```


原文件保持不变，转换结果保存到 newfile.txt

### 3\. 批量转换

```bash
dos2unix *.txt
```


转换当前目录下所有 .txt 文件

### 4\. 递归转换目录

```bash
find . -type f -name "*.sh" -exec dos2unix {} ;
```


转换当前目录及子目录下所有 .sh 文件

### 5\. 保留时间戳

```bash
dos2unix -k script.py
```


转换 script.py 但保持其修改时间不变

* * *

## 实际应用场景

### 1\. 修复从 Windows 传输的脚本

## 实例

```bash
# 转换脚本文件 dos2unix backup_script.sh # 添加执行权限 chmod +x backup_script.sh # 执行脚本 . / backup_script.sh
```


### 2\. 处理开发团队共享的配置文件

## 实例

```bash
# 转换整个配置目录 find / etc / myapp / conf.d / -type f -exec dos2unix { } ;
```


### 3\. 准备上传到 Linux 服务器的文件

```bash
dos2unix -b *.php # 转换并创建备份
```


* * *

## 注意事项

  1. **二进制文件** ：不要对二进制文件（如图片、PDF）使用 dos2unix，这会损坏文件
  2. **版本控制** ：在 Git 等版本控制系统中，最好统一设置换行符处理方式
  3. **编码问题** ：如果文件包含非 ASCII 字符，可能需要使用 `-c` 和 `-e` 选项处理编码
  4. **备份** ：重要文件转换前建议使用 `-b` 选项创建备份



* * *

## 替代方案

如果系统没有安装 dos2unix，可以使用以下替代方法：

### 1\. 使用 tr 命令

```bash
tr -d 'r' unixfile.txt
```


### 2\. 使用 sed 命令

```bash
sed -i 's/r$//' winfile.txt
```


### 3\. 使用 vim

## 实例

```bash
: set ff =unix : wq
```


* * *

## 总结

dos2unix 是处理跨平台文本文件格式问题的实用工具，特别适合：

  * 系统管理员维护服务器
  * 开发者在不同平台间协作
  * 处理从 Windows 迁移到 Linux 的脚本和配置文件



掌握 dos2unix 命令能有效避免因换行符差异导致的各种问题，提高工作效率。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
