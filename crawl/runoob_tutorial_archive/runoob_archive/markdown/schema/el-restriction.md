# XML Schema restriction 元素

- Source: https://www.runoob.com/schema/el-restriction.html

---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)

---


## 定义和用法


restriction 元素定义对 simpleType、simpleContent 或 complexContent 定义的约束。


### 元素信息


- **父元素：** simpleType, simpleContent, complexContent


### 语法


<restriction**
id=ID

base=QName
*any attributes*

>


Content for simpleType:

(annotation?,(simpleType?,(minExclusive|minInclusive|

maxExclusive|maxInclusive|totalDigits|fractionDigits|

length|minLength|maxLength|enumeration|whiteSpace|pattern)*))


Content for simpleContent:

(annotation?,(simpleType?,(minExclusive |minInclusive|

maxExclusive|maxInclusive|totalDigits|fractionDigits|

length|minLength|maxLength|enumeration|whiteSpace|pattern)*)?,

((attribute|attributeGroup)*,anyAttribute?))


Content for complexContent:

(annotation?,(group|all|choice|sequence)?,

((attribute|attributeGroup)*,anyAttribute?))


</restriction>


（? 符号声明在 restriction 元素中该元素可出现零次或一次。）


| 属性 | 描述 |
| --- | --- |
| id | 可选。规定该元素的唯一的 ID。 |
| base | 必需。规定在该 schema（或由指定的命名空间指示的其他 schema）中定义的内建数据类型、simpleType 或 complexType 元素的名称。 |
| any attributes | 可选。规定带有 non-schema 命名空间的任何其他属性。 |


### 实例 1


下面的例子定义了一个带有约束且名为 "age" 的元素。age 的值不能小于 0 或大于 100：


<xs:element name="age">

  <xs:simpleType>

    <xs:restriction base="xs:integer">

      <xs:minInclusive value="0"/>

      <xs:maxInclusive value="100"/>

    </xs:restriction>

  </xs:simpleType>

</xs:element>


### 实例 2


本例定义了一个名为 "initials" 的元素。"initials" 元素是带有约束的简单类型。可接受的值是三个从 a 到 z 的大写或小写字母：


<xs:element name="initials">

  <xs:simpleType>

    <xs:restriction base="xs:string">

      <xs:pattern value="[a-zA-Z][a-zA-Z][a-zA-Z]"/>

    </xs:restriction>

  </xs:simpleType>

</xs:element>


### 实例 3


本例定义了一个名为 "password" 元素。"password" 元素是带有约束的简单类型。值必须为最少 5 个字符且最多 8 个字符：


<xs:element name="password">

  <xs:simpleType>

    <xs:restriction base="xs:string">

      <xs:minLength value="5"/>

      <xs:maxLength value="8"/>

    </xs:restriction>

  </xs:simpleType>

</xs:element>


### 实例 4


本例展示了一个使用约束的复杂类型定义。复杂类型 "Chinese_customer" 从一个普通的 customer 复杂类型派生而来，其 country 元素的固定值是 "China"：


<xs:complexType name="customer">

  <xs:sequence>

    <xs:element name="firstname" type="xs:string"/>

    <xs:element name="lastname" type="xs:string"/>

    <xs:element name="country" type="xs:string"/>

  </xs:sequence>

</xs:complexType>


<xs:complexType name="Norwegian_customer">

  <xs:complexContent>

    <xs:restriction base="customer">

      <xs:sequence>

        <xs:element name="firstname" type="xs:string"/>

        <xs:element name="lastname" type="xs:string"/>

        <xs:element name="country" type="xs:string" fixed="Norway"/>

      </xs:sequence>

    </xs:restriction>

  </xs:complexContent>

</xs:complexType>


---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)







	  AI 思考中...





			** [XML Schema redefine 元素](https://www.runoob.com/el-redefine.html)
			[XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html) **













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