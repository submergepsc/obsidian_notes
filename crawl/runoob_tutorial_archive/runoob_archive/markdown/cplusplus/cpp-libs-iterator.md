# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-iterator.html

C++ 标准库中的 `` 头文件提供了一组工具，用于遍历容器中的元素。迭代器是 C++ 标准模板库（STL）中的核心概念之一，它允许程序员以统一的方式访问容器中的元素，而不需要关心容器的具体实现细节。


迭代器是一个对象，它提供了一种方法来遍历容器中的元素。迭代器可以被视为指向容器中元素的指针，但它比指针更加灵活和强大。迭代器可以用于访问、修改容器中的元素，并且可以与 STL 算法一起使用。


迭代器主要分为以下几类：


- **输入迭代器（Input Iterator）**：只能进行单次读取操作，不能进行写入操作。
- **输出迭代器（Output Iterator）**：只能进行单次写入操作，不能进行读取操作。
- **正向迭代器（Forward Iterator）**：可以进行读取和写入操作，并且可以向前移动。
- **双向迭代器（Bidirectional Iterator）**：除了可以进行正向迭代器的所有操作外，还可以向后移动。
- **随机访问迭代器（Random Access Iterator）**：除了可以进行双向迭代器的所有操作外，还可以进行随机访问，例如通过下标访问元素。


## 常用函数（重点）


| 函数 | 作用 | 示例 | 说明 |
| --- | --- | --- | --- |
| std::advance(it, n) | 移动迭代器 n 步 | advance(it, 2); | 会修改原迭代器 |
| std::distance(a, b) | 计算两个迭代器距离 | distance(v.begin(), v.end()); | 返回元素个数 |
| std::next(it, n) | 返回向前 n 步的新迭代器 | auto it2 = next(it, 2); | 推荐，不修改原值 |
| std::prev(it, n) | 返回向后 n 步的新迭代器 | auto it2 = prev(it, 1); | C++11 起支持 |


## 迭代器适配器（非常重要）


迭代器适配器可以改变迭代器的行为，使其适配不同的使用场景。


| 适配器 | 作用 | 示例 |
| --- | --- | --- |
| std::back_inserter | 尾部插入（调用 push_back） | back_inserter(vec) |
| std::front_inserter | 头部插入（调用 push_front） | front_inserter(list) |
| std::inserter | 指定位置插入 | inserter(vec, it) |


## 流迭代器（IO 简化神器）


| 类型 | 作用 | 示例 |
| --- | --- | --- |
| std::istream_iterator | 从输入流读取数据 | istream_iterator(cin) |
| std::ostream_iterator | 写入输出流 | ostream_iterator(cout, " ") |


## 迭代器的语法


迭代器的语法通常如下：


```
#include &lt;iterator&gt;

// 使用迭代器遍历容器
for (ContainerType::iterator it = container.begin(); it != container.end(); ++it) {
    // 访问元素 *it
}
```


## 实例


下面是一个使用 `` 头文件和迭代器遍历 `std::vector` 的示例：


## 实例


```cpp
#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

int main() {
    // 创建一个 vector 容器并初始化
    std::vector<int> vec = {1, 2, 3, 4, 5};

    // 使用迭代器遍历 vector
    for (std::vector<int>::iterator it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // 使用 auto 关键字简化迭代器类型
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // 使用 C++11 范围 for 循环
    for (int elem : vec) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // 使用 back_inserter 自动插入
    std::vector<int> v2;
    std::fill_n(std::back_inserter(v2), 3, 100);

    // 使用 ostream_iterator 输出
    std::copy(v2.begin(), v2.end(),
              std::ostream_iterator<int>(std::cout, " "));
    std::cout << std::endl;

    return 0;
}
```


输出结果:


```
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
100 100 100
```


## 总结


**** 的核心作用可以总结为三点：


- 统一访问方式：不同容器使用同一套遍历逻辑
- 解耦容器与算法：算法只依赖迭代器
- 提升代码复用性：同一段代码可适用于多种数据结构


对于初学者来说，建议优先掌握以下内容：


- `next / prev / distance`
- `back_inserter`
- 迭代器遍历方式








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-regex.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-functional.html) **













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