# XQuery FLWOR 表达式

- Source: https://www.runoob.com/xquery/xquery-flwor.html

---


## XML 实例文档


我们将在下面的例子中继续使用这个 "books.xml" 文档（与上一节中的 XML 文件相同）。


[在您的浏览器中查看 "books.xml" 文件](https://www.runoob.com/try/xml/books.xml)。


---


## 如果使用 FLWOR 从 "books.xml" 选取节点


请看下面这个路径表达式：


doc("books.xml")/bookstore/book[price>30]/title


上面这个表达式可选取 bookstore 元素下的 book 元素下所有的 title 元素，并且其中的 price 元素的值必须大于 30。


下面这个 FLWOR 表达式所选取的数据和上面的路径表达式是相同的：


for $x in doc("books.xml")/bookstore/book**
where $x/price>30

return $x/title


输出结果：


<title lang="en">XQuery Kick Start</title>

<title lang="en">Learning XML</title>


通过 FLWOR，您可以对结果进行排序：


for $x in doc("books.xml")/bookstore/book

where $x/price>30

order by $x/title

return $x/title


FLWOR 是 "For, Let, Where, Order by, Return" 的只取首字母缩写。**


**for** 语句把 bookstore 元素下的所有 book 元素提取到名为 $x 的变量中。


**where** 语句选取了 price 元素值大于 30 的 book 元素。


**order by** 语句定义了排序次序。将根据 title 元素进行排序。


**return** 语句规定返回什么内容。在此返回的是 title 元素。


上面的 XQuery 表达式的结果：


<title lang="en">Learning XML</title>**
<title lang="en">XQuery Kick Start</title>









	  AI 思考中...





			** [XQuery 实例](https://www.runoob.com/xquery-example.html)
			[XQuery FLWOR + HTML](https://www.runoob.com/xquery-flwor-html.html) **













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