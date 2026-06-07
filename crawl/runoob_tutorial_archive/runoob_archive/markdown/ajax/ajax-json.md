# AJAX JSON 实例

- Source: https://www.runoob.com/ajax/ajax-json.html

---


AJAX 可用来与 JSON 文件进行交互式通信。


---


## AJAX JSON 实例


下面的例子将演示网页如何使用 AJAX 来读取来自 JSON 文件的信息：


## 实例

**

获取课程数据


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryajax_json)


---


## 实例解析 - loadXMLDoc() 函数


当用户点击上面的"获取课程数据"**这个按钮，就会执行 loadXMLDoc() 函数。


loadXMLDoc() 函数创建 XMLHttpRequest 对象，添加当服务器响应就绪时执行的函数，并将请求发送到服务器。


当服务器响应就绪时，我们就使用 [JSON.parse()](https://www.runoob.com/../json/json-parse.html) 方法将数据转换为 JavaScript 对象。：


## 异步加载 JSON 文档


```javascript
function loadXMLDoc()
{
  var xmlhttp;
  if (window.XMLHttpRequest)
  {
    // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
  }
  else
  {
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      var myArr = JSON.parse(this.responseText);
      myFunction(myArr)
    }
  }
  xmlhttp.open("GET","/try/ajax/json_ajax.json",true);
  xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xmlhttp.send();
}
function myFunction(arr) {
  var out = "";
  var i;
  for(i = 0; i < arr.length; i++) {
    out += '<a href="' + arr[i].url + '">' +
    arr[i].title + '</a><br>';
  }
 document.getElementById("myDiv").innerHTML=out;
}
```


**
---


## AJAX 服务器页面


上面这个例子中使用的服务器页面实际上是一个名为 "[json_ajax.json](https://www.runoob.com/try/ajax/json_ajax.json)" JSON 文件。


JSON 数据如下：


## json_ajax.json 文件：


```javascript
[
  {
    "title": "JavaScript 教程",
    "url": "https://www.runoob.com/js/"
  },
  {
    "title": "HTML 教程",
    "url": "https://www.runoob.com/html/"
  },
  {
    "title": "CSS 教程",
    "url": "https://www.runoob.com/css/"
  }
]
```


发送 JSON 数据：


```
xmlhttp.send(JSON.stringify({ "email": "[email protected]", "response": { "name": "runoob" } }));
```









	  AI 思考中...





			** [AJAX 实例](https://www.runoob.com/ajax-examples.html)
			[Fetch API](https://www.runoob.com/fetch-api.html) **













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