# Node.js 构建简单应用

- Source: https://www.runoob.com/nodejs/nodejs-build-app.html

在 Node.js 中构建一个简单应用通常包括以下几个步骤：


- 安装 Node.js
- 设置项目目录
- 初始化项目
- 创建服务器
- 并处理请求和响应


接下来，我们将一步步介绍如何用 Node.js 构建一个简单的 HTTP 应用程序。


### 1、安装 Node.js

首先确保系统上已安装 Node.js 和 npm，可以在命令行中输入以下命令进行验证：


```
node -v
npm -v
```


如果还未安装，请参考：[Node.js 安装配置](https://www.runoob.com/nodejs-install-setup.html)。


### 2、创建项目文件夹

在终端中，创建一个项目文件夹 **my-first-node-app** 并进入该文件夹：


```
mkdir my-first-node-app
cd my-first-node-app
```


### 3、初始化项目

通过 **npm init** 命令生成 package.json 文件，它包含了项目的配置信息。


运行以下命令并按提示填写信息（可以直接按回车跳过）：


```
npm init -y
```


把 package.json 文件修改为以下内容：


```
{
  "name": "my-first-node-app",
  "version": "1.0.0",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {}
}
```


### 4、创建应用入口文件


在项目根目录 **my-first-node-app** 下创建一个 **app.js** 文件，这是应用的入口文件，用于设置服务器和处理请求。


### 5、编写服务器代码

在 app.js 文件中编写以下代码，用于创建一个简单的 HTTP 服务器：


## 实例


```javascript
const http = require('http');

// 创建服务器
const server = http.createServer((req, res) => {
  // 设置HTTP响应的状态码和头信息
  res.writeHead(200, {
    // 设置内容类型为 HTML，并指定字符集为 UTF-8，这样中文不会乱码
    'Content-Type': 'text/html; charset=utf-8'
  });

  // 发送响应体
  res.end('<h1>Hello, World!</h1><p>这是我的第一个 Node.js 应用。</p>');
});

// 监听端口
const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```


### 6、运行服务器

在项目根目录下执行以下命令，启动服务器：


```
npm start
```


你会看到控制台输出如下信息：


```
Server is running on http://localhost:3000
```


### 7、访问服务器


打开浏览器并访问 http://localhost:3000，你会看到页面显示如下：


![](https://www.runoob.com/wp-content/uploads/2024/11/a19c5ff5f88cd14db6ac69707a634cfb.png)

说明服务器已经成功运行。


### 8、添加路由

为了处理不同的请求路径，可以在服务器代码中添加简单的路由，例如：


## 实例


```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Welcome to the homepage!');
  } else if (req.url === '/about') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('This is the about page.');
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found');
  }
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```


通过上述步骤，你已经构建了一个简单的 Node.js 应用，并且可以处理不同的请求路径。

这个基础应用可以进一步扩展，如添加数据库支持、引入 Express 框架处理复杂路由等，为更复杂的项目奠定基础。








	  AI 思考中...





			** [Node.js 连接 MongoDB](https://www.runoob.com/nodejs-mongodb.html)
			[Node.js 基础概念](https://www.runoob.com/nodejs-intro.html) **













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