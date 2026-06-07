# ASP.NET Razor - C# 和 VB 代码语法

- Source: https://www.runoob.com/aspnet/razor-syntax.html

---


Razor 同时支持 C# (C sharp) 和 VB (Visual Basic)。


---


## 主要的 Razor C# 语法规则


- Razor 代码块包含在 @{ ... } 中
- 内联表达式（变量和函数）以 @ 开头
- 代码语句用分号结束
- 变量使用 var 关键字声明
- 字符串用引号括起来
- C# 代码区分大小写
- C# 文件的扩展名是 .cshtml


## C# 实例


```csharp
<!-- Single statement block -->@{ var myMessage =	"Hello World"; }
<!-- Inline expression or variable -->
<p>The value of myMessage is: @myMessage</p>
<!--	Multi-statement block -->@{
var greeting = "Welcome to our site!";
var weekDay = DateTime.Now.DayOfWeek;
var greetingMessage = greeting + " Here in Huston it is: " + weekDay;
}<p>The greeting is: @greetingMessage</p>
```


**[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_cs_001)


---


## 主要的 Razor VB 语法规则


- Razor 代码块包含在 @Code ... End Code 中
- 内联表达式（变量和函数）以 @ 开头
- 变量使用 Dim 关键字声明
- 字符串用引号括起来
- VB 代码不区分大小写
- VB 文件的扩展名是 .vbhtml


## 实例


```csharp
<!-- Single statement block  --> @Code dim myMessage = "Hello World" End Code

<!-- Inline expression or variable -->
<p>The value of myMessage is: @myMessage</p>

<!-- Multi-statement block --> @Code
dim greeting = "Welcome to our site!"
dim weekDay = DateTime.Now.DayOfWeek
dim greetingMessage = greeting & " Here in Huston it is: " & weekDay
End Code

<p>The greeting is: @greetingMessage</p>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_vb_001)


---


## 它是如何工作的？


Razor 是一种将服务器代码嵌入在网页中的简单的编程语法。


Razor 语法是基于 ASP.NET 框架，专门用于创建 Web 应用程序的部分 Microsoft.NET 框架。


Razor 语法支持所有 ASP.NET 的功能，但是使用的是一种简化语法，对初学者而言更容易学习，对专家而言更有效率的。


Razor 网页可以被描述成带以下两种类型内容的 HTML 网页： HTML 内容和 Razor 代码。


当服务器读取页面时，它首先运行 Razor 代码，然后再发送 HTML 页面到浏览器。在服务器上执行的代码能够执行一些在浏览器上不能完成的任务，比如，访问服务器数据库。服务器代码能创建动态的 HTML 内容，然后发送到浏览器。从浏览器上看，服务器代码生成的 HTML 与静态的 HTML 内容没有什么不同。


带 Razor 语法的 ASP.NET 网页有特殊的文件扩展名 cshtml（Razor C#）或者 vbhtml（Razor VB）。


---


## 使用对象


服务器编码往往涉及到对象。

"Date" 对象是一个典型的内置的 ASP.NET 对象，但对象也可以是自定义的，一个网页，一个文本框，一个文件，一个数据库记录，等等。

对象有用于执行的方法。一个数据库记录可能有一个 "Save" 方法，一个图像对象可能有一个 "Rotate" 方法，一个电子邮件对象可能有一个 "Send" 方法，等等。 对象也有用于描述各自特点的属性。一个数据库记录可能有 FirstName 和 LastName 属性。


ASP.NET Date 对象有一个 Now 属性（写成 Date.Now），Now 属性有一个 Day 属性（写成 Date.Now.Day）。下面实例演示了如何访问 Date 对象的一些属性：


## 实例


```csharp
<table border="1"><tr><th
width="100px">Name</th><td width="100px">Value</td>
</tr><tr><td>Day</td><td>@DateTime.Now.Day</td>
</tr><tr><td>Hour</td><td>@DateTime.Now.Hour</td>
</tr><tr><td>Minute</td><td>@DateTime.Now.Minute</td>
</tr><tr><td>Second</td><td>@DateTime.Now.Second</td>
</tr></td></table>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_cs_002)


---


## If 和 Else条件


动态网页的一个重要特点是，您可以根据条件决定做什么。


做到这一点的常用方法是使用 if ... else 语句：


## 实例


```csharp
@{var txt = "";if(DateTime.Now.Hour > 12)
{txt = "Good Evening";}else  {txt = "Good Morning";}}
<html><body><p>The message is @txt</p>
</body></html>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_cs_003)


---


## 读取用户输入


动态网页的另一个重要特点是，您可以读取用户输入。


输入是通过 Request[] 功能读取的，并且传送输入数据是经过 IsPost 条件判断的：


## 实例


```csharp
@{var totalMessage = "";if(IsPost)

{    var num1 = Request["text1"];

var num2 = Request["text2"];    var total = num1.AsInt() + num2.AsInt();    totalMessage =
"Total = " + total;    }}<html><body
style="background-color: beige; font-family: Verdana, Arial;"><form
action="" method="post"><p><label for="text1">First Number:</label><br>
<input type="text" name="text1" /></p><p><label for="text2">Second
Number:</label><br><input type="text" name="text2" /></p><p><input
type="submit" value=" Add " /></p></form><p>@totalMessage</p>
</body></html>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_cs_004)










	  AI 思考中...





			** [ASP.NET Razor 标记](https://www.runoob.com/razor-intro.html)
			[ASP.NET Razor C# 变量](https://www.runoob.com/razor-cs-variables.html) **













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