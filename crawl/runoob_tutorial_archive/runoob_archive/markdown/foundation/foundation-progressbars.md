# Foundation 进度条

- Source: https://www.runoob.com/foundation/foundation-progressbars.html

Foundation 进度条可以作为程序处理的程度来显示：

![](https://www.runoob.com/wp-content/uploads/2015/11/progress.jpg)


我们可以在 `` 元素中使用 `.progress` 类来创建进度条， `.meter` 类用于子元素()。我们可以在  元素中设置进度百分比，如下所示：


### 实例


```
<div class="progress">  <span class="meter"
	style="width:70%"></span></div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_progressbar)


---


## 进度条颜色


默认情况下，进度条颜色为蓝色。不同颜色的类为：`.secondary`, `.success`, 或 ` .alert`:


### 实例


```
<div class="progress">  <span class="meter"
	style="width:50%"></span></div><div class="progress
	secondary">  <span class="meter"
	style="width:50%"></span></div><div class="progress
	success">  <span class="meter"
	style="width:50%"></span></div><div class="progress
	alert">  <span class="meter"
	style="width:50%"></span></div>
```




[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_progressbar_contextual)


---


## 圆角进度条


`.radius` 和 `.round` 类用于为进度条添加圆角效果：


### 实例


```
<div class="progress">  <span class="meter"
		style="width:50%"></span></div><div class="progress radius">  <span
		class="meter" style="width:50%"></span></div><div
		class="progress round">  <span class="meter"
		style="width:50%"></span></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_progressbar_rounded)


---

## 进度条尺寸


可以使用 `.small-*num*` 或 `.large-*num*` 来修改进度条的宽度， *num* 是一个数字在 1(8.33%) 和 12(default (100%)) 之间:


### 实例


```
<div class="progress large-1">  <span class="meter"
	style="width:50%"></span></div><div class="progress
	large-6">  <span class="meter"
	style="width:50%"></span></div><div class="progress
	large-9">  <span class="meter"
	style="width:50%"></span></div><div class="progress
	large-11">  <span class="meter"
	style="width:50%"></span></div><!--
	Default width --><div class="progress
	large-12">  <span class="meter"
	style="width:50%"></span></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_progressbar_width)


---


## 进度条标签


可以使用 CSS 为进度条添加标签。以下实例中我们添加了 元素来显示百分比：


### 实例


```
<style>.percentage {  position: absolute;  top: 50%;  left:
		50%;  color:
		white;   transform: translate(-50%, -50%);  font-size: 12px;}</style>
		<div class="progress">  <span class="meter"
		style="position:relative;width:75%">    <span
		class="percentage">75%</span>  </span></div><div
		class="progress success">  <span class="meter"
		style="position:relative;width:50%">    <span
		class="percentage">50%</span>  </span></div><div
		class="progress alert">  <span class="meter"
		style="position:relative;width:25%">    <span
		class="percentage">25%</span>  </span></div>
```




[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_progressbar_css)









	  AI 思考中...





			** [Foundation 提醒框](https://www.runoob.com/foundation-alerts.html)
			[Foundation 面板](https://www.runoob.com/foundation-panels.html) **













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