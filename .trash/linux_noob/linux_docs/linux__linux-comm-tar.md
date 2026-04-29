# Linux tar 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux tar（英文全拼：tape archive ）命令用于备份文件。

tar 是 Linux 和 Unix 系统中用于归档文件和目录的强大命令行工具。

tar 名字来自 "tape archive"（磁带归档），最初用于将文件打包到磁带设备中，但现在广泛用于在文件系统中打包和压缩文件。

tar 通常用于将多个文件和目录打包成一个归档文件，称为 "tarball"（通常带有 .tar 扩展名）。

tar 本身不压缩文件，但可以与压缩工具（如 gzip 或 bzip2）结合使用，创建压缩的归档文件（如 .tar.gz 或 .tar.bz2）。

### 语法

```bash
tar [options] -f archive.tar [files...]
```


  * `-f archive.tar`：指定归档文件的名称。
  * `[files...]`：要打包的文件和目录。



### options 参数

**基本操作选项**

  * `-c`：创建一个新的归档文件。
  * `-x`：解压归档文件。
  * `-t`：列出归档文件的内容。
  * `-r`：向现有归档文件中追加文件。
  * `-u`：仅追加比归档文件中已有文件更新的文件。
  * `-d`：找到归档文件中与文件系统不同步的差异。
  * `-A`：将一个 `.tar` 文件追加到另一个 `.tar` 文件中。



**文件选择和排除**

  * `-f <file>`：指定归档文件的名称（必须放在选项列表的最后）。
  * `-C <directory>`：切换到指定目录进行操作。
  * `--exclude=<pattern>`：排除匹配指定模式的文件。
  * `--exclude-from=<file>`：从指定文件读取要排除的模式。
  * `--exclude-caches`：排除目录中的缓存文件。
  * `--exclude-backups`：排除以 `~` 结尾的备份文件。
  * `--exclude-vcs`：排除版本控制系统生成的文件（如 `.git`、`.svn` 等）。



**压缩和解压选项**

  * `-z`：使用 `gzip` 压缩归档文件。
  * `-j`：使用 `bzip2` 压缩归档文件。
  * `-J`：使用 `xz` 压缩归档文件。
  * `--lzip`：使用 `lzip` 压缩归档文件。
  * `--lzma`：使用 `lzma` 压缩归档文件。
  * `--lzop`：使用 `lzop` 压缩归档文件。
  * `--zstd`：使用 `zstd` 压缩归档文件。
  * `-a`：自动选择压缩方式（基于归档文件的扩展名，如 `.tar.gz`、`.tar.bz2` 等）。
  * `-I <command>`：使用指定的压缩程序进行压缩或解压。



**输出和交互选项**

  * `-v`：显示详细操作过程（verbose）。
  * `--progress`：显示进度条（与 `-v` 一起使用时）。
  * `-w` 或 `--interactive`：在每次操作前询问用户确认。
  * `--checkpoint`：在处理每个文件后显示一个检查点。
  * `--checkpoint-action=<action>`：在检查点执行指定的动作，如 `echo`、`dot` 等。
  * `--totals`：在操作结束后显示处理的总字节数。
  * `--verbose`：详细显示处理的信息。
  * `--quiet`：尽可能少的输出信息。



**文件和权限相关选项**

  * `-p`：保留文件的原始权限（解压时）。
  * `--same-owner`：尝试将解压的文件设为原始所有者（需超级用户权限）。
  * `--no-same-owner`：不设置文件所有者。
  * `--same-permissions`：保留文件的原始权限（与 `-p` 相同）。
  * `--no-same-permissions`：不保留原始权限，使用当前用户的 umask 设置权限。
  * `-m`：在解压时不恢复文件的修改时间，而使用当前时间。



**归档管理选项**

  * `-k` 或 `--keep-old-files`：解压时保留已有文件，不覆盖。
  * `--overwrite`：解压时强制覆盖已有文件。
  * `--remove-files`：归档成功后删除原始文件。
  * `--delete`：从归档文件中删除指定文件（仅限 `gnu tar`）。
  * `--keep-newer-files`：解压时保留比归档中较新的文件。
  * `--listed-incremental=<file>`：创建增量备份或从增量备份恢复。



