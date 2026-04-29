# 枚举 - OI Wiki

- Source: https://oi-wiki.org/basic/enumerate/

# 枚举

本页面将简要介绍枚举算法．

## 简介

枚举（英语：Enumerate）是基于已有知识来猜测答案的一种问题求解策略．

枚举的思想是不断地猜测，从可能的集合中一一尝试，然后再判断题目的条件是否成立．

## 要点

### 给出解空间

建立简洁的数学模型．

枚举的时候要想清楚：可能的情况是什么？要枚举哪些要素？

### 减少枚举的空间

枚举的范围是什么？是所有的内容都需要枚举吗？

在用枚举法解决问题的时候，一定要想清楚这两件事，否则会带来不必要的时间开销．

### 选择合适的枚举顺序

根据题目判断．比如例题中要求的是最大的符合条件的素数，那自然是从大到小枚举比较合适．

## 例题

以下是一个使用枚举解题与优化枚举范围的例子．

例题

给定一个数组，其所有元素互不相同且均不为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．求该数组中和为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数对个数．

解题思路

枚举两个数的代码很容易就可以写出来．

C++PythonJava

```text 1 2 3 ``` |  ```text for ( int i = 0 ; i < n ; ++ i ) for ( int j = 0 ; j < n ; ++ j ) if ( a [ i ] \+ a [ j ] == 0 ) ++ ans ; ```   
---|---  
  
```text 1 2 3 4 ``` |  ```text for i in range ( n ): for j in range ( n ): if a [ i ] \+ a [ j ] == 0 : ans += 1 ```   
---|---  
  
```text 1 2 3 ``` |  ```text for ( int i = 0 ; i < n ; ++ i ) for ( int j = 0 ; j < n ; ++ j ) if ( a [ i ] \+ a [ j ] == 0 ) ++ ans ; ```   
---|---  
  
来看看枚举的范围如何优化．由于题中没要求数对是有序的，答案就是有序的情况的两倍（考虑如果 `(a, b)` 是答案，那么 `(b, a)` 也是答案）．对于这种情况，只需统计人为要求有顺序之后的答案，最后再乘上 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就好了．

不妨要求第一个数要出现在靠后的位置．代码如下：

C++PythonJava

```text 1 2 3 4 ``` |  ```text for ( int i = 0 ; i < n ; ++ i ) for ( int j = 0 ; j < i ; ++ j ) if ( a [ i ] \+ a [ j ] == 0 ) ++ ans ; ans *= 2 ; ```   
---|---  
  
```text 1 2 3 4 5 ``` |  ```text for i in range ( n ): for j in range ( i ): if a [ i ] \+ a [ j ] == 0 : ans += 1 ans *= 2 ```   
---|---  
  
```text 1 2 3 4 ``` |  ```text for ( int i = 0 ; i < n ; ++ i ) for ( int j = 0 ; j < i ; ++ j ) if ( a [ i ] \+ a [ j ] == 0 ) ++ ans ; ans *= 2 ; ```   
---|---  
  
不难发现这里已经减少了 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的枚举范围，减少了这段代码的时间开销．

我们可以在此之上进一步优化．

两个数是否都一定要枚举出来呢？枚举其中一个数之后，题目的条件已经确定了其他的要素（另一个数）的条件，如果能找到一种方法直接判断题目要求的那个数是否存在，就可以省掉枚举后一个数的时间了．较为进阶地，在数据范围允许的情况下，我们可以使用桶1记录遍历过的数．

C++PythonJava

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text #include <cstring> constexpr int MAXN = 100000 ; // 此处 MAXN 是数组内元素的界 int solve ( int n , int a []) { bool met [ MAXN * 2 \+ 1 ]; // 创建一个能装下 [-MAXN, MAXN] 的桶 memset ( met , 0 , sizeof ( met )); int ans = 0 ; for ( int i = 0 ; i < n ; ++ i ) { if ( met [ MAXN \- a [ i ]]) ++ ans ; // 如果桶内有想要的元素，答案加一 met [ MAXN \+ a [ i ]] = true ; // 无论如何，都要把当前元素放进桶里 } return ans * 2 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 ``` |  ```text met = [ False ] * ( MAXN * 2 \+ 1 ) for i in range ( n ): if met [ MAXN \- a [ i ]]: ans += 1 met [ a [ i ] \+ MAXN ] = True ans *= 2 ```   
---|---  
  
```text 1 2 3 4 5 6 ``` |  ```text boolean [] met = new boolean [ MAXN * 2 \+ 1 ] ; for ( int i = 0 ; i < n ; ++ i ) { if ( met [ MAXN \- a [ i ]] ) ++ ans ; met [ MAXN \+ a [ i ]] = true ; } ans *= 2 ; ```   
---|---  
  
### 复杂度分析

  * 时间复杂度分析：对 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组遍历了一遍就能完成题目要求，当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 足够大的时候时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 空间复杂度分析：𝑂(𝑛 +max{|𝑥| :𝑥 ∈𝑎})O(n+max{|x|:x∈a})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 习题

  * [2811: 熄灯问题 - OpenJudge](http://bailian.openjudge.cn/practice/2811/)

## 脚注

* * *

  1. [桶排序](../bucket-sort/) 以及 [主元素问题](../../misc/main-element/#离线算法) 以及 [Stack Overflow 上对桶数据结构的讲解](https://stackoverflow.com/questions/42399355/what-is-a-bucket-or-double-bucket-data-structure)（英文） ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/enumerate.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/enumerate.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Ir1d](https://github.com/Ir1d), [frank-xjh](https://github.com/frank-xjh), [NachtgeistW](https://github.com/NachtgeistW), [Xeonacid](https://github.com/Xeonacid), [Enter-tainer](https://github.com/Enter-tainer), [HeRaNO](https://github.com/HeRaNO), [ksyx](https://github.com/ksyx), [shuzhouliu](https://github.com/shuzhouliu), [c-forrest](https://github.com/c-forrest), [CamberLoid](https://github.com/CamberLoid), [CCXXXI](https://github.com/CCXXXI), [Ciutto](https://github.com/Ciutto), [Early0v0](https://github.com/Early0v0), [Great-designer](https://github.com/Great-designer), [he-zhiyuan](https://github.com/he-zhiyuan), [hoseahsu](https://github.com/hoseahsu), [iamtwz](https://github.com/iamtwz), [LeiJinpeng](https://github.com/LeiJinpeng), [Menci](https://github.com/Menci), [Planet6174](https://github.com/Planet6174), [qiqistyle](https://github.com/qiqistyle), [ryze](mailto:42087725+ryze-borgia@users.noreply.github.com), [Saisyc](https://github.com/Saisyc), [ScrapW](https://github.com/ScrapW), [shawlleyw](https://github.com/shawlleyw), [sshwy](https://github.com/sshwy), [tinjyu](https://github.com/tinjyu), [TrickEye](https://github.com/TrickEye), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [xyf007](https://github.com/xyf007)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
