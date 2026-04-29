# 块状数组 - OI Wiki

- Source: https://oi-wiki.org/ds/block-array/

# 块状数组

## 建立块状数组

块状数组，即把一个数组分为几个块，块内信息整体保存，若查询时遇到两边不完整的块直接暴力查询．一般情况下，块的长度为 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．详细分析可以阅读 2017 年国家集训队论文中徐明宽的《非常规大小分块算法初探》．

下面直接给出一种建立块状数组的代码．

实现

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text num = sqrt ( n ); for ( int i = 1 ; i <= num ; i ++ ) st [ i ] = n / num * ( i \- 1 ) \+ 1 , ed [ i ] = n / num * i ; ed [ num ] = n ; for ( int i = 1 ; i <= num ; i ++ ) { for ( int j = st [ i ]; j <= ed [ i ]; j ++ ) { belong [ j ] = i ; } size [ i ] = ed [ i ] \- st [ i ] \+ 1 ; } ```   
---|---  
  
其中 `st[i]` 和 `ed[i]` 为块的起点和终点，`size[i]` 为块的大小．

## 保存与修改块内信息

### 例题 1：[教主的魔法](https://www.luogu.com.cn/problem/P2801)

两种操作：

  1. 区间 [𝑥,𝑦][x,y]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 每个数都加上 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 查询区间 [𝑥,𝑦][x,y]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内大于等于 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数的个数．

我们要询问一个块内大于等于一个数的数的个数，所以需要一个 `t` 数组对块内排序，`a` 为原来的（未被排序的）数组．对于整块的修改，使用类似于标记永久化的方式，用 `delta` 数组记录现在块内整体加上的值．设 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为查询和修改的操作次数总和，则时间复杂度 𝑂(𝑞√𝑛log⁡𝑛)O(qnlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

用 `delta` 数组记录每个块的整体赋值情况．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` |  ```text void Sort ( int k ) { for ( int i = st [ k ]; i <= ed [ k ]; i ++ ) t [ i ] = a [ i ]; sort ( t \+ st [ k ], t \+ ed [ k ] \+ 1 ); } void Modify ( int l , int r , int c ) { int x = belong [ l ], y = belong [ r ]; if ( x == y ) // 区间在一个块内就直接修改 { for ( int i = l ; i <= r ; i ++ ) a [ i ] += c ; Sort ( x ); return ; } for ( int i = l ; i <= ed [ x ]; i ++ ) a [ i ] += c ; // 直接修改起始段 for ( int i = st [ y ]; i <= r ; i ++ ) a [ i ] += c ; // 直接修改结束段 for ( int i = x \+ 1 ; i < y ; i ++ ) delta [ i ] += c ; // 中间的块整体打上标记 Sort ( x ); Sort ( y ); } int Answer ( int l , int r , int c ) { int ans = 0 , x = belong [ l ], y = belong [ r ]; if ( x == y ) { for ( int i = l ; i <= r ; i ++ ) if ( a [ i ] \+ delta [ x ] >= c ) ans ++ ; return ans ; } for ( int i = l ; i <= ed [ x ]; i ++ ) if ( a [ i ] \+ delta [ x ] >= c ) ans ++ ; for ( int i = st [ y ]; i <= r ; i ++ ) if ( a [ i ] \+ delta [ y ] >= c ) ans ++ ; for ( int i = x \+ 1 ; i <= y \- 1 ; i ++ ) ans += ed [ i ] \- ( lower_bound ( t \+ st [ i ], t \+ ed [ i ] \+ 1 , c \- delta [ i ]) \- t ) \+ 1 ; // 用 lower_bound 找出中间每一个整块中第一个大于等于 c 的数的位置 return ans ; } ```   
---|---  
  
### 例题 2：寒夜方舟

两种操作：

  1. 区间 [𝑥,𝑦][x,y]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 每个数都变成 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 查询区间 [𝑥,𝑦][x,y]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内小于等于 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数的个数．

