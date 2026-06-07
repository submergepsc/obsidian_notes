# ASP.NET Web Pages - 添加 Razor 代码

- Source: https://www.runoob.com/aspnet/webpages-razor.html

---


在本教程中，我们将使用 C# 和 Visual Basic 代码的 Razor 标记。


---


## 什么是 Razor ？


- Razor 是一种将基于服务器的代码添加到网页中的标记语法
- Razor 具有传统 ASP.NET 标记的功能，但更容易使用并且更容易学习
- Razor 是一种服务器端标记语法，与 ASP 和 PHP 很像
- Razor 支持 C# 和 Visual Basic 编程语言


---


## 添加 Razor 代码


请记住上一章实例中的网页：


<!DOCTYPE html>**

<html lang="en">

<head>

   <meta charset="utf-8" />


<title>Web Pages Demo</title>

</head>

<body>

    <h1>Hello Web Pages</h1>

</body>

</html>


现在向实例中添加一些 Razor 代码：


## 实例


```csharp
<!DOCTYPE html>
<html lang="en">
<head>
     <meta charset="utf-8" />
     <title>Web Pages Demo</title>
</head>
<body>
     <h1>Hello Web Pages</h1>
     <p>The time is @DateTime.Now</p>
</body>
</html>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_001)


该页面中包含普通的 HTML 标记，除此之外，还添加了一个 @ 标识的 Razor 代码。


Razor 代码能够在服务器上实时地完成多有的动作，并将结果显示出来。（您可以指定格式化选项，否则只会显示默认项。）


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
var greetingMessage = greeting + " Today is: " + weekDay;
}<p>The greeting is: @greetingMessage</p>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_cs_001)


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
dim greetingMessage = greeting & " Today is: " & weekDay
End Code

<p>The greeting is: @greetingMessage</p>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_vb_001)


---


## 更多关于 C# 和 Visual Basic


如果您想学习更多关于 Razor、C#、Visual Basic 编程语言，请查看本教程的 [Razor 部分](https://www.runoob.com/razor-intro.html)。










	  AI 思考中...





			** [ASP.NET Web Pages 教程](https://www.runoob.com/webpages-intro.html)
			[ASP.NET Web Pages 布局](https://www.runoob.com/webpages-layout.html) **













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