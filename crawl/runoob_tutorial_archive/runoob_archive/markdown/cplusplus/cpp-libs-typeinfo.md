# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-typeinfo.html

在 C++ 中，`` 是标准库的一部分，它提供了运行时类型识别（RTTI，Run-Time Type Identification）功能。RTTI 允许程序在运行时确定对象的类型。这是通过使用 `typeid` 运算符和 `type_info` 类实现的。


`type_info` 类是一个抽象基类，它提供了关于类型信息的接口。每个类型都有一个与之关联的 `type_info` 对象，可以通过 `typeid` 运算符访问。


## 语法

`` 相关的主要语法：


- `typeid` 运算符：用于获取对象的类型信息。
- `type_info` 类：包含类型信息的类。


## 类型信息类 type_info



`typeinfo` 头文件提供了对类型信息的运行时支持。它主要包含两个核心组件：`std::type_info` 类和 `typeid` 运算符。`typeinfo` 允许程序在运行时获取对象的类型信息，这在多态和类型安全的代码中非常有用。以下是对 `typeinfo` 的详细介绍：


### std::type_info 类


`std::type_info` 类是 `typeinfo` 头文件的核心类，用于描述一个类型。它提供了多个成员函数用于查询类型的信息。常用成员函数如下：


- `const char* name() const noexcept;` 返回一个指向类型名称的 C 字符串指针。注意，这个名称不一定是人类可读的类型名，其格式由编译器实现决定。
- `bool before(const std::type_info& rhs) const noexcept;` 按照某种顺序比较两个 `type_info` 对象，返回当前对象是否在 `rhs` 之前。
- `bool operator==(const std::type_info& rhs) const noexcept;` 比较两个 `type_info` 对象是否表示相同的类型。
- `bool operator!=(const std::type_info& rhs) const noexcept;` 比较两个 `type_info` 对象是否表示不同的类型。


### typeid 运算符


`typeid` 运算符用于在运行时获取类型信息。`typeid` 可以作用于对象（带有多态行为的指针或引用）或类型（无需实例化对象）。


- `typeid(object)`：返回一个 `std::type_info` 对象，表示 `object` 的动态类型。如果 `object` 是一个多态类型（即包含虚函数），则 `typeid` 会返回该对象的实际类型。
- `typeid(T)`：返回一个 `std::type_info` 对象，表示类型 `T`。


## 实例


下面是一个使用 `` 的简单示例：


## 实例


```cpp
#include <iostream>
#include <typeinfo>

class Base {
public:
    virtual void show() { std::cout << "Base show" << std::endl; }
};

class Derived : public Base {
public:
    void show() override { std::cout << "Derived show" << std::endl; }
};

int main() {
    Base* basePtr = new Derived();
    Base* basePtr2 = new Base();

    std::cout << "Type of basePtr: " << typeid(*basePtr).name() << std::endl;
    std::cout << "Type of basePtr2: " << typeid(*basePtr2).name() << std::endl;

    if (typeid(*basePtr) == typeid(Derived)) {
        std::cout << "basePtr is of type Derived" << std::endl;
    } else {
        std::cout << "basePtr is not of type Derived" << std::endl;
    }

    delete basePtr;
    delete basePtr2;

    return 0;
}
```


输出结果:


```
Type of basePtr: 9Derived  // 注意：typeid的name()返回的类型名称可能因编译器而异
Type of basePtr2: 8Base     // 同上
basePtr is of type Derived
```


### 注意事项


- RTTI 功能依赖于编译器的实现，因此 `typeid` 运算符返回的类型名称可能因编译器而异。
- 使用 RTTI 可能会对程序性能产生一定影响，因为它需要在运行时进行类型检查。
- RTTI 只适用于多态类型，即具有虚函数的类。


`` 提供了一种在运行时识别对象类型的方法，这对于实现多态和类型安全非常有用。然而，开发者应该谨慎使用 RTTI，以避免不必要的性能开销和潜在的类型错误。








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-type_traits.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-atomic.html) **













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