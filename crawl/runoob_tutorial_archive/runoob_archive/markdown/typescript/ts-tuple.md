# 

- Source: https://www.runoob.com/typescript/ts-tuple.html

TypeScript 元组

我们知道数组中元素的数据类型都一般是相同的（any[] 类型的数组可以不同），如果存储的元素数据类型不同，则需要使用元组。


TypeScript 中的元组（Tuple）是一种特殊类型的数组，它允许在数组中存储不同类型的元素，与普通数组不同，元组中的每个元素都有明确的类型和位置。元组可以在很多场景下用于表示固定长度、且各元素类型已知的数据结构。


创建元组的语法格式如下：


```
let tuple: [类型1, 类型2, 类型3, ...];
```


### 实例


声明一个元组并初始化：


```
let mytuple: [number, string];
mytuple = [42,"Runoob"];
```


在上面的例子中，mytuple 是一个元组，它包含一个 number 类型和一个 string 类型的元素。


### 访问元组


元组中元素使用索引来访问，第一个元素的索引值为 0，第二个为 1，以此类推第 n 个为 n-1，语法格式如下:


```
tuple_name[index]
```


### 实例


以下实例定义了元组，包含了数字和字符串两种类型的元素：


## TypeScript


```javascript
let mytuple: [number, string, boolean] = [42, "Runoob", true];

// 访问元组中的元素
let num = mytuple[0]; // 访问第一个元素，值为 42，类型为 number
let str = mytuple[1]; // 访问第二个元素，值为 "Runoob"，类型为 string
let bool = mytuple[2]; // 访问第三个元素，值为 true，类型为 boolean

console.log(num);  // 输出: 42
console.log(str);  // 输出: Runoob
console.log(bool); // 输出: true
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var mytuple = [42, "Runoob", true];
// 访问元组中的元素
var num = mytuple[0]; // 访问第一个元素，值为 42，类型为 number
var str = mytuple[1]; // 访问第二个元素，值为 "Runoob"，类型为 string
var bool = mytuple[2]; // 访问第三个元素，值为 true，类型为 boolean
console.log(num); // 输出: 42
console.log(str); // 输出: Runoob
console.log(bool); // 输出: true
```


输出结果为：


```
42
Runoob
true
```


---


## 元组运算


我们可以使用以下两个函数向元组添加新元素或者删除元素：


- push() 向元组添加元素，添加在最后面。
- pop() 从元组中移除元素（最后一个），并返回移除的元素。

push 方法可以向元组的末尾添加一个元素，类型必须符合元组定义中的类型约束。如果超出元组的类型约束，TypeScript 会报错。


## TypeScript


```javascript
var tuple = [42, "Hello"];
// 添加符合类型的元素
tuple.push("World"); // 合法，因为元组定义了可选的 string 类型
console.log(tuple); // 输出: [42, "Hello", "World"]
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var tuple = [42, "Hello"];
// 添加符合类型的元素
tuple.push("World"); // 合法，因为元组定义了可选的 string 类型
console.log(tuple); // 输出: [42, "Hello", "World"]
```


输出结果为：


```
[ 42, 'Hello', 'World' ]
```


pop 方法从元组的末尾移除一个元素，并返回该元素。返回的元素类型将根据元组的定义类型推断。


## 实例


```javascript
let tuple: [number, string, boolean] = [42, "Hello", true];

// 移除最后一个元素
let lastElement = tuple.pop();

console.log(lastElement); // 输出: true
console.log(tuple);       // 输出: [42, "Hello"]
```


---


## 更新元组


元组是可变的，这意味着我们可以对元组进行更新操作：


## TypeScript


