# HTML 音频/视频 DOM audioTracks 属性

- Source: https://www.runoob.com/tags/av-prop-audiotracks.html

[![HTML audio/video 标签参考手册](https://www.runoob.com/images/up.gif) HTML 音频/视频 DOM 参考手册](https://www.runoob.com/ref-av-dom.html)


## 实例


获得可用音频轨道的数量：


```
myVid=document.getElementById("video1");alert(myVid.audioTracks.length);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_av_prop_audiotracks)


---


## 定义和用法


audioTracks 属性返回 AudioTrackList 对象。


AudioTrackList 对象表示音频/视频的可用音频轨道。


每个可用的音频轨道由一个 AudioTrack 对象表示。


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/incompatible_ie.gif)![Firefox](https://www.runoob.com/images/incompatible_firefox.gif)![Opera](https://www.runoob.com/images/incompatible_opera.gif)![Google Chrome](https://www.runoob.com/images/incompatible_chrome.gif)![Safari](https://www.runoob.com/images/incompatible_safari.gif)


所有主流浏览器都不支持 audioTracks 属性。


---


## 语法



		*audio|video*.audioTracks


## 返回值


| 类型 | 描述 |
| --- | --- |
| AudioTrackList 对象 | 表示音频/视频的可用音频轨道。 AudioTrackList 对象： audioTracks.length - 获得可用音频轨道的数量 audioTracks.getTrackById(id) - 通过 id 来获得 AudioTrack 对象 audioTracks[index] - 通过 index 来获得 AudioTrack 对象 注释：第一个可用的 AudioTrack 对象的下标是 0。 |
| AudioTrack 对象 | 表示音频轨道。AudioTrack 对象的属性： id - 获得音频轨道的 id kind - 获得音频轨道的类型（可以是 "alternative"、"description"、"main"、"translation"、"commentary" 或者 ""（空字符串）） label - 获得音频轨道的标签 language - 获得音频轨道的语言 enabled - 获得或设置音频轨道是否是活动的（true\|false） |


---

[![HTML audio/video 标签参考手册](https://www.runoob.com/images/up.gif) HTML 音频/视频 DOM 参考手册](https://www.runoob.com/ref-av-dom.html)







	  AI 思考中...





			** [HTML 音频/视频 DOM pause() 方法](https://www.runoob.com/av-met-pause.html)
			[HTML 音频/视频 DOM autoplay 属性](https://www.runoob.com/av-prop-autoplay.html) **













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