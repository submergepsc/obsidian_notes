# HTML canvas miterLimit 属性

- Source: https://www.runoob.com/tags/canvas-miterlimit.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


以最大斜接长度 5 绘制线条：


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById("myCanvas");var ctx=c.getContext("2d");
	ctx.lineWidth=10;ctx.lineJoin="miter";ctx.miterLimit=5;
	ctx.moveTo(20,20);ctx.lineTo(50,27);
	ctx.lineTo(20,34);ctx.stroke();
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_miterlimit)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 miterLimit 属性。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


miterLimit 属性设置或返回最大斜接长度。


斜接长度指的是在两条线交汇处内角和外角之间的距离。

![Miter Limit figure 1](https://www.runoob.com/wp-content/uploads/2013/11/img_miterlimitFig.gif)
**提示：**只有当 lineJoin 属性为 "miter" 时，miterLimit 才有效。


边角的角度越小，斜接长度就会越大。


为了避免斜接长度*过长*，我们可以使用 miterLimit 属性。


如果斜接长度超过 miterLimit 的值，边角会以 lineJoin 的 "bevel" 类型来显示（Fig 3）：

![Miter Limit figure 2](https://www.runoob.com/wp-content/uploads/2013/11/img_miterlimitBevelFig.gif)
| 默认值： | 10 |
| --- | --- |
| JavaScript 语法： | context.miterLimit=number; |


## 属性值


| 值 | 描述 |
| --- | --- |
| number | 正数。规定最大斜接长度。如果斜接长度超过 miterLimit 的值，边角会以 lineJoin 的 "bevel" 类型来显示。 |

**
---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas lineWidth 属性](https://www.runoob.com/canvas-linewidth.html)
			[HTML canvas rect() 方法](https://www.runoob.com/canvas-rect.html) **













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