# HTML canvas font 属性

- Source: https://www.runoob.com/tags/canvas-font.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


在画布上写一段 30 像素的文本，使用的字体是 "Arial"：


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById("myCanvas");var ctx=c.getContext("2d");
	ctx.font="30px Arial";ctx.fillText("Hello World",10,50);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_font)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 font 属性。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


font 属性设置或返回画布上文本内容的当前字体属性。


font 属性使用的语法与 [CSS font 属性](https://www.runoob.com/../cssref/pr-font-font.html) 相同。


| 默认值： | 10px sans-serif |
| --- | --- |
| JavaScript 语法： | context.font="italic small-caps bold 12px arial"; |


## 属性值


| 值 | 描述 |
| --- | --- |
| font-style | 规定字体样式。可能的值： normal italic oblique |
| font-variant | 规定字体变体。可能的值： normal small-caps |
| font-weight | 规定字体的粗细。可能的值： normal bold bolder lighter 100 200 300 400 500 600 700 800 900 |
| font-size/line-height | 规定字号和行高，以像素计。 |
| font-family | 规定字体系列。 |
| caption | 使用标题控件的字体（比如按钮、下拉列表等）。 |
| icon | 使用用于标记图标的字体。 |
| menu | 使用用于菜单中的字体（下拉列表和菜单列表）。 |
| message-box | 使用用于对话框中的字体。 |
| small-caption | 使用用于标记小型控件的字体。 |
| status-bar | 使用用于窗口状态栏中的字体。 |

**
---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas setTransform() 方法](https://www.runoob.com/canvas-settransform.html)
			[HTML canvas textAlign 属性](https://www.runoob.com/canvas-textalign.html) **













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