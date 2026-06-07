# JavaScript HTML DOM - 改变CSS

- Source: https://www.runoob.com/js/js-htmldom-css.html

---


HTML DOM 允许 JavaScript 改变 HTML 元素的样式。


---


## 改变 HTML 样式


如需改变 HTML 元素的样式，请使用这个语法：


document.getElementById(*id*).style.*property*=*新样式*


下面的例子会改变  元素的样式：


## 实例


```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<p id="p1">Hello World!</p>
<p id="p2">Hello World!</p>
<script>
document.getElementById("p2").style.color="blue";
document.getElementById("p2").style.fontFamily="Arial";
document.getElementById("p2").style.fontSize="larger";
</script>
<p>以上段落通过脚本修改。</p>

</body>
</html>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_change_style)

---


## 使用事件


HTML DOM 允许我们通过触发事件来执行代码。


比如以下事件：


- 元素被点击。
- 页面加载完成。
- 输入框被修改。
- ……


在接下来的章节，你会学到更多关于事件的知识。


本例改变了 id="id1" 的 HTML 元素的样式，当用户点击按钮时：


## 实例


```javascript
<!DOCTYPE html><html><body><h1 id="id1">我的标题 1</h1>
	<button type="button" onclick="document.getElementById('id1').style.color='red'">
	点我!</button></body></html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trydhtml_dom_color2)


---


## 更多实例


[Visibility](https://www.runoob.com/try/try.php?filename=trydhtml_visibility) 如何使元素不可见。您希望元素显示或消失吗？









	  AI 思考中...





			** [JavaScript HTML DOM 改变 HTML 内容](https://www.runoob.com/js-htmldom-html.html)
			[JavaScript HTML DOM 事件](https://www.runoob.com/js-htmldom-events.html) **













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