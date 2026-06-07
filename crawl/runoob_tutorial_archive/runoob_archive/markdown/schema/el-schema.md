# XML Schema 元素

- Source: https://www.runoob.com/schema/el-schema.html

---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)

---


## 定义和用法


schema 元素定义 schema 的根元素。


### 元素信息


- **父元素：** （无父元素）


### 语法


<schema**
id=ID

attributeFormDefault=qualified|unqualified

elementFormDefault=qualified|unqualified

blockDefault=(#all|list of (extension|restriction|substitution))

finalDefault=(#all|list of (extension|restriction|list|union))

targetNamespace=anyURI

version=token

xmlns=anyURI
*any attributes*

>


((include|import|redefine|annotation)*,(((simpleType|complexType|

group|attributeGroup)|element|attribute|notation),annotation*)*)


</schema>


| 属性 | 描述 |
| --- | --- |
| id | 可选。规定该元素的唯一的 ID。 |
| attributeFormDefault | 可选。在该 schema 的目标命名空间中声明的属性的形式。该值必须是下列字符串之一： "qualified" 或 "unqualified"。 默认值为 "unqualified"。 "unqualified" 指示无须通过命名空间前缀限定目标命名空间的属性。 "qualified" 指示必须通过命名空间前缀限定目标命名空间的属性。 |
| elementFormDefault | 可选。在该 schema 的目标命名空间中声明的元素的形式。该值必须是下列字符串之一： "qualified" 或 "unqualified"。 默认值为 "unqualified"。 "unqualified" 指示无须通过命名空间前缀限定目标命名空间的元素。 "qualified" 指示必须通过命名空间前缀限定目标命名空间的元素。 |
| blockDefault | 可选。规定在目标命名空间中 element 和 complexType 元素上的 block 属性的默认值。block 属性防止具有指定派生类型的复杂类型（或元素）被用来代替继承的复杂类型（或元素）。该值可以包含 #all 或者一个列表，该列表是 extension、restriction 或 substitution 的子集： extension - 防止通过扩展派生的复杂类型被用来替代该复杂类型。 restriction - 防止通过限制派生的复杂类型被用来替代该复杂类型。 substitution - 防止元素的替换。 #all - 防止所有派生的复杂类型被用来替代该复杂类型。 |
| finalDefault | 可选。规定在该架构的目标命名空间中 element、simpleType 和 complexType 元素的 final 属性的默认值。final 属性防止 element、simpleType 或 complexType 元素的指定的派生类型。对于 element 和 complexType 元素，该值可以包含 #all 或一个列表，该列表是 extension 或 restriction 的子集。 对于 simpleType 元素，该值还可以包含 list 和 union： extension - 默认情况下，该 schema 中的元素不能通过扩展派生。仅适用于 element 和 complexType 元素。 restriction - 防止通过限制派生。 list - 防止通过列表派生。仅适用于 simpleType 元素。 union - 防止通过联合派生。仅适用于 simpleType 元素。 #all - 默认情况下，该 schema 中的元素不能通过任何方法派生。 |
| targetNamespace | 该 schema 的命名空间的 URI 引用。还可以分配该命名空间的前缀。如果没有分配任何前缀，则该命名空间的 schema 组件可以和非限定的引用一起使用。 |
| version | 可选。规定 schema 的版本。 |
| xmlns | 规定在此 schema 中使用的一个或多个命名空间的 URI 引用。如果没有分配前缀，该命名空间的 schema 组件可与未限制的引用使用。 |
| any attributes | 可选。规定带有 non-schema 命名空间的任何其他属性。 |


### 实例 1


<?xml version="1.0"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">


<xs:element name="values" type="xs:string">


</xs:schema>


### 实例 2


在本例中，http://www.w3.org/2001/XMLSchema 命名空间中 schema 组件 (element name, type) 是未限制的，而 http://www.w3school.com.cn/w3schoolschema (mystring) 是通过 wsc 前缀限制的：


<?xml version="1.0"?>

<schema xmlns="http://www.w3.org/2001/XMLSchema"

xmlns:wsc="http://www.w3cschool.cc/w3shoolsschema">


<element name="fname" type="wsc:mystring"/>


</schema>


---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)







	  AI 思考中...





			** [XML Schema 总结](https://www.runoob.com/schema-summary.html)
			[XML Schema selector 元素](https://www.runoob.com/el-selector.html) **













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