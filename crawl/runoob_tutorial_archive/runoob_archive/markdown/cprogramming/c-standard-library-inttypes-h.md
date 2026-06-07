# C 标准库

- Source: https://www.runoob.com/cprogramming/c-standard-library-inttypes-h.html

在 C 语言编程中，处理整数类型时，我们经常需要确保代码在不同平台上的可移植性，不同的平台可能有不同的整数大小和表示方式，这可能导致代码在不同环境下表现不一致。


为了解决以上问题，C 标准库提供了``头文件，它定义了一组固定大小的整数类型和相应的格式化宏，帮助开发者编写可移植的代码。


`inttypes.h` 是 C 标准库中一个非常重要的头文件，它提供了一组固定宽度的整数类型和相应的格式化宏，通过使用这些类型和宏，开发者可以确保在不同平台上，整数的大小和格式化输出是一致的，从而避免潜在的问题。


### 固定宽度整数类型


`inttypes.h` 定义了一组固定宽度的整数类型，这些类型在不同的平台上具有相同的大小。以下是常见的固定宽度整数类型：


- `int8_t`：8位有符号整数
- `uint8_t`：8位无符号整数
- `int16_t`：16位有符号整数
- `uint16_t`：16位无符号整数
- `int32_t`：32位有符号整数
- `uint32_t`：32位无符号整数
- `int64_t`：64位有符号整数
- `uint64_t`：64位无符号整数


这些类型确保了在不同平台上，整数的大小是一致的，从而提高了代码的可移植性。


### 格式化宏


`inttypes.h` 还定义了一组格式化宏，用于在`printf`和`scanf`等函数中格式化固定宽度整数类型。这些宏确保了在不同平台上，整数的格式化输出是一致的。


以下是常见的格式化宏：


- `PRId8`：用于格式化`int8_t`类型的有符号整数
- `PRIu8`：用于格式化`uint8_t`类型的无符号整数
- `PRId16`：用于格式化`int16_t`类型的有符号整数
- `PRIu16`：用于格式化`uint16_t`类型的无符号整数
- `PRId32`：用于格式化`int32_t`类型的有符号整数
- `PRIu32`：用于格式化`uint32_t`类型的无符号整数
- `PRId64`：用于格式化`int64_t`类型的有符号整数
- `PRIu64`：用于格式化`uint64_t`类型的无符号整数


这些宏的使用方式如下：


## 实例


```c
#include <stdio.h>
#include <inttypes.h>

int main() {
    int32_t myInt = 42;
    printf("The value of myInt is: %" PRId32 "\n", myInt);
    return 0;
}
```


在上面的代码中，`PRId32` 宏用于格式化 `int32_t` 类型的有符号整数，确保在不同平台上输出一致。


输出结果为：


```
The value of myInt is: 42
```


---


## 其他宏


`inttypes.h` 还定义了一些其他有用的宏，例如：


- `INT8_MIN`、`INT8_MAX`：`int8_t`类型的最小值和最大值
- `UINT8_MAX`：`uint8_t`类型的最大值
- `INT16_MIN`、`INT16_MAX`：`int16_t`类型的最小值和最大值
- `UINT16_MAX`：`uint16_t`类型的最大值
- `INT32_MIN`、`INT32_MAX`：`int32_t`类型的最小值和最大值
- `UINT32_MAX`：`uint32_t`类型的最大值
- `INT64_MIN`、`INT64_MAX`：`int64_t`类型的最小值和最大值
- `UINT64_MAX`：`uint64_t`类型的最大值


这些宏可以帮助开发者在代码中安全地使用固定宽度整数类型，避免溢出和其他潜在问题。


### 实例


以下是一个使用`inttypes.h`的完整示例，展示了如何定义和使用固定宽度整数类型及其格式化宏：


## 实例


```c
#include <stdio.h>
#include <inttypes.h>

int main() {
    int32_t myInt = 42;
    uint64_t myUInt = 1234567890123456789ULL;

    printf("The value of myInt is: %" PRId32 "\n", myInt);
    printf("The value of myUInt is: %" PRIu64 "\n", myUInt);

    printf("The minimum value of int32_t is: %" PRId32 "\n", INT32_MIN);
    printf("The maximum value of uint64_t is: %" PRIu64 "\n", UINT64_MAX);

    return 0;
}
```


输出结果为：


```
The value of myInt is: 42
The value of myUInt is: 1234567890123456789
The minimum value of int32_t is: -2147483648
The maximum value of uint64_t is: 18446744073709551615
```


以上代码中，我们定义了一个 `int32_t` 类型的有符号整数和一个 `uint64_t` 类型的无符号整数，并使用相应的格式化宏将它们打印出来。我们还使用了 `INT32_MIN` 和 `UINT64_MAX` 宏来打印这些类型的最小值和最大值。









	  AI 思考中...





			** [C 标准库 ](https://www.runoob.com/c-standard-library-stdint-h.html)
			[C 标准库 ](https://www.runoob.com/c-standard-library-complex-h.html) **













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