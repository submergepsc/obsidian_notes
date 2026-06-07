# TypeScript type 别名

- Source: https://www.runoob.com/typescript/ts-type-alias.html

type 别名（Type Alias）用于为现有类型创建别名，让代码更简洁、更易读。


通过类型别名，可以为复杂类型定义一个简短的名字，提高代码的可维护性。


---






  type 别名工作原理



  原始复杂类型

    type User = {
    name: string;
    age: number;
    email: string;
    }




定义 type 别名 type UserID = User; // 或 type ID = string | number; 使用 代码中使用 var id: UserID; var uid: ID; type 别名应用场景 基础类型别名 联合类型别名 函数类型别名 泛型类型别名 --- ## 为什么需要 type 别名 当代码中多次使用同一个复杂类型时，每次都写完整类型会很冗长。


type 别名可以为复杂类型定义一个简洁的名字，让代码更易读、更易维护。


特别是在使用联合类型、函数类型、元组等复杂类型时，type 别名非常有用。


**
概念说明：**type 别名使用 `type` 关键字定义，它只是为现有类型起了一个新名字，不会创建新的类型。


---


## 基本用法


使用 type 关键字为类型定义别名。


## 实例


```javascript
// 类型别名：为联合类型定义别名
// ID 可以是字符串或数字
type ID = string | number;

// 类型别名：为对象类型定义别名
// Point 表示一个坐标点
type Point = { x: number; y: number };

// 使用类型别名
var userId: ID = "123";
var productId: ID = 456;

// 使用 Point 类型别名
var point: Point = { x: 10, y: 20 };

console.log("用户ID: " + userId);
console.log("产品ID: " + productId);
console.log("坐标: " + JSON.stringify(point));
```


**运行结果：**


```
用户ID: 123
产品ID: 456
坐标: {"x":10,"y":20}
```


**
说明：**类型别名只是给类型起了个新名字，编译后不会产生实际代码，它完全用于开发时的类型检查。


---


## 接口 vs 类型别名


类型别名和接口非常相似，都可以用来定义对象类型，但有一些细微区别。


## 实例


```javascript
// 使用 type 别名定义对象类型
// type 可以定义任何类型，不仅仅是对象
type PersonType = {
    name: string;
    age: number;
};

// 使用接口定义对象类型
// 接口可以声明合并，可以被类实现
interface PersonInterface {
    name: string;
    age: number;
}

// 两者都可以用来声明变量类型
var person1: PersonType = { name: "Alice", age: 25 };
var person2: PersonInterface = { name: "Bob", age: 30 };

console.log("PersonType: " + JSON.stringify(person1));
console.log("PersonInterface: " + JSON.stringify(person2));
```


**
区别：**type 可以定义任何类型（联合类型、元组、函数类型等），而接口主要用于定义对象类型。接口支持声明合并，type 不支持。


---


## 类型别名与联合类型


类型别名非常适合定义联合类型，让代码更清晰。


## 实例


```javascript
// 联合类型别名：定义状态的可能值
// Status 只能是这三个字符串字面量之一
type Status = "pending" | "success" | "error";

// 联合类型别名：定义多种可能的返回类型
// Result 可以是字符串、数字或布尔值
type Result = string | number | boolean;

// 使用联合类型别名
function getStatus(status: Status): void {
    console.log("状态: " + status);
}

getStatus("success");
getStatus("error");

// 使用 Result 类型
var result: Result = "hello";
result = 42;
console.log("结果: " + result);
```


**运行结果：**


```
状态: success
状态: error
结果: 42
```


**
应用场景：**联合类型别名常用于定义状态码、错误类型、API 返回值等场景。


---


## 类型别名与元组


类型别名也可以用于定义元组类型。


## 实例


```javascript
// 元组类型别名：定义坐标
// Coordinate 是一个包含两个数字的元组
type Coordinate = [number, number];

// 元组类型别名：定义姓名和年龄
// NameAge 是一个字符串和数字的元组
type NameAge = [string, number];

// 使用元组类型别名
var coord: Coordinate = [10, 20];
var person: NameAge = ["Alice", 25];

console.log("坐标: " + coord);
console.log("信息: " + person[0] + ", " + person[1]);
```


