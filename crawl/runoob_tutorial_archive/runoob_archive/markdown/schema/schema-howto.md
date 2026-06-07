# XSD 如何使用?

- Source: https://www.runoob.com/schema/schema-howto.html

---


XML 文档可对 DTD 或 XML Schema 进行引用。


---


## 一个简单的 XML 文档：


请看这个名为 "note.xml" 的 XML 文档：


<?xml version="1.0"?>**
<note>


<to>Tove</to>


<from>Jani</from>


<heading>Reminder</heading>


<body>Don't forget me this weekend!</body>

</note>


---


## DTD 文件


下面这个例子是名为 "note.dtd" 的 DTD 文件，它对上面那个 XML 文档（ "note.xml" ）的元素进行了定义：


<!ELEMENT note (to, from, heading, body)>

<!ELEMENT to (#PCDATA)>

<!ELEMENT from (#PCDATA)>

<!ELEMENT heading (#PCDATA)>

<!ELEMENT body (#PCDATA)>


第 1 行定义 note 元素有四个子元素："to, from, heading, body"。


第 2-5 行定义了 to, from, heading, body 元素的类型是 "#PCDATA"。


---


## XML Schema


下面这个例子是一个名为 "note.xsd" 的 XML Schema 文件，它定义了上面那个 XML 文档（ "note.xml" ）的元素：


<?xml version="1.0"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"

targetNamespace="http://www.w3schools.com"

xmlns="http://www.w3schools.com"

elementFormDefault="qualified">


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


</xs:schema>


note 元素是一个复合类型，因为它包含其他的子元素。其他元素 (to, from, heading, body) 是简易类型，因为它们没有包含其他元素。您将在下面的章节学习更多有关复合类型和简易类型的知识。


---


## 对 DTD 的引用


此文件包含对 DTD 的引用：


<?xml version="1.0"?>


<!DOCTYPE note SYSTEM

"http://www.w3schools.com/dtd/note.dtd">


<note>


<to>Tove</to>


<from>Jani</from>


<heading>Reminder</heading>


<body>Don't forget me this weekend!</body>

</note>


---


## 对 XML Schema 的引用


此文件包含对 XML Schema 的引用：


<?xml version="1.0"?>


<note

xmlns="http://www.w3schools.com"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:schemaLocation="http://www.w3schools.com note.xsd">

<to>Tove</to>


<from>Jani</from>


<heading>Reminder</heading>


<body>Don't forget me this weekend!</body>

</note>








	  AI 思考中...





			** [为什么使用 XML Schema？](https://www.runoob.com/schema-why.html)
			[XML schema 元素](https://www.runoob.com/schema-schema.html) **













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