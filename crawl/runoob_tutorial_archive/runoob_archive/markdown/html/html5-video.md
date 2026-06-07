# HTML5 Video(视频)

- Source: https://www.runoob.com/html/html5-video.html

---


很多站点都会使用到视频. HTML5 提供了展示视频的标准。


## 检测您的浏览器是否支持 HTML5 视频：


```html
检测
```


**
---


## Web站点上的视频


直到现在，仍然不存在一项旨在网页上显示视频的标准。


今天，大多数视频是通过插件（比如 Flash）来显示的。然而，并非所有浏览器都拥有同样的插件。


HTML5 规定了一种通过 video 元素来包含视频的标准方法。


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9+, Firefox, Opera, Chrome, 和 Safari 支持  元素.


注意:** Internet Explorer 8 或者更早的IE版本不支持  元素。


---


## HTML5 (视频)- 如何工作


如需在 HTML5 中显示视频，您所有需要的是：


## 实例


```html
<video width="320" height="240" controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
您的浏览器不支持Video标签。
</video>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_video_all)


 元素提供了 播放、暂停和音量控件来控制视频。


同时  元素也提供了 width 和 height 属性控制视频的尺寸.如果设置的高度和宽度，所需的视频空间会在页面加载时保留。如果没有设置这些属性，浏览器不知道大小的视频，浏览器就不能再加载时保留特定的空间，页面就会根据原始视频的大小而改变。


 与 标签之间插入的内容是提供给不支持 video 元素的浏览器显示的。


 元素支持多个  元素.  元素可以链接不同的视频文件。浏览器将使用第一个可识别的格式：


---


## 视频格式与浏览器的支持


当前，  元素支持三种视频格式： MP4, WebM, 和 Ogg:


| 浏览器 | MP4 | WebM | Ogg |
| --- | --- | --- | --- |
| Internet Explorer | YES | NO | NO |
| Chrome | YES | YES | YES |
| Firefox | YES | YES | YES |
| Safari | YES | NO | NO |
| Opera | YES (从 Opera 25 起) | YES | YES |


- MP4 = 带有 H.264 视频编码和 AAC 音频编码的 MPEG 4 文件
- WebM = 带有 VP8 视频编码和 Vorbis 音频编码的 WebM 文件
- Ogg = 带有 Theora 视频编码和 Vorbis 音频编码的 Ogg 文件


---


## 视频格式


| 格式 | MIME-type |
| --- | --- |
| MP4 | video/mp4 |
| WebM | video/webm |
| Ogg | video/ogg |


---


## HTML5 - 使用 DOM 进行控制


HTML5  和  元素同样拥有方法、属性和事件。


 和 元素的方法、属性和事件可以使用JavaScript进行控制.


其中的方法用于播放、暂停以及加载等。其中的属性（比如时长、音量等）可以被读取或设置。其中的 DOM 事件能够通知您，比方说， 元素开始播放、已暂停，已停止，等等。


例中简单的方法，向我们演示了如何使用  元素，读取并设置属性，以及如何调用方法。


## 实例 1


为视频创建简单的播放/暂停以及调整尺寸控件：


```html
播放/暂停
  放大
  缩小
  普通

    你的浏览器不支持 HTML5 video.
```






上面的例子调用了两个方法：play() 和 pause()。它同时使用了两个属性：paused 和 width。

[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_video_js_prop)


更多参考请查看 [HTML5 Audio/Video DOM 参考手册](https://www.runoob.com/../tags/ref-av-dom.html)。


---


## HTML5 Video 标签


| 标签 | 描述 |
| --- | --- |
|  | 定义一个视频 |
|  | 定义多种媒体资源,比如 和 |
|  | 定义在媒体播放器文本轨迹 |








	  AI 思考中...





			** [HTML5 地理定位](https://www.runoob.com/html5-geolocation.html)
			[HTML5 Audio(音频)](https://www.runoob.com/html5-audio.html) **













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