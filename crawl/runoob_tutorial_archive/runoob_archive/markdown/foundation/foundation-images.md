# Foundation 图片

- Source: https://www.runoob.com/foundation/foundation-images.html

Foundation 提供了响应式的图片，可以创建缩略图和图片弹窗：

*
[尝试一下 »](https://www.runoob.com/try/demo_source/tryfoundation_thumbs_iframe.htm)

---


## 缩略图


在 `` 元素外添加 `` 元素将图片作为一个锚链接。


在 `` 标签中添加 `.th` 类将图片设置为缩略图。 鼠标移动到上面会显示一个浅蓝色外框:


### 实例


```
<a href="paris.jpg" class="th">
	<img src="paris.jpg" alt="Paris"></a>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_thumbnail)


|  | 响应式图片 Foundation 中图片默认是响应式的。我们可以在实例页面重置浏览器大小来查看图片缩放效果。 |
| --- | --- |


---


## 圆角图片


我们可以在 `.th` 类添加 `.radius` 类来设置圆角缩略图：


### 实例


```
<a href="paris.jpg" class="th radius">
	<img src="paris.jpg" alt="Paris"></a>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_thumbnail_radius)


---


## 简洁的弹窗


Foundation 可以很容易实现图片弹窗。


要创建一个弹窗可以在 ` ` 元素上添加 `.clearing-thumbs` 类及 `data-clearing` 属性。在 `` 内添加图片列表。


注意:** 图片弹窗需要 JavaScript。所以使用它前需要初始化 Foundation JS。


### 实例


```
<ul class="clearing-thumbs" data-clearing>  <li><a href="rock600x400.jpg"
	class="th"><img
	src="rock200x100.jpg"></a></li>  <li><a href="skies600x400.jpg"
	class="th"><img
	src="skies200x100.jpg"></a></li>  <li><a href="lights600x400.jpg"
	class="th"><img
	src="lights200x100.jpg"></a></li></ul>
	<!-- Initialize Foundation JS --><script>
	$(document).ready(function() {
	$(document).foundation();})
	</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_lightbox)


---


## 图片文本描述


可以添加 `data-caption` 属性到每个图片来设置图片的描述:


### 实例


```
<ul class="clearing-thumbs" data-clearing>
	<li><a href="rock600x400.jpg" class="th"><img data-caption="The Pulpit Rock"
	src="rock200x100.jpg"></a></li>  <li><a href="skies600x400.jpg"
	class="th"><img data-caption="Sunrise Skies" src="skies200x100.jpg"></a></li>
	<li><a href="lights600x400.jpg" class="th"><img data-caption="Northern
	Lights" src="lights200x100.jpg"></a></li>
	</ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_lightbox_caption)


|  | 提示： 你可以在 data-caption 属性中添加 HTML 元素，如 data-caption="Pulpit RockLocated in Norway" |
| --- | --- |


---


## 只显示一张缩略图


当你需要实现只显示一张缩略图时你可以在 ` ` 中使用 `.clearing-feature` 类并在`` 中使用 `.clearing-featured-img` 类。


### 实例


```
<ul class="clearing-thumbs clearing-feature" data-clearing>  <li><a
	href="rock600x400.jpg" class="th"><img data-caption="The Pulpit Rock" src="rock200x100.jpg"></a></li>
	<li><a href="skies600x400.jpg" class="th"><img data-caption="Sunrise Skies"
	src="skies200x100.jpg"></a></li>  <li
	class="clearing-featured-img"><a href="lights600x400.jpg" class="th"><img
	data-caption="Northern Lights" src="lights200x100.jpg"></a></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_lightbox_feature)










	  AI 思考中...





			* [Foundation 面板](https://www.runoob.com/foundation-panels.html)
			[Foundation 下拉菜单](https://www.runoob.com/foundation-dropdowns.html) **













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