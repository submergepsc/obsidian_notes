# Linux lsattr 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux lsattr 命令用于显示文件扩展属性。

用 [chattr](https://www.runoob.com/linux/linux-comm-chattr.html) 执行改变文件或目录的属性，可执行 lsattr 指令查询其属性。

### 语法

```bash
lsattr [选项] [文件或目录...]
```


**常用选项** ：

  * -R: 递归显示目录及其子目录中所有文件的属性
  * -a: 显示所有文件，包括隐藏文件（以 `.` 开头的文件）
  * -d: 显示目录本身的属性，而不是目录内容
  * -v: 显示文件版本信息
  * -l: 使用长格式显示属性名称



运行 lsattr 后，输出格式通常如下：

```bash
\----i--------- /etc/passwd
```


  * **每一列代表一个属性** （类似 `ls -l` 的权限位）。
  * **`-` 表示未设置该属性**，**字母表示已设置** （如 `i`、`a`）。
  * **常见属性** （与 `chattr` 对应）：
    * `s`: secure deletion (安全删除)
    * `u`: undeletable (不可删除)
    * `c`: compressed (压缩)
    * `S`: synchronous updates (同步更新)
    * `i`: immutable (不可变)
    * `a`: append only (只能追加)
    * `d`: no dump (不备份)
    * `A`: no atime updates (不更新访问时间)
    * `I`: indexed directory (索引目录)
    * `j`: data journalling (数据日志)
    * `t`: no tail-merging (不进行尾部合并)
    * `T`: top of directory hierarchy (目录层次结构顶部)
    * `e`: extent format (扩展格式)



### 实例

**1\. 查看单个文件的属性**

```bash
lsattr /etc/passwd
```


输出示例：

```bash
\----i--------- /etc/passwd
```


`i` 表示该文件不可修改/删除。

**2\. 查看目录及其内容**

```bash
lsattr -R /var/log/ # 递归查看 /var/log/ 下所有文件
```


**3\. 仅查看目录本身的属性（不显示子文件）**

```bash
lsattr -d /tmp/
```


**4\. 显示隐藏文件的属性**

```bash
lsattr -a ~/.bashrc
```


**5\. 结合 chattr 使用**

```bash
sudo chattr +i important_file.txt # 设置为不可变 lsattr important_file.txt # 检查是否生效
```


输出：

```bash
\----i--------- important_file.txt
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
