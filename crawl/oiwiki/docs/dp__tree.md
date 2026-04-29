# 树形 DP - OI Wiki

- Source: https://oi-wiki.org/dp/tree/

# 树形 DP

树形 DP，即在树上进行的 DP．由于树固有的递归性质，树形 DP 一般都是递归进行的．

## 基础

以下面这道题为例，介绍一下树形 DP 的一般过程．

例题 [洛谷 P1352 没有上司的舞会](https://www.luogu.com.cn/problem/P1352)

某大学有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个职员，编号为 1 ∼𝑁1∼N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．他们之间有从属关系，也就是说他们的关系就像一棵以校长为根的树，父结点就是子结点的直接上司．现在有个周年庆宴会，宴会每邀请来一个职员都会增加一定的快乐指数 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是呢，如果某个职员的直接上司来参加舞会了，那么这个职员就无论如何也不肯来参加舞会了．所以，请你编程计算，邀请哪些职员可以使快乐指数最大，求最大的快乐指数．

我们设 𝑓(𝑖,0/1)f(i,0/1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表以 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树的最优解（第二维的值为 0 代表 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不参加舞会的情况，1 代表 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 参加舞会的情况）．

对于每个状态，都存在两种决策（其中下面的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的儿子）：

  * 上司不参加舞会时，下属可以参加，也可以不参加，此时有 𝑓(𝑖,0) =∑max{𝑓(𝑥,1),𝑓(𝑥,0)}f(i,0)=∑max{f(x,1),f(x,0)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 上司参加舞会时，下属都不会参加，此时有 𝑓(𝑖,1) =∑𝑓(𝑥,0) +𝑎𝑖f(i,1)=∑f(x,0)+ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们可以通过 DFS，在返回上一层时更新当前结点的最优解．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` |  ```text #include <algorithm> #include <iostream> using namespace std ; struct edge { int v , next ; } e [ 6005 ]; int head [ 6005 ], n , cnt , f [ 6005 ][ 2 ], ans , is_h [ 6005 ], vis [ 6005 ]; void addedge ( int u , int v ) { // 建图 e [ ++ cnt ]. v = v ; e [ cnt ]. next = head [ u ]; head [ u ] = cnt ; } void calc ( int k ) { vis [ k ] = 1 ; for ( int i = head [ k ]; i ; i = e [ i ]. next ) { // 枚举该结点的每个子结点 if ( vis [ e [ i ]. v ]) continue ; calc ( e [ i ]. v ); f [ k ][ 1 ] += f [ e [ i ]. v ][ 0 ]; f [ k ][ 0 ] += max ( f [ e [ i ]. v ][ 0 ], f [ e [ i ]. v ][ 1 ]); // 转移方程 } return ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n ; for ( int i = 1 ; i <= n ; i ++ ) cin >> f [ i ][ 1 ]; for ( int i = 1 ; i < n ; i ++ ) { int l , k ; cin >> l >> k ; is_h [ l ] = 1 ; addedge ( k , l ); } for ( int i = 1 ; i <= n ; i ++ ) if ( ! is_h [ i ]) { // 从根结点开始DFS calc ( i ); cout << max ( f [ i ][ 1 ], f [ i ][ 0 ]); return 0 ; } } ```   
---|---  
  
通常，树形 DP 状态一般都为当前节点的最优解．先 DFS 遍历子树的所有最优解，然后向上传递给子树的父节点来转移，最终根节点的值即为所求的最优解．

### 习题

  * [HDU 2196 Computer](https://acm.hdu.edu.cn/showproblem.php?pid=2196)

  * [POJ 1463 Strategic game](http://poj.org/problem?id=1463)

  * [[POI2014]FAR-FarmCraft](https://www.luogu.com.cn/problem/P3574)

## 树上背包

树上的背包问题，简单来说就是背包问题与树形 DP 的结合．

例题 [洛谷 P2014 CTSC1997 选课](https://www.luogu.com.cn/problem/P2014)

现在有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 门课程，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 门课程的学分为 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每门课程有零门或一门先修课，有先修课的课程需要先学完其先修课，才能学习该课程．

一位学生要学习 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 门课程，求其能获得的最多学分数．

𝑛,𝑚 ≤300n,m≤300![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

每门课最多只有一门先修课的特点，与有根树中一个点最多只有一个父亲结点的特点类似．

因此可以想到根据这一性质建树，从而所有课程组成了一个森林的结构．为了方便起见，我们可以新增一门 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 学分的课程（设这个课程的编号为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），作为所有无先修课课程的先修课，这样我们就将森林变成了一棵以 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号课程为根的树．

我们设 𝑓(𝑢,𝑖,𝑗)f(u,i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示以 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号点为根的子树中，已经遍历了 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号点的前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵子树，选了 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 门课程的最大学分．

转移的过程结合了树形 DP 和 [背包 DP](../knapsack/) 的特点，我们枚举 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点的每个子结点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，同时枚举以 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树选了几门课程，将子树的结果合并到 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上．

记点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的儿子个数为 𝑠𝑥sx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树大小为 𝑠𝑖𝑧𝑥sizx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以写出下面的状态转移方程：

𝑓(𝑢,𝑖,𝑗)=max𝑣,𝑘≤𝑗,𝑘≤𝑠𝑖𝑧𝑣𝑓(𝑢,𝑖−1,𝑗−𝑘)+𝑓(𝑣,𝑠𝑣,𝑘)f(u,i,j)=maxv,k≤j,k≤sizvf(u,i−1,j−k)+f(v,sv,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意上面状态转移方程中的几个限制条件，这些限制条件确保了一些无意义的状态不会被访问到．

𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第二维可以很轻松地用滚动数组的方式省略掉，注意这时需要倒序枚举 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

可以证明，该做法的时间复杂度为 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)1．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``` |  ```text #include <algorithm> #include <iostream> #include <vector> using namespace std ; int f [ 305 ][ 305 ], s [ 305 ], n , m ; vector < int > e [ 305 ]; int dfs ( int u ) { int p = 1 ; f [ u ][ 1 ] = s [ u ]; for ( auto v : e [ u ]) { int siz = dfs ( v ); // 注意下面两重循环的上界和下界 // 只考虑已经合并过的子树，以及选的课程数超过 m+1 的状态没有意义 for ( int i = min ( p , m \+ 1 ); i ; i \-- ) for ( int j = 1 ; j <= siz && i \+ j <= m \+ 1 ; j ++ ) f [ u ][ i \+ j ] = max ( f [ u ][ i \+ j ], f [ u ][ i ] \+ f [ v ][ j ]); // 转移方程 p += siz ; } return p ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m ; for ( int i = 1 ; i <= n ; i ++ ) { int k ; cin >> k >> s [ i ]; e [ k ]. push_back ( i ); } dfs ( 0 ); cout << f [ 0 ][ m \+ 1 ]; return 0 ; } ```   
---|---  
  
### 习题

  * [「CTSC1997」选课](https://www.luogu.com.cn/problem/P2014)

  * [「JSOI2018」潜入行动](https://loj.ac/problem/2546)

  * [「SDOI2017」苹果树](https://loj.ac/problem/2268)

  * [「Codeforces Round 875 Div. 1」Problem D. Mex Tree](https://codeforces.com/contest/1830/problem/D)

## 换根 DP

树形 DP 中的换根 DP 问题又被称为二次扫描，通常不会指定根结点，并且根结点的变化会对一些值，例如子结点深度和、点权和等产生影响．

通常需要两次 DFS，第一次 DFS 预处理诸如深度，点权和之类的信息，在第二次 DFS 开始运行换根动态规划．

接下来以一些例题来带大家熟悉这个内容．

例题 [[POI2008]STA-Station](https://www.luogu.com.cn/problem/P3478)

给定一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的树，请求出一个结点，使得以这个结点为根时，所有结点的深度之和最大．

不妨令 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为当前结点，𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为当前结点的子结点．首先需要用 𝑠𝑖si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来表示以 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树中的结点个数，并且有 𝑠𝑢 =1 +∑𝑠𝑣su=1+∑sv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．显然需要一次 DFS 来计算所有的 𝑠𝑖si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这次的 DFS 就是预处理，我们得到了以某个结点为根时其子树中的结点总数．

考虑状态转移，这里就是体现＂换根＂的地方了．令 𝑓𝑢fu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为以 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根时，所有结点的深度之和．

𝑓𝑣 ←𝑓𝑢fv←fu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以体现换根，即以 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根转移到以 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根．显然在换根的转移过程中，以 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根或以 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根会导致其子树中的结点的深度产生改变．具体表现为：

  * 所有在 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子树上的结点深度都减少了一，那么总深度和就减少了 𝑠𝑣sv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

  * 所有不在 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子树上的结点深度都增加了一，那么总深度和就增加了 𝑛 −𝑠𝑣n−sv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

根据这两个条件就可以推出状态转移方程 𝑓𝑣 =𝑓𝑢 −𝑠𝑣 +𝑛 −𝑠𝑣 =𝑓𝑢 +𝑛 −2 ×𝑠𝑣fv=fu−sv+n−sv=fu+n−2×sv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

于是在第二次 DFS 遍历整棵树并状态转移 𝑓𝑣 =𝑓𝑢 +𝑛 −2 ×𝑠𝑣fv=fu+n−2×sv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么就能求出以每个结点为根时的深度和了．最后只需要遍历一次所有根结点深度和就可以求出答案．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` |  ```text #include <iostream> using namespace std ; int head [ 1000010 << 1 ], tot ; long long n , sz [ 1000010 ], dep [ 1000010 ]; long long f [ 1000010 ]; struct node { int to , next ; } e [ 1000010 << 1 ]; void add ( int u , int v ) { // 建图 e [ ++ tot ] = { v , head [ u ]}; head [ u ] = tot ; } void dfs ( int u , int fa ) { // 预处理dfs sz [ u ] = 1 ; dep [ u ] = dep [ fa ] \+ 1 ; for ( int i = head [ u ]; i ; i = e [ i ]. next ) { int v = e [ i ]. to ; if ( v != fa ) { dfs ( v , u ); sz [ u ] += sz [ v ]; } } } void get_ans ( int u , int fa ) { // 第二次dfs换根dp for ( int i = head [ u ]; i ; i = e [ i ]. next ) { int v = e [ i ]. to ; if ( v != fa ) { f [ v ] = f [ u ] \- sz [ v ] * 2 \+ n ; get_ans ( v , u ); } } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n ; int u , v ; for ( int i = 1 ; i <= n \- 1 ; i ++ ) { cin >> u >> v ; add ( u , v ); add ( v , u ); } dfs ( 1 , 1 ); for ( int i = 1 ; i <= n ; i ++ ) f [ 1 ] += dep [ i ]; get_ans ( 1 , 1 ); long long int ans = -1 ; int id ; for ( int i = 1 ; i <= n ; i ++ ) { // 统计答案 if ( f [ i ] > ans ) { ans = f [ i ]; id = i ; } } cout << id << '\n' ; return 0 ; } ```   
---|---  
  
### 习题

  * [Atcoder Educational DP Contest, Problem V, Subtree](https://atcoder.jp/contests/dp/tasks/dp_v)

  * [Educational Codeforces Round 67, Problem E, Tree Painting](https://codeforces.com/contest/1187/problem/E)

  * [POJ 3585 Accumulation Degree](http://poj.org/problem?id=3585)

  * [[USACO10MAR]Great Cow Gathering G](https://www.luogu.com.cn/problem/P2986)

  * [CodeForce 708C Centroids](http://codeforces.com/problemset/problem/708/C)

## 参考资料与注释

* * *

  1. [子树合并背包类型的 dp 的复杂度证明 - LYD729 的 CSDN 博客](https://blog.csdn.net/lyd_7_29/article/details/79854245) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/tree.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/tree.md "edit.link.title")  
>  __本页面贡献者：[StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [Ir1d](https://github.com/Ir1d), [NachtgeistW](https://github.com/NachtgeistW), [countercurrent-time](https://github.com/countercurrent-time), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [ShaoChenHeng](https://github.com/ShaoChenHeng), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [aaron20100919](https://github.com/aaron20100919), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [greyqz](https://github.com/greyqz), [Henry-ZHR](https://github.com/Henry-ZHR), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [lychees](https://github.com/lychees), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [ouuan](https://github.com/ouuan), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [amakerlife](https://github.com/amakerlife), [billchenchina](https://github.com/billchenchina), [c-forrest](https://github.com/c-forrest), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [isdanni](https://github.com/isdanni), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [Marcythm](https://github.com/Marcythm), [Peanut-Tang](https://github.com/Peanut-Tang), [qz-cqy](https://github.com/qz-cqy), [ShizuhaAki](https://github.com/ShizuhaAki), [SukkaW](https://github.com/SukkaW), [thredreams](https://github.com/thredreams), [widsnoy](https://github.com/widsnoy), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
