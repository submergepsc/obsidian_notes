# 斯坦纳树 - OI Wiki

- Source: https://oi-wiki.org/graph/steiner-tree/

# 斯坦纳树

斯坦纳树问题是组合优化问题，与最小生成树相似，是最短网络的一种．最小生成树是在给定的点集和边中寻求最短网络使所有点连通．而最小斯坦纳树允许在给定点外增加额外的点，使生成的最短网络开销最小．

## 问题引入

19 世纪初叶，柏林大学几何方面的著名学者斯坦纳，研究了一个非常简单却很有启示性的问题：将三个村庄用总长为极小的道路连接起来．从数学上说，就是在平面内给定三个点 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 找出平面内第四个点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得和数 𝑎 +𝑏 +𝑐a+b+c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为最短，这里 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别表示从 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的距离．

问题的答案是：如果三角形 𝐴𝐵𝐶ABC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每个内角都小于 120∘120∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是使边 𝐴𝐵AB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐵𝐶BC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐴𝐶AC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对该点所张的角都是 120∘120∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点．如果三角形 𝐴𝐵𝐶ABC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有一个角，例如 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 角，大于或等于 120∘120∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与顶点 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 重合．

### 问题推广

  1. 在斯坦纳问题中，给定了三个固定点 𝐴,𝐵,𝐶A,B,C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．很自然地可以把这个问题推广到给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点 𝐴1,𝐴2,…,𝐴𝑛A1,A2,…,An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形；我们要求出平面内的点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使距离和 𝑎1 +𝑎2 +⋯ +𝑎𝑛a1+a2+⋯+an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为极小，其中 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是距离 𝑃𝐴𝑖PAi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  2. 考虑到点的其他相关因素，加入了权重的表示．𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的其他相关因素可以换算成一个权重表示，求出平面内的点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使距离与权重的乘积的总和 𝑎1 ⋅𝑤1 +𝑎2 ⋅𝑤2 +⋯ +𝑎𝑛 ⋅𝑤𝑛a1⋅w1+a2⋅w2+⋯+an⋅wn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为极小，其中 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是每个点的权重．

  3. 库朗（R.Courant）和罗宾斯（H.Robbins）提出第一个定义的推广是肤浅的．为了求得斯坦纳问题真正有价值的推广，必须放弃寻找一个单独的点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而代之以具有最短总长的＂道路网＂．数学上表述成：给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点 𝐴1,𝐴2,⋯,𝐴𝑛A1,A2,⋯,An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，试求连接此 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，总长最短的直线段连接系统，并且任意两点都可由系统中的直线段组成的折线连接起来．他们将此新问题称为 **斯坦纳树问题** ．在给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的情形，最多将有 𝑛 −2n−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个复接点（斯坦纳点）．过每一斯坦纳点，至多有三条边通过．若为三条边，则它们两两交成 120∘120∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 角；若为两条边，则此斯坦纳点必为某一已给定的点，且此两条边交成的角必大于或等于 120∘120∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

连接三个以上的点的最短网络

![steiner-tree1](./images/steiner-tree-1.svg)

在第一种情形，解是由五条线段组成的，其中有两个斯坦纳点（红色 𝑠1,𝑠2s1,s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），在那里有三条线段相交且相互间的交角为 120∘120∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．第二种情形的解含有三个斯坦纳点．第三种情形，一个或几个斯坦纳点可能退化，或被一个或几个给定的点所代替．

我们将斯坦纳树的问题模型以图论形式呈现．

![steiner-tree2](./images/steiner-tree-2.svg)

对于形式一，如果令关键点为 {1,2,3,4}{1,2,3,4}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以发现若直接将这四个关键点相连的最小边权和是 12，显然这不是最优的．如果考虑使用 5 号节点那么最小边权和就会是 9，得到一个更优的答案．

对于形式二，如果令关键点为 {1,2,3,4}{1,2,3,4}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以发现这四个关键点中的一些点甚至没有直接相连的边，必须考虑使用复接点（斯坦纳点）．这时将 5 号考虑进去可以得到最小边权和 9．

并且我们可以发现在两张图中 1 号和 4 号的斯坦纳点是退化的，被 1 号或 4 号代替了．

## 例题

