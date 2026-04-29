# 概率不等式 - OI Wiki

- Source: https://oi-wiki.org/math/probability/concentration-inequality/

# 概率不等式

算法竞赛中有时会用到 [随机化算法](../../../misc/rand-technique/)，这些算法的正确性与时空复杂度通常依赖于「某些随机事件发生的概率很小」这一前提．例如，快速排序的复杂度依赖于「所选的 `pivot` 元素几乎是最小或最大元素」这一事件较少发生．

本文将简要介绍一些用于分析随机化算法的工具并给出几个简单应用的例子．

## Union Bound

记 𝐴1,⋯,𝐴𝑚A1,⋯,Am![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为随机事件，则

𝑃{𝑚⋃𝑖=1𝐴𝑖}≤𝑚∑𝑖=1𝑃{𝐴𝑖}P{⋃i=1mAi}≤∑i=1mP{Ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即：一组事件中至少一个发生的概率，不超过每一个的发生概率之和．

实际上，这一结论还可以稍作加强：

  * 一组事件中至少一者发生的概率，**不小于** 每一个的发生概率之和，减掉每两个同时发生的概率之和．
  * 一组事件中至少一者发生的概率，**不超过** 每一个的发生概率之和，减掉每两个同时发生的概率之和，加上每三个同时发生的概率之和．
  * ……

随着层数越来越多，交替出现的上界和下界也越来越紧．这一系列结论形式上类似容斥原理，证明过程也和容斥类似，这里略去．

## Markov 不等式

设 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个取值非负的随机变量，则对任意正实数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

𝑃{𝑋≥𝑎}≤𝐸𝑋𝑎P{X≥a}≤EXa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

事实上，由于 Markov 不等式本身并没有用到随机变量除期望外的与分布有关的任何信息，因此直接应用这个不等式得到的约束通常很松．

### 证明

记 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为事件 𝑋 ≥𝑎X≥a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的示性函数，则有

𝐼≤𝑋𝑎I≤Xa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而

𝑃{𝑋≥𝑎}=𝐸𝐼≤𝐸[𝑋𝑎]=𝐸𝑋𝑎P{X≥a}=EI≤E[Xa]=EXa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## Chebyshev 不等式

设 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一随机变量，则对任意的 𝑎 >0a>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有

𝑃{|𝑋−𝐸𝑋|≥𝑎}≤𝐷𝑋𝑎2P{|X−EX|≥a}≤DXa2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

特别地，当 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取 𝑘𝜎kσ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时有

𝑃{|𝑋−𝐸𝑋|≥𝑘𝜎}≤1𝑘2P{|X−EX|≥kσ}≤1k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的标准差．

### 证明

由已知，有

𝑃{|𝑋−𝐸𝑋|≥𝑎}=𝑃{(𝑋−𝐸𝑋)2≥𝑎2}P{|X−EX|≥a}=P{(X−EX)2≥a2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到 (𝑋 −𝐸𝑋)2(X−EX)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非负，故由 Markov 不等式可知

𝑃{(𝑋−𝐸𝑋)2≥𝑎2}≤𝐸(𝑋−𝐸𝑋)2𝑎2=𝐷𝑋𝑎2P{(X−EX)2≥a2}≤E(X−EX)2a2=DXa2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## Chernoff 不等式

一般的 Chernoff 不等式可以从直接对随机变量 e𝑡𝑋etX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应用 Markov 不等式得出：

设 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一随机变量，则对任意的 𝑡 >0t>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有

𝑃{𝑋≥𝑎}=𝑃{e𝑡𝑋>e𝑡𝑎}≤𝐸e𝑡𝑋e𝑡𝑎P{X≥a}=P{etX>eta}≤EetXeta![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

类似地，当 𝑡 <0t<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时有

𝑃{𝑋≤𝑎}=𝑃{e𝑡𝑋>e𝑡𝑎}≤𝐸e𝑡𝑋e𝑡𝑎P{X≤a}=P{etX>eta}≤EetXeta![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### Poisson 试验之和的 Chernoff 不等式

算法竞赛中涉及的随机变量通常没有那么「一般」，我们可以用概率论中的 Poisson 试验对其进行描述．

所谓 Poisson 试验，是指在只有两种可能结果的随机试验．

一次的 Poisson 试验的结果可以用一个取值为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行刻画，其概率分布为

𝑃{𝑋=𝑖}={𝑝𝑖,𝑖=11−𝑝1,𝑖=0P{X=i}={pi,i=11−p1,i=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于 Poisson 试验，我们有如下结论：

对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个独立的 Poisson 试验 𝑋1,𝑋2,⋯,𝑋𝑛X1,X2,⋯,Xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记 𝑋 =∑𝑛𝑖=1𝑋𝑖X=∑i=1nXi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以及 𝜇 =𝐸𝑋μ=EX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对任意 0 <𝜖 <10<ϵ<1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

𝑃{|𝑋−𝜇|≥𝜖𝜇}≤2exp⁡(−13𝜇𝜖2)P{|X−μ|≥ϵμ}≤2exp⁡(−13μϵ2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## Hoeffding 不等式

若 𝑋1,⋯,𝑋𝑛X1,⋯,Xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为互相独立的实随机变量且 𝑋𝑖 ∈[𝑎𝑖,𝑏𝑖]Xi∈[ai,bi]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记随机变量 𝑋 =𝑛∑𝑖=1𝑋𝑖X=∑i=1nXi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则

𝑃{|𝑋−𝐸𝑋|≥𝜖}≤2exp⁡⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝−2𝜖2𝑛∑𝑖=1(𝑏𝑖−𝑎𝑖)2⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠P{|X−EX|≥ϵ}≤2exp⁡(−2ϵ2∑i=1n(bi−ai)2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Chernoff 不等式和 Hoeffding 不等式都限制了随机变量偏离其期望值的程度．这两个不等式的证明过程较为冗长，有兴趣的同学可以查阅 Probability and Computing 一书中的相关章节．

从经验上讲，如果 𝐸𝑋EX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不太接近 𝑎1 +⋯ +𝑎𝑛a1+⋯+an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则该不等式给出的界往往相对比较紧；如果非常接近的话（例如在 [UOJ #72 全新做法](https://matthew99.blog.uoj.ac/blog/5511) 中），给出的界则往往很松，此时更好的选择是使用 Chernoff 不等式．

## 应用举例

### 例：随机撒点估算圆周率

考虑下列估计圆周率 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的精确值的算法：

在正方形区域 [ −1,1]2[−1,1]2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内随机生成 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，记其中落入单位圆盘 𝑥2 +𝑦2 ≤1x2+y2≤1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点数为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则可以取 4𝑚𝑛4mn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的近似值．

问题：若要保证上述算法以至少 (1 −𝛿)(1−δ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率返回相对误差不超过 𝜖ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结果，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应该如何取定？

解答

记 𝑋𝑖Xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示事件「随机生成的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点在单位圆内」，则圆内总点数 𝑋 =∑𝑛𝑖=1𝑋𝑖X=∑i=1nXi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们需要找到一个合适的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝑃{∣4𝑋𝑛−𝜋∣≥𝜖𝜋}≤𝛿P{|4Xn−π|≥ϵπ}≤δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上式等价于

𝑃{∣𝑋−𝜋4𝑛∣≥𝜖⋅𝜋4𝑛}≤𝛿P{|X−π4n|≥ϵ⋅π4n}≤δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据 Chernoff 不等式，我们只需令

2exp⁡(−13𝜖2⋅𝜋4𝑛)≤𝛿2exp⁡(−13ϵ2⋅π4n)≤δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即可，由此可解得

𝑛≥12𝜋𝜖−2ln⁡2𝛿n≥12πϵ−2ln⁡2δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即当 𝑛 =Ω(𝜖−2ln⁡1𝛿)n=Ω(ϵ−2ln⁡1δ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时可以达到需要的准确率．

### 例：抽奖问题

一个箱子里有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个球，其中恰有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个球对应着大奖．你要进行若干次独立、等概率的随机抽取，每次抽完之后会把球放回箱子．请问抽多少次能保证以至少 (1 −𝜖)(1−ϵ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率，满足 **每一个** 奖球都被抽到至少一次？

解答

假如只有一个奖球，则抽取 𝑀 =𝑛log⁡𝜖−1M=nlog⁡ϵ−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次即可保证，因为 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次全不中的概率

(1−1𝑛)𝑛log⁡𝜖−1≤𝑒log⁡𝜖=𝜖(1−1n)nlog⁡ϵ−1≤elog⁡ϵ=ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

现在有 𝑘 >1k>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个奖球，那么根据 Union Bound，我们只需保证每个奖球被漏掉的概率都不超过 𝜖𝑘ϵk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．于是答案是 𝑛log⁡𝑘𝜖nlog⁡kϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 例：随机选取一半元素

给出一个算法，从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素中等概率随机选取一个大小为 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集，保证 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶数．你能使用的唯一的随机源是一枚均匀硬币，同时请你尽量减少抛硬币的次数（不要求最少）．

解法

首先可以想到这样的算法：

  * 通过抛 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次硬币，可以从所有子集中等概率随机选一个．
  * 不断重复这一过程，直到选出的子集大小恰好为 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
    * 注意到大小为 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集至少占所有子集的 1𝑛1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此重复次数的期望值 ≤𝑛≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这一算法期望需要抛 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次硬币．

另一个算法：

  * 我们可以通过抛期望 2⌈log2⁡𝑛⌉2⌈log2⁡n⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次硬币来实现随机 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 选 1．
    * 具体方法：随机生成 ⌈log2⁡𝑛⌉⌈log2⁡n⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的二进制数，如果大于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则重新随机，否则选择对应编号（编号从 0 开始）的元素并结束过程．
  * 然后我们从所有元素中选一个，再从剩下的元素中再选一个，以此类推，直到选出 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素为止．

这一算法期望需要抛 𝑛⌈log2⁡𝑛⌉n⌈log2⁡n⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次硬币．

将两个算法缝合起来：

  * 先用第一个算法随机得到一个子集．
  * 如果该子集大小不到 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则利用第二个算法不断添加元素，直到将大小补到 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 如果该子集大小超过 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则利用第二个算法不断删除元素，直到将大小削到 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

尝试分析第二、第三步所需的操作次数（即添加/删除元素的次数）：

  * 记 01 随机变量 𝑋𝑖Xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否被选入初始的子集，令 𝑋 :=𝑋1 +⋯ +𝑋𝑛X:=X1+⋯+Xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示子集大小，则第二、第三步所需的操作次数等于 ∣𝑋 −E[𝑋]∣|X−E[X]|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在 Hoeffding 不等式中取 𝑡 =𝑐 ⋅√𝑛t=c⋅n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（其中 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为任意常数），得到 Pr[∣𝑋 −E[𝑋]∣ ≥𝑡] ≤2e−𝑐2Pr[|X−E[X]|≥t]≤2e−c2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，我们可以通过允许 Θ(√𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别的偏移，来得到任意小的常数级别的失败概率．

至此我们已经说明：该算法可以以很大概率保证抛硬币次数在 𝑛 +Θ(√𝑛log⁡𝑛)n+Θ(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以内．

  * 其中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来自获得初始子集的抛硬币次数；Θ(√𝑛log⁡𝑛)Θ(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Θ(√𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次添加/删除元素的总开销．

计算期望复杂度

我们再从另一个角度分析，尝试计算该算法的期望抛硬币次数．

用 Hoeffding 不等式求第二、第三步中操作次数期望值的上界：

𝐸|𝑋−𝐸𝑋|=∫∞0𝑃{|𝑋−𝐸[𝑋]|≥𝑡}d𝑡≤2∫∞0exp⁡(−𝑡2𝑛)d𝑡=√𝜋𝑛E|X−EX|=∫0∞P{|X−E[X]|≥t}dt≤2∫0∞exp⁡(−t2n)dt=πn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从而第二、第三步所需抛硬币次数的期望值是 √𝜋𝑛 ⋅2⌈log2⁡𝑛⌉πn⋅2⌈log2⁡n⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

综上，该算法期望需要抛 𝑛 +2√𝜋𝑛⌈log2⁡𝑛⌉n+2πn⌈log2⁡n⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次硬币．

### 练习：Balls and Bins

𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个球独立随机地扔到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个盒子里，试证明：球最多的盒子中的球数以 1 −1𝑛1−1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率不少于 Ω(log⁡𝑛log⁡log⁡𝑛)Ω(log⁡nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/probability/concentration-inequality.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/probability/concentration-inequality.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [aofall](https://github.com/aofall), [CCXXXI](https://github.com/CCXXXI), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Marcythm](https://github.com/Marcythm), [MegaOwIer](https://github.com/MegaOwIer), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu), [SparkleInfinity](https://github.com/SparkleInfinity)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
