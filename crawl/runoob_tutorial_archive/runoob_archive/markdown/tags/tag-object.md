# HTML 标签

- Source: https://www.runoob.com/tags/tag-object.html

**
## 实例


使用 元素在 HTML 加入 Flash 文件：


```
<object width="400" height="400" data="helloworld.swf"></object>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_object)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif) ![Firefox](https://www.runoob.com/images/compatible_firefox.gif) ![Opera](https://www.runoob.com/images/compatible_opera.gif) ![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif) ![Safari](https://www.runoob.com/images/compatible_safari.gif)


目前大多数浏览器支持  标签。


---


## 标签定义及使用说明


定义一个嵌入的对象。请使用此元素向您的 XHTML 页面添加多媒体。此元素允许您规定插入 HTML 文档中的对象的数据和参数，以及可用来显示和操作数据的代码。


 标签用于包含对象，比如图像、音频、视频、Java applets、ActiveX、PDF 以及 Flash。


object 的初衷是取代 img 和 applet 元素。不过由于漏洞以及缺乏浏览器支持，这一点并未实现。


浏览器的对象支持有赖于对象类型。不幸的是，主流浏览器都使用不同的代码来加载相同的对象类型。


而幸运的是，object 对象提供了解决方案。如果未显示 object 元素，就会执行位于  和  之间的代码。通过这种方式，我们能够嵌套多个 object 元素（每个对应一个浏览器）。


---


## HTML 4.01 与 HTML5中的差异


一些 HTML 4.01 属性在 HTML5 中不被支持。


"form" 是 HTML5 定义的新属性。


在 HTML5 中，objects 可以在form表单中提交。


在 HTML5 中，objects 不再出现在  元素区域内。


---


## 属性


New：HTML5 新属性。


| 属性 | 值 | 描述 |
| --- | --- | --- |
| align | top bottom middle left right | HTML5 不支持。HTML 4.01 已废弃。 规定 元素相对于周围元素的对齐方式。 |
| archive | URL | HTML5 不支持。由空格分隔的指向档案文件的 URL 列表。这些档案文件包含了与对象相关的资源。 |
| border | pixels | HTML5 不支持。HTML 4.01 已废弃。 规定 周围的边框宽度。 |
| classid | class_ID | HTML5 不支持。定义嵌入 Windows Registry 中或某个 URL 中的类的 ID 值，此属性可用来指定浏览器中包含的对象的位置，通常是一个 Java 类。 |
| codebase | URL | HTML5 不支持。定义在何处可找到对象所需的代码，提供一个基准 URL。 |
| codetype | MIME_type | HTML5 不支持。通过 classid 属性所引用的代码的 MIME 类型。 |
| data | URL | 规定对象使用的资源的 URL。 |
| declare | declare | HTML5 不支持。定义该对象仅可被声明，但不能被创建或例示，直到该对象得到应用为止。 |
| formNew | form_id | 规定对象所属的一个或多个表单。 |
| height | pixels | 规定对象的高度。 |
| hspace | pixels | HTML5 不支持。HTML 4.01 已废弃。 规定对象左侧和右侧的空白。 |
| name | name | 为对象规定名称。 |
| standby | text | HTML5 不支持。定义当对象正在加载时所显示的文本。 |
| type | MIME_type | 规定 data 属性中规定的数据的 MIME 类型。 |
| usemap | #mapname | 规定与对象一同使用的客户端图像映射的名称。 |
| vspace | pixels | HTML5 不支持。HTML 4.01 已废弃。 规定对象的顶部和底部的空白。 |
| width | pixels | 规定对象的宽度。 |


---


## 全局属性


 标签支持全局属性，查看完整属性表 [HTML全局属性](https://www.runoob.com/ref-standardattributes.html)。


---


## 事件属性


 标签支持所有 [HTML事件属性](https://www.runoob.com/ref-eventattributes.html)。


---


## 相关文章


HTML 教程：[HTML Object 元素](https://www.runoob.com/../html/html-object.html)








	  AI 思考中...





			** [HTML  标签](https://www.runoob.com/tag-ol.html)
			[HTML  标签](https://www.runoob.com/tag-noscript.html) **













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