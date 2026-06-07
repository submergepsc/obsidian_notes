# HTML 标签

- Source: https://www.runoob.com/tags/tag-map.html

**
## 实例


带有可点击区域的图像映射：


```
<img src="planets.gif"
      width="145" height="126"
      alt="Planets"
      usemap="#planetmap">
      <map
      name="planetmap">

      <area shape="rect" coords="0,0,82,126" href="sun.htm" alt="Sun">

      <area shape="circle" coords="90,58,3" href="mercur.htm" alt="Mercury">

      <area shape="circle" coords="124,58,8" href="venus.htm" alt="Venus">
      </map>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_areamap)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif) ![Firefox](https://www.runoob.com/images/compatible_firefox.gif) ![Opera](https://www.runoob.com/images/compatible_opera.gif) ![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif) ![Safari](https://www.runoob.com/images/compatible_safari.gif)


目前大多数浏览器支持 标签。


---


## 标签定义及使用说明


 标签用于客户端图像映射。图像映射指带有可点击区域的一幅图像。


中的 usemap 属性可引用  中的 id 或 name 属性（取决于浏览器），所以我们应同时向  添加 id 和 name 属性。


area 元素永远嵌套在 map 元素内部。area 元素可定义图像映射中的区域。


---


## HTML 4.01 与 HTML5之间的差异


注意:** 在 HTML5 中, 如果 id 属性在 标签中指定, 则你必须同样指定 name 属性。


---


## HTML 与 XHTML 之间的差异


在 XHTML 中，name 属性已经废弃，使用 id 属性替换它。


---


## 属性


| 属性 | 值 | 描述 |
| --- | --- | --- |
| name | mapname | 必需。为 image-map 规定的名称。 |

**
---


## 全局属性


 标签支持全局属性，查看完整属性表 [HTML全局属性](https://www.runoob.com/ref-standardattributes.html)。


---


## 事件属性


 标签支持所有 [HTML事件属性](https://www.runoob.com/ref-eventattributes.html)。








	  AI 思考中...





			** [HTML5  标签](https://www.runoob.com/tag-mark.html)
			[HTML 标签](https://www.runoob.com/tag-link.html) **













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