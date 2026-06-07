# ASP.NET MVC - 控制器

- Source: https://www.runoob.com/aspnet/mvc-controllers.html

---


为了学习 ASP.NET MVC，我们将构建一个 Internet 应用程序。


第 4 部分：添加控制器。


---


## Controllers 文件夹


**Controllers 文件夹**包含负责处理用户输入和响应的控制类。


MVC 要求所有控制器文件的名称以 "Controller" 结尾。


在我们的实例中，Visual Web Developer 已经创建好了以下文件： **HomeController.cs**（用于 Home 页面和 About 页面）和**AccountController.cs** （用于登录页面）：


![Controllers](https://www.runoob.com/wp-content/uploads/2013/08/pic_mvc_controllers.jpg)


Web 服务器通常会将进入的 URL 请求直接映射到服务器上的磁盘文件。例如：URL 请求 "http://www.w3cschool.cc/index.php" 将直接映射到服务器根目录上的文件 "index.php"。


MVC 框架的映射方式有所不同。MVC 将 URL 映射到方法。这些方法在类中被称为"控制器"。


控制器负责处理进入的请求，处理输入，保存数据，并把响应发送回客户端。


---


## Home 控制器


在我们应用程序中的控制器文件**HomeController.cs**，定义了两个控件 **Index** 和 **About**。


把 HomeController.cs 文件的内容替换成：


using System;**
using System.Collections.Generic;

using System.Linq;

using System.Web;

using System.Web.Mvc;

namespace MvcDemo.Controllers
{
public class HomeController : Controller
{

	public ActionResult Index()
{return View();}

public ActionResult
	About()
{return View();}
}
}


---


## Controller 视图


Views 文件夹中的文件 Index.cshtml** 和 **About.cshtml** 定义了控制器中的 ActionResult 视图 Index() 和 About()。


**







	  AI 思考中...





			** [ASP.NET MVC 页面和布局](https://www.runoob.com/mvc-layout.html)
			[ASP.NET MVC 视图](https://www.runoob.com/mvc-views.html) **













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