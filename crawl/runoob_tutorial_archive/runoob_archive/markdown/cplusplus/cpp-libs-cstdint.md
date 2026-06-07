# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-cstdint.html

`` 是 C++11 引入的一个头文件，它定义了一组固定宽度的整数类型，这些类型在不同的平台上具有相同的大小和表示范围。


### 为什么使用


在 C++ 中，标准整数类型（如 `int`、`long` 等）的大小和表示范围依赖于编译器和平台。这可能导致在不同平台上编译的程序行为不一致。使用 `` 中定义的固定宽度整数类型可以避免这些问题，因为它们在所有平台上具有相同的大小和表示范围。


### 定义和语法


`` 定义了以下整数类型：


- `int8_t`：8位有符号整数
- `uint8_t`：8位无符号整数
- `int16_t`：16位有符号整数
- `uint16_t`：16位无符号整数
- `int32_t`：32位有符号整数
- `uint32_t`：32位无符号整数
- `int64_t`：64位有符号整数
- `uint64_t`：64位无符号整数


此外，还定义了最大宽度的整数类型：


- `intmax_t`：最大宽度的有符号整数
- `uintmax_t`：最大宽度的无符号整数


以及用于位操作的类型：


- `intptr_t`：足够大的有符号整数，可以存储指针的值
- `uintptr_t`：足够大的无符号整数，可以存储指针的值


## 实例


下面是一个使用 `` 的简单示例，展示了如何声明和使用这些类型。


## 实例


```cpp
#include <iostream>
#include <cstdint>

int main() {
    // 声明固定宽度的整数类型
    int8_t a = -128; // 最小值
    uint8_t b = 255; // 最大值
    int16_t c = -32768;
    uint16_t d = 65535;
    int32_t e = -2147483648;
    uint32_t f = 4294967295U; // 使用 U 后缀表示无符号常量
    int64_t g = -9223372036854775807LL; // 使用 LL 后缀表示长长整型常量
    uint64_t h = 18446744073709551615ULL; // 使用 ULL 后缀表示无符号长长整型常量

    // 输出结果
    std::cout << "int8_t: " << static_cast<int>(a) << std::endl;
    std::cout << "uint8_t: " << static_cast<unsigned int>(b) << std::endl;
    std::cout << "int16_t: " << c << std::endl;
    std::cout << "uint16_t: " << d << std::endl;
    std::cout << "int32_t: " << e << std::endl;
    std::cout << "uint32_t: " << f << std::endl;
    std::cout << "int64_t: " << g << std::endl;
    std::cout << "uint64_t: " << h << std::endl;

    return 0;
}
```


输出结果：


```
int8_t: -128
uint8_t: 255
int16_t: -32768
uint16_t: 65535
int32_t: -2147483648
uint32_t: 4294967295
int64_t: -9223372036854775807
uint64_t: 18446744073709551615
```


---


## 定宽整数类型


定宽整数类型确保了变量具有固定的宽度，这在需要精确控制数据大小和布局的情况下非常有用。它们的命名形式为 `intN_t` 和 `uintN_t`，其中 `N` 表示位宽。


- `int8_t`, `int16_t`, `int32_t`, `int64_t`: 有符号定宽整数类型。
- `uint8_t`, `uint16_t`, `uint32_t`, `uint64_t`: 无符号定宽整数类型。


## 实例


```cpp
#include <cstdint>
#include <iostream>

int main() {
    int8_t a = -128;
    uint8_t b = 255;
    int32_t c = 2147483647;
    uint64_t d = 18446744073709551615U;

    std::cout << "a = " << static_cast<int>(a) << std::endl;
    std::cout << "b = " << static_cast<unsigned>(b) << std::endl;
    std::cout << "c = " << c << std::endl;
    std::cout << "d = " << d << std::endl;

    return 0;
}
```



### 最小宽度整数类型


最小宽度整数类型确保了变量具有至少指定的位宽，这在需要最低位宽保证但不需要精确控制位宽的情况下非常有用。它们的命名形式为 `int_leastN_t` 和 `uint_leastN_t`。


