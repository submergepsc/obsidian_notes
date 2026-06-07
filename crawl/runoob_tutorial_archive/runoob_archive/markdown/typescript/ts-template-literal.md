# TypeScript 模板字面量类型

- Source: https://www.runoob.com/typescript/ts-template-literal.html

模板字面量类型基于字符串字面量类型构建，支持通过插值生成新的字符串类型。


这让 TypeScript 能够对字符串进行更精确的类型检查，适用于事件名、路径、类名等场景。


---






  模板字面量类型工作原理



  输入类型

    type Event = "click" | "focus"
    type Method = "get" | "post"




模板 模板字面量类型 type Name = `on${Capitalize}` type Path = `${Method}:/${string}` 输出类型 "onClick" "onFocus" "get:/..." 内置工具类型 Uppercase "hello" → "HELLO" Lowercase "HELLO" → "hello" Capitalize "hello" → "Hello" Uncapitalize "Hello" → "hello" --- ## 为什么需要模板字面量类型 在开发中，我们经常需要处理格式化的字符串，如事件名（onClick）、API 路径（get:/users）、CSS 类名（btn-primary-md）等。


使用普通的 string 类型无法精确描述这些格式，而模板字面量类型让我们可以精确地定义这些字符串的类型。


这大大增强了 TypeScript 的类型安全性，减少了运行时错误。


**
概念说明：**模板字面量类型使用反引号（`` ` ``）和 `${}` 插值语法来定义字符串类型，类似于 JavaScript 的模板字符串，但用在类型层面。


---


## 基本语法


模板字面量类型使用反引号和插值来定义类型。


## 实例


```javascript
// 定义基础字符串字面量类型
type World = "world";

// 使用模板字面量类型
// `Hello ${World}` 相当于 "Hello world"
type Greeting = `Hello ${World}`;

// 只能赋值符合类型定义的字符串
var greeting: Greeting = "Hello world";
console.log("问候: " + greeting);
```


**运行结果：**


```
问候: Hello world
```


**
说明：**模板字面量类型会将插值的位置替换为实际的字符串，生成新的字面量类型。


---


## 内置工具类型


TypeScript 提供了四个内置的工具类型来处理字符串大小写。


## 实例


```javascript
// Uppercase：将字符串转为大写
type UpperHello = Uppercase<"hello">;  // "HELLO"

// Lowercase：将字符串转为小写
type LowerHELLO = Lowercase<"HELLO">;  // "hello"

// Capitalize：将字符串首字母大写
type CapitalizedHello = Capitalize<"hello">;  // "Hello"

// Uncapitalize：将字符串首字母小写
type UncapitalizedHello = Uncapitalize<"Hello">;  // "hello"

console.log("Uppercase: " + UpperHello);
console.log("Lowercase: " + LowerHELLO);
console.log("Capitalize: " + CapitalizedHello);
console.log("Uncapitalize: " + UncapitalizedHello);
```


**运行结果：**


```
Uppercase: HELLO
Lowercase: hello
Capitalize: Hello
Uncapitalize: hello
```


**
应用场景：**这些工具类型在处理事件名、方法名等需要统一格式的场景非常有用。


---


## 事件类型


使用模板字面量类型可以精确地定义事件名称的类型。


## 实例


```javascript
// 构建事件名类型
// `on${Capitalize<string>}` 生成以 "on" 开头，首字母大写的字符串
type EventName = `on${Capitalize<string>}`;
// `handle${Capitalize<string>}` 生成以 "handle" 开头，首字母大写的字符串
type Handler = `handle${Capitalize<string>}`;

// 只能赋值符合格式的字符串
var clickEvent: EventName = "onClick";
var focusEvent: EventName = "onFocus";
var handler: Handler = "handleSubmit";

console.log("事件: " + clickEvent);
console.log("处理器: " + handler);
```


**运行结果：**


```
事件: onClick
处理器: handleSubmit
```


**
优势：**使用模板字面量类型后，像 "onclick"（小写）这样的错误格式会被 TypeScript 拒绝。


---


## 路径类型


使用模板字面量类型可以精确地定义 API 路径的类型。


## 实例


```javascript
// 定义 HTTP 方法类型
type HttpMethod = "get" | "post" | "put" | "delete";

// 定义路径格式
type ApiEndpoint = `/${string}`;  // 以斜杠开头的字符串

// 组合成完整的 API 路径类型
type ApiPath = `${HttpMethod}${ApiEndpoint}`;

// 只能赋值符合格式的路径
var getUsers: ApiPath = "/get/users";
var createUser: ApiPath = "/post/users";

console.log("路径: " + getUsers);
console.log("路径: " + createUser);
```


**运行结果：**


```
路径: /get/users
路径: /post/users
```


**
类型安全：**像 "/users"（没有方法前缀）这样的路径会被 TypeScript 报错。


---


## 复杂示例


模板字面量类型可以组合多个联合类型，生成所有可能的组合。


## 实例


```javascript
// 带数字的模板类型
// ${number} 匹配任意数字
type Row = `row${number}`;
type Row10 = Row;  // row0, row1, row2... 直到 row9...

// 组合多个类型
type Variant = "primary" | "secondary";
type Size = "sm" | "md" | "lg";
// 这会生成 6 种组合：btn-primary-sm, btn-primary-md, btn-primary-lg...
type ClassName = `btn-${Variant}-${Size}`;

// 只能赋值生成的 6 种组合之一
var className: ClassName = "btn-primary-md";
console.log("类名: " + className);
```


**运行结果：**


```
类名: btn-primary-md
```


**
组合爆炸：**模板字面量类型会自动展开所有组合。如果联合类型有很多选项，生成的类型可能会非常庞大。


---


## 自定义工具类型


可以创建自己的模板字面量工具类型。


## 实例


```javascript
// 添加前缀的工具类型
// T 是任意字符串，P 是要添加的前缀
type Prefix<T extends string, P extends string> = `${P}${Capitalize<T>}`;

// 添加后缀的工具类型
// T 是任意字符串，S 是要添加的后缀
type Suffix<T extends string, S extends string> = `${Capitalize<T>}${S}`;

// 使用自定义工具类型
type HandlerName = Prefix<"click", "on">;
type ButtonId = Suffix<"submit", "Btn">;

var handler: HandlerName = "onClick";
var id: ButtonId = "SubmitBtn";

console.log("处理器: " + handler);
console.log("ID: " + id);
```


**运行结果：**


```
处理器: onClick
ID: SubmitBtn
```


**
泛型模板：**模板字面量类型可以与泛型结合，创建可复用的工具类型。


---


## 注意事项


- **插值类型：**模板中的 `${}` 可以是具体字符串、联合类型、string、number 等
- **组合数量：**组合多个联合类型时，生成的类型可能非常大
- **大小写处理：**使用内置工具类型处理字符串大小写


**
最佳实践：**使用模板字面量类型处理事件名、路径、类名等有固定格式的字符串，可以获得更好的类型安全。


---


## 总结


模板字面量类型是 TypeScript 强大的类型系统的一部分。


- **模板语法：**使用 `${T}` 插值构建类型
- **内置工具：**Uppercase、Lowercase、Capitalize、Uncapitalize
- **应用场景：**事件名、API 路径、CSS 类名等
- **自定义：**创建可复用的工具类型


**
建议：**在需要格式化字符串的场景，优先使用模板字面量类型来获得编译期的类型检查。


---









	  AI 思考中...





			** [TypeScript 交叉类型](https://www.runoob.com/ts-intersection-types.html)
			[TypeScript 从 JavaScript 迁移](https://www.runoob.com/ts-migration.html) **













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