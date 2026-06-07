# XSLT - 编辑 XML

- Source: https://www.runoob.com/xsl/xsl-editxml.html

---


存储在 XML 文件中的数据可通过因特网浏览器进行编辑。


---


## 打开、编辑并保存 XML


现在，我们会为您展示如何打开、编辑及保存存储于服务器上的 XML 文件。


我们将使用 XSL 把 XML 文档转换到一个 HTML 表单中。XML 元素的值会被写到 HTML 表单中的 HTML 输入域。这个 HTML 表单是可编辑的。在被编辑完成后，数据会被提交回服务器，XML 文件会得到更新（这部分由 ASP 完成）。


---


## XML 文件和 XSL 文件


首先，请看将被使用的 XML 文档（"tool.xml"）：


<?xml version="1.0" encoding="ISO-8859-1"?>**
<tool>


  <field id="prodName">


    <value>HAMMER HG2606</value>


  </field>


  <field id="prodNo">


    <value>32456240</value>


  </field>


  <field id="price">


    <value>$30.00</value>


  </field>

</tool>


[查看 XML 文件](https://www.runoob.com/try/xml/tool.xml)。


接着，请看下面的样式表（"tool.xsl"）：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template match="/">


<html>


<body>


<form method="post" action="edittool.html">


<h2>Tool Information (edit):</h2>


<table border="0">


<xsl:for-each select="tool/field">


<tr>


<td><xsl:value-of select="@id"/></td>


<td>


<input type="text">


<xsl:attribute name="id">

        <xsl:value-of select="@id" />

      </xsl:attribute>


<xsl:attribute name="name">

        <xsl:value-of select="@id" />

      </xsl:attribute>


<xsl:attribute name="value">

        <xsl:value-of select="value" />

      </xsl:attribute>


</input>


</td>


</tr>


</xsl:for-each>


</table>


<br />


<input type="submit" id="btn_sub" name="btn_sub" value="Submit" />


<input type="reset" id="btn_res" name="btn_res" value="Reset" />


</form>


</body>


</html>

</xsl:template>


</xsl:stylesheet>


[查看 XSL 文件](https://www.runoob.com/try/xml/tool.xsl)。


上面这个 XSL 文件会循环遍历 XML 文件中的元素，并为每个 XML "field" 元素创建一个输入域。XML "field" 元素的 "id" 属性的值被添加到每个 HTML 输入域的 "id" 和 "name" 属性。每个 XML "value" 元素的值被添加到每个 HTML 输入域的 "value" 属性。结果是，可以得到一个包含 XML 文件中值的可编辑的 HTML 表单。


然后，我们还有第二个样式表："tool_updated.xsl"。这个 XSL 文件会被用来显示已更新的 XML 数据。这个样式表不会输出可编辑 HTML 表单，而是一个静态的 HTML 表格：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template match="/">


<html>


<body>


<h2>Updated Tool Information:</h2>


<table border="1">


<xsl:for-each select="tool/field">


<tr>


<td><xsl:value-of select="@id" /></td>


<td><xsl:value-of select="value" /></td>


</tr>


</xsl:for-each>


</table>


</body>


</html>

</xsl:template>


</xsl:stylesheet>


[查看 XSL 文件](https://www.runoob.com/try/xml/tool_updated.xsl)。


---


## ASP 文件


在上面 "tool.xsl" 文件中，HTML 表单的 action 属性的值是 "edittool.asp" 。


"edittool.asp" 页面包含两个函数：loadFile() 函数载入并转换 XML 文件，updateFile() 函数更新 XML 文件：


<%

function loadFile(xmlfile,xslfile)

Dim xmlDoc,xslDoc
'Load XML file

set xmlDoc = Server.CreateObject("Microsoft.XMLDOM")

xmlDoc.async = false

xmlDoc.load(xmlfile)
'Load XSL file

set xslDoc = Server.CreateObject("Microsoft.XMLDOM")

xslDoc.async = false

xslDoc.load(xslfile)
'Transform file

Response.Write(xmlDoc.transformNode(xslDoc))

end function


function updateFile(xmlfile)

Dim xmlDoc,rootEl,f

Dim i
'Load XML file

set xmlDoc = Server.CreateObject("Microsoft.XMLDOM")

xmlDoc.async = false

xmlDoc.load(xmlfile)


'Set the rootEl variable equal to the root element

Set rootEl = xmlDoc.documentElement


'Loop through the form collection

for i = 1 To Request.Form.Count


'Eliminate button elements in the form


if instr(1,Request.Form.Key(i),"btn_")=0 then


'The selectSingleNode method queries the XML file for a single node


'that matches a query. This query requests the value element that is


'the child of a field element that has an id attribute which matches


'the current key value in the Form Collection. When there is a match -


'set the text property equal to the value of the current field in the


'Form Collection.


set f = rootEl.selectSingleNode("field[@id='" & _


Request.Form.Key(i) & "']/value")


f.Text = Request.Form(i)


end if

next


'Save the modified XML file

xmlDoc.save xmlfile


'Release all object references

set xmlDoc=nothing

set rootEl=nothing

set f=nothing


'Load the modified XML file with a style sheet that

'allows the client to see the edited information

loadFile xmlfile,server.MapPath("tool_updated.xsl")

end function


'If the form has been submitted update the

'XML file and display result - if not,

'transform the XML file for editing

if Request.Form("btn_sub")="" then


loadFile server.MapPath("tool.xml"),server.MapPath("tool.xsl")

else


updateFile server.MapPath("tool.xml")

end if

%>


提示：**假如您不了解如何编写 ASP，请学习我们的 [ASP 教程](https://www.runoob.com/../asp/asp-tutorial.html)。


**注意：**我们正在转换并更新位于服务器上的 XML 文件。这是一个跨平台的解决方案。客户端仅能获得从服务器返回的 HTML - 而 HTML 可运行于任何浏览器。

**







	  AI 思考中...





			** [XSLT 在服务器端](https://www.runoob.com/xsl-server.html)
			[XML 编辑器](https://www.runoob.com/xsl-editors.html) **













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