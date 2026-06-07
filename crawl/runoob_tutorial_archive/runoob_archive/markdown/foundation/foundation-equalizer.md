# Foundation 均衡器(Equalizer)

- Source: https://www.runoob.com/foundation/foundation-equalizer.html

我们可以在容器元素添加 `data-equalizer` 属性，并为每个子元素添加 `data-equalizer-watch` 属性来创建一个相同高度的均衡器。最高的元素决定了其他元素的高度。


**注意:** 均衡器需要使用 JavaScript，所以你需要初始化 Foundation JS:


### 实例


```
<div class="row" data-equalizer>  <div class="medium-4 columns
	panel" data-equalizer-watch>    Lorem ipsum...  </div>
	<div class="medium-4 columns panel" data-equalizer-watch>
	    Sed ut...  </div>  <div class="medium-4 columns panel"
	data-equalizer-watch>    Lorem ipsum...  </div></div>
	<!-- Initialize Foundation JS --><script>
	$(document).ready(function() {
	$(document).foundation();})
	</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_equalizer)


---


## 不同屏幕的均衡器


在均衡器上通过添加 `data-equalizer-mq="*value*"` 属性为不同屏幕尺寸设置相同高度。值可以是以下之一：


| 值 | 描述 | 实例 |
| --- | --- | --- |
| medium-up | 默认。 创建相同高度的容器，宽度大于 40.063em |  |
| large-up | 创建相同高度的容器，宽度大于 64.063em | 尝试一下 |
| xlarge-up | 创建相同高度的容器，宽度大于 90.063em | 尝试一下 |
| xxlarge-up | 创建相同高度的容器，宽度大于 120.063em | 尝试一下 |


---


## 嵌套内容


为 `data-equalizer` 和 `data-equalizer-watch` 属性添加相同的值。 这会一起连接到均衡器容器。 重复多次嵌套均衡器，确保他们是匹配的：


### 实例


```
<!-- The Equalized Container --><div class="row" data-equalizer="first">  <div class="medium-4
	columns">    <div class="panel"
	data-equalizer-watch="first">
	<h3>Panel</h3>      <!-- An Equalized
	Container Inside The Equalized Container -->
	<div class="row" data-equalizer="second">
	<div class="panel" data-equalizer-watch="second">
	<h3>Nested Panel</h3>
	<p>Lorem ipsum...</p>        </div>
	<div class="panel" data-equalizer-watch="second">
	<h3>Nested Panel</h3>
	<p>Lorem ipsum...</p>        </div>
	<div class="panel" data-equalizer-watch="second">
	<h3>Nested Panel</h3>
	<p>Lorem ipsum...</p>        </div>
	</div>      <!-- End Nested Equalized Container
	-->    </div>  </div>  <div
	class="medium-4 columns">    <div class="panel"
	data-equalizer-watch="first">
	<h3>Panel</h3>      <p>Ut enim...</p>
	</div>  </div>  <div class="medium-4 columns">
	<div class="panel" data-equalizer-watch="first">
	<h3>Panel</h3>      <p>Lorem ipsum....</p>
	</div>  </div></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_equalizer_nested)








	  AI 思考中...





			** [Foundation Joyride](https://www.runoob.com/foundation-joyride.html)
			[Foundation 网格系统](https://www.runoob.com/foundation-grid-system.html) **













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