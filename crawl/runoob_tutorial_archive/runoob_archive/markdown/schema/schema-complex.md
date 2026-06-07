# XSD 复合元素

- Source: https://www.runoob.com/schema/schema-complex.html

---


复合元素包含了其他的元素及/或属性。


---


## 什么是复合元素？


复合元素指包含其他元素及/或属性的 XML 元素。


### 有四种类型的复合元素：


- 空元素
- 包含其他元素的元素
- 仅包含文本的元素
- 包含元素和文本的元素


**注意：** 上述元素均可包含属性！


---


## 复合元素的例子


复合元素，"product"，是空的：


<product pid="1345"/>


复合元素，"employee"，仅包含其他元素：


<employee>**

<firstname>John</firstname>


<lastname>Smith</lastname>

</employee>


复合 XML 元素，"food"，仅包含文本：


<food type="dessert">Ice cream</food>


复合XML元素，"description"包含元素和文本：


<description>

It happened on <date lang="norwegian">03.03.99</date> ....

</description>


---


## 如何定义复合元素？


请看这个复合 XML 元素，"employee"，仅包含其他元素：


<employee>


<firstname>John</firstname>


<lastname>Smith</lastname>

</employee>


在 XML Schema 中，我们有两种方式来定义复合元素：


1. 通过命名此元素，可直接对"employee"元素进行声明，就像这样：


<xs:element name="employee">


  <xs:complexType>


    <xs:sequence>


      <xs:element name="firstname" type="xs:string"/>


      <xs:element name="lastname" type="xs:string"/>


    </xs:sequence>


  </xs:complexType>

</xs:element>


假如您使用上面所描述的方法，那么仅有 "employee" 可使用所规定的复合类型。请注意其子元素，"firstname" 以及 "lastname"，被包围在指示器 中。这意味着子元素必须以它们被声明的次序出现。您会在 [XSD 指示器](https://www.runoob.com/schema-complex-indicators.html) 这一节学习更多有关指示器的知识。


2. "employee" 元素可以使用 type 属性，这个属性的作用是引用要使用的复合类型的名称：


<xs:element name="employee" type="personinfo"/>


<xs:complexType name="personinfo">


  <xs:sequence>


    <xs:element name="firstname" type="xs:string"/>


    <xs:element name="lastname" type="xs:string"/>


  </xs:sequence>

</xs:complexType>


如果您使用了上面所描述的方法，那么若干元素均可以使用相同的复合类型，比如这样：


<xs:element name="employee" type="personinfo"/>

<xs:element name="student" type="personinfo"/>

<xs:element name="member" type="personinfo"/>


<xs:complexType name="personinfo">


  <xs:sequence>


    <xs:element name="firstname" type="xs:string"/>


    <xs:element name="lastname" type="xs:string"/>


  </xs:sequence>

</xs:complexType>


您也可以在已有的复合元素之上以某个复合元素为基础，然后添加一些元素，就像这样：


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








	  AI 思考中...





			** [XML Schema 限定 / Facets](https://www.runoob.com/schema-facets.html)
			[XML Schema 复合空元素](https://www.runoob.com/schema-complex-empty.html) **













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