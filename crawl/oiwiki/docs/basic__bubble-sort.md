# 冒泡排序 - OI Wiki

- Source: https://oi-wiki.org/basic/bubble-sort/

# 冒泡排序

本页面将简要介绍冒泡排序．

## 定义

冒泡排序（英语：Bubble sort）是一种简单的排序算法．由于在算法的执行过程中，较小的元素像是气泡般慢慢「浮」到数列的顶端，故叫做冒泡排序．

## 过程

它的工作原理是每次检查相邻两个元素，如果前面的元素与后面的元素满足给定的排序条件，就将相邻两个元素交换．当没有相邻的元素需要交换时，排序就完成了．

经过 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次扫描后，数列的末尾 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项必然是最大的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项，因此冒泡排序最多需要扫描 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍数组就能完成排序．

## 性质

### 稳定性

冒泡排序是一种稳定的排序算法．

### 时间复杂度

在序列完全有序时，冒泡排序只需遍历一遍数组，不用执行任何交换操作，时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在最坏情况下，冒泡排序要执行 (𝑛−1)𝑛2(n−1)n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次交换操作，时间复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

冒泡排序的平均时间复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 代码实现

### 伪代码

1𝐈𝐧𝐩𝐮𝐭. An array 𝐴 consisting of 𝑛 elements.2𝐎𝐮𝐭𝐩𝐮𝐭. 𝐴 will be sorted in nondecreasing order stably.3𝐌𝐞𝐭𝐡𝐨𝐝. 4𝑓𝑙𝑎𝑔←𝑇𝑟𝑢𝑒5𝐰𝐡𝐢𝐥𝐞 𝑓𝑙𝑎𝑔6𝑓𝑙𝑎𝑔←𝐹𝑎𝑙𝑠𝑒7𝐟𝐨𝐫 𝑖←1 𝐭𝐨 𝑛−18𝐢𝐟 𝐴[𝑖]>𝐴[𝑖+1]9𝑓𝑙𝑎𝑔←𝑇𝑟𝑢𝑒10Swap 𝐴[𝑖] and 𝐴[𝑖+1]1Input. An array A consisting of n elements.2Output. A will be sorted in nondecreasing order stably.3Method. 4flag←True5while flag6flag←False7for i←1 to n−18if A[i]>A[i+1]9flag←True10Swap A[i] and A[i+1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

C++PythonJava

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text // 假设数组的大小是 n + 1，冒泡排序从数组下标 1 开始 void bubble_sort ( int * a , int n ) { bool flag = true ; while ( flag ) { flag = false ; for ( int i = 1 ; i < n ; ++ i ) { if ( a [ i ] > a [ i \+ 1 ]) { flag = true ; int t = a [ i ]; a [ i ] = a [ i \+ 1 ]; a [ i \+ 1 ] = t ; } } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text def bubble_sort ( a , n ): flag = True while flag : flag = False for i in range ( 1 , n ): if a [ i ] > a [ i \+ 1 ]: flag = True a [ i ], a [ i \+ 1 ] = a [ i \+ 1 ], a [ i ] ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text // 假设数组的大小是 n + 1，冒泡排序从数组下标 1 开始 static void bubble_sort ( int [] a , int n ) { boolean flag = true ; while ( flag ) { flag = false ; for ( int i = 1 ; i < n ; i ++ ) { if ( a [ i ] > a [ i \+ 1 ] ) { flag = true ; int t = a [ i ] ; a [ i ] = a [ i \+ 1 ] ; a [ i \+ 1 ] = t ; } } } } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/bubble-sort.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/bubble-sort.md "edit.link.title")  
>  __本页面贡献者：[NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [iamtwz](https://github.com/iamtwz), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [mcendu](https://github.com/mcendu), [Menci](https://github.com/Menci), [partychicken](https://github.com/partychicken), [shawlleyw](https://github.com/shawlleyw), [TrickEye](https://github.com/TrickEye), [WException](https://github.com/WException), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
