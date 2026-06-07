# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-codecvt.html

`` 是 C++ 标准库中的一个头文件，提供了字符转换的工具。这个头文件主要包含 `std::codecvt` 类模板及其特化，支持字符编码之间的转换，例如从 UTF-8 到 UTF-16，或从宽字符（`wchar_t`）到窄字符（`char`）等。`std::codecvt` 类通常与 `std::wstring_convert` 类一起使用，以实现字符编码转换。


## 语法


`codecvt` 命名空间中的主要类和函数如下：


- `codecvt_base`：定义了编码转换的状态类型和错误处理方式。
- `codecvt_byname`：模板类，用于创建特定编码的转换器。
- `codecvt_utf8`、`codecvt_utf16`：特定编码的转换器类。


### 基本语法


```
#include <codecvt>
#include <locale>
#include <string>

std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> converter;
std::wstring wide_string = converter.from_bytes("Hello, World!");
std::string narrow_string = converter.to_bytes(L"你好，世界！");
```


## 实例


### 示例 1：UTF-8 到 UTF-16 的转换


在这个示例中，我们将演示如何使用 `codecvt` 将 UTF-8 编码的字符串转换为 UTF-16 编码的宽字符串。


## 实例


```cpp
#include <iostream>
#include <codecvt>
#include <locale>
#include <string>

int main() {
    // 创建一个 UTF-8 到 UTF-16 的转换器
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>> converter;

    // 原始的 UTF-8 字符串
    std::string narrow_string = "Hello, World!";

    // 转换为 UTF-16 宽字符串
    std::wstring wide_string = converter.from_bytes(narrow_string);

    // 输出宽字符串
    std::wcout << L"Wide string: " << wide_string << std::endl;

    // 将宽字符串转换回 UTF-8 字符串
    std::string converted_string = converter.to_bytes(wide_string);

    // 输出转换后的字符串
    std::cout << "Converted string: " << converted_string << std::endl;

    return 0;
}
```


**输出结果：**


```
Wide string: Hello, World!
Converted string: Hello, World!
```


### 示例 2：使用 codecvt_byname 进行编码转换


在这个示例中，我们将演示如何使用 `codecvt_byname` 类来创建一个基于名称的编码转换器，并使用它进行转换。


## 实例


```cpp
#include <iostream>
#include <codecvt>
#include <locale>
#include <string>

int main() {
    // 创建一个基于名称的转换器，这里使用 "zh_CN.UTF-8" 表示简体中文的 UTF-8 编码
    std::wstring_convert<std::codecvt_byname<wchar_t>> converter("zh_CN.UTF-8");

    // 原始的 UTF-8 字符串
    std::string narrow_string = "你好，世界！";

    // 转换为宽字符串
    std::wstring wide_string = converter.from_bytes(narrow_string);

    // 输出宽字符串
    std::wcout << L"Wide string: " << wide_string << std::endl;

    // 将宽字符串转换回 UTF-8 字符串
    std::string converted_string = converter.to_bytes(wide_string);

    // 输出转换后的字符串
    std::cout << "Converted string: " << converted_string << std::endl;

    return 0;
}
```


**输出结果：**


```
Wide string: 你好，世界！
Converted string: 你好，世界！
```



### std::codecvt 类模板特化


`std::codecvt` 有多个特化版本，用于不同的字符编码转换：


- `std::codecvt_utf8`：宽字符（`wchar_t`）与 UTF-8 之间的转换。
- `std::codecvt_utf8_utf16`：UTF-8 与 UTF-16 之间的转换。
- `std::codecvt_utf8`：UTF-8 与 UTF-32 之间的转换。


### std::wstring_convert 类模板


`std::wstring_convert` 类模板是一个辅助类，用于管理字符编码转换的生命周期和异常处理：


- `to_bytes`：将宽字符或其他编码的字符串转换为窄字符（字节序列）。
- `from_bytes`：将窄字符（字节序列）转换为宽字符或其他编码的字符串。


### 注意事项


- C++17 标准中 `std::codecvt` 已被弃用，建议在未来使用其他替代方案（如 ICU 库）进行字符编码转换。
- 对于跨平台应用程序，处理字符编码时应特别小心，确保在所有平台上行为一致。


### 总结


`` 提供了一套强大的工具，用于不同字符编码之间的转换，特别是 UTF-8、UTF-16 和宽字符之间的转换。虽然在 C++17 中已被弃用，但它在处理字符编码转换时仍然是一个有用的工具。了解和掌握这些工具的使用，可以帮助你编写更灵活和国际化的应用程序。如果你有特定的使用需求或问题，可以进一步讨论。








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-climits.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-cwchar.html) **













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