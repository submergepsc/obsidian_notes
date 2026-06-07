# XSLT - 转换

- Source: https://www.runoob.com/xsl/xsl-transformation.html

---


实例研究：如何使用 XSLT 将 XML 转换为 XHTML。


我们会在下一章对本实例的细节进行解释。


---


## 正确的样式表声明


把文档声明为 XSL 样式表的根元素是  或 。


**注意：** 和  是完全同义的，均可被使用！


根据 W3C 的 XSLT 标准，声明 XSL 样式表的正确方法是：


<xsl:stylesheet version="1.0"**
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


或者：


<xsl:transform version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


如需访问 XSLT 的元素、属性以及特性，我们必须在文档顶端声明 XSLT 命名空间。


xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 指向了官方的 W3C XSLT 命名空间。如果您使用此命名空间，就必须包含属性 version="1.0"。


---


## 从一个原始的 XML 文档开始


我们现在要把下面这个 XML 文档（"cdcatalog.xml"）转换**为 XHTML：


<?xml version="1.0" encoding="ISO-8859-1"?>**
<catalog>


  <cd>


    <title>Empire Burlesque</title>


    <artist>Bob Dylan</artist>


    <country>USA</country>


    <company>Columbia</company>


    <price>10.90</price>


    <year>1985</year>


  </cd>

.

.

</catalog>


在 Firefox 和 Internet Explorer 中查看 XML 文件：**打开 XML 文件（通常通过点击某个链接） - XML 文档会以颜色化的代码方式来显示根元素及子元素。点击元素左侧的加号（+）或减号（-）可展开或收缩元素的结构。如需查看原始的 XML 源文件（不带有加号和减号），请在浏览器菜单中选择"查看页面源代码"或"查看源代码"。


**在 Netscape 6 中查看 XML 文件：**打开 XML 文件，然后在 XML 文件中右击，并选择"查看页面源代码"。XML 文档会以颜色化的代码方式来显示根元素及子元素。


**在 Opera 7 中查看 XML 文件：**打开 XML 文件，然后在 XML 文件中右击，选择"框架"/"查看源代码"。XML 文档将显示为纯文本。


[查看 "cdcatalog.xml"](https://www.runoob.com/try/xml/cdcatalog.xml)


---


## 创建 XSL 样式表


然后创建一个带有转换模板的 XSL 样式表（"cdcatalog.xsl"）：


<?xml version="1.0" encoding="ISO-8859-1"?>**

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template match="/">


  <html>


  <body>


    <h2>My CD Collection</h2>


    <table border="1">


    <tr bgcolor="#9acd32">


      <th>Title</th>


      <th>Artist</th>


    </tr>


    <xsl:for-each select="catalog/cd">


    <tr>


      <td><xsl:value-of select="title"/></td>


      <td><xsl:value-of select="artist"/></td>


    </tr>


    </xsl:for-each>


    </table>


  </body>


  </html>

</xsl:template>


</xsl:stylesheet>


[查看 "cdcatalog.xsl"](https://www.runoob.com/try/xml/cdcatalog.xsl)


---


## 把 XSL 样式表链接到 XML 文档


向 XML 文档（"cdcatalog.xml"）添加 XSL 样式表引用：


<?xml version="1.0" encoding="ISO-8859-1"?>
**<?xml-stylesheet type="text/xsl" href="cdcatalog.xsl"?>**

<catalog>


  <cd>


    <title>Empire Burlesque</title>


    <artist>Bob Dylan</artist>


    <country>USA</country>


    <company>Columbia</company>


    <price>10.90</price>


    <year>1985</year>


  </cd>

.

.

</catalog>


如果您使用的浏览器兼容 XSLT，它会很顺利地把您的 XML 转换**为 XHTML。


[查看结果](https://www.runoob.com/try/xml/cdcatalog_with_xsl.xml)


我们会在下一章对上面的例子中的细节进行解释。

**







	  AI 思考中...





			** [XSLT 浏览器](https://www.runoob.com/xsl-browsers.html)
			[XSLT  元素](https://www.runoob.com/xsl-templates.html) **













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