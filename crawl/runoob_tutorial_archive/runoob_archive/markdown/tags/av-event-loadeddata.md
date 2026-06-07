# HTML 音频/视频 DOM loadeddata 事件

- Source: https://www.runoob.com/tags/av-event-loadeddata.html

[![HTML audio/video 标签参考手册](https://www.runoob.com/images/up.gif) HTML 音频/视频 DOM 参考手册](https://www.runoob.com/ref-av-dom.html)


## 实例


提示当前帧的数据是可用的：


```
myVid=document.getElementById("video1");myVid.onloadeddata=alert("Browser
	has loaded the current frame");
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_av_event_loadeddata)


---


## 定义和用法


当当前帧的数据已加载，但没有足够的数据来播放指定音频/视频的下一帧时，会发生 loadeddata 事件。


当音频/视频处于加载过程中时，会依次发生以下事件：


- [loadstart](https://www.runoob.com/av-event-loadstart.html)
- [durationchange](https://www.runoob.com/av-event-durationchange.html)
- [loadedmetadata](https://www.runoob.com/av-event-loadedmetadata.html)
- loadeddata
- [progress](https://www.runoob.com/av-event-progress.html)
- [canplay](https://www.runoob.com/av-event-canplay.html)
- [canplaythrough](https://www.runoob.com/av-event-canplaythrough.html)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


所有主流浏览器都支持 loadeddata 事件。


注意：**Internet Explorer 8 及之前的版本不支持该事件。


---


## 语法


在 HTML 中：


	*<audio|video* onloadeddata="*SomeJavaScriptCode*">

在 JavaScript 中：


	*audio|video*.onloadeddata=*SomeJavaScriptCode*;

使用 addEventListener()：


	*audio|video*.addEventListener("loadeddata", function()**  {
  *
	//SomeJavaScriptCode*

	}
);


## 技术细节


| 以下 HTML 标签支持： | , |
| --- | --- |
| 以下 JavaScript 对象支持： | Audio, Video |


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[在 HTML 元素上使用 onloadeddata 属性](https://www.runoob.com/try/try.php?filename=tryhtml5_av_event_loadeddata_html)


[使用 addEventListener() 来监听 loadeddata 事件](https://www.runoob.com/try/try.php?filename=tryhtml5_av_event_loadeddata_el)


---

[![HTML audio/video 标签参考手册](https://www.runoob.com/images/up.gif) HTML 音频/视频 DOM 参考手册](https://www.runoob.com/ref-av-dom.html)







	  AI 思考中...





			** [HTML 音频/视频 DOM durationchange 事件](https://www.runoob.com/av-event-durationchange.html)
			[HTML 音频/视频 DOM loadedmetadata 事件](https://www.runoob.com/av-event-loadedmetadata.html) **













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