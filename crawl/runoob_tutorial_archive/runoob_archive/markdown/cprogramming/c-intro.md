# C 简介

- Source: https://www.runoob.com/cprogramming/c-intro.html

C 语言是一种通用的高级编程语言，最初由丹尼斯·里奇（Dennis Ritchie）在贝尔实验室为开发 UNIX 操作系统而设计。C 语言于 1972 年在 DEC PDP-11 计算机上首次实现，是现代编程语言体系中最具影响力的语言之一。


1978 年，布莱恩·柯林汉（Brian Kernighan）和丹尼斯·里奇（Dennis Ritchie）共同出版了《The C Programming Language》一书，书中对 C 语言进行了第一次完整的公开描述，这一版本被称为 K&R 标准，成为此后数年间事实上的 C 语言规范。


UNIX 操作系统、C 编译器以及几乎所有的 UNIX 应用程序都是用 C 语言编写的。凭借其简洁的语法、接近硬件的控制能力和出色的运行效率，C 语言已成为系统编程领域最重要的专业语言，并深刻影响了 C++、Java、Go、Rust 等众多后继语言的设计。


- 语法简洁，易于学习和掌握。
- 结构化编程语言，逻辑清晰。
- 编译后生成高效率的机器代码，运行速度接近汇编语言。
- 可直接操作内存和硬件，处理底层任务。
- 可移植性强，能在多种计算机平台和操作系统上编译运行。
- 拥有丰富的标准库，生态成熟，社区庞大。


## 关于 C


- C 语言最初是为了编写 UNIX 操作系统而发明的，诞生于 1972 年的贝尔实验室。
- C 语言以 B 语言为基础演化而来，B 语言由肯·汤普森（Ken Thompson）于 1970 年前后设计。
- 1983 年，美国国家标准协会（ANSI）开始着手制定 C 语言标准，并于 1989 年正式发布 C89（也称 ANSI C），这是 C 语言的第一个官方标准。
- 截至 1973 年，UNIX 操作系统内核已完全使用 C 语言重写，这标志着 C 语言在系统编程领域的奠基性地位。
- C 语言是目前最广泛使用的系统程序设计语言，在嵌入式开发、操作系统、编译器等领域长期占据核心地位。
- 众多重要的基础软件和框架（包括 CPython 解释器、V8 引擎的底层组件等）都使用 C 语言实现。
- 当今最流行的 Linux 操作系统内核和关系数据库管理系统 MySQL 的核心部分均使用 C 语言编写。
- C 语言经历了 C89、C99、C11、C17 等多个标准版本的演进，持续保持活力与现代性。


## 为什么要使用 C？


C 语言最初用于系统开发，特别是构成操作系统的核心程序。由于 C 语言编译后产生的机器代码运行速度与汇编语言几乎相当，同时又具备比汇编更好的可读性和可维护性，因此成为系统级开发的首选语言。下面列举几个 C 语言的典型应用场景：


- 操作系统内核（如 Linux、Windows NT 内核、macOS XNU 内核）
- 语言编译器与解释器（如 GCC、Clang、CPython）
- 汇编器与链接器
- 文本编辑器与命令行工具
- 打印机固件与驱动程序
- 网络协议栈与网络驱动
- 嵌入式系统与单片机开发
- 数据库系统（如 SQLite、MySQL、PostgreSQL）
- 高性能计算与科学计算库（如 BLAS、LAPACK）
- 游戏引擎底层与图形渲染库（如 OpenGL 实现）


## C 程序


一个 C 语言程序，可以只有几行，也可以多达数百万行，源代码保存在扩展名为 **".c"** 的文本文件中，例如 *hello.c*。对于大型项目，代码通常会被拆分到多个 **".c"** 源文件和 **".h"** 头文件中，由构建系统统一管理编译。


您可以使用 **"vi"**、**"vim"**、**"VS Code"** 或任何其他文本编辑器来编写 C 语言程序。编写完成后，通过 GCC 或 Clang 等编译器将源代码编译为可执行文件：


