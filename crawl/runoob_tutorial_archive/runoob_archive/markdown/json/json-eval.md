# JSON 使用

- Source: https://www.runoob.com/json/json-eval.html

---


## 把 JSON 文本转换为 JavaScript 对象


JSON 最常见的用法之一，是从 web 服务器上读取 JSON 数据（作为文件或作为 HttpRequest），将 JSON 数据转换为 JavaScript 对象，然后在网页中使用该数据。


为了更简单地为您讲解，我们使用字符串作为输入进行演示（而不是文件）。


---


## JSON 实例 - 来自字符串的对象


创建包含 JSON 语法的 JavaScript 字符串：


```json
var txt = '{ "sites" : [' +
'{ "name":"菜鸟教程" , "url":"www.runoob.com" },' +
'{ "name":"google" , "url":"www.google.com" },' +
'{ "name":"微博" , "url":"www.weibo.com" } ]}';
```


由于 JSON 语法是 JavaScript 语法的子集，JavaScript 函数 eval() 可用于将 JSON 文本转换为 JavaScript 对象。


eval() 函数使用的是 JavaScript 编译器，可解析 JSON 文本，然后生成 JavaScript 对象。必须把文本包围在括号中，这样才能避免语法错误：


var obj = eval ("(" + txt + ")");


在网页中使用 JavaScript 对象：


## 实例


```json
var txt = '{ "sites" : [' +
'{ "name":"菜鸟教程" , "url":"www.runoob.com" },' +
'{ "name":"google" , "url":"www.google.com" },' +
'{ "name":"微博" , "url":"www.weibo.com" } ]}';

var obj = eval ("(" + txt + ")");

document.getElementById("name").innerHTML=obj.sites[0].name
document.getElementById("url").innerHTML=obj.sites[0].url
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_eval)


---


## JSON 解析器


![lamp](https://www.runoob.com/images/lamp2.gif) eval() 函数可编译并执行任何 JavaScript 代码。这隐藏了一个潜在的安全问题。


使用 JSON 解析器将 JSON 转换为 JavaScript 对象是更安全的做法。JSON 解析器只能识别 JSON 文本，而不会编译脚本。


在浏览器中，这提供了原生的 JSON 支持，而且 JSON 解析器的速度更快。


较新的浏览器和最新的 ECMAScript (JavaScript) 标准中均包含了原生的对 JSON 的支持。


| Web 浏览器支持 | Web 软件支持 |
| --- | --- |
| Firefox (Mozilla) 3.5 Internet Explorer 8 Chrome Opera 10 Safari 4 | jQuery Yahoo UI Prototype Dojo ECMAScript 1.5 |


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_parse)


对于较老的浏览器，可使用 JavaScript 库： [https://github.com/douglascrockford/JSON-js](https://github.com/douglascrockford/JSON-js)


JSON 格式最初是 [originally specified by Douglas Crockford](http://developer.yahoo.com/yui/theater/video.php?v=crockford-json)








	  AI 思考中...





			** [JSON 教程](https://www.runoob.com/json-tutorial.html)
			[JSON 语法](https://www.runoob.com/json-syntax.html) **













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