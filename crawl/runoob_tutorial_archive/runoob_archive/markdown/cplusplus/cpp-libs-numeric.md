# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-numeric.html

在日常 C++ 开发中，我们经常会遇到如下需求：


- 求数组总和 / 连乘
- 计算前缀和用于区间查询
- 批量累积生成新序列
- 做向量之间的内积（点积）


如果你还在手写 `for` 循环，那么 `` 正是你应该掌握的标准库工具。


C++ 标准库中的 `` 头文件提供了一组用于数值计算的函数模板，这些函数可以对容器中的元素进行各种数值操作，如求和、乘积、最小值、最大值等。这些函数模板非常强大，可以应用于任何类型的容器，包括数组、向量、列表等。


在使用 `` 头文件中的函数之前，需要在你的 C++ 程序中包含这个头文件：


```
#include <numeric>
```


## 常用函数


- `` 是 C++ 处理**数值序列计算**的核心头文件，专注于归约、累积、差分等操作，兼容所有STL容器；
- 基础函数（`accumulate`/`partial_sum`/`iota`）是C++98/11的核心，满足绝大多数常规数值计算需求；
- C++17 新增的 `reduce`/`inclusive_scan` 等并行函数，可显著提升大数据量下的计算效率，需配合并行执行策略使用。


| 函数名 | C++ 版本 | 核心功能 | 简化函数原型（以 vector 为例） | 典型适用场景 |
| --- | --- | --- | --- | --- |
| accumulate | C++98 | 计算序列的累加和（可自定义二元操作） | int accumulate(iterator beg, iterator end, int init); | 求数组总和、统计累计值 |
| inner_product | C++98 | 计算两个序列的内积（对应元素相乘后累加，可自定义操作） | int inner_product(iter1 b1, iter1 e1, iter2 b2, int init); | 向量点积、加权求和 |
| partial_sum | C++98 | 计算序列的前缀和（第n个结果=前n个元素的和，可自定义操作） | void partial_sum(iter b, iter e, iter res); | 生成前缀和数组、累积统计 |
| adjacent_difference | C++98 | 计算序列相邻元素的差值（第n个结果=elem[n]-elem[n-1]，可自定义操作） | void adjacent_difference(iter b, iter e, iter res); | 计算差分、检测序列变化量 |
| iota | C++11 | 用连续递增的值填充序列（从 init 开始，逐个+1） | void iota(iter b, iter e, T init); | 生成连续整数序列、初始化有序容器 |
| reduce | C++17 | 并行版累加（类似 accumulate，支持并行执行，无序归约） | T reduce(iter b, iter e, T init = T{}); | 大数据量并行求和、提升计算效率 |
| transform_reduce | C++17 | 变换+归约（先对元素做变换，再累加，支持并行） | T transform_reduce(iter1 b1, iter1 e1, iter2 b2, T init); | 并行计算内积、变换后求和 |
| inclusive_scan | C++17 | 并行版前缀和（包含当前元素，类似 partial_sum，支持并行） | void inclusive_scan(iter b, iter e, iter res); | 并行生成前缀和数组 |
| exclusive_scan | C++17 | 并行版前缀和（不包含当前元素，第n个结果=前n-1个元素的和） | void exclusive_scan(iter b, iter e, iter res, T init); | 并行生成"不包含自身"的前缀和 |


### 1. accumulate


`accumulate` 函数用于计算容器中所有元素的总和。它接受三个参数：容器的开始迭代器、结束迭代器和初始值。


**语法**:


```
template <InputIterator Iter, class T>
T accumulate(Iter first, Iter last, T init);
```


**实例**:


## 实例


```cpp
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4, 5};
    int sum = std::accumulate(v.begin(), v.end(), 0);
    std::cout << "Sum: " << sum << std::endl; // 输出: Sum: 15
    return 0;
}
```


### 2. inner_product


`inner_product` 函数用于计算两个容器中对应元素乘积的总和。


**语法**:


```
template <InputIterator1 Iter1, InputIterator2 Iter2, class T>
T inner_product(Iter1 first1, Iter1 last1, Iter2 first2, T init);
```


