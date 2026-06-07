# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-iomanip.html

`` 是 C++ 标准库中的一个头文件，它提供了对输入/输出流的格式化操作。

`iomanip` 库中的函数允许开发者控制输出格式，如设置小数点后的位数、设置宽度、对齐方式等。


`iomanip` 是 Input/Output Manipulators 的缩写，它提供了一组操作符，用于控制 C++ 标准库中的输入/输出流的格式，适用以下场景：


- 科学计算中浮点数格式的处理；
- 数据对齐与美化；
- 显示特定进制或格式的数值。


### 语法


`iomanip` 库中的函数通常与 `>` 操作符一起使用，以实现对输出流的控制。

以下是一些常用的 `iomanip` 函数：


| 函数/操纵符 | 功能 | 实例代码 | 输出结果 |
| --- | --- | --- | --- |
| std::setw(int n) | 设置字段宽度，为下一次输出指定宽度 | std::cout | 42 |
| std::setfill(char) | 设置填充字符（默认是空格） | std::cout | ***42 |
| std::left | 设置左对齐 | std::cout | 42 |
| std::right | 设置右对齐 | std::cout | 42 |
| std::internal | 符号靠左，其余靠右 | std::cout | - 42 |
| std::setprecision(int) | 设置浮点数的有效位数 | std::cout | 3.14 |
| std::fixed | 设置定点格式输出浮点数 | std::cout | 3.14 |
| std::scientific | 设置科学计数法格式输出浮点数 | std::cout | 3.141590e+00 |
| std::hex | 设置整数以 16 进制显示 | std::cout | 2a |
| std::oct | 设置整数以 8 进制显示 | std::cout | 52 |
| std::dec | 设置整数以 10 进制显示（默认） | std::cout | 42 |
| std::showbase | 显示进制前缀（如 0x 表示 16 进制） | std::cout | 0x2a |
| std::noshowbase | 隐藏进制前缀（默认） | std::cout | 2a |
| std::uppercase | 16 进制字母显示为大写 | std::cout | 2A |
| std::nouppercase | 16 进制字母显示为小写（默认） | std::cout | 2a |
| std::showpos | 在正数前显示 + 符号 | std::cout | +42 |
| std::noshowpos | 不显示正数的 + 符号（默认） | std::cout | 42 |
| std::boolalpha | 布尔值以 true/false 输出 | std::cout | true |
| std::noboolalpha | 布尔值以 1/0 输出（默认） | std::cout | 1 |
| std::setbase(int n) | 设置整数的进制（支持 8、10、16） | std::cout | 2a |
| std::resetiosflags | 重置指定的流状态 | std::cout | 2a |
| std::setiosflags | 设置指定的流状态 | std::cout | 0x2a |


## 实例


### 1. 设置宽度


使用 `setw` 可以设置输出的宽度。如果输出内容的字符数少于设置的宽度，剩余部分将用空格填充。


## 实例


```cpp
#include <iostream>
#include <iomanip>

int main() {
    std::cout << std::setw(10) << "Hello" << std::endl;
    return 0;
}
```


**输出结果:**


```
Hello
```


### 2. 设置精度


使用 `setprecision` 可以设置设置浮点数的有效位数。


## 实例


```cpp
#include <iostream>
#include <iomanip>

int main() {
    double pi = 3.141592653589793;
    std::cout << "Default: " << pi << "\n";
    std::cout << "Set precision (3): " << std::setprecision(3) << pi << "\n";
    std::cout << "Set precision (7): " << std::setprecision(7) << pi << "\n";
    return 0;
}
```


**输出结果:**


```
Default: 3.14159
Set precision (3): 3.14
Set precision (7): 3.141593
```


### 3. 固定小数点和科学计数法


`fixed` 和 `scientific` 可以控制浮点数的输出格式。


## 实例


```cpp
#include <iostream>
#include <iomanip>

int main() {
    double num = 123456789.0;
    std::cout << "Fixed: " << std::fixed << num << std::endl;
    std::cout << "Scientific: " << std::scientific << num << std::endl;
    return 0;
}
```


**输出结果:**


```
Fixed: 123456789.000000
Scientific: 1.23456789e+08
```


### 4. 设置填充字符


使用 `setfill` 可以设置填充字符，通常与 `setw` 一起使用。


## 实例


```cpp
#include <iostream>
#include <iomanip>

int main() {
    std::cout << std::setfill('*') << std::setw(10) << "World" << std::endl;
    return 0;
}
```


**输出结果:**


```
*****World
```


### 5. 设置和重置格式标志


`setiosflags` 和 `resetiosflags` 可以设置或重置流的格式标志。


## 实例


```cpp
#include <iostream>
#include <iomanip>

int main() {
    std::cout << std::setiosflags(std::ios::uppercase) << std::hex << 255 << std::endl;
    std::cout << std::resetiosflags(std::ios::uppercase) << std::hex << 255 << std::endl;
    return 0;
}
```


**输出结果:**


```
FF
ff
```










	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-sstream.html)
			[C++ 容器类 ](https://www.runoob.com/cpp-libs-array.html) **













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