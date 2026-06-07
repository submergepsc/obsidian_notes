# XML 应用程序

- Source: https://www.runoob.com/xml/xml-applications.html

---


本章演示一些基于 XML, HTML, XML DOM 和 JavaScript 构建的小型 XML 应用程序。


---


## XML 文档实例


在本应用程序中，我们将使用 ["cd_catalog.xml"](https://www.runoob.com/try/xml/cd_catalog.xml) 文件。


---


## 在 HTML div 元素中显示第一个 CD


下面的实例从第一个 CD 元素中获取 XML 数据，然后在 id="showCD" 的 HTML 元素中显示数据。displayCD() 函数在页面加载时调用：


## 实例


```xml
x=xmlDoc.getElementsByTagName("CD");
i=0;
function displayCD()
{
artist=(x[i].getElementsByTagName("ARTIST")[0].childNodes[0].nodeValue);
title=(x[i].getElementsByTagName("TITLE")[0].childNodes[0].nodeValue);
year=(x[i].getElementsByTagName("YEAR")[0].childNodes[0].nodeValue);
txt="Artist: " + artist + "<br />Title: " + title + "<br />Year: "+ year;
document.getElementById("showCD").innerHTML=txt;
}
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryxml_app_first)


---


## 添加导航脚本


为了向上面的实例添加导航（功能），需要创建 next() 和 previous() 两个函数：


## 实例


```xml
function next()
{ // display the next CD, unless you are on the last CD
if (i<x.length-1)
  {
  i++;
  displayCD();
  }
}
function previous()
{ // displays the previous CD, unless you are on the first CD
if (i>0)
  {
  i--;
  displayCD();
  }
}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryxml_app_navigate)


---


## 当点击 CD 时显示专辑信息


最后的实例展示如何在用户点击某个 CD 项目时显示专辑信息：


[尝试一下](https://www.runoob.com/try/tryit.php?filename=tryxml_app)。


如需了解更多关于使用 JavaScript 和 XML DOM 的信息，请访问我们的 [XML DOM 教程](https://www.runoob.com/../dom/dom-tutorial.html)。










	  AI 思考中...





			** [在 HTML 页面中显示 XML 数据](https://www.runoob.com/xml-to-html.html)
			[XML 命名空间](https://www.runoob.com/xml-namespaces.html) **













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