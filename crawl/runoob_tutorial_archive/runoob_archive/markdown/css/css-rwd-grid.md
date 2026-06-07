# 响应式 Web 设计 - 网格视图

- Source: https://www.runoob.com/css/css-rwd-grid.html

---


## 什么是网格视图?


很多网页都是基于网格设计的，这说明网页是按列来布局的。

![](https://www.runoob.com/wp-content/uploads/2015/06/viewgrid1.jpg)

使用网格视图有助于我们设计网页。这让我们向网页添加元素变的更简单。

![](https://www.runoob.com/wp-content/uploads/2015/06/viewgrid2.jpg)

响应式网格视图通常是 12 列，宽度为100%，在浏览器窗口大小调整时会自动伸缩。


[响应式网格视图](https://www.runoob.com/try/demo_source/tryresponsive_grid.htm) --- ## 创建响应式网格视图 接下来我们来创建一个响应式网格视图。


首先确保所有的 HTML 元素都有 **box-sizing** 属性且设置为 **border-box**。


确保边距和边框包含在元素的宽度和高度间。


添加如下代码：


```
* {
    box-sizing: border-box;
}
```


查看更多 box-sizing 内容请点击：[CSS3 box-sizing 属性](https://www.runoob.com/../cssref/css3-pr-box-sizing.html)。


以下实例演示了简单的响应式网页，包含两列：


## 实例


```css
.menu {    width: 25%;
	float: left;}
	.main {    width: 75%;
	float: left;}
```


	**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_webpage)

以上实例包含两列。

12 列的网格系统可以更好的控制响应式网页。

首先我们可以计算每列的百分比: 100% / 12 列 = 8.33%。

在每列中指定 class， class="col-"** 用于定义每列有几个 span ：


## CSS:


```css
.col-1 {width: 8.33%;}.col-2 {width: 16.66%;}.col-3 {width: 25%;}
	.col-4 {width: 33.33%;}.col-5 {width: 41.66%;}.col-6 {width: 50%;}
	.col-7 {width: 58.33%;}.col-8 {width: 66.66%;}.col-9 {width: 75%;}
	.col-10 {width: 83.33%;}.col-11 {width: 91.66%;}.col-12 {width:
	100%;}
```


	**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_cols)


所有的列向左浮动，间距(padding) 为 15px：


## CSS:


```css
[class*="col-"] {    float: left;
	padding: 15px;    border: 1px solid red;}
```


每一行使用  包裹。所有列数加起来应为 12：


```css
<div class="row">  <div class="col-3">...</div>  <div class="col-9">...</div></div>
```


列中行为左浮动，并添加清除浮动：


## CSS:


```css
.row:after {    content: "";
	clear: both;    display: block;}
```


我们可以添加一些样式和颜色，让其更好看：


## 实例


```css
html {    font-family: "Lucida Sans", sans-serif;}
	.header {    background-color: #9933cc;
	color: #ffffff;    padding: 15px;}.menu ul {
	list-style-type: none;    margin: 0;
	padding: 0;}.menu li {
	padding: 8px;    margin-bottom: 7px;
	background-color :#33b5e5;    color: #ffffff;
	box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);}.menu li:hover {
	background-color: #0099cc;}
```



[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_styles)









	  AI 思考中...





			** [响应式 Web 设计 – Viewport](https://www.runoob.com/css-rwd-viewport.html)
			[响应式 Web 设计 – 媒体查询](https://www.runoob.com/css-rwd-mediaqueries.html) **













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

      : ·[CSS 实例](https://www.runoob.com/css-examples.html)

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