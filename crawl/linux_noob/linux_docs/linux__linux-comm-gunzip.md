# Linux gunzip 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux gunzip 命令用于解压文件。

gunzip 是个使用广泛的解压缩程序，它用于解开被 gzip 压缩过的文件，这些压缩文件预设最后的扩展名为 `.gz`。事实上 gunzip 就是 gzip 的硬连接，因此不论是压缩或解压缩，都可通过 gzip 指令单独完成。

### 语法

**参数** ：

```bash
gunzip [选项] 压缩文件
```


  * `-c`：将解压缩后的文件内容输出到标准输出（而不是写入文件）。
  * `-d`：解压缩文件。这是默认的行为，可以省略。
  * `-f`：强制解压缩，即使已存在同名的解压缩文件。
  * `-h`：显示帮助信息。
  * `-k`：保留原始的压缩文件。解压缩后的文件会保留在同一目录下，而不会删除原始文件。
  * `-l`：显示压缩文件的详细信息，包括压缩前后的文件大小、压缩比等。
  * `-n`：不覆盖已存在的解压缩文件。如果已存在同名文件，则不会进行解压缩操作。
  * `-q`：静默模式，不显示解压缩进度和错误信息。
  * `-r`：递归地解压缩指定目录下的所有文件。
  * `-t`：测试压缩文件的完整性，而不进行实际的解压缩操作。
  * `-v`：显示详细的解压缩信息，包括解压缩的文件名、压缩比等。
  * `--help`：显示帮助信息。
  * `--version`：显示 `gunzip` 命令的版本信息。



### 实例

1、解压缩文件：

```bash
gunzip example.txt.gz
```


这将解压缩名为 example.txt.gz 的文件，并生成一个名为 example.txt 的解压缩文件。

2、解压缩文件并保留原始文件：

```bash
gunzip -k example.txt.gz
```


这将解压缩 example.txt.gz 文件，并生成一个名为 example.txt 的解压缩文件，同时保留原始的 example.txt.gz 文件。

解压缩文件并将内容输出到标准输出：

```bash
gunzip -c example.txt.gz
```


这将解压缩 example.txt.gz 文件，并将解压缩后的内容输出到标准输出，而不是生成解压缩文件。

递归地解压缩目录下的所有文件：

```bash
gunzip -r directory
```


这将递归地解压缩指定目录 directory 下的所有以 gzip 格式压缩的文件。

需要注意的是，gunzip 命令只能解压缩 gzip 格式的文件，不能用于解压其他压缩格式，如 ZIP、RAR 等。如需解压其他格式的压缩文件，可以使用相应的工具，例如 unzip 命令用于解压缩 ZIP 文件。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
