# A* - OI Wiki

- Source: https://oi-wiki.org/search/astar/

# A*

本文介绍 A* 搜索算法．

A* 搜索算法（A* search algorithm，A* 读作 A-star），简称 A* 算法，是一种在带权有向图上，找到给定起点与终点之间的最短路径的算法．它属于图遍历（graph traversal）和最佳优先搜索算法（best-first search），亦是 [BFS](../bfs/) 的改进．

## 过程

A* 算法的目标是找到有向图上从起点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到终点 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短路径．设 𝑑(𝑥,𝑦)d(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的距离，也就是它们之间最短路径的长度．记 𝑔(𝑥) =𝑑(𝑠,𝑥)g(x)=d(s,x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为从起点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的距离函数，ℎ∗(𝑥)h∗(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为从结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到终点 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的距离函数，ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 ℎ∗(𝑥)h∗(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个估计1．最后，记从 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发经由 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到达 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短路径长度的估计为

𝑓(𝑥)=𝑔(𝑥)+ℎ(𝑥).f(x)=g(x)+h(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

搜索时，A* 算法每次从优先队列中取出一个 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小的结点．然后，将它的所有后继结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都推入优先队列中，并利用实际记录的 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和估计的 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更新 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 性质

由于 ℎ∗(𝑥)h∗(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的实际值在搜索的时候是未知的，所以，需要使用容易计算的 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为它的估计．A* 搜索的实际复杂度就取决于这一估计函数 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的性质．容易想象，如果 ℎ ≡ℎ∗h≡h∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，估计是精确的，那么，搜索过程就会严格按照最短路径前进．而如果 ℎ ≡0h≡0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，A* 算法就退化为 [Dijkstra 算法](../../graph/shortest-path/#dijkstra-算法)；当 ℎ ≡0h≡0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并且边权为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，这就是 [BFS](../bfs/)．

假设图没有负权边．如果估计 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 永远不超过实际距离 ℎ∗(𝑥)h∗(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 0 ≤ℎ ≤ℎ∗0≤h≤h∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，A* 算法就一定能够找到最优解．满足这一条件的估计函数 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 **可采纳的** （admissible）．根据前文的讨论，ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 越接近 ℎ∗h∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，相应的 A* 算法效率就越高．一般来说，在最差情形中，算法会经过所有满足

𝑓(𝑥)=𝑔(𝑥)+ℎ(𝑥)≤𝐶∗f(x)=g(x)+h(x)≤C∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的结点，其中，𝐶∗C∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是起点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和终点 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的最短距离．直觉上，ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 越接近 ℎ∗h∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每次扩展时，能够满足该条件的后继结点就越少，因此，算法搜索到的分支就越少．所以，A* 算法可以看作是对搜索算法的一种「剪枝」优化．

如果 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不仅是可采纳的，还是 **一致的** （consistent），即

ℎ(𝑥)≤ℎ(𝑦)+𝑑(𝑥,𝑦),h(x)≤h(y)+d(x,y),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么，A* 算法不会将已经弹出队列的结点再次加入队列．一致性条件，可以理解为结点 𝑥,𝑦,𝑡x,y,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的三角形不等式．

## 例题

A* 算法的一个经典应用是解决 k 短路问题．关于该问题的描述、A* 做法，以及复杂度更优的可持久化可并堆做法，请移步 [k 短路问题](../../graph/kth-path/) 页面．

本节介绍一个可以用 A* 算法解决的经典问题．

[八数码](https://www.luogu.com.cn/problem/P1379)

在 3 ×33×3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的棋盘上，摆有八个棋子，每个棋子上标有 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的某一数字．棋盘中留有一个空格，空格用 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来表示．空格周围的棋子可以移到空格中，这样原来的位置就会变成空格．给出一种初始布局和目标布局（为了使题目简单，设目标状态如下），找到一种从初始布局到目标布局最少步骤的移动方法．

123804765123804765![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)解题思路

ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 函数可以定义为，不在应该在的位置的棋子个数．容易发现，ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既是可采纳的，也是一致的．此题可以使用 A* 算法求解．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 ``` |  ```text #include <algorithm> #include <cstring> #include <iostream> #include <queue> #include <set> using namespace std ; constexpr int dx [ 4 ] = { 1 , -1 , 0 , 0 }, dy [ 4 ] = { 0 , 0 , 1 , -1 }; int fx , fy ; char ch ; struct matrix { int a [ 5 ][ 5 ]; bool operator < ( matrix x ) const { for ( int i = 1 ; i <= 3 ; i ++ ) for ( int j = 1 ; j <= 3 ; j ++ ) if ( a [ i ][ j ] != x . a [ i ][ j ]) return a [ i ][ j ] < x . a [ i ][ j ]; return false ; } } f , st ; int h ( matrix a ) { int ret = 0 ; for ( int i = 1 ; i <= 3 ; i ++ ) for ( int j = 1 ; j <= 3 ; j ++ ) if ( a . a [ i ][ j ] != st . a [ i ][ j ] && a . a [ i ][ j ] != 0 ) ret ++ ; return ret ; } struct node { matrix a ; int t ; bool operator < ( node x ) const { return t \+ h ( a ) > x . t \+ h ( x . a ); } } x ; priority_queue < node > q ; // 搜索队列 set < matrix > s ; // 防止搜索队列重复 int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); st . a [ 1 ][ 1 ] = 1 ; // 定义标准表 st . a [ 1 ][ 2 ] = 2 ; st . a [ 1 ][ 3 ] = 3 ; st . a [ 2 ][ 1 ] = 8 ; st . a [ 2 ][ 2 ] = 0 ; st . a [ 2 ][ 3 ] = 4 ; st . a [ 3 ][ 1 ] = 7 ; st . a [ 3 ][ 2 ] = 6 ; st . a [ 3 ][ 3 ] = 5 ; for ( int i = 1 ; i <= 3 ; i ++ ) // 输入 for ( int j = 1 ; j <= 3 ; j ++ ) { cin >> ch ; f . a [ i ][ j ] = ch \- '0' ; } s . insert ( f ); q . push ({ f , 0 }); while ( ! q . empty ()) { x = q . top (); q . pop (); if ( ! h ( x . a )) { // 判断是否与标准矩阵一致 cout << x . t << '\n' ; return 0 ; } for ( int i = 1 ; i <= 3 ; i ++ ) for ( int j = 1 ; j <= 3 ; j ++ ) if ( ! x . a . a [ i ][ j ]) fx = i , fy = j ; // 查找空格子（0号点）的位置 for ( int i = 0 ; i < 4 ; i ++ ) { // 对四种移动方式分别进行搜索 int xx = fx \+ dx [ i ], yy = fy \+ dy [ i ]; if ( 1 <= xx && xx <= 3 && 1 <= yy && yy <= 3 ) { swap ( x . a . a [ fx ][ fy ], x . a . a [ xx ][ yy ]); if ( ! s . count ( x . a )) s . insert ( x . a ), q . push ({ x . a , x . t \+ 1 }); // 这样移动后，将新的情况放入搜索队列中 swap ( x . a . a [ fx ][ fy ], x . a . a [ xx ][ yy ]); // 如果不这样移动的情况 } } } return 0 ; } ```   
---|---  
  
## 参考资料与注释

  * [A* search algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)

* * *

  1. 此处的 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意为 heuristic．详见 [启发式搜索 - 维基百科](https://zh.wikipedia.org/wiki/%E5%90%AF%E5%8F%91%E5%BC%8F%E6%90%9C%E7%B4%A2) 和 [A* search algorithm - Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm#Bounded_relaxation) 的 Bounded relaxation 一节． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/search/astar.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/search/astar.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [Henry-ZHR](https://github.com/Henry-ZHR), [hsfzLZH1](https://github.com/hsfzLZH1), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [Xeonacid](https://github.com/Xeonacid), [billchenchina](https://github.com/billchenchina), [c-forrest](https://github.com/c-forrest), [ChungZH](https://github.com/ChungZH), [cn-Mouxy](https://github.com/cn-Mouxy), [flylai](https://github.com/flylai), [greyqz](https://github.com/greyqz), [iamtwz](https://github.com/iamtwz), [interestingLSY](https://github.com/interestingLSY), [kenlig](https://github.com/kenlig), [leoleoasd](https://github.com/leoleoasd), [NachtgeistW](https://github.com/NachtgeistW), [ree-chee](https://github.com/ree-chee), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [WaterWan](https://github.com/WaterWan), [Wh1tD](https://github.com/Wh1tD)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
