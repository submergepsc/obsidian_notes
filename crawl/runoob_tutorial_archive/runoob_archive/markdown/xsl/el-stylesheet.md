# XSLT 和 元素

- Source: https://www.runoob.com/xsl/el-stylesheet.html

---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)

---


## 定义和用法


 和  元素是完全同义的元素。都被用来定义样式表的根元素。


---


## 语法


<xsl:stylesheet**
id="name"

version="version"

extension-element-prefixes="list"

exclude-result-prefixes="list">


  <!-- Content:(<xsl:import>*,top-level-elements) -->


</xsl:stylesheet>


<xsl:transform

id="name"

version="version"

extension-element-prefixes="list"

exclude-result-prefixes="list">


  <!-- Content:(<xsl:import>*,top-level-elements) -->


</xsl:transform>


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| version | version | 必需。规定样式表的 XSLT 版本。 |
| extension-element-prefixes | list | 可选。扩展元素的命名空间前缀列表，用空格分隔。Netscape 6 不支持该属性。 |
| exclude-result-prefixes | list | 可选。不应在输出中出现的命名空间前缀列表，用空格分隔。 |
| id | name | 可选。样式表的唯一 id。Netscape 6 不支持该属性。 |


### 实例 1


<?xml version="1.0" encoding="ISO-8859-1"?>


<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


....


....


</xsl:stylesheet>


### 实例 2


<?xml version="1.0" encoding="ISO-8859-1"?>


<xsl:transform version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


....


....


</xsl:transform>


---

[![XSLT 元素参考手册](https://www.runoob.com/images/up.gif) 完整的 XSLT 元素参考手册](https://www.runoob.com/xsl-w3celementref.html)







	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/el-sort.html)
			[XSLT  元素](https://www.runoob.com/el-template.html) **













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