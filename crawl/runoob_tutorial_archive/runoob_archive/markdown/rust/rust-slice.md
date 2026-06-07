# Rust Slice（切片）类型

- Source: https://www.runoob.com/rust/rust-slice.html

切片（Slice）是对数据值的部分引用。

切片这个名字往往出现在生物课上，我们做样本玻片的时候要从生物体上获取切片，以供在显微镜上观察。在 Rust 中，切片的意思大致也是这样，只不过它从数据取材引用。


### 字符串切片

最简单、最常用的数据切片类型是字符串切片（String Slice）。


## 实例


```rust
fn main() {
    let s = String::from("broadcast");

    let part1 = &s[0..5];
    let part2 = &s[5..9];

    println!("{}={}+{}", s, part1, part2);
}
```


运行结果：


```
broadcast=broad+cast
```


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-slice1.png)

上图解释了字符串切片的原理（注：Rust 中的字符串类型实质上记录了字符在内存中的起始位置和其长度，我们暂时了解到这一点）。

使用 **..** 表示范围的语法在循环章节中出现过。**x..y** 表示 **[x, y)** 的数学含义。**..** 两边可以没有运算数：


```
..y 等价于 0..y
x.. 等价于位置 x 到数据结束
.. 等价于位置 0 到结束
```


**注意：**到目前为止，尽量不要在字符串中使用非英文字符，因为编码的问题。具体原因会在"字符串"章节叙述。


被切片引用的字符串禁止更改其值：


## 实例


```rust
fn main() {
    let mut s = String::from("runoob");
    let slice = &s[0..3];
    s.push_str("yes!"); // 错误
    println!("slice = {}", slice);
}
```


这段程序不正确。

s 被部分引用，禁止更改其值。

实际上，到目前为止你一定疑惑为什么每一次使用字符串都要这样写**String::from("runoob")** ，直接写 **"runoob"** 不行吗？


事已至此我们必须分辨这两者概念的区别了。在 Rust 中有两种常用的字符串类型：str 和 String。str 是 Rust 核心语言类型，就是本章一直在讲的字符串切片（String Slice），常常以引用的形式出现（&str;）。

凡是用双引号包括的字符串常量整体的类型性质都是 **&str;**：


```
let s = "hello";
```


这里的 s 就是一个 &str; 类型的变量。

String 类型是 Rust 标准公共库提供的一种数据类型，它的功能更完善——它支持字符串的追加、清空等实用的操作。String 和 str 除了同样拥有一个字符开始位置属性和一个字符串长度属性以外还有一个容量（capacity）属性。

String 和 str 都支持切片，切片的结果是 &str; 类型的数据。

注意：切片结果必须是引用类型，但开发者必须自己明示这一点:


```
let slice = &s[0..3];
```


有一个快速的办法可以将 String 转换成 &str;：


```
let s1 = String::from("hello");
let s2 = &s1[..];
```


### 非字符串切片

除了字符串以外，其他一些线性数据结构也支持切片操作，例如数组：


## 实例


```rust
fn main() {
    let arr = [1, 3, 5, 7, 9];
    let part = &arr[0..3];
    for i in part.iter() {
        println!("{}", i);
    }
}
```


运行结果：


```
1
3
5
```










	  AI 思考中...





			** [Rust 所有权](https://www.runoob.com/rust-ownership.html)
			[Rust 结构体](https://www.runoob.com/rust-struct.html) **













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