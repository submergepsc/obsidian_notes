# Zig 循环

- Source: https://www.runoob.com/zig/zig-loop.html

在 Zig 中，循环结构包括 `while` 循环和 `for` 循环。每种循环都有其特定的语法和用法。下面详细介绍这两种循环结构，包括其语法、说明和实例。


## 1、while 循环


### 语法



```
while (condition) : (increment) {
    // code block
}
```



- `condition`：一个布尔表达式，只要它为 `true`，循环就会继续执行。
- `increment`（可选）：一个在每次循环结束后执行的表达式。


### 说明


`while` 循环在每次迭代前检查条件。如果条件为 `true`，则执行循环体中的代码。循环体执行完毕后，执行 `increment` 表达式（如果有）。然后再次检查条件，直到条件为 `false`。


### 实例


## 实例


```zig
const std = @import("std");

pub fn main() void {
    var i: i32 = 0;
    while (i < 5) : (i += 1) {
        std.debug.print("i: {}\n", .{i});
    }
}
```



解析：


- 初始化变量 `i` 为 0。
- 只要 `i` 小于 5，循环体就会执行。
- 每次循环结束后，`i` 自增 1。

代码编译执行结果为：


```
i: 0
i: 1
i: 2
i: 3
i: 4
```



## 2、for 循环


### 语法



```
for (collection) |item, index| {
    // code block
}
```



- `collection`：一个数组、切片或其他可迭代的集合。
- `item`：在每次迭代中，集合的当前元素。
- `index`（可选）：当前元素的索引。


### 说明


`for` 循环用于遍历一个集合中的每个元素。在每次迭代中，集合的当前元素被赋值给 `item`，并执行循环体中的代码。


### 实例


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const array = [5]i32{ 1, 2, 3, 4, 5 };
    var index: usize = 0; // 索引变量需要声明类型
    for (array) |item| {
        std.debug.print("index: {}, item: {}\n", .{ index, item });
        index += 1; // 更新索引
    }
}
```



解析：


- 定义了一个包含 5 个整数的数组。
- 使用 `for` 循环遍历数组中的每个元素，并将元素值赋给 `item`，索引赋给 `index`。
- 在循环体中，打印每个元素的值和索引。

代码编译执行结果为：


```
index: 0, item: 1
index: 1, item: 2
index: 2, item: 3
index: 3, item: 4
index: 4, item: 5
```



## 3、continue 和 break


### 语法


- `continue`：跳过当前迭代并继续下一次迭代。
- `break`：终止循环。


### 说明


`continue` 用于跳过当前迭代中剩余的代码，并立即开始下一次迭代。`break` 用于终止整个循环。


### 实例


## 实例


```zig
const std = @import("std");

pub fn main() void {
    var i: i32 = 0;
    while (i < 10) : (i += 1) {
        if (i == 5) {
            continue; // 跳过 i 等于 5 的那次迭代
        }
        if (i == 8) {
            break; // 终止循环
        }
        std.debug.print("i: {}\n", .{i});
    }
}
```



解析：


- 当 `i` 等于 5 时，`continue` 跳过该次迭代。
- 当 `i` 等于 8 时，`break` 终止循环。

代码编译执行结果为：


```
i: 0
i: 1
i: 2
i: 3
i: 4
i: 6
i: 7
```



## 5、嵌套循环


### 语法



```
for (outer_collection) |outer_item| {
    for (inner_collection) |inner_item| {
        // code block
    }
}
```



### 说明


在一个循环体内包含另一个循环称为嵌套循环。外层循环的每次迭代中，都会执行内层循环。


### 实例


## 实例


```zig
const std = @import("std");

pub fn main() void {
    // 声明一个包含三个字符串的数组
    const letters = [_][]const u8{ "A", "B", "C" };
    // 遍历数组
    for (letters) |letter| {
        var count: i32 = 0; // 声明计数器
        // 使用 while 循环来打印每个字母和计数
        while (count < 3) : (count += 1) {
            std.debug.print("{s} - {}\n", .{ letter, count });
        }
    }
}
```



解析：


- 外层 `for` 循环遍历字母数组。
- 内层 `while` 循环执行 3 次，打印字母和计数。


代码编译执行结果为：


```
A - 0
A - 1
A - 2
B - 0
B - 1
B - 2
C - 0
C - 1
C - 2
```



## 6、更多循环


### 无限循环

可以使用 while 循环创建一个无限循环，只要条件始终为真：


## 实例


```zig
pub fn main() void {
    while (true) {
        // 代码块
        // 必须包含某种退出机制，否则程序将永远运行
    }
}
```


### 范围循环

Zig 还允许你使用范围来循环，这在某些情况下可以简化代码：


## 实例


```zig
pub fn main() void {
    for (0..10) |i| {
        std.debug.print("i: {}\n", .{i});
    }
}
```


### 标签循环


Zig 支持标签循环，允许你命名循环，这在嵌套循环中非常有用：


## 实例


```zig
pub fn main() void {
    loop: while (true) {
        while (true) {
            std.debug.print("Inside nested loop\n");
            break :loop; // 退出外部循环
        }
    }
}
```









	  AI 思考中...





			** [Zig 变量和常量](https://www.runoob.com/zig-var-const.html)
			[Zig 流程控制](https://www.runoob.com/zig-if.html) **













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