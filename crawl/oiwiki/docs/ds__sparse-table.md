# ST 表 - OI Wiki

- Source: https://oi-wiki.org/ds/sparse-table/

# ST 表

## 定义

![ST 表示意图](./images/st.svg)

ST 表（Sparse Table，稀疏表）是用于解决 **可重复贡献问题** 的数据结构．

什么是可重复贡献问题？

**可重复贡献问题** 是指对于运算 optopt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 𝑥opt⁡𝑥 =𝑥xopt⁡x=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对应的区间询问就是一个可重复贡献问题．例如，最大值有 max(𝑥,𝑥) =𝑥max(x,x)=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，gcd 有 gcd⁡(𝑥,𝑥) =𝑥gcd⁡(x,x)=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 RMQ 和区间 GCD 就是一个可重复贡献问题．像区间和就不具有这个性质，如果求区间和的时候采用的预处理区间重叠了，则会导致重叠部分被计算两次，这是我们所不愿意看到的．另外，optopt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还必须满足结合律才能使用 ST 表求解．

什么是 RMQ？

RMQ 是英文 Range Maximum/Minimum Query 的缩写，表示区间最大（最小）值．解决 RMQ 问题有很多种方法，可以参考 [RMQ 专题](../../topic/rmq/)．

## 引入

