# HTML5 Audio(音频)

- Source: https://www.runoob.com/html/html5-audio.html

---


HTML5 提供了播放音频文件的标准。


---


## 互联网上的音频


直到现在，仍然不存在一项旨在网页上播放音频的标准。


今天，大多数音频是通过插件（比如 Flash）来播放的。然而，并非所有浏览器都拥有同样的插件。


HTML5 规定了在网页上嵌入音频元素的标准，即使用  元素。


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9+, Firefox, Opera, Chrome, 和 Safari 都支持  元素.


**注意:** Internet Explorer 8 及更早IE版本不支持  元素.


---


## HTML5 Audio - 如何工作


如需在 HTML5 中播放音频，你需要使用以下代码：


## 实例


```html
<audio controls>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
您的浏览器不支持 audio 元素。
</audio>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_audio_all)


control 属性供添加播放、暂停和音量控件。


在 与  之间你需要插入浏览器不支持的元素的提示文本 。


 元素允许使用多个  元素.  元素可以链接不同的音频文件，浏览器将使用第一个支持的音频文件


---


## 音频格式及浏览器支持


目前, 元素支持三种音频格式文件: MP3, Wav, 和 Ogg:


| 浏览器 | MP3 | Wav | Ogg |
| --- | --- | --- | --- |
| Internet Explorer 9+ | YES | NO | NO |
| Chrome 6+ | YES | YES | YES |
| Firefox 3.6+ | YES | YES | YES |
| Safari 5+ | YES | YES | NO |
| Opera 10+ | YES | YES | YES |


---


## 音频格式的MIME类型


| Format | MIME-type |
| --- | --- |
| MP3 | audio/mpeg |
| Ogg | audio/ogg |
| Wav | audio/wav |


---


## HTML5 Audio 标签


| 标签 | 描述 |
| --- | --- |
|  | 定义了声音内容 |
|  | 规定了多媒体资源, 可以是多个，在 与 标签中使用 |









	  AI 思考中...





			** [HTML5 Video(视频)](https://www.runoob.com/html5-video.html)
			[HTML5 Input 类型](https://www.runoob.com/html5-form-input-types.html) **













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