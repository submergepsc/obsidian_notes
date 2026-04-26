# Linux cp 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux cp（英文全拼：copy file）命令主要用于复制文件或目录。

通过 cp 命令，用户可以将文件或目录从一个位置复制到另一个位置，同时可以选择保留原文件的属性（如权限、时间戳等）。

### 语法

```bash
cp [options] source dest 或 cp [选项] 源文件 目标文件
```


其中，source（源文件）表示要复制的文件或目录的路径，dest（目标文件）表示复制后的文件或目录的路径。

**选项说明** ：

  * `-r` 或 `-R`：递归复制目录及其内容（用于复制目录）。

  * `-i`：交互模式，覆盖前提示用户确认。

  * `-f`：强制复制，覆盖目标文件而不提示。

  * `-v`：显示详细的复制过程（verbose）。

  * `-p`：保留文件的原始属性（如权限、时间戳等）。

  * `-a`：归档模式，等同于 `-dpR`，保留所有文件属性和递归复制目录。

  * `-u`：仅当源文件比目标文件新时才复制（更新模式）。

  * `-l`：创建硬链接而不是复制文件。

  * `-s`：创建符号链接（软链接）而不是复制文件。




### 实例

**1\. 复制文件到目标目录**

```bash
cp file.txt /path/to/destination/
```


将 file.txt 复制到 /path/to/destination/ 目录中。

**2\. 复制文件并重命名**

```bash
cp file.txt /path/to/destination/newfile.txt
```


将 file.txt 复制到 /path/to/destination/ 目录并重命名为 newfile.txt。

**3\. 递归复制目录**

```bash
cp -r /path/to/source_dir /path/to/destination/
```


将 source_dir 目录及其内容递归复制到 destination 目录。

**4\. 交互模式复制**

```bash
cp -i file.txt /path/to/destination/
```


如果目标位置已存在同名文件，会提示用户确认是否覆盖。

**5\. 保留文件属性**

```bash
cp -p file.txt /path/to/destination/
```


复制文件并保留其原始属性（如权限、时间戳等）。

**6\. 仅复制更新的文件**

```bash
cp -u file.txt /path/to/destination/
```


仅当 file.txt 比目标文件新时才复制。

**7\. 显示复制过程**

```bash
cp -v file.txt /path/to/destination/
```


显示复制的详细信息。

**8\. 创建硬链接或符号链接**

```bash
cp -l file.txt /path/to/destination/ # 创建硬链接 cp -s file.txt /path/to/destination/ # 创建符号链接
```


**9\. 复制多个文件到目录**

```bash
cp file1.txt file2.txt /path/to/destination/
```


将多个文件复制到目标目录。

**10\. 使用通配符复制**

```bash
cp *.txt /path/to/destination/
```


复制所有 .txt 文件到目标目录。

**11\. 结合 find 命令复制特定文件**

```bash
find /path/to/source -name "*.log" -exec cp {} /path/to/destination/ \;
```


查找并复制所有 .log 文件到目标目录。

以上只是 cp 命令的一些常见用法，你可以通过运行 `man cp` 命令查看更多选项和用法。

### 注意事项

  1. 如果目标路径是一个目录，`cp` 会将源文件或目录复制到该目录中。

  2. 如果目标路径是一个文件名，`cp` 会将源文件复制并重命名为目标文件名。

  3. 复制目录时，必须使用 `-r` 或 `-R` 选项，否则会报错。

  4. 如果目标文件已存在，默认情况下 `cp` 会覆盖它（除非使用 `-i` 选项）。




[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
