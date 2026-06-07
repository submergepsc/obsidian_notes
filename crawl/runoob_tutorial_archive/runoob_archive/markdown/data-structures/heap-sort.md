# 基础堆排序

- Source: https://www.runoob.com/data-structures/heap-sort.html

### 一、概念及其介绍

堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。

堆是一个近似 完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。


### 二、适用说明


我们之前构造堆的过程是一个个数据调用 insert 方法使用 shift up 逐个插入到堆中，这个算法的时候时间复杂度是 **O(nlogn)**，本小节介绍的一种构造堆排序的过程，称为 **Heapify**，算法时间复杂度为 **O(n)**。


### 三、过程图示


完全二叉树有个重要性质，对于第一个非叶子节点的索引是 **n/2** 取整数得到的索引值，其中 **n** 是元素个数(前提是数组索引从 1 开始计算)。


![](https://www.runoob.com/wp-content/uploads/2020/09/heapify-01.png)


索引 5 位置是第一个非叶子节点，我们从它开始逐一向前分别把每个元素作为根节点进行 shift down 操作满足最大堆的性质。


索引 5 位置进行 shift down 操作后，22 和 62 交换位置。


![](https://www.runoob.com/wp-content/uploads/2020/09/heapify-02.png)


对索引 4 元素进行 shift down 操作


![](https://www.runoob.com/wp-content/uploads/2020/09/heapify-03.png)


对索引 3 元素进行 shift down 操作


![](https://www.runoob.com/wp-content/uploads/2020/09/heapify-04.png)


对索引 2 元素进行 shift down 操作


![](https://www.runoob.com/wp-content/uploads/2020/09/heapify-05.png)


最后对根节点进行 shift down 操作，整个堆排序过程就完成了。


![](https://www.runoob.com/wp-content/uploads/2020/09/heapify-06.png)


### 四、Java 实例代码


**源码包下载：**[Download](https://www.runoob.com/wp-content/uploads/2020/09/runoob-algorithm-Heapify.zip)


## src/runoob/heap/Heapify.java 文件代码：


```
package runoob.heap;

import runoob.sort.SortTestHelper;

/**
 * 用heapify进行堆排序
 */
public class Heapify<T extends Comparable> {

    protected T[] data;
    protected int count;
    protected int capacity;

    // 构造函数, 通过一个给定数组创建一个最大堆
    // 该构造堆的过程, 时间复杂度为O(n)
    public Heapify(T arr[]){

        int n = arr.length;

        data = (T[])new Comparable[n+1];
        capacity = n;

        for( int i = 0 ; i < n ; i ++ )
            data[i+1] = arr[i];
        count = n;
        //从第一个不是叶子节点的元素开始
        for( int i = count/2 ; i >= 1 ; i -- )
            shiftDown(i);
    }
    // 返回堆中的元素个数
    public int size(){
        return count;
    }
    // 返回一个布尔值, 表示堆中是否为空
    public boolean isEmpty(){
        return count == 0;
    }
    // 像最大堆中插入一个新的元素 item
    public void insert(T item){
        assert count + 1 <= capacity;
        data[count+1] = item;
        count ++;
        shiftUp(count);
    }
    // 从最大堆中取出堆顶元素, 即堆中所存储的最大数据
    public T extractMax(){
        assert count > 0;
        T ret = data[1];
        swap( 1 , count );
        count --;
        shiftDown(1);
        return ret;
    }
    // 获取最大堆中的堆顶元素
    public T getMax(){
        assert( count > 0 );
        return data[1];
    }

    // 交换堆中索引为i和j的两个元素
    private void swap(int i, int j){
        T t = data[i];
        data[i] = data[j];
        data[j] = t;
    }

    //********************
    //* 最大堆核心辅助函数
    //********************
    private void shiftUp(int k){

        while( k > 1 && data[k/2].compareTo(data[k]) < 0 ){
            swap(k, k/2);
            k /= 2;
        }
    }

    private void shiftDown(int k){

        while( 2*k <= count ){
            int j = 2*k; // 在此轮循环中,data[k]和data[j]交换位置
            if( j+1 <= count && data[j+1].compareTo(data[j]) > 0 )
                j ++;
            // data[j] 是 data[2*k]和data[2*k+1]中的最大值

            if( data[k].compareTo(data[j]) >= 0 ) break;
            swap(k, j);
            k = j;
        }
    }

    // 测试 heapify
    public static void main(String[] args) {
        int N = 100;
        Integer[] arr = SortTestHelper.generateRandomArray(N, 0, 100000);
        Heapify<Integer> heapify = new Heapify<Integer>(arr);
        // 将heapify中的数据逐渐使用extractMax取出来
        // 取出来的顺序应该是按照从大到小的顺序取出来的
        for( int i = 0 ; i < N ; i ++ ){
            arr[i] = heapify.extractMax();
            System.out.print(arr[i] + " ");
        }

        // 确保arr数组是从大到小排列的
        for( int i = 1 ; i < N ; i ++ )
            assert arr[i-1] >= arr[i];
    }
}
```









	  AI 思考中...





			** [堆的 shift down](https://www.runoob.com/heap-shift-down.html)
			[优化堆排序](https://www.runoob.com/heap-sort-optimization.html) **













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