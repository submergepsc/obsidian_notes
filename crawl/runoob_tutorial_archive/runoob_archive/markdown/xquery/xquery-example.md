# XQuery 实例

- Source: https://www.runoob.com/xquery/xquery-example.html

---


在本节，让我们通过研究一个例子来学习一些基础的 XQuery 语法。


---


## XML 实例文档


我们将在下面的例子中使用这个 XML 文档。


"books.xml":


<?xml version="1.0" encoding="ISO-8859-1"?>**

<bookstore>


<book category="COOKING">


  <title lang="en">Everyday Italian</title>


  <author>Giada De Laurentiis</author>


  <year>2005</year>


  <price>30.00</price>

</book>


<book category="CHILDREN">


  <title lang="en">Harry Potter</title>


  <author>J K. Rowling</author>


  <year>2005</year>


  <price>29.99</price>

</book>


<book category="WEB">


  <title lang="en">XQuery Kick Start</title>


  <author>James McGovern</author>


  <author>Per Bothner</author>


  <author>Kurt Cagle</author>


  <author>James Linn</author>


  <author>Vaidyanathan Nagarajan</author>


  <year>2003</year>


  <price>49.99</price>

</book>


<book category="WEB">


  <title lang="en">Learning XML</title>


  <author>Erik T. Ray</author>


  <year>2003</year>


  <price>39.95</price>

</book>


</bookstore>


[在您的浏览器中查看 "books.xml" 文件](https://www.runoob.com/try/xml/books.xml)。


---


## 如何从 "books.xml" 选取节点？


### 函数


XQuery 使用函数来提取 XML 文档中的数据。


doc() 用于打开 "books.xml" 文件：


doc("books.xml")


### 路径表达式


XQuery 使用路径表达式在 XML 文档中通过元素进行导航。


下面的路径表达式用于在 "books.xml" 文件中选取所有的 title 元素：


doc("books.xml")**/bookstore/book/title**


(/bookstore 选取 bookstore 元素，/book 选取 bookstore 元素下的所有 book 元素，而 /title 选取每个 book 元素下的所有 title 元素)


上面的 XQuery 可提取以下数据：


<title lang="en">Everyday Italian</title>

<title lang="en">Harry Potter</title>

<title lang="en">XQuery Kick Start</title>

<title lang="en">Learning XML</title>


### 谓语


XQuery 使用谓语来限定从 XML 文档所提取的数据。


下面的谓语用于选取 bookstore 元素下的所有 book 元素，并且所选取的 book 元素下的 price 元素的值必须小于 30：


doc("books.xml")/bookstore/book**[price<30]**


上面的 XQuery 可提取到下面的数据：


<book category="CHILDREN">


  <title lang="en">Harry Potter</title>


  <author>J K. Rowling</author>


  <year>2005</year>


  <price>29.99</price>

</book>








	  AI 思考中...





			** [XQuery 简介](https://www.runoob.com/xquery-intro.html)
			[XQuery FLWOR 表达式](https://www.runoob.com/xquery-flwor.html) **













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