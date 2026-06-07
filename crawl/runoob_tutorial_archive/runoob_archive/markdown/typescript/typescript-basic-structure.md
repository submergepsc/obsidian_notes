# TypeScript 基本结构

- Source: https://www.runoob.com/typescript/typescript-basic-structure.html

TypeScript 程序的基本结构可以分为几个部分，每个部分都有特定的作用。

以下是 TypeScript 程序的常见组成部分：


- **声明部分**：包括类型声明、接口声明等。
- **变量声明**：包括 `let`, `const` 和 `var` 的使用。
- **函数声明**：包括普通函数和箭头函数。
- **类声明**：用于定义类及其成员。
- **接口与类型别名**：描述类型的结构。
- **模块化**：通过 `import` 和 `export` 组织代码。
- **类型断言**：强制类型转换。
- **泛型**：使代码具备更多的复用性。
- **注释**：增加代码的可读性。
- **类型推断**：自动推断类型。
- **类型守卫**：缩小类型范围。
- **异步编程**：支持 `async/await`。
- **错误处理**：通过 `try/catch` 进行错误捕捉。

以上几个部分共同构成了 TypeScript 程序的基本结构，并为开发者提供了强大的类型检查、代码结构和可维护性。


---


## 1. 声明部分（Declarations）

**类型声明：**TypeScript 是一种静态类型的语言，可以通过类型声明来定义变量、函数、类等的类型。类型声明可以帮助代码更具可维护性和可读性。


## 实例


```javascript
let name: string = "Alice";
let age: number = 30;
```


**接口声明：**用于定义对象的结构，包括对象的属性和方法。


## 实例


```javascript
interface Person {
    name: string;
    age: number;
}
```


---

## 2. 变量声明（Variable Declarations）


在 TypeScript 中，可以使用 let, const, 和 var 来声明变量。推荐使用 let 和 const，var 用法不再推荐。


## 实例


```javascript
let age: number = 25;
const pi: number = 3.14;
```


## 3. 函数声明（Function Declarations）


函数声明：TypeScript 允许声明带有类型注解的函数，包括参数类型和返回值类型。


## 实例


```javascript
function greet(name: string): string {
    return "Hello, " + name;
}
```


**箭头函数：**TypeScript 同样支持 ES6 的箭头函数，使用简洁的语法来声明函数。


## 实例


```javascript
const greet = (name: string): string => "Hello, " + name;
```


## 4. 类声明（Class Declarations）


TypeScript 提供对面向对象编程的支持，允许定义类和类的方法、属性。


## 实例


```javascript
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
    }

    greet() {
    return `Hello, my name is ${this.name}`;
    }
}
```


## 5. 接口与类型别名（Interfaces & Type Aliases）


接口（Interface）：用于描述对象的形状，接口可以继承和扩展。


## 实例


```javascript
interface Animal {
    name: string;
    sound: string;
    makeSound(): void;
}
```


**类型别名（Type Alias）：**允许为对象类型、联合类型、交叉类型等定义别名。


## 实例


```javascript
type ID = string | number;
```


---

## 6. 模块和导入导出（Modules & Imports/Exports）


TypeScript 支持模块化编程，可以使用 import 和 export 来组织代码。


** 导出：**


## 实例


```javascript
export class Person {
    constructor(public name: string) {}
}
```


**导入：**


## 实例


```javascript
import { Person } from './person';
```


---

## 7. 类型断言（Type Assertions）


在某些情况下，TypeScript 无法推断出一个变量的准确类型，开发者可以使用类型断言来强制指定类型。


## 实例


```javascript
let value: any = "hello";
let strLength: number = (value as string).length;
```


---

## 8. 泛型（Generics）

泛型允许在定义函数、接口或类时不指定具体类型，而是使用占位符，让用户在使用时传入具体类型。泛型能够增加代码的复用性和类型安全性。


## 实例


```javascript
function identity<T>(arg: T): T {
    return arg;
}
```


---

## 9. 注释（Comments）

注释在 TypeScript 程序中用于解释代码的作用、思路等，增加代码的可读性。


**单行注释：**


## 实例


```javascript
// 这是一个单行注释
```


**多行注释：**


## 实例


```javascript
/* 这是一个
    多行注释 */
```


---

## 10. 类型推断（Type Inference）


TypeScript 在某些情况下会自动推断变量的类型。例如，在声明变量并赋值时，TypeScript 会推断出该变量的类型。


## 实例


```javascript
let num = 10;  // TypeScript 推断 num 为 number 类型
```


---

## 11. 类型守卫（Type Guards）


TypeScript 提供了类型守卫（如 typeof 和 instanceof），用于在运行时缩小变量的类型范围。


## 实例


```javascript
function isString(value: any): value is string {
    return typeof value === 'string';
}
```


---

## 12. 异步编程（Asynchronous Programming）


TypeScript 完全支持异步编程，可以使用 async/await 语法来处理异步操作。


## 实例


```javascript
async function fetchData(): Promise<string> {
    const response = await fetch("https://example.com");
    const data = await response.text();
    return data;
}
```


---

## 13. 错误处理（Error Handling）


TypeScript 允许使用 try/catch 块进行错误处理，还可以使用类型来描述错误的类型。


## 实例


```javascript
try {
    throw new Error("Something went wrong");
} catch (error) {
    if (error instanceof Error) {
        console.error(error.message);
    }
}
```









	  AI 思考中...





			** [TypeScript 特性](https://www.runoob.com/ts-features.html)
			[TypeScript vs JavaScript 对比](https://www.runoob.com/typescript-vs-javascript.html) **













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