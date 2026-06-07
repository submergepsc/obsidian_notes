# XML Schema anyAttribute 元素

- Source: https://www.runoob.com/schema/el-anyattribute.html

---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)

---


## 定义和用法


anyAttribute 元素使创作者可以通过未被 schema 规定的属性来扩展 XML 文档。


### 元素信息


- **父元素：** complexType, restriction (both simpleContent and complexContent), extension (both simpleContent and complexContent), attributeGroup


### 语法


<anyAttribute**
id=ID

namespace=namespace

processContents=lax|skip|strict
*any attributes*

>


(annotation?)


</anyAttribute>


（? 符号声明该元素可在 anyAttribute 元素内出现零次或一次。）


| 属性 | 描述 |
| --- | --- |
| id | 可选。规定该元素的唯一的 ID。 |
| namespace | 可选。规定包含可以使用的元素的命名空间。如果没有指定命名空间，则 ##any 为默认值。如果指定命名空间，则必须是以下值之一。 ##any - 来自任何命名空间的元素都可以出现（默认）。 ##other - 来自该元素的父元素的目标命名空间之外的任何命名空间的元素都可以出现。 ##local - 未由命名空间限定的元素可以出现。 ##targetNamespace - 来自包含该元素的父元素的目标命名空间的元素可以出现。 {URI references of namespaces, ##targetNamespace, ##local} 的列表 - 来自通过空格分隔的命名空间列表的元素可以出现。 该列表可以包含以下内容： 命名空间 ##targetNamespace 和 ##local 的 URI 引用。 |
| processContents | 可选。一个指示符，指示应用程序或 XML 处理器应如何根据由该 any 元素指定的元素处理 XML 文档的验证。 如果没有指定 processContents 属性，则默认为 strict。 如果指定了 processContents，必须是以下值之一。 strict - XML 处理器必须获得所需命名空间的架构，并且必须验证来自这些命名空间的所有元素。（默认） lax - 与 strict 相同；但是，即使不能获取该架构，也不会发生任何错误。 skip - XML 处理器不尝试验证来自指定命名空间的所有元素。 |
| any attributes | 可选。规定带有 non-schema 命名空间的任何其他属性。 |


### 实例 1


下面的例子展示了针对 "person" 元素的一个声明。通过使用 元素，创作者能够向 "person" 元素添加任意数量的属性：


<xs:element name="person">

  <xs:complexType>

    <xs:sequence>

      <xs:element name="firstname" type="xs:string"/>

      <xs:element name="lastname" type="xs:string"/>

    </xs:sequence>

    <xs:anyAttribute/>

  </xs:complexType>

</xs:element>


---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)







	  AI 思考中...





			** [XML Schema any 元素](https://www.runoob.com/el-any.html)
			[XML Schema appinfo 元素](https://www.runoob.com/el-appinfo.html) **













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