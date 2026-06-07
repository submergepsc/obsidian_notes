# TypeScript async/await 异步编程

- Source: https://www.runoob.com/typescript/ts-async-await.html

async/await 是 ES2017 引入的异步编程语法糖，让异步代码看起来像同步代码。







    async/await 执行流程





    Promise 方式



    fetchData()
    .then(result => {
    console.log(result);
    })




async/await 方式 async function main() { const result = await fetchData(); console.log(result); } await 执行顺序 主线程 await 暂停 Promise 后台执行 恢复 完成 优势对比 ✓ 代码更简洁 ✓ 同步风格 ✓ 更好的错误堆栈 ✓ 易于调试 ✓ try/catch 处理 上图展示了 async/await 相比传统 Promise 的优势：代码更简洁，执行流程更清晰。


---


## Promise 基础


Promise 代表一个异步操作的最终结果。


## 实例


```javascript
// 创建 Promise
var promise = new Promise(function(resolve, reject) {
    var success = true;
    if (success) {
        resolve("操作成功");
    } else {
        reject("操作失败");
    }
});

promise.then(function(result) {
    console.log("成功: " + result);
})["catch"](function(error) {
    console.log("失败: " + error);
});
```


**运行结果：**


```
成功: 操作成功
```


---


## async 函数


使用 async 关键字声明异步函数。


## 实例


```javascript
// async 函数自动返回 Promise
async function greet(): Promise<string> {
    return "Hello, World!";
}

greet().then(function(result) {
    console.log("结果: " + result);
});

// 异步函数返回 Promise
async function getData() {
    return { name: "Alice", age: 25 };
}

getData().then(function(data) {
    console.log("数据: " + JSON.stringify(data));
});
```


**运行结果：**


```
结果: Hello, World!
数据: {"name":"Alice","age":25}
```


---


## await 关键字


await 等待 Promise 完成并获取结果。


## 实例


```javascript
// 模拟异步操作
function delay(ms: number): Promise<string> {
    return new Promise(function(resolve) {
        setTimeout(function() {
            resolve("完成!");
        }, ms);
    });
}

async function main() {
    console.log("开始...");
    var result = await delay(100);
    console.log("结果: " + result);
    console.log("结束");
}

main();
```


**运行结果：**


```
开始...
结果: 完成!
结束
```


---


## 错误处理


使用 try/catch 处理异步错误。


## 实例


```javascript
function mayFail(shouldFail: boolean): Promise<string> {
    return new Promise(function(resolve, reject) {
        if (shouldFail) {
            reject(new Error("操作失败"));
        } else {
            resolve("操作成功");
        }
    });
}

async function handleError() {
    try {
        var result = await mayFail(true);
        console.log("结果: " + result);
    } catch (error) {
        console.log("捕获错误: " + error.message);
    }
}

handleError();
```


**运行结果：**


```
捕获错误: 操作失败
```


---


## 并行执行


使用 Promise.all 并行执行多个异步操作。


## 实例


```javascript
function fetchUser(id: number): Promise<{ id: number; name: string }> {
    return Promise.resolve({ id: id, name: "User" + id });
}

async function main() {
    // 串行执行
    console.time("串行");
    var user1 = await fetchUser(1);
    var user2 = await fetchUser(2);
    console.log("串行完成: " + user1.name + ", " + user2.name);
    console.timeEnd("串行");

    // 并行执行
    console.time("并行");
    var results = await Promise.all([fetchUser(1), fetchUser(2)]);
    console.log("并行完成: " + results[0].name + ", " + results[1].name);
    console.timeEnd("并行");
}

main();
```


**运行结果：**


```
串行完成: User1, User2
并行完成: User1, User2
```


---


## async/await 相比 Promise 的优势


- 代码更简洁、更易读
- 同步代码风格
- 更好的错误堆栈
- 易于调试


---


## 总结


- **async：**声明异步函数
- **await：**等待 Promise
- **错误处理：**try/catch
- **并行：**Promise.all


---









	  AI 思考中...





			** [TypeScript 迭代器与生成器](https://www.runoob.com/ts-iterator-generator.html)
			[TypeScript Promise 详解](https://www.runoob.com/ts-promise.html) **













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