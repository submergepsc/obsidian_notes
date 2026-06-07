title: "01 Linux 终端基础与帮助系统"
# 01 Linux 终端基础与帮助系统
## 1. 什么是终端
终端是用文字命令和系统交互的界面。你输入命令，Shell 解释命令，然后系统执行。
常见 Shell：

| Shell | 说明 |
| --- | --- |
| `bash` | Ubuntu 常见默认 Shell |
| `zsh` | 功能更丰富，很多人搭配 Oh My Zsh 使用 |
| `sh` | 更基础的 Shell |

查看当前 Shell：
```bash
echo $SHELL
```
查看当前正在运行的 Shell：
```bash
ps -p $$
```
## 2. 命令的基本结构
Linux 命令通常长这样：
```text
命令 [选项] [参数]
```
例子：
```bash
ls -lah /home
```
拆开看：
```text
ls       命令，list 的缩写
-lah     选项，等价于 -l -a -h
/home    参数，表示要查看的目录
```
再看一个例子：
```bash
grep -n "error" app.log
```
拆开看：
```text
grep     命令，用来搜索文本
-n       显示行号
"error"  搜索关键词
app.log  被搜索的文件
```
## 3. 短选项与长选项
短选项通常是一个减号：
```bash
ls -l
ls -a
ls -h
```
多个短选项可以合并：
```bash
ls -lah
```
长选项通常是两个减号：
```bash
ls --help
grep --ignore-case "hello" file.txt
```
## 4. 命令提示符
你可能看到类似：
```text
loviya@nibaba:~$
```
含义：
```text
loviya    当前用户名
nibaba    主机名
~         当前目录，~ 表示家目录
$         普通用户提示符
```
如果是：
```text
root@nibaba:/#
```
通常表示 root 用户，权限很高，操作要更谨慎。
## 5. 命令路径和 PATH
当你输入：
```bash
ls
```
Shell 会在 `PATH` 变量列出的目录里寻找叫 `ls` 的可执行文件。
查看 `PATH`：
```bash
echo $PATH
```
查看命令来自哪里：
```bash
which ls
type ls
```
区别：

| 命令 | 说明 |
| --- | --- |
| `which` | 查找外部可执行文件路径 |
| `type` | 更全面，能看出命令是内建命令、别名还是文件 |

例子：
```bash
type cd
```
你会发现 `cd` 是 Shell 内建命令，不是普通文件。
## 6. 常用快捷键
| 快捷键 | 作用 |
| --- | --- |
| `Ctrl + C` | 中断当前命令 |
| `Ctrl + D` | 发送 EOF，常用于退出 |
| `Ctrl + L` | 清屏，类似 `clear` |
| `Ctrl + A` | 光标移动到行首 |
| `Ctrl + E` | 光标移动到行尾 |
| `Ctrl + U` | 删除光标前内容 |
| `Ctrl + K` | 删除光标后内容 |
| `↑` / `↓` | 上一条/下一条历史命令 |
| `Tab` | 自动补全命令或路径 |

例子：
```bash
cd ~/linux<Tab>
```
Shell 会尝试补全目录名。
## 7. 查看帮助
### `--help`
很多命令支持：
```bash
ls --help
grep --help
tar --help
```
适合快速查看选项。
### `man`
`man` 是 manual 的缩写：
```bash
man ls
man grep
man tar
```
在 `man` 页面里：

| 按键 | 作用 |
| --- | --- |
| `q` | 退出 |
| `/关键词` | 搜索 |
| `n` | 下一个搜索结果 |
| `空格` | 下一页 |
| `b` | 上一页 |

### `info`
有些 GNU 工具文档更详细：
```bash
info coreutils
```
### `tldr`
如果安装了 `tldr`，可以看简短例子：
```bash
tldr tar
tldr grep
```
## 8. 命令历史
查看历史命令：
```bash
history
```
查看最近 20 条：
```bash
history | tail -20
```
重复执行上一条命令：
```bash
!!
```
搜索历史命令：
```text
Ctrl + R
```
然后输入关键词，例如：
```text
gcc
```
## 9. 引号和空格
路径或文件名里有空格时，需要加引号或转义。
推荐写法：
```bash
cat "my file.txt"
```
也可以写：
```bash
cat my\ file.txt
```
单引号和双引号的区别：
```bash
name="Linux"
echo "$name"
echo '$name'
```
输出：
```text
Linux
$name
```
双引号会展开变量，单引号不会。
## 10. 管道和重定向
### 管道 `|`
把前一个命令的输出交给后一个命令：
```bash
ps aux | grep bash
```
含义：
```text
ps aux      列出所有进程
|           把输出传给后面的命令
grep bash   只保留包含 bash 的行
```
### 输出重定向 `>`
写入文件，覆盖原内容：
```bash
echo "hello" > file.txt
```
### 追加重定向 `>>`
追加到文件末尾：
```bash
echo "world" >> file.txt
```
### 输入重定向 `<`
从文件读取输入：
```bash
sort < names.txt
```
## 11. 常见错误
### `command not found`
说明命令不存在，或不在 `PATH` 中。
排查：
```bash
which 命令名
type 命令名
echo $PATH
```
### `Permission denied`
说明没有权限。
如果是脚本不能执行：
```bash
chmod +x script.sh
./script.sh
```
如果是系统目录不能写，先确认是否真的需要 `sudo`。
### `No such file or directory`
说明路径写错，或当前目录不是你以为的目录。
排查：
```bash
pwd
ls -lah
```
