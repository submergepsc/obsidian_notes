# Node.js Promise

- Source: https://www.runoob.com/nodejs/nodejs-promise.html

Promise 是 Node.js 中处理异步操作的核心概念之一。


Promise 提供了一种更优雅的方式来管理异步代码，避免了传统的回调地狱（Callback Hell）问题。

本文将详细介绍 Promise 的概念、用法和常见模式。


---


## 什么是 Promise？


Promise 是一个表示异步操作最终完成或失败的对象。它有三种状态：


- **Pending（等待中）**：初始状态，既不是成功，也不是失败
- **Fulfilled（已成功）**：操作成功完成
- **Rejected（已失败）**：操作失败


![](https://www.runoob.com/wp-content/uploads/2025/05/feb4c0cc-88c1-4507-915d-484f0a89c626.png)


Promise 的状态一旦改变（从 pending 变为 fulfilled 或 rejected），就不会再改变。


---


## 创建 Promise


在 Node.js 中，可以使用 `Promise` 构造函数创建新的 Promise 对象：


## 实例


```javascript
const myPromise = new Promise((resolve, reject) => {
  // 异步操作
  const success = true; // 假设这是异步操作的结果

  if (success) {
    resolve('操作成功！'); // 状态变为 fulfilled
  } else {
    reject('操作失败！'); // 状态变为 rejected
  }
});
```


---


## 使用 Promise


Promise 提供了 `.then()` 和 `.catch()` 方法来处理成功和失败的情况：


## 实例


```javascript
myPromise
  .then((result) => {
    console.log(result); // 输出："操作成功！"
  })
  .catch((error) => {
    console.error(error); // 输出："操作失败！"
  });
```


---


## Promise 链式调用


Promise 的强大之处在于可以链式调用多个异步操作：


## 实例


```javascript
function asyncOperation1() {
  return new Promise((resolve) => {
    setTimeout(() => resolve('第一步完成'), 1000);
  });
}

function asyncOperation2(data) {
  return new Promise((resolve) => {
    setTimeout(() => resolve(`${data}, 第二步完成`), 1000);
  });
}

asyncOperation1()
  .then((result) => asyncOperation2(result))
  .then((finalResult) => {
    console.log(finalResult); // 输出："第一步完成, 第二步完成"
  })
  .catch((error) => {
    console.error('链式中出错:', error);
  });
```


---


## Promise 的静态方法


Promise 提供了一些有用的静态方法：


### Promise.all()


等待所有 Promise 完成，或任意一个 Promise 失败：


## 实例


```javascript
const promise1 = Promise.resolve('第一个');
const promise2 = Promise.resolve('第二个');

Promise.all([promise1, promise2])
  .then((results) => {
    console.log(results); // 输出：['第一个', '第二个']
  });
```


### Promise.race()


返回最先完成或失败的 Promise：


## 实例


```javascript
const promise1 = new Promise((resolve) => setTimeout(resolve, 500, '第一个'));
const promise2 = new Promise((resolve) => setTimeout(resolve, 100, '第二个'));

Promise.race([promise1, promise2])
  .then((result) => {
    console.log(result); // 输出："第二个"
  });
```


---


## 错误处理


Promise 的错误处理可以通过 `.catch()` 或 `.then()` 的第二个参数实现：


## 实例


```javascript
someAsyncFunction()
  .then(
    (result) => { /* 处理成功 */ },
    (error) => { /* 处理失败 */ }
  );

// 或者
someAsyncFunction()
  .then((result) => { /* 处理成功 */ })
  .catch((error) => { /* 处理所有错误 */ });
```


---


## async/await 语法


ES2017 引入了 async/await 语法，让 Promise 的使用更加直观：


## 实例


```javascript
async function runOperations() {
  try {
    const result1 = await asyncOperation1();
    const result2 = await asyncOperation2(result1);
    console.log(result2);
  } catch (error) {
    console.error(error);
  }
}

runOperations();
```


---


## 最佳实践


- **总是处理错误**：不要忽略 `.catch()` 或 try-catch
- **避免嵌套**：使用链式调用或 async/await 保持代码扁平
- **命名 Promise**：给 Promise 变量起有意义的名称
- **返回 Promise**：在函数中返回 Promise 以便链式调用









	  AI 思考中...





			** [Node.js 异步编程](https://www.runoob.com/nodejs-asynchronous.html)
			[Node.js async/await](https://www.runoob.com/nodejs-async-await.html) **













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