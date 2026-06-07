# ASP.NET Web Pages - HTML 表单

- Source: https://www.runoob.com/aspnet/webpages-forms.html

---


表单是 HTML 文档中放置输入控件（文本框、复选框、单选按钮、下拉列表）的部分。


---


## 创建一个 HTML 输入页面


## Razor 实例


```csharp
<html>
<body> @{
if (IsPost) {
string companyname = Request["companyname"];
string contactname = Request["contactname"]; <p>You entered: <br />
Company Name: @companyname <br />
Contact Name: @contactname </p>
}
else
{<form method="post" action="">
	Company Name:<br />
<input type="text" name="CompanyName" value="" /><br />
	Contact Name:<br />
<input type="text" name="ContactName" value="" /><br /><br />
	<input type="submit" value="Submit" class="submit" />
</form>}}
</body>
</html>
```


**[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_009)


---


## Razor 实例 - 显示图像


假设在您的图像文件夹中有 3 张图像，您想根据用户的选择动态地显示图像。


这可以通过一段简单的 Razor 代码来实现。


如果在您的网站的图像文件夹中有一个名为 "Photo1.jpg" 的图像，您可以使用 HTML 的  元素来显示图像，如下所示：


<img src="images/Photo1.jpg" alt="Sample" />


下面的例子演示了如何显示用户从下列列表中选择的图像：


## Razor 实例


```csharp
@{
var imagePath="";
if (Request["Choice"] != null)
   {imagePath="images/" + Request["Choice"];}
} <!DOCTYPE html>
<html>
<body>
<h1>Display Images</h1>
<form method="post" action="">
I want to see:
<select name="Choice">

<option value="Photo1.jpg">Photo 1</option>

<option value="Photo2.jpg">Photo 2</option>

<option value="Photo3.jpg">Photo 3</option>
</select>
<input type="submit" value="Submit" />
	@if (imagePath != "")
{<p><img src="@imagePath" alt="Sample" /></p>}
</form>
</body>
</html>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_010)


## 实例解释


服务器创建了一个叫 imagePath** 的变量。


HTML 页面有一个名为 **Choice** 的**下拉列表**（ 元素）。它允许用户根据自己的意愿选择一个名称（如 **Photo 1**），当页面被提交到 Web 服务器时，则传递了一个文件名（如 **Photo1.jpg**）。


Razor 代码通过 **Request["Choice"]** 读取 Choice 的值。如果通过代码构建的图像路径（images/Photo1.jpg）有效，就把图像路径赋值给变量 **imagePath**。


在 HTML 页面中， 元素用来显示图像。当页面显示时，src 属性用来设置 imagePath 变量的值。


 元素是在一个 if 块中，这是为了防止显示没有名称的图像，比如页面第一次被加载显示的时候。








	  AI 思考中...





			** [ASP.NET Web Pages 全局文件](https://www.runoob.com/webpages-global.html)
			[ASP.NET Web Pages 对象](https://www.runoob.com/webpages-objects.html) **













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