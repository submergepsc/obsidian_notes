# C 标准库 -

- Source: https://www.runoob.com/cprogramming/c-standard-library-limits-h.html

## 简介

`` 是 C 标准库中的一个头文件，定义了各种数据类型的限制。这些宏提供了有关整数类型（`char`、`short`、`int`、`long` 和 `long long` 等）和其他数据类型的最大值和最小值的信息。


这些限制指定了变量不能存储任何超出这些限制的值，例如一个无符号可以存储的最大值是 255。


## 库宏


下面的值是特定实现的，且是通过 #define 指令来定义的，这些值都不得低于下边所给出的值。


| 宏 | 描述 | 值 |
| --- | --- | --- |
| 字符类型 |  |  |
| CHAR_BIT | char 类型的位数 | 通常为 8 |
| CHAR_MIN | char 类型的最小值（有符号或无符号） | -128 或 0 |
| CHAR_MAX | char 类型的最大值（有符号或无符号） | 127 或 255 |
| SCHAR_MIN | signed char 类型的最小值 | -128 |
| SCHAR_MAX | signed char 类型的最大值 | 127 |
| UCHAR_MAX | unsigned char 类型的最大值 | 255 |
| 短整数类型 |  |  |
| SHRT_MIN | short 类型的最小值 | -32768 |
| SHRT_MAX | short 类型的最大值 | 32767 |
| USHRT_MAX | unsigned short 类型的最大值 | 65535 |
| 整数类型 |  |  |
| INT_MIN | int 类型的最小值 | -2147483648 |
| INT_MAX | int 类型的最大值 | 2147483647 |
| UINT_MAX | unsigned int 类型的最大值 | 4294967295 |
| 长整数类型 |  |  |
| LONG_MIN | long 类型的最小值 | -9223372036854775808L |
| LONG_MAX | long 类型的最大值 | 9223372036854775807L |
| ULONG_MAX | unsigned long 类型的最大值 | 18446744073709551615UL |
| 长长整数类型 |  |  |
| LLONG_MIN | long long 类型的最小值 | -9223372036854775808LL |
| LLONG_MAX | long long 类型的最大值 | 9223372036854775807LL |
| ULLONG_MAX | unsigned long long 类型的最大值 | 18446744073709551615ULL |


## 实例


下面的实例演示了 limit.h 文件中定义的一些常量的使用。


## 实例


```c
#include <stdio.h>
#include <limits.h>

int main() {
    printf("Character types:\n");
    printf("CHAR_BIT: %d\n", CHAR_BIT);
    printf("CHAR_MIN: %d\n", CHAR_MIN);
    printf("CHAR_MAX: %d\n", CHAR_MAX);
    printf("SCHAR_MIN: %d\n", SCHAR_MIN);
    printf("SCHAR_MAX: %d\n", SCHAR_MAX);
    printf("UCHAR_MAX: %u\n", UCHAR_MAX);

    printf("\nShort integer types:\n");
    printf("SHRT_MIN: %d\n", SHRT_MIN);
    printf("SHRT_MAX: %d\n", SHRT_MAX);
    printf("USHRT_MAX: %u\n", USHRT_MAX);

    printf("\nInteger types:\n");
    printf("INT_MIN: %d\n", INT_MIN);
    printf("INT_MAX: %d\n", INT_MAX);
    printf("UINT_MAX: %u\n", UINT_MAX);

    printf("\nLong integer types:\n");
    printf("LONG_MIN: %ld\n", LONG_MIN);
    printf("LONG_MAX: %ld\n", LONG_MAX);
    printf("ULONG_MAX: %lu\n", ULONG_MAX);

    printf("\nLong long integer types:\n");
    printf("LLONG_MIN: %lld\n", LLONG_MIN);
    printf("LLONG_MAX: %lld\n", LLONG_MAX);
    printf("ULLONG_MAX: %llu\n", ULLONG_MAX);

    return 0;
}
```


让我们编译和运行上面的程序，这将产生下列结果：


```
Character types:
CHAR_BIT: 8
CHAR_MIN: -128
CHAR_MAX: 127
SCHAR_MIN: -128
SCHAR_MAX: 127
UCHAR_MAX: 255

Short integer types:
SHRT_MIN: -32768
SHRT_MAX: 32767
USHRT_MAX: 65535

Integer types:
INT_MIN: -2147483648
INT_MAX: 2147483647
UINT_MAX: 4294967295

Long integer types:
LONG_MIN: -9223372036854775808
LONG_MAX: 9223372036854775807
ULONG_MAX: 18446744073709551615

Long long integer types:
LLONG_MIN: -9223372036854775808
LLONG_MAX: 9223372036854775807
ULLONG_MAX: 18446744073709551615
```


`` 提供了许多与整数类型相关的宏，用于描述各种数据类型的限制。这些宏对于编写健壮和移植性强的代码非常有用，因为它们允许程序员在不同平台上轻松获取数据类型的限制值。








	  AI 思考中...





			** [C 标准库 – ](https://www.runoob.com/c-standard-library-setjmp-h.html)
			[C 标准库 – ](https://www.runoob.com/c-standard-library-locale-h.html) **













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