# AJAX - 创建 XMLHttpRequest 对象

- Source: https://www.runoob.com/ajax/ajax-xmlhttprequest-create.html

---


XMLHttpRequest 是 AJAX 的基础。


---


## XMLHttpRequest 对象


所有现代浏览器均支持 XMLHttpRequest 对象（IE5 和 IE6 使用 ActiveXObject）。


XMLHttpRequest 用于在后台与服务器交换数据。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。


---


## 创建 XMLHttpRequest 对象


所有现代浏览器（IE7+、Edge、Firefox、Chrome、Safari 以及 Opera）均内建 XMLHttpRequest 对象。


创建 XMLHttpRequest 对象的语法：


```
var xhr = new XMLHttpRequest();
```


老版本的 Internet Explorer （IE5 和 IE6）使用 ActiveX 对象：


```
var xhr = new ActiveXObject("Microsoft.XMLHTTP");
```


为了应对所有的现代浏览器，包括 IE5 和 IE6（**现在应该很少人使用了**），请检查浏览器是否支持 XMLHttpRequest 对象。如果支持，则创建 XMLHttpRequest 对象。如果不支持，则创建 ActiveXObject ：


## 实例


```javascript
var xmlhttp;
if (window.XMLHttpRequest) {
    //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
} else {
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryajax_first)


创建一个 XMLHttpRequest 对象的示例：


## 实例


```javascript
// 创建 XMLHttpRequest 对象
var xhr = new XMLHttpRequest();

// 配置请求
xhr.open('GET', 'https://api.example.com/data', true);

// 设置请求头（如果需要的话）
// xhr.setRequestHeader('Content-Type', 'application/json');

// 定义回调函数
xhr.onload = function () {
    if (xhr.status >= 200 && xhr.status < 300) {
        // 请求成功，处理响应
        console.log('Response:', xhr.responseText);
    } else {
        // 处理错误
        console.error('Error:', xhr.statusText);
    }
};

// 处理网络错误
xhr.onerror = function () {
    console.error('Request failed');
};

// 发送请求
xhr.send();
```


在下一章中，您将学习发送服务器请求的知识。








	  AI 思考中...





			** [AJAX – 向服务器发送](https://www.runoob.com/ajax-xmlhttprequest-send.html)
			[AJAX 简介](https://www.runoob.com/ajax-intro.html) **













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