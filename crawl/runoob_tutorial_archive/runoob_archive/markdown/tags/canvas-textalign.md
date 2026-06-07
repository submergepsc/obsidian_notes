# HTML canvas textAlign 属性

- Source: https://www.runoob.com/tags/canvas-textalign.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


在位置 150 创建一条红线。位置 150 是下面实例中定义的所有文本的锚点。请研究每种 textAlign 属性值的效果：


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById("myCanvas");
	var ctx=c.getContext("2d");
	// Create a red line in position 150
	ctx.strokeStyle="red";
	ctx.moveTo(150,20);
	ctx.lineTo(150,170);
	ctx.stroke();
	ctx.font="15px Arial";
	// Show the different textAlign values
	ctx.textAlign="start";
	ctx.fillText("textAlign=start",150,60);
	ctx.textAlign="end";
	ctx.fillText("textAlign=end",150,80);
	ctx.textAlign="left";
	ctx.fillText("textAlign=left",150,100);
	ctx.textAlign="center";
	ctx.fillText("textAlign=center",150,120);
	ctx.textAlign="right";
	ctx.fillText("textAlign=right",150,140);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_textalign)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 textAlign 属性。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


textAlign 属性根据锚点，设置或返回文本内容的当前对齐方式。


通常，文本会从指定位置**开始**，不过，如果您设置为 textAlign="right" 并将文本放置到位置 150，那么会在**位置 150** **结束**。


**提示：**请使用 [fillText()](https://www.runoob.com/canvas-filltext.html) 或 [strokeText()](https://www.runoob.com/canvas-stroketext.html) 方法在画布上实际地绘制并定位文本。


| 默认值： | start |
| --- | --- |
| JavaScript 语法： | context.textAlign="center\|end\|left\|right\|start"; |


## 属性值


| 值 | 描述 |
| --- | --- |
| start | 默认。文本在指定的位置开始。 |
| end | 文本在指定的位置结束。 |
| center | 文本的中心被放置在指定的位置。 |
| left | 文本在指定的位置开始。 |
| right | 文本在指定的位置结束。 |

**
---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas font 属性](https://www.runoob.com/canvas-font.html)
			[HTML canvas textBaseline 属性](https://www.runoob.com/canvas-textbaseline.html) **













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