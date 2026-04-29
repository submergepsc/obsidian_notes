# 错位排列 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/derangement/

# 错位排列

## 错位排列

### 定义

错位排列（derangement）是没有任何元素出现在其有序位置的排列．即，对于 1 ∼𝑛1∼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排列 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果满足 𝑃𝑖 ≠𝑖Pi≠i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的错位排列．

例如，三元错位排列有 {2,3,1}{2,3,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 {3,1,2}{3,1,2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．四元错位排列有 {2,1,4,3}{2,1,4,3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、{2,3,4,1}{2,3,4,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、{2,4,1,3}{2,4,1,3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、{3,1,4,2}{3,1,4,2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、{3,4,1,2}{3,4,1,2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、{3,4,2,1}{3,4,2,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、{4,1,2,3}{4,1,2,3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、{4,3,1,2}{4,3,1,2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 {4,3,2,1}{4,3,2,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．错位排列是没有不动点的排列，即没有长度为 1 的循环．

### 容斥原理的计算

全集 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为 1 ∼𝑛1∼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排列，|𝑈| =𝑛!|U|=n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；令 𝑆𝑖Si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是其中满足 𝑃𝑖 ≠𝑖Pi≠i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排列．运用补集和 [容斥原理](../inclusion-exclusion-principle/) 的知识，问题变成求：

∣𝑛⋂𝑖=1𝑆𝑖∣=|𝑈|−∣𝑛⋃𝑖=1――𝑆𝑖∣=𝑛!−𝑛∑𝑘=1(−1)𝑘−1∑𝑎𝑖<𝑎𝑖+1∣𝑘⋂𝑖=1―――𝑆𝑎𝑖∣|⋂i=1nSi|=|U|−|⋃i=1nSi―|=n!−∑k=1n(−1)k−1∑ai<ai+1|⋂i=1kSai―|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中求和的含义是 1,2,⋯,𝑛1,2,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中取 𝑎1,𝑎2,⋯,𝑎𝑘a1,a2,⋯,ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且满足 𝑎𝑖 <𝑎𝑖+1ai<ai+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．于是

∣𝑘⋂𝑖=1―――𝑆𝑎𝑖∣|⋂i=1kSai―|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

表示有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数 𝑎1,𝑎2,⋯,𝑎𝑘a1,a2,⋯,ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑃𝑎𝑖 =𝑎𝑖Pai=ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而剩下 𝑛 −𝑘n−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数的位置任意的排列数，因此：

∣𝑘⋂𝑖=1―――𝑆𝑎𝑖∣=(𝑛−𝑘)!|⋂i=1kSai―|=(n−k)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数的选择情况共 (𝑛𝑘)(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种，对其求和有：

𝑛∑𝑘=1(−1)𝑘−1∑𝑎𝑖<𝑎𝑖+1∣𝑘⋂𝑖=1―――𝑆𝑎𝑖∣=𝑛∑𝑘=1(−1)𝑘−1(𝑛𝑘)(𝑛−𝑘)!=𝑛∑𝑘=1(−1)𝑘−1𝑛!𝑘!=𝑛!𝑛∑𝑘=1(−1)𝑘−1𝑘!∑k=1n(−1)k−1∑ai<ai+1|⋂i=1kSai―|=∑k=1n(−1)k−1(nk)(n−k)!=∑k=1n(−1)k−1n!k!=n!∑k=1n(−1)k−1k!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的错位排列数为：

𝐷𝑛=𝑛!−𝑛!𝑛∑𝑘=1(−1)𝑘−1𝑘!=𝑛!𝑛∑𝑘=0(−1)𝑘𝑘!Dn=n!−n!∑k=1n(−1)k−1k!=n!∑k=0n(−1)kk!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

错位排列数列的前几项为 0,1,2,9,44,2650,1,2,9,44,265![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（[OEIS A000166](http://oeis.org/A000166)）．

### 递推的计算

把错位排列问题具体化，考虑这样一个问题：

𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 封不同的信，编号分别是 1,2,3,4,51,2,3,4,5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，现在要把这五封信放在编号 1,2,3,4,51,2,3,4,5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的信封中，要求信封的编号与信的编号不一样．问有多少种不同的放置方法？

假设考虑到第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个信封，初始时暂时把第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 封信放在第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个信封中，然后考虑两种情况的递推：

  * 前面 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个信封全部装错；
  * 前面 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个信封有一个没有装错其余全部装错．

对于第一种情况，前面 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个信封全部装错：因为前面 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个已经全部装错了，所以第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 封只需要与前面任一一个位置交换即可，总共有 𝐷𝑛−1 ×(𝑛 −1)Dn−1×(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种情况．

对于第二种情况，前面 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个信封有一个没有装错其余全部装错：考虑这种情况的目的在于，若 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个信封中如果有一个没装错，那么把那个没装错的与 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 交换，即可得到一个全错位排列情况．

其他情况，不可能通过一次操作来把它变成一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的错排．

于是可得，错位排列数满足递推关系：

𝐷𝑛=(𝑛−1)(𝐷𝑛−1+𝐷𝑛−2)Dn=(n−1)(Dn−1+Dn−2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里也给出另一个递推关系：

𝐷𝑛=𝑛𝐷𝑛−1+(−1)𝑛Dn=nDn−1+(−1)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 其他关系

错位排列数有一个简单的取整表达式，增长速度与阶乘仅相差常数：

𝐷𝑛=⌊𝑛!e+12⌋Dn=⌊n!e+12⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

随着元素数量的增加，形成错位排列的概率 P 接近：

𝑃=lim𝑛→∞𝐷𝑛𝑛!=1eP=limn→∞Dnn!=1e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

* * *

>  __本页面最近更新： 2026/3/25 06:20:21，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/derangement.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/derangement.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Great-designer](https://github.com/Great-designer), [amlhdsan](https://github.com/amlhdsan), [BeiChenStanly](https://github.com/BeiChenStanly), [Enter-tainer](https://github.com/Enter-tainer), [untitledunrevised](https://github.com/untitledunrevised), [xzdeyg](https://github.com/xzdeyg)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
