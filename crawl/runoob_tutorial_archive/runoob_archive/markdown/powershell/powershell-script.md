# PowerShell 脚本编写

- Source: https://www.runoob.com/powershell/powershell-script.html

---


## 引言


PowerShell 是一门功能强大的命令行脚本语言，不仅能交互式运行命令，还能将命令组合成脚本文件，实现复杂自动化任务。


本篇文章将带你逐步掌握 PowerShell 脚本开发的基础技能，包括：


- 如何创建和运行 `.ps1` 脚本
- 如何定义和使用函数
- 如何进行模块化开发并复用你的脚本逻辑


---


## 一、PowerShell 脚本入门


### 脚本文件的创建（.ps1）


PowerShell 脚本文件是以 **`.ps1`** 为扩展名的纯文本文件，其中包含一组要执行的 PowerShell 命令。


#### 示例：hello.ps1


```
# hello.ps1
Write-Output "Hello from PowerShell script!"
```


可使用任意文本编辑器（推荐 VS Code）创建 `.ps1` 文件。


### 执行策略（Execution Policy）


Windows 出于安全考虑，默认 **不允许执行脚本**，你需要设置执行策略。


查看当前策略：


```
Get-ExecutionPolicy
```


临时设置为允许本地脚本运行：


```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```


**

RemoteSigned：运行本地脚本无需签名，但下载的脚本必须由可信发布者签名。


### 脚本的运行方法


命令行运行：


```
.\hello.ps1
```


指定 PowerShell 执行器运行：


```
powershell.exe -File .\hello.ps1
pwsh.exe -File .\hello.ps1   # PowerShell 7+
```


右键"使用 PowerShell 运行"（需配合策略设置）


### 参数传递和处理


可以在脚本中定义接收外部参数的方式：


#### 示例：带参数的脚本 greet.ps1


```
param (
    [string]$name,
    [int]$age
)

Write-Output "你好，$name，你的年龄是 $age 岁。"
```


运行时传参：


```
.\greet.ps1 -name "小明" -age 18
```


还支持默认值和参数验证：


```
param (
    [Parameter(Mandatory=$true)]
    [ValidateNotNullOrEmpty()]
    [string]$City = "北京"
)
```


---


## 二、函数的使用


### 函数定义和调用


```
function Say-Hello {
    Write-Output "Hello from function"
}

Say-Hello
```


### 参数声明和验证


函数也可以带参数，使用 `param` 块定义：


```
function Add-Numbers {
    param (
        [int]$a,
        [int]$b
    )
    return $a + $b
}

Add-Numbers -a 3 -b 5  # 输出 8
```


也可以使用位置参数：


```
function Add {
    param ($x, $y)
    $x + $y
}
Add 10 20
```


### 返回值处理


PowerShell 函数默认返回所有输出（包括 `Write-Output`）。


推荐使用 `return` 明确返回：


```
function Get-Square {
    param ([int]$num)
    return $num * $num
}

$result = Get-Square -num 6
Write-Output $result
```


### 函数作用域


函数内部定义的变量默认是局部变量：


```
function Demo-Scope {
    $message = "Hello"
}
Demo-Scope
Write-Output $message  # 无法访问
```


如果要从外部访问变量，可使用作用域前缀：


```
$global:x = 5
```


---


## 三、模块化开发


### 什么是 PowerShell 模块


模块（Module）是多个函数、脚本、资源的集合，用于组织代码、方便复用。


常见模块类型：


- 脚本模块（`.psm1`）
- 清单模块（`.psd1`）
- 二进制模块（.dll）


### 导入和使用模块


使用 `Import-Module` 导入模块：


```
Import-Module MyModule.psm1
```


查看已加载的模块：


```
Get-Module
```


调用模块中的函数：


```
Say-Hello
```


### PowerShell Gallery 简介


[PowerShell Gallery](https://www.powershellgallery.com/) 是 PowerShell 的官方模块仓库，你可以下载并安装数千个模块。


安装模块示例：


```
Install-Module -Name PSReadLine
```


更新模块：


```
Update-Module PSReadLine
```


### 创建简单的自定义模块

新建 MyModule.psm1 文件，添加函数：


```
# MyModule.psm1
function Greet-User {
    param ([string]$name)
    Write-Output "欢迎你，$name"
}
```


在脚本中导入并调用：


```
Import-Module .\MyModule.psm1
Greet-User -name "小红"
```


> 提示：可以将模块文件放入 `$env:PSModulePath` 中的路径，让系统自动识别。


---


## 四、小结


| 内容 | 说明 |
| --- | --- |
| .ps1 文件 | PowerShell 脚本扩展名，存储命令 |
| param | 用于定义脚本/函数参数 |
| Set-ExecutionPolicy | 控制脚本是否允许运行 |
| 函数 | 封装复用代码，提高结构清晰度 |
| 模块（.psm1） | 组织多个函数，实现可移植性 |
| PowerShell Gallery | 官方模块仓库，可下载第三方模块 |









	  AI 思考中...





			** [PowerShell 控制结构](https://www.runoob.com/powershell-control-structures.html)
			[PowerShell 实际应用](https://www.runoob.com/powershell-practice.html) **













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