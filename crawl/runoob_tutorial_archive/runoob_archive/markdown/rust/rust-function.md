# Rust 函数

- Source: https://www.runoob.com/rust/rust-function.html

函数在 Rust 语言中是普遍存在的。

通过之前的章节已经可以了解到 Rust 函数的基本形式：


```
fn <函数名> ( <参数> ) <函数体>
```


其中 Rust 函数名称的命名风格是小写字母以下划线分割：


## 实例


```rust
fn main() {
    println!("Hello, world!");
    another_function();
}

fn another_function() {
    println!("Hello, runoob!");
}
```


运行结果：


```
Hello, world!
Hello, runoob!
```


注意，我们在源代码中的 main 函数之后定义了another_function。 Rust不在乎您在何处定义函数，只需在某个地方定义它们即可。


### 函数参数


Rust 中定义函数如果需要具备参数必须声明参数名称和类型：


## 实例


```rust
fn main() {
    another_function(5, 6);
}

fn another_function(x: i32, y: i32) {
    println!("x 的值为 : {}", x);
    println!("y 的值为 : {}", y);
}
```


运行结果：


```
x 的值为 : 5
y 的值为 : 6
```


### 函数体的语句和表达式


Rust 函数体由一系列可以以表达式（Expression）结尾的语句（Statement）组成。到目前为止，我们仅见到了没有以表达式结尾的函数，但已经将表达式用作语句的一部分。


语句是执行某些操作且没有返回值的步骤。例如：


```
let a = 6;
```


这个步骤没有返回值，所以以下语句不正确：


```
let a = (let b = 2);
```


表达式有计算步骤且有返回值。以下是表达式（假设出现的标识符已经被定义）：


```
a = 7
b + 2
c * (a + b)
```


Rust 中可以在一个用 **{}** 包括的块里编写一个较为复杂的表达式：


## 实例


```rust
fn main() {
    let x = 5;

    let y = {
        let x = 3;
        x + 1
    };

    println!("x 的值为 : {}", x);
    println!("y 的值为 : {}", y);
}
```


运行结果：


```
x 的值为 : 5
y 的值为 : 4
```


很显然，这段程序中包含了一个表达式块：


```
{
    let x = 3;
    x + 1
};
```


而且在块中可以使用函数语句，最后一个步骤是表达式，此表达式的结果值是整个表达式块所代表的值。这种表达式块叫做函数体表达式。


注意：**x + 1** 之后没有分号，否则它将变成一条语句！


这种表达式块是一个合法的函数体。而且在 Rust 中，函数定义可以嵌套：


## 实例


```rust
fn main() {
    fn five() -> i32 {
        5
    }
    println!("five() 的值为: {}", five());
}
```


### 函数返回值


在上一个嵌套的例子中已经显示了 Rust 函数声明返回值类型的方式：在参数声明之后用 **->** 来声明函数返回值的类型（不是 **:** ）。


在函数体中，随时都可以以 return 关键字结束函数运行并返回一个类型合适的值。这也是最接近大多数开发者经验的做法：


## 实例


```rust
fn add(a: i32, b: i32) -> i32 {
    return a + b;
}
```


但是 Rust 不支持自动返回值类型判断！如果没有明确声明函数返回值的类型，函数将被认为是"纯过程"，不允许产生返回值，return 后面不能有返回值表达式。这样做的目的是为了让公开的函数能够形成可见的公报。


**注意：**函数体表达式并不能等同于函数体，它不能使用 **return**** 关键字。









	  AI 思考中...





			** [Rust 数据类型](https://www.runoob.com/rust-data-types.html)
			[Rust 注释](https://www.runoob.com/rust-comments.html) **













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