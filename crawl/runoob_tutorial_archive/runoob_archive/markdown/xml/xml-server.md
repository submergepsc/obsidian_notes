# 服务器上的 XML

- Source: https://www.runoob.com/xml/xml-server.html

---


XML 文件是类似 HTML 文件的纯文本文件。


XML 能够通过标准的 Web 服务器轻松地存储和生成。


---


## 在服务器上存储 XML 文件


XML 文件在 Internet 服务器上进行存储的方式与 HTML 文件完全相同。


启动 Windows 记事本，并写入以下行：


<?xml version="1.0" encoding="ISO-8859-1"?>**
<note>


  <from>Jani</from>


  <to>Tove</to>


  <message>Remember me this weekend</message>

</note>



然后用适当的文件名，比如 "note.xml"，在 Web 服务器上保存这个文件。


---


## 通过 ASP 生成 XML


XML 可在不安装任何 XML 软件的情况下在服务器端生成。


如需从服务器生成 XML 响应 - 只需简单地编写以下代码并在 Web 服务器上把它保存为一个 ASP 文件：


<%

response.ContentType="text/xml"

response.Write("<?xml version='1.0' encoding='ISO-8859-1'?>")

response.Write("<note>")

response.Write("<from>Jani</from>")

response.Write("<to>Tove</to>")

response.Write("<message>Remember me this weekend</message>")

response.Write("</note>")

%>



请注意，此响应的内容类型必须设置为 "text/xml"。


[查看这个 ASP 文件如何从服务器返回](https://www.runoob.com/try/xml/note.asp.xml)。


如果您想要学习 ASP，请在我们的[首页](https://www.runoob.com/../index/index.html)查找 ASP 教程。


---


## 通过 PHP 生成 XML


如需使用 PHP 从服务器上生成 XML 响应，请使用下面的代码：


<?php

header("Content-type: text/xml");

echo "<?xml version='1.0' encoding='ISO-8859-1'?>";

echo "<note>";

echo "<from>Jani</from>";

echo "<to>Tove</to>";

echo "<message>Remember me this weekend</message>";

echo "</note>";

?>



请注意，响应头部的内容类型必须设置为 "text/xml"。


[查看这个 PHP 文件如何从服务器返回](https://www.runoob.com/try/xml/note.php.xml)。


如果您想要学习 PHP，请在我们的[首页](https://www.runoob.com/../index/index.html)查找 PHP 教程。


---


## 从数据库生成 XML


XML 可在不安装任何 XML 软件的情况下从数据库生成。


如需从服务器生成 XML 数据库响应，只需简单地编写以下代码，并把它在 Web 服务器上保存为 ASP 文件：


<%

response.ContentType = "text/xml"

set conn=Server.CreateObject("ADODB.Connection")

conn.provider="Microsoft.Jet.OLEDB.4.0;"

conn.open server.mappath("/db/database.mdb")


sql="select fname,lname from tblGuestBook"

set rs=Conn.Execute(sql)


response.write("<?xml version='1.0' encoding='ISO-8859-1'?>")

response.write("<guestbook>")

while (not rs.EOF)

  response.write("<guest>")

  response.write("<fname>" & rs("fname") & "</fname>")

  response.write("<lname>" & rs("lname") & "</lname>")

  response.write("</guest>")

  rs.MoveNext()

wend


rs.close()

conn.close()

response.write("</guestbook>")

%>




[查看以上 ASP 文件的实际数据库输出](https://www.runoob.com/try/xml/guestbook.asp.xml)。


上面的实例使用了带有 ADO 的 ASP。


如果您想要学习 ASP 和 ADO，请在我们的[首页](https://www.runoob.com/../index/index.html)查找相关教程。


---


## 在服务器上通过 XSLT 转换 XML


下面的 ASP 代码在服务器上把 XML 文件转换为 XHTML：


<%

'Load XML

set xml = Server.CreateObject("Microsoft.XMLDOM")

xml.async = false

xml.load(Server.MapPath("simple.xml"))


'Load XSL

set xsl = Server.CreateObject("Microsoft.XMLDOM")

xsl.async = false

xsl.load(Server.MapPath("simple.xsl"))


'Transform file

Response.Write(xml.transformNode(xsl))

%>


实例解释


- 第一个代码块创建微软 XML 解析器的实例（XMLDOM），并把 XML 文件载入内存。
- 第二个代码块创建解析器的另一个实例，并把 XSL 文件载入内存。
- 最后一个代码使用 XSL 文档来转换 XML 文档，并把结果以 XHTML 发送到您的浏览器。


[看看上面的代码怎么运行](https://www.runoob.com/try/xml/simple.php)。


---


## 通过 ASP 把 XML 保存为文件


这个 ASP 实例会创建一个简单的 XML 文档，并把该文档保存到服务器上：


<%

text="<note>"

text=text & "<to>Tove</to>"

text=text & "<from>Jani</from>"

text=text & "<heading>Reminder</heading>"

text=text & "<body>Don't forget me this weekend!</body>"

text=text & "</note>"


set xmlDoc=Server.CreateObject("Microsoft.XMLDOM")

xmlDoc.async=false

xmlDoc.loadXML(text)


xmlDoc.Save("test.xml")

%>










	  AI 思考中...





			** [XML 编码](https://www.runoob.com/xml-encoding.html)
			[XML DOM 高级](https://www.runoob.com/xml-dom-advanced.html) **













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

      : ·[XML 实例](https://www.runoob.com/xml-examples.html)

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