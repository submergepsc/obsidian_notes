# C++ 标准库中的

- Source: https://www.runoob.com/cplusplus/cpp-libs-cassert.html

`` 是 C++ 标准库中的一个头文件，它提供了断言功能，用于在程序运行时检查条件是否为真。如果条件为假，程序将终止执行，并输出一条错误信息。断言主要用于调试阶段，以确保程序的逻辑正确性。


断言是一种调试工具，用于在开发过程中检查程序的运行状态。如果断言失败，程序将立即终止，这有助于开发者快速定位问题。


## 语法


`cassert` 中的 `assert` 宏的基本语法如下：


```
#include <cassert>

assert(expression);
```


其中 `expression` 是一个布尔表达式，如果表达式的结果为 `true`，则程序继续执行；如果结果为 `false`，则程序将终止，并输出一条错误信息。


## 实例


下面是一个使用 `cassert` 的简单示例：


## 实例


```cpp
#include <iostream>
#include <cassert>

int main() {
    int a = 5;
    int b = 3;

    // 检查 a 是否大于 b
    assert(a > b);

    // 如果 a 不大于 b，程序将在这里终止，并输出错误信息
    std::cout << "a is greater than b" << std::endl;

    return 0;
}
```


### 输出结果


当运行上述程序时，由于 `a` 确实大于 `b`，所以程序将正常执行，并输出：


```
a is greater than b
```


如果我们修改 `a` 的值为 2，使其不大于 `b`，程序将输出错误信息并终止：


```
Assertion failed: a > b, file main.cpp, line 8.
```


## 断言的高级用法


`assert` 宏还可以接受一个额外的表达式，用于输出自定义的错误信息：


## 实例


```cpp
#include <iostream>
#include <cassert>

int main() {
    int x = 10;
    int y = 0;

    // 使用自定义错误信息
    assert(y != 0 && "Division by zero error");

    int result = x / y; // 这行代码将不会执行，因为断言已经失败

    return 0;
}
```


当运行上述程序时，由于 `y` 为 0，断言将失败，并输出：


```
Division by zero error
Assertion failed: y != 0 && "Division by zero error", file main.cpp, line 8.
```


### 注意事项


- 在发布版本的程序中，通常需要禁用断言，以避免程序在运行时意外终止。这可以通过定义 `NDEBUG` 宏来实现：
```
#define NDEBUG
#include <cassert>
```

- 断言应该只用于检查程序的逻辑错误，而不是用于处理运行时的错误。运行时错误应该通过异常处理或其他机制来处理。
- 断言的表达式应该是简单的，避免使用复杂的逻辑或计算，以减少性能开销。


通过使用 `cassert` 中的 `assert` 宏，开发者可以在开发过程中快速发现并修复逻辑错误，提高程序的稳定性和可靠性。








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-cwchar.html)
			[C++ 数据结构](https://www.runoob.com/cpp-data-structures.html) **













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