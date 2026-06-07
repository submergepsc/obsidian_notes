# Zig 结构体和枚举

- Source: https://www.runoob.com/zig/zig-struct-enum.html

在 Zig 编程语言中，结构体（struct）和枚举（enum）是两种基本的数据类型。

结构体和枚举是定义和使用自定义数据类型的两种主要方式。


结构体和枚举提供了更高层次的数据组织和类型安全，适用于不同的编程场景。

- **结构体（Struct）**：用于将相关变量组合成一个复合数据类型。结构体可以包含字段和方法，适用于组织复杂的数据。
- **枚举（Enum）**：用于定义一组命名的常量，可以是无值或带值的枚举。枚举适用于表示有限的离散值。


---


## 结构体（Struct）


结构体是一种复合数据类型，它允许将多个不同类型的数据项组合成一个单一的类型。


Zig 中结构体的语法如下：


```
const structName = struct {
    field1: FieldType1,
    field2: FieldType2,
    // 其他字段
};
```


以下代码中，MyStruct 是一个结构体类型，它有三个字段：field1 是一个 32 位整数，field2 是一个双精度浮点数，field3 是一个指向字节数组的指针。


```
struct MyStruct {
    field1: i32,
    field2: f64,
    field3: []const u8,
}
```


## 实例


```zig
const std = @import("std");

// 定义一个结构体
const Person = struct {
    name: []const u8,
    age: u32,
};

pub fn main() void {
    // 创建结构体实例
    const person = Person{
        .name = "Alice",
        .age = 30,
    };

    // 访问结构体字段并正确格式化
    std.debug.print("Name: {s}\n", .{person.name}); // 使用 {s} 格式化切片
    std.debug.print("Age: {}\n", .{person.age});
}
```


编译执行以上代码，输出结果为：


```
Name: Alice
Age: 30
```


要修改结构体中的字段，确保你使用 var 来定义结构体实例，以便能够修改字段值。如果你使用 const 定义结构体实例，则不能修改其字段值。


## 实例


```zig
const std = @import("std");

// 定义一个结构体
const Person = struct {
    name: []const u8,
    age: u32,
};

pub fn main() void {
    // 创建结构体实例
    var person = Person{
        .name = "Alice",
        .age = 30,
    };

    // 输出初始值
    std.debug.print("Initial Name: {s}\n", .{person.name});
    std.debug.print("Initial Age: {}\n", .{person.age});

    // 修改结构体字段的值
    person.name = "Bob";
    person.age = 35;

    // 输出修改后的值
    std.debug.print("Modified Name: {s}\n", .{person.name});
    std.debug.print("Modified Age: {}\n", .{person.age});
}
```


编译执行以上代码，输出结果为：


```
Initial Name: Alice
Initial Age: 30
Modified Name: Bob
Modified Age: 35
```


### 方法

在 Zig 中，结构体方法通过 fn 关键字定义，类似于其他编程语言中的类方法。


## 实例


```zig
const std = @import("std");

const Rectangle = struct {
    width: u32,
    height: u32,

    // 计算面积的方法
    fn area(self: Rectangle) u32 {
        return self.width * self.height;
    }
};

pub fn main() void {
    var rect = Rectangle{
        .width = 10,
        .height = 5,
    };

    // 调用结构体方法
    std.debug.print("Area: {}\n", .{rect.area()});
}
```


编译执行以上代码，输出结果为：


```
Area: 50
```


---


## 枚举（Enum）


枚举是一种数据类型，它由一组固定的常量值组成。


Zig 中枚举的语法如下：


```
const enumName = enum {
    Variant1,
    Variant2,
    // 其他变体
};
```


以下代码中，MyEnum 是一个枚举类型，它有三个可能的值：Option1、Option2 和 Option3。


```
enum MyEnum {
    Option1,
    Option2,
    Option3,
}
```


## 实例


```zig
const std = @import("std");

// 定义一个枚举
const Color = enum {
    Red,
    Green,
    Blue,
};

pub fn main() void {
    // 使用枚举
    const favoriteColor = Color.Green;

    switch (favoriteColor) {
        Color.Red => std.debug.print("Red\n", .{}),
        Color.Green => std.debug.print("Green\n", .{}),
        Color.Blue => std.debug.print("Blue\n", .{}),
    }
}
```


编译执行以上代码，输出结果为：


```
Green
```


### 带值的枚举

Zig 允许为枚举的每个变体指定具体的值，这可以用来表示更多的信息或进行比较。


## 实例


```zig
const std = @import("std");

// 定义一个带值的枚举
const Status = enum(u32) {
    Pending = 1,
    InProgress = 2,
    Completed = 3,
};

pub fn main() void {
    const taskStatus = Status.InProgress;

    switch (taskStatus) {
        Status.Pending => std.debug.print("Pending\n", .{}),
        Status.InProgress => std.debug.print("InProgress\n", .{}),
        Status.Completed => std.debug.print("Completed\n", .{}),
    }
}
```


编译执行以上代码，输出结果为：


```
InProgress
```


### 使用枚举作为字段

枚举可以用作结构体字段，使得结构体更加灵活和功能强大。


## 实例


```zig
const std = @import("std");

const Status = enum {
    Active,
    Inactive,
    Suspended,
};

const User = struct {
    name: []const u8,
    status: Status,
};

pub fn main() void {
    // 创建 User 实例
    const user = User{
        .name = "Alice",
        .status = Status.Active,
    };

    // 输出 User 的 name 字段
    std.debug.print("User: {s}\n", .{user.name}); // 使用 {s} 格式化切片

    // 使用 switch 语句根据 status 输出不同的状态
    switch (user.status) {
        Status.Active => std.debug.print("Status: Active\n", .{}),
        Status.Inactive => std.debug.print("Status: Inactive\n", .{}),
        Status.Suspended => std.debug.print("Status: Suspended\n", .{}),
    }
}
```


编译执行以上代码，输出结果为：


```
User: Alice
Status: Active
```









	  AI 思考中...





			** [Zig 数组和切片](https://www.runoob.com/zig-array-slice.html)
			[zig 错误处理](https://www.runoob.com/zig-error.html) **













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