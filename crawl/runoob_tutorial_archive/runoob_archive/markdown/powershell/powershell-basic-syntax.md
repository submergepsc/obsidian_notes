# PowerShell 基本语法

- Source: https://www.runoob.com/powershell/powershell-basic-syntax.html

PowerShell 不只是一个命令行工具，它还是一个完整的脚本语言。学习它的基本语法，就像学习一门新的编程语言一样，是入门的重要一步。


本节将详细介绍 PowerShell 中最基本的语法元素，包括变量、注释、数据类型、运算符、条件判断、循环结构等内容，为后续编写脚本打下扎实基础。


---


## 一、注释


PowerShell 中的注释与大多数编程语言相似，用于解释代码，不会被执行。


单行注释使用 **#** 开头：


```
# 这是一个单行注释
Write-Output "Hello, PowerShell"
```


多行注释使用 **** 包裹：


```
<#
这是多行注释
可用于文档说明
#>
```


---


## 二、变量


### 定义变量


PowerShell 中变量以 **`$` 符号开头**，无需事先声明类型：


```
$name = "Alice"
$age = 25
```


### 使用变量


```
Write-Output "Name: $name"
```


也可以使用字符串插值：


```
Write-Output "User: $($name), Age: $($age)"
```


---


## 三、数据类型


PowerShell 是弱类型语言，但变量背后都有对应的 .NET 类型。


| 类型 | 示例 |
| --- | --- |
| 字符串 | $str = "Hello" |
| 整数 | $num = 123 |
| 小数 | $pi = 3.14 |
| 布尔值 | $isTrue = $true |
| 数组 | $arr = @(1, 2, 3) |
| 哈希表 | $h = @{Name="Tom"; Age=30} |


可以使用 `.GetType()` 查看变量类型：


```
$str.GetType().Name   # String
```


---


## 四、运算符


| 类别 | 示例 | 说明 |
| --- | --- | --- |
| 算术运算 | + - * / % | 常见数学运算 |
| 比较运算 | -eq -ne -lt -gt | 等于、不等于、小于、大于 |
| 逻辑运算 | -and -or -not | 逻辑运算符 |
| 字符串 | -like -match -replace | 模式匹配和替换 |
| 包含运算 | -in -contains | 集合判断 |


示例：


```
5 -eq 5       # True
"abc" -like "a*"  # True
```


---


## 五、条件判断


### if 语句


```
if ($age -ge 18) {
    Write-Output "成年人"
} else {
    Write-Output "未成年人"
}
```


### if-elseif-else


```
if ($score -ge 90) {
    "优秀"
} elseif ($score -ge 60) {
    "及格"
} else {
    "不及格"
}
```


---


## 六、循环结构


### for 循环


```
for ($i = 1; $i -le 5; $i++) {
    Write-Output "第 $i 次循环"
}
```


### foreach 循环


```
$colors = @("Red", "Green", "Blue")
foreach ($color in $colors) {
    Write-Output "颜色：$color"
}
```


### while 循环


```
$count = 0
while ($count -lt 3) {
    Write-Output $count
    $count++
}
```


---


## 七、函数定义


PowerShell 允许自定义函数，语法如下：


```
function Say-Hello {
    param([string]$name)
    Write-Output "Hello, $name!"
}

Say-Hello -name "PowerShell"
```


也可以使用简洁写法：


```
function Square($x) { return $x * $x }
Square 5  # 输出 25
```


---


## 八、错误处理


使用 `try {}` `catch {}` 块来处理可能出错的语句：


```
try {
    Get-Item "C:\NotExist.txt"
} catch {
    Write-Output "找不到文件"
}
```


---


## 九、脚本文件基本格式


PowerShell 脚本文件使用 `.ps1` 后缀名。可以使用 VS Code 或记事本创建：


```
# hello.ps1
$name = "World"
Write-Output "Hello, $name"
```


在 PowerShell 中运行：


```
.\hello.ps1
```


**

注意：如果脚本未能执行，请检查执行策略（`Get-ExecutionPolicy`），必要时使用 `Set-ExecutionPolicy` 允许运行脚本。










	  AI 思考中...





			** [PowerShell Cmdlet 基础](https://www.runoob.com/powershell-cmdlet.html)
			[Cmdlet 文件系统操作](https://www.runoob.com/cmdlet-file-system-operations.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/../skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/../skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/../skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/../skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/../skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/../skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/../skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)

      : · [免责声明](https://www.runoob.com/../disclaimer/index.html)

      : · [关于我们](https://www.runoob.com/../aboutus/index.html)

      : · [文章归档](https://www.runoob.com/../archives/index.html)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/../index/index.html)**
    **[runoob.com](https://www.runoob.com/../index/index.html)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **