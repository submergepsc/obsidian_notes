# JavaScript 弹窗

- Source: https://www.runoob.com/js/js-popup.html

---


可以在 JavaScript 中创建三种消息框：警告框、确认框、提示框。


---


## 警告框


警告框经常用于确保用户可以得到某些信息。


当警告框出现后，用户需要点击确定按钮才能继续进行操作。


### 语法


	window.alert("*sometext*");

**window.alert()** 方法可以不带上window对象，直接使用**alert()**方法。


## 实例


```javascript
<!DOCTYPE html><html>
<head>
<script>
function myFunction()
{
    alert("你好，我是一个警告框！");
}
</script>
</head>
<body>
<input type="button" onclick="myFunction()" value="显示警告框">
</body>
</html>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_alert)


---


## 确认框


确认框通常用于验证是否接受用户操作。


当确认框弹出时，用户可以点击 "确认" 或者 "取消" 来确定用户操作。


当你点击 "确认", 确认框返回 true， 如果点击 "取消", 确认框返回 false。


### 语法


	window.confirm("*sometext*");

window.confirm()** 方法可以不带上window对象，直接使用**confirm()**方法。


## 实例


```javascript
var r=confirm("按下按钮");
if (r==true)
{
    x="你按下了\"确定\"按钮!";
}
else
{
    x="你按下了\"取消\"按钮!";
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_confirm)


---


## 提示框


提示框经常用于提示用户在进入页面前输入某个值。


当提示框出现后，用户需要输入某个值，然后点击确认或取消按钮才能继续操纵。


如果用户点击确认，那么返回值为输入的值。如果用户点击取消，那么返回值为 null。


### 语法


	window.prompt("*sometext*","*defaultvalue*");

window.prompt()** 方法可以不带上window对象，直接使用**prompt()**方法。


## 实例


```javascript
var person=prompt("请输入你的名字","Harry Potter");
if (person!=null && person!="")
{
    x="你好 " + person + "! 今天感觉如何?";
    document.getElementById("demo").innerHTML=x;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_prompt)


---


## 换行


弹窗使用 反斜杠 + "n"(\n) 来设置换行。


## 实例


```javascript
alert("Hello\nHow are you?");
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_alert2)








	  AI 思考中...





			** [JavaScript Window Navigator](https://www.runoob.com/js-window-navigator.html)
			[JavaScript 计时事件](https://www.runoob.com/js-timing.html) **













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