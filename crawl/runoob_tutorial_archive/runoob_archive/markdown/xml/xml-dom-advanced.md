# XML DOM 高级

- Source: https://www.runoob.com/xml/xml-dom-advanced.html

---


## XML DOM - 高级


在[本教程的较早章节](https://www.runoob.com/xml-dom.html)中，我们介绍了 XML DOM，并使用了 XML DOM 的 getElementsByTagName() 方法从 XML 文档中取回数据。


在本章中我们将结合一些其他重要的 XML DOM 方法。


您可以在我们的 [XML DOM 教程](https://www.runoob.com/../dom/dom-tutorial.html) 中学习更多有关 XML DOM 的知识。


---


## 获取元素的值


下面的实例中使用的 XML 文件：[books.xml](https://www.runoob.com/try/xml/books.xml)。


下面的实例检索第一个  元素的文本值：


## 实例


```xml
txt=xmlDoc.getElementsByTagName("title")[0].childNodes[0].nodeValue;
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryxml_dom_getelement)


---


## 获取属性的值


下面的实例检索第一个  元素的 "lang" 属性的文本值：


## 实例


```xml
txt=xmlDoc.getElementsByTagName("title")[0].getAttribute("lang");
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryxml_dom_getattribute)


---


## 改变元素的值


下面的实例改变第一个  元素的文本值：


## 实例


```xml
x=xmlDoc.getElementsByTagName("title")[0].childNodes[0];
x.nodeValue="Easy Cooking";
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryxml_dom_changeelement)


---


## 创建新的属性


XML DOM 的 setAttribute() 方法可用于改变现有的属性值，或创建一个新的属性。


下面的实例创建了一个新的属性（edition="first"），然后把它添加到每一个  元素中：


## 实例


```xml
x=xmlDoc.getElementsByTagName("book");
for(i=0;i<x.length;i++)
  {
  x[i].setAttribute("edition","first");
  }
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryxml_dom_addattribute)


---


## 创建元素


XML DOM 的 createElement() 方法创建一个新的元素节点。


XML DOM 的 createTextNode() 方法创建一个新的文本节点。


XML DOM 的 appendChild() 方法向节点添加子节点（在最后一个子节点之后）。


如需创建带有文本内容的新元素，需要同时创建元一个新的元素节点和一个新的文本节点，然后把他追加到现有的节点。


下面的实例创建了一个新的元素（），带有如下文本：First，然后把它添加到第一个  元素：


## 实例


```xml
newel=xmlDoc.createElement("edition");
newtext=xmlDoc.createTextNode("First");
newel.appendChild(newtext);
x=xmlDoc.getElementsByTagName("book");
x[0].appendChild(newel);
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryxml_dom_createelement)


实例解释


- 创建一个  元素
- 创建值为 "First" 的文本节点
- 把这个文本节点追加到新的  元素
- 把  元素追加到第一个  元素


---


## 删除元素


下面的实例删除第一个  元素的第一个节点：


## 实例


```xml
x=xmlDoc.getElementsByTagName("book")[0];
x.removeChild(x.childNodes[0]);
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryxml_dom_removeelement)


注释：**上面实例的结果可能会根据所用的浏览器而不同。Firefox 把新行字符当作空的文本节点，而 Internet Explorer 不是这样。您可以在我们的 [XML DOM 教程](https://www.runoob.com/../dom/dom-tutorial.html) 中阅读到更多有关这个问题以及如何避免它的知识。








	  AI 思考中...





			** [服务器上的 XML](https://www.runoob.com/xml-server.html)
			[XML 注意事项](https://www.runoob.com/xml-dont.html) **













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

      : ·[XML 实例](https://www.runoob.com/xml-examples.html)

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