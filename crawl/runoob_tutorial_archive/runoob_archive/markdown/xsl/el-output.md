# XSLT 元素

- Source: https://www.runoob.com/xsl/el-output.html

---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)

---


## 定义和用法


 元素定义了输出文档的格式。


**注释：** 是顶层元素（top-level element），必须是  或  的子节点。


---


## 语法


<xsl:output**
method="xml|html|text|name"

version="string"

encoding="string"

omit-xml-declaration="yes|no"

standalone="yes|no"

doctype-public="string"

doctype-system="string"

cdata-section-elements="namelist"

indent="yes|no"

media-type="string"/>


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| method | xml html text name | 可选。定义输出的格式。默认是 XML（但是如果根节点的第一个子节点是 ，且在这之前没有文本节点，则默认是 HTML）。Netscape 6 仅支持 "html" 和 "xml"。 |
| version | string | 可选。设置输出格式的 W3C 版本号。（仅在 method="html" or method="xml" 时使用）。 |
| encoding | string | 可选。设置输出中编码属性的值。 |
| omit-xml-declaration | yes no | 可选。"yes" 规定在输出中省略 XML 声明（）。"no" 规定应在输出中包含的 XML 声明。默认是 "no"。 |
| standalone | yes no | 可选。"yes" 规定 XSLT 处理器应输出独立文档声明。"no" 规定 XSLT 处理器不应输出独立文档声明。默认是 "no"。 Netscape 6 不支持该属性。 |
| doctype-public | string | 可选。规定 DTD 中要使用的公共标识符。即输出中 DOCTYPE 声明的 PUBLIC 属性的值。 |
| doctype-system | string | 可选。规定 DTD 中要使用的系统标识符。即输出中 DOCTYPE 声明的 SYSTEM 属性的值。 |
| cdata-section-elements | namelist | 可选。一个空格分隔的元素列表，这些元素的文本内容应作为 CDATA 部分来输出。 |
| indent | yes no | 可选。"yes" 规定输出应根据其层次结构进行缩排。"no" 规定输出不应根据其层次结构进行缩排。Netscape 6 不支持该属性。 |
| media-type | string | 可选。定义输出的 MIME 类型（数据的媒体类型）。默认是 "text/xml"。 Netscape 6 不支持该属性。 |


### 实例 1


在本例中，输出是 XML 文档，版本为 1.0。字符编码方式被设置为 "ISO-8859-1"，输出会进行缩进，以增进可读性：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:output method="xml" version="1.0"

encoding="iso-8859-1" indent="yes"/>


...


...


</xsl:stylesheet>


### 实例 2


在本例中，输出是 HTML 文档，版本是 4.0。字符编码方式被设置为 "ISO-8859-1"，输出会进行缩进，以增进可读性：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:output method="html" version="4.0"

encoding="iso-8859-1" indent="yes"/>


...


...


</xsl:stylesheet>


---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)







	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/el-otherwise.html)
			[XSLT  元素](https://www.runoob.com/el-param.html) **













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