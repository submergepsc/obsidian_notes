# HTML 音频(Audio)

- Source: https://www.runoob.com/html/html-sounds.html

---


声音在HTML中可以以不同的方式播放.


---


## 问题以及解决方法


在 HTML 中播放音频并不容易！


您需要谙熟大量技巧，以确保您的音频文件在所有浏览器中（Internet Explorer, Chrome, Firefox, Safari, Opera）和所有硬件上（PC, Mac , iPad, iPhone）都能够播放。


在本章，菜鸟教程为您总结了问题和解决方法。


---


## 使用插件


浏览器插件是一种扩展浏览器标准功能的小型计算机程序。


插件可以使用  标签 或者  标签添加在页面上.


这些标签定义资源（通常非 HTML 资源）的容器，根据类型，它们即会由浏览器显示，也会由外部插件显示。


---


## 使用 元素


标签定义外部（非 HTML）内容的容器。（这是一个 HTML5 标签，在 HTML4 中是非法的，但是所有浏览器中都有效）。


下面的代码片段能够显示嵌入网页中的 MP3 文件：


## 实例


```html
<embed height="50" width="100" src="horse.mp3">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_soundmidiembed)


### 问题:


- * 标签在 HTML 4 中是无效的。页面无法通过 HTML 4 验证。
- 不同的浏览器对音频格式的支持也不同。
- 如果浏览器不支持该文件格式，没有插件的话就无法播放该音频。
- 如果用户的计算机未安装插件，无法播放音频。
- 如果把该文件转换为其他格式，仍然无法在所有浏览器中播放。


---


## 使用 元素


 标签也可以定义外部（非 HTML）内容的容器。


下面的代码片段能够显示嵌入网页中的 MP3 文件：


## 实例


```html
<object height="50" width="100" data="horse.mp3"></object>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_soundmidobject)


### 问题:


- 不同的浏览器对音频格式的支持也不同。
- 如果浏览器不支持该文件格式，没有插件的话就无法播放该音频。
- 如果用户的计算机未安装插件，无法播放音频。
- 如果把该文件转换为其他格式，仍然无法在所有浏览器中播放。


---


## 使用 HTML5 元素


HTML5  元素是一个 HTML5 元素，在 HTML 4 中是非法的，但在所有浏览器中都有效。


The  element works in all modern browsers.


### 浏览器兼容


格中的数字表示支持该属性的第一个浏览器版本号。


| 元素 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 4.0 | 9.0 | 3.5 | 4.0 | 10.5 |


以下我们将使用  标签来描述 MP3 文件(Internet Explorer、Chrome 以及 Safari 中是有效的), 同样添加了一个 OGG 类型文件(Firefox 和 Opera浏览器中有效).如果失败，它会显示一个错误文本信息:


## 实例


```html
<audio controls>
  <source src="horse.mp3" type="audio/mpeg">
  <source src="horse.ogg" type="audio/ogg">

	Your browser does not support this audio format.
	</audio>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_audio_5)


### 问题:


-  标签在 HTML 4 中是无效的。您的页面无法通过 HTML 4 验证。
- 您必须把音频文件转换为不同的格式。
-  元素在老式浏览器中不起作用。


---


## 最好的 HTML 解决方法


下面的例子使用了两个不同的音频格式。HTML5  元素会尝试以 mp3 或 ogg 来播放音频。如果失败，代码将回退尝试  元素。


## 实例


```html
<audio controls height="100" width="100">

	<source src="horse.mp3" type="audio/mpeg">
  <source src="horse.ogg" type="audio/ogg">

	<embed height="50" width="100" src="horse.mp3">
	</audio>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_audio_all)


### 问题:


- 您必须把音频转换为不同的格式。
-  元素无法回退来显示错误消息。


---


## 使用超链接


如果网页包含指向媒体文件的超链接，大多数浏览器会使用"辅助应用程序"来播放文件。


以下代码片段显示指向 mp3 文件的链接。如果用户点击该链接，浏览器会启动"辅助应用程序"来播放该文件：


## 实例


```html
<a href="horse.mp3">Play the sound</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_sound_mp3link)


---


## 内联的声音说明


当您在网页中包含声音，或者作为网页的组成部分时，它被称为内联声音。


如果您打算在 web 应用程序中使用内联声音，您需要意识到很多人都觉得内联声音令人恼火。同时请注意，用户可能已经关闭了浏览器中的内联声音选项。


我们最好的建议是只在用户希望听到内联声音的地方包含它们。一个正面的例子是，在用户需要听到录音并点击某个链接时，会打开页面然后播放录音。


---


## HTML 多媒体标签


New : HTML5 新标签


| 标签 | 描述 |
| --- | --- |
|  | 定义内嵌对象。HTML4 中不赞成，HTML5 中允许。 |
|  | 定义内嵌对象。 |
|  | 定义对象的参数。 |
| New | 定义了声音内容 |
| New | 定义一个视频或者影片 |
| New | 定义了media元素的多媒体资源( 和 ) |
| New | 规定media元素的字幕文件或其他包含文本的文件 ( 和) |








	  AI 思考中...





			* [HTML 插件](https://www.runoob.com/html-object.html)
			[HTML 视频（Video）播放](https://www.runoob.com/html-videos.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html-examples.html)

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