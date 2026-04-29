# 树的直径 - OI Wiki

- Source: https://oi-wiki.org/graph/tree-diameter/

# 树的直径

树上任意两节点之间最长的简单路径即为树的「直径」．

前置知识：[树基础](../tree-basic/)．

## 引入

显然，一棵树可以有多条直径，他们的长度相等．

可以用两次 DFS 或者树形 DP 的方法在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间求出树的直径．

## 两次 DFS

首先从任意节点 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始进行第一次 DFS，到达距离其最远的节点，记为 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后再从 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始做第二次 DFS，到达距离 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最远的节点，记为 𝑧′z′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝛿(𝑧,𝑧′)δ(z,z′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为树的直径．

显然，如果第一次 DFS 到达的节点 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是直径的一端，那么第二次 DFS 到达的节点 𝑧′z′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定是直径的一端．我们只需证明在任意情况下，𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必为直径的一端．

定理：在一棵树上，从任意节点 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始进行一次 DFS，到达的距离其最远的节点 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必为直径的一端．

证明

使用反证法．记出发节点为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设真实的直径是 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而从 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行的第一次 DFS 到达的距离其最远的节点 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不为 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．共分三种情况：

  * 若 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上：

![y 在 s-t 上](./images/tree-diameter1.svg)

有 𝛿(𝑦,𝑧) >𝛿(𝑦,𝑡) ⟹𝛿(𝑥,𝑧) >𝛿(𝑥,𝑡) ⟹𝛿(𝑠,𝑧) >𝛿(𝑠,𝑡)δ(y,z)>δ(y,t)⟹δ(x,z)>δ(x,t)⟹δ(s,z)>δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，与 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为树上任意两节点之间最长的简单路径矛盾．

  * 若 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不在 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上，且 𝛿(𝑦,𝑧)δ(y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在重合路径：

![y 不在 s-t 上，y-z 与 s-t 存在重合路径](./images/tree-diameter2.svg)

有 𝛿(𝑦,𝑧) >𝛿(𝑦,𝑡) ⟹𝛿(𝑥,𝑧) >𝛿(𝑥,𝑡) ⟹𝛿(𝑠,𝑧) >𝛿(𝑠,𝑡)δ(y,z)>δ(y,t)⟹δ(x,z)>δ(x,t)⟹δ(s,z)>δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，与 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为树上任意两节点之间最长的简单路径矛盾．

  * 若 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不在 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上，且 𝛿(𝑦,𝑧)δ(y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不存在重合路径：

![y 不在 s-t 上，y-z 与 s-t 不存在重合路径](./images/tree-diameter3.svg)

有 𝛿(𝑦,𝑧) >𝛿(𝑦,𝑡) ⟹𝛿(𝑥′,𝑧) >𝛿(𝑥′,𝑡) ⟹𝛿(𝑥,𝑧) >𝛿(𝑥,𝑡) ⟹𝛿(𝑠,𝑧) >𝛿(𝑠,𝑡)δ(y,z)>δ(y,t)⟹δ(x′,z)>δ(x′,t)⟹δ(x,z)>δ(x,t)⟹δ(s,z)>δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，与 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为树上任意两节点之间最长的简单路径矛盾．

综上，三种情况下假设均会产生矛盾，故原定理得证．

负权边

上述证明过程建立在所有路径均不为负的前提下．如果树上存在负权边，则上述证明不成立．故若存在负权边，则无法使用两次 DFS 的方式求解直径．

如果需要求出一条直径上所有的节点，则可以在第二次 DFS 的过程中，记录每个点的前序节点，即可从直径的一端一路向前，遍历直径上所有的节点．

## 树形 DP

### 方法 1

我们记录当 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为树的根时，每个节点作为子树的根向下，所能延伸的最长路径长度 𝑑1d1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与次长路径（与最长路径无公共边）长度 𝑑2d2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么直径就是对于每一个点，该点 𝑑1 +𝑑2d1+d2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能取到的值中的最大值．

树形 DP 可以在存在负权边的情况下求解出树的直径．

如果需要求出一条直径上所有的节点，则可以在 DP 的过程中，记录下每个节点能向下延伸的最长路径与次长路径（定义同上）所对应的子节点，在求 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的同时记下对应的节点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑑 =𝑑1[𝑢] +𝑑2[𝑢]d=d1[u]+d2[u]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即可分别沿着从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始的最长路径的次长路径对应的子节点一路向某个方向（对于无根树，虽然这里指定了 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为树的根，但仍需记录每点跳转的方向；对于有根树，一路向上跳即可），遍历直径上所有的节点．

### 方法 2

这里提供一种只使用一个数组进行的树形 DP 方法．

我们定义 𝑑𝑝[𝑢]dp[u]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为以 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树中，从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发的最长路径．那么容易得出转移方程：𝑑𝑝[𝑢] =max(𝑑𝑝[𝑢],𝑑𝑝[𝑣] +𝑤(𝑢,𝑣))dp[u]=max(dp[u],dp[v]+w(u,v))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中的 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子节点，𝑤(𝑢,𝑣)w(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示所经过边的权重．

对于树的直径，实际上是可以通过枚举从某个节点出发不同的两条路径相加的最大值求出．因此，在 DP 求解的过程中，我们只需要在更新 𝑑𝑝[𝑢]dp[u]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之前，计算 𝑑 =max(𝑑,𝑑𝑝[𝑢] +𝑑𝑝[𝑣] +𝑤(𝑢,𝑣))d=max(d,dp[u]+dp[v]+w(u,v))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可算出直径 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 例题

[Luogu B4016 树的直径](https://www.luogu.com.cn/problem/B4016)

给定一棵 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点的树，求其直径的长度．1 ≤𝑛 ≤1051≤n≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

两次 DFS 的参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` |  ```text #include <cstdio> #include <vector> using namespace std ; constexpr int N = 100000 \+ 10 ; int n , c , d [ N ]; vector < int > E [ N ]; void dfs ( int u , int fa ) { for ( int v : E [ u ]) { if ( v == fa ) continue ; d [ v ] = d [ u ] \+ 1 ; if ( d [ v ] > d [ c ]) c = v ; dfs ( v , u ); } } int main () { scanf ( "%d" , & n ); for ( int i = 1 ; i < n ; i ++ ) { int u , v ; scanf ( "%d %d" , & u , & v ); E [ u ]. push_back ( v ), E [ v ]. push_back ( u ); } dfs ( 1 , 0 ); d [ c ] = 0 , dfs ( c , 0 ); printf ( "%d \n " , d [ c ]); return 0 ; } ```   
---|---  
  
使用两个数组的树形 DP 参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``` |  ```text #include <algorithm> #include <cstdio> #include <vector> using namespace std ; constexpr int N = 100000 \+ 10 ; int n , d ; int d1 [ N ], d2 [ N ]; vector < int > E [ N ]; void dfs ( int u , int fa ) { d1 [ u ] = d2 [ u ] = 0 ; for ( int v : E [ u ]) { if ( v == fa ) continue ; dfs ( v , u ); int t = d1 [ v ] \+ 1 ; if ( t > d1 [ u ]) d2 [ u ] = d1 [ u ], d1 [ u ] = t ; else if ( t > d2 [ u ]) d2 [ u ] = t ; } d = max ( d , d1 [ u ] \+ d2 [ u ]); } int main () { scanf ( "%d" , & n ); for ( int i = 1 ; i < n ; i ++ ) { int u , v ; scanf ( "%d %d" , & u , & v ); E [ u ]. push_back ( v ), E [ v ]. push_back ( u ); } dfs ( 1 , 0 ); printf ( "%d \n " , d ); return 0 ; } ```   
---|---  
  
使用一个数组的树形 DP 参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text #include <algorithm> #include <cstdio> #include <vector> using namespace std ; constexpr int N = 100000 \+ 10 ; int n , d ; int dp [ N ]; vector < int > E [ N ]; void dfs ( int u , int fa ) { for ( int v : E [ u ]) { if ( v == fa ) continue ; dfs ( v , u ); d = max ( d , dp [ u ] \+ dp [ v ] \+ 1 ); dp [ u ] = max ( dp [ u ], dp [ v ] \+ 1 ); } } int main () { scanf ( "%d" , & n ); for ( int i = 1 ; i < n ; i ++ ) { int u , v ; scanf ( "%d %d" , & u , & v ); E [ u ]. push_back ( v ), E [ v ]. push_back ( u ); } dfs ( 1 , 0 ); printf ( "%d \n " , d ); return 0 ; } ```   
---|---  
  
## 性质

树的直径具有如下性质：若树上所有边边权均为正，则树的所有直径中点重合．

证明

证明：使用反证法．设两条中点不重合的直径分别为 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝛿(𝑠′,𝑡′)δ(s′,t′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，中点分别为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑥′x′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．显然，𝛿(𝑠,𝑥) =𝛿(𝑥,𝑡) =𝛿(𝑠′,𝑥′) =𝛿(𝑥′,𝑡′)δ(s,x)=δ(x,t)=δ(s′,x′)=δ(x′,t′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

![无负权边的树所有直径的中点重合](./images/tree-diameter4.svg)

有 𝛿(𝑠,𝑡′) =𝛿(𝑠,𝑥) +𝛿(𝑥,𝑥′) +𝛿(𝑥′,𝑡′) >𝛿(𝑠,𝑥) +𝛿(𝑥,𝑡) =𝛿(𝑠,𝑡)δ(s,t′)=δ(s,x)+δ(x,x′)+δ(x′,t′)>δ(s,x)+δ(x,t)=δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，与 𝛿(𝑠,𝑡)δ(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为树上任意两节点之间最长的简单路径矛盾，故性质得证．

## 习题

  * [CodeChef, Diameter of Tree](https://www.codechef.com/problems/DTREE)
  * [Educational Codeforces Round 35, Problem F, Tree Destruction](https://codeforces.com/contest/911/problem/F)
  * [ZOJ 3820 Building Fire Stations](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827369872&page=28)
  * [CEOI2019/CodeForces 1192B. Dynamic Diameter](https://codeforces.com/contest/1192/problem/B)
  * [ICPC 2019 上海赛区网络赛 Lightning Routing I](https://vjudge.net/problem/%E8%AE%A1%E8%92%9C%E5%AE%A2-A2290)
  * [NOIP2007 提高组 树网的核](https://www.luogu.com.cn/problem/P1099)
  * [SDOI2011 消防](https://www.luogu.com.cn/problem/P2491)
  * [APIO2010 巡逻](https://www.luogu.com.cn/problem/P3629)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/tree-diameter.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/tree-diameter.md "edit.link.title")  
>  __本页面贡献者：[StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [lychees](https://github.com/lychees), [Mout-sea](https://github.com/Mout-sea), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [H-J-Granger](https://github.com/H-J-Granger), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [HeRaNO](https://github.com/HeRaNO), [NachtgeistW](https://github.com/NachtgeistW), [sshwy](https://github.com/sshwy), [383494](https://github.com/383494), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GavinZhengOI](https://github.com/GavinZhengOI), [GekkaSaori](https://github.com/GekkaSaori), [Gesrua](https://github.com/Gesrua), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [Kaiser-Yang](https://github.com/Kaiser-Yang), [Konano](https://github.com/Konano), [kxccc](https://github.com/kxccc), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mcendu](https://github.com/mcendu), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [ouuan](https://github.com/ouuan), [P-Y-Y](https://github.com/P-Y-Y), [Peanut-Tang](https://github.com/Peanut-Tang), [PeterlitsZo](https://github.com/PeterlitsZo), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sbofgayschool](https://github.com/sbofgayschool), [SukkaW](https://github.com/SukkaW), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [zcz0263](https://github.com/zcz0263)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
