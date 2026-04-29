# 四边形不等式优化 - OI Wiki

- Source: https://oi-wiki.org/dp/opt/quadrangle/

# 四边形不等式优化

四边形不等式优化利用的是状态转移方程中的决策单调性，也常称为 **决策单调性优化 DP** ．

## 基础知识

考虑最简单的情形，我们要解决如下一系列最优化问题：

𝑓(𝑖)=min1≤𝑗≤𝑖𝑤(𝑗,𝑖)(1≤𝑖≤𝑛)(1)(1)f(i)=min1≤j≤iw(j,i)(1≤i≤n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里假定成本函数 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算．

约定

动态规划的状态转移方程经常可以写作一系列最优化问题的形式．以（1）式为例，这些问题含有参数 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，问题的目标函数和可行域都可以依赖于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每一个问题都是在给定参数 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，选取某个可行解 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来最小化目标函数的取值．为表述方便，下文将参数为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优化问题简称为「问题 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」，该最优化问题的可行解 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为「决策 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」，目标函数在最优解处取得的值则称为「状态 𝑓(𝑖)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」．同时，记问题 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的最小最优决策点为 opt⁡(𝑖)opt⁡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在一般的情形下，这些问题总时间复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这是由于对于问题 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们需要考虑所有可能的决策 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而在满足决策单调性时，可以有效缩小决策空间，优化总复杂度．

  * **决策单调性** ：对于任意 𝑖1 <𝑖2i1<i2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必然成立 opt⁡(𝑖1) ≤opt⁡(𝑖2)opt⁡(i1)≤opt⁡(i2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

附注

对于问题 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最优决策集合未必是一个区间．决策单调性实际可以定义在最优决策集合上．对于集合 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以定义 𝐴 ≤𝐵A≤B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当对于任意 𝑎 ∈𝐴a∈A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏 ∈𝐵b∈B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，成立 min{𝑎,𝑏} ∈𝐴min{a,b}∈A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 max{𝑎,𝑏} ∈𝐵max{a,b}∈B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这蕴含最小（最大）最优决策点的单调性，即此处采取的定义．本文关于最小最优决策点叙述的结论，同样适用于最大最优决策点．但是，存在情形，某更大问题的最小最优决策严格小于另一更小问题的最大最优决策，亦即可能对某些 𝑖1 <𝑖2i1<i2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立 optmax⁡(𝑖1) >optmin⁡(𝑖2)optmax⁡(i1)>optmin⁡(i2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以在书写代码时，应保证总是求得最小或最大的最优决策点．

另一方面，拥有相同最小最优决策的问题构成一个区间．这一区间，作为最小最优决策的函数，应严格递增．亦即，给定 𝑗1 =opt⁡(𝑖1)j1=opt⁡(i1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑗2 =opt⁡(𝑖2)j2=opt⁡(i2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果 𝑗1 <𝑗2j1<j2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么必然有 𝑖1 <𝑖2i1<i2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．换言之，如果决策 𝑗1 <𝑗2j1<j2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能够成为最小最优决策的问题区间分别是 [𝑙𝑗1,𝑟𝑗1][lj1,rj1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 [𝑙𝑗2,𝑟𝑗2][lj2,rj2]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么必然有 𝑟𝑗1 <𝑙𝑗2rj1<lj2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最常见的判断决策单调性的方法是通过四边形不等式（quadrangle inequality）．在不同的语境下，这一性质也常称为 Monge 性质（用于描述矩阵 𝐴𝑗,𝑖Aj,i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）或次模性（submodularity，用于描述以区间为自变量的函数 𝑓([𝑗,𝑖])f([j,i])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

  * **四边形不等式** ：如果对于任意 𝑎 ≤𝑏 ≤𝑐 ≤𝑑a≤b≤c≤d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均成立

𝑤(𝑎,𝑐)+𝑤(𝑏,𝑑)≤𝑤(𝑎,𝑑)+𝑤(𝑏,𝑐),w(a,c)+w(b,d)≤w(a,d)+w(b,c),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则称函数 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式（简记为「交叉小于包含」）．若等号永远成立，则称函数 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 **四边形恒等式** ．

如果没有特别说明，以下都会保证 𝑎 ≤𝑏 ≤𝑐 ≤𝑑a≤b≤c≤d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．四边形不等式给出了一个决策单调性的充分不必要条件．

定理 1

若 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式，则问题 (1) 满足决策单调性．

证明

要证明这一点，可采用反证法．假设对某些 𝑐 <𝑑c<d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，成立 𝑎 =opt⁡(𝑑) <opt⁡(𝑐) =𝑏a=opt⁡(d)<opt⁡(c)=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时有 𝑎 <𝑏 ≤𝑐 <𝑑a<b≤c<d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据最优化条件，𝑤(𝑎,𝑑) ≤𝑤(𝑏,𝑑)w(a,d)≤w(b,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑤(𝑏,𝑐) <𝑤(𝑎,𝑐)w(b,c)<w(a,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是，𝑤(𝑎,𝑑) −𝑤(𝑏,𝑑) ≤0 <𝑤(𝑎,𝑐) −𝑤(𝑏,𝑐)w(a,d)−w(b,d)≤0<w(a,c)−w(b,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这与四边形不等式矛盾．

四边形不等式可以理解在合理的定义域内，𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二阶混合差分 Δ𝑖Δ𝑗𝑤(𝑗,𝑖)ΔiΔjw(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非正．

利用决策单调性，有很多常见算法都可以将算法复杂度优化到 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这些算法的适用范围、实现难度、运行效率各不相同，需要根据实际场景选择合适的算法．这主要取决于 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的性质．不加说明时，本文默认 𝑤(𝑖,𝑗)w(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以 **随机访问** ，即 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内查询或计算．但是，并非所有问题中，𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都这样容易计算．因此，除了基本情形外，本文还讨论了 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只具有如下性质时，利用决策单调性优化 DP 的方法：

  * **移动访问** ：𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以从 𝑤(𝑗 ±1,𝑖)w(j±1,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑤(𝑗,𝑖 ±1)w(j,i±1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间转移得到．（类似 [莫队算法](../../../misc/mo-algo/) 中的情形）
  * **动态计算** ：𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算依赖于 {𝑓(𝑗′) :𝑗′ <𝑗}{f(j′):j′<j}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这意味着 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只能顺次计算．下文介绍了不限制区间个数的区间分拆问题，它就属于这一情形．

这两条性质并不互斥，可能存在 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既需要动态计算，又只支持移动访问的情形．

### 分治

要求解所有状态，只需要求解所有最优决策点．为了对所有 1 ≤𝑖 ≤𝑛1≤i≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求解 opt⁡(𝑖)opt⁡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，首先计算 opt⁡(𝑛/2)opt⁡(n/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而后分别计算 1 ≤𝑖 <𝑛/21≤i<n/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛/2 <𝑖 ≤𝑛n/2<i≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的 opt⁡(𝑖)opt⁡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，注意此时已知前半段的 opt⁡(𝑖)opt⁡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然位于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 opt⁡(𝑛/2)opt⁡(n/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间（含端点），而后半段的 opt⁡(𝑖)opt⁡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然位于 opt⁡(𝑛/2)opt⁡(n/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间（含端点）．对于两个子区间，也类似处理，直至计算出每个问题的最优决策．在分治的过程中记录搜索的上下边界，就可以保证算法复杂度控制在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．递归树层数为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而每层中，单个决策点至多计算两次，所以总的计算次数是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` |  ```text val_t w ( int j , int i ); // 成本函数 val_t f [ N ]; // 最优值 int opt [ N ]; // 最小最优决策 // 递归求解 [l,r] 中的问题 // 已知它们的最小最优决策点一定出现在区间 [opt_l, opt_r] 中 void calc ( int l , int r , int opt_l , int opt_r ) { int mid = ( l \+ r ) / 2 ; // 求问题 mid 的最优决策点 for ( int j = opt_l ; j <= std :: min ( opt_r , mid ); ++ j ) { if ( w ( j , mid ) < f [ mid ]) { f [ mid ] = w ( j , mid ); opt [ mid ] = j ; } } // 根据决策单调性得出左右两部分的决策区间，递归处理 if ( l < mid ) calc ( l , mid \- 1 , opt_l , opt [ mid ]); if ( r > mid ) calc ( mid \+ 1 , r , opt [ mid ], opt_r ); } // 求解整个区间 [1,n] 的问题 void solve ( int n ) { // 每次调用递归函数前，都需要清空数组 f std :: fill ( f \+ 1 , f \+ n \+ 1 , inf ); // 最开始时，只知道问题 [1,n] 的所有决策点都一定在 [1,n] 中 calc ( 1 , n , 1 , n ); } ```   
---|---  
  
除了随机访问的基本情形外，分治算法还可以应用于 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只支持移动访问的情形．只需要在计算过程中维护游标 (𝑗,𝑖)(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和相应函数值 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在需要查询新的值时，将游标暴力移动到当前位置并更新函数值即可．这样做的时间复杂度仍然为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对此更为详细的讨论，可以参考下文 简化 LARSCH 算法 一节．但是，分治算法无法解决 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要动态计算的情形，因为分治算法没有办法在左半区间问题尚未解决时，就计算出区间中点处的最小最优决策 opt⁡(𝑛/2)opt⁡(n/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 二分队列

注意到对于每个决策点 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，能使其成为最小最优决策点的问题 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然构成一个区间．可以通过单调队列记录到目前为止每个决策点可以解决的问题的区间，这样，问题的最优解自然可以通过队列中记录的决策点计算得到．

具体地，算法需要顺次遍历决策点．当遍历到决策点 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，队列中需要记录到目前为止每个可行的决策点 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和能够解决的问题区间左右端点 𝑙𝑗lj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟𝑗rj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成的 **三元组** ．对于给定区间 [𝑙𝑗,𝑟𝑗][lj,rj]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的问题，𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应该是到目前为止考虑过的决策点（即区间 [1,𝑘][1,k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的决策点）中最小最优的．每时每刻，队列中存储的决策未必是连续的，但是尚未解决的问题 [𝑗,𝑛][j,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应该是队列中存储的问题区间的不交并．

为了说明队列更新过程中，决策点 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是最小最优决策的问题 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总构成一段连续的区间，需要适当加强前文的结论：

推论 1

设 opt𝑘⁡(𝑖)optk⁡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是仅考虑 [1,𝑘][1,k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的决策时，问题 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小最优决策．如果 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式，那么对于任意 𝑖1 <𝑖2i1<i2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必然成立 opt𝑘⁡(𝑖1) ≤opt𝑘⁡(𝑖2)optk⁡(i1)≤optk⁡(i2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

设 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是充分大的正实数．函数 𝑤′(𝑗,𝑖) =𝑤(𝑗,𝑖) +𝑀[𝑗 >𝑘]w′(j,i)=w(j,i)+M[j>k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然满足四边形不等式，其中，[ ⋅][⋅]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Iverson 括号．考虑以 𝑤′w′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为成本函数的辅助 DP．在辅助 DP 中，对于任何问题 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，决策 𝑗 >𝑘j>k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都不可能是最小最优的，即 opt′⁡(𝑖) =opt′𝑘⁡(𝑖) =opt𝑘⁡(𝑖)opt′⁡(i)=optk′⁡(i)=optk⁡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对辅助 DP 应用定理 1 就得到本推论．

该算法过程如下：1

  * 初始时，队列是空的．类似于单调队列，每次考虑下一个决策 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候，都需要进行出队和入队操作．
  * **出队** ：首先将上一个问题 𝑗 −1j−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从队列中移除．如果队首的决策能够解决的问题的右端点恰为 𝑗 −1j−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直接弹出队首；否则，将队首决策能够解决问题的左端点更新为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * **入队** ：要对决策 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行入队时，首先比较它和队尾的决策 𝑗′j′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
    * 如果对于问题 𝑙𝑗′lj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将要入队的决策 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比已有的决策 𝑗′j′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 严格更优，即 𝑤(𝑗,𝑙𝑗′) <𝑤(𝑗′,𝑙𝑗′)w(j,lj′)<w(j′,lj′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，则弹出队尾的决策 𝑗′j′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此操作持续到队列为空或队尾的决策 𝑗′j′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比起 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于问题 𝑙𝑗′lj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更优时为止．
    * 如果队列已空，入队 (𝑗,𝑗,𝑛)(j,j,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即认为决策 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是尚未解决的所有问题的最优解．
    * 如果队尾决策 𝑗′j′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于问题 𝑟𝑗′rj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同样不劣于将入队的决策 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么当 𝑟𝑗′ <𝑛rj′<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，入队 (𝑗,𝑟𝑗′ +1,𝑛)(j,rj′+1,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是问题 [𝑟𝑗′ +1,𝑛][rj′+1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小最优决策；否则，不需要入队 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为它并不比已有的决策更优．
    * 最后的情形是，队尾决策 𝑗′j′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比起要入队的决策 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于问题 𝑙𝑗′lj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 严格更优，而对于问题 𝑟𝑗′rj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 严格更劣．这说明，存在问题 𝑖 ∈(𝑙𝑗′,𝑟𝑗′]i∈(lj′,rj′]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得问题 [𝑙𝑗′,𝑖 −1][lj′,i−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小最优决策为 𝑗′j′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且问题 [𝑖,𝑟𝑗′][i,rj′]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小最优决策为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因而，需要通过 **二分** 找到最小的 𝑖 ∈[𝑙𝑗′,𝑟𝑗′]i∈[lj′,rj′]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑤(𝑗,𝑖) <𝑤(𝑗′,𝑖)w(j,i)<w(j′,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再将队尾的区间右端点 𝑟𝑗′rj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 修改为 𝑖 −1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并入队 (𝑗,𝑖,𝑛)(j,i,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 处理完决策 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，就已经处理了所有到 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为止的决策．此时，队首决策就是问题 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小最优决策，可以记录相应的最优解．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 ``` |  ```text val_t w ( int j , int i ); // 成本函数 val_t f [ N ]; // 最优值 int opt [ N ]; // 最小最优决策 int lt [ N ], rt [ N ]; // 决策 j 可以解决的问题区间 [l_j,r_j] // 求解整个区间 [1,n] 的问题 void solve ( int n ) { std :: deque < int > dq ; // 存储所有可行决策的单调队列 // 顺次考虑所有问题和决策，下标从 1 开始 for ( int j = 1 ; j <= n ; ++ j ) { // 出队 if ( ! dq . empty () && rt [ dq . front ()] < j ) dq . pop_front (); if ( ! dq . empty ()) lt [ dq . front ()] = j ; // 入队 while ( ! dq . empty () && w ( j , lt [ dq . back ()]) < w ( dq . back (), lt [ dq . back ()])) { dq . pop_back (); } if ( dq . empty ()) { lt [ j ] = j ; rt [ j ] = n ; dq . emplace_back ( j ); } else if ( w ( j , rt [ dq . back ()]) >= w ( dq . back (), rt [ dq . back ()])) { if ( rt [ dq . back ()] < n ) { lt [ j ] = rt [ dq . back ()] \+ 1 ; rt [ j ] = n ; dq . emplace_back ( j ); } } else { int ll = lt [ dq . back ()], rr = rt [ dq . back ()], i = rr ; // 二分 while ( ll <= rr ) { int mm = ( ll \+ rr ) / 2 ; if ( w ( j , mm ) < w ( dq . back (), mm )) { i = mm ; rr = mm \- 1 ; } else { ll = mm \+ 1 ; } } rt [ dq . back ()] = i \- 1 ; lt [ j ] = i ; rt [ j ] = n ; dq . emplace_back ( j ); } // 计算 f [ j ] = w ( dq . front (), j ); opt [ j ] = dq . front (); } } ```   
---|---  
  
类似于单调队列，每个决策点至多入队一次，出队一次．其中，出队是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，而入队是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的（可能需要二分），所以总的时间复杂度是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于二分队列算法顺次考虑所有问题和决策点，它可以应用于 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要动态计算的情形．这是它相较于分治算法的优势．但是，因为算法中的二分步骤依赖于对 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的随机访问，它无法应用于 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只支持移动访问的情形．

例题 1：[「POI2011」Lightning Conductor](https://loj.ac/problem/2157)

给定一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 𝑎1,𝑎2,⋯,𝑎𝑛a1,a2,⋯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要求对于每一个 1 ≤𝑖 ≤𝑛1≤i≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，找到最小的非负整数 𝑓𝑖fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足

∀𝑗∈[1,𝑛]:𝑎𝑗≤𝑎𝑖+𝑓𝑖−√|𝑖−𝑗|.∀j∈[1,n]:aj≤ai+fi−|i−j|.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)思路

显然，经过不等式变形，我们可以得到待求整数 𝑓𝑖 =max𝑗{𝑎𝑗 +√|𝑖−𝑗| −𝑎𝑖}fi=maxj{aj+|i−j|−ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．不妨先考虑 𝑗 ≤𝑖j≤i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况（另外一种情况类似），此时我们可以得到状态转移方程：

𝑓𝑖=−min𝑗≤𝑖{−𝑎𝑗−√𝑖−𝑗+𝑎𝑖}.fi=−minj≤i{−aj−i−j+ai}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据 −√𝑥−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸性，我们很容易得出（后文将详细描述）函数 𝑤(𝑙,𝑟) = −𝑎𝑙 −√𝑟−𝑙 +𝑎𝑟w(l,r)=−al−r−l+ar![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式，因此套用上述的算法便可在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内解决此题了．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 ``` |  ```text #include <algorithm> #include <cmath> #include <deque> #include <iostream> #define all \ for (auto i : {&q, &l, &r}) (*i) using namespace std ; int n , a [ 500009 ], ans [ 500009 ]; deque < int > q , l , r ; double f ( int i , int j ) { return a [ i ] \+ sqrtl ( j \- i ); } void work () { all . clear (); for ( int i = 0 ; i < n ; ++ i ) { if ( q . size () && r . front () < i ) all . pop_front (); // 队首出队 if ( q . size ()) l . front () = i ; for (; q . size () && f ( q . back (), l . back ()) <= f ( i , l . back ());) // 队尾出队 all . pop_back (); if ( q . empty ()) // 入队 q . emplace_back ( i ), l . emplace_back ( i ), r . emplace_back ( n ); else if ( f ( q . back (), n ) < f ( i , n )) { int ll = l . back (), rr = n , mid ; for (; ll <= rr ;) { mid = ( ll \+ rr ) >> 1 ; if ( f ( q . back (), mid ) < f ( i , mid )) rr = mid \- 1 ; else ll = mid \+ 1 ; } r . back () = rr ; q . emplace_back ( i ), l . emplace_back ( ll ), r . emplace_back ( n ); } ans [ i ] = max ( ans [ i ], ( int )( ceil ( f ( q . front (), i ))) \- a [ i ]); } } int main () { cin >> n ; for ( int i = 0 ; i < n ; cin >> a [ i ++ ]); work (); reverse ( a , a \+ n ); reverse ( ans , ans \+ n ); work (); reverse ( ans , ans \+ n ); for ( int i = 0 ; i < n ; cout << ans [ i ++ ] << '\n' ); } ```   
---|---  
  
### 简化 LARSCH 算法

前两种算法都无法处理 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既需要动态计算，也只支持移动访问的情形．本节介绍一种能够同时克服这两种困难的算法．它是 Larmore 和 Schieber 在 1991 年提出的 LARSCH 算法2的简化版本，故称为 **简化 LARSCH 算法** ．该算法的原始版本可以在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内解决决策单调性 DP 问题，但实现较复杂，本文不做介绍．

仍然考虑分治求解．求解区间 (𝑙,𝑟](l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的问题时，假设如下信息已知：

  * 区间 [1,𝑙][1,l]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中问题 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小最优决策 opt⁡(𝑖)opt⁡(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和最优值，以及
  * 仅考虑区间 [1,𝑙][1,l]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的决策，问题 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小最优决策 opt𝑙⁡(𝑟)optl⁡(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和最优值．

区间 (𝑙,𝑟](l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的问题求解结束时，需要得到区间 (𝑙,𝑟](l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内问题的最小最优决策和最优值．

设 𝑚𝑖𝑑mid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为区间 (𝑙,𝑟](l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的中点．求解过程如下：

  1. 遍历决策 𝑖 ∈[opt⁡(𝑙),opt𝑙⁡(𝑟)]i∈[opt⁡(l),optl⁡(r)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，更新问题 𝑚𝑖𝑑mid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小最优决策和最优值．
  2. 递归求解区间 (𝑙,𝑚𝑖𝑑](l,mid]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的问题．
  3. 遍历决策 𝑖 ∈(𝑙,𝑚𝑖𝑑]i∈(l,mid]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，更新问题 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小最优决策和最优值．
  4. 递归求解区间 (𝑚𝑖𝑑,𝑟](mid,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的问题．

对整个区间 [1,𝑛][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 执行递归前，首先需要用决策 𝑗 =1j=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更新问题 𝑖 ∈{1,𝑛}i∈{1,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．该算法在递归到 𝑙 =𝑟l=r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时就终止．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text val_t w ( int j , int i ); // 成本函数 val_t f [ N ]; // 最优值 int opt [ N ]; // 最小最优决策 // 用决策 j 更新问题 i void check ( int j , int i ) { if ( w ( j , i ) < f [ i ]) { f [ i ] = w ( j , i ); opt [ i ] = j ; } } // 递归求解区间 (l, r] 内的问题 void calc ( int l , int r ) { int mid = ( l \+ r \+ 1 ) / 2 ; for ( int j = opt [ l ]; j <= opt [ r ]; ++ j ) check ( j , mid ); if ( mid < r ) calc ( l , mid ); for ( int j = l \+ 1 ; j <= mid ; ++ j ) check ( j , r ); if ( mid > l ) calc ( mid , r ); } // 求解整个区间 [1, n] 内的问题 void solve ( int n ) { // 清空 f 数组 std :: fill ( f \+ 1 , f \+ n \+ 1 , inf ); // 初始化 check ( 1 , 1 ); check ( 1 , n ); // 递归求解区间 (1, n] 内的问题 calc ( 1 , n ); } ```   
---|---  
  
首先，可以说明这一算法的正确性．为此，只要检查每一递归求解的步骤（即步骤 2 和 4）前都满足上文给出的前提条件．由前一节得到的推论 1，有 opt⁡(𝑙) =opt𝑙⁡(𝑙) ≤opt𝑙⁡(𝑚𝑖𝑑) ≤opt𝑙⁡(𝑟)opt⁡(l)=optl⁡(l)≤optl⁡(mid)≤optl⁡(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以步骤 1 后，opt𝑙⁡(𝑚𝑖𝑑)optl⁡(mid)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是已知的，进而执行步骤 2 前递归求解区间 (𝑙,𝑚𝑖𝑑](l,mid]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中问题的前提条件成立．由于之前 {opt⁡(𝑖) :𝑖 ∈[1,𝑙]}{opt⁡(i):i∈[1,l]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是已知的，步骤 2 又得到了 {opt⁡(𝑖) :𝑖 ∈(𝑙,𝑚𝑖𝑑]}{opt⁡(i):i∈(l,mid]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值，所以这之后 {opt⁡(𝑖) :𝑖 ∈[1,𝑚𝑖𝑑]}{opt⁡(i):i∈[1,mid]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是已知的；同时，由于之前 opt𝑙⁡(𝑟)optl⁡(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是已知的，步骤 3 后，opt𝑚𝑖𝑑⁡(𝑟)optmid⁡(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就也是已知的．因此，执行步骤 4 前递归求解区间 (𝑚𝑖𝑑,𝑟](mid,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中问题的前提条件也成立．

然后，需要说明该算法的复杂度仍然是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．递归树的层数是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．对于递归树中的同一层的每个结点，分别遍历区间 [opt⁡(𝑙),opt𝑙⁡(𝑟)][opt⁡(l),optl⁡(r)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑙,𝑚𝑖𝑑](l,mid]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的决策．因为 opt⁡(𝑙) ≤opt𝑙⁡(𝑟) ≤opt⁡(𝑟)opt⁡(l)≤optl⁡(r)≤opt⁡(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以在同一层中，每个决策点只遍历了 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．故而，递归树的每一层中总的遍历次数是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．假设单次访问或计算 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，算法的时间复杂度就是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

对于一些 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只支持移动访问的情形，这一算法的复杂度仍然是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．此时，需要为算法流程中的步骤 1 和步骤 3 分别维护游标 (𝑗,𝑖)(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的当前取值．每次需要访问新的值时，需要将游标 (𝑗,𝑖)(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从上一次访问时的位置暴力更新到当前位置，并对函数值 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行转移．容易验证，当对递归树进行遍历时，这些暴力更新的总次数是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．所以，算法的时间复杂度仍然是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

非随机访问的复杂度证明

只需要证明游标移动的总次数是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为步骤 1 和 3 对应的游标．实际上可以保证：在求解区间 (𝑙,𝑟](l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题之前，游标 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处于位置 (opt⁡(𝑙),𝑙)(opt⁡(l),l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，游标 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处于位置 (𝑙,𝑙)(l,l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；而在这之后，游标 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处于位置 (opt⁡(𝑟),𝑟)(opt⁡(r),r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，游标 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处于位置 (𝑟,𝑟)(r,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑构造如下游标移动规则．步骤 1 中，可以令游标 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 沿着路径

(opt⁡(𝑙),𝑙)→(opt⁡(𝑙),𝑚𝑖𝑑)→(opt𝑙⁡(𝑟),𝑚𝑖𝑑)→(opt⁡(𝑙),𝑚𝑖𝑑)→(opt⁡(𝑙),𝑙)(opt⁡(l),l)→(opt⁡(l),mid)→(optl⁡(r),mid)→(opt⁡(l),mid)→(opt⁡(l),l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

移动．此时，游标 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均处于求解区间 (𝑙,𝑚𝑖𝑑](l,mid]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题之前的规定位置上．步骤 2 中，按规定，游标 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将移动到 (opt⁡(𝑚𝑖𝑑),𝑚𝑖𝑑)(opt⁡(mid),mid)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，游标 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将移动到 (𝑚𝑖𝑑,𝑚𝑖𝑑)(mid,mid)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．步骤 3 中，可以令游标 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 沿着路径

(𝑚𝑖𝑑,𝑚𝑖𝑑)→(𝑙,𝑚𝑖𝑑)→(𝑙,𝑟)→(𝑚𝑖𝑑,𝑟)→(𝑚𝑖𝑑,𝑚𝑖𝑑)(mid,mid)→(l,mid)→(l,r)→(mid,r)→(mid,mid)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

移动．此时，游标 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均处于求解区间 (𝑚𝑖𝑑,𝑟](mid,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题之前的规定位置上．步骤 4 中，按规定，游标 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将移动到 (opt⁡(𝑟),𝑟)(opt⁡(r),r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，游标 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将移动到 (𝑟,𝑟)(r,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．两个游标均在结束求解区间 (𝑙,𝑟](l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题的规定位置上．因此，这一移动规则符合上述规定．而且，该移动规则足以完成步骤 1 和 3 中的所有计算．直接计算该规则中游标的移动次数可知，步骤 1 需要

2(opt𝑙⁡(𝑟)−opt⁡(𝑙))+2(𝑚𝑖𝑑−𝑙)2(optl⁡(r)−opt⁡(l))+2(mid−l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

次移动，步骤 3 需要

2(𝑚𝑖𝑑−𝑙)+2(𝑟−𝑚𝑖𝑑)=2(𝑟−𝑙)2(mid−l)+2(r−mid)=2(r−l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

次移动．将这些移动次数对递归树中的所有结点求和，利用同一层中的所有 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 [opt⁡(𝑙),opt𝑙⁡(𝑟)][opt⁡(l),optl⁡(r)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至多只在端点处重合这一性质，就可以说明总的移动次数是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

由于上述移动规则比起实际计算时游标的移动设置了更多的途径点，所以游标的实际移动次数不会超过该规则下移动次数的估计．因此，游标的实际移动次数也是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

由于该算法在求解区间 (𝑙,𝑟](l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题前，已经计算出了区间 [1,𝑙][1,l]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的最优解 𝑓(𝑖)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以该算法也可以应用于 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要动态计算的情形．

## 区间分拆问题

考虑将某个区间拆分成若干个子区间的问题．形式化地说，将给定区间 [1,𝑛][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拆分成 [𝑎1,𝑏1],⋯,[𝑎𝑘,𝑏𝑘][a1,b1],⋯,[ak,bk]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑎1 =1a1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏𝑘 =𝑛bk=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以及 𝑏𝑖 +1 =𝑎𝑖+1bi+1=ai+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对任意 𝑖 <𝑘i<k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．对于给定拆分，成本为 ∑𝑘𝑖=1𝑤(𝑎𝑖,𝑏𝑖)∑i=1kw(ai,bi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．问题要求最小化这一成本．可以列出如下的 1D1D 状态转移方程．

𝑓(𝑖)=min1≤𝑗≤𝑖𝑓(𝑗−1)+𝑤(𝑗,𝑖)(1≤𝑖≤𝑛)f(i)=min1≤j≤if(j−1)+w(j,i)(1≤i≤n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，𝑓(0) =0f(0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意到，只要 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式，𝑓(𝑗 −1) +𝑤(𝑗,𝑖)f(j−1)+w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然满足四边形不等式，因为第一项并不包括 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的交叉项，在混合差分时会消去．但是由于成本函数依赖于前面的子问题，这一转移只能够顺序计算，所以无法应用前文描述的第一种分治算法，通常只适合应用二分队列算法或简化 LARSCH 算法．算法复杂度为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 限制区间个数的情形

上述问题可以加强为限制区间个数的情形，即问题指定将区间拆分成 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子区间．此时需要将拆分后的区间个数作为转移状态的一维．相应地，有 2D1D 状态转移方程如下．

𝑓(𝑘,𝑖)=min1≤𝑗≤𝑖𝑓(𝑘−1,𝑗−1)+𝑤(𝑗,𝑖)(1≤𝑘≤𝑚, 1≤𝑖≤𝑛)(2)(2)f(k,i)=min1≤j≤if(k−1,j−1)+w(j,i)(1≤k≤m, 1≤i≤n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，𝑓(0,0) =0f(0,0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑓(0,𝑖) =𝑓(𝑘,0) =∞f(0,i)=f(k,0)=∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对任意 1 ≤𝑘 ≤𝑚1≤k≤m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 1 ≤𝑖 ≤𝑛1≤i≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．和上文同样的道理，这里的 𝑓(𝑘 −1,𝑗 −1) +𝑤(𝑗,𝑖)f(k−1,j−1)+w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然满足四边形不等式．此时对于第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的计算，并不再依赖于该层的结果，所以对于每一层，都可以通过上一节描述的任何算法进行计算，此时算法复杂度为 𝑂(𝑚𝑛log⁡𝑛)O(mnlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于这一问题，利用决策单调性，实际上还存在其他的优化算法．第二种优化思路依赖于如下结果．这种优化算法和下文详细描述的 Knuth 优化算法十分相似．

定理 2

若 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式，则对于问题 (2) 成立 opt⁡(𝑘 −1,𝑖) ≤opt⁡(𝑘,𝑖) ≤opt⁡(𝑘,𝑖 +1)opt⁡(k−1,i)≤opt⁡(k,i)≤opt⁡(k,i+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

第二个不等式只是第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的决策单调性．关键在于第一个不等式．

下证 opt⁡(𝑘,𝑖) ≤opt⁡(𝑘 +1,𝑖)opt⁡(k,i)≤opt⁡(k+1,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．假设有如下两个区间 [1,𝑖][1,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分划（逆序标号）：[𝑎𝑘,𝑑𝑘],⋯,[𝑎1,𝑑1][ak,dk],⋯,[a1,d1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 [𝑏𝑘+1,𝑐𝑘+1],⋯,[𝑏1,𝑐1][bk+1,ck+1],⋯,[b1,c1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中，每个区间的左端点都是其右端点处对应问题的最小最优决策；同样地，从右向左考虑所有可能的分划，右端点也是左端点对应问题的最小最优决策．例如，𝑑𝑗dj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐𝑗cj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是将 [𝑎𝑗,𝑖][aj,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 [𝑏𝑗,𝑖][bj,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分成 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段左起第一个区间右端点的最小最优决策．根据决策单调性，如果 𝑎𝑗−1 >𝑏𝑗−1aj−1>bj−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即 𝑑𝑗 >𝑐𝑗dj>cj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么必然有 𝑎𝑗 >𝑏𝑗aj>bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，如果所证不成立，则有 𝑎1 >𝑏1a1>b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而可以归纳地证明 𝑎𝑘 >𝑏𝑘ak>bk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这显然与所设矛盾．由此得证．

第一个不等式可以另证如下．同样考虑上面证明中的两个分划．如果所证命题不成立，则有 𝑎1 >𝑏1a1>b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是由于有 𝑎𝑘 <𝑏𝑘ak<bk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以找到最小的 𝑗 >1j>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑎𝑗 ≤𝑏𝑗aj≤bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而，此时有 𝑎𝑗−1 >𝑏𝑗−1aj−1>bj−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故 𝑑𝑗 >𝑐𝑗dj>cj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们找到了一组区间满足 𝑎𝑗 ≤𝑏𝑗 ≤𝑐𝑗 <𝑑𝑗aj≤bj≤cj<dj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考虑将这两个分拆重新组合的结果．考虑分拆 [𝑏𝑘+1,𝑐𝑘+1],⋯,[𝑏𝑗+1,𝑐𝑗+1],[𝑏𝑗,𝑑𝑗],[𝑎𝑗−1,𝑑𝑗−1],⋯,[𝑎1,𝑑1][bk+1,ck+1],⋯,[bj+1,cj+1],[bj,dj],[aj−1,dj−1],⋯,[a1,d1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，共 (𝑘 +1)(k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段，于是由前设的最优性可推知，

𝑤(𝑏𝑘+1,𝑐𝑘+1)+⋯+𝑤(𝑏𝑗+1,𝑐𝑗+1)+𝑤(𝑏𝑗,𝑐𝑗)+𝑤(𝑏𝑗−1,𝑐𝑗−1)+⋯+𝑤(𝑏1,𝑐1)≤𝑤(𝑏𝑘+1,𝑐𝑘+1)+⋯+𝑤(𝑏𝑗+1,𝑐𝑗+1)+𝑤(𝑏𝑗,𝑑𝑗)+𝑤(𝑎𝑗−1,𝑑𝑗−1)+⋯+𝑤(𝑎1,𝑑1).w(bk+1,ck+1)+⋯+w(bj+1,cj+1)+w(bj,cj)+w(bj−1,cj−1)+⋯+w(b1,c1)≤w(bk+1,ck+1)+⋯+w(bj+1,cj+1)+w(bj,dj)+w(aj−1,dj−1)+⋯+w(a1,d1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

同样地，考虑分拆 [𝑎𝑘,𝑑𝑘],⋯,[𝑎𝑗+1,𝑑𝑗+1],[𝑎𝑗,𝑐𝑗],[𝑏𝑗−1,𝑐𝑗−1],⋯,[𝑏1,𝑐1][ak,dk],⋯,[aj+1,dj+1],[aj,cj],[bj−1,cj−1],⋯,[b1,c1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，共 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段，则有

𝑤(𝑎𝑘,𝑑𝑘)+⋯+𝑤(𝑎𝑗+1,𝑑𝑗+1)+𝑤(𝑎𝑗,𝑑𝑗)+𝑤(𝑎𝑗−1,𝑑𝑗−1)+⋯+𝑤(𝑎1,𝑑1)<𝑤(𝑎𝑘,𝑑𝑘)+⋯+𝑤(𝑎𝑗+1,𝑑𝑗+1)+𝑤(𝑎𝑗,𝑐𝑗)+𝑤(𝑏𝑗−1,𝑐𝑗−1)+⋯+𝑤(𝑏1,𝑐1).w(ak,dk)+⋯+w(aj+1,dj+1)+w(aj,dj)+w(aj−1,dj−1)+⋯+w(a1,d1)<w(ak,dk)+⋯+w(aj+1,dj+1)+w(aj,cj)+w(bj−1,cj−1)+⋯+w(b1,c1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此时，不等号是严格的，因为 𝑎1 >𝑏1a1>b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是按假设，𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是所有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段分拆最末一段的左端点中最小最优的．两个不等式条件相加，得到 𝑤(𝑏𝑗,𝑐𝑗) +𝑤(𝑎𝑗,𝑑𝑗) <𝑤(𝑏𝑗,𝑑𝑗) +𝑤(𝑎𝑗,𝑐𝑗)w(bj,cj)+w(aj,dj)<w(bj,dj)+w(aj,cj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这有悖于四边形不等式．故而原结论得证．

利用这一结果，我们可以限制决策 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的搜索范围．算法实现时，对 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 正向遍历，对 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 逆向遍历，在之前已确定的上下界范围内暴力搜索 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以保证 𝑂(𝑛(𝑛 +𝑚))O(n(n+m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的算法复杂度．

注意

这里算法复杂度不是 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．正确的复杂度计算需要考虑 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维状态矩阵．因为对于问题 (𝑖,𝑘)(i,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只需要考虑 opt⁡(𝑘 −1,𝑖) ≤𝑗 ≤opt⁡(𝑘,𝑖 +1)opt⁡(k−1,i)≤j≤opt⁡(k,i+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的决策，所以每条次对角线上（即 𝑖 −𝑘i−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一定值）的问题所需遍历的决策总数为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．这样的对角线共计 (𝑛 +𝑚)(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条，故而总的时间复杂度为 𝑂(𝑛(𝑛 +𝑚))O(n(n+m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后一种优化方法来源于如下的观察．

定理 3

若 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式，则问题 (2) 的最优解 𝑔(𝑘) :=𝑓(𝑛,𝑘)g(k):=f(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数．

证明

下证 𝑔(𝑘 −1) +𝑔(𝑘 +1) ≥2𝑔(𝑘)g(k−1)+g(k+1)≥2g(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．为此，考虑长度为 (𝑘 −1)(k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段和 (𝑘 +1)(k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段的最优分划，分别是 [𝑎1,𝑑1],⋯,[𝑎𝑘−1,𝑑𝑘−1][a1,d1],⋯,[ak−1,dk−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 [𝑏1,𝑐1],⋯,[𝑏𝑘+1,𝑐𝑘+1][b1,c1],⋯,[bk+1,ck+1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．取最小的 1 ≤𝑗 ≤𝑘 −11≤j≤k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑐𝑗+1 ≤𝑑𝑗cj+1≤dj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其存在性可由 𝑐𝑘 <𝑛 =𝑑𝑘−1ck<n=dk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 推知．根据其最小性得知，𝑏𝑗+1 >𝑎𝑗bj+1>aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，𝑎𝑗 <𝑏𝑗+1 ≤𝑐𝑗+1 ≤𝑑𝑗aj<bj+1≤cj+1≤dj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．与上文类似，交换两个现有分拆的后半段，可以得到如下两个区间分拆：

[𝑎1,𝑑1],⋯,[𝑎𝑗−1,𝑑𝑗−1],[𝑎𝑗,𝑐𝑗+1],[𝑏𝑗+2,𝑐𝑗+2],⋯,[𝑏𝑘+1,𝑐𝑘+1],[𝑏1,𝑐1],⋯,[𝑏𝑗,𝑐𝑗],[𝑏𝑗+1,𝑑𝑗],[𝑎𝑗+1,𝑑𝑗+1],⋯,[𝑎𝑘−1,𝑑𝑘−1].[a1,d1],⋯,[aj−1,dj−1],[aj,cj+1],[bj+2,cj+2],⋯,[bk+1,ck+1],[b1,c1],⋯,[bj,cj],[bj+1,dj],[aj+1,dj+1],⋯,[ak−1,dk−1].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

两个所得区间都是 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段的，所以由最优性条件可知

2𝑔(𝑘)≤𝑤(𝑎1,𝑑1)+⋯+𝑤(𝑎𝑗−1,𝑑𝑗−1)+𝑤(𝑎𝑗,𝑐𝑗+1)+𝑤(𝑏𝑗+2,𝑐𝑗+2)+⋯+𝑤(𝑏𝑘+1,𝑐𝑘+1)+𝑤(𝑏1,𝑐1)+⋯+𝑤(𝑏𝑗,𝑐𝑗)+𝑤(𝑏𝑗+1,𝑑𝑗)+𝑤(𝑎𝑗+1,𝑑𝑗+1)+⋯+𝑤(𝑎𝑘−1,𝑑𝑘−1)≤𝑤(𝑎1,𝑑1)+⋯+𝑤(𝑎𝑗−1,𝑑𝑗−1)+𝑤(𝑎𝑗,𝑑𝑗)+𝑤(𝑎𝑗+1,𝑑𝑗+1)+⋯+𝑤(𝑎𝑘−1,𝑑𝑘−1)+𝑤(𝑏1,𝑐1)+⋯+𝑤(𝑏𝑗,𝑐𝑗)+𝑤(𝑏𝑗+1,𝑐𝑗+1)+𝑤(𝑏𝑗+2,𝑐𝑗+2)+⋯+𝑤(𝑏𝑘+1,𝑐𝑘+1)=𝑔(𝑘−1)+𝑔(𝑘+1).2g(k)≤w(a1,d1)+⋯+w(aj−1,dj−1)+w(aj,cj+1)+w(bj+2,cj+2)+⋯+w(bk+1,ck+1)+w(b1,c1)+⋯+w(bj,cj)+w(bj+1,dj)+w(aj+1,dj+1)+⋯+w(ak−1,dk−1)≤w(a1,d1)+⋯+w(aj−1,dj−1)+w(aj,dj)+w(aj+1,dj+1)+⋯+w(ak−1,dk−1)+w(b1,c1)+⋯+w(bj,cj)+w(bj+1,cj+1)+w(bj+2,cj+2)+⋯+w(bk+1,ck+1)=g(k−1)+g(k+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里第二个不等式正是四边形不等式．所求凸性由此得证．

这一结论保证了可以通过 WQS 二分（国外称 Aliens Trick）的方法解决此问题．具体来说，考虑带参的成本函数 𝑤𝑐(𝑗,𝑖) :=𝑤(𝑗,𝑖) +𝑐wc(j,i):=w(j,i)+c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，解决不限制区间个数的问题，求得其最优解为 𝑓𝑐(𝑛)fc(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．随着实数 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递增，相应的最优区间的数目单调递减，故而可以通过二分的方法找到恰使得最优区间个数等于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的参数 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则原题最优解为 𝑓(𝑛,𝑚) =𝑓𝑐(𝑛) −𝑐𝑚f(n,m)=fc(n)−cm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这里的实数 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以看作区间个数限制的 Lagrange 乘子．该算法的实现有很多细节，可以参考 [WQS 二分](../wqs-binary-search/) 页面．这一算法的时间复杂度为 𝑂(𝑛log⁡𝑛log⁡𝐶)O(nlog⁡nlog⁡C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这里 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为某一常数．

对于限制区间个数的区间分拆问题的三种算法，在不同的数据范围时表现各有优劣，需要结合具体的题目选择合适的算法．

例题 3：[P4767 [IOI2000] 邮局 加强版](https://www.luogu.com.cn/problem/P4767) [P6246 [IOI2000] 邮局 加强版 加强版](https://www.luogu.com.cn/problem/P6246)

高速公路旁边有一些村庄．高速公路表示为整数轴，每个村庄的位置用单个整数坐标标识．没有两个在同样地方的村庄．两个位置之间的距离是其整数坐标差的绝对值．

邮局将建在一些，但不一定是所有的村庄中．为了建立邮局，应选择他们建造的位置，使每个村庄与其最近的邮局之间的距离总和最小．

你要编写一个程序，已知村庄的位置和邮局的数量，计算每个村庄和最近的邮局之间所有距离的最小可能的总和．

思路

每个村庄有其最近的邮局，那么每个邮局也有其管辖的村庄，易知这是一个区间．

考虑把这 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个村庄分成 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个区间，再在每个区间中决出一个邮局．

根据数学知识，对于区间 [𝑖,𝑗][i,j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，邮局应该建在第 ⌊𝑖+𝑗2⌋⌊i+j2⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个村庄处．使用前缀和容易算出 𝑤(𝑖,𝑗)w(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

问题转化为限制区间个数的区间分拆问题．可以证明，𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 函数满足四边形不等式．直接应用上述优化方法即可．

实现 1，前文第二种优化，复杂度 𝑂(𝑛(𝑛 +𝑚))O(n(n+m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` |  ```text #include <iostream> constexpr int N = 3009 ; constexpr int M = 309 ; using namespace std ; int n , m , a [ N ], s [ N ], g [ M ][ N ], p [ M ][ N ]; int f ( int i , int j ) { int k = ( i \+ j ) >> 1 ; return a [ k ] * ( k \- i \+ 1 ) \- ( s [ k ] \- s [ i \- 1 ]) \+ ( s [ j ] \- s [ k ]) \- a [ k ] * ( j \- k ); } int main () { cin >> n >> m ; for ( int i = 1 ; i <= n ; cin >> a [ i ], s [ i ] = s [ i \- 1 ] \+ a [ i ], ++ i ); for ( int i = 1 ; i <= n ; ++ i ) g [ 0 ][ i ] = 1 << 30 , p [ m \+ 1 ][ i ] = i ; for ( int i = 1 ; i <= m ; ++ i ) p [ i ][ 0 ] = 1 ; for ( int i = 1 ; i <= n ; ++ i ) for ( int j = m ; j ; \-- j ) { g [ j ][ i ] = 1 << 30 ; for ( int k = p [ j ][ i \- 1 ]; k <= p [ j \+ 1 ][ i ]; ++ k ) { int tmp = g [ j \- 1 ][ k \- 1 ] \+ f ( k , i ); if ( tmp < g [ j ][ i ]) g [ j ][ i ] = tmp , p [ j ][ i ] = k ; } } cout << g [ m ][ n ]; } ```   
---|---  
  
实现 2，WQS 二分，复杂度 𝑂(𝑛log⁡𝑛log⁡𝐶)O(nlog⁡nlog⁡C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ``` |  ```text #include <deque> #include <iostream> #define all \ for (auto i : {&q, &l, &r}) (*i) using namespace std ; long long n , m , a [ 500009 ], s [ 500009 ], u , v , w , sum [ 500009 ], cnt [ 500009 ]; deque < int > q , l , r ; long long f ( int i , int j ) { int k = ( i \+ j ) >> 1 ; return sum [ i \- 1 ] \+ v \+ a [ k ] * ( k \- i \+ 1 ) \- ( s [ k ] \- s [ i \- 1 ]) \+ ( s [ j ] \- s [ k ]) \- a [ k ] * ( j \- k ); } void work () { all . clear (); for ( int i = 1 ; i <= n ; ++ i ) { if ( q . size () && r . front () < i ) all . pop_front (); // 队首出队 if ( q . size ()) l . front () = i ; for (; q . size () && f ( q . back (), l . back ()) >= f ( i , l . back ());) // 队尾出队 all . pop_back (); if ( q . empty ()) // 入队 q . emplace_back ( i ), l . emplace_back ( i ), r . emplace_back (( int ) n ); else if ( f ( q . back (), n ) >= f ( i , n )) { int ll = l . back (), rr = n , mid ; for (; ll <= rr ;) { mid = ( ll \+ rr ) >> 1 ; if ( f ( q . back (), mid ) >= f ( i , mid )) rr = mid \- 1 ; else ll = mid \+ 1 ; } r . back () = rr ; q . emplace_back ( i ), l . emplace_back ( ll ), r . emplace_back (( int ) n ); } sum [ i ] = f ( q . front (), i ); cnt [ i ] = cnt [ q . front () \- 1 ] \+ 1 ; } } int main () { cin >> n >> m ; for ( int i = 1 ; i <= n ; cin >> a [ i ], s [ i ] = s [ i \- 1 ] \+ a [ i ], ++ i ); for ( w = 2e12 ; u <= w ;) { // wqs二分 v = ( u \+ w ) >> 1 ; work (); if ( cnt [ n ] < m ) w = v \- 1 ; else u = v \+ 1 ; } v = w ; work (); cout << sum [ n ] \- m * v ; } ```   
---|---  
  
## 区间合并问题

另一类可以通过四边形不等式优化的动态规划问题是区间合并问题，即要将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个长度为一的区间 [𝑖,𝑖][i,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两合并起来，直到得到区间 [1,𝑛][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每次合并 [𝑗,𝑘][j,k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 [𝑘 +1,𝑖][k+1,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时都需要支付成本 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．问题要求找到成本最低的合并方式．对于此类问题，有如下 2D1D 状态转移方程：

𝑓(𝑗,𝑖)=min𝑗≤𝑘<𝑖𝑓(𝑗,𝑘)+𝑓(𝑘+1,𝑖)+𝑤(𝑗,𝑖)(1≤𝑗<𝑖≤𝑛)(3)(3)f(j,i)=minj≤k<if(j,k)+f(k+1,i)+w(j,i)(1≤j<i≤n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，初始成本 𝑓(𝑖,𝑖) =0f(i,i)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．暴力算法的总复杂度为 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而当存在决策单调性时，可以优化至 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的算法复杂度．这一算法最早由 Knuth 在解决最优二叉搜索树问题时提出，并由姚储枫进一步研究总结，在国外称为 Knuth's optimization 或 Knuth-Yao speedup．

除了四边形不等式以外，区间合并问题的决策单调性还要求成本函数满足区间包含单调性．

  * **区间包含单调性** ：如果对于任意 𝑎 ≤𝑏 ≤𝑐 ≤𝑑a≤b≤c≤d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均成立

𝑤(𝑏,𝑐)≤𝑤(𝑎,𝑑),w(b,c)≤w(a,d),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则称函数 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于区间包含关系具有单调性．

这实质是成本函数的一阶条件，即 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递减，关于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递增．

引理 1

若 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足区间包含单调性和四边形不等式，则状态 𝑓(𝑗,𝑖)f(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式．

证明

不妨设 𝑎 ≤𝑏 ≤𝑐 ≤𝑑a≤b≤c≤d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．下证 𝑓(𝑎,𝑑) +𝑓(𝑏,𝑐) ≥𝑓(𝑎,𝑐) +𝑓(𝑏,𝑑)f(a,d)+f(b,c)≥f(a,c)+f(b,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考虑依 𝑑 −𝑎d−a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 归纳．当 𝑎 =𝑏a=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑐 =𝑑c=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，所求即一等式．对于一般的情形，根据 𝑑′ =opt⁡(𝑎,𝑑)d′=opt⁡(a,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置分类讨论．

第一种情况，𝑐 ≤𝑑′c≤d′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑑′ <𝑏d′<b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 [𝑏,𝑐][b,c]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含于 [𝑎,𝑑′][a,d′]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 [𝑑′ +1,𝑑][d′+1,d]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之中．

不妨假设 𝑐 ≤𝑑′c≤d′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，另一种情形同理．此时有

𝑓(𝑎,𝑑)+𝑓(𝑏,𝑐)=𝑓(𝑎,𝑑′)+𝑓(𝑑′+1,𝑑)+𝑤(𝑎,𝑑)+𝑓(𝑏,𝑐)≥𝑓(𝑎,𝑐)+𝑓(𝑏,𝑑′)+𝑓(𝑑′+1,𝑑)+𝑤(𝑎,𝑑)≥𝑓(𝑎,𝑐)+𝑓(𝑏,𝑑′)+𝑓(𝑑′+1,𝑑)+𝑤(𝑏,𝑑)≥𝑓(𝑎,𝑐)+𝑓(𝑏,𝑑).f(a,d)+f(b,c)=f(a,d′)+f(d′+1,d)+w(a,d)+f(b,c)≥f(a,c)+f(b,d′)+f(d′+1,d)+w(a,d)≥f(a,c)+f(b,d′)+f(d′+1,d)+w(b,d)≥f(a,c)+f(b,d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，第一个不等式来自于归纳假设 𝑓(𝑎,𝑐) +𝑓(𝑏,𝑑′) ≤𝑓(𝑎,𝑑′) +𝑓(𝑏,𝑐)f(a,c)+f(b,d′)≤f(a,d′)+f(b,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第二个不等式来自于区间包含单调性 𝑤(𝑏,𝑑) ≤𝑤(𝑎,𝑑)w(b,d)≤w(a,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第三个不等式来自于最优性条件 𝑓(𝑏,𝑑) ≤𝑓(𝑏,𝑑′) +𝑓(𝑑′ +1,𝑑) +𝑤(𝑏,𝑑)f(b,d)≤f(b,d′)+f(d′+1,d)+w(b,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

第二种情况，𝑏 ≤𝑑′ <𝑐b≤d′<c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑑′d′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位于 [𝑏,𝑐][b,c]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之中．此时，考虑 𝑐′ =opt⁡(𝑏,𝑐)c′=opt⁡(b,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置．

不妨假设 𝑐′ ≤𝑑′c′≤d′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 [𝑏,𝑐′][b,c′]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含于 [𝑎,𝑑′][a,d′]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之中，另一种情形同理．此时有

𝑓(𝑎,𝑑)+𝑓(𝑏,𝑐)=𝑓(𝑎,𝑑′)+𝑓(𝑑′+1,𝑑)+𝑤(𝑎,𝑑)+𝑓(𝑏,𝑐′)+𝑓(𝑐′+1,𝑐)+𝑤(𝑏,𝑐)≥𝑓(𝑎,𝑐′)+𝑓(𝑐′+1,𝑐)+𝑤(𝑏,𝑐)+𝑓(𝑏,𝑑′)+𝑓(𝑑′+1,𝑑)+𝑤(𝑎,𝑑)≥𝑓(𝑎,𝑐′)+𝑓(𝑐′+1,𝑐)+𝑤(𝑎,𝑐)+𝑓(𝑏,𝑑′)+𝑓(𝑑′+1,𝑑)+𝑤(𝑏,𝑑)≥𝑓(𝑎,𝑐)+𝑓(𝑏,𝑑).f(a,d)+f(b,c)=f(a,d′)+f(d′+1,d)+w(a,d)+f(b,c′)+f(c′+1,c)+w(b,c)≥f(a,c′)+f(c′+1,c)+w(b,c)+f(b,d′)+f(d′+1,d)+w(a,d)≥f(a,c′)+f(c′+1,c)+w(a,c)+f(b,d′)+f(d′+1,d)+w(b,d)≥f(a,c)+f(b,d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，第一个不等式来自于归纳假设 𝑓(𝑎,𝑐′) +𝑓(𝑏,𝑑′) ≤𝑓(𝑎,𝑑′) +𝑓(𝑏,𝑐′)f(a,c′)+f(b,d′)≤f(a,d′)+f(b,c′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第二个不等式来自于四边形不等式 𝑤(𝑎,𝑐) +𝑤(𝑏,𝑑) ≤𝑤(𝑎,𝑑) +𝑤(𝑏,𝑐)w(a,c)+w(b,d)≤w(a,d)+w(b,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第三个不等式来自于 𝑓(𝑎,𝑐)f(a,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(𝑏,𝑑)f(b,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优性条件．

定理 4

若 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足区间包含单调性和四边形不等式，则问题 (3) 中最小最优决策 opt⁡(𝑗,𝑖)opt⁡(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足

opt⁡(𝑗,𝑖−1)≤opt⁡(𝑗,𝑖)≤opt⁡(𝑗+1,𝑖).(𝑗+1<𝑖)opt⁡(j,i−1)≤opt⁡(j,i)≤opt⁡(j+1,i).(j+1<i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

引理 1 已经证得 𝑓(𝑗,𝑖)f(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式，所以目标函数 𝑓(𝑗,𝑘) +𝑓(𝑘 +1,𝑖) +𝑤(𝑗,𝑖)f(j,k)+f(k+1,i)+w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于给定 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为 (𝑘,𝑖)(k,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的函数满足四边形不等式，所以由定理 1 有，opt⁡(𝑗,𝑖 −1) ≤opt⁡(𝑗,𝑖)opt⁡(j,i−1)≤opt⁡(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意，不同时含有 (𝑘,𝑖)(k,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的项并不影响四边形不等式成立．类似地，它对于给定 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为 (𝑘,𝑗)(k,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的函数也满足四边形不等式，所以 opt⁡(𝑗,𝑖) ≤opt⁡(𝑗 +1,𝑖)opt⁡(j,i)≤opt⁡(j+1,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．即得所证．

利用这一结论，同样可以限制决策点 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的搜索范围．在这里，正序遍历区间长度 𝑖 −𝑗 +1i−j+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再遍历具有同样长度的所有区间 [𝑗,𝑖][j,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，暴力搜索 opt⁡(𝑗,𝑖 −1)opt⁡(j,i−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 opt⁡(𝑗 +1,𝑖)opt⁡(j+1,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的所有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求得最优解 𝑓(𝑗,𝑖)f(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并记录最小最优决策 opt⁡(𝑗,𝑖)opt⁡(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于同样长度的所有区间，此算法中决策空间总长度是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，而可能的区间长度的数目同样是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，故而总的算法复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` |  ```text val_t w ( int j , int i ); // 成本函数 val_t f [ N ][ N ]; // 最优值 int opt [ N ][ N ]; // 最小最优决策 // 求解整个区间 [1,n] 对应的问题 void solve ( int n ) { // 初始化 for ( int i = 1 ; i <= n ; ++ i ) { f [ i ][ i ] = 0 ; opt [ i ][ i ] = i ; } // 枚举区间长度 for ( int len = 2 ; len <= n ; ++ len ) { // 枚举长度为 len 的所有区间 for ( int j = 1 , i = len ; i <= n ; ++ j , ++ i ) { f [ j ][ i ] = inf ; for ( int k = opt [ j ][ i \- 1 ]; k <= opt [ j \+ 1 ][ i ]; ++ k ) if ( f [ j ][ i ] > f [ j ][ k ] \+ f [ k \+ 1 ][ i ] \+ w ( j , i )) { f [ j ][ i ] = f [ j ][ k ] \+ f [ k \+ 1 ][ i ] \+ w ( j , i ); // 更新状态值 opt [ j ][ i ] = k ; // 更新（最小）最优决策点 } } } } ```   
---|---  
  
## 满足四边形不等式的函数类

为了更方便地证明一个函数满足四边形不等式，我们有以下几条性质：

**性质 1** ：若函数 𝑤1(𝑗,𝑖)w1(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑤2(𝑗,𝑖)w2(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均满足四边形不等式（或区间包含单调性），则对于任意 𝑐1,𝑐2 ≥0c1,c2≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，函数 𝑐1𝑤1 +𝑐2𝑤2c1w1+c2w2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也满足四边形不等式（或区间包含单调性）．

**性质 2** ：若存在函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑤(𝑗,𝑖) =𝑓(𝑗) −𝑔(𝑖)w(j,i)=f(j)−g(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则函数 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形恒等式．当函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单调增加时，函数 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还满足区间包含单调性．

**性质 3** ：设 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个单调增加的凸函数，若函数 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式并且对区间包含关系具有单调性，则复合函数 ℎ(𝑤(𝑗,𝑖))h(w(j,i))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也满足四边形不等式和区间包含单调性．

**性质 4** ：设 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个凸函数，若函数 𝑤(𝑗,𝑖)w(j,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形恒等式并且对区间包含关系具有单调性，则复合函数 ℎ(𝑤(𝑗,𝑖))h(w(j,i))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也满足四边形不等式．

首先需要澄清一点，凸函数（Convex Function）的定义在国内教材中有分歧，此处的凸函数指的是下凸函数，即（可微时）一阶导数单调增加的函数．

证明

前两条性质根据定义很容易证明，下面证明第三条性质，性质四的证明过程类似．由于 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单调，ℎ(𝑤(𝑗,𝑖))h(w(j,i))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 自然保持对区间包含的单调性．关键在于四边形不等式的证明．

为此，下面考虑 𝑎 ≤𝑗 ≤𝑏 ≤𝑐 ≤𝑖 ≤𝑑a≤j≤b≤c≤i≤d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的二阶混合差分．

Δ𝑖Δ𝑗ℎ(𝑤(𝑗,𝑖))=ℎ(𝑤(𝑏,𝑑))−ℎ(𝑤(𝑎,𝑐)+Δ𝑗𝑤(𝑗,𝑐)+Δ𝑖𝑤(𝑎,𝑖))+ℎ(𝑤(𝑎,𝑐)+Δ𝑗𝑤(𝑗,𝑐)+Δ𝑖𝑤(𝑎,𝑖))−ℎ(𝑤(𝑎,𝑐)+Δ𝑗𝑤(𝑗,𝑐))−ℎ(𝑤(𝑎,𝑐)+Δ𝑖𝑤(𝑎,𝑖))+ℎ(𝑤(𝑎,𝑐)).ΔiΔjh(w(j,i))=h(w(b,d))−h(w(a,c)+Δjw(j,c)+Δiw(a,i))+h(w(a,c)+Δjw(j,c)+Δiw(a,i))−h(w(a,c)+Δjw(j,c))−h(w(a,c)+Δiw(a,i))+h(w(a,c)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，根据区间单调性，Δ𝑖𝑤(𝑎,𝑖) :=𝑤(𝑎,𝑑) −𝑤(𝑎,𝑐) ≥0Δiw(a,i):=w(a,d)−w(a,c)≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 Δ𝑗𝑤(𝑗,𝑐) :=𝑤(𝑏,𝑐) −𝑤(𝑎,𝑐) ≤0Δjw(j,c):=w(b,c)−w(a,c)≤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 具有凸性，对于 𝑡1,𝑡2 ≥0t1,t2≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立 ℎ(𝑥 +𝑡1 −𝑡2) −ℎ(𝑥 +𝑡1) ≤ℎ(𝑥 −𝑡2) −ℎ(𝑥)h(x+t1−t2)−h(x+t1)≤h(x−t2)−h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以后两行必然非正．同时，由于四边形不等式，𝑤(𝑏,𝑑) ≤𝑤(𝑎,𝑐) +Δ𝑗𝑤(𝑗,𝑐) +Δ𝑖𝑤(𝑎,𝑖) =𝑤(𝑏,𝑐) +𝑤(𝑎,𝑑) −𝑤(𝑎,𝑐)w(b,d)≤w(a,c)+Δjw(j,c)+Δiw(a,i)=w(b,c)+w(a,d)−w(a,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而，第一行的差在 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单调增加的情况下必然也非正．所以，总的二阶混合差分非正．此即四边形不等式．

这一证明实际是如下导数证明的离散版本．

𝜕2𝜕𝑥𝜕𝑦ℎ(𝑤(𝑥,𝑦))=ℎ″(𝑤(𝑥,𝑦))𝜕𝜕𝑥𝑤(𝑥,𝑦)𝜕𝜕𝑦𝑤(𝑥,𝑦)+ℎ′(𝑤(𝑥,𝑦))𝜕2𝜕𝑥𝜕𝑦𝑤(𝑥,𝑦)≤0.∂2∂x∂yh(w(x,y))=h″(w(x,y))∂∂xw(x,y)∂∂yw(x,y)+h′(w(x,y))∂2∂x∂yw(x,y)≤0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这在 ℎ′ ≥0h′≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，ℎ″ ≥0h″≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑤𝑥 ≤0wx≤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑤𝑦 ≥0wy≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以及 𝑤𝑥𝑦 ≤0wxy≤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的条件下显然成立．其中，区间包含单调性给出了 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一阶条件，而四边形不等式给出了其二阶条件．

## 习题

  * [Codeforces - Ciel and Gondolas](https://codeforces.com/contest/321/problem/E)(Be careful with I/O!)
  * [SPOJ - LARMY](https://www.spoj.com/problems/LARMY/)
  * [Codechef - CHEFAOR](https://www.codechef.com/problems/CHEFAOR)
  * [Hackerrank - Guardians of the Lunatics](https://www.hackerrank.com/contests/ioi-2014-practice-contest-2/challenges/guardians-lunatics-ioi14)
  * [ACM ICPC World Finals 2017 - Money](https://open.kattis.com/problems/money)

## 参考资料与注释

  * [Quora Answer by Michael Levin](https://www.quora.com/What-is-divide-and-conquer-optimization-in-dynamic-programming)
  * [Video Tutorial by "Sothe" the Algorithm Wolf](https://www.youtube.com/watch?v=wLXEWuDWnzI)
  * [Divide and Conquer DP](https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html)
  * [Knuth's Optimization](https://cp-algorithms.com/dynamic_programming/knuth-optimization.html)
  * [Quadrangle Inequality Properties](https://codeforces.com/blog/entry/86306)
  * [王钦石《浅析一类二分方法》](https://github.com/hzwer/shareOI/blob/master/%E5%9F%BA%E7%A1%80%E7%AE%97%E6%B3%95/%E6%B5%85%E6%9E%90%E4%B8%80%E7%B1%BB%E4%BA%8C%E5%88%86%E6%96%B9%E6%B3%95_%E7%8E%8B%E9%92%A6%E7%9F%B3.pdf)
  * [簡易版 LARSCH Algorithm by noshi91](https://noshi91.hatenablog.com/entry/2023/02/18/005856)
  * [四边形不等式和决策单调性 by b6e0_ - 洛谷专栏](https://www.luogu.com.cn/article/h81hh5lk)
  * [在线决策单调性的丐版 LARSCH 算法 by Register_int - 洛谷专栏](https://www.luogu.com.cn/article/vqf42hah)

* * *

  1. 算法描述中提到的「更劣」和「更优」都应看做是在描述先比较函数值大小再比较决策点大小的字典序．在这一字典序下，「更优」意味着要么函数值更小，要么函数值一样但是决策点更小． ↩

  2. Larmore, Lawrence L., and Baruch Schieber. "On-line dynamic programming with applications to the prediction of RNA secondary structure." Journal of Algorithms 12, no. 3 (1991): 490-515. ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/opt/quadrangle.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/opt/quadrangle.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest), [izlyforever](https://github.com/izlyforever), [Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [Enter-tainer](https://github.com/Enter-tainer), [Marcythm](https://github.com/Marcythm), [ouuan](https://github.com/ouuan), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [Henry-ZHR](https://github.com/Henry-ZHR), [ksyx](https://github.com/ksyx), [NFLSCode](https://github.com/NFLSCode), [ranwen](https://github.com/ranwen), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [billchenchina](https://github.com/billchenchina), [CCXXXI](https://github.com/CCXXXI), [chang-wenxuan](https://github.com/chang-wenxuan), [Chrogeek](https://github.com/Chrogeek), [Elitedj](https://github.com/Elitedj), [fps5283](https://github.com/fps5283), [greyqz](https://github.com/greyqz), [HeRaNO](https://github.com/HeRaNO), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [Menci](https://github.com/Menci), [MingqiHuang](https://github.com/MingqiHuang), [NachtgeistW](https://github.com/NachtgeistW), [nanmenyangde](https://github.com/nanmenyangde), [opsiff](https://github.com/opsiff), [shawlleyw](https://github.com/shawlleyw), [TOMWT-qwq](https://github.com/TOMWT-qwq), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [zryi2003](https://github.com/zryi2003), [zyf0726](https://github.com/zyf0726)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