用 `delta` 数组记录现在块内被整体赋值为何值．当该块未被整体赋值时，用一个特殊值（如 `0x3f3f3f3f3f3f3f3fll`）加以表示．对于边角块，查询前要 `pushdown`，把块内存的信息下放到每一个数上．赋值之后记得重新 `sort` 一遍．其他方面同上题．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 ``` |  ```text void Sort ( int k ) { for ( int i = st [ k ]; i <= ed [ k ]; i ++ ) t [ i ] = a [ i ]; sort ( t \+ st [ k ], t \+ ed [ k ] \+ 1 ); } void PushDown ( int x ) { if ( delta [ x ] != 0x3f3f3f3f3f3f3f3fll ) // 用该值标记块内没有被整体赋值 for ( int i = st [ x ]; i <= ed [ x ]; i ++ ) a [ i ] = t [ i ] = delta [ x ]; delta [ x ] = 0x3f3f3f3f3f3f3f3fll ; } void Modify ( int l , int r , int c ) { int x = belong [ l ], y = belong [ r ]; PushDown ( x ); if ( x == y ) { for ( int i = l ; i <= r ; i ++ ) a [ i ] = c ; Sort ( x ); return ; } PushDown ( y ); for ( int i = l ; i <= ed [ x ]; i ++ ) a [ i ] = c ; for ( int i = st [ y ]; i <= r ; i ++ ) a [ i ] = c ; Sort ( x ); Sort ( y ); for ( int i = x \+ 1 ; i < y ; i ++ ) delta [ i ] = c ; } int Binary_Search ( int l , int r , int c ) { int ans = l \- 1 , mid ; while ( l <= r ) { mid = ( l \+ r ) / 2 ; if ( t [ mid ] <= c ) ans = mid , l = mid \+ 1 ; else r = mid \- 1 ; } return ans ; } int Answer ( int l , int r , int c ) { int ans = 0 , x = belong [ l ], y = belong [ r ]; PushDown ( x ); if ( x == y ) { for ( int i = l ; i <= r ; i ++ ) if ( a [ i ] <= c ) ans ++ ; return ans ; } PushDown ( y ); for ( int i = l ; i <= ed [ x ]; i ++ ) if ( a [ i ] <= c ) ans ++ ; for ( int i = st [ y ]; i <= r ; i ++ ) if ( a [ i ] <= c ) ans ++ ; for ( int i = x \+ 1 ; i <= y \- 1 ; i ++ ) { if ( 0x3f3f3f3f3f3f3f3fll == delta [ i ]) ans += Binary_Search ( st [ i ], ed [ i ], c ) \- st [ i ] \+ 1 ; else if ( delta [ i ] <= c ) ans += size [ i ]; } return ans ; } ```   
---|---  
  
## 练习

  1. [单点修改，区间查询](https://loj.ac/problem/130)
  2. [区间修改，区间查询](https://loj.ac/problem/132)
  3. [【模板】线段树 2](https://www.luogu.com.cn/problem/P3373)
  4. [「Ynoi2019 模拟赛」Yuno loves sqrt technology III](https://www.luogu.com.cn/problem/P5048)
  5. [「Violet」蒲公英](https://www.luogu.com.cn/problem/P4168)
  6. [作诗](https://www.luogu.com.cn/problem/P4135)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/block-array.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/block-array.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [R-G-Mocoratioen](https://github.com/R-G-Mocoratioen), [Enter-tainer](https://github.com/Enter-tainer), [Henry-ZHR](https://github.com/Henry-ZHR), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [Alpacabla](https://github.com/Alpacabla), [chenyanlann](https://github.com/chenyanlann), [iamtwz](https://github.com/iamtwz), [Marcythm](https://github.com/Marcythm), [partychicken](https://github.com/partychicken), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [zhuzeyu22](https://github.com/zhuzeyu22)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
