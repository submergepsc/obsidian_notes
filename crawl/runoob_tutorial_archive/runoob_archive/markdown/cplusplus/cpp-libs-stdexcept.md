# C++ 异常处理库

- Source: https://www.runoob.com/cplusplus/cpp-libs-stdexcept.html

`` 是 C++ 标准库中的一个头文件，它定义了一组标准异常类，用于处理程序运行时的错误情况。


异常是程序运行时发生的错误，它们可以被捕获并处理，以避免程序的非正常终止。`` 头文件定义了一组从 `std::exception` 派生的异常类，这些类提供了一种标准的方式来报告和处理错误。


### 语法


要使用 `` 中的异常类，首先需要包含这个头文件：


```
#include <stdexcept>
```


然后，你可以使用这些异常类来抛出和捕获异常。例如：


```
throw std::runtime_error("An error occurred");
```


### 异常类


`` 头文件定义了以下异常类：


- `std::exception`：所有标准异常类的基类。
- `std::bad_exception`：当异常处理过程中发生错误时抛出。
- `std::bad_alloc`：当内存分配失败时抛出。
- `std::bad_cast`：当类型转换失败时抛出。
- `std::bad_typeid`：当 `typeid` 操作失败时抛出。
- `std::logic_error`：当逻辑错误发生时抛出，例如无效的输入参数。
- `std::domain_error`：当函数调用的参数不在有效范围内时抛出。
- `std::invalid_argument`：当函数调用的参数无效时抛出。
- `std::length_error`：当容器操作因为长度限制而失败时抛出。
- `std::out_of_range`：当访问容器的非法索引时抛出。
- `std::overflow_error`：当算术运算导致溢出时抛出。
- `std::range_error`：当函数返回值不在期望的范围内时抛出。
- `std::underflow_error`：当算术运算导致下溢时抛出。


## 实例


下面是一个使用 `` 的简单示例，演示了如何抛出和捕获异常：


## 实例


```cpp
#include <iostream>
#include <stdexcept>

void riskyFunction(int x) {
    if (x < 0) {
        throw std::invalid_argument("Negative value not allowed");
    }
    std::cout << "Processing " << x << std::endl;
}

int main() {
    try {
        riskyFunction(-1);
    } catch (const std::invalid_argument& e) {
        std::cerr << "Caught an exception: " << e.what() << std::endl;
    }
    return 0;
}
```


输出结果:


```
Caught an exception: Negative value not allowed
```


在这个示例中，`riskyFunction` 函数检查传入的参数是否为负数，如果是，则抛出 `std::invalid_argument` 异常。在 `main` 函数中，我们使用 `try-catch` 块来捕获并处理这个异常。


---


## 标准异常类

### std::exception

std::exception 是所有标准异常类的基类。它提供了一个虚函数 what()，用于返回描述异常的字符串。


## 实例


```cpp
#include <iostream>
#include <exception>

int main() {
    try {
        throw std::exception();
    } catch (const std::exception& e) {
        std::cout << "Caught exception: " << e.what() << std::endl;
    }
    return 0;
}
```


### std::logic_error

std::logic_error 派生自 std::exception，表示程序逻辑错误。它是一个抽象基类，通常由派生类来具体化。


## 实例


```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::logic_error("Logic error occurred");
    } catch (const std::logic_error& e) {
        std::cout << "Caught logic error: " << e.what() << std::endl;
    }
    return 0;
}
```


### std::invalid_argument

std::invalid_argument 派生自 std::logic_error，表示传递了无效的参数。


## 实例


```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::invalid_argument("Invalid argument provided");
    } catch (const std::invalid_argument& e) {
        std::cout << "Caught invalid argument: " << e.what() << std::endl;
    }
    return 0;
}
```


### std::domain_error

std::domain_error 派生自 std::logic_error，表示参数超出了有效范围。


## 实例


```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::domain_error("Domain error occurred");
    } catch (const std::domain_error& e) {
        std::cout << "Caught domain error: " << e.what() << std::endl;
    }
    return 0;
}
```


### std::length_error

std::length_error 派生自 std::logic_error，表示长度错误，如在容器操作中超出了最大长度限制。


## 实例


```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::length_error("Length error occurred");
    } catch (const std::length_error& e) {
        std::cout << "Caught length error: " << e.what() << std::endl;
    }
    return 0;
}
```


### std::out_of_range

std::out_of_range 派生自 std::logic_error，表示访问超出了有效范围。


## 实例


```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::out_of_range("Out of range error occurred");
    } catch (const std::out_of_range& e) {
        std::cout << "Caught out of range error: " << e.what() << std::endl;
    }
    return 0;
}
```


### std::runtime_error

std::runtime_error 派生自 std::exception，表示程序运行时错误。它是一个抽象基类，通常由派生类来具体化。


## 实例


```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::runtime_error("Runtime error occurred");
    } catch (const std::runtime_error& e) {
        std::cout << "Caught runtime error: " << e.what() << std::endl;
    }
    return 0;
}
```


### std::range_error

std::range_error 派生自 std::runtime_error，表示计算结果超出了表示范围。


## 实例


```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::range_error("Range error occurred");
    } catch (const std::range_error& e) {
        std::cout << "Caught range error: " << e.what() << std::endl;
    }
    return 0;
}
```


### std::overflow_error

std::overflow_error 派生自 std::runtime_error，表示算术溢出错误。


## 实例


```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::overflow_error("Overflow error occurred");
    } catch (const std::overflow_error& e) {
        std::cout << "Caught overflow error: " << e.what() << std::endl;
    }
    return 0;
}
```


### std::underflow_error

std::underflow_error 派生自 std::runtime_error，表示算术下溢错误。


## 实例


```cpp
#include <iostream>
#include <stdexcept>

int main() {
    try {
        throw std::underflow_error("Underflow error occurred");
    } catch (const std::underflow_error& e) {
        std::cout << "Caught underflow error: " << e.what() << std::endl;
    }
    return 0;
}
```


### 使用自定义异常类

除了标准异常类，我们还可以定义自己的异常类，继承自标准异常类。


## 实例


```cpp
#include <iostream>
#include <stdexcept>

class MyException : public std::runtime_error {
public:
    MyException(const std::string& message) : std::runtime_error(message) {}
};

int main() {
    try {
        throw MyException("My custom exception occurred");
    } catch (const MyException& e) {
        std::cout << "Caught custom exception: " << e.what() << std::endl;
    }
    return 0;
}
```


`` 是 C++ 标准库中一个重要的组成部分，它提供了一组标准异常类，使得错误处理更加一致和可预测。通过使用这些异常类，你可以编写更加健壮和易于维护的代码。对于初学者来说，理解异常的基本概念和如何使用 `` 中的异常类是非常重要的。








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-cstdio.html)
			[C++ 异常处理库 ](https://www.runoob.com/cpp-libs-exception.html) **













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