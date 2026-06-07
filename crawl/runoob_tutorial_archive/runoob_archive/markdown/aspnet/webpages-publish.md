# ASP.NET Web Pages - 发布网站

- Source: https://www.runoob.com/aspnet/webpages-publish.html

---


学习如何在不使用 WebMatrix 的情况下发布 Web Pages 应用程序。


---


## 在不使用 WebMatrix 的情况下发布您的应用程序


通过在 WebMatrix（或者 Visual Studio）中使用发布命令，可以发布一个 ASP.NET Web Pages 应用程序到远程服务器上。


此功能会复制所有您的应用程序文件、cshtml页面、图像以及用于 Web Pages、Razor、Helpers、SQL Server Compact（如果使用数据库）所有必需的 DLL 文件。


有时您不想使用 WebMatrix 发布您的应用程序。也许是因为您的托管服务提供商只支持 FTP，也许您已经有一个基于经典 ASP 的网站，也许您想自己复制所有的文件，也许您想使用 Front Page、Expression Web 等其他一些发布软件。


**您会遇到问题吗？是的，会的。但是您有办法解决它。**


要执行网站复制，您必须知道如何引用正确的文件，哪些 DLL 文件需要复制，并在何处存储它们。


请按照下列步骤操作：


---


## 1. 使用最新版本的 ASP.NET


在您继续操作之前，请确保您的主机运行的是最新版的 ASP.NET（4.0 或者 4.5）。


---


## 2. 复制 Web 文件夹


从您的开发计算机上复制您的网站（所有文件夹和内容）到远程主机（服务器）上的应用程序文件夹中。


|  | 如果您的应用程序中包含数据，不要复制数据（详见下面的第 4 点）。 |
| --- | --- |


---


## 3. 复制 DLL 文件


确保您的远程主机上的 bin 文件夹中包含了和您开发计算机上相同的 dll 文件。


复制 bin 文件夹之后，它应该包含以下文件：


Microsoft.Web.Infrastructure.dll** NuGet.Core.dll System.Web.Helpers.dll System.Web.Razor.dll System.Web.WebPages.Administration.dll System.Web.WebPages.Deployment.dll System.Web.WebPages.dll System.Web.WebPages.Razor.dll WebMatrix.Data.dll WebMatrix.WebData


---


## 4. 复制您的数据


如果您的应用程序包含数据或者数据库。例如 SQL Server Compact 数据库（在 App_Data 文件夹中的一个 .sdf 文件），请考虑以下几点：


您是否希望发布您的测试数据到远程服务器上？


大多数时候一般是不希望。


如果在您的开发计算机上有测试数据，它将覆盖您的远程主机上的生产数据。


如果您一定要复制 SQL 数据库（.sdf 文件），那么您应该删除数据库中的所有数据，然后从您的开发计算机上复制一个空的 .sdf 文件到服务器上。


就是这样。GOOD LUCK！**

**







	  AI 思考中...





			** [ASP.NET Web Pages PHP](https://www.runoob.com/webpages-php.html)
			[ASP.NET Web 的 C# 和 VB 实例](https://www.runoob.com/webpages-examples.html) **













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