# 插入排序 - OI Wiki

- Source: https://oi-wiki.org/basic/insertion-sort/

# 插入排序

本页面将简要介绍插入排序．

## 定义

插入排序（英语：Insertion sort）是一种简单直观的排序算法．它的工作原理为将待排列元素划分为「已排序」和「未排序」两部分，每次从「未排序的」元素中选择一个插入到「已排序的」元素中的正确位置．

一个与插入排序相同的操作是打扑克牌时，从牌桌上抓一张牌，按牌面大小插到手牌后，再抓下一张牌．

![insertion sort animate example](./images/insertion-sort-animate.svg)

## 性质

### 稳定性

插入排序是一种稳定的排序算法．

### 时间复杂度

插入排序的最优时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在数列几乎有序时效率很高．

插入排序的最坏时间复杂度和平均时间复杂度都为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 代码实现

### 伪代码

1𝐈𝐧𝐩𝐮𝐭. An array 𝐴 consisting of 𝑛 elements.2𝐎𝐮𝐭𝐩𝐮𝐭. 𝐴 will be sorted in nondecreasing order stably.3𝐌𝐞𝐭𝐡𝐨𝐝. 4𝐟𝐨𝐫 𝑖←2 𝐭𝐨 𝑛5𝑘𝑒𝑦←𝐴[𝑖]6𝑗←𝑖−17𝐰𝐡𝐢𝐥𝐞 𝑗>0 𝐚𝐧𝐝 𝐴[𝑗]>𝑘𝑒𝑦8𝐴[𝑗+1]←𝐴[𝑗]9𝑗←𝑗−110𝐴[𝑗+1]←𝑘𝑒𝑦1Input. An array A consisting of n elements.2Output. A will be sorted in nondecreasing order stably.3Method. 4for i←2 to n5key←A[i]6j←i−17while j>0 and A[j]>key8A[j+1]←A[j]9j←j−110A[j+1]←key![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

C++PythonJava

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text void insertion_sort ( int arr [], int len ) { for ( int i = 1 ; i < len ; ++ i ) { int key = arr [ i ]; int j = i \- 1 ; while ( j >= 0 && arr [ j ] > key ) { arr [ j \+ 1 ] = arr [ j ]; j \-- ; } arr [ j \+ 1 ] = key ; } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text def insertion_sort ( arr , n ): for i in range ( 1 , n ): key = arr [ i ] j = i \- 1 while j >= 0 and arr [ j ] > key : arr [ j \+ 1 ] = arr [ j ] j -= 1 arr [ j \+ 1 ] = key ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text public static void insertionSort ( int [] arr ) { for ( int i = 1 ; i < arr . length ; i ++ ) { int key = arr [ i ] ; int j = i \- 1 ; while ( j >= 0 && arr [ j ] > key ) { arr [ j \+ 1 ] = arr [ j ] ; j \-- ; } arr [ j \+ 1 ] = key ; } } ```   
---|---  
  
## 折半插入排序

插入排序还可以通过二分算法优化性能，在排序元素数量较多时优化的效果比较明显．

### 时间复杂度

折半插入排序与直接插入排序的基本思想是一致的，折半插入排序仅对插入排序时间复杂度中的常数进行了优化，所以优化后的时间复杂度仍然不变．

### 代码实现

C++

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text void insertion_sort ( int arr [], int len ) { if ( len < 2 ) return ; for ( int i = 1 ; i != len ; ++ i ) { int key = arr [ i ]; auto index = upper_bound ( arr , arr \+ i , key ) \- arr ; // 使用 memmove 移动元素，比使用 for 循环速度更快，时间复杂度仍为 O(n) memmove ( arr \+ index \+ 1 , arr \+ index , ( i \- index ) * sizeof ( int )); arr [ index ] = key ; } } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/insertion-sort.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/insertion-sort.md "edit.link.title")  
>  __本页面贡献者：[NachtgeistW](https://github.com/NachtgeistW), [H-J-Granger](https://github.com/H-J-Granger), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [Junyan721113](https://github.com/Junyan721113), [Konano](https://github.com/Konano), [Tiphereth-A](https://github.com/Tiphereth-A), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [AprilNEA](https://github.com/AprilNEA), [c-forrest](https://github.com/c-forrest), [clee01](https://github.com/clee01), [EmptyDreams](https://github.com/EmptyDreams), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Great-designer](https://github.com/Great-designer), [hsfzLZH1](https://github.com/hsfzLZH1), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [mcendu](https://github.com/mcendu), [Menci](https://github.com/Menci), [Molly166](https://github.com/Molly166), [ouuan](https://github.com/ouuan), [partychicken](https://github.com/partychicken), [Peanut-Tang](https://github.com/Peanut-Tang), [shawlleyw](https://github.com/shawlleyw), [SukkaW](https://github.com/SukkaW), [thy233](https://github.com/thy233), [TrickEye](https://github.com/TrickEye), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
