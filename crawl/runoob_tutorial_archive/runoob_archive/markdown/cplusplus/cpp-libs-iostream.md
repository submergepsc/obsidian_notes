# C++ 标准输入输出 --

- Source: https://www.runoob.com/cplusplus/cpp-libs-iostream.html

``库是 C++ 标准库中用于输入输出操作的头文件。

 定义了几个常用的流类和操作符，允许程序与标准输入输出设备（如键盘和屏幕）进行交互。

以下是``库的详细使用说明，包括其主要类和常见用法示例。


### 主要类


- `std::istream`：用于输入操作的抽象基类。
- `std::ostream`：用于输出操作的抽象基类。
- `std::iostream`：继承自`std::istream`和`std::ostream`，用于同时进行输入和输出操作。
- `std::cin`：标准输入流对象，通常与键盘关联。
- `std::cout`：标准输出流对象，通常与屏幕关联。
- `std::cerr`：标准错误输出流对象，不带缓冲，通常与屏幕关联。
- `std::clog`：标准日志流对象，带缓冲，通常与屏幕关联。


### 常用操作符


- `>>`：输入操作符，从输入流读取数据。
- ``库可以对输出进行格式化，例如设置宽度、精度和对齐方式。


## 实例


```cpp
#include <iostream>
#include <iomanip>

int main() {
    double pi = 3.14159;

    // 设置输出精度
    std::cout << std::setprecision(3) << pi << std::endl;

    // 设置输出宽度和对齐方式
    std::cout << std::setw(10) << std::left << pi << std::endl;
    std::cout << std::setw(10) << std::right << pi << std::endl;

    return 0;
}
```


### 流的状态检查:


可以检查输入输出流的状态，以确定操作是否成功。


## 实例


```cpp
#include <iostream>

int main() {
    int num;
    std::cout << "Enter a number: ";
    std::cin >> num;

    // 检查输入操作是否成功
    if (std::cin.fail()) {
        std::cerr << "Invalid input!" << std::endl;
    } else {
        std::cout << "You entered: " << num << std::endl;
    }

    return 0;
}
```


### 处理字符串输入


使用`std::getline`函数可以读取包含空格的整行输入。


## 实例


```cpp
#include <iostream>
#include <string>

int main() {
    std::string fullName;
    std::cout << "Enter your full name: ";
    std::getline(std::cin, fullName);
    std::cout << "Hello, " << fullName << "!" << std::endl;

    return 0;
}
```


以上示例展示了``库的基本用法和常见操作，帮助你在C++程序中进行输入输出处理。









	  AI 思考中...





			** [C++ vector 容器](https://www.runoob.com/cpp-vector.html)
			[C++ 文件输入输出库 – ](https://www.runoob.com/cpp-libs-fstream.html) **













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