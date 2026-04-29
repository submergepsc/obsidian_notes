# Linux zip 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux zip 命令用于压缩文件。

zip 是个使用广泛的压缩程序，压缩后的文件后缀名为 `.zip`。

与 gzip 或 bzip2 不同，zip 可以压缩多个文件或整个目录，并保留文件的目录结构。

zip 在跨平台（如 Windows、macOS）上也广泛支持。

### 语法

```bash
zip [options] output.zip file1 file2 ...
```


  * `output.zip`：生成的压缩文件名。
  * `file1 file2 ...`：要压缩的文件或目录。



**options 参数选项：**

  * `-r`：递归压缩目录及其子目录中的所有文件。
  * `-e`：为压缩文件设置密码保护。
  * `-q`：静默模式，不显示压缩过程。
  * `-v`：显示详细的压缩过程。
  * `-x`：排除某些文件或目录，不进行压缩。
  * `-m`：压缩后删除原始文件。
  * `-0` 到 `-9`：指定压缩级别，`-0` 表示存储不压缩，`-9` 表示最高压缩率，默认是 `-6`。



### 实例

**压缩单个文件**

```bash
zip archive.zip example.txt
```


此命令会将 example.txt 压缩为 archive.zip。

**压缩多个文件**

```bash
zip archive.zip file1.txt file2.txt file3.txt
```


此命令会将 file1.txt、file2.txt 和 file3.txt 压缩到 archive.zip 中。

**递归压缩目录**

```bash
zip -r archive.zip directory/
```


此命令会递归压缩 directory 目录及其子目录中的所有文件，并保留目录结构。

**压缩并设置密码保护**

```bash
zip -e archive.zip file.txt
```


此命令会压缩 file.txt 并设置密码保护，解压时需要输入密码。

**排除特定文件**

```bash
zip -r archive.zip directory/ -x "*.log"
```


此命令会压缩 directory/ 目录下的所有文件，但排除所有 .log 文件。

**压缩后删除原始文件**

```bash
zip -m archive.zip file.txt
```


此命令会将 file.txt 压缩为 archive.zip，并删除原始文件 file.txt。

**解压缩文件**

使用 unzip 命令来解压缩 .zip 文件：

```bash
unzip archive.zip
```


这会将 archive.zip 文件解压缩到当前目录，保留原始目录结构和文件。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
