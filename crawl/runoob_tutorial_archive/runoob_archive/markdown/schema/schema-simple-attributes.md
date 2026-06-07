# XSD 属性

- Source: https://www.runoob.com/schema/schema-simple-attributes.html

---


所有的属性均作为简易类型来声明。


---


## 什么是属性？


简易元素无法拥有属性。假如某个元素拥有属性，它就会被当作某种复合类型。但是属性本身总是作为简易类型被声明的。


---


## 如何声明属性？


定义属性的语法是


<xs:attribute name="xxx" type="yyy"/>


在此处，xxx 指属性名称，yyy 则规定属性的数据类型。XML Schema 拥有很多内建的数据类型。


### 最常用的类型是：


- xs:string
- xs:decimal
- xs:integer
- xs:boolean
- xs:date
- xs:time


### 实例


这是带有属性的 XML 元素：


<lastname lang="EN">Smith</lastname>


这是对应的属性定义：


<xs:attribute name="lang" type="xs:string"/>

**
---


## 属性的默认值和固定值


属性可拥有指定的默认值或固定值。


当没有其他的值被规定时，默认值就会自动分配给元素。


在下面的例子中，默认值是 "EN"：


<xs:attribute name="lang" type="xs:string" default="EN"/>


固定值同样会自动分配给元素，并且您无法规定另外的值。


在下面的例子中，固定值是 "EN"：


<xs:attribute name="lang" type="xs:string" fixed="EN"/>


---


## 可选的和必需的属性


在默认的情况下，属性是可选的。如需规定属性为必选，请使用 "use" 属性：


<xs:attribute name="lang" type="xs:string" use="required"/>


---


## 对内容的限定


当 XML 元素或属性拥有被定义的数据类型时，就会向元素或属性的内容添加限定。


假如 XML 元素的类型是 "xs:date"，而其包含的内容是类似 "Hello World" 的字符串，元素将不会（通过）验证。


通过 XML schema，您也可向您的 XML 元素及属性添加自己的限定。这些限定被称为 facet（编者注：意为(多面体的)面，可译为限定面）。您会在下一节了解到更多有关 facet 的知识。









	  AI 思考中...





			** [XSD 简易元素](https://www.runoob.com/schema-simple.html)
			[XML Schema 限定 / Facets](https://www.runoob.com/schema-facets.html) **













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