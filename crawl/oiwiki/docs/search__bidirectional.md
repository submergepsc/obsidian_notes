# 双向搜索 - OI Wiki

- Source: https://oi-wiki.org/search/bidirectional/

# 双向搜索

本页面将简要介绍两种双向搜索算法：「双向同时搜索」和「Meet in the middle」．

## 双向同时搜索

### 定义

双向同时搜索的基本思路是从状态图上的起点和终点同时开始进行 [广搜](../bfs/) 或 [深搜](../dfs/)．

如果发现搜索的两端相遇了，那么可以认为是获得了可行解．

### 过程

双向广搜的步骤：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text 将开始结点和目标结点加入队列 q 标记开始结点为 1 标记目标结点为 2 while (队列 q 不为空) { 从 q.front() 扩展出新的 s 个结点 如果 新扩展出的结点已经被其他数字标记过 那么 表示搜索的两端碰撞 那么 循环结束 如果 新的 s 个结点是从开始结点扩展来的 那么 将这个 s 个结点标记为 1 并且入队 q 如果 新的 s 个结点是从目标结点扩展来的 那么 将这个 s 个结点标记为 2 并且入队 q } ```   
---|---  
  
### 例题

例题 [八数码难题](https://www.luogu.com.cn/problem/P1379)

在 3 ×33×3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的棋盘上，摆有八个棋子，每个棋子上标有 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的某一数字．棋盘中留有一个空格，空格用 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来表示．空格周围的棋子可以移到空格中．要求解的问题是：给出一种初始布局（初始状态）和目标布局（为了使题目简单，设目标状态为 123804765123804765![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），找到一种最少步骤的移动方法，实现从初始布局到目标布局的转变．

解题思路

很好想出暴力 bfs．本题使用暴力 bfs 也不会超时．但是这里把它作为双向同时搜索的例题．我们可以使用两个 bfs，一个从起点状态开始正着搜，一个从终点状态开始反着搜，交替使用两个 bfs，搜索树的大小会大大减小．当其中一个 bfs 搜出另一个 bfs 已经搜出的状态，即可得到答案．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 ``` |  ```text #include <iostream> #include <map> #include <queue> #include <string> using namespace std ; struct State { int A [ 3 ][ 3 ]; State () = default ; State ( string s ) { for ( int i = 0 ; i < 3 ; i ++ ) { for ( int j = 0 ; j < 3 ; j ++ ) { A [ i ][ j ] = s [ i * 3 \+ j ] \- '0' ; } } } friend bool operator < ( const State & a , const State & b ) { for ( int i = 0 ; i < 3 ; i ++ ) { for ( int j = 0 ; j < 3 ; j ++ ) { if ( a . A [ i ][ j ] != b . A [ i ][ j ]) { return a . A [ i ][ j ] < b . A [ i ][ j ]; } } } return false ; } }; int dir [ 4 ][ 2 ] = {{ 1 , 0 }, { -1 , 0 }, { 0 , 1 }, { 0 , -1 }}; void bfs ( queue < State > & q , map < State , int > & m1 , map < State , int > & m2 ) { auto u = q . front (); q . pop (); int xx , yy ; for ( int i = 0 ; i < 3 ; i ++ ) { for ( int j = 0 ; j < 3 ; j ++ ) { if ( u . A [ i ][ j ] == 0 ) { xx = i ; yy = j ; } } } for ( int i = 0 ; i < 4 ; i ++ ) { int tx = dir [ i ][ 0 ] \+ xx , ty = dir [ i ][ 1 ] \+ yy ; if ( tx >= 0 && tx < 3 && ty >= 0 && ty < 3 ) { auto v = u ; swap ( v . A [ xx ][ yy ], v . A [ tx ][ ty ]); if ( m2 . count ( v )) { cout << m1 [ u ] \+ m2 [ v ] << endl ; exit ( 0 ); } if ( ! m1 . count ( v )) { m1 [ v ] = m1 [ u ] \+ 1 ; q . push ( v ); } } } } int main () { string I , O ; cin >> I ; O = "123804765" ; State in = I , ou = O ; queue < State > q1 , q2 ; map < State , int > mp1 , mp2 ; q1 . push ( in ); mp1 [ in ] = 0 ; q2 . push ( ou ); mp2 [ ou ] = 1 ; if ( I == O ) { cout << 0 ; return 0 ; } while ( 1 ) { bfs ( q1 , mp1 , mp2 ); bfs ( q2 , mp2 , mp1 ); } return 0 ; } ```   
---|---  
  
## Meet in the middle

Warning

本节要介绍的不是 [**二分搜索**](../../basic/binary/)（二分搜索的另外一个译名为「折半搜索」）．

### 引入

