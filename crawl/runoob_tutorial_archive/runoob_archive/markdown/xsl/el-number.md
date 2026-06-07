# XSLT 元素

- Source: https://www.runoob.com/xsl/el-number.html

---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)

---


## 定义和用法


 元素用于测定在源中当前节点的整数位置。它也用于对数字进行格式化。


---


## 语法


<xsl:number**
count="expression"

level="single|multiple|any"

from="expression"

value="expression"

format="formatstring"

lang="languagecode"

letter-value="alphabetic|traditional"

grouping-separator="character"

grouping-size="number"/>


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| count | expression | 可选。一个 XPath 表达式，规定要计数的节点。 |
| level | single multiple any | 可选。控制如何分配序号。 可以使用的值： single （默认） multiple any （Netscape 6 不支持） |
| from | expression | 可选。一个 XPath 表达式，规定从何处开始计数。 |
| value | expression | 可选。规定用户提供的数字，用于代替产生的序号。 |
| format | formatstring | 可选。定义数字的输出格式。可以使用的值： format="1" 结果 1 2 3 . . format="01" 结果 01 02 03 （Netscape 6 不支持） format="a" 结果 a b c . . （Netscape 6 不支持） format="A" 结果 A B C. . （Netscape 6 不支持） format="i" 结果 i ii iii iv . . （Netscape 6 不支持） format="I" 结果 I II III IV . . （Netscape 6 不支持） |
| lang | languagecode | 可选。规定用于编号的语言字母表。（Netscape 6 不支持） |
| letter-value | alphabetic traditional | 可选。规定选定语言的编号是字母序列（"alphabetic"）还是其他序列（"traditional"）。值 "alphabetic" 指定字母序列；值 "traditional" 指定其他序列。默认是 "alphabetic"。 |
| grouping-separator | character | 可选。规定使用什么字符来分隔组或数字。默认是逗号。 |
| grouping-size | number | 可选。规定由 grouping-separator 属性指定的分隔字符分隔的每个分组中的数字个数。默认是 3。 |


### 实例 1


<xsl:number value="250000" grouping-separator="."/>


Output:


250.000


### 实例 2


<xsl:number value="250000" grouping-size="2"/>


Output:


25,00,00


### 实例 3


<xsl:number value="12" grouping-size="1"

grouping-separator="#" format="I"/>


Output:


X#I#I


### 实例 4


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template match="/">

  <html>

  <body>

  <p>

  <xsl:for-each select="catalog/cd">

    <xsl:number value="position()" format="1" />

    <xsl:value-of select="title" /><br />

  </xsl:for-each>

  </p>

  </body>

  </html>

</xsl:template>


</xsl:stylesheet>


---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)







	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/el-namespace-alias.html)
			[XSLT  元素](https://www.runoob.com/el-otherwise.html) **













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