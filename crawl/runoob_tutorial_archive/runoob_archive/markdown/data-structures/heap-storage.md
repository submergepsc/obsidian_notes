# 堆的基本存储

- Source: https://www.runoob.com/data-structures/heap-storage.html

### 一、概念及其介绍


堆(Heap)是计算机科学中一类特殊的数据结构的统称。

堆通常是一个可以被看做一棵完全二叉树的数组对象。

堆满足下列性质：


- 堆中某个节点的值总是不大于或不小于其父节点的值。
- 堆总是一棵完全二叉树。


### 二、适用说明


堆是利用完全二叉树的结构来维护一组数据，然后进行相关操作，一般的操作进行一次的时间复杂度在 **O(1)~O(logn)** 之间，堆通常用于动态分配和释放程序所使用的对象。


若为优先队列的使用场景，普通数组或者顺序数组，最差情况为 **O(n^2)**，堆这种数据结构也可以提高入队和出队的效率。


|  | 入队 | 出队 |
| --- | --- | --- |
| 普通数组 | O(1) | O(n) |
| 顺序数组 | O(n) | O(1) |
| 堆 | O(logn) | O(log) |


### 三、结构图示

二叉堆是一颗完全二叉树，且堆中某个节点的值总是不大于其父节点的值，该完全二叉树的深度为 k，除第 k 层外，其它各层 (1～k-1) 的结点数都达到最大个数，第k 层所有的结点都连续集中在最左边。

其中堆的根节点最大称为最大堆，如下图所示：


![](https://www.runoob.com/wp-content/uploads/2020/09/heap-01.png)


我们可以使用数组存储二叉堆，右边的标号是数组的索引。


![](https://www.runoob.com/wp-content/uploads/2020/09/heap-02.png)


![](https://www.runoob.com/wp-content/uploads/2020/09/heap-03.png)


假设当前元素的索引位置为 i，可以得到规律：


```
parent(i) = i/2（取整）
left child(i) = 2*i
right child(i) = 2*i +1
```


### 四、Java 实例代码

**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/09/runoob-algorithm-heap.zip)


## src/runoob/heap/MaxHeap.java 文件代码：


```
package runoob.heap;

/**
 * 堆定义
 */
public class MaxHeap<T> {
    private T[] data;
    private int count;
    // 构造函数, 构造一个空堆, 可容纳capacity个元素
    public MaxHeap(int capacity){
        data = (T[])new Object[capacity+1];
        count = 0;
    }
    // 返回堆中的元素个数
    public int size(){
        return count;
    }
    // 返回一个布尔值, 表示堆中是否为空
    public boolean isEmpty(){
        return count == 0;
    }
    // 测试 MaxHeap
    public static void main(String[] args) {
        MaxHeap<Integer> maxHeap = new MaxHeap<Integer>(100);
        System.out.println(maxHeap.size());
    }
}
```









	  AI 思考中...





			** [排序算法衍生问题](https://www.runoob.com/sorting-algorithm-derivative-problem.html)
			[堆的 shift up](https://www.runoob.com/heap-shift-up.html) **













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