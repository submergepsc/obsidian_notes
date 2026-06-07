# JSON.stringify()

- Source: https://www.runoob.com/json/json-stringify.html

JSON 通常用于与服务端交换数据。

在向服务器发送数据时一般是字符串。

我们可以使用 JSON.stringify() 方法将 JavaScript 对象转换为字符串。


### 语法


```
JSON.stringify(value[, replacer[, space]])
```


**参数说明：**


- **value:**必需， 要转换的 JavaScript 值（通常为对象或数组）。
- **replacer:** 可选。用于转换结果的函数或数组。 如果 replacer 为函数，则 JSON.stringify 将调用该函数，并传入每个成员的键和值。使用返回值而不是原始值。如果此函数返回 undefined，则排除成员。根对象的键是一个空字符串：""。 如果 replacer 是一个数组，则仅转换该数组中具有键值的成员。成员的转换顺序与键在数组中的顺序一样。当 value 参数也为数组时，将忽略 replacer 数组。
- **space:** 可选，文本添加缩进、空格和换行符，如果 space 是一个数字，则返回值文本在每个级别缩进指定数目的空格，如果 space 大于 10，则文本缩进 10 个空格。space 也可以使用非数字，如：\t。


---


## JavaScript 对象转换


例如我们向服务器发送以下数据：


```json
var obj = { "name":"runoob", "alexa":10000, "site":"www.runoob.com"};
```


我们使用 JSON.stringify() 方法处理以上数据，将其转换为字符串：


```json
var myJSON = JSON.stringify(obj);
```


myJSON 为字符串。


我们可以将 myJSON 发送到服务器：


## 实例


```json
var obj = { "name":"runoob", "alexa":10000, "site":"www.runoob.com"};
var myJSON = JSON.stringify(obj);
document.getElementById("demo").innerHTML = myJSON;
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_stringify1)


---


## JavaScript 数组转换


我们也可以将 JavaScript 数组转换为 JSON 字符串：


## 实例


```json
var arr = [ "Google", "Runoob", "Taobao", "Facebook" ];
var myJSON = JSON.stringify(arr);
```


myJSON 为字符串。


我们可以将 myJSON 发送到服务器：


## 实例


```json
var arr = [ "Google", "Runoob", "Taobao", "Facebook" ];
var myJSON = JSON.stringify(arr);
document.getElementById("demo").innerHTML = myJSON;
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_stringify2)


---


## 异常


### 解析数据


JSON 不能存储 Date 对象。


JSON.stringify() 会将所有日期转换为字符串。


## 实例


```json
var obj = { "name":"Runoob", "initDate":new Date(), "site":"www.runoob.com"};
var myJSON = JSON.stringify(obj);
document.getElementById("demo").innerHTML = myJSON;
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_stringify_date)


之后你可以再将字符串转换为 Date 对象。


---


## 解析函数


JSON 不允许包含函数，JSON.stringify() 会删除 JavaScript 对象的函数，包括 key 和 value。


## 实例


```json
var obj = { "name":"Runoob", "alexa":function () {return 10000;}, "site":"www.runoob.com"};
var myJSON = JSON.stringify(obj);

document.getElementById("demo").innerHTML = myJSON;
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_stringify_function)


我们可以在执行 JSON.stringify() 函数前将函数转换为字符串来避免以上问题的发生：


## 实例


```json
var obj = { "name":"Runoob", "alexa":function () {return 10000;}, "site":"www.runoob.com"};
obj.alexa = obj.alexa.toString();
var myJSON = JSON.stringify(obj);

document.getElementById("demo").innerHTML = myJSON;
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_stringify_function_tostring)


不建议在 JSON 中使用函数。


---


## 浏览器支持


主流浏览器都支持 JSON.stringify() 函数：


- Firefox 3.5
- Internet Explorer 8
- Chrome
- Opera 10
- Safari 4








	  AI 思考中...





			** [JSON.parse()](https://www.runoob.com/json-parse.html)
			[JSON vs XML](https://www.runoob.com/json-vs-xml.html) **













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