首先以一道模板题来带大家熟悉最小斯坦纳树问题．见 [【模板】最小斯坦纳树](https://www.luogu.com.cn/problem/P6192)．

题意已经很明确了，给定连通图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点与 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个关键点，连接 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个关键点，使得生成树的所有边的权值和最小．

结合上面的知识我们可以知道直接连接这 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个关键点生成的权值和不一定是最小的，或者这 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个关键点不会直接（相邻）连接．所以应当使用剩下的 𝑛 −𝑘n−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点．

我们使用状态压缩动态规划来求解．用 𝑓(𝑖,𝑆)f(i,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示以 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的一棵树，包含集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有点的最小边权值和．

考虑状态转移：

  * 首先对连通的子集进行转移，𝑓(𝑖,𝑆) ←min(𝑓(𝑖,𝑆),𝑓(𝑖,𝑇) +𝑓(𝑖,𝑆 −𝑇))f(i,S)←min(f(i,S),f(i,T)+f(i,S−T))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 在当前的子集连通状态下进行边的松弛操作，𝑓(𝑖,𝑆) ←min(𝑓(𝑖,𝑆),𝑓(𝑗,𝑆) +𝑤(𝑗,𝑖))f(i,S)←min(f(i,S),f(j,S)+w(j,i))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在下面的代码中用一个 `tree[tot]` 来记录两个相连节点 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的相关信息．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 ``` |  ```text #include <cstring> #include <iostream> #include <queue> #include <vector> using namespace std ; constexpr int MAXN = 510 ; constexpr int INF = 0x3f3f3f3f ; using P = pair < int , int > ; int n , m , k ; struct edge { int to , next , w ; } e [ MAXN << 1 ]; int head [ MAXN << 1 ], tree [ MAXN << 1 ], tot ; int dp [ MAXN ][ 5000 ], vis [ MAXN ]; int key [ MAXN ]; priority_queue < P , vector < P > , greater < P >> q ; void add ( int u , int v , int w ) { e [ ++ tot ] = edge { v , head [ u ], w }; head [ u ] = tot ; } void dijkstra ( int s ) { // 求解最短路 memset ( vis , 0 , sizeof ( vis )); while ( ! q . empty ()) { P item = q . top (); q . pop (); if ( vis [ item . second ]) continue ; vis [ item . second ] = 1 ; for ( int i = head [ item . second ]; i ; i = e [ i ]. next ) { if ( dp [ tree [ i ]][ s ] > dp [ item . second ][ s ] \+ e [ i ]. w ) { dp [ tree [ i ]][ s ] = dp [ item . second ][ s ] \+ e [ i ]. w ; q . push ( P ( dp [ tree [ i ]][ s ], tree [ i ])); } } } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); memset ( dp , INF , sizeof ( dp )); cin >> n >> m >> k ; int u , v , w ; for ( int i = 1 ; i <= m ; i ++ ) { cin >> u >> v >> w ; add ( u , v , w ); tree [ tot ] = v ; add ( v , u , w ); tree [ tot ] = u ; } for ( int i = 1 ; i <= k ; i ++ ) { cin >> key [ i ]; dp [ key [ i ]][ 1 << ( i \- 1 )] = 0 ; } for ( int s = 1 ; s < ( 1 << k ); s ++ ) { for ( int i = 1 ; i <= n ; i ++ ) { for ( int subs = s & ( s \- 1 ); subs ; subs = s & ( subs \- 1 )) // 状压 dp 可以看下题解里写的比较详细 dp [ i ][ s ] = min ( dp [ i ][ s ], dp [ i ][ subs ] \+ dp [ i ][ s ^ subs ]); if ( dp [ i ][ s ] != INF ) q . push ( P ( dp [ i ][ s ], i )); } dijkstra ( s ); } cout << dp [ key [ 1 ]][( 1 << k ) \- 1 ] << '\n' ; return 0 ; } ```   
---|---  
  
另外一道经典例题 [[WC2008] 游览计划](https://www.luogu.com.cn/problem/P4294)．

这道题是求点权和最小的斯坦纳树，用 𝑓(𝑖,𝑆)f(i,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示以 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的一棵树，包含集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有点的最小点权值和．𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示点权．

考虑状态转移：

  * 𝑓(𝑖,𝑆) ←min(𝑓(𝑖,𝑆),𝑓(𝑖,𝑇) +𝑓(𝑖,𝑆 −𝑇) −𝑎𝑖)f(i,S)←min(f(i,S),f(i,T)+f(i,S−T)−ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于此处合并时同一个点 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，会被加两次，所以减去．

  * 𝑓(𝑖,𝑆) ←min(𝑓(𝑖,𝑆),𝑓(𝑗,𝑆) +𝑤(𝑗,𝑖))f(i,S)←min(f(i,S),f(j,S)+w(j,i))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

可以发现状态转移与上面的模板题是类似的，麻烦的是对答案的输出，在 DP 的过程中还要记录路径．

用 `pre[i][s]` 记录转移到 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根，连通状态集合为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时的点与集合的信息．在 DP 结束后从 `pre[root][S]` 出发，寻找与集合里的点相连的那些点并逐步分解集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用 ans 数组来记录被使用的那些点，当集合分解完毕时搜索也就结束了．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 ``` |  ```text #include <cstring> #include <iostream> #include <queue> using namespace std ; #define mp make_pair using P = pair < int , int > ; using PP = pair < P , int > ; constexpr int INF = 0x3f3f3f3f ; constexpr int dx [] = { 0 , 0 , -1 , 1 }; constexpr int dy [] = { 1 , -1 , 0 , 0 }; int n , m , K , root ; int f [ 101 ][ 1111 ], a [ 101 ], ans [ 11 ][ 11 ]; bool inq [ 101 ]; PP pre [ 101 ][ 1111 ]; queue < P > q ; bool legal ( P u ) { if ( u . first >= 0 && u . second >= 0 && u . first < n && u . second < m ) { return true ; } return false ; } int num ( P u ) { return u . first * m \+ u . second ; } void spfa ( int s ) { memset ( inq , 0 , sizeof ( inq )); while ( ! q . empty ()) { P u = q . front (); q . pop (); inq [ num ( u )] = false ; for ( int d = 0 ; d < 4 ; d ++ ) { P v = mp ( u . first \+ dx [ d ], u . second \+ dy [ d ]); int du = num ( u ), dv = num ( v ); if ( legal ( v ) && f [ dv ][ s ] > f [ du ][ s ] \+ a [ dv ]) { f [ dv ][ s ] = f [ du ][ s ] \+ a [ dv ]; if ( ! inq [ dv ]) { inq [ dv ] = true ; q . push ( v ); } pre [ dv ][ s ] = mp ( u , s ); } } } } void dfs ( P u , int s ) { if ( ! pre [ num ( u )][ s ]. second ) return ; ans [ u . first ][ u . second ] = 1 ; int nu = num ( u ); if ( pre [ nu ][ s ]. first == u ) dfs ( u , s ^ pre [ nu ][ s ]. second ); // 通过 dfs 来找到答案 dfs ( pre [ nu ][ s ]. first , pre [ nu ][ s ]. second ); } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); memset ( f , INF , sizeof ( f )); cin >> n >> m ; int tot = 0 ; for ( int i = 0 ; i < n ; i ++ ) { for ( int j = 0 ; j < m ; j ++ ) { cin >> a [ tot ]; if ( ! a [ tot ]) { f [ tot ][ 1 << ( K ++ )] = 0 ; root = tot ; } tot ++ ; } } for ( int s = 1 ; s < ( 1 << K ); s ++ ) { for ( int i = 0 ; i < n * m ; i ++ ) { for ( int subs = s & ( s \- 1 ); subs ; subs = s & ( subs \- 1 )) { if ( f [ i ][ s ] > f [ i ][ subs ] \+ f [ i ][ s ^ subs ] \- a [ i ]) { f [ i ][ s ] = f [ i ][ subs ] \+ f [ i ][ s ^ subs ] \- a [ i ]; // 状态转移 pre [ i ][ s ] = mp ( mp ( i / m , i % m ), subs ); } } if ( f [ i ][ s ] < INF ) q . push ( mp ( i / m , i % m )); } spfa ( s ); } cout << f [ root ][( 1 << K ) \- 1 ] << '\n' ; dfs ( mp ( root / m , root % m ), ( 1 << K ) \- 1 ); for ( int i = 0 , tot = 0 ; i < n ; i ++ ) { for ( int j = 0 ; j < m ; j ++ ) { if ( ! a [ tot ++ ]) cout << 'x' ; else cout << ( ans [ i ][ j ] ? 'o' : '_' ); } if ( i != n \- 1 ) cout << '\n' ; } return 0 ; } ```   
---|---  
  
## 习题

  * [【模板】最小斯坦纳树](https://www.luogu.com.cn/problem/P6192)
  * [[WC2008] 游览计划](https://www.luogu.com.cn/problem/P4294)
  * [[JLOI2015] 管道连接](https://loj.ac/problem/2110)
  * [[APIO2013] 机器人](https://www.luogu.com.cn/problem/P3638)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/steiner-tree.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/steiner-tree.md "edit.link.title")  
>  __本页面贡献者：[ShaoChenHeng](https://github.com/ShaoChenHeng), [ChungZH](https://github.com/ChungZH), [Enter-tainer](https://github.com/Enter-tainer), [kenlig](https://github.com/kenlig), [mcendu](https://github.com/mcendu), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
