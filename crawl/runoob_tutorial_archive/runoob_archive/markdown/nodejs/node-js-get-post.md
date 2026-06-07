# Node.js GET/POST请求

- Source: https://www.runoob.com/nodejs/node-js-get-post.html

在很多场景中，我们的服务器都需要跟用户的浏览器打交道，如表单提交。


表单提交到服务器一般都使用 GET/POST 请求。


本章节我们将为大家介绍 Node.js GET/POST请求。


---


## 获取GET请求内容


由于 GET 请求直接被嵌入在路径中，URL 是完整的请求路径，包括了 **?** 后面的部分，因此你可以手动解析后面的内容作为 GET 请求的参数。

node.js 中 可以使用 URL 构造函数解析请求的 URL。


URL 对象是 Node.js 中用于解析和操作 URL 的一种标准工具。它提供了方便的接口来访问和修改 URL 的各个组成部分，如协议、主机名、路径、查询参数等。


## 实例


```javascript
const http = require('http');
const util = require('util');

http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });

    // 使用 URL 构造函数解析请求的 URL
    const myUrl = new URL(req.url, `http://${req.headers.host}`);

    // 输出 URL 的各个部分
    res.end(util.inspect({
        href: myUrl.href,
        origin: myUrl.origin,
        protocol: myUrl.protocol,
        host: myUrl.host,
        hostname: myUrl.hostname,
        port: myUrl.port,
        pathname: myUrl.pathname,
        search: myUrl.search,
        searchParams: Object.fromEntries(myUrl.searchParams) // 将 searchParams 转为普通对象
    }));
}).listen(3000);

console.log("Server is running at http://localhost:3000");
```


在浏览器中访问 **http://localhost:3000/user?name=菜鸟教程&url;=www.runoob.com** 然后查看返回结果:


![](https://www.runoob.com/wp-content/uploads/2014/06/4A1C02B2-2EB8-4976-9F35-F3760713D495.jpg)


### 获取 URL 的参数


我们可以使用 url.parse 方法来解析 URL 中的参数，代码如下：


## 实例


```javascript
const http = require('http');

http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });

    // 使用 URL 构造函数解析请求 URL
    const myUrl = new URL(req.url, `http://${req.headers.host}`);

    // 获取查询参数
    const name = myUrl.searchParams.get("name");
    const siteUrl = myUrl.searchParams.get("url");

    res.write("网站名：" + (name || "未提供"));
    res.write("\n");
    res.write("网站 URL：" + (siteUrl || "未提供"));
    res.end();

}).listen(3000);

console.log("Server is running at http://localhost:3000");
```


在浏览器中访问 **http://localhost:3000/user?name=菜鸟教程&url;=www.runoob.com** 然后查看返回结果:


![](https://www.runoob.com/wp-content/uploads/2014/06/ADF34B0E-6715-41EE-9A88-4BE067100868.jpg)


### URL 对象

以下是 URL 对象的属性和方法：

| 属性/方法 | 描述 | 示例输出 |
| --- | --- | --- |
| href | 完整的 URL 字符串 | "http://example.com:8080/path?foo=bar#section" |
| origin | URL 的源，包括协议、主机名和端口号（如果存在） | "http://example.com:8080" |
| protocol | URL 的协议部分，后面带有 : | "http:" |
| host | 主机名和端口号 | "example.com:8080" |
| hostname | 主机名，不包含端口号 | "example.com" |
| port | 端口号（如果指定） | "8080" |
| pathname | 路径名部分 | "/path" |
| search | 查询字符串部分，包含开头的 ? | "?foo=bar&hello=world" |
| searchParams | URLSearchParams 对象，用于操作查询参数 | { foo: 'bar', hello: 'world' } |
| hash | 锚点部分，包含 # | "#section" |


| 方法 | 描述 | 示例代码 | 示例输出 |
| --- | --- | --- | --- |
| get(name) | 获取指定名称的查询参数值 | myUrl.searchParams.get("foo") | "bar" |
| append(name, value) | 向查询字符串中追加新的参数 | myUrl.searchParams.append("newKey", "newValue") | ?foo=bar&newKey=newValue |
| set(name, value) | 设置查询字符串中指定名称的参数（若已存在则更新） | myUrl.searchParams.set("foo", "newBar") | ?foo=newBar |
| delete(name) | 删除指定名称的查询参数 | myUrl.searchParams.delete("foo") | ?hello=world |
| has(name) | 判断查询字符串中是否存在指定名称的参数 | myUrl.searchParams.has("foo") | true 或 false |
| forEach(callback) | 遍历查询参数的键值对，并执行回调函数 | myUrl.searchParams.forEach((v, k) => console.log(k, v)) | 键值对输出 |
| toString() | 将查询参数转换为字符串形式，适合重新构建 URL | myUrl.searchParams.toString() | "foo=bar&hello=world" |


## 实例


```javascript
const myUrl = new URL("http://example.com/path?foo=bar&hello=world");

console.log(myUrl.pathname);            // 输出: /path
console.log(myUrl.searchParams.get("foo")); // 输出: bar

