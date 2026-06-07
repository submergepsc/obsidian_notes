# ASP.NET Web Forms - ArrayList 对象

- Source: https://www.runoob.com/aspnet/aspnet-arraylist.html

---


ArrayList 对象是包含单个数据值的项目的集合。


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[ArrayList DropDownList](https://www.runoob.com/try/showaspx.php?filename=demo_arraylist_drop1)


[ArrayList RadioButtonList](https://www.runoob.com/try/showaspx.php?filename=demo_arraylist_radio1)


---


## 创建 ArrayList


ArrayList 对象是包含单个数据值的项目的集合。


通过 Add() 方法向 ArrayList 添加项目。


下面的代码创建了一个名为 mycountries 的 ArrayList 对象，并添加了四个项目：


<script runat="server">**
Sub Page_Load

if Not Page.IsPostBack then


  dim mycountries=New ArrayList


  mycountries.Add("Norway")


  mycountries.Add("Sweden")


  mycountries.Add("France")


  mycountries.Add("Italy")

end if

end sub

</script>


在默认情况下，一个 ArrayList 对象包含 16 个条目。可通过 TrimToSize() 方法把 ArrayList 调整为最终尺寸：


<script runat="server">

Sub Page_Load

if Not Page.IsPostBack then


  dim mycountries=New ArrayList


  mycountries.Add("Norway")


  mycountries.Add("Sweden")


  mycountries.Add("France")


  mycountries.Add("Italy")


  mycountries.TrimToSize()

end if

end sub

</script>


通过 Sort() 方法，ArrayList 也能够按照字母顺序或者数字顺序进行排序：


<script runat="server">

Sub Page_Load

if Not Page.IsPostBack then


  dim mycountries=New ArrayList


  mycountries.Add("Norway")


  mycountries.Add("Sweden")


  mycountries.Add("France")


  mycountries.Add("Italy")


  mycountries.TrimToSize()


  mycountries.Sort()

end if

end sub

</script>


要实现反向排序，请在 Sort() 方法后应用 Reverse() 方法：


<script runat="server">

Sub Page_Load

if Not Page.IsPostBack then


  dim mycountries=New ArrayList


  mycountries.Add("Norway")


  mycountries.Add("Sweden")


  mycountries.Add("France")


  mycountries.Add("Italy")


  mycountries.TrimToSize()


  mycountries.Sort()


  mycountries.Reverse()

end if

end sub

</script>


---


## 绑定数据到 ArrayList


ArrayList 对象可为下列的控件自动生成文本和值：


- asp:RadioButtonList
- asp:CheckBoxList
- asp:DropDownList
- asp:Listbox


为了绑定数据到 RadioButtonList 控件，首先要在 .aspx 页面中创建一个 RadioButtonList 控件（不带任何 asp:ListItem 元素）：


<html>

<body>


<form runat="server">

<asp:RadioButtonList id="rb" runat="server" />

</form>


</body>

</html>


然后添加创建列表的脚本，并且绑定列表中的值到 RadioButtonList 控件：


## 实例


```csharp
<script runat="server">
Sub Page_Load
if Not Page.IsPostBack then
  dim mycountries=New ArrayList
  mycountries.Add("Norway")
  mycountries.Add("Sweden")
  mycountries.Add("France")
  mycountries.Add("Italy")
  mycountries.TrimToSize()
  mycountries.Sort()
  rb.DataSource=mycountries
  rb.DataBind()
end if
end sub
</script>
<html>
<body>
<form runat="server">
<asp:RadioButtonList id="rb" runat="server" />
</form>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showaspx.php?filename=demo_arraylist_radio1)


RadioButtonList 控件的 DataSource 属性被设置为该 ArrayList，它定义了这个 RadioButtonList 控件的数据源。RadioButtonList 控件的 DataBind() 方法把 RadioButtonList 控件与数据源绑定在一起。


注释：**数据值作为控件的 Text 和 Value 属性来使用。如需添加不同于 Text 的 Value，请使用 Hashtable 对象或者 SortedList 对象。

**







	  AI 思考中...





			** [ASP.NET 数据绑定](https://www.runoob.com/aspnet-databinding.html)
			[ASP.NET Hashtable](https://www.runoob.com/aspnet-hashtable.html) **













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