# JavaScript HTML DOM - 改变 HTML

- Source: https://www.runoob.com/js/js-htmldom-html.html

---


HTML DOM 允许 JavaScript 改变 HTML 元素的内容。


---


## 改变 HTML 输出流


JavaScript 能够创建动态的 HTML 内容：


**今天的日期是： **


在 JavaScript 中，document.write() 可用于直接向 HTML 输出流写内容。


## 实例


```javascript
<!DOCTYPE html><html>
<body>
<script>
document.write(Date());
</script>
</body>
</html>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trydhtml_date)


|  | 绝对不要在文档(DOM)加载完成之后使用 document.write()。这会覆盖该文档。 |
| --- | --- |


---


## 改变 HTML 内容


修改 HTML 内容的最简单的方法是使用 innerHTML 属性。


如需改变 HTML 元素的内容，请使用这个语法：


document.getElementById(*id*).innerHTML=*新的 HTML*


本例改变了 元素的内容：


## 实例


```javascript
<html>
<body>
<p id="p1">Hello World!</p>
<script>
document.getElementById("p1").innerHTML="新文本!";
</script>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_change_innerhtml)


本例改变了  元素的内容：


## 实例


```javascript
<!DOCTYPE html><html>
<body>
<h1 id="header">Old Header</h1>
<script>
	var element=document.getElementById("header");element.innerHTML="新标题";
</script>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trydhtml_dom_innertext)


实例讲解：


- 上面的 HTML 文档含有 id="header" 的  元素
- 我们使用 HTML DOM 来获得 id="header" 的元素
- JavaScript 更改此元素的内容 (innerHTML)


---


## 改变 HTML 属性


如需改变 HTML 元素的属性，请使用这个语法：


document.getElementById(*id*).*attribute=新属性值*


本例改变了  元素的 src 属性：


## 实例


```javascript
<!DOCTYPE html><html>
<body>
<img id="image" src="smiley.gif">
<script>
document.getElementById("image").src="landscape.jpg";
</script>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trydhtml_dom_image)


实例讲解：


- 上面的 HTML 文档含有 id="image" 的  元素
- 我们使用 HTML DOM 来获得 id="image" 的元素
- JavaScript 更改此元素的属性（把 "smiley.gif" 改为 "landscape.jpg"）








	  AI 思考中...





			** [JavaScript HTML DOM](https://www.runoob.com/js-htmldom.html)
			[JavaScript HTML DOM 改变 CSS](https://www.runoob.com/js-htmldom-css.html) **













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