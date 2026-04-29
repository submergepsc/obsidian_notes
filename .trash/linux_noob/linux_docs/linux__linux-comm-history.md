# Linux history 命令完全指南

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

history 是 Linux 系统中一个极其有用的内置命令，它记录了用户在终端中执行过的所有命令历史。这个功能对于以下场景特别有价值：

  1. **追溯操作** ：查看之前执行过的命令
  2. **快速重用** ：无需重新输入长命令
  3. **问题排查** ：检查系统操作记录
  4. **效率提升** ：通过历史命令快速完成重复工作



当你在终端输入命令时，Bash 会将这些命令保存在内存中，并在退出时写入到 `~/.bash_history` 文件中（默认配置下）。

* * *

## 基本语法和使用

history 命令的基本语法非常简单：

```bash
history [选项] [参数]
```


### 常用形式

1、查看完整历史记录：

```bash
history
```


2、查看最近 N 条记录：

```bash
history 10 # 显示最近10条命令
```


3、清除所有历史记录：

```bash
history -c
```


4、删除特定历史记录（例如删除第1010条）：

```bash
history -d 1010
```


* * *

## 常用选项参数详解

history 命令支持多个实用选项：

选项 | 说明 | 示例  
---|---|---  
`-c` | 清除所有历史记录 | `history -c`  
`-d` | 删除指定位置的历史记录 | `history -d 1005`  
`-a` | 立即将内存中的历史写入历史文件 | `history -a`  
`-n` | 从历史文件中读取未读的历史记录 | `history -n`  
`-r` | 读取历史文件内容到当前会话 | `history -r`  
`-w` | 将当前历史记录写入历史文件 | `history -w`  
  
* * *

## 实用技巧和高级用法

### 1\. 快速执行历史命令

## 实例

```bash
! n # 执行历史记录中第n条命令 !! # 执行上一条命令 ! string # 执行最近一条以string开头的命令
```


示例：

## 实例

```bash
! 1024 # 执行历史记录中编号为1024的命令 !! # 重新执行上一条命令 ! vim # 执行最近一条以vim开头的命令
```


### 2\. 搜索历史命令

使用 `Ctrl+R` 可以反向搜索历史命令，输入部分关键词即可找到匹配的命令。

### 3\. 历史命令替换

## 实例

```bash
^old^new # 将上一条命令中的old替换为new后执行
```


示例：

## 实例

```bash
$ cat file1.txt $ ^file1^file2 # 相当于执行 cat file2.txt
```


### 4\. 显示命令时间戳

在 `~/.bashrc` 中添加以下配置可以显示命令执行时间：

## 实例

```bash
export HISTTIMEFORMAT = "%F %T "
```


然后执行：

## 实例

```bash
source ~ / .bashrc
```


之后 `history` 命令会显示每条命令的执行时间。

* * *

## 环境变量配置

通过环境变量可以自定义 history 命令的行为：

变量 | 说明 | 推荐值  
---|---|---  
`HISTSIZE` | 内存中保存的历史命令数量 | `5000`  
`HISTFILESIZE` | 历史文件中保存的命令数量 | `10000`  
`HISTCONTROL` | 控制历史记录方式 | `ignoredups:erasedups`  
`HISTIGNORE` | 指定不记录的命令 | `"ls:cd:pwd:exit"`  
  
配置示例（添加到 `~/.bashrc`）：

## 实例

```bash
export HISTSIZE = 5000 export HISTFILESIZE = 10000 export HISTCONTROL =ignoredups:erasedups export HISTIGNORE = "ls:cd:pwd:exit" export HISTTIMEFORMAT = "%F %T "
```


* * *

## 实际应用场景

### 场景1：找回忘记的命令

## 实例

```bash
history | grep "apt install"
```


### 场景2：统计最常用命令

## 实例

```bash
history | awk '{CMD[$2]++;count++;} END {for (a in CMD)print CMD[a] " " CMD[a]/count*100 "% " a;}' | grep -v "./" | column -c3 -s " " -t | sort -nr | nl | head -n10
```


### 场景3：备份历史记录

## 实例

```bash
history -a # 确保最新命令已写入文件 cp ~ / .bash_history ~ / command_history_backup_$ ( date \+ % F ) .txt
```


* * *

## 注意事项

  1. **隐私安全** ：历史记录可能包含敏感信息（如密码），注意保护
  2. **多终端问题** ：不同终端会话默认不会实时共享历史记录
  3. **历史记录丢失** ：异常退出可能导致命令未保存
  4. **大文件处理** ：过大的历史文件可能影响性能



* * *

## 总结练习

  1. 查看你的命令历史，找出最近使用的5条git命令

```bash
history | grep git | tail -5
```

  2. 配置你的bash环境，使历史记录包含时间戳并忽略重复命令

  3. 创建一个别名，快速备份当前历史记录到指定目录

```bash
alias backup_history='cp ~/.bash_history ~/history_backups/history_$(date +%Y%m%d_%H%M%S).txt'
```

  4. 尝试使用 `Ctrl+R` 搜索你之前用过的某个复杂命令




通过掌握 history 命令，你可以显著提高在 Linux 终端的工作效率，减少重复输入，并更好地管理你的命令行操作历史。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
