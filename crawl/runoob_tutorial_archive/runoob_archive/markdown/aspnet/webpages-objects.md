# ASP.NET Web Pages - 对象

- Source: https://www.runoob.com/aspnet/webpages-objects.html

---


Web Pages 经常是跟对象有关的。


---


## Page 对象


您已经看到了一些在使用的 Page 对象方法：


	@RenderPage("header.cshtml")**
@RenderBody()


在前面的章节中，您已经看到了两个 Page 对象属性（isPost 和 Request）：


	If (isPost) {

if (Request["Choice"] != null ) {


---


## 某些 Page 对象方法


| 方法 | 描述 |
| --- | --- |
| href | 使用指定的值创建 URL。 |
| RenderBody() | 呈现不在布局页命名区域的内容页的一部分。 |
| RenderPage(page) | 在另一个页面中呈现某一个页面的内容。 |
| RenderSection(section) | 呈现布局页命名区域的内容。 |
| Write(object) | 将对象作为 HTML 编码字符串写入。 |
| WriteLiteral | 写入对象时优先不使用 HTML 编码。 |


---


## 某些 Page 对象属性


| 属性 | 描述 |
| --- | --- |
| isPost | 如果客户端使用的 HTTP 数据传输方法是 POST 请求，则返回 true。 |
| Layout | 获取或者设置布局页面的路径。 |
| Page | 提供了对页面和布局页之间共享的数据的类似属性访问。 |
| Request | 为当前的 HTTP 请求获取 HttpRequest 对象。 |
| Server | 获取 HttpServerUtility 对象，该对象提供了网页处理方法。 |


---


## Page 对象的 Page 属性


Page 对象的 Page 属性，提供了对页面和布局页之间共享的数据的类似属性访问。


您可以对 Page 属性使用（添加）您自己的属性：


- Page.Title
- Page.Version
- Page.anythingyoulike


页面属性是非常有用的。例如，在内容文件中设置页面标题，并在布局文件中使用：


## Home.cshtml


```csharp
@{Layout="~/Shared/Layout.cshtml";Page.Title="Home Page"}
	<h1>Welcome to runoob.com</h1> <h2>Web Site Main Ingredients</h2><p>A Home Page (Default.cshtml)</p><p>A Layout File (Layout.cshtml)</p>
	<p>A Style Sheet (Site.css)</p>
```


## Layout.cshtml


```csharp
<!DOCTYPE html><html><head><title>@Page.Title</title></head><body>@RenderBody()
	</body>
	</html
```










	  AI 思考中...





			** [ASP.NET Web Pages HTML 表单](https://www.runoob.com/webpages-forms.html)
			[ASP.NET Web Pages 文件](https://www.runoob.com/webpages-files.html) **













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