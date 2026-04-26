# 最小割 - OI Wiki

- Source: https://oi-wiki.org/graph/flow/min-cut/

# 最小割

## 概念

### 割

对于一个网络流图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其割的定义为一种 **点的划分方式** ：将所有的点划分为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇 =𝑉 −𝑆T=V−S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两个集合，其中源点 𝑠 ∈𝑆s∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，汇点 𝑡 ∈𝑇t∈T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 割的容量

我们的定义割 (𝑆,𝑇)(S,T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的容量 𝑐(𝑆,𝑇)c(S,T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示所有从 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边的容量之和，即 𝑐(𝑆,𝑇) =∑𝑢∈𝑆,𝑣∈𝑇𝑐(𝑢,𝑣)c(S,T)=∑u∈S,v∈Tc(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．当然我们也可以用 𝑐(𝑠,𝑡)c(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑐(𝑆,𝑇)c(S,T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 最小割

最小割就是求得一个割 (𝑆,𝑇)(S,T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得割的容量 𝑐(𝑆,𝑇)c(S,T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小．

## 证明

### 最大流最小割定理

参见 [最大流](../max-flow/) 页面最大流最小割定理一节．

## 代码

### 最小割

通过 **最大流最小割定理** ，我们可以直接得到如下代码：

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 ``` |  ```text #include <algorithm> #include <cstdio> #include <cstring> #include <queue> constexpr int N = 1e4 \+ 5 , M = 2e5 \+ 5 ; int n , m , s , t , tot = 1 , lnk [ N ], ter [ M ], nxt [ M ], val [ M ], dep [ N ], cur [ N ]; void add ( int u , int v , int w ) { ter [ ++ tot ] = v , nxt [ tot ] = lnk [ u ], lnk [ u ] = tot , val [ tot ] = w ; } void addedge ( int u , int v , int w ) { add ( u , v , w ), add ( v , u , 0 ); } int bfs ( int s , int t ) { memset ( dep , 0 , sizeof ( dep )); memcpy ( cur , lnk , sizeof ( lnk )); std :: queue < int > q ; q . push ( s ), dep [ s ] = 1 ; while ( ! q . empty ()) { int u = q . front (); q . pop (); for ( int i = lnk [ u ]; i ; i = nxt [ i ]) { int v = ter [ i ]; if ( val [ i ] && ! dep [ v ]) q . push ( v ), dep [ v ] = dep [ u ] \+ 1 ; } } return dep [ t ]; } int dfs ( int u , int t , int flow ) { if ( u == t ) return flow ; int ans = 0 ; for ( int & i = cur [ u ]; i && ans < flow ; i = nxt [ i ]) { int v = ter [ i ]; if ( val [ i ] && dep [ v ] == dep [ u ] \+ 1 ) { int x = dfs ( v , t , std :: min ( val [ i ], flow \- ans )); if ( x ) val [ i ] -= x , val [ i ^ 1 ] += x , ans += x ; } } if ( ans < flow ) dep [ u ] = -1 ; return ans ; } int dinic ( int s , int t ) { int ans = 0 ; while ( bfs ( s , t )) { int x ; while (( x = dfs ( s , t , 1 << 30 ))) ans += x ; } return ans ; } int main () { scanf ( "%d%d%d%d" , & n , & m , & s , & t ); while ( m \-- ) { int u , v , w ; scanf ( "%d%d%d" , & u , & v , & w ); addedge ( u , v , w ); } printf ( "%d \n " , dinic ( s , t )); return 0 ; } ```   
---|---  
  
### 方案

我们可以通过从源点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始 DFS，每次走残量大于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边，找到所有 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点集内的点．

```text 1 2 3 4 5 6 7 ``` |  ```text void dfs ( int u ) { vis [ u ] = 1 ; for ( int i = lnk [ u ]; i ; i = nxt [ i ]) { int v = ter [ i ]; if ( ! vis [ v ] && val [ i ]) dfs ( v ); } } ```   
---|---  
  
### 割边数量

如果需要在最小割的前提下最小化割边数量，那么先求出最小割，把没有满流的边容量改成 ∞∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满流的边容量改成 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，重新跑一遍最小割就可求出最小割边数量；如果没有最小割的前提，直接把所有边的容量设成 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求一遍最小割就好了．

## 问题模型 1

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品和两个集合 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果一个物品没有放入 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 集合会花费 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，没有放入 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 集合会花费 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；还有若干个形如 𝑢𝑖,𝑣𝑖,𝑤𝑖ui,vi,wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 限制条件，表示如果 𝑢𝑖ui![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同时不在一个集合会花费 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每个物品必须且只能属于一个集合，求最小的代价．

这是一个经典的 **二者选其一** 的最小割题目．我们对于每个集合设置源点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和汇点 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点由 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条容量为 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边、向 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条容量为 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边．对于限制条件 𝑢,𝑣,𝑤u,v,w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们在 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间连容量为 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的双向边．

注意到当源点和汇点不相连时，代表这些点都选择了其中一个集合．如果将连向 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边割开，表示不放在 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 集合，如果把物品之间的边割开，表示这两个物品不放在同一个集合．

最小割就是最小花费．

## 问题模型 2

最大权值闭合图，即给定一张有向图，每个点都有一个权值（可以为正或负或 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），你需要选择一个权值和最大的子图，使得子图中每个点的后继都在子图中．

做法：建立超级源点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和超级汇点 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若节点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 权值为正，则 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条有向边，边权即为该点点权；若节点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 权值为负，则由 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条有向边，边权即为该点点权的相反数．原图上所有边权改为 ∞∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．跑网络最大流，将所有正权值之和减去最大流，即为答案．

几个小结论来证明：

  1. 每一个符合条件的子图都对应流量网络中的一个割．因为每一个割将网络分为两部分，与 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连的那部分满足没有边指向另一部分，于是满足上述条件．这个命题是充要的．
  2. 最小割所去除的边必须与 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 其中一者相连．因为否则边权是 ∞∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不可能成为最小割．
  3. 我们所选择的那部分子图，权值和 ==![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所有正权值之和 −−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 我们未选择的正权值点的权值之和 ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 我们选择的负权值点的权值之和．当我们不选择一个正权值点时，其与 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连边会被断开；当我们选择一个负权值点时，其与 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连边会被断开．断开的边的边权之和即为割的容量．于是上述式子转化为：权值和 ==![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所有正权值之和 −−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 割的容量．
  4. 于是得出结论，最大权值和 ==![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所有正权值之和 −−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小割 ==![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所有正权值之和 −−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最大流．

## 习题

  * [「USACO 4.4」Pollutant Control](https://www.luogu.com.cn/problem/P1344)
  * [「USACO 5.4」Telecowmunication](https://www.luogu.com.cn/problem/P1345)
  * [「Luogu 1361」小 M 的作物](https://www.luogu.com.cn/problem/P1361)
  * [「SHOI 2007」善意的投票](https://www.luogu.com.cn/problem/P2057)
  * [太空飞行计划问题](https://www.luogu.com.cn/problem/P2762)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/flow/min-cut.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/flow/min-cut.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [MegaOwIer](https://github.com/MegaOwIer), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Henry-ZHR](https://github.com/Henry-ZHR), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [diauweb](https://github.com/diauweb), [huaruoji](https://github.com/huaruoji), [ImpleLee](https://github.com/ImpleLee), [laocongsc](https://github.com/laocongsc), [LuoYisu](https://github.com/LuoYisu), [Lynricsy](https://github.com/Lynricsy), [NachtgeistW](https://github.com/NachtgeistW), [Nanarikom](https://github.com/Nanarikom), [Siyuan](mailto:hydingsy@gmail.com)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
