# 洲阁筛 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/zhou/

# 洲阁筛

## 前置知识

  * [积性函数](../basic/#积性函数)

## 定义

洲阁筛是一种能在亚线性时间复杂度内求出大多数积性函数前缀和的筛法．

下面将以求解 𝑛∑𝑖=1𝑓(𝑖)∑i=1nf(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为例，具体阐述洲阁筛的原理．

## 约定

  * ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示质数集，𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个质数．
  * 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的质数个数．

## 要求

当 𝑝 ∈ℙ,𝑐 ∈ℕp∈P,c∈N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑓(𝑝𝑐)f(pc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一个关于 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的低阶多项式．

## 思想

  * 对于任意 [1,𝑛][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的整数，其至多只有一个 >√𝑛>n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的质因子．
  * 利用 ⌊𝑛𝑖⌋(𝑖 ∈[1,𝑛] ∩ℕ)⌊ni⌋(i∈[1,n]∩N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只有 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别个取值的性质来降低时间复杂度．

## 过程

将 [1,𝑛][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的所有整数按是否有 >√𝑛>n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的质因子分为两类：

𝑛∑𝑖=1𝑓(𝑖)=𝑛∑𝑖=1[∃𝑑∈(√𝑛,𝑛]∩ℙ,𝑑∣𝑖]𝑓(𝑖)+𝑛∑𝑖=1[∀𝑑∈(√𝑛,𝑛]∩ℙ,𝑑∤𝑖]𝑓(𝑖)∑i=1nf(i)=∑i=1n[∃d∈(n,n]∩P,d∣i]f(i)+∑i=1n[∀d∈(n,n]∩P,d∤i]f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于前半部分，枚举最大因子，根据积性函数的性质可以转换：

𝑛∑𝑖=1𝑓(𝑖)=√𝑛∑𝑖=1𝑓(𝑖)⋅⎛⎜ ⎜ ⎜⎝⌊𝑛𝑖⌋∑𝑑=⌊√𝑛⌋+1[𝑑∈ℙ]𝑓(𝑑)⎞⎟ ⎟ ⎟⎠+𝑛∑𝑖=1[∀𝑑∈(√𝑛,𝑛]∩ℙ,𝑑∤𝑖]𝑓(𝑖)∑i=1nf(i)=∑i=1nf(i)⋅(∑d=⌊n⌋+1⌊ni⌋[d∈P]f(d))+∑i=1n[∀d∈(n,n]∩P,d∤i]f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

前后部分可以分别计算．

### Part 1

> 计算 √𝑛∑𝑖=1𝑓(𝑖) ⋅⎛⎜ ⎜ ⎜⎝⌊𝑛𝑖⌋∑𝑑=⌊√𝑛⌋+1[𝑑∈ℙ]𝑓(𝑑)⎞⎟ ⎟ ⎟⎠∑i=1nf(i)⋅(∑d=⌊n⌋+1⌊ni⌋[d∈P]f(d))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑枚举 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算括号内部分．

记 𝑔(𝑡,𝑙) =𝑙∑𝑖=1[∀𝑗 ∈[1,𝑡],gcd(𝑖,𝑝𝑗) =1]𝑓(𝑖)g(t,l)=∑i=1l[∀j∈[1,t],gcd(i,pj)=1]f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 [1,𝑙][1,l]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中与 𝑝1,𝑝2,…,𝑝𝑡p1,p2,…,pt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均互质的数的 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值之和．

这样 Part 1 的计算就变成了 √𝑛∑𝑖=1𝑓(𝑖) ⋅𝑔(𝑚,⌊𝑛𝑖⌋)∑i=1nf(i)⋅g(m,⌊ni⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

边界 𝑔(0,𝑙) =∑𝑙𝑖=1𝑓(𝑖)g(0,l)=∑i=1lf(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，转移 𝑔(𝑡,𝑙) =𝑔(𝑡 −1,𝑙) −𝑓(𝑝𝑡) ⋅𝑔(𝑡−1,⌊𝑙𝑝𝑡⌋)g(t,l)=g(t−1,l)−f(pt)⋅g(t−1,⌊lpt⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共有 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别种取值，对于每种取值则需要枚举其质因子，所以复杂度为 𝑂(√𝑛ln⁡√𝑛⋅√𝑛) =𝑂(𝑛log⁡𝑛)O(nln⁡n⋅n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，需要优化．

注意到 𝑝2𝑡+1 >𝑙pt+12>l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时符合条件的数只有 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以此时 𝑔(𝑡,𝑙) =𝑓(1) =1g(t,l)=f(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

代入递推式可得：当 𝑝2𝑡 >𝑙pt2>l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑔(𝑡,𝑙) =𝑔(𝑡 −1,𝑙) −𝑓(𝑝𝑡)g(t,l)=g(t−1,l)−f(pt)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

所以一旦发现 𝑝2𝑡 >𝑙pt2>l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就停止转移，记此时的 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑡𝑙tl![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 ∀𝑡 >𝑡𝑙,𝑔(𝑡,𝑙) =𝑔(𝑡𝑙,𝑙) −∑𝑡−1𝑖=𝑡𝑙𝑓(𝑝𝑖)∀t>tl,g(t,l)=g(tl,l)−∑i=tlt−1f(pi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

预处理质数的 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值前缀和即可快速求出 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时间复杂度被优化至 𝑂(𝑛34log⁡𝑛)O(n34log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### Part 2

> 计算 𝑛∑𝑖=1[∀𝑑∈(√𝑛,𝑛]∩ℙ,𝑑∤𝑖]𝑓(𝑖)∑i=1n[∀d∈(n,n]∩P,d∤i]f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

记 ℎ(𝑡,𝑙) =𝑙∑𝑖=1[𝑖=𝑚∏𝑗=𝑡𝑝𝑐𝑗𝑗,𝑐𝑗∈ℕ]𝑓(𝑖)h(t,l)=∑i=1l[i=∏j=tmpjcj,cj∈N]f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 [1,𝑙][1,l]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有只含 𝑝𝑡,𝑝𝑡+1,…,𝑝𝑚pt,pt+1,…,pm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 质因子的数的 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值之和．

Part 2 即为求 ℎ(0,𝑛)h(0,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

边界 ℎ(𝑚 +1,𝑙) =1h(m+1,l)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，转移 ℎ(𝑡,𝑙) =ℎ(𝑡 +1,𝑙) +∑𝑐∈ℕ∗𝑓(𝑝𝑐𝑡) ⋅ℎ(𝑡+1,⌊𝑙𝑝𝑐𝑡⌋)h(t,l)=h(t+1,l)+∑c∈N∗f(ptc)⋅h(t+1,⌊lptc⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共有 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别种取值，所以直接转移复杂度为 𝑂(√𝑛⋅√𝑛ln⁡√𝑛) =𝑂(𝑛log⁡𝑛)O(n⋅nln⁡n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，需要优化．

与 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的优化方式类似，注意到 𝑝𝑡 >𝑙pt>l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，能用 𝑝𝑡,𝑝𝑡+1,…,𝑝𝑚pt,pt+1,…,pm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组成的数只有 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时的 ℎ(𝑡,𝑙) =𝑓(1) =1h(t,l)=f(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

类似的，推出 ∀𝑝2𝑡 >𝑙,ℎ(𝑡,𝑙) =ℎ(𝑡 +1,𝑙) +𝑓(𝑝𝑡)∀pt2>l,h(t,l)=h(t+1,l)+f(pt)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

所以一旦发现 𝑝2𝑡 >𝑙pt2>l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就停止转移，记此时的 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑡𝑙tl![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，之后用到 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，把此时的 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值加上 min(𝑙,√𝑛)∑𝑖=𝑝𝑡𝑙[𝑖 ∈ℙ]𝑓(𝑖)∑i=ptlmin(l,n)[i∈P]f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

时间复杂度被优化至 𝑂(𝑛34log⁡𝑛)O(n34log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 求和

算出了 Part 1 和 Part 2 的答案，将其相加即为 𝑛∑𝑖=1𝑓(𝑖)∑i=1nf(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 参考

[积性函数线性筛/杜教筛/洲阁筛学习笔记 | Bill Yang's Blog](https://blog.bill.moe/multiplicative-function-sieves-notes)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/zhou.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/zhou.md "edit.link.title")  
>  __本页面贡献者：[Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [AlephInfinity1](https://github.com/AlephInfinity1), [billchenchina](https://github.com/billchenchina), [CCXXXI](https://github.com/CCXXXI), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Nanarikom](https://github.com/Nanarikom), [ouuan](https://github.com/ouuan), [scp020](https://github.com/scp020), [shuzhouliu](https://github.com/shuzhouliu), [StudyingFather](https://github.com/StudyingFather)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
