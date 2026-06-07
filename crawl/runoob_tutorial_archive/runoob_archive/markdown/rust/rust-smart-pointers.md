# Rust 智能指针

- Source: https://www.runoob.com/rust/rust-smart-pointers.html

智能指针（Smart pointers）是一种在 Rust 中常见的数据结构，它们提供了额外的功能和安全性保证，以帮助管理内存和数据。

在 Rust 中，智能指针是一种封装了对动态分配内存的所有权和生命周期管理的数据类型。

智能指针通常封装了一个原始指针，并提供了一些额外的功能，比如引用计数、所有权转移、生命周期管理等。

在 Rust 中，标准库提供了几种常见的智能指针类型，例如 Box、Rc、Arc 和 RefCell。


**智能指针的使用场景:**


- 当需要在堆上分配内存时，使用 `Box`。
- 当需要多处共享所有权时，使用 `Rc` 或 `Arc`。
- 当需要内部可变性时，使用 `RefCell`。
- 当需要线程安全的共享所有权时，使用 `Arc`。
- 当需要互斥访问数据时，使用 `Mutex`。
- 当需要读取-写入访问数据时，使用 `RwLock`。
- 当需要解决循环引用问题时，使用 `Weak`。


### Box 智能指针

Box 是 Rust 中最简单的智能指针之一，它允许在堆上分配一块内存，并将值存储在这个内存中。

由于 Rust 的所有权规则，使用 Box 可以在堆上创建具有已知大小的数据。


## 实例


```rust
let b = Box::new(5);
println!("b = {}", b);
```


### Rc 智能指针

Rc（引用计数指针）允许多个所有者共享数据，它使用引用计数来跟踪数据的所有者数量，并在所有者数量为零时释放数据。

Rc 适用于单线程环境下的数据共享。


## 实例


```rust
use std::rc::Rc;

let data = Rc::new(5);
let data_clone = Rc::clone(&data);
```


### Arc 智能指针

Arc（原子引用计数指针）与 Rc 类似，但是可以安全地在多线程环境中共享数据，因为它使用原子操作来更新引用计数。


## 实例


```rust
use std::sync::Arc;

let data = Arc::new(5);
let data_clone = Arc::clone(&data);
```


### RefCell 智能指针

RefCell 允许在运行时检查借用规则，它使用内部可变性来提供了一种安全的内部可变性模式，允许在不可变引用的情况下修改数据。

但是，RefCell 只能用于单线程环境。


## 实例


```rust
use std::cell::RefCell;

let data = RefCell::new(5);
let mut borrowed_data = data.borrow_mut();
*borrowed_data = 10;
```


### Mutex 智能指针


Mutex 是一个互斥锁，它保证了在任何时刻只有一个线程可以访问 Mutex 内部的数据。


## 实例


```rust
use std::sync::Mutex;

let m = Mutex::new(5);
let mut data = m.lock().unwrap();
```


### RwLock 智能指针

RwLock 是一种读取-写入锁，允许多个读取者同时访问数据，但在写入时是排他的。


## 实例


```rust
use std::sync::RwLock;

let lock = RwLock::new(5);
let read_guard = lock.read().unwrap();
```


### Weak 智能指针

Weak 是 Rc 的非拥有智能指针，它不增加引用计数，用于解决循环引用问题。


## 实例


```rust
use std::rc::{Rc, Weak};

let five = Rc::new(5);
let weak_five = Rc::downgrade(&five);
```


### 智能指针的生命周期管理

智能指针可以帮助管理数据的生命周期，当智能指针被销毁时，它们会自动释放内存，从而避免了内存泄漏和野指针的问题。

此外，智能指针还允许在创建时指定特定的析构函数，以实现自定义的资源管理。


### 实例

下面是一个简单的 Rust 智能指针完整实例，该示例使用 Rc 智能指针实现了一个简单的引用计数功能，并演示了多个所有者共享数据的情况。


## 实例


```rust
// 引入所需的依赖库
use std::rc::Rc;

// 定义一个结构体，用于存储数据
#[derive(Debug)]
struct Data {
    value: i32,
}

// 主函数
fn main() {
    // 创建一个 Rc 智能指针，共享数据
    let data = Rc::new(Data { value: 5 });

    // 克隆 Rc 智能指针，增加数据的引用计数
    let data_clone1 = Rc::clone(&data);
    let data_clone2 = Rc::clone(&data);

    // 输出数据的值和引用计数
    println!("Data value: {}", data.value);
    println!("Reference count: {}", Rc::strong_count(&data));

    // 打印克隆后的 Rc 智能指针
    println!("Data clone 1: {:?}", data_clone1);
    println!("Data clone 2: {:?}", data_clone2);
}
```


以上代码中，我们首先定义了一个 `Data` 结构体，用于存储一个整数值。然后在 `main` 函数中创建了一个 `Rc` 智能指针，用于共享数据。接着通过 `Rc::clone` 方法克隆了两个智能指针，增加了数据的引用计数。最后打印了数据的值、引用计数和克隆后的智能指针。


运行该程序，可以看到输出了数据的值和引用计数，以及克隆后的智能指针。由于 `Rc` 智能指针使用引用计数来跟踪数据的所有者数量，因此在每次克隆时，数据的引用计数会增加，当所有者数量为零时，数据会被自动释放。

输出结果如下：


```
Data value: 5
Reference count: 3
Data clone 1: Data { value: 5 }
Data clone 2: Data { value: 5 }
```


### 总结

Rust 的智能指针提供了一种安全和自动化的方式来管理内存和共享所有权。


智能指针是 Rust 中非常重要的一种数据结构，它们提供了一种安全、灵活和方便的内存管理方式，帮助程序员避免了常见的内存安全问题，提高了代码的可靠性和可维护性。


智能指针是 Rust 安全性模型的重要组成部分，允许开发者编写低级代码而不必担心内存安全问题。

通过智能指针，Rust 既保持了 C 语言的控制能力，又避免了其风险。








	  AI 思考中...





			** [Rust 闭包](https://www.runoob.com/rust-closure.html)
			[Rust 异步编程 async/await](https://www.runoob.com/rust-async-await.html) **













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