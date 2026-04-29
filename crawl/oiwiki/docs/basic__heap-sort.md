# 堆排序 - OI Wiki

- Source: https://oi-wiki.org/basic/heap-sort/

# 堆排序

本页面将简要介绍堆排序．

## 定义

堆排序（英语：Heapsort）是指利用 [二叉堆](../../ds/binary-heap/) 这种数据结构所设计的一种排序算法．堆排序的适用数据结构为数组．

## 过程

堆排序的本质是建立在堆上的选择排序．

### 排序

首先建立大顶堆，然后将堆顶的元素取出，作为最大值，与数组尾部的元素交换，并维持残余堆的性质；

之后将堆顶的元素取出，作为次大值，与数组倒数第二位元素交换，并维持残余堆的性质；

以此类推，在第 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次操作后，整个数组就完成了排序．

### 在数组上建立二叉堆

从根节点开始，依次将每一层的节点排列在数组里．

于是有数组中下标为 `i` 的节点，对应的父结点、左子结点和右子结点如下：

```text 1 2 3 ``` |  ```text iParent ( i ) = ( i \- 1 ) / 2 ; iLeftChild ( i ) = 2 * i \+ 1 ; iRightChild ( i ) = 2 * i \+ 2 ; ```   
---|---  
  
## 性质

### 稳定性

同选择排序一样，由于其中交换位置的操作，所以是不稳定的排序算法．

### 时间复杂度

堆排序的最优时间复杂度、平均时间复杂度、最坏时间复杂度均为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 空间复杂度

由于可以在输入数组上建立堆，所以这是一个原地算法．

## 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` |  ```text void sift_down ( int arr [], int start , int end ) { // 计算父结点和子结点的下标 int parent = start ; int child = parent * 2 \+ 1 ; while ( child <= end ) { // 子结点下标在范围内才做比较 // 先比较两个子结点大小，选择最大的 if ( child \+ 1 <= end && arr [ child ] < arr [ child \+ 1 ]) child ++ ; // 如果父结点比子结点大，代表调整完毕，直接跳出函数 if ( arr [ parent ] >= arr [ child ]) return ; else { // 否则交换父子内容，子结点再和孙结点比较 swap ( arr [ parent ], arr [ child ]); parent = child ; child = parent * 2 \+ 1 ; } } } void heap_sort ( int arr [], int len ) { // 从最后一个节点的父节点开始 sift down 以完成堆化 (heapify) for ( int i = ( len \- 1 \- 1 ) / 2 ; i >= 0 ; i \-- ) sift_down ( arr , i , len \- 1 ); // 先将第一个元素和已经排好的元素前一位做交换，再重新调整（刚调整的元素之前的元素），直到排序完毕 for ( int i = len \- 1 ; i > 0 ; i \-- ) { swap ( arr [ 0 ], arr [ i ]); sift_down ( arr , 0 , i \- 1 ); } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` |  ```text def sift_down ( arr , start , end ): # 计算父结点和子结点的下标 parent = int ( start ) child = int ( parent * 2 \+ 1 ) while child <= end : # 子结点下标在范围内才做比较 # 先比较两个子结点大小，选择最大的 if child \+ 1 <= end and arr [ child ] < arr [ child \+ 1 ]: child += 1 # 如果父结点比子结点大，代表调整完毕，直接跳出函数 if arr [ parent ] >= arr [ child ]: return else : # 否则交换父子内容，子结点再和孙结点比较 arr [ parent ], arr [ child ] = arr [ child ], arr [ parent ] parent = child child = int ( parent * 2 \+ 1 ) def heap_sort ( arr , len ): # 从最后一个节点的父节点开始 sift down 以完成堆化 (heapify) i = ( len \- 1 \- 1 ) / 2 while i >= 0 : sift_down ( arr , i , len \- 1 ) i -= 1 # 先将第一个元素和已经排好的元素前一位做交换，再重新调整（刚调整的元素之前的元素），直到排序完毕 i = len \- 1 while i > 0 : arr [ 0 ], arr [ i ] = arr [ i ], arr [ 0 ] sift_down ( arr , 0 , i \- 1 ) i -= 1 ```   
---|---  
  
## 外部链接

  * [堆排序 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/heap-sort.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/heap-sort.md "edit.link.title")  
>  __本页面贡献者：[NachtgeistW](https://github.com/NachtgeistW), [Enter-tainer](https://github.com/Enter-tainer), [iamtwz](https://github.com/iamtwz), [sshwy](https://github.com/sshwy), [CamberLoid](https://github.com/CamberLoid), [Ir1d](https://github.com/Ir1d), [ksyx](https://github.com/ksyx), [Menci](https://github.com/Menci), [minghu6](https://github.com/minghu6), [ouuan](https://github.com/ouuan), [partychicken](https://github.com/partychicken), [shawlleyw](https://github.com/shawlleyw), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
