# TypeScript 迭代器与生成器

- Source: https://www.runoob.com/typescript/ts-iterator-generator.html

迭代器和生成器是 JavaScript/TypeScript 中处理集合的重要模式。


它们提供了一种统一的遍历数据的方式，让处理大数据流、无限序列等变得更加简单。


---






  迭代器与生成器工作流程



  迭代器协议

    实现 Symbol.iterator
    返回 next() 方法
    { done, value }




for...of 循环 自动调用 next() 遍历所有元素 done=true 时停止 生成器 function* yield 暂停 惰性计算 生成器特性 惰性求值 - 按需生成 状态保持 - 暂停位置 可组合 - yield* 委托 --- ## 为什么需要迭代器和生成器 在处理集合数据时，我们经常需要遍历数组、对象等数据结构。


迭代器提供了一种统一的、可自定义的遍历接口，让任何对象都可以被遍历。


生成器是创建迭代器的简洁方式，它允许你使用函数来暂停和恢复执行，非常适合处理大数据流或无限序列。


**
概念说明：**迭代器是一个对象，它提供 next() 方法用于遍历数据。生成器是一种特殊的函数，可以在执行过程中暂停并返回一个值。


---


## 可迭代协议


实现 Symbol.iterator 方法的对象可以被 for...of 循环遍历。


## 实例


```javascript
// 数组默认可迭代
var arr = [1, 2, 3];
for (var _i = 0, arr_1 = arr; _i < arr_1.length; _i++) {
    var item = arr_1[_i];
    console.log("数组元素: " + item);
}

// 字符串默认可迭代
var str = "hello";
for (var _i = 0, str_1 = str; _i < str_1.length; _i++) {
    var char = str_1[_i];
    console.log("字符: " + char);
}
```


**运行结果：**


```
数组元素: 1
数组元素: 2
数组元素: 3
字符: h
字符: e
字符: l
字符: l
字符: o
```


**
说明：**数组和字符串都内置实现了 Symbol.iterator 方法，所以可以直接使用 for...of 遍历。


---


## 自定义可迭代对象


让普通对象实现 Symbol.iterator 接口，使其可被遍历。


## 实例


```javascript
// 创建自定义可迭代对象：范围
var range = {
    from: 1,
    to: 5,
    // 实现 Symbol.iterator 方法
    [Symbol.iterator]: function() {
        return {
            current: this.from,
            last: this.to,
            // next 方法返回迭代结果
            next: function() {
                if (this.current <= this.last) {
                    // 未完成，返回当前值并递增
                    return { done: false, value: this.current++ };
                }
                // 已完成
                return { done: true, value: undefined };
            }
        };
    }
};

// 使用 for...of 遍历
for (var _i = 0, range_1 = range; _i < range_1.length; _i++) {
    var num = range_1[_i];
    console.log("范围: " + num);
}
```


**
迭代器协议：**迭代器必须有一个 next() 方法，返回 { done: boolean, value: any } 格式的对象。


---


## 生成器函数


使用 function* 语法创建生成器，使用 yield 暂停执行并返回值。


## 实例


```javascript
// 生成器函数：使用 function* 语法
function* numberGenerator() {
    yield 1;  // 暂停并返回 1
    yield 2;  // 暂停并返回 2
    yield 3;  // 暂停并返回 3
}

// 创建生成器实例
var gen = numberGenerator();

// 每次调用 next() 都会执行到下一个 yield
console.log("第一个: " + gen.next().value);
console.log("第二个: " + gen.next().value);
console.log("第三个: " + gen.next().value);
console.log("完成: " + gen.next().done);
```


**运行结果：**


```
第一个: 1
第二个: 2
第三个: 3
完成: true
```


**
生成器：**生成器函数会返回一个迭代器，每次调用 next() 都会执行到下一个 yield 语句。


---


## 无限生成器


生成器可以产生无限序列，由于是惰性求值，不会占用无限内存。


## 实例


```javascript
// 无限数字生成器
// 每次调用只生成一个数字，不会一次性生成所有数字
function* infiniteNumbers() {
    var n = 1;
    while (true) {  // 无限循环
        yield n++;   // 暂停并返回当前值，然后递增
    }
}

var gen = infiniteNumbers();
console.log("第1个: " + gen.next().value);
console.log("第2个: " + gen.next().value);
console.log("第3个: " + gen.next().value);

// 只获取前5个数字
var nums = [];
var iter = infiniteNumbers();
for (var i = 0; i < 5; i++) {
    nums.push(iter.next().value);
}
console.log("前5个: " + nums);
```


**运行结果：**


```
第1个: 1
第2个: 2
第3个: 3
前5个: 1,2,3,4,5
```


**
惰性求值：**生成器的最大优势是惰性求值，只有在调用 next() 时才会计算下一个值，非常适合处理无限序列。


---


## 委托生成器


使用 yield* 委托另一个生成器或可迭代对象。


## 实例


```javascript
// 第一个生成器
function* gen1() {
    yield 1;
    yield 2;
}

// 第二个生成器
function* gen2() {
    yield 3;
    yield 4;
}

// 组合生成器：使用 yield* 委托
function* combined() {
    yield* gen1();  // 委托给 gen1
    yield* gen2();  // 委托给 gen2
}

// 遍历组合生成器
for (var _i = 0, combined_1 = combined(); _i < combined_1.length; _i++) {
    var num = combined_1[_i];
    console.log("值: " + num);
}
```


**运行结果：**


```
值: 1
值: 2
值: 3
值: 4
```


**
yield*：**委托生成器可以组合多个生成器或可迭代对象，非常适合构建可复用的数据流。


---


## TypeScript 生成器类型


生成器的类型注解使用 Generator 类型。


## 实例


```javascript
// 生成器类型：Generator<yield类型, return类型, next参数类型>
function* idGenerator(): Generator<number, void, unknown> {
    var i = 1;
    while (i <= 3) {
        yield i++;  // yield number 类型
    }
    // return void
}

var gen = idGenerator();
console.log(Array.from(gen));
```


**
类型说明：**Generator 表示：T 是 yield 的类型，R 是最终返回的类型，N 是 next() 参数的类型。


---


## 注意事项


- **迭代器协议：**实现 Symbol.iterator 返回带 next() 方法的对象
- **生成器语法：**使用 function* 而非 function
- **yield 关键字：**暂停执行并返回值
- **惰性计算：**生成器按需计算，不会一次性生成所有值


**最佳实践：**处理大数据流、无限序列或需要暂停/恢复的场景时，使用生成器。

---


## 总结


迭代器和生成器是 TypeScript 中强大的数据处理工具。


- **可迭代对象：**实现 Symbol.iterator 接口
- **生成器：**使用 function* 和 yield 创建
- **yield：**暂停执行并返回值
- **委托：**使用 yield* 组合多个生成器


**
建议：**在需要遍历自定义对象、处理数据流或创建无限序列时，使用迭代器和生成器。









	  AI 思考中...





			** [TypeScript 箭头函数与 this](https://www.runoob.com/ts-arrow-function.html)
			[TypeScript async/await 异步编程](https://www.runoob.com/ts-async-await.html) **













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