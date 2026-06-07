# JavaScript 调试

- Source: https://www.runoob.com/js/js-debugging.html

---


在编写 JavaScript 时，如果没有调试工具将是一件很痛苦的事情。


---


## JavaScript 调试


没有调试工具是很难去编写 JavaScript 程序的。


你的代码可能包含语法错误，逻辑错误，如果没有调试工具，这些错误比较难于发现。


通常，如果 JavaScript 出现错误，是不会有提示信息，这样你就无法找到代码错误的位置。


|  | 通常，你在编写一个新的 JavaScript 代码过程中都会发生错误。 |
| --- | --- |


---


## JavaScript 调试工具


在程序代码中寻找错误叫做代码调试。


调试很难，但幸运的是，很多浏览器都内置了调试工具。


内置的调试工具可以开启或关闭，严重的错误信息会发送给用户。


有了调试工具，我们就可以设置断点 (代码停止执行的位置), 且可以在代码执行时检测变量。


浏览器启用调试工具一般是按下 F12 键，并在调试菜单中选择 "Console" 。**


---


## console.log() 方法


如果浏览器支持调试，你可以使用 console.log() 方法在调试窗口上打印 JavaScript 值：


## 实例


```javascript
a = 5;
b = 6;
c = a + b;
console.log(c);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_console)


---


## 设置断点


在调试窗口中，你可以设置 JavaScript 代码的断点。


在每个断点上，都会停止执行 JavaScript 代码，以便于我们检查 JavaScript 变量的值。


在检查完毕后，可以重新执行代码（如播放按钮）。


---


## debugger 关键字


debugger** 关键字用于停止执行 JavaScript，并调用调试函数。


这个关键字与在调试工具中设置断点的效果是一样的。


如果没有调试可用，debugger 语句将无法工作。


开启 debugger ，代码在第三行前停止执行。


## 实例


```javascript
var x = 15 * 5;
debugger;
document.getElementbyId("demo").innerHTML = x;
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_debugger)


---


## 主要浏览器的调试工具


通常，浏览器启用调试工具一般是按下 F12 键，并在调试菜单中选择 "Console" 。


各浏览器的步骤如下:


## Chrome 浏览器


- 打开浏览器。
- 在菜单中选择 **"更多工具"**。
- 在 **"更多工具"** 中选择 **"开发者工具"**。
- 最后，选择 Console。


![](https://www.runoob.com/wp-content/uploads/2014/10/chrome1.png)


或者你可以右击鼠标选择 "检查"**，如下图：


![](https://www.runoob.com/wp-content/uploads/2014/10/chrome2.png)


## Firefox 浏览器


- 打开浏览器。
- 右击鼠标，选择 **"查看元素"**。


![](https://www.runoob.com/wp-content/uploads/2014/10/firebug.png)


## Safari


- 打开浏览器。
- 右击鼠标，选择检查元素。
- 在底部弹出的窗口中选择"控制台"。


![](https://www.runoob.com/wp-content/uploads/2014/10/safari.png)


## Internet Explorer 浏览器。


- 打开浏览器。
- 在菜单中选择工具。
- 在工具中选择开发者工具。
- 最后，选择 Console。


![](https://www.runoob.com/wp-content/uploads/2014/10/6fff3e1agw1fbmoikj240j208b09iwf4.jpg)


## Opera


- 打开浏览器。
- 点击左上角，选择**"开发者工具"**,选择**"WEB检查器"**。


![](https://www.runoob.com/wp-content/uploads/2014/10/opera1.png)


更简单的方式是：右击鼠标，选择**"查看元素"**


![](https://www.runoob.com/wp-content/uploads/2014/10/opera2.png)








	  AI 思考中...





			** [JavaScript 语法](https://www.runoob.com/js-syntax.html)
			[JavaScript 函数定义](https://www.runoob.com/js-function-definition.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

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