# 响应式 Web 设计 - 媒体查询

- Source: https://www.runoob.com/css/css-rwd-mediaqueries.html

---


媒体(media)查询在 CSS3 上有介绍：[CSS3 @media 查询](https://www.runoob.com/../cssref/css3-pr-mediaquery.html)。


使用 @media 查询，你可以针对不同的媒体类型定义不同的样式。


## 实例


如果浏览器窗口小于 500px, 背景将变为浅蓝色：


```css
@media only screen and (max-width: 500px) {    body {

	background-color: lightblue;    }}
```


	**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_mediaquery)


---


## 添加断点


在先前的教程中我们使用行和列来制作网页，它是响应式的，但在小屏幕上并不能友好的展示。


媒体查询可以帮我们解决这个问题。我们可以在设计稿的中间添加断点，不同的断点有不同的效果。


### 桌面设备

![](https://www.runoob.com/wp-content/uploads/2015/06/rwd_desktop.png)

### 手机设备

![](https://www.runoob.com/wp-content/uploads/2015/06/rwd_phone.png)


使用媒体查询在 768px 添加断点：


## 实例


当屏幕 (浏览器窗口) 小于 768px, 每一列的宽度是 100%:


```css
/* For desktop: */.col-1 {width: 8.33%;}.col-2 {width: 16.66%;}.col-3 {width: 25%;}
	.col-4 {width: 33.33%;}.col-5 {width: 41.66%;}.col-6 {width: 50%;}
	.col-7 {width: 58.33%;}.col-8 {width: 66.66%;}.col-9 {width: 75%;}
	.col-10 {width: 83.33%;}.col-11 {width: 91.66%;}.col-12 {width:
	100%;}@media only screen and (max-width: 768px) {
	/* For mobile phones: */
	[class*="col-"] {        width: 100%;
	}}
```



[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_breakpoints)


---


## 为移动端优先设计


移动端优先意味着在设计桌面和其他设备时优先考虑移动端的设计。


这就意味着我们必须对 CSS 做一些改变。


我们在屏幕小于 768px 进行样式修改，同样在屏幕宽度大于 768px 时也需要修改样式。以下是移动端优先实例：


```css
/* 为移动端设计: */[class*="col-"] {    width: 100%;}@media only screen and (min-width:
	768px) {    /* For desktop: */    .col-1 {width: 8.33%;}    .col-2 {width: 16.66%;}    .col-3 {width: 25%;}    .col-4 {width: 33.33%;}    .col-5 {width: 41.66%;}    .col-6 {width: 50%;}    .col-7 {width: 58.33%;}    .col-8 {width: 66.66%;}    .col-9 {width: 75%;}    .col-10 {width: 83.33%;}    .col-11 {width: 91.66%;}    .col-12 {width: 100%;}}
```


---


## 其他断点


你可以根据自己的需要添加断点。

我们同样可以为平板设备和移动手机设备设置断点。


### 桌面设备

![](https://www.runoob.com/wp-content/uploads/2015/06/rwd_desktop.png)


### 平板设备

![](https://www.runoob.com/wp-content/uploads/2015/06/rwd_tablet.png)

### 手机设备

![](https://www.runoob.com/wp-content/uploads/2015/06/rwd_phone.png)


在屏幕为 600px 时添加媒体查询，并设置新的样式（屏幕大于600px但小于768px）：


## 实例


注意两组类样式是相同的，但名称不同 (col- 和 col-m-):


```css
/* For mobile phones: */[class*="col-"] {    width: 100%;}@media only screen and (min-width: 600px) {
	/* For tablets: */    .col-m-1 {width: 8.33%;}    .col-m-2 {width: 16.66%;}    .col-m-3 {width: 25%;}    .col-m-4 {width: 33.33%;}    .col-m-5 {width: 41.66%;}    .col-m-6 {width: 50%;}    .col-m-7 {width: 58.33%;}    .col-m-8 {width: 66.66%;}    .col-m-9 {width: 75%;}    .col-m-10 {width: 83.33%;}    .col-m-11 {width: 91.66%;}    .col-m-12 {width: 100%;}}@media only screen and (min-width:
	768px) {    /* For desktop: */    .col-1 {width: 8.33%;}    .col-2 {width: 16.66%;}    .col-3 {width: 25%;}    .col-4 {width: 33.33%;}    .col-5 {width: 41.66%;}    .col-6 {width: 50%;}    .col-7 {width: 58.33%;}    .col-8 {width: 66.66%;}    .col-9 {width: 75%;}    .col-10 {width: 83.33%;}    .col-11 {width: 91.66%;}    .col-12 {width: 100%;}}
```



[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_col-s)


以上代码看起来很多余，但是他可以根据屏幕大小自动设置不同的样式，所以还是非常必要的。


## HTML 实例


针对桌面设备:


第一和第三部分跨越 3 列。中间部分跨域 6 列。


针对平板设备:


第一跨域 3列，第二部分跨越 9 列，第三部分跨域 12 列：


```css
<div class="row"><div class="col-3 col-m-3">...</div><div
	class="col-6 col-m-9">...</div><div
	class="col-3 col-m-12">...</div></div>
```


---


## 方向：横屏/竖屏


结合CSS媒体查询,可以创建适应不同设备的方向(横屏landscape、竖屏portrait等)的布局。


### 语法：


```
orientation：portrait | landscape
```


- ** portrait：**指定输出设备中的页面可见区域高度大于或等于宽度
- ** landscape：** 除portrait值情况外，都是landscape


## 实例


如果是横屏背景将是浅蓝色：


```css
@media only screen and (orientation:
	landscape) {    body {

	background-color: lightblue;    }}
```



[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_mediaquery_orientation)








	  AI 思考中...





			** [响应式 Web 设计 – 网格视图](https://www.runoob.com/css-rwd-grid.html)
			[响应式 Web 设计 – 图片](https://www.runoob.com/css-rwd-images.html) **













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