**实例**:


## 实例


```cpp
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> v1 = {1, 2, 3};
    std::vector<int> v2 = {4, 5, 6};
    int product_sum = std::inner_product(v1.begin(), v1.end(), v2.begin(), 0);
    std::cout << "Product Sum: " << product_sum << std::endl; // 输出: Product Sum: 32
    return 0;
}
```


### 3. partial_sum


`partial_sum` 函数用于计算容器中元素的部分和，并将结果存储在另一个容器中。


**语法**:


```
template <InputIterator InIter, OutputIterator OutIter>
OutIter partial_sum(InIter first, InIter last, OutIter result);
```


**实例**:


## 实例


```cpp
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4};
    std::vector<int> result(v.size());
    std::partial_sum(v.begin(), v.end(), result.begin());
    for (int i : result) {
        std::cout << i << " "; // 输出: 1 3 6 10
    }
    return 0;
}
```


### 4. adjacent_difference


`adjacent_difference` 函数用于计算容器中相邻元素的差值，并将结果存储在另一个容器中。


**语法**:


```
template <InputIterator InIter, OutputIterator OutIter>
OutIter adjacent_difference(InIter first, InIter last, OutIter result);
```


**实例**:


## 实例


```cpp
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> v = {1, 2, 3, 4};
    std::vector<int> result(v.size() - 1);
    std::adjacent_difference(v.begin(), v.end(), result.begin());
    for (int i : result) {
        std::cout << i << " "; // 输出: 1 1 1
    }
    return 0;
}
```


### 5. std::gcd


使用 std::gcd 计算两个整数的最大公约数：


## 实例


```cpp
#include <iostream>
#include <numeric>

int main() {
    int a = 48;
    int b = 18;
    int result = std::gcd(a, b);  // 计算 48 和 18 的最大公约数
    std::cout << "GCD: " << result << std::endl;  // 输出 6
    return 0;
}
```


### 6. std::lcm


使用 std::lcm 计算两个整数的最小公倍数：


## 实例


```cpp
#include <iostream>
#include <numeric>

int main() {
    int a = 48;
    int b = 18;
    int result = std::lcm(a, b);  // 计算 48 和 18 的最小公倍数
    std::cout << "LCM: " << result << std::endl;  // 输出 144
    return 0;
}
```


### 7. std::iota


## 实例


```cpp
#include <iostream>
#include <numeric>  // 包含 numeric 头文件
#include <vector>

int main() {
    std::vector<int> v(5); // 创建一个包含5个元素的向量

    // 使用 std::iota 填充向量，起始值为1
    std::iota(std::begin(v), std::end(v), 1);

    // 输出填充后的向量
    for (int i : v) {
        std::cout << i << " ";
    }
    std::cout << std::endl; // 输出: 1 2 3 4 5

    return 0;
}
```


使用 std::iota 填充范围内的序列值。


```
template<class ForwardIt, class T>
void iota(ForwardIt first, ForwardIt last, T value);
```


### 8.查找最大值与最小值


`min_element` 和 `max_element` 函数用于找到容器中的最大值和最小值。


## 实例


```cpp
#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm> // 为了使用 std::min_element 和 std::max_element

int main() {
    // 定义一个包含整数的向量
    std::vector<int> v = {3, 1, 4, 1, 5, 9};

    // 计算最小值和最大值
    int min_val = *std::min_element(v.begin(), v.end());
    int max_val = *std::max_element(v.begin(), v.end());

    // 计算总和
    int sum_val = std::accumulate(v.begin(), v.end(), 0);

    // 计算平均值
    double avg_val = static_cast<double>(sum_val) / v.size();

    // 输出结果
    std::cout << "Min: " << min_val << std::endl;
    std::cout << "Max: " << max_val << std::endl;
    std::cout << "Sum: " << sum_val << std::endl;
    std::cout << "Average: " << avg_val << std::endl;

    return 0;
}
```


输出结果为：


```
Min: 1
Max: 9
Sum: 23
Average: 3.83333
```









	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-functional.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-complex.html) **













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