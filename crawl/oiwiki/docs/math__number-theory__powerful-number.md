# Powerful Number 筛 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/powerful-number/

# Powerful Number 筛

## 定义

Powerful Number（以下简称 PN）筛类似于杜教筛，或者说是杜教筛的一个扩展，可以拿来求一些积性函数的前缀和．

**要求** ：

  * 存在一个函数 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足：
    * 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数．
    * 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 易求前缀和．
    * 对于质数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑔(𝑝) =𝑓(𝑝)g(p)=f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

假设现在要求积性函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和 𝐹(𝑛) =∑𝑛𝑖=1𝑓(𝑖)F(n)=∑i=1nf(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## Powerful Number

**定义** ：对于正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的质因数分解为 𝑛 =∏𝑚𝑖=1𝑝𝑒𝑖𝑖n=∏i=1mpiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 PN 当且仅当 ∀1 ≤𝑖 ≤𝑚,𝑒𝑖 >1∀1≤i≤m,ei>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**性质 1** ：所有 PN 都可以表示成 𝑎2𝑏3a2b3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式．

**证明** ：若 𝑒𝑖ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶数，则将 𝑝𝑒𝑖𝑖piei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 合并进 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 里；若 𝑒𝑖ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为奇数，则先将 𝑝3𝑖pi3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 合并进 𝑏3b3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 里，再将 𝑝𝑒𝑖−3𝑖piei−3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 合并进 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 里．

**性质 2** ：𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以内的 PN 至多有 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．

**证明** ：考虑枚举 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再考虑满足条件的 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数，有 PN 的个数约等于

∫√𝑛13√𝑛𝑥2d𝑥=𝑂(√𝑛)∫1nnx23dx=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么如何求出 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以内所有的 PN 呢？线性筛找出 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的所有素数，再 DFS 搜索各素数的指数即可．由于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以内的 PN 至多有 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，所以至多搜索 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．

## PN 筛

首先，构造出一个易求前缀和的积性函数 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且满足对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑔(𝑝) =𝑓(𝑝)g(p)=f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．记 𝐺(𝑛) =∑𝑛𝑖=1𝑔(𝑖)G(n)=∑i=1ng(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

然后，构造函数 ℎ =𝑓/𝑔h=f/g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这里的 //![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示狄利克雷卷积除法．根据狄利克雷卷积的性质可以得知 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也为积性函数，因此 ℎ(1) =1h(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑓 =𝑔 ∗ℎf=g∗h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这里 ∗∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示狄利克雷卷积．

对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑓(𝑝) =𝑔(1)ℎ(𝑝) +𝑔(𝑝)ℎ(1) =ℎ(𝑝) +𝑔(𝑝) ⟹ ℎ(𝑝) =0f(p)=g(1)h(p)+g(p)h(1)=h(p)+g(p)⟹h(p)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据 ℎ(𝑝) =0h(p)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数可以推出对于非 PN 的数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 ℎ(𝑛) =0h(n)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仅在 PN 处取有效值．

现在，根据 𝑓 =𝑔 ∗ℎf=g∗h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

𝐹(𝑛)=𝑛∑𝑖=1𝑓(𝑖)=𝑛∑𝑖=1∑𝑑|𝑖ℎ(𝑑)𝑔(𝑖𝑑)=𝑛∑𝑑=1⌊𝑛𝑑⌋∑𝑖=1ℎ(𝑑)𝑔(𝑖)=𝑛∑𝑑=1ℎ(𝑑)⌊𝑛𝑑⌋∑𝑖=1𝑔(𝑖)=𝑛∑𝑑=1ℎ(𝑑)𝐺(⌊𝑛𝑑⌋)=𝑛∑𝑑=1𝑑 is PNℎ(𝑑)𝐺(⌊𝑛𝑑⌋)F(n)=∑i=1nf(i)=∑i=1n∑d|ih(d)g(id)=∑d=1n∑i=1⌊nd⌋h(d)g(i)=∑d=1nh(d)∑i=1⌊nd⌋g(i)=∑d=1nh(d)G(⌊nd⌋)=∑d=1d is PNnh(d)G(⌊nd⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 找出所有 PN，计算出所有 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有效值．对于 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有效值的计算，只需要计算出所有 ℎ(𝑝𝑐)h(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的值，就可以根据 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为积性函数推出 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有有效值．现在对于每一个有效值 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，计算 ℎ(𝑑)𝐺(⌊𝑛𝑑⌋)h(d)G(⌊nd⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并累加即可得到 𝐹(𝑛)F(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

下面考虑计算 ℎ(𝑝𝑐)h(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一共有两种方法：一种是直接推出 ℎ(𝑝𝑐)h(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仅与 𝑝,𝑐p,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有关的计算公式，再根据公式计算 ℎ(𝑝𝑐)h(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；另一种是根据 𝑓 =𝑔 ∗ℎf=g∗h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑓(𝑝𝑐) =∑𝑐𝑖=0𝑔(𝑝𝑖)ℎ(𝑝𝑐−𝑖)f(pc)=∑i=0cg(pi)h(pc−i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，移项可得 ℎ(𝑝𝑐) =𝑓(𝑝𝑐) −∑𝑐𝑖=1𝑔(𝑝𝑖)ℎ(𝑝𝑐−𝑖)h(pc)=f(pc)−∑i=1cg(pi)h(pc−i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，现在就可以枚举素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再枚举指数 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求解出所有 ℎ(𝑝𝑐)h(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 过程

  1. 构造 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 构造快速计算 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方法
  3. 计算 ℎ(𝑝𝑐)h(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. 搜索 PN，过程中累加答案
  5. 得到结果

对于第 3 步，可以直接根据公式计算，可以使用枚举法预处理打表，也可以搜索到了再临时推．

### 性质

以使用第二种方法计算 ℎ(𝑝𝑐)h(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为例进行分析．可以分为计算 ℎ(𝑝𝑐)h(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和搜索两部分进行分析．

对于第一部分，根据 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的素数个数为 𝑂(√𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每个素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的指数 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至多为 log⁡𝑛log⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，计算 ℎ(𝑝𝑐)h(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要循环 (𝑐 −1)(c−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，由此有第一部分的时间复杂度为 𝑂(√𝑛log⁡𝑛⋅log⁡𝑛⋅log⁡𝑛) =𝑂(√𝑛log⁡𝑛)O(nlog⁡n⋅log⁡n⋅log⁡n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且这是一个宽松的上界．根据题目的不同还可以添加不同的优化，从而降低第一部分的时间复杂度．

对于搜索部分，由于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以内的 PN 至多有 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，所以至多搜索 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．对于每一个 PN，根据计算 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方法不同，时间复杂度也不同．例如，假设计算 𝐺(⌊𝑛𝑑⌋)G(⌊nd⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度为 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则第二部分的复杂度为 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

特别地，若借助杜教筛计算 𝐺(⌊𝑛𝑑⌋)G(⌊nd⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则第二部分的时间复杂度为杜教筛的时间复杂度，即 𝑂(𝑛23)O(n23)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为若事先计算一次 𝐺(𝑛)G(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且预先使用线性筛优化和用支持快速随机访问的数据结构（如 C++ 中的 `std::map` 和 `std::unordered_map`）记录较大的值，则杜教筛过程中用到的 𝐺(⌊𝑛𝑑⌋)G(⌊nd⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是线性筛中记录的或者 `std::map` 中记录的，这一点可以直接用程序验证．

对于空间复杂度，其瓶颈在于存储 ℎ(𝑝𝑐)h(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若使用二维数组 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记录，𝑎𝑖,𝑗ai,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 ℎ(𝑝𝑗𝑖)h(pij)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，则空间复杂度为 𝑂(√𝑛log⁡𝑛⋅log⁡𝑛) =𝑂(√𝑛)O(nlog⁡n⋅log⁡n)=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 例题

### [Luogu P5325【模板】Min_25 筛](https://www.luogu.com.cn/problem/P5325)

**题意** ：给定积性函数 𝑓(𝑝𝑘) =𝑝𝑘(𝑝𝑘 −1)f(pk)=pk(pk−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 ∑𝑛𝑖=1𝑓(𝑖)∑i=1nf(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

易得 𝑓(𝑝) =𝑝(𝑝 −1) =id⁡(𝑝)𝜑(𝑝)f(p)=p(p−1)=id⁡(p)φ(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，构造 𝑔(𝑛) =id⁡(𝑛)𝜑(𝑛)g(n)=id⁡(n)φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑使用杜教筛求 𝐺(𝑛)G(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据 (id ⋅𝜑) ∗id =id2(id⋅φ)∗id=id2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可得 𝐺(𝑛) =∑𝑛𝑖=1𝑖2 −∑𝑛𝑑=2𝑑 ⋅𝐺(⌊𝑛𝑑⌋)G(n)=∑i=1ni2−∑d=2nd⋅G(⌊nd⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

之后 ℎ(𝑝𝑘)h(pk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值可以枚举计算，这种方法不再赘述．

此外，此题还可以直接求出 ℎ(𝑝𝑘)h(pk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仅与 𝑝,𝑘p,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有关的公式，过程如下：

𝑓(𝑝𝑘)=𝑘∑𝑖=0𝑔(𝑝𝑘−𝑖)ℎ(𝑝𝑖)⟺𝑝𝑘(𝑝𝑘−1)=𝑘∑𝑖=0𝑝𝑘−𝑖𝜑(𝑝𝑘−𝑖)ℎ(𝑝𝑖)⟺𝑝𝑘(𝑝𝑘−1)=𝑘∑𝑖=0𝑝2𝑘−2𝑖−1(𝑝−1)ℎ(𝑝𝑖)⟺𝑝𝑘(𝑝𝑘−1)=ℎ(𝑝𝑘)+𝑘−1∑𝑖=0𝑝2𝑘−2𝑖−1(𝑝−1)ℎ(𝑝𝑖)⟺ℎ(𝑝𝑘)=𝑝𝑘(𝑝𝑘−1)−𝑘−1∑𝑖=0𝑝2𝑘−2𝑖−1(𝑝−1)ℎ(𝑝𝑖)⟺ℎ(𝑝𝑘)−𝑝2ℎ(𝑝𝑘−1)=𝑝𝑘(𝑝𝑘−1)−𝑝𝑘+1(𝑝𝑘−1−1)−𝑝(𝑝−1)ℎ(𝑝𝑘−1)⟺ℎ(𝑝𝑘)−𝑝ℎ(𝑝𝑘−1)=𝑝𝑘+1−𝑝𝑘⟺ℎ(𝑝𝑘)𝑝𝑘−ℎ(𝑝𝑘−1)𝑝𝑘−1=𝑝−1f(pk)=∑i=0kg(pk−i)h(pi)⟺pk(pk−1)=∑i=0kpk−iφ(pk−i)h(pi)⟺pk(pk−1)=∑i=0kp2k−2i−1(p−1)h(pi)⟺pk(pk−1)=h(pk)+∑i=0k−1p2k−2i−1(p−1)h(pi)⟺h(pk)=pk(pk−1)−∑i=0k−1p2k−2i−1(p−1)h(pi)⟺h(pk)−p2h(pk−1)=pk(pk−1)−pk+1(pk−1−1)−p(p−1)h(pk−1)⟺h(pk)−ph(pk−1)=pk+1−pk⟺h(pk)pk−h(pk−1)pk−1=p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再根据 ℎ(𝑝) =0h(p)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，通过累加法即可推出 ℎ(𝑝𝑘) =(𝑘 −1)(𝑝 −1)𝑝𝑘h(pk)=(k−1)(p−1)pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 ``` |  ```text #include <iostream> #include <map> using namespace std ; constexpr int MOD = 1e9 \+ 7 ; template < typename T > int mint ( T x ) { x %= MOD ; if ( x < 0 ) x += MOD ; return x ; } int add ( int x , int y ) { return x \+ y >= MOD ? x \+ y \- MOD : x \+ y ; } int mul ( int x , int y ) { return ( long long ) 1 * x * y % MOD ; } int sub ( int x , int y ) { return x < y ? x \- y \+ MOD : x \- y ; // 防止负数 } int qp ( int x , int y ) { int r = 1 ; for (; y ; y >>= 1 ) { if ( y & 1 ) r = mul ( r , x ); x = mul ( x , x ); } return r ; } int inv ( int x ) { return qp ( x , MOD \- 2 ); } namespace PNS { constexpr int N = 2e6 \+ 5 ; constexpr int M = 35 ; long long global_n ; int g [ N ], sg [ N ]; int h [ N ][ M ]; bool vis_h [ N ][ M ]; int ans ; int pcnt , prime [ N ], phi [ N ]; bool isp [ N ]; void sieve ( int n ) { pcnt = 0 ; for ( int i = 2 ; i <= n ; ++ i ) isp [ i ] = true ; // 判断质数数组 phi [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; ++ i ) { if ( isp [ i ]) { ++ pcnt ; prime [ pcnt ] = i ; phi [ i ] = i \- 1 ; } for ( int j = 1 ; j <= pcnt ; ++ j ) { // 筛去非质数 long long nxt = ( long long ) 1 * i * prime [ j ]; if ( nxt > n ) break ; isp [ nxt ] = false ; if ( i % prime [ j ] == 0 ) { // i是非质数的情况 phi [ nxt ] = phi [ i ] * prime [ j ]; break ; } phi [ nxt ] = phi [ i ] * phi [ prime [ j ]]; } } for ( int i = 1 ; i <= n ; ++ i ) g [ i ] = mul ( i , phi [ i ]); sg [ 0 ] = 0 ; for ( int i = 1 ; i <= n ; ++ i ) sg [ i ] = add ( sg [ i \- 1 ], g [ i ]); // g函数的前缀和 } int inv2 , inv6 ; void init () { sieve ( N \- 1 ); for ( int i = 1 ; i <= pcnt ; ++ i ) h [ i ][ 0 ] = 1 , h [ i ][ 1 ] = 0 ; for ( int i = 1 ; i <= pcnt ; ++ i ) vis_h [ i ][ 0 ] = vis_h [ i ][ 1 ] = true ; inv2 = inv ( 2 ); inv6 = inv ( 6 ); } int S1 ( long long n ) { return mul ( mul ( mint ( n ), mint ( n \+ 1 )), inv2 ); } int S2 ( long long n ) { return mul ( mul ( mint ( n ), mul ( mint ( n \+ 1 ), mint ( n * 2 \+ 1 ))), inv6 ); } map < long long , int > mp_g ; int G ( long long n ) { if ( n < N ) return sg [ n ]; if ( mp_g . count ( n )) return mp_g [ n ]; int ret = S2 ( n ); for ( long long i = 2 , j ; i <= n ; i = j \+ 1 ) { j = n / ( n / i ); ret = sub ( ret , mul ( sub ( S1 ( j ), S1 ( i \- 1 )), G ( n / i ))); } mp_g [ n ] = ret ; return ret ; } void dfs ( long long d , int hd , int pid ) { ans = add ( ans , mul ( hd , G ( global_n / d ))); for ( int i = pid ; i <= pcnt ; ++ i ) { if ( i > 1 && d > global_n / prime [ i ] / prime [ i ]) break ; // 剪枝 int c = 2 ; for ( long long x = d * prime [ i ] * prime [ i ]; x <= global_n ; x *= prime [ i ], ++ c ) { // 计算f.g函数 if ( ! vis_h [ i ][ c ]) { int f = qp ( prime [ i ], c ); f = mul ( f , sub ( f , 1 )); int g = mul ( prime [ i ], prime [ i ] \- 1 ); int t = mul ( prime [ i ], prime [ i ]); for ( int j = 1 ; j <= c ; ++ j ) { f = sub ( f , mul ( g , h [ i ][ c \- j ])); g = mul ( g , t ); } h [ i ][ c ] = f ; vis_h [ i ][ c ] = true ; } if ( h [ i ][ c ]) dfs ( x , mul ( hd , h [ i ][ c ]), i \+ 1 ); } } } int solve ( long long n ) { global_n = n ; ans = 0 ; dfs ( 1 , 1 , 1 ); return ans ; } } // namespace PNS int main () { PNS :: init (); long long n ; cin >> n ; cout << PNS :: solve ( n ) << '\n' ; return 0 ; } ```   
---|---  
  
### [「LOJ #6053」简单的函数](https://loj.ac/problem/6053)

给定 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑓(𝑛)=⎧{ {⎨{ {⎩1𝑛=1𝑝⊕𝑐𝑛=𝑝𝑐𝑓(𝑎)𝑓(𝑏)𝑛=𝑎𝑏 and 𝑎⟂𝑏f(n)={1n=1p⊕cn=pcf(a)f(b)n=ab and a⟂b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

易得：

𝑓(𝑝)={𝑝+1𝑝=2𝑝−1otherwisef(p)={p+1p=2p−1otherwise![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

构造 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

𝑔(𝑛)={3𝜑(𝑛)2∣𝑛𝜑(𝑛)otherwiseg(n)={3φ(n)2∣nφ(n)otherwise![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

易证 𝑔(𝑝) =𝑓(𝑝)g(p)=f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为积性函数．

下面考虑求 𝐺(𝑛)G(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

𝐺(𝑛)=𝑛∑𝑖=1[𝑖mod2=1]𝜑(𝑖)+3𝑛∑𝑖=1[𝑖mod2=0]𝜑(𝑖)=𝑛∑𝑖=1𝜑(𝑖)+2𝑛∑𝑖=1[𝑖mod2=0]𝜑(𝑖)=𝑛∑𝑖=1𝜑(𝑖)+2⌊𝑛2⌋∑𝑖=1𝜑(2𝑖)G(n)=∑i=1n[imod2=1]φ(i)+3∑i=1n[imod2=0]φ(i)=∑i=1nφ(i)+2∑i=1n[imod2=0]φ(i)=∑i=1nφ(i)+2∑i=1⌊n2⌋φ(2i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

记 𝑆1(𝑛) =∑𝑛𝑖=1𝜑(𝑖)S1(n)=∑i=1nφ(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑆2(𝑛) =∑𝑛𝑖=1𝜑(2𝑖)S2(n)=∑i=1nφ(2i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝐺(𝑛) =𝑆1(𝑛) +2𝑆2(⌊𝑛2⌋)G(n)=S1(n)+2S2(⌊n2⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当 2 ∣𝑛2∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有

𝑆2(𝑛)=𝑛∑𝑖=1𝜑(2𝑖)=𝑛2∑𝑖=1(𝜑(2(2𝑖−1))+𝜑(2(2𝑖)))=𝑛2∑𝑖=1(𝜑(2𝑖−1)+2𝜑(2𝑖))=𝑛2∑𝑖=1(𝜑(2𝑖−1)+𝜑(2𝑖))+𝑛2∑𝑖=1𝜑(2𝑖)=𝑛∑𝑖=1𝜑(𝑖)+𝑆2(𝑛2)=𝑆1(𝑛)+𝑆2(⌊𝑛2⌋)S2(n)=∑i=1nφ(2i)=∑i=1n2(φ(2(2i−1))+φ(2(2i)))=∑i=1n2(φ(2i−1)+2φ(2i))=∑i=1n2(φ(2i−1)+φ(2i))+∑i=1n2φ(2i)=∑i=1nφ(i)+S2(n2)=S1(n)+S2(⌊n2⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当 2 ∤𝑛2∤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有

𝑆2(𝑛)=𝑆2(𝑛−1)+𝜑(2𝑛)=𝑆2(𝑛−1)+𝜑(𝑛)=𝑛−1∑𝑖=1𝜑(𝑖)+𝑆2(𝑛−12)+𝜑(𝑛)=𝑆1(𝑛)+𝑆2(⌊𝑛2⌋)S2(n)=S2(n−1)+φ(2n)=S2(n−1)+φ(n)=∑i=1n−1φ(i)+S2(n−12)+φ(n)=S1(n)+S2(⌊n2⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

综上，有 𝑆2(𝑛) =𝑆1(𝑛) +𝑆2(⌊𝑛2⌋)S2(n)=S1(n)+S2(⌊n2⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

𝑆1S1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以用杜教筛求，𝑆2S2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 直接按照公式推，这样 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也可以求出来了．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 ``` |  ```text #include <iostream> #include <map> using namespace std ; constexpr int MOD = 1e9 \+ 7 ; constexpr int inv2 = ( MOD \+ 1 ) / 2 ; template < typename T > int mint ( T x ) { x %= MOD ; if ( x < 0 ) x += MOD ; return x ; } int add ( int x , int y ) { return x \+ y >= MOD ? x \+ y \- MOD : x \+ y ; // 防止大于模数 } int mul ( int x , int y ) { return ( long long ) 1 * x * y % MOD ; } int sub ( int x , int y ) { return x < y ? x \- y \+ MOD : x \- y ; // 防负数 } namespace PNS { constexpr int N = 2e6 \+ 5 ; constexpr int M = 35 ; long long global_n ; int s1 [ N ], s2 [ N ]; int h [ N ][ M ]; bool vis_h [ N ][ M ]; int ans ; int pcnt , prime [ N ], phi [ N ]; bool isp [ N ]; void sieve ( int n ) { pcnt = 0 ; for ( int i = 2 ; i <= n ; ++ i ) isp [ i ] = true ; // 判断质数数组 phi [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; ++ i ) { if ( isp [ i ]) { ++ pcnt ; prime [ pcnt ] = i ; phi [ i ] = i \- 1 ; } for ( int j = 1 ; j <= pcnt ; ++ j ) { // 筛去非质数 long long nxt = ( long long ) 1 * i * prime [ j ]; if ( nxt > n ) break ; isp [ nxt ] = false ; if ( i % prime [ j ] == 0 ) { // i是非质数的情况 phi [ nxt ] = phi [ i ] * prime [ j ]; break ; } phi [ nxt ] = phi [ i ] * phi [ prime [ j ]]; } } s1 [ 0 ] = 0 ; for ( int i = 1 ; i <= n ; ++ i ) s1 [ i ] = add ( s1 [ i \- 1 ], phi [ i ]); s2 [ 0 ] = 0 ; for ( int i = 1 ; i <= n / 2 ; ++ i ) { s2 [ i ] = add ( s2 [ i \- 1 ], phi [ 2 * i ]); } } void init () { sieve ( N \- 1 ); for ( int i = 1 ; i <= pcnt ; ++ i ) h [ i ][ 0 ] = 1 ; for ( int i = 1 ; i <= pcnt ; ++ i ) vis_h [ i ][ 0 ] = true ; } map < long long , int > mp_s1 ; int S1 ( long long n ) { if ( n < N ) return s1 [ n ]; if ( mp_s1 . count ( n )) return mp_s1 [ n ]; int ret = mul ( mul ( mint ( n ), mint ( n \+ 1 )), inv2 ); for ( long long i = 2 , j ; i <= n ; i = j \+ 1 ) { j = n / ( n / i ); ret = sub ( ret , mul ( mint ( j \- i \+ 1 ), S1 ( n / i ))); } mp_s1 [ n ] = ret ; return ret ; } map < long long , int > mp_s2 ; int S2 ( long long n ) { if ( n < N / 2 ) return s2 [ n ]; if ( mp_s2 . count ( n )) return mp_s2 [ n ]; int ret = add ( S1 ( n ), S2 ( n / 2 )); mp_s2 [ n ] = ret ; return ret ; } int G ( long long n ) { return add ( S1 ( n ), mul ( 2 , S2 ( n / 2 ))); } void dfs ( long long d , int hd , int pid ) { ans = add ( ans , mul ( hd , G ( global_n / d ))); for ( int i = pid ; i <= pcnt ; ++ i ) { if ( i > 1 && d > global_n / prime [ i ] / prime [ i ]) break ; // 剪枝 int c = 2 ; for ( long long x = d * prime [ i ] * prime [ i ]; x <= global_n ; x *= prime [ i ], ++ c ) { if ( ! vis_h [ i ][ c ]) { int f = prime [ i ] ^ c , g = prime [ i ] \- 1 ; // p = 2时特判一下 if ( i == 1 ) g = mul ( g , 3 ); for ( int j = 1 ; j <= c ; ++ j ) { f = sub ( f , mul ( g , h [ i ][ c \- j ])); g = mul ( g , prime [ i ]); } h [ i ][ c ] = f ; vis_h [ i ][ c ] = true ; } if ( h [ i ][ c ]) dfs ( x , mul ( hd , h [ i ][ c ]), i \+ 1 ); } } } int solve ( long long n ) { global_n = n ; ans = 0 ; dfs ( 1 , 1 , 1 ); return ans ; } } // namespace PNS int main () { PNS :: init (); // 预处理函数 long long n ; cin >> n ; cout << PNS :: solve ( n ) << '\n' ; return 0 ; } ```   
---|---  
  
## 习题

  * [PE708 Twos are all you need](https://projecteuler.net/problem=708)
  * [PE639 Summing a multiplicative function](https://projecteuler.net/problem=639)
  * [PE484 Arithmetic Derivative](https://projecteuler.net/problem=484)

## 参考资料

  * [破壁人五号 - Powerful number 筛略解](https://www.cnblogs.com/wallbreaker5th/p/13901487.html)
  * [command_block - 杜教筛（+ 贝尔级数 + powerful number）](https://www.luogu.com.cn/blog/command-block/du-jiao-shai)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/powerful-number.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/powerful-number.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [Backl1ght](https://github.com/Backl1ght), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid), [cy1999](https://github.com/cy1999), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [LaDeXX](https://github.com/LaDeXX), [lrherqwq](https://github.com/lrherqwq), [Marcythm](https://github.com/Marcythm), [xyf007](https://github.com/xyf007)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
