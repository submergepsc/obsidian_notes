# Linux zipinfo 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux zipinfo 命令用于显示 `.zip` 压缩文件的详细信息，而不解压文件。

zipinfo 提供了有关压缩文件的内容、压缩比、时间戳等详细信息，是检查 .zip 文件内容的常用工具。

### 语法

```bash
zipinfo [options] file.zip
```


  * `file.zip`：要查看信息的 `.zip` 文件。



**options 参数** ：

  * `-1`：仅列出 `.zip` 文件中的文件名，每个文件占一行。
  * `-t`：显示每个文件的总数和未压缩后的总大小。
  * `-h`：以更加可读的格式（人性化的格式）显示文件大小（如 KB, MB）。
  * `-m`：显示 `.zip` 文件中每个文件的权限信息（Unix 格式）。
  * `-v`：显示更详细的信息，包括压缩方式、版本、压缩比等。
  * `-s`：总结 `.zip` 文件的总体信息，如文件数量、总大小等。
  * `-l`：详细列出 `.zip` 文件的内容，包括文件大小、日期、时间等。



### 实例

**列出 .zip 文件的内容**

```bash
zipinfo archive.zip
```


此命令会列出 archive.zip 中的所有文件和目录，并显示文件的基本信息，如文件大小、日期、时间和压缩比。

**仅列出文件名**

```bash
zipinfo -1 archive.zip
```


此命令只会列出 archive.zip 中的文件名，每个文件占一行，没有其他详细信息。

**显示详细信息**

```bash
zipinfo -v archive.zip
```


此命令会显示 archive.zip 中每个文件的详细信息，包括文件权限、压缩方式、压缩率、版本等。

**显示人性化的文件大小信息**

```bash
zipinfo -h archive.zip
```


此命令会显示文件大小的更加可读的格式（如 KB, MB），让文件大小更容易理解。

**总结 .zip 文件的整体信息**

```bash
zipinfo -s archive.zip
```


此命令会提供 archive.zip 文件的总信息，如文件总数、压缩和解压后的总大小等。

### 注意事项

  * `zipinfo` 是一个只读工具，不会对 `.zip` 文件进行任何修改。
  * `zipinfo` 提供的信息比 `unzip -l` 更为详细，适合在需要深入了解 `.zip` 文件时使用。



[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
