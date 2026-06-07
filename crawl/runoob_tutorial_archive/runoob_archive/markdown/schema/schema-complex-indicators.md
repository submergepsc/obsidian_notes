# XSD 指示器

- Source: https://www.runoob.com/schema/schema-complex-indicators.html

---


通过指示器，我们可以控制在文档中使用元素的方式。


---


## 指示器


有七种指示器：


Order 指示器：


- All
- Choice
- Sequence


Occurrence 指示器：


- maxOccurs
- minOccurs


Group 指示器：


- Group name
- attributeGroup name


---


## Order 指示器


Order 指示器用于定义元素的顺序。


### All 指示器


 指示器规定子元素可以按照任意顺序出现，且每个子元素必须只出现一次：


<xs:element name="person">**

  <xs:complexType>


    <xs:all>


      <xs:element name="firstname" type="xs:string"/>


      <xs:element name="lastname" type="xs:string"/>


    </xs:all>


  </xs:complexType>

</xs:element>


注意：** 当使用  指示器时，你可以把  设置为 0 或者 1，而只能把  指示器设置为 1（稍后将讲解  以及 ）。


### Choice 指示器


 指示器规定可出现某个子元素或者可出现另外一个子元素（非此即彼）：


<xs:element name="person">**

  <xs:complexType>


    <xs:choice>


      <xs:element name="employee" type="employee"/>


      <xs:element name="member" type="member"/>


    </xs:choice>


  </xs:complexType>

</xs:element>


### Sequence 指示器


 规定子元素必须按照特定的顺序出现：


<xs:element name="person">


  <xs:complexType>


    <xs:sequence>


      <xs:element name="firstname" type="xs:string"/>


      <xs:element name="lastname" type="xs:string"/>


    </xs:sequence>


  </xs:complexType>

</xs:element>


---


## Occurrence 指示器


Occurrence 指示器用于定义某个元素出现的频率。


注意： **对于所有的 "Order" 和 "Group" 指示器（any、all、choice、sequence、group name 以及 group reference），其中的 maxOccurs 以及 minOccurs 的默认值均为 1。


### maxOccurs 指示器


 指示器可规定某个元素可出现的最大次数：


<xs:element name="person">**

  <xs:complexType>


    <xs:sequence>


      <xs:element name="full_name" type="xs:string"/>


      <xs:element name="child_name" type="xs:string" maxOccurs="10"/>


    </xs:sequence>


  </xs:complexType>

</xs:element>


上面的例子表明，子元素 "child_name" 可在 "person" 元素中最少出现一次（其中 minOccurs 的默认值是 1），最多出现 10 次。


### minOccurs 指示器


 指示器可规定某个元素能够出现的最小次数：


<xs:element name="person">


  <xs:complexType>


    <xs:sequence>


      <xs:element name="full_name" type="xs:string"/>


      <xs:element name="child_name" type="xs:string"


      maxOccurs="10" minOccurs="0"/>


    </xs:sequence>


  </xs:complexType>

</xs:element>


上面的例子表明，子元素 "child_name" 可在 "person" 元素中出现最少 0 次，最多出现 10 次。


提示：**如需使某个元素的出现次数不受限制，请使用 maxOccurs="unbounded" 这个声明：


### 一个实际的例子：


名为 "Myfamily.xml" 的 XML 文件：


<?xml version="1.0" encoding="ISO-8859-1"?>**

<persons xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:noNamespaceSchemaLocation="family.xsd">


<person>


<full_name>Hege Refsnes</full_name>


<child_name>Cecilie</child_name>

</person>


<person>


<full_name>Tove Refsnes</full_name>


<child_name>Hege</child_name>


<child_name>Stale</child_name>


<child_name>Jim</child_name>


<child_name>Borge</child_name>

</person>


<person>


<full_name>Stale Refsnes</full_name>

</person>


</persons>


上面这个 XML 文件含有一个名为 "persons" 的根元素。在这个根元素内部，我们定义了三个 "person" 元素。每个 "person" 元素必须含有一个 "full_name" 元素，同时它可以包含多至 5 个 "child_name" 元素。


这是schema文件"family.xsd"：


<?xml version="1.0" encoding="ISO-8859-1"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"

elementFormDefault="qualified">


<xs:element name="persons">


  <xs:complexType>


    <xs:sequence>


      <xs:element name="person" maxOccurs="unbounded">


        <xs:complexType>


          <xs:sequence>


            <xs:element name="full_name" type="xs:string"/>


            <xs:element name="child_name" type="xs:string"


            minOccurs="0" maxOccurs="5"/>


          </xs:sequence>


        </xs:complexType>


      </xs:element>


    </xs:sequence>


  </xs:complexType>

</xs:element>


</xs:schema>


---


## Group 指示器


Group 指示器用于定义相关的数批元素。


### 元素组


元素组通过 group 声明进行定义：


<xs:group name="groupname">

  ...

</xs:group>


您必须在 group 声明内部定义一个 all、choice 或者 sequence 元素。下面这个例子定义了名为 "persongroup" 的 group，它定义了必须按照精确的顺序出现的一组元素：


<xs:group name="persongroup">


  <xs:sequence>


    <xs:element name="firstname" type="xs:string"/>


    <xs:element name="lastname" type="xs:string"/>


    <xs:element name="birthday" type="xs:date"/>


  </xs:sequence>

</xs:group>


在您把 group 定义完毕以后，就可以在另一个定义中引用它了：


<xs:group name="persongroup">


  <xs:sequence>


    <xs:element name="firstname" type="xs:string"/>


    <xs:element name="lastname" type="xs:string"/>


    <xs:element name="birthday" type="xs:date"/>


  </xs:sequence>

</xs:group>


<xs:element name="person" type="personinfo"/>


<xs:complexType name="personinfo">


  <xs:sequence>


    <xs:group ref="persongroup"/>


    <xs:element name="country" type="xs:string"/>


  </xs:sequence>

</xs:complexType>


### 属性组


属性组通过 attributeGroup 声明来进行定义：


<xs:attributeGroup name="groupname">

  ...

</xs:attributeGroup>


下面这个例子定义了名为 "personattrgroup" 的一个属性组：


<xs:attributeGroup name="personattrgroup">


  <xs:attribute name="firstname" type="xs:string"/>


  <xs:attribute name="lastname" type="xs:string"/>


  <xs:attribute name="birthday" type="xs:date"/>

</xs:attributeGroup>


在您已定义完毕属性组之后，就可以在另一个定义中引用它了，就像这样：


<xs:attributeGroup name="personattrgroup">


  <xs:attribute name="firstname" type="xs:string"/>


  <xs:attribute name="lastname" type="xs:string"/>


  <xs:attribute name="birthday" type="xs:date"/>

</xs:attributeGroup>


<xs:element name="person">


  <xs:complexType>


    <xs:attributeGroup ref="personattrgroup"/>


  </xs:complexType>

</xs:element>








	  AI 思考中...





			** [XML Schema 复合类型 – 混合内容](https://www.runoob.com/schema-complex-mixed.html)
			[XML Schema any 元素](https://www.runoob.com/schema-complex-any.html) **













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