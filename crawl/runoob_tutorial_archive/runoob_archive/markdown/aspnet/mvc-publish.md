# ASP.NET MVC - 发布网站

- Source: https://www.runoob.com/aspnet/mvc-publish.html

---


学习如何在不使用 Visual Web Developer 的情况下发布 MVC 应用程序。


---


## 在不使用 Visual Web Developer 的情况下发布您的应用程序


通过在 WebMatrix、Visual Web Developer 或 Visual Studio 中使用发布命令，可以发布一个 ASP.NET MVC 应用程序到远程服务器上。


此功能会复制所有您的应用程序文件、控制器、模型、图像以及用于 MVC、Web Pages、Razor、Helpers、SQL Server Compact（如果使用数据库）所有必需的 DLL 文件。


有时您不希望使用这些选项。或许您的主机提供商仅支持 FTP？或许您的网站基于经典 ASP？或许您希望亲自拷贝这些文件？又或许您希望使用 Front Page、Expression Web 等其他一些发布软件？


**您会遇到问题吗？是的，会的。但是您有办法解决它。**


要执行网站复制，您必须知道如何引用正确的文件，哪些 DLL 文件需要复制，并在何处存储它们。


请按照下列步骤操作：


---


## 1. 使用最新版本的 ASP.NET


在您继续操作之前，请确保您的主机运行的是最新版的 ASP.NET（4.0 或者 4.5）。


---


## 2. 复制 Web 文件夹


从您的开发计算机上复制您的网站（所有文件夹和内容）到远程主机（服务器）上的应用程序文件夹中。


如果您的 **App_Data** 文件夹中包含测试数据，请不要复制这个 App_Data 文件夹（详见下面的第 5 点）。


---


## 3. 复制 DLL 文件


在远程服务器上的应用程序根目录中创建 bin 文件夹。（如果您已经安装 Helpers，则 bin 文件夹已经存在）


复制下列文件夹中的所有文件：


**C:Program Files (x86)Microsoft ASP.NETASP.NET Web Pagesv1.0Assemblies**


**C:Program Files (x86)Microsoft ASP.NETASP.NET MVC 3Assemblies**


到您的远程服务器上的应用程序的 bin 文件夹中。


---


## 4. 复制 SQL Server Compact DLL 文件


如果您的应用程序使用了 SQL Server Compact 数据库（在 App_Data 文件夹中的一个 .sdf 文件），那么您必须复制 SQL Server Compact DLL 文件：


复制下列文件夹中的所有文件：


**C:Program Files (x86)Microsoft SQL Server Compact Editionv4.0Private**


到您的远程服务器上的应用程序的 bin 文件夹中。


创建（或者编辑）应用程序的 Web.config 文件：


## 实例 C#


```csharp
<?xml version="1.0" encoding="UTF-8"?><configuration><system.data>
	<DbProviderFactories><remove invariant="System.Data.SqlServerCe.4.0" /><add invariant="System.Data.SqlServerCe.4.0"name="Microsoft SQL
	Server Compact 4.0"description=".NET Framework Data Provider for Microsoft SQL
	Server Compact" type="System.Data.SqlServerCe.SqlCeProviderFactory,
	System.Data.SqlServerCe, Version=4.0.0.1,Culture=neutral, PublicKeyToken=89845dcd8080cc91"
	/></DbProviderFactories></system.data></configuration>
```


**
---


## 5. 复制 SQL Server Compact 数据


您的 App_Data 文件夹中有没有包含测试数据的 .sdf 文件？


您是否希望发布您的测试数据到远程服务器上？


大多数时候一般是不希望。


如果您一定要复制 SQL 数据文件（.sdf 文件），那么您应该删除数据库中的所有数据，然后从您的开发计算机上复制一个空的 .sdf 文件到服务器上。


就是这样。GOOD LUCK！**

**







	  AI 思考中...





			** [ASP.NET MVC HTML 帮助器](https://www.runoob.com/mvc-htmlhelpers.html)
			[ASP.NET MVC 参考手册](https://www.runoob.com/mvc-reference.html) **













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