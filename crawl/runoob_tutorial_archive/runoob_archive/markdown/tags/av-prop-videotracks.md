# HTML 音频/视频 DOM videoTracks 属性

- Source: https://www.runoob.com/tags/av-prop-videotracks.html

[![HTML audio/video 标签参考手册](https://www.runoob.com/images/up.gif) HTML 音频/视频 DOM 参考手册](https://www.runoob.com/ref-av-dom.html)


## 实例


获得可用视频轨道的数量：


```
myVid=document.getElementById("video1");alert(myVid.videoTracks.length);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_av_prop_videotracks)


---


## 定义和用法


videoTracks 属性返回 VideoTrackList 对象。


VideoTrackList 对象表示视频的可用视频轨道。


每个可用的视频轨道是由 VideoTrack 对象表示的。


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/incompatible_ie.gif)![Firefox](https://www.runoob.com/images/incompatible_firefox.gif)![Opera](https://www.runoob.com/images/incompatible_opera.gif)![Google Chrome](https://www.runoob.com/images/incompatible_chrome.gif)![Safari](https://www.runoob.com/images/incompatible_safari.gif)


所有主流浏览器都不支持 videoTracks 属性。


---


## 语法



		*video*.videoTracks


## 返回值


| 类型 | 描述 |
| --- | --- |
| VideoTrackList 对象 | 表示视频的可用视频轨道。 VideoTrackList 对象： videoTracks.length - 获得视频中可用视频轨道的数量 videoTracks.getTrackById(id) - 通过 id 获得 VideoTrack 对象 videoTracks[index] - 通过下标 index 获得 VideoTrack 对象 videoTracks.selectedIndex - 获得当前 VideoTrack 对象的下标 注释：第一个可用 VideoTrack 对象的下标 index 是 0。 |
| VideoTrack 对象 | 表示一个视频轨道。VideoTrack 对象的属性： id - 获得视频轨道的 id kind - 获得视频轨道的类型（可以是 "alternative"、"captions"、"main"、"sign"、"subtitles"、"commentary" 或 ""（空字符串）） label - 获得视频轨道的标签 language - 获得视频轨道的语言 selected - 获得或设置视频轨道是否是活动的（true\|false） |


---

[![HTML audio/video 标签参考手册](https://www.runoob.com/images/up.gif) HTML 音频/视频 DOM 参考手册](https://www.runoob.com/ref-av-dom.html)







	  AI 思考中...





			** [HTML 音频/视频 DOM textTracks 属性](https://www.runoob.com/av-prop-texttracks.html)
			[HTML 音频/视频 DOM volume 属性](https://www.runoob.com/av-prop-volume.html) **













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