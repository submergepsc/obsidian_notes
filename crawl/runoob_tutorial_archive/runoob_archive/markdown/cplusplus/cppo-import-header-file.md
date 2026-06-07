# C++ 导入标准库

- Source: https://www.runoob.com/cplusplus/cppo-import-header-file.html

在 C++ 编程中，标准库（Standard Library）是一个非常重要的组成部分。


标准库提供了大量的预定义函数和类，可以帮助我们更高效地完成各种任务，为了使用这些功能，我们需要在程序中导入相应的标准库头文件。

本文将详细介绍如何在 C++ 中导入标准库，并解释一些常见的标准库头文件及其用途。


### 什么是C++标准库？


C++ 标准库是 C++ 语言的一部分，它包含了一系列的类和函数，用于处理常见的编程任务，如输入输出、字符串操作、数学计算、容器管理等。

标准库的设计目标是提供高效、可移植和易于使用的工具，以帮助开发者快速构建应用程序。


---

## 如何导入 C++ 标准库？


### 1、使用 #include 包含头文件


在 C++ 中，我们使用 `#include` 预处理指令来导入标准库头文件。

`#include` 指令告诉编译器在编译时将指定的头文件内容插入到当前文件中，头文件通常包含函数声明、类定义、宏定义等内容。


### 基本语法

导入 C++ 标准库语法格式如下：


```
#include <header_file>
```


其中，``是标准库头文件的名称。


### 实例


## 实例


```cpp
#include <iostream>  // 导入输入输出流库
#include <vector>    // 导入向量容器库
#include <cmath>     // 导入数学函数库
```


在上面的示例中，我们导入了三个常用的标准库头文件：


- `*`：提供了输入输出流的功能，如`std::cout`和`std::cin`。
- ``：提供了向量容器的实现，用于存储动态数组。
- ``：提供了常用的数学函数，如`sqrt()`、`sin()`、`cos()`等。


### 2、使用模块导入标准库（C++20/C++23）

从 C++20 开始，C++ 引入了模块（Modules），并在 C++23 中进一步完善了对标准库模块的支持。

模块提供了一种更高效、更安全的方式来导入标准库。


- **编译速度更快**：模块只编译一次，后续导入时直接使用编译好的二进制接口。
- **隔离性更好**：模块不会泄露宏定义和私有符号，避免了命名冲突。
- **依赖关系清晰**：模块的导入和导出机制使得代码的依赖关系更加清晰。


## 实例


```cpp
import std; // 导入整个标准库（C++23 特性）

int main() {
    std::cout << "Hello, C++23 Modules!\n"; // 使用 std::cout 输出
    return 0;
}
```


或者导入标准库的特定部分：


## 实例


```cpp
import std.core;      // 导入核心库
import std.iostream;  // 导入输入输出流库

int main() {
    std::cout << "Hello, C++23 Modules!\n";
    return 0;
}
```


目前，主流编译器对 C++ 模块的支持正在逐步完善。

以下是一些编译器的支持情况和使用方法：


**GCC**：需要启用 C++23 标准和模块支持。


编译命令示例：


```
g++ -std=c++23 -fmodules-ts -o program main.cpp
```


**Clang**：需要启用 C++23 标准和模块支持。


编译命令示例：


```
clang++ -std=c++23 -fmodules -o program main.cpp
```


**MSVC（Visual Studio）**：需要启用 C++23 标准和模块支持。


编译命令示例：


```
cl /std:c++23 /experimental:module /EHsc /Fe:program main.cpp
```


---


## 常见的C++标准库头文件


C++标准库包含了许多头文件，每个头文件都提供了特定的功能。

以下是一些常见的标准库头文件及其用途：


###


``是C++标准库中最常用的头文件之一，它提供了输入输出流的功能。通过这个头文件，我们可以使用`std::cout`和`std::cin`来进行标准输出和输入。


## 实例


```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```


###


``提供了向量容器的实现。向量是一个动态数组，可以在运行时动态调整大小。它提供了许多有用的成员函数，如`push_back()`、`size()`等。


## 实例


```cpp
#include <vector>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5};
    vec.push_back(6);
    for (int i : vec) {
        std::cout << i << " ";
    }
    return 0;
}
```


###


``提供了常用的数学函数，如平方根、三角函数、指数函数等。这些函数通常用于数值计算。


## 实例


```cpp
#include <cmath>
#include <iostream>

int main() {
    double x = 4.0;
    double y = std::sqrt(x);
    std::cout << "Square root of " << x << " is " << y << std::endl;
    return 0;
}
```


###


``提供了字符串类的实现。C++中的字符串类`std::string`比C语言中的字符数组更易于使用，并且提供了许多有用的成员函数，如`length()`、`substr()`等。


## 实例


```cpp
#include <string>
#include <iostream>

int main() {
    std::string str = "Hello, C++!";
    std::cout << "Length of string: " << str.length() << std::endl;
    return 0;
}
```


###


``提供了许多常用的算法，如排序、查找、遍历等。这些算法可以应用于各种容器，如向量、列表等。


## 实例


```cpp
#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec = {5, 3, 1, 4, 2};
    std::sort(vec.begin(), vec.end());
    for (int i : vec) {
        std::cout << i << " ";
    }
    return 0;
}
```


---


## 注意事项


- **命名空间**：C++标准库中的函数和类通常位于`std`命名空间中。因此，在使用这些函数和类时，通常需要加上`std::`前缀，或者使用`using namespace std;`来避免重复输入`std::`。
- **头文件保护**：在编写自己的头文件时，通常需要使用头文件保护（Header Guards）来防止重复包含。标准库头文件已经包含了这些保护机制，因此我们不需要担心重复包含的问题。
- **兼容性**：C++标准库在不同的编译器和平台上可能会有一些差异。因此，在编写跨平台的代码时，需要注意这些差异，并确保代码在不同环境下都能正常工作。










	  AI 思考中...





			* [C++ 标准库 ](https://www.runoob.com/cpp-libs-numbers.html)
			[C++ OpenCV](https://www.runoob.com/cpp-opencv.html) **













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