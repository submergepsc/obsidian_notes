# HTML canvas arcTo() 方法

- Source: https://www.runoob.com/tags/canvas-arcto.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


在画布上创建介于两个切线之间的弧：


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.beginPath();
ctx.moveTo(20,20);           // 创建起始点
ctx.lineTo(100,20);          // 创建水平线
ctx.arcTo(150,20,150,70,50); // 创建弧
ctx.lineTo(150,120);         // 创建垂直线
ctx.stroke();                // 画出来
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_arcto)


---


## 浏览器支持

表格中的数字表示支持该方法的第一个浏览器版本号。


| 方法 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| arcTo() | Yes | 9.0 | Yes | Yes | No |


---


## 定义和用法


arcTo() 方法在画布上创建介于两个切线之间的弧/曲线。


![](https://www.runoob.com/wp-content/uploads/2013/11/img_canvas_arcto.png)


提示：**请使用 [stroke()](https://www.runoob.com/canvas-stroke.html) 方法在画布上绘制确切的弧。


| JavaScript 语法： | context.arcTo(x1,y1,x2,y2,r); |
| --- | --- |


## 参数值


| 参数 | 描述 |
| --- | --- |
| x1 | 两切线交点的横坐标。 |
| y1 | 两切线交点的纵坐标。 |
| x2 | 第二条切线上一点的横坐标。 |
| y2 | 第二条切线上一点的纵坐标。 |
| r | 弧的半径。 |


其中第一条线上的任意一点的横纵坐标为上一次点的位置，此示例中为 **100,20**。由 **(x1,y1),(x2,y2),(100,20)** 三点可确定两条直线的位置再由半径确定弧的位置。

**
---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas arc() 方法](https://www.runoob.com/canvas-arc.html)
			[HTML canvas isPointInPath() 方法](https://www.runoob.com/canvas-ispointinpath.html) **













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