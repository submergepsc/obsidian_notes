# XML Schema simpleType 元素

- Source: https://www.runoob.com/schema/el-simpletype.html

---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)

---


## 定义和用法


simpleType 元素定义一个简单类型，规定与具有纯文本内容的元素或属性的值有关的信息以及对它们的约束。


### 元素信息


- **父元素：** attribute, element, list, restriction, schema, union


### 语法


<simpleType**
id=ID

name=NCName
*any attributes*

>


(annotation?,(restriction|list|union))


</simpleType>


(? 符号声明元素可在 simpleType 元素中出现零次或一次。)


| 属性 | 描述 |
| --- | --- |
| id | 可选。规定该元素的唯一的 ID。 |
| name | 类型名称。 该名称必须是在 XML 命名空间规范中定义的无冒号名称 (NCName)。 如果指定，该名称在所有 simpleType 和 complexType 元素之间必须是唯一的。 如果 simpleType 元素是 schema 元素的子元素，则为必选项，在其他时候则是不允许的。 |
| any attributes | 可选。规定带有 non-schema 命名空间的任何其他属性。 |


### 实例 1


本例声明 "age" 元素是一个带有约束的简单类型。age 的值不能小于 0 或大于 100：


<xs:element name="age">

  <xs:simpleType>

    <xs:restriction base="xs:integer">

      <xs:minInclusive value="0"/>

      <xs:maxInclusive value="100"/>

    </xs:restriction>

  </xs:simpleType>

</xs:element>


---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)







	  AI 思考中...





			** [XML Schema simpleContent 元素](https://www.runoob.com/el-simplecontent.html)
			[XML Schema union 元素](https://www.runoob.com/el-union.html) **













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