# XML 验证

- Source: https://www.runoob.com/xml/xml-dtd.html

---


拥有正确语法的 XML 被称为"形式良好"的 XML。


通过 DTD 验证的XML是"合法"的 XML。


---


## 形式良好的 XML 文档


"形式良好"的 XML 文档拥有正确的语法。


在前面的章节描述的语法规则：


- XML 文档必须有一个根元素
- XML元素都必须有一个关闭标签
- XML 标签对大小写敏感
- XML 元素必须被正确的嵌套
- XML 属性值必须加引号


<?xml version="1.0" encoding="ISO-8859-1"?>**
<note>

<to>Tove</to>

<from>Jani</from>

<heading>Reminder</heading>

<body>Don't forget me this weekend!</body>

</note>


---


## 验证 XML 文档


合法的 XML 文档是"形式良好"的 XML 文档，这也符合文档类型定义（DTD）的规则：


<?xml version="1.0" encoding="ISO-8859-1"?>
**<!DOCTYPE note SYSTEM "Note.dtd">**

<note>

<to>Tove</to>

<from>Jani</from>

<heading>Reminder</heading>

<body>Don't forget me this weekend!</body>

</note>


在上面的实例中，DOCTYPE 声明是对外部 DTD 文件的引用。下面的段落展示了这个文件的内容。


---


## XML DTD


DTD 的目的是定义 XML 文档的结构。它使用一系列合法的元素来定义文档结构：


<!DOCTYPE note

[

  <!ELEMENT note (to,from,heading,body)>

  <!ELEMENT to      (#PCDATA)>

  <!ELEMENT from    (#PCDATA)>

  <!ELEMENT heading (#PCDATA)>

  <!ELEMENT body    (#PCDATA)>

]>


如果您想要学习 DTD，请在我们的[首页](https://www.runoob.com/../index/index.html)查找 DTD 教程。


---


## XML Schema


W3C 支持一种基于 XML 的 DTD 代替者，它名为 XML Schema：


<xs:element name="note">


<xs:complexType>

  <xs:sequence>

    <xs:element name="to" type="xs:string"/>

    <xs:element name="from" type="xs:string"/>

    <xs:element name="heading" type="xs:string"/>

    <xs:element name="body" type="xs:string"/>

  </xs:sequence>

</xs:complexType>


</xs:element>

如果您想要学习 XML Schema，请在我们的[首页](https://www.runoob.com/../index/index.html)查找 Schema 教程。


---


## 一个通用的 XML 验证器


为了帮助您检查 XML 文件的语法，我们创建了 XML 验证器，以便您对任何 XML 文件进行语法检查。


请看下一章。










	  AI 思考中...





			** [XML 属性](https://www.runoob.com/xml-attributes.html)
			[XML 验证器](https://www.runoob.com/xml-validator.html) **













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

      : ·[XML 实例](https://www.runoob.com/xml-examples.html)

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