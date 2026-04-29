# 悬线法 - OI Wiki

- Source: https://oi-wiki.org/misc/hoverline/

# 悬线法

## 引入

悬线法的适用范围是单调栈的子集．具体来说，悬线法可以应用于满足以下条件的题目：

  * 需要在扫描序列时维护单调的信息；
  * 可以使用单调栈解决；
  * 不需要在单调栈上二分．

看起来悬线法可以被替代，用处不大，但是悬线法概念比单调栈简单，更适合初学 OI 的选手理解并解决最大子矩阵等问题．

## 例题

[SPOJ HISTOGRA - Largest Rectangle in a Histogram](https://www.spoj.com/problems/HISTOGRA)

大意：在一条水平线上有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个宽为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩形，求包含于这些矩形的最大子矩形面积．

悬线，就是一条竖线，这条竖线有初始位置和高度两个性质，可以在其上端点不超过当前位置的矩形高度的情况下左右移动．

对于一条悬线，我们在这条上端点不超过当前位置的矩形高度且不移出边界的前提下，将这条悬线左右移动，求出其最多能向左和向右扩展到何处，此时这条悬线扫过的面积就是包含这条悬线的尽可能大的矩形．容易发现，最大子矩形必定是包含一条初始位置为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，高度为 ℎ𝑖hi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的悬线．枚举实现这个过程的时间复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是我们可以用悬线法将其优化到 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们考虑如何快速找到悬线可以到达的最左边的位置．

### 过程

定义 𝑙𝑖li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为当前找到的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位置的悬线能扩展到的最左边的位置，容易得到 𝑙𝑖li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 初始为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们需要进一步判断还能不能进一步往左扩展．

  * 如果当前 𝑙𝑖 =1li=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则已经扩展到了边界，不可以．
  * 如果当前 𝑎𝑖 >𝑎𝑙𝑖−1ai>ali−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则从当前悬线扩展到的位置不能再往左扩展了．
  * 如果当前 𝑎𝑖 ≤𝑎𝑙𝑖−1ai≤ali−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则从当前悬线还可以往左扩展，并且 𝑙𝑖 −1li−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位置的悬线能向左扩展到的位置，𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位置的悬线一定也可以扩展到，于是我们将 𝑙𝑖li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更新为 𝑙𝑙𝑖−1lli−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并继续执行判断．

通过摊还分析，可以证明每个 𝑙𝑖li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最多会被其他的 𝑙𝑗lj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历到一次，因此时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 实现

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text #include <algorithm> #include <iostream> using std :: max ; constexpr int N = 100010 ; int n , a [ N ]; int l [ N ], r [ N ]; long long ans ; using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); while ( cin >> n , n ) { ans = 0 ; for ( int i = 1 ; i <= n ; i ++ ) cin >> a [ i ], l [ i ] = r [ i ] = i ; for ( int i = 1 ; i <= n ; i ++ ) while ( l [ i ] > 1 && a [ i ] <= a [ l [ i ] \- 1 ]) l [ i ] = l [ l [ i ] \- 1 ]; for ( int i = n ; i >= 1 ; i \-- ) while ( r [ i ] < n && a [ i ] <= a [ r [ i ] \+ 1 ]) r [ i ] = r [ r [ i ] \+ 1 ]; for ( int i = 1 ; i <= n ; i ++ ) ans = max ( ans , ( long long )( r [ i ] \- l [ i ] \+ 1 ) * a [ i ]); cout << ans << '\n' ; } return 0 ; } ```   
---|---  
  
[UVa1619 感觉不错 Feel Good](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4494)

对于一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数列，找出一个子区间，使子区间内的最小值与子区间内元素和的乘积最大，要求在满足舒适值最大的情况下最小化长度，最小化长度的情况下最小化左端点序号．

本题中我们可以考虑枚举最小值，将每个位置的数 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当作最小值，并考虑从 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向左右扩展，找到满足 𝑟min𝑗=𝑙𝑎𝑗 =𝑎𝑖minj=lraj=ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的尽可能向左右扩展的区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这样本题就被转化成了悬线法模型．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` |  ```text #include <cstring> #include <iostream> constexpr int N = 100010 ; int n , a [ N ], l [ N ], r [ N ]; long long sum [ N ]; long long ans ; int ansl , ansr ; bool fir = true ; using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); while ( cin >> n ) { memset ( a , -1 , sizeof ( a )); if ( ! fir ) cout << '\n' ; else fir = false ; ans = 0 ; ansl = ansr = 1 ; for ( int i = 1 ; i <= n ; i ++ ) { cin >> a [ i ]; sum [ i ] = sum [ i \- 1 ] \+ a [ i ]; l [ i ] = r [ i ] = i ; } for ( int i = 1 ; i <= n ; i ++ ) while ( a [ l [ i ] \- 1 ] >= a [ i ]) l [ i ] = l [ l [ i ] \- 1 ]; for ( int i = n ; i >= 1 ; i \-- ) while ( a [ r [ i ] \+ 1 ] >= a [ i ]) r [ i ] = r [ r [ i ] \+ 1 ]; for ( int i = 1 ; i <= n ; i ++ ) { long long x = a [ i ] * ( sum [ r [ i ]] \- sum [ l [ i ] \- 1 ]); if ( ans < x || ( ans == x && ansr \- ansl > r [ i ] \- l [ i ])) ans = x , ansl = l [ i ], ansr = r [ i ]; } cout << ans << '\n' << ansl << ' ' << ansr << '\n' ; } return 0 ; } ```   
---|---  
  
## 最大子矩形

[P4147 玉蟾宫](https://www.luogu.com.cn/problem/P4147)

给定一个 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的包含 `'F'` 和 `'R'` 的矩阵，求其面积最大的子矩阵的面积 ×3×3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得这个子矩阵中的每一位的值都为 `'F'`．

我们会发现本题的模型和第一题的模型很像．仔细分析，发现如果我们每次只考虑某一行的所有元素，将位置 (𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素尽可能向上扩展的距离作为该位置的悬线长度，那最大子矩阵一定是这些悬线向左右扩展得到的尽可能大的矩形中的一个．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` |  ```text #include <algorithm> #include <iostream> int m , n , a [ 1010 ], l [ 1010 ], r [ 1010 ], ans ; using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m ; for ( int i = 1 ; i <= n ; i ++ ) { for ( int j = 1 ; j <= m ; j ++ ) { l [ j ] = r [ j ] = j ; } char s [ 3 ]; for ( int j = 1 ; j <= m ; j ++ ) { cin >> s ; if ( s [ 0 ] == 'F' ) a [ j ] ++ ; else if ( s [ 0 ] == 'R' ) a [ j ] = 0 ; } for ( int j = 1 ; j <= m ; j ++ ) while ( l [ j ] != 1 && a [ l [ j ] \- 1 ] >= a [ j ]) l [ j ] = l [ l [ j ] \- 1 ]; for ( int j = m ; j >= 1 ; j \-- ) while ( r [ j ] != m && a [ r [ j ] \+ 1 ] >= a [ j ]) r [ j ] = r [ r [ j ] \+ 1 ]; for ( int j = 1 ; j <= m ; j ++ ) ans = std :: max ( ans , ( r [ j ] \- l [ j ] \+ 1 ) * a [ j ]); } cout << ans * 3 ; return 0 ; } ```   
---|---  
  
## 习题

  * [P1169「ZJOI2007」棋盘制作](https://www.luogu.com.cn/problem/P1169)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/hoverline.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/hoverline.md "edit.link.title")  
>  __本页面贡献者：[countercurrent-time](https://github.com/countercurrent-time), [StudyingFather](https://github.com/StudyingFather), [GekkaSaori](https://github.com/GekkaSaori), [H-J-Granger](https://github.com/H-J-Granger), [NachtgeistW](https://github.com/NachtgeistW), [Enter-tainer](https://github.com/Enter-tainer), [Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A), [weiyong1024](https://github.com/weiyong1024), [Ahacad](https://github.com/Ahacad), [c-forrest](https://github.com/c-forrest), [dis-GU-ise](https://github.com/dis-GU-ise), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [gi-b716](https://github.com/gi-b716), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [mwsht](https://github.com/mwsht), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [SukkaW](https://github.com/SukkaW)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
