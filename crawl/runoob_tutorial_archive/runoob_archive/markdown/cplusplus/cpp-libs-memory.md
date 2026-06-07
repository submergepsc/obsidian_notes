# C++ 内存管理库

- Source: https://www.runoob.com/cplusplus/cpp-libs-memory.html

`` 是 C++ 标准库中的一个头文件，它包含了用于动态内存管理的模板和函数。


在 C++ 中，内存管理是一个重要的概念。动态内存管理允许程序在运行时分配和释放内存，这在处理不确定大小的数据结构时非常有用。然而，不正确的内存管理可能导致内存泄漏、野指针等问题。

`` 头文件提供了智能指针等工具，帮助开发者更安全地管理动态内存。


### 智能指针


智能指针是 `` 头文件中的核心内容。它们是 C++11 引入的特性，用于自动管理动态分配的内存。智能指针的主要类型有：


- `std::unique_ptr`：独占所有权的智能指针，同一时间只能有一个 `unique_ptr` 指向特定内存。
- `std::shared_ptr`：共享所有权的智能指针，多个 `shared_ptr` 可以指向同一内存，内存在最后一个 `shared_ptr` 被销毁时释放。
- `std::weak_ptr`：弱引用智能指针，用于与 `shared_ptr` 配合使用，避免循环引用导致的内存泄漏。


## 实例


### 使用 std::unique_ptr


## 实例


```cpp
#include <iostream>
#include <memory>

class MyClass {
public:
    void doSomething() {
        std::cout << "Doing something" << std::endl;
    }
};

int main() {
    std::unique_ptr<MyClass> myPtr(new MyClass());
    myPtr->doSomething(); // 使用智能指针调用成员函数

    // 当 main 函数结束时，myPtr 被销毁，自动释放 MyClass 对象的内存
    return 0;
}
```


输出结果：


```
Doing something
```


### 使用 std::shared_ptr


## 实例


```cpp
#include <iostream>
#include <memory>

class MyClass {
public:
    void doSomething() {
        std::cout << "Doing something" << std::endl;
    }
};

int main() {
    std::shared_ptr<MyClass> myPtr1(new MyClass());
    std::shared_ptr<MyClass> myPtr2 = myPtr1;

    myPtr1->doSomething(); // 使用 myPtr1 调用成员函数
    myPtr2->doSomething(); // 使用 myPtr2 调用成员函数

    // 当 myPtr1 和 myPtr2 都被销毁时，MyClass 对象的内存才会被释放
    return 0;
}
```


输出结果：


```
Doing something
Doing something
```


### 使用 std::weak_ptr


`std::weak_ptr` 通常不单独使用，而是与 `std::shared_ptr` 结合使用，以解决循环引用问题。


## 实例


```cpp
#include <iostream>
#include <memory>

class Node {
public:
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;

    Node() : next(nullptr), prev() {}
};

int main() {
    std::shared_ptr<Node> node1 = std::make_shared<Node>();
    std::shared_ptr<Node> node2 = std::make_shared<Node>();

    node1->next = node2;
    node2->prev = node1;

    // 循环引用，但使用 weak_ptr 避免了内存泄漏
    return 0;
}
```


在这个例子中，`node1` 和 `node2` 形成了循环引用。由于 `prev` 是 `weak_ptr`，当 `node1` 和 `node2` 的 `shared_ptr` 被销毁时，它们指向的内存也会被正确释放。


## 分配器

分配器是  中的另一重要部分。

分配器用于为容器分配内存，标准库的所有容器都使用分配器来处理内存分配。


### std::allocator

std::allocator 是标准分配器，提供了基本的内存分配和释放功能。


## 实例


```cpp
#include <memory>
#include <vector>

int main() {
    std::allocator<int> alloc;
    int* p = alloc.allocate(1); // 分配内存
    alloc.construct(p, 42); // 构造对象

    std::cout << *p << std::endl;

    alloc.destroy(p); // 销毁对象
    alloc.deallocate(p, 1); // 释放内存

    return 0;
}
```


## 其他内存管理工具

### std::align

std::align 用于调整指针的对齐方式，以确保所分配内存满足特定对齐要求。


## 实例


```cpp
#include <memory>
#include <iostream>

int main() {
    alignas(16) char buffer[64];
    void* p = buffer;
    size_t space = sizeof(buffer);

    void* aligned_ptr = std::align(16, sizeof(int), p, space);
    if (aligned_ptr) {
        std::cout << "Memory aligned\n";
    } else {
        std::cout << "Memory alignment failed\n";
    }

    return 0;
}
```


`` 头文件是 C++ 标准库中处理动态内存管理的重要部分。

通过使用智能指针，如 `unique_ptr`、`shared_ptr` 和 `weak_ptr`，开发者可以更安全、更有效地管理内存，避免常见的内存管理错误。希望这篇文章能帮助初学者更好地理解和使用 C++ 的 `` 头文件。








	  AI 思考中...





			** [C++ 内存管理库 ](https://www.runoob.com/cpp-libs-new.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-cstdint.html) **













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