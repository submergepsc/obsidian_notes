# 猫树 - OI Wiki

- Source: https://oi-wiki.org/ds/cat-tree/

# 猫树

## 引入

众所周知线段树可以支持高速查询某一段区间的信息和，比如区间最大子段和，区间和，区间矩阵的连乘积等等．

但是有一个问题在于普通线段树的区间询问在某些毒瘤的眼里可能还是有些慢了．

简单来说就是线段树建树的时候需要做 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次合并操作，而每一次区间询问需要做 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次合并操作，询问区间和这种东西的时候还可以忍受，但是当我们需要询问区间线性基这种合并复杂度高达 𝑂(log2⁡𝑤)O(log2⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的信息的话，此时就算是做 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次合并有些时候在时间上也是不可接受的．

而所谓「猫树」就是一种不支持修改，仅仅支持快速区间询问的一种静态线段树．

构造一棵这样的静态线段树需要 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次合并操作，但是此时的查询复杂度被加速至 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次合并操作．

在处理线性基这样特殊的信息的时候甚至可以将复杂度降至 𝑂(𝑛log2⁡𝑤)O(nlog2⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 原理

在查询 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这段区间的信息和的时候，将线段树树上代表 [𝑙,𝑙][l,l]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的节点和代表 [𝑟,𝑟][r,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这段区间的节点在线段树上的 LCA 求出来，设这个节点 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表的区间为 [𝐿,𝑅][L,R]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们会发现一些非常有趣的性质：

  1. [𝐿,𝑅][L,R]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这个区间一定包含 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．显然，因为它既是 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的祖先又是 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的祖先．

  2. [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这个区间一定跨越 [𝐿,𝑅][L,R]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的中点．由于 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 LCA，这意味着 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左儿子是 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的祖先而不是 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的祖先，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右儿子是 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的祖先而不是 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的祖先．因此，𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定在 [𝐿,mid][L,mid]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这个区间内，𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定在 (mid,𝑅](mid,R]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这个区间内．

有了这两个性质，我们就可以将询问的复杂度降至 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了．

## 实现

具体来讲我们建树的时候对于线段树树上的一个节点，设它代表的区间为 (𝑙,𝑟](l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

不同于传统线段树在这个节点里只保留 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的和，我们在这个节点里面额外保存 (𝑙,mid](l,mid]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后缀和数组和 (mid,𝑟](mid,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和数组．

这样的话建树的复杂度为 𝑇(𝑛) =2𝑇(𝑛/2) +𝑂(𝑛) =𝑂(𝑛log⁡𝑛)T(n)=2T(n/2)+O(n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同理空间复杂度也从原来的 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变成了 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

下面是最关键的询问了．

如果我们询问的区间是 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么我们把代表 [𝑙,𝑙][l,l]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的节点和代表 [𝑟,𝑟][r,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的节点的 LCA 求出来，记为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

根据刚才的两个性质，𝑙,𝑟l,r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所包含的区间之内并且一定跨越了 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的中点．

这意味这一个非常关键的事实是我们可以使用 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 里面的前缀和数组和后缀和数组，将 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拆成 [𝑙,mid] +(mid,𝑟][l,mid]+(mid,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从而拼出来 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这个区间．

而这个过程仅仅需要 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次合并操作！

不过我们好像忽略了点什么？

似乎求 LCA 的复杂度似乎还不是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，暴力求是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，倍增法则是 𝑂(log⁡log⁡𝑛)O(log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，转 ST 表的代价又太大……

## 堆式建树

具体来将我们将这个序列补成 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整次幂，然后建线段树．

此时我们发现线段树上两个节点的 LCA 编号，就是两个节点二进制编号的最长公共前缀 LCP．

稍作思考即可发现发现在 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制下 `lcp(x,y)=x>>digits[x^y]`．（其中 `digits[x]` 表示二进制下 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位数，即 ⌊log2⁡𝑥⌋ +1⌊log2⁡x⌋+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

所以我们预处理一个 `digits` 数组即可轻松完成求 LCA 的工作．

这样我们就构建了一个猫树．

由于建树的时候涉及到求前缀和和求后缀和，所以对于线性基这种虽然合并是 𝑂(log2⁡𝑤)O(log2⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 但是求前缀和却是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的信息，使用猫树可以将静态区间线性基从 𝑂(𝑛log2⁡𝑤 +𝑚log2⁡𝑤log⁡𝑛)O(nlog2⁡w+mlog2⁡wlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 优化至 𝑂(𝑛log⁡𝑛log⁡𝑤 +𝑚log2⁡𝑤)O(nlog⁡nlog⁡w+mlog2⁡w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度．

### 参考

  * [immortalCO 的博客](https://immortalco.blog.uoj.ac/blog/2102)
  * [[Kle77]](http://ieeexplore.ieee.org/document/1675628/) V. Klee, "Can the Measure of be Computed in Less than O (n log n) Steps?," Am. Math. Mon., vol. 84, no. 4, pp. 284–285, Apr. 1977.
  * [[BeW80]](https://www.tandfonline.com/doi/full/10.1080/00029890.1977.11994336) Bentley and Wood, "An Optimal Worst Case Algorithm for Reporting Intersections of Rectangles," IEEE Trans. Comput., vol. C–29, no. 7, pp. 571–577, Jul. 1980.

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/cat-tree.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/cat-tree.md "edit.link.title")  
>  __本页面贡献者：[hcx2012Git](https://github.com/hcx2012Git), [Tiphereth-A](https://github.com/Tiphereth-A), [billchenchina](https://github.com/billchenchina), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [chenryang](https://github.com/chenryang), [chenzheAya](https://github.com/chenzheAya), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [CJSoft](https://github.com/CJSoft), [cjsoft](https://github.com/cjsoft), [countercurrent-time](https://github.com/countercurrent-time), [DawnMagnet](https://github.com/DawnMagnet), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [ethan-enhe](https://github.com/ethan-enhe), [GavinZhengOI](https://github.com/GavinZhengOI), [Haohu Shen](https://github.com/Haohu Shen), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [hjsjhn](https://github.com/hjsjhn), [hly1204](https://github.com/hly1204), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [jaxvanyang](https://github.com/jaxvanyang), [Jebearssica](https://github.com/Jebearssica), [kenlig](https://github.com/kenlig), [konnyakuxzy](https://github.com/konnyakuxzy), [ksyx](https://github.com/ksyx), [luoguojie](https://github.com/luoguojie), [Marcythm](https://github.com/Marcythm), [megakite](https://github.com/megakite), [Menci](https://github.com/Menci), [moon-dim](https://github.com/moon-dim), [NachtgeistW](https://github.com/NachtgeistW), [onelittlechildawa](https://github.com/onelittlechildawa), [orzAtalod](https://github.com/orzAtalod), [ouuan](https://github.com/ouuan), [shadowice1984](https://github.com/shadowice1984), [shawlleyw](https://github.com/shawlleyw), [shuzhouliu](https://github.com/shuzhouliu), [StudyingFather](https://github.com/StudyingFather), [SukkaW](https://github.com/SukkaW), [wy-luke](https://github.com/wy-luke), [x2e6](https://github.com/x2e6), [Xeonacid](https://github.com/Xeonacid), [Ycrpro](https://github.com/Ycrpro), [yifan0305](https://github.com/yifan0305), [zeningc](https://github.com/zeningc)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
