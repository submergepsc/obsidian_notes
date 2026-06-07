# ASP.NET Web Forms - 数据绑定

- Source: https://www.runoob.com/aspnet/aspnet-databinding.html

---


我们可以使用数据绑定（Data Binding）来完成带可选项的列表，这些可选项来自某个导入的数据源，比如数据库、XML 文件或者脚本。


---


## 数据绑定


下面的控件是支持数据绑定的列表控件：


- asp:RadioButtonList
- asp:CheckBoxList
- asp:DropDownList
- asp:Listbox


以上每个控件的可选项通常是在一个或者多个 asp:ListItem 控件中定义，如下：


<html>**
<body>


<form runat="server">

<asp:RadioButtonList id="countrylist" runat="server">

<asp:ListItem value="N" text="Norway" />

<asp:ListItem value="S" text="Sweden" />

<asp:ListItem value="F" text="France" />

<asp:ListItem value="I" text="Italy" />

</asp:RadioButtonList>

</form>


</body>

</html>


然而，我们可以使用某种独立的数据源进行数据绑定，比如数据库、XML 文件或者脚本，通过数据绑定来填充列表的可选项。


通过使用导入的数据源，数据从 HTML 中分离出来，并且对可选项的修改都是在独立的数据源中完成的。


在下面的三个章节中，我们将描述如何从脚本化的数据源中绑定数据。










	  AI 思考中...





			** [ASP.NET Button 控件](https://www.runoob.com/aspnet-button.html)
			[ASP.NET ArrayList](https://www.runoob.com/aspnet-arraylist.html) **













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