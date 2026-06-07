# XSD 空元素

- Source: https://www.runoob.com/schema/schema-complex-empty.html

---


空的复合元素不能包含内容，只能含有属性。


---


## 复合空元素：


一个空的 XML 元素：


<product prodid="1345" />


上面的 "product" 元素根本没有内容。为了定义无内容的类型，我们就必须声明一个在其内容中只能包含元素的类型，但是实际上我们并不会声明任何元素，比如这样：


<xs:element name="product">**

  <xs:complexType>


    <xs:complexContent>


      <xs:restriction base="xs:integer">


        <xs:attribute name="prodid" type="xs:positiveInteger"/>


      </xs:restriction>


    </xs:complexContent>


  </xs:complexType>

</xs:element>


在上面的例子中，我们定义了一个带有复合内容的复合类型。complexContent 元素给出的信号是，我们打算限定或者拓展某个复合类型的内容模型，而 integer 限定则声明了一个属性但不会引入任何的元素内容。


但是，也可以更加紧凑地声明此 "product" 元素：


<xs:element name="product">


  <xs:complexType>


    <xs:attribute name="prodid" type="xs:positiveInteger"/>


  </xs:complexType>

</xs:element>


或者您可以为一个 complexType 元素起一个名字，然后为 "product" 元素设置一个 type 属性并引用这个 complexType 名称（通过使用此方法，若干个元素均可引用相同的复合类型）：


<xs:element name="product" type="prodtype"/>


<xs:complexType name="prodtype">


  <xs:attribute name="prodid" type="xs:positiveInteger"/>

</xs:complexType>








	  AI 思考中...





			** [XML Schema 复合元素](https://www.runoob.com/schema-complex.html)
			[XML Schema 复合类型 – 仅含元素](https://www.runoob.com/schema-complex-elements.html) **













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