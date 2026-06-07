# Node.js 函数

- Source: https://www.runoob.com/nodejs/nodejs-function.html

函数是一段可重复使用的代码块，用于执行特定任务。


在 Node.js 中，函数是 JavaScript 的核心组成部分之一，是构建应用程序的基本单元。


Node.js 继承了 JavaScript 的所有函数特性，并在其异步编程模型中发挥了重要作用。


在 JavaScript中，一个函数可以作为另一个函数的参数。我们可以先定义一个函数，然后传递，也可以在传递参数的地方直接定义函数。


### 函数的重要性


- **代码复用**：避免重复编写相同逻辑
- **模块化**：将复杂问题分解为小函数
- **可维护性**：便于调试和修改独立功能单元


### 函数声明


使用 **function** 关键字声明一个函数。


```
function greet(name) {
    console.log(`Hello, ${name}!`);
}
```


### 函数表达式


将函数赋值给一个变量。


```
const greet = function(name) {
    console.log(`Hello, ${name}!`);
};
```


### 箭头函数

ES6 引入的简洁函数表达式。


```
const greet = (name) => {
    console.log(`Hello, ${name}!`);
};

// 单行箭头函数
const greet = name => console.log(`Hello, ${name}!`);
```


### 函数的类型


**1、普通函数**

最常见的函数形式，可以有参数和返回值。


```
function add(a, b) {
    return a + b;
}
```


**2、匿名函数**

没有名字的函数，通常作为参数传递给其他函数。


```
setTimeout(function() {
    console.log('This is an anonymous function.');
}, 1000);
```


**3、回调函数**

作为参数传递给另一个函数，并在某个操作完成后被调用。


```
function fetchData(callback) {
    setTimeout(() => {
        const data = 'Some data';
        callback(data);
    }, 1000);
}

fetchData((data) => {
    console.log(data);
});
```


### 异步函数


从回调到 Promise。


## 实例


```javascript
function readFilePromise(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}
```


使用 async 和 await 关键字处理异步操作。


## 实例


```javascript
async function fetchUser(id) {
    try {
        const response = await fetch(`https://api.example.com/users/${id}`);
        const user = await response.json();
        return user;
    } catch (error) {
        console.error('Error fetching user:', error);
    }
}

fetchUser(1).then(user => console.log(user));
```


### 调用方式对比


| 调用方式 | 示例 | 特点 |
| --- | --- | --- |
| 直接调用 | greet('Alice') | 最常见的方式 |
| 作为方法调用 | obj.method() | this 指向调用对象 |
| 构造函数调用 | new Constructor() | 创建新实例 |
| 间接调用 | greet.call(null, 'Bob') | 可改变 this 指向 |


---


## 高级用法


**1、闭包**

闭包是指一个函数能够记住并访问其词法作用域，即使这个函数在其词法作用域之外执行。


## 实例


```javascript
function createCounter() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}

const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2
```


**2、高阶函数**

接受函数作为参数或返回函数的函数。


## 实例


```javascript
function applyOperation(a, b, operation) {
    return operation(a, b);
}

const sum = applyOperation(5, 3, (x, y) => x + y);
const product = applyOperation(5, 3, (x, y) => x * y);

console.log(sum); // 8
console.log(product); // 15
```


---


## 函数参数处理


### 默认参数

在函数声明时为参数提供默认值。


```
function greet(name = 'Guest') {
    console.log(`Hello, ${name}!`);
}

greet(); // Hello, Guest!
greet('Alice'); // Hello, Alice!
```


### 剩余参数


允许将不定数量的参数表示为一个数组。


## 实例


```javascript
function sum(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
}

console.log(sum(1, 2, 3, 4)); // 10
```


### 解构参数

从对象或数组中提取数据并将其赋值给变量。


## 实例


```javascript
function getUserInfo({ name, age }) {
    console.log(`Name: ${name}, Age: ${age}`);
}

