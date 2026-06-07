# HTML 标签

- Source: https://www.runoob.com/tags/tag-video.html

**
## 实例


播放录像：


```
<video width="320" height="240" controls>
    <source src="movie.mp4" type="video/mp4">
    <source src="movie.ogg" type="video/ogg">
    您的浏览器不支持 video 标签。
</video>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_video)


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


| 元素 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 4.0 | 9.0 | 3.5 | 4.0 | 10.5 |


---


## 标签定义及使用说明


 标签定义视频，比如电影片段或其他视频流。


目前， 元素支持三种视频格式：MP4、WebM、Ogg。


| 浏览器 | MP4 | WebM | Ogg |
| --- | --- | --- | --- |
| Internet Explorer | YES | NO | NO |
| Chrome | YES | YES | YES |
| Firefox | YES从 Firefox 21 版本开始Linux 系统从 Firefox 30 开始 | YES | YES |
| Safari | YES | NO | NO |
| Opera | YES从 Opera 25 版本开始 | YES | YES |


- MP4 = MPEG 4文件使用 H264 视频编解码器和AAC音频编解码器
- WebM = WebM 文件使用 VP8 视频编解码器和 Vorbis 音频编解码器
- Ogg = Ogg 文件使用 Theora 视频编解码器和 Vorbis音频编解码器


由于不同浏览器支持不同的视频格式，通常建议提供多种格式：


## 实例


```
<video controls width="640" height="360">
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.webm" type="video/webm">
  您的浏览器不支持 HTML5 video 标签。
</video>
```


---


## 视频格式的 MIME 类型


| 格式 | MIME-type |
| --- | --- |
| MP4 | video/mp4 |
| WebM | video/webm |
| Ogg | video/ogg |


---


## HTML 4.01 与 HTML5之间的差异


 标签是 HTML5 的新标签。


---


## 提示和注释


提示：**可以在  和  标签之间放置文本内容，这样不支持  元素的浏览器就可以显示出该标签的信息。


---


## 可选属性


New ：HTML5 中的新属性。


| 属性 | 值 | 描述 |
| --- | --- | --- |
| autoplayNew | autoplay | 如果出现该属性，则视频在就绪后马上播放。 |
| controlsNew | controls | 如果出现该属性，则向用户显示控件，比如播放按钮。 |
| heightNew | pixels | 设置视频播放器的高度。 |
| loopNew | loop | 如果出现该属性，则当媒介文件完成播放后再次开始播放。 |
| mutedNew | muted | 如果出现该属性，视频的音频输出为静音。 |
| posterNew | URL | 规定视频正在下载时显示的图像，直到用户点击播放按钮。 |
| preloadNew | auto metadata none | 如果出现该属性，则视频在页面加载时进行加载，并预备播放。如果使用 "autoplay"，则忽略该属性。 |
| srcNew | URL | 要播放的视频的 URL。 |
| widthNew | pixels | 设置视频播放器的宽度。 |


## 全局属性


 标签支持 [HTML 的全局属性](https://www.runoob.com/ref-standardattributes.html)。


---


## 事件属性


 标签支持 [HTML 的事件属性](https://www.runoob.com/ref-eventattributes.html)。








	  AI 思考中...





			** [HTML  标签](https://www.runoob.com/tag-wbr.html)
			[HTML  标签](https://www.runoob.com/tag-ul.html) **













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

      : · [HTML ASCII 字符集](https://www.runoob.com/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/html-colorpicker.html)

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