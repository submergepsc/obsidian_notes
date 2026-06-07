# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-cstdlib.html

`` 是 C++ 标准库中的一个头文件，提供了各种通用工具函数，包括内存分配、进程控制、环境查询、排序和搜索、数学转换、伪随机数生成等。这些函数最初来自 C 标准库 ``，在 C++ 中进行了标准化和扩展。


### 语法


在 C++ 程序中，要使用 `cstdlib` 中的函数，需要先包含这个头文件：


```
#include <cstdlib>
```


### 常用函数


`cstdlib` 中包含了许多有用的函数，以下是一些常用的函数及其简要说明：


- `exit(int status)`: 终止程序执行，并返回一个状态码。
- `system(const char* command)`: 执行一个命令行字符串。
- `malloc(size_t size)`: 分配指定大小的内存。
- `free(void* ptr)`: 释放之前分配的内存。
- `atoi(const char* str)`: 将字符串转换为整数。
- `atof(const char* str)`: 将字符串转换为浮点数。
- `rand()`: 生成一个随机数。
- `srand(unsigned int seed)`: 设置随机数生成器的种子。


### 实例


以下是一些使用 `cstdlib` 中函数的实例：


### 实例 1：使用 exit 函数


## 实例


```cpp
#include <iostream>
#include <cstdlib>

int main() {
    std::cout << "This program will exit now." << std::endl;
    exit(0); // 正常退出程序
    return 0; // 这行代码不会被执行
}
```


**输出结果：**


```
This program will exit now.
```


### 实例 2：使用 system 函数


## 实例


```cpp
#include <iostream>
#include <cstdlib>

int main() {
    std::cout << "Executing a system command: dir" << std::endl;
    system("dir"); // 在 Windows 上显示当前目录的文件和文件夹
    return 0;
}
```


**输出结果：**


```
Executing a system command: dir
```


然后显示当前目录的文件和文件夹列表。


### 实例 3：使用 malloc 和 free 函数


## 实例


```cpp
#include <iostream>
#include <cstdlib>

int main() {
    int* ptr = (int*)malloc(10 * sizeof(int)); // 分配内存
    if (ptr == NULL) {
        std::cout << "Memory allocation failed." << std::endl;
        return 1;
    }

    for (int i = 0; i < 10; ++i) {
        ptr[i] = i * i; // 使用分配的内存
    }

    for (int i = 0; i < 10; ++i) {
        std::cout << "Element " << i << ": " << ptr[i] << std::endl;
    }

    free(ptr); // 释放内存
    return 0;
}
```


**输出结果：**


```
Element 0: 0
Element 1: 1
Element 2: 4
...
Element 9: 81
```


### 实例 4：使用 atoi 和 atof 函数


## 实例


```cpp
#include <iostream>
#include <cstdlib>

int main() {
    std::string str1 = "123";
    std::string str2 = "456.78";

    int num1 = std::atoi(str1.c_str()); // 将字符串转换为整数
    double num2 = std::atof(str2.c_str()); // 将字符串转换为浮点数

    std::cout << "Integer: " << num1 << std::endl;
    std::cout << "Float: " << num2 << std::endl;
    return 0;
}
```


**输出结果：**


```
Integer: 123
Float: 456.78
```


### 实例 5：使用 rand 和 srand 函数


## 实例


```cpp
#include <cstdlib>
#include <iostream>
#include <ctime>

int main() {
    std::srand(std::time(nullptr));  // 使用当前时间作为随机数种子
    for (int i = 0; i < 5; ++i) {
        std::cout << std::rand() % 100 << " ";  // 生成0到99之间的随机数
    }
    std::cout << std::endl;

    return 0;
}
```


**输出结果：**


```
53 22 62 68 62
```









	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-locale.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-cfloat.html) **













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