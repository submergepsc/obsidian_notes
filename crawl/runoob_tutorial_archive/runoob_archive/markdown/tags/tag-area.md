# HTML 标签

- Source: https://www.runoob.com/tags/tag-area.html

**


## 实例


带有可点击区域的图像映射：


```
<img src="planets.gif" width="145" height="126" alt="Planets" usemap="#planetmap">

<map name="planetmap">
  <area shape="rect" coords="0,0,82,126" alt="Sun" href="sun.htm">
  <area shape="circle" coords="90,58,3" alt="Mercury" href="mercur.htm">
  <area shape="circle" coords="124,58,8" alt="Venus" href="venus.htm">
</map>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_areamap)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif) ![Firefox](https://www.runoob.com/images/compatible_firefox.gif) ![Opera](https://www.runoob.com/images/compatible_opera.gif) ![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif) ![Safari](https://www.runoob.com/images/compatible_safari.gif)


所有主流浏览器都支持  标签。


---


## 标签定义及使用说明


 标签定义图像映射内部的区域（图像映射指的是带有可点击区域的图像）。


 元素始终嵌套在  标签内部。


注释：** [](https://www.runoob.com/tag-img.html) 标签中的 usemap 属性与 [](https://www.runoob.com/tag-map.html) 元素中的 name 相关联，以创建图像与映射之间的关系。


---


## HTML 4.01 与 HTML5之间的差异


HTML5 提供了一些新属性，同时不再支持 HTML 4.01 中的某些属性。


---


## HTML 与 XHTML 之间的差异


在 HTML 中， 标签没有结束标签。


在 XHTML 中， 标签必须正确地关闭。


---


## 属性


New ：HTML5 中的新属性。


| 属性 | 值 | 描述 |
| --- | --- | --- |
| alt | text | 规定区域的替代文本。如果使用 href 属性，则该属性是必需的。 |
| coords | coordinates | 规定区域的坐标。 |
| href | URL | 规定区域的目标 URL。 |
| hreflangNew | language_code | 规定目标 URL 的语言。 |
| mediaNew | media query | 规定目标 URL 是为何种媒介/设备优化的。默认：all。 |
| nohref | value | HTML5 不支持。 规定没有相关链接的区域。 |
| relNew | alternate author bookmark help license next nofollow noreferrer prefetch prev search tag | 规定当前文档与目标 URL 之间的关系。 |
| shape | default rect circle poly | 规定区域的形状。 |
| target | _blank _parent _self _top framename | 规定在何处打开目标 URL。 |
| typeNew | MIME_type | 规定目标 URL 的 MIME 类型。注：MIME = Multipurpose Internet Mail Extensions。 |


## 全局属性


 标签支持 [HTML 的全局属性](https://www.runoob.com/ref-standardattributes.html)。


---


## 事件属性


 标签支持 [HTML 的事件属性](https://www.runoob.com/ref-eventattributes.html)。


---


## 相关文章


HTML DOM 参考手册： [Area 对象](https://www.runoob.com/tag-area.html)








	  AI 思考中...





			** [HTML  标签](https://www.runoob.com/tag-applet.html)
			[HTML  标签](https://www.runoob.com/tag-article.html) **













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