- `int_least8_t`, `int_least16_t`, `int_least32_t`, `int_least64_t`: 有符号最小宽度整数类型。
- `uint_least8_t`, `uint_least16_t`, `uint_least32_t`, `uint_least64_t`: 无符号最小宽度整数类型。


## 实例


```cpp
#include <cstdint>
#include <iostream>

int main() {
    int_least8_t a = -128;
    uint_least8_t b = 255;
    int_least32_t c = 2147483647;
    uint_least64_t d = 18446744073709551615U;

    std::cout << "a = " << static_cast<int>(a) << std::endl;
    std::cout << "b = " << static_cast<unsigned>(b) << std::endl;
    std::cout << "c = " << c << std::endl;
    std::cout << "d = " << d << std::endl;

    return 0;
}
```



### 最快宽度整数类型


最快宽度整数类型确保了变量具有至少指定的位宽，并且在给定系统上尽可能快。它们的命名形式为 `int_fastN_t` 和 `uint_fastN_t`。


- `int_fast8_t`, `int_fast16_t`, `int_fast32_t`, `int_fast64_t`: 有符号最快宽度整数类型。
- `uint_fast8_t`, `uint_fast16_t`, `uint_fast32_t`, `uint_fast64_t`: 无符号最快宽度整数类型。


## 实例


```cpp
#include <cstdint>
#include <iostream>

int main() {
    int_fast8_t a = -128;
    uint_fast8_t b = 255;
    int_fast32_t c = 2147483647;
    uint_fast64_t d = 18446744073709551615U;

    std::cout << "a = " << static_cast<int>(a) << std::endl;
    std::cout << "b = " << static_cast<unsigned>(b) << std::endl;
    std::cout << "c = " << c << std::endl;
    std::cout << "d = " << d << std::endl;

    return 0;
}
```



### 特殊类型


- `intmax_t`: 能够表示的最大有符号整数类型。
- `uintmax_t`: 能够表示的最大无符号整数类型。
- `intptr_t`: 足够大的有符号整数类型，用于存储指针。
- `uintptr_t`: 足够大的无符号整数类型，用于存储指针。


## 实例


```cpp
#include <cstdint>
#include <iostream>

int main() {
    intmax_t max_int = INTMAX_MAX;
    uintmax_t max_uint = UINTMAX_MAX;
    intptr_t ptr_int = reinterpret_cast<intptr_t>(&max_int);
    uintptr_t ptr_uint = reinterpret_cast<uintptr_t>(&max_uint);

    std::cout << "max_int = " << max_int << std::endl;
    std::cout << "max_uint = " << max_uint << std::endl;
    std::cout << "ptr_int = " << ptr_int << std::endl;
    std::cout << "ptr_uint = " << ptr_uint << std::endl;

    return 0;
}
```



### 边界值宏


`` 还定义了一组宏，用于表示这些类型的边界值。


- `INT8_MIN`, `INT8_MAX`, `UINT8_MAX`
- `INT16_MIN`, `INT16_MAX`, `UINT16_MAX`
- `INT32_MIN`, `INT32_MAX`, `UINT32_MAX`
- `INT64_MIN`, `INT64_MAX`, `UINT64_MAX`


## 实例


```cpp
#include <cstdint>
#include <iostream>

int main() {
    std::cout << "INT8_MIN = " << static_cast<int>(INT8_MIN) << std::endl;
    std::cout << "INT8_MAX = " << static_cast<int>(INT8_MAX) << std::endl;
    std::cout << "UINT8_MAX = " << static_cast<unsigned>(UINT8_MAX) << std::endl;

    std::cout << "INT32_MIN = " << INT32_MIN << std::endl;
    std::cout << "INT32_MAX = " << INT32_MAX << std::endl;
    std::cout << "UINT32_MAX = " << UINT32_MAX << std::endl;

    return 0;
}
```


`` 提供了一组固定宽度的整数类型，这些类型在不同的平台上具有相同的大小和表示范围。使用这些类型可以提高代码的可移植性和可预测性。在编写跨平台的 C++ 程序时，推荐使用 `` 中定义的类型。








	  AI 思考中...





			** [C++ 内存管理库 ](https://www.runoob.com/cpp-libs-memory.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-cstdio.html) **













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