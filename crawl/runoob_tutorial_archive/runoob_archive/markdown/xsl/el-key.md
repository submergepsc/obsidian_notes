# XSLT 元素

- Source: https://www.runoob.com/xsl/el-key.html

---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)

---


## 定义和用法


The  元素是顶层元素（top-level element），它可声明一个命名的键（即为 XML 文档中指定的元素分配的名称和值对）。该键通过 key() 函数在样式表中使用，帮助您有效地在复杂的 XML 文档中访问分配的元素。


**注意：**键不必是唯一的！


---


## 语法


<xsl:key**
name="name"

match="pattern"

use="expression"/>


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| name | name | 必需。规定键的名称。 |
| match | pattern | 必需。定义该键被应用到哪个节点。 |
| use | expression | 必需。指定要作为每个节点的键的值使用的表达式。 |


### 实例 1


假设您拥有名为 "persons.xml" 的 XML 文件：


<persons>

  <person name="Tarzan" id="050676"/>

  <person name="Donald" id="070754"/>

  <person name="Dolly" id="231256"/>

</persons>


您可以在 XSL 文件中定义一个键，如下所示：


<xsl:key name="preg" match="person" use="@id"/>


如需找到 id="050676" 的 person，请使用这些代码（在 XSL 文件中）：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:key name="preg" match="person" use="@id"/>


<xsl:template match="/">

  <html>

  <body>

  <xsl:for-each select="key('preg','050676')">

    <p>

    Id: <xsl:value-of select="@id"/><br />

    Name: <xsl:value-of select="@name"/>

    </p>

  </xsl:for-each>

  </body>

  </html>

</xsl:template>


</xsl:stylesheet>


---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)







	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/el-include.html)
			[XSLT  元素](https://www.runoob.com/el-message.html) **













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