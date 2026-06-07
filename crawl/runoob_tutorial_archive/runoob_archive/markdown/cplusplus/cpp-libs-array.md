# C++ 容器类

- Source: https://www.runoob.com/cplusplus/cpp-libs-array.html

C++11 标准引入了 `` 头文件，它提供了一种固定大小的数组容器，与 C 语言中的数组相比，具有更好的类型安全和内存管理特性。


`std::array` 是 C++ 标准库中的一个模板类，它定义在 `` 头文件中。`std::array` 模板类提供了一个固定大小的数组，其大小在编译时确定，并且不允许动态改变。


### 语法


`std::array` 的基本语法如下：


```
#include <array>

std::array<T, N> array_name;
```


- `T` 是数组中元素的类型。
- `N` 是数组的大小，必须是一个非负整数。


### 声明与初始化


`` 需要在编译时确定大小，不能动态改变。使用示例：


```
#include <iostream>
#include <array>

int main() {
    std::array<int, 5> arr = {1, 2, 3, 4, 5}; // 声明一个定长为5的int数组
    return 0;
}
```


## 特点


- **类型安全**：`std::array` 强制类型检查，避免了 C 语言数组的类型不安全问题。
- **固定大小**：数组的大小在编译时确定，不能在运行时改变。
- **内存连续**：`std::array` 的元素在内存中是连续存储的，这使得它可以高效地访问元素。
- **标准容器**：`std::array` 提供了与 `std::vector` 类似的接口，如 `size()`, `at()`, `front()`, `back()` 等。


## 实例


下面是一个使用 `std::array` 的简单示例，包括输出结果。


## 实例


```cpp
#include <iostream>
#include <array>

int main() {
    // 创建一个包含 5 个整数的 std::array
    std::array<int, 5> myArray = {1, 2, 3, 4, 5};

    // 使用范围 for 循环遍历数组
    for (const auto& value : myArray) {
        std::cout << value << " ";
    }
    std::cout << std::endl;

    // 使用索引访问数组元素
    std::cout << "Element at index 2: " << myArray.at(2) << std::endl;

    // 获取数组的大小
    std::cout << "Array size: " << myArray.size() << std::endl;

    // 修改数组元素
    myArray[3] = 10;

    // 再次遍历数组以显示修改后的元素
    for (const auto& value : myArray) {
        std::cout << value << " ";
    }
    std::cout << std::endl;

    return 0;
}
```


输出结果:


```
1 2 3 4 5
Element at index 2: 3
Array size: 5
1 2 3 10 5
```


---


## 常用成员函数

以下是 `` 中的一些常用成员函数：


| 函数 | 说明 |
| --- | --- |
| at(size_t pos) | 返回指定位置的元素，带边界检查 |
| operator[] | 返回指定位置的元素，不带边界检查 |
| front() | 返回数组的第一个元素 |
| back() | 返回数组的最后一个元素 |
| data() | 返回指向数组数据的指针 |
| size() | 返回数组大小（固定不变） |
| fill(const T& value) | 将数组所有元素设置为指定值 |
| swap(array& other) | 交换两个数组的内容 |
| begin() / end() | 返回数组的起始/结束迭代器 |

### 实例


**1、基本操作**


## 实例


```cpp
#include <iostream>
#include <array>

int main() {
    std::array<int, 5> arr = {10, 20, 30, 40, 50};

    std::cout << "Array elements: ";
    for (int i = 0; i < arr.size(); ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    // 获取第一个和最后一个元素
    std::cout << "First element: " << arr.front() << std::endl;
    std::cout << "Last element: " << arr.back() << std::endl;

    return 0;
}
```


**使用 at 和边界检查**


## 实例


```cpp
#include <iostream>
#include <array>

int main() {
    std::array<int, 3> arr = {1, 2, 3};

    try {
        std::cout << arr.at(2) << std::endl;  // 正常输出
        std::cout << arr.at(5) << std::endl;  // 超出范围，抛出异常
    } catch (const std::out_of_range& e) {
        std::cout << "Exception: " << e.what() << std::endl;
    }

    return 0;
}
```


**3、使用 fill 填充元素**


## 实例


```cpp
#include <iostream>
#include <array>

int main() {
    std::array<int, 5> arr;
    arr.fill(100);  // 将所有元素设置为100

    std::cout << "Filled array: ";
    for (const auto& elem : arr) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    return 0;
}
```


**4、数组交换**


## 实例


```cpp
#include <iostream>
#include <array>

int main() {
    std::array<int, 3> arr1 = {1, 2, 3};
    std::array<int, 3> arr2 = {4, 5, 6};

    arr1.swap(arr2);

    std::cout << "Array 1: ";
    for (const auto& elem : arr1) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    std::cout << "Array 2: ";
    for (const auto& elem : arr2) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    return 0;
}
```


---

## 与其他数组类型对比


| 特性 | std::array | C 风格数组 | std::vector |
| --- | --- | --- | --- |
| 大小 | 编译时固定 | 编译时固定 | 动态可变 |
| 边界检查 | at() 提供边界检查 | 无 | at() 提供边界检查 |
| 内存管理 | 栈上分配 | 栈上分配 | 堆上分配 |
| 性能 | 高效 | 高效 | 较低（动态分配） |
| 接口 | 支持 STL 标准接口 | 不支持 STL 标准接口 | 支持 STL 标准接口 |


`std::array` 是 C++ 标准库中一个非常有用的容器，它提供了固定大小的数组，具有类型安全和内存管理的优势。通过上述示例，我们可以看到如何创建、访问和修改 `std::array` 的元素。对于需要固定大小数组的场景，`std::array` 是一个非常好的选择。








	  AI 思考中...





			** [C++ 标准库 *](https://www.runoob.com/cpp-libs-iomanip.html)
			[C++ 容器 ](https://www.runoob.com/cpp-libs-forward_list.html) *













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