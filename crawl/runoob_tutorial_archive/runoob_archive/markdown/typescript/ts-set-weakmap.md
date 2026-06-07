# TypeScript Set 和 WeakMap

- Source: https://www.runoob.com/typescript/ts-set-weakmap.html

TypeScript 继承自 JavaScript 的 Set 和 WeakMap 数据结构，提供了更强大的类型支持。


这些数据结构在处理唯一值集合、键值对映射、缓存等场景非常有用。


---






  Set 和 Map 数据结构



  Set

    值的集合
    值唯一，不重复
    可遍历
    add/has/delete




  WeakSet

    对象弱引用
    不影响 GC
    不可遍历
    add/has/delete




  Map

    键值对集合
    键可以是任意类型
    可遍历
    set/get/has




  WeakMap

    键弱引用
    键必须是对象
    不影响 GC
    不可遍历




  应用场景



  Set: 去重、唯一值集合


  Map: 键值映射、缓存


  WeakMap/WeakSet: 内存优化





--- ## 为什么需要 Set 和 WeakMap 在开发中，我们经常需要处理唯一值集合和键值对映射。


Set 提供了自动去重的集合功能，比数组更方便处理唯一值。


WeakSet 和 WeakMap 使用弱引用，不会阻止垃圾回收，适用于需要避免内存泄漏的场景，如缓存 DOM 节点。


**
概念说明：**Set 是值的集合，值唯一；Map 是键值对集合，键可以是任意类型。WeakSet 和 WeakMap 使用弱引用，不影响垃圾回收。


---


## Set


Set 是值的集合，值唯一，不允许重复。


## 实例


```javascript
// 创建 Set，指定元素类型为 number
var numbers = new Set<number>();

// 添加元素
numbers.add(1);
numbers.add(2);
numbers.add(3);
numbers.add(1); // 重复值会被忽略，不会添加

// 检查大小和包含
console.log("Set 大小: " + numbers.size);
console.log("是否包含 2: " + numbers.has(2));

// 遍历 Set
numbers.forEach(function(value) {
    console.log("值: " + value);
});

// 转换为数组
var arr = Array.from(numbers);
console.log("转换为数组: " + arr);
```


**运行结果：**


```
Set 大小: 3
是否包含 2: true
值: 1
值: 2
值: 3
转换为数组: 1,2,3
```


**
去重：**Set 会自动忽略重复的值，这使得它非常适合用于数组去重。


---


## Set 类型注解


可以显式指定 Set 中值的类型。


## 实例


```javascript
// 字符串 Set
// 只能添加字符串类型的值
var stringSet: Set<string> = new Set();
stringSet.add("a");
stringSet.add("b");

// 对象 Set
// 定义 Person 接口
interface Person {
    name: string;
}
// 创建存储 Person 对象的 Set
var personSet: Set<Person> = new Set();
personSet.add({ name: "Alice" });
personSet.add({ name: "Bob" });

console.log("字符串 Set: " + Array.from(stringSet));
console.log("对象 Set 大小: " + personSet.size);
```


**
泛型：**使用 `Set` 语法指定 Set 中元素的类型。


---


## WeakSet


WeakSet 存储对象引用，引用为弱引用（不影响垃圾回收）。


## 实例


```javascript
// WeakSet 只能存储对象，不能存储原始值
var weakSet = new WeakSet();

// 创建对象
var obj1 = { name: "Alice" };
var obj2 = { name: "Bob" };

// 添加对象到 WeakSet
weakSet.add(obj1);
weakSet.add(obj2);

// 检查是否包含
console.log("是否包含 obj1: " + weakSet.has(obj1));

// 移除引用后，对象可能被垃圾回收
weakSet.delete(obj1);
console.log("删除后是否包含 obj1: " + weakSet.has(obj1));
```


**
注意：**WeakSet 不能遍历，类型注解只能是 `object`。这使得 WeakSet 适合存储需要被垃圾回收的对象。


