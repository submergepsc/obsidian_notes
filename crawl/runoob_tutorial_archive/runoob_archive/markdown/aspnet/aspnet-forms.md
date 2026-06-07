# ASP.NET Web Forms - HTML 表单

- Source: https://www.runoob.com/aspnet/aspnet-forms.html

---


所有的服务器控件都必须出现在  标签中， 标签必须包含 runat="server" 属性。


---


## ASP.NET Web 表单


所有的服务器控件都必须出现在  标签中， 标签必须包含 runat="server" 属性。runat="server" 属性表明该表单必须在服务器上进行处理。同时也表明了包含在它内部的控件可被服务器脚本访问：


<form runat="server">**

...HTML + server controls


</form>


注释：**该表单总是被提交到自身页面。如果您指定了一个 action 属性，它会被忽略。如果您省略了 method 属性，它将会默认设置 method="post"。同时，如果您没有指定 name 和 id 属性，它们会由 ASP.NET 自动分配。


**注释：**一个 .aspx 页面只能包含一个  控件！


如果您在一个包含不带有 name、method、action 或 id 属性的表单的 .aspx 页面中选择查看源代码，您会看到 ASP.NET 添加这些属性到表单上了，如下所示：


<form name="_ctl0" method="post" action="page.aspx" id="_ctl0">**

...some code


</form>


---


## 提交表单


表单通常通过点击按钮来提交。ASP.NET 中的 Button 服务器控件的格式如下：


<asp:Button id="id" text="label" OnClick="sub" runat="server" />


id 属性为按钮定义了一个唯一的名称，text 属性为按钮分配了一个标签。onClick 事件句柄规定了一个要执行的已命名的子例程。


在下面的例子中，我们在一个 .aspx 文件中声明了一个按钮控件。一次鼠标单击就可以运行一个子例程，可以更改该按钮上的文本。


[实例](https://www.runoob.com/try/showfile_c.php?filename=demo_aspnet_button)










	  AI 思考中...





			** [ASP.NET 事件句柄](https://www.runoob.com/aspnet-events.html)
			[ASP.NET ViewState](https://www.runoob.com/aspnet-viewstate.html) **













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