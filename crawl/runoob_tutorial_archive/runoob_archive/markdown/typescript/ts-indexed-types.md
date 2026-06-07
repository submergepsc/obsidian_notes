# TypeScript 索引类型与 keyof 关键字

- Source: https://www.runoob.com/typescript/ts-indexed-types.html

索引类型和 keyof 是 TypeScript 中操作对象类型的强大工具。


它们允许我们动态地访问对象的属性，并创建灵活的类型映射。


---






  索引类型与 keyof 工作原理



  keyof 操作符

    type Keys = keyof User
    // "id" | "name" | "email"




索引访问类型 type Value = User["name"] // string 映射类型 type Partial {[P in keyof T]?: T[P]} 索引类型应用场景 动态属性访问 类型安全的对象操作 创建通用工具类型 --- ## 为什么需要索引类型 在 JavaScript 中，我们经常需要动态访问对象的属性。


例如，一个函数可能需要获取对象的所有键，或者根据键访问对应的值类型。


索引类型和 keyof 让我们能够在类型系统中表达这种动态性，同时保持类型安全。


**
概念：**索引类型是一类允许动态访问对象属性的类型，keyof 用于获取对象类型的所有键组成的联合类型。


---


## keyof 操作符


keyof 操作符用于获取对象类型的所有键组成的联合类型。


## 实例


```javascript
// 定义用户类型
interface User {
    id: number;       // 用户ID
    name: string;     // 用户名
    email: string;    // 邮箱
    age?: number;     // 年龄（可选）
}

// 使用 keyof 获取所有键的联合类型
// 结果: "id" | "name" | "email" | "age"
type UserKeys = keyof User;

// 测试 keyof
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

const user: User = {
    id: 1,
    name: "Alice",
    email: "[email protected]"
};

// 获取 name 属性
const userName: string = getProperty(user, "name");
console.log("用户名: " + userName);
```


**运行结果：**


```
用户名: Alice
```


**
说明：**keyof 返回的是键名的字面量联合类型，而不是字符串类型。


---


## 索引访问类型


使用索引访问类型（Index Access Type）可以获取对象属性的类型。


## 实例


```javascript
// 定义用户类型
interface User {
    id: number;
    name: string;
    email: string;
}

// 使用索引访问类型获取属性类型
type UserId = User["id"];      // number
type UserName = User["name"];  // string

// 可以使用联合类型进行多个键的访问
type UserIdAndName = User["id" | "name"];  // number | string

// 使用 keyof 获取所有属性类型的联合
type AllUserValues = User[keyof User];  // number | string

// 实际使用示例
function getValue<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

const user: User = { id: 1, name: "Bob", email: "[email protected]" };

// 获取 id 类型
const idValue: number = getValue(user, "id");
console.log("ID: " + idValue);

// 获取 name 类型
const nameValue: string = getValue(user, "name");
console.log("Name: " + nameValue);
```


**
索引访问：**使用方括号 [] 可以访问对象类型的具体属性类型，非常强大且灵活。


---


## 映射类型基础


映射类型允许基于现有类型创建新类型，遍历其所有键。


## 实例


```javascript
// 定义用户类型
interface User {
    id: number;
    name: string;
    email: string;
    age: number;
}

// 将所有属性变为可选
type PartialUser = Partial<User>;

// 将所有属性变为只读
type ReadonlyUser = Readonly<User>;

// 自定义映射类型：将所有属性变为可选且字符串化
type Stringify<T> = {
    [P in keyof T]: string;
};

type StringifiedUser = Stringify<User>;

// 实际使用示例
const partialUser: PartialUser = {
    id: 1,
    name: "Alice"
    // email 和 age 可选
};

const readonlyUser: ReadonlyUser = {
    id: 1,
    name: "Bob",
    email: "[email protected]",
    age: 25
};
// readonlyUser.name = "Charlie"; // 错误：只读

console.log("部分用户: " + partialUser.name);
console.log("只读用户: " + readonlyUser.name);
```


**
映射类型：**使用 [P in keyof T] 语法遍历类型的所有键，是创建工具类型的基础。


---


## 约束键的类型


使用 keyof 和泛型约束来限制函数接受的键。


