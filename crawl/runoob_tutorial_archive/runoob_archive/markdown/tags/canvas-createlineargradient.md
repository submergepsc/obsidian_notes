# HTML canvas createLinearGradient() 方法

- Source: https://www.runoob.com/tags/canvas-createlineargradient.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


定义从黑到白的渐变（从左向右），作为矩形的填充样式：


YourbrowserdoesnotsupporttheHTML5canvastag.


JavaScript：


```
var c=document.getElementById("myCanvas");var
	ctx=c.getContext("2d");var grd=ctx.createLinearGradient(0,0,170,0);
	grd.addColorStop(0,"black");
	grd.addColorStop(1,"white");
	ctx.fillStyle=grd;
	ctx.fillRect(20,20,150,100);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_createlineargradient)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 createLinearGradient() 方法。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


createLinearGradient() 方法创建线性的渐变对象。


渐变可用于填充矩形、圆形、线条、文本等等。


**提示：**请使用该对象作为 [strokeStyle](https://www.runoob.com/canvas-strokestyle.html) 或 [fillStyle](https://www.runoob.com/canvas-fillstyle.html) 属性的值。


**提示：**请使用 [addColorStop()](https://www.runoob.com/canvas-addcolorstop.html) 方法规定不同的颜色，以及在 gradient 对象中的何处定位颜色。


| JavaScript 语法： | context.createLinearGradient(x0,y0,x1,y1); |
| --- | --- |


## 参数值


| 参数 | 描述 |
| --- | --- |
| x0 | 渐变开始点的 x 坐标 |
| y0 | 渐变开始点的 y 坐标 |
| x1 | 渐变结束点的 x 坐标 |
| y1 | 渐变结束点的 y 坐标 |

**
---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


## 实例


定义一个渐变（从上到下）作为矩形的填充样式：


Yourbrowserdoesnotsupportthecanvastag.


JavaScript：


```
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
var my_gradient=ctx.createLinearGradient(0,0,0,170);
my_gradient.addColorStop(0,"black");
my_gradient.addColorStop(1,"white");
ctx.fillStyle=my_gradient;
ctx.fillRect(20,20,150,100);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_fillstyle_gradient)


## 实例


定义一个从黑到红再到白的渐变，作为矩形的填充样式：


Yourbrowserdoesnotsupportthecanvastag.


JavaScript：


```
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
var my_gradient=ctx.createLinearGradient(0,0,170,0);
my_gradient.addColorStop(0,"black");
my_gradient.addColorStop(0.5,"red");
my_gradient.addColorStop(1,"white");
ctx.fillStyle=my_gradient;
ctx.fillRect(20,20,150,100);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_fillstyle_gradient3)


---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas shadowOffsetY 属性](https://www.runoob.com/canvas-shadowoffsety.html)
			[HTML canvas createPattern() 方法](https://www.runoob.com/canvas-createpattern.html) **













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