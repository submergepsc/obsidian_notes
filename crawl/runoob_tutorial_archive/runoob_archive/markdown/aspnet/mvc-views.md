# ASP.NET MVC - 视图

- Source: https://www.runoob.com/aspnet/mvc-views.html

---


为了学习 ASP.NET MVC，我们将构建一个 Internet 应用程序。


第 5 部分：添加用于显示应用程序的视图。


---


## Views 文件夹


**Views** 文件夹存储的是与应用程序显示（用户界面）相关的文件（HTML 文件）。根据所采用的语言内容，这些文件可能扩展名可能是 html、asp、aspx、cshtml 和 vbhtml。


Views 文件夹中包含每个控制器对应的一个文件夹。


在 Views 文件夹中，Visual Web Developer 已经创建了一个 Account 文件夹、一个 Home 文件夹、一个 Shared 文件夹。


Account 文件夹包含用于用户账号注册和登录的页面。


Home 文件夹用于存储诸如 home 页和 about 页之类的应用程序页面。


Shared 文件夹用于存储控制器间分享的视图（母版页和布局页）。


![Views](https://www.runoob.com/wp-content/uploads/2013/08/pic_mvc_views.jpg)


---


## ASP.NET 文件类型


在 Views 文件夹中可以看到以下 HTML 文件类型：


| 文件类型 | 扩展名 |
| --- | --- |
| 纯 HTML | .htm or .html |
| 经典 ASP | .asp |
| 经典 ASP.NET | .aspx |
| ASP.NET Razor C# | .cshtml |
| ASP.NET Razor VB | .vbhtml |

**
---


## Index 文件


文件 Index.cshtml 表示应用程序的 Home 页面。它是应用程序的默认文件（首页文件）。


在文件中写入以下内容：


@{ViewBag.Title = "Home Page";}

<h1>Welcome to
	runoob.com</h1>

<p>Put Home Page content here</p>


---


## About 文件


文件 About.cshtml 表示应用程序的 About 页面。


在文件中写入以下内容：


@{ViewBag.Title = "About Us";}


	<h1>About Us</h1>

<p>Put About Us content here</p>


---


## 运行应用程序


选择 Debug，从 Visual Web Developer 菜单中启动调试 Start Debugging（或者按 F5）。


您的应用程序将显示如下：


![MVC Application](https://www.runoob.com/wp-content/uploads/2013/08/pic_mvc_app.jpg)


点击 "Home" 标签页和 "About" 标签页，看看它是如何运作的。


---


## 祝贺您


祝贺您。您已经创建好了您的第一个 MVC 应用程序。


注释：**您暂时还不能点击 "Movies" 标签页。我们将在本教程的后面章节中为 "Movies" 标签页添加代码。

**







	  AI 思考中...





			** [ASP.NET MVC 控制器](https://www.runoob.com/mvc-controllers.html)
			[ASP.NET MVC 数据库](https://www.runoob.com/mvc-database.html) **













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