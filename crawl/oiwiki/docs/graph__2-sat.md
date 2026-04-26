# 2-SAT - OI Wiki

- Source: https://oi-wiki.org/graph/2-sat/

# 2-SAT

SAT 是适定性（Satisfiability）问题的简称．一般形式为 k - 适定性问题，简称 k-SAT．而当 𝑘 >2k>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时该问题为 NP 完全的．所以我们只研究 𝑘 =2k=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况．

## 定义

2-SAT，简单的说就是给出 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个布尔方程，每个方程和两个变量相关，如 𝑎 ∨𝑏a∨b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示变量 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至少满足一个．然后判断是否存在可行方案，显然可能有多种选择方案，一般题中只需要求出一种即可．另外，¬𝑎¬a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取反．

## 解决思路

[洛谷 P4782「模板」2-SAT](https://www.luogu.com.cn/problem/P4782)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个布尔变量 𝑥1 ∼𝑥𝑛x1∼xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，另有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个需要满足的条件，每个条件的形式都是「𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 `true`/`false` 或 𝑥𝑗xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 `true`/`false`」．比如「𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为真或 𝑥3x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为假」、「𝑥7x7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为假或 𝑥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为假」．

2-SAT 问题的目标是给每个变量赋值使得所有条件得到满足．

使用布尔方程表示上述问题．设 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑥𝑎xa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为真（¬𝑎¬a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就表示 𝑥𝑎xa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为假）．如果有个人提出的要求分别是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 (𝑎 ∨𝑏)(a∨b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（变量 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至少满足一个）．对这些变量关系建有向图，则把 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立或不成立用图中的点表示，¬𝑎 →𝑏¬a→b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) ¬𝑏 →𝑎¬b→a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **不成立** 则 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **一定成立** ；同理，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **不成立** 则 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **一定成立** ．建图之后，我们就可以使用缩点算法来求解 2-SAT 问题了．

原式| 建图  
---|---  
¬𝑎 ∨𝑏¬a∨b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 𝑎 →𝑏a→b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ¬𝑏 →¬𝑎¬b→¬a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
𝑎 ∨𝑏a∨b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ¬𝑎 →𝑏¬a→b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ¬𝑏 →𝑎¬b→a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
¬𝑎 ∨¬𝑏¬a∨¬b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 𝑎 →¬𝑏a→¬b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏 →¬𝑎b→¬a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
许多 2-SAT 问题都需要找出如 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **不成立** ，则 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **成立** 的关系．

## 求解

思考如果两点在同一强连通分量里有什么含义．根据前文边的逻辑意义可知：若两点在同一强连通分量内，则这两点代表的条件 **要么都满足，要么都不满足** ．

建图后我们使用 [Tarjan 算法找 SCC](../scc/)，判断对于任意布尔变量 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立的点和表示 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不成立的点是否在同一个 SCC 中（同一条件不可能既满足又不满足，或既不满足又并非不满足），若有则输出无解，否则有解．

输出方案时可以通过变量在图中的拓扑序确定该变量的取值．如果变量 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的拓扑序在 ¬𝑥¬x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之后，那么取 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值为真．应用到 Tarjan 算法的缩点，即 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在 SCC 编号在 ¬𝑥¬x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之前时，取 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为真．因为 Tarjan 算法求强连通分量时使用了栈，如果跑完 Tarjan 缩点之后呈现出的拓扑序更大，在 Tarjan 会更晚被遍历到，就会更早地被弹出栈而缩点，分量编号会更小，所以 Tarjan 求得的 SCC 编号相当于 **反拓扑序** ．

算法会把整张图遍历一遍，由于这张图 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同阶，计算答案时复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此总复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

代码实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 ``` |  ```text #include <algorithm> #include <cstdio> #include <stack> using namespace std ; const int N = 2e6 \+ 2 ; int n , m , dfn [ N ], low [ N ], t , tot , head [ N ], a [ N ]; bool vis [ N ]; stack < int > s ; struct node { int to , Next ; } e [ N ]; void adde ( int u , int v ) { e [ ++ tot ]. to = v ; e [ tot ]. Next = head [ u ]; head [ u ] = tot ; } void Tarjan ( int u ) { dfn [ u ] = low [ u ] = ++ t ; s . push ( u ); vis [ u ] = 1 ; for ( int i = head [ u ]; i ; i = e [ i ]. Next ) { int v = e [ i ]. to ; if ( ! dfn [ v ]) { Tarjan ( v ); low [ u ] = min ( low [ u ], low [ v ]); } else if ( vis [ v ]) low [ u ] = min ( low [ u ], dfn [ v ]); } if ( dfn [ u ] == low [ u ]) { int cur ; ++ tot ; do { cur = s . top (); s . pop (); vis [ cur ] = 0 ; a [ cur ] = tot ; } while ( cur != u ); } } int main () { scanf ( "%d%d" , & n , & m ); for ( int i = 1 , I , J , A , B ; i <= m ; i ++ ) { scanf ( "%d%d%d%d" , & I , & A , & J , & B ); adde ( A ? I \+ n : I , B ? J : J \+ n ); adde ( B ? J \+ n : J , A ? I : I \+ n ); } tot = 0 ; for ( int i = 1 ; i <= ( n << 1 ); i ++ ) if ( ! dfn [ i ]) Tarjan ( i ); for ( int i = 1 ; i <= n ; i ++ ) { if ( a [ i ] == a [ i \+ n ]) { printf ( "IMPOSSIBLE" ); return 0 ; } } puts ( "POSSIBLE" ); for ( int i = 1 ; i <= n ; i ++ ) printf ( "%c%c" , a [ i ] < a [ i \+ n ] ? '1' : '0' , " \n " [ i == n ]); return 0 ; } ```   
---|---  
  
## 例题

### 例题 1

[HDU3062 Party](https://acm.hdu.edu.cn/showproblem.php?pid=3062)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对夫妻被邀请参加一个聚会，因为场地的问题，每对夫妻中只有一人可以列席．在 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人中，某些人之间有着很大的矛盾（当然夫妻之间是没有矛盾的），有矛盾的两个人是不会同时出现在聚会上的．有没有可能会有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人同时列席？

按照上面的分析，如果 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的丈夫和 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的妻子不合，我们就把 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的丈夫和 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的丈夫连边，把 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的妻子和 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的妻子连边，然后缩点染色判断即可．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 ``` |  ```text #include <algorithm> #include <cstring> #include <iostream> constexpr int MAXN = 2018 ; constexpr int MAXM = 4000400 ; using namespace std ; int Index , instack [ MAXN ], DFN [ MAXN ], LOW [ MAXN ]; int tot , color [ MAXN ]; int numedge , head [ MAXN ]; struct Edge { int nxt , to ; } edge [ MAXM ]; int sta [ MAXN ], top ; int n , m ; void add ( int x , int y ) { edge [ ++ numedge ]. to = y ; edge [ numedge ]. nxt = head [ x ]; head [ x ] = numedge ; } void tarjan ( int x ) { // 缩点看不懂请移步强连通分量上面有一个链接可以点。 sta [ ++ top ] = x ; instack [ x ] = 1 ; DFN [ x ] = LOW [ x ] = ++ Index ; for ( int i = head [ x ]; i ; i = edge [ i ]. nxt ) { int v = edge [ i ]. to ; if ( ! DFN [ v ]) { tarjan ( v ); LOW [ x ] = min ( LOW [ x ], LOW [ v ]); } else if ( instack [ v ]) LOW [ x ] = min ( LOW [ x ], DFN [ v ]); } if ( DFN [ x ] == LOW [ x ]) { tot ++ ; do { color [ sta [ top ]] = tot ; // 染色 instack [ sta [ top ]] = 0 ; } while ( sta [ top \-- ] != x ); } } bool solve () { for ( int i = 0 ; i < 2 * n ; i ++ ) if ( ! DFN [ i ]) tarjan ( i ); for ( int i = 0 ; i < 2 * n ; i += 2 ) if ( color [ i ] == color [ i \+ 1 ]) return false ; return true ; } void init () { top = 0 ; tot = 0 ; Index = 0 ; numedge = 0 ; memset ( sta , 0 , sizeof ( sta )); memset ( DFN , 0 , sizeof ( DFN )); memset ( instack , 0 , sizeof ( instack )); memset ( LOW , 0 , sizeof ( LOW )); memset ( color , 0 , sizeof ( color )); memset ( head , 0 , sizeof ( head )); } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); while ( cin >> n >> m ) { init (); for ( int i = 1 ; i <= m ; i ++ ) { int a1 , a2 , c1 , c2 ; cin >> a1 >> a2 >> c1 >> c2 ; add ( 2 * a1 \+ c1 , 2 * a2 \+ 1 \- c2 ); // 对于第 i 对夫妇，我们用 2i+1 表示丈夫，2i 表示妻子。 add ( 2 * a2 \+ c2 , 2 * a1 \+ 1 \- c1 ); } if ( solve ()) cout << "YES \n " ; else cout << "NO \n " ; } return 0 ; } ```   
---|---  
  
### 例题 2

[2018-2019 ACM-ICPC Asia Seoul Regional K TV Show Game](https://codeforces.com/gym/101987/problem/K)

有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 盏灯，每盏灯是红色或者蓝色，但是初始的时候不知道灯的颜色．有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人，每个人选择三盏灯并猜灯的颜色．一个人猜对两盏灯或以上的颜色就可以获得奖品．判断是否存在一个灯的着色方案使得每个人都能领奖，若有则输出一种灯的着色方案．

根据 [伍昱 -《由对称性解 2-sat 问题》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2003%E8%AE%BA%E6%96%87%E9%9B%86/%E4%BC%8D%E6%98%B1--%E7%94%B1%E5%AF%B9%E7%A7%B0%E6%80%A7%E8%A7%A32-SAT%E9%97%AE%E9%A2%98/%E4%BC%8D%E6%98%B1.ppt)，我们可以得出：如果要输出 2-SAT 问题的一个可行解，只需要在 tarjan 缩点后所得的 DAG 上自底向上地进行选择和删除．

具体实现的时候，可以通过构造 DAG 的反图后在反图上进行拓扑排序实现；也可以根据 tarjan 缩点后，所属连通块编号越小，节点越靠近叶子节点这一性质，优先对所属连通块编号小的节点进行选择．

下面给出第二种实现方法的代码．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 ``` |  ```text #include <algorithm> #include <iostream> using namespace std ; constexpr int MAXN = 1e4 \+ 5 ; constexpr int MAXK = 5005 ; int n , k ; int id [ MAXN ][ 5 ]; char s [ MAXN ][ 5 ][ 5 ], ans [ MAXK ]; bool vis [ MAXN ]; struct Edge { int v , nxt ; } e [ MAXN * 100 ]; int head [ MAXN ], tot = 1 ; void addedge ( int u , int v ) { e [ tot ]. v = v ; e [ tot ]. nxt = head [ u ]; head [ u ] = tot ++ ; } int dfn [ MAXN ], low [ MAXN ], color [ MAXN ], stk [ MAXN ], ins [ MAXN ], top , dfs_clock , c ; void tarjan ( int x ) { // tarjan算法求强联通 stk [ ++ top ] = x ; ins [ x ] = 1 ; dfn [ x ] = low [ x ] = ++ dfs_clock ; for ( int i = head [ x ]; i ; i = e [ i ]. nxt ) { int v = e [ i ]. v ; if ( ! dfn [ v ]) { tarjan ( v ); low [ x ] = min ( low [ x ], low [ v ]); } else if ( ins [ v ]) low [ x ] = min ( low [ x ], dfn [ v ]); } if ( dfn [ x ] == low [ x ]) { c ++ ; do { color [ stk [ top ]] = c ; ins [ stk [ top ]] = 0 ; } while ( stk [ top \-- ] != x ); } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> k >> n ; for ( int i = 1 ; i <= n ; i ++ ) { for ( int j = 1 ; j <= 3 ; j ++ ) cin >> id [ i ][ j ] >> s [ i ][ j ]; for ( int j = 1 ; j <= 3 ; j ++ ) { for ( int k = 1 ; k <= 3 ; k ++ ) { if ( j == k ) continue ; int u = 2 * id [ i ][ j ] \- ( s [ i ][ j ][ 0 ] == 'B' ); int v = 2 * id [ i ][ k ] \- ( s [ i ][ k ][ 0 ] == 'R' ); addedge ( u , v ); } } } for ( int i = 1 ; i <= 2 * k ; i ++ ) if ( ! dfn [ i ]) tarjan ( i ); for ( int i = 1 ; i <= 2 * k ; i += 2 ) if ( color [ i ] == color [ i \+ 1 ]) { cout << "-1 \n " ; return 0 ; } for ( int i = 1 ; i <= 2 * k ; i += 2 ) { int f1 = color [ i ], f2 = color [ i \+ 1 ]; if ( vis [ f1 ]) { ans [( i \+ 1 ) >> 1 ] = 'R' ; continue ; } if ( vis [ f2 ]) { ans [( i \+ 1 ) >> 1 ] = 'B' ; continue ; } if ( f1 < f2 ) { vis [ f1 ] = true ; ans [( i \+ 1 ) >> 1 ] = 'R' ; } else { vis [ f2 ] = true ; ans [( i \+ 1 ) >> 1 ] = 'B' ; } } ans [ k \+ 1 ] = 0 ; cout << ( ans \+ 1 ) << '\n' ; return 0 ; } ```   
---|---  
  
## 习题

  * [洛谷 P5782 和平委员会](https://www.luogu.com.cn/problem/P5782)
  * [POJ3683 Priest John's Busiest Day](http://poj.org/problem?id=3683)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/2-sat.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/2-sat.md "edit.link.title")  
>  __本页面贡献者：[AndrewWayne](https://github.com/AndrewWayne), [Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [Backl1ght](https://github.com/Backl1ght), [chu-yuehan](https://github.com/chu-yuehan), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [frank-xjh](https://github.com/frank-xjh), [H-J-Granger](https://github.com/H-J-Granger), [akakw1](https://github.com/akakw1), [algosheep](https://github.com/algosheep), [Anguei](https://github.com/Anguei), [c-forrest](https://github.com/c-forrest), [felixesintot](https://github.com/felixesintot), [guodong2005](https://github.com/guodong2005), [HeRaNO](https://github.com/HeRaNO), [jpy-cpp](https://github.com/jpy-cpp), [kenlig](https://github.com/kenlig), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [sshwy](https://github.com/sshwy)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
