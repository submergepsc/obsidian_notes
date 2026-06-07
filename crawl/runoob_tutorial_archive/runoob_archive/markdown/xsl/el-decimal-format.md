# XSLT 元素

- Source: https://www.runoob.com/xsl/el-decimal-format.html

---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)

---


## 定义和用法


 元素定义了当通过 format-number() 函数把数字转换为字符串时，所要使用的字符和符号。


不是所有国家都使用相同的字符来分隔小数部分与整数部分，或者对数字进行分组。通过  元素，您可以把具体的字符更改为其他的符号。


该元素是顶层元素（top level element）。


format-number() 函数可通过名称（name）来引用  元素。


---


## 语法


<xsl:decimal-format**
name="name"

decimal-separator="char"

grouping-separator="char"

infinity="string"

minus-sign="char"

NaN="string"

percent="char"

per-mille="char"

zero-digit="char"

digit="char"

pattern-separator="char"/>


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| name | name | 可选。为此格式规定名称。 |
| decimal-separator | char | 可选。规定小数点字符。默认是 "."。 |
| grouping-separator | char | 可选。规定千的分隔字符。默认是 ","。 |
| infinity | string | 可选。规定用来表示无穷大的字符串。默认是 "Infinity"。 |
| minus-sign | char | 可选。规定表示负数的字符。默认是 "-"。 |
| NaN | string | 可选。规定当值不是数字时使用的字符串。默认是 "NaN"。 |
| percent | char | 可选。规定百分比符号的字符。默认是 "%"。 |
| per-mille | char | 可选。规定千分号的字符。默认是 "‰"。 |
| zero-digit | char | 可选。规定数字 0 的字符。默认是 "0"。 |
| digit | char | 可选。规定字符，该字符用于指示需要使用数字的地方。默认是 #。 |
| pattern-separator | char | 可选。规定字符，该字符用于分隔格式模式中的正负子模式。默认是 ";"。 |


### 实例 1


下面的实例展示了如何格式化为欧洲货币（请注意，format-number() 函数中的第三个参数引用了  元素的名称）：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:decimal-format name="euro"

decimal-separator="," grouping-separator="."/>


<xsl:template match="/">

<xsl:value-of

select="format-number(26825.8, '#.###,00', 'euro')"/>

</xsl:template>


</xsl:stylesheet>


Output:


26,825.80


---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)







	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/el-copy-of.html)
			[XSLT  元素](https://www.runoob.com/el-element.html) **













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