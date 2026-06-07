# XSD 元素替换(Element Substitution)

- Source: https://www.runoob.com/schema/schema-complex-subst.html

---


通过 XML Schema，一个元素可对另一个元素进行替换。


---


## 元素替换


让我们举例说明：我们的用户来自英国和挪威。我们希望有能力让用户选择在 XML 文档中使用挪威语的元素名称还是英语的元素名称。


为了解决这个问题，我们可以在 XML schema 中定义一个 *substitutionGroup*。首先，我们声明主元素，然后我们会声明次元素，这些次元素可声明它们能够替换主元素。


<xs:element name="name" type="xs:string"/>**
<xs:element name="navn" substitutionGroup="name"/>


在上面的例子中，"name" 元素是主元素，而 "navn" 元素可替代 "name" 元素。


请看一个 XML schema 的片段：


<xs:element name="name" type="xs:string"/>

<xs:element name="navn" substitutionGroup="name"/>


<xs:complexType name="custinfo">


  <xs:sequence>


    <xs:element ref="name"/>


  </xs:sequence>

</xs:complexType>


<xs:element name="customer" type="custinfo"/>

<xs:element name="kunde" substitutionGroup="customer"/>


有效的 XML 文档类似这样（根据上面的 schema）：


<customer>


  <name>John Smith</name>

</customer>


或类似这样：


<kunde>


  <navn>John Smith</navn>

</kunde>


---


## 阻止元素替换


为防止其他的元素替换某个指定的元素，请使用 block 属性：


<xs:element name="name" type="xs:string" block="substitution"/>


请看某个 XML schema 的片段：


<xs:element name="name" type="xs:string" block="substitution"/>

<xs:element name="navn" substitutionGroup="name"/>


<xs:complexType name="custinfo">


  <xs:sequence>


    <xs:element ref="name"/>


  </xs:sequence>

</xs:complexType>


<xs:element name="customer" type="custinfo" block="substitution"/>

<xs:element name="kunde" substitutionGroup="customer"/>


合法的 XML 文档应该类似这样（根据上面的 schema）：


<customer>


  <name>John Smith</name>

</customer>


但是下面的文档不再合法：


<kunde>


  <navn>John Smith</navn>

</kunde>


---


## 使用 substitutionGroup


可替换元素的类型必须和主元素相同，或者从主元素衍生而来。假如可替换元素的类型与主元素的类型相同，那么您就不必规定可替换元素的类型了。


请注意，substitutionGroup 中的所有元素（主元素和可替换元素）必须被声明为全局元素，否则就无法工作！


---


## 什么是全局元素（Global Elements）？


全局元素指 "schema" 元素的直接子元素！本地元素（Local elements）指嵌套在其他元素中的元素。









	  AI 思考中...





			** [XML Schema anyAttribute 元素](https://www.runoob.com/schema-complex-anyattribute.html)
			[XML Schema 实例](https://www.runoob.com/schema-example.html) **













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