# C++ 内存管理库

- Source: https://www.runoob.com/cplusplus/cpp-libs-new.html

C++ 是一种功能强大的编程语言，它提供了丰富的标准库来帮助开发者更高效地编写代码。

在 C++ 中，`` 是一个非常重要的头文件，它包含了用于动态内存分配的函数和异常类型。

动态内存分配允许程序在运行时请求内存，这在处理不确定大小的数据结构时非常有用。


`` 头文件定义了以下几个关键组件：


- `new` 运算符：用于动态分配内存。
- `delete` 运算符：用于释放动态分配的内存。
- `nothrow` 运算符：用于在内存分配失败时不抛出异常。
- `std::bad_alloc` 异常：当内存分配失败时抛出。


## 语法


### 使用 new 运算符


`new` 运算符用于在堆上分配内存。其基本语法如下：


```
<code class="language-cpp">pointer new (type [, initializer]);</code>
```


- `pointer` 是指向分配的内存的指针。
- `type` 是要分配的对象的类型。
- `initializer` 是一个可选的初始化表达式。


### 使用 delete 运算符


`delete` 运算符用于释放之前使用 `new` 分配的内存。其基本语法如下：


```
<code class="language-cpp">delete pointer;</code>
```


- `pointer` 是之前使用 `new` 分配的内存的指针。


## 实例

动态分配单个对象:


## 实例


```cpp
#include <iostream>
#include <new> // 包含 <new> 头文件

class MyClass {
public:
    int value;
    MyClass() : value(0) {}
};

int main() {
    MyClass* myObject = new MyClass; // 分配一个 MyClass 对象
    myObject->value = 10; // 使用点操作符访问成员
    std::cout << "Value: " << myObject->value << std::endl;

    delete myObject; // 释放内存
    return 0;
}
```


输出结果：


```
Value: 10
```


动态分配数组:


## 实例


```cpp
#include <iostream>
#include <new>

int main() {
    int* myArray = new int[10]; // 分配一个包含10个整数的数组
    for (int i = 0; i < 10; ++i) {
        myArray[i] = i * 2; // 初始化数组
    }

    for (int i = 0; i < 10; ++i) {
        std::cout << "Array[" << i << "]: " << myArray[i] << std::endl;
    }

    delete[] myArray; // 释放数组内存
    return 0;
}
```


输出结果：


```
Array[0]: 0
Array[1]: 2
Array[2]: 4
Array[3]: 6
Array[4]: 8
Array[5]: 10
Array[6]: 12
Array[7]: 14
Array[8]: 16
Array[9]: 18
```


使用 nothrow 避免异常:


## 实例


```cpp
#include <iostream>
#include <new>

int main() {
    int* myArray = new(std::nothrow) int[10000000]; // 尝试分配一个大数组
    if (!myArray) {
        std::cout << "Memory allocation failed." << std::endl;
    } else {
        std::cout << "Memory allocation succeeded." << std::endl;
        delete[] myArray; // 释放内存
    }
    return 0;
}
```


输出结果：


```
Memory allocation failed. // 或者 Memory allocation succeeded. 取决于系统内存情况
```


### 异常处理

当使用 new 运算符分配内存失败时，C++ 会抛出一个 std::bad_alloc 异常。

开发者可以通过 try-catch 块来捕获并处理这个异常。


## 实例


```cpp
#include <iostream>
#include <new>

int main() {
    try {
        int* myArray = new int[10000000]; // 尝试分配一个大数组
        std::cout << "Memory allocation succeeded." << std::endl;
        delete[] myArray; // 释放内存
    } catch (const std::bad_alloc& e) {
        std::cout << "Exception caught: " << e.what() << std::endl;
    }
    return 0;
}
```


输出结果：


```
Exception caught: std::bad_alloc // 如果内存分配失败
```










	  AI 思考中...





			** [C++ 算法库 ](https://www.runoob.com/cpp-libs-algorithm.html)
			[C++ 内存管理库 ](https://www.runoob.com/cpp-libs-memory.html) **













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