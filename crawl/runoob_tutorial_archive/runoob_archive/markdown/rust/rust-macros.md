# Rust 宏

- Source: https://www.runoob.com/rust/rust-macros.html

Rust 宏（Macros）是一种在编译时生成代码的强大工具，它允许你在编写代码时创建自定义语法扩展。


宏（Macro）是一种在代码中进行元编程（Metaprogramming）的技术，它允许在编译时生成代码，宏可以帮助简化代码，提高代码的可读性和可维护性，同时允许开发者在编译时执行一些代码生成的操作。


宏在 Rust 中有两种类型：声明式宏（Declarative Macros）和过程宏（Procedural Macros）。


本文主要介绍声明式宏。


### 宏的定义

在 Rust 中，使用 **macro_rules!** 关键字来定义声明式宏。


```
macro_rules! my_macro {
    // 模式匹配和展开
    ($arg:expr) => {
        // 生成的代码
        // 使用 $arg 来代替匹配到的表达式
    };
}
```


声明式宏使用 **macro_rules!** 关键字进行定义，它们被称为 **"macro_rules"** 宏。这种宏的定义是基于模式匹配的，可以匹配代码的结构并根据匹配的模式生成相应的代码。这样的宏在不引入新的语法结构的情况下，可以用来简化一些通用的代码模式。


下面是一个简单的宏定义的例子：


## 实例


```rust
// 宏的定义
macro_rules! greet {
    // 模式匹配
    ($name:expr) => {
        // 宏的展开
        println!("Hello, {}!", $name);
    };
}

fn main() {
    // 调用宏
    greet!("World");
}
```


**说明**

- **模式匹配：**宏通过模式匹配来匹配传递给宏的代码片段，模式是宏规则的左侧部分，用于捕获不同的代码结构。
- **规则：**宏规则是一组由 **$** 引导的模式和相应的展开代码，规则由分号分隔。
- ** 宏的展开：**当宏被调用时，匹配的模式将被替换为相应的展开代码，展开代码是宏规则的右侧部分。


### 实例

下面是一个更复杂的例子，演示了如何使用宏创建一个简单的 **vec!** 宏，以便更方便地创建 Vec：


## 实例


```rust
// 宏的定义
macro_rules! vec {
    // 基本情况，空的情况
    () => {
        Vec::new()
    };

    // 递归情况，带有元素的情况
    ($($element:expr),+ $(,)?) => {
        {
            let mut temp_vec = Vec::new();
            $(
                temp_vec.push($element);
            )+
            temp_vec
        }
    };
}

fn main() {
    // 调用宏
    let my_vec = vec![1, 2, 3];
    println!("{:?}", my_vec); // 输出: [1, 2, 3]

    let empty_vec = vec![];
    println!("{:?}", empty_vec); // 输出: []
}
```


在这个例子中，**vec!** 宏使用了模式匹配，以及 **$($element:expr),+ $(,)?)** 这样的语法来捕获传递给宏的元素，并用它们创建一个 Vec。

注意，$**(,)?)** 用于处理末尾的逗号，使得在不同的使用情境下都能正常工作。


---


## 过程宏（Procedural Macros）


过程宏是一种更为灵活和强大的宏，允许在编译时通过自定义代码生成过程来操作抽象语法树（AST）。过程宏在功能上更接近于函数，但是它们在编写和使用上更加复杂。


过程宏的类型：


- **派生宏（Derive Macros）**：用于自动实现trait（比如`Copy`、`Debug`）的宏。
- **属性宏（Attribute Macros）**：用于在声明上附加额外的元数据，如`#[derive(Debug)]`。


过程宏的实现通常需要使用 proc_macro 库提供的功能，例如 TokenStream 和 TokenTree，以便更直接地操纵源代码。








	  AI 思考中...





			** [Rust 并发编程](https://www.runoob.com/rust-concurrency.html)
			[Rust 迭代器](https://www.runoob.com/rust-iter.html) **













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