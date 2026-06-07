# TypeScript Map 对象

- Source: https://www.runoob.com/typescript/ts-map.html

Map 对象保存键值对，并且能够记住键的原始插入顺序。

任何值(对象或者原始值) 都可以作为一个键或一个值。


Map 是 ES6 中引入的一种新的数据结构，可以参考 [ES6 Map 与 Set](https://www.runoob.com/w3cnote/es6-map-set.html)。


---


## 创建 Map

TypeScript 使用 Map 类型和 new 关键字来创建 Map：


```
let myMap = new Map();
```


初始化 Map，可以以数组的格式来传入键值对：


```
let myMap = new Map([
        ["key1", "value1"],
        ["key2", "value2"]
    ]);
```


Map 相关的函数与属性：


- **map.clear()** – 移除 Map 对象的所有键/值对 。
- **map.set()** – 设置键值对，返回该 Map 对象。
- **map.get()** – 返回键对应的值，如果不存在，则返回 undefined。
- **map.has()** – 返回一个布尔值，用于判断 Map 中是否包含键对应的值。
- **map.delete()** – 删除 Map 中的元素，删除成功返回 true，失败返回 false。
- **map.size** – 返回 Map 对象键/值对的数量。
- **map.keys()** - 返回一个 Iterator 对象， 包含了 Map 对象中每个元素的键 。
- **map.values()** – 返回一个新的Iterator对象，包含了Map对象中每个元素的值 。
- **map.entries()** – 返回一个包含 Map 中所有键值对的迭代器 。


### 常用函数


**set(key: K, value: V): this** - 向 Map 中添加或更新键值对。


```
map.set('key1', 'value1');
```


**get(key: K): V | undefined** - 根据键获取值，如果键不存在则返回 undefined。


```
const value = map.get('key1');
```


**has(key: K): boolean **- 检查 Map 中是否存在指定的键。


```
const exists = map.has('key1');
```


**delete(key: K): boolean **- 删除指定键的键值对，成功删除返回 true，否则返回 false。


```
const removed = map.delete('key1');
```


**clear(): void **- 清空 Map 中的所有键值对。


```
map.clear();
```


**size: number** - 返回 Map 中键值对的数量。


```
const size = map.size;
```


### 迭代方法

keys(): IterableIterator<K> - 返回一个包含 Map 中所有键的迭代器。


```
for (const key of map.keys()) {
  console.log(key);
}
```


**values(): IterableIterator** - 返回一个包含 Map 中所有值的迭代器。


```
for (const value of map.values()) {
  console.log(value);
}
```


**entries(): IterableIterator** - 返回一个包含 Map 中所有键值对的迭代器，每个元素是一个 [key, value] 数组。


```
for (const [key, value] of map.entries()) {
  console.log(key, value);
}
```


**forEach(callbackfn: (value: V, key: K, map: Map) => void, thisArg?: any): void** - 对 Map 中的每个键值对执行一次提供的回调函数。


```
map.forEach((value, key) => {
  console.log(key, value);
});
```


### 实例


## 实例


```javascript
const map = new Map<string, number>();

map.set('one', 1);
map.set('two', 2);

console.log(map.get('one')); // 输出: 1

console.log(map.has('two')); // 输出: true

map.delete('one');

console.log(map.size); // 输出: 1

map.forEach((value, key) => {
  console.log(key, value); // 输出: two 2
});

map.clear();

console.log(map.size); // 输出: 0
```


## 实例 - test.ts 文件


```javascript
let nameSiteMapping = new Map();

// 设置 Map 对象
nameSiteMapping.set("Google", 1);
nameSiteMapping.set("Runoob", 2);
nameSiteMapping.set("Taobao", 3);

// 获取键对应的值
console.log(nameSiteMapping.get("Runoob"));     // 2

// 判断 Map 中是否包含键对应的值
console.log(nameSiteMapping.has("Taobao"));       // true
console.log(nameSiteMapping.has("Zhihu"));        // false

// 返回 Map 对象键/值对的数量
console.log(nameSiteMapping.size);                // 3

// 删除 Runoob
console.log(nameSiteMapping.delete("Runoob"));    // true
console.log(nameSiteMapping);
// 移除 Map 对象的所有键/值对
nameSiteMapping.clear();             // 清除 Map
console.log(nameSiteMapping);
```


使用 **es6** 编译：


```
tsc --target es6 test.ts
```


编译以上代码得到如下 JavaScript 代码：


## 实例 - test.js 文件


```javascript
let nameSiteMapping = new Map();
// 设置 Map 对象
nameSiteMapping.set("Google", 1);
nameSiteMapping.set("Runoob", 2);
nameSiteMapping.set("Taobao", 3);
// 获取键对应的值
console.log(nameSiteMapping.get("Runoob")); //40
// 判断 Map 中是否包含键对应的值
console.log(nameSiteMapping.has("Taobao")); //true
console.log(nameSiteMapping.has("Zhihu")); //false
// 返回 Map 对象键/值对的数量
console.log(nameSiteMapping.size); //3
// 删除 Runoob
console.log(nameSiteMapping.delete("Runoob")); // true
console.log(nameSiteMapping);
// 移除 Map 对象的所有键/值对
nameSiteMapping.clear(); //清除 Map
console.log(nameSiteMapping);
```


执行以上 JavaScript 代码，输出结果为：


```
2
true
false
3
true
Map { 'Google' => 1, 'Taobao' => 3 }
Map {}
```


### 迭代 Map

Map 对象中的元素是按顺序插入的，我们可以迭代 Map 对象，每一次迭代返回 [key, value] 数组。


TypeScript使用 **for...of** 来实现迭代：


## 实例 -test.ts 文件


```javascript
let nameSiteMapping = new Map();

nameSiteMapping.set("Google", 1);
nameSiteMapping.set("Runoob", 2);
nameSiteMapping.set("Taobao", 3);

// 迭代 Map 中的 key
for (let key of nameSiteMapping.keys()) {
    console.log(key);
}

// 迭代 Map 中的 value
for (let value of nameSiteMapping.values()) {
    console.log(value);
}

// 迭代 Map 中的 key => value
for (let entry of nameSiteMapping.entries()) {
    console.log(entry[0], entry[1]);
}

// 使用对象解析
for (let [key, value] of nameSiteMapping) {
    console.log(key, value);
}
```


使用 **es6** 编译：


```
tsc --target es6 test.ts
```


编译以上代码得到如下 JavaScript 代码：


## 实例


```javascript
let nameSiteMapping = new Map();
nameSiteMapping.set("Google", 1);
nameSiteMapping.set("Runoob", 2);
nameSiteMapping.set("Taobao", 3);
// 迭代 Map 中的 key
for (let key of nameSiteMapping.keys()) {
    console.log(key);
}
// 迭代 Map 中的 value
for (let value of nameSiteMapping.values()) {
    console.log(value);
}
// 迭代 Map 中的 key => value
for (let entry of nameSiteMapping.entries()) {
    console.log(entry[0], entry[1]);
}
// 使用对象解析
for (let [key, value] of nameSiteMapping) {
    console.log(key, value);
}
```


执行以上 JavaScript 代码，输出结果为：


```
Google
Runoob
Taobao
1
2
3
Google 1
Runoob 2
Taobao 3
Google 1
Runoob 2
Taobao 3
```









	  AI 思考中...





			** [TypeScript 声明文件](https://www.runoob.com/ts-ambient.html)
			[TypeScript 测验](https://www.runoob.com/../quiz/ts-quiz.html) **













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