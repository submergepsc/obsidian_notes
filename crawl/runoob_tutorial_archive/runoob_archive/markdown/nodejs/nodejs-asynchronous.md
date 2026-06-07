# Node.js 异步编程

- Source: https://www.runoob.com/nodejs/nodejs-asynchronous.html

在传统的**同步（Synchronous）编程**中，代码是按顺序执行的，每一行代码必须等待前一行代码执行完成后才能运行。而**异步编程（Asynchronous）**则允许代码在等待某些操作（如 I/O 操作）完成的同时继续执行其他任务，不会阻塞程序的运行。


![](https://www.runoob.com/wp-content/uploads/2025/05/Asynchronous-Synchronous.png)


Node.js 采用异步 I/O 模型，这使得它特别适合处理高并发的网络应用。理解异步编程是掌握 Node.js 的关键。


---


## 为什么 Node.js 需要异步编程


Node.js 是单线程的，这意味着它一次只能执行一个任务。如果使用同步编程方式，当一个耗时操作（如读取大文件或网络请求）执行时，整个程序会被阻塞，无法处理其他请求。


异步编程解决了这个问题：


- 提高应用程序的吞吐量
- 更有效地利用系统资源
- 提供更好的用户体验


---


## Node.js 异步编程的三种主要方式


### 1、回调函数 (Callbacks)


回调函数是 Node.js 中最基础的异步处理方式。它通过将一个函数作为参数传递给另一个函数，在操作完成后调用这个函数。


## 实例


```javascript
const fs = require('fs');

// 异步读取文件
fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('读取文件出错:', err);
    return;
  }
  console.log('文件内容:', data);
});

console.log('读取文件请求已发送，继续执行其他代码...');
```


**特点**：


- 简单直接
- 容易导致"回调地狱"(Callback Hell)
- 错误处理不够直观


### 2、Promise


Promise 是 ES6 引入的异步编程解决方案，它表示一个异步操作的最终完成或失败及其结果值。


## 实例


```javascript
const fs = require('fs').promises;

// 使用 Promise 读取文件
fs.readFile('example.txt', 'utf8')
  .then(data => {
    console.log('文件内容:', data);
  })
  .catch(err => {
    console.error('读取文件出错:', err);
  });

console.log('读取文件请求已发送，继续执行其他代码...');
```


**特点**：


- 链式调用，避免回调地狱
- 更好的错误处理机制
- 状态不可逆（pending → fulfilled 或 rejected）


### 3、async/await


async/await 是 ES8 引入的语法糖，基于 Promise，使异步代码看起来像同步代码。


## 实例


```javascript
const fs = require('fs').promises;

async function readFile() {
  try {
    const data = await fs.readFile('example.txt', 'utf8');
    console.log('文件内容:', data);
  } catch (err) {
    console.error('读取文件出错:', err);
  }
}

readFile();
console.log('读取文件请求已发送，继续执行其他代码...');
```


**特点**：


- 代码更简洁，更易读
- 错误处理使用 try/catch 结构
- 必须用在 async 函数中


---


## 错误处理最佳实践


### 回调函数中的错误处理


## 实例


```javascript
fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('读取文件出错:', err);
    return; // 重要：处理错误后返回，避免执行后续代码
  }
  console.log('文件内容:', data);
});
```


### Promise 的错误处理


## 实例


```javascript
fs.readFile('example.txt', 'utf8')
  .then(data => {
    console.log('文件内容:', data);
    return someOtherAsyncOperation(data);
  })
  .then(result => {
    console.log('第二步结果:', result);
  })
  .catch(err => {
    console.error('处理过程中出错:', err);
  });
```


### async/await 的错误处理


## 实例


```javascript
async function processData() {
  try {
    const data = await fs.readFile('example.txt', 'utf8');
    const result = await someOtherAsyncOperation(data);
    console.log('最终结果:', result);
  } catch (err) {
    console.error('处理过程中出错:', err);
  }
}

processData();
```


---


## 性能考虑


- **避免阻塞事件循环**：长时间运行的同步代码会阻塞整个应用
- **合理使用异步**：不是所有操作都需要异步，简单的计算任务使用同步方式可能更高效
- **控制并发量**：过多的并行异步操作可能导致资源耗尽
- **使用流处理大文件**：对于大文件，使用流(Stream)而不是一次性读取








	  AI 思考中...





			** [NVM 管理多版本 Node.js](https://www.runoob.com/nodejs-nvm.html)
			[Node.js Promise](https://www.runoob.com/nodejs-promise.html) **













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