# XML Schema group 元素

- Source: https://www.runoob.com/schema/el-group.html

---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)

---


## 定义和用法


group 元素用于定义在复杂类型定义中使用的元素组。


### 元素信息


- **父元素：** schema, choice, sequence, complexType, restriction (both simpleContent and complexContent), extension (both simpleContent and complexContent)


### 语法


<group**
id=ID

name=NCName

ref=QName

maxOccurs=nonNegativeInteger|unbounded

minOccurs=nonNegativeInteger
*any attributes*

>


(annotation?,(all|choice|sequence)?)


</group>


（? 符号声明在 group 元素中，该元素可出现零次或一次。）


| 属性 | 描述 |
| --- | --- |
| id | 可选。规定该元素的唯一的 ID。 |
| name | 可选。规定组的名称。该名称必须是在 XML 命名空间规范中定义的无冒号名称 (NCName)。 仅当 schema 元素是该 group 元素的父元素时才使用该属性。在此情况下，group 是由 complexType、choice 和 sequence 元素使用的模型组。 name 属性和 ref 属性不能同时出现。 |
| ref | 可选。引用另一个组的名称。ref 值必须是 QName。 ref 可以包含命名空间前缀。 name 属性和 ref 属性不能同时出现。 |
| maxOccurs | 可选。规定 group 元素可在父元素中出现的最大次数。该值可以是大于或等于零的整数。若不想对最大次数设置任何限制，请使用字符串 "unbounded"。默认值为 1。 |
| minOccurs | 可选。规定 group 元素可在父元素中出现的最小次数。该值可以是大于或等于零的整数。默认值为 1。 |
| any attributes | 可选。规定带有 non-schema 命名空间的任何其他属性。 |


### 实例 1


下面的例子定义一个包含四个元素的序列的组，并在一个复杂类型定义中使用了这个 group 元素：


<?xml version="1.0"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">


<xs:group name="custGroup">

  <xs:sequence>

    <xs:element name="customer" type="xs:string"/>

    <xs:element name="orderdetails" type="xs:string"/>

    <xs:element name="billto" type="xs:string"/>

    <xs:element name="shipto" type="xs:string"/>

  </xs:sequence>

</xs:group>


<xs:element name="order" type="ordertype"/>


<xs:complexType name="ordertype">

  <xs:group ref="custGroup"/>

  <xs:attribute name="status" type="xs:string"/>

</xs:complexType>


</xs:schema>


---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)







	  AI 思考中...





			** [XML Schema field 元素](https://www.runoob.com/el-field.html)
			[XML Schema import 元素](https://www.runoob.com/schema-el-import.html) **













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