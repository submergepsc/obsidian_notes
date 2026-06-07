# HTML canvas addColorStop() 方法

- Source: https://www.runoob.com/tags/canvas-addcolorstop.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


定义一个从黑到白的渐变，作为矩形的填充样式：


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById('myCanvas');
	var ctx=c.getContext('2d');
	var grd=ctx.createLinearGradient(0,0,170,0);
	grd.addColorStop(0,"black");
	grd.addColorStop(1,"white");
	ctx.fillStyle=grd;
	ctx.fillRect(20,20,150,100);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_createlineargradient)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 addColorStop() 方法。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


addColorStop() 方法规定渐变对象中的颜色和位置。


addColorStop() 方法与 [createLinearGradient()](https://www.runoob.com/canvas-createlineargradient.html) 或 [createRadialGradient()](https://www.runoob.com/canvas-createradialgradient.html) 一起使用。


**注意：**您可以多次调用 addColorStop() 方法来改变渐变。如果您不对渐变对象使用该方法，那么渐变将不可见。为了获得可见的渐变，您需要创建至少一个色标。


| JavaScript 语法： | gradient.addColorStop(stop,color); |
| --- | --- |


## 参数值


| 参数 | 描述 |
| --- | --- |
| stop | 介于 0.0 与 1.0 之间的值，表示渐变中开始与结束之间的位置。 |
| color | 在 stop 位置显示的 CSS 颜色值。 |

**
---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


## 实例


通过多个 addColorStop() 方法来定义渐变：


Yourbrowserdoesnotsupportthecanvastag.


JavaScript：


```
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
var grd=ctx.createLinearGradient(0,0,170,0);
grd.addColorStop(0,"black");
grd.addColorStop("0.3","magenta");
grd.addColorStop("0.5","blue");
grd.addColorStop("0.6","green");
grd.addColorStop("0.8","yellow");
grd.addColorStop(1,"red");
ctx.fillStyle=grd;
ctx.fillRect(20,20,150,100);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_addcolorstop_multiple)


---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas createRadialGradient() 方法](https://www.runoob.com/canvas-createradialgradient.html)
			[HTML canvas lineCap 属性](https://www.runoob.com/canvas-linecap.html) **













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