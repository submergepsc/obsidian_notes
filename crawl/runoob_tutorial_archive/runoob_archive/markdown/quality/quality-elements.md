# Web 品质 - 重要的 HTML 元素

- Source: https://www.runoob.com/quality/quality-elements.html

---


对于提升 web 品质，、 以及  都是重要的标签。


---


## 元素


所有的 HTML 和 XHTML 页面都应当使用  元素来定义遵照何种 HTML 版本。


doctype 定义了您正在使用的 HTML 版本，并为浏览器提供重要的信息以便其更快速一致地呈现您的页面。


文档类型声明同时也使验证软件可以对页面的语法进行检查：


### HTML 5


```
<!DOCTYPE html>
```


### HTML 4.01 Strict, Transitional, Frameset


```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN"
"http://www.w3.org/TR/html4/frameset.dtd">
```


### XHTML 1.0 Strict, Transitional, Frameset


```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
```


### XHTML 1.1


```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
```


**
---


## 元素


 元素是最重要的 HTML 元素之一。它的主要功能是描述网页的内容。


即使标题不是网页的一个可见的部分，它对于提升网站的品质依然是重要的，这是因为它在以下位置都是可见的：


- 搜索引擎列表
- 窗口的标题栏
- 用户的书签中


标题应当尽可能地短，并具有可描述性。


当某个用户在 internet 上搜索网站时，大部分搜索引擎都会在搜索结果中显示出网站的标题。请确保标题与网页的内容是吻合的。这样的话用户有更多的可能通过点击这些链接来访问到你的网站。


当用户访问您的网站时，在窗口的标题栏中标题是可见的。请确保即使窗口被最小化，标题同样能起到描述网站内容的作用。


在用户访问你的网站之后，网页的标题会存储于历史文件夹（用户甚至会把网页收藏到他的收藏夹中）。为了后续的成功访问，同样请确保标题可以清楚地描述您的网站。


优秀的标题：**


## 实例


```
<title>HTML Tutorial</title>

<title>XML Introduction</title>
```


**不好得标题例子：:**


## 实例


```
<title>Introduction</title>

<title>Chapter 1</title>
```


菜鸟教程拥有一整套组织良好、易于理解的 HTML、CSS、JavaScript、 DHTML、XML、XHTML、WAP、ASP、SQL 教程，并包含非常多实例和源代码。


---


## 元素


 元素用来描述网页中最上层的标题。


由于一些浏览器会默认地把  元素显示为很大的字体，因此会有一些 web 开发者使用  元素代替  元素来显示最上层的标题。这样做不会对读者产生影响，但会使那些试图"理解网页结构"的搜索引擎和其他软件感到迷惑。


请确保把  用于最顶层的标题， 和  用于较低的层级。


可以试着根据此模版来构造您的网页：


| # This is the main heading Some initial text ## This is a level 2 heading This is some text. This is some text. This is some text. ### This is a level 3 heading This is some text. This is some text. This is some text. ### This is a level 3 heading This is some text. This is some text. This is some text. |
| --- |


如果您不喜欢默认的标题字体尺寸，可以使用样式或样式表来改变。








	  AI 思考中...





			** [Web 品质标准](https://www.runoob.com/quality-standards.html)
			[Web 品质国际化](https://www.runoob.com/quality-international.html) **













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