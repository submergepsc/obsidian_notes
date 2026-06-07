# Java 数据结构

- Source: https://www.runoob.com/java/java-data-structures.html

Java 提供了丰富的数据结构来处理和组织数据。

Java 的 java.util 包中提供了许多这些数据结构的实现，可以根据需要选择合适的类。


以下是一些常见的 Java 数据结构：


### 数组（Arrays）


数组（Arrays）是一种基本的数据结构，可以存储固定大小的相同类型的元素。


```
int[] array = new int[5];
```


- **特点：** 固定大小，存储相同类型的元素。
- **优点：** 随机访问元素效率高。
- **缺点：** 大小固定，插入和删除元素相对较慢。


### 列表（Lists）


Java 提供了多种列表实现，如 ArrayList 和 LinkedList。


```
List<String> arrayList = new ArrayList<>();
List<Integer> linkedList = new LinkedList<>();
```


**ArrayList:**


- **特点：** 动态数组，可变大小。
- **优点：** 高效的随机访问和快速尾部插入。
- **缺点：** 中间插入和删除相对较慢。


**LinkedList:**


- **特点：** 双向链表，元素之间通过指针连接。
- **优点：** 插入和删除元素高效，迭代器性能好。
- **缺点：** 随机访问相对较慢。


### 集合（Sets）


集合（Sets）用于存储不重复的元素，常见的实现有 HashSet 和 TreeSet。


```
Set<String> hashSet = new HashSet<>();
Set<Integer> treeSet = new TreeSet<>();
```


**HashSet:**


- **特点：** 无序集合，基于HashMap实现。
- **优点：** 高效的查找和插入操作。
- **缺点：** 不保证顺序。


**TreeSet:**


- **特点：**TreeSet 是有序集合，底层基于红黑树实现，不允许重复元素。
- ** 优点：** 提供自动排序功能，适用于需要按顺序存储元素的场景。
- ** 缺点：** 性能相对较差，不允许插入 null 元素。


### 映射（Maps）


映射（Maps）用于存储键值对，常见的实现有 HashMap 和 TreeMap。


```
Map<String, Integer> hashMap = new HashMap<>();
Map<String, Integer> treeMap = new TreeMap<>();
```


**HashMap:**


- **特点：** 基于哈希表实现的键值对存储结构。
- **优点：** 高效的查找、插入和删除操作。
- **缺点：** 无序，不保证顺序。


**TreeMap:**


- **特点：** 基于红黑树实现的有序键值对存储结构。
- **优点：** 有序，支持按照键的顺序遍历。
- **缺点：** 插入和删除相对较慢。


### 栈（Stack）

栈（Stack）是一种线性数据结构，它按照后进先出（Last In, First Out，LIFO）的原则管理元素。在栈中，新元素被添加到栈的顶部，而只能从栈的顶部移除元素。这就意味着最后添加的元素是第一个被移除的。


```
Stack<Integer> stack = new Stack<>();
```


**Stack 类:**


- **特点：** 代表一个栈，通常按照后进先出（LIFO）的顺序操作元素。


### 队列（Queue）


队列（Queue）遵循先进先出（FIFO）原则，常见的实现有 LinkedList 和 PriorityQueue。


```
Queue<String> queue = new LinkedList<>();
```


**Queue 接口:**


- **特点：** 代表一个队列，通常按照先进先出（FIFO）的顺序操作元素。
- **实现类：** LinkedList, PriorityQueue, ArrayDeque。


### 堆（Heap）


堆（Heap）优先队列的基础，可以实现最大堆和最小堆。


```
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
```


### 树（Trees）


Java 提供了 TreeNode 类型，可以用于构建二叉树等数据结构。


```
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
```


### 图（Graphs）


图的表示通常需要自定义数据结构或使用图库，Java 没有内建的图类。


以上介绍的只是 Java 中一些常见的数据结构，实际上还有很多其他的数据结构和算法可以根据具体问题选择使用。


---


## 其他一些说明


以下这些类是传统遗留的，在 Java2 中引入了一种新的框架-集合框架(Collection)，我们后面再讨论。


### 枚举（Enumeration）


枚举（Enumeration）接口虽然它本身不属于数据结构,但它在其他数据结构的范畴里应用很广。 枚举（The Enumeration）接口定义了一种从数据结构中取回连续元素的方式。

例如，枚举定义了一个叫nextElement 的方法，该方法用来得到一个包含多元素的数据结构的下一个元素。

关于枚举接口的更多信息，[请参见枚举（Enumeration）](https://www.runoob.com/java-enumeration-interface.html)。


### 位集合（BitSet）


位集合类实现了一组可以单独设置和清除的位或标志。

该类在处理一组布尔值的时候非常有用，你只需要给每个值赋值一"位"，然后对位进行适当的设置或清除，就可以对布尔值进行操作了。

关于该类的更多信息，[请参见位集合（BitSet）](https://www.runoob.com/java-bitset-class.html)。


### 向量（Vector）


向量（Vector）类和传统数组非常相似，但是Vector的大小能根据需要动态的变化。

和数组一样，Vector对象的元素也能通过索引访问。

使用Vector类最主要的好处就是在创建对象的时候不必给对象指定大小，它的大小会根据需要动态的变化。

关于该类的更多信息，[请参见向量(Vector)](https://www.runoob.com/java-vector-class.html)


### 栈（Stack）


栈（Stack）实现了一个后进先出（LIFO）的数据结构。

你可以把栈理解为对象的垂直分布的栈，当你添加一个新元素时，就将新元素放在其他元素的顶部。

当你从栈中取元素的时候，就从栈顶取一个元素。换句话说，最后进栈的元素最先被取出。

关于该类的更多信息，[请参见栈（Stack）](https://www.runoob.com/java-stack-class.html)。


### 字典（Dictionary）


字典（Dictionary） 类是一个抽象类，它定义了键映射到值的数据结构。

当你想要通过特定的键而不是整数索引来访问数据的时候，这时候应该使用 Dictionary。

由于 Dictionary 类是抽象类，所以它只提供了键映射到值的数据结构，而没有提供特定的实现。

关于该类的更多信息，[请参见字典（ Dictionary）](https://www.runoob.com/java-dictionary-class.html)。


Dictionary 类在较新的 Java 版本中已经被弃用（deprecated），推荐使用 Map 接口及其实现类，如 HashMap、TreeMap 等，来代替 Dictionary。


Map 接口及其实现类 可以参考：[Java 集合框架](https://www.runoob.com/java-collections.html)。


### 哈希表（Hashtable）


Hashtable类提供了一种在用户定义键结构的基础上来组织数据的手段。

例如，在地址列表的哈希表中，你可以根据邮政编码作为键来存储和排序数据，而不是通过人名。

哈希表键的具体含义完全取决于哈希表的使用情景和它包含的数据。

关于该类的更多信息，[请参见哈希表（HashTable）](https://www.runoob.com/java-hashTable-class.html)。


### 属性（Properties）


Properties 继承于 Hashtable.Properties 类表示了一个持久的属性集.属性列表中每个键及其对应值都是一个字符串。

Properties 类被许多Java类使用。例如，在获取环境变量时它就作为System.getProperties()方法的返回值。

关于该类的更多信息，[请参见属性（Properties）](https://www.runoob.com/java-properties-class.html)。








	  AI 思考中...





			** [Java Properties 类](https://www.runoob.com/java-properties-class.html)
			[Java 集合框架](https://www.runoob.com/java-collections.html) **













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

      : ·[Java 实例](https://www.runoob.com/java-examples.html)





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