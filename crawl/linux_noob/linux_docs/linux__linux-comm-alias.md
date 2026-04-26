# Linux alias 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux alias 命令用于设置指令的别名，用户可利用 alias，自定指令的别名。。

它可以使您以一种更简单和易于记忆的方式执行命令，而不必每次都键入完整的命令。

若仅输入 alias，则可列出目前所有的别名设置。

alias 的效果仅在该次登入的操作有效，若想要每次登入都生效，可在 `.profile` 或 `.cshrc` 中设定指令的别名。

### 语法

```bash
alias[别名]=[指令名称]
```


**参数说明** ：若不加任何参数，则列出目前所有的别名设置。

### 实例

1、创建别名：

```bash
alias ll='ls -alF'
```


此命令创建一个名为 `ll` 的别名，用于显示当前目录下所有文件和目录的详细列表。

2、显示别名：

```bash
alias
```


此命令将显示当前系统上所有的别名及其相应的命令。

删除别名：

```bash
unalias ll
```


此命令将删除名为 `ll` 的别名。

3、以 root 权限执行命令：

```bash
alias sudo='sudo '
```


此命令将创建一个名为 `sudo` 的别名，以便您可以通过在命令前加上 `sudo` 来以 **root** 权限执行命令。

**注意：** 在命令末尾有一个空格，这是因为如果没有空格，则无法正确识别以root权限执行的命令。

4、向历史记录中添加时间戳：

```bash
alias history='history | awk '"'"'{CMD="date +\"[%Y-%m-%d %H:%M:%S]\""; print CMD " " $0 }'"'"' | cut -c 29-'
```


此命令将创建一个名为 `history` 的别名，它会在您执行历史记录命令时添加时间戳。

**

注意：

** 此命令中的单引号内部有多个单引号和双引号，需要进行正确的转义。 

5、启用颜色输出

在 alias 命令中使用 "--color=auto" 参数可以让该命令在支持颜色输出的终端上自动启用颜色输出，从而提高命令行的可读性。例如：

```bash
alias ls='ls --color=auto'
```


这个命令将创建一个简化的 `ls` 命令，它将自动启用颜色输出。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
