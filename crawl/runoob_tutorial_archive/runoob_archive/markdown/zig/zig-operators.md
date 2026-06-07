# Zig 运算符

- Source: https://www.runoob.com/zig/zig-operators.html

运算符和表达式是编程语言中用于执行各种操作的基本组成部分。


在 Zig 中，运算符可以分为几类，包括算术运算符、关系运算符、逻辑运算符、位运算符、赋值运算符以及其他运算符。

以下是每种运算符的详细说明和示例。


## 算术运算符


| 运算符 | 描述 |
| --- | --- |
| + | 加法 |
| - | 减法 |
| * | 乘法 |
| / | 除法 |
| % | 取余（模运算） |


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const a: i32 = 5;
    const b: i32 = 3;

    const add: i32 = a + b;
    const subtract: i32 = a - b;
    const multiply: i32 = a * b;
    const divide: i32 = a / b;
    const remainder: i32 = a % b;

    std.debug.print("a + b = {}\n", .{add});
    std.debug.print("a - b = {}\n", .{subtract});
    std.debug.print("a * b = {}\n", .{multiply});
    std.debug.print("a / b = {}\n", .{divide});
    std.debug.print("a % b = {}\n", .{remainder});
}
```


编译输出结果为：


```
a + b = 8
a - b = 2
a * b = 15
a / b = 1
a % b = 2
```


## 关系运算符


| 运算符 | 描述 |
| --- | --- |
| == | 等于 |
| != | 不等于 |
| > | 大于 |
| = | 大于等于 |
| > | 右移 |


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const a: i32 = 5;  // 0101
    const b: i32 = 3;  // 0011

    const bit_and: i32 = a & b;      // 0001
    const bit_or: i32 = a | b;       // 0111
    const bit_xor: i32 = a ^ b;      // 0110
    const bit_not: i32 = ~a;         // 11111111111111111111111111111010
    const left_shift: i32 = a << 1;  // 1010
    const right_shift: i32 = a >> 1; // 0010

    std.debug.print("a & b: {}\n", .{bit_and});
    std.debug.print("a | b: {}\n", .{bit_or});
    std.debug.print("a ^ b: {}\n", .{bit_xor});
    std.debug.print("~a: {}\n", .{bit_not});
    std.debug.print("a << 1: {}\n", .{left_shift});
    std.debug.print("a >> 1: {}\n", .{right_shift});
}
```


编译输出结果为：


```
a & b: 1
a | b: 7
a ^ b: 6
~a: -6
a << 1: 10
a >> 1: 2
```


## 赋值运算符


| 运算符 | 描述 |
| --- | --- |
| = | 赋值 |
| += | 加法赋值 |
| -= | 减法赋值 |
| *= | 乘法赋值 |
| /= | 除法赋值 |
| %= | 取余赋值 |
| &= | 按位与赋值 |
| \|= | 按位或赋值 |
| ^= | 按位异或赋值 |
| >= | 右移赋值 |


## 实例


```zig
const std = @import("std");

pub fn main() void {
    var a: i32 = 5;
    const b: i32 = 3;

    a += b; // 相当于 a = a + b;
    std.debug.print("a += b: {}\n", .{a});

    a -= b; // 相当于 a = a - b;
    std.debug.print("a -= b: {}\n", .{a});

    a *= b; // 相当于 a = a * b;
    std.debug.print("a *= b: {}\n", .{a});

    a = @divTrunc(a, b); // 相当于 a = a / b;
    std.debug.print("a /= b: {}\n", .{a});

    a = @mod(a, b); // 相当于 a = a % b;
    std.debug.print("a %= b: {}\n", .{a});

    a &= b; // 相当于 a = a & b;
    std.debug.print("a &= b: {}\n", .{a});

    a |= b; // 相当于 a = a | b;
    std.debug.print("a |= b: {}\n", .{a});

    a ^= b; // 相当于 a = a ^ b;
    std.debug.print("a ^= b: {}\n", .{a});

    a <<= 1; // 相当于 a = a << 1;
    std.debug.print("a <<= 1: {}\n", .{a});

    a >>= 1; // 相当于 a = a >> 1;
    std.debug.print("a >>= 1: {}\n", .{a});
}
```