const user = { name: 'Alice', age: 30 };
getUserInfo(user); // Name: Alice, Age: 30
```


---

## 实例

**函数单一职责：**每个函数应该只做一件事，这样更容易测试和维护。


## 实例


```javascript
function calculateArea(width, height) {
    return width * height;
}
```


**避免全局变量：**尽量减少全局变量的使用，使用局部变量和函数参数。


## 实例


```javascript
function calculateTotal(items) {
    let total = 0;
    for (const item of items) {
        total += item.price * item.quantity;
    }
    return total;
}
```


**使用箭头函数：**箭头函数简洁明了，特别是在处理回调函数时。


## 实例


```javascript
const users = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' }
];

const names = users.map(user => user.name);
console.log(names); // ['Alice', 'Bob']
```


**错误处理：** 使用 try...catch 语句处理可能抛出的错误。


## 实例


```javascript
async function fetchUser(id) {
    try {
        const response = await fetch(`https://api.example.com/users/${id}`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const user = await response.json();
        return user;
    } catch (error) {
        console.error('Error fetching user:', error);
    }
}
```


**函数作为参数:** 函数作为一个参数来使用。


## 实例


```javascript
function say(word) {
  console.log(word);
}

function execute(someFunction, value) {
  someFunction(value);
}

execute(say, "Hello");
```


以上代码中，我们把 say 函数作为 execute 函数的第一个变量进行了传递。这里传递的不是 say 的返回值，而是 say 本身！


这样一来， say 就变成了execute 中的本地变量 someFunction ，execute 可以通过调用 someFunction() （带括号的形式）来使用 say 函数。


当然，因为 say 有一个变量， execute 在调用 someFunction 时可以传递这样一个变量。

**匿名函数：**我们可以把一个函数作为变量传递。但是我们不一定要绕这个"先定义，再传递"的圈子，我们可以直接在另一个函数的括号中定义和传递这个函数：


## 实例


```javascript
function execute(someFunction, value) {
  someFunction(value);
}

execute(function(word){ console.log(word) }, "Hello");
```


我们在 execute 接受第一个参数的地方直接定义了我们准备传递给 execute 的函数。


用这种方式，我们甚至不用给这个函数起名字，这也是为什么它被叫做匿名函数 。


---


## 函数传递是如何让 HTTP 服务器工作的


带着这些知识，我们再来看看我们简约而不简单的HTTP服务器：


## 实例


```javascript
var http = require("http");

http.createServer(function(request, response) {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.write("Hello World");
  response.end();
}).listen(8888);
```


现在它看上去应该清晰了很多：我们向 createServer 函数传递了一个匿名函数。


用这样的代码也可以达到同样的目的：


## 实例


```javascript
var http = require("http");

function onRequest(request, response) {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.write("Hello World");
  response.end();
}

http.createServer(onRequest).listen(8888);
```


---


## 函数最佳实践


### 函数设计原则


- **单一职责**：一个函数只做一件事
- **合理命名**：使用动词+名词形式（如 `getUserInfo`）
- **控制长度**：建议不超过20行代码
- **避免副作用**：纯函数更易于测试和维护


### 性能优化技巧


## 实例


```javascript
// 使用闭包缓存结果
function memoize(fn) {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}
```


---


## 实战练习


### 练习1：创建温度转换函数


## 实例


```javascript
/**
 * 实现摄氏度和华氏度互相转换
 * @param {number} temp - 温度值
 * @param {string} unit - 原始单位 ('C' 或 'F')
 * @returns {number} 转换后的温度
 */
function convertTemperature(temp, unit) {
  // 你的代码...
}
```


### 练习2：实现简单的事件发射器


## 实例


```javascript
class EventEmitter {
  constructor() {
    this.events = {};
  }

  // 实现 on/emit/off 方法
}
```










	  AI 思考中...





			** [Node.js EventEmitter](https://www.runoob.com/nodejs-event.html)
			[Node.js 路由](https://www.runoob.com/nodejs-router.html) **













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