```
gcc hello.c -o hello   # 编译
./hello                # 运行（Linux/macOS）
```


本教程假定您已经知道如何编辑文本文件，以及如何在程序文件中编写源代码。


---


## C11


C11（也称 C1X）是 C 语言的第三个主要官方标准，对应 ISO 标准 ISO/IEC 9899:2011，于 2011 年 12 月正式发布。它在 C99 的基础上进一步完善了语言特性，重点增强了多线程支持、泛型编程和安全性。


### 新特性


- **对齐处理（Alignment）标准化**：引入 `_Alignas` 说明符和 `alignof` 运算符，以及 `aligned_alloc()` 函数和 `` 头文件，允许程序员精确控制数据在内存中的对齐方式，对性能敏感的底层开发尤为重要。
- **`_Noreturn` 函数标记**：用于标记永不返回的函数（如 `exit()`、`abort()`），类似于 GCC 的 `__attribute__((noreturn))`，帮助编译器进行更好的优化和警告分析。
- **`_Generic` 泛型选择关键字**：允许根据表达式的类型在编译期选择不同的代码路径，是 C 语言实现类型安全泛型宏的基础机制，弥补了 C 语言长期缺乏泛型能力的不足。
- **多线程（Multithreading）支持**：首次在 C 语言标准层面引入原生多线程支持，包括： `_Thread_local` 线程局部存储类型标识符，每个线程拥有各自独立的变量副本。
- `` 头文件，提供线程创建（`thrd_create`）、同步（`mtx_lock`/`cnd_wait`）等管理函数。
- `_Atomic` 类型修饰符和 `` 头文件，提供无锁原子操作，是多线程编程的重要基础。


**增强的 Unicode 支持**：基于 ISO/IEC TR 19769:2004，新增 `char16_t` 和 `char32_t` 数据类型，分别对应 UTF-16 和 UTF-32 编码，并提供 `` 头文件包含 Unicode 字符串转换函数，改善了 C 语言对国际化编程的支持。


**移除 `gets()` 函数**：由于 `gets()` 不检查缓冲区边界，是历史上缓冲区溢出漏洞的常见来源，C11 正式将其从标准中删除，推荐使用更安全的 `fgets()` 或新增的 `gets_s()` 替代。


**边界检查函数接口（Annex K）**：定义了一系列带 `_s` 后缀的安全函数，如 `fopen_s()`、`strcat_s()`、`strcpy_s()` 等，这些函数要求调用者传入缓冲区大小，从根源上防止缓冲区溢出问题。


**更多浮点处理宏**：扩展了 `` 和 `` 中的浮点处理宏，提供更精细的浮点运算控制与异常处理能力，满足高精度科学计算需求。


**匿名结构体 / 联合体支持**：允许在结构体或联合体内嵌套定义没有名称的结构体或联合体，访问其成员时无需中间层名称，简化了复杂数据结构的定义。此特性在 GCC 中早已作为扩展存在，C11 将其纳入标准。


**静态断言 `_Static_assert()`**：在编译期对常量表达式进行断言检查，若条件不满足则产生编译错误（而非运行时错误），常用于验证类型大小、结构体偏移等编译期假设，提高代码健壮性。


**`fopen()` 新增独占模式 `"x"`**：在文件打开模式字符串中追加 `"x"`（如 `"wx"`），表示独占创建——若文件已存在则失败，类似于 POSIX 中的 `O_CREAT|O_EXCL` 标志，常用于安全的临时文件创建场景。


**新增 `quick_exit()` 函数**：提供第三种程序终止方式（另外两种是 `return` 和 `exit()`），当 `exit()` 无法正常完成清理时，`quick_exit()` 会执行通过 `at_quick_exit()` 注册的处理函数后立即终止，适用于多线程程序的应急退出场景。










	  AI 思考中...





			** [C 语言教程](https://www.runoob.com/c-tutorial.html)
			[C 环境设置](https://www.runoob.com/c-environment-setup.html) **













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