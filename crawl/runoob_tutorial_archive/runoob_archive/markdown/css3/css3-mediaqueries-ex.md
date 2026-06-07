# CSS3 多媒体查询实例

- Source: https://www.runoob.com/css3/css3-mediaqueries-ex.html

本章节我们将为大家演示一些多媒体查询实例。


开始之前我们先制作一个电子邮箱的链接列表。HTML 代码如下：


### 实例 1


```css
<!DOCTYPE html><html><head><style>ul {
	list-style-type: none;}ul li a {    color:
	green;    text-decoration: none;
	padding: 3px;     display: block;}</style>
	</head><body><ul>  <li><a data-email="[email protected]"
	href="mailto:[email protected]">John Doe</a></li>  <li><a
	data-email="[email protected]" href="mailto:[email protected]">Mary
	Moe</a></li>  <li><a data-email="[email protected]" href="mailto:[email protected]">Amanda
	Panda</a></li></ul></body></html>
```


**
	[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_mediaqueries_ex1)


注意 `data-email` 属性。在 HTML 中我们可以使用带 `data-` 前缀的属性来存储信息。


---


## 520 到 699px 宽度 - 添加邮箱图标


当浏览器的宽度在 520 到 699px, 邮箱链接前添加邮件图标：


### 实例 2


```css
@media screen and (max-width: 699px) and (min-width: 520px) {
	ul li a {
	padding-left: 30px;
	background: url(email-icon.png) left center no-repeat;
	}}
```


	[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_mediaqueries_ex2)


---


## 700 到 1000px - 添加文本前缀信息


当浏览器的宽度在 700 到 1000px, 会在邮箱链接前添加 "Email: ":


### 实例 3


```css
@media screen and (max-width: 1000px) and (min-width: 700px) {
	ul li a:before {
	content: "Email: ";
	font-style: italic;        color: #666666;
	}}
```


	[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_mediaqueries_ex3)


---


## 大于 1001px 宽度 - 添加邮件地址


当浏览器的宽度大于 1001px 时，会在链接后添加邮件地址接。


我们会使用 `data-` 属性来为每个人名后添加邮件地址：


### 实例 4


```css
@media screen and (min-width: 1001px) {    ul li
	a:after {        content: " (" attr(data-email)
	")";        font-size: 12px;
	font-style: italic;        color:
	#666666;    }}
```


	[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_mediaqueries_ex4)


---


## 大于 1151px 宽度 - 添加图标


当浏览器的宽度大于 1001px 时，会在人名前添加图标。


实例中，我们没有编写额外的查询块，我们可以在已有的查询媒体后使用逗号分隔来添加其他媒体查询 (类似 OR 操作符):


### 实例 5


```css
@media screen and (max-width: 699px) and (min-width: 520px), (min-width:
	1151px) {
	ul li a {
	padding-left: 30px;
	background: url(email-icon.png) left center no-repeat;
	}}
```


	[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_mediaqueries_ex5)


---


![实例](https://www.runoob.com/images/tryitimg.gif)

## 更多实例


[在一个网页的侧栏上使用邮件列表链接](https://www.runoob.com/try/try.php?filename=trycss3_mediaqueries_ex6) 该实例在网页的左侧栏添加了邮件链接列表。








	  AI 思考中...





			** [CSS3 多媒体查询](https://www.runoob.com/css3-mediaqueries.html)
			[CSS3 rotation-point](https://www.runoob.com/css3-pr-rotation-point.html) **













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