# HTML 音频/视频 DOM addTextTrack() 方法

- Source: https://www.runoob.com/tags/av-met-addtexttrack.html

[![HTML audio/video 标签参考手册](https://www.runoob.com/images/up.gif) HTML 音频/视频 DOM 参考手册](https://www.runoob.com/ref-av-dom.html)


## 实例


向视频添加一个新的文本轨道：


```
text1=myVid.addTextTrack("caption");text1.addCue(new TextTrackCue("Test
	text", 01.000, 04.000,"","","",true));
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_av_met_addtexttrack)


---


## 定义和用法


addTextTrack() 方法创建和返回新的 TextTrack 对象。


新的 TextTrack 对象会被添加到视频/音频（audio/video）元素的文本轨道列表中。


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/incompatible_ie.gif)![Firefox](https://www.runoob.com/images/incompatible_firefox.gif)![Opera](https://www.runoob.com/images/incompatible_opera.gif)![Google Chrome](https://www.runoob.com/images/incompatible_chrome.gif)![Safari](https://www.runoob.com/images/incompatible_safari.gif)


所有主流浏览器都不支持 addTextTrack() 方法。


---


## 语法



		*audio|video*.addTextTrack(*kind*,*label*,*language*)



## 参数


| 值 | 描述 |
| --- | --- |
| kind | 规定文本轨道的类型。可能的值： "subtitles" "caption" "descriptions" "chapters" "metadata" |
| label | 字符串值，为文本轨道规定标签。用于为用户对文本轨道进行标识。 |
| language | 双字母语言代码，规定文本轨道的语言。 如需查看所有可用的语言代码，请参阅我们的 语言代码参考手册。 |


## 返回值


| 类型 | 描述 |
| --- | --- |
| TextTrack 对象 | 表示新的文本轨道。 |


---

[![HTML audio/video 标签参考手册](https://www.runoob.com/images/up.gif) HTML 音频/视频 DOM 参考手册](https://www.runoob.com/ref-av-dom.html)







	  AI 思考中...





			** [HTML canvas globalCompositeOperation 属性](https://www.runoob.com/canvas-globalcompositeoperation.html)
			[HTML 音频/视频 DOM canPlayType() 方法](https://www.runoob.com/av-met-canplaytype.html) **













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