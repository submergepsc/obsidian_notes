# Entringer Number - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/entringer/

# Entringer Number

## 恩特林格数

恩特林格数（Entringer number，[OEIS A008281](http://oeis.org/A008281)）𝐸(𝑛,𝑘)E(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是满足下述条件的 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数的置换数目：

  * 首元素是 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 首元素的下一个元素比首元素小，再下一个元素比前一个元素大，再下一个元素比前一个元素小……后面相邻元素的大小关系均满足这样的规则．

恩特林格数的初值有：

𝐸(0,0)=1E(0,0)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝐸(𝑛,0)=0E(n,0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

有递推关系：

𝐸(𝑛,𝑘)=𝐸(𝑛,𝑘−1)+𝐸(𝑛−1,𝑛−𝑘)E(n,k)=E(n,k−1)+E(n−1,n−k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## Seidel–Entringer–Arnold 三角

恩特林格数的一个适当排列的数字三角，称为 Seidel–Entringer–Arnold 三角（Seidel–Entringer–Arnold triangle，[OEIS A008280](http://oeis.org/A008280)）．该三角是按照「牛耕」顺序（ox-plowing order）排列的恩特林格数 𝐸(𝑛,𝑘)E(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝐸(0,0)𝐸(1,0)→𝐸(1,1)𝐸(2,2)←𝐸(2,1)←𝐸(2,0)𝐸(3,0)→𝐸(3,1)→𝐸(3,2)→𝐸(3,3)𝐸(4,4)←𝐸(4,3)←𝐸(4,2)←𝐸(4,1)←𝐸(4,0)E(0,0)E(1,0)→E(1,1)E(2,2)←E(2,1)←E(2,0)E(3,0)→E(3,1)→E(3,2)→E(3,3)E(4,4)←E(4,3)←E(4,2)←E(4,1)←E(4,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即：

10→11←1←00→1→2→25←5←4←2←010→11←1←00→1→2→25←5←4←2←0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

按照这种方式排列的恩特林格数的优势是，与它的递推关系 𝐸(𝑛,𝑘) =𝐸(𝑛,𝑘 −1) +𝐸(𝑛 −1,𝑛 −𝑘)E(n,k)=E(n,k−1)+E(n−1,n−k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一致，可以方便记忆和理解．

恩特林格数有一个指数型生成函数：

∞∑𝑚=0∞∑𝑛=0𝐸(𝑚+𝑛,12(𝑚+𝑛+(−1)𝑚+𝑛(𝑛−𝑚)))𝑥𝑚𝑚!𝑥𝑛𝑛!=cos⁡𝑥+sin⁡𝑥cos⁡(𝑥+𝑦)∑m=0∞∑n=0∞E(m+n,12(m+n+(−1)m+n(n−m)))xmm!xnn!=cos⁡x+sin⁡xcos⁡(x+y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个生成函数的系数分布事实上是上面的 Seidel–Entringer–Arnold 三角的简单拉伸变形：

𝐸(0,0)𝐸(1,1)𝐸(2,0)𝐸(3,3)𝐸(4,0)𝐸(1,0)𝐸(2,1)𝐸(3,2)𝐸(4,1)𝐸(2,2)𝐸(3,1)𝐸(4,2)𝐸(3,0)𝐸(4,3)𝐸(4,4)E(0,0)E(1,1)E(2,0)E(3,3)E(4,0)E(1,0)E(2,1)E(3,2)E(4,1)E(2,2)E(3,1)E(4,2)E(3,0)E(4,3)E(4,4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即：

110200122114055110200122114055![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## zigzag 置换

一个 zigzag 置换（zigzag permutation）是一个 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排列 𝑐1c1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得任意一个元素 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小都不介于 𝑐𝑖−1ci−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐𝑖+1ci+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间．

对于 zigzag 置换的个数 𝑍𝑛Zn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（[OEIS A001250](http://oeis.org/A001250)），从 𝑛 =0n=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始有：

1,1,2,4,10,32,122,544,⋯1,1,2,4,10,32,122,544,⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

例如，前几个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的交替置换有：

𝑛=1:{1}𝑛=2:{1,2},{2,1}𝑛=3:{1,3,2},{2,1,3},{2,3,1},{3,1,2}𝑛=4:{1,3,2,4},{1,4,2,3},{2,1,4,3},{2,3,1,4},{2,4,1,3},{3,1,4,2},{3,2,4,1},{3,4,1,2},{4,1,3,2},{4,2,3,1}n=1:{1}n=2:{1,2},{2,1}n=3:{1,3,2},{2,1,3},{2,3,1},{3,1,2}n=4:{1,3,2,4},{1,4,2,3},{2,1,4,3},{2,3,1,4},{2,4,1,3},{3,1,4,2},{3,2,4,1},{3,4,1,2},{4,1,3,2},{4,2,3,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 交替置换与 zigzag 数

（注意和「错位排列」进行概念上的区分．）

对于大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每个 zigzag 置换翻转过来仍旧为 zigzag 置换，可以两两配对，所以必然为偶数．

这里再给出一种配对的方法：将 zigzag 置换分为交替置换（alternating permutation）和反交替置换（reverse alternating permutation）．

交替置换的首元素大于第二个元素，大小关系为：

𝑐1>𝑐2<𝑐3>⋯c1>c2<c3>⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

反交替置换的首元素小于第二个元素，大小关系为：

𝑐1<𝑐2>𝑐3<⋯c1<c2>c3<⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果将 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位置互换，22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位置互换，以此类推，即可将交替置换与反交替置换两个集合互换．因此，交替置换与反交替置换的个数相等，恰好为 zigzag 置换的一半．

对于大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记：

𝐴𝑛=𝑍𝑛2An=Zn2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定义初值：

𝐴0=𝐴1=1A0=A1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里的 𝐴𝑛An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 zigzag 数（Euler zigzag number，[OEIS A000111](http://oeis.org/A000111)），从 𝑛 =0n=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始有：

1,1,1,2,5,16,61,272,⋯1,1,1,2,5,16,61,272,⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

接下来试着求解 𝐴𝑛An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之中，选取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数构成子集，有 (𝑛𝑘)(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种选法．

在这个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元子集中，选反交替置换 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝐴𝑘Ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种选法；用全集减掉这个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元子集，剩余的 𝑛 −𝑘n−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元子集中，选反交替置换 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝐴𝑛−𝑘An−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种选法．

考虑 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元排列 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倒置作为开头，接上 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再接上 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定是 zigzag 置换，并且任意一个 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元 zigzag 置换，都可以在 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处截断得到对应的反交替置换 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且不同的 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元 zigzag 置换对应的 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不同．

因此有递推关系：

2𝐴𝑛+1=𝑛∑𝑘=0(𝑛𝑘)𝐴𝑘𝐴𝑛−𝑘2An+1=∑k=0n(nk)AkAn−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)2(𝑛+1)𝐴𝑛+1(𝑛+1)!=𝑛∑𝑘=0𝐴𝑘𝑘!𝐴𝑛−𝑘(𝑛−𝑘)!2(n+1)An+1(n+1)!=∑k=0nAkk!An−k(n−k)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时并不满足这个递推式，初值 𝐴0A0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐴1A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

可见，这是一个指数型生成函数的卷积．假设 𝐴𝑛An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的指数型生成函数为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有微分方程：

2d𝑦d𝑥=𝑦2+12dydx=y2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

等式右面加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是为了处理 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时的特殊情况．该方程的通解为：

𝑦=tan⁡(12𝑥+𝐶)y=tan⁡(12x+C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之后，可以得到特解：

𝑦=tan⁡𝑥+sec⁡𝑥y=tan⁡x+sec⁡x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

正切函数是奇函数，正割函数是偶函数，两者之和构成 zigzag 数的生成函数．

## 恩特林格数与 zigzag 数的关系

根据恩特林格数的定义，恩特林格数 𝐸(𝑛,𝑘)E(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是首元素为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的交替置换个数．因此恩特林格数与 zigzag 数事实上有关系：

𝐴𝑛=𝐸(𝑛,𝑛)An=E(n,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将 𝐴𝑛An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为「zigzag 数」也有原因：记 𝐸𝑛En![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是欧拉数（Euler number），𝐵𝑛Bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是伯努利数．

当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为偶数时，偶数项下标的 zigzag 数也称「正割数」𝑆𝑛Sn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或者「zig 数」．有关系：

𝐴𝑛=(−1)𝑛/2𝐸𝑛An=(−1)n/2En![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

前几项为（[OEIS A000364](http://oeis.org/A000364)）：

1,1,5,61,1385,⋯1,1,5,61,1385,⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为奇数时，奇数项下标的 zigzag 数也称「正切数」𝑇𝑛Tn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或者「zag 数」．有关系：

𝐴𝑛=(−1)(𝑛−1)/22𝑛+1(2𝑛+1−1)𝐵𝑛+1𝑛+1An=(−1)(n−1)/22n+1(2n+1−1)Bn+1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

前几项为（[OEIS A000182](http://oeis.org/A000182)）：

1,2,16,272,7936,⋯1,2,16,272,7936,⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是对于在 𝑥 =0x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的泰勒展开，可以给出正割数和正切数：

sec⁡𝑥=𝐴0+𝐴2𝑥22!+𝐴4𝑥44!+⋯sec⁡x=A0+A2x22!+A4x44!+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)tan⁡𝑥=𝐴1𝑥+𝐴3𝑥33!+𝐴5𝑥55!+⋯tan⁡x=A1x+A3x33!+A5x55!+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

或者写到一起：

sec⁡𝑥+tan⁡𝑥=𝐴0+𝐴1𝑥+𝐴2𝑥22!+𝐴3𝑥33!+𝐴4𝑥44!+𝐴5𝑥55!+⋯sec⁡x+tan⁡x=A0+A1x+A2x22!+A3x33!+A4x44!+A5x55!+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

构成 zigzag 数的生成函数．

## 参考资料与链接

  1. [Alternating permutation - Wikipedia](https://en.wikipedia.org/wiki/Alternating_permutation)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/entringer.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/entringer.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Great-designer](https://github.com/Great-designer), [CCXXXI](https://github.com/CCXXXI), [ChungZH](https://github.com/ChungZH), [jifbt](https://github.com/jifbt)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
