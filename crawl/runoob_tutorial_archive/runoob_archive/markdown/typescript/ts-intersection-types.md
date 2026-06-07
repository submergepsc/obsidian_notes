# TypeScript 交叉类型

- Source: https://www.runoob.com/typescript/ts-intersection-types.html

交叉类型（Intersection Types）将多个类型合并成一个新类型，新类型包含所有成员的类型。


这类似于面向对象中的多重继承，让一个类型可以拥有多个类型的特性。


---






  交叉类型工作原理



  类型 A (Person)

    name: string
    age: number



  &



  类型 B (Worker)

    company: string
    salary: number




合并 A & B (Employee) name: string age: number company: string salary: number 交叉类型使用场景 类型组合 合并多个类型特性 Mixin 模式 组合多个类的功能 替代接口继承 更简洁的类型组合 --- ## 为什么需要交叉类型 在开发中，一个类型往往需要拥有多个类型的特性。


例如，一个员工既是一个人（Person），也是一个工作者（Worker），需要同时具有两者的属性。


交叉类型让我们可以将多个类型合并成一个，满足这种需求。


**
概念说明：**交叉类型使用 `&` 符号连接多个类型，表示新类型包含所有类型的成员。这类似于多重继承的概念。


---


## 基本语法


使用 `&` 符号组合多个类型。


## 实例


```javascript
// 定义人员类型
// 包含姓名和年龄
interface Person {
    name: string;
    age: number;
}

// 定义工作者类型
// 包含公司名称和薪资
interface Worker {
    company: string;
    salary: number;
}

// 使用交叉类型合并两个接口
// Employee 类型同时具有 Person 和 Worker 的所有属性
type Employee = Person & Worker;

// 创建同时具有两个类型特性的对象
var employee: Employee = {
    name: "Alice",
    age: 25,
    company: "Google",
    salary: 100000
};

console.log("员工: " + JSON.stringify(employee));
```


**运行结果：**


```
员工: {"name":"Alice","age":25,"company":"Google","salary":100000}
```


**
说明：**交叉类型 `A & B` 意味着新类型同时具有 A 和 B 的所有属性，缺一不可。


---


## 交叉类型与接口继承


交叉类型可以替代接口的多重继承。


## 实例


```javascript
// 定义类型 A
interface A {
    a: string;
}

// 定义类型 B
interface B {
    b: number;
}

// 使用接口继承多个接口
// 需要使用 extends 继承多个接口
interface AB extends A, B {
    c: boolean;
}

// 使用交叉类型（更简洁）
// 直接使用 & 符号组合类型
type ABType = A & B & { c: boolean };

// 两种方式都能创建包含所有属性的类型
var obj: ABType = { a: "hello", b: 42, c: true };
console.log("对象: " + JSON.stringify(obj));
```


**运行结果：**


```
对象: {"a":"hello","b":42,"c":true}
```


**
对比：**交叉类型比接口继承更简洁，特别是当需要继承多个类型且需要添加额外属性时。


---


## 类型混合（Mixin 模式）


使用交叉类型实现 Mixin 模式，可以动态组合类的功能。


## 实例


```javascript
// 定义构造函数类型
// 接受任意参数，返回一个对象
type Constructor = new (...args: any[]) => {};

// Mixin：添加时间戳功能
// 返回一个扩展了 Base 的新类
function Timestamped<T extends Constructor>(Base: T) {
    return class extends Base {
        timestamp = Date.now();
    };
}

// Mixin：添加序列化功能
// 返回一个扩展了 Base 的新类，包含 serialize 方法
function Serializable<T extends Constructor>(Base: T) {
    return class extends Base {
        serialize() {
            return JSON.stringify(this);
        }
    };
}

// 基础用户类
class User {
    name: string;
    constructor(name: string) {
        this.name = name;
    }
}

// 组合 Mixin
// 创建具有时间戳功能的用户类
var TimestampedUser = Timestamped(User);
// 创建具有序列化功能的用户类
var SerializableUser = Serializable(User);
// 组合两个 Mixin
var FullUser = Serializable(Timestamped(User));

// 创建实例并测试
var user = new FullUser("Alice");
console.log("时间戳: " + user.timestamp);
console.log("序列化: " + user.serialize());
```


