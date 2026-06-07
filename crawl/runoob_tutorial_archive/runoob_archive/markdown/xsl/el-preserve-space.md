# XSLT 和 元素

- Source: https://www.runoob.com/xsl/el-preserve-space.html

---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)

---


## 定义和用法


 元素用于定义保留空白的元素。


 元素用于定义删除空白的元素。


**注释：**保留空白是默认的设置，所以只有当使用  元素时才有必要使用  元素。


**注释：** 元素和  元素都是顶层元素（top-level element）。


---


## 语法


<xsl:preserve-space elements="list-of-element-names"/>**

<xsl:strip-space elements="list-of-element-names"/>


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| elements | list-of-element-names | 必需。一个空格分隔的元素列表，规定了保留/删除空白的元素。 注意：列表中可包含 "*" 和 "prefix:*"，这样就可以加入所有元素或来自特定命名空间的所有元素。 |


### 实例 1


在本例中，我们为 title 和 artist 元素预留了空白节点，并从 country、company、price 以及 year 元素删除了空白节点：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:strip-space elements="country company price year" />

<xsl:preserve-space elements="title artist" />


<xsl:template match="/">

  <html>

  <body>

  <xsl:for-each select="catalog/cd">

    <p>

    <xsl:value-of select="title" /><br />

    <xsl:value-of select="artist" /><br />

    <xsl:value-of select="country" /><br />

    <xsl:value-of select="company" /><br />

    <xsl:value-of select="price" /><br />

    <xsl:value-of select="year" />

    </p>

  </xsl:for-each>

  </body>

  </html>

</xsl:template>


</xsl:stylesheet>


---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)







	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/el-param.html)
			[XSLT  元素](https://www.runoob.com/el-processing-instruction.html) **













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