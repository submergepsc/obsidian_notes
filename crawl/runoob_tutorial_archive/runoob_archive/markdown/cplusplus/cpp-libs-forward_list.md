# C++ 容器

- Source: https://www.runoob.com/cplusplus/cpp-libs-forward_list.html

C++ 标准库中的 `` 是一种容器，它提供了一种单向链表的数据结构。


与双向链表（`std::list`）不同，`std::forward_list` 只支持单向遍历。它适用于需要频繁进行前向遍历和插入、删除操作的场景。以下是对 `std::forward_list` 的详细说明：



**单向链表**：


- `std::forward_list` 是单向链表，只能从前往后遍历，不能反向遍历。
- 由于其单向链表的结构，插入和删除操作在已知位置的情况下非常高效（O(1) 复杂度）。



**低内存开销**：


- 与 `std::list` 相比，`std::forward_list` 只需要一个指向下一个节点的指针，节省了内存。



**不支持随机访问**：


- 不支持通过索引访问元素，不能使用 `operator[]` 或 `at` 方法，只能通过迭代器进行访问。


### 语法


`std::forward_list` 是 C++ 标准库中的一个模板类，定义在 `` 头文件中。它使用模板参数 `T` 来指定存储在列表中的元素类型。


以下是 `std::forward_list` 的基本语法：


```
#include <forward_list>

std::forward_list<T> list;
```


### 构造函数


`std::forward_list` 提供了多种构造函数，包括：


- 默认构造函数：创建一个空的 `forward_list`。
- 带初始值的构造函数：创建一个包含给定初始值的 `forward_list`。
- 带范围的构造函数：创建一个包含指定范围内元素的 `forward_list`。


### 常用成员函数


- `void push_front(const T& value)`：在列表的前端插入一个元素。
- `void pop_front()`：移除列表前端的元素。
- `iterator before_begin()`：返回指向列表前端之前的迭代器。
- `iterator begin()`：返回指向列表前端的迭代器。
- `iterator end()`：返回指向列表末尾的迭代器。


## 实例


下面是一个使用 `std::forward_list` 的简单示例，包括创建列表、添加元素、遍历列表和输出结果。


## 实例


```cpp
#include <iostream>
#include <forward_list>

int main() {
    // 创建一个空的 forward_list
    std::forward_list<int> fl;

    // 在列表前端添加元素
    fl.push_front(10);
    fl.push_front(20);
    fl.push_front(30);

    // 遍历 forward_list 并输出元素
    for (auto it = fl.begin(); it != fl.end(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;

    // 输出结果：30 20 10

    return 0;
}
```


当你运行上述代码时，你将看到以下输出：


```
30 20 10
```


`std::forward_list` 是 C++ 标准库中一个非常有用的容器，特别适合于需要在列表前端进行频繁插入和删除操作的场景。虽然它不支持随机访问，但在某些情况下，它的性能优势可以弥补这一不足。希望这篇文章能帮助初学者更好地理解和使用 `std::forward_list`。








	  AI 思考中...





			** [C++ 容器类 ](https://www.runoob.com/cpp-libs-array.html)
			[C++ 容器类 ](https://www.runoob.com/cpp-libs-vector.html) **













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