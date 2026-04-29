# Linux resize命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux resize命令设置终端机视窗的大小。

执行resize指令可设置虚拟终端机的视窗大小。

### 语法

```bash
resize [-cu][-s <列数> <行数>]
```


**参数** ：

  * -c 就算用户环境并非C Shell，也用C Shell指令改变视窗大小。
  * -s <列数> <行数> 设置终端机视窗的垂直高度和水平宽度。
  * -u 就算用户环境并非Bourne Shell，也用Bourne Shell指令改变视窗大小。



###  实例

使用 C shell 

```bash
[root@linux runoob]# resize -c set noglob; setenv COLUMNS '99'; setenv LINES '34'; unset noglob;
```


使用 Bourne shell

```bash
[root@hnlinux runoob]# resize -u COLUMNS=99; LINES=34; export COLUMNS LINES;
```


设置指定大小

```bash
[root@hnlinux runoob]# resize -s 80 160
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
