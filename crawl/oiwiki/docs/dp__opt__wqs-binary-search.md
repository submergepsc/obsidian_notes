# WQS 二分 - OI Wiki

- Source: https://oi-wiki.org/dp/opt/wqs-binary-search/

# WQS 二分

## 引入

本文介绍利用 WQS 二分优化动态规划问题的方法．在不同的文章中，它也常称作带权二分、凸优化 DP、凸完全单调性 DP、Lagrange 乘子法等，在国外也称作 Aliens Trick．它最早由王钦石在《浅析一类二分方法》一文中总结．

WQS 二分通常用于解决这样一类优化问题：它们带有数量限制，直接求解代价较高；但一旦去除这一限制，问题本身就变得容易得多．

比如，假设要解决的问题是，要从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品中选取 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，并最优化某个较复杂的目标函数．如果设从前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品中选取 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，目标函数的最优值为 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么原问题的答案就是 𝑓(𝑛,𝑚)f(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这类问题中，状态转移方程通常是二维的．直接实现该状态转移方程，时间复杂度是 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，难以接受．

进一步假设，没有数量限制的最优化问题容易解决．但是，选取到的最优数量未必满足原问题的数量限制．假设选取的物品过多．那么，就可以考虑在选取物品时，为每个选取到的物品都附加一个固定大小的惩罚 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即「带权二分」中的「权」），仍然解没有数量限制的最优化问题．根据 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值不同，选取到的最优数量也会有所不同；而且，随着 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的变化，选取到的最优数量也是单调变化的．所以，可以通过二分，找到 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得选取到的最优数量恰为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．假设此时目标函数的最优值为 𝑓𝑘(𝑛)fk(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，只要消除额外附加的惩罚造成的价值损失，就能得到原问题的答案 𝑓(𝑛,𝑚) =𝑓𝑘(𝑛) +𝑘𝑚f(n,m)=fk(n)+km![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．假设单次求解附加惩罚的问题的复杂度是 𝑂(𝑇(𝑛))O(T(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，那么，算法的整体复杂度也就降低到了 𝑂(𝑇(𝑛)log⁡𝐿)O(T(n)log⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑂(log⁡𝐿)O(log⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是二分 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要的次数．

这就是 WQS 二分的基本想法．但是，这一想法能够行得通，前提是 𝑓(𝑛,𝑚)f(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是凸的．否则，可能不存在使得最优数量恰为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的附加惩罚 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这也是这种 DP 优化方法常常称为「凸优化 DP」或「凸完全单调性 DP」的原因．

## 传统方法

设非空集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为（有限的）决策空间，𝑓 :𝑋 →𝐑f:X→R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为目标函数，且另有函数 𝑔 :𝑋 →𝐑𝑑g:X→Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用于施加限制．需要求解的问题，可以看作是计算如下最优化问题的价值函数 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在某处的取值：

𝑣(𝑦)=min𝑥∈𝑋𝑓(𝑥)subject to 𝑔(𝑥)=𝑦.v(y)=minx∈Xf(x)subject to g(x)=y.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

比如，对于前文提到的限制数量的问题，𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以理解为所有物品集合的子集族，𝑥 ∈𝑋x∈X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是单个子集，𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是单个子集的价值函数，𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是子集 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素个数．当然，𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并非只能是数量限制，后文提供了更为广泛的限制条件的例子．

约定

为了行文方便，本文仅讨论最小化目标函数的问题．最大化目标函数的问题与之相仿，只是需要将本文中的（下）凸函数相应地替换成凹函数（或称上凸函数）．或者，可以通过添加负号，将最大化目标函数的问题，转化为最小化它的相反数的问题．

### 几何直观

因为算法竞赛中遇到的大多数问题都是组合优化问题，决策空间 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通常没有良好的结构，所以，可以转而考察集合

D={(𝑔(𝑥),𝑓(𝑥))∈𝐑×𝐑𝑑:𝑥∈𝑋}.D={(g(x),f(x))∈R×Rd:x∈X}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

传统方法能够解决的主要是 𝑑 =1d=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，即只有一个限制的情形．下图提供了此时点集 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一种可能的图示．

![](./images/wqs-f-g-space.svg)

图中的红点和蓝点是 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有可能的选择投影在平面 (𝑔(𝑥),𝑓(𝑥))(g(x),f(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上得到的集合 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．于是，原问题所要求的就是横坐标为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的那些点中，纵坐标的最小值 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．当 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变动时，所有这样的点 (𝑦,𝑣(𝑦))(y,v(y))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就构成了图中的红点的集合．

为了求得点 (𝑦,𝑣(𝑦))(y,v(y))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的纵坐标，可以考虑用斜率为 𝜆 ∈𝐑λ∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的直线去切集合 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如图所示，当直线的斜率选取得恰当时，经过点 (𝑦,𝑣(𝑦))(y,v(y))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的那条直线，是所有经过集合 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的点且斜率为 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的直线中，截距 𝑓(𝑥) −𝜆𝑔(𝑥)f(x)−λg(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小的．将这一最小值记为

ℎ(𝜆)=min𝑥∈𝑋𝑓(𝑥)−𝜆𝑔(𝑥).h(λ)=minx∈Xf(x)−λg(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么，因为 (𝑦,𝑣(𝑦))(y,v(y))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同样位于该直线上，就可以得到原问题的解

𝑣(𝑦)=ℎ(𝜆)+𝜆𝑦.v(y)=h(λ)+λy.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

假设对于所有合理范围的 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，上述函数 ℎ(𝜆)h(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是容易求解的．这在算法竞赛中常常是成立的，因为它去掉了原问题中的限制条件．那么，现在面临的最为重要的两个问题，就是

  1. 是否存在这样的直线斜率 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得它的截距最小值恰好取得在点 (𝑦,𝑣(𝑦))(y,v(y))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处，以及
  2. 如果存在，如何找到这样的斜率 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

第一个问题相对容易解决．因为当直线斜率 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 发生变化时，所有这些直线切出的集合（即它们对应的上半平面的交）必然是一个凸集．因此，这些直线能够经过某个点，当且仅当这个点在该凸集的下凸壳上．这等价于说，函数 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 [凸函数](../slope-trick/#离散点集上的凸函数)．

第二个问题则更为精细．因为所求点的横坐标已经知道是 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，一个自然的思路是，计算 ℎ(𝜆)h(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，顺便求出限制函数 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在当前最优解 𝑥𝜆xλ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的取值．比如，在前文提到的例子中，求解带惩罚的问题时，可以记录带惩罚的目标函数取得最优解时，选取的物品数量．然后，将 𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与所期望的 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行比较，并相应调整下次计算时的 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．这就是最为传统的 WQS 二分的方法．

总结一下，传统 WQS 二分的基本流程如下：

  1. 初始时，选取一个 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的合理的区间；
  2. 在当前的区间中选择一个 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  3. 求解带惩罚的问题 ℎ(𝜆) =min𝑥∈𝑋𝑓(𝑥) −𝜆𝑔(𝑥)h(λ)=minx∈Xf(x)−λg(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并记录它的最优解 𝑥𝜆xλ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值 𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  4. 如果 𝑔(𝑥𝜆) =𝑦g(xλ)=y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到原问题的最优价值 𝑣(𝑦) =ℎ(𝜆) +𝜆𝑦v(y)=h(λ)+λy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直接结束算法；
  5. 否则，根据 𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小关系，调整 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的区间，并回到步骤 2．

这一基本流程已经足以解决一些问题，但并不完善．接下来，本文将讨论对这一基本流程的改进．

### 共线情形的处理

在应用基本流程时，首先遇到的问题就是共线情形无法正确处理．

如果点集 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的下凸壳上有三个及以上的红点共线，那么在上述基本流程中，可能无法正确地判断 𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小关系．比如，设共线的三个红点的横坐标分别为 𝑦1,𝑦2,𝑦3y1,y2,y3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且它们共线的直线的斜率为 𝜆∗λ∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，要正确求解 𝑣(𝑦2)v(y2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就必须保证算法终止时，最后计算的问题是 ℎ(𝜆∗)h(λ∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为 𝜆∗λ∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是唯一一个最小化截距时能够经过点 (𝑦2,𝑣(𝑦2))(y2,v(y2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的直线的斜率．但是，因为在求解 ℎ(𝜆∗)h(λ∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的过程中，记录的 𝑔(𝑥𝜆∗)g(xλ∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能是 𝑦1,𝑦2,𝑦3y1,y2,y3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的任意一个．如果记录到的 𝑔(𝑥𝜆∗)g(xλ∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不等于 𝑦2y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么算法将错误地继续运行，并向着背离 𝑦2y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方向调整 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的区间，最终将得到错误的结果．

为了解决共线的情形，一种处理方法是在记录最优解 𝑥𝜆xλ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的 𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，总是使之尽可能大（或尽可能小）．同时，将二分中的终止条件从寻找恰好满足 𝑔(𝑥𝜆) =𝑦g(xλ)=y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 改为寻找满足 𝑔(𝑥𝜆) ≥𝑦g(xλ)≥y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（或 𝑔(𝑥𝜆) ≤𝑦g(xλ)≤y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的最小（或最大）的 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在上一段的例子中，这相当于计算问题 ℎ(𝜆∗)h(λ∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，输出的 𝑔(𝑥𝜆∗)g(xλ∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑦3y3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就保证了算法终止时，最后计算的问题是 ℎ(𝜆∗)h(λ∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．实现这一方法时，需要注意最后输出的不是 ℎ(𝜆) +𝜆𝑔(𝑥𝜆)h(λ)+λg(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而是 ℎ(𝜆) +𝜆𝑦h(λ)+λy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为记录的 𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 未必等于实际的限制 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

另一种处理方法是实数二分．如果问题涉及的数字都是整数，显然，WQS 二分中的斜率也是整数．在二分中引入实数，是为了保证错误地排除正确选项 𝜆∗λ∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，可以通过小数部分调整回来，最终逼近正确答案 𝜆∗λ∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．例如，在上面的例子中，如果计算问题 ℎ(𝜆∗)h(λ∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，记录的 𝑔(𝑥𝜆∗)g(xλ∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑦1y1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，小于所希望的 𝑦2y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，算法就会转而考虑区间 (𝜆∗,𝜆𝑟](λ∗,λr]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝜆𝑟λr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在区间的右端点．对于整数的情形，这一区间实际应该写作 [𝜆∗ +1,𝜆𝑟][λ∗+1,λr]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这就排除了在后续算法中接近正确答案 𝜆∗λ∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的可能．但是，实数二分时，考虑的区间仍然是 (𝜆∗,𝜆𝑟](λ∗,λr]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而且，对于该区间中的 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求解 ℎ(𝜆)h(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时记录的 𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是不小于 𝑦3y3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而严格大于 𝑦2y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．因此，随着算法继续进行，会不断地舍去右半区间，从而，最终得到的 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的范围可以保证在 𝜆∗λ∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 附近．当然，因为已经知道所求的斜率是一个整数，实数二分终止时的精度不必太高，只要能保证二分的区间中只包含一个整数即可，这一整数就是要寻找的 𝜆∗λ∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

正确地处理共线情形后，WQS 二分足以解决绝大多数算法竞赛会遇到的 WQS 二分的问题．但是，这一方法仍然存在一些不足之处：它无法处理 𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 难以记录的情形，也无法处理高维 WQS 二分中多个点共面的情形．本文将进一步考察最优化问题 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的性质，并提出更为一般的处理方法．

## 对偶方法

本节介绍一种 WQS 二分的实现方法，它只要求对于所有 𝜆 ∈𝐑𝑑λ∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以高效地计算

ℎ(𝜆)=min𝑥∈𝑋𝑓(𝑥)−𝜆⋅𝑔(𝑥)h(λ)=minx∈Xf(x)−λ⋅g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的取值，且原问题的最优价值 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝑦 ∈𝐑𝑑y∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数1．用一句话概括，本节将证明原问题的价值函数 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就等于它的对偶问题的最优价值

𝑣⋆(𝑦)=sup𝜆∈𝐑𝑑ℎ(𝜆)+𝜆⋅𝑦,v⋆(y)=supλ∈Rdh(λ)+λ⋅y,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而对偶问题的目标函数是关于 𝜆 ∈𝐑𝑑λ∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凹函数，从而是单峰函数，可以通过 [三分法](../../../basic/binary/#三分法) 或 [黄金分割法](../../../basic/binary/#优化黄金分割法) 高效地求解，复杂度仍然是 𝑂(𝑇(𝑛)log𝑑⁡𝐿)O(T(n)logd⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．这就完全地解决了传统 WQS 二分方法中记录 𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值可能会出现的问题，同时，允许将 WQS 二分的思想应用至高维的情形．

另外，本节还说明，𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的范围可以通过 ℎ(𝜆)h(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求得，而无需在求解 ℎ(𝜆)h(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时额外记录．例如，对于 𝑑 =1d=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且问题只涉及整数的情形，可以证明 𝑔(𝑥𝜆)g(xλ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值范围恰为

[ℎ(𝜆−1)−ℎ(𝜆),ℎ(𝜆)−ℎ(𝜆+1)].[h(λ−1)−h(λ),h(λ)−h(λ+1)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这实际上也对于不得不采取前文所述二分流程的题目，提供了又一种解决共线问题的方法．

接下来，本节将用凸分析的理论证明这些结论成立．至于这些方法的具体应用，可以参考 例题 一节．

### Lagrange 对偶

考虑用 [Lagrange 乘子法](https://en.wikipedia.org/wiki/Lagrange_multiplier) 解决该问题．引入 Lagrange 乘子 𝜆 ∈𝐑𝑑λ∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，Lagrangian 可以写作

𝐿(𝑥,𝜆,𝑦)=𝑓(𝑥)−𝜆⋅𝑔(𝑥)+𝜆⋅𝑦.L(x,λ,y)=f(x)−λ⋅g(x)+λ⋅y.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为只要 𝑔(𝑥) −𝑦g(x)−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有一个分量非零，就可以让相应的 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分量趋于（正或负）无穷，所以有

sup𝜆∈𝐑𝑑𝐿(𝑥,𝜆,𝑦)={𝑓(𝑥),𝑔(𝑥)=𝑦,+∞,otherwise.supλ∈RdL(x,λ,y)={f(x),g(x)=y,+∞,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这说明，原问题可以写作

𝑣(𝑦)=min𝑥∈𝑋sup𝜆∈𝐑𝑑𝐿(𝑥,𝜆,𝑦).v(y)=minx∈Xsupλ∈RdL(x,λ,y).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

交换两次最值操作，就得到它的 [对偶问题](https://en.wikipedia.org/wiki/Duality_%28optimization%29)：

𝑣⋆(𝑦)=sup𝜆∈𝐑𝑑min𝑥∈𝑋𝐿(𝑥,𝜆,𝑦)=sup𝜆∈𝐑𝑑ℎ(𝜆)+𝜆⋅𝑦.v⋆(y)=supλ∈Rdminx∈XL(x,λ,y)=supλ∈Rdh(λ)+λ⋅y.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

马上要说明的是，在 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数的条件下，强对偶（strong duality）成立，即 𝑣⋆(𝑦) =𝑣(𝑦)v⋆(y)=v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 凸共轭

为了说明强对偶成立，需要引入凸共轭的概念．

凸共轭

对于函数 𝑓 :𝐑𝑑 →𝐑 ∪{ ±∞}f:Rd→R∪{±∞}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的 **凸共轭** （convex conjugate），或称 **Legendre–Fenchel 变换** （Legendre–Fenchel transformation），是指函数

𝑓∗(𝑥∗)=sup𝑥∈𝐑𝑑𝑥∗⋅𝑥−𝑓(𝑥).f∗(x∗)=supx∈Rdx∗⋅x−f(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从变量 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的角度看，𝑓∗(𝑥∗)f∗(x∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一系列线性函数的上确界，所以，必然是 𝐑𝑑Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的凸函数．

超平面的「斜率向量」和「截距」

本文所讨论的向量空间 𝐑𝑑+1Rd+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的超平面的方程都具有形式

𝑦=𝑘⋅𝑥+𝑏.y=k⋅x+b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，本文不会涉及平行于 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴的超平面．为表述方便，本文并不严谨地将 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为该超平面的「斜率向量」，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为该超平面的「截距」．将这一超平面的方程写成更标准的形式，就是

𝑘⋅𝑥−𝑦=−𝑏.k⋅x−y=−b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它的一个法向量是 (𝑘, −1)(k,−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，所谓的斜率向量其实是将超平面的法向量归一化使得它的最后一个分量等于 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，所得到的法向量的前 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个分量．

几何直观上，函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸共轭描述的是，对于所有斜率向量为 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且与函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的上境图

epi⁡𝑓={(𝑥,𝑦)∈𝐑𝑑×𝐑:𝑓(𝑥)≤𝑦}epi⁡f={(x,y)∈Rd×R:f(x)≤y}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

相交的超平面，截距 𝑓(𝑥) −𝑥∗ ⋅𝑥f(x)−x∗⋅x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小值就是 −𝑓∗(𝑥∗)−f∗(x∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．换句话说，函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总在超平面 𝑦 =𝑥∗ ⋅𝑥 −𝑓∗(𝑥∗)y=x∗⋅x−f∗(x∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上方，且与该平面切于点 (𝑥0,𝑓(𝑥0))(x0,f(x0))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；当然，可能存在其余的切点．这样的超平面，称为 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的 **支撑超平面** （supporting hyperplane）．函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个支撑超平面的截距由它的斜率向量唯一确定，凸共轭就提供了这个从斜率向量到截距的映射．

在集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上最小化 𝑓(𝑥) −𝜆 ⋅𝑔(𝑥)f(x)−λ⋅g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就等价于在集合 {(𝑦,𝑣(𝑦))}{(y,v(y))}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上最小化 𝑣(𝑦) −𝜆 ⋅𝑦v(y)−λ⋅y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

min𝑥𝑓(𝑥)−𝜆⋅𝑔(𝑥)=min𝑦∈𝑔(𝑋)(min𝑥∈𝑋:𝑔(𝑥)=𝑦𝑓(𝑥)−𝜆⋅𝑔(𝑥))=min𝑦∈𝑔(𝑋)(min𝑥∈𝑋:𝑔(𝑥)=𝑦𝑓(𝑥))−𝜆⋅𝑦=min𝑦∈𝑔(𝑋)𝑣(𝑦)−𝜆⋅𝑦.minxf(x)−λ⋅g(x)=miny∈g(X)(minx∈X:g(x)=yf(x)−λ⋅g(x))=miny∈g(X)(minx∈X:g(x)=yf(x))−λ⋅y=miny∈g(X)v(y)−λ⋅y.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，有

ℎ(𝜆)=min𝑦∈𝑔(𝑋)𝑣(𝑦)−𝜆⋅𝑦=−𝑣∗(𝜆).h(λ)=miny∈g(X)v(y)−λ⋅y=−v∗(λ).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这说明 ℎ(𝜆)h(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝜆 ∈𝐑𝑑λ∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凹函数．进而，有

𝑣⋆(𝑦)=sup𝜆∈𝐑𝑑𝜆⋅𝑦−𝑣∗(𝜆)=𝑣∗∗(𝑦).v⋆(y)=supλ∈Rdλ⋅y−v∗(λ)=v∗∗(y).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，对偶问题的价值函数 𝑣⋆(𝑦)v⋆(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是原问题的价值函数 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的双重凸共轭，也称为 **双共轭** （biconjugate）．

所以，问题转化为：什么样的函数 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足它的双共轭就等于它自身？这一问题的答案由如下定理给出：

定理（Fenchel–Moreau）

对于函数 𝑓 :𝐑𝑑 →𝐑 ∪{ ±∞}f:Rd→R∪{±∞}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的双共轭等于它自身，即 𝑓∗∗ =𝑓f∗∗=f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当以下三个条件之一满足：

  1. 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是正常凸函数且 [下半连续](https://en.wikipedia.org/wiki/Semi-continuity)，
  2. 𝑓(𝑥) ≡ +∞f(x)≡+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或
  3. 𝑓(𝑥) ≡ −∞f(x)≡−∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

一个函数是正常的（proper），当且仅当它从不取得 −∞−∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，且不永远取得 +∞+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

对于非正常函数的情形，可以验证 𝑓(𝑥) ≡ +∞f(x)≡+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(𝑥) ≡ −∞f(x)≡−∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互为共轭．除此之外，只要 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在任何一点处取到 −∞−∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必然有 𝑓∗(𝑥∗) ≡ +∞f∗(x∗)≡+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，满足 𝑓∗∗ =𝑓f∗∗=f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非正常函数只有这两种情形．下面的讨论仅限于正常函数．对于正常函数，下半连续且凸的条件等价于它的上境图是闭凸集．

这一条件的必要性是容易的．因为 𝑓 =𝑓∗∗f=f∗∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑓∗f∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸共轭，作为一系列线性函数的上确界，它的上境图必然是一系列闭凸集的交集，所以必然是闭凸集．这就说明，满足 𝑓∗∗ =𝑓f∗∗=f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正常函数必然是下半连续且凸的．

反过来，这些条件也是充分的．和其他强对偶定理的证明一样，证明可以分为两步．

第一步，说明弱对偶成立，即 𝑓(𝑥) ≥𝑓∗∗(𝑥)f(x)≥f∗∗(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由凸共轭的定义可知，对于所有 𝑥,𝑥∗ ∈𝐑𝑑x,x∗∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

𝑓∗(𝑥∗)≥𝑥∗⋅𝑥−𝑓(𝑥).f∗(x∗)≥x∗⋅x−f(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就说明，对于所有 𝑥,𝑥∗ ∈𝐑𝑑x,x∗∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，同样有

𝑓(𝑥)≥𝑥∗⋅𝑥−𝑓∗(𝑥∗).f(x)≥x∗⋅x−f∗(x∗).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对不等式右侧中的 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取上确界，就有 𝑓(𝑥) ≥𝑓∗∗(𝑥)f(x)≥f∗∗(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

第二步，利用 [超平面分离定理](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem) 说明 𝑓(𝑥) ≤𝑓∗∗(𝑥)f(x)≤f∗∗(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．假设不然，存在 𝑥0 ∈𝐑𝑑x0∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑓(𝑥0) >𝑓∗∗(𝑥0)f(x0)>f∗∗(x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．因为 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的上境图 epi⁡(𝑓)epi⁡(f)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是闭凸集，而且单点集 {(𝑥0,𝑓∗∗(𝑥0))}{(x0,f∗∗(x0))}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是紧凸集，所以，根据超平面分离定理，存在 (𝜆,𝑡) ∈𝐑𝑑 ×𝐑(λ,t)∈Rd×R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛼 ∈𝐑α∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得对于所有 𝑥 ∈dom⁡𝑓 :={𝑥 ∈𝐑𝑑 :𝑓(𝑥) < +∞}x∈dom⁡f:={x∈Rd:f(x)<+∞}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和所有 𝑦 ≥𝑓(𝑥)y≥f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有

𝜆⋅𝑥−𝑡𝑦<𝛼<𝜆⋅𝑥0−𝑡𝑓∗∗(𝑥0)λ⋅x−ty<α<λ⋅x0−tf∗∗(x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

成立．因为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以选得任意大，所以必然有 𝑡 ≥0t≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这又可以分为两种情形．

首先，讨论 𝑡 >0t>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．此时，将不等式的各部分都同除以 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并设 𝜆′ =𝑡−1𝜆λ′=t−1λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛼′ =𝑡−1𝛼α′=t−1α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到

𝜆′⋅𝑥−𝑦<𝛼′<𝜆′⋅𝑥0−𝑓∗∗(𝑥0).λ′⋅x−y<α′<λ′⋅x0−f∗∗(x0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对所有 𝑥 ∈dom⁡𝑓x∈dom⁡f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝑦 =𝑓(𝑥)y=f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就都成立

𝛼′>𝜆′⋅𝑥−𝑓(𝑥).α′>λ′⋅x−f(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

故而，对不等号右侧的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取上确界，有

𝛼′≥sup𝑥∈𝐑𝑑𝜆′⋅𝑥−𝑓(𝑥)=𝑓∗(𝜆′).α′≥supx∈Rdλ′⋅x−f(x)=f∗(λ′).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而，有

𝑓∗∗(𝑥0)<𝜆′⋅𝑥0−𝑓∗(𝜆′)≤sup𝑥∗∈𝐑𝑑𝑥∗⋅𝑥0−𝑓∗(𝑥∗)=𝑓∗∗(𝑥0).f∗∗(x0)<λ′⋅x0−f∗(λ′)≤supx∗∈Rdx∗⋅x0−f∗(x∗)=f∗∗(x0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这一矛盾说明 𝑡 >0t>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形并不成立．

最后，讨论 𝑡 =0t=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．事实上，将要说明的是，可以通过微扰，将它转化为 𝑡 >0t>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．任取 𝜆0 ∈dom⁡𝑓∗λ0∈dom⁡f∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据凸共轭的定义可知，对于任何 𝑥 ∈dom⁡𝑓x∈dom⁡f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦 ≥𝑓(𝑥)y≥f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有

𝜆0⋅𝑥−𝑦≤𝑓∗(𝜆0).λ0⋅x−y≤f∗(λ0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，对于任意 𝜀 >0ε>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

(𝜆+𝜀𝜆0)⋅𝑥−𝜀𝑦<𝛼+𝜀𝑓∗(𝜆0).(λ+ελ0)⋅x−εy<α+εf∗(λ0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

同时，因为 𝛼 <𝜆 ⋅𝑥0α<λ⋅x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，对于充分小的 𝜀 >0ε>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又有

𝛼+𝜀𝑓∗(𝜆0)<(𝜆+𝜀𝜆0)⋅𝑥0−𝜀𝑓∗∗(𝑥0).α+εf∗(λ0)<(λ+ελ0)⋅x0−εf∗∗(x0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，如果取 𝜆′ =𝜆 +𝜀𝜆0λ′=λ+ελ0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑡′ =𝜀t′=ε![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛼′ =𝛼 +𝜀𝑓∗(𝜆0)α′=α+εf∗(λ0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，就有

𝜆′⋅𝑥−𝑡′𝑦<𝛼′<𝜆′⋅𝑥0−𝑡′𝑓∗∗(𝑥0).λ′⋅x−t′y<α′<λ′⋅x0−t′f∗∗(x0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就又回到了前一种情形，仍然会导致矛盾．

这一矛盾说明，并不存在满足 𝑓(𝑥0) >𝑓∗∗(𝑥0)f(x0)>f∗∗(x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点 𝑥0 ∈𝐑𝑑x0∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．故而，总有 𝑓(𝑥0) ≤𝑓∗∗(𝑥0)f(x0)≤f∗∗(x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

结合这两步证明的结果，就得到 𝑓∗∗(𝑥) =𝑓(𝑥)f∗∗(x)=f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．

因此，强对偶成立，当且仅当 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝑦 ∈𝐑𝑑y∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数2．

### 次梯度

上一节说明了，带惩罚的问题的价值函数 ℎ(𝜆)h(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是原问题的价值函数 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸共轭的相反数．因为凸共轭的定义实际上是一个含参数的最优化问题，所以它也成立类似 [包络定理](https://en.wikipedia.org/wiki/Envelope_theorem) 的结论．但是，因为凸函数并非处处可微的，所以需要首先将导数的定义推广到凸函数的情形．这就引出了次梯度的概念．

次梯度

对于凸函数 𝑓 :𝐑𝑑 →𝐑 ∪{ ±∞}f:Rd→R∪{±∞}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥0 ∈dom⁡𝑓x0∈dom⁡f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果向量 𝑥∗ ∈𝐑𝑑x∗∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足对于任何 𝑥 ∈𝐑𝑑x∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

𝑓(𝑥)≥𝑓(𝑥0)+𝑥∗⋅(𝑥−𝑥0),f(x)≥f(x0)+x∗⋅(x−x0),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么，就称 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的一个 **次梯度** （subgradient）．函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的全体次梯度的集合称为它在该处的 **次微分** （subdifferential），记作 𝜕𝑓(𝑥0)∂f(x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

几何直观上，凸函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的次微分，就是它在该处的所有支撑超平面的斜率向量的集合．对于一维的情形，次微分

𝜕𝑓(𝑥0)=[𝜕−𝑓(𝑥0),𝜕+𝑓(𝑥0)],∂f(x0)=[∂−f(x0),∂+f(x0)],![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝜕−𝑓(𝑥0)∂−f(x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜕+𝑓(𝑥0)∂+f(x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的左右导数．进一步地，对于整数集上的凸函数 𝑓 :𝐙 →𝐑 ∪{ ±∞}f:Z→R∪{±∞}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 延拓而来的 ˜𝑓(𝑥)f~(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它在整数点 𝑥 =𝑘x=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的左右导数就是左右两侧的一阶差分：

𝜕˜𝑓(𝑘)=[𝑓(𝑘)−𝑓(𝑘−1),𝑓(𝑘+1)−𝑓(𝑘)].∂f~(k)=[f(k)−f(k−1),f(k+1)−f(k)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

显然，凸函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在点 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处可微，当且仅当它在该处的次微分 𝜕𝑓(𝑥0)∂f(x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是单点集．

因为凸共轭提供了从支撑超平面的斜率向量到它的截距的映射，所以，利用凸共轭，可以判断一个斜率向量 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否是凸函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在给定点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的一个次梯度．

定理（凸共轭与次梯度）

对于正常凸函数 𝑓 :𝐑𝑑 →𝐑f:Rd→R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和任意 𝑥,𝑥∗ ∈𝐑𝑑x,x∗∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

𝑥∗∈𝜕𝑓(𝑥)⟺𝑥∗⋅𝑥=𝑓(𝑥)+𝑓∗(𝑥∗).x∗∈∂f(x)⟺x∗⋅x=f(x)+f∗(x∗).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而，如果 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还是下半连续的，那么这两个条件都等价于 𝑥 ∈𝜕𝑓∗(𝑥∗)x∈∂f∗(x∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

按照次梯度的定义，𝑥∗ ∈𝜕𝑓(𝑥)x∗∈∂f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当

𝑓(𝑥′)≥𝑓(𝑥)+𝑥∗⋅(𝑥′−𝑥), ∀𝑥′∈𝐑𝑑.f(x′)≥f(x)+x∗⋅(x′−x), ∀x′∈Rd.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这等价于

𝑥∗⋅𝑥−𝑓(𝑥)≥𝑥∗⋅𝑥′−𝑓(𝑥′), ∀𝑥′∈𝐑𝑑.x∗⋅x−f(x)≥x∗⋅x′−f(x′), ∀x′∈Rd.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这又等价于

𝑥∗⋅𝑥−𝑓(𝑥)≥sup𝑥′∈𝐑𝑑𝑥∗⋅𝑥′−𝑓(𝑥′)=𝑓∗(𝑥∗).x∗⋅x−f(x)≥supx′∈Rdx∗⋅x′−f(x′)=f∗(x∗).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但是，依据凸共轭的定义，总是有

𝑥∗⋅𝑥−𝑓(𝑥)≤𝑓∗(𝑥∗).x∗⋅x−f(x)≤f∗(x∗).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，前一式中的大于等于号实际上等价于等号，也就等价于下式

𝑥∗⋅𝑥=𝑓(𝑥)+𝑓∗(𝑥∗).x∗⋅x=f(x)+f∗(x∗).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就完成了第一部分的证明．

对于 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是下半连续的正常凸函数的情形，依 Fenchel–Moreau 定理，有 𝑓∗∗ =𝑓f∗∗=f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，这两个条件等价于

𝑥∗⋅𝑥=𝑓∗(𝑥∗)+𝑓∗∗(𝑥).x∗⋅x=f∗(x∗)+f∗∗(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再次应用第一部分的结论，它们也就等价于 𝑥 ∈𝜕𝑓∗(𝑥∗)x∈∂f∗(x∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这一结论说明，如果 𝑓∗∗ =𝑓f∗∗=f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么凸共轭 𝑓∗f∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的次微分 𝜕𝑓∗(𝑥∗)∂f∗(x∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，恰好就是斜率向量为 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的支撑超平面与上境图 epi⁡𝑓epi⁡f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的交点的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分量的集合．

推论

对于下半连续的正常凸函数 𝑓 :𝐑𝑑 →𝐑f:Rd→R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和任意 𝑥,𝑥∗ ∈𝐑𝑑x,x∗∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

𝜕𝑓(𝑥)=arg⁡max𝑦∗∈𝐑𝑑𝑥⋅𝑦∗−𝑓∗(𝑦∗),𝜕𝑓∗(𝑥∗)=arg⁡max𝑦∈𝐑𝑑𝑥∗⋅𝑦−𝑓(𝑦).∂f(x)=arg⁡maxy∗∈Rdx⋅y∗−f∗(y∗),∂f∗(x∗)=arg⁡maxy∈Rdx∗⋅y−f(y).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

下面，证明第二个等式．第一个等式的证明与之类似．

按照凸共轭的定义，有

𝑓∗(𝑥∗)=sup𝑦∈𝐑𝑑𝑥∗⋅𝑦−𝑓(𝑦),f∗(x∗)=supy∈Rdx∗⋅y−f(y),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，

𝑥∈arg⁡max𝑦∈𝐑𝑑𝑥∗⋅𝑦−𝑓(𝑦)x∈arg⁡maxy∈Rdx∗⋅y−f(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当且仅当 𝑓∗(𝑥∗) =𝑥∗ ⋅𝑥 −𝑓(𝑥)f∗(x∗)=x∗⋅x−f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而这一等式成立，又当且仅当 𝑥 ∈𝜕𝑓∗(𝑥∗)x∈∂f∗(x∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就证明了两个集合是相等的．

应用到本文的场景中，这一结论说明，求解问题

ℎ(𝜆)=min𝑥∈𝑋𝑓(𝑥)−𝜆⋅𝑔(𝑥)=min𝑦∈𝑔(𝑋)𝑣(𝑦)−𝜆⋅𝑦h(λ)=minx∈Xf(x)−λ⋅g(x)=miny∈g(X)v(y)−λ⋅y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时，限制函数 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在最优决策集合上的取值恰为 𝜕( −ℎ(𝜆))∂(−h(λ))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于 𝑑 =1d=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且问题只涉及整数的情形，这一集合就是区间

[ℎ(𝜆−1)−ℎ(𝜆),ℎ(𝜆)−ℎ(𝜆+1)].[h(λ−1)−h(λ),h(λ)−h(λ+1)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于连续的整数 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这些区间首尾相接，所以，如果用于二分，只需要计算一侧的端点即可．

## 凸性证明

应用 WQS 二分的前提条件是价值函数的凸性．在算法竞赛中，可以通过打表、感性理解等方式猜测凸性成立．但是，严格地证明凸性成立，往往并不容易．本节结合如下经典题目，介绍算法竞赛中常见的证明凸性的方法．

种树问题

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个树坑，要种 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树．树不能栽种于相邻的两个坑．给定长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示在每个坑种树的收益，收益可正可负．求种完这 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树最大可能的收益和．

简言之，就是在长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的链上，求解大小为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大权独立集的问题．

这些方法粗略地可以分为四类：

  * 归约为凸优化问题（包括 [线性规划](../../../math/linear-programming/) 等）的价值函数对参数的凸性，这包括建立 [费用流](../../../graph/flow/min-cost/) 模型等方法；
  * 利用状态转移方程也可以归纳地证明凸性成立，过程中可能会用到一些 [保持凸性的变换](../slope-trick/#凸函数的变换)；
  * 对于区间分拆类型的问题，可以验证每段区间的成本函数满足 [四边形不等式](../quadrangle/)；
  * 最后，对于特殊的问题，也可以通过交换论证直接说明凸性成立．

这些证明方法本身往往都同该问题的某种解法联系在一起．

### 归约为含参凸优化

考虑如下形式的含参凸优化问题：

𝑣(𝑦)=inf𝑥∈D(𝑦)𝑓(𝑥,𝑦).v(y)=infx∈D(y)f(x,y).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，目标函数 𝑓 :𝐑𝑛 ×𝐑𝑑 →𝐑 ∪{ ±∞}f:Rn×Rd→R∪{±∞}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于每个 𝑦 ∈𝐑𝑑y∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是关于 𝑥 ∈𝐑𝑚x∈Rm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数，而可行域 D :𝐑𝑑 →P(𝐑𝑚)D:Rd→P(Rm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐑𝑑Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的集合值函数，且对于每个 𝑦 ∈𝐑𝑑y∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，集合 D(𝑦)D(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是凸集．这些条件保证了对于任意参数 𝑦 ∈𝐑𝑑y∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这都是一个凸优化问题．

定理

假设上述含参凸优化问题满足如下条件：

  1. 目标函数 𝑓(𝑥,𝑦)f(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 (𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数；
  2. 可行域映射 𝑦 ↦D(𝑦)y↦D(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的图像 {(𝑥,𝑦) :𝑥 ∈D(𝑦)}{(x,y):x∈D(y)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是凸集．

如果对于任意 𝑦 ∈𝐑𝑑y∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑣(𝑦) > −∞v(y)>−∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，价值函数 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正常凸函数．

证明

对于任意 𝑦1,𝑦2 ∈𝐑𝑑y1,y2∈Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛼 ∈(0,1)α∈(0,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，需要证明

𝑣(𝛼𝑦1+(1−𝛼)𝑦2)≤𝛼𝑣(𝑦1)+(1−𝛼)𝑣(𝑦2).v(αy1+(1−α)y2)≤αv(y1)+(1−α)v(y2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果 𝑣(𝑦1) = +∞v(y1)=+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑣(𝑦2) = +∞v(y2)=+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么不等式的右侧就是 +∞+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不等式必然成立．否则，𝑣(𝑦1)v(y1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣(𝑦2)v(y2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是有限值．对于任意 𝜀 >0ε>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑖 =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都存在 𝑥𝑖 ∈D(𝑦𝑖)xi∈D(yi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑓(𝑥𝑖,𝑦𝑖) <𝑣(𝑦𝑖) +𝜀f(xi,yi)<v(yi)+ε![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．利用映射 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的图像的凸性可知

𝛼𝑥1+(1−𝛼)𝑥2∈D(𝛼𝑦1+(1−𝛼)𝑦2).αx1+(1−α)x2∈D(αy1+(1−α)y2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，𝛼𝑥1 +(1 −𝛼)𝑥2αx1+(1−α)x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是参数为 𝛼𝑦1 +(1 −𝛼)𝑦2αy1+(1−α)y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优化问题的一个可行解．利用最优化条件和目标函数的凸性可知

𝑣(𝛼𝑦1+(1−𝛼)𝑦2)≤𝑓(𝛼𝑥1+(1−𝛼)𝑥2,𝛼𝑦1+(1−𝛼)𝑦2)≤𝛼𝑓(𝑥1,𝑦1)+(1−𝛼)𝑓(𝑥2,𝑦2)<𝛼𝑣(𝑦1)+(1−𝛼)𝑣(𝑦2)+𝜀.v(αy1+(1−α)y2)≤f(αx1+(1−α)x2,αy1+(1−α)y2)≤αf(x1,y1)+(1−α)f(x2,y2)<αv(y1)+(1−α)v(y2)+ε.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝜀ε![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选取是任意的，令 𝜀 →0ε→0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有

𝑣(𝛼𝑦1+(1−𝛼)𝑦2)≤𝛼𝑣(𝑦1)+(1−𝛼)𝑣(𝑦2).v(αy1+(1−α)y2)≤αv(y1)+(1−α)v(y2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，价值函数 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸性成立．

算法竞赛中，最为常见的凸优化问题就是线性规划问题．

推论

设 𝑐 ∈𝐑𝑛c∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐴1 ∈𝐑𝑑1×𝑛A1∈Rd1×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐴2 ∈𝐑𝑑2×𝑛A2∈Rd2×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑦1 ∈𝐑𝑑1y1∈Rd1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑦2 ∈𝐑𝑑2y2∈Rd2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考虑如下含参线性规划问题：

𝑣(𝑦1,𝑦2)=min𝑥∈𝐑𝑛𝑐⋅𝑥 subject to 𝐴1𝑥≤𝑦1,𝐴2𝑥=𝑦2,𝑥≥0.v(y1,y2)=minx∈Rnc⋅x subject to A1x≤y1,A2x=y2,x≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么，价值函数 𝑣(𝑦1,𝑦2)v(y1,y2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 (𝑦1,𝑦2)(y1,y2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数．

无论是不等式约束，还是等式约束，线性规划的价值函数都是约束条件参数的凸函数．

很多图论问题都可以写成线性规划问题的形式：

  * 网络流问题：最大流、最小割、最小费用流；
  * 无负环的最短路问题；
  * 二分图的最大（权）匹配、最小点覆盖等问题；
  * 一般图的最大（权）匹配问题；
  * 最小生成树问题3．

因此，这些问题的价值函数都是这些问题的参数的凸（凹）函数．

整数约束

利用图论模型为实际问题建模时，通常有隐含的整数限制，例如一条边只能选或不选、流量只能是整数等．因此，它们只能转化为整数线性规划（integer linear programming, ILP）问题而非线性规划（LP）问题．因为 ILP 问题并非凸优化问题，所以它的价值函数未必是该问题的参数的凸函数．将一个 ILP 问题中的整数约束松弛掉后就得到一个 LP 问题，但后者未必存在满足整数约束的最优解．因此，松弛整数约束后得到的 LP 的最优价值有可能严格优于相应的 ILP 问题，两者未必等价．

上文列举的那些图论问题，都可以写成一个 LP 问题而不需要施加整数约束；但对于其他的一些问题，例如一般图的最大独立集问题等，整数约束则是必要的．另外，即使一个图论问题可以写成 LP 的形式，在该问题引入额外的线性约束条件后，仍然可能会破坏相应的 ILP 问题和 LP 问题的等价性，从而这个带约束的图论问题不再能够写成线性规划的形式．

例如，在费用流的语境下，有如下常见结论：

推论

[最小费用流模型](../../../graph/flow/min-cost/) 中，最小费用 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是流量 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数．

证明

设有向图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，边 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的容量为 𝑐𝑖𝑗cij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，单位流量的费用为 𝑤𝑖𝑗wij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),，源点和汇点分别为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．记决策变量为 {𝑓𝑖𝑗}{fij}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑓𝑖𝑗fij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为边 (𝑖,𝑗) ∈𝐸(i,j)∈E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的流量．那么，最小费用流可以写成如下线性规划问题：

𝑣(𝑚)=min{𝑓𝑖𝑗}∑(𝑖,𝑗)∈𝐸𝑤𝑖𝑗𝑓𝑖𝑗subject to ∑(𝑗,𝑖)∈𝐸𝑓𝑗𝑖−∑(𝑖,𝑗)∈𝐸𝑓𝑖𝑗=⎧{ {⎨{ {⎩−𝑚,𝑖=𝑠,𝑚,𝑖=𝑡,0,otherwise, ∀𝑖∈𝑉,0≤𝑓𝑖𝑗≤𝑐𝑖𝑗, ∀(𝑖,𝑗)∈𝐸.v(m)=min{fij}∑(i,j)∈Ewijfijsubject to ∑(j,i)∈Efji−∑(i,j)∈Efij={−m,i=s,m,i=t,0,otherwise, ∀i∈V,0≤fij≤cij, ∀(i,j)∈E.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，最小费用 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是参数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数．

算法竞赛中很多问题都可以归约为网络流等图论问题，从而都可以通过类似的方式建立价值函数的凸性．

利用这一方法，可以得到种树问题的第一个凸性证明：

凸性证明一

种树问题的最大收益实际上可以通过如下最大费用最大流模型得出：

  * 从源点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，向结点 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，连接一条容量为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、费用为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边；
  * 从结点 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，向每个奇数结点 𝑖 =1,3,⋯,2⌈𝑛/2⌉ −1i=1,3,⋯,2⌈n/2⌉−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连接一条容量为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、费用为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边；
  * 从每个偶数结点 𝑖 =0,2,⋯,2⌊𝑛/2⌋i=0,2,⋯,2⌊n/2⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，向汇点 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连接一条容量为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、费用为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边；
  * 对于每个 𝑖 =1,⋯,𝑛i=1,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从 𝑖 −1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的奇数结点出发，向偶数结点连接一条容量为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、费用为 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边．

最终答案就是求得的最大费用．将这一图论模型转换为相应的线性规划问题（具体见上文推论的证明），那么，总流量 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将出现在表示边 (𝑠,𝑟)(s,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的流量限制的不等式中．由推论可知，最大费用 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是流量 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凹函数．

利用该费用流模型，可以通过模拟费用流或 [反悔贪心](../../../basic/greedy/#后悔解法) 的方法在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度内解决该问题．

### 利用状态转移方程

尽管状态转移方程无法提供有效的计算方式，但是，它常常可以用于证明状态函数 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于参数 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 具有凸性．具体地说，就是将 𝑓(𝑖, ⋅)f(i,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这一函数视为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的状态，就可以将关于 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的状态转移方程看作是关于 𝑓(𝑖, ⋅)f(i,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递推关系，从而可以归纳地证明每个 𝑓(𝑖, ⋅)f(i,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是凸函数．这类证明凸性的方法在 [Slope Trick 优化 DP](../slope-trick/) 的场景中更为常见，该页面也讨论了常见的保持凸性的变换．

这一方法同样可以用于证明种树问题的凸性：

凸性证明二

设 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个坑种 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树时的最大收益．考察如下状态转移方程：

𝑓(𝑖,𝑗)=max{𝑓(𝑖−1,𝑗),𝑓(𝑖−2,𝑗−1)+𝑎𝑖}.f(i,j)=max{f(i−1,j),f(i−2,j−1)+ai}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将这一状态转移方程看作是函数 𝑓(𝑖, ⋅)f(i,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递推关系式．因为最值符号内涉及两个不同的函数，这并不能表达为卷积上确界的形式．但是，仍然可以通过归纳的方法证明函数 𝑓(𝑖, ⋅)f(i,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是凹函数．

实际上，需要归纳地证明如下两点：

  * 𝑓(𝑖,𝑗) −𝑓(𝑖 −2,𝑗 −1)f(i,j)−f(i−2,j−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递减；
  * 𝑓(𝑖,𝑗) −𝑓(𝑖 −1,𝑗)f(i,j)−f(i−1,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递增．

归纳起点是平凡的．假设它们对于所有 𝑖 −1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 及之前的自然数都成立，现在证明它对 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也成立．直接验证即可．

首先，由归纳假设，有

𝑓(𝑖−1,𝑗)−𝑓(𝑖−2,𝑗−1)=(𝑓(𝑖,𝑗)−𝑓(𝑖−2,𝑗−1))−(𝑓(𝑖,𝑗)−𝑓(𝑖−1,𝑗))f(i−1,j)−f(i−2,j−1)=(f(i,j)−f(i−2,j−1))−(f(i,j)−f(i−1,j))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

关于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递减．所以，有

𝑓(𝑖,𝑗)−𝑓(𝑖−2,𝑗−1)=max{𝑓(𝑖−1,𝑗)−𝑓(𝑖−2,𝑗−1),𝑎𝑖}f(i,j)−f(i−2,j−1)=max{f(i−1,j)−f(i−2,j−1),ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

关于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递减，且

𝑓(𝑖,𝑗)−𝑓(𝑖−1,𝑗)=max{0,𝑎𝑖−(𝑓(𝑖,𝑗)−𝑓(𝑖−2,𝑗−1))}f(i,j)−f(i−1,j)=max{0,ai−(f(i,j)−f(i−2,j−1))}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

关于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递增．这就完成了归纳．

进而，有

𝑓(𝑖,𝑗)−𝑓(𝑖,𝑗−1)=(𝑓(𝑖,𝑗)−𝑓(𝑖−2,𝑗−1))−(𝑓(𝑖,𝑗−1)−𝑓(𝑖−1,𝑗−1))−(𝑓(𝑖−1,𝑗−1)−𝑓(𝑖−2,𝑗−1))f(i,j)−f(i,j−1)=(f(i,j)−f(i−2,j−1))−(f(i,j−1)−f(i−1,j−1))−(f(i−1,j−1)−f(i−2,j−1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

关于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递减．这就说明 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凹函数，从而，价值函数 𝑣(𝑚) =𝑓(𝑛,𝑚)v(m)=f(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凹函数．

这个证明的一个副产品是，对于任意 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都存在 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝑓(𝑖,𝑗)={𝑓(𝑖−1,𝑗),𝑗≤𝑝𝑖,𝑓(𝑖−2,𝑗−1)+𝑎𝑖,𝑗>𝑝𝑖.f(i,j)={f(i−1,j),j≤pi,f(i−2,j−1)+ai,j>pi.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这说明，可以通过平衡树直接维护序列 𝑓(𝑖, ⋅)f(i,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，复杂度是 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．但是，好处是可以处理任意种树间隔的一般情形，且一次性地获得了所有 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

### 四边形不等式

算法竞赛中，另一类常见的成立凸性的问题是 [区间分拆问题](../quadrangle/#区间分拆问题)．该页面证明了，如果单个区间的成本函数满足四边形不等式，那么限制区间个数的区间分拆问题的最小成本是区间个数的凸函数．该页面同样提供了一些判断某个函数 𝑤(𝑙,𝑟)w(l,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否满足四边形不等式的方法．最为直接的方法就是计算它的二阶混合差分：

Δ𝑙Δ𝑟𝑤(𝑙,𝑟)=Δ𝑙(𝑤(𝑙,𝑟+1)−𝑤(𝑙,𝑟))=𝑤(𝑙+1,𝑟+1)−𝑤(𝑙+1,𝑟)−𝑤(𝑙,𝑟+1)+𝑤(𝑙,𝑟).ΔlΔrw(l,r)=Δl(w(l,r+1)−w(l,r))=w(l+1,r+1)−w(l+1,r)−w(l,r+1)+w(l,r).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

函数 𝑤(𝑙,𝑟)w(l,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足四边形不等式，当且仅当 Δ𝑙Δ𝑟𝑤(𝑙,𝑟)ΔlΔrw(l,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非正．直观上，满足四边形不等式的函数通常意味着，区间向两侧扩大——即左端点向左移动和右端点向右移动——具有某种协同效应．

种树问题同样可以看作是一个区间分拆问题，可以通过验证四边形不等式进行证明．

凸性证明三

在种树的收益序列前添加一个 𝑎0a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它可以是任何值．然后，种树问题就等价于将序列 {𝑎0,𝑎1,⋯,𝑎𝑛}{a0,a1,⋯,an}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分成 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段，且每段的收益函数为

𝑤(𝑙,𝑟)=max𝑖∈[𝑙+1,𝑟]𝑎𝑖w(l,r)=maxi∈[l+1,r]ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的区间分拆问题．也就是说，每一段的收益是除去第一棵树外，其余树的收益的最大值——这就保证了间隔种树．

因为这是最大化问题，需要验证「交叉大于包含」，即对于任意 𝑎 <𝑏 <𝑐 <𝑑a<b<c<d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都成立

𝑤(𝑎,𝑐)+𝑤(𝑏,𝑑)≥𝑤(𝑎,𝑑)+𝑤(𝑏,𝑐).w(a,c)+w(b,d)≥w(a,d)+w(b,c).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入收益函数的表达式，并设

𝐴=max𝑖∈[𝑎+1,𝑏]𝑎𝑖, 𝐵=max𝑖∈[𝑏+1,𝑐]𝑎𝑖, 𝐶=max𝑖∈[𝑐+1,𝑑]𝑎𝑖,A=maxi∈[a+1,b]ai, B=maxi∈[b+1,c]ai, C=maxi∈[c+1,d]ai,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则要证明的不等式可以写作

max{𝐴,𝐵}+max{𝐵,𝐶}≥max{𝐴,𝐵,𝐶}+𝐵.max{A,B}+max{B,C}≥max{A,B,C}+B.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到不等号左侧的两项 max{𝐴,𝐵}max{A,B}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 max{𝐵,𝐶}max{B,C}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中较大的那个就等于 max{𝐴,𝐵,𝐶}max{A,B,C}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而它们中较小的那个总是不小于 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此该不等式成立．

将种树问题转化为区间分拆问题后，只需要用 ST 表等方式预处理区间最值，可以单次 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 地计算单个区间的成本，就可以套用区间分拆问题的算法在 𝑂(𝑛log⁡𝑛log⁡𝐿)O(nlog⁡nlog⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑂(𝑛(𝑛 +𝑚))O(n(n+m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内解决该问题．该方法同样可以处理任意种树间隔的问题．

### 交换论证

组合优化问题中，证明价值函数的凸性常常会用到交换论证（exchange argument）．具体地说，就是从参数为 𝑚 −1m−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚 +1m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题的最优解出发，通过交换部分元素，构造出参数为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且价值不超过 (𝑣(𝑚 −1) +𝑣(𝑚 +1))/2(v(m−1)+v(m+1))/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的可行解，从而利用 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优性来证明凸性的论证方法．相较于凸优化的情形，组合优化问题中并不存在自然地构造两个解的「中间形态」的方法，因此，交换论证的应用通常具有一定的技巧性．

「边际成本递增」并不一定导致凸性

组合优化问题中，目标函数常常具有一些「边际成本递增」的性质，但是这并不必然导致凸性．一个典型的例子是 [[IOI 2005] Riv 河流](https://www.luogu.com.cn/problem/P3354)，该问题的链上版本是满足四边形不等式因而具有凸性的，但是树上版本存在凸性不成立的例子．

用于刻画「边际成本递增」的一个常见性质是函数的超模性（supermodularity）．对于有限集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集族 P𝑋PX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的函数 𝑓 :P𝑋 →𝐑f:PX→R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果它满足以下两条等价性质之一：

  1. （交叉小于包含）对于任何子集 𝐴,𝐵 ⊆𝑋A,B⊆X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑓(𝐴) +𝑓(𝐵) ≤𝑓(𝐴 ∪𝐵) +𝑓(𝐴 ∩𝐵)f(A)+f(B)≤f(A∪B)+f(A∩B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立；
  2. （边际成本递增）对于任何子集 𝐴 ⊆𝐵 ⊆𝑋A⊆B⊆X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以及 𝑥 ∈𝑋 ∖𝐵x∈X∖B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑓(𝐴 ∪{𝑥}) −𝑓(𝐴) ≤𝑓(𝐵 ∪{𝑥}) −𝑓(𝐵)f(A∪{x})−f(A)≤f(B∪{x})−f(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立；

就称函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 **超模的** （supermodular）．但是，超模函数作为目标函数的最优化问题中，价值函数

𝑣(𝑚)=min𝐴⊆𝑋𝑓(𝐴) subject to |𝐴|=𝑚v(m)=minA⊆Xf(A) subject to |A|=m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**未必** 是 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数．究其原因，就是从子集大小分别为 𝑚 −1m−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚 +1m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优解，一般来说是无法构造出子集大小为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且满足前述价值函数大小关系的可行解的．

交换论证提供了种树问题凸性的又一种证明方式．

凸性证明四

利用交换论证．设种 𝑚 −1m−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树和种 𝑚 +1m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树的最优方案分别由 {𝑥(𝑚−1)𝑖} ∈{0,1}𝑛{xi(m−1)}∈{0,1}n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 {𝑥(𝑚+1)𝑖} ∈{0,1}𝑛{xi(m+1)}∈{0,1}n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 给出，其中，取值为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示该坑位种了一棵树，取值为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示该坑位没有种树．定义序列 {𝑧𝑖} ∈{0, ±1}𝑛{zi}∈{0,±1}n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足

𝑧𝑖=𝑥(𝑚+1)𝑖−𝑥(𝑚−1)𝑖, 𝑖=1,⋯,𝑛.zi=xi(m+1)−xi(m−1), i=1,⋯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个序列标记了两个种树方案的差异．这一序列中取值为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置表示该坑位要么在两个方案中都种了一棵树，要么在两个方案中都没有种树；而取值为 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置则分别表示只在方案 𝑥(𝑚−1)x(m−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或只在方案 𝑥(𝑚+1)x(m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，该坑位种了一棵树．因为任何方案中都不能在相邻的坑位种树，所以有如下观察：

  * 连续的非零子段中，𝑧𝑖zi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值必然在 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间相互交错的；
  * 极大的连续非零子段左右两侧的 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必然表示在两个方案中都没有种树．

因此，如果某个极大的连续非零子段中，𝑧𝑖zi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的和恰好为 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，在该段坑位中，方案 𝑥(𝑚+1)x(m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比方案 𝑥(𝑚−1)x(m−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 多种了一棵树，那么就可以在该段内交换两个方案的种树位置．这样，就得到了两个各种 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树的可行方案．因为没有改变两个方案中总的种树的位置和数量，只是将它们重新分配，所以总的收益不变，仍然是 𝑣(𝑚 −1) +𝑣(𝑚 +1)v(m−1)+v(m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，这两个种 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树的方案未必是最优的，因此，它们各自的收益不会超过 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就证明了

𝑣(𝑚−1)+𝑣(𝑚+1)≤2𝑣(𝑚),v(m−1)+v(m+1)≤2v(m),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凹函数．

现在，只剩下一个问题，就是和恰好为 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极大连续非零子段是否存在．因为是若干个交错的 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相加，一个连续非零子段的和只能是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．又因为所有这些极大连续非零子段的和等于 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，一定存在至少两个和恰好为 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极大连续非零子段．这就完成了证明．

## 例题

本节介绍几个不同场景下应用 WQS 二分方法的例题．

### 模板题目

[Luogu P1484 种树](https://www.luogu.com.cn/problem/P1484)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个树坑，**至多** 种 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树．树不能栽种于相邻的两个坑．给定长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示在每个坑种树的收益，收益可正可负．求种完这 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树最大可能的收益和．

解答

与前文讨论的种树问题稍有不同，本题要求至多种 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树，而非恰好种 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树．仍然用 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示前文讨论的种树问题的价值函数，本题的答案实际上是 ˜𝑣(𝑚) =max𝑘≤𝑚𝑣(𝑘)v~(m)=maxk≤mv(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是凹函数，也就是一个单峰函数，本题的答案相当于只保留 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上升至峰顶的部分，然后函数会一直留在峰顶；这相当于仅仅保留切线斜率非负的部分．因此，本题与前文讨论的题目的唯一差别，就是 WQS 二分时，初始的斜率范围为 [0,max𝑖𝑎𝑖][0,maxiai]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而非 [min𝑖𝑎𝑖,max𝑖𝑎𝑖][miniai,maxiai]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

应用 WQS 二分的方法移除数量限制后，问题转化为计算链上最大权独立集，只是将原本的收益 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替换为了 {𝑎𝑖 +𝑘}{ai+k}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这是经典的动态规划题目．可以设 𝑓(𝑖,𝑗)f(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个坑位选择种树（𝑗 =1j=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）或不种树（𝑗 =0j=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）时，前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个树坑的子问题的最大收益．由此，可以写出状态转移方程为

𝑓(𝑖,0)=max{𝑓(𝑖−1,0),𝑓(𝑖−1,1)},𝑓(𝑖,1)=𝑓(𝑖−1,0)+𝑎𝑖+𝑘.f(i,0)=max{f(i−1,0),f(i−1,1)},f(i,1)=f(i−1,0)+ai+k.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

初始条件为 𝑓(0,0) =0f(0,0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(0,1) = −∞f(0,1)=−∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最终答案为 max{𝑓(𝑛,0),𝑓(𝑛,1)}max{f(n,0),f(n,1)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．单次计算复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，整体时间复杂度为 𝑂(𝑛log⁡𝐿)O(nlog⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝐿 =max𝑖|𝑎𝑖|L=maxi|ai|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考实现如下：

传统方法对偶方法

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 ``` |  ```text #include <algorithm> #include <cstring> #include <iostream> #include <tuple> #include <vector> int main () { int n , m ; std :: cin >> n >> m ; std :: vector < int > a ( n \+ 1 ); for ( int i = 1 ; i <= n ; ++ i ) std :: cin >> a [ i ]; // Calculate h(k) = max_x f(x) - k * g(x). // Meanwhile, obtain the maximum value g(x) of the optimizer x. auto calc = [ & ]( int k ) -> std :: pair < long long , int > { long long dp [ 2 ] = { 0 , -0x3f3f3f3f3f3f3f3f }; int opt [ 2 ] = { 0 , 0 }; for ( int i = 1 ; i <= n ; ++ i ) { long long tmp_dp [ 2 ]; int tmp_opt [ 2 ]; if ( dp [ 0 ] > dp [ 1 ]) { tmp_dp [ 0 ] = dp [ 0 ]; tmp_opt [ 0 ] = opt [ 0 ]; } else if ( dp [ 1 ] > dp [ 0 ]) { tmp_dp [ 0 ] = dp [ 1 ]; tmp_opt [ 0 ] = opt [ 1 ]; } else { tmp_dp [ 0 ] = dp [ 0 ]; tmp_opt [ 0 ] = std :: max ( opt [ 0 ], opt [ 1 ]); } tmp_dp [ 1 ] = dp [ 0 ] \+ a [ i ] \- k ; tmp_opt [ 1 ] = opt [ 0 ] \+ 1 ; std :: memcpy ( dp , tmp_dp , sizeof ( dp )); std :: memcpy ( opt , tmp_opt , sizeof ( opt )); } long long val ; int opt_m ; if ( dp [ 0 ] > dp [ 1 ]) { val = dp [ 0 ]; opt_m = opt [ 0 ]; } else if ( dp [ 1 ] > dp [ 0 ]) { val = dp [ 1 ]; opt_m = opt [ 1 ]; } else { val = dp [ 0 ]; opt_m = std :: max ( opt [ 0 ], opt [ 1 ]); } return { val , opt_m }; }; // WQS binary search. long long val , tar_val ; int opt_m , tar_k ; std :: tie ( val , opt_m ) = calc ( 0 ); if ( opt_m <= m ) { // Have already reached the peak. tar_k = 0 ; tar_val = val ; } else { // Find the maximum k such that g(x) >= m. int ll = 0 , rr = 1000000 ; while ( ll <= rr ) { int mm = ( ll \+ rr ) / 2 ; std :: tie ( val , opt_m ) = calc ( mm ); if ( opt_m >= m ) { tar_k = mm ; tar_val = val ; ll = mm \+ 1 ; } else { rr = mm \- 1 ; } } } long long res = tar_val \+ ( long long ) tar_k * m ; std :: cout << res << std :: endl ; return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 ``` |  ```text #include <algorithm> #include <iostream> #include <tuple> #include <type_traits> #include <vector> // Golden section search on integer domain (unimodal function) template < typename T , typename F > typename std :: enable_if < std :: is_integral < T >:: value , std :: pair < T , decltype ( std :: declval < F > ()( std :: declval < T > ())) >>:: type golden_section_search ( T ll , T rr , F func ) { constexpr long double phi = 0.618033988749894848204586834L ; T ml = ll \+ static_cast < T > (( rr \- ll ) * ( 1 \- phi )); T mr = ll \+ static_cast < T > (( rr \- ll ) * phi ); auto fl = func ( ml ), fr = func ( mr ); while ( ml < mr ) { if ( fl > fr ) { rr = mr ; mr = ml ; fr = fl ; ml = ll \+ static_cast < T > (( rr \- ll ) * ( 1 \- phi )); fl = func ( ml ); } else { ll = ml ; ml = mr ; fl = fr ; mr = ll \+ static_cast < T > (( rr \- ll ) * phi ); fr = func ( mr ); } } T best_x = ll ; auto best_val = func ( ll ); for ( T i = ll \+ 1 ; i <= rr ; ++ i ) { auto val = func ( i ); if ( val > best_val ) { best_val = val ; best_x = i ; } } return { best_x , best_val }; } int main () { int n , m ; std :: cin >> n >> m ; std :: vector < int > a ( n \+ 1 ); for ( int i = 1 ; i <= n ; ++ i ) std :: cin >> a [ i ]; // Calculate h(k) = max_x f(x) + k * g(x). auto calc = [ & ]( int k ) -> long long { long long dp [ 2 ] = { 0 , -0x3f3f3f3f3f3f3f3f }; for ( int i = 1 ; i <= n ; ++ i ) { std :: tie ( dp [ 0 ], dp [ 1 ]) = std :: make_pair ( std :: max ( dp [ 0 ], dp [ 1 ]), dp [ 0 ] \+ a [ i ] \+ k ); } return std :: max ( dp [ 0 ], dp [ 1 ]); }; // Solve the dual problem to find v(m). // Implemented as a minimization problem by adding negative signs. // Only consider tangent lines of negative slopes to ignore the part // of the curve after the peak. auto res = \- golden_section_search ( -1000000 , 0 , [ & ]( int k ) -> long long { return \- calc ( k ) \+ ( long long ) k * m ; }). second ; std :: cout << res << std :: endl ; return 0 ; } ```   
---|---  
  
[Luogu P2619 [国家集训队] Tree I](https://www.luogu.com.cn/problem/P2619)

给定一张带权无向连通图，每条边是黑色或白色．求恰有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条白边的生成树的最小权．

解答

首先，通过交换论证可以证明 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是凸函数．不妨假设所有边的边权各不相同：那些存在两边边权相同的情形，可以通过微扰使之变为边权各不相同的情形；然后只要令微扰的幅度趋近于零，就可以证明函数的凸性在极限情形——也就是存在两边边权相同的情形——仍然成立．证明的关键在于如下引理：4

引理

设 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是无向连通图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的两个生成树．对于任意 𝑒 ∈𝑆 ∖𝑇e∈S∖T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都存在至少一条边 𝑓 ∈𝑇 ∖𝑆f∈T∖S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑆 −𝑒 +𝑓S−e+f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇 −𝑓 +𝑒T−f+e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成树．

证明

设 𝑒 =(𝑢,𝑣)e=(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是树 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中连接 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的唯一一条路径．因为 𝑃 +𝑒P+e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是图 𝑇 +𝑒T+e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中唯一的环路，所以删掉 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的任何一条边 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以使得 𝑇 −𝑓 +𝑒T−f+e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一棵生成树．与此同时，图 𝑆 −𝑒S−e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是有两个连通分量的森林，它们的顶点集分别记作 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，只要选择边 𝑓 ∈𝑃f∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连通了 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就能保证 𝑆 −𝑒 +𝑓S−e+f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一棵生成树．这样的边 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是存在的，因为 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别属于 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连接了 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而且，𝑓 ∉𝑆f∉S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为图 𝑆 −𝑒S−e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并不是连通的．这就完成了证明．

设 𝑇𝑚−1Tm−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇𝑚+1Tm+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是白边数量分别为 𝑚 −1m−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚 +1m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小生成树．设 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑇𝑚+1 ∖𝑇𝑚−1Tm+1∖Tm−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一条白边，对它应用上述引理可知，存在边 𝑓 ∈𝑇𝑚−1 ∖𝑇𝑚+1f∈Tm−1∖Tm+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑇′ =𝑇𝑚+1 −𝑒 +𝑓T′=Tm+1−e+f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇″ =𝑇𝑚−1 +𝑒 −𝑓T″=Tm−1+e−f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是生成树．因为只是交换了一对边，所以，树 𝑇′T′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和树 𝑇″T″![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边权和仍然是 𝑣(𝑚 −1) +𝑣(𝑚 +1)v(m−1)+v(m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而，分两种情形讨论：

  * 如果 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一条黑边，那么，𝑇′T′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇″T″![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的白边数量都是 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．它们各自的边权和都不会小于 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就证明了 2𝑣(𝑚) ≤𝑣(𝑚 −1) +𝑣(𝑚 +1)2v(m)≤v(m−1)+v(m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是凸的．
  * 如果 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一条白边，那么，𝑇′T′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇″T″![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的白边数量分别是 𝑚 +1m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚 −1m−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以它们的边权和分别不小于 𝑣(𝑚 +1)v(m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣(𝑚 −1)v(m−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，上面已经说明，它们的边权和加在一起就等于 𝑣(𝑚 −1) +𝑣(𝑚 +1)v(m−1)+v(m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这说明，𝑇′T′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边权和就等于 𝑣(𝑚 +1)v(m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．将 𝑇′T′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑇𝑚+1Tm+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比较可知，𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边权必然相等．这与假设矛盾，所以该情形并不成立．

这就证明了 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数．

建立了函数 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸性后，就可以用 WQS 二分解决该问题．移除数量限制并将每条白边的权重都减去 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并求解最小生成树问题．为此，可以应用 [Kruskal 算法](../../../graph/mst/#kruskal-算法)．利用并查集维护连通性，算法的复杂度就是 𝑂(𝐸log⁡𝐸 +𝐸𝛼(𝑉))O(Elog⁡E+Eα(V))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为边数和顶点数，𝛼( ⋅)α(⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为反 Ackerman 函数．复杂度的主要部分 𝑂(𝐸log⁡𝐸)O(Elog⁡E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是给边排序的复杂度，在本题中可以进一步优化．虽然在 WQS 二分的过程中需要多次计算最小生成树，但是每次只有白边的边权会整体加减一个数．所以，可以在预处理时给白边、黑边分别排序，然后每次计算最小生成树时，只需要将调整完权重后的白边和黑边归并到一起就可以了．这样，整体复杂度就降低到了 𝑂(𝐸log⁡𝐸 +𝐸𝛼(𝑉)log⁡𝐿)O(Elog⁡E+Eα(V)log⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为边权的取值范围的长度．

参考实现如下：

传统方法对偶方法

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 ``` |  ```text #include <algorithm> #include <array> #include <iostream> #include <numeric> #include <tuple> #include <vector> class DisjointSet { std :: vector < int > fa , sz ; int find ( int x ) { return fa [ x ] == x ? x : fa [ x ] = find ( fa [ x ]); } public : DisjointSet ( int n ) : fa ( n ), sz ( n , 1 ) { std :: iota ( fa . begin (), fa . end (), 0 ); } bool unite ( int x , int y ) { x = find ( x ); y = find ( y ); if ( x == y ) return false ; if ( sz [ x ] < sz [ y ]) std :: swap ( x , y ); fa [ y ] = x ; sz [ x ] += sz [ y ]; return true ; } }; int main () { int V , E , m ; std :: cin >> V >> E >> m ; std :: array < std :: vector < std :: array < int , 3 >> , 2 > edges ; edges [ 0 ]. reserve ( E ); // white edges. edges [ 1 ]. reserve ( E ); // black edges. for ( int i = 0 ; i < E ; ++ i ) { int u , v , c , w ; std :: cin >> u >> v >> w >> c ; edges [ c ]. push_back ({ u , v , w }); } // Sort edges. std :: sort ( edges [ 0 ]. begin (), edges [ 0 ]. end (), [ & ]( const auto & lhs , const auto & rhs ) -> bool { return lhs [ 2 ] < rhs [ 2 ]; }); std :: sort ( edges [ 1 ]. begin (), edges [ 1 ]. end (), [ & ]( const auto & lhs , const auto & rhs ) -> bool { return lhs [ 2 ] < rhs [ 2 ]; }); // Calculate h(k) = min_x f(x) - k * g(x) by Kruskal algorithm. // Use white edges first, whenever possible. auto calc = [ & ]( int k ) -> std :: pair < int , int > { int res = 0 , cnt = 0 ; DisjointSet djs ( V ); int i [ 2 ] = {}; while ( i [ 0 ] < edges [ 0 ]. size () && i [ 1 ] < edges [ 1 ]. size ()) { int c = edges [ 0 ][ i [ 0 ]][ 2 ] \- k > edges [ 1 ][ i [ 1 ]][ 2 ]; if ( djs . unite ( edges [ c ][ i [ c ]][ 0 ], edges [ c ][ i [ c ]][ 1 ])) { res += edges [ c ][ i [ c ]][ 2 ] \- ( c ? 0 : k ); cnt += c ? 0 : 1 ; } ++ i [ c ]; } while ( i [ 0 ] < edges [ 0 ]. size ()) { if ( djs . unite ( edges [ 0 ][ i [ 0 ]][ 0 ], edges [ 0 ][ i [ 0 ]][ 1 ])) { res += edges [ 0 ][ i [ 0 ]][ 2 ] \- k ; ++ cnt ; } ++ i [ 0 ]; } while ( i [ 1 ] < edges [ 1 ]. size ()) { if ( djs . unite ( edges [ 1 ][ i [ 1 ]][ 0 ], edges [ 1 ][ i [ 1 ]][ 1 ])) { res += edges [ 1 ][ i [ 1 ]][ 2 ]; } ++ i [ 1 ]; } return { res , cnt }; }; // WQS binary search. // Find the minimum k such that g(x) >= m. int val , opt_m , tar_val , tar_k ; int ll = -100 , rr = 100 ; while ( ll <= rr ) { int mm = ll \+ ( rr \- ll ) / 2 ; std :: tie ( val , opt_m ) = calc ( mm ); if ( opt_m >= m ) { tar_val = val ; tar_k = mm ; rr = mm \- 1 ; } else { ll = mm \+ 1 ; } } int res = tar_val \+ tar_k * m ; std :: cout << res << std :: endl ; return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 ``` |  ```text #include <algorithm> #include <array> #include <iostream> #include <numeric> #include <tuple> #include <type_traits> #include <vector> // Golden section search on integer domain (unimodal function) template < typename T , typename F > typename std :: enable_if < std :: is_integral < T >:: value , std :: pair < T , decltype ( std :: declval < F > ()( std :: declval < T > ())) >>:: type golden_section_search ( T ll , T rr , F func ) { constexpr long double phi = 0.618033988749894848204586834L ; T ml = ll \+ static_cast < T > (( rr \- ll ) * ( 1 \- phi )); T mr = ll \+ static_cast < T > (( rr \- ll ) * phi ); auto fl = func ( ml ), fr = func ( mr ); while ( ml < mr ) { if ( fl > fr ) { rr = mr ; mr = ml ; fr = fl ; ml = ll \+ static_cast < T > (( rr \- ll ) * ( 1 \- phi )); fl = func ( ml ); } else { ll = ml ; ml = mr ; fl = fr ; mr = ll \+ static_cast < T > (( rr \- ll ) * phi ); fr = func ( mr ); } } T best_x = ll ; auto best_val = func ( ll ); for ( T i = ll \+ 1 ; i <= rr ; ++ i ) { auto val = func ( i ); if ( val > best_val ) { best_val = val ; best_x = i ; } } return { best_x , best_val }; } class DisjointSet { std :: vector < int > fa , sz ; int find ( int x ) { return fa [ x ] == x ? x : fa [ x ] = find ( fa [ x ]); } public : DisjointSet ( int n ) : fa ( n ), sz ( n , 1 ) { std :: iota ( fa . begin (), fa . end (), 0 ); } bool unite ( int x , int y ) { x = find ( x ); y = find ( y ); if ( x == y ) return false ; if ( sz [ x ] < sz [ y ]) std :: swap ( x , y ); fa [ y ] = x ; sz [ x ] += sz [ y ]; return true ; } }; int main () { int V , E , m ; std :: cin >> V >> E >> m ; std :: array < std :: vector < std :: array < int , 3 >> , 2 > edges ; edges [ 0 ]. reserve ( E ); // white edges. edges [ 1 ]. reserve ( E ); // black edges. for ( int i = 0 ; i < E ; ++ i ) { int u , v , c , w ; std :: cin >> u >> v >> w >> c ; edges [ c ]. push_back ({ u , v , w }); } // Sort edges. std :: sort ( edges [ 0 ]. begin (), edges [ 0 ]. end (), [ & ]( const auto & lhs , const auto & rhs ) -> bool { return lhs [ 2 ] < rhs [ 2 ]; }); std :: sort ( edges [ 1 ]. begin (), edges [ 1 ]. end (), [ & ]( const auto & lhs , const auto & rhs ) -> bool { return lhs [ 2 ] < rhs [ 2 ]; }); // Calculate h(k) = min_x f(x) - k * g(x) by Kruskal algorithm. auto calc = [ & ]( int k ) -> int { int res = 0 ; DisjointSet djs ( V ); int i [ 2 ] = {}; while ( i [ 0 ] < edges [ 0 ]. size () && i [ 1 ] < edges [ 1 ]. size ()) { int c = edges [ 0 ][ i [ 0 ]][ 2 ] \- k > edges [ 1 ][ i [ 1 ]][ 2 ]; if ( djs . unite ( edges [ c ][ i [ c ]][ 0 ], edges [ c ][ i [ c ]][ 1 ])) { res += edges [ c ][ i [ c ]][ 2 ] \- ( c ? 0 : k ); } ++ i [ c ]; } while ( i [ 0 ] < edges [ 0 ]. size ()) { if ( djs . unite ( edges [ 0 ][ i [ 0 ]][ 0 ], edges [ 0 ][ i [ 0 ]][ 1 ])) { res += edges [ 0 ][ i [ 0 ]][ 2 ] \- k ; } ++ i [ 0 ]; } while ( i [ 1 ] < edges [ 1 ]. size ()) { if ( djs . unite ( edges [ 1 ][ i [ 1 ]][ 0 ], edges [ 1 ][ i [ 1 ]][ 1 ])) { res += edges [ 1 ][ i [ 1 ]][ 2 ]; } ++ i [ 1 ]; } return res ; }; // Solve the dual problem to find v(m). auto res = golden_section_search ( -100 , 100 , [ & ]( int k ) -> int { return calc ( k ) \+ k * m ; }). second ; std :: cout << res << std :: endl ; return 0 ; } ```   
---|---  
  
### 区间分拆问题

[Luogu P6246 [IOI 2000] 邮局 加强版 加强版](https://www.luogu.com.cn/problem/P6246)

给定长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且递增的正整数序列 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示一条高速公路旁的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个村庄的位置，需要修建 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个邮局．邮局位置的选择，需要最小化所有村庄与其最近邮局的距离之和．求这个最小值．

解答

这是典型的 [区间分拆问题](../quadrangle/#区间分拆问题)．二分队列的实现细节请参考该页面．

每个邮局服务离它最近的村庄，那么，这些村庄必然是高速公路旁连续的若干个村庄．所以，修建 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个邮局，就相当于将所有村庄划分为连续的 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段，并为每一段村庄修建一个成本最低的邮局．众所周知，邮局应当修建在村庄位置的中位数的位置．由此，可以写出区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的成本函数为

𝑤(𝑙,𝑟)=𝑟∑𝑖=𝑙|𝑎𝑖−𝑎⌊(𝑙+𝑟)/2⌋|.w(l,r)=∑i=lr|ai−a⌊(l+r)/2⌋|.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它满足四边形不等式，因为它的二阶混合差分非正：

Δ𝑙Δ𝑟𝑤(𝑙,𝑟)=Δ𝑙(𝑎𝑟+1−𝑎⌊(𝑙+𝑟+1)/2⌋)=𝑎⌊(𝑙+𝑟+1)/2⌋−𝑎⌊(𝑙+𝑟+2)/2⌋≤0.ΔlΔrw(l,r)=Δl(ar+1−a⌊(l+r+1)/2⌋)=a⌊(l+r+1)/2⌋−a⌊(l+r+2)/2⌋≤0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这说明，可以通过二分队列结合 WQS 二分的方法在 𝑂(𝑛log⁡𝑛log⁡𝐿)O(nlog⁡nlog⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度内求解该问题．

参考实现如下：

传统方法对偶方法

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 ``` |  ```text #include <cmath> #include <deque> #include <iostream> #include <tuple> #include <type_traits> #include <vector> // Monotone decision DP. // This solves f(i) = min f(j-1) + w(j,i) s.t. 1 <= j <= i. // Also records the minimal optimal decision j for each f(i). template < typename W > std :: pair < std :: vector < decltype ( std :: declval < W > ()( 0 , 0 )) > , std :: vector < int >> monotone_decision_opt_dp ( int n , W ww ) { using ValueT = decltype ( std :: declval < W > ()( 0 , 0 )); std :: vector < ValueT > f ( n \+ 1 ); std :: vector < int > opt ( n \+ 1 ), lt ( n \+ 1 ), rt ( n \+ 1 ); std :: deque < int > dq ; auto w = [ & ]( int j , int i ) -> ValueT { return ww ( j , i ) \+ f [ j \- 1 ]; }; for ( int j = 1 ; j <= n ; ++ j ) { if ( ! dq . empty () && rt [ dq . front ()] < j ) dq . pop_front (); if ( ! dq . empty ()) lt [ dq . front ()] = j ; while ( ! dq . empty () && w ( j , lt [ dq . back ()]) < w ( dq . back (), lt [ dq . back ()])) { dq . pop_back (); } if ( dq . empty ()) { lt [ j ] = j ; rt [ j ] = n ; dq . emplace_back ( j ); } else if ( w ( j , rt [ dq . back ()]) >= w ( dq . back (), rt [ dq . back ()])) { if ( rt [ dq . back ()] < n ) { lt [ j ] = rt [ dq . back ()] \+ 1 ; rt [ j ] = n ; dq . emplace_back ( j ); } } else { int ll = lt [ dq . back ()], rr = rt [ dq . back ()], i = rr ; while ( ll <= rr ) { int mm = ( ll \+ rr ) / 2 ; if ( w ( j , mm ) < w ( dq . back (), mm )) { i = mm ; rr = mm \- 1 ; } else { ll = mm \+ 1 ; } } rt [ dq . back ()] = i \- 1 ; lt [ j ] = i ; rt [ j ] = n ; dq . emplace_back ( j ); } f [ j ] = w ( dq . front (), j ); opt [ j ] = dq . front (); } return { f , opt }; } int main () { int n , m ; std :: cin >> n >> m ; std :: vector < long long > a ( n \+ 1 ), ps ( n \+ 1 ); for ( int i = 1 ; i <= n ; ++ i ) { std :: cin >> a [ i ]; ps [ i ] = ps [ i \- 1 ] \+ a [ i ]; } // Cost function for interval [l,r]. auto w = [ & ]( int j , int i ) -> long long { int mm = j \+ ( i \- j ) / 2 ; return ps [ i ] \+ ps [ j \- 1 ] \- 2 * ps [ mm ] \+ ( 2 * mm \- j \- i \+ 1 ) * a [ mm ]; }; // Calculate h(k) = min_x f(x) - k * g(x). // Also record the minimum of optimal number of segments. auto calc = [ & ]( long long k ) -> std :: pair < long long , int > { auto res = monotone_decision_opt_dp ( n , [ & ]( int j , int i ) -> long long { return w ( j , i ) \- k ; }); auto val = res . first [ n ]; int cnt = 0 ; for ( int i = n ; i ; i = res . second [ i ] \- 1 ) { ++ cnt ; } return { val , cnt }; }; // WQS binary search. // Find the largest k such that g(x) <= m. long long val , tar_val ; int opt_m , tar_k ; long long ll = \- ( 1L L << 32 ), rr = 0 ; while ( ll <= rr ) { long long mm = ll \+ ( rr \- ll ) / 2 ; std :: tie ( val , opt_m ) = calc ( mm ); if ( opt_m <= m ) { tar_val = val ; tar_k = mm ; ll = mm \+ 1 ; } else { rr = mm \- 1 ; } } long long res = tar_val \+ ( long long ) tar_k * m ; std :: cout << res << std :: endl ; return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 ``` |  ```text #include <cmath> #include <deque> #include <iostream> #include <type_traits> #include <utility> #include <vector> // Monotone decision DP. // This solves f(i) = min f(j-1) + w(j,i) s.t. 1 <= j <= i. // Also records the minimal optimal decision j for each f(i). template < typename W > std :: pair < std :: vector < decltype ( std :: declval < W > ()( 0 , 0 )) > , std :: vector < int >> monotone_decision_opt_dp ( int n , W ww ) { using ValueT = decltype ( std :: declval < W > ()( 0 , 0 )); std :: vector < ValueT > f ( n \+ 1 ); std :: vector < int > opt ( n \+ 1 ), lt ( n \+ 1 ), rt ( n \+ 1 ); std :: deque < int > dq ; auto w = [ & ]( int j , int i ) -> ValueT { return ww ( j , i ) \+ f [ j \- 1 ]; }; for ( int j = 1 ; j <= n ; ++ j ) { if ( ! dq . empty () && rt [ dq . front ()] < j ) dq . pop_front (); if ( ! dq . empty ()) lt [ dq . front ()] = j ; while ( ! dq . empty () && w ( j , lt [ dq . back ()]) < w ( dq . back (), lt [ dq . back ()])) { dq . pop_back (); } if ( dq . empty ()) { lt [ j ] = j ; rt [ j ] = n ; dq . emplace_back ( j ); } else if ( w ( j , rt [ dq . back ()]) >= w ( dq . back (), rt [ dq . back ()])) { if ( rt [ dq . back ()] < n ) { lt [ j ] = rt [ dq . back ()] \+ 1 ; rt [ j ] = n ; dq . emplace_back ( j ); } } else { int ll = lt [ dq . back ()], rr = rt [ dq . back ()], i = rr ; while ( ll <= rr ) { int mm = ( ll \+ rr ) / 2 ; if ( w ( j , mm ) < w ( dq . back (), mm )) { i = mm ; rr = mm \- 1 ; } else { ll = mm \+ 1 ; } } rt [ dq . back ()] = i \- 1 ; lt [ j ] = i ; rt [ j ] = n ; dq . emplace_back ( j ); } f [ j ] = w ( dq . front (), j ); opt [ j ] = dq . front (); } return { f , opt }; } // Golden section search on integer domain (unimodal function) template < typename T , typename F > typename std :: enable_if < std :: is_integral < T >:: value , std :: pair < T , decltype ( std :: declval < F > ()( std :: declval < T > ())) >>:: type golden_section_search ( T ll , T rr , F func ) { constexpr long double phi = 0.618033988749894848204586834L ; T ml = ll \+ static_cast < T > (( rr \- ll ) * ( 1 \- phi )); T mr = ll \+ static_cast < T > (( rr \- ll ) * phi ); auto fl = func ( ml ), fr = func ( mr ); while ( ml < mr ) { if ( fl > fr ) { rr = mr ; mr = ml ; fr = fl ; ml = ll \+ static_cast < T > (( rr \- ll ) * ( 1 \- phi )); fl = func ( ml ); } else { ll = ml ; ml = mr ; fl = fr ; mr = ll \+ static_cast < T > (( rr \- ll ) * phi ); fr = func ( mr ); } } T best_x = ll ; auto best_val = func ( ll ); for ( T i = ll \+ 1 ; i <= rr ; ++ i ) { auto val = func ( i ); if ( val > best_val ) { best_val = val ; best_x = i ; } } return { best_x , best_val }; } int main () { int n , m ; std :: cin >> n >> m ; std :: vector < long long > a ( n \+ 1 ), ps ( n \+ 1 ); for ( int i = 1 ; i <= n ; ++ i ) { std :: cin >> a [ i ]; ps [ i ] = ps [ i \- 1 ] \+ a [ i ]; } // Cost function for interval [l,r]. auto w = [ & ]( int j , int i ) -> long long { int mm = j \+ ( i \- j ) / 2 ; return ps [ i ] \+ ps [ j \- 1 ] \- 2 * ps [ mm ] \+ ( 2 * mm \- j \- i \+ 1 ) * a [ mm ]; }; // Calculate h(k) = min_x f(x) - k * g(x). auto solve = [ & ]( long long k ) -> long long { return monotone_decision_opt_dp ( n , [ & ]( int j , int i ) -> long long { return w ( j , i ) \- k ; }) . first [ n ] \+ k * m ; }; // Solve the dual problem to find v(m). auto res = golden_section_search ( \- ( 1L L << 32 ), 0L L , solve ). second ; std :: cout << res << std :: endl ; return 0 ; } ```   
---|---  
  
### 二维的限制条件

[Codeforces 739 E. Gosha is hunting](https://codeforces.com/problemset/problem/739/E)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只神奇宝贝，序列 {𝑝𝑖}{pi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 {𝑞𝑖}{qi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别表示用宝贝球和超级球抓到第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只神奇宝贝的概率．可以向一个神奇宝贝扔一个宝贝球，或者扔一个超级球，或者两种球各扔一个，或者什么球都不扔．现有 𝑚1m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个宝贝球和 𝑚2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个神奇球，需要合理分配，并同时扔出．求抓到的神奇宝贝的期望数量的最大值．单次抓捕成功与否，与其它抓捕的结果无关．

更一般地，可以抽象为如下问题：

给定长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的三个正实数序列 {𝐴𝑖},{𝐵𝑖},{𝐶𝑖}{Ai},{Bi},{Ci}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而且，对所有 𝑖 =1,⋯,𝑛i=1,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 𝐶𝑖 ≤𝐴𝑖 +𝐵𝑖Ci≤Ai+Bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．求最优的下标集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 |𝑋| =𝑚1|X|=m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 |𝑌| =𝑚2|Y|=m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且最大化

∑𝑖∈𝑋∖𝑌𝐴𝑖+∑𝑖∈𝑌∖𝑋𝐵𝑖+∑𝑖∈𝑋∩𝑌𝐶𝑖.∑i∈X∖YAi+∑i∈Y∖XBi+∑i∈X∩YCi.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)解答

原问题可以看作是这个更一般的问题在

𝐴𝑖=𝑝𝑖, 𝐵𝑖=𝑞𝑖, 𝐶𝑖=𝑝𝑖+𝑞𝑖−𝑝𝑖𝑞𝑖Ai=pi, Bi=qi, Ci=pi+qi−piqi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时的特殊情形．因此，只需要讨论更一般的问题的解决方案就可以了．

用 𝑣(𝑚1,𝑚2)v(m1,m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示该问题的价值函数，需要证明它是关于 (𝑚1,𝑚2)(m1,m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凹函数．考虑如下费用流模型：

  * 从源点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，分别向结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条边，容量分别为 𝑚1m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，费用均为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 对于所有 𝑖 =1,⋯,𝑛i=1,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，分别从结点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向结点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条边，容量均为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，费用分别为 𝐴𝑖Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵𝑖Bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 对于所有 𝑖 =1,⋯,𝑛i=1,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从结点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发向汇点 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连两条边，容量均为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，费用分别为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐶𝑖 −𝐴𝑖 −𝐵𝑖Ci−Ai−Bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

问题的答案就是该费用流模型的最大费用最大流．条件 𝐶𝑖 −𝐴𝑖 −𝐵𝑖 ≤0Ci−Ai−Bi≤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 保证了当流经结点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的流量为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，会优先选择费用为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的那条边流出．将这个费用流模型写成线性规划问题，那么，𝑚1m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就会分别出现在表示边 (𝑠,𝑥)(s,x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和边 (𝑠,𝑦)(s,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的流量限制的不等式中．因此，𝑣(𝑚1,𝑚2)v(m1,m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 确实是 (𝑚1,𝑚2)(m1,m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凹函数．

为了应用 WQS 二分，需要考虑移除数量限制后的最优化问题．设 𝑘1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑘2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为将一个下标放入集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时获得的额外奖励．没有数量限制后，关于每个下标的决策都是独立的，因此，有

ℎ(𝑘1,𝑘2)=𝑛∑𝑖=1max{0,𝐴𝑖+𝑘1,𝐵𝑖+𝑘2,𝐶𝑖+𝑘1+𝑘2}.h(k1,k2)=∑i=1nmax{0,Ai+k1,Bi+k2,Ci+k1+k2}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

原问题的答案就由

𝑣(𝑚1,𝑚2)=min𝑘1,𝑘2ℎ(𝑘1,𝑘2)−𝑘1𝑚1−𝑘2𝑚2v(m1,m2)=mink1,k2h(k1,k2)−k1m1−k2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

给出．总的时间复杂度为 𝑂(𝑛log2⁡𝐿)O(nlog2⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑂(log⁡𝐿)O(log⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为对单个维度二分的次数．

抓捕神奇宝贝问题的参考实现如下：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 ``` |  ```text #include <algorithm> #include <iomanip> #include <iostream> #include <tuple> #include <type_traits> #include <vector> // Golden section search on floating-point domain (unimodal function) template < typename T , typename F > typename std :: enable_if < std :: is_floating_point < T >:: value , std :: pair < T , decltype ( std :: declval < F > ()( std :: declval < T > ())) >>:: type golden_section_search ( T ll , T rr , F func , T eps ) { constexpr long double phi = 0.618033988749894848204586834L ; T ml = ll \+ ( rr \- ll ) * ( 1 \- phi ); T mr = ll \+ ( rr \- ll ) * phi ; auto fl = func ( ml ), fr = func ( mr ); while (( rr \- ll ) > eps ) { if ( fl > fr ) { rr = mr ; mr = ml ; fr = fl ; ml = ll \+ ( rr \- ll ) * ( 1 \- phi ); fl = func ( ml ); } else { ll = ml ; ml = mr ; fl = fr ; mr = ll \+ ( rr \- ll ) * phi ; fr = func ( mr ); } } T mid = ( ll \+ rr ) / 2 ; return { mid , func ( mid )}; } int main () { int n , m1 , m2 ; std :: cin >> n >> m1 >> m2 ; std :: vector < long double > p ( n \+ 1 ), q ( n \+ 1 ); for ( int i = 1 ; i <= n ; ++ i ) std :: cin >> p [ i ]; for ( int i = 1 ; i <= n ; ++ i ) std :: cin >> q [ i ]; // Calculate h(k1,k2). auto solve = [ & ]( long double k1 , long double k2 ) -> long double { long double res = 0 ; for ( int i = 1 ; i <= n ; ++ i ) { res += std :: max ( { 0.0l , p [ i ] \+ k1 , q [ i ] \+ k2 , p [ i ] \+ q [ i ] \- p [ i ] * q [ i ] \+ k1 \+ k2 }); } return res ; }; // Solve the dual problem to find v(m1,m2). // Implemented as a minimization problem by adding negative signs. auto res = \- golden_section_search ( -1.0l , 0.0l , [ & ]( long double k1 ) -> long double { return golden_section_search ( -1.0l , 0.0l , [ & ]( long double k2 ) -> long double { return \- solve ( k1 , k2 ) \+ k2 * m2 ; }, 1e-8l ) . second \+ k1 * m1 ; }, 1e-8l ) . second ; std :: cout << std :: fixed << std :: setprecision ( 10 ) << res << std :: endl ; return 0 ; } ```   
---|---  
  
### 更广泛的限制条件

[Codeforces 1661 F. Teleporters](https://codeforces.com/problemset/problem/1661/F)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条线段，它们的长度由序列 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 给出．可以将它们任意切割为若干条整数长度的线段，目标是最小化所有线段长度平方的总和．求至少需要切割多少次，才能使这个平方和降到不超过 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答

设将长度为 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线段切割 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次能得到的最小平方和为 𝑓(𝑎,𝑚)f(a,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于均值不等式，当两数之和一定时，两数之差越小，两数的平方和也越小．所以，切割之后得到的线段长度越均匀，总的长度平方和也就越小．但是由于整数约束的存在，最均匀的情形就是得到了 𝑎mod(𝑚 +1)amod(m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条长度为 ⌈𝑎/(𝑚 +1)⌉⌈a/(m+1)⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线段和 𝑚 +1 −(𝑎mod(𝑚 +1))m+1−(amod(m+1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条长度为 ⌊𝑎/(𝑚 +1)⌋⌊a/(m+1)⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线段．因此，有如下表达式：

𝑓(𝑎,𝑚)=(𝑎mod(𝑚+1))⌈𝑎𝑚+1⌉2+(𝑚+1−(𝑎mod(𝑚+1)))⌊𝑎𝑚+1⌋2=(𝑎mod(𝑚+1))(⌊𝑎𝑚+1⌋+1)2+(𝑚+1−(𝑎mod(𝑚+1)))⌊𝑎𝑚+1⌋2.f(a,m)=(amod(m+1))⌈am+1⌉2+(m+1−(amod(m+1)))⌊am+1⌋2=(amod(m+1))(⌊am+1⌋+1)2+(m+1−(amod(m+1)))⌊am+1⌋2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

第二步的等号成立，是因为 ⌈𝑎/(𝑚 +1)⌉ ≠⌊𝑎/(𝑚 +1)⌋ +1⌈a/(m+1)⌉≠⌊a/(m+1)⌋+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当 𝑎mod(𝑚 +1) =0amod(m+1)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

可以证明，函数 𝑓(𝑎,𝑚)f(a,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸函数．为此，需要将它延拓到 𝑚 ∈𝐑+m∈R+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．当 ⌊𝑎/(𝑚 +1)⌋ =𝑞⌊a/(m+1)⌋=q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有

𝑓(𝑎,𝑚)=(𝑎−(𝑚+1)𝑞)(𝑞+1)2+((𝑚+1)(𝑞+1)−𝑎)𝑞2=𝑎(2𝑞+1)−𝑞(𝑞+1)(𝑚+1).f(a,m)=(a−(m+1)q)(q+1)2+((m+1)(q+1)−a)q2=a(2q+1)−q(q+1)(m+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是斜率为 −𝑞(𝑞 +1)−q(q+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的直线．因此，𝑓(𝑎,𝑚)f(a,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是分段线性函数，且斜率随着 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的增加而增加．这就说明了 𝑓(𝑎,𝑚)f(a,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是凸函数，它限制在整点上当然也是凸函数5．

利用 𝑓( ⋅, ⋅)f(⋅,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以将所有线段总共切割 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次得到的最小平方和写作如下最优化问题的价值函数：

𝑣(𝑚)=min{𝑚𝑖}∑𝑖𝑓(𝑎𝑖,𝑚𝑖) subject to ∑𝑖𝑚𝑖=𝑚, 𝑚𝑖∈𝐍.v(m)=min{mi}∑if(ai,mi) subject to ∑imi=m, mi∈N.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是若干个凸函数的 [卷积下确界](../slope-trick/#卷积下确界minkowski-和)，所以也是凸函数．如果题目要求的是 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，可以使用与之前的例题一致的方法求解，时间复杂度为 𝑂(𝑛log2⁡𝐿)O(nlog2⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；但是，本题求的是满足 𝑣(𝑚) ≤𝑉v(m)≤V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小的 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．利用 WQS 二分计算 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再对 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 二分的方法是行不通的，它的复杂度达到了 𝑂(𝑛log3⁡𝐿)O(nlog3⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．就本题而言，有如下两种处理方法．

**方法一** ：仍然二分斜率 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是二分的依据是对 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上下界的估计．

传统的 WQS 二分的方法中，对于给定的斜率 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以计算出相应的最优的 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值范围．因为这些 (𝑚,𝑣(𝑚))(m,v(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共线，所以这相当于确定了 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值范围．因此，可以直接二分斜率 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．得到斜率 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之后，可以利用直线方程

𝑣(𝑚)=ℎ(𝑘)+𝑘𝑚v(m)=h(k)+km![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

计算出最小的 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．整体复杂度为 𝑂(𝑛log2⁡𝐿)O(nlog2⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

为了确定 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值范围，需要确定 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值范围．一种做法是，在计算 ℎ(𝑘)h(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时记录相应的最大最优解，利用它可以计算相应的 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的下界；另一种做法是，利用 ℎ(𝑘) −ℎ(𝑘 −1)h(k)−h(k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到相应的 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的上界，进而得到相应的 𝑣(𝑚)v(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的下界．参考实现中，采用的是第二种做法，它不依赖于问题的具体结构，无需特别处理．

**方法二** ：改写最优化问题，使得对偶问题的价值函数就是本问题的解．

本问题可以直接看作是如下最优化问题：

𝑚(𝑣)=min{𝑚𝑖}∑𝑖𝑚𝑖 subject to ∑𝑖𝑓(𝑎𝑖,𝑚𝑖)≤𝑉.m(v)=min{mi}∑imi subject to ∑if(ai,mi)≤V.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

本文的分析仍然适用于这一问题．故而，可以利用它的对偶问题求解所要求的 𝑚(𝑣)m(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑚(𝑣)=max𝑘∑𝑖min𝑚𝑖(𝑚𝑖−𝜆𝑓(𝑎𝑖,𝑚𝑖))+𝜆𝑉.m(v)=maxk∑iminmi(mi−λf(ai,mi))+λV.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

整体算法复杂度仍然是 𝑂(𝑛log2⁡𝐿)O(nlog2⁡L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

参考代码如下：

方法一方法二

代码仅做示意，为通过原题数据范围，需要 128 位整数，并调整二分初始区间为 [0,1060][0,1060]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 ``` |  ```text #include <algorithm> #include <iostream> #include <tuple> #include <type_traits> #include <vector> // Golden section search on integer domain (unimodal function) template < typename T , typename F > typename std :: enable_if < std :: is_integral < T >:: value , std :: pair < T , decltype ( std :: declval < F > ()( std :: declval < T > ())) >>:: type golden_section_search ( T ll , T rr , F func ) { constexpr long double phi = 0.618033988749894848204586834L ; T ml = ll \+ static_cast < T > (( rr \- ll ) * ( 1 \- phi )); T mr = ll \+ static_cast < T > (( rr \- ll ) * phi ); auto fl = func ( ml ), fr = func ( mr ); while ( ml < mr ) { if ( fl > fr ) { rr = mr ; mr = ml ; fr = fl ; ml = ll \+ static_cast < T > (( rr \- ll ) * ( 1 \- phi )); fl = func ( ml ); } else { ll = ml ; ml = mr ; fl = fr ; mr = ll \+ static_cast < T > (( rr \- ll ) * phi ); fr = func ( mr ); } } T best_x = ll ; auto best_val = func ( ll ); for ( T i = ll \+ 1 ; i <= rr ; ++ i ) { auto val = func ( i ); if ( val > best_val ) { best_val = val ; best_x = i ; } } return { best_x , best_val }; } int main () { int n ; std :: cin >> n ; std :: vector < int > a ( n \+ 1 ); for ( int i = 1 ; i <= n ; ++ i ) std :: cin >> a [ i ]; for ( int i = n ; i >= 1 ; \-- i ) a [ i ] -= a [ i \- 1 ]; long long v ; std :: cin >> v ; // Cost of adding M more teleporters to a segment of length LEN. auto f = [ & ]( int len , int m ) -> long long { long long rem = len % ( m \+ 1 ); int q = len / ( m \+ 1 ); return ( m \+ 1 \- rem ) * q * q \+ rem * ( q \+ 1 ) * ( q \+ 1 ); }; // Calculate h(k) = min_x f(x) - k * g(x). auto calc = [ & ]( long long k ) -> long long { long long res = 0 ; for ( int i = 1 ; i <= n ; ++ i ) { res += \- golden_section_search ( 0 , a [ i ], [ & ]( int m ) -> long long { return \- f ( a [ i ], m ) \+ m * k ; }). second ; } return res ; }; // Find the smallest k such that h(k) + k * m <= v. long long ll = \- ( 1L L << 30 ), rr = 0 , ti = 0 ; while ( ll <= rr ) { auto mm = ll \+ ( rr \- ll ) / 2 ; auto fi = calc ( mm ); auto ub = fi \- calc ( mm \+ 1 ); if ( fi \+ ub * mm <= v ) { ti = mm ; rr = mm \- 1 ; } else { ll = mm \+ 1 ; } } std :: cout << ( int )(( calc ( ti ) \- v \- 1 \- ti ) / ( \- ti )) << std :: endl ; return 0 ; } ```   
---|---  
  
代码仅做示意，由于浮点数精度问题无法通过原题数据范围．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 ``` |  ```text #include <algorithm> #include <cmath> #include <iostream> #include <tuple> #include <type_traits> #include <vector> // Golden section search on integer domain (unimodal function) template < typename T , typename F > typename std :: enable_if < std :: is_integral < T >:: value , std :: pair < T , decltype ( std :: declval < F > ()( std :: declval < T > ())) >>:: type golden_section_search ( T ll , T rr , F func ) { constexpr long double phi = 0.618033988749894848204586834L ; T ml = ll \+ static_cast < T > (( rr \- ll ) * ( 1 \- phi )); T mr = ll \+ static_cast < T > (( rr \- ll ) * phi ); auto fl = func ( ml ), fr = func ( mr ); while ( ml < mr ) { if ( fl > fr ) { rr = mr ; mr = ml ; fr = fl ; ml = ll \+ static_cast < T > (( rr \- ll ) * ( 1 \- phi )); fl = func ( ml ); } else { ll = ml ; ml = mr ; fl = fr ; mr = ll \+ static_cast < T > (( rr \- ll ) * phi ); fr = func ( mr ); } } T best_x = ll ; auto best_val = func ( ll ); for ( T i = ll \+ 1 ; i <= rr ; ++ i ) { auto val = func ( i ); if ( val > best_val ) { best_val = val ; best_x = i ; } } return { best_x , best_val }; } // Golden section search on floating-point domain (unimodal function) template < typename T , typename F > typename std :: enable_if < std :: is_floating_point < T >:: value , std :: pair < T , decltype ( std :: declval < F > ()( std :: declval < T > ())) >>:: type golden_section_search ( T ll , T rr , F func , T eps ) { constexpr long double phi = 0.618033988749894848204586834L ; T ml = ll \+ ( rr \- ll ) * ( 1 \- phi ); T mr = ll \+ ( rr \- ll ) * phi ; auto fl = func ( ml ), fr = func ( mr ); while (( rr \- ll ) > eps ) { if ( fl > fr ) { rr = mr ; mr = ml ; fr = fl ; ml = ll \+ ( rr \- ll ) * ( 1 \- phi ); fl = func ( ml ); } else { ll = ml ; ml = mr ; fl = fr ; mr = ll \+ ( rr \- ll ) * phi ; fr = func ( mr ); } } T mid = ( ll \+ rr ) / 2 ; return { mid , func ( mid )}; } int main () { int n ; std :: cin >> n ; std :: vector < int > a ( n \+ 1 ); for ( int i = 1 ; i <= n ; ++ i ) std :: cin >> a [ i ]; for ( int i = n ; i >= 1 ; \-- i ) a [ i ] -= a [ i \- 1 ]; long long v ; std :: cin >> v ; // Cost of adding M more teleporters to a segment of length LEN. auto f = [ & ]( int len , int m ) -> long long { long long rem = len % ( m \+ 1 ); int q = len / ( m \+ 1 ); return ( m \+ 1 \- rem ) * q * q \+ rem * ( q \+ 1 ) * ( q \+ 1 ); }; // Calculate h(k) = min_x f(x) - k * g(x). auto calc = [ & ]( long double k ) -> long double { long double res = 0 ; for ( int i = 1 ; i <= n ; ++ i ) { res += \- golden_section_search ( 0 , a [ i ], [ & ]( int m ) -> long double { return \- m \+ k * f ( a [ i ], m ); }). second ; } return res ; }; // Solve the dual problem. auto res = golden_section_search ( -1.0l , 0.0l , [ & ]( long double k ) -> long double { return calc ( k ) \+ k * v ; }, 1e-12l ) . second ; std :: cout << ( int ) ceill ( res ) << std :: endl ; return 0 ; } ```   
---|---  
  
## 习题

最后，列举一些可以通过 WQS 二分解决的题目，以供练习：

  * [Luogu P1484 种树](https://www.luogu.com.cn/problem/P1484)
  * [Luogu P1792 [国家集训队] 种树](https://www.luogu.com.cn/problem/P1792)
  * [Luogu P2619 [国家集训队] Tree I](https://www.luogu.com.cn/problem/P2619)
  * [Luogu P3620 [APIO/CTSC2007] 数据备份](https://www.luogu.com.cn/problem/P3620)
  * [Luogu P4072 [SDOI2016] 征途](https://www.luogu.com.cn/problem/P4072)
  * [Luogu P4383 [八省联考 2018] 林克卡特树](https://www.luogu.com.cn/problem/P4383)
  * [Luogu P4983 忘情](https://www.luogu.com.cn/problem/P4983)
  * [Luogu P5308 [COCI 2018/2019 #4] Akvizna](https://www.luogu.com.cn/problem/P5308)
  * [Luogu P5633 最小度限制生成树](https://www.luogu.com.cn/problem/P5633)
  * [Luogu P5896 [IOI 2016] aliens](https://www.luogu.com.cn/problem/P5896)
  * [Luogu P6246 [IOI 2000] 邮局 加强版 加强版](https://www.luogu.com.cn/problem/P6246)
  * [AtCoder Beginner Contest 218 H - Red and Blue Lamps](https://atcoder.jp/contests/abc218/tasks/abc218_h)
  * [AtCoder Beginner Contest 305 Ex - Shojin](https://atcoder.jp/contests/abc305/tasks/abc305_h)
  * [AtCoder Regular Contest 164 E - Segment-Tree Optimization](https://atcoder.jp/contests/arc164/tasks/arc164_e)
  * [Codeforces 125 E. MST Company](https://codeforces.com/problemset/problem/125/E)
  * [Codeforces 321 E. Ciel and Gondolas](https://codeforces.com/problemset/problem/321/E)
  * [Codeforces 739 E. Gosha is hunting](https://codeforces.com/problemset/problem/739/E)
  * [Codeforces 802 O. April Fools' Problem (hard)](https://codeforces.com/contest/802/problem/O)
  * [Codeforces 958 E2. Guard Duty (medium)](https://codeforces.com/problemset/problem/958/E2)
  * [Codeforces 1279 F. New Year and Handle Change](https://codeforces.com/problemset/problem/1279/F)
  * [Codeforces 1661 F. Teleporters](https://codeforces.com/problemset/problem/1661/F)
  * [Codeforces 1799 F. Halve or Subtract](https://codeforces.com/problemset/problem/1799/F)
  * [2019 Summer Petrozavodsk Camp H. Honorable Mention](https://codeforces.com/gym/102331/problem/H)

## 参考资料与注释

  * [王钦石《浅析一类二分方法》](https://github.com/hzwer/shareOI/blob/master/%E5%9F%BA%E7%A1%80%E7%AE%97%E6%B3%95/%E6%B5%85%E6%9E%90%E4%B8%80%E7%B1%BB%E4%BA%8C%E5%88%86%E6%96%B9%E6%B3%95_%E7%8E%8B%E9%92%A6%E7%9F%B3.pdf)
  * [Theoretical grounds of lambda optimization by adamant - Codeforces blog](https://codeforces.com/blog/entry/98334)
  * [严谨的 WQS 二分方法 by YeahPotato - 洛谷博客](https://www.luogu.com.cn/article/vsffwrc3)
  * [【学习笔记】WQS 二分详解及常见理解误区解释 by ikrvxt - CSDN 博客](https://blog.csdn.net/Emm_Titan/article/details/124035796)
  * [Convex conjugate - Wikipedia](https://en.wikipedia.org/wiki/Convex_conjugate)
  * [Fenchel–Moreau theorem - Wikipedia](https://en.wikipedia.org/wiki/Fenchel%E2%80%93Moreau_theorem)
  * [Subderivative - Wikipedia](https://en.wikipedia.org/wiki/Subderivative)
  * [Boyd, Stephen P., and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004.](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
  * Papadimitriou, Christos H., and Kenneth Steiglitz. Combinatorial optimization: algorithms and complexity. Courier Corporation, 1998.
  * Conforti, Michele, Gérard Cornuéjols, and Giacomo Zambelli. Integer programming. Springer International Publishing, 2014.
  * Schrijver, Alexander. Combinatorial optimization: polyhedra and efficiency. Vol. 24, no. 2. Berlin: Springer, 2003.

* * *

  1. 实际问题中，𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能只能取到 𝐑𝑑Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的有限多个格点．此处实际需要的条件是，原问题的解 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以延拓为 𝐑𝑑Rd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的凸函数 ˜𝑣 :𝐑𝑑 →𝐑 ∪{ ±∞}v~:Rd→R∪{±∞}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 **可凸延拓的** （convex-extensible）．为行文方便，正文中仍然用 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示延拓后的函数．几何直观上，这相当于说点集 {(𝑦,𝑣(𝑦))}{(y,v(y))}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 全部都位于它们的凸包的下凸壳上．对于一维的情形，这一条件利用代数语言 [很容易刻画](../slope-trick/#离散点集上的凸函数)；但是，对于高维的情形，这稍微有些复杂，[这份讲义](https://kzmurota.fpark.tmu.ac.jp/paper/HIMSummerSchool15Murota.pdf) 中提供了一些简单的充分条件． ↩

  2. 定理中提供的条件看似比凸函数更强一些，但是，对于算法竞赛能够遇到的情形，特别是 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为有限集合时，仅强调凸函数就已经足够．由离散集合上的正常凸函数 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 延拓而来的函数 ˜𝑣v~![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然是下半连续的凸函数，因为有限多个点的凸包必然是闭凸包，而所谓下半连续的凸函数，就等价于它的上境图是闭凸包．至于正常凸函数中的「正常」一词，只要 𝑣(𝑦)v(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在至少一个点处取得有限值且是凸函数，就可以保证． ↩

  3. 最小生成树问题有两种常见的写成线性规划问题的 [方法](https://math.arizona.edu/~glickenstein/math443f14/golari.pdf)：子回路消除模型（subtour-elimination formulation）和基于割集的模型（cut-based formulation）．只有前一种建模方式能够保证得到的线性规划问题和原问题是等价的． ↩

  4. 这一引理对于一般的 [拟阵](../../../math/matroid/) 也是成立的．它称为 **对称基交换性质** （symmetric base-exchange property），相关资料可以参考 [Wikipedia 页面](https://en.wikipedia.org/wiki/Basis_of_a_matroid)．因此，本题关于凸性的结论可以推广到一般的拟阵上． ↩

  5. 当然，𝑓(𝑎,𝑚)f(a,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和它限制在整点上得到的函数的凸包并不相同，因为 𝑓(𝑎,𝑚)f(a,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能存在非整数位置处的极点．这说明，并不能将定义域为实数的 𝑓(𝑎,𝑚)f(a,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 直接用于本题的最优化问题中． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/dp/opt/wqs-binary-search.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/dp/opt/wqs-binary-search.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest), [HeRaNO](https://github.com/HeRaNO), [jyeric](https://github.com/jyeric), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
