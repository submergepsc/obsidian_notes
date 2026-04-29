# 差分约束 - OI Wiki

- Source: https://oi-wiki.org/graph/diff-constraints/

# 差分约束

## 定义

**差分约束系统** 是一种特殊的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元一次不等式组，它包含 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个变量 𝑥1,𝑥2,…,𝑥𝑛x1,x2,…,xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以及 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个约束条件，每个约束条件是由两个其中的变量做差构成的，形如 𝑥𝑖 −𝑥𝑗 ≤𝑐𝑘xi−xj≤ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 1 ≤𝑖,𝑗 ≤𝑛,𝑖 ≠𝑗,1 ≤𝑘 ≤𝑚1≤i,j≤n,i≠j,1≤k≤m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并且 𝑐𝑘ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是常数（可以是非负数，也可以是负数）．我们要解决的问题是：求一组解 𝑥1 =𝑎1,𝑥2 =𝑎2,…,𝑥𝑛 =𝑎𝑛x1=a1,x2=a2,…,xn=an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得所有的约束条件得到满足，否则判断出无解．

差分约束系统中的每个约束条件 𝑥𝑖 −𝑥𝑗 ≤𝑐𝑘xi−xj≤ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以变形成 𝑥𝑖 ≤𝑥𝑗 +𝑐𝑘xi≤xj+ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这与单源最短路中的三角形不等式 𝑑𝑖𝑠𝑡[𝑦] ≤𝑑𝑖𝑠𝑡[𝑥] +𝑧dist[y]≤dist[x]+z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非常相似．因此，我们可以把每个变量 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 看做图中的一个结点，对于每个约束条件 𝑥𝑖 −𝑥𝑗 ≤𝑐𝑘xi−xj≤ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从结点 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向结点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条长度为 𝑐𝑘ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有向边．

注意到，如果 {𝑎1,𝑎2,…,𝑎𝑛}{a1,a2,…,an}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是该差分约束系统的一组解，那么对于任意的常数 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{𝑎1 +𝑑,𝑎2 +𝑑,…,𝑎𝑛 +𝑑}{a1+d,a2+d,…,an+d}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 显然也是该差分约束系统的一组解，因为这样做差后 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 刚好被消掉．

## 过程

