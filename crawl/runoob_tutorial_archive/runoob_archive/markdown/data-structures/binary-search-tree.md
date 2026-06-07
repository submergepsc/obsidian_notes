# 二分搜索树

- Source: https://www.runoob.com/data-structures/binary-search-tree.html

### 一、概念及其介绍


二分搜索树（英语：Binary Search Tree），也称为 二叉查找树 、二叉搜索树 、有序二叉树或排序二叉树。满足以下几个条件：


- 若它的左子树不为空，左子树上所有节点的值都小于它的根节点。
- 若它的右子树不为空，右子树上所有的节点的值都大于它的根节点。


它的左、右子树也都是二分搜索树。


如下图所示：


![](https://www.runoob.com/wp-content/uploads/2020/09/PbZvFQEItGIFirEP.png)


### 二、适用说明

二分搜索树有着高效的插入、删除、查询操作。

平均时间的时间复杂度为 **O(log n)**，最差情况为 **O(n)**。二分搜索树与堆不同，不一定是完全二叉树，底层不容易直接用数组表示故采用链表来实现二分搜索树。


|  | 查找元素 | 插入元素 | 删除元素 |
| --- | --- | --- | --- |
| 普通数组 | O(n) | O(n) | O(n) |
| 顺序数组 | O(logn) | O(n) | O(n) |
| 二分搜索树 | O(logn) | O(logn) | O(logn) |


下面先介绍数组形式的二分查找法作为思想的借鉴，后面继续介绍二分搜索树的查找方式。


### 三、二分查找法过程图示

二分查找法的思想在 1946 年提出，查找问题是计算机中非常重要的基础问题，对于有序数列，才能使用二分查找法。如果我们要查找一元素，先看数组中间的值V和所需查找数据的大小关系，分三种情况：


- 1、等于所要查找的数据，直接找到
- 2、若小于 V，在小于 V 部分分组继续查询
- 2、若大于 V，在大于 V 部分分组继续查询


![](https://www.runoob.com/wp-content/uploads/2020/09/RsvE28BWbRdtJ7YM.png)


### 四、Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/09/runoob-algorithm-BinarySearch.zip)


## src/runoob/binary/BinarySearch.java 文件代码：


```
package runoob.binarySearch;

/**
 * 二分查找法
 */
public class BinarySearch {
    // 二分查找法,在有序数组arr中,查找target
    // 如果找到target,返回相应的索引index
    // 如果没有找到target,返回-1
    public static int find(Comparable[] arr, Comparable target) {

        // 在arr[l...r]之中查找target
        int l = 0, r = arr.length-1;
        while( l <= r ){

            //int mid = (l + r)/2;
            // 防止极端情况下的整形溢出，使用下面的逻辑求出mid
            int mid = l + (r-l)/2;

            if( arr[mid].compareTo(target) == 0 )
                return mid;

            if( arr[mid].compareTo(target) > 0 )
                r = mid - 1;
            else
                l = mid + 1;
        }

        return -1;
    }
}
```










	  AI 思考中...





			** [索引堆及其优化](https://www.runoob.com/heap-index.html)
			[二分搜索树节点的插入](https://www.runoob.com/binary-search-tree-insert.html) **













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