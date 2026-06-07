# ASP AdRotator 组件

- Source: https://www.runoob.com/asp/asp-adrotator.html

---


## ASP AdRotator 组件


每当用户进入网站或刷新页面时，ASP AdRotator 组件就会创建一个 AdRotator 对象来显示一幅不同的图像。有关图像的信息是包含在一个文本文件中。


**注释：**AdRotator 在 Internet Information Server 7 (IIS7) 中不起作用。


### 语法


<%**
set adrotator=server.createobject("MSWC.AdRotator")

adrotator.GetAdvertisement("textfile.txt")

%>


---


## ASP AdRotator 实例


假设我们有一个名为 "ads.txt" 的文件，如下所示：


REDIRECT banners.asp

*

runoob.gif

http://www.runoob.com

Free Tutorials from RUNOOB

50

xmlspy.gif

http://www.altova.com

XML Editor from Altova

50


在上面的文本文件中型号下面的行规定了要显示的图像的名称、超链接地址、图像的替换文本和每百次点击中的显示几率。


上述文本文件的第一行指定当访客点击图像时进行的动作。重定向页（banners.asp）将收到一个带有重定向 URL 的查询字符串。


提示：**如需规定图像的高度、宽度和边框，您可以在 REDIRECT 下面插入如下代码：




      REDIRECT banners.asp**
      WIDTH 468

      HEIGHT 60

      BORDER 0

      *

      runoob.gif

      ...




"banners.asp" 文件如下所示：


## 实例


```
<%
url=Request.QueryString("url")
If url<>"" then Response.Redirect(url)
%>
	<!DOCTYPE html><html>
<body>
<%
set adrotator=Server.CreateObject("MSWC.AdRotator")
response.write(adrotator.GetAdvertisement("textfile.txt"))
%>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showasp.php?filename=demo_adrotator)


好了，以上就是全部的内容！


---


## ASP AdRotator 属性


| 属性 | 描述 | 实例 |
| --- | --- | --- |
| Border | 规定围绕广告的边框的尺寸。 | set adrot=Server.CreateObject("MSWC.AdRotator") adrot.Border="2" Response.Write(adrot.GetAdvertisement("ads.txt")) %> |
| Clickable | 规定广告本身是否是超链接。 | set adrot=Server.CreateObject("MSWC.AdRotator") adrot.Clickable=false Response.Write(adrot.GetAdvertisement("ads.txt")) %> |
| TargetFrame | 显示广告的框架名称。 | set adrot=Server.CreateObject("MSWC.AdRotator") adrot.TargetFrame="target='_blank'" Response.Write(adrot.GetAdvertisement("ads.txt")) %> |


## ASP AdRotator 方法


| 方法 | 描述 | 实例 |
| --- | --- | --- |
| GetAdvertisement | 返回在页面中显示广告的 HTML。 | set adrot=Server.CreateObject("MSWC.AdRotator") Response.Write(adrot.GetAdvertisement("ads.txt")) %> |










	  AI 思考中...





			** [ASP ADO](https://www.runoob.com/asp-ado.html)
			[ASP Browser Capabilities](https://www.runoob.com/asp-browser.html) **













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