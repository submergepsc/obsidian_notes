# Bootstrap HTML编码规范

- Source: https://www.runoob.com/bootstrap/bootstrap-html-codeguide.html

## 语法


- 用两个空格来代替制表符（tab） -- 这是唯一能保证在所有环境下获得一致展现的方法。
- 嵌套元素应当缩进一次（即两个空格）。
- 对于属性的定义，确保全部使用双引号，绝不要使用单引号。
- 不要在自闭合（self-closing）元素的尾部添加斜线 -- [HTML5 规范](http://dev.w3.org/html5/spec-author-view/syntax.html#syntax-start-tag)中明确说明这是可选的。
- 不要省略可选的结束标签（closing tag）（例如，`` 或 ``）。


实例：


```
<!DOCTYPE html>
<html>
  <head>
    <title>Page title</title>
  </head>
  <body>
    <img src="images/company-logo.png" alt="Company">
    <h1 class="hello-world">Hello, world!</h1>
  </body>
</html>
```


## HTML5 doctype


为每个 HTML 页面的第一行添加标准模式（standard mode）的声明，这样能够确保在每个浏览器中拥有一致的展现。


实例：


```
<!DOCTYPE html>
<html>
  <head>
  </head>
</html>
```


## 语言属性


根据 HTML5 规范：


强烈建议为 html 根元素指定 lang 属性，从而为文档设置正确的语言。这将有助于语音合成工具确定其所应该采用的发音，有助于翻译工具确定其翻译时所应遵守的规则等等。


这里列出了[语言代码表](https://www.runoob.com/../tags/html-language-codes.html)。


```
<html lang="zh">
  <!-- ... -->
</html>
```


## IE 兼容模式


IE 支持通过特定的 `` 标签来确定绘制当前页面所应该采用的 IE 版本。除非有强烈的特殊需求，否则最好是设置为 **edge mode**，从而通知 IE 采用其所支持的最新的模式。


```
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
```


## 字符编码


通过明确声明字符编码，能够确保浏览器快速并容易的判断页面内容的渲染方式。这样做的好处是，可以避免在 HTML 中使用字符实体标记（character entity），从而全部与文档编码一致（一般采用 UTF-8 编码）。


```
<head>
  <meta charset="UTF-8">
</head>
```


## 引入 CSS 和 JavaScript 文件


根据 HTML5 规范，在引入 CSS 和 JavaScript 文件时一般不需要指定 `type` 属性，因为 `text/css` 和 `text/javascript` 分别是它们的默认值。


### HTML5 spec links


- [Using link](http://www.w3.org/TR/2011/WD-html5-20110525/semantics.html#the-link-element)
- [Using style](http://www.w3.org/TR/2011/WD-html5-20110525/semantics.html#the-style-element)
- [Using script](http://www.w3.org/TR/2011/WD-html5-20110525/scripting-1.html#the-script-element)


```
<!-- External CSS -->
<link rel="stylesheet" href="code-guide.css">

<!-- In-document CSS -->
<style>
  /* ... */
</style>

<!-- JavaScript -->
<script src="code-guide.js"></script>
```


## 实用为王


尽量遵循 HTML 标准和语义，但是不要以牺牲实用性为代价。任何时候都要尽量使用最少的标签并保持最小的复杂度。


## 属性顺序


HTML 属性应当按照以下给出的顺序依次排列，确保代码的易读性。


- `class`
- `id`, `name`
- `data-*`
- `src`, `for`, `type`, `href`
- `title`, `alt`
- `aria-*`, `role`


class 用于标识高度可复用组件，因此应该排在首位。id 用于标识具体组件，应当谨慎使用（例如，页面内的书签），因此排在第二位。


```
<a class="..." id="..." data-modal="toggle" href="#">
  Example link
</a>

<input class="form-control" type="text">

<img src="..." alt="...">
```


## 布尔（boolean）型属性


布尔型属性可以在声明时不赋值。XHTML 规范要求为其赋值，但是 HTML5 规范不需要。


更多信息请参考 [WhatWG section on boolean attributes](https://www.whatwg.org/specs/web-apps/current-work/multipage/common-microsyntaxes.html#boolean-attributes)：


元素的布尔型属性如果有值，就是 true，如果没有值，就是 false。


如果*一定*要为其赋值的话，请参考 WhatWG 规范：


如果属性存在，其值必须是空字符串或 [...] 属性的规范名称，并且不要在首尾添加空白符。


**简单来说，就是不用赋值。**


```
<input type="text" disabled>

<input type="checkbox" value="1" checked>

<select>
  <option value="1" selected>1</option>
</select>
```


## 减少标签的数量


编写 HTML 代码时，尽量避免多余的父元素。很多时候，这需要迭代和重构来实现。请看下面的案例：


```
<!-- Not so great -->
<span class="avatar">
  <img src="...">
</span>

<!-- Better -->
<img class="avatar" src="...">
```


## JavaScript 生成的标签


通过 JavaScript 生成的标签让内容变得不易查找、编辑，并且降低性能。能避免时尽量避免。








	  AI 思考中...





			** [Bootstrap v2 教程](https://www.runoob.com/bootstrap-v2-tutorial.html)
			[Bootstrap CSS编码规范](https://www.runoob.com/bootstrap-css-codeguide-html.html) **













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