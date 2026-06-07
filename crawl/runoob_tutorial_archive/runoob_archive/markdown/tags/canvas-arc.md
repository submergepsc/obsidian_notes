# HTML canvas arc() 方法

- Source: https://www.runoob.com/tags/canvas-arc.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


创建一个圆形：


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById("myCanvas");var ctx=c.getContext("2d");
	ctx.beginPath();ctx.arc(100,75,50,0,2*Math.PI);ctx.stroke();
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_arc)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 arc() 方法。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


arc() 方法创建弧/曲线（用于创建圆或部分圆）。


**提示：**如需通过 arc() 来创建圆，请把起始角设置为 0，结束角设置为 2*Math.PI。


**提示：**请使用 [stroke()](https://www.runoob.com/canvas-stroke.html) 或 [fill()](https://www.runoob.com/canvas-fill.html) 方法在画布上绘制实际的弧。


![An arc](https://www.runoob.com/wp-content/uploads/2013/11/img_arc.gif)


中心： arc(**100,75**,50,0*Math.PI,1.5*Math.PI)


起始角： arc(100,75,50,**0**,1.5*Math.PI)


结束角： arc(100,75,50,0*Math.PI,**1.5*Math.PI**)

**

| JavaScript 语法： | context.arc(x,y,r,sAngle,eAngle,counterclockwise); |
| --- | --- |


## 参数值


| 参数 | 描述 | x | 圆的中心的 x 坐标。 |
| --- | --- | --- | --- |
| y | 圆的中心的 y 坐标。 |  |  |
| r | 圆的半径。 |  |  |
| sAngle | 起始角，以弧度计（弧的圆形的三点钟位置是 0 度）。 |  |  |
| eAngle | 结束角，以弧度计。 |  |  |
| counterclockwise | 可选。规定应该逆时针还是顺时针绘图。False = 顺时针，true = 逆时针。 |  |  |


---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas bezierCurveTo() 方法](https://www.runoob.com/canvas-beziercurveto.html)
			[HTML canvas arcTo() 方法](https://www.runoob.com/canvas-arcto.html) **













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