# HTML canvas textBaseline 属性

- Source: https://www.runoob.com/tags/canvas-textbaseline.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


在 y=100 处绘制一条红线，然后在 y=100 处用不同的 textBaseline 值放置每个单词：


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById("myCanvas");
	var ctx=c.getContext("2d");
	//Draw a red line at y=100
	ctx.strokeStyle="red";
	ctx.moveTo(5,100);
	ctx.lineTo(395,100);
	ctx.stroke();
	ctx.font="20px Arial"
	//Place each word at y=100 with different textBaseline values
	ctx.textBaseline="top";
	ctx.fillText("Top",5,100);
	ctx.textBaseline="bottom";
	ctx.fillText("Bottom",50,100);
	ctx.textBaseline="middle";
	ctx.fillText("Middle",120,100);
	ctx.textBaseline="alphabetic";
	ctx.fillText("Alphabetic",190,100);
	ctx.textBaseline="hanging";
	ctx.fillText("Hanging",290,100);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_textbaseline)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 textBaseline 属性。


注意：**textBaseline 属性在不同的浏览器上效果不同，特别是使用 "hanging" 或 "ideographic" 时。


**注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


textBaseline 属性设置或返回在绘制文本时的当前文本基线。


下面的图示演示了 textBaseline 属性支持的各种基线：

![textBaseline illustration](https://www.runoob.com/wp-content/uploads/2013/11/img_textbaseline.gif)
**注意：**[fillText()](https://www.runoob.com/canvas-filltext.html) 和 [strokeText()](https://www.runoob.com/canvas-stroketext.html) 方法在画布上定位文本时，将使用指定的 textBaseline 值。


| 默认值： | alphabetic |
| --- | --- |
| JavaScript 语法： | context.textBaseline="alphabetic\|top\|hanging\|middle\|ideographic\|bottom"; |


## 属性值


| 值 | 描述 |
| --- | --- |
| alphabetic | 默认。文本基线是普通的字母基线。 |
| top | 文本基线是 em 方框的顶端。 |
| hanging | 文本基线是悬挂基线。 |
| middle | 文本基线是 em 方框的正中。 |
| ideographic | 文本基线是表意基线。 |
| bottom | 文本基线是 em 方框的底端。 |

**
---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas textAlign 属性](https://www.runoob.com/canvas-textalign.html)
			[HTML canvas fillText() 方法](https://www.runoob.com/canvas-filltext.html) **













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