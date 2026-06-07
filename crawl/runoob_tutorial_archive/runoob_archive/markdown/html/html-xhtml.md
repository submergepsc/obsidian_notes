# HTML - XHTML

- Source: https://www.runoob.com/html/html-xhtml.html

---


XHTML 是以 XML 格式编写的 HTML。


---


## 什么是 XHTML?


- XHTML 指的是可扩展超文本标记语言
- XHTML 与 HTML 4.01 几乎是相同的
- XHTML 是更严格更纯净的 HTML 版本
- XHTML 是以 XML 应用的方式定义的 HTML
- XHTML 是 [2001 年 1 月](https://www.runoob.com/../w3c/w3c-xhtml.html)发布的 W3C 推荐标准
- XHTML 得到所有主流浏览器的支持


---


## 为什么使用 XHTML?


因特网上的很多页面包含了"糟糕"的 HTML。


如果在浏览器中查看，下面的 HTML 代码运行起来非常正常（即使它并未遵守 HTML 规则）：


```html
<html>
<head>
<meta charset="utf-8">
<title>这是一个不规范的 HTML</title>
<body>
<h1>不规范的 HTML
<p>这是一个段落
</body>
```


XML 是一种必须正确标记且格式良好的标记语言。


如果希望学习 XML，请阅读我们的[XML 教程](https://www.runoob.com/../xml/xml-tutorial.html)。


今日的科技界存在一些不同的浏览器技术。其中一些在计算机上运行，而另一些可能在移动电话或其他小型设备上运行。小型设备往往缺乏解释"糟糕"的标记语言的资源和能力。


所以 - 通过结合 XML 和 HTML 的长处，开发出了 XHTML。XHTML 是作为 XML 被重新设计的 HTML。


---


## 与 HTML 相比最重要的区别：


### 文档结构


- XHTML DOCTYPE 是*强制性的*
-  中的 XML namespace 属性是*强制性的*
- 、、 以及 ** 也是*强制性的*


### 元素语法


- XHTML 元素必须*正确嵌套*
- XHTML 元素必须始终*关闭*
- XHTML 元素必须*小写*
- XHTML 文档必须有*一个根元素*


### 属性语法


- XHTML 属性必须使用*小写*
- XHTML 属性值必须用*引号包围*
- XHTML 属性最小化也是*禁止的*

---


## 是强制性的


XHTML 文档必须进行 XHTML 文档类型声明（XHTML DOCTYPE declaration）。


您可以在菜鸟教程的标签参考手册中找到完整的 [XHTML 文档类型。](https://www.runoob.com/../tags/tag-doctype.html)


, , , 和  元素也必须存在，并且必须使用  中的 xmlns 属性为文档规定 xml 命名空间。


下面的例子展示了带有最少的必需标签的 XHTML 文档：


```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <meta charset="utf-8">
  <title>文档标题</title>
</head>

<body>
文档内容
</body>

</html>
```


---


## XHTML 元素必须合理嵌套


在 HTML 中，一些元素可以不互相嵌套，像这样：


```html
<b><i>粗体和斜体文本</b></i>
```


在 XHTML 中，所有的元素都必须互相合理地嵌套，像这样：


```html
<b><i>粗体和斜体文本</i></b>
```


---


## XHTML 元素必须有关闭标签


错误示例：


```html
<p>这是一个段落
<p>这是另外一个段落
```


正确示例：


```html
<p>这是一个段落</p>
<p>这是另外一个段落</p>
```


---


## 空元素必须包含关闭标签


错误示例：


```html
分行:<br>
水平线: <hr>
图片: <img src="happy.gif" alt="Happy face">
```


正确示例：


```html
分行:<br />
水平线: <hr />
图片: <img src="happy.gif" alt="Happy face" />
```


---


## XHTML 元素必须是小写


错误示例:


```html
<BODY>
<P>这是一个段落</P>
</BODY>
```


正确示例：


```html
<body>
<p>这是一个段落</p>
</body>
```


---


## 属性名称必须是小写


错误示例：


```html
<table WIDTH="100%">
```


正确示例:


```html
<table width="100%">
```


---


## 属性值必须有引号


错误示例：


```html
<table width=100%>
```


正确示例：


```html
<table width="100%">
```


---


## 不允许属性简写


错误示例：


```html
<input checked>
<input readonly>
<input disabled>
<option selected>
```


正确示例：


```html
<input checked="checked">
<input readonly="readonly">
<input disabled="disabled">
<option selected="selected">
```


---


## 如何将 HTML 转换为 XHTML


- 添加一个 XHTML  到你的网页中
- 添加 xmlns 属性添加到每个页面的html元素中。
- 改变所有的元素为小写
- 关闭所有的空元素
- 修改所有的属性名称为小写
- 所有属性值添加引号


---


## 使用 W3C 验证器来测试你的 XHTML


请在下面的输入框中输入您的网址：


*










	  AI 思考中...





			* [HTML 总结](https://www.runoob.com/html-summary.html)
			[HTML5 教程](https://www.runoob.com/html5-intro.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html-examples.html)

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