**
说明：**元组类型别名让元组的使用更加清晰，避免了每次都需要写出完整元组类型的问题。


---


## 类型别名与函数


类型别名可以简化函数类型的声明。


## 实例


```javascript
// 函数类型别名：定义回调函数类型
// Callback 接受一个字符串参数，返回 void
type Callback = (result: string) => void;

// 函数类型别名：定义数学运算函数类型
// MathOperation 接受两个数字参数，返回数字
type MathOperation = (a: number, b: number) => number;

// 使用函数类型别名
var add: MathOperation = function(a, b) { return a + b; };
var multiply: MathOperation = function(a, b) { return a * b; };

console.log("加法: " + add(2, 3));
console.log("乘法: " + multiply(4, 5));
```


**运行结果：**


```
加法: 5
乘法: 20
```


**
优势：**函数类型别名让函数类型声明更简洁，特别是在需要多次使用相同函数签名时。


---


## 类型别名与泛型


类型别名可以配合泛型使用，创建可复用的类型定义。


## 实例


```javascript
// 泛型类型别名：定义结果类型
// Result<T> 是一个泛型类型，T 是成功时的数据类型
type Result<T> = { success: boolean; data?: T; error?: string };

// 泛型类型别名：定义键值对类型
// Pair<K, V> 有两个类型参数
type Pair<K, V> = { key: K; value: V };

// 使用泛型类型别名
var result: Result<string> = { success: true, data: "Hello" };
var pair: Pair<string, number> = { key: "age", value: 25 };

console.log("结果: " + JSON.stringify(result));
console.log("键值对: " + JSON.stringify(pair));
```


**运行结果：**


```
结果: {"success":true,"data":"Hello"}
键值对: {"key":"age","value":25}
```


**
泛型优势：**泛型类型别名可以适应不同的数据类型，提高代码的复用性。


---


## 类型别名与映射类型


类型别名可以与映射类型结合，创建强大的类型转换。


## 实例


```javascript
// 映射类型：将所有属性变为只读
// Readonly<T> 遍历 T 的所有属性并添加 readonly
type Readonly<T> = { readonly [P in keyof T]: T[P] };

// 映射类型：将所有属性变为可选
// Partial<T> 遍历 T 的所有属性并添加 ?
type Partial<T> = { [P in keyof T]?: T[P] };

// 定义用户接口
interface User {
    name: string;
    age: number;
}

// 使用映射类型别名
var readonlyUser: Readonly<User> = { name: "Alice", age: 25 };
// readonlyUser.name = "Bob"; // 错误：只读属性不能修改

var partialUser: Partial<User> = { name: "Bob" };

console.log("只读用户: " + JSON.stringify(readonlyUser));
console.log("部分用户: " + JSON.stringify(partialUser));
```


**
提示：**映射类型是 TypeScript 非常强大的特性，可以基于现有类型创建新的类型变化。


---


## 注意事项


- **不能重复定义：**同一个 type 别名不能重复定义（接口可以声明合并）
- **仅编译时有效：**type 别名在编译后不产生任何代码
- **可读性优先：**不要滥用类型别名，简洁明了的代码更好


**
最佳实践：**当类型需要复用，或者类型名称过长时使用 type 别名。对于简单的对象类型，可以根据团队习惯选择 type 或接口。


---


## 总结


type 别名是 TypeScript 中非常有用的特性。


- **基本用法：**使用 type 关键字为复杂类型定义别名
- **联合类型：**定义多个可能类型的组合
- **函数类型：**简化函数类型声明
- **泛型：**创建可复用的泛型类型
- **映射类型：**基于现有类型创建新类型


**
建议：**合理使用 type 别名可以让代码更清晰，但不要过度使用，保持代码简洁易读最重要。








	  AI 思考中...





			** [TypeScript Promise 详解](https://www.runoob.com/ts-promise.html)
			[TypeScript 字面量类型](https://www.runoob.com/ts-literal-types.html) **













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