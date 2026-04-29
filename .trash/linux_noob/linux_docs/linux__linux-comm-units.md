# Linux units 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

units 是 Linux 系统中一个强大的单位转换工具，它能够处理各种物理量之间的转换，包括长度、重量、温度、速度、时间等。这个命令行工具特别适合工程师、科学家和需要进行复杂单位换算的技术人员使用。

units 命令的特点：

  * 支持超过 3000 种单位的转换
  * 可以进行复合单位的计算（如将瓦特小时转换为焦耳）
  * 允许用户自定义单位
  * 提供交互式和命令行两种使用模式



* * *

## 安装 units 命令

大多数 Linux 发行版默认不安装 units，需要手动安装：

## 实例

```bash
# Debian/Ubuntu 系统 sudo apt-get install units # CentOS/RHEL 系统 sudo yum install units # Fedora 系统 sudo dnf install units # Arch Linux 系统 sudo pacman -S units
```


安装完成后，可以通过以下命令验证是否安装成功：

```bash
units --version
```


* * *

## 基本使用方法

units 命令有两种主要使用模式：交互式和非交互式。

### 交互式模式

直接输入 `units` 命令进入交互式模式：

## 实例

```bash
$ units 2861 units, 109 prefixes, 109 nonlinear units You have:
```


在提示符后输入要转换的单位，例如：

```bash
You have: 1 mile You want: km * 1.609344 / 0.62137119
```


输出结果中：

  * `*` 后面的数字表示乘法因子（1 英里 = 1.609344 公里）
  * `/` 后面的数字表示倒数因子（1 公里 = 0.62137119 英里）



### 非交互式模式

可以直接在命令行中完成转换：

```bash
units "1 mile" "km"
```


输出结果与交互式模式相同。

* * *

## 常用单位转换示例

### 长度单位转换

## 实例

```bash
# 英寸转厘米 $ units "12 inch" "cm" * 30.48 / 0.032808399 # 英尺转米 $ units "6 feet" "meters" * 1.8288 / 0.54680665
```


### 温度单位转换

## 实例

```bash
# 华氏度转摄氏度 $ units "98.6 degF" "degC" * 37 / 0.027027027 # 开尔文转摄氏度 $ units "300 K" "degC" * 26.85 / 0.037243908
```


### 速度单位转换

## 实例

```bash
# 英里/小时转公里/小时 $ units "60 mph" "kph" * 96.56064 / 0.010356187 # 节转米/秒 $ units "15 knots" "m/s" * 7.7166667 / 0.12958963
```


### 数据存储单位转换

## 实例

```bash
# 吉字节转兆字节 $ units "1 gibibyte" "megabyte" * 1073.7418 / 0.00093132257 # 注意：units 默认使用二进制前缀(1024为基数) # 如果要使用十进制前缀(1000为基数)，使用 'megabytes' 而不是 'megabyte'
```


* * *

## 高级功能

### 复合单位转换

units 可以处理复杂的复合单位：

## 实例

```bash
# 将千瓦时转换为焦耳 $ units "1 kWh" "joules" * 3600000 / 2.7777778e-07 # 将磅力每平方英寸转换为帕斯卡 $ units "1 psi" "pascal" * 6894.7573 / 0.00014503774
```


### 自定义单位

可以在 `~/.units` 文件中定义自己的单位。例如，添加一个"足球场"单位：

```bash
footballfield 100 m
```


然后就可以使用：

## 实例

```bash
$ units "1 footballfield" "km" * 0.1 / 10
```


### 货币转换（需要联网）

units 支持货币转换，但需要联网获取最新汇率：

```bash
$ units "100 USD" "EUR"
```


注意：货币转换功能可能在某些系统中不可用或需要额外配置。

* * *

## 实用技巧

  1. **查看可用单位列表** ：在交互模式下输入 `?` 或 `help` 可以查看帮助信息

  2. **模糊搜索** ：输入部分单位名称后按 Tab 键可以自动补全

  3. **历史记录** ：在交互模式下可以使用上下箭头查看历史命令

  4. **精确控制输出** ：使用 `-v` 参数显示更详细的信息


```bash
units -v "1 lightyear" "km"
```

  5. **检查单位兼容性** ：使用 `-c` 参数只检查单位是否兼容而不进行转换

```bash
units -c "joules" "watt hours"
```


* * *

## 常见问题解答

### 为什么某些单位转换结果不准确？

units 使用预定义的单位数据库，某些转换（特别是货币）可能有精度限制或使用近似值。对于精确的科学计算，建议查阅专业参考资料。

### 如何更新单位数据库？

单位数据库通常位于 `/usr/share/units/definitions.units`。可以手动编辑这个文件或等待系统更新。

### 能否进行批量转换？

可以编写 shell 脚本结合 units 命令实现批量转换：

## 实例

```bash
#!/bin/bash for value in 1 2 5 10 ; do result =$ ( units " $value feet" "meters" | awk 'NR==1 {print $2}' ) echo " $value feet = $result meters" done
```


* * *

## 总结

units 命令是 Linux 系统中一个强大而灵活的单位转换工具，适用于各种科学、工程和日常计算场景。通过本文的介绍，你应该已经掌握了：

  1. units 命令的基本安装和使用方法
  2. 常见物理量的单位转换技巧
  3. 高级功能如复合单位转换和自定义单位
  4. 实际应用中的实用技巧和问题解决方法



要深入了解 units 命令的更多功能，可以查阅其手册页：

```bash
man units
```


现在，尝试用 units 命令解决你遇到的下一个单位转换问题吧！

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
