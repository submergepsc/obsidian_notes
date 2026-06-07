# Node.js async/await

- Source: https://www.runoob.com/nodejs/nodejs-async-await.html

在 Node.js 中，`async/await` 是一种处理异步操作的语法糖。


`async/await` 基于 Promise，但让异步代码看起来更像同步代码，极大地提高了代码的可读性和可维护性。


`async` 关键字用于声明一个函数是异步的，而 `await` 关键字用于等待一个 Promise 的解决（resolve）或拒绝（reject）。

使用 `async/await` 可以避免回调地狱（callback hell）并使错误处理更加直观。


![](https://www.runoob.com/wp-content/uploads/2025/05/144869840-33551e3d-49f0-47ee-b7c2-9d7ec300fad2.png)


JavaScript 是单线程的，遇到异步任务（如 setTimeout 或网络请求）时，会交给 浏览器 API 处理，完成后将回调放入消息队列。

事件循环不断检查调用栈是否为空，如果是，就从队列中取出回调推入调用栈执行。这样既不会阻塞主线程，又能按顺序处理异步结果。


---


## 基本语法


### async 函数


任何函数都可以通过添加 `async` 关键字变成异步函数：


```javascript
async function myFunction() {
  return "Hello World";
}
```


`async` 函数总是返回一个 Promise。如果返回值不是 Promise，它会被自动包装成 Promise。


### await 表达式


`await` 只能在 `async` 函数内部使用，它会暂停函数的执行，等待 Promise 解决，然后继续执行并返回结果：


```javascript
async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  return data;
}
```


---


## 错误处理


### try/catch 方式


处理 `async/await` 错误最常用的方法是使用 `try/catch`：


## 实例


```javascript
async function getUser() {
  try {
    const response = await fetch('https://api.example.com/user');
    const user = await response.json();
    return user;
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error; // 可以选择重新抛出错误
  }
}
```


### 直接处理 Promise


你也可以直接处理返回的 Promise：


## 实例


```javascript
getUser()
  .then(user => console.log(user))
  .catch(error => console.error(error));
```


---


## 实际应用示例


### 并行执行多个异步操作


使用 `Promise.all` 结合 `async/await` 可以并行执行多个异步操作：


## 实例


```javascript
async function fetchMultipleUrls(urls) {
  try {
    const requests = urls.map(url => fetch(url));
    const responses = await Promise.all(requests);
    const data = await Promise.all(responses.map(r => r.json()));
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}
```


### 数据库操作示例


## 实例


```javascript
async function getUserAndPosts(userId) {
  try {
    const user = await User.findById(userId);
    const posts = await Post.find({ userId });
    return { user, posts };
  } catch (error) {
    console.error('Database error:', error);
    throw error;
  }
}
```


---


## 最佳实践


- **总是处理错误**：不要忽略 `await` 可能抛出的错误，使用 `try/catch` 或 `.catch()` 处理
- **避免不必要的 await**：如果不需要等待结果，可以直接返回 Promise
- **合理使用并行**：多个独立的异步操作应该并行执行（使用 `Promise.all`）
- **保持代码清晰**：避免过深的 `async/await` 嵌套，必要时提取函数
- **注意性能影响**：每个 `await` 都会暂停函数执行，在循环中要特别注意


---


## 常见问题


### async/await 与 Promise 的关系


`async/await` 是建立在 Promise 之上的语法糖。任何 `async` 函数都返回 Promise，任何 `await` 后面都可以接 Promise。


### 为什么我的 async 函数返回 undefined？


这可能是因为忘记在 `await` 前使用 `return`，或者在 Promise 解决前函数就退出了。


### 可以在顶层使用 await 吗？


在 ES 模块中（文件以 `.mjs` 结尾或 `package.json` 中 `"type": "module"`），可以直接在顶层使用 `await`。在 CommonJS 模块中，需要包裹在 `async` 函数中。


## 实例


```javascript
// 在 ES 模块中
const data = await fetchData();
console.log(data);
```










	  AI 思考中...





			** [Node.js Promise](https://www.runoob.com/nodejs-promise.html)
			[使用 VS Code 开发 Node.js](https://www.runoob.com/nodejs-vscode.html) **













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