# XSLT 元素

- Source: https://www.runoob.com/xsl/el-import.html

---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)

---


## 定义和用法


 元素是顶层元素，用于把一个样式表中的内容导入另一个样式表中。


**注意：**被导入的样式表的优先级低于导出的样式表。


**注意：**该元素必须是  或  的第一个子节点。


---


## 语法


<xsl:import href="URI"/>


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| href | URI | 必需。规定要导入的样式表的 URI。 |


### 实例 1


假设您有一个名为 "cdcatalog_ex3.xsl" 的样式表：


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

      <tr>

        <td><xsl:value-of select="catalog/cd/title"/></td>

        <td><xsl:value-of select="catalog/cd/artist"/></td>

      </tr>

    </table>

  </body>

  </html>

</xsl:template>


</xsl:stylesheet>


第二个名为 "cdcatalog_import.xsl" 的样式表会导入 "cdcatalog_ex3.xsl"：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:import href="cdcatalog_ex3.xsl"/>


<xsl:template match="/">

  <xsl:apply-imports/>

</xsl:template>


</xsl:stylesheet>


[查看 XML 文件](https://www.runoob.com/try/xml/cdcatalog.xml)、 [查看 XSL 文件](https://www.runoob.com/try/xml/cdcatalog_import.xsl)、 [查看结果](https://www.runoob.com/try/xml/cdcatalog_import.xml)。


注意：**该实例无法在 Netscape 6 运行，因为 Netscape 6 不支持  元素！**


---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)







	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/el-if.html)
			[XSLT  元素](https://www.runoob.com/el-include.html) **













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