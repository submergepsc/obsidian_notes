# AJAX - 向服务器发送请求

- Source: https://www.runoob.com/ajax/ajax-xmlhttprequest-send.html

---


XMLHttpRequest 对象用于和服务器交换数据。


---


## 向服务器发送请求


如需将请求发送到服务器，我们使用 **XMLHttpRequest** 对象的 **open()** 和 **send()** 方法：


```
xmlhttp.open("GET","ajax_info.txt",true);
xmlhttp.send();
```


**
| 方法 | 描述 |
| --- | --- |
| open(method,url,async) | 规定请求的类型、URL 以及是否异步处理请求。 method：请求的类型；GET 或 POST url：文件在服务器上的位置 async：true（异步）或 false（同步） |
| send(string) | 将请求发送到服务器。 string：仅用于 POST 请求 |


---


## GET 还是 POST？


与 POST 相比，GET 更简单也更快，并且在大部分情况下都能用。


然而，在以下情况中，请使用 POST 请求：


- 不愿使用缓存文件（更新服务器上的文件或数据库）
- 向服务器发送大量数据（POST 没有数据量限制）
- 发送包含未知字符的用户输入时，POST 比 GET 更稳定也更可靠


![](https://www.runoob.com/wp-content/uploads/2013/09/ytxdmm71yvt3zokkrpn4-scaled.jpeg)


---


## GET 请求


一个简单的 GET 请求：


## 实例


```javascript
xmlhttp.open("GET","/try/ajax/demo_get.php",true);
xmlhttp.send();
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryajax_get)


在上面的例子中，您可能得到的是缓存的结果。


为了避免这种情况，请向 URL 添加一个唯一的 ID：


## 实例


```javascript
xmlhttp.open("GET","/try/ajax/demo_get.php?t=" + Math.random(),true);
xmlhttp.send();
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryajax_get_unique)


如果您希望通过 GET 方法发送信息，请向 URL 添加信息：


## 实例


```javascript
xmlhttp.open("GET","/try/ajax/demo_get2.php?fname=Henry&lname=Ford",true);
xmlhttp.send();
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryajax_get2)


---


## POST 请求


一个简单 POST 请求：


## 实例


```javascript
xmlhttp.open("POST","/try/ajax/demo_post.php",true);
xmlhttp.send();
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryajax_post)


如果需要像 HTML 表单那样 POST 数据，请使用 setRequestHeader() 来添加 HTTP 头。然后在 send() 方法中规定您希望发送的数据：


## 实例


```javascript
xmlhttp.open("POST","/try/ajax/demo_post2.php",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send("fname=Henry&lname=Ford");
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryajax_post2)


| 方法 | 描述 |
| --- | --- |
| setRequestHeader(header,value) | 向请求添加 HTTP 头。 header: 规定头的名称 value: 规定头的值 |


---


## url - 服务器上的文件


open() 方法的 *url* 参数是服务器上文件的地址：


```
xmlhttp.open("GET","ajax_test.html",true);
```


该文件可以是任何类型的文件，比如 .txt 和 .xml，或者服务器脚本文件，比如 .asp 和 .php （在传回响应之前，能够在服务器上执行任务）。


---


## 异步 - True 或 False？


AJAX 指的是异步 JavaScript 和 XML（Asynchronous JavaScript and XML）。


XMLHttpRequest 对象如果要用于 AJAX 的话，其 open() 方法的 async 参数必须设置为 true：


```
xmlhttp.open("GET","ajax_test.html",true);
```


对于 web 开发人员来说，发送异步请求是一个巨大的进步。很多在服务器执行的任务都相当费时。AJAX 出现之前，这可能会引起应用程序挂起或停止。


通过 AJAX，JavaScript 无需等待服务器的响应，而是：


- 在等待服务器响应时执行其他脚本
- 当响应就绪后对响应进行处理


---


## Async=true


当使用 async=true 时，请规定在响应处于 onreadystatechange 事件中的就绪状态时执行的函数：


## 实例


```javascript
xmlhttp.onreadystatechange=function()
{
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
        document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
}
xmlhttp.open("GET","/try/ajax/ajax_info.txt",true);
xmlhttp.send();
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryajax_first)


您将在稍后的章节学习更多有关 onreadystatechange 的内容。


---


## Async = false


如需使用 async=false，请将 open() 方法中的第三个参数改为 false：


```
xmlhttp.open("GET","test1.txt",false);
```


我们不推荐使用 async=false，但是对于一些小型的请求，也是可以的。


请记住，JavaScript 会等到服务器响应就绪才继续执行。如果服务器繁忙或缓慢，应用程序会挂起或停止。


注意：**当您使用 async=false 时，请不要编写 onreadystatechange 函数 - 把代码放到 send() 语句后面即可：


## 实例


```javascript
xmlhttp.open("GET","/try/ajax/ajax_info.txt",false);
xmlhttp.send();
document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryajax_asyncfalse)








	  AI 思考中...





			** [AJAX XMLHttpRequest 服务器响应](https://www.runoob.com/ajax-xmlhttprequest-response.html)
			[AJAX 创建 XMLHttpRequest 对象](https://www.runoob.com/ajax-xmlhttprequest-create.html) **













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