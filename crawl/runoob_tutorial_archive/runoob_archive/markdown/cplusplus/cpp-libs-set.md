# C++ 容器类

- Source: https://www.runoob.com/cplusplus/cpp-libs-set.html

C++ 标准库中的 `` 是一个关联容器，它存储了一组唯一的元素，并按照一定的顺序进行排序。

`` 提供了高效的元素查找、插入和删除操作。它是基于红黑树实现的，因此具有对数时间复杂度的查找、插入和删除性能。


`` 容器中存储的元素类型必须满足以下条件：


- 元素类型必须可以比较大小。
- 元素类型必须可以被复制和赋值。


### 语法


包含头文件:


```
#include <set>
```


声明 set 容器


```
std::set<元素类型> 容器名;
```


### 常用操作


- `insert(元素)`: 插入一个元素。
- `erase(元素)`: 删除一个元素。
- `find(元素)`: 查找一个元素。
- `size()`: 返回容器中元素的数量。
- `empty()`: 检查容器是否为空。


## 实例


下面是一个使用 `` 的简单示例，包括元素的插入、查找、删除和输出结果。


## 实例


```cpp
#include <iostream>
#include <set>

int main() {
    // 声明一个整型 set 容器
    std::set<int> mySet;

    // 插入元素
    mySet.insert(10);
    mySet.insert(20);
    mySet.insert(30);
    mySet.insert(40);

    // 输出 set 中的元素
    std::cout << "Set contains: ";
    for (int num : mySet) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // 查找元素
    if (mySet.find(20) != mySet.end()) {
        std::cout << "20 is in the set." << std::endl;
    } else {
        std::cout << "20 is not in the set." << std::endl;
    }

    // 删除元素
    mySet.erase(20);

    // 再次输出 set 中的元素
    std::cout << "After erasing 20, set contains: ";
    for (int num : mySet) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // 检查 set 是否为空
    if (mySet.empty()) {
        std::cout << "The set is empty." << std::endl;
    } else {
        std::cout << "The set is not empty." << std::endl;
    }

    // 输出 set 中元素的数量
    std::cout << "The set contains " << mySet.size() << " elements." << std::endl;

    return 0;
}
```


输出结果:


```
Set contains: 10 20 30 40
20 is in the set.
After erasing 20, set contains: 10 30 40
The set is not empty.
The set contains 3 elements.
```


## 总结


`` 是 C++ 标准库中一个非常有用的容器，特别适合需要快速查找、插入和删除操作的场景。通过上述示例，初学者可以对 `` 的基本用法有一个清晰的了解。在实际开发中，合理利用 `` 可以提高程序的效率和可读性。








	  AI 思考中...





			** [C++ 容器类 ](https://www.runoob.com/cpp-libs-stack.html)
			[C++ 容器类 **](https://www.runoob.com/cpp-libs-bitset.html) **













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