# XSLT 元素

- Source: https://www.runoob.com/xsl/xsl-templates.html

---


XSL 样式表由一个或多套被称为模板（template）的规则组成。


每个模板含有当某个指定的节点被匹配时所应用的规则。


---


## 元素


 元素用于构建模板。


**match** 属性用于关联 XML 元素和模板。match 属性也可用来为整个 XML 文档定义模板。match 属性的值是 XPath 表达式（举例，match="/" 定义整个文档）。


好了，让我们看一下上一章中的 XSL 文件的简化版本：


## 实例


```xml
<?xml version="1.0" encoding="UTF-8"?>
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
    <tr>
      <td>.</td>
      <td>.</td>
    </tr>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>
```


**[尝试一下 »](https://www.runoob.com/try/tryxslt.php?xmlfile=cdcatalog&xsltfile=cdcatalog_ex1)


## 实例解释


由于 XSL 样式表本身也是一个 XML 文档，因此它总是由 XML 声明起始：**.


下一个元素，****，** **，定义此文档是一个 XSLT 样式表文档（连同版本号和 XSLT 命名空间属性）。


**** 元素定义了一个模板。而 **match="/"** 属性则把此模板与 XML 源文档的根相联系。


 元素内部的内容定义了写到输出结果的 HTML 代码。


最后两行定义了模板的结尾及样式表的结尾。


这个实例的结果有一点小缺陷，因为数据没有从 XML 文档被复制到输出。在下一章中，您将学习到如何使用 **** 元素从 XML 元素选取值。

**







	  AI 思考中...





			** [XSLT 转换](https://www.runoob.com/xsl-transformation.html)
			[XSLT  元素](https://www.runoob.com/xsl-value-of.html) **













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