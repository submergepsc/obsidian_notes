# 有向无环图 - OI Wiki

- Source: https://oi-wiki.org/graph/dag/

# 有向无环图

## 定义

边有向，无环．

英文名叫 Directed Acyclic Graph，缩写是 DAG．

## 性质

  * 能 [拓扑排序](../topo/) 的图，一定是有向无环图；

如果有环，那么环上的任意两个节点在任意序列中都不满足条件了．

  * 有向无环图，一定能拓扑排序；

（归纳法）假设节点数不超过 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 有向无环图都能拓扑排序，那么对于节点数等于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，考虑执行拓扑排序第一步之后的情形即可．

## 判定

如何判定一个图是否是有向无环图呢？

检验它是否可以进行 [拓扑排序](../topo/) 即可．

当然也有另外的方法，可以对图进行一遍 [DFS](../../search/dfs/)，在得到的 DFS 树上看看有没有连向祖先的非树边（返祖边）．如果有的话，那就有环了．

## 应用

### DP 求最长（短）路

在一般图上，求单源最长（短）路径的最优时间复杂度为 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（[Bellman–Ford 算法](../shortest-path/#bellmanford-算法)，适用于有负权图）或 𝑂(𝑚log⁡𝑚)O(mlog⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（[Dijkstra 算法](../shortest-path/#dijkstra-算法)，适用于无负权图）．

但在 DAG 上，我们可以使用 DP 求最长（短）路，使时间复杂度优化到 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．状态转移方程为 𝑑𝑖𝑠𝑣 =𝑚𝑖𝑛(𝑑𝑖𝑠𝑣,𝑑𝑖𝑠𝑢 +𝑤𝑢,𝑣)disv=min(disv,disu+wu,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑑𝑖𝑠𝑣 =𝑚𝑎𝑥(𝑑𝑖𝑠𝑣,𝑑𝑖𝑠𝑢 +𝑤𝑢,𝑣)disv=max(disv,disu+wu,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

拓扑排序后，按照拓扑序遍历每个节点，用当前节点来更新之后的节点．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` |  ```text struct edge { int v , w ; }; int n , m ; vector < edge > e [ MAXN ]; vector < int > L ; // 存储拓扑排序结果 int max_dis [ MAXN ], min_dis [ MAXN ], in [ MAXN ]; // in 存储每个节点的入度 void toposort () { // 拓扑排序 queue < int > S ; memset ( in , 0 , sizeof ( in )); for ( int i = 1 ; i <= n ; i ++ ) { for ( int j = 0 ; j < e [ i ]. size (); j ++ ) { in [ e [ i ][ j ]. v ] ++ ; } } for ( int i = 1 ; i <= n ; i ++ ) if ( in [ i ] == 0 ) S . push ( i ); while ( ! S . empty ()) { int u = S . front (); S . pop (); L . push_back ( u ); for ( int i = 0 ; i < e [ u ]. size (); i ++ ) { if ( \-- in [ e [ u ][ i ]. v ] == 0 ) { S . push ( e [ u ][ i ]. v ); } } } } void dp ( int s ) { // 以 s 为起点求单源最长（短）路 toposort (); // 先进行拓扑排序 memset ( min_dis , 0x3f , sizeof ( min_dis )); memset ( max_dis , 0 , sizeof ( max_dis )); min_dis [ s ] = 0 ; for ( int i = 0 ; i < L . size (); i ++ ) { int u = L [ i ]; for ( int j = 0 ; j < e [ u ]. size (); j ++ ) { min_dis [ e [ u ][ j ]. v ] = min ( min_dis [ e [ u ][ j ]. v ], min_dis [ u ] \+ e [ u ][ j ]. w ); max_dis [ e [ u ][ j ]. v ] = max ( max_dis [ e [ u ][ j ]. v ], max_dis [ u ] \+ e [ u ][ j ]. w ); } } } ```   
---|---  
  
参见：[DAG 上的 DP](../../dp/dag/)．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/dag.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/dag.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [ouuan](https://github.com/ouuan), [Tiphereth-A](https://github.com/Tiphereth-A), [billchenchina](https://github.com/billchenchina), [dong628](https://github.com/dong628), [HeRaNO](https://github.com/HeRaNO)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
