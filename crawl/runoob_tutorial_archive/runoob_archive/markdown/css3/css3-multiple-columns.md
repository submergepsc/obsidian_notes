# CSS3 多列

- Source: https://www.runoob.com/css3/css3-multiple-columns.html

CSS3 可以将文本内容设计成像报纸一样的多列布局，如下实例:


菜鸟教程 - 学的不仅是技术，更是梦想！菜鸟教程(www.runoob.com)提供了最全的编程技术基础教程, 介绍了HTML、CSS、Javascript、Python，Java，Ruby，C，PHP , MySQL等各种编程语言的基础知识。 同时本站中也提供了大量的在线实例，通过实例，您可以更好的学习编程。


---


## 浏览器支持


表格中的数字表示支持该方法的第一个浏览器的版本号。

紧跟在数字后面的 -webkit- 或 -moz- 为指定浏览器的前缀。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| column-count | 4.0 -webkit- | 10.0 | 2.0 -moz- | 3.1 -webkit- | 15.0 -webkit-11.1 |
| column-gap | 4.0 -webkit- | 10.0 | 2.0 -moz- | 3.1 -webkit- | 15.0 -webkit-11.1 |
| column-rule | 4.0 -webkit- | 10.0 | 2.0 -moz- | 3.1 -webkit- | 15.0 -webkit-11.1 |
| column-rule-color | 4.0 -webkit- | 10.0 | 2.0 -moz- | 3.1 -webkit- | 15.0 -webkit11.1 |
| column-rule-style | 4.0 -webkit- | 10.0 | 2.0 -moz- | 3.1 -webkit- | 15.0 -webkit11.1 |
| column-rule-width | 4.0 -webkit- | 10.0 | 2.0 -moz- | 3.1 -webkit- | 15.0 -webkit11.1 |
| column-width | 4.0 -webkit- | 10.0 | 2.0 -moz- | 3.1 -webkit- | 15.0 -webkit11.1 |


---


## CSS3 多列属性


本章节我们将学习以下几个 CSS3 的多列属性:


- `column-count`
- `column-gap`
- `column-rule-style`
- `column-rule-width`
- `column-rule-color`
- `column-rule`
- `column-span`
- `column-width`


---


## CSS3 创建多列


`column-count` 属性指定了需要分割的列数。


以下实例将  元素中的文本分为 3 列：


### 实例


```css
div
{

	-webkit-column-count: 3; /* Chrome, Safari, Opera */

-moz-column-count: 3; /* Firefox */
    column-count: 3;
}
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_column-count)


---


## CSS3 多列中列与列间的间隙


`column-gap` 属性指定了列与列间的间隙。


以下实例指定了列与列间的间隙为 40 像素：


### 实例


```css
div
{

	-webkit-column-gap: 40px; /* Chrome, Safari, Opera */

-moz-column-gap: 40px; /* Firefox */

column-gap: 40px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_column-gap)


---


## CSS3 列边框


`column-rule-style` 属性指定了列与列间的边框样式：


### 实例


```css
div
{

	-webkit-column-rule-style: solid; /* Chrome, Safari, Opera */

-moz-column-rule-style: solid; /* Firefox */

column-rule-style: solid;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_column-rule-style)


`column-rule-width` 属性指定了两列的边框厚度:


### 实例


```css
div
{

	-webkit-column-rule-width: 1px; /* Chrome, Safari, Opera */

-moz-column-rule-width: 1px; /* Firefox */

column-rule-width: 1px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_column-rule-width)


`column-rule-color` 属性指定了两列的边框颜色：


### 实例


```css
div
{

	-webkit-column-rule-color: lightblue; /* Chrome, Safari, Opera */

-moz-column-rule-color: lightblue; /* Firefox */

column-rule-color: lightblue;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_column-rule-color)


`column-rule` 属性是 column-rule-* 所有属性的简写。


以下实例设置了列直接的边框的厚度，样式及颜色：


### 实例


```css
div
{

	-webkit-column-rule: 1px solid lightblue; /* Chrome, Safari, Opera */

-moz-column-rule: 1px solid lightblue; /* Firefox */

column-rule: 1px solid lightblue;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_column-rule)


---


## 指定元素跨越多少列


以下实例指定  元素跨越所有列：


### 实例


```css
h2 {

	-webkit-column-span: all; /* Chrome, Safari, Opera */

column-span: all;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_column-span)


---


## 指定列的宽度


`column-width` 属性指定了列的宽度。


### 实例


```css
div {

	-webkit-column-width: 100px; /* Chrome, Safari, Opera */

column-width: 100px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_column-width)


---


## CSS3 多列属性


下表列出了所有 CSS3 的多列属性：


| 属性 | 描述 |
| --- | --- |
| column-count | 指定元素应该被分割的列数。 |
| column-fill | 指定如何填充列 |
| column-gap | 指定列与列之间的间隙 |
| column-rule | 所有 column-rule-* 属性的简写 |
| column-rule-color | 指定两列间边框的颜色 |
| column-rule-style | 指定两列间边框的样式 |
| column-rule-width | 指定两列间边框的厚度 |
| column-span | 指定元素要跨越多少列 |
| column-width | 指定列的宽度 |
| columns | column-width 与 column-count 的简写属性。 |








	  AI 思考中...





			** [CSS3 动画](https://www.runoob.com/css3-animations.html)
			[CSS3 用户界面](https://www.runoob.com/css3-user-interface.html) **













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