```javascript
var mytuple = [42, "Runoob", "Taobao", "Google"]; // 创建一个元组
console.log("元组的第一个元素为：" + mytuple[0])

// 更新元组元素
mytuple[0] = 121
console.log("元组中的第一个元素更新为："+ mytuple[0])
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var mytuple = [42, "Runoob", "Taobao", "Google"]; // 创建一个元组
console.log("元组的第一个元素为：" + mytuple[0]);
// 更新元组元素
mytuple[0] = 121;
console.log("元组中的第一个元素更新为：" + mytuple[0]);
```


输出结果为：


```
元组的第一个元素为：42
元组中的第一个元素更新为：121
```


---


## 解构元组


我们也可以把元组元素赋值给变量，如下所示：


## TypeScript


```javascript
let a: [number, string, boolean] = [42, "Hello", true];// 创建一个元组

var [b,c] = a
console.log( b )
console.log( c )
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var a = [42, "Hello", true]; // 创建一个元组
var b = a[0], c = a[1];
console.log(b);
console.log(c);
```


输出结果为：


```
42
Hello
```


---


## 使用标签元组

TypeScript 还允许为元组中的每个元素添加标签，这使得元组的含义更加清晰：


```
let tuple: [id: number, name: string] = [1, "John"];
```


在这个例子中，id 和 name 是元组的标签，可以让代码更加可读。


---


## 元组的实际应用

元组常用于函数返回多个值的场景，或者表示某些固定结构的数据，比如：


## 实例


```javascript
function getUserInfo(): [number, string] {
    return [1, "John Doe"];
}

const [userId, userName] = getUserInfo();
console.log(userId);   // 输出: 1
console.log(userName); // 输出: John Doe
```


---


## 元组的类型推断


TypeScript 可以根据数组的元素自动推断出元组的类型：


```
let tuple = [42, "Hello"] as const; // 元组类型：[42, "Hello"]
```


通过 as const 断言，TypeScript 会将该元组视为一个不可变的常量元组。


---


## 连接元组

元组可以使用数组的 concat 方法进行连接，但需要注意连接后的结果是一个普通的数组，而不是元组。


## 实例


```javascript
let tuple1: [number, string] = [42, "Hello"];
let tuple2: [boolean, number] = [true, 100];

let result = tuple1.concat(tuple2); // 结果是一个数组: [42, "Hello", true, 100]
console.log(result); // 输出: [42, "Hello", true, 100]
```


---


## 切片元组

你可以使用数组的 slice 方法对元组进行切片操作，返回一个新的数组。


## 实例


```javascript
let tuple: [number, string, boolean] = [42, "Hello", true];

let sliced = tuple.slice(1); // 从索引 1 开始切片
console.log(sliced); // 输出: ["Hello", true]
```


---


## 遍历元组

你可以使用 for...of 循环或者 forEach 方法遍历元组中的元素。


## 实例


```javascript
let tuple: [number, string, boolean] = [42, "Hello", true];

// 使用 for...of 循环
for (let item of tuple) {
    console.log(item);
}

// 使用 forEach 方法
tuple.forEach(item => console.log(item));
```


---


## 转换为普通数组

虽然元组是一个固定长度、固定类型的数组，但可以通过 Array.prototype 的方法将其转换为普通数组进行进一步处理。


## 实例


```javascript
let tuple: [number, string, boolean] = [42, "Hello", true];

// 转换为数组并使用数组方法
let array = Array.from(tuple);
array.push("New Element");

console.log(array); // 输出: [42, "Hello", true, "New Element"]
```


---


## 扩展元组

使用剩余运算符可以轻松地将多个元组合并成一个新的元组：


## 实例


```javascript
let tuple1: [number, string] = [42, "Hello"];
let tuple2: [boolean] = [true];

let extendedTuple: [number, string, ...typeof tuple2] = [42, "Hello", ...tuple2];

console.log(extendedTuple); // 输出: [42, "Hello", true]
```









	  AI 思考中...





			** [TypeScript Array(数组)](https://www.runoob.com/ts-array.html)
			[TypeScript 联合类型](https://www.runoob.com/ts-union.html) **













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