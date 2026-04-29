# 图的存储 - OI Wiki

- Source: https://oi-wiki.org/graph/save/

# 图的存储

在 OI 中，想要对图进行操作，就需要先学习图的存储方式．

## 约定

本文默认读者已阅读并了解了 [图论相关概念](../concept/) 中的基础内容，如果在阅读中遇到困难，也可以在 [图论相关概念](../concept/) 中进行查阅．

在本文中，用 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代指图的点数，用 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代指图的边数，用 𝑑+(𝑢)d+(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代指点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的出度，即以 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为出发点的边数．

## 直接存边

### 方法

使用一个数组来存边，数组中的每个元素都包含一条边的起点与终点（带边权的图还包含边权）．（或者使用多个数组分别存起点，终点和边权．）

参考代码

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 ``` |  ```text #include <iostream> #include <vector> using namespace std ; struct Edge { int u , v ; }; int n , m ; vector < Edge > e ; vector < bool > vis ; bool find_edge ( int u , int v ) { for ( int i = 1 ; i <= m ; ++ i ) { if ( e [ i ]. u == u && e [ i ]. v == v ) { return true ; } } return false ; } void dfs ( int u ) { if ( vis [ u ]) return ; vis [ u ] = true ; for ( int i = 1 ; i <= m ; ++ i ) { if ( e [ i ]. u == u ) { dfs ( e [ i ]. v ); } } } int main () { cin >> n >> m ; vis . resize ( n \+ 1 , false ); e . resize ( m \+ 1 ); for ( int i = 1 ; i <= m ; ++ i ) cin >> e [ i ]. u >> e [ i ]. v ; return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` |  ```text class Edge : def __init__ ( self , u = 0 , v = 0 ): self . u = u self . v = v n , m = map ( int , input () . split ()) e = [ Edge () for _ in range ( m )] vis = [ False ] * n for i in range ( m ): e [ i ] . u , e [ i ] . v = map ( int , input () . split ()) def find_edge ( u , v ): for i in range ( m ): if e [ i ] . u == u and e [ i ] . v == v : return True return False def dfs ( u ): if vis [ u ]: return vis [ u ] = True for i in range ( m ): if e [ i ] . u == u : dfs ( e [ i ] . v ) ```   
---|---  
  
### 复杂度

查询是否存在某条边：𝑂(𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

遍历一个点的所有出边：𝑂(𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

遍历整张图：𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

空间复杂度：𝑂(𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 应用

由于直接存边的遍历效率低下，一般不用于遍历图．

在 [Kruskal 算法](../mst/#kruskal-算法) 中，由于需要将边按边权排序，需要直接存边．

在有的题目中，需要多次建图（如建一遍原图，建一遍反图），此时既可以使用多个其它数据结构来同时存储多张图，也可以将边直接存下来，需要重新建图时利用直接存下的边来建图．

## 邻接矩阵

### 方法

使用一个二维数组 `adj` 来存边，其中 `adj[u][v]` 为 1 表示存在 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边，为 0 表示不存在．如果是带边权的图，可以在 `adj[u][v]` 中存储 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边的边权．

参考代码

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` |  ```text #include <iostream> #include <vector> using namespace std ; int n , m ; vector < bool > vis ; vector < vector < bool >> adj ; bool find_edge ( int u , int v ) { return adj [ u ][ v ]; } void dfs ( int u ) { if ( vis [ u ]) return ; vis [ u ] = true ; for ( int v = 1 ; v <= n ; ++ v ) { if ( adj [ u ][ v ]) { dfs ( v ); } } } int main () { cin >> n >> m ; vis . resize ( n \+ 1 ); adj . resize ( n \+ 1 , vector < bool > ( n \+ 1 )); for ( int i = 1 ; i <= m ; ++ i ) { int u , v ; cin >> u >> v ; adj [ u ][ v ] = true ; } return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text vis = [ False ] * ( n \+ 1 ) adj = [[ False ] * ( n \+ 1 ) for _ in range ( n \+ 1 )] for i in range ( 1 , m \+ 1 ): u , v = map ( lambda x : int ( x ), input () . split ()) adj [ u ][ v ] = True def find_edge ( u , v ): return adj [ u ][ v ] def dfs ( u ): if vis [ u ]: return vis [ u ] = True for v in range ( 1 , n \+ 1 ): if adj [ u ][ v ]: dfs ( v ) ```   
---|---  
  
### 复杂度

查询是否存在某条边：𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

遍历一个点的所有出边：𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

遍历整张图：𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

空间复杂度：𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 应用

邻接矩阵只适用于没有重边（或重边可以忽略）的情况．

其最显著的优点是可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 查询一条边是否存在．

由于邻接矩阵在稀疏图上效率很低（尤其是在点数较多的图上，空间无法承受），所以一般只会在稠密图上使用邻接矩阵．

## 邻接表

### 方法

使用一个支持动态增加元素的数据结构构成的数组，如 `vector<int> adj[n + 1]` 来存边，其中 `adj[u]` 存储的是点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有出边的相关信息（终点、边权等）．

参考代码

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``` |  ```text #include <iostream> #include <vector> using namespace std ; int n , m ; vector < bool > vis ; vector < vector < int >> adj ; bool find_edge ( int u , int v ) { for ( int i = 0 ; i < adj [ u ]. size (); ++ i ) { if ( adj [ u ][ i ] == v ) { return true ; } } return false ; } void dfs ( int u ) { if ( vis [ u ]) return ; vis [ u ] = true ; for ( int i = 0 ; i < adj [ u ]. size (); ++ i ) dfs ( adj [ u ][ i ]); } int main () { cin >> n >> m ; vis . resize ( n \+ 1 ); adj . resize ( n \+ 1 ); for ( int i = 1 ; i <= m ; ++ i ) { int u , v ; cin >> u >> v ; adj [ u ]. push_back ( v ); } return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text vis = [ False ] * ( n \+ 1 ) adj = [[] for _ in range ( n \+ 1 )] for i in range ( 1 , m \+ 1 ): u , v = map ( lambda x : int ( x ), input () . split ()) adj [ u ] . append ( v ) def find_edge ( u , v ): for i in range ( 0 , len ( adj [ u ])): if adj [ u ][ i ] == v : return True return False def dfs ( u ): if vis [ u ]: return vis [ u ] = True for i in range ( 0 , len ( adj [ u ])): dfs ( adj [ u ][ i ]) ```   
---|---  
  
### 复杂度

查询是否存在 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边：𝑂(𝑑+(𝑢))O(d+(u))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（如果事先进行了排序就可以使用 [二分查找](../../basic/binary/) 做到 𝑂(log⁡(𝑑+(𝑢)))O(log⁡(d+(u)))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

遍历点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有出边：𝑂(𝑑+(𝑢))O(d+(u))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

遍历整张图：𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

空间复杂度：𝑂(𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 应用

存各种图都很适合，除非有特殊需求（如需要快速查询一条边是否存在，且点数较少，可以使用邻接矩阵）．

尤其适用于需要对一个点的所有出边进行排序的场合．

## 链式前向星

### 方法

本质上是用链表实现的邻接表，核心代码如下：

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text // head[u] 和 cnt 的初始值都为 -1 void add ( int u , int v ) { nxt [ ++ cnt ] = head [ u ]; // 当前边的后继 head [ u ] = cnt ; // 起点 u 的第一条边 to [ cnt ] = v ; // 当前边的终点 } // 遍历 u 的出边 for ( int i = head [ u ]; ~ i ; i = nxt [ i ]) { // ~i 表示 i != -1 int v = to [ i ]; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text # head[u] 和 cnt 的初始值都为 -1 def add ( u , v ): cnt = cnt \+ 1 nex [ cnt ] = head [ u ] # 当前边的后继 head [ u ] = cnt # 起点 u 的第一条边 to [ cnt ] = v # 当前边的终点 # 遍历 u 的出边 i = head [ u ] while ~ i : # ~i 表示 i != -1 v = to [ i ] i = nxt [ i ] ```   
---|---  
  
参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` |  ```text #include <iostream> #include <vector> using namespace std ; int n , m ; vector < bool > vis ; vector < int > head , nxt , to ; void add ( int u , int v ) { nxt . push_back ( head [ u ]); head [ u ] = to . size (); to . push_back ( v ); } bool find_edge ( int u , int v ) { for ( int i = head [ u ]; ~ i ; i = nxt [ i ]) { // ~i 表示 i != -1 if ( to [ i ] == v ) { return true ; } } return false ; } void dfs ( int u ) { if ( vis [ u ]) return ; vis [ u ] = true ; for ( int i = head [ u ]; ~ i ; i = nxt [ i ]) dfs ( to [ i ]); } int main () { cin >> n >> m ; vis . resize ( n \+ 1 , false ); head . resize ( n \+ 1 , -1 ); for ( int i = 1 ; i <= m ; ++ i ) { int u , v ; cin >> u >> v ; add ( u , v ); } return 0 ; } ```   
---|---  
  
### 复杂度

查询是否存在 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边：𝑂(𝑑+(𝑢))O(d+(u))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

遍历点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有出边：𝑂(𝑑+(𝑢))O(d+(u))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

遍历整张图：𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

空间复杂度：𝑂(𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 应用

存各种图都很适合，但不能快速查询一条边是否存在，也不能方便地对一个点的出边进行排序．

优点是边是带编号的，有时会非常有用，而且如果 `cnt` 的初始值为奇数，存双向边时 `i ^ 1` 即是 `i` 的反边（常用于 [网络流](../flow/)）．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/save.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/save.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [ouuan](https://github.com/ouuan), [ImpleLee](https://github.com/ImpleLee), [Menci](https://github.com/Menci), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [Anguei](https://github.com/Anguei), [billchenchina](https://github.com/billchenchina), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [partychicken](https://github.com/partychicken), [shawlleyw](https://github.com/shawlleyw), [shenshuaijie](https://github.com/shenshuaijie), [sshwy](https://github.com/sshwy), [zhu-yifang](https://github.com/zhu-yifang), [zychen20](https://github.com/zychen20)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
