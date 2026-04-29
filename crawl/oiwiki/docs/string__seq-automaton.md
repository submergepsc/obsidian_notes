# 序列自动机 - OI Wiki

- Source: https://oi-wiki.org/string/seq-automaton/

# 序列自动机

在阅读本文之前，请先阅读 [自动机](../../misc/fsm/)．

## 定义

序列自动机是接受且仅接受一个字符串的子序列的自动机．

本文中用 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代指这个字符串．

### 状态

若 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符，那么序列自动机包含 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个状态．

令 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个子序列，那么 𝛿(𝑠𝑡𝑎𝑟𝑡,𝑡)δ(start,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中第一次出现时末端的位置．

也就是说，一个状态 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示前缀 𝑠[1..𝑖]s[1..i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子序列与前缀 𝑠[1..𝑖 −1]s[1..i−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子序列的差集．

序列自动机上的所有状态都是接受状态．

### 转移

由状态定义可以得到，𝛿(𝑢,𝑐) =min{𝑖|𝑖 >𝑢,𝑠[𝑖] =𝑐}δ(u,c)=min{i|i>u,s[i]=c}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是字符 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下一次出现的位置．

为什么是「下一次」出现的位置呢？因为若 𝑖 >𝑗i>j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，后缀 𝑠[𝑖..|𝑠|]s[i..|s|]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子序列是后缀 𝑠[𝑗..|𝑠|]s[j..|s|]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子序列的子集，一定是选尽量靠前的最优．

## 实现

从后向前扫描，过程中维护每个字符最前的出现位置：

1𝐈𝐧𝐩𝐮𝐭. A string 𝑆2𝐎𝐮𝐭𝐩𝐮𝐭. The state transition of the sequence automaton of 𝑆3𝐌𝐞𝐭𝐡𝐨𝐝. 4𝐟𝐨𝐫 𝑐∈Σ5𝑛𝑒𝑥𝑡[𝑐]←𝑛𝑢𝑙𝑙6𝐟𝐨𝐫 𝑖←|𝑆| 𝐝𝐨𝐰𝐧𝐭𝐨 17𝑛𝑒𝑥𝑡[𝑆[𝑖]]←𝑖8𝐟𝐨𝐫 𝑐∈Σ9𝛿(𝑖−1,𝑐)←𝑛𝑒𝑥𝑡[𝑐]10𝐫𝐞𝐭𝐮𝐫𝐧 𝛿1Input. A string S2Output. The state transition of the sequence automaton of S3Method. 4for c∈Σ5next[c]←null6for i←|S| downto 17next[S[i]]←i8for c∈Σ9δ(i−1,c)←next[c]10return δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样构建的复杂度是 𝑂(𝑛|Σ|)O(n|Σ|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 例题

[「HEOI2015」最短不公共子串](https://loj.ac/problem/2123)

给你两个由小写英文字母组成的串 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（1 ≤|𝐴|,|𝐵| ≤20001≤|A|,|B|≤2000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），求：

  1. 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个最短的子串，它不是 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子串；
  2. 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个最短的子串，它不是 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子序列；
  3. 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个最短的子序列，它不是 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子串；
  4. 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个最短的子序列，它不是 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子序列．

题解

题目的 1 和 3 两问需要后缀自动机，而且做法类似，在这里只讲解 2 和 4 两问．

第 2 问比较简单，枚举 A 的子串输入进 B 的序列自动机，若不接受则计入答案．

第 4 问需要 DP．令 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示在 A 的序列自动机中处于状态 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在 B 的序列自动机中处于状态 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，需要再添加多少个字符能够不是公共子序列．状态转移方程为：

𝑓(𝑖,𝑗)=min𝛿𝐴(𝑖,𝑐)≠𝑛𝑢𝑙𝑙𝑓(𝛿𝐴(𝑖,𝑐),𝛿𝐵(𝑗,𝑐))+1.f(i,j)=minδA(i,c)≠nullf(δA(i,c),δB(j,c))+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

转移起点为 𝑓(𝑖,𝑛𝑢𝑙𝑙) =0f(i,null)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 ``` |  ```text #include <algorithm> #include <cstring> #include <iostream> #include <string> using namespace std ; constexpr int N = 2005 ; string s , t ; int na [ N ][ 26 ], nb [ N ][ 26 ], nxt [ 26 ]; int n , m , a [ N ], b [ N ], tot = 1 , p = 1 , f [ N ][ N << 1 ]; struct SAM { int par , ch [ 26 ], len ; } sam [ N << 1 ]; void insert ( int x ) { int np = ++ tot ; // 新节点 sam [ np ]. len = sam [ p ]. len \+ 1 ; while ( p && ! sam [ p ]. ch [ x ]) { sam [ p ]. ch [ x ] = np ; p = sam [ p ]. par ; } if ( p == 0 ) sam [ np ]. par = 1 ; else { int q = sam [ p ]. ch [ x ]; if ( sam [ q ]. len == sam [ p ]. len \+ 1 ) sam [ np ]. par = q ; else { int nq = ++ tot ; sam [ nq ]. len = sam [ p ]. len \+ 1 ; memcpy ( sam [ nq ]. ch , sam [ q ]. ch , sizeof ( sam [ q ]. ch )); sam [ nq ]. par = sam [ q ]. par ; sam [ q ]. par = sam [ np ]. par = nq ; while ( p && sam [ p ]. ch [ x ] == q ) { sam [ p ]. ch [ x ] = nq ; p = sam [ p ]. par ; } } } p = np ; } int main () { cin >> s >> t ; n = s . size (); m = t . size (); s = " " \+ s ; t = " " \+ t ; for ( int i = 1 ; i <= n ; ++ i ) a [ i ] = s [ i ] \- 'a' ; for ( int i = 1 ; i <= m ; ++ i ) b [ i ] = t [ i ] \- 'a' ; for ( int i = 1 ; i <= m ; ++ i ) insert ( b [ i ]); // nxt[S[i]]<-i for ( int i = 0 ; i < 26 ; ++ i ) nxt [ i ] = n \+ 1 ; for ( int i = n ; i >= 0 ; \-- i ) { memcpy ( na [ i ], nxt , sizeof ( nxt )); nxt [ a [ i ]] = i ; } for ( int i = 0 ; i < 26 ; ++ i ) nxt [ i ] = m \+ 1 ; for ( int i = m ; i >= 0 ; \-- i ) { memcpy ( nb [ i ], nxt , sizeof ( nxt )); nxt [ b [ i ]] = i ; } // 四种情况计算答案 // 1 int ans = N ; for ( int l = 1 ; l <= n ; ++ l ) { for ( int r = l , u = 1 ; r <= n ; ++ r ) { u = sam [ u ]. ch [ a [ r ]]; if ( ! u ) { ans = min ( ans , r \- l \+ 1 ); break ; } } } cout << ( ans == N ? -1 : ans ) << '\n' ; // 2 ans = N ; for ( int l = 1 ; l <= n ; ++ l ) { for ( int r = l , u = 0 ; r <= n ; ++ r ) { u = nb [ u ][ a [ r ]]; if ( u == m \+ 1 ) { ans = min ( ans , r \- l \+ 1 ); break ; } } } cout << ( ans == N ? -1 : ans ) << '\n' ; // 3 for ( int i = n ; i >= 0 ; \-- i ) { for ( int j = 1 ; j <= tot ; ++ j ) { f [ i ][ j ] = N ; for ( int c = 0 ; c < 26 ; ++ c ) { int u = na [ i ][ c ]; int v = sam [ j ]. ch [ c ]; if ( u <= n ) f [ i ][ j ] = min ( f [ i ][ j ], f [ u ][ v ] \+ 1 ); } } } cout << ( f [ 0 ][ 1 ] == N ? -1 : f [ 0 ][ 1 ]) << '\n' ; // 4 memset ( f , 0 , sizeof ( f )); for ( int i = n ; i >= 0 ; \-- i ) { for ( int j = 0 ; j <= m ; ++ j ) { f [ i ][ j ] = N ; for ( int c = 0 ; c < 26 ; ++ c ) { int u = na [ i ][ c ]; int v = nb [ j ][ c ]; if ( u <= n ) f [ i ][ j ] = min ( f [ i ][ j ], f [ u ][ v ] \+ 1 ); } } } cout << ( f [ 0 ][ 0 ] == N ? -1 : f [ 0 ][ 0 ]) << '\n' ; return 0 ; } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/seq-automaton.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/seq-automaton.md "edit.link.title")  
>  __本页面贡献者：[ouuan](https://github.com/ouuan), [Enter-tainer](https://github.com/Enter-tainer), [Ir1d](https://github.com/Ir1d), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [FFjet](https://github.com/FFjet), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [ouuan](mailto:1609483441@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
