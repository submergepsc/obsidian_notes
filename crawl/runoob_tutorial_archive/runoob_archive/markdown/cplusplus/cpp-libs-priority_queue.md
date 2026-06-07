# C++ 容器类

- Source: https://www.runoob.com/cplusplus/cpp-libs-priority_queue.html

在 C++ 中，`` 是标准模板库（STL）的一部分，用于实现优先队列。

优先队列是一种特殊的队列，它允许我们快速访问队列中具有最高（或最低）优先级的元素。

在 C++ 中，`priority_queue` 默认是一个最大堆，这意味着队列的顶部元素总是具有最大的值。


`priority_queue` 是一个容器适配器，它提供了对底层容器的堆操作。它不提供迭代器，也不支持随机访问。


### 语法


以下是 `priority_queue` 的基本语法：


```
#include <queue>

// 声明一个整型优先队列
priority_queue<int> pq;

// 声明一个自定义类型的优先队列，需要提供比较函数
struct compare {
    bool operator()(int a, int b) {
        return a > b; // 这里定义了最小堆
    }
};
priority_queue<int, vector<int>, compare> pq_min;
```


### 常用操作


- `empty()`: 检查队列是否为空。
- `size()`: 返回队列中的元素数量。
- `top()`: 返回队列顶部的元素（不删除它）。
- `push()`: 向队列添加一个元素。
- `pop()`: 移除队列顶部的元素。


## 实例


下面是一个使用 `priority_queue` 的简单实例，我们将创建一个最大堆，并展示如何添加元素和获取队列顶部的元素。


## 实例


```cpp
#include <iostream>
#include <queue>

int main() {
    // 创建一个整型优先队列
    std::priority_queue<int> pq;

    // 向优先队列中添加元素
    pq.push(30);
    pq.push(10);
    pq.push(50);
    pq.push(20);

    // 输出队列中的元素
    std::cout << "队列中的元素：" << std::endl;
    while (!pq.empty()) {
        std::cout << pq.top() << std::endl;
        pq.pop();
    }

    return 0;
}
```


输出结果：


```
队列中的元素：
50
30
20
10
```


## 自定义优先级


如果你需要一个最小堆，可以通过自定义比较函数来实现：


## 实例


```cpp
#include <iostream>
#include <queue>
#include <vector>

struct compare {
    bool operator()(int a, int b) {
        return a > b; // 定义最小堆
    }
};

int main() {
    // 创建一个自定义类型的优先队列，使用最小堆
    std::priority_queue<int, std::vector<int>, compare> pq_min;

    // 向优先队列中添加元素
    pq_min.push(30);
    pq_min.push(10);
    pq_min.push(50);
    pq_min.push(20);

    // 输出队列中的元素
    std::cout << "最小堆中的元素：" << std::endl;
    while (!pq_min.empty()) {
        std::cout << pq_min.top() << std::endl;
        pq_min.pop();
    }

    return 0;
}
```


输出结果：


```
最小堆中的元素：
10
20
30
50
```


`` 是C++ STL中一个非常有用的容器，特别适合需要快速访问最高或最低优先级元素的场景。通过自定义比较函数，我们可以轻松地实现最大堆或最小堆。希望这篇文章能帮助初学者更好地理解和使用 `priority_queue`。








	  AI 思考中...





			** [C++ 容器类 ](https://www.runoob.com/cpp-libs-queue.html)
			[C++ 容器类 ](https://www.runoob.com/cpp-libs-stack.html) **













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