# XQuery FLWOR + HTML

- Source: https://www.runoob.com/xquery/xquery-flwor-html.html

---


## XML 实例文档


我们将在下面的例子中继续使用这个 "books.xml" 文档（与上一节中的文件相同）。


[在您的浏览器中查看 "books.xml" 文件](https://www.runoob.com/try/xml/books.xml)。


---


## 在一个 HTML 列表中提交结果


请看下面的 XQuery FLWOR 表达式：


for $x in doc("books.xml")/bookstore/book/title**
order by $x

return $x


上面的表达式会选取 bookstore 元素下的 book 元素下的所有 title 元素，并以字母顺序返回 title 元素。


现在，我们希望使用 HTML 列表列出我们的书店中所有的书目。我们向 FLWOR 表达式添加  和  标签：


**<ul>

{**

for $x in doc("books.xml")/bookstore/book/title

order by $x

return **<li>{**$x**}</li>

}

</ul>**


以上代码输出结果：


<ul>

<li><title lang="en">Everyday Italian</title></li>

<li><title lang="en">Harry Potter</title></li>

<li><title lang="en">Learning XML</title></li>

<li><title lang="en">XQuery Kick Start</title></li>

</ul>


现在我们希望去除 title 元素，而仅仅显示 title 元素内的数据。


<ul>

{

for $x in doc("books.xml")/bookstore/book/title

order by $x

return <li>{**data(**$x**)**}</li>

}

</ul>


结果将是一个 HTML 列表：


<ul>

<li>Everyday Italian</li>

<li>Harry Potter</li>

<li>Learning XML</li>

<li>XQuery Kick Start</li>

</ul>








	  AI 思考中...





			** [XQuery FLWOR 表达式](https://www.runoob.com/xquery-flwor.html)
			[XQuery 术语](https://www.runoob.com/xquery-terms.html) **













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