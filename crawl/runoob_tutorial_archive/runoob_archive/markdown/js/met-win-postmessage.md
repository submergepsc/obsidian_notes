# Window postMessage() 方法

- Source: https://www.runoob.com/js/met-win-postmessage.html

[![Window 对象参考手册](https://www.runoob.com/images/up.gif) Window 对象](https://www.runoob.com/obj-window.html)

---


## 定义和用法


postMessage() 方法用于安全地实现跨源通信。


## 语法


```
otherWindow.postMessage(message, targetOrigin, [transfer]);
```


**
| 参数 | 说明 |
| --- | --- |
| otherWindow | 其他窗口的一个引用，比如 iframe 的 contentWindow 属性、执行 window.open 返回的窗口对象、或者是命名过或数值索引的 window.frames。 |
| message | 将要发送到其他 window的数据。 |
| targetOrigin | 指定哪些窗口能接收到消息事件，其值可以是 *（表示无限制）或者一个 URI。 |
| transfer | 可选，是一串和 message 同时传递的 Transferable 对象。这些对象的所有权将被转移给消息的接收方，而发送一方将不再保有所有权。 |


---


## 浏览器支持


|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Chrome 1 | Edge 12 | Firefox 8 | Safari 4 | Opera 9.5 |


---


## 实例


## 发送程序


```javascript
<div>
    <input id="text" type="text" value="Runoob" />
    <button id="sendMessage" >发送消息</button>
</div>
<iframe id="receiver" src="https://c.runoob.com/runoobtest/postMessage_receiver.html" width="300" height="360">
    <p>你的浏览器不支持 iframe。</p>
</iframe>
<script>
window.onload = function() {
    var receiver = document.getElementById('receiver').contentWindow;
    var btn = document.getElementById('sendMessage');
    btn.addEventListener('click', function (e) {
        e.preventDefault();
        var val = document.getElementById('text').value;
        receiver.postMessage("Hello "+val+"！", "https://c.runoob.com");
    });
}
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_postMessage)


## 接收程序：https://c.runoob.com/runoobtest/postMessage_receiver.html


接收程序有一个事件监听器，监听 "message" 事件，同时我们要验证消息来源地址，以确保是个可信的发送地址。


```javascript
<div id="recMessage">
Hello World!
</div>
<script>
window.onload = function() {
    var messageEle = document.getElementById('recMessage');
    window.addEventListener('message', function (e) {  // 监听 message 事件
        alert(e.origin);
        if (e.origin !== "https://www.runoob.com") {  // 验证消息来源地址
            return;
        }
        messageEle.innerHTML = "从"+ e.origin +"收到消息： " + e.data;
    });
}
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_postMessage)


- **e.source** – 消息源，消息的发送窗口/iframe。
- **e.origin** – 消息源的 URI(可能包含协议、域名和端口)，用来验证数据源。
- **e.data** – 发送过来的数据。


---

[![Window 对象 参考手册](https://www.runoob.com/images/up.gif) Window 对象](https://www.runoob.com/obj-window.html)







	  AI 思考中...





			** [Chrome 浏览器中执行 JavaScript](https://www.runoob.com/js-chrome.html)
			[JavaScript 类(class)](https://www.runoob.com/js-class-intro.html) **













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