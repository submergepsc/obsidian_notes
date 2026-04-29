# Linux lha 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux lha 命令用于压缩或解压缩文件。

lha 是一个在 Linux 系统中用于处理 `.lzh` 和 `.lha` 压缩文件的命令行工具。它最初是为处理日本流行的 LHA 压缩格式而开发的，现在仍然在某些特定场景下使用。

### 主要特点

  * 支持压缩和解压缩 `.lzh` 和 `.lha` 格式文件
  * 兼容旧的 DOS/Windows 压缩文件
  * 轻量级，适合资源有限的环境
  * 保留文件原始属性（如时间戳）



* * *

## 安装 lha 工具

在大多数 Linux 发行版中，lha 不是预装工具，需要手动安装：

### Ubuntu/Debian 系统

## 实例

```bash
sudo apt-get update sudo apt-get install lha
```


### CentOS/RHEL 系统

## 实例

```bash
sudo yum install lha
```


### 验证安装

## 实例

```bash
lha \--version
```


* * *

## 基本命令语法

lha 命令的基本语法格式为：

## 实例

```bash
lha [ 选项 ] 命令 压缩文件 [ 文件 / 目录... ]
```


### 常用命令参数

命令 | 说明  
---|---  
a | 添加文件到压缩包  
e | 解压文件（不保留路径）  
x | 解压文件（保留完整路径）  
l | 列出压缩包内容  
t | 测试压缩包完整性  
d | 从压缩包删除文件  
  
### 常用选项参数

选项 | 说明  
---|---  
-v | 显示详细操作信息  
-q | 安静模式（不显示输出）  
-f | 强制执行操作  
-x | 允许扩展属性  
-p | 保留文件权限  
  
* * *

## 使用示例

### 1\. 创建压缩文件

将目录 `project` 压缩为 `project.lzh`：

## 实例

```bash
lha a project.lzh project /
```


添加多个文件和目录：

## 实例

```bash
lha a archive.lzh file1.txt file2.txt dir1 /
```


### 2\. 列出压缩包内容

查看 `archive.lzh` 中的文件列表：

## 实例

```bash
lha l archive.lzh
```


输出示例：

```bash
PERMISSION UID GID SIZE RATIO STAMP NAME \---------- ----------- ------- ------ ------------ -------------------- -rw-r--r-- 1000/1000 1024 65.3% May 15 10:00 file1.txt -rw-r--r-- 1000/1000 2048 70.1% May 15 10:05 file2.txt drwxr-xr-x 1000/1000 0 0.0% May 15 09:55 dir1/
```


### 3\. 解压文件

解压到当前目录（不保留路径）：

## 实例

```bash
lha e archive.lzh
```


解压并保留完整路径结构：

## 实例

```bash
lha x archive.lzh
```


解压特定文件：

## 实例

```bash
lha e archive.lzh file1.txt
```


### 4\. 测试压缩包完整性

## 实例

```bash
lha t archive.lzh
```


### 5\. 从压缩包删除文件

删除 `archive.lzh` 中的 `file1.txt`：

## 实例

```bash
lha d archive.lzh file1.txt
```


* * *

## 高级用法

### 1\. 分卷压缩

创建分卷压缩（每卷1MB）：

## 实例

```bash
lha -v -s1024k a archive.lzh large_dir /
```


### 2\. 设置压缩级别

指定压缩级别（0-5，默认2）：

## 实例

```bash
lha -2 a archive.lzh files / # 较高压缩率 lha -0 a archive.lzh files / # 仅存储，不压缩
```


### 3\. 排除特定文件

使用 `-x` 排除文件：

## 实例

```bash
lha a -x * .tmp archive.lzh dir /
```


* * *

## 常见问题解答

### Q1: lha 和 zip/gzip 有什么区别？

  * lha 是专门处理 `.lzh/.lha` 格式的工具
  * 压缩率通常不如 gzip/bzip2
  * 主要优势是兼容旧的日本系统文件



### Q2: 如何解压密码保护的 .lzh 文件？

lha 本身不支持密码保护，需要使用其他工具如 `unar`：

## 实例

```bash
unar -p password protected.lzh
```


### Q3: 为什么我的 lha 命令不起作用？

可能原因：

  1. 未安装 lha 工具（参考安装部分）
  2. 文件权限问题（尝试使用 sudo）
  3. 压缩文件损坏（使用 `lha t` 测试）



* * *

## 最佳实践建议

  1. **兼容性考虑** ：只在需要处理旧系统文件时使用 lha，新项目建议使用更通用的 zip 或 tar.gz

  2. **脚本中使用** ：添加 `-q` 选项避免输出干扰：




## 实例

```bash
lha -q a backup.lzh / path / to / files
```


  3. **结合 find 使用** ：压缩特定类型的文件



## 实例

```bash
find . -name "*.txt" -exec lha a textfiles.lzh { } \+
```


  4. **备份场景** ：保留文件属性



## 实例

```bash
lha -p a backup.lzh important_dir /
```


* * *

## 替代方案

虽然 lha 有其特定用途，但现代 Linux 系统更常用这些工具：

工具 | 格式 | 特点  
---|---|---  
tar | .tar | 仅打包，不压缩  
gzip | .gz | 高压缩比  
bzip2 | .bz2 | 更高压缩比，速度较慢  
xz | .xz | 极高压缩比  
zip | .zip | 跨平台兼容  
7z | .7z | 多种压缩算法支持  
  
[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
