# HTML canvas globalCompositeOperation 属性

- Source: https://www.runoob.com/tags/canvas-globalcompositeoperation.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 实例


使用不同的 globalCompositeOperation 值绘制矩形。红色矩形是*目标图像*，蓝色矩形是*源图像*：


source-over
destination-over


YourbrowserdoesnotsupporttheHTML5canvastag.


JavaScript：


```
var c=document.getElementById("myCanvas");
	var ctx=c.getContext("2d");
	ctx.fillStyle="red";
	ctx.fillRect(20,20,75,50);
	ctx.globalCompositeOperation="source-over";
	ctx.fillStyle="blue";
	ctx.fillRect(50,50,75,50);
	ctx.fillStyle="red";
	ctx.fillRect(150,20,75,50);
	ctx.globalCompositeOperation="destination-over";
	ctx.fillStyle="blue";
	ctx.fillRect(180,50,75,50);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_globalcompop)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 globalCompositeOperation 属性。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


globalCompositeOperation 属性设置或返回如何将一个源（新的）图像绘制到目标（已有的）的图像上。


*源图像 = *您打算放置到画布上的绘图。


*目标图像 = *您已经放置在画布上的绘图。


| 默认值： | source-over |
| --- | --- |
| JavaScript 语法： | context.globalCompositeOperation="source-in"; |


## 属性值


| 值 | 描述 |
| --- | --- |
| source-over | 默认。在目标图像上显示源图像。 |
| source-atop | 在目标图像顶部显示源图像。源图像位于目标图像之外的部分是不可见的。 |
| source-in | 在目标图像中显示源图像。只有目标图像之内的源图像部分会显示，目标图像是透明的。 |
| source-out | 在目标图像之外显示源图像。只有目标图像之外的源图像部分会显示，目标图像是透明的。 |
| destination-over | 在源图像上显示目标图像。 |
| destination-atop | 在源图像顶部显示目标图像。目标图像位于源图像之外的部分是不可见的。 |
| destination-in | 在源图像中显示目标图像。只有源图像之内的目标图像部分会被显示，源图像是透明的。 |
| destination-out | 在源图像之外显示目标图像。只有源图像之外的目标图像部分会被显示，源图像是透明的。 |
| lighter | 显示源图像 + 目标图像。 |
| copy | 显示源图像。忽略目标图像。 |
| xor | 使用异或操作对源图像与目标图像进行组合。 |

**
## 实例


所有 globalCompositeOperation 属性值：


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_globalcompop_all)


---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)







	  AI 思考中...





			** [HTML canvas globalAlpha 属性](https://www.runoob.com/canvas-globalalpha.html)
			[HTML 音频/视频 DOM addTextTrack() 方法](https://www.runoob.com/av-met-addtexttrack.html) **













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