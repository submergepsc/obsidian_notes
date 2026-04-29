# 希尔排序 - OI Wiki

- Source: https://oi-wiki.org/basic/shell-sort/

# 希尔排序

本页面将简要介绍希尔排序．

## 定义

希尔排序（英语：Shell sort），也称为缩小增量排序法，是 [插入排序](../insertion-sort/) 的一种改进版本．希尔排序以它的发明者希尔（英语：Donald Shell）命名．

## 过程

排序对不相邻的记录进行比较和移动：

  1. 将待排序序列分为若干子序列（每个子序列的元素在原始数组中间距相同）；
  2. 对这些子序列进行插入排序；
  3. 减小每个子序列中元素之间的间距，重复上述过程直至间距减少为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 性质

### 稳定性

希尔排序是一种不稳定的排序算法．

### 时间复杂度

希尔排序的最优时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

希尔排序的平均时间复杂度和最坏时间复杂度与间距序列的选取有关．设间距序列为 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，下面给出 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的两种经典选取方式，这两种选取方式均使得排序算法的复杂度降为 𝑜(𝑛2)o(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别．

命题 1

若间距序列为 𝐻 ={2𝑘 −1 ∣𝑘 =1,2,…,⌊log2⁡𝑛⌋}H={2k−1∣k=1,2,…,⌊log2⁡n⌋}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（从大到小），则希尔排序算法的时间复杂度为 𝑂(𝑛3/2)O(n3/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

命题 2

若间距序列为 𝐻 ={𝑘 =2𝑝 ⋅3𝑞 ∣𝑝,𝑞 ∈ℕ,𝑘 ≤𝑛}H={k=2p⋅3q∣p,q∈N,k≤n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（从大到小），则希尔排序算法的时间复杂度为 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

为证明这两个命题，我们先给出一个重要的定理并证明它，这个定理反应了希尔排序的最主要特征．

定理 1

只要程序执行了一次 InsertionSort(ℎ)InsertionSort(h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不管之后怎样调用 InsertionSortInsertionSort![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 函数，𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组怎样变换，下列性质均会被一直保持：

𝐴1,𝐴1+ℎ,𝐴1+2ℎ,…𝐴2,𝐴2+ℎ,𝐴2+2ℎ,…⋮𝐴ℎ,𝐴ℎ+ℎ,𝐴ℎ+2ℎ,…A1,A1+h,A1+2h,…A2,A2+h,A2+2h,…⋮Ah,Ah+h,Ah+2h,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

接下来我们证明定理 1．

我们先证明引理 1．

引理 1

对于整数 𝑛,𝑚n,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、正整数 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与两个数组 𝑋(𝑥1,𝑥2,…,𝑥𝑛+𝑙),𝑌(𝑦1,𝑦2,…,𝑦𝑚+𝑙)X(x1,x2,…,xn+l),Y(y1,y2,…,ym+l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足如下要求：

𝑦1≤𝑥𝑛+1,𝑦2≤𝑥𝑛+2,…,𝑦𝑙≤𝑥𝑛+𝑙y1≤xn+1,y2≤xn+2,…,yl≤xn+l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则我们将两个数组分别升序排序后，上述要求依然成立．

引理 1 证明

设数组 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 排序完为数组 𝑋′(𝑥′1,…,𝑥′𝑛+𝑙)X′(x1′,…,xn+l′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，数组 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 排序完为数组 𝑌′(𝑦′1,…,𝑦′𝑚+𝑙)Y′(y1′,…,ym+l′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于任何 1 ≤𝑖 ≤𝑙1≤i≤l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥′𝑛+𝑖xn+i′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小等于数组 𝑋′X′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝑙 −𝑖l−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素，也小等于数组 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝑙 −𝑖l−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素（这是因为 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑋′X′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素可重集合是相同的）．

那么在可重集合 {𝑥𝑛+1,…,𝑥𝑛+𝑙} ⊂𝑋{xn+1,…,xn+l}⊂X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，大等于 𝑥′𝑛+𝑖xn+i′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素个数不超过 𝑙 −𝑖l−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．

进而小于 𝑥′𝑛+𝑖xn+i′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素个数至少有 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，取出其中的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，设它们为 𝑥𝑛+𝑘1,𝑥𝑛+𝑘2,…,𝑥𝑛+𝑘𝑖xn+k1,xn+k2,…,xn+ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．于是有：

𝑦𝑘1≤𝑥𝑛+𝑘1≤𝑥′𝑛+𝑖,𝑦𝑘2≤𝑥𝑛+𝑘2≤𝑥′𝑛+𝑖,…,𝑦𝑘𝑖≤𝑥𝑛+𝑘𝑖≤𝑥′𝑛+𝑖yk1≤xn+k1≤xn+i′,yk2≤xn+k2≤xn+i′,…,yki≤xn+ki≤xn+i′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以 𝑥′𝑛+𝑖xn+i′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至少大于等于 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也即 𝑌′Y′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素，那么自然有 𝑦′𝑖 ≤𝑥′𝑛+𝑖 (1 ≤𝑖 ≤𝑙)yi′≤xn+i′(1≤i≤l)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

再回到原命题的证明：

我们实际上只需要证明调用完 InsertionSort(ℎ)InsertionSort(h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的紧接着下一次调用 InsertionSort(𝑘)InsertionSort(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子列仍有序即可，之后容易用归纳法得出．下面只考虑下一个调用：

执行完 InsertionSort(ℎ)InsertionSort(h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，如下组已经完成排序：

𝐴1,𝐴1+ℎ,𝐴1+2ℎ,…𝐴2,𝐴2+ℎ,𝐴2+2ℎ,…⋮𝐴ℎ,𝐴ℎ+ℎ,𝐴ℎ+2ℎ,…A1,A1+h,A1+2h,…A2,A2+h,A2+2h,…⋮Ah,Ah+h,Ah+2h,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而之后执行 InsertionSort(𝑘)InsertionSort(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则会将如下组排序：

𝐴1,𝐴1+𝑘,𝐴1+2𝑘,…𝐴2,𝐴2+𝑘,𝐴2+2𝑘,…⋮𝐴𝑘,𝐴𝑘+𝑘,𝐴𝑘+2𝑘,…A1,A1+k,A1+2k,…A2,A2+k,A2+2k,…⋮Ak,Ak+k,Ak+2k,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于每个 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) (1 ≤𝑖 ≤min(ℎ,𝑘))(1≤i≤min(h,k))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考虑如下两个组：

𝐴𝑖,𝐴𝑖+𝑘,𝐴𝑖+2𝑘,……,𝐴𝑖+ℎ,𝐴𝑖+ℎ+𝑘,𝐴𝑖+ℎ+2𝑘,…Ai,Ai+k,Ai+2k,……,Ai+h,Ai+h+k,Ai+h+2k,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

第二个组前面也加上「……![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」的原因是可能 𝑖 +ℎ ≥𝑘i+h≥k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从而前面也有元素．

则第二个组就是引理 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组，第一个组就是 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组，𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是第二个组从 𝑖 +ℎi+h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之后顶到末尾的长度，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是第二个组中前面那个「……![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」的长度，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是第一个组去掉前 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个后剩下的个数．

又因为有：

𝐴𝑖≤𝐴𝑖+ℎ,𝐴𝑖+𝑘≤𝐴𝑖+ℎ+𝑘,…Ai≤Ai+h,Ai+k≤Ai+h+k,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以由引理 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可得执行 InsertionSort(𝑘)InsertionSort(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将两个组分别排序后，这个关系依然满足，即依然有 𝐴𝑖 ≤𝐴𝑖+ℎ (1 ≤𝑖 ≤min(ℎ,𝑘))Ai≤Ai+h(1≤i≤min(h,k))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

若有 𝑖 >min(ℎ,𝑘)i>min(h,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，容易发现取正整数 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) (1 ≤𝑤 ≤min(ℎ,𝑘))(1≤w≤min(h,k))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再加上若干个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可得到 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则之前的情况已经蕴含了此情况的证明．

综合以上论述便有：执行完 InsertionSort(𝑘)InsertionSort(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 依然有 𝐴𝑖 ≤𝐴𝑖+ℎ (1 ≤𝑖 ≤𝑛 −ℎ)Ai≤Ai+h(1≤i≤n−h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此定理 1 得证．

这个定理揭示了希尔排序在特定集合 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下可以优化复杂度的关键，因为在整个过程中，它可以一致保持前面的成果不被摧毁（即 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个子列分别有序），从而使后面的调用中，指针 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的移动次数大大减少．

接下来我们单拎出来一个数论引理进行证明．这个定理在 OI 界因 [小凯的疑惑](https://www.luogu.com.cn/problem/P3951) 一题而大为出名．而在希尔排序复杂度的证明中，它也使得定理 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到了很大的扩展．

引理 2

若 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为正整数且互素，则不在集合 {𝑎𝑥 +𝑏𝑦 ∣𝑥,𝑦 ∈ℕ}{ax+by∣x,y∈N}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的最大正整数为 𝑎𝑏 −𝑎 −𝑏ab−a−b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

引理 2 证明

分两步证明：

  * 先证明方程 𝑎𝑥 +𝑏𝑦 =𝑎𝑏 −𝑎 −𝑏ax+by=ab−a−b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为非负整数的解：

若无非负整数的限制，容易得到两组解 (𝑏 −1, −1),( −1,𝑎 −1)(b−1,−1),(−1,a−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

通过其通解形式 𝑥 =𝑥0 +𝑡𝑏,𝑦 =𝑦0 −𝑡𝑎x=x0+tb,y=y0−ta![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，容易得到上面两组解是「相邻」的（因为 𝑏 −1 −𝑏 = −1b−1−b=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

当 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递增时，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递增，𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递减，所以如果方程有非负整数解，必然会夹在这两组解中间，但这两组解「相邻」，中间没有别的解．

故不可能有非负整数解．

  * 再证明对任意整数 𝑐 >𝑎𝑏 −𝑎 −𝑏c>ab−a−b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，方程 𝑎𝑥 +𝑏𝑦 =𝑐ax+by=c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有非负整数解：

我们找一组解 (𝑥0,𝑦0)(x0,y0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 0 ≤𝑥0 <𝑏0≤x0<b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（由通解的表达式，这可以做到）．

则有：

𝑏𝑦0=𝑐−𝑎𝑥0≥𝑐−𝑎(𝑏−1)>𝑎𝑏−𝑎−𝑏−𝑎𝑏+𝑎=−𝑏by0=c−ax0≥c−a(b−1)>ab−a−b−ab+a=−b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以 𝑏(𝑦0 +1) >0b(y0+1)>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又因为 𝑏 >0b>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑦0 +1 >0y0+1>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑦0 ≥0y0≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

所以 (𝑥0,𝑦0)(x0,y0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一组非负整数解．

综上得证．

而下面这个定理则揭示了引理 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是如何扩展定理 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

定理 2

如果 gcd(ℎ𝑡+1,ℎ𝑡) =1gcd(ht+1,ht)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则程序先执行完 InsertionSort(ℎ𝑡+1)InsertionSort(ht+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 InsertionSort(ℎ𝑡)InsertionSort(ht)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，执行 InsertionSort(ℎ𝑡−1)InsertionSort(ht−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度为 𝑂(𝑛ℎ𝑡+1ℎ𝑡ℎ𝑡−1)O(nht+1htht−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且对于每个 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的移动次数是 𝑂(ℎ𝑡+1ℎ𝑡ℎ𝑡−1)O(ht+1htht−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别的．

定理 2 证明

对于 𝑗 ≤ℎ𝑡+1ℎ𝑡j≤ht+1ht![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的部分，𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的移动次数显然是是 𝑂(ℎ𝑡+1ℎ𝑡ℎ𝑡−1)O(ht+1htht−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别的．

故以下假设 𝑗 >ℎ𝑡+1ℎ𝑡j>ht+1ht![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于任意的正整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 1 ≤𝑘 ≤𝑗 −ℎ𝑡+1ℎ𝑡1≤k≤j−ht+1ht![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，注意到：ℎ𝑡+1ℎ𝑡 −ℎ𝑡+1 −ℎ𝑡 <ℎ𝑡+1ℎ𝑡 ≤𝑗 −𝑘 ≤𝑗 −1ht+1ht−ht+1−ht<ht+1ht≤j−k≤j−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

又因为 gcd(ℎ𝑡+1,ℎ𝑡) =1gcd(ht+1,ht)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故由引理 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得存在非负整数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得：𝑎ℎ𝑡+1 +𝑏ℎ𝑡 =𝑗 −𝑘aht+1+bht=j−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

即得：

𝑘=𝑗−𝑎ℎ𝑡+1−𝑏ℎ𝑡k=j−aht+1−bht![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由定理 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得：

𝐴𝑗−𝑏ℎ𝑡≤𝐴𝑗−(𝑏−1)ℎ𝑡≤…≤𝐴𝑗−ℎ𝑡≤𝐴𝑗Aj−bht≤Aj−(b−1)ht≤…≤Aj−ht≤Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

与

𝐴𝑗−𝑏ℎ𝑡−𝑎ℎ𝑡+1≤𝐴𝑗−𝑏ℎ𝑡−(𝑎−1)ℎ𝑡+1≤…≤𝐴𝑗−𝑏ℎ𝑡−ℎ𝑡+1≤𝐴𝑗−𝑏ℎ𝑡Aj−bht−aht+1≤Aj−bht−(a−1)ht+1≤…≤Aj−bht−ht+1≤Aj−bht![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

综合以上既有：𝐴𝑘 =𝐴𝑗−𝑎ℎ𝑡+1−𝑏ℎ𝑡 ≤𝐴𝑗Ak=Aj−aht+1−bht≤Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

所以对于任何 1 ≤𝑘 ≤𝑗 −ℎ𝑡+1ℎ𝑡1≤k≤j−ht+1ht![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝐴𝑘 ≤𝐴𝑗Ak≤Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在 Shell-Sort 伪代码中 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指针每次减 ℎ𝑡−1ht−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，减 𝑂(ℎ𝑡+1ℎ𝑡ℎ𝑡−1)O(ht+1htht−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，即可使得 𝑖 ≤𝑗 −ℎ𝑡+1ℎ𝑡i≤j−ht+1ht![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进而有 𝐴𝑖 ≤𝐴𝑗Ai≤Aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不满足 while 循环的条件退出．

证明完对于每个 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的移动复杂度后，即可得到总的时间复杂度：

𝑛∑𝑗=ℎ𝑡−1+1𝑂(ℎ𝑡+1ℎ𝑡ℎ𝑡−1)=𝑂(𝑛ℎ𝑡+1ℎ𝑡ℎ𝑡−1)∑j=ht−1+1nO(ht+1htht−1)=O(nht+1htht−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

得证．

认真观察定理 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的证明过程，可以发现：定理 1 可以进行「线性组合」，即 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为间隔有序，以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为间隔亦有序，则以 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非负系数线性组合仍是有序的．而这种「线性性」即是由引理 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 保证的．

有了这两个定理，我们可以证明命题 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

命题 1 证明

将 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 写为序列的形式：

𝐻(ℎ1=1,ℎ2=3,ℎ3=7,…,ℎ⌊log2⁡𝑛⌋=2⌊log2⁡𝑛⌋−1)H(h1=1,h2=3,h3=7,…,h⌊log2⁡n⌋=2⌊log2⁡n⌋−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Shell-Sort 执行顺序为：InsertionSort(ℎ⌊log2⁡𝑛⌋),InsertionSort(ℎ⌊log2⁡𝑛⌋−1),…,InsertionSort(ℎ2),InsertionSort(ℎ1)InsertionSort(h⌊log2⁡n⌋),InsertionSort(h⌊log2⁡n⌋−1),…,InsertionSort(h2),InsertionSort(h1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

分两部分去分析复杂度：

  * 对于前面的若干个满足 ℎ𝑡 ≥√𝑛ht≥n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 ℎ𝑡ht![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然有 InsertionSort(ℎ𝑡)InsertionSort(ht)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度为 𝑂(𝑛2ℎ𝑡)O(n2ht)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑对最接近 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的项 ℎ𝑘hk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

𝑂(𝑛2ℎ𝑡)=𝑂(𝑛3/2)O(n2ht)=O(n3/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而对于 𝑖 >𝑘i>k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 ℎ𝑖hi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为有 2ℎ𝑖 <ℎ𝑖+12hi<hi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以可得：

𝑂(𝑛2ℎ𝑖)=𝑂(𝑛3/2/2𝑖−𝑘)(𝑖>𝑘)O(n2hi)=O(n3/2/2i−k)(i>k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以大等于 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 部分的总时间复杂度为：

⌊log2⁡𝑛⌋∑𝑖=𝑘𝑂(𝑛3/2/2𝑖−𝑘)=𝑂(𝑛3/2)∑i=k⌊log2⁡n⌋O(n3/2/2i−k)=O(n3/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 对于后面剩下的满足 ℎ𝑡 <√𝑛ht<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的项，前两项的复杂度还是 𝑂(𝑛3/2)O(n3/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而对于后面的项 ℎ𝑡ht![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有定理 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可得时间复杂度为：

𝑂(𝑛ℎ𝑡+2ℎ𝑡+1ℎ𝑡)=𝑂(𝑛ℎ𝑡+2⋅ℎ𝑡+2/2ℎ𝑡+2/4)=𝑂(𝑛ℎ𝑡+2)O(nht+2ht+1ht)=O(nht+2⋅ht+2/2ht+2/4)=O(nht+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再次利用 2ℎ𝑖 <ℎ𝑖+12hi<hi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 性质可得此部分总时间复杂度为（下式中 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 沿用了上一种情况中的含义）：

2𝑂(𝑛3/2)+𝑘−3∑𝑖=1𝑂(𝑛ℎ𝑖+1)=𝑂(𝑛3/2)+𝑘−3∑𝑖=1𝑂(𝑛ℎ𝑘−1/2𝑘−𝑖−3)=𝑂(𝑛3/2)+𝑂(𝑛ℎ𝑘−1)=𝑂(𝑛3/2)2O(n3/2)+∑i=1k−3O(nhi+1)=O(n3/2)+∑i=1k−3O(nhk−1/2k−i−3)=O(n3/2)+O(nhk−1)=O(n3/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

综上可得总时间复杂度即为 𝑂(𝑛3/2)O(n3/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

命题 2 证明

注意到一个事实：如果已经执行过了 InsertionSort(2)InsertionSort(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 InsertionSort(3)InsertionSort(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么因为 2 ⋅3 −2 −3 =12⋅3−2−3=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以由定理 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每个元素只有与它相邻的前一个元素可能大于它，之前的元素全部都小于它．于是 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指针只需要最多两次就可以退出 while 循环．也就是说，此时再执行 InsertionSort(1)InsertionSort(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，复杂度降为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

更进一步：如果已经执行过了 InsertionSort(4)InsertionSort(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 InsertionSort(6)InsertionSort(6)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们考虑所有的下标为奇数的元素组成的子列与下标为偶数的元素组成的子列．则这相当于把这两个子列分别执行 InsertionSort(2)InsertionSort(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 InsertionSort(3)InsertionSort(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么也是一样，这时候再执行 InsertionSort(2)InsertionSort(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，相当于对两个子列分别执行 InsertionSort(1)InsertionSort(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也只需要两个序列和的级别，即 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度就可以将数组变为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 间隔有序．

不断归纳，就可以得到：如果已经执行过了 InsertionSort(2ℎ)InsertionSort(2h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 InsertionSort(3ℎ)InsertionSort(3h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则执行 InsertionSort(ℎ)InsertionSort(h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度也只有 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

接下来分为两部分分析复杂度：

  * 对于 ℎ𝑡 >𝑛/3ht>n/3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的部分，则执行每个 InsertionSort(ℎ𝑡)InsertionSort(ht)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度为 𝑂(𝑛2/ℎ𝑡)O(n2/ht)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

而 𝑛2/ℎ𝑡 <3𝑛n2/ht<3n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以单词插入排序复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

而这一部分元素个数是 𝑂(log2⁡𝑛)O(log2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别的，所以这一部分时间复杂度为 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 对于 ℎ𝑡 ≤𝑛/3ht≤n/3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的部分，因为 3ℎ𝑡 ≤𝑛3ht≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以这之前已经执行了 InsertionSort(2ℎ𝑡)InsertionSort(2ht)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 InsertionSort(3ℎ𝑡)InsertionSort(3ht)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是执行 InsertionSort(ℎ𝑡)InsertionSort(ht)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

还是一样的，这一部分元素个数也是 𝑂(log2⁡𝑛)O(log2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别的，所以这一部分时间复杂度为 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

综上可得总时间复杂度即为 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 空间复杂度

希尔排序的空间复杂度为 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 实现

C++1Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text template < typename T > void shell_sort ( T array [], int length ) { int h = 1 ; while ( h < length / 3 ) { h = 3 * h \+ 1 ; } while ( h >= 1 ) { for ( int i = h ; i < length ; i ++ ) { for ( int j = i ; j >= h && array [ j ] < array [ j \- h ]; j -= h ) { std :: swap ( array [ j ], array [ j \- h ]); } } h = h / 3 ; } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text def shell_sort ( array , length ): h = 1 while h < length / 3 : h = int ( 3 * h \+ 1 ) while h >= 1 : for i in range ( h , length ): j = i while j >= h and array [ j ] < array [ j \- h ]: array [ j ], array [ j \- h ] = array [ j \- h ], array [ j ] j -= h h = int ( h / 3 ) ```   
---|---  
  
## 参考资料与注释

* * *

  1. [希尔排序 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F) ↩

* * *

>  __本页面最近更新： 2026/2/26 03:56:39，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/shell-sort.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/shell-sort.md "edit.link.title")  
>  __本页面贡献者：[NachtgeistW](https://github.com/NachtgeistW), [Tiphereth-A](https://github.com/Tiphereth-A), [iamtwz](https://github.com/iamtwz), [Alisahhh](https://github.com/Alisahhh), [CroMarmot](https://github.com/CroMarmot), [Enter-tainer](https://github.com/Enter-tainer), [HeRaNO](https://github.com/HeRaNO), [Menci](https://github.com/Menci), [partychicken](https://github.com/partychicken), [Peanut-Tang](https://github.com/Peanut-Tang), [shawlleyw](https://github.com/shawlleyw), [ShwStone](https://github.com/ShwStone), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
