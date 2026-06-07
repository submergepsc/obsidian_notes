# 响应式 Web 设计 - 图片

- Source: https://www.runoob.com/css/css-rwd-images.html

---


## 使用 width 属性


如果 width 属性设置为 100%，图片会根据上下范围实现响应式功能：


## 实例


```css
img {
    width: 100%;    height: auto;
}
```


	**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_image2)


注意在以上实例中，图片会比它的原始图片大。我们可以使用 max-width** 属性很好的解决这个问题。


---


## 使用 max-width 属性


如果 max-width 属性设置为 100%, 图片永远不会大于其原始大小：


## 实例


```css
img {
    max-width: 100%;    height: auto;
}
```


	**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_image)


---


## 网页中添加图片


## 实例


```css
img {
    width: 100%;    height: auto;
}
```



[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_image3)


---


## 背景图片

背景图片可以响应调整大小或缩放。


以下是三个不同的方法：


1. 如果 background-size 属性设置为 "contain", 背景图片将按比例自适应内容区域。图片保持其比例不变：


这是 CSS 代码:


## 实例


```css
div {    width: 100%;    height: 400px;
	background-image: url('img_flowers.jpg');
	background-repeat: no-repeat;
	background-size: contain;    border: 1px solid red;}
```




	[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_image_background1)


2. 如果 background-size 属性设置为 "100% 100%" ，背景图片将延展覆盖整个区域：



## 实例


这是 CSS 代码:


```css
div {    width: 100%;    height: 400px;
	background-image: url('img_flowers.jpg');
	background-size: 100% 100%;    border: 1px solid red;}
```




	[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_image_background2)


3. 如果 background-size 属性设置为 "cover"，则会把背景图像扩展至足够大，以使背景图像完全覆盖背景区域。注意该属性保持了图片的比例因此 背景图像的某些部分无法显示在背景定位区域中。


这是 CSS 代码:


## 实例


```css
div {    width: 100%;    height: 400px;
	background-image: url('img_flowers.jpg');    background-size: cover;
	border: 1px solid red;}
```




	[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_image_background3)


---


## 不同设备显示不同图片


大尺寸图片可以显示在大屏幕上，但在小屏幕上却不能很好显示。我们没有必要在小屏幕上去加载大图片，这样很影响加载速度。所以我们可以使用媒体查询，根据不同的设备显示不同的图片。


以下大图片和小图片将显示在不同设备上：


![](https://www.runoob.com/wp-content/uploads/2015/06/img_flowers.jpg)


![](https://www.runoob.com/wp-content/uploads/2015/06/img_smallflower.jpg)


## 实例


```css
/* For width smaller than 400px: */body {    background-image:
	url('img_smallflower.jpg'); }/*
	For width 400px and larger: */@media only screen and (min-width: 400px)
	{    body {
	background-image: url('img_flowers.jpg');     }}
```




	[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_image_mediaq)


你可以使用媒体查询的 min-device-width 替代 min-width 属性，它将检测的是设备宽度而不是浏览器宽度。浏览器大小重置时，图片大小不会改变。


## 实例


```css
/* 设备小于 400px: */body {    background-image:
	url('img_smallflower.jpg'); }/*
	设备大于 400px (也等于): */@media only screen and (min-device-width: 400px)
	{    body {
	background-image: url('img_flowers.jpg');     }}
```




	[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_image_mediaq2)


---


## HTML5 元素


HTML5 的 `` 元素可以设置多张图片。


### 浏览器支持


| 元素 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 不支持 | 38.0 | 38.0 | 不支持 | 25.0 |


`` 元素类似于 `` 和 `` 元素。可以设备不同的资源，第一个设置的资源为首选使用的：


## 实例


```css
<picture>  <source srcset="img_smallflower.jpg" media="(max-width:
	400px)">  <source srcset="img_flowers.jpg">  <img
	src="img_flowers.jpg" alt="Flowers"></picture>
```




	[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryresponsive_image_picture)


`srcset` 属性的必须的，定义了图片资源。


`media` 属性是可选的，可以在媒体查询的 [CSS @media 规则](https://www.runoob.com/../cssref/css3-pr-mediaquery.html) 查看详情。


对于不支持 `` 元素的浏览器你也可以定义 `` 元素来替代。










	  AI 思考中...





			** [响应式 Web 设计 – 媒体查询](https://www.runoob.com/css-rwd-mediaqueries.html)
			[响应式 Web 设计 – 视频(Video)](https://www.runoob.com/css-rwd-videos.html) **













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