---


## Map


Map 是键值对集合，键可以是任意类型。


## 实例


```javascript
// 创建 Map，键类型为 string，值类型为 number
var map = new Map<string, number>();

// 设置键值对
map.set("one", 1);
map.set("two", 2);
map.set("three", 3);

// 获取值
console.log("获取 two: " + map.get("two"));
console.log("Map 大小: " + map.size);
console.log("是否包含 three: " + map.has("three"));

// 遍历 Map
map.forEach(function(value, key) {
    console.log(key + ": " + value);
});

// 转换为数组
console.log("转换为数组: " + Array.from(map.entries()));
```


**运行结果：**


```
获取 two: 2
Map 大小: 3
是否包含 three: true
one: 1
two: 2
three: 3
转换为数组: one,1,two,2,three,3
```


**
优势：**Map 的键可以是任意类型（对象、函数等），这比使用对象作为键更灵活。


---


## WeakMap


WeakMap 的键是弱引用，不影响垃圾回收。


## 实例


```javascript
// WeakMap 的键必须是对象
// 键类型为 object，值类型为 string
var weakMap = new WeakMap<object, string>();

// 创建对象作为键
var keyObj = { id: 1 };
// 设置键值对
weakMap.set(keyObj, "value1");

// 获取值
console.log("获取值: " + weakMap.get(keyObj));
console.log("是否包含: " + weakMap.has(keyObj));

// 删除键值对
weakMap.delete(keyObj);
console.log("删除后: " + weakMap.has(keyObj));
```


**
应用场景：**WeakMap 常用于缓存 DOM 节点数据，当 DOM 节点被移除时，缓存数据也会被自动清理，避免内存泄漏。


---


## 实际应用场景


使用 Map 统计数组元素出现次数。


## 实例


```javascript
// 使用 Map 统计数组中每个元素的出现次数
function countElements(arr: string[]): Map<string, number> {
    // 创建 Map，键是字符串，值是数字
    var counts = new Map<string, number>();

    // 遍历数组
    for (var _i = 0, arr_1 = arr; _i < arr_1.length; _i++) {
        var item = arr_1[_i];
        // 获取当前计数，如果没有则返回 0
        var currentCount = counts.get(item) || 0;
        // 更新计数
        counts.set(item, currentCount + 1);
    }

    return counts;
}

// 测试
var fruits = ["apple", "banana", "apple", "orange", "banana", "apple"];
var result = countElements(fruits);

// 遍历结果
result.forEach(function(count, fruit) {
    console.log(fruit + ": " + count);
});
```


**运行结果：**


```
apple: 3
banana: 2
orange: 1
```


**
实用：**Map 是实现缓存、统计、索引等功能的理想选择。


---


## 注意事项


- **Set 唯一性：**Set 自动忽略重复值
- **WeakSet/WeakMap：**键必须是对象，不能遍历
- **Map 键类型：**Map 的键可以是任意类型
- **内存管理：**WeakSet/WeakMap 不阻止垃圾回收


**
选择建议：**需要唯一值集合用 Set，需要键值映射用 Map，需要避免内存泄漏用 WeakSet/WeakMap。


---


## 总结


Set 和 Map 是 TypeScript 中非常有用的数据结构。


- **Set：**值的集合，值唯一，自动去重
- **WeakSet：**对象弱引用集合，不可遍历，适用于需要被垃圾回收的场景
- **Map：**键值对集合，键可以是任意类型
- **WeakMap：**键弱引用，不可遍历，适用于缓存和私有数据


**
建议：**根据具体需求选择合适的数据结构：需要去重用 Set，需要映射用 Map，需要内存优化用 Weak 版本。









	  AI 思考中...





			** [TypeScript 特殊类型：never、void、unknown、any](https://www.runoob.com/ts-special-types.html)
			[TypeScript 函数重载](https://www.runoob.com/ts-function-overload.html) **













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