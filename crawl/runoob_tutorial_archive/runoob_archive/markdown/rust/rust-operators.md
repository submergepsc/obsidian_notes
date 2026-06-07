# Rust 运算符

- Source: https://www.runoob.com/rust/rust-operators.html

在 Rust 中，无论是简单的数值计算、逻辑判断，还是更复杂的模式匹配和位操作，运算符都承担着核心的角色。


Rust 既支持我们熟悉的 C 系语言常见运算符，也提供了一些独特的操作符号。熟练掌握这些运算符，不仅能让代码更简洁高效，也能帮助你更好地理解 Rust 的语义。


---


## 1、算术运算符


| 运算符 | 说明 | 示例 | 结果 |
| --- | --- | --- | --- |
| + | 加法 | 5 + 2 | 7 |
| - | 减法 | 5 - 2 | 3 |
| * | 乘法 | 5 * 2 | 10 |
| / | 除法（整除） | 5 / 2 | 2 （整数） |
| % | 取余 | 5 % 2 | 1 |


## 实例


```rust
fn main() {
    let a = 10;
    let b = 3;

    println!("a + b = {}", a + b);
    println!("a - b = {}", a - b);
    println!("a * b = {}", a * b);
    println!("a / b = {}", a / b);
    println!("a % b = {}", a % b);
}
```


**输出：**


```
a + b = 13
a - b = 7
a * b = 30
a / b = 3
a % b = 1
```


Rust 没有 ****** 或 **^** 这样的乘方运算符（注意：**^** 是按位异或），如果要做乘方，需要使用内置的 pow 或 powf 方法：


- **整数类型**使用 `.pow(exp: u32)`
- **浮点类型**使用 `.powf(exp: f64)`


### 整数乘方


## 实例


```rust
fn main() {
    let base: i32 = 2;
    let result = base.pow(3); // 2^3

    println!("2^3 = {}", result);
}
```


输出：


```
2^3 = 8
```


### 浮点数乘方


## 实例


```rust
fn main() {
    let base: f64 = 2.0;
    let result = base.powf(2.5); // 2^2.5

    println!("2^2.5 = {}", result);
}
```


输出：


```
2^2.5 = 5.656854249492381
```


---


## 2、关系（比较）运算符


| 运算符 | 说明 | 示例 | 结果 |
| --- | --- | --- | --- |
| == | 相等 | 5 == 5 | true |
| != | 不相等 | 5 != 2 | true |
| > | 大于 | 5 > 2 | true |
|  | 小于 | 5 | false |
| >= | 大于等于 | 5 >= 5 | true |
|  | 小于等于 | 2 | true |


## 实例


```rust
fn main() {
    let x = 5;
    let y = 10;

    println!("x == y : {}", x == y);
    println!("x != y : {}", x != y);
    println!("x > y  : {}", x > y);
    println!("x < y  : {}", x < y);
    println!("x >= y : {}", x >= y);
    println!("x <= y : {}", x <= y);
}
```


**输出：**


```
x == y : false
x != y : true
x > y  : false
x < y  : true
x >= y : false
x <= y : true
```


---


## 3、逻辑运算符


| 运算符 | 说明 | 示例 | 结果 |
| --- | --- | --- | --- |
| && | 逻辑与（AND） | true && false | false |
| \|\| | 逻辑或（OR） | true \|\| false | true |
| ! | 逻辑非（NOT） | !true | false |


## 实例


```rust
fn main() {
    let a = true;
    let b = false;

    println!("a && b = {}", a && b);
    println!("a || b = {}", a || b);
    println!("!a = {}", !a);
}
```


**输出：**


```
a && b = false
a || b = true
!a = false
```


---


## 4、位运算符


| 运算符 | 说明 | 示例 | 结果 |
| --- | --- | --- | --- |
| & | 按位与 | 5 & 3 | 1 |
| \| | 按位或 | 5 \| 3 | 7 |
| ^ | 按位异或 | 5 ^ 3 | 6 |
| ! | 按位取反 | !5 | -6 |
|  | 左移 | 5 | 10 |
| >> | 右移 | 5 >> 1 | 2 |


## 实例


```rust
fn main() {
    let x: u8 = 0b1010; // 10
    let y: u8 = 0b1100; // 12

    println!("x & y = {:b}", x & y);
    println!("x | y = {:b}", x | y);
    println!("x ^ y = {:b}", x ^ y);
    println!("!x = {:b}", !x);
    println!("x << 1 = {:b}", x << 1);
    println!("x >> 1 = {:b}", x >> 1);
}
```


**输出：**


```
x & y = 1000
x | y = 1110
x ^ y = 110
!x = 11110101
x << 1 = 10100
x >> 1 = 101
```


---


## 5、赋值与复合赋值运算符


| 运算符 | 说明 | 示例 | 结果 |
| --- | --- | --- | --- |
| = | 赋值 | let mut x = 5; x = 3; | x = 3 |
| += | 加并赋值 | x += 2 | x = x + 2 |
| -= | 减并赋值 | x -= 2 | x = x - 2 |
| *= | 乘并赋值 | x *= 2 | x = x * 2 |
| /= | 除并赋值 | x /= 2 | x = x / 2 |
| %= | 取余并赋值 | x %= 2 | x = x % 2 |
| &= \|= ^= >= | 位运算复合赋值 | x &= 2 | 类似 |


## 实例


```rust
fn main() {
    let mut n = 5;

    n += 3;
    println!("n += 3 -> {}", n);

    n *= 2;
    println!("n *= 2 -> {}", n);

    n >>= 1;
    println!("n >>= 1 -> {}", n);
}
```


**输出：**


```
n += 3 -> 8
n *= 2 -> 16
n >>= 1 -> 8
```


---


## 6、 其他常见运算符


| 运算符 | 说明 | 示例 |
| --- | --- | --- |
| .. | 范围（不含右端） | 0..5 产生 0 到 4 |
| ..= | 范围（含右端） | 0..=5 产生 0 到 5 |
| as | 类型转换 | 5 as f32 |
| ? | 错误传播（在 Result 中） | some()?; |
| * | 解引用 | *ptr |
| & | 取引用 | &x |
| ref | 绑定为引用 | let ref y = x; |


## 实例


```rust
fn main() {
    let x = 5;
    let y = x as f64;

    for i in 1..4 {
        print!("{} ", i);
    }
    println!();

    for i in 1..=3 {
        print!("{} ", i);
    }
    println!();

    let a = 10;
    let b = &a;
    println!("*b = {}", *b);
}
```


**输出：**


```
1 2 3
1 2 3
*b = 10
```










	  AI 思考中...





			** [Rust 异步编程 async/await](https://www.runoob.com/rust-async-await.html)














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