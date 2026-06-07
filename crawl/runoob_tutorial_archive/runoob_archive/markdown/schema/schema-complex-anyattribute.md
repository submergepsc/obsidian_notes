# XSD 元素

- Source: https://www.runoob.com/schema/schema-complex-anyattribute.html

---


 元素使我们有能力通过未被 schema 规定的属性来扩展 XML 文档！


---


 元素使我们有能力通过未被 schema 规定的属性来扩展 XML 文档！


下面的例子是来自名为 "family.xsd" 的 XML schema 的一个片段。它为我们展示了针对 "person" 元素的一个声明。通过使用  元素，我们就可以向 "person" 元素添加任意数量的属性：


<xs:element name="person">**

  <xs:complexType>


    <xs:sequence>


      <xs:element name="firstname" type="xs:string"/>


      <xs:element name="lastname" type="xs:string"/>


    </xs:sequence>


    <xs:anyAttribute/>


  </xs:complexType>

</xs:element>


现在，我们希望通过 "gender" 属性来扩展 "person" 元素。在这种情况下我们就可以这样做，即使这个 schema 的作者从未声明过任何 "gender" 属性。


请看这个 schema 文件，名为 "attribute.xsd"：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"

targetNamespace="http://www.w3schools.com"

xmlns="http://www.w3schools.com"

elementFormDefault="qualified">


<xs:attribute name="gender">


  <xs:simpleType>


    <xs:restriction base="xs:string">


      <xs:pattern value="male|female"/>


    </xs:restriction>


  </xs:simpleType>

</xs:attribute>


</xs:schema>


下面这个 XML（名为 "Myfamily.xml"），使用了来自不同 schema 的成分，"family.xsd" 和 "attribute.xsd"：


<?xml version="1.0" encoding="ISO-8859-1"?>


<persons xmlns="http://www.microsoft.com"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:SchemaLocation="http://www.microsoft.com family.xsd

http://www.w3schools.com attribute.xsd">


<person gender="female">


<firstname>Hege</firstname>


<lastname>Refsnes</lastname>

</person>


<person gender="male">


<firstname>Stale</firstname>


<lastname>Refsnes</lastname>

</person>


</persons>


上面这个 XML 文件是有效的，这是因为 schema "family.xsd" 允许我们向 "person" 元素添加属性。


 和  均可用于制作可扩展的文档！它们使文档有能力包含未在主 XML schema 中声明过的附加元素。









	  AI 思考中...





			** [XML Schema any 元素](https://www.runoob.com/schema-complex-any.html)
			[XML Schema 元素替换](https://www.runoob.com/schema-complex-subst.html) **













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