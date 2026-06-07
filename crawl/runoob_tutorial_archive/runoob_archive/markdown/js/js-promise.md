# JavaScript Promise

- Source: https://www.runoob.com/js/js-promise.html

在学习本章节内容前，你需要先了解什么是异步编程，可以参考：[JavaScript 异步编程](https://www.runoob.com/javascript-async.html)


Promise 是一个 ECMAScript 6 提供的类，目的是更加优雅地书写复杂的异步任务。


Promise 是 JavaScript 中用于处理异步操作的对象，它代表一个异步操作的最终完成（或失败）及其结果值。


简单来说，Promise 是一个"承诺"，表示将来某个时间点会返回一个结果（可能是成功的结果，也可能是失败的原因）。 Promise 有三种状态：


- pending：初始状态，既不是成功，也不是失败状态
- fulfilled：意味着操作成功完成
- rejected：意味着操作失败


![](https://www.runoob.com/wp-content/uploads/2025/05/feb4c0cc-88c1-4507-915d-484f0a89c626.png)


## 实例


```javascript
const myPromise = new Promise((resolve, reject) => {
  // 异步操作代码

  if (/* 操作成功 */) {
    resolve('成功的结果'); // 将 Promise 状态改为 fulfilled
  } else {
    reject('失败的原因'); // 将 Promise 状态改为 rejected
  }
});
```


### 浏览器支持


由于 Promise 是 ES6 新增加的，所以一些旧的浏览器并不支持，苹果的 Safari 10 和 Windows 的 Edge 14 版本以上浏览器才开始支持 ES6 特性。

以下是 Promise 浏览器支持的情况：


|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Chrome 58 | Edge 14 | Firefox 54 | Safari 10 | Opera 55 |


---


## Promise 的使用方法


### then() 方法


`then()` 方法用于指定 Promise 状态变为 fulfilled 或 rejected 时的回调函数。


## 实例


```javascript
myPromise.then(
  (result) => {
    // 处理成功情况
    console.log('成功:', result);
  },
  (error) => {
    // 处理失败情况
    console.error('失败:', error);
  }
);
```


### catch() 方法


`catch()` 方法专门用于处理 Promise 被拒绝的情况。


## 实例


```javascript
myPromise
  .then((result) => {
    console.log('成功:', result);
  })
  .catch((error) => {
    console.error('失败:', error);
  });
```


### finally() 方法


`finally()` 方法无论 Promise 最终状态如何都会执行。


## 实例


```javascript
myPromise
  .then((result) => {
    console.log('成功:', result);
  })
  .catch((error) => {
    console.error('失败:', error);
  })
  .finally(() => {
    console.log('操作完成');
  });
```


---


## Promise 的链式调用


Promise 的一个强大特性是可以链式调用多个异步操作。


## 实例


```javascript
doFirstThing()
  .then((result) => doSecondThing(result))
  .then((newResult) => doThirdThing(newResult))
  .then((finalResult) => {
    console.log('最终结果:', finalResult);
  })
  .catch((error) => {
    console.error('链中某处出错:', error);
  });
```


---


## Promise 的静态方法


### Promise.all()


等待所有 Promise 完成，或任意一个 Promise 失败。


## 实例


```javascript
Promise.all([promise1, promise2, promise3])
  .then((results) => {
    // results 是一个包含所有 Promise 结果的数组
    console.log(results);
  })
  .catch((error) => {
    // 任一 Promise 失败就会进入这里
    console.error(error);
  });
```


### Promise.race()


返回最先完成（无论成功或失败）的 Promise 的结果。


## 实例


```javascript
Promise.race([promise1, promise2, promise3])
  .then((result) => {
    // 使用最先完成的 Promise 的结果
    console.log(result);
  })
  .catch((error) => {
    // 如果最先完成的 Promise 是失败的
    console.error(error);
  });
```


### Promise.resolve() 和 Promise.reject()


快速创建已解决或已拒绝的 Promise。


## 实例


```javascript
const resolvedPromise = Promise.resolve('立即解决的值');
const rejectedPromise = Promise.reject('立即拒绝的原因');
```


---


## 实际应用示例


### 示例 1: 使用 Promise 处理 AJAX 请求


## 实例


```javascript
function fetchData(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.onload = () => {
      if (xhr.status === 200) {
        resolve(xhr.response);
      } else {
        reject(new Error(xhr.statusText));
      }
    };
    xhr.onerror = () => reject(new Error('网络错误'));
    xhr.send();
  });
}

fetchData('https://api.example.com/data')
  .then((data) => {
    console.log('获取数据成功:', data);
  })
  .catch((error) => {
    console.error('获取数据失败:', error);
  });
```


### 示例 2: 使用 Promise 链处理多个异步操作


## 实例


```javascript
function getUser(userId) {
  return fetch(`/users/${userId}`);
}

function getPosts(userId) {
  return fetch(`/users/${userId}/posts`);
}

getUser(123)
  .then((user) => {
    console.log('获取用户信息:', user);
    return getPosts(user.id);
  })
  .then((posts) => {
    console.log('获取用户帖子:', posts);
  })
  .catch((error) => {
    console.error('操作失败:', error);
  });
```


---


## 常见问题与最佳实践


### 1. 避免 Promise 嵌套


错误做法（回调地狱的 Promise 版本）：


## 实例


```javascript
doFirstThing().then((firstResult) => {
  doSecondThing(firstResult).then((secondResult) => {
    doThirdThing(secondResult).then((thirdResult) => {
      console.log(thirdResult);
    });
  });
});
```


正确做法（使用链式调用）：


## 实例


```javascript
doFirstThing()
  .then(doSecondThing)
  .then(doThirdThing)
  .then((finalResult) => {
    console.log(finalResult);
  });
```


### 2. 总是处理拒绝情况


忘记处理 Promise 的拒绝会导致"未捕获的 Promise 拒绝"错误。总是使用 `.catch()` 或 `try/catch`（在 async/await 中）来处理错误。


### 3. Promise 不是可取消的


一旦创建，Promise 就无法取消。如果需要取消功能，可以考虑使用 AbortController 或其他模式。


### 4. 回答常见的问题（FAQ）


**Q: then、catch 和 finally 序列能否顺序颠倒？**

A: 可以，效果完全一样。但不建议这样做，最好按 then-catch-finally 的顺序编写程序。


**Q: 除了 then 块以外，其它两种块能否多次使用？**

A: 可以，finally 与 then 一样会按顺序执行，但是 catch 块只会执行第一个，除非 catch 块里有异常。所以最好只安排一个 catch 和 finally 块。


**Q: then 块如何中断？**

A: then 块默认会向下顺序执行，return 是不能中断的，可以通过 throw 来跳转至 catch 实现中断。


**Q: 什么时候适合用 Promise 而不是传统回调函数？**

A: 当需要多次顺序执行异步操作的时候，例如，如果想通过异步方法先后检测用户名和密码，需要先异步检测用户名，然后再异步检测密码的情况下就很适合 Promise。


**Q: Promise 是一种将异步转换为同步的方法吗？**

A: 完全不是。Promise 只不过是一种更良好的编程风格。


**Q: 什么时候我们需要再写一个 then 而不是在当前的 then 接着编程？**

A: 当你又需要调用一个异步任务的时候。


---


## Promise 与 async/await


ES2017 引入了 async/await，它基于 Promise 并提供更直观的语法来处理异步操作。


## 实例


```javascript
async function fetchData() {
  try {
    const user = await getUser(123);
    const posts = await getPosts(user.id);
    console.log('用户帖子:', posts);
  } catch (error) {
    console.error('获取数据失败:', error);
  }
}
```


虽然 async/await 更易读，但理解 Promise 的基本概念仍然很重要，因为它是 async/await 的基础。









	  AI 思考中...





			** [JavaScript 异步编程](https://www.runoob.com/js-async.html)
			[Chrome 浏览器中执行 JavaScript](https://www.runoob.com/js-chrome.html) **