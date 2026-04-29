# 随机化技巧 - OI Wiki

- Source: https://oi-wiki.org/misc/rand-technique/

# 随机化技巧

## 概述

前置知识：[随机函数](../random/) 和 [概率初步](../../math/probability/basic-conception/)

本文将对 OI/ICPC 中的随机化相关技巧做一个简单的分类，并对每个分类予以介绍．本文也将介绍一些在 OI/ICPC 中很少使用，但与 OI/ICPC 在风格等方面较为贴近的方法，这些内容前将用 `(*)` 标注．

这一分类并不代表广泛共识，也必定不能囊括所有可能性，因此仅供参考．

**记号和约定** ：

  * Pr[𝐴]Pr[A]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 发生的概率．
  * E[𝑋]E[X]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望．
  * 赋值号 :=:=![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示引入新的量，例如 𝑌 :=1926Y:=1926![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示引入值为 19261926![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的量 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 用随机集合覆盖目标元素

庞大的解空间中有一个（或多个）解是我们想要的．我们可以尝试进行多次撒网，只要有一次能够网住目标解就能成功．

### 例：三部图的判定

问题

给定一张 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点、𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边的简单无向图，用 RGB 三种颜色给每个结点染色 满足任意一对邻居都不同色，或者报告无解．

对每个点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从 {𝑅,𝐺,𝐵}{R,G,B}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中等概率独立随机地选一种颜色 𝐶𝑣Cv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并钦定 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **不** 被染成 𝐶𝑣Cv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．最优解恰好符合这些限制的概率，显然是 (23)𝑛(23)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在这些限制下，对于一对邻居 (𝑢,𝑣)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，「𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不同色」的要求等价于以下这条「推出」关系：

  * 对于所有异于 𝐶𝑢,𝐶𝑣Cu,Cv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的颜色 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被染成 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被染成 {𝑅,𝐺,𝐵} ∖{𝑋,𝐶𝑣}{R,G,B}∖{X,Cv}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

于是我们可以对每个 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 设置布尔变量 𝐵𝑣Bv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其取值表示 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被染成两种剩余的颜色中的哪一种．借助 2-SAT 模型即可以 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度解决这个问题．

这样做，单次的正确率是 (23)𝑛(23)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．将算法重复运行 −(32)𝑛log⁡𝜖−(32)nlog⁡ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，只要有一次得到解就输出，这样即可保证 1 −𝜖1−ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正确率．（详见后文中「概率上界的分析」）

* * *

**回顾** ：本题中「解空间」就是集合 {𝑅,𝐺,𝐵}𝑛{R,G,B}n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们每次通过随机施加限制来在一个缩小的范围内搜寻「目标解」——即合法的染色方案．

### 例：[CodeChef SELEDGE](https://www.codechef.com/problems/SELEDGE)

简要题意

给定一张点、边都有非负权值的无向图，找到一个大小 ≤𝐾≤K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以最大化与 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连的点的权值和减去 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边权和．一个点的权值只被计算一次．

观察：如果选出的边中有三条边构成一条链，则删掉中间的那条一定不劣；如果选出的边中有若干条构成环，则删掉任何一条一定不劣．

推论：最优解选出的边集，一定构成若干个不相交的菊花图（即直径不超过 2 的树）．

推论：最优解选出的边集，一定构成一张二分图．

我们对每个点等概率独立随机地染上黑白两种颜色之一，并要求这一染色方案，恰好也是最优解所对应的二分图的黑白染色方案．

尝试计算最优解符合这一要求的概率：

  * 考虑一张 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的菊花图，显然它有 2 种染色方案，所以它被染对颜色的概率是 22𝑛 =21−𝑛22n=21−n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 假设最优解中每个菊花的结点数分别为 𝑎1,⋯,𝑎𝑙a1,⋯,al![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则一定有 (𝑎1 −1) +⋯ +(𝑎𝑙 −1) ≤𝐾(a1−1)+⋯+(al−1)≤K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝐾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示最多能够选出的边数．
  * 从而所有菊花都被染对颜色的概率是 21−𝑎1⋯21−𝑎𝑙 ≥2−𝐾21−a1⋯21−al≥2−K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在上述要求下，尝试建立费用流模型计算最优答案：

  * 建立二分图，白点在左侧并与 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连，黑点在右侧并与 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连．
    * 对于白点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向它连一条容量为 1、费用为 −𝐴𝑣−Av![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边，和一条容量为 ∞∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、费用为 0 的边．
    * 对于黑点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从它向 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条容量为 1、费用为 −𝐴𝑣−Av![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边，和一条容量为 ∞∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、费用为 0 的边．
  * 对于原图中的边 (𝑢,𝑣,𝐵)(u,v,B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为白色、𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为黑色，连一条从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边，容量为 1，费用为 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 在该图中限制流量不超过 𝐾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则最小费用的相反数就是答案．

用 SPFA 费用流求解的话，复杂度是 𝑂(𝐾2(𝑛 +𝑚))O(K2(n+m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，证明：

  * 首先，显然 SPFA 的运行次数 ≤𝐾≤K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 然后，在一次 SPFA 中，任何一个结点至多入队 𝑂(𝐾)O(K)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．这是因为：
    * 任意时刻有流量的边不会超过 3𝐾3K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条，否则就意味着在原图中选了超过 𝐾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边．
    * 对于任何一条长为 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的增广路，其中至少有 𝐿2 −2L2−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边是某条有流量的边的反向边，因为正向边都是从图的左侧指向右侧，只有这些反向边才会从右侧指向左侧．
    * 综合以上两条，得到任意一条增广路的长度不超过 6𝐾 +46K+4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 综上，复杂度是 𝑂(𝐾2(𝑛 +𝑚))O(K2(n+m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

和上一题类似，我们需要把整个过程重复 −2𝐾log⁡𝜖−2Klog⁡ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次以得到 1 −𝜖1−ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正确率．总复杂度 𝑂(2𝐾𝐾2(𝑛 +𝑚) ⋅ −log⁡𝜖)O(2KK2(n+m)⋅−log⁡ϵ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 用随机元素命中目标集合

我们需要确定一个集合中的任意一个元素，为此我们随机选取元素，以期能够恰好命中这一集合．

### 例：[Gym 101550I](https://codeforces.com/gym/101550/attachments)

简要题意

有一张图形如：两条平行的链，加上连接两链的两条平行边．给定这张图上的若干条简单路径（每条路径表示一次通话），请你选择尽量少的边放置窃听器，以使得每条给定的路径上都有至少一个窃听器．

整张图可以拆分为一个环加上四条从环伸出去的链．对于这四条链中的任何一条（记作 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），考虑在这条链上如何放置窃听器，容易通过贪心算法得到满足以下条件的方案：

  * 在拦截所有 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内部进行的通话的前提下，用的窃听器数量最少．
  * 在上一条的前提下，使得 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的窃听器离环的最短距离尽可能小．
    * 作这一要求的目的是尽可能地拦截恰有一个端点在 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内部的通话．

接着考虑链与环相接处的共计 4 条边，我们暴力枚举这些边上有没有放窃听器．显然，如果想要拦截跨越链和环的通话，在这 4 条边上放窃听器一定是最优的．现在，我们可以把通话线路分为以下几种：

  1. 完全在链上的通话线路．这些线路一定已经被拦截，故可以忽略．
  2. 跨越链和环，且已经被拦截的通话线路．它们可以忽略．
  3. 跨越链和环，且未被拦截的通话线路．我们可以直接截掉它在链上的部分（因为链上的窃听器放置方案已经固定了），只保留环上的部分．
  4. 完全在环上的通话线路．

至此，问题转化成了环上的问题．

设最优解中在环上的边集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上放置了窃听器，如果我们已经确定了 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的任何一个元素 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以：

  * 先在 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处断环为链．
  * 然后从 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始贪心，不断找到下一个放置窃听器的边．注意到如果经过合适的预处理，贪心的每一步可以做到 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度．
  * 从而以 𝑂(|𝑆|)O(|S|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度解决问题．

我们考虑随机选取环上的一条边 𝑒′e′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并钦定 𝑒′ ∈𝑆e′∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再执行上述过程，重复多次取最优．

分析单次复杂度：

  * 观察：记 𝑆′S′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示所有选取了 𝑒′e′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方案中的最优解，则 |𝑆′| ≤|𝑆| +1|S′|≤|S|+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 从而单次复杂度 𝑂(|𝑆′|) =𝑂(|𝑆|)O(|S′|)=O(|S|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

分析正确率：

  * 显然单次正确率 |𝑆|𝑛|S|n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示环长．
  * 所以需要重复 −𝑛|𝑆|log⁡𝜖−n|S|log⁡ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次以得到 1 −𝜖1−ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正确率．

综上，该算法的复杂度 𝑂(|𝑆| ⋅ −𝑛|𝑆|log⁡𝜖) =𝑂( −𝑛log⁡𝜖)O(|S|⋅−n|S|log⁡ϵ)=O(−nlog⁡ϵ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 例：[CSES 1685 New Flight Routes](https://cses.fi/problemset/task/1685)

简要题意

给定一张有向图，请你加最少的边使得该图强连通，需 **输出方案** ．

先对原图进行强连通缩点．我们的目标显然是使每个汇点能到达每个源点．

不难证明，我们一定只会从汇点到源点连边，因为任何其他的连边，都能对应上一条不弱于它的、从汇点到源点的连边．

我们的一个核心操作是，取汇点 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和源点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（它们不必在同一个弱连通分量里），连边 𝑡 →𝑠t→s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 **使得 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都不再是汇点或源点**（记作目标 I）．理想情况下这种操作每次能减少一个汇点和一个源点，那我们不断操作直到只剩一个汇点或只剩一个源点，而这样的情形就很平凡了．由此，我们猜测答案是源点个数与汇点个数的较大值．

不难发现，上述操作能够达到目标 I 的充要条件是：𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拥有 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以外的前驱、且 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拥有 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以外的后继．可以证明（等会会给出证明），对于任意一张有着至少两个源点和至少两个汇点的 DAG，都存在这样的 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；但存在性的结论无法帮助我们构造方案，还需做其他分析．

  * 有了这个充要条件还难以直接得到算法，主要的原因是连边 𝑡 →𝑠t→s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后可能影响其他 (𝑠′,𝑡′)(s′,t′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 二元组的合法性，这个比较难处理．

注意到我们关于源汇点间的关系知之甚少（甚至连快速查询一对 𝑠 −𝑡s−t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 间是否可达都需要 dfs + bitset 预处理，而时限并不允许这么做），这提示我们需要某种非常一般和强大的性质．

观察：不满足目标 I 的 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至多有 𝑛 +𝑚 −1n+m−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对，其中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示源点个数，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示汇点个数．

  * 理由：对于每一对这样的 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若把它看成 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 间的一条边，则所有这些边构成的图形如若干条不相交的链，于是边数不超过点数减一．
  * 作出这一观察的动机是，要想将存在性结论应用于算法，前置步骤往往是把定性的结果加强为定量的结果．

推论：等概率随机选取 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足前述要求的概率 ≥(𝑛−1)(𝑚−1)𝑛𝑚≥(n−1)(m−1)nm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 注意到这个结论严格强于先前给出的存在性结论．

推论：等概率独立随机地连续选取 min(𝑛,𝑚)2min(n,m)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对不含公共元素的 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并对它们 **依次** 操作（即连边 𝑡 →𝑠t→s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），则这些操作全部满足目标 I 的概率 ≥14≥14![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 理由：

= (𝑛−1)(𝑚−1)𝑛𝑚⋅(𝑛−2)(𝑚−2)(𝑛−1)(𝑚−1)⋯(𝑛−𝑘)(𝑚−𝑘)(𝑛−𝑘+1)(𝑚−𝑘+1)=(𝑛−𝑘)(𝑚−𝑘)𝑛𝑚≥14= (n−1)(m−1)nm⋅(n−2)(m−2)(n−1)(m−1)⋯(n−k)(m−k)(n−k+1)(m−k+1)=(n−k)(m−k)nm≥14![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而连续选完 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后判断它们是否全部满足目标 I 很简单，只要再跑一遍强连通缩点，判断一下 𝑛,𝑚n,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否都减小了 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．注意到若每次减少 𝑘 =min(𝑛,𝑚)2k=min(n,m)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 min(𝑛,𝑚)min(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必在 𝑂(log⁡(𝑛+𝑚))O(log⁡(n+m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轮内变成 1，也就转化到了平凡的情况．

算法伪代码

```text 1 2 3 4 5 6 ``` |  ```text while(n>1 and m>1): randomly choose k=min(n,m)/2 pairs (s,t) add edge t->s for all these pairs if new_n>n-k or new_m>m-k: roll_back() solve_trivial() ```   
---|---  
  
复杂度 𝑂((|𝑉| +|𝐸|)log⁡|𝑉|)O((|V|+|E|)log⁡|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

* * *

**回顾** ：我们需要确定任意一对能够实现目标 I 的二元组 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，为此我们随机选择 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 用随机化获得随机数据的性质

如果一道题的数据随机生成，我们可能可以利用随机数据的性质解决它．而在有些情况下，即使数据并非随机生成，我们也可以通过随机化来给其赋予随机数据的某些特性，从而帮助解决问题．

### 例：随机增量法

随机生成的元素序列可能具有「前缀最优解变化次数期望下很小」等性质，而随机增量法就通过随机打乱输入的序列来获得这些性质．

详见 [随机增量法](../../geometry/random-incremental/)．

### 例：[TopCoder MagicMolecule](https://archive.topcoder.com/ProblemStatement/pm/11705) 随机化解法

简要题意

给定一张 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点、带点权的无向图，在其中所有大小不小于 2𝑛32n3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的团中，找到点权和最大的那个．

𝑛 ≤50n≤50![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

不难想到折半搜索．把点集均匀分成左右两半 𝑉𝐿,𝑉𝑅VL,VR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（大小都为 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），计算数组 𝑓𝐿,𝑘fL,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示点集 𝐿 ⊆𝑉𝐿L⊆VL![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的所有 ≥𝑘≥k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元团的最大权值和．接着我们枚举右半边的每个团 𝐶𝑅CR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，算出左半边有哪些点与 𝐶𝑅CR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的所有点相连（这个点集记作 𝑁𝐿NL![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），并用 𝑓𝑁𝐿,23𝑛−|𝐶𝑅| +𝑣𝑎𝑙𝑢𝑒(𝐶𝑅)fNL,23n−|CR|+value(CR)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更新答案．

  * 注意到可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移每一个 𝑓𝐿,𝑘fL,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．具体地说，取 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的任意一个元素，然后分类讨论：
    * 假设最优解中 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不在团中，则从 𝑓𝐿∖{𝑑},𝑘fL∖{d},k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移而来．
    * 假设最优解中 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在团中，则从 𝑓𝐿∩𝑁(𝑑),𝑘 +𝑣𝑎𝑙𝑢𝑒(𝑑)fL∩N(d),k+value(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转移而来，其中 𝑁(𝑑)N(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的邻居集合．
    * 别忘了还要用 𝑓𝐿,𝑘+1fL,k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来更新 𝑓𝐿,𝑘fL,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这个解法会超时．尝试优化：

  * 平分点集时均匀随机地划分．这样的话，最优解的点集 𝐶𝑟𝑒𝑠Cres![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以可观的概率也被恰好平分（即 |𝐶𝑟𝑒𝑠 ∩𝑉𝐿| =|𝐶𝑟𝑒𝑠 ∩𝑉𝑅||Cres∩VL|=|Cres∩VR|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．
    * 当然，|𝐶𝑟𝑒𝑠||Cres|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能是奇数．简单起见，这里假设它是偶数；奇数的情况对解法没有本质改变．
    * 实验发现，随机尝试约 20 次就能以很大概率有至少一次满足该性质．也就是说，如果我们的算法依赖于「𝐶𝑟𝑒𝑠Cres![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被平分」这一性质，则将算法重复执行 20 次取最优，同样也能保证以很大概率得到正确答案．
  * 有了这一性质，我们就可以直接钦定左侧团 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、右侧团 𝐶𝑅CR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小都 ≥𝑛3≥n3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这会对复杂度带来两处改进：
    * 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以省掉记录大小的维度．
    * 因为只需考虑大小 ≥𝑛3≥n3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的团，所以需要考虑的左侧团 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 右侧团 𝐶𝑅CR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量也大大减少至约 1.8 ⋅1061.8⋅106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 现在的瓶颈变成了求单侧的某一子集的权值和，因为这需要 𝑂(2|𝑉𝐿| +2|𝑉𝑅|)O(2|VL|+2|VR|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的预处理．
    * 解决方案：在 𝑉𝐿,𝑉𝑅VL,VR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内部再次折半；当查询一个子集的权值和时，将这个子集分成左右两半查询，再把答案相加．
  * 这样即可通过本题．

* * *

**回顾** ：一个随机的集合有着「在划分出的两半的数量差距不会太悬殊」这一性质，而我们通过随机划分获取了这个性质．

## 随机化用于哈希

### 例：[UOJ #207 共价大爷游长沙](https://uoj.ac/problem/207)

简要题意

维护一棵动态变化的树，和一个动态变化的结点二元组集合．你需要支持：

  * 删边、加边．保证得到的还是一棵树．
  * 加入/删除某个结点二元组．
  * 给定一条边 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，判断是否对于集合中的每个结点二元组 (𝑠,𝑡)(s,t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都在 𝑠,𝑡s,t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 间的简单路径上．

对图中的每条边 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们定义集合 𝑆𝑒Se![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示经过该边的关键路径（即题中的 (𝑎,𝑏)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）集合．考虑对每条边动态维护集合 𝑆𝑒Se![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的哈希值，这样就能轻松判定 𝑆𝑒Se![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否等于全集（即 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否是「必经之路」）．

哈希的方式是，对每个 (𝑎,𝑏)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 赋予 264264![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以内的随机非负整数 𝐻(𝑎,𝑏)H(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后一个集合的哈希值就是其中元素的 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值的异或和．

这样的话，任何一个固定的集合的哈希值一定服从 𝑅 :={0,1,⋯,264−1}R:={0,1,⋯,264−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的均匀分布（换句话说，哈希值的取值范围为 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且取每一个值的概率相等）．这是因为：

  1. 单个 𝐻(𝑎,𝑏)H(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 显然服从均匀分布．
  2. 两个独立且服从 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的均匀分布的随机变量的异或和，一定也服从 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的均匀分布．自证不难．

从而该算法的正确率是有保障的．

至于如何维护这个哈希值，使用 LCT 即可．

### 例：[CodeChef PANIC](https://www.codechef.com/problems/PANIC) 及其错误率分析

本题的大致解法：

  1. 可以证明3 𝑆(𝑁)S(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 服从一个关于 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑂(𝐾)O(K)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶线性递推式．
  2. 用 BM 算法求出该递推式．
  3. 借助递推式，用凯莱哈密顿定理计算出 𝑆(𝑁)S(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这里仅关注第二部分，即如何求一个矩阵序列的递推式．所以我们只需考虑下述问题：

问题

给定一个矩阵序列，该序列在模 𝑃 :=998244353P:=998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下服从一个齐次线性递推式（递推式中的数乘和加法运算定义为矩阵的数乘和加法），求出最短递推式．

如果一系列矩阵服从一个递推式 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么它的每一位也一定服从 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．然而，如果对某一位求出最短递推式 𝐹′F′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝐹′F′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能会比 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更短，从而产生问题．

解决方案：给矩阵的每一位 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 赋予一个 <𝑃<P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的随机权值 𝑥𝑖,𝑗xi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后对于序列中每个矩阵计算其所有位的加权和模 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结果，再把每个矩阵算出的这个数连成一个数列，最后我们对所得数列运行 BM 算法．

错误率分析：

  * 假设上述做法求得了不同于 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（且显然也不长于 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶递推式 𝐹′F′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 因为矩阵序列不服从 𝐹′F′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以一定存在矩阵中的某个位置 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足该位置对应的数列 𝑆𝑖,𝑗Si,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在某个 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处不服从 𝐹′F′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说：

𝑆(𝑁)𝑖,𝑗−𝐹′1𝑆(𝑁−1)𝑖,𝑗−⋯−𝐹′𝑙𝑆(𝑁−𝑙)𝑖,𝑗≢0(mod𝑃)S(N)i,j−F1′S(N−1)i,j−⋯−Fl′S(N−l)i,j≢0(modP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 假设 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是唯一的不服从的位置，则一定有：

𝑇𝑖,𝑗:=(𝑥𝑖,𝑗⋅(𝑆(𝑁)𝑖,𝑗−𝐹′1𝑆(𝑁−1)𝑖,𝑗−⋯−𝐹′𝑙𝑆(𝑁−𝑙)𝑖,𝑗)mod𝑃)=0Ti,j:=(xi,j⋅(S(N)i,j−F1′S(N−1)i,j−⋯−Fl′S(N−l)i,j)modP)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 显然这仅当 𝑥𝑖,𝑗 =0xi,j=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时才成立，概率 𝑃−1P−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 如果有多个不服从的位置呢？
    * 对每个这样的位置 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，易证 𝑇𝑖,𝑗Ti,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 服从 𝑅 :={0,1,⋯,𝑃 −1}R:={0,1,⋯,P−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的均匀分布．
    * 若干个互相独立的、服从 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的均匀分布的随机变量，它们在模意义下的和，依然服从 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的均匀分布．自证不难．
    * 从而这种情况下的错误率也是 𝑃−1P−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 例：[UOJ #552 同构判定鸭](https://uoj.ac/problem/552) 及其错误率分析

简要题意

给定两张边权为小写字母的有向图 𝐺0,𝐺1G0,G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，你要对这两张图分别算出「所有路径对应的字符串构成的多重集」（可能是无穷集），并判断这两个多重集是否相等．如果不相等，你要给出一个最短的串，满足它在两个多重集中的出现次数不相等．

令 𝑓𝐾,𝑖,𝑗fK,i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示图 𝐺𝐾GK![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中从点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始的所有长为 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径，这些路径对应的所有字符串构成的多重集的哈希值．按照 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 升序考虑每个状态，转移时枚举 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的出边并钦定该边为路径上的第一条边．

要判断是否存在长度 =𝐿=L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的坏串，只需把 {𝑓0,∗,𝐿}{f0,∗,L}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 {𝑓1,∗,𝐿}{f1,∗,L}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 各自「整合」起来再比较即可（通配符 `*` 这里表示每一个结点，例如 {𝑓0,∗,𝐿}{f0,∗,L}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示全体 𝑓0,𝑖,𝐿f0,i,L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成的集合，其中 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取遍所有结点）．官方题解1中证明了最短坏串（如果存在的话）长度一定不超过 𝑛1 +𝑛2n1+n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以这个解法的复杂度是可靠的．

接下来考虑具体的哈希方式．注意到常规的哈希方法——即把串 𝑎1𝑎2⋯𝑎𝑘a1a2⋯ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 映射到 (𝑎1 +𝑃𝑎2 +𝑃2𝑎3 +⋯ +𝑃𝑘−1𝑎𝑘)mod𝑄(a1+Pa2+P2a3+⋯+Pk−1ak)modQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上、再把多重集的哈希值定为其中元素的哈希值之和模 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)——在这里是行不通的．一个反例是，集合 `{"ab","cd"}` 与集合 `{"cb","ad"}` 的哈希值是一样的，不论 𝑃,𝑄P,Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 如何取值．

上述做法的问题在于，一个串的哈希值是一个和式，从而其中的每一项可以拆出来并重组．为避免这一问题，我们考虑把哈希值改为一个连乘式．此外，乘法交换律会使得不同的位不可区分，为避免这一点我们要为不同的位赋予不同的权值．

对每一个二元组 (𝑐,𝑗)(c,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（其中 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为字符，𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为整数表示 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在某个串中的第几位）我们都预先生成一个随机数 𝑥𝑐,𝑗xc,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．然后我们把串 𝑎1𝑎2⋯𝑎𝑘a1a2⋯ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 映射到 𝑥𝑎1,1𝑥𝑎2,2⋯𝑥𝑎𝑘,𝑘mod𝑄xa1,1xa2,2⋯xak,kmodQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上（其中 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **随机选取** 的质数）、再把多重集的哈希值定为其中元素的哈希值之和模 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．接下来分析它的错误率．

(*)Schwartz–Zippel 引理

令 𝑓 ∈𝐹[𝑧1,⋯,𝑧𝑘]f∈F[z1,⋯,zk]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为域 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次非零多项式，令 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有限子集，则至多有 𝑑 ⋅|𝑆|𝑘−1d⋅|S|k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组 (𝑧1,⋯,𝑧𝑘) ∈𝑆𝑘(z1,⋯,zk)∈Sk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑓(𝑧1,⋯,𝑧𝑘) =0f(z1,⋯,zk)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如果你不知道域是什么

你只需记得这两样东西都是域：

  1. 模质数的剩余系，以及其上的各种运算．
  2. 实数集，以及其上的各种运算．

推论：若 𝑧1,⋯,𝑧𝑘z1,⋯,zk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都在 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中等概率独立随机选取，则 Pr[𝑓(𝑧1,⋯,𝑧𝑘) =0] ≤𝑑|𝑆|Pr[f(z1,⋯,zk)=0]≤d|S|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

记 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为模 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的剩余系所对应的域，则对于一个 𝐿 ≤𝑛1 +𝑛2L≤n1+n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，∑𝑖𝑓0,𝑖,𝐿∑if0,i,L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ∑𝑖𝑓1,𝑖,𝐿∑if1,i,L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就分别对应着一个 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上关于变元集合 {𝑥∗,∗}{x∗,∗}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次多元多项式，不妨将这两个多项式记为 𝑃0,𝑃1P0,P1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

假如两个不同的字符串多重集的哈希值相同，则有两种可能：

  1. 𝑃0 ≡𝑃1(mod𝑄)P0≡P1(modQ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑃0,𝑃1P0,P1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每一项系数在模 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下都对应相等．
  2. 𝑃0 ≢𝑃1(mod𝑄),𝑃0(𝑥∗,∗) ≡𝑃1(𝑥∗,∗)(mod𝑄)P0≢P1(modQ),P0(x∗,∗)≡P1(x∗,∗)(modQ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑃0,𝑃1P0,P1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 虽然不恒等，但我们选取的这一组 {𝑥∗,∗}{x∗,∗}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 恰好使得它们在此处的点值相等．

分析前者发生的概率：

  * 观察：对于任意的 𝐴 ≠𝐵;𝐴,𝐵 ≤𝑁A≠B;A,B≤N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和随机选取的质数 𝑄 ≤𝑄maxQ≤Qmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一定有：

Pr[𝐴≡𝐵(mod𝑄)]=𝑂(log⁡𝑁log⁡𝑄𝑚𝑎𝑥𝑄𝑚𝑎𝑥)Pr[A≡B(modQ)]=O(log⁡Nlog⁡QmaxQmax)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 这是因为：使 𝐴 ≡𝐵A≡B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立的 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定满足 𝑄∣(𝐴 −𝐵)Q|(A−B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样的 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝜔(𝐴 −𝐵) ≤log2⁡𝑁ω(A−B)≤log2⁡N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个；而由质数定理，𝑄maxQmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以内不同的质数又有 Θ(𝑄maxlog⁡𝑄max)Θ(Qmaxlog⁡Qmax)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．将两者相除即可得到上式．
  * 在上述观察中取 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（满足 𝐴 ≠𝐵A≠B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）为某一特定项在 𝑃0,𝑃1P0,P1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的系数（也就等于该项对应的串在 𝐺0,𝐺1G0,G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的出现次数），则易见 𝐴,𝐵 ≤(𝑚1 +𝑚2)𝐿A,B≤(m1+m2)L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得到：

Pr[𝐴≡𝐵(mod𝑄)]=𝑂(𝐿log⁡(𝑚1+𝑚2)log⁡𝑄𝑚𝑎𝑥𝑄𝑚𝑎𝑥)Pr[A≡B(modQ)]=O(Llog⁡(m1+m2)log⁡QmaxQmax)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 所以取 𝑄max ≈1012Qmax≈1012![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就绰绰有余．如果机器无法支持这么大的整数运算，可以用双哈希代替．

分析后者发生的概率：

  * 在 Schwartz–Zippel 引理中：
    * 取域 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为模 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的剩余系对应的域
    * 取 𝑓(𝑥∗,∗) =𝑃0(𝑥∗,∗) −𝑃1(𝑥∗,∗)f(x∗,∗)=P0(x∗,∗)−P1(x∗,∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次非零多项式
    * 取 𝑆 =𝐹S=F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 得到：所求概率 ≤𝐿𝑄≤LQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意到我们需要对每个 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都能保证正确性，所以要想保证严谨的话还需用 Union Bound（见后文）说明一下．

实践上我们不必随机选取模数，因为——比如说——用自己的生日做模数的话，实际上已经相当于随机数了．

### 例：（*）子矩阵不同元素个数

问题

给定 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵，𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次询问一个连续子矩阵中不同元素的个数，要求在线算法．

允许 𝜖ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的相对误差和 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的错误率，换句话说，你要对至少 (1 −𝛿)𝑞(1−δ)q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个询问给出离正确答案相对误差不超过 𝜖ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的回答．

𝑛 ⋅𝑚 ≤2 ⋅105;𝑞 ≤106;𝜖 =0.5,𝛿 =0.2n⋅m≤2⋅105;q≤106;ϵ=0.5,δ=0.2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

引理：令 𝑋1⋯𝑘X1⋯k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为互相独立的随机变量，且取值在 [0,1][0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中均匀分布，则 E[min𝑖𝑋𝑖] =1𝑘+1E[miniXi]=1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 证明：考虑一个单位圆，其上分布着 **相对位置** 均匀随机的 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，分别在位置 0,𝑋1,𝑋2,⋯,𝑋𝑘0,X1,X2,⋯,Xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处．那么 min𝑖𝑋𝑖miniXi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就等于 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段空隙中特定的一段的长度．而因为这些空隙之间是「对称」的，所以其中任何一段特定空隙的期望长度都是 1𝑘+11k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为不同元素的个数，并借助上述引理来从 min𝑖𝑋𝑖miniXi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 反推得到 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑采用某个哈希函数，将矩阵中每个元素都均匀、独立地随机映射到 [0,1][0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的实数上去，且相等的元素会映射到相等的实数．这样的话，一个子矩阵中的所有元素对应的那些实数，在去重后就恰好是先前的集合 {𝑋1,⋯,𝑋𝑘}{X1,⋯,Xk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个实例，其中 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等于子矩阵中不同元素的个数．

于是我们得到了算法：

  1. 给矩阵中元素赋 [0,1][0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的哈希值．为保证随机性，哈希函数可以直接用 `map` 和随机数生成器实现，即每遇到一个新的未出现过的值就给它随机一个哈希值．
  2. 回答询问时设法求出子矩阵中哈希值的最小值 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并输出 1𝑀 −11M−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

然而，这个算法并不能令人满意．它的输出值的期望是 E[1min𝑖𝑋𝑖 −1]E[1miniXi−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但事实上这个值并不等于 1E[min𝑖𝑋𝑖] −1 =𝑘1E[miniXi]−1=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而（可以证明）等于 ∞∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

也就是说，我们不能直接把 min𝑖𝑋𝑖miniXi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的单次取值放在分母上，而要先算得它的期望，再把期望值放在分母上．

怎么算期望值？多次随机取平均．

我们用 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组不同的哈希函数分别执行前述过程，回答询问时计算出 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同的 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值，并算出其平均数 ―――𝑀M―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后输出 (―――𝑀)−1 −1(M―)−1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实验发现取 𝐶 ≈80C≈80![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可满足要求．严格证明十分繁琐，在此略去．

最后，怎么求子矩阵最小值？用二维 S-T 表即可，预处理 𝑂(𝑛𝑚log⁡𝑛log⁡𝑚)O(nmlog⁡nlog⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，回答询问 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 随机化在算法中的其他应用

随机化的其他作用还包括：

  * 防止被造数据者用针对性数据卡掉．例如在搜索时随机打乱邻居的顺序．
  * 保证算法过程中进行的「操作」具有（某种意义上的）均匀性．例如 [模拟退火](../simulated-annealing/) 算法．

在这些场景下，随机化常常（但并不总是）与乱搞、骗分等做法挂钩．

### 例：[「TJOI2015」线性代数](https://loj.ac/problem/2100)

本题的标准算法是网络流，但这里我们采取这样的乱搞做法：

  * 每次随机一个位置，把这个位置取反，判断大小并更新答案．

代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` |  ```text #include <algorithm> #include <cstdlib> #include <iostream> int n ; int a [ 510 ], b [ 510 ], c [ 510 ][ 510 ], d [ 510 ]; int p [ 510 ], q [ 510 ]; int maxans = 0 ; void check () { memset ( d , 0 , sizeof d ); int nowans = 0 ; for ( int i = 1 ; i <= n ; i ++ ) for ( int j = 1 ; j <= n ; j ++ ) d [ i ] += a [ j ] * c [ i ][ j ]; for ( int i = 1 ; i <= n ; i ++ ) nowans += ( d [ i ] \- b [ i ]) * a [ i ]; maxans = std :: max ( maxans , nowans ); } int main () { srand ( 19260817 ); std :: cin >> n ; for ( int i = 1 ; i <= n ; i ++ ) for ( int j = 1 ; j <= n ; j ++ ) std :: cin >> c [ i ][ j ]; for ( int i = 1 ; i <= n ; i ++ ) std :: cin >> b [ i ]; for ( int i = 1 ; i <= n ; i ++ ) a [ i ] = 1 ; check (); for ( int T = 1000 ; T ; T \-- ) { int tmp = rand () % n \+ 1 ; a [ tmp ] ^= 1 ; check (); } std :: cout << maxans << '\n' ; } ```   
---|---  
  
### 例：（*）随机堆2

可并堆最常用的写法应该是左偏树了，通过维护树高让树左偏来保证合并的复杂度．然而维护树高有点麻烦，我们希望尽量避开．

那么可以考虑使用随机堆，即不按照树高来交换儿子，而是随机交换．

代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text struct Node { int child [ 2 ]; long long val ; } nd [ 100010 ]; int root [ 100010 ]; int merge ( int u , int v ) { if ( ! ( u && v )) return u | v ; int x = rand () & 1 , p = nd [ u ]. val > nd [ v ]. val ? u : v ; nd [ p ]. child [ x ] = merge ( nd [ p ]. child [ x ], u \+ v \- p ); return p ; } void pop ( int & now ) { now = merge ( nd [ now ]. child [ 0 ], nd [ now ]. child [ 1 ]); } ```   
---|---  
  
随机堆对堆的形态没有任何硬性或软性的要求，合并操作的期望复杂度对任何两个堆（作为 `merge` 函数的参数）都成立．下证．

期望复杂度的证明

将证，对于任意的堆 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从根节点开始每次随机选左或者右走下去（直到无路可走），路径长度（即路径上的结点数）的期望值 ℎ(𝐴) ≤log2⁡(|𝐴| +1)h(A)≤log2⁡(|A|+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 注意到在前述过程中合并堆 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望复杂度是 𝑂(ℎ(𝐴) +ℎ(𝐵))O(h(A)+h(B))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，所以上述结论可以保证随机堆的期望复杂度．

证明采用数学归纳．边界情况是 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为空图，此时显然．下设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非空．

假设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的两个子树分别为 𝐿,𝑅L,R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则：

ℎ(𝐴)=1+ℎ(𝐿)+ℎ(𝑅)2≤1+log2⁡(|𝐿|+1)+log2⁡(|𝑅|+1)2=log2⁡2√(|𝐿|+1)(|𝑅|+1)≤log2⁡2((|𝐿|+1)+(|𝑅|+1))2=log2⁡(|𝐴|+1)h(A)=1+h(L)+h(R)2≤1+log2⁡(|L|+1)+log2⁡(|R|+1)2=log2⁡2(|L|+1)(|R|+1)≤log2⁡2((|L|+1)+(|R|+1))2=log2⁡(|A|+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证毕．

## 与随机性有关的证明技巧

以下列举几个比较有用的技巧．

自然，这寥寥几项不可能就是全部；如果你了解某种没有列出的技巧，那么欢迎补充．

### 概率上界的分析

详见 [概率不等式](../../math/probability/concentration-inequality/) 页面．

除了上述页面中提到的各种不等式外，推导过程中还经常会用到以下结论：

**自然常数的使用** ：(1 −1𝑛)𝑛 ≤1e,∀𝑛 ≥1(1−1n)n≤1e,∀n≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 左式关于 𝑛 ≥1n≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单调递增且在 +∞+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的极限是 1e1e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此有这个结论．
  * 这告诉我们，如果 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个互相独立的事件，每个的发生概率为 1 −1𝑛1−1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则它们全部发生的概率至多为 1e1e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 「耦合」思想

「耦合」思想常用于同时处理超过一个有随机性的对象，或者同时处理随机的对象和确定性的对象．

#### 引子：随机图的连通性

问题

对于 𝑛 ∈𝐍∗;𝑝,𝑞 ∈[0,1]n∈N∗;p,q∈[0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑞 ≤𝑝q≤p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求证：随机图 𝐺1(𝑛,𝑝)G1(n,p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连通分量个数的期望值不超过随机图 𝐺2(𝑛,𝑞)G2(n,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连通分量个数的期望值．这里 𝐺(𝑛,𝛼)G(n,α)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示一张 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点的简单无向图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑛(𝑛−1)2n(n−1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条可能的边中的每一条都有 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率出现，且这些概率互相独立．

这个结论看起来再自然不过，但严格证明却并不那么容易．

证明思路

我们假想这两张图分别使用了一个 01 随机数生成器来获知每条边存在与否，其中 𝐺1G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成器 𝑇1T1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 每次以 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率输出 1，𝐺2G2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成器 𝑇2T2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 每次以 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率输出 1．这样，要构造一张图，就只需把对应的生成器运行 𝑛(𝑛−1)2n(n−1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍即可．

现在我们把两个生成器合二为一．考虑随机数生成器 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每次以 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率输出 0，以 𝑝 −𝑞p−q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率输出 1，以 1 −𝑝1−p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率输出 2．如果我们将这个 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 运行 𝑛(𝑛−1)2n(n−1)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍，就能同时构造出 𝐺1G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺2G2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．具体地说，如果输出是 0，则认为 𝐺1G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺2G2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中都没有当前考虑的边；如果输出是 1，则认为只有 𝐺1G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中有当前考虑的边；如果输出是 2，则认为 𝐺1G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺2G2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中都有当前考虑的边．

容易验证，这样生成的 𝐺1G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺2G2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符合其定义，而且在每个实例中，𝐺2G2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边集都是 𝐺1G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边集的子集．因此在每个实例中，𝐺2G2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连通分量个数都不小于 𝐺1G1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连通分量个数；那么期望值自然也满足同样的大小关系．

这一段证明中用到的思想被称为「耦合」，可以从字面意思来理解这种思想．本例中它体现为把两个本来独立的随机过程合二为一．

#### 应用：[NERC 2019 Problem G: Game Relics](https://codeforces.com/contest/1267/problem/G)

简要题意

有若干个物品，每个物品有一个价格 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．你想要获得所有物品，为此你可以任意地进行两种操作：

  1. 选择一个未拥有的物品 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，花 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块钱买下来．
  2. 花 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块钱从所有物品（包括已经拥有的）中等概率随机抽取一个．如果尚未拥有该物品，则直接获得它；否则一无所获，但是会返还 𝑥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块钱．𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为输入的常数．

问最优策略下的期望花费．

观察：如果选择抽物品，就一定会一直抽直到获得新物品为止．

  * 理由：如果抽一次没有获得新物品，则新的局面和抽物品之前的局面一模一样，所以如果旧局面的最优行动是「抽一发」，则新局面的最优行动一定也是「再抽一发」．

我们可以计算出 𝑓𝑘fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示：如果当前已经拥有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同物品，则期望要花多少钱才能抽到新物品．根据刚才的观察，我们可以直接把 𝑓𝑘fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当作一个固定的代价，即转化为「每次花 𝑓𝑘fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块钱随机获得一个新物品」．

期望代价的计算

显然 𝑓𝑘 =𝑥2 ⋅(𝑅 −1) +𝑥fk=x2⋅(R−1)+x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示要得到新物品期望的抽取次数．

引理：如果一枚硬币有 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率掷出正面，则首次掷出正面所需的期望次数为 1𝑝1p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 感性理解：1𝑝 ⋅𝑝 =11p⋅p=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以扔这么多次期望得到 1 次正面，看起来就比较对．
  * 这种感性理解可以通过 [大数定律](https://en.wikipedia.org/wiki/Law_of_large_numbers) 严谨化，即考虑 𝑛 →∞n→∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次「不断抛硬币直到得到正面」的实验．推导细节略．
  * 另一种可行的证法是，直接把期望的定义带进去暴算．推导细节略．

显然抽一次得到新物品的概率是 𝑛−𝑘𝑛n−kn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑅 =𝑛𝑛−𝑘R=nn−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

结论：最优策略一定是先抽若干次，再买掉所有没抽到的物品．

这个结论符合直觉，因为 𝑓𝑘fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递增的，早抽似乎确实比晚抽看起来好一点．

证明

先考虑证明一个特殊情况．将证：

  * 随机过程 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：先买物品 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后不断抽直到得到所有物品
  * ……一定不优于……
  * 随机过程 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：不断抽直到得到 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以外的所有物品，然后如果还没有 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则买下来

考虑让随机过程 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和随机过程 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使用同一个随机数生成器．即，𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第一次抽取和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第一次抽取会抽到同一个元素，第二次、第三次……也是一样．

显然，此时 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 抽取的次数必定相等．对于一个被 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 抽到的物品 𝑦 ≠𝑥y≠x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，观察到：

  * 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中抽到 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时已经持有的物品数，一定大于等于 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中抽到 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时已经持有的物品数．

因此 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的单次抽取代价不高于 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的单次抽取代价，进而抽取的总代价也不高于 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

显然 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的购买代价同样不高于 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．综上，𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定不劣于 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

然后可以通过数学归纳把这一结论推广到一般情况．具体地说，每次我们找到当前策略中的最后一次购买，然后根据上述结论，把这一次购买移到最后一定不劣．细节略．

基于这个结论，我们再次等价地转化问题：把「选一个物品并支付对应价格购买」的操作，改成「随机选一个未拥有的物品并支付对应价格购买」．等价性的理由是，既然购买只是用来扫尾的，那选到哪个都无所谓．

现在我们发现，「抽取」和「购买」，实质上已经变成了相同的操作，区别仅在于付出的价格不同．选择购买还是抽取，对于获得物品的顺序毫无影响，而且每种获得物品的顺序都是等可能的．

观察：在某一时刻，我们应当选择买，当且仅当下一次抽取的代价（由已经抽到的物品数确定）大于剩余物品的平均价格（等于的话则任意）．

  * 可以证明，随着时间的推移，抽取代价的增速一定不低于剩余物品均价的增速．这说明从抽到买的「临界点」只有一个，进一步验证了先前结论．

最后，我们枚举所有可能的局面（即已经拥有的元素集合），算出这种局面出现的概率（已有元素的排列方案数除以总方案数），乘上当前局面最优决策的代价（由拥有元素个数和剩余物品总价确定），再加起来即可．这个过程可以用背包式的 DP 优化，即可通过本题．

* * *

**回顾** ：可以看到，耦合的技巧在本题中使用了两次．第一次是在证明过程中，令两个随机过程使用同一个随机源；第二次是把购买转化成随机购买（即引入随机源），从而使得购买和抽取这两种操作实质上「耦合」为同一种操作（即令抽取和购买操作共享一个随机源）．

## 参考资料

* * *

  1. [UOJ NOI Round #4 Day2 题解](https://peehs-moorhsum.blog.uoj.ac/blog/6375) ↩

  2. [Anna Gambin and Adam Malinowski, Randomized Meldable Priority Queues](https://www.researchgate.net/publication/2801527_Randomized_Meldable_Priority_Queues) ↩

  3. [PANIC - Editorial](https://discuss.codechef.com/t/panic-editorial/80145) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/rand-technique.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/rand-technique.md "edit.link.title")  
>  __本页面贡献者：[TianyiQ](https://github.com/TianyiQ), [Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [Ir1d](https://github.com/Ir1d), [leoleoasd](https://github.com/leoleoasd), [ouuan](https://github.com/ouuan), [billchenchina](https://github.com/billchenchina), [CCXXXI](https://github.com/CCXXXI), [HeRaNO](https://github.com/HeRaNO), [ImpleLee](https://github.com/ImpleLee), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [MegaOwIer](https://github.com/MegaOwIer), [partychicken](https://github.com/partychicken)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
