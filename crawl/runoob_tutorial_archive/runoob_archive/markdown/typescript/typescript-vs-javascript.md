# TypeScript vs JavaScript 对比

- Source: https://www.runoob.com/typescript/typescript-vs-javascript.html

TypeScript 和 JavaScript 是前端开发中两个最重要的语言，理解它们之间的区别对于现代 Web 开发至关重要。


JavaScript 是 Web 的原生脚本语言，而 TypeScript 是 JavaScript 的超集，添加了类型系统和其他高级特性。


![](https://www.runoob.com/wp-content/uploads/2026/04/235fbd76-a3e2-438b-8c84-02a2cfc83704.png)


---


## 核心区别


| 特性 | JavaScript | TypeScript |
| --- | --- | --- |
| 类型系统 | 动态类型 | 静态类型（可选） |
| 编译 | 解释执行 | 编译为 JavaScript |
| 开发时类型检查 | 无 | 有 |
| IDE 支持 | 基础 | 强大的智能提示 |
| 代码重构 | 困难 | 安全简单 |






  TypeScript 是 JavaScript 的超集



  JavaScript
  动态类型
  解释执行
  无需编译



  TypeScript
  静态类型（可选）
  编译为 JS
  类型检查
  智能提示



包含关系 所有 JS 代码 都是有效 TS --- ## 类型系统对比 JavaScript 是动态类型语言，变量类型在运行时确定：


## JavaScript 动态类型


```javascript
// JavaScript - 变量类型可以随时改变
var message = "Hello";
message = 123;           // 合法，不会报错
message = true;          // 仍然合法

// 运行前不知道变量类型
function greet(name) {
    return "Hello, " + name;
}
```


TypeScript 是静态类型语言，在编译时检查类型：


## TypeScript 静态类型


```javascript
// TypeScript - 声明时指定类型
var message: string = "Hello";
// message = 123;    // 编译错误：Type 'number' is not assignable to type 'string'

// 函数参数和返回值类型明确
function greet(name: string): string {
    return "Hello, " + name;
}

// 类型错误会在编译时发现
greet(123);  // 编译错误：Argument of type 'number' is not assignable to parameter of type 'string'
```


---


## 编译过程


TypeScript 需要编译为 JavaScript 才能在浏览器中运行：


## TypeScript 源码


```javascript
// app.ts - TypeScript 源码
interface User {
    name: string;
    age: number;
}

function createUser(name: string, age: number): User {
    return { name, age };
}

var user = createUser("Alice", 25);
console.log(user);
```


编译后的 JavaScript：


## 编译后的 JavaScript


```javascript
// app.js - 编译后的 JavaScript
function createUser(name, age) {
    return { name: name, age: age };
}

var user = createUser("Alice", 25);
console.log(user);
```


---


## 类型推断


TypeScript 具有强大的类型推断能力，即使不显式声明类型：


## 类型推断


```javascript
// TypeScript 自动推断类型
var num = 10;          // 推断为 number
var str = "hello";    // 推断为 string
var isActive = true;  // 推断为 boolean

// 函数返回值类型也会推断
function add(a, b) {
    return a + b;     // 推断返回值为 number
}

var result = add(1, 2);  // result 类型为 number
```


---


## 开发体验对比


### 智能提示


TypeScript 为 IDE 提供丰富的类型信息，实现智能提示：


```
// 在 TypeScript 中，IDE 知道 user 对象有 name 和 age 属性
user.    // 自动提示 .name 和 .age

// JavaScript 中 IDE 无法确定类型，提示有限
user.    // 可能没有有用的提示
```


### 重构支持


TypeScript 使得代码重构更安全：


- 重命名变量/函数时，所有引用自动更新
- 修改函数签名时，调用处会显示错误
- 提取代码时，类型自动保持


---


## 选择 TypeScript 的理由

**
为什么选择 TypeScript：


- 编译时错误检测，提前发现 bug
- 更好的代码可读性和可维护性
- 强大的 IDE 智能提示
- 安全的重构
- 现代前端框架的标配（React、Vue、Angular）


TypeScript 是 JavaScript 的超集，它在保持 JavaScript 灵活性的同时，增加了类型系统来提高代码质量。对于大型项目，TypeScript 的优势更加明显。









	  AI 思考中...





			** [TypeScript 基本结构](https://www.runoob.com/typescript-basic-structure.html)
			[TypeScript tsconfig.json 配置](https://www.runoob.com/ts-tsconfig.html) **













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