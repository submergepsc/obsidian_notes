# XML Schema element 元素

- Source: https://www.runoob.com/schema/schema-el-element.html

---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)

---


## 定义和用法


element 元素定义一个元素。


### 元素信息


- **父元素：** schema, choice, all, sequence, group


### 语法


<element**
id=ID

name=NCName

ref=QName

type=QName

substitutionGroup=QName

default=string

fixed=string

form=qualified|unqualified

maxOccurs=nonNegativeInteger|unbounded

minOccurs=nonNegativeInteger

nillable=true|false

abstract=true|false

block=(#all|list of (extension|restriction))

final=(#all|list of (extension|restriction))
*any attributes*

>


annotation?,(simpleType|complexType)?,(unique|key|keyref)*


</element>


（? 符号声明在 element 元素中，该元素可出现零次或一次，* 符号声明元素可出现零次或多次。）


| 属性 | 描述 |
| --- | --- |
| id | 可选。规定该元素的唯一的 ID。 |
| name | 可选。规定元素的名称。如果父元素是 schema 元素，则此属性是必需的。 |
| ref | 可选。对另一个元素的引用。ref 属性可包含一个命名空间前缀。如果父元素是 schema 元素，则不是使用该属性。 |
| type | 可选。规定内建数据类型的名称，或者规定 simpleType 或 complexType 元素的名称。 |
| substitutionGroup | 可选。规定可用来替代该元素的元素的名称。 该元素必须具有相同的类型或从指定元素类型派生的类型。 如果父元素不是 schema 元素，则不可以使用该属性。 |
| default | 可选。为元素规定默认值（仅当元素内容是简单类型或 textOnly 时使用）。 |
| fixed | 可选。为元素规定固定值（仅当元素内容是简单类型或 textOnly 时使用）。 |
| form | 可选。该元素的形式。 默认值是包含该属性的 schema 元素的 elementFormDefault 属性的值。 该值必须是下列字符串之一： "qualified" 或 "unqualified"。 如果父元素是 schema 元素，则不能使用该属性。 如果该值是 "unqualified"，则无须通过命名空间前缀限定该元素。 如果该值是 "qualified"，则必须通过命名空间前缀限定该元素。 |
| maxOccurs | 可选。规定 element 元素在父元素中可出现的最大次数。该值可以是大于或等于零的整数。若不想对最大次数设置任何限制，请使用字符串 "unbounded"。 默认值为 1。 如果父元素是 schema 元素，则不能使用该属性。 |
| minOccurs | 可选。规定 element 元素在父元素中可出现的最小次数。该值可以是大于或等于零的整数。默认值为 1。 如果父元素是 schema 元素，则不能使用该属性。 |
| nillable | 可选。指示是否可以将显式的零值分配给该元素。此项应用于元素内容并且不是该元素的属性。 默认值为 false。 如果 nillable 为 true，将使该元素的实例可以将 nil 属性设置为 true。 nil 属性被定义为实例的 XML 架构命名空间的一部分。 |
| abstract | 可选。指示元素是否可以在实例文档中使用。如果该值为 true，则元素不能出现在实例文档中。 相反，substitutionGroup 属性包含该元素的限定名 (QName) 的其他元素必须出现在该元素的位置。多个元素可以在其 substitutionGroup 属性中引用该元素。默认值是 false。 |
| block | 可选。派生的类型。 block 属性防止具有指定派生类型的元素被用于替代该元素。该值可以包含 #all 或者一个列表，该列表是 extension、restriction 或 substitution 的子集： extension - 防止通过扩展派生的元素被用来替代该元素。 restriction - 防止通过限制派生的元素被用来替代该元素。 substitution - 防止通过替换派生的元素被用来替代该元素。 #all - 防止所有派生的元素被用来替代该元素。 |
| final | 可选。设置 element 元素上 final 属性的默认值。如果父元素不是 schema 元素，则不能使用该属性。该值可以包含 #all 或者一个列表，该列表是 extension 或 restriction 的子集： extension - 防止通过扩展派生的元素被用来替代该元素 restriction - 防止通过限制派生的元素被用来替代该元素 #all - 防止所有派生的元素被用来替代该元素 |
| any attributes | 可选。规定带有 non-schema 命名空间的任何其他属性。 |


### 实例 1


下面的例子是一个schema，其中带有四个简单元素："fname", "lname", "age" 以及 "dateborn"，类型是 string、nonNegativeInteger 以及 date：


<?xml version="1.0"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">


<xs:element name="fname" type="xs:string"/>

<xs:element name="lname" type="xs:string"/>

<xs:element name="age" type="xs:nonNegativeInteger"/>

<xs:element name="dateborn" type="xs:date"/>


</xs:schema>


### 实例 2


下面的例子是一个带有复杂类型 "note" 元素的 schema。"note" 元素包含四个简单元素："to", "from", "heading" 以及 "body":


<?xml version="1.0"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">


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


### 实例 3


本例与例子 2 相同，但是在此例中，我们选择使用 ref 属性来引用元素名称：


<?xml version="1.0"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">


<xs:element name="note">

  <xs:complexType>

    <xs:sequence>

    <xs:element ref="to"/>

    <xs:element ref="from"/>

    <xs:element ref="heading"/>

    <xs:element ref="body"/>

    </xs:sequence>

  </xs:complexType>

</xs:element>


<xs:element name="to" type="xs:string"/>

<xs:element name="from" type="xs:string"/>

<xs:element name="heading" type="xs:string"/>

<xs:element name="body" type="xs:string"/>


</xs:schema>


---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)







	  AI 思考中...





			** [XML Schema documentation 元素](https://www.runoob.com/el-documentation.html)
			[XML Schema extension 元素](https://www.runoob.com/el-extension.html) **













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