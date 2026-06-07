# HTML canvas quadraticCurveTo() 方法

- Source: https://www.runoob.com/tags/canvas-quadraticcurveto.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


绘制一条二次贝塞尔曲线：


YourbrowserdoesnotsupporttheHTML5canvastag.




JavaScript：


```
var c=document.getElementById("myCanvas");var ctx=c.getContext("2d");ctx.beginPath();ctx.moveTo(20,20);
	ctx.quadraticCurveTo(20,100,200,20);ctx.stroke();
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_quadraticcurveto)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif) ![Firefox](https://www.runoob.com/images/compatible_firefox.gif) ![Opera](https://www.runoob.com/images/compatible_opera.gif) ![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif) ![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 quadraticCurveTo() 方法。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


quadraticCurveTo() 方法通过使用表示二次贝塞尔曲线的指定控制点，向当前路径添加一个点。


二次贝塞尔曲线需要两个点。第一个点是用于二次贝塞尔计算中的控制点，第二个点是曲线的结束点。曲线的开始点是当前路径中最后一个点。如果路径不存在，那么请使用 [beginPath()](https://www.runoob.com/canvas-beginpath.html) 和 [moveTo()](https://www.runoob.com/canvas-moveto.html) 方法来定义开始点。

![二次贝塞尔曲线](https://www.runoob.com/wp-content/uploads/2013/11/img_quadraticcurve.gif)
**


 开始点： moveTo(20,20**)**
 控制点： quadraticCurveTo(20,100**,200,20)**
 结束点： quadraticCurveTo(20,100,200,20**)
**

提示：**请查看 [bezierCurveTo()](https://www.runoob.com/canvas-beziercurveto.html) 方法。 它有两个控制点，而不是一个。

**

| JavaScript 语法： | context.quadraticCurveTo(cpx,cpy,x,y); |
| --- | --- |


## 参数值


| 参数 | 描述 |
| --- | --- |
| cpx | 贝塞尔控制点的 x 坐标。 |
| cpy | 贝塞尔控制点的 y 坐标。 |
| x | 结束点的 x 坐标。 |
| y | 结束点的 y 坐标。 |


---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas clip() 方法](https://www.runoob.com/canvas-clip.html)
			[HTML canvas bezierCurveTo() 方法](https://www.runoob.com/canvas-beziercurveto.html) **













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