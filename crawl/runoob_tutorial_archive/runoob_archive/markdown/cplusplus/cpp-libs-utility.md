# C++ 标准库 utility

- Source: https://www.runoob.com/cplusplus/cpp-libs-utility.html

在 C++ 标准库中，`` 头文件包含了一些实用的工具类和函数，这些工具类和函数在编写高效、可读性强的代码时非常有用。


`utility` 库的核心价值在于：


- 提供基础的数据结构和工具函数
- 简化常见编程任务的实现
- 为其他标准库组件提供基础支持


`utility` 头文件虽然小巧，但提供的工具非常实用：


| 组件/函数 | 用途 | 使用场景 |
| --- | --- | --- |
| std::pair | 存储两个相关值 | 函数返回多个值、map 元素 |
| std::make_pair | 便捷创建 pair | 模板类型推导、简化代码 |
| std::swap | 交换两个值 | 算法实现、排序操作 |
| std::move | 启用移动语义 | 资源管理、性能优化 |
| std::forward | 完美转发 | 通用引用、模板编程 |


---


## 核心组件详解


### std::pair：键值对容器


`std::pair` 是 `utility` 库中最常用的组件，用于将两个值组合成一个单一对象。


#### 基本语法


```
#include <utility>

// 创建 pair 对象的基本方式
std::pair<类型1, 类型2> 变量名(值1, 值2);
```


## 实例


```cpp
#include <iostream>
#include <utility>
#include <string>

int main() {
    // 方式1：直接初始化
    std::pair<int, std::string> student1(101, "Alice");

    // 方式2：使用 make_pair 函数（推荐）
    auto student2 = std::make_pair(102, "Bob");

    // 方式3：C++17 起支持的推导指引
    std::pair student3(103, "Charlie");

    // 访问 pair 的成员
    std::cout << "学号: " << student1.first << ", 姓名: " << student1.second << std::endl;

    return 0;
}
```


#### pair 的常用操作


## 实例


```cpp
#include <utility>
#include <iostream>

void pairOperations() {
    // 创建 pair
    std::pair<int, double> p1(10, 3.14);
    std::pair<int, double> p2(20, 2.71);

    // 比较操作
    if (p1 < p2) {
        std::cout << "p1 小于 p2" << std::endl;
    }

    // 赋值操作
    p1 = p2;

    // C++11 起支持的逐成员赋值
    int a;
    double b;
    std::tie(a, b) = p1;  // 将 p1 的值分别赋给 a 和 b

    // C++17 结构化绑定（更简洁）
    auto [x, y] = p1;
    std::cout << "x = " << x << ", y = " << y << std::endl;
}
```


### std::make_pair：便捷创建函数


`std::make_pair` 是一个模板函数，可以自动推导类型，简化 pair 的创建过程。


## 实例


```cpp
#include <utility>
#include <iostream>
#include <string>

void demonstrateMakePair() {
    // 自动类型推导，无需显式指定模板参数
    auto p1 = std::make_pair(42, "Hello");
    auto p2 = std::make_pair(3.14, true);

    // 在容器中使用特别方便
    std::vector<std::pair<int, std::string>> students;
    students.push_back(std::make_pair(101, "Alice"));
    students.push_back(std::make_pair(102, "Bob"));

    for (const auto& student : students) {
        std::cout << "学号: " << student.first
                  << ", 姓名: " << student.second << std::endl;
    }
}
```


---


## 实用工具函数


### std::swap：交换两个值


`std::swap` 用于交换两个同类型对象的值。


## 实例


```cpp
#include <utility>
#include <iostream>

void demonstrateSwap() {
    int a = 10, b = 20;
    std::cout << "交换前: a = " << a << ", b = " << b << std::endl;

    std::swap(a, b);
    std::cout << "交换后: a = " << a << ", b = " << b << std::endl;

    // 也可以用于自定义类型（如果实现了移动语义）
    std::string str1 = "Hello", str2 = "World";
    std::swap(str1, str2);
    std::cout << "字符串交换: " << str1 << " " << str2 << std::endl;
}
```


### std::move：移动语义支持


`std::move` 用于将对象转换为右值引用，启用移动语义。


## 实例


```cpp
#include <utility>
#include <iostream>
#include <vector>

void demonstrateMove() {
    std::vector<int> v1 = {1, 2, 3, 4, 5};
    std::vector<int> v2;

    std::cout << "移动前 - v1大小: " << v1.size()
              << ", v2大小: " << v2.size() << std::endl;

    // 使用移动语义转移资源所有权
    v2 = std::move(v1);

    std::cout << "移动后 - v1大小: " << v1.size()
              << ", v2大小: " << v2.size() << std::endl;

    // v1 现在处于有效但未定义的状态
    // 通常不应该再使用 v1，除非重新赋值
}
```


### std::forward：完美转发


`std::forward` 用于实现完美转发，保持参数的值类别。


## 实例


```cpp
#include <utility>
#include <iostream>

// 普通函数 - 不能保持值类别
template<typename T>
void normalFunction(T arg) {
    std::cout << "普通函数参数" << std::endl;
}

// 使用完美转发的函数
template<typename T>
void perfectForwardingFunction(T&& arg) {
    // 保持参数原有的值类别（左值或右值）
    normalFunction(std::forward<T>(arg));
}

void demonstrateForward() {
    int x = 10;

    // 传递左值
    perfectForwardingFunction(x);

    // 传递右值
    perfectForwardingFunction(20);
}
```


