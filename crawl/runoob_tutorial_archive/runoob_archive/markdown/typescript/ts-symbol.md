# TypeScript Symbol

- Source: https://www.runoob.com/typescript/ts-symbol.html

Symbol 是 ES6 引入的原始数据类型，表示唯一的标识符。


在 TypeScript 中，Symbol 可以用作对象的属性键，确保属性的唯一性。


这在需要创建私有属性、避免属性名冲突等场景非常有用。


---






  Symbol 特性



  Symbol() 创建

    var sym1 = Symbol("key")
    var sym2 = Symbol("key")
    // sym1 !== sym2
    每次创建都唯一




用作对象属性键 var obj = { [sym]: "value" } // 唯一属性名 Symbol.for() 全局注册表 相同 key 相等 常见内置 Symbol Symbol.iterator - 迭代器 Symbol.toStringTag - 对象描述 Symbol.hasInstance - instanceof --- ## 为什么需要 Symbol 在 JavaScript 中，对象的属性名都是字符串，有时可能会发生冲突。


Symbol 提供了创建唯一标识符的方式，每次调用 Symbol() 都会创建一个新的、唯一的值。


这在需要创建私有属性、定义唯一常量、实现迭代器等场景非常有用。


**
概念说明：**Symbol 是 JavaScript 的原始数据类型之一，通过 Symbol() 函数创建。每个 Symbol 值都是唯一的，即使描述相同也不相等。


---


## 创建 Symbol


使用 Symbol() 函数创建唯一的 Symbol 值。


## 实例


```javascript
// 创建 Symbol，传入描述字符串（可选）
var sym1 = Symbol("description");
var sym2 = Symbol("description");

// 每次创建的 Symbol 都是唯一的，即使描述相同
console.log("sym1 === sym2: " + (sym1 === sym2));
console.log("sym1: " + sym1.toString());
```


**运行结果：**


```
sym1 === sym2: false
sym1: Symbol(description)
```


**
唯一性：**这是 Symbol 最重要的特性，每次调用 Symbol() 都会创建一个新值，与任何其他值都不相等。


---


## Symbol 作为对象属性


Symbol 可以用作对象的属性键，创建唯一的属性名。


## 实例


```javascript
// 创建 Symbol 作为属性键
var sym = Symbol("key");

// 使用 Symbol 作为对象的属性键
var obj = {
    name: "Alice",  // 普通字符串属性
    [sym]: "secret value"  // Symbol 属性，计算属性名
};

// 访问普通属性
console.log("普通属性: " + obj.name);
// 访问 Symbol 属性
console.log("Symbol 属性: " + obj[sym]);
// Symbol 属性不会出现在 JSON 中
console.log("对象: " + JSON.stringify(obj));
```


**运行结果：**


```
普通属性: Alice
Symbol 属性: secret value
对象: {"name":"Alice"}
```


**
隐私：**Symbol 属性不会出现在 JSON 序列化中，也不会被 for...in 遍历到，可以用来创建"私有"属性。


---


## 全局 Symbol 注册表


使用 Symbol.for() 访问全局注册表中的 Symbol，相同 key 会返回相同的 Symbol。


## 实例


```javascript
// 使用 Symbol.for 方法创建/获取全局 Symbol
// 如果 key 不存在，会创建新的；如果已存在，返回已有的
var globalSym1 = Symbol.for("global");
var globalSym2 = Symbol.for("global");

// 相同 key 的 Symbol 是相等的
console.log("全局 Symbol 相等: " + (globalSym1 === globalSym2));

// 获取 Symbol 的 key
console.log("Symbol key: " + Symbol.keyFor(globalSym1));
```


**运行结果：**


```
全局 Symbol 相等: true
Symbol key: global
```


**
区别：**Symbol() 每次创建新的值，Symbol.for() 在全局注册表中查找或创建。


---


## 内置 Symbol


JavaScript 定义了一些内置的 Symbol 值，用于自定义语言行为。


## 实例


```javascript
// Symbol.iterator 用于定义对象的默认迭代器
var arr = [1, 2, 3];
// 获取数组的迭代器
var iterator = arr[Symbol.iterator]();

// 使用迭代器遍历
console.log("第一个元素: " + iterator.next().value);
console.log("第二个元素: " + iterator.next().value);

// Symbol.toStringTag 自定义对象的 toString() 返回值
var obj = {
    [Symbol.toStringTag]: "MyObject"
};
console.log("对象类型: " + obj.toString());
```


**运行结果：**


```
第一个元素: 1
第二个元素: 2
对象类型: [object MyObject]
```


**
重要：**内置 Symbol 用于自定义语言行为，如迭代器、类型转换等，是 JavaScript 高级特性的基础。


---


## Symbol 类型注解


在 TypeScript 中使用 Symbol 类型进行类型注解。


## 实例


```javascript
// Symbol 类型注解
var sym: symbol = Symbol("key");

// 对象的键类型为 symbol，值为 string
var obj: { [key: symbol]: string } = {};

// 使用 Symbol 作为键
obj[sym] = "value";
console.log("Symbol 属性值: " + obj[sym]);
```


**
类型：**TypeScript 中使用 `symbol` 类型注解 Symbol 值。


---


## 注意事项


- **唯一性：**每次 Symbol() 调用的值都不同
- **不可枚举：**Symbol 属性不会出现在 for...in 循环中
- **JSON 忽略：**Symbol 属性不会被 JSON 序列化
- **全局注册：**Symbol.for() 在全局注册表中共享


**
应用场景：**Symbol 常用于创建对象的私有属性、定义唯一常量、避免属性名冲突等。


---


## 总结


Symbol 是 TypeScript 中重要的原始类型。


- **唯一性：**每次创建的 Symbol 都不相等
- **属性键：**可用作对象的唯一属性键
- **全局注册：**Symbol.for() 创建/获取全局 Symbol
- **内置 Symbol：**Symbol.iterator、Symbol.toStringTag 等
- **类型注解：**使用 symbol 类型


**
建议：**在需要创建唯一标识符、避免属性名冲突、或需要"私有"属性时，使用 Symbol。









	  AI 思考中...





			** [TypeScript null 和 undefined](https://www.runoob.com/ts-null-undefined.html)
			[TypeScript 特殊类型：never、void、unknown、any](https://www.runoob.com/ts-special-types.html) **













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