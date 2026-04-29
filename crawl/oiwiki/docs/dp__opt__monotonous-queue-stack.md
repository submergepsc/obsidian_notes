# 单调队列/单调栈优化 - OI Wiki

- Source: https://oi-wiki.org/dp/opt/monotonous-queue-stack/

# 单调队列/单调栈优化

## 引入

前置知识：[单调队列](../../../ds/monotonous-queue/)、[单调栈](../../../ds/monotonous-stack/)．

单调队列主要用于维护两端指针单调不减的区间最值，而单调栈则主要用于维护前/后第一个大于/小于当前值的数．

注意

  * 求最小值要维护 **单调递增/不减** 的单调队列/单调栈，反之亦然．
  * 维护单调递增/递减比较时用 **小于等于/大于等于** ，维护单调不减/不增比较时用 **小于/大于** ．

## 单调队列优化具体步骤

  * 加入所需元素：向单调队列重复加入元素直到当前元素达到所求区间的右边界，这样就能保证所需元素都在单调队列中．
  * 弹出越界队首：单调队列本质上是维护的是所有已插入元素的最值，但我们想要的往往是一个区间最值．于是我们弹出在左边界外的元素，以保证单调队列中的元素都在所求区间中．
  * 获取最值：直接取队首作为答案即可．

## 单调栈优化具体步骤

  * 弹出非法栈顶：通过比较当前元素与栈顶的大小，弹出不满足单调栈性质的栈顶．以单调递增的栈（即栈顶最大，维护最小值）为例，将所有大于等于当前元素的栈内元素全部弹出．
  * 加入当前元素：将当前元素入栈即可．

## 单调队列优化多重背包

问题描述

你有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品，每个物品重量为 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，价值为 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，数量为 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．你有一个承重上限为 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包，现在要求你在不超过重量上限的情况下选取价值和尽可能大的物品放入背包．求最大价值．

不了解背包 DP 的请先阅读 [背包 DP](../../knapsack/)．设 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品装入承重为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包的最大价值，朴素的转移方程为

