# XSLT 元素

- Source: https://www.runoob.com/xsl/el-when.html

---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)

---


## 定义和用法


 元素用于为  元素规定相关动作。  元素会计算一个表达式，如果返回 true，则执行规定的动作。


**注意：** 元素与  元素和  元素协同使用，来表达多个条件测试。


---


## 语法


<xsl:when**
test="boolean-expression">


  <!-- Content: template -->


</xsl:when>


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| test | boolean-expression | 必需。规定要测试的布尔表达式。 |


### 实例 1


下面的代码会在 cd 的价格高于 10 时向 artist 列添加粉色的背景色。


<?xml version="1.0" encoding="ISO-8859-1"?>

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

        <xsl:choose>

          <xsl:when test="price&gt;'10'">

            <td bgcolor="#ff00ff">

            <xsl:value-of select="artist"/></td>

          </xsl:when>

          <xsl:otherwise>

            <td><xsl:value-of select="artist"/></td>

          </xsl:otherwise>

        </xsl:choose>

      </tr>

      </xsl:for-each>

    </table>

  </body>

  </html>

</xsl:template>


</xsl:stylesheet>


[查看 XML 文件](https://www.runoob.com/try/xml/cdcatalog.xml)、 [查看 XSL 文件](https://www.runoob.com/try/xml/cdcatalog_choose.xsl)、 [查看结果](https://www.runoob.com/try/xml/cdcatalog_choose.xml)。


### 实例 2


声明了一个名为 "color" 的变量。把它的值赋给当前元素的 color 属性。如果当前元素没有 color 属性，则 "color" 的值将是 "green"：


<xsl:variable name="color">

  <xsl:choose>

    <xsl:when test="@color">

      <xsl:value-of select="@color"/>

    </xsl:when>

    <xsl:otherwise>green</xsl:otherwise>

  </xsl:choose>

</xsl:variable>


---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)







	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/el-variable.html)
			[XSLT  元素](https://www.runoob.com/el-with-param.html) **













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