[Luogu P3865【模板】ST 表 & RMQ 问题](https://www.luogu.com.cn/problem/P3865)

给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（1 ≤𝑛 ≤1051≤n≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）个整数，有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（1 ≤𝑚 ≤2 ×1061≤m≤2×106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）个询问，对于每个询问，你需要回答区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的最大值．

考虑暴力做法．每次都对区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 扫描一遍，求出最大值．

显然，这个算法会超时．

## ST 表

ST 表基于 [倍增](../../basic/binary-lifting/) 思想，可以做到 Θ(𝑛log⁡𝑛)Θ(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 预处理，Θ(1)Θ(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 回答每个询问．但是不支持修改操作．

基于倍增思想，我们考虑如何求出区间最大值．可以发现，如果按照一般的倍增流程，每次跳 2𝑖2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步的话，询问时的复杂度仍旧是 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并没有比线段树更优，反而预处理一步还比线段树慢．

我们发现 max(𝑥,𝑥) =𝑥max(x,x)=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，区间最大值是一个具有「可重复贡献」性质的问题．即使用来求解的预处理区间有重叠部分，只要这些区间的并是所求的区间，最终计算出的答案就是正确的．

如果手动模拟一下，可以发现我们能使用至多两个预处理过的区间来覆盖询问区间，也就是说询问时的时间复杂度可以被降至 Θ(1)Θ(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在处理有大量询问的题目时十分有效．

具体实现如下：

令 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示区间 [𝑖,𝑖 +2𝑗 −1][i,i+2j−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大值．

显然 𝑓(𝑖,0) =𝑎𝑖f(i,0)=ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

根据定义式，第二维就相当于倍增的时候「跳了 2𝑗 −12j−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步」，依据倍增的思路，写出状态转移方程：𝑓(𝑖,𝑗) =max(𝑓(𝑖,𝑗 −1),𝑓(𝑖 +2𝑗−1,𝑗 −1))f(i,j)=max(f(i,j−1),f(i+2j−1,j−1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

![](./images/st-preprocess-lift.svg)

以上就是预处理部分．而对于查询，可以简单实现如下：

对于每个询问 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们把它分成两部分：[𝑙,𝑙 +2𝑠 −1][l,l+2s−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 [𝑟 −2𝑠 +1,𝑟][r−2s+1,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑠 =⌊log2⁡(𝑟−𝑙+1)⌋s=⌊log2⁡(r−l+1)⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．两部分的结果的最大值就是回答．

![ST 表的查询过程](./images/st-query.svg)

根据上面对于「可重复贡献问题」的论证，由于最大值是「可重复贡献问题」，重叠并不会对区间最大值产生影响．又因为这两个区间完全覆盖了 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以保证答案的正确性．

[Luogu P3865【模板】ST 表 & RMQ 问题](https://www.luogu.com.cn/problem/P3865) 参考实现

C 风格C++ 风格Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``` |  ```text #include <algorithm> #include <iostream> using namespace std ; constexpr int N = 100000 \+ 5 ; constexpr int logN = 16 ; // ⌊ log_2 N ⌋ int f [ logN \+ 1 ][ N ], Logn [ N ]; // 初始化对数值 void pre () { Logn [ 2 ] = 1 ; for ( int i = 3 ; i < N ; i ++ ) { Logn [ i ] = Logn [ i / 2 ] \+ 1 ; } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); pre (); int n , m ; cin >> n >> m ; for ( int i = 1 ; i <= n ; i ++ ) cin >> f [ 0 ][ i ]; for ( int j = 1 ; j <= logN ; j ++ ) for ( int i = 1 ; i \+ ( 1 << j ) \- 1 <= n ; i ++ ) f [ j ][ i ] = max ( f [ j \- 1 ][ i ], f [ j \- 1 ][ i \+ ( 1 << ( j \- 1 ))]); // ST表具体实现 for ( int i = 1 ; i <= m ; i ++ ) { int x , y ; cin >> x >> y ; int s = Logn [ y \- x \+ 1 ]; cout << max ( f [ s ][ x ], f [ s ][ y \- ( 1 << s ) \+ 1 ]) << '\n' ; } return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 ``` |  ```text #include <algorithm> #include <functional> #include <iostream> #include <vector> #if defined(_MSC_VER) && !defined(__clang__) #include <immintrin.h> #define __builtin_clz _lzcnt_u32 #endif using namespace std ; // 使用内建函数计算 ⌊ log_2 x ⌋ int lg2 ( int x ) { return 31 \- __builtin_clz ( x ); } template < typename T > class SparseTable { using VT = vector < T > ; using VVT = vector < VT > ; using func_type = function < T ( const T & , const T & ) > ; VVT ST ; static T default_func ( const T & t1 , const T & t2 ) { return max ( t1 , t2 ); } func_type op ; public : SparseTable ( const vector < T > & v , func_type _func = default_func ) { op = _func ; int n = v . size (), l = lg2 ( n ); ST . assign ( l \+ 1 , VT ( n , 0 )); for ( int i = 0 ; i < n ; ++ i ) { ST [ 0 ][ i ] = v [ i ]; } for ( int j = 1 ; j <= l ; ++ j ) { for ( int i = 0 ; i \+ ( 1 << j ) <= n ; ++ i ) { ST [ j ][ i ] = op ( ST [ j \- 1 ][ i ], ST [ j \- 1 ][ i \+ ( 1 << ( j \- 1 ))]); } } } T query ( int l , int r ) { int q = lg2 ( r \- l \+ 1 ); return op ( ST [ q ][ l ], ST [ q ][ r \- ( 1 << q ) \+ 1 ]); } }; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int n , m ; cin >> n >> m ; vector < int > a ( n ); for ( int & i : a ) cin >> i ; SparseTable < int > st ( a ); for ( int i = 1 ; i <= m ; ++ i ) { int x , y ; cin >> x >> y ; cout << st . query ( x \- 1 , y \- 1 ) << '\n' ; } return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` |  ```text import sys input = sys . stdin . readline class SparseTable : def __init__ ( self , arr : list , func = min ): self . func = func self . n = len ( arr ) self . log = [ 0 ] * ( self . n \+ 1 ) for i in range ( 2 , self . n \+ 1 ): self . log [ i ] = self . log [ i // 2 ] \+ 1 self . k = self . log [ self . n ] self . st = [[ 0 ] * ( self . n ) for _ in range ( self . k \+ 1 )] self . st [ 0 ] = arr for j in range ( 1 , self . k \+ 1 ): i = 0 while i \+ ( 1 << j ) <= self . n : self . st [ j ][ i ] = self . func ( self . st [ j \- 1 ][ i ], self . st [ j \- 1 ][ i \+ ( 1 << ( j \- 1 ))] ) i += 1 def query ( self , left : int , right : int ): j = self . log [ right \- left \+ 1 ] return self . func ( self . st [ j ][ left ], self . st [ j ][ right \- ( 1 << j ) \+ 1 ]) n , m = map ( int , input () . split ()) a = list ( map ( int , input () . split ())) st = SparseTable ( a , max ) for _ in range ( m ): left , right = map ( int , input () . split ()) print ( st . query ( left \- 1 , right \- 1 )) ```   
---|---  
  
## 注意点

  1. 输入输出数据一般很多，建议开启输入输出优化．

  2. 在预处理 ST 表时通常需要建立一个一维大小为 log⁡𝑛log⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，另一维大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数组，此时应优先让大小为 log⁡𝑛log⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的维度作为第一维，以提升缓存局部性．

  3. 每次用 [std::log](https://en.cppreference.com/w/cpp/numeric/math/log) 重新计算对数函数值并不值得，建议利用 `__builtin_clz` 或 `__lg` 等内建函数进行计算．如无法利用这些内建函数，也可以预处理对数函数值．预处理方式如下所示：

{𝙻𝚘𝚐𝚗[1]←0,𝙻𝚘𝚐𝚗[𝑖]←𝙻𝚘𝚐𝚗[𝑖2]+1.{Logn[1]←0,Logn[i]←Logn[i2]+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## ST 表维护其他信息

除 RMQ 以外，还有其它的「可重复贡献问题」．例如「区间按位与」、「区间按位或」、「区间 GCD」，ST 表都能高效地解决．

需要注意的是，对于「区间 GCD」，ST 表的查询复杂度并没有比线段树更优（令值域为 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，ST 表的查询复杂度为 Θ(log⁡𝑤)Θ(log⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而线段树为 Θ(log⁡𝑛 +log⁡𝑤)Θ(log⁡n+log⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且值域一般是大于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的），但是 ST 表的预处理复杂度也没有比线段树更劣，而编程复杂度方面 ST 表比线段树简单很多．

如果分析一下，「可重复贡献问题」一般都带有某种类似 RMQ 的成分．例如「区间按位与」就是每一位取最小值，而「区间 GCD」则是每一个质因数的指数取最小值．

## 总结

ST 表能较好的维护「可重复贡献」的区间信息（同时也应满足结合律），时间复杂度较低，代码量相对其他算法很小．但是，ST 表能维护的信息非常有限，不能较好地扩展，并且不支持修改操作．

## 习题

  * [「SCOI2007」降雨量](https://loj.ac/p/2279)

  * [[USACO07JAN] 平衡的阵容 Balanced Lineup](https://www.luogu.com.cn/problem/P2880)

## 附录：ST 表求区间 GCD 的时间复杂度分析

在算法运行的时候，可能要经过 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次迭代．每一次迭代都可能会使用 GCD 函数进行递归，令值域为 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，GCD 函数的时间复杂度最高是 Ω(log⁡𝑤)Ω(log⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，所以总时间复杂度看似有 𝑂(𝑛log⁡𝑛log⁡𝑤)O(nlog⁡nlog⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

但是，在 GCD 的过程中，每一次递归（除最后一次递归之外）都会使数列中的某个数至少减半，而数列中的数最多减半的次数为 log2⁡(𝑤𝑛) =Θ(𝑛log⁡𝑤)log2⁡(wn)=Θ(nlog⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，GCD 的递归部分最多只会运行 𝑂(𝑛log⁡𝑤)O(nlog⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．再加上循环部分（以及最后一层递归）的 Θ(𝑛log⁡𝑛)Θ(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最终时间复杂度则是 𝑂(𝑛(log⁡𝑤 +log⁡𝑛))O(n(log⁡w+log⁡n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由于可以构造数据使得时间复杂度为 Ω(𝑛(log⁡𝑤 +log⁡𝑛))Ω(n(log⁡w+log⁡n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以最终的时间复杂度即为 Θ(𝑛(log⁡𝑤 +log⁡𝑛))Θ(n(log⁡w+log⁡n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

而查询部分的时间复杂度很好分析，考虑最劣情况，即每次询问都询问最劣的一对数，时间复杂度为 Θ(log⁡𝑤)Θ(log⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，ST 表维护「区间 GCD」的时间复杂度为预处理 Θ(𝑛(log⁡𝑛 +log⁡𝑤))Θ(n(log⁡n+log⁡w))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，单次查询 Θ(log⁡𝑤)Θ(log⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

线段树的相应操作是预处理 Θ(𝑛log⁡𝑤)Θ(nlog⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，单次查询 Θ(log⁡𝑛 +log⁡𝑤)Θ(log⁡n+log⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这并不是一个严谨的数学论证，更为严谨的附在下方：

更严谨的证明

理解本段，可能需要具备 [时间复杂度](../../basic/complexity/) 的关于「势能分析法」的知识．

先分析预处理部分的时间复杂度：

设「待考虑数列」为在预处理 ST 表的时候当前层循环的数列．例如，第零层的数列就是原数列，第一层的数列就是第零层的数列经过一次迭代之后的数列，即 `st[1..n][1]`，我们将其记为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

而势能函数就定义为「待考虑数列」中所有数的累乘的以二为底的对数．即：Φ(𝐴) =log2⁡(𝑛∏𝑖=1𝐴𝑖)Φ(A)=log2⁡(∏i=1nAi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在一次迭代中，所花费的时间相当于迭代循环所花费的时间与 GCD 所花费的时间之和．其中，GCD 花费的时间有长有短．最短可能只有两次甚至一次递归，而最长可能有 𝑂(log⁡𝑤)O(log⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次递归．但是，GCD 过程中，除最开头一层与最末一层以外，每次递归都会使「待考虑数列」中的某个结果至少减半．即，Φ(𝐴)Φ(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 会减少至少 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，该层递归所用的时间可以被势能函数均摊．

同时，我们可以看到，Φ(𝐴)Φ(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的初值最大为 log2⁡(𝑤𝑛) =Θ(𝑛log⁡𝑤)log2⁡(wn)=Θ(nlog⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 Φ(𝐴)Φ(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不增．所以，ST 表预处理部分的时间复杂度为 𝑂(𝑛(log⁡𝑤 +log⁡𝑛))O(n(log⁡w+log⁡n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/sparse-table.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/sparse-table.md "edit.link.title")  
>  __本页面贡献者：[orzAtalod](https://github.com/orzAtalod), [ouuan](mailto:1609483441@qq.com), [Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [Xeonacid](https://github.com/Xeonacid), [abc1763613206](https://github.com/abc1763613206), [CCXXXI](https://github.com/CCXXXI), [Enter-tainer](https://github.com/Enter-tainer), [AngelKitty](https://github.com/AngelKitty), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Henry-ZHR](https://github.com/Henry-ZHR), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [ShadowsEpic](https://github.com/ShadowsEpic), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A), [weiyong1024](https://github.com/weiyong1024), [Backl1ght](https://github.com/Backl1ght), [c-forrest](https://github.com/c-forrest), [Chrogeek](https://github.com/Chrogeek), [DawnMagnet](https://github.com/DawnMagnet), [firogh](https://github.com/firogh), [Fomalhauthmj](https://github.com/Fomalhauthmj), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [hsfzLZH1](https://github.com/hsfzLZH1), [hsn8086](https://github.com/hsn8086), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lbdoknow](https://github.com/lbdoknow), [leoleoasd](https://github.com/leoleoasd), [lychees](https://github.com/lychees), [mcendu](https://github.com/mcendu), [MingqiHuang](mailto:hmq011212@163.com), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [purinliang](https://github.com/purinliang), [shuzhouliu](https://github.com/shuzhouliu), [Siger Young](mailto:siger-young@users.noreply.github.com), [SukkaW](https://github.com/SukkaW), [zymooll](https://github.com/zymooll)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
