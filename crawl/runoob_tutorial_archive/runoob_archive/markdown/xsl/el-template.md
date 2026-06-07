# XSLT 元素

- Source: https://www.runoob.com/xsl/el-template.html

---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)

---


## 定义和用法


 元素包含了当匹配指定节点时要应用的规则。


match 属性用于把模板关联到某个 XML 元素。match 属性也能用于为 XML 文档的全部分支定义模板（比如，match="/" 定义了整个文档）。


**注意：** 是顶层元素（top-level element）。


---


## 语法


<xsl:template**
name="name"

match="pattern"

mode="mode"

priority="number">


  <!-- Content:(<xsl:param>*,template) -->


</xsl:template>


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| name | name | 可选。为模板定义名称。注释：如果省略该属性，则必须设置 match 属性。 |
| match | pattern | 可选。模板的匹配模式。注释：如果省略该属性，则必须设置 name 属性。 |
| mode | mode | 可选。为模板规定模式。 |
| priority | number | 可选。一个表示模板的优先级编号的数字。 |


### 实例


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template match="/">

  <html>

  <body>

  <h2>My CD Collection</h2>

  <xsl:apply-templates/>

  </body>

  </html>

</xsl:template>


<xsl:template match="cd">

  <p>

  <xsl:apply-templates select="title"/>

  <xsl:apply-templates select="artist"/>

  </p>

</xsl:template>


<xsl:template match="title">

  Title: <span style="color:#ff0000">

  <xsl:value-of select="."/></span>

  <br />

</xsl:template>


<xsl:template match="artist">

  Artist: <span style="color:#00ff00">

  <xsl:value-of select="."/></span>

  <br />

</xsl:template>


</xsl:stylesheet>


[查看 XML 文件](https://www.runoob.com/try/xml/cdcatalog.xml)、 [查看 XSL 文件](https://www.runoob.com/try/xml/cdcatalog_apply.xsl)、 [查看结果](https://www.runoob.com/try/xml/cdcatalog_apply.xml)。


---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)







	  AI 思考中...





			** [XSLT  和  元素](https://www.runoob.com/el-stylesheet.html)
			[XSLT  元素](https://www.runoob.com/el-text.html) **













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