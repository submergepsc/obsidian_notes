# XSLT - 在客户端

- Source: https://www.runoob.com/xsl/xsl-client.html

---


如果您的浏览器支持 XSLT，那么在浏览器中它可被用来将文档转换为 XHTML。


---


## JavaScript 解决方案

在前面的章节，我们已向您讲解如何使用 XSLT 将某个 XML 文档转换为 XHTML。我们是通过以下途径完成这个工作的：向 XML 文件添加 XSL 样式表，并通过浏览器完成转换。即使这种方法的效果很好，在 XML 文件中包含样式表引用也不总是令人满意的（例如，在无法识别 XSLT 的浏览器这种方法就无法奏效）。


更通用的方法是使用 JavaScript 来完成转换。


通过使用 JavaScript，我们可以：


- 进行浏览器确认测试
- 根据浏览器和用户需求来使用不同的样式表


这就是 XSLT 的魅力所在！XSLT 的设计目的之一就是使数据从一种格式转换到另一种格式成为可能，同时支持不同类型的浏览器以及不同的用户需求。


客户端的 XSLT 转换一定会成为未来浏览器所执行的主要任务之一，同时我们也会看到其在特定的浏览器市场的增长（盲文、听觉浏览器、网络打印机，手持设备，等等）。


---


## XML 文件和 XSL 文件


请看这个在前面的章节已展示过的 XML 文档：


## 实例


```xml
<?xml version="1.0" encoding="UTF-8"?>
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
```


[查看 XML 文件](https://static.jyshare.com/download/cdcatalog_client.xsl)。


以及附随的 XSL 样式表：


## 实例


```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<body>
  <h2>My CD Collection</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th style="text-align:left">Title</th>
      <th style="text-align:left">Artist</th>
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
```


[查看 XSL 文件](https://static.jyshare.com/download/cdcatalog_client.xsl)。


**请注意，这个 XML 文件没有包含对 XSL 文件的引用。**


**重要事项：**上面这句话意味着，XML 文件可使用多个不同的 XSL 样式表来进行转换。


**注意，要确保 XSL 文件可以通过链接在浏览器中正常打开，如下所示：**


![](https://www.runoob.com/wp-content/uploads/2013/10/62203CF4-AFA7-41CD-90F9-42AED17DDCA1.jpeg)

否则可能出现错误 **Uncaught TypeError: Failed to execute 'importStylesheet' on 'XSLTProcessor': parameter 1 is not of type 'Node'.**。


![](https://www.runoob.com/wp-content/uploads/2013/10/2DB74753-81DC-4E62-ABFD-3F0186E5ED43.jpg)


---


## 在浏览器中把 XML 转换为 XHTML


这是用于在客户端把 XML 文件转换为 XHTML 的源代码：


## 实例


```xml
<!DOCTYPE html>
<html>
<head>
<script>
```

function loadXMLDoc(filename) {
    if (window.ActiveXObject) {
        xhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } else {
        xhttp = new XMLHttpRequest();
    }
    xhttp.open("GET", filename, false);
    try {
        xhttp.responseType = "msxml-document"
    } catch (err) {} // Helping IE11
    xhttp.send("");
    return xhttp.responseXML;
}

function displayResult() {
    xml = loadXMLDoc("cdcatalog.xml");
    xsl = loadXMLDoc("cdcatalog.xsl");
    // code for IE
    if (window.ActiveXObject || xhttp.responseType == "msxml-document") {
        ex = xml.transformNode(xsl);
        document.getElementById("example").innerHTML = ex;
    }
    // code for Chrome, Firefox, Opera, etc.
    else if (document.implementation && document.implementation.createDocument) {
        xsltProcessor = new XSLTProcessor();
        xsltProcessor.importStylesheet(xsl);
        resultDocument = xsltProcessor.transformToFragment(xml, document);
        document.getElementById("example").appendChild(resultDocument);
    }
}</script>
</head>
<body onload="displayResult()">
<div id="example" />
</body>
</html>

**[尝试一下 »](https://www.runoob.com/try/try.php?filename=cdcatalog)


提示：**假如您不了解如何编写 JavaScript，请学习我们的 [JavaScript 教程](https://www.runoob.com/../js/js-tutorial.html)。


## 实例解释：


**loadXMLDoc() 函数**


loadXMLDoc() 函数是用来加载 XML 和 XSL 文件。


它检查用户拥有的和加载文件的浏览器类型。


**displayResult() 函数**


该函数用来显示使用 XSL 文件定义样式的 XML 文件。


- 加载 XML 和 XSL 文件
- 测试用户拥有的浏览器类型
- 如果用户浏览器支持 ActiveX 对象： 使用 transformNode() 方法把 XSL 样式表应用到 XML 文档
- 设置当前文档（id="example"）的 body 包含已经应用样式的 XML 文档


	 如果用户的浏览器不支持 ActiveX 对象：
- 创建一个新的 XSLTProcessor 对象并导入 XSL 文件
- 使用 transformToFragment() 方法把 XSL 样式表应用到 XML 文档
- 设置当前文档（id="example"）的 body 包含已经应用样式的 XML 文档


**







	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/xsl-apple-templates.html)
			[XSLT 在服务器端](https://www.runoob.com/xsl-server.html) **













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