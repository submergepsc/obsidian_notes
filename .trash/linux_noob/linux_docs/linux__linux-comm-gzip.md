# Linux gzip 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux gzip 命令用于压缩文件。

gzip 是个使用广泛的压缩程序，文件经它压缩过后，其名称后面会多出 `.gz` 的扩展名。

gzip 使用 DEFLATE 压缩算法，通常比 [bzip2](https://www.runoob.com/linux/linux-comm-bzip2.html) 更快，但压缩比稍低。

### 语法

```bash
gzip [options] [file...]
```


  * `file...`：要压缩的文件。`gzip` 会将指定的文件压缩，并生成一个 `.gz` 后缀的压缩文件，同时删除原始文件。



**options 参数选项** ：

  * `-d`：解压缩 `.gz` 文件。相当于使用 `gunzip` 命令。
  * `-k`：保留原始文件，不删除。
  * `-r`：递归压缩目录下的所有文件。
  * `-v`：显示详细的压缩或解压缩过程。
  * `-l`：显示压缩文件的详细信息，如压缩率、原始大小等。
  * `-1` 到 `-9`：指定压缩比。`-1` 是最快的压缩，压缩率最低；`-9` 是最慢的压缩，压缩率最高。默认是 `-6`。
  * `-t`：测试压缩文件的完整性。



### 实例

**压缩文件**

```bash
gzip example.txt
```


此命令会将 example.txt 压缩为 example.txt.gz，并删除原始文件 example.txt。

**保留原始文件**

如果希望在压缩后保留原始文件，可以使用 -k 选项：

```bash
gzip -k example.txt
```


此命令会保留原始的 example.txt 文件，并生成 example.txt.gz。

**解压缩文件**

要解压缩 .gz 文件，可以使用 -d 选项或直接使用 gunzip：

```bash
gzip -d example.txt.gz
```


或

```bash
gunzip example.txt.gz
```


这会将 example.txt.gz 解压缩为原始的 example.txt 文件。

**递归压缩目录**

你可以使用 -r 选项递归压缩整个目录：

```bash
gzip -r directory/
```


此命令会压缩 directory 目录下的所有文件，并保留目录结构。

**显示压缩文件信息**

使用 -l 选项可以查看 .gz 文件的详细信息：

```bash
gzip -l example.txt.gz
```


此命令会显示文件的原始大小、压缩后大小、压缩率等信息。

**测试压缩文件**

使用 -t 选项测试压缩文件的完整性：

```bash
gzip -t example.txt.gz
```


如果文件完整且无损坏，该命令将不会有输出；否则会提示错误。

gzip 主要用于压缩单个文件。如果需要压缩多个文件或整个目录，通常先用 tar 归档，再用 gzip 压缩。例如：

```bash
tar -cvzf archive.tar.gz directory/
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
