# XSLT current() 函数

- Source: https://www.runoob.com/xsl/func-current.html

---

[![XSLT 函数参考对象](https://www.runoob.com/images/up.gif) 完整的 XSLT 函数参考对象](https://www.runoob.com/xsl-functions.html)

---


## 定义和用法


current() 函数返回仅包含当前节点的节点集。通常，当前节点与上下文节点是相同的。


等于


不过，有一点不同。让我们看一下下面的 XPath 表达式："catalog/cd"。表达式选择了当前节点的  子节点，然后选择了  节点的  子节点。这意味着，在计算的每一步上，"." 都有不同的意义。


下面这行：


将处理 title 属性的值等于当前节点的 ref 属性的值的所有 cd 元素。


与这个不同：


这个会处理 title 属性和 ref 属性具有相同值的所有 cd 元素。


---


## 语法


node-set current()


### 实例 1


<?xml version="1.0" encoding="ISO-8859-1"?>**
<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template match="/">

  <html>

  <body>

  <xsl:for-each select="catalog/cd/artist">

    Current node: <xsl:value-of select="current()"/>

    <br />

  </xsl:for-each>

  </body>

  </html>

</xsl:template>


</xsl:stylesheet>



[查看 XML 文件](https://www.runoob.com/try/xml/cdcatalog.xml)、 [查看 XSL 文件](https://www.runoob.com/try/xml/cdcatalog_current.xsl)、 [查看结果](https://www.runoob.com/try/xml/cdcatalog_current.xml)。


---

[![XSLT 函数参考对象](https://www.runoob.com/images/up.gif) 完整的 XSLT 函数参考对象](https://www.runoob.com/xsl-functions.html)







	  AI 思考中...





			** [XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)
			[XSLT document() 函数](https://www.runoob.com/func-document.html) **













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