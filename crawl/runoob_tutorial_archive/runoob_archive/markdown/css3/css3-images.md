# CSS 图片

- Source: https://www.runoob.com/css3/css3-images.html

本章节将为大家介绍如何使用 CSS 来布局图片。


---


## 圆角图片


### 实例


圆角图片:


```css
img {    border-radius: 8px;}
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_images_round)


### 实例


椭圆形图片:


```css
img {    border-radius: 50%;}
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_images_circle)


---


## 缩略图


我们使用 `border` 属性来创建缩略图。


### 实例


```css
img {    border: 1px solid #ddd;
	border-radius: 4px;    padding: 5px;}
	<img src="paris.jpg"
	alt="Paris">
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_images_thumbnail)


### 实例


```css
a {    display: inline-block;    border: 1px solid #ddd;
	border-radius: 4px;    padding: 5px;
	transition: 0.3s;}a:hover {    box-shadow: 0
	0 2px 1px rgba    (0, 140, 186, 0.5);}
	<a href="paris.jpg">
	<img src="paris.jpg" alt="Paris"></a>
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_images_thumbnail_link)


---


## 响应式图片


响应式图片会自动适配各种尺寸的屏幕。


实例中，你可以通过重置浏览器大小查看效果:


![Norway](https://www.runoob.com/wp-content/uploads/2016/04/trolltunga.jpg)


如果你需要自由缩放图片，且图片放大的尺寸不大于其原始的最大值，则可使用以下代码：


### 实例


```css
img {    max-width: 100%;    height:
	auto;}
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_images_responsive)


提示:** Web 响应式设计更多内容可以参考 [CSS 响应式设计教程](https://www.runoob.com/../css/css-rwd-intro.html)。


---


## 图片文本


如何定位图片文本:


### 实例


![Norway](https://www.runoob.com/wp-content/uploads/2016/04/trolltunga.jpg)
左下角
左上角
右上角
右下角
居中


尝试一下:

[左上角 »](https://www.runoob.com/try/try.php?filename=trycss_image_text_top_left)

[右上角 »](https://www.runoob.com/try/try.php?filename=trycss_image_text_top_right)

[左下角 »](https://www.runoob.com/try/try.php?filename=trycss_image_text_bottom_left)

[右下角 »](https://www.runoob.com/try/try.php?filename=trycss_image_text_bottom_right)

[居中 »](https://www.runoob.com/try/try.php?filename=trycss_image_text_center)


---


## 卡片式图片


### 实例


```css
div.polaroid {    width: 80%;
	background-color: white;    box-shadow: 0 4px 8px 0 rgba(0,
	0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);}img {width: 100%}
	div.container {    text-align: center;
	padding: 10px 20px;}
```


	**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_images_card)


---


## 图片滤镜


CSS `filter` 属性用为元素添加可视效果 (例如：模糊与饱和度) 。


注意:** Internet Explorer 或 Safari 5.1 (及更早版本) 不支持该属性。


### 实例


修改所有图片的颜色为黑白 (100% 灰度):


```css
img {    -webkit-filter: grayscale(100%); /* Chrome, Safari,
	Opera */

    filter: grayscale(100%);}
```



*

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_images_filters)


提示:** 访问 [CSS 滤镜参考手册](https://www.runoob.com/../cssref/css3-pr-filter.html) 查看更多内容。


---


## 响应式图片相册


### 实例


```css
.responsive {
	padding: 0 6px;    float: left;
	width: 24.99999%;}@media only screen and
	(max-width: 700px){    .responsive {
	width: 49.99999%;        margin: 6px
	0;    }}@media only screen and (max-width: 500px){
	.responsive {        width: 100%;
	}}
```


	**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_image_gallery_responsive)


---


## 图片 Modal(模态)


本实例演示了如何结合 CSS 和 JavaScript 来一起渲染图片。


首先，我们使用 CSS 来创建 modal 窗口 (对话框), 默认是隐藏的。


然后，我们使用 JavaScript 来显示模态窗口，当我们点击图片时，图片会在弹出的窗口中显示：


### 实例


```css
// 获取模态窗口var modal = document.getElementById('myModal');// 获取图片模态框，alt 属性作为图片弹出中文本描述var img =
	document.getElementById('myImg');var modalImg = document.getElementById("img01");
	var captionText = document.getElementById("caption");img.onclick =
	function(){    modal.style.display = "block";
	modalImg.src = this.src;    modalImg.alt = this.alt;
	captionText.innerHTML = this.alt;}
	// Get the <span> element that closes the modalvar span =
	document.getElementsByClassName("close")[0];// When the user clicks
	on <span> (x), close the modalspan.onclick = function() {
	modal.style.display = "none";}
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_image_modal_js)









	  AI 思考中...





			* [CSS3 圆角](https://www.runoob.com/css3-border-radius.html)
			[CSS 按钮](https://www.runoob.com/css3-buttons.html) **













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