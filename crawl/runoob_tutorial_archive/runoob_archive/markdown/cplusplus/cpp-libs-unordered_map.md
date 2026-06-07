# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-unordered_map.html

在 C++ 中，`` 是标准模板库（STL）的一部分，提供了一种基于哈希表的键值对容器。

与 `std::map` 不同，`unordered_map` 不保证元素的排序，但通常提供更快的查找速度。


`unordered_map` 是一个关联容器，它存储了键值对（key-value pairs），其中每个键（key）都是唯一的。`unordered_map` 使用哈希表来存储元素，这使得它在查找、插入和删除操作中具有平均常数时间复杂度。


### 语法


以下是 `unordered_map` 的基本语法：


```
#include <unordered_map>

std::unordered_map<key_type, value_type> map_name;
```


- `key_type` 是键的类型。
- `value_type` 是值的类型。


### 构造函数


`unordered_map` 可以以多种方式构造：


```
// 默认构造
std::unordered_map<int, std::string> myMap;

// 构造并初始化
std::unordered_map<int, std::string> myMap = {{1, "one"}, {2, "two"}};

// 构造并指定初始容量
std::unordered_map<int, std::string> myMap(10);

// 构造并复制另一个 unordered_map
std::unordered_map<int, std::string> anotherMap = myMap;
```


### 基本操作


插入元素:


```
myMap.insert({3, "three"});
```


访问元素:


```
std::string value = myMap[1]; // 获取键为1的值
```


删除元素:


```
myMap.erase(1); // 删除键为1的元素
```


查找元素:


```
auto it = myMap.find(2); // 查找键为2的元素
if (it != myMap.end()) {
    std::cout << "Found: " << it->second << std::endl;
}
```


## 实例


下面是一个使用 `unordered_map` 的简单实例，包括输出结果。


## 实例


```cpp
#include <iostream>
#include <unordered_map>

int main() {
    // 创建一个 unordered_map，键为 int，值为 string
    std::unordered_map<int, std::string> myMap;

    // 插入一些键值对
    myMap[1] = "one";
    myMap[2] = "two";
    myMap[3] = "three";

    // 打印所有元素
    for (const auto& pair : myMap) {
        std::cout << "Key: " << pair.first << ", Value: " << pair.second << std::endl;
    }

    // 访问特定键的值
    std::cout << "Value for key 2: " << myMap[2] << std::endl;

    // 删除键为1的元素
    myMap.erase(1);

    // 再次打印所有元素
    std::cout << "After erasing key 1:" << std::endl;
    for (const auto& pair : myMap) {
        std::cout << "Key: " << pair.first << ", Value: " << pair.second << std::endl;
    }

    return 0;
}
```


输出结果:


```
Key: 1, Value: one
Key: 2, Value: two
Key: 3, Value: three
Value for key 2: two
After erasing key 1:
Key: 2, Value: two
Key: 3, Value: three
```


### 注意事项


- `unordered_map` 不保证元素的顺序，因此元素的迭代顺序可能在不同的运行中不同。
- 哈希表的性能依赖于良好的哈希函数，以避免过多的哈希冲突。
- 与 `std::map` 相比，`unordered_map` 在元素数量较少时可能占用更多的内存。








	  AI 思考中...





			** [C++ 容器类 ](https://www.runoob.com/cpp-libs-unordered_set.html)
			[C++ 容器类 ](https://www.runoob.com/cpp-libs-map.html) **













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