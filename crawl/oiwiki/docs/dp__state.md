# 状压 DP - OI Wiki

- Source: https://oi-wiki.org/dp/state/

# 状压 DP

## 简介

状压 DP 是动态规划的一种，通过将状态集合转化为整数记录在 DP 状态中来实现状态转移的目的．

为了达到更低的时间复杂度，通常需要寻找更低状态数的状态．大部分题目中会利用二元状态，用 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位二进制数表示 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个独立二元状态的情况．

使用状态压缩通常涉及位操作，关于基础位操作详见 [位操作](../../math/bit/) 页面．

## 例题 1

[「SCOI2005」互不侵犯](https://loj.ac/problem/2153)

在 𝑁 ×𝑁N×N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的棋盘里面放 𝐾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个国王（1 ≤𝑁 ≤9,1 ≤𝐾 ≤𝑁 ×𝑁1≤N≤9,1≤K≤N×N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），使他们互不攻击，共有多少种摆放方案．

国王能攻击到它上下左右，以及左上左下右上右下八个方向上附近的各一个格子，共 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个格子．

### 解释

设 𝑓(𝑖,𝑗,𝑙)f(i,j,l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的状态为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且棋盘上已经放置 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个国王时的合法方案数．

对于编号为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的状态，我们用二进制整数 𝑠𝑖𝑡(𝑗)sit(j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示国王的放置情况，𝑠𝑖𝑡(𝑗)sit(j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的某个二进制位为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示对应位置不放国王，为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示在对应位置上放置国王；用 𝑠𝑡𝑎(𝑗)sta(j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示该状态的国王个数，即二进制数 𝑠𝑖𝑡(𝑗)sit(j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数．例如，如下图所示的状态可用二进制数 100101100101![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来表示（棋盘左边对应二进制低位），则有 𝑠𝑖𝑡(𝑗) =100101(2) =37,𝑠𝑡𝑎(𝑗) =3sit(j)=100101(2)=37,sta(j)=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

![](./images/SCOI2005-%E4%BA%92%E4%B8%8D%E4%BE%B5%E7%8A%AF.png)

设当前行的状态为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，上一行的状态为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以得到下面的状态转移方程：𝑓(𝑖,𝑗,𝑙) =∑𝑓(𝑖 −1,𝑥,𝑙 −𝑠𝑡𝑎(𝑗))f(i,j,l)=∑f(i−1,x,l−sta(j))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

设上一行的状态编号为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在保证当前行和上一行不冲突的前提下，枚举所有可能的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行转移，转移方程：

𝑓(𝑖,𝑗,𝑙)=∑𝑓(𝑖−1,𝑥,𝑙−𝑠𝑡𝑎(𝑗))f(i,j,l)=∑f(i−1,x,l−sta(j))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` |  ```text #include <algorithm> #include <iostream> using namespace std ; long long sta [ 2005 ], sit [ 2005 ], f [ 15 ][ 2005 ][ 105 ]; int n , k , cnt ; void dfs ( int x , int num , int cur ) { if ( cur >= n ) { // 有新的合法状态 sit [ ++ cnt ] = x ; sta [ cnt ] = num ; return ; } dfs ( x , num , cur \+ 1 ); // cur位置不放国王 dfs ( x \+ ( 1 << cur ), num \+ 1 , cur \+ 2 ); // cur位置放国王，与它相邻的位置不能再放国王 } bool compatible ( int j , int x ) { if ( sit [ j ] & sit [ x ]) return false ; if (( sit [ j ] << 1 ) & sit [ x ]) return false ; if ( sit [ j ] & ( sit [ x ] << 1 )) return false ; return true ; } int main () { cin >> n >> k ; dfs ( 0 , 0 , 0 ); // 先预处理一行的所有合法状态 for ( int j = 1 ; j <= cnt ; j ++ ) f [ 1 ][ j ][ sta [ j ]] = 1 ; for ( int i = 2 ; i <= n ; i ++ ) for ( int j = 1 ; j <= cnt ; j ++ ) for ( int x = 1 ; x <= cnt ; x ++ ) { if ( ! compatible ( j , x )) continue ; // 排除不合法转移 for ( int l = sta [ j ]; l <= k ; l ++ ) f [ i ][ j ][ l ] += f [ i \- 1 ][ x ][ l \- sta [ j ]]; } long long ans = 0 ; for ( int i = 1 ; i <= cnt ; i ++ ) ans += f [ n ][ i ][ k ]; // 累加答案 cout << ans << endl ; return 0 ; } ```   
---|---  
  
## 例题 2

[[POI2004] PRZ](https://www.luogu.com.cn/problem/P5911)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人需要过桥，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的人的重量为 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，过桥用时为 𝑡𝑖ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 这些人过桥时会分成若干组，只有在某一组的所有人全部过桥后，其余的组才能过桥．桥最大承重为 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，问这些人全部过桥的最短时间．

100 ≤𝑊 ≤400100≤W≤400![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑛 ≤161≤n≤16![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑡𝑖 ≤501≤ti≤50![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，10 ≤𝑤𝑖 ≤10010≤wi≤100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

### 解释

我们用 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示所有人构成集合的一个子集，设 𝑡(𝑆)t(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中人的最长过桥时间，𝑤(𝑆)w(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有人的总重量，𝑓(𝑆)f(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有人全部过桥的最短时间，则：

{𝑓(∅)=0,𝑓(𝑆)=min𝑇⊆𝑆; 𝑤(𝑇)≤𝑊{𝑡(𝑇)+𝑓(𝑆∖𝑇)}.{f(∅)=0,f(S)=minT⊆S; w(T)≤W{t(T)+f(S∖T)}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

需要注意的是这里不能直接枚举集合再判断是否为子集，而应使用 [子集枚举](../../math/binary-set/#遍历所有掩码的子掩码)，从而使时间复杂度为 𝑂(3𝑛)O(3n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

### 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` |  ```text #include <iostream> #include <limits> #include <vector> using namespace std ; int main () { ios :: sync_with_stdio ( false ); cin . tie ( nullptr ); int W , n ; cin >> W >> n ; const int S = ( 1 << n ) \- 1 ; vector < int > ts ( S \+ 1 ), ws ( S \+ 1 ); for ( int j = 0 , t , w ; j < n ; ++ j ) { cin >> t >> w ; for ( int i = 0 ; i <= S ; ++ i ) if ( i & ( 1 << j )) { ts [ i ] = max ( ts [ i ], t ); ws [ i ] += w ; } } vector < int > dp ( S \+ 1 , numeric_limits < int >:: max () / 2 ); for ( int i = 0 ; i <= S ; ++ i ) { if ( ws [ i ] <= W ) dp [ i ] = ts [ i ]; for ( int j = i ; j ; j = i & ( j \- 1 )) if ( ws [ i ^ j ] <= W ) dp [ i ] = min ( dp [ i ], dp [ j ] \+ ts [ i ^ j ]); } cout << dp [ S ] << '\n' ; return 0 ; } ```   
---|---  
  
## 习题

  * [「NOI2001」炮兵阵地](https://loj.ac/problem/10173)
  * [「USACO06NOV」玉米田 Corn Fields](https://www.luogu.com.cn/problem/P1879)
  * [「九省联考 2018」一双木棋](https://loj.ac/problem/2471)

* * *

>  __本页面最近更新： 2026/1/27 12:26:08，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/state.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/state.md "edit.link.title")  
>  __本页面贡献者：[StudyingFather](https://github.com/StudyingFather), [Ir1d](https://github.com/Ir1d), [H-J-Granger](https://github.com/H-J-Granger), [NachtgeistW](https://github.com/NachtgeistW), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [ouuan](https://github.com/ouuan), [Marcythm](https://github.com/Marcythm), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [AngelKitty](https://github.com/AngelKitty), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [chieh2lu2](https://github.com/chieh2lu2), [Chrogeek](https://github.com/Chrogeek), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [hhc0001](https://github.com/hhc0001), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [Link-cute](https://github.com/Link-cute), [lychees](https://github.com/lychees), [Peanut-Tang](https://github.com/Peanut-Tang), [REYwmp](https://github.com/REYwmp), [shinzanmono](https://github.com/shinzanmono), [SukkaW](https://github.com/SukkaW), [TianKong-y](https://github.com/TianKong-y), [TOMWT-qwq](https://github.com/TOMWT-qwq), [Xeonacid](https://github.com/Xeonacid), [YuJunDongGit](https://github.com/YuJunDongGit), [zhb2000](https://github.com/zhb2000)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
