# ASP.NET Web Pages - 全局页面

- Source: https://www.runoob.com/aspnet/webpages-global.html

---


本章介绍全局页面 AppStart 和 PageStart。


---


## 在 Web 启动之前：_AppStart


大多数的服务器端代码是写在个人网页里边。例如，如果网页中包含输入表单，那么这个网页通常包含用来读取表单数据的服务器端代码。


然而，您可以通过在您的站点根目录下创建一个名为 _AppStart 的页面，这样在站点启动之前可以先启动代码执行。如果存在此页面，ASP.NET 会在站点中其它页面被请求时，优先运行这个页面。


_AppStart 的典型用途是启动代码和初始化全局数值（比如计数器和全局名称）。


**注释 1：**_AppStart 的文件扩展名与您的网页一致，比如：_AppStart.cshtml。


**注释 2：**_AppStart 有下划线前缀。因此，这些文件不可以直接浏览。


---


## 在每一个页面之前：_PageStart


就像 _AppStart 在您的站点启动之前就运行一样，您可以编写在每个文件夹中的任何页面之前运行的代码。


对于您网站中的每个文件夹，您可以添加一个名为 _PageStart 的文件。


_PageStart 的典型用途是为一个文件夹中的所有页面设置布局页面，或者在运行某个页面之前检查用户是否已经登录。


---


## 它是如何工作的？


下图显示了它是如何工作的：


![PageStart](https://www.runoob.com/wp-content/uploads/2013/07/pic_webpages_pagestart.jpg)


当接收到一个请求时，ASP.NET 会首先检查 _AppStart 是否存在。 如果 _AppStart 存在且这是站点接收到的第一个请求，则运行 _AppStart。


然后 ASP.NET 检查 _PageStart 是否存在。如果 _PageStart 存在，则在其它被请求的页面运行之前先运行 _PageStart。


您可以在 _PageStart 中调用 RunPage() 来指定被请求页面的运行位置。否则，默认情况下，被请求页面是在 _PageStart 运行之后才被运行。

**







	  AI 思考中...





			** [ASP.NET Web Pages 文件夹](https://www.runoob.com/webpages-folders.html)
			[ASP.NET Web Pages HTML 表单](https://www.runoob.com/webpages-forms.html) **













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