编译输出结果为：


```
a += b: 8
a -= b: 5
a *= b: 15
a /= b: 5
a %= b: 2
a &= b: 2
a |= b: 3
a ^= b: 0
a <<= 1: 0
a >>= 1: 0
```


## 其他运算符


| 运算符 | 描述 |
| --- | --- |
| ++ | 自增 |
| -- | 自减 |


## 实例


```zig
const std = @import("std");

pub fn main() void {
    var a: i32 = 5;

    a += 1; // Zig 中没有 ++ 运算符，可以用 += 1 替代
    std.debug.print("a += 1: {}\n", .{a});

    a -= 1; // Zig 中没有 -- 运算符，可以用 -= 1 替代
    std.debug.print("a -= 1: {}\n", .{a});
}
```


编译输出结果为：


```
a += 1: 6
a -= 1: 5
```


## 运算符优先级

以下是 Zig 运算符的优先级列表，从高到低排列：


| 优先级 | 运算符 | 描述 |
| --- | --- | --- |
| 1 | [] | 下标操作，数组或指针访问 |
| 1 | . | 成员访问 |
| 2 | fn_call() | 函数调用 |
| 2 | @builtin() | 内置函数调用 |
| 3 | ! | 错误传播 |
| 3 | ? | 可选值解包 |
| 4 | * & | 指针解引用和地址操作 |
| 5 | + - | 一元正号和负号 |
| 6 | ~ | 按位取反 |
| 7 | * / % | 乘法、除法、取余 |
| 8 | + - | 加法、减法 |
| 9 | >> | 按位左移、右移 |
| 10 | & | 按位与 |
| 11 | ^ | 按位异或 |
| 12 | ` | ` |
| 13 | == != | 相等、不相等 |
| 13 | > >= | 小于、小于等于、大于、大于等于 |
| 14 | and | 逻辑与 |
| 15 | or | 逻辑或 |
| 16 | orelse | 或者返回另一个值 |
| 17 | catch | 捕获错误 |
| 18 | = | 赋值 |
| 19 | -> | 闭包函数体或返回值类型指示符 |


**说明：**


- **结合性**：通常 Zig 的运算符是左结合的，但可以根据运算符的具体功能查阅文档。
- **注意事项**：Zig 中的操作符设计简洁明确，避免了许多语言中复杂的隐式行为，例如没有隐式类型转换。


以下示例展示了运算符优先级如何影响表达式的计算顺序：


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const a: i32 = 5;
    const b: i32 = 3;
    const c: i32 = 2;

    // 乘法优先于加法
    const result1: i32 = a + b * c; // 5 + (3 * 2) = 11
    std.debug.print("a + b * c = {}\n", .{result1});

    // 使用圆括号改变优先级
    const result2: i32 = (a + b) * c; // (5 + 3) * 2 = 16
    std.debug.print("(a + b) * c = {}\n", .{result2});

    // 比较运算符优先于逻辑运算符
    const result3: bool = a > b and b > c; // (5 > 3) and (3 > 2) = true
    std.debug.print("a > b and b > c = {}\n", .{result3});

    // 逻辑非优先于逻辑与
    const result4: bool = !(a > b) and b > c; // !(5 > 3) and (3 > 2) = false
    std.debug.print("!(a > b) and b > c = {}\n", .{result4});
}
```


编译输出结果为：


```
a + b * c = 11
(a + b) * c = 16
a > b and b > c = true
!(a > b) and b > c = false
```










	  AI 思考中...





			** [Zig 流程控制](https://www.runoob.com/zig-if.html)
			[Zig 函数](https://www.runoob.com/zig-fn.html) **













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