# HTML Audio/Video DOM error 事件

- Source: https://www.runoob.com/tags/av-event-error.html

[![HTML audio/video 标签参考手册](https://www.runoob.com/images/up.gif) HTML 音频/视频 DOM 参考手册](https://www.runoob.com/ref-av-dom.html)


## 实例


视频加载发生错误时弹出错误提示信息：


```
var vid = document.getElementById("myVideo");vid.onerror =
	function() {    alert("Error! 出错了");
	};
```


**


---


## 定义和用法


error 事件在音频/视频(audio/video)加载发生错误时触发。


提示：** 影响多媒体数据加载的事件有：


- [abort](https://www.runoob.com/av-event-abort.html)
- emptied
- [stalled](https://www.runoob.com/av-event-stalled.html)
- [suspend](https://www.runoob.com/av-event-suspend.html)


---


## 浏览器支持


表格中的数字表示支持该事件的第一个浏览器的版本号。


| 事件 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| error | Yes | 9.0 | Yes | Yes | Yes |

**
---


## 语法


HTML 中：


<*element* onerror="*myScript*">

JavaScript 中：


	*object*.onerror=function(){*myScript*};

JavaScript 中, 使用 addEventListener() 方法:


	*object*.addEventListener("error", *myScript*);

注意：** Internet Explorer 8 及更早 IE 版本不支持 [addEventListener()](https://www.runoob.com/met-element-addeventlistener.html) 方法。


---

技术细节

| 支持的 HTML 标签: | and |
| --- | --- |
| 支持的JavaScript对象： | Audio, Video |

**
---

[![HTML audio/video 标签参考手册](https://www.runoob.com/images/up.gif) HTML 音频/视频 DOM 参考手册](https://www.runoob.com/ref-av-dom.html)







	  AI 思考中...





			** [HTML Audio/Video DOM ended 事件](https://www.runoob.com/av-event-ended.html)
			[HTML Audio/Video DOM pause 事件](https://www.runoob.com/av-event-pause.html) **













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