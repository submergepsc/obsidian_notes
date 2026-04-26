# Shell test 命令

`test` 命令是 Shell 内置的条件判断工具，用于评估表达式并返回布尔值（真/假），它通常与 `if` 语句结合使用，是 Shell 脚本中实现逻辑控制的基础。

Shell 中的 test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。

### 语法格式

```bash
test EXPRESSION # 或 [ EXPRESSION ] # 注意方括号内必须有空格
```


* * *

## 文件测试操作

`test` 命令最常用于检查文件属性，以下是常用文件测试选项：

操作符 | 描述 | 示例  
---|---|---  
-e | 文件是否存在 | `[ -e file.txt ]`  
-f | 是普通文件 | `[ -f /path/to/file ]`  
-d | 是目录 | `[ -d /path/to/dir ]`  
-r | 可读 | `[ -r file.txt ]`  
-w | 可写 | `[ -w file.txt ]`  
-x | 可执行 | `[ -x script.sh ]`  
-s | 文件大小 >0 | `[ -s logfile ]`  
-L | 是符号链接 | `[ -L symlink ]`  
  
**示例脚本** ：

## 实例

```bash
#!/bin/bash file = "/etc/passwd" if [ -e " $file " ] ; then echo " $file 存在" if [ -r " $file " ] ; then echo "并且可读" fi else echo " $file 不存在" fi
```


输出结果为：

```bash
/etc/passwd 存在 并且可读
```


* * *

## 字符串比较

`test` 提供了多种字符串比较方式：

操作符 | 描述 | 示例  
---|---|---  
-z STRING | 字符串为空 | `[ -z "$var" ]`  
-n STRING | 字符串非空 | `[ -n "$var" ]`  
STRING1 = STRING2 | 字符串相等 | `[ "$var1" = "$var2" ]`  
STRING1 != STRING2 | 字符串不等 | `[ "$var1" != "$var2" ]`  
  
**重要提示** ：字符串变量应该总是用双引号括起来，防止空变量导致语法错误。

**示例** ：

## 实例

```bash
#!/bin/bash read -p "输入用户名: " username if [ -z " $username " ] ; then echo "错误：用户名不能为空" exit 1 elif [ " $username " = "root" ] ; then echo "警告：不建议使用root账户" else echo "欢迎, $username " fi
```


执行后，我们在终端输入 runoob，输出结果类似如下：

```bash
输入用户名: runoob 欢迎, runoob
```


* * *

## 数值比较

对于数值比较，`test` 使用不同的操作符：

操作符 | 描述 | 示例  
---|---|---  
-eq | 等于 | `[ "$a" -eq "$b" ]`  
-ne | 不等于 | `[ "$a" -ne "$b" ]`  
-gt | 大于 | `[ "$a" -gt "$b" ]`  
-ge | 大于或等于 | `[ "$a" -ge "$b" ]`  
-lt | 小于 | `[ "$a" -lt "$b" ]`  
-le | 小于或等于 | `[ "$a" -le "$b" ]`  
  
**示例** ：

## 实例

```bash
#!/bin/bash read -p "输入年龄: " age if [ " $age " -lt 0 ] ; then echo "年龄不能为负数" elif [ " $age " -lt 18 ] ; then echo "未成年人" elif [ " $age " -ge 18 ] && [ " $age " -lt 60 ] ; then echo "成年人" else echo "老年人" fi
```


执行后，我们在终端输入 12，输出结果类似如下：

```bash
输入年龄: 12 未成年人
```


* * *

## 逻辑操作符

`test` 支持逻辑组合：

操作符 | 描述 | 示例  
---|---|---  
! | 逻辑非 | `[ ! -f "$file" ]`  
-a | 逻辑与 | `[ "$a" -eq 1 -a "$b" -eq 2 ]`  
-o | 逻辑或 | `[ "$a" -eq 1 -o "$b" -eq 2 ]`  
  
**现代推荐写法** ：使用 `&&` 和 `||` 替代 `-a` 和 `-o`，更符合 POSIX 标准：

## 实例

```bash
[ " $a " -eq 1 ] && [ " $b " -eq 2 ] # 与 [ " $a " -eq 1 ] || [ " $b " -eq 2 ] # 或
```


* * *

## 高级用法：[[ ]] 和 (( ))

Bash 提供了更强大的测试语法：

### 双括号 [[ ]]

  * 支持模式匹配：`[[ "$var" == *.txt ]]`
  * 支持正则表达式：`[[ "$var" =~ ^[0-9]+$ ]]`
  * 更安全的字符串处理



### 算术比较 (( ))

  * 专为数值比较设计：`(( a > b ))`
  * 支持更复杂的算术表达式



**示例** ：

## 实例

```bash
if [ [ " $file " == * .log ] ] ; then echo "这是日志文件" fi if ( ( $count > 10 ) ) ; then echo "数量超过10" fi
```


* * *

## 实际应用示例

### 1\. 检查服务是否运行

## 实例

```bash
#!/bin/bash service = "nginx" if systemctl is-active \--quiet " $service " ; then echo " $service 正在运行" else echo " $service 未运行" # 可以添加启动服务的命令 fi
```


### 2\. 备份文件检查

## 实例

```bash
#!/bin/bash backup_file = "/backups/data_ $(date +%Y%m%d) .tar.gz" if [ ! -f " $backup_file " ] ; then echo "错误：备份文件 $backup_file 不存在" exit 1 elif [ ! -s " $backup_file " ] ; then echo "警告：备份文件为空" else echo "备份验证成功" fi
```


* * *

## 常见错误与调试技巧

  1. **缺少空格** ：`[ "$a"="$b" ]` 是错误的，正确是 `[ "$a" = "$b" ]`
  2. **未引用的变量** ：`[ -f $file ]` 应该为 `[ -f "$file" ]`
  3. **混淆字符串和数值比较** ：使用 `=` 比较字符串，`-eq` 比较数值



调试技巧：在脚本开头添加 `set -x` 开启调试模式，或使用 `echo` 打印测试表达式：

## 实例

```bash
echo "测试表达式: [ $a -eq $b ]" [ " $a " -eq " $b " ] && echo "成立" || echo "不成立"
```
