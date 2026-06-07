# Zig 流程控制

- Source: https://www.runoob.com/zig/zig-if.html

Zig 编程语言流程控制语句通过程序设定一个或多个条件语句来设定。

在条件为 true 时执行指定程序代码，在条件为 false 时执行其他指定代码。


以下是典型的流程控制流程图：

![](https://www.runoob.com/wp-content/uploads/2015/12/if.png)


Zig 提供了以下控制结构语句：


## if 语句


### 语法

基本的 if 语句包含一个条件和一个与之相关联的代码块，如果条件为真（true），则执行代码块。


```
if (<condition) {
    // 如果 condition 为 true，执行这里的代码
}
```


if-else 语句在基本 if 语句的基础上增加了一个 else 分支，如果 if 中的条件为假（false），则执行 else 分支中的代码。


```
if (<condition>) {
    // 如果 condition 为 true，执行这里的代码
} else {
    // 如果 condition 为 false，执行这里的代码
}
```


**condition：**一个布尔表达式。如果条件为 true，则执行第一个代码块；否则执行 else 代码块。


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const x: i32 = 10;
    if (x > 5) {
        std.debug.print("x is greater than 5\n", .{});
    } else {
        std.debug.print("x is not greater than 5\n", .{});
    }
}
```


编译执行输出结果为：


```
x is greater than 5
```


## if-else...else 语句

### 语法


支持多个条件检查，按顺序检查每个条件，直到某个条件为 true 并执行相应的代码块。


## 实例


```zig
if (condition1) {
    // 如果 condition1 为 true，执行这里的代码
} else if (condition2) {
    // 如果 condition2 为 true，执行这里的代码
} else {
    // 如果所有条件为 false，执行这里的代码
}
```


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const x: i32 = 10;
    if (x > 10) {
        std.debug.print("x is greater than 10\n", .{});
    } else if (x == 10) {
        std.debug.print("x is equal to 10\n", .{});
    } else {
        std.debug.print("x is less than 10\n", .{});
    }
}
```


编译执行输出结果为：


```
x is equal to 10
```


## 嵌套的 if-else

if-else 语句可以嵌套使用，这意味着你可以在 if 或 else 分支中再包含一个 if 语句。


```
if (<条件1>) {
    // 如果条件1为真，执行这里的代码
    if (<条件2>) {
        // 如果条件1和条件2都为真，执行这里的代码
    } else {
        // 如果条件1为真但条件2为假，执行这里的代码
    }
} else {
    // 如果条件1为假，执行这里的代码
}
```


## 实例


```zig
const std = @import("std");

pub fn main() void {
    const input = 5; // 假设这是用户的输入
    const max_value = 10;

    if (input > max_value) {
        std.debug.print("Input is greater than {}\n", .{max_value});
    } else if (input == max_value) {
        std.debug.print("Input is equal to {}\n", .{max_value});
    } else {
        if (input < 5) {
            std.debug.print("Input is less than 5\n");
        } else {
            std.debug.print("Input is between 5 and {}\n", .{max_value});
        }
    }
}
```


编译执行输出结果为：


```
Input is between 5 and 10
```


---

## if 语句中的类型推导


Zig 编译器可以推导出 if 语句中变量的类型，如果条件表达式的结果是一个布尔值。


```
const condition = true;
if (condition) {
    // 这里 condition 的类型是 bool，编译器自动推导
}
```










	  AI 思考中...





			** [Zig 循环](https://www.runoob.com/zig-loop.html)
			[Zig 运算符](https://www.runoob.com/zig-operators.html) **













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