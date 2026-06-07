# ASP.NET MVC 教程

- Source: https://www.runoob.com/aspnet/mvc-intro.html

**

ASP.NET 是一个使用 HTML、CSS、JavaScript 和服务器脚本创建网页和网站的开发框架。


ASP.NET 支持三种不同的开发模式： Web Pages（Web 页面）、MVC（Model View Controller 模型-视图-控制器）、Web Forms（Web 窗体）。


本教程介绍 MVC**。


| Web Pages |  | MVC |  | Web Forms |
| --- | --- | --- | --- | --- |

**
---


## MVC 编程模式


MVC 是三种 ASP.NET 编程模式中的一种。


MVC 是一种使用 MVC（Model View Controller 模型-视图-控制器）设计创建 Web 应用程序的模式：


- Model（模型）表示应用程序核心（比如数据库记录列表）。
- View（视图）显示数据（数据库记录）。
- Controller（控制器）处理输入（写入数据库记录）。


MVC 模式同时提供了对 HTML、CSS 和 JavaScript 的完全控制。


---


|  | MVC 模式定义 Web 应用程序带有三个逻辑层： 业务层（模型逻辑） 显示层（视图逻辑） 输入控制（控制器逻辑） |
| --- | --- |


Model（模型）**是应用程序中用于处理应用程序数据逻辑的部分。** 通常模型对象负责在数据库中存取数据。


View（视图）**是应用程序中处理数据显示的部分。** 通常视图是依据模型数据创建的。


Controller（控制器）**是应用程序中处理用户交互的部分。** 通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据。


MVC 分层有助于管理复杂的应用程序，因为您可以在一个时间内专门关注一个方面。例如，您可以在不依赖业务逻辑的情况下专注于视图设计。同时也让应用程序的测试更加容易。


MVC 分层同时也简化了分组开发。不同的开发人员可同时开发视图、控制器逻辑和业务逻辑。


---


## Web Forms 对比 MVC


MVC 编程模式是对传统 ASP.NET（Web Forms）的一种轻量级的替代方案。它是轻量级的、可测试性高的框架，同时整合了所有已有的 ASP.NET 特性，比如母版页、安全性和认证。


---


## Visual Studio Express 2012/2010


Visual Studio Express 是 Microsoft Visual Studio 的免费版本。


Visual Studio Express 是为 MVC（和 Web Forms）量身定制的开发工具。


Visual Studio Express 包含：


- MVC 和 Web Forms
- 拖拽 Web 控件和 Web 组件
- Web 服务器语言（Razor 使用 VB 或者 C#）
- Web 服务器（IIS Express）
- 数据库服务器（SQL Server Compact）
- 完整的 Web 开发框架（ASP.NET）


如果您已经安装了 Visual Studio Express，您将从本教程中学到更多。


如果您想安装 Visual Studio Express，请点击下列链接中的一个：


[Visual Web Developer 2012](http://www.microsoft.com/web/handlers/webpi.ashx?command=getinstallerredirect&appid=VWDOrVs11AzurePack)（Windows 7 或者 Windows 8）


[Visual Web Developer 2010](http://www.microsoft.com/web/gallery/install.aspx?appid=VWDorVS2010SP1Pack)（Windows Vista 或者 XP）


|  | 在您首次安装完 Visual Studio Express 之后，您可以通过再次运行安装程序来安装补丁和服务包，只需要再次点击链接即可。 |
| --- | --- |


---


## ASP.NET MVC 参考手册


在本教程的最后，我们提供了完整的 ASP.NET MVC 参考手册供您查阅。










	  AI 思考中...





			** [ASP.NET Razor VB 逻辑](https://www.runoob.com/razor-vb-logic.html)
			[ASP.NET MVC Web 应用程序](https://www.runoob.com/mvc-app.html) **













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