# XSD 简易元素

- Source: https://www.runoob.com/schema/schema-simple.html

---


XML Schema 可定义 XML 文件的元素。


简易元素指那些只包含文本的元素。它不会包含任何其他的元素或属性。


---


## 什么是简易元素？


简易元素指那些仅包含文本的元素。它不会包含任何其他的元素或属性。


不过，"仅包含文本"这个限定却很容易造成误解。文本有很多类型。它可以是 XML Schema 定义中包括的类型中的一种（布尔、字符串、数据等等），或者它也可以是您自行定义的定制类型。


您也可向数据类型添加限定（即 facets），以此来限制它的内容，或者您可以要求数据匹配某种特定的模式。


---


## 定义简易元素


定义简易元素的语法：


<xs:element name="xxx" type="yyy"/>


此处 xxx 指元素的名称，yyy 指元素的数据类型。XML Schema 拥有很多内建的数据类型。


### 最常用的类型是：


- xs:string
- xs:decimal
- xs:integer
- xs:boolean
- xs:date
- xs:time


### 实例


这是一些 XML 元素：


<lastname>Refsnes</lastname>**
<age>36</age>

<dateborn>1970-03-27</dateborn>


这是相应的简易元素定义：


<xs:element name="lastname" type="xs:string"/>

<xs:element name="age" type="xs:integer"/>

<xs:element name="dateborn" type="xs:date"/>


---


## 简易元素的默认值和固定值


简易元素可拥有指定的默认值或固定值。


当没有其他的值被规定时，默认值就会自动分配给元素。


在下面的例子中，默认值是 "red"：


<xs:element name="color" type="xs:string" default="red"/>


固定值同样会自动分配给元素，并且您无法规定另外一个值。


在下面的例子中，固定值是 "red"：


<xs:element name="color" type="xs:string" fixed="red"/>








	  AI 思考中...





			** [XML schema 元素](https://www.runoob.com/schema-schema.html)
			[XML Schema 属性](https://www.runoob.com/schema-simple-attributes.html) **













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