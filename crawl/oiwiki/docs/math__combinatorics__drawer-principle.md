# 抽屉原理 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/drawer-principle/

# 抽屉原理

## 定义

抽屉原理，亦称鸽巢原理（the pigeonhole principle）．

它常被用于证明存在性证明和求最坏情况下的解．

## 简单情况

将 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物体，划分为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组，那么有至少一组有两个（或以上）的物体．

这个定理看起来比较显然，证明方法考虑反证法：假如每个分组有至多 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物体，那么最多有 1 ×𝑛1×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物体，而实际上有 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物体，矛盾．

## 推广

将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物体，划分为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组，那么至少存在一个分组，含有大于或等于 ⌈𝑛𝑘⌉⌈nk⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物品．

推广的形式也可以使用反证法证明：若每个分组含有小于 ⌈𝑛𝑘⌉⌈nk⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个物体，则其总和 𝑆 ≤(⌈𝑛𝑘⌉ −1) ×𝑘 =𝑘⌈𝑛𝑘⌉ −𝑘 <𝑘(𝑛𝑘 +1) −𝑘 =𝑛S≤(⌈nk⌉−1)×k=k⌈nk⌉−k<k(nk+1)−k=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矛盾．

此外，划分还可以弱化为覆盖结论不变．  
给定集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 一个 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非空子集构成的簇 {𝐴1,𝐴2…𝐴𝑘}{A1,A2…Ak}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 若满足 ⋃𝑘𝑖=1𝐴𝑖⋃i=1kAi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则称为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个覆盖（cover）
  * 若一个覆盖还满足 𝑖 ≠𝑗 →𝐴𝑖 ∩𝐴𝑗 =∅i≠j→Ai∩Aj=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则称为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个划分．

鸽巢原理可以有如下叙述：对于 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个覆盖 {𝐴1,𝐴2…𝐴𝑘}{A1,A2…Ak}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有至少一个集合 𝐴𝑖Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 |𝐴𝑖| ≥⌈|𝑆|𝑘⌉|Ai|≥⌈|S|k⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 参考文献

  * [Wikipedia: Pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle)
  *  _Discrete Mathematics and Its Applications_ : Chapter 6, Section 1

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/drawer-principle.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/drawer-principle.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [MegaOwIer](https://github.com/MegaOwIer), [Tiphereth-A](https://github.com/Tiphereth-A), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid), [aofall](https://github.com/aofall), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Great-designer](https://github.com/Great-designer), [hehelego](mailto:2364261262@qq.com), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [Persdre](https://github.com/Persdre), [ranwen](https://github.com/ranwen), [shuzhouliu](https://github.com/shuzhouliu), [william-song-shy](https://github.com/william-song-shy)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
