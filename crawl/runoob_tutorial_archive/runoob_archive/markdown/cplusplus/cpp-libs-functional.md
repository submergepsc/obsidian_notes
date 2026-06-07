# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-functional.html

C++ 标准库中的 `` 头文件提供了一组函数模板，这些模板允许我们使用函数对象（function objects）作为参数传递给算法，或者作为算法的返回值。函数对象是那些重载了 `operator()` 的对象，它们可以像普通函数一样被调用。


在 C++ 中，函数对象是一种特殊的类，它重载了 `operator()` 来允许对象像函数一样被调用。这使得我们可以将行为作为对象传递，增加了代码的灵活性和可重用性。


## 语法


要使用 `` 头文件中的功能，你需要在你的 C++ 程序中包含这个头文件：


```
#include <functional>
```


## 常用函数对象


`` 头文件中定义了一些常用的函数对象，包括：


- `std::function`：一个通用的多态函数封装器。
- `std::bind`：用于绑定函数的参数。
- `std::plus`、`std::minus`、`std::multiplies`、`std::divides`、`std::modulus`：基本的算术操作。
- `std::equal_to`、`std::not_equal_to`、`std::greater`、`std::less`、`std::greater_equal`、`std::less_equal`：比较操作。
- `std::unary_negate`、`std::binary_negate`：逻辑否定操作。
- `std::logical_and`、`std::logical_or`、`std::logical_not`：逻辑操作。


## 实例


### 使用 std::function


`std::function` 是一个模板类，可以存储、调用和复制任何可调用对象，比如函数、lambda 表达式或函数对象。


## 实例


```cpp
#include <iostream>
#include <functional>

void greet() {
    std::cout << "Hello, World!" << std::endl;
}

int main() {
    std::function<void()> f = greet; // 使用函数
    f(); // 输出: Hello, World!

    std::function<void()> lambda = []() {
        std::cout << "Hello, Lambda!" << std::endl;
    };
    lambda(); // 输出: Hello, Lambda!

    return 0;
}
```


### 使用 std::bind


`std::bind` 允许我们创建一个可调用对象，它在调用时会将给定的参数绑定到一个函数或函数对象。


## 实例


```cpp
#include <iostream>
#include <functional>

int add(int a, int b) {
    return a + b;
}

int main() {
    auto bound_add = std::bind(add, 5, std::placeholders::_1);
    std::cout << bound_add(10) << std::endl; // 输出: 15

    return 0;
}
```


在这个例子中，`std::placeholders::_1` 是一个占位符，它在调用 `bound_add` 时会被实际的参数替换。


### 使用比较函数对象


比较函数对象可以用于算法，比如 `std::sort`。


## 实例


```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

bool compare(int a, int b) {
    return a < b;
}

int main() {
    std::vector<int> v = {5, 3, 9, 1, 4};
    std::sort(v.begin(), v.end(), compare); // 使用自定义比较函数
    for (int i : v) {
        std::cout << i << " "; // 输出: 1 3 4 5 9
    }

    std::sort(v.begin(), v.end(), std::less<int>()); // 使用标准库比较函数对象
    for (int i : v) {
        std::cout << i << " "; // 输出: 1 3 4 5 9
    }

    return 0;
}
```


`` 头文件是 C++ 标准库中一个非常强大的部分，它提供了丰富的函数对象和工具，使得我们可以编写更灵活、更可重用的代码。通过使用函数对象，我们可以将行为作为参数传递，或者将它们存储在容器中，从而实现更高级的编程技术。








	  AI 思考中...





			** [C++ 标准库 *](https://www.runoob.com/cpp-libs-iterator.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-numeric.html) *













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