---


## 整数序列工具（C++14）


C++14 引入了整数序列相关工具，主要用于模板元编程。


### std::integer_sequence


## 实例


```cpp
#include <utility>
#include <iostream>

// 使用整数序列打印序列中的每个值
template<typename T, T... Ints>
void print_sequence(std::integer_sequence<T, Ints...>) {
    // 使用折叠表达式（C++17）打印所有值
    ((std::cout << Ints << " "), ...);
    std::cout << std::endl;
}

void demonstrateIntegerSequence() {
    // 创建整数序列
    auto seq = std::integer_sequence<int, 1, 2, 3, 4, 5>();
    print_sequence(seq);

    // 使用 make_integer_sequence 生成序列
    auto seq2 = std::make_integer_sequence<int, 5>();
    print_sequence(seq2);  // 输出: 0 1 2 3 4
}
```


---


## 实际应用案例


### 案例 1：函数返回多个值


## 实例


```cpp
#include <utility>
#include <iostream>
#include <cmath>

// 函数返回多个值：计算结果和错误码
std::pair<double, bool> calculateSqrt(double number) {
    if (number < 0) {
        return std::make_pair(0.0, false);  // 错误情况
    }
    return std::make_pair(std::sqrt(number), true);  // 成功情况
}

void multipleReturnValues() {
    auto result1 = calculateSqrt(16.0);
    if (result1.second) {
        std::cout << "平方根: " << result1.first << std::endl;
    } else {
        std::cout << "计算错误: 负数不能求平方根" << std::endl;
    }

    auto result2 = calculateSqrt(-4.0);
    if (!result2.second) {
        std::cout << "计算错误: 负数不能求平方根" << std::endl;
    }
}
```


### 案例 2：在 STL 容器中的应用


## 实例


```cpp
#include <utility>
#include <map>
#include <iostream>
#include <string>

void mapWithPair() {
    // std::map 的每个元素都是 std::pair
    std::map<int, std::string> studentMap;

    // 插入键值对
    studentMap.insert(std::make_pair(101, "Alice"));
    studentMap.emplace(102, "Bob");  // 更高效的方式

    // 遍历 map
    for (const auto& [id, name] : studentMap) {
        std::cout << "学号: " << id << ", 姓名: " << name << std::endl;
    }

    // 查找元素
    auto it = studentMap.find(101);
    if (it != studentMap.end()) {
        std::cout << "找到学生: " << it->second << std::endl;
    }
}
```


### 案例 3：实现简单的字典


## 实例


```cpp
#include <utility>
#include <vector>
#include <iostream>
#include <algorithm>

class SimpleDictionary {
private:
    std::vector<std::pair<std::string, std::string>> entries;

public:
    void addWord(const std::string& word, const std::string& meaning) {
        entries.emplace_back(word, meaning);
    }

    std::pair<bool, std::string> findMeaning(const std::string& word) {
        for (const auto& [w, m] : entries) {
            if (w == word) {
                return std::make_pair(true, m);
            }
        }
        return std::make_pair(false, "");
    }

    void printAll() {
        for (const auto& [word, meaning] : entries) {
            std::cout << word << ": " << meaning << std::endl;
        }
    }
};

void dictionaryExample() {
    SimpleDictionary dict;
    dict.addWord("apple", "一种水果");
    dict.addWord("book", "用于阅读的物体");

    auto result = dict.findMeaning("apple");
    if (result.first) {
        std::cout << "含义: " << result.second << std::endl;
    }
}
```


---


## 最佳实践和注意事项


### 1. 使用 auto 简化 pair 创建


## 实例


```cpp
// 推荐：使用 auto 和 make_pair
auto student = std::make_pair(101, "Alice");

// 不推荐：显式指定类型（更冗长）
std::pair<int, std::string> student(101, "Alice");
```


### 2. 优先使用 emplace 而非 insert


## 实例


```cpp
std::map<int, std::string> myMap;

// 推荐：使用 emplace（更高效）
myMap.emplace(1, "one");

// 不推荐：使用 insert（需要构造临时对象）
myMap.insert(std::make_pair(1, "one"));
```


### 3. 正确使用移动语义


## 实例


```cpp
std::string createString() {
    std::string str = "很大的字符串";
    // 正确：返回时使用移动
    return str;  // 编译器会自动优化，无需显式 move
}

void processString(std::string str) {
    // 处理字符串
}

void usageExample() {
    std::string largeStr = "很大的数据";

    // 正确：传递时使用移动
    processString(std::move(largeStr));
    // 注意：largeStr 现在不应再使用
}
```


### 4. 结构化绑定的使用


## 实例


```cpp
// C++17 起支持的结构化绑定
std::pair<int, std::string> getStudent() {
    return {101, "Alice"};
}

void structuredBindingExample() {
    // 传统方式
    auto student = getStudent();
    int id = student.first;
    std::string name = student.second;

    // 现代方式（C++17）
    auto [id2, name2] = getStudent();  // 更简洁清晰
}
```










	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-cmath.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-random.html) **













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