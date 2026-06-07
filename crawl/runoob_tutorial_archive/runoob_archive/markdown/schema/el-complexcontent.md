# XML Schema complexContent 元素

- Source: https://www.runoob.com/schema/el-complexcontent.html

---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)

---


## 定义和用法


complexContent 元素定义对复杂类型（包含混合内容或仅包含元素）的扩展或限制。


### 元素信息


- **父元素：** complexType


### 语法


<complexContent**
id=ID

mixed=true|false*

any attributes*

>


(annotation?,(restriction|extension))


</complexContent>


（? 符号声明元素可在 complexContent 元素内出现零次或一次。）


| 属性 | 描述 |
| --- | --- |
| id | 可选。规定该元素的唯一的 ID。 |
| mixed | 可选。规定是否允许字符数据出现在该 complexType 元素的子元素之间。 默认值为 false。 |
| any attributes | 可选。规定带有 non-schema 命名空间的任何其他属性。 |


### 实例 1


下面的例子中有一个复杂类型 "fullpersoninfo"，这个复杂类型是通过用三个补充的元素扩展继承的类型，从另一个复杂类型 "personinfo" 衍生而来的：


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


在上例中，"employee" 元素必须按顺序包含下面的元素："firstname"、"lastname"、"address"、"city" 以及 "country"。


---

[![XML Schema 参考手册](https://www.runoob.com/images/up.gif) 完整 XML Schema 参考手册](https://www.runoob.com/schema-elements-ref.html)







	  AI 思考中...





			** [XML Schema choice 元素](https://www.runoob.com/el-choice.html)
			[XML Schema complexType 元素](https://www.runoob.com/el-complextype.html) **













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