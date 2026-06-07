# Zig 数据类型

- Source: https://www.runoob.com/zig/zig-datatype.html

Zig 支持多种数据类型，涵盖了整数、浮点数、布尔值、字符、数组、切片、结构体、枚举、联合体和指针等。


下表是 Zig 中各种数据类型的说明：


| 数据类型类别 | 数据类型示例 | 描述 |
| --- | --- | --- |
| 整数类型 | i8, i16, i32, i64, isize | 有符号整数类型，isize是平台相关的大小。 |
| 无符号整数 | u8, u16, u32, u64, usize | 无符号整数类型，usize是平台相关的大小。 |
| 浮点数 | f16, f32, f64, f128 | IEEE 浮点数类型。 |
| 布尔类型 | bool | 布尔类型，值为true或false。 |
| 字符类型 | char | Unicode 标量值。 |
| 复合类型 | array, vector | 固定大小数组和可变大小数组。 |
| 指针类型 | *T, *const T, *mut T | 指向T类型值的指针，*const为只读，*mut为可变。 |
| 引用类型 | &T, &const T, &mut T | 对T类型值的引用，&const为只读，&mut为可变。 |
| 元组类型 | (T1, T2, ...) | 包含固定数量和类型的值的有序集合。 |
| 可选类型 | ?T | 可以是null或者T类型值。 |
| 错误集合类型 | error{...} | 包含错误值的枚举类型。 |
| 函数类型 | fn(T1, T2, ...) -> R | 接受参数并返回结果的函数类型。 |
| 结构体类型 | struct { ... } | 包含多个字段的复合数据类型。 |
| 枚举类型 | enum { ... } | 固定数量的命名值的集合。 |
| 联合体类型 | union { ... } | 可以存储多种不同类型值的类型，但一次只能存储一个。 |
| 别名类型 | alias T = U | T是U的别名。 |


### 1、整数类型


Zig 提供了多种整数类型，包括有符号和无符号整数，大小从 8 位到 64 位不等。


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const a: i8 = -128; // 8-bit signed integer
    const b: u8 = 255;  // 8-bit unsigned integer
    const c: i32 = -2147483648; // 32-bit signed integer
    const d: u64 = 18446744073709551615; // 64-bit unsigned integer

    std.debug.print("a: {}, b: {}, c: {}, d: {}\n", .{a, b, c, d});
}
```


2、浮点数类型

Zig 支持 f32 和 f64 两种浮点数类型。


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const pi: f32 = 3.14;   // 32-bit floating point
    const e: f64 = 2.71828; // 64-bit floating point

    std.debug.print("pi: {}, e: {}\n", .{pi, e});
}
```


### 3、布尔类型

布尔类型使用 bool 表示，取值可以是 true 或 false。


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const is_true: bool = true;
    const is_false: bool = false;

    std.debug.print("is_true: {}, is_false: {}\n", .{is_true, is_false});
}
```


### 4、字符类型

字符类型使用 u8 来表示单个字符。


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const letter: u8 = 'A';

    std.debug.print("letter: {}\n", .{letter});
}
```


### 5、数组和切片

数组是固定大小的，切片则是动态大小的数组。


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const array: [5]i32 = [5]i32{1, 2, 3, 4, 5}; // 固定大小数组
    const slice: []const i32 = array[1..4]; // 切片

    std.debug.print("array: {}, slice: {}\n", .{array, slice});
}
```


### 6、结构体

结构体用 struct 定义，允许你创建复杂的数据类型。


## 实例


```zig
const std = @import("std");

const Point = struct {
    x: i32,
    y: i32,
};

pub fn main() void {
    const p = Point{ .x = 10, .y = 20 };

    std.debug.print("Point: ({}, {})\n", .{p.x, p.y});
}
```


### 7、枚举


枚举用 enum 定义，允许你创建有命名值的类型。


## 实例


```zig
const std = @import("std");

const Color = enum {
    Red,
    Green,
    Blue,
};

pub fn main() void {
    const color: Color = Color.Green;

    std.debug.print("Color: {}\n", .{color});
}
```


### 8、联合体

联合体用 union 定义，允许你创建一个可以存储不同类型值的变量。


## 实例


```zig
const std = @import("std");

const Number = union(enum) {
    Int: i32,
    Float: f32,
};

pub fn main() void {
    const num: Number = Number{ .Int = 10 };

    switch (num) {
        Number.Int => std.debug.print("Integer: {}\n", .{num.Int}),
        Number.Float => std.debug.print("Float: {}\n", .{num.Float}),
    }
}
```


### 9、指针

指针用 ***** 定义，可以指向特定类型的变量。


## 实例


```zig
const std = @import("std");

pub fn main() void {
    var a: i32 = 10;
    const p: *i32 = &a; // 指向 a 的指针

    std.debug.print("Value: {}, Pointer: {}\n", .{a, p.*});
}
```









	  AI 思考中...





			** [Zig 注释](https://www.runoob.com/zig-comments.html)
			[Zig 变量和常量](https://www.runoob.com/zig-var-const.html) **













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