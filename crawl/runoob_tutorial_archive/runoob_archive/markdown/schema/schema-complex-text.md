# XSD 仅含文本

- Source: https://www.runoob.com/schema/schema-complex-text.html

---


仅含文本的复合元素可包含文本和属性。


---


## 仅含文本的复合元素


此类型仅包含简易的内容（文本和属性），因此我们要向此内容添加 simpleContent 元素。当使用简易内容时，我们就必须在 simpleContent 元素内定义扩展或限定，就像这样：


<xs:element name="somename">**

  <xs:complexType>


    <xs:simpleContent>


      <xs:extension base="basetype">


        ....


        ....


      </xs:extension>


    </xs:simpleContent>


  </xs:complexType>

</xs:element>


或者：


<xs:element name="somename">


  <xs:complexType>


    <xs:simpleContent>


      <xs:restriction base="basetype">


        ....


        ....


      </xs:restriction>


    </xs:simpleContent>


  </xs:complexType>

</xs:element>


提示：** 请使用 extension 或 restriction 元素来扩展或限制元素的基本简易类型。 这里有一个 XML 元素的例子，"shoesize"，其中仅包含文本：


<shoesize country="france">35</shoesize>


下面这个例子声明了一个复合类型，其内容被定义为整数值，并且 "shoesize" 元素含有名为 "country" 的属性：


<xs:element name="shoesize">**

  <xs:complexType>


    <xs:simpleContent>


      <xs:extension base="xs:integer">


        <xs:attribute name="country" type="xs:string" />


      </xs:extension>


    </xs:simpleContent>


  </xs:complexType>

</xs:element>


我们也可为 complexType 元素设定一个名称，并让 "shoesize" 元素的 type 属性来引用此名称（通过使用此方法，若干元素均可引用相同的复合类型）：


<xs:element name="shoesize" type="shoetype"/>


<xs:complexType name="shoetype">


  <xs:simpleContent>


    <xs:extension base="xs:integer">


      <xs:attribute name="country" type="xs:string" />


    </xs:extension>


  </xs:simpleContent>

</xs:complexType>








	  AI 思考中...





			** [XML Schema 复合类型 – 仅含元素](https://www.runoob.com/schema-complex-elements.html)
			[XML Schema 复合类型 – 混合内容](https://www.runoob.com/schema-complex-mixed.html) **













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