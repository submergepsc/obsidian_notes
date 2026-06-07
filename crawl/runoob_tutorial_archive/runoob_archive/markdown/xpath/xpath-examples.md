# XPath Examples

- Source: https://www.runoob.com/xpath/xpath-examples.html

---


在本节，让我们通过实例来学习一些基础的 XPath 语法。


---


## XML实例文档


我们将在下面的例子中使用这个 XML 文档：


"books.xml":


<?xml version="1.0" encoding="UTF-8"?>**

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


[在您的浏览器中查看此 "books.xml" 文件](https://www.runoob.com/try/xml/books.xml)。


---


## 加载 XML 文档


所有现代浏览器都支持使用 XMLHttpRequest 来加载 XML 文档的方法。


针对大多数现代浏览器的代码：


var xmlhttp=new XMLHttpRequest()

针对古老的微软浏览器（IE 5 和 6）的代码：


var xmlhttp=new ActiveXObject("Microsoft.XMLHTTP")


---


## 选取节点


不幸的是，Internet Explorer 和其他处理 XPath 的方式不同。


在我们的例子中，包含适用于大多数主流浏览器的代码。


Internet Explorer 使用 selectNodes() 方法从 XML 文档中的选取节点：


xmlDoc.selectNodes(*xpath*);


Firefox、Chrome、Opera 以及 Safari 使用 evaluate() 方法从 XML 文档中选取节点：


xmlDoc.evaluate(*xpath*, xmlDoc, null, XPathResult.ANY_TYPE,null);


---


## 选取所有 title


下面的例子选取所有 title 节点：


## 实例


```xml
/bookstore/book/title
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_xpath_select_cdnodes)


---


## 选取第一个 book 的 title


下面的例子选取 bookstore 元素下面的第一个 book 节点的 title：


## 实例


```xml
/bookstore/book[1]/title
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_xpath_select_cdnodes_first)


这里有一个问题。上面的例子在 IE 和其他浏览器中输出不同的结果。


IE5 以及更高版本将 [0] 视为第一个节点，而根据 W3C 的标准，应该是 [1]。


### 一种解决方法！


为了解决 IE5+ 中 [0] 和 [1] 的问题，可以为 XPath 设置语言选择（SelectionLanguage）。


下面的例子选取 bookstore 元素下面的第一个 book 节点的 title：


## 实例


```xml
xml.setProperty("SelectionLanguage","XPath");xml.selectNodes("/bookstore/book[1]/title");
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_xpath_select_cdnodes_firstIE6SP1)


---


## 选取所有价格


下面的例子选取 price 节点中的所有文本：


## 实例


```xml
/bookstore/book/price/text()
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_xpath_select_pricenodes_text)


---


## 选取价格高于 35 的 price 节点


下面的例子选取价格高于 35 的所有 price 节点：


## 实例


```xml
/bookstore/book[price>35]/price
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_xpath_select_pricenodes_35)


---


## 选取价格高于 35 的 title 节点


下面的例子选取价格高于 35 的所有 title 节点：


## 实例


```xml
/bookstore/book[price>35]/title
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_xpath_select_pricenodes_high)








	  AI 思考中...





			** [XPath 运算符](https://www.runoob.com/xpath-operators.html)
			[XPath 总结](https://www.runoob.com/xpath-summary.html) **













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