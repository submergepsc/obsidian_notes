# XML - E4X

- Source: https://www.runoob.com/xml/xml-e4x.html

---


E4X 向 JavaScript 添加了对 XML 的直接支持。


---


## E4X 实例


```xml
var employees=
<employees>
<person>
    <name>Tove</name>
    <age>32</age>
</person>
<person>
    <name>Jani</name>
    <age>26</age>
</person>
</employees>;
document.write(employees.person.(name == "Tove").age);
```


**这个实例仅适用于 Firefox！**


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trye4x_demo)


**
---


## 作为一个 JavaScript 对象的 XML


E4X 是正式的 JavaScript 标准，增加了对 XML 的直接支持。


使用 E4X，您可以用声明 Date 或 Array 对象变量的方式声明 XML 对象变量：


var x = new XML()****

var y = new Date()


var z = new Array()


---


## E4X 是一个 ECMAScript（JavaScript）标准


ECMAScript 是 JavaScript 的正式名称。ECMA-262（JavaScript 1.3）是在 1999 年 12 月标准化的。


E4X 是 JavaScript 的扩展，增加了对 XML 的直接支持。ECMA-357（E4X）是在 2004 年 6 月标准化的。


ECMA 组织（成立于 1961 年），是专门用于信息和通信技术（ICT）和消费电子（CE）的标准化。 ECMA 制定的标准为：


- JavaScript
- C# 语言
- 国际字符集
- 光盘
- 磁带
- 数据压缩
- 数据通信
- 等等...


---


## 没有使用 E4X


下面的实例是一个跨浏览器的实例，实例加载一个现有的 XML 文档（"note.xml"）到 XML 解析器，并显示消息说明：


## 实例


```xml
var xmlDoc;
//code for Internet Explorer
if (window.ActiveXObject)
{
xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
xmlDoc.async=false;
xmlDoc.load("note.xml");
displaymessage();
}
// code for Mozilla, Firefox, etc.
else (document.implementation && document.implementation.createDocument)
{
xmlDoc= document.implementation.createDocument("","",null);
xmlDoc.load("note.xml");
xmlDoc.onload=displaymessage;
}
function displaymessage()
{
document.write(xmlDoc.getElementsByTagName("body")[0].firstChild.nodeValue);
}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=note_parsertest_crossbrowser)


---


## 使用 E4X


下面的实例是上面的实例相同，但是使用了 E4X：


var xmlDoc=new XML();

xmlDoc.load("note.xml");

document.write(xmlDoc.body);


简单多了，是不是？


---


## 浏览器支持


Firefox** 是目前唯一对 E4X 的支持比较好的浏览器。


目前还没有支持 E4X 的有 **Opera**、**Chrome** 或 **Safari**。


到目前为止，没有迹象显示在 **Internet Explorer** 中对 E4X 的支持。


---


## E4X 的未来


E4X 没有得到广泛的支持。也许它提供的实用功能太少，尚未被其他的解决方案涉及：


- 对于完整的 XML 处理，您还需要学习 [XML DOM](https://www.runoob.com/../dom/dom-tutorial.html) 和 [XPath](https://www.runoob.com/../xpath/xpath-tutorial.html)
- 对于访问 XMLHttpRequests，[JSON](https://www.runoob.com/../json/json-tutorial.html) 是首选的格式。
- 对于简单的文档处理，[JQuery](https://www.runoob.com/../jquery/jquery-tutorial.html) 选择更容易。

**







	  AI 思考中...





			** [XML 编辑器](https://www.runoob.com/xml-editors.html)
			[XML 总结](https://www.runoob.com/xml-summary.html) **













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