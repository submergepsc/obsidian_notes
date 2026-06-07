# Foundation 提醒框

- Source: https://www.runoob.com/foundation/foundation-alerts.html

Foundation 可以很简单的创建一个提醒框：

![](https://www.runoob.com/wp-content/uploads/2015/11/alert.jpg)


提醒框可以使用 `.alert-box` 类创建, 可以添加可选的类： `.secondary`, `.success`, `.info`, `.warning` 或 `.alert`:


### 实例


```
<div data-alert class="alert-box">  This is a
	default alert box.
	</div><div data-alert
	class="alert-box secondary">  This is a secondary alert box.
	</div><div data-alert class="alert-box success">
	<strong>Success!</strong> This alert box indicates a successful or positive
	action.</div>
	<div data-alert class="alert-box info">  <strong>Info!</strong>
	This alert box indicates a neutral informative change or action.</div><div
	data-alert class="alert-box warning">  <strong>Warning!</strong>
	This alert box indicates a warning that might need attention.</div>
	<div data-alert class="alert-box alert">  <strong>Alert!</strong>
	This alert box indicates a dangerous or potentially negative action.
	</div>
```

**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_alerts)


|  | 提醒框的宽度为容器的 100%。 |
| --- | --- |


---


## 圆角提醒框


`.radius` 和 `.round` 类用于为提醒框添加圆角：


### 实例


```
<div data-alert class="alert-box success radius">
	<strong>Success!</strong> Alert box with a radius.
</div><div data-alert class="alert-box info round">  <strong>Info!</strong> Alert box that is rounded.</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_alerts_rounded)


---


## 关闭提醒框


要关闭提醒框，可以在连接或按钮元素上添加 `class="close"` 类，并初始化 Foundation JS:


### 实例


```
<div data-alert class="alert-box">
	This is a default alert box with closing functionality.  <a href="#" class="close">&times;</a></div><script>
	// Initialize Foundation JS For Functionality
	$(document).ready(function() {
	$(document).foundation();})
	</script>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_alerts_close)


|  | × (×) 是一个 HTML 字符实体表示一个关闭按钮的图标，而不是字母 "x"。 |
| --- | --- |









	  AI 思考中...





			** [Foundation 标签](https://www.runoob.com/foundation-labels.html)
			[Foundation 进度条](https://www.runoob.com/foundation-progressbars.html) **













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