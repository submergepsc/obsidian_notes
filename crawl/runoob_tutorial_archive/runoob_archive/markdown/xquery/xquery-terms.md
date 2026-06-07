# XQuery 术语

- Source: https://www.runoob.com/xquery/xquery-terms.html

---


在 XQuery 中，有七种节点：元素、属性、文本、命名空间、处理指令、注释、以及文档节点（或称为根节点）。


---


## XQuery 术语


### 节点


在 XQuery 中，有七种节点：元素、属性、文本、命名空间、处理指令、注释、以及文档（根）节点。XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。


请看下面的 XML 文档：


<?xml version="1.0" encoding="ISO-8859-1"?>**

<bookstore>


<book>


  <title lang="en">Harry Potter</title>


  <author>J K. Rowling</author>


  <year>2005</year>


  <price>29.99</price>

</book>


</bookstore>


上面的 XML 文档中的节点例子：


<bookstore> (文档节点)


<author>J K. Rowling</author> (元素节点)


lang="en" (属性节点)


### 基本值是无父或无子的节点。 基本值的例子： J K. Rowling "en" 项目


项目是基本值或者节点。


---


## 节点关系


### 父（Parent）


每个元素以及属性都有一个父。


在下面的例子中，book 元素是 title、author、year 以及 price 元素的父：


<book>


  <title>Harry Potter</title>


  <author>J K. Rowling</author>


  <year>2005</year>


  <price>29.99</price>

</book>


### 子（Children）


节点元素可有零个、一个或多个子。


在下面的例子中，title、author、year 以及 price 元素都是 book 元素的子：


<book>


  <title>Harry Potter</title>


  <author>J K. Rowling</author>


  <year>2005</year>


  <price>29.99</price>

</book>


### 同胞（Sibling）


拥有相同的父的节点。


在下面的例子中，title、author、year 以及 price 元素都是同胞：


<book>


  <title>Harry Potter</title>


  <author>J K. Rowling</author>


  <year>2005</year>


  <price>29.99</price>

</book>


### 先辈（Ancestor）


某节点的父、父的父，等等。


在下面的例子中，title 元素的先辈是 book 元素和 bookstore元素：


<bookstore>


<book>


  <title>Harry Potter</title>


  <author>J K. Rowling</author>


  <year>2005</year>


  <price>29.99</price>

</book>


</bookstore>


### 后代（Descendant）


某个节点的子，子的子，等等。


在下面的例子中，bookstore 的后代是 book、title、author、year 以及 price元素：


<bookstore>


<book>


  <title>Harry Potter</title>


  <author>J K. Rowling</author>


  <year>2005</year>


  <price>29.99</price>

</book>


</bookstore>








	  AI 思考中...





			** [XQuery FLWOR + HTML](https://www.runoob.com/xquery-flwor-html.html)
			[XQuery 语法](https://www.runoob.com/xquery-syntax.html) **













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