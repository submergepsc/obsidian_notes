# C++ 容器类

- Source: https://www.runoob.com/cplusplus/cpp-libs-map.html

在 C++ 中，`` 是标准模板库（STL）的一部分，它提供了一种关联容器，用于存储键值对（key-value pairs）。

`map` 容器中的元素是按照键的顺序自动排序的，这使得它非常适合需要快速查找和有序数据的场景。


### 定义和特性


- **键值对**：`map` 存储的是键值对，其中每个键都是唯一的。
- **排序**：`map` 中的元素按照键的顺序自动排序，通常是升序。
- **唯一性**：每个键在 `map` 中只能出现一次。
- **双向迭代器**：`map` 提供了双向迭代器，可以向前和向后遍历元素。


### 基本语法


包含头文件:


```
#include <map>
```


声明 map 容器:


```
std::map<key_type, value_type> myMap;
```


- `key_type` 是键的类型。
- `value_type` 是值的类型。


插入元素:


```
myMap[key] = value;
```


访问元素:


```
value = myMap[key];
```


遍历 map:


```
for (std::map<key_type, value_type>::iterator it = myMap.begin(); it != myMap.end(); ++it) {
    std::cout << it->first << " => " << it->second << std::endl;
}
```


C++11 及以上标准，遍历部分可以简化为范围 for 循环，代码更简洁：


```
for (auto &p : m) {
    std::cout << p.first << " : " << p.second << std::endl;
}
```


## 实例


下面是一个使用 `map` 的简单实例，我们将创建一个 `map` 来存储员工的姓名和他们的年龄，并遍历这个 `map` 来打印每个员工的姓名和年龄。


## 实例


```cpp
#include <iostream>#include <map>
#include <string>

int main() {
    // 创建一个 map 容器，存储员工的姓名和年龄
    std::map<std::string, int> employees;

    // 插入员工信息
    employees["Alice"] = 30;
    employees["Bob"] = 25;
    employees["Charlie"] = 35;

    // 遍历 map 并打印员工信息
    for (std::map<std::string, int>::iterator it = employees.begin(); it != employees.end(); ++it) {
        std::cout << it->first << " is " << it->second << " years old." << std::endl;
    }

    return 0;
}
```


输出结果:


```
Alice is 30 years old.
Bob is 25 years old.
Charlie is 35 years old.
```


### 进阶用法


检查键是否存在:


```
if (myMap.find(key) != myMap.end()) {
    // 键存在
}
```


删除元素:


```
myMap.erase(key);
```


清空 map:


```
myMap.clear();
```


获取 map 的大小:


```
size_t size = myMap.size();
```


其他方法：


```
myMap.empty();      // 是否为空
myMap.count("Bob"); // key 是否存在（返回 0 或 1）
```


自定义排序，默认升序排序，可以用 std::greater 或自定义比较函数：


```
std::map<int, std::string, std::greater<int>> m;  // 降序
```


使用自定义比较函数:


## 实例


```cpp
#include <map>
#include <string>
#include <functional>

bool myCompare(const std::string& a, const std::string& b) {
    return a < b;
}

int main() {
    std::map<std::string, int, std::function<bool(const std::string&, const std::string&)>> myMap(myCompare);

    // 其他操作...

    return 0;
}
```


map 是 C++ STL 中一个非常有用的容器，特别适合需要快速查找和有序数据的场景。


## 实例


```cpp
#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, int> scores;

    // 插入
    scores["Alice"] = 90;
    scores["Bob"] = 85;
    scores.insert({"Charlie", 92});

    // 遍历
    for (auto &p : scores) {
        std::cout << p.first << " => " << p.second << std::endl;
    }

    // 查找
    auto it = scores.find("Bob");
    if (it != scores.end()) {
        std::cout << "Bob's score: " << it->second << std::endl;
    }

    // 删除
    scores.erase("Alice");

    std::cout << "Size: " << scores.size() << std::endl;

    return 0;
}
```


运行结果（自动按 key 排序）：


```
Alice => 90
Bob => 85
Charlie => 92
Bob's score: 85
Size: 2
```









	  AI 思考中...





			** [C++ 容器类 ](https://www.runoob.com/cpp-libs-unordered_map.html)
			[C++ 算法库 ](https://www.runoob.com/cpp-libs-algorithm.html) **













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