# TypeScript Promise 详解

- Source: https://www.runoob.com/typescript/ts-promise.html

Promise 是 JavaScript 异步编程的基础，TypeScript 对 Promise 有完整的类型支持。


通过泛型参数，可以精确地指定 Promise 解决值和拒绝值的类型。


---






  Promise 工作流程



  创建 Promise

    new Promise((resolve,
     reject) => {...})




pending 等待中 fulfilled ✓ rejected ✗ then() · catch() · finally() --- ## 为什么需要 Promise 在 JavaScript 中，很多操作是异步的，如网络请求、文件读取、定时器等。


Promise 提供了统一的异步编程接口，让异步代码更容易编写和管理。


TypeScript 通过泛型支持，让 Promise 的类型安全得到了保障。


**
概念说明：**Promise 是一个对象，表示一个异步操作的最终结果。它有三种状态：pending（进行中）、fulfilled（已成功）、rejected（已失败）。


---


## 创建 Promise


使用 Promise 构造函数创建 Promise，传入执行器函数。


## 实例


```javascript
// 创建 Promise，使用泛型指定解决值的类型
// Promise<string> 表示成功时返回字符串
var promise = new Promise<string>(function(resolve, reject) {
    var success = true;
    if (success) {
        // 调用 resolve 表示操作成功，传入结果值
        resolve("成功!");
    } else {
        // 调用 reject 表示操作失败，传入错误
        reject(new Error("失败"));
    }
});

// 使用 then 处理成功情况
promise.then(function(value) {
    console.log("完成: " + value);
})["catch"](function(error) {
    // 使用 catch 处理失败情况
    console.log("错误: " + error.message);
});
```


**运行结果：**


```
完成: 成功!
```


**
泛型说明：**`Promise` 中的 T 是 Promise 成功解决时的值的类型。这让 TypeScript 能够推断返回值的类型。


---


## Promise 链式调用


then 和 catch 方法返回新的 Promise，可以链式调用。


## 实例


```javascript
// 链式调用：每个 then 返回新的值，被下一个 then 接收
var promise = Promise.resolve(1)
    .then(function(n) {
        // 第一个 then，n = 1
        return n * 2;  // 返回 2
    })
    .then(function(n) {
        // 第二个 then，n = 2
        return n + 10;  // 返回 12
    })
    .then(function(n) {
        // 第三个 then，n = 12
        console.log("最终结果: " + n);
        return n;
    });

console.log("Promise 链: " + promise);
```


**运行结果：**


```
最终结果: 12
Promise 链: [object Promise]
```


**
链式调用：**每个 then 会返回一个新的 Promise，这允许我们按顺序执行多个异步操作。


---


## Promise.all


Promise.all 等待所有 Promise 完成，返回一个包含所有结果的数组。


## 实例


```javascript
// 创建三个 Promise
var p1 = Promise.resolve(1);
var p2 = Promise.resolve(2);
var p3 = Promise.resolve(3);

// Promise.all 等待所有 Promise 完成
// 返回一个数组，包含所有 Promise 的结果
Promise.all([p1, p2, p3]).then(function(results) {
    console.log("全部完成: " + results);
    // 计算总和
    console.log("总和: " + results.reduce(function(a, b) { return a + b; }, 0));
});
```


**运行结果：**


```
全部完成: 1,2,3
总和: 6
```


**
注意：**如果任何一个 Promise 失败，Promise.all 会立即 rejection，不会等待其他 Promise 完成。


---


## Promise.race


Promise.race 返回最先完成（无论成功或失败）的 Promise 的结果。


## 实例


```javascript
// 创建三个不同延迟的 Promise
var p1 = new Promise(function(resolve) {
    setTimeout(function() { resolve("p1"); }, 100);
});
var p2 = new Promise(function(resolve) {
    setTimeout(function() { resolve("p2"); }, 50);
});
var p3 = new Promise(function(resolve) {
    setTimeout(function() { resolve("p3"); }, 30);
});

// Promise.race 返回最先完成的 Promise 的结果
Promise.race([p1, p2, p3]).then(function(value) {
    console.log("最先完成: " + value);
});
```


**运行结果：**


```
最先完成: p3
```


**
应用场景：**Promise.race 常用于实现超时功能：把一个长时间操作的 Promise 和一个超时 Promise 竞争。


---


## Promise.allSettled


Promise.allSettled 等待所有 Promise 结束（无论成功或失败），返回每个 Promise 的状态和结果。


## 实例


```javascript
// 创建三个 Promise，其中一个会失败
var p1 = Promise.resolve("成功");
var p2 = Promise.reject(new Error("失败"));
var p3 = Promise.resolve("完成");

// Promise.allSettled 等待所有 Promise 结束
// 返回每个 Promise 的状态和值/reason
Promise.allSettled([p1, p2, p3]).then(function(results) {
    results.forEach(function(result, index) {
        if (result.status === "fulfilled") {
            console.log("Promise " + index + ": " + result.value);
        } else {
            console.log("Promise " + index + ": " + result.reason.message);
        }
    });
});
```


**运行结果：**


```
Promise 0: 成功
Promise 1: 失败
Promise 2: 完成
```


**
区别：**Promise.all 会在第一个失败时立即停止；Promise.allSettled 会等待所有 Promise 结束。


---


## Promise 类型注解


TypeScript 的泛型支持让 Promise 的类型声明变得精确。


## 实例


```javascript
// 定义返回 Promise 的函数
// Promise<{ name: string; age: number }> 指定了返回的用户对象类型
function getUser(): Promise<{ name: string; age: number }> {
    return Promise.resolve({ name: "Alice", age: 25 });
}

// async 函数：隐式返回 Promise
async function main() {
    // await 会自动推断 user 的类型
    var user = await getUser();
    console.log("用户: " + JSON.stringify(user));
}

main();
```


**
类型推断：**TypeScript 会根据泛型参数自动推断 Promise 的返回类型，这让我们在 async/await 中也能获得完整的类型提示。


---


## 注意事项


- **泛型参数：**始终为 Promise 指定泛型参数，明确返回类型
- **错误处理：**记得使用 catch 处理 Promise 失败的情况
- **all vs allSettled：**需要全部结果时用 allSettled，需要快速失败时用 all
- **async/await：**现代代码推荐使用 async/await，语法更简洁


**
最佳实践：**优先使用 async/await 语法，它本质上还是基于 Promise，但写起来像同步代码。


---


## 总结


Promise 是 TypeScript 异步编程的核心。


- **Promise：**异步操作容器，有 pending/fulfilled/rejected 三种状态
- **then/catch：**链式处理异步结果
- **Promise.all：**等待全部完成，任一失败则整体失败
- **Promise.race：**返回最先完成的结果
- **Promise.allSettled：**等待全部结束，返回每个的状态


**
建议：**使用 async/await 语法配合 Promise，让异步代码既类型安全又易于阅读。

x







	  AI 思考中...





			** [TypeScript async/await 异步编程](https://www.runoob.com/ts-async-await.html)
			[TypeScript type 别名](https://www.runoob.com/ts-type-alias.html) **













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