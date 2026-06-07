# C++ 容器类

- Source: https://www.runoob.com/cplusplus/cpp-libs-unordered_set.html

在C++中，`` 是标准模板库（STL）的一部分，提供了一种基于哈希表的容器，用于存储唯一的元素集合。

与 `set` 不同，`unordered_set` 不保证元素的排序，但通常提供更快的查找、插入和删除操作。


`unordered_set` 是一个模板类，其定义如下：


```
#include <unordered_set>

std::unordered_set<Key, Hash = std::hash<Key>, Pred = std::equal_to<Key>, Alloc = std::allocator<Key>>
```


- `Key` 是存储在 `unordered_set` 中的元素类型。
- `Hash` 是一个函数或函数对象，用于生成元素的哈希值，默认为 `std::hash`。
- `Pred` 是一个二元谓词，用于比较两个元素是否相等，默认为 `std::equal_to`。
- `Alloc` 是分配器类型，用于管理内存分配，默认为 `std::allocator`。


### 语法


以下是一些基本的 `unordered_set` 操作：


- **构造函数**：创建一个空的 `unordered_set`。
```
std::unordered_set<int> uset;
```

- **插入元素**：使用 `insert()` 方法。
```
uset.insert(10);
```

- **查找元素**：使用 `find()` 方法。
```
auto it = uset.find(10);
if (it != uset.end()) {
  // 元素存在
}
```

- **删除元素**：使用 `erase()` 方法。
```
uset.erase(10);
```

- **大小和空检查**：使用 `size()` 和 `empty()` 方法。
```
size_t size = uset.size();
bool isEmpty = uset.empty();
```

- **清空容器**：使用 `clear()` 方法。
```
uset.clear();
```


## 实例


下面是一个使用 `unordered_set` 的简单示例，包括输出结果。


## 实例


```cpp
#include <iostream>
#include <unordered_set>

int main() {
    // 创建一个整数类型的 unordered_set
    std::unordered_set<int> uset;

    // 插入元素
    uset.insert(10);
    uset.insert(20);
    uset.insert(30);

    // 打印 unordered_set 中的元素
    std::cout << "Elements in uset: ";
    for (int elem : uset) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // 查找元素
    auto it = uset.find(20);
    if (it != uset.end()) {
        std::cout << "Element 20 found in uset." << std::endl;
    } else {
        std::cout << "Element 20 not found in uset." << std::endl;
    }

    // 删除元素
    uset.erase(20);
    std::cout << "After erasing 20, elements in uset: ";
    for (int elem : uset) {
        std::cout << elem << " ";
    }
    std::cout << std::endl;

    // 检查大小和是否为空
    std::cout << "Size of uset: " << uset.size() << std::endl;
    std::cout << "Is uset empty? " << (uset.empty() ? "Yes" : "No") << std::endl;

    // 清空 unordered_set
    uset.clear();
    std::cout << "After clearing, is uset empty? " << (uset.empty() ? "Yes" : "No") << std::endl;

    return 0;
}
```


输出结果:


```
Elements in uset: 10 20 30
Element 20 found in uset.
After erasing 20, elements in uset: 10 30
Size of uset: 2
Is uset empty? No
After clearing, is uset empty? Yes
```


`unordered_set` 是一个非常有用的容器，特别适合于需要快速查找、插入和删除操作的场景，同时不需要元素的有序性。








	  AI 思考中...





			** [C++ 容器类 **](https://www.runoob.com/cpp-libs-bitset.html)
			[C++ 容器类 ](https://www.runoob.com/cpp-libs-unordered_map.html) **













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