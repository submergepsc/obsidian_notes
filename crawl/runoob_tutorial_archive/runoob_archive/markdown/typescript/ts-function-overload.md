# TypeScript 函数重载

- Source: https://www.runoob.com/typescript/ts-function-overload.html

函数重载（Function Overloading）允许为一个函数定义多个签名，编译器会根据传入的参数类型选择正确的实现。







    函数重载工作原理





    函数重载签名（声明）



    // 签名 1
    function add(a: number, b: number): number;
    // 签名 2
    function add(a: string, b: string): string;




编译器 匹配 函数实现（实际代码） function add(a: any, b: any): any { return a + b; } 必须兼容所有签名 调用时类型推断 add(1, 2) → number add("a", "b") → string add(true, false) → any --- ## 基本语法 先声明多个函数签名，然后实现一个统一函数。


## 实例


```javascript
// 函数重载签名
function add(a: number, b: number): number;
function add(a: string, b: string): string;
function add(a: any, b: any): any {
    return a + b;
}

console.log("数字相加: " + add(1, 2));
console.log("字符串相加: " + add("Hello, ", "World"));
```


**运行结果：**


```
数字相加: 3
字符串相加: Hello, World
```


---


## 多参数重载


可以定义多个参数的不同组合。


## 实例


```javascript
// 多种重载签名
function greet(name: string): string;
function greet(name: string, greeting: string): string;

// 实现
function greet(name: any, greeting?: any): any {
    if (greeting) {
        return greeting + ", " + name + "!";
    }
    return "Hello, " + name + "!";
}

console.log(greet("Alice"));
console.log(greet("Bob", "Hi"));
```


**运行结果：**


```
Hello, Alice!
Hi, Bob!
```


---


## 方法重载


类中的方法也可以使用重载。


## 实例


```javascript
class Calculator {
    // 重载签名
    add(a: number, b: number): number;
    add(a: string, b: string): string;
    add(a: number, b: string): string;
    add(a: any, b: any): any {
        return a + b;
    }
}

var calc = new Calculator();
console.log("数字: " + calc.add(1, 2));
console.log("字符串: " + calc.add("Hello", "World"));
console.log("混合: " + calc.add(5, " apples"));
```


**运行结果：**


```
数字: 3
字符串: HelloWorld
混合: 5 apples
```


---


## 构造函数重载


构造函数同样可以重载。


## 实例


```javascript
class User {
    name: string;
    age: number;

    // 构造函数重载
    constructor(name: string);
    constructor(name: string, age: number);
    constructor(name: any, age?: any) {
        this.name = name;
        this.age = age || 0;
    }
}

var user1 = new User("Alice");
var user2 = new User("Bob", 25);

console.log("用户1: " + JSON.stringify(user1));
console.log("用户2: " + JSON.stringify(user2));
```


**运行结果：**


```
用户1: {"name":"Alice","age":0}
用户2: {"name":"Bob","age":25}
```


---


## 重载与联合类型


使用重载而不是联合类型可以获得更精确的类型推断。


## 实例


```javascript
// 推荐：使用重载
function process(value: number): number;
function process(value: string): string;
function process(value: any): any {
    if (typeof value === "number") {
        return value * 2;
    }
    return value.toUpperCase();
}

// TypeScript 知道返回类型
var numResult: number = process(10);  // number
var strResult: string = process("hello");  // string

console.log("数字结果: " + numResult);
console.log("字符串结果: " + strResult);
```


**运行结果：**


```
数字结果: 20
字符串结果: HELLO
```


---


## 注意事项


- 重载签名必须放在实现签名之前
- 实现签名必须兼容所有重载签名
- 重载签名只是类型声明，不生成实际代码


---


## 总结


- **函数重载：**定义多个签名，编译器选择匹配的实现
- **方法重载：**类中同样适用
- **构造函数重载：**提供多种初始化方式
- **优于联合类型：**返回类型更精确








	  AI 思考中...





			** [TypeScript Set 和 WeakMap](https://www.runoob.com/ts-set-weakmap.html)
			[TypeScript 箭头函数与 this](https://www.runoob.com/ts-arrow-function.html) **













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