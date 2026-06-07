# Foundation 滑块

- Source: https://www.runoob.com/foundation/foundation-sliders.html

Foundation 滑块允许用户通过拖动来选取区间值:

*


滑块可以通过使用 `` 创建。在 `` 内, 添加两个 `` 元素: `` 创建矩形滑块（蓝色背景）， `` 是在滑块后的灰色横条，是滑块拖动区域。


**注意:** 滑块需要使用 JavaScript。所以你需要初始化 Foundation JS:


### 实例


```
<div class="range-slider" data-slider>  <span
	class="range-slider-handle"></span>  <span
	class="range-slider-active-segment"></span></div>
	<!-- Initialize Foundation JS --><script>
	$(document).ready(function() {
	$(document).foundation();})
	</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_slider)


---


## 圆角和禁用滑块


使用 `.radius` 和 `.round` 类来添加圆角滑块。使用 `.disabled` 类来禁用滑块：


### 实例


```
<div class="range-slider" data-slider>..</div><div
	class="range-slider radius" data-slider>...</div>
	<div class="range-slider round" data-slider>...</div>
	<div class="range-slider disabled" data-slider>...</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_slider_round)


---


## 垂直滑块


使用 `.vertical-range` 类和 `data-options="vertical: true;"` 来创建垂直滑块:


### 实例


```
<div class="range-slider vertical-range" data-slider data-options="vertical:
	true;">  <span class="range-slider-handle"></span>  <span
	class="range-slider-active-segment"></span></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_slider_vertical)


---


## 滑块值


默认情况下，滑块放在横条的中间 (数值为 "50")。可以通过添加 `data-options="initial: num*"` 属性来修改默认值:


### 实例


```
<div class="range-slider" data-slider
	data-options="initial: 80;">  <span
	class="range-slider-handle"></span>  <span
	class="range-slider-active-segment"></span></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_slider_default_value)


### 显示滑块值


如果我们需要在滑块拖动时实时显示值，可以通过在 ` ` 中添加 `data-options="display_selector:#*id*"` 属性且元素 id 值与滑块的 id 匹配，如下实例：


### 实例


```
<!-- Display the slider value in this span --><span id="mySlider"></span><div class="range-slider" data-slider
	data-options="display_selector: #mySlider;">  <span
	class="range-slider-handle"></span>  <span
	class="range-slider-active-segment"></span></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_slider_value)


### 组合数据选项


以下实例使用了 `display_selector` 和 `initial` 数据选项:


### 实例


```
<span id="mySlider"></span><div class="range-slider" data-slider
	data-options="display_selector: #mySlider; initial: 20;"> <span
	class="range-slider-handle"></span>  <span
	class="range-slider-active-segment"></span></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_slider_combining_value)


### 步长


默认情况下，滑块滑动的增加减少的数量为 "1"。可以通过添加 `data-options="step: *num*;"` 属性来修改步长值。实例中设置为 25:


### 实例


```
<span id="mySlider"></span><div class="range-slider" data-slider
	data-options="display_selector: #mySlider; step: 25;">  <span
	class="range-slider-handle"></span>  <span
	class="range-slider-active-segment"></span></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_slider_step)


### 自定义区间


默认情况下，区间值在 "0" 到 "100"。可以通过添加 data-options `start` 和 `end` 来设置区间值。以下实例设置区间值为 "1" 到 "20":


### 实例


```
<span id="mySlider"></span><div
	class="range-slider" data-slider data-options="display_selector: #mySlider;
	start: 1; end: 20;">  <span
	class="range-slider-handle"></span>  <span
	class="range-slider-active-segment"></span></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_slider_range)


### 使用网格


以下使用为在网格中使用滑块：


### 实例


```
<div class="row">  <div class="small-10 columns">
	<div class="range-slider" data-slider data-options="display_selector:
	#mySlider;">      <span
	class="range-slider-handle"></span>      <span
	class="range-slider-active-segment"></span>    </div>
	</div>  <div class="small-2 columns">
	<!-- The display element (Tip: use CSS to perfectly position it) -->    <span
	id="mySlider" style="display:block;margin-top:14px;"></span>
	</div></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_slider_value_grid)


### 使用 Input


以下实例使用 `` 取代 `` 来显示滑块的值:


### 实例


```
<div class="row">  <div class="small-10 columns">
	<div class="range-slider" data-slider data-options="display_selector:
	#mySlider; initial: 72;">      <span
	class="range-slider-handle"></span>      <span
	class="range-slider-active-segment"></span>    </div>
	</div>  <div class="small-2 columns">
	<!-- The display element (Tip: use CSS to perfectly position it) -->
	<input type="number" id="mySlider" style="margin-top:7px;" value="72">
	</div></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_slider_value_input)








	  AI 思考中...





			** [Foundation 开关](https://www.runoob.com/foundation-switches.html)
			[Foundation 提示框](https://www.runoob.com/foundation-tooltips.html) **













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