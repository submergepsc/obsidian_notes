# 选择排序 - OI Wiki

- Source: https://oi-wiki.org/basic/selection-sort/

# 选择排序

本页面将简要介绍选择排序．

## 定义

选择排序（英语：Selection sort）是一种简单直观的排序算法．它的工作原理是每次找出第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小的元素（也就是 𝐴𝑖..𝑛Ai..n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中最小的元素），然后将这个元素与数组第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个位置上的元素交换．

![selection sort animate example](./images/selection-sort-animate.svg)

## 性质

### 稳定性

选择排序的稳定性取决于其具体实现．

倘若使用链表实现，由于链表的任意位置插入和删除均为 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故无需使用 swap（交换两个元素）操作：每次从未排序部分选择最小元素（若有多个，选取第 1 个）后，将其插入到未排序部分的第 1 个元素之前，这样就能够保证稳定性．

假如使用数组实现（OI 中一般的实现方式），由于数组任意位置插入和删除均为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故只能使用 swap 将未排序部分的元素移到已排序部分．swap 操作使得数组实现的选择排序不稳定．

下面给出的实现示例均是基于数组元素的交换，因此均为 **不稳定的** ．

### 时间复杂度

选择排序的最优时间复杂度、平均时间复杂度和最坏时间复杂度均为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 代码实现

### 伪代码

1𝐈𝐧𝐩𝐮𝐭. An array 𝐴 consisting of 𝑛 elements.2𝐎𝐮𝐭𝐩𝐮𝐭. 𝐴 will be sorted in nondecreasing order.3𝐌𝐞𝐭𝐡𝐨𝐝. 4𝐟𝐨𝐫 𝑖←1 𝐭𝐨 𝑛−15𝑖𝑡ℎ←𝑖6𝐟𝐨𝐫 𝑗←𝑖+1 𝐭𝐨 𝑛7𝐢𝐟 𝐴[𝑗]<𝐴[𝑖𝑡ℎ]8𝑖𝑡ℎ←𝑗9swap 𝐴[𝑖] and 𝐴[𝑖𝑡ℎ]1Input. An array A consisting of n elements.2Output. A will be sorted in nondecreasing order.3Method. 4for i←1 to n−15ith←i6for j←i+1 to n7if A[j]<A[ith]8ith←j9swap A[i] and A[ith]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

C++PythonJava

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text #include <utility> void selection_sort ( int * a , int n ) { for ( int i = 1 ; i < n ; ++ i ) { int ith = i ; for ( int j = i \+ 1 ; j <= n ; ++ j ) { if ( a [ j ] < a [ ith ]) { ith = j ; } } std :: swap ( a [ i ], a [ ith ]); } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text def selection_sort ( a , n ): for i in range ( 1 , n ): ith = i for j in range ( i \+ 1 , n \+ 1 ): if a [ j ] < a [ ith ]: ith = j a [ i ], a [ ith ] = a [ ith ], a [ i ] ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text // arr代码下标从 1 开始索引 static void selection_sort ( int [] arr , int n ) { for ( int i = 1 ; i < n ; i ++ ) { int ith = i ; for ( int j = i \+ 1 ; j <= n ; j ++ ) { if ( arr [ j ] < arr [ ith ] ) { ith = j ; } } // swap int temp = arr [ i ] ; arr [ i ] = arr [ ith ] ; arr [ ith ] = temp ; } } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/selection-sort.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/selection-sort.md "edit.link.title")  
>  __本页面贡献者：[NachtgeistW](https://github.com/NachtgeistW), [iamtwz](https://github.com/iamtwz), [Junyan721113](https://github.com/Junyan721113), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [ksyx](https://github.com/ksyx), [mcendu](https://github.com/mcendu), [Menci](https://github.com/Menci), [ouuan](https://github.com/ouuan), [partychicken](https://github.com/partychicken), [shawlleyw](https://github.com/shawlleyw), [tfia](https://github.com/tfia), [TrickEye](https://github.com/TrickEye), [WException](https://github.com/WException), [ZbohZbp](https://github.com/ZbohZbp)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
