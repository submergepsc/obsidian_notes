# LGV 引理 - OI Wiki

- Source: https://oi-wiki.org/graph/lgv/

# LGV 引理

## 简介

Lindström–Gessel–Viennot lemma，即 LGV 引理，可以用来处理有向无环图上不相交路径计数等问题．

前置知识：[图论相关概念](../concept/) 中的基础部分、[矩阵](../../math/linear-algebra/matrix/)、[高斯消元求行列式](../../math/numerical/gauss/)．

LGV 引理仅适用于 **有向无环图** ．

## 定义

𝜔(𝑃)ω(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这条路径上所有边的边权之积．（路径计数时，可以将边权都设为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）（事实上，边权可以为生成函数）

𝑒(𝑢,𝑣)e(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **每一条** 路径 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝜔(𝑃)ω(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之和，即 𝑒(𝑢,𝑣) =∑𝑃:𝑢→𝑣𝜔(𝑃)e(u,v)=∑P:u→vω(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

起点集合 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，是有向无环图点集的一个子集，大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

终点集合 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也是有向无环图点集的一个子集，大小也为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

一组 𝐴 →𝐵A→B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的不相交路径 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：𝑆𝑖Si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一条从 𝐴𝑖Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝐵𝜎(𝑆)𝑖Bσ(S)i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径（𝜎(𝑆)σ(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个排列），对于任何 𝑖 ≠𝑗i≠j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑆𝑖Si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑆𝑗Sj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有公共顶点．

𝑡(𝜎)t(σ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示排列 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆序对个数．

## 引理

𝑀=⎡⎢ ⎢ ⎢ ⎢⎣𝑒(𝐴1,𝐵1)𝑒(𝐴1,𝐵2)⋯𝑒(𝐴1,𝐵𝑛)𝑒(𝐴2,𝐵1)𝑒(𝐴2,𝐵2)⋯𝑒(𝐴2,𝐵𝑛)⋮⋮⋱⋮𝑒(𝐴𝑛,𝐵1)𝑒(𝐴𝑛,𝐵2)⋯𝑒(𝐴𝑛,𝐵𝑛)⎤⎥ ⎥ ⎥ ⎥⎦M=[e(A1,B1)e(A1,B2)⋯e(A1,Bn)e(A2,B1)e(A2,B2)⋯e(A2,Bn)⋮⋮⋱⋮e(An,B1)e(An,B2)⋯e(An,Bn)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)det⁡(𝑀)=∑𝑆:𝐴→𝐵(−1)𝑡(𝜎(𝑆))𝑛∏𝑖=1𝜔(𝑆𝑖)det⁡(M)=∑S:A→B(−1)t(σ(S))∏i=1nω(Si)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 ∑𝑆:𝐴→𝐵∑S:A→B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示满足上文要求的 𝐴 →𝐵A→B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每一组不相交路径 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 证明

由行列式定义可得

det⁡(𝑀)=∑𝜎(−1)𝑡(𝜎)𝑛∏𝑖=1𝑒(𝑎𝑖,𝑏𝜎(𝑖))=∑𝜎(−1)𝑡(𝜎)𝑛∏𝑖=1∑𝑃:𝑎𝑖→𝑏𝜎(𝑖)𝜔(𝑃)det⁡(M)=∑σ(−1)t(σ)∏i=1ne(ai,bσ(i))=∑σ(−1)t(σ)∏i=1n∑P:ai→bσ(i)ω(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

观察到 𝑛∏𝑖=1∑𝑃:𝑎𝑖→𝑏𝜎(𝑖)𝜔(𝑃)∏i=1n∑P:ai→bσ(i)ω(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，实际上是所有从 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 排列为 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径组 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝜔(𝑃)ω(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之和．

∑𝜎(−1)𝑡(𝜎)𝑛∏𝑖=1∑𝑃:𝑎𝑖→𝑏𝜎(𝑖)𝜔(𝑃)=∑𝜎(−1)𝑡(𝜎)∑𝑃=𝜎𝜔(𝑃)=∑𝑃:𝐴→𝐵(−1)𝑡(𝜎)𝑛∏𝑖=1𝜔(𝑃𝑖)∑σ(−1)t(σ)∏i=1n∑P:ai→bσ(i)ω(P)=∑σ(−1)t(σ)∑P=σω(P)=∑P:A→B(−1)t(σ)∏i=1nω(Pi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此处 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为任意路径组．

设 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为不相交路径组，𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为相交路径组，

∑𝑃:𝐴→𝐵(−1)𝑡(𝜎)𝑛∏𝑖=1𝜔(𝑃𝑖)=∑𝑈:𝐴→𝐵(−1)𝑡(𝑈)𝑛∏𝑖=1𝜔(𝑈𝑖)+∑𝑉:𝐴→𝐵(−1)𝑡(𝑉)𝑛∏𝑖=1𝜔(𝑉𝑖)∑P:A→B(−1)t(σ)∏i=1nω(Pi)=∑U:A→B(−1)t(U)∏i=1nω(Ui)+∑V:A→B(−1)t(V)∏i=1nω(Vi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中存在一个相交路径组 𝑃𝑖 :𝑎1 →𝑢 →𝑏1,𝑃𝑗 :𝑎2 →𝑢 →𝑏2Pi:a1→u→b1,Pj:a2→u→b2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则必然存在和它相对的一个相交路径组 𝑃′𝑖 =𝑎1 →𝑢 →𝑏2,𝑃′𝑗 =𝑎2 →𝑢 →𝑏1Pi′=a1→u→b2,Pj′=a2→u→b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑃′P′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的其他路径与 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同．可得 𝜔(𝑃) =𝜔(𝑃′),𝑡(𝑃) =𝑡(𝑃′) ±1ω(P)=ω(P′),t(P)=t(P′)±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此我们有 ∑𝑉:𝐴→𝐵( −1)𝑡(𝜎)𝑛∏𝑖=1𝜔(𝑉𝑖) =0∑V:A→B(−1)t(σ)∏i=1nω(Vi)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

则 det⁡(𝑀) =∑𝑈:𝐴→𝐵( −1)𝑡(𝑈)𝑛∏𝑖=1𝜔(𝑈𝑖)det⁡(M)=∑U:A→B(−1)t(U)∏i=1nω(Ui)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证毕1．

## 例题

例 1 [CF348D Turtles](https://codeforces.com/contest/348/problem/D)

题意：有一个 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的格点棋盘，其中某些格子可走，某些格子不可走．有一只海龟从 (𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只能走到 (𝑥 +1,𝑦)(x+1,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑥,𝑦 +1)(x,y+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置，求海龟从 (1,1)(1,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑛,𝑚)(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的不相交路径数对 109 +7109+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模之后的结果．2 ≤𝑛,𝑚 ≤30002≤n,m≤3000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

比较直接的 LGV 引理的应用．考虑所有合法路径，发现从 (1,1)(1,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发一定要经过 𝐴 ={(1,2),(2,1)}A={(1,2),(2,1)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而到达终点一定要经过 𝐵 ={(𝑛 −1,𝑚),(𝑛,𝑚 −1)}B={(n−1,m),(n,m−1)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可立即选定．应用 LGV 引理可得答案为：

∣𝑓(𝑎1,𝑏1)𝑓(𝑎1,𝑏2)𝑓(𝑎2,𝑏1)𝑓(𝑎2,𝑏2)∣=𝑓(𝑎1,𝑏1)×𝑓(𝑎2,𝑏2)−𝑓(𝑎1,𝑏2)×𝑓(𝑎2,𝑏1)|f(a1,b1)f(a1,b2)f(a2,b1)f(a2,b2)|=f(a1,b1)×f(a2,b2)−f(a1,b2)×f(a2,b1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑓(𝑎,𝑏)f(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为图上 𝑎 →𝑏a→b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径数，带有障碍格点的路径计数问题可以直接做一个 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 dp，则 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 易求．最终复杂度 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 ``` |  ```text #include <cstring> #include <iostream> #include <string> using namespace std ; using ll = long long ; constexpr int MOD = 1e9 \+ 7 ; constexpr int SIZE = 3010 ; string board [ SIZE ]; int dp [ SIZE ][ SIZE ]; int f ( int x1 , int y1 , int x2 , int y2 ) { memset ( dp , 0 , sizeof dp ); dp [ x1 ][ y1 ] = board [ x1 ][ y1 ] == '.' ; for ( int i = 1 ; i <= x2 ; i ++ ) { for ( int j = 1 ; j <= y2 ; j ++ ) { if ( board [ i ][ j ] == '#' ) { continue ; } dp [ i ][ j ] = ( dp [ i ][ j ] \+ dp [ i \- 1 ][ j ]) % MOD ; dp [ i ][ j ] = ( dp [ i ][ j ] \+ dp [ i ][ j \- 1 ]) % MOD ; } } return dp [ x2 ][ y2 ] % MOD ; } int main () { ios :: sync_with_stdio ( false ); cin . tie ( nullptr ); int n , m ; cin >> n >> m ; for ( int i = 1 ; i <= n ; i ++ ) { cin >> board [ i ]; board [ i ] = " " \+ board [ i ]; } ll f11 = f ( 1 , 2 , n \- 1 , m ); ll f12 = f ( 1 , 2 , n , m \- 1 ); ll f21 = f ( 2 , 1 , n \- 1 , m ); ll f22 = f ( 2 , 1 , n , m \- 1 ); ll ans = (( f11 * f22 ) % MOD \- ( f12 * f21 ) % MOD \+ MOD ) % MOD ; cout << ans << '\n' ; return 0 ; } ```   
---|---  
  
例 2 [HDU 5852 Intersection is not allowed!](https://acm.hdu.edu.cn/showproblem.php?pid=5852)

题意：有一个 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的棋盘，一个棋子从 (𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只能走到 (𝑥,𝑦 +1)(x,y+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 (𝑥 +1,𝑦)(x+1,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个棋子，一开始第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个棋子放在 (1,𝑎𝑖)(1,ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最终要到 (𝑛,𝑏𝑖)(n,bi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，路径要两两不相交，求方案数对 109 +7109+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模．1 ≤𝑛 ≤1051≤n≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑘 ≤1001≤k≤100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，保证 1 ≤𝑎1 <𝑎2 <⋯ <𝑎𝑛 ≤𝑛1≤a1<a2<⋯<an≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑏1 <𝑏2 <⋯ <𝑏𝑛 ≤𝑛1≤b1<b2<⋯<bn≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

观察到如果路径不相交就一定是 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 LGV 引理中一定有 𝜎(𝑆)𝑖 =𝑖σ(S)i=i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不需要考虑符号问题．边权设为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直接套用引理即可．

从 (1,𝑎𝑖)(1,ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑛,𝑏𝑗)(n,bj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径条数相当于从 𝑛 −1 +𝑏𝑗 −𝑎𝑖n−1+bj−ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步中选 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步向下走，所以 𝑒(𝐴𝑖,𝐵𝑗) =(𝑛−1+𝑏𝑗−𝑎𝑖𝑛−1)e(Ai,Bj)=(n−1+bj−ain−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

行列式可以使用高斯消元求．

复杂度为 𝑂(𝑛 +𝑘(𝑘2 +log⁡𝑝))O(n+k(k2+log⁡p))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 log⁡𝑝log⁡p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是求逆元复杂度．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 ``` |  ```text #include <algorithm> #include <iostream> using ll = long long ; constexpr int K = 105 ; constexpr int N = 100005 ; constexpr int mod = 1e9 \+ 7 ; int T , n , k , a [ K ], b [ K ], fact [ N << 1 ], m [ K ][ K ]; int qpow ( int x , int y ) { int out = 1 ; while ( y ) { if ( y & 1 ) out = ( ll ) out * x % mod ; x = ( ll ) x * x % mod ; y >>= 1 ; } return out ; } int c ( int x , int y ) { return ( ll ) fact [ x ] * qpow ( fact [ y ], mod \- 2 ) % mod * qpow ( fact [ x \- y ], mod \- 2 ) % mod ; } using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); fact [ 0 ] = 1 ; for ( int i = 1 ; i < N * 2 ; ++ i ) fact [ i ] = ( ll ) fact [ i \- 1 ] * i % mod ; cin >> T ; while ( T \-- ) { cin >> n >> k ; for ( int i = 1 ; i <= k ; ++ i ) cin >> a [ i ]; for ( int i = 1 ; i <= k ; ++ i ) cin >> b [ i ]; for ( int i = 1 ; i <= k ; ++ i ) { for ( int j = 1 ; j <= k ; ++ j ) { if ( a [ i ] <= b [ j ]) m [ i ][ j ] = c ( b [ j ] \- a [ i ] \+ n \- 1 , n \- 1 ); else m [ i ][ j ] = 0 ; } } for ( int i = 1 ; i < k ; ++ i ) { if ( ! m [ i ][ i ]) { for ( int j = i \+ 1 ; j <= k ; ++ j ) { if ( m [ j ][ i ]) { std :: swap ( m [ i ], m [ j ]); break ; } } } if ( ! m [ i ][ i ]) continue ; int inv = qpow ( m [ i ][ i ], mod \- 2 ); for ( int j = i \+ 1 ; j <= k ; ++ j ) { if ( ! m [ j ][ i ]) continue ; int mul = ( ll ) m [ j ][ i ] * inv % mod ; for ( int p = i ; p <= k ; ++ p ) { m [ j ][ p ] = ( m [ j ][ p ] \- ( ll ) m [ i ][ p ] * mul % mod \+ mod ) % mod ; } } } int ans = 1 ; for ( int i = 1 ; i <= k ; ++ i ) ans = ( ll ) ans * m [ i ][ i ] % mod ; cout << ans << '\n' ; } return 0 ; } ```   
---|---  
  
## 参考资料

* * *

  1. 证明来源于 [知乎 - LGV 引理证明](https://zhuanlan.zhihu.com/p/517819133) ↩

* * *

>  __本页面最近更新： 2026/1/30 21:35:24，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/lgv.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/lgv.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Ir1d](https://github.com/Ir1d), [ouuan](https://github.com/ouuan), [c-forrest](https://github.com/c-forrest), [chenyichen0420](https://github.com/chenyichen0420), [Cidoai](https://github.com/Cidoai), [H-J-Granger](https://github.com/H-J-Granger), [HeRaNO](https://github.com/HeRaNO), [kenlig](https://github.com/kenlig), [lxdlam](https://github.com/lxdlam), [memset0](https://github.com/memset0), [Menci](https://github.com/Menci)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
