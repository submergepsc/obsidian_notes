# Linux printf 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 一、printf 命令概述

printf 是 Linux/Unix 系统中一个强大的格式化输出命令，它源自 C 语言中的 printf() 函数。与 echo 命令相比，printf 提供了更精确的输出控制和格式化能力。

### 主要特点

  * **精确格式化** ：可以控制输出的对齐方式、宽度、精度等
  * **不自动换行** ：默认不会在输出末尾添加换行符（与 echo 不同）
  * **多语言支持** ：支持 Unicode 字符输出
  * **变量插入** ：可以在字符串中插入变量值



* * *

## 二、基本语法

```bash
printf format-string [arguments...]
```


### 参数说明

  * **format-string** ：格式字符串，包含普通字符和格式说明符
  * **arguments** ：与格式说明符对应的参数列表



* * *

## 三、格式说明符详解

格式说明符以 `%` 开头，基本形式为：

```bash
%[flags][width][.precision]specifier
```


### 常用格式说明符

说明符 | 描述 | 示例  
---|---|---  
%s | 字符串 | printf "%s" "hello"  
%d | 十进制整数 | printf "%d" 123  
%f | 浮点数 | printf "%f" 3.14  
%x | 十六进制整数(小写) | printf "%x" 255  
%X | 十六进制整数(大写) | printf "%X" 255  
%o | 八进制整数 | printf "%o" 8  
%c | 单个字符 | printf "%c" 65  
  
### 修饰符选项

#### 1\. 标志(flags)

标志 | 描述 | 示例  
---|---|---  
- | 左对齐 | printf "%-10s" "hi"  
+ | 显示正负号 | printf "%+d" 123  
0 | 用零填充 | printf "%05d" 12  
空格 | 正数前留空格 | printf "% d" 123  
# | 特殊格式(如0x前缀) | printf "%#x" 255  
  
#### 2\. 宽度(width)

指定最小字段宽度，不足时填充

## 实例

```bash
printf "%10s \n " "hello" # 右对齐，宽度10 printf "%-10s \n " "hello" # 左对齐，宽度10
```


#### 3\. 精度(.precision)

对于浮点数，指定小数点后位数；对于字符串，指定最大字符数

## 实例

```bash
printf "%.2f \n " 3.14159 # 输出 3.14 printf "%.5s \n " "abcdefg" # 输出 abcde
```


* * *

## 四、实用示例

### 示例1：基本格式化输出

## 实例

```bash
printf "Name: %s, Age: %d, Height: %.2f \n " "Alice" 25 1.68
```


输出：

```bash
Name: Alice, Age: 25, Height: 1.68
```


### 示例2：表格对齐输出

## 实例

```bash
printf "%-10s %-10s %-10s \n " "Name" "Age" "Score" printf "%-10s %-10d %-10.2f \n " "Alice" 25 89.5 printf "%-10s %-10d %-10.2f \n " "Bob" 23 92.3
```


输出：

```bash
Name Age Score Alice 25 89.50 Bob 23 92.30
```


### 示例3：特殊字符处理

## 实例

```bash
printf "Temperature: %d°C \n " 25 printf "Path: %s \n " "/home/user" printf "Alert: \a \n " # 响铃字符
```


### 示例4：变量插入

## 实例

```bash
name = "John" age = 30 printf "User: %s, %d years old \n " " $name " " $age "
```


* * *

## 五、高级用法

### 1\. 格式化日期输出

## 实例

```bash
printf "Today is %(%Y-%m-%d)T \n " -1
```


### 2\. 颜色输出

## 实例

```bash
printf "\e[31mRed Text\e[0m \n " printf "\e[32mGreen Text\e[0m \n "
```


### 3\. 动态指定宽度

## 实例

```bash
width = 20 printf "%*s \n " $width "Right aligned"
```


* * *

## 六、常见问题与注意事项

**换行问题** ：printf 默认不添加换行符，需要手动添加 `\n`

## 实例

```bash
printf "No newline" printf "Add newline \n "
```


**参数数量不匹配** ：当参数少于格式说明符时，会输出未定义值

## 实例

```bash
printf "%s %s \n " "only_one" # 第二个%s会输出空
```


**引号处理** ：建议将格式字符串用双引号括起来，变量也用双引号

## 实例

```bash
printf "%s \n " " $variable "
```


**特殊字符转义** ：需要在格式字符串中使用反斜杠转义特殊字符

* * *

## 七、printf vs echo

特性 | printf | echo  
---|---|---  
换行 | 需显式添加\n | 自动添加  
格式化 | 支持复杂格式化 | 简单输出  
一致性 | 各系统行为一致 | 不同系统可能有差异  
变量扩展 | 需要显式指定 | 自动扩展  
特殊字符 | 需要转义 | 部分版本支持-e选项  
  
[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
