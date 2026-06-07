# 索引堆及其优化

- Source: https://www.runoob.com/data-structures/heap-index.html

### 一、概念及其介绍


索引堆是对堆这个数据结构的优化。

索引堆使用了一个新的 int 类型的数组，用于存放索引信息。

相较于堆，优点如下：


- 优化了交换元素的消耗。
- 加入的数据位置固定，方便寻找。


### 二、适用说明


如果堆中存储的元素较大，那么进行交换就要消耗大量的时间，这个时候可以用索引堆的数据结构进行替代，堆中存储的是数组的索引，我们相应操作的是索引。


### 三、结构图示


![](https://www.runoob.com/wp-content/uploads/2020/09/indexHeap-01.png)


我们需要对之前堆的代码实现进行改造，换成直接操作索引的思维。首先构造函数添加索引数组属性 indexes。


```
protected T[] data;      // 最大索引堆中的数据
protected int[] indexes;    // 最大索引堆中的索引
protected int count;
protected int capacity;
```


相应构造函数调整为，添加初始化索引数组。


```
...
public IndexMaxHeap(int capacity){
    data = (T[])new Comparable[capacity+1];
    indexes = new int[capacity+1];
    count = 0;
    this.capacity = capacity;
}
...
```


调整插入操作，indexes 数组中添加的元素是真实 data 数组的索引 **indexes[count+1] = i**。


```
...
// 向最大索引堆中插入一个新的元素, 新元素的索引为i, 元素为item
// 传入的i对用户而言,是从0索引的
public void insert(int i, Item item){
    assert count + 1 <= capacity;
    assert i + 1 >= 1 && i + 1 <= capacity;
    i += 1;
    data[i] = item;
    indexes[count+1] = i;
    count ++;
    shiftUp(count);
}
...
```


调整 shift up 操作：比较的是 data 数组中父节点数据的大小，所以需要表示为 **data[index[k/2]]







	  AI 思考中...





			** [优化堆排序](https://www.runoob.com/heap-sort-optimization.html)
			[二分搜索树](https://www.runoob.com/binary-search-tree.html) **













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