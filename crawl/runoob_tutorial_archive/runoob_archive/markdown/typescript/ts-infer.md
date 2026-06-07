# TypeScript infer 关键字

- Source: https://www.runoob.com/typescript/ts-infer.html

infer 是 TypeScript 条件类型中的关键字，用于从类型中推断出新的类型。


它允许在泛型条件类型中提取和推导类型，实现强大的类型操作。


---






  infer 关键字工作原理



  原始类型

    type Promise<T> = {
    value: T
    }




infer 推导 提取出的类型 type ValueOf = T extends Promise ? V : never 示例 ValueOf> → string infer 常见应用场景 提取 Promise 值类型 提取数组元素类型 提取函数返回类型 --- ## 为什么需要 infer 关键字 在泛型编程中，我们经常需要从复杂的类型中提取出部分类型。


例如，从 `Promise` 中提取 `string`，从 `Array` 中提取 `User`。


infer 关键字让这种类型提取变得优雅和类型安全，它可以在条件类型中声明一个类型变量，然后在 true 分支中使用。


**
概念说明：**infer 是 "infer" 的缩写，意为"推断"。它只能在条件类型的 extends 子句中使用，用于声明一个待推断的类型变量。


---


## 基本用法


在条件类型中使用 infer 推断类型。


## 实例


```javascript
// 从 Promise 中提取值类型
// 如果 T 是 Promise<V>，则返回 V；否则返回 never
type ValueOf<T> = T extends Promise<infer V> ? V : never;

// 测试
type Str = ValueOf<Promise<string>>;  // string
type Num = ValueOf<Promise<number>>; // number
type NotPrm = ValueOf<string>;        // never

// 使用示例
var promise: Promise<string> = Promise.resolve("hello");
var value: ValueOf<typeof promise> = "world";

console.log("字符串提取: " + (typeof value === "string" ? "成功" : "失败"));
```


**运行结果：**


```
字符串提取: 成功
```


**
说明：**`infer V` 声明了一个类型变量 V，TypeScript 会自动推断 V 的类型。


---


## 提取数组元素类型


从数组类型中提取元素类型。


## 实例


```javascript
// 提取数组的元素类型
// 如果 T 是数组 V[]，则返回 V
type ArrayElement<T> = T extends (infer V)[] ? V : never;

// 测试
type User = { name: string };
type Users = User[];

type E1 = ArrayElement<string[]>;   // string
type E2 = ArrayElement<Users>;       // User
type E3 = ArrayElement<number>;       // never（非数组）

// 使用示例
var users: Users = [{ name: "Alice" }];
var element: ArrayElement<Users> = users[0];

console.log("元素类型: " + element.name);
```


**
应用：**这种模式常用于从联合类型中提取特定类型的元素。


---


## 提取函数返回类型


从函数类型中提取返回类型。


## 实例


```javascript
// 提取函数的返回类型
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

// 测试
function getData() {
    return { id: 1, name: "Alice" };
}
function fetchUser(id: number): Promise<User> {
    return Promise.resolve({ id, name: "Bob" });
}

type R1 = ReturnType<typeof getData>;  // { id: number; name: string }
type R2 = ReturnType<typeof fetchUser>; // Promise<User>

// 使用示例
var result: R1 = { id: 1, name: "Test" };
console.log("返回类型: " + JSON.stringify(result));
```


**
内置类型：**TypeScript 内置的 `ReturnType` 工具类型就是使用 infer 实现的。


---


## 提取函数参数类型


从函数类型中提取参数类型。


实例


```javascript
// 提取函数的第一参数类型
type FirstParameter<T> = T extends (first: infer P, ...rest: any[]) => any ? P : never;

// 测试
function createUser(name: string, age: number): User {
    return { id: 1, name };
}
function logMessage(msg: string): void {
    console.log(msg);
}

type P1 = FirstParameter<typeof createUser>; // string
type P2 = FirstParameter<typeof logMessage>;  // string
type P3 = FirstParameter<() => void>;          // never

// 使用示例
var nameParam: P1 = "Alice";
console.log("参数类型: " + nameParam);
```


**
注意：**可以使用 `...rest: any[]` 来匹配任意数量的剩余参数。


---


## 多个 infer


在一个条件类型中使用多个 infer。


## 实例


```javascript
// 提取元组的前两个元素类型
type FirstTwo<T> = T extends [infer A, infer B, ...rest: any[]] ? [A, B] : never;

// 测试
type Tuple = [string, number, boolean];
type FirstTwoTypes = FirstTwo<Tuple>; // [string, number]

// 提取对象属性
type ObjectValue<T> = T extends { value: infer V } ? V : never;

type WithValue = { value: string; name: string };
type ExtractedValue = ObjectValue<WithValue>; // string

// 使用示例
var tupleResult: FirstTwoTypes = ["hello", 123];
console.log("元组: " + JSON.stringify(tupleResult));
```


**
元组：**使用 `...rest: any[]` 可以匹配元组的剩余元素。


---


## 在递归类型中使用 infer


在递归类型工具中使用 infer 实现复杂类型操作。


## 实例


```javascript
// 深度只读类型 - 递归应用 infer
type DeepReadonly<T> = T extends Function
    ? T
    : T extends object
        ? { readonly [P in keyof T]: DeepReadonly<T[P]> }
        : T;

// 测试
interface User {
    name: string;
    address: {
        city: string;
        zip: string;
    };
}

type ReadonlyUser = DeepReadonly<User>;

// 扁平化 Promise 类型
type FlattenPromise<T> = T extends Promise<infer U>
    ? U extends Promise<any>
        ? FlattenPromise<U>
        : U
    : T;

type Nested = Promise<Promise<string>>;
type Flat = FlattenPromise<Nested>; // string

// 使用示例
var user: ReadonlyUser = {
    name: "Alice",
    address: { city: "Beijing", zip: "100000" }
};
// user.name = "Bob"; // 错误：只读
console.log("深度只读: " + user.name);
```


**
递归 infer：**在递归类型中使用 infer 可以实现深度类型转换，如深度只读、深度可选等。


---


## 注意事项


- **只能用在 extends 右侧：**infer 只能在条件类型的 extends 子句中使用
- **声明类型变量：**使用 `infer V` 声明待推断的类型变量
- **可以多个使用：**一个条件类型中可以使用多个 infer
- **推断失败返回 never：**如果推断失败，条件类型返回 never


**
最佳实践：**infer 是实现自定义工具类型的核心，掌握它可以实现强大的类型操作。


---


## 总结


infer 是 TypeScript 类型系统中最强大的特性之一。


- **类型提取：**从复杂类型中提取部分类型
- **条件推断：**在条件类型中推断类型
- **函数相关：**提取函数参数、返回类型
- **递归工具：**实现深度类型转换


**
建议：**深入理解 infer 可以让你编写更高级的类型工具，提升类型安全性和开发效率。









	  AI 思考中...





			** [TypeScript 单元测试](https://www.runoob.com/ts-unit-testing.html)
			[TypeScript 索引类型与 keyof 关键字](https://www.runoob.com/ts-indexed-types.html) **













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