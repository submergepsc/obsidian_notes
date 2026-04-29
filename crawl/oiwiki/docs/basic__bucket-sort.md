# 桶排序 - OI Wiki

- Source: https://oi-wiki.org/basic/bucket-sort/

# 桶排序

本页面将简要介绍桶排序．

## 定义

桶排序（英文：Bucket sort）是排序算法的一种，适用于待排序数据值域较大但分布比较均匀的情况．

## 过程

桶排序按下列步骤进行：

  1. 设置一个定量的数组当作空桶；
  2. 遍历序列，并将元素一个个放到对应的桶中；
  3. 对每个不是空的桶进行排序；
  4. 从不是空的桶里把元素再放回原来的序列中．

## 性质

### 稳定性

如果使用稳定的内层排序，并且将元素插入桶中时不改变元素间的相对顺序，那么桶排序就是一种稳定的排序算法．

由于每块元素不多，一般使用插入排序．此时桶排序是一种稳定的排序算法．

### 时间复杂度

桶排序的平均时间复杂度为 𝑂(𝑛 +𝑛2/𝑘 +𝑘)O(n+n2/k+k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（将值域平均分成 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块 + 排序 + 重新合并元素），当 𝑘 ≈𝑛k≈n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．1

桶排序的最坏时间复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ``` |  ```text constexpr int N = 100010 ; int n , w , a [ N ]; vector < int > bucket [ N ]; void insertion_sort ( vector < int >& A ) { for ( int i = 1 ; i < A . size (); ++ i ) { int key = A [ i ]; int j = i \- 1 ; while ( j >= 0 && A [ j ] > key ) { A [ j \+ 1 ] = A [ j ]; \-- j ; } A [ j \+ 1 ] = key ; } } void bucket_sort () { int bucket_size = w / n \+ 1 ; for ( int i = 0 ; i < n ; ++ i ) { bucket [ i ]. clear (); } for ( int i = 1 ; i <= n ; ++ i ) { bucket [ a [ i ] / bucket_size ]. push_back ( a [ i ]); } int p = 0 ; for ( int i = 0 ; i < n ; ++ i ) { insertion_sort ( bucket [ i ]); for ( int j = 0 ; j < bucket [ i ]. size (); ++ j ) { a [ ++ p ] = bucket [ i ][ j ]; } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` |  ```text N = 100010 w = n = 0 a = [ 0 ] * N bucket = [[] for i in range ( N )] def insertion_sort ( A ): for i in range ( 1 , len ( A )): key = A [ i ] j = i \- 1 while j >= 0 and A [ j ] > key : A [ j \+ 1 ] = A [ j ] j -= 1 A [ j \+ 1 ] = key def bucket_sort (): bucket_size = int ( w / n \+ 1 ) for i in range ( 0 , n ): bucket [ i ] . clear () for i in range ( 1 , n \+ 1 ): bucket [ int ( a [ i ] / bucket_size )] . append ( a [ i ]) p = 0 for i in range ( 0 , n ): insertion_sort ( bucket [ i ]) for j in range ( 0 , len ( bucket [ i ])): a [ p ] = bucket [ i ][ j ] p += 1 ```   
---|---  
  
## 参考资料与注释

* * *

  1. [（英文）Bucket sort - Wikipedia](https://en.wikipedia.org/wiki/Bucket_sort#Average-case_analysis) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/bucket-sort.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/bucket-sort.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [Marcythm](https://github.com/Marcythm), [NachtgeistW](https://github.com/NachtgeistW), [iamtwz](https://github.com/iamtwz), [ouuan](https://github.com/ouuan), [Tiphereth-A](https://github.com/Tiphereth-A), [Menci](https://github.com/Menci), [partychicken](https://github.com/partychicken), [shawlleyw](https://github.com/shawlleyw), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
