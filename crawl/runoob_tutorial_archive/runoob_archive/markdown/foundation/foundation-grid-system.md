# Foundation 网格系统

- Source: https://www.runoob.com/foundation/foundation-grid-system.html

Foundation 网格系统为 12 列。


如果你不需要 12 列，你可以合并一些列，创建一些更大宽度的列。


![](https://www.runoob.com/wp-content/uploads/2015/11/grid-f.jpg) Foundation 的网格系统是响应式的。 列会根据屏幕尺寸自动调整大小。在大尺寸屏幕上，可能是三列，小屏幕尺寸就可能是三个单列，按顺序排列。


---


## 网格列


Foundation 网格系统有三个列：


- `.small` (手机端)
- `.medium` (平板设备)
- `.large` (电脑设备：笔记本，台式机)


以上类可以结合使用，创建更灵活的布局


---


## 基本的网格结构


以下是基本的 Foundation 网格结构实例:


### 实例


```
<div
	class="row">  <div class="small|medium|large-num
		columns"></div></div><div
	class="row">  <div class="small|medium|large-num
		columns"></div>
	<div class="small|medium|large-num columns"></div>
	<div class="small|medium|large-num columns"></div></div><div
	class="row">  ...</div>
```


首先，创建一行 (``)。 这是一个水平的垂直列。然后添加列的数量说明 `small-*num*`, `medium-*num*` 及 `large-*num*` 类。注意：列的数量 `* num*` 加起来必须等于 12 :


### 实例


```
<div
	class="row">  <div class="small-12
		columns">.small-12 yellow</div></div><div
	class="row">  <div class="small-8
		columns">.small-8 beige</div>
	<div class="small-4 columns">.small-4 gray</div></div><div
	class="row">  <div class="large-9 small-8
		columns">.small-8 .large-9 pink</div>
	<div class="large-3 small-4 columns">.small-4 .large-3
		orange</div></div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_grid_system)

实例中，第一行的  类为 `.small-12`, 这会创建 12 列（100%宽度）。


第二行创建了两个列， `.small-4` 的宽度为33.3% ，`.small-8` 的宽度为 66.6%。


第三行我们添加了额外的两个列 (`.large-3` 和 `.large-9`)。这意味着如果在大屏幕尺寸下，列就会变为 25% (`.large-3`) 和 75% (`.large-9`)的比例。同时我们也指定了小屏幕上列的比例 33% (`.small-4`) 和 66% (`.small-8`) 。这种组合的方式对于不同屏幕显示效果是非常有帮助的。


## 网格选项


下表总结了 Foundation 网格系统在多个设备上的说明：


|  | 小型设备Phones (=40.0625em (640px)) | 大设备Laptops & Desktops (>=64.0625em (1025px)) |
| --- | --- | --- | --- |
| 网格行为 | 一直是水平的 | 以折叠开始，断点以上是水平的 | 以折叠开始，断点以上是水平的 |
| 类前缀 | .small-* | .medium-* | .large-* |
| 类的数量 | 12 | 12 | 12 |
| 可内嵌 | Yes | Yes | Yes |
| 偏移量 | Yes | Yes | Yes |
| 列排序 | Yes | Yes | Yes |


---


## 宽屏


网格最大(`.row`) 宽度为 62.5rem。在宽屏上，当宽度大于 62.5rem, 列不会跨越页面的宽度， 即使宽度设定为 100%。但你可以通过 CSS 重新设置 max-width:


### 实例


```
<style>.row {    max-width: 100%;}</style>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_grid_maxwidth)

如果你使用默认的 max-width, 但希望背景颜色跨越整个页面宽度，你可以使用 `.row` 包裹整个容器，并指定你需要的背景颜色:


### 实例


```
<div style="background-color:coral;padding:25px;">  <div
		class="row">    <div class="small-6 columns" style="background-color:yellow;">.small-6</div>
		<div class="small-6 columns" style="background-color:pink;">.small-6</div>
		</div></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_grid_container)








	  AI 思考中...





			** [Foundation 均衡器(Equalizer)](https://www.runoob.com/foundation-equalizer.html)
			[Foundation 网格 – 水平堆叠](https://www.runoob.com/foundation-grid-stacked-to-horizontal.html) **













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