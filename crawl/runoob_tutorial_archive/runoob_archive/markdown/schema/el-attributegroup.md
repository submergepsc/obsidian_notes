# XML Schema attributeGroup 元素

- Source: https://www.runoob.com/schema/el-attributegroup.html

---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)

---


## 定义和用法


attributeGroup 元素用于对属性声明进行组合，这样这些声明就能够以组合的形式合并到复杂类型中。


### 元素信息


- **父元素：** attributeGroup, complexType, schema, restriction (both simpleContent and complexContent), extension (both simpleContent and complexContent)


### 语法


<attributeGroup**
id=ID

name=NCName

ref=QName
*any attributes*

>


(annotation?),((attribute|attributeGroup)*,anyAttribute?))


</attributeGroup>


（? 符号声明在 attributeGroup 元素中，元素可出现零次或一次，* 符号声明元素可出现零次或多次。）


| 属性 | 描述 |
| --- | --- |
| id | 可选。规定该元素的唯一的 ID。 |
| name | 可选。规定属性组的名称。name 和 ref 属性不能同时出现。 |
| ref | 可选。规定对指定的属性组的引用。name 和 ref 属性不能同时出现。 |
| any attributes | 可选。规定带有 non-schema 命名空间的任何其他属性。 |


### 实例 1


<xs:attributeGroup name="personattr">

  <xs:attribute name="attr1" type="string"/>

  <xs:attribute name="attr2" type="integer"/>

</xs:attributeGroup>


<xs:complexType name="person">

  <xs:attributeGroup ref="personattr"/>

</xs:complexType>


上面的例子定义了一个名为 "personattr" 的属性组，在名为 "person" 的复杂类型中使用。


---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)








	  AI 思考中...





			** [XML Schema attribute 元素](https://www.runoob.com/schema-el-attribute.html)
			[XML Schema choice 元素](https://www.runoob.com/el-choice.html) **













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