**运行结果：**


```
时间戳: 17134...
序列化: {"name":"Alice","timestamp":17134...}
```


**
Mixin 模式：**这是一种强大的模式，可以在不修改原有类的情况下为其添加新功能。


---


## 交叉类型与联合类型


交叉类型和联合类型结合时需要特别注意优先级。


## 实例


```javascript
// 联合类型：可以是字符串或数字
type StringOrNumber = string | number;

// 交叉类型：不兼容类型的交叉
// string & number = never（没有类型同时是字符串和数字）
type Both = string & number;

// 定义三个类型
type A = { a: string };
type B = { b: number };
type C = { c: boolean };

// 联合类型与交叉类型结合
// (A | B) & C 会将联合类型的每个分支都与 C 交叉
type Combined = (A | B) & C;

// 实际结果是：{ a: string; c: boolean } | { b: number; c: boolean }
// 即要么是 A + C，要么是 B + C
var obj: Combined = { a: "hello", c: true };
console.log("组合: " + JSON.stringify(obj));
```


**运行结果：**


```
组合: {"a":"hello","c":true}
```


**
重要：**不兼容的类型进行交叉会得到 `never` 类型。例如 `string & number` 是无效的。


---


## 实用交叉类型


交叉类型常用于创建工具类型，实现类型的转换。


## 实例


```javascript
// 映射类型：将所有属性变为可选
// 遍历 T 的所有属性，添加 ? 使其可选
type Partial<T> = { [P in keyof T]?: T[P] };

// 映射类型：将所有属性变为必填
// 遍历 T 的所有属性，移除 ? 使其必填
type Required<T> = { [P in keyof T]-?: T[P] };

// 映射类型：将所有属性变为只读
// 遍历 T 的所有属性，添加 readonly
type Readonly<T> = { readonly [P in keyof T]: T[P] };

// 定义配置接口
interface Config {
    host: string;
    port: number;
}

// 使用工具类型
var partialConfig: Partial<Config> = { host: "localhost" };
var requiredConfig: Required<Config> = { host: "localhost", port: 8080 };
var readonlyConfig: Readonly<Config> = { host: "localhost", port: 8080 };

console.log("部分: " + JSON.stringify(partialConfig));
console.log("必填: " + JSON.stringify(requiredConfig));
console.log("只读: " + JSON.stringify(readonlyConfig));
```


**运行结果：**


```
部分: {"host":"localhost"}
必填: {"host":"localhost","port":8080}
只读: {"host":"localhost","port":8080}
```


**
工具类型：**TypeScript 标准库中提供了许多基于交叉类型和映射类型的工具类型，如 Partial、Required、Readonly 等。


---


## 注意事项


- **不兼容类型：**交叉不兼容的类型会得到 never
- **优先级：**联合类型的优先级高于交叉类型
- **方法冲突：**如果两个类型有同名的方法，需要手动处理冲突


**
最佳实践：**交叉类型适合组合多个接口或类型，当需要多重继承时，优先使用交叉类型而非接口继承。


---


## 总结


交叉类型是 TypeScript 中强大的类型组合工具。


- **语法：**使用 `&` 符号连接多个类型
- **合并：**新类型包含所有类型的成员
- **Mixin：**可以用于实现类的功能组合
- **never：**不兼容类型交叉会得到 never 类型


**
建议：**合理使用交叉类型可以创建灵活的类型组合，但要注意避免不必要类型交叉导致的 never 类型。


---









	  AI 思考中...





			** [TypeScript 错误处理](https://www.runoob.com/ts-error-handling.html)
			[TypeScript 模板字面量类型](https://www.runoob.com/ts-template-literal.html) **













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