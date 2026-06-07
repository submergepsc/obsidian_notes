# PowerShell 控制结构

- Source: https://www.runoob.com/powershell/powershell-control-structures.html

控制结构是程序的"大脑"，决定代码在什么条件下执行、是否重复执行，以及如何优雅地处理错误。


PowerShell 作为现代脚本语言，提供了完整的流程控制语法，包括：


- 条件语句：`if`、`elseif`、`else`、`switch`
- 循环结构：`for`、`foreach`、`while`、`do-while`
- 错误处理机制：`try`-`catch`-`finally`


---


## 一、条件语句


### if / elseif / else


基本语法：


```
if (条件1) {
    # 条件1为真执行
} elseif (条件2) {
    # 条件2为真执行
} else {
    # 其他情况
}
```


#### 示例：判断磁盘空间是否不足


```
$disk = Get-PSDrive C
if ($disk.Free -lt 5GB) {
    Write-Output "磁盘空间不足！"
} elseif ($disk.Free -lt 10GB) {
    Write-Output "磁盘空间偏低。"
} else {
    Write-Output "磁盘空间充足。"
}
```


### switch


当有多个可能值要判断时，`switch` 比多个 `if` 更清晰。


```
switch ($value) {
    "start" { Write-Output "开始任务" }
    "stop"  { Write-Output "停止任务" }
    "exit"  { Write-Output "退出程序" }
    default { Write-Output "未知命令" }
}
```


支持匹配模式：


```
switch -Wildcard ($filename) {
    "*.txt" { "文本文件" }
    "*.jpg" { "图片文件" }
    default { "其他类型" }
}
```


---


## 二、循环结构


### for 循环（经典计数循环）


```
for ($i = 1; $i -le 5; $i++) {
    Write-Output "第 $i 次"
}
```


### foreach 循环（遍历集合）


```
$names = "张三", "李四", "王五"
foreach ($name in $names) {
    Write-Output "你好，$name"
}
```


也可使用 `ForEach-Object` 管道版本：


```
$names | ForEach-Object { Write-Output "你好，$_" }
```


### while 循环（条件为真执行）


```
$count = 0
while ($count -lt 3) {
    Write-Output "计数：$count"
    $count++
}
```


### do-while 与 do-until


`do` 循环会 **至少执行一次**：


```
$count = 0
do {
    Write-Output "当前值：$count"
    $count++
} while ($count -lt 3)
```


`do-until`：直到条件为真才停止


```
$count = 0
do {
    Write-Output "当前值：$count"
    $count++
} until ($count -ge 3)
```


---


## 三、错误处理：try / catch / finally


PowerShell 提供结构化异常处理机制，用于捕获和响应运行时错误。


### 3.1 基本结构


```
try {
    # 尝试运行可能出错的代码
}
catch {
    # 错误时执行
}
finally {
    # 无论是否出错，都会执行（可选）
}
```


### 示例：处理除零错误


```
try {
    $result = 10 / 0
}
catch {
    Write-Output "发生错误：$($_.Exception.Message)"
}
finally {
    Write-Output "运算结束"
}
```


### 捕获特定异常类型


```
try {
    Get-Content "不存在的文件.txt"
}
catch [System.IO.FileNotFoundException] {
    Write-Output "文件未找到！"
}
catch {
    Write-Output "其他错误：$($_.Exception.Message)"
}
```









	  AI 思考中...





			** [PowerShell 变量和作用域](https://www.runoob.com/powershell-variables-and-scope.html)
			[PowerShell 脚本编写](https://www.runoob.com/powershell-script.html) **













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