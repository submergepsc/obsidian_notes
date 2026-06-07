# ASP.NET MVC - 模型

- Source: https://www.runoob.com/aspnet/mvc-models.html

---


为了学习 ASP.NET MVC，我们将构建一个 Internet 应用程序。


第 7 部分：添加数据模型。


---


## MVC 模型


MVC **模型**包含了除纯视图和控制器逻辑以外的其他所有应用程序逻辑（业务逻辑、验证逻辑、数据访问逻辑）。


通过 MVC，模型可以控制并操作应用程序数据。


---


## Models 文件夹


**Models 文件夹**包含表示应用程序模型的类。


Visual Web Developer 自动创建一个 **AccountModels.cs** 文件，该文件包含用于应用程序安全的模型。


**AccountModels** 包含 **LogOnModel**、**ChangePasswordModel** 和 **RegisterModel**。


---


## 添加数据库模型


本教程所需的数据库模型可以通过以下几个简单的步骤来创建：


- 在 **Solution Explorer**窗口中，右击 ** Models** 文件夹，并选择 **Add** 和 **Class**。
- 将类命名为 **MovieDB.cs**，然后点击 **Add**。
- 编辑这个类：


using System;**using System.Collections.Generic;

	using System.Linq;
using System.Web;
using System.Data.Entity;


	namespace MvcDemo.Models
{
public class MovieDB
{
public int ID
	{ get; set; }
public string Title { get; set; }
public string Director
	{ get; set; }
public DateTime Date { get; set; }

}
public class
	MovieDBContext : DbContext
{
public DbSet<MovieDB> Movies { get; set;
	}
}
}


注释：**


我们特意把模型命名为 "MovieDB"。在上一章中，您已经看到用于数据库表的 "MovieDBs"（以 s 结尾）。这看起来有点奇怪，不过这种命名惯例能确保模型连接上数据库表，您必须这么使用。


---


## 添加数据库控制器


本教程所需的数据库控制器可以通过以下几个简单的步骤来创建：


- 重建您的项目：选择 **Debug**，然后从菜单中选择 ** Build MvcDemo**。
- 在 Solution Explorer（解决方案资源管理器）中，右击 **Controllers** 文件夹，选择 **Add** 和 **Controller**。
- 设置控制器名称为 **MoviesController**。
- 选择模板：**Controller with read/write actions and views, using Entity Framework**
- 选择模型类：**MovieDB (MvcDemo.Models)**
- 选择 data context 类：**MovieDBContext (MvcDemo.Models)**
- 选择视图 **Razor (CSHTML)**
- 点击 **Add**


Visual Web Developer 将创建以下文件：


- **Controllers** 文件夹中的 **MoviesController.cs** 文件
- **Views** 文件夹中的 **Movies** 文件夹


---


## 添加数据库视图


在 Movies 文件夹中，会自动创建以下文件：


- Create.cshtml
- Delete.cshtml
- Details.cshtml
- Edit.cshtml
- Index.cshtml


---


## 祝贺您


祝贺您。您已经向应用程序添加了您的第一个 MVC 数据模型。


现在您可以点击 "Movies" 标签页了。


**







	  AI 思考中...





			** [ASP.NET MVC 数据库](https://www.runoob.com/mvc-database.html)
			[ASP.NET MVC 安全](https://www.runoob.com/mvc-security.html) **













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