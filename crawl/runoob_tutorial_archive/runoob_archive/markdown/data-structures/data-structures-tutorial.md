# 数据结构与算法

- Source: https://www.runoob.com/data-structures/data-structures-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2020/09/data-structure.png)

数据结构（英语：data structure）是计算机中存储、组织数据的方式。

数据结构是一种具有一定逻辑关系，在计算机中应用某种存储结构，并且封装了相应操作的数据元素集合。它包含三方面的内容，逻辑关系、存储关系及操作。


不同种类的数据结构适合于不同种类的应用，而部分甚至专门用于特定的作业任务。例如，计算机网络依赖于路由表运作，B 树高度适用于数据库的封装。


**

## 为什么要学习数据结构和算法？


随着应用程序变得越来越复杂和数据越来越丰富，几百万、几十亿甚至几百亿的数据就会出现，对这么大对数据进行搜索、插入或者排序等的操作就越来越慢，数据结构就是用来解决这些问题的。


学习数据结构和算法可以：


- **提高代码效率**：好的数据结构和算法能让程序运行更快、占用更少内存
- **解决复杂问题**：许多实际问题需要特定的数据结构和算法才能有效解决
- **面试必备**：技术面试中几乎必考的知识点
- **编程基础**：它是所有高级编程技术的基石


## 阅读本教程前，您需要了解的知识？


在您开始阅读本教程之前，您必须具备基本的基本的编程知识，如 Python或 Java 等编程的概念。


如果您还不了解这些概念，那么建议您先阅读我们的 [Python 教程](https://www.runoob.com/../python3/python3-tutorial.html) 或 [Java 教程](https://www.runoob.com/../java/java-tutorial.html)。



我们推荐使用 Python 作为学习语言，原因如下：


| 特性 | Python | Java | C++ |
| --- | --- | --- | --- |
| 学习难度 | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 语法简洁度 | 高 | 中 | 低 |
| 执行效率 | 中 | 高 | 很高 |
| 社区支持 | 丰富 | 丰富 | 丰富 |
| 推荐指数 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |


---


## 数据结构与算法说明


数据结构**就像是我们整理物品的方式。想象一下你的书架：


- 如果随意堆放，找一本书会很困难（低效的数据结构）
- 如果按类别、作者、字母顺序摆放，找书就很快（高效的数据结构）


**算法**则是解决问题的步骤和方法。就像做菜的食谱：


- 同样的食材（数据），不同的做法（算法）会产生不同的结果
- 有些做法又快又好，有些则费时费力


### 基本术语


| 术语 | 生活比喻 | 技术定义 |
| --- | --- | --- |
| 数据 | 物品 | 信息的载体，是描述客观事物的符号 |
| 数据元素 | 单个物品 | 数据的基本单位 |
| 数据结构 | 物品整理方式 | 数据元素之间存在的一种或多种特定关系的集合 |
| 算法 | 做事步骤 | 解决问题的明确指令，有限时间内完成 |


### 常见的数据结构


- **栈（Stack）：**栈是一种特殊的线性表，它只能在一个表的一个固定端进行数据结点的插入和删除操作。
- **队列（Queue）：**队列和栈类似，也是一种特殊的线性表。和栈不同的是，队列只允许在表的一端进行插入操作，而在另一端进行删除操作。
- **数组（Array）：**数组是一种聚合数据类型，它是将具有相同类型的若干变量有序地组织在一起的集合。
- **链表（Linked List）：**链表是一种数据元素按照链式存储结构进行存储的数据结构，这种存储结构具有在物理上存在非连续的特点。
- **树（Tree）：**树是典型的非线性结构，它是包括，2 个结点的有穷集合 K。
- **图（Graph）：**图是另一种非线性数据结构。在图结构中，数据结点一般称为顶点，而边是顶点的有序偶对。
- **堆（Heap）：**堆是一种特殊的树形数据结构，一般讨论的堆都是二叉堆。
- **散列表（Hash table）：**散列表源自于散列函数(Hash function)，其思想是如果在结构中存在关键字和T相等的记录，那么必定在F(T)的存储位置可以找到该记录，这样就可以不用进行比较操作而直接取得所查记录。


### 常用算法

数据结构研究的内容：就是如何按一定的逻辑结构，把数据组织起来，并选择适当的存储表示方法把逻辑结构组织好的数据存储到计算机的存储器里。算法研究的目的是为了更有效的处理数据，提高数据运算效率。数据的运算是定义在数据的逻辑结构上，但运算的具体实现要在存储结构上进行。一般有以下几种常用运算：


- **检索：**检索就是在数据结构里查找满足一定条件的节点。一般是给定一个某字段的值，找具有该字段值的节点。
- **插入：**往数据结构中增加新的节点。
- **删除：**把指定的结点从数据结构中去掉。
- **更新：**改变指定节点的一个或多个字段的值。
- **排序：**把节点按某种指定的顺序重新排列。例如递增或递减。


---


## 参考资料


Hello 算法：[https://github.com/krahets/hello-algo](https://github.com/krahets/hello-algo)


Python 算法实现：[https://github.com/TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)。


Play-with-Algorithms: [https://github.com/liuyubobobo/Play-with-Algorithms](https://github.com/liuyubobobo/Play-with-Algorithms)。










	  AI 思考中...






			[插入排序](https://www.runoob.com/insertion-sort.html) **













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