# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-type_traits.html

`` 是 C++ 标准库中一个非常有用的头文件，它包含了一组编译时检查类型特性的工具。这些工具可以帮助开发者在编译时确定类型的特性，从而实现更安全、更灵活的代码。


`` 头文件定义了一组模板，这些模板可以用于查询和操作类型属性。这些属性包括但不限于：


- 是否是整数类型
- 是否是浮点类型
- 是否是指针类型
- 是否是引用类型
- 是否是可调用的（函数或函数指针）


## 语法


`` 中的模板通常使用 `std::` 前缀，例如 `std::is_integral::value` 用于检查类型 `T` 是否是整数类型。这里的 `value` 是一个静态常量，其值为 `true` 或 `false`。


以下是一些常用的 **type_traits** 功能：



**基本类型判断**：


- `std::is_void`: 判断类型 `T` 是否为 `void`。
- `std::is_integral`: 判断类型 `T` 是否为整型。
- `std::is_floating_point`: 判断类型 `T` 是否为浮点型。
- `std::is_array`: 判断类型 `T` 是否为数组类型。
- `std::is_pointer`: 判断类型 `T` 是否为指针类型。
- `std::is_reference`: 判断类型 `T` 是否为引用类型。
- `std::is_const`: 判断类型 `T` 是否为 `const` 修饰。



**类型修饰**：


- `std::remove_const`: 移除类型 `T` 的 `const` 修饰。
- `std::remove_volatile`: 移除类型 `T` 的 `volatile` 修饰。
- `std::remove_cv`: 同时移除类型 `T` 的 `const` 和 `volatile` 修饰。
- `std::remove_reference`: 移除类型 `T` 的引用修饰。
- `std::remove_pointer`: 移除类型 `T` 的指针修饰。



**类型转换**：


- `std::add_const`: 为类型 `T` 添加 `const` 修饰。
- `std::add_volatile`: 为类型 `T` 添加 `volatile` 修饰。
- `std::add_cv`: 同时为类型 `T` 添加 `const` 和 `volatile` 修饰。
- `std::add_pointer`: 为类型 `T` 添加指针修饰。
- `std::add_lvalue_reference`: 为类型 `T` 添加左值引用修饰。
- `std::add_rvalue_reference`: 为类型 `T` 添加右值引用修饰。



**类型特性检测**：


- `std::is_same`: 判断类型 `T` 和 `U` 是否相同。
- `std::is_base_of`: 判断类型 `Base` 是否为类型 `Derived` 的基类。
- `std::is_convertible`: 判断类型 `From` 是否能转换为类型 `To`。



**条件类型**：


- `std::conditional`: 如果 `Condition` 为 `true`，则类型为 `T`，否则为 `F`。
- `std::enable_if`: 如果 `Condition` 为 `true`，则类型为 `T`，否则此模板不参与重载决议。



## 实例


以下是一些使用 `` 的实例，以及它们的输出结果。


### 检查是否是整数类型


## 实例


```cpp
#include <iostream>
#include <type_traits>

int main() {
    std::cout << "int is integral: " << std::is_integral<int>::value << std::endl;
    std::cout << "float is integral: " << std::is_integral<float>::value << std::endl;
    std::cout << "char is integral: " << std::is_integral<char>::value << std::endl;
    return 0;
}
```


**输出结果:**


```
int is integral: 1
float is integral: 0
char is integral: 1
```


### 检查是否是浮点类型


## 实例


```cpp
#include <iostream>
#include <type_traits>

int main() {
    std::cout << "int is floating_point: " << std::is_floating_point<int>::value << std::endl;
    std::cout << "float is floating_point: " << std::is_floating_point<float>::value << std::endl;
    std::cout << "double is floating_point: " << std::is_floating_point<double>::value << std::endl;
    return 0;
}
```


输出结果:


```
int is floating_point: 0
float is floating_point: 1
double is floating_point: 1
```


### 检查是否是指针类型


## 实例


```cpp
#include <iostream>
#include <type_traits>

int main() {
    int a = 10;
    int* p = &a;
    std::cout << "int* is a pointer: " << std::is_pointer<int*>::value << std::endl;
    std::cout << "int is a pointer: " << std::is_pointer<int>::value << std::endl;
    return 0;
}
```


输出结果:


```
int* is a pointer: 1
int is a pointer: 0
```


### 检查是否是引用类型


## 实例


```cpp
#include <iostream>
#include <type_traits>

int main() {
    int a = 10;
    int& ref = a;
    std::cout << "int& is a reference: " << std::is_reference<int&>::value << std::endl;
    std::cout << "int is a reference: " << std::is_reference<int>::value << std::endl;
    return 0;
}
```


输出结果:


```
int& is a reference: 1
int is a reference: 0
```


### 检查是否是可调用的


## 实例


```cpp
#include <iostream>
#include <type_traits>
#include <functional>

void func() {}

int main() {
    std::cout << "int is callable: " << std::is_callable<int>::value << std::endl;
    std::cout << "void() is callable: " << std::is_callable<void()>::value << std::endl;
    std::cout << "func is callable: " << std::is_callable<decltype(func)>::value << std::endl;
    return 0;
}
```


输出结果:


```
int is callable: 0
void() is callable: 1
func is callable: 1
```


`` 是 C++ 中一个非常有用的工具，它允许开发者在编译时检查和操作类型属性。这不仅可以提高代码的安全性，还可以使代码更加灵活和可重用。








	  AI 思考中...





			** [C++ 异常处理库 ](https://www.runoob.com/cpp-libs-exception.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-typeinfo.html) **













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