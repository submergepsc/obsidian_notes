# Rust 循环

- Source: https://www.runoob.com/rust/rust-loop.html

Rust 除了灵活的条件语句以外，循环结构的设计也十分成熟。这一点作为身经百战的开发者应该能感觉出来。


### while 循环


while 循环是最典型的条件语句循环：


## 实例


```rust
fn main() {
    let mut number = 1;
    while number != 4 {
        println!("{}", number);
        number += 1;
    }
    println!("EXIT");
}
```


运行结果：



```
1
2
3
EXIT
```


Rust 语言到此教程编撰之日还没有 do-while 的用法，但是 do 被规定为保留字，也许以后的版本中会用到。


在 C 语言中 for 循环使用三元语句控制循环，但是 Rust 中没有这种用法，需要用 while 循环来代替：


## C 语言


```rust
int i;
for (i = 0; i < 10; i++) {
    // 循环体
}
```


## Rust


```rust
let mut i = 0;
while i < 10 {
    // 循环体
    i += 1;
}
```


### for 循环



for 循环是最常用的循环结构，常用来遍历一个线性数据结构（比如数组）。for 循环遍历数组：


## 实例


```rust
fn main() {
    let a = [10, 20, 30, 40, 50];
    for i in a.iter() {
        println!("值为 : {}", i);
    }
}
```


运行结果：


```
值为 : 10
值为 : 20
值为 : 30
值为 : 40
值为 : 50
```


这个程序中的 for 循环完成了对数组 a 的遍历。a.iter() 代表 a 的迭代器（iterator），在学习有关于对象的章节以前不做赘述。


当然，for 循环其实是可以通过下标来访问数组的：


## 实例


```rust
fn main() {
let a = [10, 20, 30, 40, 50];
    for i in 0..5 {
        println!("a[{}] = {}", i, a[i]);
    }
}
```


运行结果：


```
a[0] = 10
a[1] = 20
a[2] = 30
a[3] = 40
a[4] = 50
```


### loop 循环


身经百战的开发者一定遇到过几次这样的情况：某个循环无法在开头和结尾判断是否继续进行循环，必须在循环体中间某处控制循环的进行。如果遇到这种情况，我们经常会在一个 while (true) 循环体里实现中途退出循环的操作。


Rust 语言有原生的无限循环结构 —— loop：


## 实例


```rust
fn main() {
    let s = ['R', 'U', 'N', 'O', 'O', 'B'];
    let mut i = 0;
    loop {
        let ch = s[i];
        if ch == 'O' {
            break;
        }
        println!("\'{}\'", ch);
        i += 1;
    }
}
```


运行结果：


```
'R'
'U'
'N'
```


loop 循环可以通过 break 关键字类似于 return 一样使整个循环退出并给予外部一个返回值。这是一个十分巧妙的设计，因为 loop 这样的循环常被用来当作查找工具使用，如果找到了某个东西当然要将这个结果交出去：


## 实例


```rust
fn main() {
    let s = ['R', 'U', 'N', 'O', 'O', 'B'];
    let mut i = 0;
    let location = loop {
        let ch = s[i];
        if ch == 'O' {
            break i;
        }
        i += 1;
    };
    println!(" \'O\' 的索引为 {}", location);
}
```


运行结果：


```
'O' 的索引为 3
```









	  AI 思考中...





			** [Rust 条件语句](https://www.runoob.com/rust-conditions.html)
			[Rust 所有权](https://www.runoob.com/rust-ownership.html) **













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