# Rust 教程

- Source: https://www.runoob.com/rust/rust-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2020/04/rusticon.png)

Rust 是由 Mozilla 主导开发的高性能编译型编程语言，遵循"安全、并发、实用"的设计原则。


Rust 语言由 Mozilla 开发，首次发布于 2010 年。

Rust 支持多种编程范式，包括函数式、并发式、过程式和面向对象风格。


Rust 速度惊人且内存利用率极高。由于没有运行时和垃圾回收，它能够胜任对性能要求特别高的服务，可以在嵌入式设备上运行，还能轻松和其他语言集成。


Rust 系列文章内容由 **Sobin** 收集整理。


---


## Rust 语言的特点


- **内存安全**：Rust 的所有权系统在编译时防止空悬指针、数据竞争等内存错误，无需垃圾收集器。
- **并发编程**：Rust 提供了现代的语言特性来支持并发编程，如线程和消息传递，使得编写并发程序更加安全和容易。
- **性能**：Rust 编译为机器码，没有运行时或垃圾收集器，能够提供接近 C 和 C++ 的性能。
- **类型系统**：Rust 的类型系统和模式匹配提供了强大的抽象能力，有助于编写更安全、更可预测的代码。
- **错误处理**：Rust 的错误处理模型鼓励显式处理所有可能的错误情况。
- **宏系统**：Rust 提供了一个强大的宏系统，允许开发者在编译时编写和重用代码。
- **包管理**：Rust 的包管理器 Cargo 简化了依赖管理和构建过程。
- **跨平台**：Rust 支持多种操作系统和平台，包括 Windows、macOS、Linux、BSDs 等。
- **社区支持**：Rust 有一个活跃的社区，提供了大量的库和工具。
- **工具链**：Rust 拥有丰富的工具链，包括编译器、包管理器、文档生成器等。
- **无段错误**：Rust 的所有权和生命周期规则保证了引用的有效性，从而避免了段错误。
- **迭代器和闭包**：Rust 提供了强大的迭代器和闭包支持，简化了集合的处理。


---


## Rust的应用 Rust 语言可以用于开发： 系统编程：操作系统、设备驱动程序、嵌入式系统等。 网络编程：网络服务器、Web 服务、分布式系统等。 游戏开发：游戏引擎、游戏工具、游戏客户端和服务器。 WebAssembly：在 Web 浏览器中运行的高性能 Web 应用。 工具开发：命令行工具、自动化脚本、系统管理工具。 区块链技术：智能合约、加密货币、去中心化应用（DApps）。 科学计算：数值分析、数据科学、机器学习。 音视频处理：媒体服务器、流处理、编解码器。 云计算：云服务后端、容器技术、微服务架构。 嵌入式设备：IoT 设备、智能家居设备、可穿戴设备。 谁适合阅读本教程？


本教程对于初级的编程知识将默认读者已经掌握，所以如果你阅读本教程，你需要对初级的编程知识有一定的了解（最好已经初识 C/C++ 或 JavaScript 编程语言）。


### 第一个 Rust 程序


Rust 语言代码文件后缀名为 **.rs**, 如 **runoob.rs**。


## 实例：runoob.rs 文件


```rust
fn main() {
    println!("Hello World!");
}
```

**
[运行实例 »](https://www.runoob.com/try/runcode.php?filename=HelloWorld&type=rust)


使用 **rustc** 命令编译 runoob.rs 文件：


```
$ rustc runoob.rs   # 编译 runoob.rs 文件
```


编译后会生成 runoob** 可执行文件：


```
$ ./runoob    # 执行 runoob
Hello World!
```


---


## 参考链接


- Rust 官方网站：[https://www.rust-lang.org/zh-CN](https://www.rust-lang.org/zh-CN)
- Rust 官方文档：[https://doc.rust-lang.org/](https://doc.rust-lang.org/)
- Rust Play：[https://play.rust-lang.org/](https://play.rust-lang.org/)
- Visual Studio Code：[https://code.visualstudio.com/](https://code.visualstudio.com/)








	  AI 思考中...






			[Rust 环境搭建](https://www.runoob.com/rust-setup.html) **













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