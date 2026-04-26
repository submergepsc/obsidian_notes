# 同余最短路 - OI Wiki

- Source: https://oi-wiki.org/graph/mod-shortest-path/

# 同余最短路

当出现形如「给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数，求这 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数能拼凑出多少的其他整数（𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数可以重复取）」，以及「给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数，求这 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数不能拼凑出的最小（最大）的整数」，或者「至少要拼几次才能拼出模 𝐾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 余 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数」的问题时可以使用同余最短路的方法．

同余最短路利用同余来构造一些状态，可以达到优化空间复杂度的目的．

类比 [差分约束](../diff-constraints/) 方法，利用同余构造的这些状态可以看作单源最短路中的点．同余最短路的状态转移通常是这样的 𝑓(𝑖 +𝑦) =𝑓(𝑖) +𝑦f(i+y)=f(i)+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，类似单源最短路中 𝑓(𝑣) =𝑓(𝑢) +𝑒𝑑𝑔𝑒(𝑢,𝑣)f(v)=f(u)+edge(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 例题

### 例题一

[P3403 跳楼机](https://www.luogu.com.cn/problem/P3403)

题目大意：给定 𝑥，𝑦，𝑧，ℎx，y，z，h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对于 𝑘 ∈[1,ℎ]k∈[1,h]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有多少个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能够满足 𝑎𝑥 +𝑏𝑦 +𝑐𝑧 =𝑘ax+by+cz=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（0 ≤𝑎,𝑏,𝑐0≤a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑥,𝑦,𝑧 ≤1051≤x,y,z≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，ℎ ≤263 −1h≤263−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

不妨假设 𝑥 <𝑦 <𝑧x<y<z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

令 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为只通过 **操作 2** 和 **操作 3** ，需满足 𝑝mod𝑥 =𝑖pmodx=i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能够达到的最低楼层 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 **操作 2** 和 **操作 3** 操作后能得到的模 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下与 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同余的最小数，用来计算该同余类满足条件的数个数．

可以得到两个状态：

  * 𝑖𝑦→(𝑖 +𝑦)mod𝑥i→y(i+y)modx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 𝑖𝑧→(𝑖 +𝑧)mod𝑥i→z(i+z)modx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意通常选取一组 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中最小的那个数对它取模，也就是此处的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样可以尽量减小空间复杂度（剩余系最小）．

那么实际上相当于执行了最短路中的建边操作：

`add(i, (i+y) % x, y)`

`add(i, (i+z) % x, z)`

接下来只需要求出 𝑑0,𝑑1,𝑑2,…,𝑑𝑥−1d0,d1,d2,…,dx−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只需要跑一次最短路就可求出相应的 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

基于最短路的实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 ``` |  ```text #include <iostream> #include <queue> using namespace std ; using ll = long long ; constexpr int MAXN = 100010 ; constexpr ll linf = ( 1ull << 63 ) \- 1 ; ll h , x , y , z ; ll head [ MAXN << 1 ], tot ; ll dis [ MAXN ], vis [ MAXN ]; queue < int > q ; struct edge { ll to , next , w ; } e [ MAXN << 1 ]; void add ( ll u , ll v , ll w ) { e [ ++ tot ] = edge { v , head [ u ], w }; head [ u ] = tot ; } void spfa () { // spfa算法，可看最短路部分 dis [ 0 ] = 0 ; vis [ 0 ] = 1 ; q . push ( 0 ); while ( ! q . empty ()) { int u = q . front (); q . pop (); vis [ u ] = 0 ; for ( int i = head [ u ]; i ; i = e [ i ]. next ) { int v = e [ i ]. to , w = e [ i ]. w ; if ( dis [ v ] > dis [ u ] \+ w ) { dis [ v ] = dis [ u ] \+ w ; if ( ! vis [ v ]) { q . push ( v ); vis [ v ] = 1 ; } } } } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> h ; cin >> x >> y >> z ; if ( x == 1 || y == 1 || z == 1 ) { cout << h << '\n' ; return 0 ; } \-- h ; for ( int i = 0 ; i < x ; i ++ ) { add ( i , ( i \+ z ) % x , z ); add ( i , ( i \+ y ) % x , y ); dis [ i ] = linf ; } spfa (); ll ans = 0 ; for ( int i = 0 ; i < x ; i ++ ) { if ( h >= dis [ i ]) ans += ( h \- dis [ i ]) / x \+ 1 ; } cout << ans << '\n' ; return 0 ; } ```   
---|---  
  
但是事实上也不需要进行正常的最短路求解，注意到有两个特殊的性质：

首先，只有两种边权，且对于每一条路径，由于加法交换律，走两种边权的顺序是无影响的．因此可以考虑做两次最短路，每次只建出一类边权的边；

其次，对于只有一类边权的图，每个点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有一个入度（来自 (𝑢 −𝑦)mod𝑥(u−y)modx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）和一个出度（来自 (𝑢 +𝑦)mod𝑥(u+y)modx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），因此整个图必然由若干个环构成．并且可以证明共有 gcd(𝑥,𝑦)gcd(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个等长的环．

证明

设 𝑑 =gcd(𝑥,𝑦)d=gcd(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设 𝑥 =𝑑𝑎,𝑦 =𝑑𝑏x=da,y=db![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 gcd(𝑎,𝑏) =1gcd(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发走 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步，到达 (𝑢 +𝑘𝑦)mod𝑥(u+ky)modx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若成环，则 𝑘𝑦 ≡0(mod𝑥)ky≡0(modx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即有 𝑘𝑏 ≡0(mod𝑎)kb≡0(moda)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于 gcd(𝑎,𝑏) =1gcd(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最小的 𝑘 =𝑎k=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即环长为 𝑎 =𝑥𝑑a=xd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于是从任意点开始，故每个可能的环长相等，环的数量为 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

并且，边权为正，绕环两圈后，一定不能继续松弛．直接循环更新一遍就行了．这样处理就不会受限于最短路的复杂度，可以做到 𝑂(𝑥)O(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

与差分约束问题相同，当存在一组解 {𝑎1,𝑎2,⋯,𝑎𝑛}{a1,a2,⋯,an}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，{𝑎1 +𝑑,𝑎2 +𝑑,⋯,𝑎𝑛 +𝑑}{a1+d,a2+d,⋯,an+d}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同样为一组解，因此在该题让 𝑖 =1i=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为源点，此时源点处的 𝑑𝑖𝑠1 =1dis1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在已知范围内最小，因此得到的也是一组最小的解．

答案即为：

𝑥−1∑𝑖=0(ℎ−𝑑𝑖𝑥+1)∑i=0x−1(h−dix+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

加 1 是由于 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在楼层也算一次．

代码实现上注意到 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的范围是 ℎ ≤263 −1h≤263−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以在求解最短路之前 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的初始值应至少设为 263263![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这超过了 C++ 中 `long long` 的最大值．所以可以使用 `unsigned long long` 或者先把 ℎ ←ℎ −1h←h−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后把最低楼层设为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层，其他代码无异．

基于环优化的实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 ``` |  ```text #include <algorithm> #include <climits> #include <cstring> #include <iostream> #include <vector> using ll = long long ; constexpr int maxn = 1e5 \+ 100 ; ll d [ maxn ]; bool vis [ maxn ]; ll ans ; int gcd ( int a , int b ) { return b ? gcd ( b , a % b ) : a ; } void upd ( int step , int M ) { int D = gcd ( step , M ); int len = M / D ; for ( int st = 0 ; st < D ; st ++ ) { if ( vis [ st ]) continue ; std :: vector < int > v ; int u = st ; for ( int i = 0 ; i < len ; i ++ ) { v . push_back ( u ); vis [ u ] = true ; u = ( u \+ step ) % M ; } for ( int r = 0 ; r < 2 ; r ++ ) { for ( int i = 0 ; i < len ; i ++ ) { int las = v [ i ]; int now = v [( i \+ 1 ) % len ]; if ( d [ las ] != LLONG_MAX ) { // 如果d[las]=LLONG_MAX，d[las]+step会越界，需要特判 d [ now ] = std :: min ( d [ now ], d [ las ] \+ step ); } } } } } int main () { ll h ; std :: cin >> h ; int x [ 3 ]; for ( int i = 0 ; i < 3 ; i ++ ) { std :: cin >> x [ i ]; } std :: sort ( x , x \+ 3 ); int M = x [ 0 ]; for ( int i = 0 ; i < M ; i ++ ) { d [ i ] = LLONG_MAX ; // 本题的h达到了ll的上界，如果使用ll的话必需把初值置为LLONG_MAX } d [ 0 ] = 0 ; upd ( x [ 1 ], M ); memset ( vis , 0 , sizeof ( vis )); upd ( x [ 2 ], M ); ll H = h \- 1 ; ans = 0 ; for ( int i = 0 ; i < M ; i ++ ) { if ( d [ i ] <= H && d [ i ] != LLONG_MAX ) { ans += ( H \- d [ i ]) / M \+ 1 ; } } printf ( "%lld \n " , ans ); return 0 ; } ```   
---|---  
  
### 例题二

[ARC084B Small Multiple](https://atcoder.jp/contests/arc084/tasks/arc084_b)

题目大意：给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数中，数位和最小的那一个的数位和．（1 ≤𝑛 ≤1051≤n≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

本题可以使用循环卷积优化完全背包在 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内解决，但我们希望得到线性的算法．

观察到任意一个正整数都可以从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始，按照某种顺序执行乘 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的操作，最终得到，而其中加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 操作的次数就是这个数的数位和．这提示我们使用最短路．

对于所有 0 ≤𝑘 ≤𝑛 −10≤k≤n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向 10𝑘10k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连边权为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边；从 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连边权为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边．（点的编号均在模 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下）

每个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数在这个图中都对应了 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号点到 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号点的一条路径，求出 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短路即可．某些路径不合法（如连续走了 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边权为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边），但这些路径产生的答案一定不优，不影响答案．

时间复杂度 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 习题

[洛谷 P3403 跳楼机](https://www.luogu.com.cn/problem/P3403)

[洛谷 P2662 牛场围栏](https://www.luogu.com.cn/problem/P2662)

[[国家集训队] 墨墨的等式](https://www.luogu.com.cn/problem/P2371)

[「NOIP2018」货币系统](https://loj.ac/problem/2951)

[AGC057D - Sum Avoidance](https://atcoder.jp/contests/agc057/tasks/agc057_d)

[「THUPC 2023 初赛」背包](https://loj.ac/p/6872)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/mod-shortest-path.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/mod-shortest-path.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [Xeonacid](https://github.com/Xeonacid), [Jijidawang](https://github.com/Jijidawang), [R-G-Mocoratioen](https://github.com/R-G-Mocoratioen), [TenilTen](https://github.com/TenilTen), [CCXXXI](https://github.com/CCXXXI), [ChungZH](https://github.com/ChungZH), [F1shAndCat](https://github.com/F1shAndCat), [kenlig](https://github.com/kenlig), [Menci](https://github.com/Menci), [ShaoChenHeng](https://github.com/ShaoChenHeng), [shuzhouliu](https://github.com/shuzhouliu), [Tiphereth-A](https://github.com/Tiphereth-A), [XuYueming520](https://github.com/XuYueming520), [zhangletao](https://github.com/zhangletao)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
