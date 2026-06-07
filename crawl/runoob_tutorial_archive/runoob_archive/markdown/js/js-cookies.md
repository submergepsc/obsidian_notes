# JavaScript Cookie

- Source: https://www.runoob.com/js/js-cookies.html

---


Cookie 用于存储 web 页面的用户信息。


---


## 什么是 Cookie？


Cookie 是一些数据, 存储于你电脑上的文本文件中。


当 web 服务器向浏览器发送 web 页面时，在连接关闭后，服务端不会记录用户的信息。


Cookie 的作用就是用于解决 "如何记录客户端的用户信息":


- 当用户访问 web 页面时，他的名字可以记录在 cookie 中。
- 在用户下一次访问该页面时，可以在 cookie 中读取用户访问记录。


Cookie 以名/值对形式存储，如下所示:


username=John Doe


当浏览器从服务器上请求 web 页面时， 属于该页面的 cookie 会被添加到该请求中。服务端通过这种方式来获取用户的信息。


---


## 使用 JavaScript 创建Cookie


JavaScript 可以使用 **document.cookie** 属性来创建 、读取、及删除 cookie。


JavaScript 中，创建 cookie 如下所示：


document.cookie="username=John Doe";


您还可以为 cookie 添加一个过期时间（以 UTC 或 GMT 时间）。默认情况下，cookie 在浏览器关闭时删除：


document.cookie="username=John Doe; expires=Thu, 18 Dec 2043 12:00:00 GMT";


您可以使用 path 参数告诉浏览器 cookie 的路径。默认情况下，cookie 属于当前页面。


document.cookie="username=John Doe; expires=Thu, 18 Dec 2043 12:00:00 GMT; path=/";


---


## 使用 JavaScript 读取 Cookie


在 JavaScript 中, 可以使用以下代码来读取 cookie：


var x = document.cookie;

**

|  | document.cookie 将以字符串的方式返回所有的 cookie，类型格式： cookie1=value; cookie2=value; cookie3=value; |
| --- | --- |


---


## 使用 JavaScript 修改 Cookie


在 JavaScript 中，修改 cookie 类似于创建 cookie，如下所示：


document.cookie="username=John Smith; expires=Thu, 18 Dec 2043 12:00:00 GMT; path=/";


旧的 cookie 将被覆盖。


---


## 使用 JavaScript 删除 Cookie


删除 cookie 非常简单。您只需要设置 expires 参数为以前的时间即可，如下所示，设置为 Thu, 01 Jan 1970 00:00:00 GMT:


document.cookie = "username=; expires=Thu, 01
Jan 1970 00:00:00 GMT";


注意，当您删除时不必指定 cookie 的值。


---


## Cookie 字符串


document.cookie 属性看起来像一个普通的文本字符串，其实它不是。


即使您在 document.cookie 中写入一个完整的 cookie 字符串, 当您重新读取该 cookie 信息时，cookie 信息是以名/值对的形式展示的。


如果您设置了新的 cookie，旧的 cookie 不会被覆盖。 新 cookie 将添加到 document.cookie 中，所以如果您重新读取document.cookie，您将获得如下所示的数据：


cookie1=value; cookie2=value;


显示所有 Cookie 创建 Cookie 1 创建 Cookie 2 删除 Cookie 1 删除 Cookie 2


如果您需要查找一个指定 cookie 值，您必须创建一个JavaScript 函数在 cookie 字符串中查找 cookie 值。


---


## JavaScript Cookie 实例


在以下实例中，我们将创建 cookie 来存储访问者名称。


首先，访问者访问 web 页面, 他将被要求填写自己的名字。该名字会存储在 cookie 中。


访问者下一次访问页面时，他会看到一个欢迎的消息。


在这个实例中我们会创建 3 个 JavaScript 函数:


- 设置 cookie 值的函数
- 获取 cookie 值的函数
- 检测 cookie 值的函数


---


## 设置 cookie 值的函数


首先，我们创建一个函数用于存储访问者的名字：


```javascript
function setCookie(cname,cvalue,exdays)
{
  var d = new Date();
  d.setTime(d.getTime()+(exdays*24*60*60*1000));
  var expires = "expires="+d.toGMTString();
  document.cookie = cname + "=" + cvalue + "; " + expires;
}
```


函数解析：**


以上的函数参数中，cookie 的名称为 cname，cookie 的值为 cvalue，并设置了 cookie 的过期时间 expires。


该函数设置了 cookie 名、cookie 值、cookie过期时间。


---


## 获取 cookie 值的函数


然后，我们创建一个函数用于返回指定 cookie 的值：


```javascript
function getCookie(cname)
{
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++)
  {
    var c = ca[i].trim();
    if (c.indexOf(name)==0) return c.substring(name.length,c.length);
  }
  return "";
}
```


**函数解析：**


cookie 名的参数为 cname。


创建一个文本变量用于检索指定 cookie :cname + "="。


使用分号来分割 document.cookie 字符串，并将分割后的字符串数组赋值给 ca (ca = document.cookie.split(';'))。


循环 ca 数组 (i=0;i







	  AI 思考中...





			** [JavaScript 计时事件](https://www.runoob.com/js-timing.html)
			[JavaScript 库](https://www.runoob.com/js-libraries.html) **













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