## 实例


```javascript
// 定义配置类型
interface Config {
    apiUrl: string;
    timeout: number;
    retry: boolean;
}

// 只能获取存在的键
function getConfigValue<T, K extends keyof T>(
    config: T,
    key: K
): T[K] {
    return config[key];
}

// 定义配置
const config: Config = {
    apiUrl: "https://api.example.com",
    timeout: 5000,
    retry: true
};

// 正确：键存在
const url: string = getConfigValue(config, "apiUrl");
const timeoutVal: number = getConfigValue(config, "timeout");

// 错误：键不存在（TypeScript 会报错）
// const invalid = getConfigValue(config, "unknown");

console.log("API URL: " + url);
console.log("Timeout: " + timeoutVal);
```


**
约束：**K extends keyof T 确保传入的键一定是对象上存在的键，防止运行时错误。


---


## 只获取特定类型的属性


从对象类型中提取特定类型的属性键。


## 实例


```javascript
// 定义混合类型
interface Mixed {
    id: number;
    name: string;
    age: number;
    email: string;
    active: boolean;
}

// 提取所有字符串类型的键
type StringKeys<T> = {
    [K in keyof T]: T[K] extends string ? K : never;
}[keyof T];

// 提取所有数字类型的键
type NumberKeys<T> = {
    [K in keyof T]: T[K] extends number ? K : never;
}[keyof T];

// 测试
type StringProps = StringKeys<Mixed>;  // "name" | "email"
type NumberProps = NumberKeys<Mixed>;  // "id" | "age"

// 实际应用：获取字符串属性的值
function getStringProps<T, K extends StringKeys<T>>(
    obj: T,
    keys: K[]
): T[K][] {
    return keys.map(key => obj[key]);
}

const mixed: Mixed = {
    id: 1,
    name: "Alice",
    age: 25,
    email: "[email protected]",
    active: true
};

const strings = getStringProps(mixed, ["name", "email"]);
console.log("字符串属性: " + strings.join(", "));
```


**
条件类型：**结合条件类型和映射类型，可以实现复杂的类型过滤和提取。


---


## 遍历数组类型


使用索引类型操作数组和元组。


## 实例


```javascript
// 定义元组类型
type Tuple = [string, number, boolean];

// 获取元组元素类型
type First = Tuple[0];   // string
type Second = Tuple[1];  // number
type Third = Tuple[2];   // boolean

// 使用 number 获取所有元素类型
type AllElements = Tuple[number];  // string | number | boolean

// 获取数组元素类型
type StringArray = string[];
type ArrayElement = StringArray[number];  // string

// 实际应用：函数重载
function getElement<T extends any[]>(
    arr: T,
    index: number
): T[indexof T] | undefined {
    return index < arr.length ? arr[index] : undefined;
}

const tuple: Tuple = ["hello", 123, true];
const arr: string[] = ["a", "b", "c"];

console.log("元组元素[0]: " + getElement(tuple, 0));
console.log("数组元素[1]: " + getElement(arr, 1));
```


**
元组索引：**元组可以使用数字索引，每个索引对应特定元素类型，这是数组做不到的。


---


## 注意事项


- **keyof 返回联合类型：**keyof 返回键名的字面量联合类型
- **索引访问安全：**确保访问的键存在于目标类型中
- **泛型约束：**使用 extends keyof 约束泛型参数
- **映射类型需要 in 关键字：**映射类型使用 [P in keyof T] 语法


**
最佳实践：**索引类型是创建通用工具类型的基石，熟练掌握可以大幅提升类型操作能力。


---


## 总结


索引类型和 keyof 是 TypeScript 类型系统的重要组成部分。


- **keyof：**获取对象类型的所有键
- **索引访问：**通过键获取属性类型
- **映射类型：**基于现有类型创建新类型
- **类型安全：**确保动态属性访问的类型安全


**
建议：**在需要操作对象属性时，优先使用索引类型来保持类型安全。








	  AI 思考中...





			** [TypeScript infer 关键字](https://www.runoob.com/ts-infer.html)
			[TypeScript 递归类型](https://www.runoob.com/ts-recursive-types.html) **













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