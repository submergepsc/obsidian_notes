# C 标准库

- Source: https://www.runoob.com/cprogramming/c-standard-library-stdint-h.html

`` 是 C99 标准引入的头文件，它提供了一些整数类型的定义，这些类型具有明确的大小和符号属性，确保在不同平台上的一致性。


`` 库是为了弥补 C 语言中不同平台整数类型大小不一致的问题，从而提高代码的可移植性和可维护性。

`` 主要用于定义固定大小的整数类型、整数类型的最小/最大值、以及整数类型的类型限定符。这样可以避免依赖编译器或操作系统平台特定的整数大小。

`` 通过提供固定宽度的整数类型和相关宏，使得编程人员能够明确指定所需整数的大小，而不依赖于平台的实现细节。


`` 的主要目的是：


- 提供固定宽度的整数类型（如 `int8_t`、`int16_t` 等），确保其大小在不同平台上一致。
- 定义与平台无关的整数类型（如 `int_least8_t`、`int_fast16_t` 等），用于优化性能和内存使用。
- 提供最大宽度整数类型（如 `intmax_t`、`uintmax_t`），用于表示最大可能的整数。


### 固定宽度整数类型


这些类型明确指定了其宽度（位数），确保在不同平台上具有相同的大小。


| 类型 | 描述 |
| --- | --- |
| int8_t | 8 位有符号整数 |
| int16_t | 16 位有符号整数 |
| int32_t | 32 位有符号整数 |
| int64_t | 64 位有符号整数 |
| uint8_t | 8 位无符号整数 |
| uint16_t | 16 位无符号整数 |
| uint32_t | 32 位无符号整数 |
| uint64_t | 64 位无符号整数 |


**注意**：


- 如果平台不支持某个固定宽度类型，则不会定义该类型。


---


### 最小宽度整数类型


这些类型至少具有指定的宽度，但可能更大。


| 类型 | 描述 |
| --- | --- |
| int_least8_t | 至少 8 位有符号整数 |
| int_least16_t | 至少 16 位有符号整数 |
| int_least32_t | 至少 32 位有符号整数 |
| int_least64_t | 至少 64 位有符号整数 |
| uint_least8_t | 至少 8 位无符号整数 |
| uint_least16_t | 至少 16 位无符号整数 |
| uint_least32_t | 至少 32 位无符号整数 |
| uint_least64_t | 至少 64 位无符号整数 |


---


### 最快最小宽度整数类型


这些类型是具有指定宽度的最快整数类型，通常用于性能优化。


| 类型 | 描述 |
| --- | --- |
| int_fast8_t | 至少 8 位的最快有符号整数 |
| int_fast16_t | 至少 16 位的最快有符号整数 |
| int_fast32_t | 至少 32 位的最快有符号整数 |
| int_fast64_t | 至少 64 位的最快有符号整数 |
| uint_fast8_t | 至少 8 位的最快无符号整数 |
| uint_fast16_t | 至少 16 位的最快无符号整数 |
| uint_fast32_t | 至少 32 位的最快无符号整数 |
| uint_fast64_t | 至少 64 位的最快无符号整数 |


---


### 最大宽度整数类型


这些类型用于表示最大可能的整数。


| 类型 | 描述 |
| --- | --- |
| intmax_t | 最大宽度的有符号整数 |
| uintmax_t | 最大宽度的无符号整数 |


---


### 指针宽度整数类型


这些类型用于表示指针大小的整数。


| 类型 | 描述 |
| --- | --- |
| intptr_t | 可以存储指针的有符号整数 |
| uintptr_t | 可以存储指针的无符号整数 |


---


### 宏定义


`` 还定义了一些宏，用于表示特定类型的最大值和最小值。


| 宏 | 描述 |
| --- | --- |
| INT8_MIN | int8_t 的最小值 |
| INT8_MAX | int8_t 的最大值 |
| UINT8_MAX | uint8_t 的最大值 |
| INT16_MIN | int16_t 的最小值 |
| INT16_MAX | int16_t 的最大值 |
| UINT16_MAX | uint16_t 的最大值 |
| INT32_MIN | int32_t 的最小值 |
| INT32_MAX | int32_t 的最大值 |
| UINT32_MAX | uint32_t 的最大值 |
| INT64_MIN | int64_t 的最小值 |
| INT64_MAX | int64_t 的最大值 |
| UINT64_MAX | uint64_t 的最大值 |
| INTMAX_MIN | intmax_t 的最小值 |
| INTMAX_MAX | intmax_t 的最大值 |
| UINTMAX_MAX | uintmax_t 的最大值 |


### 实例

以下是一个使用 `` 的示例：


## 实例


```c
#include <stdio.h>
#include <stdint.h>

int main() {
    // 固定宽度整数类型
    int32_t a = 100;
    uint64_t b = 1000000000000ULL;

    // 最小宽度整数类型
    int_least16_t c = 200;

    // 最快最小宽度整数类型
    int_fast32_t d = 300;

    // 最大宽度整数类型
    intmax_t e = INTMAX_MAX;

    // 输出值
    printf("a = %d\n", a);
    printf("b = %llu\n", b);
    printf("c = %d\n", c);
    printf("d = %d\n", d);
    printf("e = %jd\n", e);

    return 0;
}
```


### 注意事项


- `` 仅在 C99 及更高版本中可用。
- 固定宽度类型（如 `int32_t`）在某些平台上可能不可用，因此在使用时应检查其是否定义。
- 使用 `` 可以提高代码的可移植性，特别是在需要精确控制整数大小的场景中。








	  AI 思考中...





			** [C 标准库 ](https://www.runoob.com/c-standard-library-stdbool-h.html)
			[C 标准库 *](https://www.runoob.com/c-standard-library-inttypes-h.html) *













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