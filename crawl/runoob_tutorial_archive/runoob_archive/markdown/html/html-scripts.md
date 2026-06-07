# HTML 脚本

- Source: https://www.runoob.com/html/html-scripts.html

---

JavaScript 使 HTML 页面具有更强的动态和交互性。


---

![Examples](https://www.runoob.com/images/tryitimg.gif)
## 在线实例


[插入一段脚本](https://www.runoob.com/try/try.php?filename=tryhtml_script)** 如何将脚本插入 HTML 文档。


[使用 标签](https://www.runoob.com/try/try.php?filename=tryhtml_noscript) 如何应对不支持脚本或禁用脚本的浏览器。


---

## HTML 标签


 标签用于定义客户端脚本，比如 JavaScript。


 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件。


JavaScript 最常用于图片操作、表单验证以及内容动态更新。


下面的脚本会向浏览器输出"Hello World!"：


## 实例


```html
<script>
document.write("Hello World!");
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_script)


![Remark](https://www.runoob.com/images/lamp.gif)Tip:** 学习更多关于Javascript教程，请查看[JavaScript 教程](https://www.runoob.com/../js/js-tutorial.html)!**


---

## HTML 标签


 标签提供无法使用脚本时的替代内容，比方在浏览器禁用脚本时，或浏览器不支持客户端脚本时。


元素可包含普通 HTML 页面的 body 元素中能够找到的所有元素。


只有在浏览器不支持脚本或者禁用脚本时，才会显示  元素中的内容：


## 实例


```html
<script>
document.write("Hello World!")
</script>
<noscript>抱歉，你的浏览器不支持 JavaScript!</noscript>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_noscript)


---


## JavaScript体验(来自本站javascript教程)


JavaScript实例代码:


## JavaScript可以直接在HTML输出:


```html
document.write("<p>这是一个段落。</p>");
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_intro_document_write)


## JavaScript事件响应:


```html
<button type="button" onclick="myFunction()">点我！</button>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_intro_event)


## JavaScript处理 HTML 样式:


```html
document.getElementById("demo").style.color="#ff0000";
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_intro_style)


---

## HTML 脚本标签


| 标签 | 描述 |
| --- | --- |
|  | 定义了客户端脚本 |
|  | 定义了不支持脚本浏览器输出的文本 |








	  AI 思考中...





			** [HTML 颜色值](https://www.runoob.com/html-colorvalues.html)
			[HTML 字符实体](https://www.runoob.com/html-entities.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

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