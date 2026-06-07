# ASP.NET Web Pages - 页面布局

- Source: https://www.runoob.com/aspnet/webpages-layout.html

---


通过 Web Pages ，创建一个布局一致的网站是很容易的事。


---


## 一致的外观


在因特网上，您会发现很多网站都具有一致的外观和风格：


- 每个页面有相同的头部
- 每个页面有相同的底部
- 每个页面有相同的样式和布局


通过 Web Pages ，您能非常高效地做到这点。您可以把重复使用的内容块（比如页面头部和底部）写在一个单独的文件中。


您还可以使用布局模板（布局文件）为站点的所有网页定义一致的布局。


---


## Content Blocks（内容块）


许多网站都有一些内容是被显示在站点的每个页面中（比如页面头部和底部）。


通过 Web Pages，您可以使用 **@RenderPage()** 方法从不同的文件导入内容。


内容块（来自另一个文件）能被导入网页中的任何地方。内容块可以包含文本，标记和代码，就像任何普通的网页一样。


将共同的头部和底部写成单独的文件，这样会帮您节省大量的工作。您不必在每个页面中书写相同的内容，当内容有变动时，您只要修改头部或者底部文件，就可以看到站点中的每个页面的相应内容都已更新。


以下显示了它在代码中是如何呈现的：


## 实例


```csharp
<html>
<body>@RenderPage("header.cshtml")
<h1>Hello Web Pages</h1>
<p>This is a paragraph</p>@RenderPage("footer.cshtml")
</body>
</html>
```


**[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_002)


---


## Layout Page（布局页）


在上一部分，您看到了，想在多个网页中显示相同内容是非常容易的。


另一种创建一致外观的方法是使用布局页。一个布局页包含了网页的结构，而不是内容。当一个网页（内容页）链接到布局页，它会根据布局页（模板）的结构进行显示。


布局页中使用 @RenderBody()** 方法嵌入内容页，除此之外，它与一个正常的网页没有什么差别。


每个内容页都必须以**布局指令**开始。


以下显示了它在代码中是如何呈现的：


## 布局页：


```csharp
<html><body><p>This is header text</p>@RenderBody()
<p>&copy; 2012 Runoob. All rights reserved.</p></body></html>
```


**
## 任何网页：


```csharp
@{Layout="Layout.cshtml";}<h1>Welcome to Runoob.com</h1><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit,sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laborisnisi ut aliquip ex ea commodo consequat.</p>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_011)


---


## D.R.Y. - Don't Repeat Yourself（不要自我重复）


通过 Content Blocks（内容块）和 Layout Pages（布局页）这两个 ASP.NET 工具，您可以让您的 Web 应用程序显示一致的外观。


这两个工具能帮您节省大量的工作，您不必再每个页面上重复相同的信息。集中的标记、样式和代码让您的 Web 应用程序更易于管理，更易于维护。


---


## 防止文件被浏览


在 ASP.NET 中，文件的名称以下划线开头，可以防止这些文件在网上被浏览。


如果您不想让您的内容块或者布局页被您的用户看到，可以重命名这些文件：


_header.cshtm


_footer.cshtml


_Layout.cshtml


---


## 隐藏敏感信息


在 ASP.NET 中，隐藏敏感信息（数据库密码、电子邮件密码等等）最通用的方法是将这些信息保存在一个名为"_AppStart"的单独的文件中。


## _AppStart.cshtml


```csharp
@{WebMail.SmtpServer = "mailserver.example.com";
WebMail.EnableSsl = true;WebMail.UserName = "[email protected]";
WebMail.Password = "your-password";WebMail.From = "[email protected]";
}
```










	  AI 思考中...





			** [ASP.NET Web Pages Razor](https://www.runoob.com/webpages-razor.html)
			[ASP.NET Web Pages 文件夹](https://www.runoob.com/webpages-folders.html) **













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