设 𝑑𝑖𝑠𝑡[0] =0dist[0]=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并向每一个点连一条权重为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边，跑单源最短路，若图中存在负环，则给定的差分约束系统无解，否则，𝑥𝑖 =𝑑𝑖𝑠𝑡[𝑖]xi=dist[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为该差分约束系统的一组解．

## 性质

一般使用 Bellman–Ford 或队列优化的 Bellman–Ford（俗称 SPFA，在某些随机图跑得很快）判断图中是否存在负环，最坏时间复杂度为 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 常用变形技巧

### 例题 [luogu P1993 小 K 的农场](https://www.luogu.com.cn/problem/P1993)

题目大意：求解差分约束系统，有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条约束条件，每条都为形如 𝑥𝑎 −𝑥𝑏 ≥𝑐𝑘xa−xb≥ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥𝑎 −𝑥𝑏 ≤𝑐𝑘xa−xb≤ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑥𝑎 =𝑥𝑏xa=xb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，判断该差分约束系统有没有解．

题意| 转化| 连边  
---|---|---  
𝑥𝑎 −𝑥𝑏 ≥𝑐xa−xb≥c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 𝑥𝑏 −𝑥𝑎 ≤ −𝑐xb−xa≤−c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `add(a, b, -c);`  
𝑥𝑎 −𝑥𝑏 ≤𝑐xa−xb≤c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 𝑥𝑎 −𝑥𝑏 ≤𝑐xa−xb≤c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `add(b, a, c);`  
𝑥𝑎 =𝑥𝑏xa=xb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 𝑥𝑎 −𝑥𝑏 ≤0, 𝑥𝑏 −𝑥𝑎 ≤0xa−xb≤0, xb−xa≤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `add(b, a, 0), add(a, b, 0);`  
  
跑判断负环，如果不存在负环，输出 `Yes`，否则输出 `No`．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 ``` |  ```text #include <cstring> #include <iostream> #include <queue> using namespace std ; struct edge { int v , w , next ; } e [ 40005 ]; int head [ 10005 ], vis [ 10005 ], tot [ 10005 ], cnt ; long long ans , dist [ 10005 ]; queue < int > q ; void addedge ( int u , int v , int w ) { // 加边 e [ ++ cnt ]. v = v ; e [ cnt ]. w = w ; e [ cnt ]. next = head [ u ]; head [ u ] = cnt ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int n , m ; cin >> n >> m ; for ( int i = 1 ; i <= m ; i ++ ) { int op , x , y , z ; cin >> op ; if ( op == 1 ) { cin >> x >> y >> z ; addedge ( y , x , z ); } else if ( op == 2 ) { cin >> x >> y >> z ; addedge ( x , y , \- z ); } else { cin >> x >> y ; addedge ( x , y , 0 ); addedge ( y , x , 0 ); } } for ( int i = 1 ; i <= n ; i ++ ) addedge ( 0 , i , 0 ); memset ( dist , -0x3f , sizeof ( dist )); dist [ 0 ] = 0 ; vis [ 0 ] = 1 ; q . push ( 0 ); while ( ! q . empty ()) { // 判负环，看上面的 int cur = q . front (); q . pop (); vis [ cur ] = 0 ; for ( int i = head [ cur ]; i ; i = e [ i ]. next ) if ( dist [ cur ] \+ e [ i ]. w > dist [ e [ i ]. v ]) { dist [ e [ i ]. v ] = dist [ cur ] \+ e [ i ]. w ; if ( ! vis [ e [ i ]. v ]) { vis [ e [ i ]. v ] = 1 ; q . push ( e [ i ]. v ); tot [ e [ i ]. v ] ++ ; if ( tot [ e [ i ]. v ] >= n ) { cout << "No \n " ; return 0 ; } } } } cout << "Yes \n " ; return 0 ; } ```   
---|---  
  
### 例题 [P4926[1007] 倍杀测量者](https://www.luogu.com.cn/problem/P4926)

不考虑二分等其他的东西，这里只论述差分系统 𝑥𝑖𝑥𝑗 ≤𝑐𝑘xixj≤ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的求解方法．

对每个 𝑥𝑖,𝑥𝑗xi,xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐𝑘ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取一个 loglog![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以把乘法变成加法运算，即 log⁡𝑥𝑖 −log⁡𝑥𝑗 ≤log⁡𝑐𝑘log⁡xi−log⁡xj≤log⁡ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样就可以用差分约束解决了．

## Bellman–Ford 判负环代码实现

下面是用 Bellman–Ford 算法判断图中是否存在负环的代码实现，请在调用前先保证图是连通的．

实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text bool Bellman_Ford () { for ( int i = 0 ; i < n ; i ++ ) { bool jud = false ; for ( int j = 1 ; j <= n ; j ++ ) for ( int k = h [ j ]; ~ k ; k = nxt [ k ]) if ( dist [ j ] > dist [ p [ k ]] \+ w [ k ]) dist [ j ] = dist [ p [ k ]] \+ w [ k ], jud = true ; if ( ! jud ) break ; } for ( int i = 1 ; i <= n ; i ++ ) for ( int j = h [ i ]; ~ j ; j = nxt [ j ]) if ( dist [ i ] > dist [ p [ j ]] \+ w [ j ]) return false ; return true ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text def Bellman_Ford (): for i in range ( 0 , n ): jud = False for j in range ( 1 , n \+ 1 ): while ~ k : k = h [ j ] if dist [ j ] > dist [ p [ k ]] \+ w [ k ]: dist [ j ] = dist [ p [ k ]] \+ w [ k ] jud = True k = nxt [ k ] if jud == False : break for i in range ( 1 , n \+ 1 ): while ~ j : j = h [ i ] if dist [ i ] > dist [ p [ j ]] \+ w [ j ]: return False j = nxt [ j ] return True ```   
---|---  
  
## 习题

[Usaco2006 Dec Wormholes 虫洞](https://loj.ac/problem/10085)

[「SCOI2011」糖果](https://loj.ac/problem/2436)

[POJ 1364 King](http://poj.org/problem?id=1364)

[POJ 2983 Is the Information Reliable?](http://poj.org/problem?id=2983)

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/diff-constraints.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/diff-constraints.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Anguei](https://github.com/Anguei), [hsfzLZH1](https://github.com/hsfzLZH1), [StudyingFather](https://github.com/StudyingFather), [Enter-tainer](https://github.com/Enter-tainer), [Henry-ZHR](https://github.com/Henry-ZHR), [iamtwz](https://github.com/iamtwz), [Menci](https://github.com/Menci), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [Chrogeek](https://github.com/Chrogeek), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [ImpleLee](https://github.com/ImpleLee), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [shawlleyw](https://github.com/shawlleyw)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
