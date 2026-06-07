# XSD 混合内容

- Source: https://www.runoob.com/schema/schema-complex-mixed.html

---


混合的复合类型可包含属性、元素以及文本。


---


## 带有混合内容的复合类型


XML 元素，"letter"，含有文本以及其他元素：


<letter>**

Dear Mr.<name>John Smith</name>.


Your order <orderid>1032</orderid>


will be shipped on <shipdate>2001-07-13</shipdate>.

</letter>


下面这个 schema 声明了这个 "letter" 元素：


<xs:element name="letter">


  <xs:complexType mixed="true">


    <xs:sequence>


      <xs:element name="name" type="xs:string"/>


      <xs:element name="orderid" type="xs:positiveInteger"/>


      <xs:element name="shipdate" type="xs:date"/>


    </xs:sequence>


  </xs:complexType>

</xs:element>


注意：** 为了使字符数据可以出现在 "letter" 的子元素之间，mixed 属性必须被设置为 "true"。 标签 (name、orderid 以及 shipdate ) 意味着被定义的元素必须依次出现在 "letter" 元素内部。


我们也可以为 complexType 元素起一个名字，并让 "letter" 元素的 type 属性引用 complexType 的这个名称（通过这个方法，若干元素均可引用同一个复合类型）：


<xs:element name="letter" type="lettertype"/>**

<xs:complexType name="lettertype" mixed="true">


  <xs:sequence>


    <xs:element name="name" type="xs:string"/>


    <xs:element name="orderid" type="xs:positiveInteger"/>


    <xs:element name="shipdate" type="xs:date"/>


  </xs:sequence>

</xs:complexType>








	  AI 思考中...





			** [XML Schema 复合元素 – 仅含文本](https://www.runoob.com/schema-complex-text.html)
			[XML Schema 指示器](https://www.runoob.com/schema-complex-indicators.html) **













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