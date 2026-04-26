# Linux test 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

`test` 是 Linux/Unix 系统中一个用于条件判断的内置命令，主要用于 shell 脚本中进行各种测试和比较操作。它可以检查文件属性、比较字符串和数值，是编写 shell 脚本时不可或缺的工具。

* * *

## 基本语法

```bash
test EXPRESSION # 或者使用方括号格式（更常用） [ EXPRESSION ]
```


> **注意** ：使用方括号格式时，表达式与方括号之间必须有空格，即 `[空格EXPRESSION空格]`

* * *

## 主要功能分类

### 1\. 文件测试

检查文件或目录的各种属性：

表达式 | 含义  
---|---  
`-e 文件` | 文件是否存在  
`-f 文件` | 是普通文件（不是目录或设备文件）  
`-d 文件` | 是目录  
`-s 文件` | 文件大小不为空  
`-r 文件` | 文件可读  
`-w 文件` | 文件可写  
`-x 文件` | 文件可执行  
`-L 文件` | 文件是符号链接  
  
**示例** ：

## 实例

```bash
if [ -f "/etc/passwd" ] ; then echo "这是一个普通文件" fi
```


* * *

### 2\. 字符串比较

比较两个字符串的关系：

表达式 | 含义  
---|---  
`-z "字符串"` | 字符串长度为0  
`-n "字符串"` | 字符串长度不为0  
`"串1" = "串2"` | 字符串相等  
`"串1" != "串2"` | 字符串不相等  
  
**示例** ：

## 实例

```bash
read -p "输入用户名: " username if [ -z " $username " ] ; then echo "用户名不能为空" fi
```


* * *

### 3\. 数值比较

比较两个整数的大小关系：

表达式 | 含义  
---|---  
`n1 -eq n2` | 等于 (equal)  
`n1 -ne n2` | 不等于 (not equal)  
`n1 -gt n2` | 大于 (greater than)  
`n1 -ge n2` | 大于等于  
`n1 -lt n2` | 小于 (less than)  
`n1 -le n2` | 小于等于  
  
**示例** ：

## 实例

```bash
if [ $ ( id -u ) -eq 0 ] ; then echo "当前是root用户" fi
```


* * *

### 4\. 逻辑运算符

组合多个测试条件：

运算符 | 含义 | 示例  
---|---|---  
`!` | 逻辑非 | `[ ! -f file ]`  
`-a` | 逻辑与 | `[ -f file -a -r file ]`  
`-o` | 逻辑或 | `[ -d dir -o -f file ]`  
  
**现代推荐写法** （使用 `&&` 和 `||`）：

## 实例

```bash
[ -f file ] && [ -r file ] # 文件存在且可读 [ -d dir ] || [ -f file ] # 是目录或者是文件
```


* * *

## 高级用法

### 1\. 复合条件判断

## 实例

```bash
if [ -f "/etc/passwd" -a -r "/etc/passwd" ] ; then echo "文件存在且可读" fi
```


### 2\. 与 if 语句结合

## 实例

```bash
if [ "$1" = "start" ] ; then echo "启动服务..." elif [ "$1" = "stop" ] ; then echo "停止服务..." else echo "无效参数" fi
```


### 3\. 在变量赋值中使用

## 实例

```bash
[ -z " $PATH " ] && PATH = "/usr/bin:/bin" # 如果PATH为空则设置默认值
```


* * *

## 常见错误与注意事项

**空格问题** ：

## 实例

```bash
[ " $var " = "value" ] # 正确 [ " $var " = "value" ] # 错误，缺少空格
```


**字符串变量引号** ：

## 实例

```bash
[ -n " $var " ] # 正确，防止变量为空时报错 [ -n $var ] # 当$var为空时会报错
```


**数值比较与字符串比较** ：

## 实例

```bash
[ "10" -gt "2" ] # 正确，数值比较 [ "10" > "2" ] # 错误，这是字符串比较（按字典序）
```


**文件测试路径** ：

## 实例

```bash
[ -f " $file " ] # 正确，变量用引号包裹 [ -f $file ] # 当路径含空格时会出错
```


* * *

## 实际应用示例

### 示例1：检查备份目录是否存在

## 实例

```bash
backup_dir = "/var/backups" if [ ! -d " $backup_dir " ] ; then mkdir -p " $backup_dir " echo "创建备份目录: $backup_dir " fi
```


### 示例2：验证用户输入

## 实例

```bash
read -p "请输入年龄: " age if [ " $age " -lt 0 -o " $age " -gt 120 ] ; then echo "无效的年龄输入" exit 1 fi
```


### 示例3：服务启动脚本

## 实例

```bash
#!/bin/bash if [ "$1" = "start" ] ; then if [ -f "/var/run/service.pid" ] ; then echo "服务已在运行" else echo "启动服务..." # 启动命令 fi elif [ "$1" = "stop" ] ; then # 停止逻辑 else echo "用法: $0 {start|stop}" fi
```


* * *

## 总结

`test` 命令是 shell 脚本编程中的基础工具，掌握它可以：

  * 实现条件分支逻辑
  * 验证文件和目录状态
  * 比较字符串和数值
  * 构建复杂的判断条件



记住关键点：

  1. 方括号格式更常用但要注意空格
  2. 变量引用要加双引号
  3. 区分字符串比较和数值比较运算符
  4. 使用现代 `&&` 和 `||` 替代 `-a` 和 `-o`



[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
