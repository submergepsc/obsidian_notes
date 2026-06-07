# XSLT 元素

- Source: https://www.runoob.com/xsl/el-apply-templates.html

---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)

---


## 定义和用法


 元素可向当前元素或当前元素的子节点应用模板。


如果我们向  元素添加 select 属性，那么它仅会处理匹配该属性的值的子元素。我们可使用 select 属性来规定要处理的子节点的顺序。


---


## 语法


<xsl:apply-templates select="expression" mode="name">**

  <!-- Content:(xsl:sort|xsl:with-param)* -->


</xsl:apply-templates>


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| select | expression | 可选。规定要处理的节点。星号选取整个节点集。如果省略该属性，则将选取当前节点的所有子节点。 |
| mode | name | 可选。如果存在为相同元素定义的多个处理方法，那么用 mode 可以区分它们。 |


### 实例 1


用 h1 元素包围文档中每个 title 元素：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template match="title">

  <h1><xsl:apply-templates/></h1>

</xsl:template>


</xsl:stylesheet>


### 实例 2


用 h1 元素包围文档中所有属于 message 的子元素的 title 元素：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template match="message">

  <h1><xsl:apply-templates select="title"/></h1>

</xsl:template>


</xsl:stylesheet>


### 实例 3


用 h1 元素包围文档中 mode 属性设置为 "big" 的 message 所有子节点：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template match="message">

  <h1><xsl:apply-templates select="*" mode="big"/></h1>

</xsl:template>


</xsl:stylesheet>


---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)







	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/el-apply-imports.html)
			[XSLT  元素](https://www.runoob.com/el-attribute.html) **













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