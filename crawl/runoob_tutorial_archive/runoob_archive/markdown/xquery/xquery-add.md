# XQuery 添加元素 和属性

- Source: https://www.runoob.com/xquery/xquery-add.html

---


## XML 实例文档


我们将在下面的例子中继续使用这个 "books.xml" 文档（和上面的章节所使用的 XML 文件相同）。


[在您的浏览器中查看 "books.xml" 文件](https://www.runoob.com/try/xml/books.xml)。


---


## 向结果添加元素和属性


正如在前面一节看到的，我们可以在结果中引用输入文件中的元素和属性：


for $x in doc("books.xml")/bookstore/book/title**
order by $x

return $x


上面的 XQuery 表达式会在结果中引用 title 元素和 lang 属性，就像这样：


<title lang="en">Everyday Italian</title>

<title lang="en">Harry Potter</title>

<title lang="en">Learning XML</title>

<title lang="en">XQuery Kick Start</title>


以上 XQuery 表达式返回 title 元素的方式和它们在输入文档中被描述的方式的相同的。


现在我们要向结果添加我们自己的元素和属性！


### 添加 HTML 元素和文本


现在，我们要向结果添加 HTML 元素。我们会把结果放在一个 HTML 列表中：


<html>

<body>


<h1>Bookstore</h1>


<ul>

{

for $x in doc("books.xml")/bookstore/book

order by $x/title

return <li>{data($x/title)}. Category: {data($x/@category)}</li>

}

</ul>


</body>

</html>


以上 XQuery 表达式会生成下面的结果：


<html>

<body>


<h1>Bookstore</h1>


<ul>

<li>Everyday Italian. Category: COOKING</li>

<li>Harry Potter. Category: CHILDREN</li>

<li>Learning XML. Category: WEB</li>

<li>XQuery Kick Start. Category: WEB</li>

</ul>


</body>

</html>


### 向 HTML 元素添加属性


接下来，我们要把 category 属性作为 HTML 列表中的 class 属性来使用：


<html>

<body>


<h1>Bookstore</h1>


<ul>

{

for $x in doc("books.xml")/bookstore/book

order by $x/title

return <li class="{data($x/@category)}">{data($x/title)}</li>

}

</ul>


</body>

</html>


上面的 XQuery 表达式可生成以下结果：


<html>

<body>

<h1>Bookstore</h1>


<ul>

<li class="COOKING">Everyday Italian</li>

<li class="CHILDREN">Harry Potter</li>

<li class="WEB">Learning XML</li>

<li class="WEB">XQuery Kick Start</li>

</ul>


</body>

</html>








	  AI 思考中...





			** [XQuery 语法](https://www.runoob.com/xquery-syntax.html)
			[XQuery 选择和过滤](https://www.runoob.com/xquery-select.html) **













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