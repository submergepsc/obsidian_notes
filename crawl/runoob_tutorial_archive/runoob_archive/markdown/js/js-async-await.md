# JavaScript async/await

- Source: https://www.runoob.com/js/js-async-await.html

在讲解 async/await 之前，我们需要先理解 JavaScript 中的异步编程概念，可以参考：[JavaScript 异步编程](https://www.runoob.com/javascript-async.html)。

JavaScript 是单线程语言，意味着它一次只能执行一个任务。为了避免长时间运行的任务阻塞主线程，JavaScript 使用异步编程模型。


### 异步 vs 同步


- **同步（Synchronous）编程**：代码按顺序执行，前一个操作完成后才会执行下一个
- **异步编程（Asynchronous）**：某些操作被放入"任务队列"，主线程继续执行后续代码，等主线程空闲时再处理队列中的任务


![](https://www.runoob.com/wp-content/uploads/2025/05/Asynchronous-Synchronous.png)


## 实例


```javascript
// 同步示例
console.log('1');
console.log('2');
// 输出: 1, 2

// 异步示例
console.log('1');
setTimeout(() => console.log('2'), 0);
console.log('3');
// 输出: 1, 3, 2
```


---


## 回调函数的问题


在 async/await 出现之前，JavaScript 主要使用回调函数处理异步操作，但这会导致"回调地狱"（Callback Hell）。


## 实例


```javascript
getData(function(a) {
  getMoreData(a, function(b) {
    getMoreData(b, function(c) {
      getMoreData(c, function(d) {
        console.log(d);
      });
    });
  });
});
```


这种嵌套结构使得代码难以阅读和维护。


---


## Promise 的引入


ES6 引入了 Promise 对象来解决回调地狱问题。


## 实例


```javascript
function getData() {
  return new Promise((resolve, reject) => {
    // 异步操作
    setTimeout(() => resolve('数据'), 1000);
  });
}

getData()
  .then(data => {
    console.log(data);
    return getMoreData(data);
  })
  .then(moreData => {
    console.log(moreData);
  })
  .catch(error => {
    console.error(error);
  });
```


虽然 Promise 改善了回调问题，但 then() 链式调用仍然不够直观。


---


## async/await 语法


ES2017 引入了 async/await，它建立在 Promise 之上，让异步代码看起来像同步代码一样。


### async 函数


在函数声明前添加 async 关键字，表示该函数是异步的：


```javascript
async function fetchData() {
  // 函数体
}
```


async 函数总是返回一个 Promise：


- 如果返回值不是 Promise，会自动包装成 resolved Promise
- 如果抛出异常，会返回 rejected Promise


### await 表达式


await 只能在 async 函数内部使用：


```javascript
async function fetchData() {
  const result = await somePromise;
  console.log(result);
}
```


await 会暂停 async 函数的执行，等待 Promise 完成：


- 如果 Promise 被 resolve，返回 resolve 的值
- 如果 Promise 被 reject，抛出错误（可以用 try/catch 捕获）


---


## 实际应用示例


### 基本用法


## 实例


```javascript
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function showMessage() {
  console.log('开始');
  await delay(1000);
  console.log('1秒后');
  await delay(1000);
  console.log('又1秒后');
}

showMessage();
```


### 错误处理


## 实例


```javascript
async function fetchUserData() {
  try {
    const response = await fetch('https://api.example.com/user');
    if (!response.ok) {
      throw new Error('网络响应不正常');
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('获取数据失败:', error);
  }
}
```


### 并行执行


如果需要并行执行多个异步操作，可以使用 Promise.all：


## 实例


```javascript
async function fetchMultipleData() {
  const [userData, productData] = await Promise.all([
    fetch('/api/user'),
    fetch('/api/products')
  ]);

  const user = await userData.json();
  const products = await productData.json();

  return { user, products };
}
```


---


## 常见问题与最佳实践


### 1. 不要忘记 await


## 实例


```javascript
// 错误示例 - 忘记 await
async function example() {
  const data = fetch('/api'); // 缺少 await
  console.log(data); // 输出 Promise 对象
}

// 正确示例
async function example() {
  const data = await fetch('/api');
  console.log(data); // 输出实际数据
}
```


### 2. 避免不必要的 async


## 实例


```javascript
// 不必要 - 函数内部没有 await
async function unnecessaryAsync() {
  return 42;
}

// 更简单的写法
function simpleFunction() {
  return 42;
}
```


### 3. 顶层 await


在模块顶层可以直接使用 await（ES2022 特性）：


## 实例


```javascript
// 在模块中
const data = await fetch('/api');
console.log(data);
```


### 4. 性能考虑


- 顺序执行 vs 并行执行：合理使用 Promise.all 提高性能
- 错误处理：确保所有可能的错误都被捕获


---


## async/await 与传统 Promise 对比


| 特性 | async/await | Promise then/catch |
| --- | --- | --- |
| 可读性 | 高，类似同步代码 | 中，链式调用 |
| 错误处理 | 使用 try/catch | 使用 .catch() |
| 调试 | 更容易，有明确的调用栈 | 较困难，调用栈可能不清晰 |
| 代码结构 | 更扁平 | 嵌套或链式 |


---


## 总结


async/await 是 JavaScript 异步编程的重大改进，它：


- 使异步代码更易读、更易维护
- 基于 Promise，与现有 Promise 代码兼容
- 提供了更直观的错误处理方式
- 改善了调试体验


虽然 async/await 不是完全替代 Promise，但在大多数情况下，它提供了更优雅的解决方案。理解 async/await 的工作原理和最佳实践，将大大提升你的 JavaScript 异步编程能力。









	  AI 思考中...





			** [JavaScript 测验](https://www.runoob.com/js-quiz.html)














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