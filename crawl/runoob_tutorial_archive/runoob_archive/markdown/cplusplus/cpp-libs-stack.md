# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-stack.html

在 C++ 中，标准库提供了多种容器和算法来帮助开发者更高效地编写程序。

`` 是 C++ 标准模板库（STL）的一部分，它实现了一个后进先出（LIFO，Last In First Out）的数据结构。这种数据结构非常适合于需要"最后添加的元素最先被移除"的场景。


`` 容器适配器提供了一个栈的接口，它基于其他容器（如 `deque` 或 `vector`）来实现。栈的元素是线性排列的，但只允许在一端（栈顶）进行添加和移除操作。


### 基本操作


- `push()`: 在栈顶添加一个元素。
- `pop()`: 移除栈顶元素。
- `top()`: 返回栈顶元素的引用，但不移除它。
- `empty()`: 检查栈是否为空。
- `size()`: 返回栈中元素的数量。


### 语法


以下是使用 `` 的基本语法：


```
#include <iostream>
#include <stack>

int main() {
    std::stack<int> s;

    // 向栈中添加元素
    s.push(1);
    s.push(2);
    s.push(3);

    // 访问栈顶元素
    std::cout << "Top element is: " << s.top() << std::endl;

    // 移除栈顶元素
    s.pop();
    std::cout << "After popping, top element is: " << s.top() << std::endl;

    // 检查栈是否为空
    if (!s.empty()) {
        std::cout << "Stack is not empty." << std::endl;
    }

    // 打印栈的大小
    std::cout << "Size of stack: " << s.size() << std::endl;

    return 0;
}
```


## 实例


下面是一个使用 `` 的完整示例，包括输出结果：


## 实例


```cpp
#include <iostream>
#include <stack>

int main() {
    std::stack<int> s;

    // 向栈中添加元素
    s.push(10);
    s.push(20);
    s.push(30);

    // 打印栈顶元素
    std::cout << "Top element is: " << s.top() << std::endl; // 输出: Top element is: 30

    // 移除栈顶元素
    s.pop();
    std::cout << "After popping, top element is: " << s.top() << std::endl; // 输出: After popping, top element is: 20

    // 检查栈是否为空
    if (!s.empty()) {
        std::cout << "Stack is not empty." << std::endl; // 输出: Stack is not empty.
    }

    // 打印栈的大小
    std::cout << "Size of stack: " << s.size() << std::endl; // 输出: Size of stack: 2

    // 继续移除元素
    s.pop();
    s.pop();

    // 检查栈是否为空
    if (s.empty()) {
        std::cout << "Stack is empty." << std::endl; // 输出: Stack is empty.
    }

    return 0;
}
```


输出结果：


```
Top element is: 30
After popping, top element is: 20
Stack is not empty.
Size of stack: 2
Stack is empty.
```


### 注意事项


- `` 不提供直接访问栈中元素的方法，只能通过 `top()` 访问栈顶元素。
- 尝试在空栈上调用 `top()` 或 `pop()` 将导致未定义行为。
- `` 的底层容器可以是任何支持随机访问迭代器的序列容器，如 `vector` 或 `deque`。








	  AI 思考中...





			** [C++ 容器类
](https://www.runoob.com/cpp-libs-priority_queue.html) [C++ 容器类 ](https://www.runoob.com/cpp-libs-set.html) ** ### 点我分享笔记 笔记需要是本篇文章的内容扩展！
**

[文章投稿，可点击这里](https://www.runoob.com/tougao)


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)


### 分享笔记前必须登录！


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)
-->





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