# 最小直径生成树 - OI Wiki

- Source: https://oi-wiki.org/graph/mdst/

# 最小直径生成树

在学习最小直径生成树（Minimum Diameter Spanning Tree）前建议先阅读 [树的直径](../tree-diameter/) 的内容．

## 定义

在无向图的所有生成树中，直径最小的那一棵生成树就是最小直径生成树．

## 图的绝对中心

求解直径最小生成树，首先需要找到 **图的绝对中心** ，**图的绝对中心** 可以存在于一条边上或某个结点上，该中心到所有点的最短距离的最大值最小．

根据 **图的绝对中心** 的定义可以知道，到绝对中心距离最远的结点至少有两个．

令 𝑑(𝑖,𝑗)d(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为顶点 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 间的最短路径长，通过多源最短路算法求出所有结点的最短路．

𝑟𝑘(𝑖,𝑗)rk(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记录点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到其他所有结点中第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小的那个结点．

图的绝对中心可能在某条边上，枚举每一条边 𝑤 =(𝑢,𝑣)w=(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且假设图的绝对中心 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就在这条边上．那么距离 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的长度为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑥 ≤𝑤x≤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），距离 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的长度就是 𝑤 −𝑥w−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于图中的任意一点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，图的绝对中心 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的距离为 𝑑(𝑐,𝑖) =min(𝑑(𝑢,𝑖) +𝑥,𝑑(𝑣,𝑖) +(𝑤 −𝑥))d(c,i)=min(d(u,i)+x,d(v,i)+(w−x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

举例一个结点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，该结点与图的绝对中心的位置关系如下图．

![mdst1](./images/mdst-graph.svg)

随着图的绝对中心 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在边上的改变会生成一个距离与 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位置的函数图像．显然的，当前的 𝑑(𝑐,𝑖)d(c,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的函数图像是一个两条斜率相同的线段构成的折线段．

![mdst2](./images/mdst-plot1.svg)

对于图上的任意一结点，图的绝对中心到最远距离结点的函数就写作 𝑓 =max{𝑑(𝑐,𝑖)},𝑖 ∈[1,𝑛]f=max{d(c,i)},i∈[1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其函数图像如下．

![mdst3](./images/mdst-plot2.svg)

并且这些折线交点中的最低点，横坐标就是图的绝对中心的位置．

图的绝对中心可能在某个结点上，用距离预选结点最远的那个结点来更新，即 𝑎𝑛𝑠 ←min(𝑎𝑛𝑠,𝑑(𝑖,𝑟𝑘(𝑖,𝑛)) ×2)ans←min(ans,d(i,rk(i,n))×2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 过程

  1. 使用多源最短路算法（[Floyd](../shortest-path/#floyd-算法)，[Johnson](../shortest-path/#johnson-全源最短路径算法) 等），求出 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组；

  2. 求出 𝑟𝑘(𝑖,𝑗)rk(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将其升序排序；

  3. 图的绝对中心可能在某个结点上，用距离预选结点最远的那个结点来更新，遍历所有结点并用 𝑎𝑛𝑠 ←min(𝑎𝑛𝑠,𝑑(𝑖,𝑟𝑘(𝑖,𝑛)) ×2)ans←min(ans,d(i,rk(i,n))×2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更新最小值．

  4. 图的绝对中心可能在某条边上，枚举所有的边．对于一条边 𝑤(𝑢,𝑣)w(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从距离 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最远的结点开始更新．当出现 𝑑(𝑣,𝑟𝑘(𝑢,𝑖)) >max𝑛𝑗=𝑖+1𝑑(𝑣,𝑟𝑘(𝑢,𝑗))d(v,rk(u,i))>maxj=i+1nd(v,rk(u,j))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况时，用 𝑎𝑛𝑠 ←min(𝑎𝑛𝑠,𝑑(𝑢,𝑟𝑘(𝑢,𝑖)) +max𝑛𝑗=𝑖+1𝑑(𝑣,𝑟𝑘(𝑢,𝑗)) +𝑤(𝑢,𝑣))ans←min(ans,d(u,rk(u,i))+maxj=i+1nd(v,rk(u,j))+w(u,v))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来更新．因为这种情况会使图的绝对中心改变．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text bool cmp ( int a , int b ) { return val [ a ] < val [ b ]; } void Floyd () { for ( int k = 1 ; k <= n ; k ++ ) for ( int i = 1 ; i <= n ; i ++ ) for ( int j = 1 ; j <= n ; j ++ ) d [ i ][ j ] = min ( d [ i ][ j ], d [ i ][ k ] \+ d [ k ][ j ]); } void solve () { Floyd (); for ( int i = 1 ; i <= n ; i ++ ) { for ( int j = 1 ; j <= n ; j ++ ) { rk [ i ][ j ] = j ; val [ j ] = d [ i ][ j ]; } sort ( rk [ i ] \+ 1 , rk [ i ] \+ 1 \+ n , cmp ); } int ans = INF ; // 图的绝对中心可能在结点上 for ( int i = 1 ; i <= n ; i ++ ) ans = min ( ans , d [ i ][ rk [ i ][ n ]] * 2 ); // 图的绝对中心可能在边上 for ( int i = 1 ; i <= m ; i ++ ) { int u = a [ i ]. u , v = a [ i ]. v , w = a [ i ]. w ; for ( int p = n , i = n \- 1 ; i >= 1 ; i \-- ) { if ( d [ v ][ rk [ u ][ i ]] > d [ v ][ rk [ u ][ p ]]) { ans = min ( ans , d [ u ][ rk [ u ][ i ]] \+ d [ v ][ rk [ u ][ p ]] \+ w ); p = i ; } } } } ```   
---|---  
  
### 例题

  * [CodeForce 266D BerDonalds](https://codeforces.com/contest/266/problem/D)

## 最小直径生成树

根据图的绝对中心的定义，容易得知图的绝对中心是最小直径生成树的直径的中点．

求解最小直径生成树首先需要找到图的绝对中心．以图的绝对中心为起点，生成一个最短路径树，那么就可以得到最小直径生成树了．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 ``` |  ```text #include <algorithm> #include <climits> #include <iostream> #include <vector> using namespace std ; constexpr int MAXN = 502 ; using ll = long long ; using pii = pair < int , int > ; ll d [ MAXN ][ MAXN ], dd [ MAXN ][ MAXN ], rk [ MAXN ][ MAXN ], val [ MAXN ]; constexpr ll INF = 1e17 ; int n , m ; bool cmp ( int a , int b ) { return val [ a ] < val [ b ]; } void floyd () { for ( int k = 1 ; k <= n ; k ++ ) for ( int i = 1 ; i <= n ; i ++ ) for ( int j = 1 ; j <= n ; j ++ ) d [ i ][ j ] = min ( d [ i ][ j ], d [ i ][ k ] \+ d [ k ][ j ]); } struct node { ll u , v , w ; } a [ MAXN * ( MAXN \- 1 ) / 2 ]; void solve () { // 求图的绝对中心 floyd (); for ( int i = 1 ; i <= n ; i ++ ) { for ( int j = 1 ; j <= n ; j ++ ) { rk [ i ][ j ] = j ; val [ j ] = d [ i ][ j ]; } sort ( rk [ i ] \+ 1 , rk [ i ] \+ 1 \+ n , cmp ); } ll P = 0 , ansP = INF ; // 在点上 for ( int i = 1 ; i <= n ; i ++ ) { if ( d [ i ][ rk [ i ][ n ]] * 2 < ansP ) { ansP = d [ i ][ rk [ i ][ n ]] * 2 ; P = i ; } } // 在边上 int f1 = 0 , f2 = 0 ; ll disu = INT_MIN , disv = INT_MIN , ansL = INF ; for ( int i = 1 ; i <= m ; i ++ ) { ll u = a [ i ]. u , v = a [ i ]. v , w = a [ i ]. w ; for ( int p = n , i = n \- 1 ; i >= 1 ; i \-- ) { if ( d [ v ][ rk [ u ][ i ]] > d [ v ][ rk [ u ][ p ]]) { if ( d [ u ][ rk [ u ][ i ]] \+ d [ v ][ rk [ u ][ p ]] \+ w < ansL ) { ansL = d [ u ][ rk [ u ][ i ]] \+ d [ v ][ rk [ u ][ p ]] \+ w ; f1 = u , f2 = v ; disu = ( d [ u ][ rk [ u ][ i ]] \+ d [ v ][ rk [ u ][ p ]] \+ w ) / 2 \- d [ u ][ rk [ u ][ i ]]; disv = w \- disu ; } p = i ; } } } cout << min ( ansP , ansL ) / 2 << '\n' ; // 最小路径生成树 vector < pii > pp ; for ( int i = 1 ; i <= 501 ; ++ i ) for ( int j = 1 ; j <= 501 ; ++ j ) dd [ i ][ j ] = INF ; for ( int i = 1 ; i <= 501 ; ++ i ) dd [ i ][ i ] = 0 ; if ( ansP <= ansL ) { for ( int j = 1 ; j <= n ; j ++ ) { for ( int i = 1 ; i <= m ; ++ i ) { ll u = a [ i ]. u , v = a [ i ]. v , w = a [ i ]. w ; if ( dd [ P ][ u ] \+ w == d [ P ][ v ] && dd [ P ][ u ] \+ w < dd [ P ][ v ]) { dd [ P ][ v ] = dd [ P ][ u ] \+ w ; pp . push_back ({ u , v }); } u = a [ i ]. v , v = a [ i ]. u , w = a [ i ]. w ; if ( dd [ P ][ u ] \+ w == d [ P ][ v ] && dd [ P ][ u ] \+ w < dd [ P ][ v ]) { dd [ P ][ v ] = dd [ P ][ u ] \+ w ; pp . push_back ({ u , v }); } } } for ( auto [ x , y ] : pp ) cout << x << ' ' << y << '\n' ; } else { d [ n \+ 1 ][ f1 ] = disu ; d [ f1 ][ n \+ 1 ] = disu ; d [ n \+ 1 ][ f2 ] = disv ; d [ f2 ][ n \+ 1 ] = disv ; a [ m \+ 1 ]. u = n \+ 1 , a [ m \+ 1 ]. v = f1 , a [ m \+ 1 ]. w = disu ; a [ m \+ 2 ]. u = n \+ 1 , a [ m \+ 2 ]. v = f2 , a [ m \+ 2 ]. w = disv ; n += 1 ; m += 2 ; floyd (); P = n ; for ( int j = 1 ; j <= n ; j ++ ) { for ( int i = 1 ; i <= m ; ++ i ) { ll u = a [ i ]. u , v = a [ i ]. v , w = a [ i ]. w ; if ( dd [ P ][ u ] \+ w == d [ P ][ v ] && dd [ P ][ u ] \+ w < dd [ P ][ v ]) { dd [ P ][ v ] = dd [ P ][ u ] \+ w ; pp . push_back ({ u , v }); } u = a [ i ]. v , v = a [ i ]. u , w = a [ i ]. w ; if ( dd [ P ][ u ] \+ w == d [ P ][ v ] && dd [ P ][ u ] \+ w < dd [ P ][ v ]) { dd [ P ][ v ] = dd [ P ][ u ] \+ w ; pp . push_back ({ u , v }); } } } cout << f1 << ' ' << f2 << '\n' ; for ( auto [ x , y ] : pp ) if ( x != n && y != n ) cout << x << ' ' << y << '\n' ; } } void init () { for ( int i = 1 ; i <= 501 ; ++ i ) for ( int j = 1 ; j <= 501 ; ++ j ) d [ i ][ j ] = INF ; for ( int i = 1 ; i <= 501 ; ++ i ) d [ i ][ i ] = 0 ; } int main () { init (); cin >> n >> m ; for ( int i = 1 ; i <= m ; ++ i ) { ll u , v , w ; cin >> u >> v >> w ; w *= 2 ; d [ u ][ v ] = w , d [ v ][ u ] = w ; a [ i ]. u = u , a [ i ]. v = v , a [ i ]. w = w ; } solve (); return 0 ; } ```   
---|---  
  
### 例题

[SPOJ MDST](https://www.spoj.com/problems/MDST/)

[timus 1569. Networking the "Iset"](https://acm.timus.ru/problem.aspx?space=1&num=1569)

[SPOJ PT07C - The GbAaY Kingdom](https://www.spoj.com/problems/PT07C)

## 参考文献

[Play with Trees Solutions The GbAaY Kingdom](https://adn.botao.hu/adn-backup/blog/attachments/month_0705/32007531153238.pdf)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/mdst.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/mdst.md "edit.link.title")  
>  __本页面贡献者：[ShaoChenHeng](https://github.com/ShaoChenHeng), [Enter-tainer](https://github.com/Enter-tainer), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [Alisahhh](https://github.com/Alisahhh), [billchenchina](https://github.com/billchenchina), [Early0v0](https://github.com/Early0v0), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [ksyx](https://github.com/ksyx), [leoleoasd](https://github.com/leoleoasd), [Marcythm](https://github.com/Marcythm), [mcendu](https://github.com/mcendu), [opsiff](https://github.com/opsiff), [ouuan](https://github.com/ouuan), [Suiseiseki-2016](https://github.com/Suiseiseki-2016), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [wplf](https://github.com/wplf)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
