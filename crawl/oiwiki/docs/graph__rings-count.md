# 环计数问题 - OI Wiki

- Source: https://oi-wiki.org/graph/rings-count/

# 环计数问题

## 普通环计数

[例题 1：Codeforces Beta Round 11 D. A Simple Task](https://codeforces.com/problemset/problem/11/D)

给定一个简单图，求图中简单环的数目．简单环是指没有重复顶点或边的环．

结点数目 1 ≤𝑛 ≤191≤n≤19![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解题思路

考虑状态压缩动态规划．记 𝑓(𝑠,𝑖)f(s,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示满足当前经过结点集合为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且现在在结点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上，且第一个结点为结点集合 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 **编号最小的那个** 的路径条数．

对于状态 𝑓(𝑠,𝑖)f(s,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，枚举下一个结点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在集合 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中且是编号最小的那个（即起点），就将答案 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加上 𝑓(𝑠,𝑖)f(s,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不在 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，就将 𝑓(𝑠,𝑖)f(s,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加上 𝑓(𝑠 ∪{𝑢},𝑢)f(s∪{u},u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这样会把二元环（即重边）也算上，并且每个非二元环会被计算两次（因为固定起点可以向两个方向走），所以答案为 𝐴−𝑚2A−m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示边数．时间复杂度 𝑂(2𝑛𝑚)O(2nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

示例代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``` |  ```text #include <iostream> using namespace std ; int n , m ; struct Edge { int to , nxt ; } edge [ 500 ]; int cntEdge , head [ 20 ]; void addEdge ( int u , int v ) { edge [ ++ cntEdge ] = { v , head [ u ]}, head [ u ] = cntEdge ; } long long answer , dp [ 1 << 19 ][ 20 ]; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m ; for ( int i = 1 ; i <= m ; i ++ ) { int u , v ; cin >> u >> v ; addEdge ( u , v ); addEdge ( v , u ); } for ( int i = 1 ; i <= n ; i ++ ) dp [ 1 << ( i \- 1 )][ i ] = 1 ; for ( int s = 1 ; s < ( 1 << n ); s ++ ) for ( int i = 1 ; i <= n ; i ++ ) { if ( ! dp [ s ][ i ]) continue ; for ( int j = head [ i ]; j ; j = edge [ j ]. nxt ) { int u = i , v = edge [ j ]. to ; if (( s & \- s ) > ( 1 << ( v \- 1 ))) continue ; if ( s & ( 1 << ( v \- 1 ))) { if (( s & \- s ) == ( 1 << ( v \- 1 ))) answer += dp [ s ][ u ]; } else dp [ s | ( 1 << ( v \- 1 ))][ v ] += dp [ s ][ u ]; } } cout << ( answer \- m ) / 2 << '\n' ; return 0 ; } ```   
---|---  
  
## 三元环计数

**三元环** 指的是一个简单图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的一个无序三元组 (𝑢, 𝑣, 𝑤)(u, v, w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足存在三条边分别连接 (𝑢, 𝑣)(u, v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，(𝑣, 𝑤)(v, w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑤, 𝑢)(w, u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而 **三元环计数问题** 要求计算出图中所有三元环的数量．

首先给所有边定向．我们规定从度数小的点指向度数大的点，度数相同就从编号小的点指向编号大的点．那么此时此图是一张有向无环图（DAG）．

该图没有环的证明

反证法，假设存在环，那么环中的点度数一个比一个大，要形成环，所有点的度数必须相等，但是编号必定不同，矛盾．

所以定向后图肯定不存在环．

事实上，可以根据上述定向规则构造一个 [偏序](../../math/order-theory/#二元关系)，所以按此规则构造的图（也即该偏序的 [Hasse 图](../../math/order-theory/#偏序集的可视化表示hasse-图)）一定是一个 DAG．

枚举 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指向的点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再在 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指向的点中枚举 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，检验 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否与 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连即可．

这个算法的时间复杂度为 𝑂(𝑚√𝑚)O(mm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

时间复杂度证明

对于定向部分，遍历了所有的边，时间复杂度 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于每一对 (𝑣, 𝑤)(v, w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量都不超过 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的入度 𝑑−(𝑣)d−(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

若 𝑑−(𝑣) ≤√𝑚d−(v)≤m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由于 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数至多为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以这部分时间复杂度为 𝑂(𝑛√𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

若 𝑑−(𝑣) >√𝑚d−(v)>m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由于 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指向 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑑(𝑣) ≤𝑑(𝑤)d(v)≤d(w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得出 𝑑(𝑤) >√𝑚d(w)>m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是总边数只有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以这样的 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数至多为 √𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故时间复杂度为 𝑂(𝑚√𝑚)O(mm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

总时间复杂度为 𝑂(𝑛 +𝑚 +𝑛√𝑚 +𝑚√𝑚) =𝑂(𝑚√𝑚)O(n+m+nm+mm)=O(mm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

事实上，如果定向时从度数大的点指向度数小的点，复杂度也正确，只需要交换 𝑢, 𝑤u, w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两个点，上述证明也成立．

示例代码（[洛谷 P1989 无向图三元环计数](https://www.luogu.com.cn/problem/P1989)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` |  ```text #include <iostream> using namespace std ; int n , m , total ; int deg [ 200001 ], u [ 200001 ], v [ 200001 ]; bool vis [ 200001 ]; struct Edge { int to , nxt ; } edge [ 200001 ]; int cntEdge , head [ 100001 ]; void addEdge ( int u , int v ) { edge [ ++ cntEdge ] = { v , head [ u ]}, head [ u ] = cntEdge ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m ; for ( int i = 1 ; i <= m ; i ++ ) cin >> u [ i ] >> v [ i ], deg [ u [ i ]] ++ , deg [ v [ i ]] ++ ; for ( int i = 1 ; i <= m ; i ++ ) { if (( deg [ u [ i ]] == deg [ v [ i ]] && u [ i ] > v [ i ]) || deg [ u [ i ]] < deg [ v [ i ]]) swap ( u [ i ], v [ i ]); addEdge ( u [ i ], v [ i ]); } for ( int u = 1 ; u <= n ; u ++ ) { for ( int i = head [ u ]; i ; i = edge [ i ]. nxt ) vis [ edge [ i ]. to ] = true ; for ( int i = head [ u ]; i ; i = edge [ i ]. nxt ) { int v = edge [ i ]. to ; for ( int j = head [ v ]; j ; j = edge [ j ]. nxt ) { int w = edge [ j ]. to ; if ( vis [ w ]) total ++ ; } } for ( int i = head [ u ]; i ; i = edge [ i ]. nxt ) vis [ edge [ i ]. to ] = false ; } cout << total << '\n' ; return 0 ; } ```   
---|---  
  
### 例题 2

[HDU 6184 Counting Stars](https://acm.hdu.edu.cn/showproblem.php?pid=6184)

给定一张有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点和 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边的无向图，求下面图形的出现次数．

![](./images/rings-count1.svg)

2 ≤𝑛 ≤1052≤n≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑚 ≤min{2×105, 𝑛(𝑛−1)2}1≤m≤min{2×105, n(n−1)2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解题思路

这个图形是两个三元环共用了一条边形成的．所以我们先跑一遍三元环计数，统计出一条边上三元环的数量，然后枚举共用的那条边，设有 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个三元环中有此边，那么对答案的贡献就是 (𝑥2)(x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

时间复杂度 𝑂(𝑚√𝑚)O(mm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

示例代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 ``` |  ```text #include <cstring> #include <iostream> using namespace std ; int n , m , total ; int deg [ 200001 ], u [ 200001 ], v [ 200001 ]; int edgeId [ 200001 ], cnt [ 200001 ]; struct Edge { int to , nxt ; } edge [ 200001 ]; int cntEdge , head [ 100001 ]; void addEdge ( int u , int v ) { edge [ ++ cntEdge ] = { v , head [ u ]}, head [ u ] = cntEdge ; } int main () { while ( cin >> n >> m ) { cntEdge = total = 0 ; memset ( deg , 0 , sizeof deg ); memset ( head , 0 , sizeof head ); for ( int i = 1 ; i <= m ; i ++ ) cin >> u [ i ] >> v [ i ], deg [ u [ i ]] ++ , deg [ v [ i ]] ++ ; for ( int i = 1 ; i <= m ; i ++ ) { if (( deg [ u [ i ]] == deg [ v [ i ]] && u [ i ] > v [ i ]) || deg [ u [ i ]] < deg [ v [ i ]]) swap ( u [ i ], v [ i ]); addEdge ( u [ i ], v [ i ]); } for ( int u = 1 ; u <= n ; u ++ ) { for ( int i = head [ u ]; i ; i = edge [ i ]. nxt ) edgeId [ edge [ i ]. to ] = i ; for ( int i = head [ u ]; i ; i = edge [ i ]. nxt ) { int v = edge [ i ]. to ; for ( int j = head [ v ]; j ; j = edge [ j ]. nxt ) { int w = edge [ j ]. to ; if ( edgeId [ w ]) cnt [ i ] ++ , cnt [ j ] ++ , cnt [ edgeId [ w ]] ++ ; } } for ( int i = head [ u ]; i ; i = edge [ i ]. nxt ) edgeId [ edge [ i ]. to ] = 0 ; } for ( int i = 1 ; i <= m ; i ++ ) total += cnt [ i ] * ( cnt [ i ] \- 1 ) / 2 , cnt [ i ] = 0 ; cout << total << '\n' ; } return 0 ; } ```   
---|---  
  
## 四元环计数

类似地，**四元环** 就是指四个点 𝑎, 𝑏, 𝑐, 𝑑a, b, c, d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 (𝑎, 𝑏)(a, b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，(𝑏, 𝑐)(b, c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，(𝑐, 𝑑)(c, d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑑, 𝑎)(d, a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均有边连接．

考虑先对点进行排序．度数小的排在前面，度数大的排在后面．

考虑枚举排在最后面的点 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时只需要对于每个比 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 排名更前的点 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都求出有多少个排名比 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前的点 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 (𝑎, 𝑏)(a, b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，(𝑏, 𝑐)(b, c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有边．然后只需要从这些 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中任取两个都能成为一个四元环．求 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量只需要遍历一遍 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

注意到我们枚举的复杂度本质上与枚举三元环等价，所以时间复杂度也是 𝑂(𝑚√𝑚)O(mm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（假设 𝑛, 𝑚n, m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同阶）．

值得注意的是，(𝑎, 𝑏, 𝑐, 𝑑)(a, b, c, d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑎, 𝑐, 𝑏, 𝑑)(a, c, b, d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以是两个不同的四元环．

另外，度数相同的结点的排名将不相同，并且需要注意判断 𝑎 ≠𝑐a≠c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

示例代码（[LibreOJ P191 无向图四元环计数](https://loj.ac/p/191)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``` |  ```text #include <iostream> #include <vector> using namespace std ; int n , m , deg [ 100001 ], cnt [ 100001 ]; vector < int > E [ 100001 ], E1 [ 100001 ]; long long total ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m ; for ( int i = 1 ; i <= m ; i ++ ) { int u , v ; cin >> u >> v ; E [ u ]. push_back ( v ); E [ v ]. push_back ( u ); deg [ u ] ++ , deg [ v ] ++ ; } for ( int u = 1 ; u <= n ; u ++ ) for ( int v : E [ u ]) if ( deg [ u ] > deg [ v ] || ( deg [ u ] == deg [ v ] && u > v )) E1 [ u ]. push_back ( v ); for ( int a = 1 ; a <= n ; a ++ ) { for ( int b : E1 [ a ]) for ( int c : E [ b ]) { if ( deg [ a ] < deg [ c ] || ( deg [ a ] == deg [ c ] && a <= c )) continue ; total += cnt [ c ] ++ ; } for ( int b : E1 [ a ]) for ( int c : E [ b ]) cnt [ c ] = 0 ; } cout << total << '\n' ; return 0 ; } ```   
---|---  
  
### 例题 3

[Gym 102028L Connected Subgraphs](https://codeforces.com/gym/102028/problem/L)

给定一张有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点和 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边的无向图，求四条边的导出子图连通的情况数．

4 ≤𝑛 ≤1054≤n≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，4 ≤𝑚 ≤2 ×1054≤m≤2×105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解题思路

容易把情况分为五种：菊花图、四元环、三元环上一个点连出一条边、四个点构成的链中间一个点连出一条边以及五个点构成的链．

菊花图直接枚举点的度数，用组合数解决即可．四元环可以直接按照上述算法求得．三元环部分只需枚举三元环 (𝑢, 𝑣, 𝑤)(u, v, w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么对答案的贡献就是 [𝑑(𝑢) −2] +[𝑑(𝑣) −2] +[𝑑(𝑤) −2][d(u)−2]+[d(v)−2]+[d(w)−2]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

下面考虑第四种情况．考虑枚举度数为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再枚举与它相邻的一个结点 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为度数为 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的那个点．此时对答案的贡献为 [𝑑(𝑥) −1] ⋅(𝑑(𝑦)−12)[d(x)−1]⋅(d(y)−12)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是注意到 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的相邻节点可能会和 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的相邻结点重合，此时的图形等价于第三种情况．但是每种多算的第三种情况都会被多算两次（因为有两个度数为 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点），所以应该减去第三种情况数目的两倍．

对于最后一种情况，先枚举中间的点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么容易发现对答案的贡献是

∑𝑦∈𝑠𝑜𝑛𝑥∑𝑧∈𝑠𝑜𝑛𝑥[𝑑(𝑦)−1]⋅[𝑑(𝑧)−1].∑y∈sonx∑z∈sonx[d(y)−1]⋅[d(z)−1].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

同样地，这其中有多算的部分．设 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的相邻结点为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的相邻结点为 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么思考后发现多算的有如下几种情况：

  1. 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 重合，但是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不重合时，等价于第三种情况；
  2. 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 重合，但是 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不重合时，同样等价于第三种情况；
  3. 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都重合时，等价于一个三元环；
  4. 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 重合时，等价于一个四元环（第二种情况）．

考虑到第三种情况中两个度数 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点作为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时正好分别对应上述多算情况的 1 和 2，所以要额外减去第三种情况数目的两倍．对于一个三元环，三个结点都可以作为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，多算了 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．同样的，四元环的情况被多算了 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．

于是我们就得出了所有情况的算法，时间复杂度为 𝑂(𝑛 +𝑚√𝑚)O(n+mm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

示例代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 ``` |  ```text #include <iostream> #include <vector> using namespace std ; constexpr int mod = 1000000007 ; constexpr long long power ( long long a , long long n = mod \- 2 ) { long long res = 1 ; while ( n ) { if ( n & 1 ) res = res * a % mod ; a = a * a % mod ; n >>= 1 ; } return res ; } constexpr long long power24 = power ( 24 ), power2 = power ( 2 ); int n , m ; vector < int > E [ 100001 ], E1 [ 100001 ], E2 [ 100001 ]; bool vis [ 100001 ]; int cnt1 [ 100001 ], cnt2 [ 100001 ]; long long solve1 (); long long solve2 (); long long solve3 (); long long solve4 (); long long solve5 (); long long ans [ 6 ]; long long solve1 () { if ( ans [ 1 ] != -1 ) return ans [ 1 ]; ans [ 1 ] = 0 ; for ( int i = 1 ; i <= n ; i ++ ) { int x = E [ i ]. size (); ans [ 1 ] += 1l l * x * ( x \- 1 ) % mod * ( x \- 2 ) % mod * ( x \- 3 ) % mod * power24 % mod ; } return ans [ 1 ] %= mod ; } long long solve2 () { if ( ans [ 2 ] != -1 ) return ans [ 2 ]; ans [ 2 ] = 0 ; for ( int i = 1 ; i <= n ; i ++ ) { for ( int j : E1 [ i ]) for ( int k : E1 [ j ]) cnt1 [ k ] ++ ; for ( int j : E2 [ i ]) for ( int k : E1 [ j ]) if ( k != i ) cnt2 [ k ] ++ ; for ( int j : E1 [ i ]) for ( int k : E1 [ j ]) ans [ 2 ] += ( 1l l * cnt1 [ k ] * ( cnt1 [ k ] \- 1 ) / 2 \+ 1l l * cnt1 [ k ] * cnt2 [ k ]) % mod , cnt1 [ k ] = 0 ; for ( int j : E2 [ i ]) for ( int k : E1 [ j ]) if ( k != i ) ans [ 2 ] += 1l l * cnt2 [ k ] * ( cnt2 [ k ] \- 1 ) / 2 % mod * power2 % mod , cnt2 [ k ] = 0 ; } return ans [ 2 ]; } long long solve3 () { if ( ans [ 3 ] != -1 ) return ans [ 3 ]; ans [ 0 ] = ans [ 3 ] = 0 ; for ( int i = 1 ; i <= n ; i ++ ) { for ( int j : E1 [ i ]) vis [ j ] = true ; for ( int j : E1 [ i ]) for ( int k : E1 [ j ]) if ( vis [ k ]) ans [ 3 ] = ( 1l l * ans [ 3 ] \+ E [ i ]. size () \+ E [ j ]. size () \+ E [ k ]. size () \- 6 ) % mod , ans [ 0 ] ++ ; for ( int j : E1 [ i ]) vis [ j ] = false ; } return ans [ 3 ]; } long long solve4 () { if ( ans [ 4 ] != -1 ) return ans [ 4 ]; ans [ 4 ] = 0 ; for ( int i = 1 ; i <= n ; i ++ ) for ( int j : E [ i ]) ( ans [ 4 ] += 1l l * ( E [ j ]. size () \- 1 ) * ( E [ j ]. size () \- 2 ) / 2 * ( E [ i ]. size () \- 1 ) % mod ) %= mod ; return ans [ 4 ] = ( ans [ 4 ] \- 2 * solve3 ()) % mod ; } long long solve5 () { if ( ans [ 5 ] != -1 ) return ans [ 5 ]; ans [ 5 ] = 0 ; for ( int i = 1 ; i <= n ; i ++ ) { long long sum = 0 ; for ( int j : E [ i ]) { ans [ 5 ] += sum * ( E [ j ]. size () \- 1 ) % mod ; sum += E [ j ]. size () \- 1 ; } } solve3 (); return ans [ 5 ] = ( ans [ 5 ] % mod \- 2 * solve3 () \- 4 * solve2 () \- 3 * ans [ 0 ]) % mod ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int T ; cin >> T ; while ( T \-- ) { ans [ 5 ] = ans [ 1 ] = ans [ 2 ] = ans [ 4 ] = ans [ 3 ] = -1 ; cin >> n >> m ; for ( int i = 1 ; i <= n ; i ++ ) E [ i ]. clear (), E1 [ i ]. clear (), E2 [ i ]. clear (); while ( m \-- ) { int x , y ; cin >> x >> y ; E [ x ]. push_back ( y ), E [ y ]. push_back ( x ); } for ( int i = 1 ; i <= n ; i ++ ) for ( int j : E [ i ]) { if ( make_pair ( E [ i ]. size (), i ) < make_pair ( E [ j ]. size (), j )) E1 [ i ]. push_back ( j ); else E2 [ i ]. push_back ( j ); } cout << (( solve5 () \+ solve1 () \+ solve2 () \+ solve4 () \+ solve3 ()) % mod \+ mod ) % mod << '\n' ; } return 0 ; } ```   
---|---  
  
## 习题

[洛谷 P3547 [POI2013] CEN-Price List](https://www.luogu.com.cn/problem/P3547)

[CodeForces 985G Team Players](https://codeforces.com/contest/985/problem/G)（容斥原理）

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/rings-count.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/rings-count.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [megakite](https://github.com/megakite), [Molmin](https://github.com/Molmin), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [untitledunrevised](https://github.com/untitledunrevised)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
