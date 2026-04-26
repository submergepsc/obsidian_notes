# Linux bzip2 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux bzip2 命令用于压缩文件。

与 gzip 类似，bzip2 通过采用更高效的压缩算法（Burrows-Wheeler算法）提供更好的压缩率，但通常压缩速度稍慢。

### 语法

```bash
bzip2 [options] [file...]
```


  * `file...`：要压缩的文件。`bzip2` 会将指定的文件压缩，并生成一个 `.bz2` 后缀的压缩文件，同时删除原始文件。



**options 常用参数** ：

  * `-d`：解压缩一个 `.bz2` 文件。相当于使用 `bunzip2` 命令。
  * `-k`：保留原始文件，不删除。
  * `-v`：显示详细的压缩或解压缩过程。
  * `-z`：强制压缩，即使文件已经被压缩。
  * `-t`：测试压缩文件的完整性。
  * `-1` 到 `-9`：指定压缩比。`-1` 是最快的压缩，压缩率最低；`-9` 是最慢的压缩，压缩率最高。默认是 `-9`。



### 实例

**压缩文件**

```bash
bzip2 example.txt
```


此命令会将 example.txt 压缩为 example.txt.bz2，并删除原始文件 example.txt。

**保留原始文件**

如果希望在压缩后保留原始文件，可以使用 `-k` 选项：

```bash
bzip2 -k example.txt
```


此命令会保留原始的 example.txt 文件，并生成 example.txt.bz2。

**解压缩文件**

要解压缩 .bz2 文件，可以使用 -d 选项或直接使用 bunzip2：

```bash
bzip2 -d example.txt.bz2
```


或

```bash
bunzip2 example.txt.bz2
```


这会将 example.txt.bz2 解压缩为原始的 example.txt 文件。

**测试压缩文件**

可以使用 -t 选项来测试压缩文件的完整性：

```bash
bzip2 -t example.txt.bz2
```


如果文件完整且无损坏，该命令将不会有输出；否则会提示错误。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
