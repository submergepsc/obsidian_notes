# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-sstream.html

在 C++ 编程中，处理字符串和数字之间的转换是一项常见的任务。

`sstream` 是 C++ 标准库中的一个组件，它提供了一种方便的方式来处理字符串流（可以像处理流一样处理字符串）。

`` 允许你将字符串当作输入/输出流来使用，这使得从字符串中读取数据或将数据写入字符串变得非常简单。


### 定义


`sstream`是 C++ 标准库中的一个命名空间，它包含了几个类，用于处理字符串流，这些类包括：


- `istringstream`：用于从字符串中读取数据。
- `ostringstream`：用于将数据写入字符串。
- `stringstream`：是`istringstream`和`ostringstream`的组合，可以同时进行读取和写入操作。


### 语法


使用`sstream`的基本语法如下：


```
#include <sstream>

// 使用istringstream
std::istringstream iss("some data");

// 使用ostringstream
std::ostringstream oss;

// 使用stringstream
std::stringstream ss;
```


## 实例


### 从字符串读取数据


下面是一个使用 `istringstream` 从字符串中读取整数和浮点数的例子：


## 实例


```cpp
#include <iostream>
#include <sstream>

int main() {
    std::string data = "10 20.5";
    std::istringstream iss(data);

    int i;
    double d;

    iss >> i >> d;

    std::cout << "Integer: " << i << std::endl;
    std::cout << "Double: " << d << std::endl;

    return 0;
}
```


**输出结果：**


```
Integer: 10
Double: 20.5
```


### 向字符串写入数据


下面是一个使用 `ostringstream` 将数据写入字符串的例子：


## 实例


```cpp
#include <iostream>
#include <sstream>

int main() {
    std::ostringstream oss;
    int i = 100;
    double d = 200.5;

    oss << i << " " << d;

    std::string result = oss.str();
    std::cout << "Resulting string: " << result << std::endl;

    return 0;
}
```


**输出结果：**


```
Resulting string: 100 200.5
```


### 使用stringstream进行读写操作


下面是一个使用 `stringstream` 同时进行读取和写入操作的例子：


## 实例


```cpp
#include <iostream>
#include <sstream>

int main() {
    std::string data = "30 40.5";
    std::stringstream ss(data);

    int i;
    double d;

    // 从stringstream读取数据
    ss >> i >> d;

    std::cout << "Read Integer: " << i << ", Double: " << d << std::endl;

    // 向stringstream写入数据
    ss.str(""); // 清空stringstream
    ss << "New data: " << 50 << " " << 60.7;

    std::string newData = ss.str();
    std::cout << "New data string: " << newData << std::endl;

    return 0;
}
```


**输出结果：**


```
Read Integer: 30, Double: 40.5
New data string: New data: 50 60.7
```


## 总结


`sstream` 是 C++ 标准库中一个非常有用的组件，它简化了字符串和基本数据类型之间的转换。通过上述实例，我们可以看到如何使用 `istringstream`、`ostringstream` 和 `stringstream` 来实现这些转换。掌握这些技能将帮助你在 C++ 编程中更加高效地处理字符串数据。








	  AI 思考中...





			** [C++ 文件输入输出库 – ](https://www.runoob.com/cpp-libs-fstream.html)
			[C++ 标准库 *](https://www.runoob.com/cpp-libs-iomanip.html) *













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