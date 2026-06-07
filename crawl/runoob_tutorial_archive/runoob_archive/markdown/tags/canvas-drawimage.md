# HTML canvas drawImage() 方法

- Source: https://www.runoob.com/tags/canvas-drawimage.html

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)


## 要使用的图片：


![The Scream](https://www.runoob.com/wp-content/uploads/2013/11/img_the_scream.jpg)


## 实例


向画布上面绘制图片：


您的浏览器不支持 HTML5 canvas 标签。


JavaScript：


```
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
var img=document.getElementById("scream");
img.onload = function(){
    ctx.drawImage(img,10,10);
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_drawimage)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


Internet Explorer 9、Firefox、Opera、Chrome 和 Safari 支持 drawImage() 方法。


注意：**Internet Explorer 8 及之前的版本不支持  元素。


---


## 定义和用法


drawImage() 方法在画布上绘制图像、画布或视频。


drawImage() 方法也能够绘制图像的某些部分，以及/或者增加或减少图像的尺寸。


## JavaScript 语法


在画布上定位图像：


| JavaScript 语法： | context.drawImage(img,x,y); |
| --- | --- |


在画布上定位图像，并规定图像的宽度和高度：


| JavaScript 语法： | context.drawImage(img,x,y,width,height); |
| --- | --- |


剪切图像，并在画布上定位被剪切的部分：


| JavaScript 语法： | context.drawImage(img,sx,sy,swidth,sheight,x,y,width,height); |
| --- | --- |


## 参数值


| 参数 | 描述 |  |  |
| --- | --- | --- | --- |
| img | 规定要使用的图像、画布或视频。 |  |  |
| sx | 可选。开始剪切的 x 坐标位置。 |  |  |
| sy | 可选。开始剪切的 y 坐标位置。 | swidth | 可选。被剪切图像的宽度。 |
| sheight | 可选。被剪切图像的高度。 |  |  |
| x | 在画布上放置图像的 x 坐标位置。 |  |  |
| y | 在画布上放置图像的 y 坐标位置。 |  |  |
| width | 可选。要使用的图像的宽度（伸展或缩小图像）。 |  |  |
| height | 可选。要使用的图像的高度（伸展或缩小图像）。 |  |  |

**
---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


## 实例


在画布上对图像进行定位，然后规定图像的宽度和高度：


您的浏览器不支持 HTML5 canvas 标签。


JavaScript：


```
var c=document.getElementById("myCanvas");var
ctx=c.getContext("2d");
var img=document.getElementById("scream");
img.onload = function(){
    ctx.drawImage(img,10,10,150,180);}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_drawimage2)


## 实例


剪切图片，并在画布上对被剪切的部分进行定位：


您的浏览器不支持 HTML5 canvas 标签。


JavaScript：


```
var c=document.getElementById("myCanvas");var
   ctx=c.getContext("2d");var
   img=document.getElementById("scream");
   ctx.drawImage(img,90,130,50,60,10,10,50,60);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_drawimage3)


## 实例


要使用的视频（请按下播放键以开始演示）：







画布：


你的浏览器不支持 canvas 标签


JavaScript（每 20 毫秒，代码就会绘制视频的当前帧）：


```
var v=document.getElementById("video1");
var c=document.getElementById("myCanvas");
ctx=c.getContext('2d');
v.addEventListener('play',function() {var i=window.setInterval(function()
{ctx.drawImage(v,5,5,260,125)},20);},false);
v.addEventListener('pause',function() {window.clearInterval(i);},false);
v.addEventListener('ended',function() {clearInterval(i);},false);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_canvas_drawimage_video)


---

[![HTML canvas 参考手册](https://www.runoob.com/images/up.gif) HTML canvas 参考手册](https://www.runoob.com/ref-canvas.html)








	  AI 思考中...





			** [HTML canvas measureText() 方法](https://www.runoob.com/canvas-measuretext.html)
			[HTML canvas ImageData width 属性](https://www.runoob.com/canvas-imagedata-width.html) **













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