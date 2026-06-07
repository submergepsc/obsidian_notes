# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-climits.html

`` 是 C++ 标准库中的一个头文件，提供了与整数类型相关的限制和特性。它定义了一组常量，描述了各种整数类型（如 `char`、`int`、`long` 等）的最小值、最大值和其他相关属性。这些常量来自 C 标准库的 `` 头文件。


### 提供的常量


这些常量描述了不同整数类型在特定平台上的特性。以下是一些常用的常量：


1. **字符类型**


- `CHAR_BIT`：`char` 类型的位数（通常为 8）。
- `CHAR_MIN`：`char` 类型的最小值。
- `CHAR_MAX`：`char` 类型的最大值。
- `SCHAR_MIN`：有符号 `char` 类型的最小值。
- `SCHAR_MAX`：有符号 `char` 类型的最大值。
- `UCHAR_MAX`：无符号 `char` 类型的最大值。


2. **短整型**


- `SHRT_MIN`：`short` 类型的最小值。
- `SHRT_MAX`：`short` 类型的最大值。
- `USHRT_MAX`：无符号 `short` 类型的最大值。


3. **整型**


- `INT_MIN`：`int` 类型的最小值。
- `INT_MAX`：`int` 类型的最大值。
- `UINT_MAX`：无符号 `int` 类型的最大值。


4. **长整型**


- `LONG_MIN`：`long` 类型的最小值。
- `LONG_MAX`：`long` 类型的最大值。
- `ULONG_MAX`：无符号 `long` 类型的最大值。


5. **长长整型**


- `LLONG_MIN`：`long long` 类型的最小值。
- `LLONG_MAX`：`long long` 类型的最大值。
- `ULLONG_MAX`：无符号 `long long` 类型的最大值。


## 实例


下面是一个使用 `` 头文件中定义的常量的示例程序：


## 实例


```cpp
#include <iostream>
#include <climits>

int main() {
    // 打印整型的最大值和最小值
    std::cout << "int 的最大值是：" << INT_MAX << std::endl;
    std::cout << "int 的最小值是：" << INT_MIN << std::endl;

    // 打印长整型的最大值和最小值
    std::cout << "long 的最大值是：" << LONG_MAX << std::endl;
    std::cout << "long 的最小值是：" << LONG_MIN << std::endl;

    // 打印无符号长整型的最大值
    std::cout << "unsigned long 的最大值是：" << ULONG_MAX << std::endl;

    // 打印字符类型的最大值和最小值
    std::cout << "char 的最大值是：" << CHAR_MAX << std::endl;
    std::cout << "char 的最小值是：" << CHAR_MIN << std::endl;

    return 0;
}
```


### 输出结果


当你运行上述程序时，输出结果将类似于以下内容（具体值可能因编译器和平台而异）：


```
int 的最大值是：2147483647
int 的最小值是：-2147483648
long 的最大值是：9223372036854775807
long 的最小值是：-9223372036854775808
unsigned long 的最大值是：18446744073709551615
char 的最大值是：127
char 的最小值是：-128
```


`` 头文件中的常量提供了关于整数类型表示的有用信息，使程序员能够编写与平台无关的代码，确保程序在不同平台上具有一致的行为。了解这些常量的含义和使用方法，对于需要高精度和范围控制的应用程序尤为重要。如果你有特定的使用需求或问题，可以进一步讨论。








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-cfloat.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-codecvt.html) **













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