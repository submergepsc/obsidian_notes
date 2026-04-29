# Linux env 命令完全指南

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

env 是 Linux/Unix 系统中一个非常实用的命令行工具，主要用于显示和修改环境变量，以及在自定义环境中运行程序。

环境变量是操作系统或用户设置的动态值，它们会影响运行中进程的行为。env 命令为我们提供了查看和操作这些变量的便捷方式。

类比理解：可以把环境变量想象成办公室里的公告板，所有工作人员(程序)都能看到上面的信息(环境变量)，并根据这些信息调整自己的工作方式。

* * *

## env 命令的基本语法

env 命令的基本语法格式如下：

```bash
env [OPTION]... [NAME=VALUE]... [COMMAND [ARG]...]
```


如果不带任何参数直接运行 `env`，它会显示当前所有的环境变量及其值。

* * *

## 常用选项参数

env 命令支持以下常用选项：

选项 | 说明  
---|---  
`-i`, `--ignore-environment` | 从一个空环境开始，忽略继承的环境变量  
`-u`, `--unset=NAME` | 从环境中移除指定的变量  
`-C`, `--chdir=DIR` | 在运行命令前切换到指定目录  
`-S`, `--split-string=S` | 将参数拆分为多个参数  
`--help` | 显示帮助信息  
`--version` | 显示版本信息  
  
* * *

## 基本用法示例

### 1\. 查看所有环境变量

最简单的用法是直接输入 `env` 命令：

## 实例

```bash
env
```


这会输出当前 shell 中的所有环境变量，格式为 `变量名=值`，例如：

```bash
USER=john HOME=/home/john PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```


### 2\. 在自定义环境中运行命令

可以临时设置环境变量来运行程序：

## 实例

```bash
env LANG =C ls
```


这个例子中，我们临时设置 `LANG=C` 然后运行 `ls` 命令，这会影响 `ls` 命令的输出语言。

### 3\. 创建干净的环境运行程序

使用 `-i` 选项可以创建一个干净的环境（不继承任何现有环境变量）：

## 实例

```bash
env -i PATH = / bin: / usr / bin ls
```


这里我们创建了一个只有 `PATH` 变量的干净环境来运行 `ls` 命令。

* * *

## 高级用法

### 1\. 临时修改变量运行脚本

## 实例

```bash
env EDITOR = nano crontab -e
```


这个命令会临时将 `EDITOR` 环境变量设置为 `nano`，然后运行 `crontab -e`，这样就会使用 nano 编辑器来编辑 crontab。

### 2\. 移除特定环境变量

## 实例

```bash
env -u HOME ls
```


这个命令会在运行 `ls` 时移除 `HOME` 环境变量。

### 3\. 结合 shebang 使用

env 常用于脚本的 shebang 行，使脚本更具可移植性：

## 实例

```bash
#!/usr/bin/env bash
```


这种写法比直接指定 `/bin/bash` 更灵活，因为它会在 `PATH` 环境变量中查找 bash 的位置。

* * *

## 实际应用场景

### 1\. 调试环境变量问题

当程序行为异常时，可以用 env 检查它运行时的环境：

## 实例

```bash
env -i / path / to / program
```


这样可以排除环境变量干扰，判断是否是环境变量导致的问题。

### 2\. 安全运行不受信任的脚本

运行来源不明的脚本时，可以创建一个受限环境：

## 实例

```bash
env -i PATH = / bin: / usr / bin / path / to / script.sh
```


### 3\. 测试不同语言环境下的程序行为

## 实例

```bash
env LANG =fr_FR.UTF- 8 program env LANG =zh_CN.UTF- 8 program
```


这样可以测试程序在不同语言环境下的表现。

* * *

## 注意事项

  1. **变量覆盖** ：通过 env 设置的变量会覆盖已有的同名环境变量
  2. **子进程影响** ：env 修改的环境变量只影响它启动的子进程，不会影响当前 shell
  3. **安全性** ：敏感信息（如密码）不应通过环境变量传递
  4. **变量顺序** ：后面设置的变量会覆盖前面设置的同名变量



[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
