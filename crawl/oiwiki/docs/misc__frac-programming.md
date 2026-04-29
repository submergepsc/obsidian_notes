# 分数规划 - OI Wiki

- Source: https://oi-wiki.org/misc/frac-programming/

# 分数规划

分数规划用来求一个分式的极值．其形式化表述是，给出 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求一组 𝑤𝑖 ∈{0,1}wi∈{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最小化或最大化

𝑛∑𝑖=1𝑎𝑖×𝑤𝑖𝑛∑𝑖=1𝑏𝑖×𝑤𝑖∑i=1nai×wi∑i=1nbi×wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

通俗来讲，这类问题类似于：每种物品有两个权值 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，选出若干个物品使得 ∑𝑎∑𝑏∑a∑b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小或最大．

一般分数规划问题还会有一些特殊的限制，比如「分母至少为 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」．

## 求解

### 二分法

分数规划问题的通用方法是二分答案法．假设当前二分到的答案为 𝑚𝑖𝑑mid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则一组满足条件的 {𝑤𝑖}{wi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 会让权值大于等于 𝑚𝑖𝑑mid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据这一条件列不等式并变形

∑𝑎𝑖×𝑤𝑖∑𝑏𝑖×𝑤𝑖≥𝑚𝑖𝑑⟹∑𝑎𝑖×𝑤𝑖−𝑚𝑖𝑑×∑𝑏𝑖⋅𝑤𝑖≥0⟹∑𝑤𝑖×(𝑎𝑖−𝑚𝑖𝑑×𝑏𝑖)≥0∑ai×wi∑bi×wi≥mid⟹∑ai×wi−mid×∑bi⋅wi≥0⟹∑wi×(ai−mid×bi)≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么只要求出不等号左边的式子的最大值就行了．如果最大值比 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 要大，说明 𝑚𝑖𝑑mid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是可行的，否则不可行．分数规划的主要难点就在于如何求 ∑𝑤𝑖 ×(𝑎𝑖 −𝑚𝑖𝑑 ×𝑏𝑖)∑wi×(ai−mid×bi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大值或最小值．

### Dinkelbach 算法

Dinkelbach 算法1的大概思想是每次用上一轮的答案当做新的 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来输入，不断地迭代，直至答案收敛．

## 例题

[LOJ 149 01 分数规划](https://loj.ac/p/149)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品，每个物品有两个权值 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．求一组 𝑤𝑖 ∈{0,1}wi∈{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中恰好有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最大化 ∑𝑎𝑖×𝑤𝑖∑𝑏𝑖×𝑤𝑖∑ai×wi∑bi×wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

解法

把 𝑎𝑖 −𝑚𝑖𝑑 ×𝑏𝑖ai−mid×bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品的权值，贪心地选权值前 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大的物品．若权值和大于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则可行，否则不可行．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` |  ```text #include <algorithm> #include <cstdio> #include <functional> using namespace std ; constexpr int N = 100000 \+ 10 ; constexpr double eps = 1e-6 ; int n , k ; int a [ N ], b [ N ]; double c [ N ]; bool check ( double mid ) { double s = 0 ; for ( int i = 1 ; i <= n ; i ++ ) c [ i ] = a [ i ] \- b [ i ] * mid ; // 将权值从大到小排序 sort ( c \+ 1 , c \+ n \+ 1 , greater < double > ()); for ( int i = 1 ; i <= k ; ++ i ) // 选择前 k 个物品 s += c [ i ]; return s >= 0 ; } int main () { scanf ( "%d %d" , & n , & k ); for ( int i = 1 ; i <= n ; ++ i ) scanf ( "%d" , & a [ i ]); for ( int i = 1 ; i <= n ; ++ i ) scanf ( "%d" , & b [ i ]); double L = 0 , R = 1 ; while ( R \- L > eps ) { double mid = ( L \+ R ) / 2 ; if ( check ( mid )) // mid 可行，答案比 mid 大 L = mid ; else // mid 不可行，答案比 mid 小 R = mid ; } printf ( "%.6lf \n " , L ); return 0 ; } ```   
---|---  
  
[洛谷 4377 Talent Show G](https://www.luogu.com.cn/problem/P4377)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品，每个物品有两个权值 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

你需要确定一组 𝑤𝑖 ∈{0,1}wi∈{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 ∑𝑤𝑖×𝑎𝑖∑𝑤𝑖×𝑏𝑖∑wi×ai∑wi×bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最大．

要求 ∑𝑤𝑖 ×𝑏𝑖 ≥𝑊∑wi×bi≥W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解法

本题多了分母至少为 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的限制，因此无法再使用上一题的贪心算法．

可以考虑 01 背包．把 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品的重量，𝑎𝑖 −𝑚𝑖𝑑 ×𝑏𝑖ai−mid×bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品的价值，然后问题就转化为背包了．那么 𝑑𝑝[𝑛][𝑊]dp[n][W]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是最大值．

在 DP 过程中，物品重量和可能超过 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时直接视为 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` |  ```text #include <algorithm> #include <cstdio> using namespace std ; constexpr int MAXN = 250 \+ 10 ; constexpr int MAXW = 1000 \+ 10 ; constexpr double eps = 1e-6 ; int n , W ; int w [ MAXN ], t [ MAXN ]; double f [ MAXW ]; bool check ( double mid ) { double s = 0 ; for ( int i = 1 ; i <= W ; i ++ ) f [ i ] = -1e9 ; for ( int i = 1 ; i <= n ; i ++ ) for ( int j = W ; j >= 0 ; j \-- ) { int k = min ( W , j \+ w [ i ]); f [ k ] = max ( f [ k ], f [ j ] \+ t [ i ] \- mid * w [ i ]); } return f [ W ] >= 0 ; } int main () { scanf ( "%d %d" , & n , & W ); double L = 0 , R = 0 ; for ( int i = 1 ; i <= n ; ++ i ) { scanf ( "%d %d" , & w [ i ], & t [ i ]); R += t [ i ]; } while ( R \- L > eps ) { double mid = ( L \+ R ) / 2 ; if ( check ( mid )) L = mid ; else R = mid ; } printf ( "%d \n " , ( int )( L * 1000 )); return 0 ; } ```   
---|---  
  
[POJ2728 Desert King](http://poj.org/problem?id=2728)

每条边有两个权值 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求一棵生成树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 ∑𝑒∈𝑇𝑎𝑒∑𝑒∈𝑇𝑏𝑒∑e∈Tae∑e∈Tbe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小．

解法

把 𝑎𝑖 −𝑚𝑖𝑑 ×𝑏𝑖ai−mid×bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为每条边的权值，那么最小生成树就是最小值．本题中需要求解一个完全图中的最小生成树，应利用 Prim 算法求解．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 ``` |  ```text #include <algorithm> #include <cmath> #include <cstdio> using namespace std ; const int N = 1000 \+ 10 ; const double eps = 1e-5 ; int n ; double d [ N ][ N ], c [ N ][ N ], dis [ N ]; int x [ N ], y [ N ], z [ N ]; bool vis [ N ]; bool ok ( double m ) { double ans = 0 ; for ( int i = 1 ; i <= n ; i ++ ) vis [ i ] = false ; dis [ 1 ] = 0 ; for ( int i = 2 ; i <= n ; i ++ ) dis [ i ] = 1e18 ; for ( int i = 1 ; i <= n ; i ++ ) { double mn = 1e18 ; int pt = -1 ; for ( int j = 1 ; j <= n ; j ++ ) if ( ! vis [ j ] && mn > dis [ j ]) { pt = j ; mn = dis [ j ]; } if ( !~ pt ) break ; vis [ pt ] = true ; ans += mn ; for ( int j = 1 ; j <= n ; j ++ ) if ( j != pt ) dis [ j ] = min ( dis [ j ], c [ pt ][ j ] \- m * d [ pt ][ j ]); } return ans >= 0 ; } int main () { while ( scanf ( "%d" , & n ) == 1 ) { if ( n == 0 ) break ; for ( int i = 1 ; i <= n ; i ++ ) scanf ( "%d %d %d" , & x [ i ], & y [ i ], & z [ i ]); for ( int i = 1 ; i <= n ; i ++ ) for ( int j = i \+ 1 ; j <= n ; j ++ ) { d [ i ][ j ] = d [ j ][ i ] = sqrt (( x [ i ] \- x [ j ]) * ( x [ i ] \- x [ j ]) \+ ( y [ i ] \- y [ j ]) * ( y [ i ] \- y [ j ])); c [ i ][ j ] = c [ j ][ i ] = abs ( z [ i ] \- z [ j ]); } double l = 0 , r = 10000000 ; while ( r \- l > eps ) { double m = ( l \+ r ) / 2 ; if ( ok ( m )) l = m ; else r = m ; } printf ( "%.3f \n " , l ); } return 0 ; } ```   
---|---  
  
[[HNOI2009] 最小圈](https://www.luogu.com.cn/problem/P3199)

每条边的边权为 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求一个环 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 ∑𝑒∈𝐶𝑤|𝐶|∑e∈Cw|C|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小．

解法

把 𝑎𝑖 −𝑚𝑖𝑑ai−mid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为边权，那么权值最小的环就是最小值．

因为我们只需要判最小值是否小于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以只需要判断图中是否存在负环即可．

另外本题存在一种复杂度 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的算法，如果有兴趣可以阅读 [这篇文章](https://www.cnblogs.com/y-clever/p/7043553.html)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``` |  ```text #include <algorithm> #include <cstdio> #include <tuple> #include <vector> using namespace std ; constexpr int N = 3000 \+ 10 ; constexpr double eps = 1e-9 ; int n , m ; double dis [ N ]; vector < pair < int , double >> g [ N ]; bool check ( double mid ) { // 如果有负环返回 true bool flag = false ; dis [ 0 ] = 0 ; for ( int i = 1 ; i <= n ; ++ i ) dis [ i ] = 1e9 ; for ( int t = 1 ; t <= n ; ++ t ) { flag = false ; for ( int u = 0 ; u <= n ; ++ u ) for ( auto vw : g [ u ]) { int v ; double w ; tie ( v , w ) = vw ; if ( dis [ v ] > dis [ u ] \+ w \- mid ) { dis [ v ] = dis [ u ] \+ w \- mid ; flag = true ; } } if ( ! flag ) break ; } return flag ; } int main () { scanf ( "%d %d" , & n , & m ); for ( int i = 1 ; i <= m ; ++ i ) { int u , v ; double w ; scanf ( "%d %d %lf" , & u , & v , & w ); g [ u ]. push_back ({ v , w }); } for ( int i = 1 ; i <= n ; i ++ ) g [ 0 ]. push_back ({ i , 0 }); double L = -1e7 , R = 1e7 ; while ( R \- L > eps ) { double mid = ( L \+ R ) / 2 ; if ( check ( mid )) R = mid ; else L = mid ; } printf ( "%.8lf \n " , L ); return 0 ; } ```   
---|---  
  
## 习题

  * [JSOI2016 最佳团体](https://loj.ac/problem/2071)
  * [SDOI2017 新生舞会](https://loj.ac/problem/2003)
  * [UVa1389 Hard Life](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4135)
  * [洛谷 P2868 [USACO07DEC] Sightseeing Cows G](https://www.luogu.com.cn/problem/P2868)
  * [AtCoder Beginner Contest 324 F - Beautiful Path](https://atcoder.jp/contests/abc324/tasks/abc324_f)

## 参考资料与注释

* * *

  1. [Dinkelbach, Werner. "On nonlinear fractional programming." Management science 13.7 (1967): 492-498.](https://doi.org/10.1287/mnsc.13.7.492) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/frac-programming.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/frac-programming.md "edit.link.title")  
>  __本页面贡献者：[StudyingFather](https://github.com/StudyingFather), [Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [greyqz](https://github.com/greyqz), [NachtgeistW](https://github.com/NachtgeistW), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [Mout-sea](https://github.com/Mout-sea), [AngelKitty](https://github.com/AngelKitty), [banglee13](https://github.com/banglee13), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [hsfzLZH1](https://github.com/hsfzLZH1), [huaruoji](https://github.com/huaruoji), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [alphagocc](https://github.com/alphagocc), [c-forrest](https://github.com/c-forrest), [ChungZH](https://github.com/ChungZH), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lyccrius](https://github.com/lyccrius), [lychees](https://github.com/lychees), [MicDZ](https://github.com/MicDZ), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [r-value](https://github.com/r-value), [SukkaW](https://github.com/SukkaW), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