myUrl.searchParams.append("newKey", "newValue");
console.log(myUrl.href);               // 输出: http://example.com/path?foo=bar&hello=world&newKey=newValue
```


---


## 获取 POST 请求内容


在 Node.js 中，处理 POST 请求通常需要通过 http 模块来接收请求体中的数据。POST 请求数据不像 GET 请求那样包含在 URL 中，而是作为请求体发送。因此，在 Node.js 中接收 POST 数据时，需要监听并处理 **request** 对象的 **data** 和 **end** 事件。


- **监听 `data` 事件**：当数据块到达服务器时，`data` 事件触发，数据块作为回调的参数传递。
- **监听 `end` 事件**：当整个请求体接收完毕时，`end` 事件触发，这时可以对完整的 POST 数据进行处理。


以下代码展示了如何在 Node.js 中使用 http 模块来处理 POST 请求:


## 实例


```javascript
const http = require('http');

// 创建 HTTP 服务器
http.createServer((req, res) => {
    // 检查请求方法是否为 POST
    if (req.method === 'POST') {
        let body = '';

        // 监听 data 事件，逐块接收数据
        req.on('data', (chunk) => {
            body += chunk; // 累加接收到的数据块
        });

        // 监听 end 事件，数据接收完毕
        req.on('end', () => {
            // 输出接收到的 POST 数据
            console.log('Received POST data:', body);

            // 设置响应头和内容
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end('POST data received successfully!');
        });

    } else {
        // 非 POST 请求的处理
        res.writeHead(405, { 'Content-Type': 'text/plain' });
        res.end('Only POST requests are supported.');
    }

}).listen(3000, () => {
    console.log('Server is running at http://localhost:3000');
});
```


**代码说明：**


- **检测请求方法**：通过 `req.method === 'POST'` 来判断请求类型是否为 POST。
- **接收数据**：在 `req.on('data')` 事件中累加数据块，形成完整的数据体。
- **完成接收**：在 `req.on('end')` 事件中处理完整的 POST 数据。
- **响应客户端**：完成数据接收和处理后，向客户端发送响应。


你可以使用 curl 命令来测试 POST 请求：


```
curl -X POST -d "name=example&age=25" http://localhost:3000
```


### 处理 JSON 数据

如果 POST 请求发送的是 JSON 数据，可以在 **req.on('end')** 中将接收的数据解析为对象：


```
req.on('end', () => {
    const parsedData = JSON.parse(body); // 将 JSON 字符串解析为对象
    console.log('Received JSON data:', parsedData);
    res.end('JSON data received successfully!');
});
```


### querystring 模块


querystring 模块用于处理 URL 查询字符串和 POST 请求的数据。

对于 application/x-www-form-urlencoded 编码的 POST 请求数据，querystring 模块可以帮助解析请求体，将它转换成 JavaScript 对象，方便访问和操作。


假设客户端发送的 POST 请求数据格式为 `application/x-www-form-urlencoded`（例如表单提交），数据形式类似于 `name=example&age=25`。在接收到数据后，可以使用 `querystring.parse` 方法将数据解析成对象。


## 基本语法结构说明


```javascript
var http = require('http');
var querystring = require('querystring');
var util = require('util');

http.createServer(function(req, res){
    // 定义了一个post变量，用于暂存请求体的信息
    var post = '';

    // 通过req的data事件监听函数，每当接受到请求体的数据，就累加到post变量中
    req.on('data', function(chunk){
        post += chunk;
    });

    // 在end事件触发后，通过querystring.parse将post解析为真正的POST请求格式，然后向客户端返回。
    req.on('end', function(){
        post = querystring.parse(post);
        res.end(util.inspect(post));
    });
}).listen(3000);
```


以下实例表单通过 POST 提交并输出数据：


## 实例


```javascript
var http = require('http');
var querystring = require('querystring');

var postHTML =
  '<html><head><meta charset="utf-8"><title>菜鸟教程 Node.js 实例</title></head>' +
  '<body>' +
  '<form method="post">' +
  '网站名： <input name="name"><br>' +
  '网站 URL： <input name="url"><br>' +
  '<input type="submit">' +
  '</form>' +
  '</body></html>';

http.createServer(function (req, res) {
  var body = "";
  req.on('data', function (chunk) {
    body += chunk;
  });
  req.on('end', function () {
    // 解析参数
    body = querystring.parse(body);
    // 设置响应头部信息及编码
    res.writeHead(200, {'Content-Type': 'text/html; charset=utf8'});

    if(body.name && body.url) { // 输出提交的数据
        res.write("网站名：" + body.name);
        res.write("<br>");
        res.write("网站 URL：" + body.url);
    } else {  // 输出表单
        res.write(postHTML);
    }
    res.end();
  });
}).listen(3000);
```


执行结果 Gif 演示：


![](https://www.runoob.com/wp-content/uploads/2014/06/nodepost.gif)








	  AI 思考中...





			** [Node.js 文件系统](https://www.runoob.com/nodejs-fs.html)
			[Node.js Buffer(缓冲区)](https://www.runoob.com/nodejs-buffer.html) **













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