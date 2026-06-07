# HTML canvas setTransform() 方法

- Source: https://www.runoob.com/tags/canvas-settransform.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


绘制一个矩形，通过 setTransform() 重置并创建新的变换矩阵，再次绘制矩形，重置并创建新的变换矩阵，然后再次绘制矩形。请注意，每当您调用 setTransform() 时，它都会重置前一个变换矩阵然后构建新的矩阵，因此在下面的例子中，不会显示红色矩形，因为它在蓝色矩形下面：


YourbrowserdoesnotsupporttheHTML5canvastag.



JavaScript：


```
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.fillStyle="yellow";
ctx.fillRect(0,0,250,100)
ctx.setTransform(1,0.5,-0.5,1,30,10);
ctx.fillStyle="red";
ctx.fillRect(0,0,250,100);
ctx.setTransform(1,0.5,-0.5,1,30,10);
ctx.fillStyle="blue";
ctx.fillRect(0,0,250,100);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_setTransform)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 setTransform() 方法。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


画布上的每个对象都拥有一个当前的变换矩阵。


setTransform() 方法把当前的变换矩阵重置为单位矩阵，然后以相同的参数运行 [transform()](https://www.runoob.com/canvas-transform.html)。


换句话说，setTransform() 允许您缩放、旋转、移动并倾斜当前的环境。


**注意：**该变换只会影响 setTransform() 方法调用之后的绘图。


| JavaScript 语法： | context.setTransform(a,b,c,d,e,f); |
| --- | --- |


## 参数值


| 参数 | 描述 |
| --- | --- |
| a | 水平缩放绘图。 |
| b | 水平倾斜绘图。 |
| c | 垂直倾斜绘图。 |
| d | 垂直缩放绘图。 |
| e | 水平移动绘图。 |
| f | 垂直移动绘图。 |

**
---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas transform() 方法](https://www.runoob.com/canvas-transform.html)
			[HTML canvas font 属性](https://www.runoob.com/canvas-font.html) **













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