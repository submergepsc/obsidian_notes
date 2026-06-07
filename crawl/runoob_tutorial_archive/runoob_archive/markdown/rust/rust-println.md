# Rust 输出到命令行

- Source: https://www.runoob.com/rust/rust-println.html

在正式学习 Rust 语言以前，我们需要先学会怎样输出一段文字到命令行，这几乎是学习每一门语言之前必备的技能，因为输出到命令行几乎是语言学习阶段程序表达结果的唯一方式。


在之前的 Hello, World 程序中大概已经告诉了大家输出字符串的方式，但并不全面，大家可能很疑惑为什么 println!( "Hello World") 中的 println 后面还有一个 **!** 符号，难道 Rust 函数之后都要加一个感叹号？显然并不是这样。println 不是一个函数，而是一个宏规则。这里不需要更深刻的挖掘宏规则是什么，后面的章节中会专门介绍，并不影响接下来的一段学习。


Rust 输出文字的方式主要有两种：**println!()** 和 **print!()**。这两个"函数"都是向命令行输出字符串的方法，区别仅在于前者会在输出的最后附加输出一个换行符。当用这两个"函数"输出信息的时候，第一个参数是格式字符串，后面是一串可变参数，对应着格式字符串中的"占位符"，这一点与 C 语言中的 printf 函数很相似。但是，Rust 中格式字符串中的占位符不是 **"% + 字母"** 的形式，而是一对 **{}**。


## 实例：runoob.rs 文件


```rust
fn main() {
    let a = 12;
    println!("a is {}", a);
}
```


使用 **rustc** 命令编译 runoob.rs 文件：


```
$ rustc runoob.rs   # 编译 runoob.rs 文件
```


编译后会生成 **runoob** 可执行文件：


```
$ ./runoob    # 执行 runoob
```


以上程序的输出结果是：



```
a is 12
```




如果我想把 a 输出两遍，那岂不是要写成：


```
println!("a is {}, a again is {}", a, a);
```


其实有更好的写法：


```
println!("a is {0}, a again is {0}", a);
```


在 **{}** 之间可以放一个数字，它将把之后的可变参数当作一个数组来访问，下标从 0 开始。


如果要输出 **{** 或 **}** 怎么办呢？格式字符串中通过 **{{** 和 **}}** 分别转义代表 { 和 }。但是其他常用转义字符与 C 语言里的转义字符一样，都是反斜杠开头的形式。



```
fn main() {
    println!("{{}}");
}
```


以上程序的输出结果是：


```
{}
```









	  AI 思考中...





			** [Cargo 教程](https://www.runoob.com/cargo-tutorial.html)
			[Rust 基础语法](https://www.runoob.com/rust-basic-syntax.html) **













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