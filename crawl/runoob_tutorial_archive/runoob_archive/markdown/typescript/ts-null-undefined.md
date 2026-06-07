# TypeScript null 和 undefined

- Source: https://www.runoob.com/typescript/ts-null-undefined.html

在 TypeScript 中，null 和 undefined 有特殊的处理方式。


启用 `strictNullChecks` 后，需要显式处理这些值，这有助于编写更安全的代码。


---






  null 和 undefined 处理方式



  null

    表示"空值"
    需要显式声明
    string | null



  vs



  undefined

    表示"未定义"
    可选属性自动包含
    name?: string




安全 安全处理方式 可选链: obj?.prop 空值合并: value ?? default 类型守卫: if (val !== null) 处理场景 联合类型声明 可选参数和属性 空值合并运算符 --- ## 为什么需要处理 null 和 undefined JavaScript 中 null 和 undefined 是常见的错误来源，很多运行时错误都与之相关。


TypeScript 的 strictNullChecks 选项要求开发者显式处理可能为空的值。


这虽然增加了编码工作量，但能大幅减少空值导致的运行时错误，提高代码可靠性。


**
概念说明：**`null` 表示"空值"，即这里没有值；`undefined` 表示"未定义"，即这里还没有被赋值。


---


## null 和 undefined 基础


null 表示"空值"，undefined 表示"未定义"。两者在 TypeScript 中是独立的类型。


## 实例


```javascript
// 声明 null 类型的变量
// 只能赋值为 null
var empty: null = null;

// 声明 undefined 类型的变量
// 只能赋值为 undefined
var notDefined: undefined = undefined;

console.log("null: " + empty);
console.log("undefined: " + notDefined);
```


**运行结果：**


```
null: null
undefined: undefined
```


**
说明：**在不启用 strictNullChecks 的情况下，这些类型可以相互赋值。启用后需要显式声明。


---


## 联合类型处理 null


启用 strictNullChecks 后，需要使用联合类型显式声明可能为 null 的值。


## 实例


```javascript
// 联合类型：可以是字符串或 null
// 显式声明值可能为空
var name: string | null = "Alice";
name = null;  // 正确：可以赋值为 null

// 访问可能为 null 的值需要先检查
// 函数参数可能是字符串或 null
function getLength(str: string | null): number {
    // 使用条件检查是否为 null
    if (str === null) {
        return 0;  // null 时返回 0
    }
    // TypeScript 会推断 str 不是 null
    return str.length;
}

console.log("长度: " + getLength("hello"));
console.log("长度: " + getLength(null));
```


**运行结果：**


```
长度: 5
长度: 0
```


**
最佳实践：**使用类型守卫（if 检查）来收窄类型，让 TypeScript 知道具体是什么类型。


---


## 可选参数和属性


可选参数和可选属性自动包含 undefined，不需要显式声明 null。


## 实例


```javascript
// 可选参数：使用 ? 标记
// 参数可能是 string 或 undefined
function greet(name?: string): string {
    // 检查是否为 undefined
    if (name === undefined) {
        return "Hello, stranger!";
    }
    return "Hello, " + name;
}

console.log(greet("Alice"));
console.log(greet());

// 可选属性：使用 ? 标记
// age 属性是可选的，可能不存在
interface User {
    name: string;
    age?: number;  // 可选属性
}

var user: User = { name: "Bob" };
console.log("用户: " + JSON.stringify(user));
```


**运行结果：**


```
Hello, Alice!
Hello, stranger!
用户: {"name":"Bob"}
```


**
说明：**可选参数 `name?: string` 等同于 `string | undefined`。


---


## 非空断言运算符


使用 `!` 告诉编译器值不为 null 或 undefined。这应该谨慎使用。


## 实例


```javascript
function getLength(str: string | null): number {
    // 非空断言：告诉编译器 str 不为 null
    // 这是一个危险的写法，如果 str 真的为 null 会报错
    return str!.length;
}

console.log("长度: " + getLength("hello"));
```


**
警告：**非空断言会绕过 TypeScript 的类型检查，如果值实际为 null，运行时仍会报错。尽量避免使用。


---


## 空值合并运算符


使用 `??` 提供默认值，只有当值为 null 或 undefined 时才使用默认值。


## 实例


```javascript
// 初始值为 null
var name: string | null = null;

// ?? 运算符：左侧为 null/undefined 时使用右侧值
// 如果 name 为 null，使用 "Guest"
var displayName = name ?? "Guest";

console.log("显示名称: " + displayName);

// 对比 || 运算符（会把 0 和空字符串视为 falsy）
var num: number | null = 0;
var result1 = num ?? 100;  // 0（正确：0 不是 null/undefined）
var result2 = num || 100;  // 100（错误：0 被视为 falsy）

console.log("?? 结果: " + result1);
console.log("|| 结果: " + result2);
```


**运行结果：**


```
显示名称: Guest
?? 结果: 0
|| 结果: 100
```


**
建议：**优先使用 `??` 而不是 `||`，因为 `??` 只会处理 null 和 undefined，不会错误地将 0 或空字符串视为 falsy。


---


## 可选链


使用 `?.` 安全访问可能不存在的嵌套属性，避免多层嵌套时的空值检查。


## 实例


```javascript
// 定义人员类型，地址是可选的
interface Person {
    name: string;
    address?: {
        city: string;
    };
}

// 创建人员对象，没有地址
var person: Person = { name: "Alice" };

// 可选链：安全访问可能不存在的属性
// 如果 address 不存在，返回 undefined 而不会报错
var city = person.address?.city;

// 结合空值合并运算符
console.log("城市: " + city);
console.log("城市: " + (person.address?.city ?? "未知"));
```


**运行结果：**


```
城市: undefined
城市: 未知
```


**
最佳实践：**可选链 `?.` 是处理嵌套可选属性的最佳方式，配合 `??` 可以提供默认值的兜底。


---


## 注意事项


- **严格模式：**建议启用 strictNullChecks 以获得更好的类型安全
- **避免断言：**尽量不要使用非空断言 `!`
- **?? vs ||：**优先使用 `??` 避免误判 0 和空字符串
- **可选链：**处理嵌套可选属性时使用 `?.`


**
最佳实践：**使用类型守卫、可选链和空值合并运算符来处理 null 和 undefined，让代码更安全、更易读。


---


## 总结


正确处理 null 和 undefined 是编写安全 TypeScript 代码的关键。


- **严格模式：**启用 strictNullChecks 后需显式处理
- **联合类型：**使用 `string | null` 声明
- **可选参数/属性：**自动包含 undefined
- **非空断言：**使用 `!`（谨慎使用）
- **空值合并：**使用 `??` 提供默认值
- **可选链：**使用 `?.` 安全访问


**
建议：**养成处理空值的习惯，使用可选链和空值合并运算符让代码更健壮。








	  AI 思考中...





			** [TypeScript 类型断言](https://www.runoob.com/ts-assertion.html)
			[TypeScript Symbol](https://www.runoob.com/ts-symbol.html) **













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