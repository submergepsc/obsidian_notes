# Foundation 模态框

- Source: https://www.runoob.com/foundation/foundation-modal.html

模态框是一个显示在页面头部的弹窗。


我们可以在容器元素上(如 `` 标签上添加 `.close-reveal-modal` 类来实现。


**注意:** 滑块需要使用 JavaScript。所以你需要初始化 Foundation JS:


### 实例


```
<!-- Trigger the Modal --><button
	type="button" class="button" data-reveal-id="myModal">Click To Open Modal</button>
	<!-- The Modal Content --><div id="myModal" class="reveal-modal" data-reveal>  <h2>Heading in
	Modal.</h2>  <p>Some text in the modal.</p>  <p>Some text in the
	modal.</p>  <a class="close-reveal-modal">&times;</a></div>
	<!-- Initialize Foundation JS --><script>
	$(document).ready(function() {
	$(document).foundation();})
	</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_modal)


---


## 模态框大小


可以在模态框容器上添加以下类来设置模态框的大小：


- `.tiny`: 30% 宽度
- `.small`: 40% 宽度
- `.medium`: 60% 宽度
- `.large`: 70% 宽度
- `.xlarge`: 95% 宽度
- `.full`: 100% 宽度和高度


注意:** 在平板、笔记本、PC 电脑上默认为 80% 宽度，在小屏幕设备上是 100% 宽度。


### 实例


```
<div id="myModal" class="reveal-modal tiny|small|medium|large|xlarge|full" data-reveal>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_modal_size)


---


## 内嵌模态框


你可以在模态框内嵌入模态框，可以在第一个模态框上添加新的触发按钮。你必须为内嵌模态框设置一个唯一的 id：


### 实例


```
<!-- Trigger the modal --><a href="#" class="button" data-reveal-id="myModal">Click
	To Open Modal</a><!-- The First Modal --><div id="myModal" class="reveal-modal" data-reveal>
	<h2>First Modal</h2>  <p>Some text..</p>  <p><a href="#"
	data-reveal-id="secondModal" class="button">Open Second Modal</a></p>
	<a class="close-reveal-modal">&times;</a></div>
	<!-- The Second Modal --><div id="secondModal" class="reveal-modal"
	data-reveal>  <h2>Tada! Second Modal</h2>
	<p>Some text..</p>  <a
	class="close-reveal-modal">&times;</a></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_modal_nested)


第二个模态框会取代第一个模态框。如果你希望在打开第二个模态框时，不关闭第一个模态框。可以在第二个模态框上添加 `data-options="multiple_opened:true;"` 属性：


### 实例


```
<div id="secondModal" class="reveal-modal" data-reveal data-options="multiple_opened:true;">
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_modal_nested2)








	  AI 思考中...





			** [Foundation 提示框](https://www.runoob.com/foundation-tooltips.html)
			[Foundation Joyride](https://www.runoob.com/foundation-joyride.html) **













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