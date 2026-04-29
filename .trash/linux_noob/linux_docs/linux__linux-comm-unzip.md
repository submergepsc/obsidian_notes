# Linux unzip 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux unzip 命令用于解压缩 `.zip` 格式的压缩文件。

unzip 工具能够解压缩包含多个文件和目录的 .zip 文件，并且广泛用于处理跨平台压缩文件。

### 语法

```bash
unzip [options] file.zip
```


  * `file.zip`：要解压缩的 `.zip` 文件。



**options 参数** ：

  * `-d <directory>`：将解压缩的文件放入指定的目录。
  * `-l`：列出 `.zip` 文件中的内容，但不解压。
  * `-v`：显示详细信息，包括 `.zip` 文件的结构和压缩率等信息。
  * `-t`：测试 `.zip` 文件的完整性，但不解压。
  * `-n`：解压时不覆盖已存在的文件。
  * `-o`：解压时覆盖已存在的文件，而不提示。
  * `-x <pattern>`：解压时排除指定的文件或目录。
  * `-j`：解压时不保留目录结构，将所有文件解压到当前目录中。



### 实例

**解压缩 .zip 文件**

```bash
unzip archive.zip
```


此命令会将 archive.zip 中的内容解压缩到当前目录。

**解压到指定目录**

```bash
unzip archive.zip -d /path/to/directory
```


此命令会将 archive.zip 中的内容解压缩到指定的 /path/to/directory 目录中。

**列出 .zip 文件的内容**

```bash
unzip -l archive.zip
```


此命令会列出 archive.zip 中的所有文件和目录，但不会实际解压。

**测试 .zip 文件的完整性**

```bash
unzip -t archive.zip
```


此命令会测试 archive.zip 文件的完整性，以确保文件没有损坏。

**解压时排除特定文件**

```bash
unzip archive.zip -x "*.log"
```


此命令会解压 archive.zip，但排除所有 .log 文件。

**解压时不覆盖已存在的文件**

```bash
unzip -n archive.zip
```


此命令会解压 archive.zip 中的文件，但如果目标目录中已经存在同名文件，则跳过该文件，不进行覆盖。

**解压缩文件并覆盖已存在的文件**

```bash
unzip -o archive.zip
```


此命令会在解压 archive.zip 时覆盖目标目录中已存在的同名文件，而不会提示用户。

**解压缩时不保留目录结构**

```bash
unzip -j archive.zip
```


此命令会解压 archive.zip 中的所有文件到当前目录，而不会保留原始的目录结构。

### 注意事项

  * `unzip` 默认解压文件时会保留原始的目录结构。如果不需要保留目录结构，可以使用 `-j` 选项。
  * `unzip` 可以通过 `-x` 选项排除某些文件或目录，这对于有选择性地解压缩特定文件很有用。



[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