**文件系统和设备选项**

  * `-L <N>`：分割大于 `N` 字节的归档文件（对于磁带机）。
  * `--tape-length=<number>`：指定磁带长度（对于磁带机）。
  * `--multi-volume`：创建或恢复多卷归档文件。
  * `-M`：与 `--multi-volume` 一起使用，处理多卷归档文件。
  * `--use-compress-program=<prog>`：使用指定的压缩程序。



**其他实用选项**

  * `--transform=<expression>`：重命名归档中的文件。
  * `--strip-components=<number>`：解压时剥离指定数量的路径组件。
  * `--ignore-failed-read`：忽略读取错误并继续操作。
  * `--occurrence=<number>`：在归档中选择第 `number` 个出现的文件。
  * `-S`：处理稀疏文件（仅归档实际使用的块）。
  * `--no-recursion`：不递归进入目录。
  * `-h` 或 `--dereference`：归档符号链接指向的文件而非链接本身。



**帮助和版本信息**

  * `--help`：显示帮助信息。
  * `--version`：显示 `tar` 的版本信息。



### 实例

**1、创建归档文件：** 将文件 file1、file2 和 directory 打包到一个名为 archive.tar 的归档文件中。

```bash
tar -cvf archive.tar file1 file2 directory
```


  * `-c`: 创建新的归档文件
  * `-v`: 显示详细输出，列出被添加到归档中的文件
  * `-f`: 指定归档文件的名称



**2、解压归档文件：** 解压名为 archive.tar 的归档文件，还原其中包含的文件和目录。

```bash
tar -xvf archive.tar
```


  * `-x`: 解压归档文件
  * `-v`: 显示详细输出，列出被解压的文件
  * `-f`: 指定要解压的归档文件的名称



**3、压缩归档文件：** 将名为 directory 的目录打包成一个归档文件，然后使用 gzip 进行压缩，生成名为 archive.tar.gz 的文件。

```bash
tar -czvf archive.tar.gz directory
```


  * `-c`: 创建新的归档文件
  * `-z`: 使用 gzip 压缩归档文件
  * `-v`: 显示详细输出，列出被添加到归档中的文件
  * `-f`: 指定归档文件的名称



**4、列出归档文件中的内容：** 列出名为 archive.tar 的归档文件中包含的所有文件和目录。

```bash
tar -tvf archive.tar
```


  * `-t`: 列出归档文件中的内容
  * `-v`: 显示详细输出，列出归档文件中的所有文件和目录
  * `-f`: 指定要列出内容的归档文件的名称



**5、追加文件到已存在的归档中：** 将名为 newfile 的文件添加到已存在的名为 archive.tar 的归档文件中。

```bash
tar -rvf archive.tar newfile
```


  * `-r`: 向已存在的归档中追加文件
  * `-v`: 显示详细输出，列出被添加到归档中的文件
  * `-f`: 指定已存在的归档文件的名称



**6、创建一个经过 gzip 压缩的归档文件：** 打包 directory 目录下的所有文件和子目录，并使用 gzip 压缩，生成名为 archive.tar.gz 的归档文件。

```bash
tar -zcvf archive.tar.gz directory
```


  * `-z`: 表示要使用 gzip 进行压缩。
  * `-c`: 表示创建新的归档文件。
  * `-v`: 表示详细输出，列出被添加到归档中的文件。
  * `-f archive.tar.gz`: 指定归档文件的名称为 `archive.tar.gz`。



**7、解压一个已经被 gzip 压缩的归档文件：** 解压 example.tar.gz 文件，并在当前目录下恢复其中包含的文件和目录。

```bash
tar -zxvf example.tar.gz
```


  * `-z`: 表示要使用 gzip 解压归档文件。
  * `-x`: 表示解压操作。
  * `-v`: 表示详细输出，列出被解压的文件。
  * `-f example.tar.gz`: 指定要解压的归档文件的名称为 `example.tar.gz`。



### 指定压缩格式

tar 可以结合不同的压缩程序来创建和解压压缩归档文件。

`z` : 使用 gzip 压缩。

```bash
tar -czvf archive.tar.gz directory tar -xzvf archive.tar.gz
```


`j`: 使用 bzip2 压缩。

```bash
tar -cjvf archive.tar.bz2 directory tar -xjvf archive.tar.bz2
```


`J`: 使用 xz 压缩。

```bash
tar -cJvf archive.tar.xz directory tar -xJvf archive.tar.xz
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