𝑓𝑖,𝑗=𝑘𝑖max𝑘=0(𝑓𝑖−1,𝑗−𝑘×𝑤𝑖+𝑣𝑖×𝑘)fi,j=maxk=0ki(fi−1,j−k×wi+vi×k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时间复杂度 𝑂(𝑊∑𝑘𝑖)O(W∑ki)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑优化 𝑓𝑖fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的转移．为方便表述，设 𝑔𝑥,𝑦 =𝑓𝑖,𝑥×𝑤𝑖+𝑦,𝑔′𝑥,𝑦 =𝑓𝑖−1,𝑥×𝑤𝑖+𝑦gx,y=fi,x×wi+y,gx,y′=fi−1,x×wi+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 0 ≤𝑦 <𝑤𝑖0≤y<wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则转移方程可以表示为：

𝑔𝑥,𝑦=𝑘𝑖max𝑘=0(𝑔′𝑥−𝑘,𝑦+𝑣𝑖×𝑘)gx,y=maxk=0ki(gx−k,y′+vi×k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 𝐺𝑥,𝑦 =𝑔′𝑥,𝑦 −𝑣𝑖 ×𝑥Gx,y=gx,y′−vi×x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．则方程可以表示为：

𝑔𝑥,𝑦=𝑘𝑖max𝑘=0(𝐺𝑥−𝑘,𝑦)+𝑣𝑖×𝑥gx,y=maxk=0ki(Gx−k,y)+vi×x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样就转化为一个经典的单调队列优化形式了．𝐺𝑥,𝑦Gx,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算，因此对于固定的 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以在 𝑂(⌊𝑊𝑤𝑖⌋)O(⌊Wwi⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内计算出 𝑔𝑥,𝑦gx,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此求出所有 𝑔𝑥,𝑦gx,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度为 𝑂(⌊𝑊𝑤𝑖⌋) ×𝑂(𝑤𝑖) =𝑂(𝑊)O(⌊Wwi⌋)×O(wi)=O(W)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这样转移的总复杂度就降为 𝑂(𝑛𝑊)O(nW)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在实现的时候，我们需要先枚举 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样才能保证枚举 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候利用单调队列进行优化，而单调队列中存储的是 𝑥 −𝑘x−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并不存储 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样使用的时候需要通过 `f[last][q.front() * w[i] + y] - q.front() * v[i]` 获取对应的 𝐺𝑥−𝑘,𝑦Gx−k,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不难发现 𝑥 −𝑘 ∈[𝑥 −𝑘𝑖,𝑥]x−k∈[x−ki,x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此在枚举 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候，我们需要删除队列中不在这个范围内的元素．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` |  ```text #include <array> #include <deque> #include <iostream> constexpr int MAXV = 4e4 \+ 10 ; constexpr int MAXN = 1e2 \+ 10 ; using namespace std ; int n , W , last = 0 , now = 1 ; array < int , MAXN > v , w , k ; array < array < int , MAXV > , 2 > f ; deque < int > q ; int main () { ios :: sync_with_stdio ( false ); cin >> n >> W ; for ( int i = 1 ; i <= n ; i ++ ) { cin >> v [ i ] >> w [ i ] >> k [ i ]; } for ( int i = 1 ; i <= n ; i ++ ) { for ( int y = 0 ; y < w [ i ]; y ++ ) { // 清空队列 deque < int > (). swap ( q ); for ( int x = 0 ; x * w [ i ] \+ y <= W ; x ++ ) { // 弹出不在范围的元素 while ( ! q . empty () && q . front () < x \- k [ i ]) { q . pop_front (); } // 保证队列单调 while ( ! q . empty () && f [ last ][ q . back () * w [ i ] \+ y ] \- q . back () * v [ i ] < f [ last ][ x * w [ i ] \+ y ] \- x * v [ i ]) { q . pop_back (); } q . push_back ( x ); f [ now ][ x * w [ i ] \+ y ] = f [ last ][ q . front () * w [ i ] \+ y ] \- q . front () * v [ i ] \+ x * v [ i ]; } } swap ( last , now ); } cout << f [ last ][ W ] << endl ; return 0 ; } ```   
---|---  
  
## 习题

例题 [CF372C Watching Fireworks is Fun](http://codeforces.com/problemset/problem/372/C)

题目大意：城镇中有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个位置，有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个烟花要放．第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个烟花放出的时间记为 𝑡𝑖ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，放出的位置记为 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果烟花放出的时候，你处在位置 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么你将收获 𝑏𝑖 −|𝑎𝑖 −𝑥|bi−|ai−x|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点快乐值．

初始你可在任意位置，你每个单位时间可以移动不大于 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个单位距离．现在你需要最大化你能获得的快乐值．

设 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示在放第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个烟花时，你的位置在 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所能获得的最大快乐值．

写出状态转移方程：𝑓𝑖,𝑗 =max{𝑓𝑖−1,𝑘 +𝑏𝑖 −|𝑎𝑖 −𝑗|}fi,j=max{fi−1,k+bi−|ai−j|}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑗 −(𝑡𝑖 −𝑡𝑖−1) ×𝑑 ≤𝑘 ≤𝑗 +(𝑡𝑖 −𝑡𝑖−1) ×𝑑j−(ti−ti−1)×d≤k≤j+(ti−ti−1)×d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

尝试变形：

由于 maxmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 里出现了一个确定的常量 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以将它提到外面去．

𝑓𝑖,𝑗 =max{𝑓𝑖−1,𝑘 +𝑏𝑖 −|𝑎𝑖 −𝑗|} =max{𝑓𝑖−1,𝑘 −|𝑎𝑖 −𝑗|} +𝑏𝑖fi,j=max{fi−1,k+bi−|ai−j|}=max{fi−1,k−|ai−j|}+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果确定了 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，那么 |𝑎𝑖 −𝑗||ai−j|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值也是确定的，也可以将这一部分提到外面去．

最后，式子变为：

𝑓𝑖,𝑗=max{𝑓𝑖−1,𝑘−|𝑎𝑖−𝑗|}+𝑏𝑖=max{𝑓𝑖−1,𝑘}−|𝑎𝑖−𝑗|+𝑏𝑖fi,j=max{fi−1,k−|ai−j|}+bi=max{fi−1,k}−|ai−j|+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

接下来考虑单调队列优化．由于最终式子中的 maxmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只和上一状态中连续的一段的最大值有关，所以我们在计算一个新的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的状态值时候只需将原来的 𝑓𝑖−1fi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构造成一个单调队列，并维护单调队列，使得其能在均摊 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内计算出 max{𝑓𝑖−1,𝑘}max{fi−1,k}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，从而根据公式计算出 𝑓𝑖,𝑗fi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

总的时间复杂度为 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``` |  ```text #include <algorithm> #include <cstring> #include <iostream> using namespace std ; using ll = long long ; constexpr int MAXN = 150000 \+ 10 ; constexpr int MAXM = 300 \+ 10 ; ll f [ 2 ][ MAXN ]; ll a [ MAXM ], b [ MAXM ], t [ MAXM ]; int n , m , d ; int que [ MAXN ]; int fl = 1 ; void init () { memset ( f , 207 , sizeof ( f )); memset ( que , 0 , sizeof ( que )); for ( int i = 1 ; i <= n ; i ++ ) f [ 0 ][ i ] = 0 ; fl = 1 ; } void dp () { init (); for ( int i = 1 ; i <= m ; i ++ ) { int l = 1 , r = 0 , k = 1 ; for ( int j = 1 ; j <= n ; j ++ ) { // 在这里使用了单调队列的优化，推式子详见上面 for (; k <= min ( 1l l * n , j \+ d * ( t [ i ] \- t [ i \- 1 ])); k ++ ) { while ( l <= r && f [ fl ^ 1 ][ que [ r ]] <= f [ fl ^ 1 ][ k ]) r \-- ; que [ ++ r ] = k ; } while ( l <= r && que [ l ] < max ( 1l l , j \- d * ( t [ i ] \- t [ i \- 1 ]))) l ++ ; f [ fl ][ j ] = f [ fl ^ 1 ][ que [ l ]] \- abs ( a [ i ] \- j ) \+ b [ i ]; } fl ^= 1 ; } } int main () { cin >> n >> m >> d ; for ( int i = 1 ; i <= m ; i ++ ) cin >> a [ i ] >> b [ i ] >> t [ i ]; // then dp dp (); ll ans = -1e18 ; for ( int i = 1 ; i <= n ; i ++ ) ans = max ( ans , f [ fl ^ 1 ][ i ]); cout << ans << endl ; return 0 ; } ```   
---|---  
  
  * [「Luogu P1886」滑动窗口](https://loj.ac/problem/10175)
  * [「NOI2005」瑰丽华尔兹](https://www.luogu.com.cn/problem/P2254)
  * [「SCOI2010」股票交易](https://loj.ac/problem/10183)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/opt/monotonous-queue-stack.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/opt/monotonous-queue-stack.md "edit.link.title")  
>  __本页面贡献者：[StudyingFather](https://github.com/StudyingFather), [sshwy](https://github.com/sshwy), [Ir1d](https://github.com/Ir1d), [fogsail](https://github.com/fogsail), [ouuan](https://github.com/ouuan), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [liujiaxi123456](https://github.com/liujiaxi123456), [Marcythm](https://github.com/Marcythm), [Tiphereth-A](https://github.com/Tiphereth-A), [Anguei](https://github.com/Anguei), [billchenchina](https://github.com/billchenchina), [c-forrest](https://github.com/c-forrest), [Crescent12138](https://github.com/Crescent12138), [Enter-tainer](https://github.com/Enter-tainer), [fps5283](https://github.com/fps5283), [greyqz](https://github.com/greyqz), [Henry-ZHR](https://github.com/Henry-ZHR), [hsfzLZH1](https://github.com/hsfzLZH1), [IceySakura](https://github.com/IceySakura), [Kaiser-Yang](https://github.com/Kaiser-Yang), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [Licheam](https://github.com/Licheam), [NachtgeistW](https://github.com/NachtgeistW), [partychicken](https://github.com/partychicken), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
