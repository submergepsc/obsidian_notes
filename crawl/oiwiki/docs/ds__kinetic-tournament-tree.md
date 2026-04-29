# Kinetic Tournament Tree - OI Wiki

- Source: https://oi-wiki.org/ds/kinetic-tournament-tree/

# Kinetic Tournament Tree

前置知识：[线段树](../seg/)

## 问题引入

给定单变量线性函数序列 𝐹 ={𝑓1,…,𝑓𝑛}F={f1,…,fn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：𝑓𝑖 :𝐑 →𝐑fi:R→R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中 𝑓𝑖(𝑥) =𝑘𝑖𝑥 +𝑏𝑖fi(x)=kix+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑘𝑖,𝑏𝑖 ∈𝐑ki,bi∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们需要维护以下操作：

  * QueryMax⁡(𝑙,𝑟)QueryMax⁡(l,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：给定 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 返回 max𝑟𝑖=𝑙𝑓𝑖(0)maxi=lrfi(0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * TranslateLeft⁡(𝑙,𝑟,𝛿)TranslateLeft⁡(l,r,δ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：给定 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 对于所有 𝑖 ∈[𝑙,𝑟]i∈[l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，执行操作 𝑓𝑖(𝑥) ←𝑓𝑖(𝑥 +𝛿)fi(x)←fi(x+δ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这个操作等价于执行 𝑏𝑖 ←𝑏𝑖 +𝑘𝑖𝛿bi←bi+kiδ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中 𝛿 >0δ>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

为了方便，我们假定所有函数互不相同．

一次函数区间向左平移的本质是 𝑏𝑖 ←𝑘𝑖 ⋅𝛿bi←ki⋅δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是对于 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 常数项，让它加上斜率 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘上横坐标的平移量 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；这种操作等价于我们在许多数据结构问题中遇到的「按位置系数加权区间加」：即对于区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的每个下标 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，给其值加上一个固定的数 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘上该位置特有的系数 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此本质上一次函数区间平移就是所谓的，按位置系数加权区间加法．

为了展示 KTT 独特的二叉树形分治结构，我们将直接从区间平移入手．

## Kinetic Data Structures

Kinetic Data Structures 简称 KDS．KDS 用于维护几何对象系统在连续运动过程中的属性．

### 事件队列

我们假设每一个点都有一个已知的运动计划，这个计划可以提供它的完整或者部分运动信息，例如函数 𝑓𝑖(𝑥)fi(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 形成的曲线或直线能够很好的描述动点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的运动轨迹．运动计划随时可能变化，它可能是由于碰撞，或者环境交互的原因；我们称造成运动计划更改的原因为事件．事件队列会按时间顺序给出事件．

KDS 的一个关键方面是需要拥有容易维护的事件，即事件队列中事件类型对应于可能的组合变化，这些变化涉及数量恒定且通常较少的物体．例如，在本题的维护中，我们使用的一种事件类型是「函数 𝑓𝑖(0)fi(0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与函数 𝑓𝑗(0)fj(0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小发生变化」．

事件队列可以隐式维护．

### 证书

这些事件应当可以等价于通过一系列低阶代数条件的交保证，每个代数条件都涉及有限数量的对象．我们将这些条件称为 KDS 的证书．例如 [𝑓𝑖(0) >𝑓𝑗(0)][fi(0)>fj(0)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

## Kinetic Tournament Tree

### 简介

Kinetic Tournament Tree（简称 KTT），属于 Kinetic Data Structures，首次出现于 1999 年的 [Data Structures for Mobile Data](https://www.sciencedirect.com/science/article/pii/S0196677498909889)，用于维护连续变化的数据．更普遍地，每一个采用如下动态化策略（kinetization strategy）的结构，都可以称为 Kinetic Tournament：

  * 为静态算法中的关键操作（例如比较）生成正确性证书，并将每个证书与一个全局事件队列关联，记录该证书可能失效的时间点．
  * 当某个证书失效时，我们能够高效地更新算法输出并维护证书集合．

在算法竞赛社区，它兴起于 2020 年国家集训队论文《[浅谈函数最值的动态维护](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/IOI2020%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%80%99%E9%80%89%E9%98%9F%E8%AE%BA%E6%96%87%E9%9B%86%20%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%89%88.pdf)》．学术界的 KTT 与算法竞赛界的 KTT 在应用领域和实现上有所不同，因此我们将介绍为算法竞赛界进行一些优化过后的 KTT．

### 基本结构

首先我们考虑设计一个线段树结构相似的数据结构用于维护静态最大值．我们将线段树的结构建立出来，对于每个非叶节点，它的权值为两个孩子节点中较大的权值．在执行了 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次比较过后，我们得到根节点的权值就是全局的最大值．现在，权值开始变化．只要 KTT 能探测到每一次树上点的最大值来源改变，我们就能够维护全局最大值．

为了让 KTT 能够探测到每一次树上最大值来源变换，对于树上节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以及其左、右儿子提供的函数 𝑓𝐿fL![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓𝑅fR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们定义证书为「𝑓𝐿fL![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓𝑅fR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小关系保持不变」．当证书失效的时候，我们就需要通过树上路径走到当前证书失效的节点来更新它的信息．为了维护每个证书失效的时间，我们发现证书失效的时刻正是两个函数拥有相同值的时刻，那么问题就变成了找到两个线性函数的交点的横坐标，可以在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内解决．

对于每个树上的节点维护出了它在 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处取到最大值的函数，以及当前证书失效的时间和整个子树内最早失效证书的失效时间；那么对于每个节点证书失效的时刻，我们就可以在这个时刻找到它并更新它的信息．这些信息是用来记录函数本身的信息的．接下来我们考虑维护区间平移操作，因为它是可以简单累加的，我们就可以使用懒标记去处理区间平移操作．

我们定义懒标记 Δ𝑣Δv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 节点子树内的所有其他节点上的函数都应该向左平移 Δ𝑣Δv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个单位．此时，对于树上节点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一个新的操作要将其子树内的所有函数区间向左平移 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 即 𝑓(𝑥) ←𝑓(𝑥 +𝛿)f(x)←f(x+δ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们需要更新懒标记：Δ𝑣 ←Δ𝑣 +𝛿Δv←Δv+δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即将子树内所有其他节点的偏移量进行累加．同时向左平移也意味着 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点函数值的变化．我们可以发现如果证书的失效横坐标为 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么平移后的失效横坐标应为 𝑡 −𝛿t−δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；此时，如果 𝑡 −𝛿t−δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 越过 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点，就代表着证书失效，我们就需要往下递归找到当前证书所在节点，更新当前节点，并将新的信息向上更新到根．这个过程可以跟随着修改一起做．

因此我们便可以得到简单实现．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 ``` |  ```text struct node { int l , r ; int tag ; // the lazy propagation tag int k , b ; // the linear function int swc ; // the time of certificate violation }; vector < node > v ; int IntegerPart ( double x ) { if ( x >= 0 && x <= inf ) return int ( ceil ( x )); return inf ; } void push_up ( int rt ) { int mx = v [ rt << 1 ]. b > v [ rt << 1 | 1 ]. b ? rt << 1 : rt << 1 | 1 , mi = mx ^ 1 ; v [ rt ]. k = v [ mx ]. k , v [ rt ]. b = v [ mx ]. b ; v [ rt ]. swc = v [ mx ]. k < v [ mi ]. k ? IntegerPart ( 1.0 * ( v [ mx ]. b \- v [ mi ]. b ) / ( v [ mi ]. k \- v [ mx ]. k )) : inf ; } void push_tag ( int rt , int val ) { v [ rt ]. tag += val , v [ rt ]. swc -= val , v [ rt ]. b += v [ rt ]. k * val ; } void push_down ( int rt ) { if ( v [ rt ]. tag ) push_tag ( rt << 1 , v [ rt ]. tag ), push_tag ( rt << 1 | 1 , v [ rt ]. tag ), v [ rt ]. tag = 0 ; } void checkswitch ( int rt ) { if ( v [ rt ]. l == v [ rt ]. r ) return ; push_down ( rt ); if ( v [ rt ]. swc <= 0 ) checkswitch ( rt << 1 ), checkswitch ( rt << 1 | 1 ); push_up ( rt ); } void build ( int rt , int l , int r ) { v [ rt ]. l = l , v [ rt ]. r = r ; if ( l == r ) return v [ rt ]. k = k [ l ], v [ rt ]. b = b [ l ], void (); int mid = ( l \+ r ) >> 1 ; build ( rt << 1 , l , mid ); build ( rt << 1 | 1 , mid \+ 1 , r ); push_up ( rt ); } void TranslateLeft ( int rt , int l , int r , int val ) { if ( l <= v [ rt ]. l && v [ rt ]. r <= r ) return push_tag ( rt , val ), checkswitch ( rt ); int mid = v [ rt << 1 ]. r ; push_down ( rt ); if ( l <= mid ) TranslateLeft ( rt << 1 , l , r , val ); if ( mid < r ) TranslateLeft ( rt << 1 | 1 , l , r , val ); push_up ( rt ); } int QueryMax ( int rt , int l , int r ) { if ( l <= v [ rt ]. l && v [ rt ]. r <= r ) return v [ rt ]. b ; int mid = v [ rt << 1 ]. r , res = 0 ; push_down ( rt ); if ( l <= mid ) res = max ( res , QueryMax ( rt << 1 , l , r )); if ( mid < r ) res = max ( res , QueryMax ( rt << 1 | 1 , l , r )); return res ; } ```   
---|---  
  
### 复杂度分析

证明 KTT 的时间复杂度需要用到势能分析．

设 𝑑(𝑥)d(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在线段树上的深度，根节点的深度为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．定义节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在线段树上的势能为：

𝛼(𝑥)={𝑑(𝑥)if the lower slope function has larger value0otherwiseα(x)={d(x)if the lower slope function has larger value0otherwise![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即在 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比较的两个函数，如果拥有较小斜率的函数的值在 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点更大，那么当前节点势能为 𝑑(𝑥)d(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

定义整个 KTT 的势能为所有节点势能之和：

Φ=∑𝑥𝛼(𝑥)Φ=∑xα(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑某次对于节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，和它的父亲 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的实际更新代价 𝑐 =1c=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，更新前后的势能分别为 ΦΦ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 Φ′Φ′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们去计算更新节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的均摊更新代价．由于当前节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被更新，那么在当下它的势能一定是由 𝑑(𝑥)d(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下降到 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而对于 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的势能最坏情况可能由 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上升到 𝑑(𝑝)d(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

ˆ𝑐=1+Φ′−Φ=1+(𝛼′(𝑝)+𝛼′(𝑥))−(𝛼(𝑝)+𝛼(𝑥))=1+(𝛼′(𝑝)−𝛼(𝑝))+(𝛼′(𝑥)−𝛼(𝑥))≤1+𝑑(𝑝)−𝑑(𝑥)=0c^=1+Φ′−Φ=1+(α′(p)+α′(x))−(α(p)+α(x))=1+(α′(p)−α(p))+(α′(x)−α(x))≤1+d(p)−d(x)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对实际代价求和，定义初始势能 Φ𝑠Φs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以及最终势能 Φ𝑡Φt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

∑𝑐=∑ˆ𝑐+Φ𝑠−Φ𝑡≤Φ𝑠−Φ𝑡=𝑂(𝑛log⁡𝑛)∑c=∑c^+Φs−Φt≤Φs−Φt=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这部分为 KTT 在仅存在全局修改的情况下，它将所有证书失效更新完毕的次数．

额外的，考虑区间平移对势能的影响．对于某次区间平移，我们需要考虑的节点应当为，其子树当中存在但不是所有树节点被执行区间平移操作的节点．这样的节点也就是我们在执行修改操作的时候在树上经过的节点，它的数量不超过 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，最坏情况下每个节点的势能上涨 𝑑(𝑥) ≤log⁡𝑛d(x)≤log⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此每次操作上涨 𝑂(log2⁡𝑛)O(log2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的势能．

为了维护区间平移，更新证书的操作将会被执行 𝑂(𝑛log⁡𝑛 +𝑚log2⁡𝑛)O(nlog⁡n+mlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．每次更新证书我们需要从树上沿着路径走到证书失效的节点，这部分是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．因此总时间复杂度为 𝑂(𝑛log2⁡𝑛 +𝑚log3⁡𝑛)O(nlog2⁡n+mlog3⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这个方法的优秀之处在于他已经触及问题时间复杂度的下界 𝑂(𝜆𝑠(𝑛)log2⁡𝑛)O(λs(n)log2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝜆𝑠(𝑛)λs(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示长度最长的 (n, s) Davenport-Schinzel 序列．其中线性函数对应 𝑠 =1s=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝜆1(𝑛) =𝑛λ1(n)=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这部分属于计算几何内容，本篇不在这里赘述．

### 高次情况

如果我们维护的不是线性函数而是多项式函数，或者更加复杂的函数我们如何应对．两个复杂函数之间可能拥有多个交点．给定一个连续、完全定义的单变量函数序列 𝐹 ={𝑓1,…,𝑓𝑛}F={f1,…,fn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：𝑓𝑖 :𝐑 →𝐑fi:R→R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中每对函数的图像至多相交于 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点．具有代表性的，𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次多项式函数集合符合这个要求．

对于同样的问题，我们使用势能分析．

𝑑(𝑥)d(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在线段树上的深度，根节点的深度为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．定义 𝐼(𝑥)I(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示在节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比较的两个函数，在 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点过后有几个交点．定义节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在线段树上的势能为：

𝛼(𝑥)=𝑑(𝑥)log2⁡(𝑠+1)𝐼(𝑥)α(x)=d(x)log2⁡(s+1)I(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定义整个 KTT 的势能为所有节点势能之和：

Φ=∑𝑥𝛼(𝑥)Φ=∑xα(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑某次对于节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，和它的父亲 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的实际更新代价 𝑐 =1c=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，更新前后的势能分别为 ΦΦ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 Φ′Φ′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们去计算更新节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的均摊更新代价．由于当前节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被更新，那么在当下它的势能一定是由 𝑑(𝑥)log2⁡(𝑠+1)𝐼(𝑥)d(x)log2⁡(s+1)I(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下降到 𝑑(𝑥)log2⁡(𝑠+1)(𝐼(𝑥) −1)d(x)log2⁡(s+1)(I(x)−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而对于 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的势能最坏情况可能由 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上升到 𝑑(𝑝)log2⁡(𝑠+1)d(p)log2⁡(s+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

ˆ𝑐=1+Φ′−Φ=1+(𝛼′(𝑥)−𝛼(𝑥))+(𝛼′(𝑝)−𝛼(𝑝))≤1−𝑑(𝑥)log2⁡(𝑠+1)+𝑠(𝑑(𝑥)−1)log2⁡(𝑠+1)≤0c^=1+Φ′−Φ=1+(α′(x)−α(x))+(α′(p)−α(p))≤1−d(x)log2⁡(s+1)+s(d(x)−1)log2⁡(s+1)≤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由第三行到第四行我们使用了 𝑑(𝑥)d(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为正整数的限制．

对实际代价求和，定义初始势能 Φ𝑠Φs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以及最终势能 Φ𝑡Φt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

∑𝑐=∑ˆ𝑐−Φ𝑡+Φ𝑠≤Φ𝑠−Φ𝑡=𝑂(𝑛𝑠(log⁡𝑛)log2⁡(𝑠+1))∑c=∑c^−Φt+Φs≤Φs−Φt=O(ns(log⁡n)log2⁡(s+1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们得到复杂度的上界 𝑂(𝑛𝑠(log⁡𝑛)1+log2⁡(𝑠+1) +𝑚𝑠(log⁡𝑛)2+log2⁡(𝑠+1))O(ns(log⁡n)1+log2⁡(s+1)+ms(log⁡n)2+log2⁡(s+1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．1

### 近似情况

给定一个连续、完全定义的单变量函数序列 𝐹 ={𝑓1,…,𝑓𝑛}F={f1,…,fn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义 𝔘𝐹(𝑥)UF(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝔏𝐹(𝑥)LF(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝔈𝐹(𝑥)EF(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为上包络、下包络和幅度．

𝔘𝐹(𝑥)=max{𝑓𝑖(𝑥)∣𝑓𝑖∈𝐹}𝔏𝐹(𝑥)=min{𝑓𝑖(𝑥)∣𝑓𝑖∈𝐹}𝔈𝐹(𝑥)=𝔘𝐹(𝑥)−𝔏𝐹(𝑥)UF(x)=max{fi(x)∣fi∈F}LF(x)=min{fi(x)∣fi∈F}EF(x)=UF(x)−LF(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们只要求程序返回 ˜𝔘𝐹(𝑥)U~F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足

𝔘𝐹(𝑥)≥˜𝔘𝐹(𝑥)≥𝔘𝐹(𝑥)−𝜖𝔈𝐹(𝑥)UF(x)≥U~F(x)≥UF(x)−ϵEF(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么在复杂情况下我们可以做到 𝑂((1/𝜖2)𝑛log3⁡𝑛)O((1/ϵ2)nlog3⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，与多项式次数无关，以及我们允许函数同时进行区间左移或者右移．

## 参考文献与注释

  * P. K. Agarwal, S. Har-Peled, and K. R. Varadarajan. Approximating extent measures of points. J. ACM, 51(4):606–635, July 2004.
  * J. Basch, L. J. Guibas, and J. Hershberger. Data structures for mobile data. Journal of Algorithms, 31(1):1–28, 1999.
  * G. Alexandron, H. Kaplan, and M. Sharir. Kinetic and dynamic data structures for convex hulls and upper envelopes. Computational Geometry, 36(2):144–158, 2007.

* * *

  1. 需要注意的是，这仅仅给出的是上界，复杂度的下界应为 𝑂(𝜆𝑠(𝑛)log⁡𝑛)O(λs(n)log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．笔者猜测这里的势能分析构造应当参考 Davenport-Schinzel 序列对应的 𝜆𝑠(𝑛)λs(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的通项公式以获取更紧的上界． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/kinetic-tournament-tree.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/kinetic-tournament-tree.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Jerry3128](https://github.com/Jerry3128), [jerry3128](https://github.com/jerry3128), [shuzhouliu](https://github.com/shuzhouliu)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
