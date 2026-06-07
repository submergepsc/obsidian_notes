# C 标准库 - 参考手册

- Source: https://www.runoob.com/cprogramming/c-standard-library.html

以下是 C 标准库头文件及其功能简介的详细列表：

C 语言是一种通用的、面向过程式的计算机程序设计语言。1972 年，为了移植与开发 UNIX 操作系统，丹尼斯·里奇在贝尔电话实验室设计开发了 C 语言。


C 语言是一种广泛使用的计算机语言，它与 Java 编程语言一样普及，二者在现代软件程序员之间都得到广泛使用。


C 标准库（C Standard Library）包含了一组头文件，这些头文件提供了许多函数和宏，用于处理输入输出、字符串操作、数学计算、内存管理等常见编程任务。。


## 谁适合阅读本教程？


C 标准库可以作为 C 程序员的参考手册，C 程序员在开发系统编程相关的项目时可以参阅这个手册。系统相关的每一个步骤帮助他们参考。我们以易于理解的方式对所有的 C 函数进行讲解，您可以直接在项目中复制使用这些项目。


## 阅读本教程前，您需要了解的知识


对 C 语言有基本的了解将有助于您理解本标准库涵盖的 C 内置函数。


## 编译/执行 C 程序 如果您想要在 Linux 服务器上学习 C 编程，但是又没有相关的配置环境，那么可以访问 C 在线编译。您只需进行简单的点击动作，即可在高端的服务器上体验真实的编程经验。这是完全免费的在线工具。 标准库


| 头文件 | 功能简介 |
| --- | --- |
|  | 标准输入输出库，包含 printf、scanf、fgets、fputs 等函数。 |
|  | 标准库函数，包含内存分配、程序控制、转换函数等，如 malloc、free、exit、atoi、rand 等。 |
|  | 字符串操作函数，如 strlen、strcpy、strcat、strcmp 等。 |
|  | 数学函数库，包含各种数学运算函数，如 sin、cos、tan、exp、log、sqrt 等。 |
|  | 时间和日期函数，如 time、clock、difftime、strftime 等。 |
|  | 字符处理函数，如 isalpha、isdigit、isspace、toupper、tolower 等。 |
|  | 定义各种类型的限制值，如 INT_MAX、CHAR_MIN、LONG_MAX 等。 |
|  | 定义浮点类型的限制值，如 FLT_MAX、DBL_MIN 等。 |
|  | 包含宏 assert，用于在调试时进行断言检查。 |
|  | 定义了错误码变量 errno 及相关宏，用于表示和处理错误。 |
|  | 定义了一些通用类型和宏，如 size_t、ptrdiff_t、NULL 等。 |
|  | 定义了处理信号的函数和宏，如 signal、raise 等。 |
|  | 提供非本地跳转功能的宏和函数，如 setjmp、longjmp 等。 |
|  | 定义了与地域化相关的函数和宏，如 setlocale、localeconv 等。 |
|  | 提供处理可变参数函数的宏，如 va_start、va_arg、va_end 等。 |
|  | 定义布尔类型和值 true 和 false。 |
|  | 定义了精确宽度的整数类型，如 int8_t、uint16_t 等。 |
|  | 提供与整数类型相关的格式化输出宏和函数。 |
|  | 提供复数运算的函数和宏，如 cabs、carg 等。 |
|  | 为泛型数学函数提供宏，以简化对不同类型数据的数学运算。 |
|  | 提供对浮点环境的控制，如舍入模式和异常状态。 |








	  AI 思考中...





			** [C 从函数返回指针](https://www.runoob.com/c-return-pointer-from-functions.html)
			[C 标准库 – ](https://www.runoob.com/c-standard-library-assert-h.html) **













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