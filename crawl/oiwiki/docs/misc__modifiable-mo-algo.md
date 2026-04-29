# 带修改莫队 - OI Wiki

- Source: https://oi-wiki.org/misc/modifiable-mo-algo/

# 带修改莫队

请确保您已经会普通莫队算法了．如果您还不会，请先阅读前面的 [普通莫队算法](../mo-algo/)．

## 特点

普通莫队是不能带修改的．

我们可以强行让它可以修改，就像 DP 一样，可以强行加上一维 **时间维** , 表示这次操作的时间．

时间维表示经历的修改次数．

即把询问 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变成 [𝑙,𝑟,time][l,r,time]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

那么我们的坐标也可以在时间维上移动，即 [𝑙,𝑟,time][l,r,time]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 多了一维可以移动的方向，可以变成：

  * [𝑙 −1,𝑟,time][l−1,r,time]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * [𝑙 +1,𝑟,time][l+1,r,time]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * [𝑙,𝑟 −1,time][l,r−1,time]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * [𝑙,𝑟 +1,time][l,r+1,time]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * [𝑙,𝑟,time −1][l,r,time−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * [𝑙,𝑟,time +1][l,r,time+1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样的转移也是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，但是我们排序又多了一个关键字，再搞搞就行了．

可以用和普通莫队类似的方法排序转移，做到 𝑂(𝑛5/3)O(n5/3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这一次我们排序的方式是以 𝑛2/3n2/3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一块，分成了 𝑛1/3n1/3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块，第一关键字是左端点所在块，第二关键字是右端点所在块，第三关键字是时间．

最优块长以及时间复杂度分析

我们设序列长为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个询问，𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个修改．

带修莫队排序的第二关键字是右端点所在块编号，不同于普通莫队．

想一想，如果不把右端点分块：

  * 乱序的右端点对于每个询问会移动 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．
  * 有序的右端点会带来乱序的时间，每次询问会移动 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．

无论哪一种情况，带来的时间开销都无法接受．

接下来分析时间复杂度．

设块长为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有 𝑛𝑠ns![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个块．对于块 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和块 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记有 𝑞𝑖,𝑗qi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个询问的左端点位于块 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，右端点位于块 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

每「组」左右端点不换块的询问 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，端点每次移动 𝑂(𝑠)O(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，时间单调递增，𝑂(𝑡)O(t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

左右端点换块的时间忽略不计．

表示一下就是：

𝑛/𝑠∑𝑖=1𝑛/𝑠∑𝑗=𝑖+1(𝑞𝑖,𝑗⋅𝑠+𝑡)=𝑚𝑠+(𝑛𝑠)2𝑡=𝑚𝑠+𝑛2𝑡𝑠2∑i=1n/s∑j=i+1n/s(qi,j⋅s+t)=ms+(ns)2t=ms+n2ts2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑求导求此式极小值．设 𝑓(𝑠) =𝑚𝑠 +𝑛2𝑡𝑠2f(s)=ms+n2ts2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那 𝑓′(𝑠) =𝑚 −2𝑛2𝑡𝑠3 =0f′(s)=m−2n2ts3=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

得 𝑠 =3√2𝑛2𝑡𝑚 =21/3𝑛2/3𝑡1/3𝑚1/3 =𝑠0s=2n2tm3=21/3n2/3t1/3m1/3=s0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

也就是当块长取 𝑛2/3𝑡1/3𝑚1/3n2/3t1/3m1/3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时有最优时间复杂度 𝑂(𝑛2/3𝑚2/3𝑡1/3)O(n2/3m2/3t1/3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

常说的 𝑂(𝑛5/3)O(n5/3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 便是把 𝑛,𝑚,𝑡n,m,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当做同数量级的时间复杂度．

实际操作中还是推荐设定 𝑛2/3n2/3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为块长．

## 例题

例题 [「国家集训队」数颜色/维护队列](https://www.luogu.com.cn/problem/P1903)

题目大意：给你一个序列，M 个操作，有两种操作：

  1. 修改序列上某一位的数字
  2. 询问区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中数字的种类数（多个相同的数字只算一个）

我们不难发现，如果不带操作 1（修改）的话，我们就能轻松用普通莫队解决．

但是题目还带单点修改，所以用 **带修改的莫队** ．

### 过程

先考虑普通莫队的做法：

  * 每次扩大区间时，每加入一个数字，则统计它已经出现的次数，如果加入前这种数字出现次数为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则说明这是一种新的数字，答案 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．然后这种数字的出现次数 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 每次减小区间时，每删除一个数字，则统计它删除后的出现次数，如果删除后这种数字出现次数为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则说明这种数字已经从当前的区间内删光了，也就是当前区间减少了一种颜色，答案 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．然后这种数字的出现次数 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

现在再来考虑修改：

  * 单点修改，把某一位的数字修改掉．假如我们是从一个经历修改次数为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的询问转移到一个经历修改次数为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的询问上，且 𝑖 <𝑗i<j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的话，我们就需要把第 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个到第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个修改强行加上．
  * 假如 𝑗 <𝑖j<i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的话，则需要把第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个到第 𝑗 +1j+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个修改强行还原．

怎么强行加上一个修改呢？假设一个修改是修改第 𝑝𝑜𝑠pos![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个位置上的颜色，原本 𝑝𝑜𝑠pos![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的颜色为 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，修改后颜色为 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，还假设当前莫队的区间扩展到了 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 加上这个修改：我们首先判断 𝑝𝑜𝑠pos![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否在区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内．如果是的话，我们等于是从区间中删掉颜色 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，加上颜色 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且当前颜色序列的第 𝑝𝑜𝑠pos![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项的颜色改成 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果不在区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的话，我们就直接修改当前颜色序列的第 𝑝𝑜𝑠pos![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项为 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 还原这个修改：等于加上一个修改第 𝑝𝑜𝑠pos![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项、把颜色 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 改成颜色 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的修改．

因此这道题就这样用带修改莫队轻松解决啦！

### 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 ``` |  ```text #include <algorithm> #include <cmath> #include <iostream> using namespace std ; long long qsize ; struct query { long long id , t , l , r ; bool operator < ( query b ) const { if ( l / qsize != b . l / qsize ) { return l / qsize > b . l / qsize ; } else if ( r / qsize != b . r / qsize ) { return r / qsize > b . r / qsize ; } else { return t > b . t ; } } } q [ 150009 ]; struct operation { long long p , x ; } r [ 150009 ]; char op ; long long n , m , x , y , cur , qcnt , rcnt , mp [ 1500009 ], a [ 150009 ], ans [ 150009 ]; void add ( long long x ) { if ( ! mp [ x ]) { cur += 1 ; } mp [ x ] += 1 ; } void del ( long long x ) { mp [ x ] -= 1 ; if ( ! mp [ x ]) { cur -= 1 ; } } void process () { sort ( q \+ 1 , q \+ qcnt \+ 1 ); long long L = 1 , R = 0 , last = 0 ; for ( long long i = 1 ; i <= qcnt ; i ++ ) { while ( R < q [ i ]. r ) { add ( a [ ++ R ]); } while ( R > q [ i ]. r ) { del ( a [ R \-- ]); } while ( L > q [ i ]. l ) { add ( a [ \-- L ]); } while ( L < q [ i ]. l ) { del ( a [ L ++ ]); } while ( last < q [ i ]. t ) { last += 1 ; if ( r [ last ]. p >= L && r [ last ]. p <= R ) { add ( r [ last ]. x ); del ( a [ r [ last ]. p ]); } swap ( a [ r [ last ]. p ], r [ last ]. x ); } while ( last > q [ i ]. t ) { if ( r [ last ]. p >= L && r [ last ]. p <= R ) { add ( r [ last ]. x ); del ( a [ r [ last ]. p ]); } swap ( a [ r [ last ]. p ], r [ last ]. x ); last -= 1 ; } ans [ q [ i ]. id ] = cur ; } } signed main () { cin . tie ( nullptr ); ios :: sync_with_stdio ( false ); cin >> n >> m ; qsize = pow ( n , 2.0 / 3.0 ); for ( long long i = 1 ; i <= n ; i ++ ) { cin >> a [ i ]; } for ( long long i = 1 ; i <= m ; i ++ ) { cin >> op >> x >> y ; if ( op == 'Q' ) { ++ qcnt , q [ qcnt ] = { qcnt , rcnt , x , y }; } else if ( op == 'R' ) { r [ ++ rcnt ] = { x , y }; } } process (); for ( long long i = 1 ; i <= qcnt ; i ++ ) { cout << ans [ i ] << '\n' ; } } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/modifiable-mo-algo.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/modifiable-mo-algo.md "edit.link.title")  
>  __本页面贡献者：[Backl1ght](https://github.com/Backl1ght), [countercurrent-time](https://github.com/countercurrent-time), [Ir1d](https://github.com/Ir1d), [Lixuannan](https://github.com/Lixuannan), [renbaoshuo](https://github.com/renbaoshuo), [Tiphereth-A](https://github.com/Tiphereth-A), [2008verser](https://github.com/2008verser), [383494](https://github.com/383494), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [Enter-tainer](https://github.com/Enter-tainer), [greyqz](https://github.com/greyqz), [Henry-ZHR](https://github.com/Henry-ZHR), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [MicDZ](https://github.com/MicDZ), [O-Omega](https://github.com/O-Omega), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [yzxoi](https://github.com/yzxoi)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
