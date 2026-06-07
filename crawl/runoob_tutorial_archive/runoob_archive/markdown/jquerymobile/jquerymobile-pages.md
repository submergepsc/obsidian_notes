# jQuery Mobile 页面

- Source: https://www.runoob.com/jquerymobile/jquerymobile-pages.html

---


## 开始学习 jQuery Mobile


|  | 尽管jQuery Mobile兼容所有的移动设备，但是并不能完全兼容PC机（由于有限的CSS3支持）。 为了更好的阅读本教程，建议您使用 Google Chrome 浏览器。 |
| --- | --- |

**
## 实例


```javascript
<body><div data-role="page">  <div
  data-role="header">    <h1>欢迎来到我的主页</h1>  </div>
  <div data-role="main" class="ui-content">    <p>我现在是一个移动端开发者!!</p>
  </div>  <div data-role="footer">    <h1>底部文本</h1>  </div></div></body>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_start)


### 实例解析：


- data-role="page" 是在浏览器中显示的页面。
- data-role="header" 是在页面顶部创建的工具条 (通常用于标题或者搜索按钮)
- data-role="main" 定义了页面的内容，比如文本， 图片，表单，按钮等。
- "ui-content" 类用于在页面添加内边距和外边距。
- data-role="footer" 用于创建页面底部工具条。
- 在这些容器中你可以添加任何 HTML 元素 - 段落, 图片, 标题, 列表等。


|  | jQuery Mobile 依赖 HTML5 data-* 属性来支持各种 UI 元素、过渡和页面结构。不支持它们的浏览器将以静默方式弃用它们。 |
| --- | --- |


---


## 在页面中添加 jQuery Mobile


使用 jQuery Mobile, 你可以在单个 HTML 文件中创建多个不同的页面。


你可以使用不同的href属性来区分使用同一个唯一id的页面：


## 实例


```javascript
<div data-role="page" id="pageone">
	  <div data-role="main" class="ui-content">    <a href="#pagetwo">跳转到第二个页面</a>  </div></div><div data-role="page"
	id="pagetwo">  <div
	data-role="main" class="ui-content">    <a href="#pageone">跳转到第一个页面</a>  </div></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_pages)


注意：** 当web应用有大量的内容（文本，图片，脚本等）将会严重影响加载时间。如果你不想使用内页链接可以使用外部文件：


```
<a href="externalfile.html">访问外部文件</a>
```


---


## 页面作为对话框使用


对话框是用于显示页面信息显示或者表单信息的输入。


在链接中添加data-rel="dialog"让用户点击链接时弹出对话框:


## 实例


```javascript
<div data-role="page" id="pageone">  <div
  data-role="main" class="ui-content">    <a href="#pagetwo">跳转到第二个页面</a>
  </div></div><div data-role="page"
  data-dialog="true" id="pagetwo">  <div
  data-role="main" class="ui-content">
  <a href="#pageone">跳转到第一个页面</a>  </div></div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_dialog)








	  AI 思考中...





			** [jQuery Mobile 安装](https://www.runoob.com/jquerymobile-install.html)
			[jQuery Mobile 列表视图](https://www.runoob.com/jquerymobile-list-views.html) **













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