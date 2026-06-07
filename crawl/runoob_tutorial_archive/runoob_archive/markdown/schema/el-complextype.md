# XML Schema complexType 元素

- Source: https://www.runoob.com/schema/el-complextype.html

---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)

---


## 定义和用法


complexType 元素定义复杂类型。复杂类型的元素是包含其他元素和/或属性的 XML 元素。


### 元素信息


- **父元素：** element, redefine, schema


### 语法


<complexType**
id=ID

name=NCName

abstract=true|false

mixed=true|false

block=(#all|list of (extension|restriction))

final=(#all|list of (extension|restriction))
*any attributes*

>


(annotation?,(simpleContent|complexContent|((group|all|

choice|sequence)?,((attribute|attributeGroup)*,anyAttribute?))))


</complexType>


（? 符号声明在 complexType 元素中，元素可出现零次或一次，* 符号声明元素可出现零次或多次。）


| 属性 | 描述 |
| --- | --- |
| id | 可选。规定该元素的唯一的 ID。 |
| name | 可选。规定元素的名称。 |
| abstract | 可选。规定在实例文档中是否可以使用复杂类型。如果该值为 true，则元素不能直接使用该复杂类型，而是必须使用从该复杂类型派生的复杂类型。 默认值为 false。 |
| mixed | 可选。规定是否允许字符数据出现在该复杂类型的子元素之间。 默认值为 false。 如果 simpleContent 元素是子元素，则不允许 mixed 属性。 如果 complexContent 元素是子元素，则该 mixed 属性可被 complexContent 元素的 mixed 属性重写。 |
| block | 可选。防止具有指定派生类型的复杂类型被用来替代该复杂类型。该值可以包含 #all 或者一个列表，该列表是 extension 或 restriction 的子集： extension - 防止通过扩展派生的复杂类型被用来替代该复杂类型。 restriction - 防止通过限制派生的复杂类型被用来替代该复杂类型。 #all - 防止所有派生的复杂类型被用来替代该复杂类型。 |
| final | 可选。防止从该 complexType 元素派生指定的类型。该值可以包含 #all 或者一个列表，该列表是 extension 或 restriction 的子集。 extension - 防止通过扩展派生。 restriction - 防止通过限制派生。 #all - 防止所有派生（扩展和限制）。 |
| any attributes | 可选。规定带有 non-schema 命名空间的任何其他属性。 |


### 实例 1


下面的例子拥有一个名为 "note" 的复杂类型元素：


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


### 实例 2


下面的例子中有一个复杂类型 "fullpersoninfo"，它通过使用三个补充的元素 (address、city 和 country) 对继承的类型进行扩展，由另一个复杂类型 "personinfo" 派生而来：


<xs:element name="employee" type="fullpersoninfo"/>


<xs:complexType name="personinfo">

  <xs:sequence>

    <xs:element name="firstname" type="xs:string"/>

    <xs:element name="lastname" type="xs:string"/>

  </xs:sequence>

</xs:complexType>


<xs:complexType name="fullpersoninfo">

  <xs:complexContent>

    <xs:extension base="personinfo">

      <xs:sequence>

        <xs:element name="address" type="xs:string"/>

        <xs:element name="city" type="xs:string"/>

        <xs:element name="country" type="xs:string"/>

      </xs:sequence>

    </xs:extension>

  </xs:complexContent>

</xs:complexType>


在上面的例子中，上面的 "employee" 元素必须按顺序包含下列元素："firstname", "lastname", "address", "city" 以及 "country"。


---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)







	  AI 思考中...





			** [XML Schema complexContent 元素](https://www.runoob.com/el-complexcontent.html)
			[XML Schema documentation 元素](https://www.runoob.com/el-documentation.html) **













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