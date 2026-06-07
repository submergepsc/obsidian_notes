# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-locale.html

在 C++ 标准库中，`locale` 类提供了一种机制来控制程序的本地化行为，特别是与语言和文化相关的格式设置和转换操作。`locale` 类在 `#include ` 头文件中定义。


C++ 标准库中的 `locale` 模块提供了一种方式，允许程序根据用户的区域设置来处理文本数据，如数字、日期和时间的格式化，以及字符串的比较和排序。这使得编写国际化应用程序变得更加容易。


### 语法


以下是使用 `locale` 类的基本语法：


```
#include <iostream>
#include <locale>

int main() {
    // 创建一个默认的 locale 对象
    std::locale loc;

    // 使用 locale 对象
    std::cout.imbue(loc); // 设置 cout 的 locale

    // 显示当前 locale 的名称
    std::cout << "Current locale: " << loc.name() << std::endl;

    // 更多操作...
    return 0;
}
```


## 实例


### 1. 基本使用


下面是一个简单的示例，展示如何使用 `locale` 来格式化数字：


## 实例


```cpp
#include <iostream>
#include <locale>

int main() {
    std::locale loc("en_US.UTF-8"); // 设置为美国英语
    std::cout.imbue(loc); // 设置 cout 的 locale

    double number = 1234567.89;
    std::cout << "Formatted number: " << number << std::endl;

    return 0;
}
```


**输出结果**:


```
Formatted number: 1,234,567.89
```


### 2. 比较字符串


使用 `locale` 可以按照特定区域设置的规则来比较字符串：


## 实例


```cpp
#include <iostream>
#include <locale>
#include <string>

int main() {
    std::locale loc("en_US.UTF-8");
    std::string str1 = "apple";
    std::string str2 = "banana";

    if (std::use_facet<std::collate<char>>(loc).compare(str1.c_str(), str1.c_str() + str1.size(),
                                                       str2.c_str(), str2.c_str() + str2.size()) < 0) {
        std::cout << str1 << " comes before " << str2 << std::endl;
    } else {
        std::cout << str1 << " comes after " << str2 << std::endl;
    }

    return 0;
}
```


**输出结果**:


```
apple comes before banana
```


### 3. 日期和时间格式化


`locale` 也可以用来格式化日期和时间：


## 实例


```cpp
#include <iostream>
#include <locale>
#include <ctime>

int main() {
    std::locale loc("en_US.UTF-8");
    std::cout.imbue(loc);

    std::time_t now = std::time(nullptr);
    std::tm* timeinfo = std::localtime(&now);

    char buffer[100];
    std::strftime(buffer, sizeof(buffer), "%A, %B %d, %Y", timeinfo);
    std::cout << "Current date: " << buffer << std::endl;

    return 0;
}
```


**输出结果**（示例）:


```
Current date: Monday, March 14, 2023
```


`locale` 类在 C++ 标准库中是一个强大的工具，它允许开发者编写能够适应不同区域设置的应用程序。








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-random.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-cstdlib.html) **













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