Meet in the middle 算法没有正式译名，常见的翻译为「折半搜索」、「双向搜索」或「中途相遇」．

它适用于输入数据较小，但还没小到能直接使用暴力搜索的情况．

### 过程

Meet in the middle 算法的主要思想是将整个搜索过程分成两半，分别搜索，最后将两半的结果合并．

### 性质

暴力搜索的复杂度往往是指数级的，而改用 meet in the middle 算法后复杂度的指数可以减半，即让复杂度从 𝑂(𝑎𝑏)O(ab)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 降到 𝑂(𝑎𝑏/2)O(ab/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 例题

例题 [「USACO09NOV」灯 Lights](https://www.luogu.com.cn/problem/P2962)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 盏灯，每盏灯与若干盏灯相连，每盏灯上都有一个开关，如果按下一盏灯上的开关，这盏灯以及与之相连的所有灯的开关状态都会改变．一开始所有灯都是关着的，你需要将所有灯打开，求最小的按开关次数．

1 ≤𝑛 ≤351≤n≤35![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解题思路

如果这道题暴力 DFS 找开关灯的状态，时间复杂度就是 𝑂(2𝑛)O(2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 显然超时．不过，如果我们用 meet in middle 的话，时间复杂度可以优化至 𝑂(𝑛2𝑛/2)O(n2n/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．meet in middle 就是让我们先找一半的状态，也就是找出只使用编号为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 midmid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的开关能够到达的状态，再找出只使用另一半开关能到达的状态．如果前半段和后半段开启的灯互补，将这两段合并起来就得到了一种将所有灯打开的方案．具体实现时，可以把前半段的状态以及达到每种状态的最少按开关次数存储在 map 里面，搜索后半段时，每搜出一种方案，就把它与互补的第一段方案合并来更新答案．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ``` |  ```text #include <algorithm> #include <iostream> #include <map> using namespace std ; int n , m , ans = 0x7fffffff ; map < long long , int > f ; long long a [ 40 ]; int main () { cin >> n >> m ; a [ 0 ] = 1 ; for ( int i = 1 ; i < n ; ++ i ) a [ i ] = a [ i \- 1 ] * 2 ; // 进行预处理 for ( int i = 1 ; i <= m ; ++ i ) { // 对输入的边的情况进行处理 int u , v ; cin >> u >> v ; \-- u ; \-- v ; a [ u ] |= (( long long ) 1 << v ); a [ v ] |= (( long long ) 1 << u ); } for ( int i = 0 ; i < ( 1 << ( n / 2 )); ++ i ) { // 对前一半进行搜索 long long t = 0 ; int cnt = 0 ; for ( int j = 0 ; j < n / 2 ; ++ j ) { if (( i >> j ) & 1 ) { t ^= a [ j ]; ++ cnt ; } } if ( ! f . count ( t )) f [ t ] = cnt ; else f [ t ] = min ( f [ t ], cnt ); } for ( int i = 0 ; i < ( 1 << ( n \- n / 2 )); ++ i ) { // 对后一半进行搜索 long long t = 0 ; int cnt = 0 ; for ( int j = 0 ; j < ( n \- n / 2 ); ++ j ) { if (( i >> j ) & 1 ) { t ^= a [ n / 2 \+ j ]; ++ cnt ; } } if ( f . count (((( long long ) 1 << n ) \- 1 ) ^ t )) ans = min ( ans , cnt \+ f [((( long long ) 1 << n ) \- 1 ) ^ t ]); } cout << ans ; return 0 ; } ```   
---|---  
  
## 外部链接

  * [What is meet in the middle algorithm w.r.t. competitive programming? - Quora](https://www.quora.com/What-is-meet-in-the-middle-algorithm-w-r-t-competitive-programming)
  * [Meet in the Middle Algorithm - YouTube](https://www.youtube.com/watch?v=57SUNQL4JFA)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/search/bidirectional.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/search/bidirectional.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [NachtgeistW](https://github.com/NachtgeistW), [Henry-ZHR](https://github.com/Henry-ZHR), [ksyx](https://github.com/ksyx), [Tiphereth-A](https://github.com/Tiphereth-A), [Alisahhh](https://github.com/Alisahhh), [AndrewWayne](https://github.com/AndrewWayne), [c-forrest](https://github.com/c-forrest), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [Enter-tainer](https://github.com/Enter-tainer), [FFjet](https://github.com/FFjet), [frank-xjh](https://github.com/frank-xjh), [hcx1204](https://github.com/hcx1204), [hcx2012Git](https://github.com/hcx2012Git), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [leoleoasd](https://github.com/leoleoasd), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [sundyloveme](https://github.com/sundyloveme), [Xarfa](https://github.com/Xarfa), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
