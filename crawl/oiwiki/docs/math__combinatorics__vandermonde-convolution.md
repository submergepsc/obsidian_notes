# 范德蒙德卷积 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/vandermonde-convolution/

# 范德蒙德卷积

## 引入

范德蒙德卷积是一种合并组合数的式子，主要应用于组合数学的公式推导．

## 范德蒙德卷积公式

𝑘∑𝑖=0(𝑛𝑖)(𝑚𝑘−𝑖)=(𝑛+𝑚𝑘)∑i=0k(ni)(mk−i)=(n+mk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 证明

考虑用二项式定理证明：

𝑛+𝑚∑𝑘=0(𝑛+𝑚𝑘)𝑥𝑘=(𝑥+1)𝑛+𝑚=(𝑥+1)𝑛(𝑥+1)𝑚=𝑛∑𝑟=0(𝑛𝑟)𝑥𝑟𝑚∑𝑠=0(𝑚𝑠)𝑥𝑠=𝑛+𝑚∑𝑘=0𝑘∑𝑟=0(𝑛𝑟)(𝑚𝑘−𝑟)𝑥𝑘∑k=0n+m(n+mk)xk=(x+1)n+m=(x+1)n(x+1)m=∑r=0n(nr)xr∑s=0m(ms)xs=∑k=0n+m∑r=0k(nr)(mk−r)xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即有：

(𝑛+𝑚𝑘)=𝑘∑𝑟=0(𝑛𝑟)(𝑚𝑘−𝑟)(n+mk)=∑r=0k(nr)(mk−r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若考虑其组合意义证明：

在一个大小为 𝑛 +𝑚n+m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合中取出 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数，可以等于把大小为 𝑛 +𝑚n+m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合拆成两个集合，大小分别为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中取出 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数，从 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中取出 𝑘 −𝑖k−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数的方案数．由于我们有了对于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的枚举，于是只需要考虑一种拆法，因为不同的拆法之间是等价的．

## 推论

### 推论 1 及证明

𝑠∑𝑖=−𝑟(𝑛𝑟+𝑖)(𝑚𝑠−𝑖)=(𝑛+𝑚𝑟+𝑠)∑i=−rs(nr+i)(ms−i)=(n+mr+s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明与原公式证明相似．

### 推论 2 及证明

𝑛∑𝑖=1(𝑛𝑖)(𝑛𝑖−1)=(2𝑛𝑛−1)∑i=1n(ni)(ni−1)=(2nn−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据基础的组合数学知识推导，有：

𝑛∑𝑖=1(𝑛𝑖)(𝑛𝑖−1)=𝑛−1∑𝑖=0(𝑛𝑖+1)(𝑛𝑖)=𝑛−1∑𝑖=0(𝑛𝑛−1−𝑖)(𝑛𝑖)=(2𝑛𝑛−1)∑i=1n(ni)(ni−1)=∑i=0n−1(ni+1)(ni)=∑i=0n−1(nn−1−i)(ni)=(2nn−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 推论 3 及证明

𝑛∑𝑖=0(𝑛𝑖)2=(2𝑛𝑛)∑i=0n(ni)2=(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据基础的组合数学知识推导，有：

𝑛∑𝑖=0(𝑛𝑖)2=𝑛∑𝑖=0(𝑛𝑖)(𝑛𝑛−𝑖)=(2𝑛𝑛)∑i=0n(ni)2=∑i=0n(ni)(nn−i)=(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 推论 4 及证明

𝑚∑𝑖=0(𝑛𝑖)(𝑚𝑖)=(𝑛+𝑚𝑚)∑i=0m(ni)(mi)=(n+mm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据基础的组合数学知识推导，有：

𝑚∑𝑖=0(𝑛𝑖)(𝑚𝑖)=𝑚∑𝑖=0(𝑛𝑖)(𝑚𝑚−𝑖)=(𝑛+𝑚𝑚)∑i=0m(ni)(mi)=∑i=0m(ni)(mm−i)=(n+mm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 (𝑛+𝑚𝑚)(n+mm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是我们较为熟悉的网格图路径计数的方案数．所以我们可以考虑其组合意义的证明．

在一张网格图中，从 (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 走到 (𝑛,𝑚)(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共走 𝑛 +𝑚n+m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步．规定 (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位于网格图左上角，其中向下走了 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步，向右走了 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步，方案数为 (𝑛+𝑚𝑚)(n+mm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

换个视角，我们将 𝑛 +𝑚n+m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步拆成两部分走，先走 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步，再走 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步，那么 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步中若有 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步向右，则 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步中就有 𝑚 −𝑖m−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步向右，故得证．

## 习题

  * [CF785D Anton and School - 2](https://codeforces.com/problemset/problem/785/D)

  * [洛谷 P2791 幼儿园篮球题](https://www.luogu.com.cn/problem/P2791)

## 参考资料与注释

  1. [Vandermonde's Convolution Formula](https://www.cut-the-knot.org/arithmetic/algebra/VandermondeConvolution.shtml)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/vandermonde-convolution.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/vandermonde-convolution.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [ChungZH](https://github.com/ChungZH), [tidongCrazy](https://github.com/tidongCrazy)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
