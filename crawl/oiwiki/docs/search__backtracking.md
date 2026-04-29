# 回溯法 - OI Wiki

- Source: https://oi-wiki.org/search/backtracking/

# 回溯法

本页面将简要介绍回溯法的概念和应用．

## 简介

回溯法是一种经常被用在 [深度优先搜索（DFS）](../dfs/) 和 [广度优先搜索（BFS）](../bfs/) 的技巧．

其本质是：走不通就回头．

## 过程

  1. 构造空间树；

  2. 进行遍历；

  3. 如遇到边界条件，即不再向下搜索，转而搜索另一条链；

  4. 达到目标条件，输出结果．

## 例题

[USACO 1.5.4 Checker Challenge](https://www.luogu.com.cn/problem/P1219)

现在有一个如下的 6 ×66×6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的跳棋棋盘，有六个棋子被放置在棋盘上，使得每行，每列，每条对角线（包括两条主对角线的所有对角线）上都至多有一个棋子．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text 0 1 2 3 4 5 6 \------------------------- 1 | | O | | | | | \------------------------- 2 | | | | O | | | \------------------------- 3 | | | | | | O | \------------------------- 4 | O | | | | | | \------------------------- 5 | | | O | | | | \------------------------- 6 | | | | | O | | \------------------------- ```   
---|---  
  
上面的布局可以用序列 {2,4,6,1,3,5}{2,4,6,1,3,5}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来描述，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数字表示在第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的第 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列有一个棋子，如下所示

行号 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：{1,2,3,4,5,6}{1,2,3,4,5,6}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

列号 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：{2,4,6,1,3,5}{2,4,6,1,3,5}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这只是跳棋放置的一个方案．请编一个程序找出所有方案并把它们以上面的序列化方法输出，按字典顺序排列．你只需输出前 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个解并在最后一行输出解的总个数．特别注意：你需要优化你的程序以保证在更大棋盘尺寸下的程序效率．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` |  ```text // 该代码为回溯法的 DFS 实现 #include <iostream> using namespace std ; int ans [ 14 ], check [ 3 ][ 28 ] = { 0 }, sum = 0 , n ; void eq ( int line ) { if ( line > n ) { // 如果已经搜索完n行 sum ++ ; if ( sum > 3 ) return ; else { for ( int i = 1 ; i <= n ; i ++ ) cout << ans [ i ] << ' ' ; cout << '\n' ; return ; } } for ( int i = 1 ; i <= n ; i ++ ) { if (( ! check [ 0 ][ i ]) && ( ! check [ 1 ][ line \+ i ]) && ( ! check [ 2 ][ line \- i \+ n ])) { // 判断在某位置放置是否合法 ans [ line ] = i ; check [ 0 ][ i ] = 1 ; check [ 1 ][ line \+ i ] = 1 ; check [ 2 ][ line \- i \+ n ] = 1 ; eq ( line \+ 1 ); // 向下递归后进行回溯，方便下一轮递归 check [ 0 ][ i ] = 0 ; check [ 1 ][ line \+ i ] = 0 ; check [ 2 ][ line \- i \+ n ] = 0 ; } } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n ; eq ( 1 ); cout << sum ; return 0 ; } ```   
---|---  
  
[迷宫](https://www.luogu.com.cn/problem/P1605)

现有一个尺寸为 𝑁 ×𝑀N×M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的迷宫，迷宫里有 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处障碍，障碍处不可通过．给定起点坐标和终点坐标，且每个方格最多经过一次，问有多少种从起点坐标到终点坐标的方案．在迷宫中移动有上、下、左、右四种移动方式，每次只能移动一个方格．数据保证起点上没有障碍．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ``` |  ```text // 该代码为回溯法的 BFS 实现 #include <cstring> #include <iostream> #include <queue> using namespace std ; int n , m , k , x , y , a , b , ans ; int dx [ 4 ] = { 0 , 0 , 1 , -1 }, dy [ 4 ] = { 1 , -1 , 0 , 0 }; // 四个方向 bool vis [ 6 ][ 6 ]; struct oo { int x , y , used [ 6 ][ 6 ]; }; oo sa ; void bfs () { queue < oo > q ; sa . x = x ; sa . y = y ; sa . used [ x ][ y ] = 1 ; q . push ( sa ); while ( ! q . empty ()) { // BFS队列 oo now = q . front (); q . pop (); for ( int i = 0 ; i < 4 ; i ++ ) { // 枚举向四个方向走 int sx = now . x \+ dx [ i ]; int sy = now . y \+ dy [ i ]; if ( now . used [ sx ][ sy ] || vis [ sx ][ sy ] || sx == 0 || sy == 0 || sx > n || sy > m ) continue ; if ( sx == a && sy == b ) { ans ++ ; continue ; } sa . x = sx ; sa . y = sy ; memcpy ( sa . used , now . used , sizeof ( now . used )); sa . used [ sx ][ sy ] = 1 ; q . push ( sa ); // 假设向此方向走，放入BFS队列 } } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m >> k ; cin >> x >> y >> a >> b ; for ( int i = 1 , aa , bb ; i <= k ; i ++ ) { cin >> aa >> bb ; vis [ aa ][ bb ] = true ; // 障碍位置不可通过 } bfs (); cout << ans ; return 0 ; } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/search/backtracking.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/search/backtracking.md "edit.link.title")  
>  __本页面贡献者：[NachtgeistW](https://github.com/NachtgeistW), [Ir1d](https://github.com/Ir1d), [ksyx](https://github.com/ksyx), [Tiphereth-A](https://github.com/Tiphereth-A), [Alisahhh](https://github.com/Alisahhh), [c-forrest](https://github.com/c-forrest), [FFjet](https://github.com/FFjet), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [luoguyuntianming](https://github.com/luoguyuntianming), [miaotony](https://github.com/miaotony), [partychicken](https://github.com/partychicken), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
