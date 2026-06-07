# C++ 容器类

- Source: https://www.runoob.com/cplusplus/cpp-libs-queue.html

C++ 标准库中的 `` 头文件提供了队列（Queue）数据结构的实现。队列是一种先进先出（FIFO, First In First Out）的数据结构，它允许在一端添加元素（称为队尾），并在另一端移除元素（称为队首）。


队列是一种线性数据结构，它遵循以下规则：


- 元素只能从队尾添加。
- 元素只能从队首移除。


### 语法


在 C++ 中，队列的语法如下：


```
#include <queue>

// 声明队列
std::queue<Type> q;
```


这里 `Type` 是队列中存储元素的数据类型。


### 常用操作


队列提供了以下常用操作：


- `empty()`: 检查队列是否为空。
- `size()`: 返回队列中的元素数量。
- `front()`: 返回队首元素的引用。
- `back()`: 返回队尾元素的引用。
- `push()`: 在队尾添加一个元素。
- `pop()`: 移除队首元素。


## 实例


下面是一个使用 C++ 标准库 `` 的简单实例：


## 实例


```cpp
#include <iostream>
#include <queue>

int main() {
    // 创建一个整数队列
    std::queue<int> q;

    // 向队列中添加元素
    q.push(10);
    q.push(20);
    q.push(30);

    // 打印队列中的元素数量
    std::cout << "队列中的元素数量: " << q.size() << std::endl;

    // 打印队首元素
    std::cout << "队首元素: " << q.front() << std::endl;

    // 打印队尾元素
    std::cout << "队尾元素: " << q.back() << std::endl;

    // 移除队首元素
    q.pop();
    std::cout << "移除队首元素后，队首元素: " << q.front() << std::endl;

    // 再次打印队列中的元素数量
    std::cout << "队列中的元素数量: " << q.size() << std::endl;

    return 0;
}
```


输出结果：


```
队列中的元素数量: 3
队首元素: 10
队尾元素: 30
移除队首元素后，队首元素: 20
队列中的元素数量: 2
```


C++ 的 `` 标准库提供了一种方便的方式来实现队列数据结构。通过使用队列，我们可以有效地管理需要按照特定顺序处理的元素集合。希望这篇文章能帮助初学者更好地理解和使用 C++ 中的队列。


### 注意事项


- 队列不允许随机访问元素，即不能直接通过索引访问队列中的元素。
- 队列的实现通常使用链表或动态数组，这取决于具体的实现。










	  AI 思考中...





			** [C++ 容器类 ](https://www.runoob.com/cpp-libs-deque.html)
			[C++ 容器类
](https://www.runoob.com/cpp-libs-priority_queue.html) ** ### 点我分享笔记 笔记需要是本篇文章的内容扩展！
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