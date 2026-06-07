# 优化堆排序

- Source: https://www.runoob.com/data-structures/heap-sort-optimization.html

上一节的堆排序，我们开辟了额外的空间进行构造堆和对堆进行排序。这一小节，我们进行优化，使用原地堆排序。


对于一个最大堆，首先将开始位置数据和数组末尾数值进行交换，那么数组末尾就是最大元素，然后再对W元素进行 shift down 操作，重新生成最大堆，然后将新生成的最大数和整个数组倒数第二位置进行交换，此时倒数第二位置就是倒数第二大数据，这个过程以此类推。


整个过程可以用如下图表示：


![](https://www.runoob.com/wp-content/uploads/2020/09/heapSort-01.png)


### Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/09/runoob-algorithm-HeapSort.zip)


## src/runoob/heap/HeapSort.java 文件代码：


```
package runoob.heap;

import runoob.sort.SortTestHelper;

/**
 * 原地堆排序
 */
public class HeapSort<T extends Comparable> {

    public static void sort(Comparable[] arr) {

        int n = arr.length;

        // 注意，此时我们的堆是从0开始索引的
        // 从(最后一个元素的索引-1)/2开始
        // 最后一个元素的索引 = n-1
        for (int i = (n - 1 - 1) / 2; i >= 0; i--)
            shiftDown(arr, n, i);

        for (int i = n - 1; i > 0; i--) {
            swap(arr, 0, i);
            shiftDown(arr, i, 0);
        }
    }

    // 交换堆中索引为i和j的两个元素
    private static void swap(Object[] arr, int i, int j) {
        Object t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    // 原始的shiftDown过程
    private static void shiftDown(Comparable[] arr, int n, int k) {

        while (2 * k + 1 < n) {
            //左孩子节点
            int j = 2 * k + 1;
            //右孩子节点比左孩子节点大
            if (j + 1 < n && arr[j + 1].compareTo(arr[j]) > 0)
                j += 1;
            //比两孩子节点都大
            if (arr[k].compareTo(arr[j]) >= 0) break;
            //交换原节点和孩子节点的值
            swap(arr, k, j);
            k = j;
        }
    }

    // 测试 HeapSort
    public static void main(String[] args) {

        int N = 100;
        Integer[] arr = SortTestHelper.generateRandomArray(N, 0, 100000);
        sort(arr);
        // 将heapify中的数据逐渐使用extractMax取出来
        // 取出来的顺序应该是按照从大到小的顺序取出来的
        for (int i = 0; i < N; i++) {
            System.out.print(arr[i] + " ");
        }
        // 确保arr数组是从大到小排列的
        for (int i = 1; i < N; i++)
            assert arr[i - 1] >= arr[i];
    }
}
```










	  AI 思考中...





			** [基础堆排序](https://www.runoob.com/heap-sort.html)
			[索引堆及其优化](https://www.runoob.com/heap-index.html) **













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