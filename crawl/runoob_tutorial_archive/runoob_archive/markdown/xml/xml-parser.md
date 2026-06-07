# XML Parser

- Source: https://www.runoob.com/xml/xml-parser.html

---


所有现代浏览器都有内建的 XML 解析器。


XML 解析器把 XML 文档转换为 XML DOM 对象 - 可通过 JavaScript 操作的对象。


---


## 解析 XML 文档


下面的代码片段把 XML 文档解析到 XML DOM 对象中：


if (window.XMLHttpRequest)**
  {// code for IE7+, Firefox, Chrome, Opera, Safari

  xmlhttp=new XMLHttpRequest();

  }

else

  {// code for IE6, IE5

  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");

  }

xmlhttp.open("GET","books.xml",false);

xmlhttp.send();

xmlDoc=xmlhttp.responseXML;


---


## 解析 XML 字符串


下面的代码片段把 XML 字符串解析到 XML DOM 对象中：


txt="<bookstore><book>";

txt=txt+"<title>Everyday Italian</title>";

txt=txt+"<author>Giada De Laurentiis</author>";

txt=txt+"<year>2005</year>";

txt=txt+"</book></bookstore>";


if (window.DOMParser)

  {

  parser=new DOMParser();

  xmlDoc=parser.parseFromString(txt,"text/xml");

  }

else // Internet Explorer

  {

  xmlDoc=new ActiveXObject("Microsoft.XMLDOM");

  xmlDoc.async=false;

  xmlDoc.loadXML(txt);

  }


注释：**Internet Explorer 使用 loadXML() 方法来解析 XML 字符串，而其他浏览器使用 DOMParser 对象。


---


## 跨域访问


出于安全方面的原因，现代的浏览器不允许跨域的访问。


这意味着，网页以及它试图加载的 XML 文件，都必须位于相同的服务器上。


---


## XML DOM


在下一章中，您将学习如何访问 XML DOM 对象并取回数据。

**







	  AI 思考中...





			** [XMLHttpRequest 对象](https://www.runoob.com/xml-http.html)
			[XML DOM](https://www.runoob.com/xml-dom.html) **













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