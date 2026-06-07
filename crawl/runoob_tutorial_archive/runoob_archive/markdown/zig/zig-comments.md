# Zig 注释

- Source: https://www.runoob.com/zig/zig-comments.html

注释不会被编译器处理，只用于在代码中添加说明和解释，帮助开发者理解代码逻辑。


在 Zig 中，注释有两种形式：单行注释和多行注释。


## 1、单行注释

单行注释以 **//** 开头，注释内容从 **//** 开始到行末结束。


## 实例


```zig
const std = @import("std");

// 这是一个单行注释
pub fn main() void {
    std.debug.print("Hello, World!\n", .{});
}
```


## 2、多行注释


多行注释以 **/*** 开始，以 ***/** 结束，注释内容可以跨越多行。


## 实例


```zig
const std = @import("std");

/*
  这是一个多行注释
  可以跨越多行
*/
pub fn main() void {
    std.debug.print("Hello, World!\n", .{});
}
```


## 注释使用

以下是一个包含单行注释和多行注释的完整示例，演示了如何在代码中添加注释。


## 实例


```zig
const std = @import("std");

// 主函数
pub fn main() void {
    // 调用标准库的 debug.print 函数打印 "Hello, World!"
    std.debug.print("Hello, World!\n", .{});

    /*
      这段代码用于演示 Zig 的基本语法
      包括函数定义、标准库使用和注释
    */

    const a: i32 = 10; // 定义一个整数常量 a，值为 10
    const b: i32 = 20; // 定义另一个整数常量 b，值为 20

    // 调用 add 函数并打印结果
    const result = add(a, b);
    std.debug.print("Result: {}\n", .{result});
}

// 一个简单的加法函数
fn add(a: i32, b: i32) i32 {
    return a + b;
}
```


- 单行注释被用来解释代码中的单个行或局部代码段。
- 多行注释被用来对较大段的代码进行说明。








	  AI 思考中...





			** [Zig 基本语法](https://www.runoob.com/zig-basic-syntax.html)
			[Zig 数据类型](https://www.runoob.com/zig-datatype.html) **













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