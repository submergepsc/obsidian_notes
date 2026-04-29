# 卡特兰数 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/catalan/

# 卡特兰数

## 引入

Catalan 数经常出现在各类计数问题中．比利时数学家 Eugène Charles Catalan 在 1958 年研究括号序列计数问题时发现了这一数列，它也因此得名．清朝数学家明安图早在 18 世纪 30 年代就已经发现这一数列．

Catalan 数满足如下递推关系：

𝐶𝑛={1,𝑛=0,∑𝑛−1𝑖=0𝐶𝑖𝐶𝑛−1−𝑖,𝑛>0.(1)(1)Cn={1,n=0,∑i=0n−1CiCn−1−i,n>0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

数列的前几项为：（[OEIS: A000108](https://oeis.org/A000108)，下标从 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始）

1,1,2,5,14,42,132,429,1430,…1,1,2,5,14,42,132,429,1430,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 应用

Catalan 数 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递推关系有着天然的递归结构：规模为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计数问题 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以通过枚举分界点，分拆为两个规模分别为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑛 −1 −𝑖)(n−1−i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子问题．这一递推关系使得 Catalan 数广泛出现于各类具有类似递归结构的问题中．

  * **路径计数问题** ：有一个大小为 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方格图，左下角为 (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，右上角为 (𝑛,𝑛)(n,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．从左下角开始，每次都只能向右或者向上走一单位，不走到对角线 𝑦 =𝑥y=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上方（但可以触碰）的情况下，到达右上角的路径总数为 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

设方案数为 𝑇𝑛Tn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考虑 𝑛 ≥2n≥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况．设路径 **第一次** 走到对角线 𝑦 =𝑥y=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点是 (𝑘,𝑘) (𝑘 ∈[1,𝑛])(k,k) (k∈[1,n])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考察从 (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑘,𝑘)(k,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的除起点和终点外，中间的点 **不经过对角线（不能碰到）** 的路径．

![catalan2](./images/catalan-2.svg)

如图所示，这些路径的第一步一定向右，从 (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (1,0)(1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；最后一步一定向上，从 (𝑘,𝑘 −1)(k,k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑘,𝑘)(k,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，这些路径就是从 (1,0)(1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑘,𝑘 −1)(k,k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的不越过直线 𝑦 =𝑥 −1y=x−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径，这样路径的数目就是 𝑇𝑘−1Tk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．同时，从 (𝑘,𝑘)(k,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑛,𝑛)(n,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的合法路径数就是 𝑇𝑛−𝑘Tn−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据乘法原理，第一次在 (𝑘,𝑘)(k,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处触碰对角线的路径数目为 𝑇𝑘−1𝑇𝑛−𝑘Tk−1Tn−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．枚举 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有可能性，所有合法路径的数目为

𝑇𝑛=𝑛∑𝑘=1𝑇𝑘−1𝑇𝑛−𝑘.Tn=∑k=1nTk−1Tn−k.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

做代换 𝑘 =𝑖 +1k=i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以发现，这就是 Catalan 数的递推关系．由 𝑇0 =1T0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知 𝑇𝑛 =𝐶𝑛Tn=Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * **圆内不相交弦计数问题** ：圆上有 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，将这些点成对连接起来且使得所得到的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条线段两两不交的方案数是 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

记 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的方案数为 𝑇𝑛Tn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．将 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点按顺时针标号，分别为 1,2,…,2𝑛1,2,…,2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于弦两两不交，11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号点只能连接偶数号点；否则，两点之间的奇数个点无法在不穿过两点连线的情况下两两配对．如果连接了 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 2𝑘 (𝑘 ∈[1,𝑛])2k (k∈[1,n])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么左边有 2𝑘 −22k−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，右边有 2𝑛 −2𝑘2n−2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点，由乘法原理，这样的方案数为 𝑇𝑘−1𝑇𝑛−𝑘Tk−1Tn−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，枚举 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑇𝑛 =∑𝑛𝑘=1𝑇𝑘−1𝑇𝑛−𝑘Tn=∑k=1nTk−1Tn−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．令 𝑘 =𝑖 +1k=i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到 Catalan 数的递推关系．由 𝑇0 =1T0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知 𝑇𝑛 =𝐶𝑛Tn=Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * **三角剖分计数问题** ：对角线不相交的情况下，将一个凸 (𝑛 +2)(n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边形区域分成三角形区域的方法数为 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

设 (𝑛 +2)(n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边形三角剖分的方案数为 𝑇𝑛Tn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．先选定一条边 (1,𝑛 +2)(1,n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为基边，它一定属于一个三角形，记该三角形的第三个点为 𝑘 (𝑘 ∈[2,𝑛 +1])k (k∈[2,n+1])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这样，原凸多边形变成了三个部分：

    * 三角形 (1,𝑘,𝑛 +2)(1,k,n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
    * 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边形，顶点 1 ∼𝑘1∼k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
    * (𝑛 +3 −𝑘)(n+3−k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边形，顶点 𝑘 ∼(𝑛 +2)k∼(n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

后面两个部分都是子问题，所以，有递推关系

𝑇𝑛=𝑛+1∑𝑘=2𝑇𝑘−2𝑇𝑛+1−𝑘.Tn=∑k=2n+1Tk−2Tn+1−k.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 𝑘 =𝑖 +2k=i+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到 Catalan 数递归关系．由 𝑇0 =𝑇1 =1T0=T1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知 𝑇𝑛 =𝐶𝑛Tn=Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * **二叉树计数问题** ：含有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点的形态不同的二叉树数目为 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．等价地，含有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个非叶结点的形态不同的满二叉树数目为 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

记 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点的二叉树数目为 𝑇𝑛Tn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．任取一个根结点，枚举左右子树大小．设左子树大小为 𝑖 ∈[0,𝑛 −1]i∈[0,n−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则右子树大小为 (𝑛 −1 −𝑖)(n−1−i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．左右子树均为子问题，所以，有递推关系

𝑇𝑛=𝑛−1∑𝑖=0𝑇𝑖𝑇𝑛−1−𝑖.Tn=∑i=0n−1TiTn−1−i.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就是 Catalan 数递推关系．由 𝑇0 =𝑇1 =1T0=T1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知 𝑇𝑛 =𝐶𝑛Tn=Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * **括号序列计数问题** ：由 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对括号构成的合法括号序列数为 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

联系路径计数问题．将左括号视为向上走，右括号视为向右走．合法括号序列即为，在任意位置，左括号的数量不少于右括号的数量．相当于路径计数问题中，在任意时刻，向上走的次数不少于向右走的次数．因此，合法括号序列与合法路径之间存在双射．合法括号序列的数目同样为 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * **出栈序列计数问题** ：一个栈（无穷大）的进栈序列为 1,2,3,…,𝑛1,2,3,…,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，合法出栈序列的数目为 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

联系括号序列计数问题．将入栈视为左括号，出栈视为右括号．任意时刻，入栈的次数不少于出栈的次数．因此，合法出栈序列与合法括号序列之间存在双射．合法出栈序列的数目同样为 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * **数列计数问题** ：由 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组成的数列 𝑎1,𝑎2,…,𝑎2𝑛a1,a2,…,a2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，部分和满足 𝑎1 +𝑎2 +… +𝑎𝑘 ≥0 (𝑘 =1,2,3,…,2𝑛)a1+a2+…+ak≥0 (k=1,2,3,…,2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数列数目为 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

联系括号序列计数问题．将 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 视为左括号，−1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 视为右括号．任意时刻，+1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量不少于 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数量．因此，合法数列与合法括号序列之间存在双射．合法数列的数目同样为 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

尽管这一递推关系应用广泛，但是直接计算复杂度较高，需要寻找更为简单的公式．

## 常见形式

Catalan 数有如下常见的表达式：

𝐶𝑛=1𝑛+1(2𝑛𝑛)=(2𝑛)!𝑛!(𝑛+1)!, 𝑛≥0.(2)(2)Cn=1n+1(2nn)=(2n)!n!(n+1)!, n≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝐶𝑛=(2𝑛𝑛)−(2𝑛𝑛+1), 𝑛≥0.(3)(3)Cn=(2nn)−(2nn+1), n≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝐶𝑛=(4𝑛−2)𝑛+1𝐶𝑛−1, 𝑛>0, 𝐶0=1.(4)(4)Cn=(4n−2)n+1Cn−1, n>0, C0=1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Catalan 数的这些形式都可以高效计算：前两个形式将它转换为阶乘和组合数的计算问题，第三个形式则提供了顺次计算的递推公式．

对于这三种常见形式，本文提供两种证明方式．

### 代数推演

通过代数方法得出 Catalan 数的上述表达式共两步．首先，验证三个形式相互等价．

证明表达式 (2) ∼(4)(2)∼(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价

只需要证明表达式 (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以转化为表达式 (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中阶乘形式：

𝐶𝑛=(2𝑛𝑛)−(2𝑛𝑛+1)=(2𝑛)!𝑛!𝑛!−(2𝑛)!(𝑛−1)!(𝑛+1)!=(2𝑛)!𝑛!𝑛!(1−𝑛!(𝑛−1)!(𝑛+1))=(2𝑛)!𝑛!𝑛!(1−𝑛𝑛+1)=(2𝑛)!𝑛!(𝑛+1)!.Cn=(2nn)−(2nn+1)=(2n)!n!n!−(2n)!(n−1)!(n+1)!=(2n)!n!n!(1−n!(n−1)!(n+1))=(2n)!n!n!(1−nn+1)=(2n)!n!(n+1)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

以及，表达式 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也可以转化为表达式 (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中阶乘形式：

𝐶𝑛=𝑛∏𝑖=1(4𝑖−2)𝑖+1=𝑛∏𝑖=12𝑖(2𝑖−1)𝑖(𝑖+1)=(2𝑛)!𝑛!(𝑛+1)!.Cn=∏i=1n(4i−2)i+1=∏i=1n2i(2i−1)i(i+1)=(2n)!n!(n+1)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，三个表达式互相等价．

紧接着，验证这些形式确实是 Catalan 数递推公式的解．为此，考虑使用生成函数方法直接求出递推公式 (1)(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解．

利用生成函数方法求解递推公式 (1)(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑 Catalan 数的普通生成函数 𝐶(𝑥) =∑∞𝑛=0𝐶𝑛𝑥𝑛C(x)=∑n=0∞Cnxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于 Catalan 数的递推关系和卷积形式很相似，所以考虑用卷积构造 𝐶(𝑥)C(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方程：

𝐶(𝑥)=∞∑𝑛=0𝐶𝑛𝑥𝑛=1+∞∑𝑛=1(𝑛−1∑𝑖=0𝐶𝑖𝐶𝑛−𝑖−1)𝑥𝑛=1+𝑥∞∑𝑛=1𝑛−1∑𝑖=0𝐶𝑖𝑥𝑖𝐶𝑛−𝑖−1𝑥𝑛−𝑖−1=1+𝑥∞∑𝑖=0𝐶𝑖𝑥𝑖∞∑𝑗=0𝐶𝑗𝑥𝑗=1+𝑥𝐶2(𝑥).C(x)=∑n=0∞Cnxn=1+∑n=1∞(∑i=0n−1CiCn−i−1)xn=1+x∑n=1∞∑i=0n−1CixiCn−i−1xn−i−1=1+x∑i=0∞Cixi∑j=0∞Cjxj=1+xC2(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，倒数第二个等号交换了求和次序，并令 𝑗 =𝑛 −1 −𝑖j=n−1−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，解得：

𝐶(𝑥)=1±√1−4𝑥2𝑥=21∓√1−4𝑥.C(x)=1±1−4x2x=21∓1−4x.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由初值条件 𝐶0 =1C0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知，𝐶(0) =1C(0)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．代入检验可以发现唯一可行的解就是

𝐶(𝑥)=1−√1−4𝑥2𝑥.C(x)=1−1−4x2x.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

接下来，需要将它展开为幂级数的形式．利用 (1 +𝑥)𝑎(1+x)a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [幂级数展开式](../../poly/intro/#常见的幂级数展开式) 可知：

√1−4𝑥=∞∑𝑛=0(12)−𝑛𝑛!(−4𝑥)𝑛,1−4x=∑n=0∞(12)−nn!(−4x)n,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，(12)−𝑛(12)−n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是下降阶乘幂：

(12)−𝑛=𝑛−1∏𝑘=0(12−𝑘)=12𝑛𝑛−1∏𝑘=1(1−2𝑘)=(−1)𝑛−12𝑛𝑛−1∏𝑘=1(2𝑘−1)=(−1)𝑛−122𝑛−1𝑛−1∏𝑘=1(2𝑘−1)2𝑘𝑘=(−1)𝑛−122𝑛−1(2𝑛−2)!(𝑛−1)!.(12)−n=∏k=0n−1(12−k)=12n∏k=1n−1(1−2k)=(−1)n−12n∏k=1n−1(2k−1)=(−1)n−122n−1∏k=1n−1(2k−1)2kk=(−1)n−122n−1(2n−2)!(n−1)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入 𝐶(𝑥)C(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式，就有

𝐶(𝑥)=12𝑥(1−∞∑𝑛=0(12)−𝑛𝑛!(−4𝑥)𝑛)=−12𝑥∞∑𝑛=1(−4𝑥)𝑛𝑛!(12)−𝑛=−12𝑥∞∑𝑛=1(−4𝑥)𝑛𝑛!(−1)𝑛−122𝑛−1(2𝑛−2)!(𝑛−1)!=∞∑𝑛=1(2𝑛−2)!(𝑛−1)!𝑛!𝑥𝑛−1=∞∑𝑛=0(2𝑛)!𝑛!(𝑛+1)!𝑥𝑛.C(x)=12x(1−∑n=0∞(12)−nn!(−4x)n)=−12x∑n=1∞(−4x)nn!(12)−n=−12x∑n=1∞(−4x)nn!(−1)n−122n−1(2n−2)!(n−1)!=∑n=1∞(2n−2)!(n−1)!n!xn−1=∑n=0∞(2n)!n!(n+1)!xn.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由此，就得到 𝐶𝑛Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式 (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 组合意义

由于 Catalan 数具有明显的组合意义，所以只使用组合计数方法同样可以证明这些形式．本节为三个表达式分别提供一个组合意义的证明．

表达式 (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的证明

考虑 数列计数问题．对于任意由 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组成的序列 {𝑎𝑖}2𝑛𝑖=1{ai}i=12n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义它的部分和为 𝑆𝑖 =∑𝑖𝑗=1𝑎𝑖Si=∑j=1iai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并定义它的 **超额量** （exceedance）为 𝑆𝑖 <0Si<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎𝑖 = −1ai=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的下标数量．超额量为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就等价于数列合法；超额量的取值范围是 [0,𝑛][0,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，共 (𝑛 +1)(n+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种可能的取值．需要证明的是，不同超额量的数列数量其实是一样的．

为此，可以构造一个从超额量为 𝑒 >0e>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数列到超额量为 (𝑒 −1)(e−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数列的映射 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于超额量为 𝑒 >0e>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，取下标 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为使得 𝑆𝑖 =0Si=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎𝑖 = +1ai=+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立的下标最小值．将 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 左右两侧的序列交换，就得到如下序列 {𝑎′𝑖}{ai′}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑎𝑘+1,𝑎𝑘+2,⋯,𝑎2𝑛,𝑎𝑘,𝑎1,𝑎2,⋯,𝑎𝑘−1.ak+1,ak+2,⋯,a2n,ak,a1,a2,⋯,ak−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于原序列中 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 右侧部分在交换前后对应的部分和序列不变，所以它们贡献的超额量也不变．对于原序列中 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 左侧部分，它们对应的部分和在交换后全部增加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此，它们贡献的超额量会减少，而且减少的数量恰好等于原序列 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 左侧部分中满足 𝑆𝑖 = −1Si=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎𝑖 = −1ai=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的下标数量．因为 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选取保证了这样的下标有且仅有一个，所以，序列 {𝑎′𝑖}{ai′}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的超额量就等于 (𝑒 −1)(e−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，映射 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以将序列的超额量恰好减少 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

映射 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是可逆的．注意到序列 {𝑎′𝑖}{ai′}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的位置恰好为满足 𝑆′𝑘 = +1Sk′=+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎′𝑖 = +1ai′=+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的下标最大值．这是因为交换后，这些部分和都比交换前对应的部分和恰好大 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此，现在的部分和为 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应交换前部分和等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，根据 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选取，交换前这一部分（即原序列 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 左侧部分）是没有满足 𝑆𝑖 =0Si=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎𝑖 = +1ai=+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立的下标的．

由此，映射 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成了超额量为 𝑒 >0e>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列和超额量为 (𝑒 −1)(e−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列之间的双射．这就说明，不同超额量的数列数量其实是一样的．由于数列总数是 (2𝑛𝑛)(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，合法数列（即超额量为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数列）数量就等于

𝐶𝑛=1𝑛+1(2𝑛𝑛).Cn=1n+1(2nn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就证明了 Catalan 数的表达式 (2)(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

表达式 (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的证明

考虑 路径计数问题．这是典型的格路计数问题，可以通过反射原理求解．具体到本问题，考虑用总路径数目减去不合法的路径数目．总路径数一共要走 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步，其中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步向右，所以方案数为 (2𝑛𝑛)(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．一条路径不合法，当且仅当它碰到了直线 𝑦 =𝑥 +1y=x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于任意一条非法路径，可以找到第一次碰到直线 𝑦 =𝑥 +1y=x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置，并将该位置之后的路径关于直线 𝑦 =𝑥 +1y=x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做对称．此时，可以发现，一条从 (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑛,𝑛)(n,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非法路径，变成了一条从 (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑛 −1,𝑛 +1)(n−1,n+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径．

![catalan1](./images/catalan-1.svg)

由于从 (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑛 −1,𝑛 +1)(n−1,n+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径必定要穿过直线 𝑦 =𝑥 +1y=x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以每条这样的路径都对应一条从 (0,0)(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑛,𝑛)(n,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非法路径．类似总路径数的计算，非法路径数目的总数就是 (2𝑛𝑛+1)(2nn+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，合法路径的总数为

𝐶𝑛=(2𝑛𝑛)−(2𝑛𝑛+1).Cn=(2nn)−(2nn+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就是 Catalan 数的表达式 (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

表达式 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的证明

考虑 三角剖分计数问题．设 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是凸 (𝑛 +2)(n+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边形，固定它的一个边为基边．对于多边形 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每一个三角剖分，都可以选择它的一个非基边（包括三角剖分时新加的边）标记，并定向．这共有 (4𝑛 +2)𝐶𝑛(4n+2)Cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种剖分加标记的方案．又设 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是凸 (𝑛 +3)(n+3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边形，仍固定它的一个边为基边．对于多边形 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以选择它的一条非基边标记，然后再做三角剖分．这共有 (𝑛 +2)𝐶𝑛+1(n+2)Cn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种标记加剖分的方案．

![](./images/catalan-triangulation.svg)

如图所示，这两组操作得到的结果之间存在明显的双射．对于 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 剖分并标记的一个结果，可以将它的标记边扩展为三角形，定向所指向的终点扩展为一条新边，并将这条新边打上标记，这就得到对 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 标记并剖分的一个结果；对于 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 标记并剖分的一个结果，可以将它的标记边压缩为一个点，并将压缩得到的对角线打上标记，且指向压缩得到的顶点，这就得到对 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 剖分并标记的一个结果．因此，

(4𝑛+2)𝐶𝑛=(𝑛+2)𝐶𝑛+1.(4n+2)Cn=(n+2)Cn+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

稍作整理，并结合 𝐶0 =1C0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到 Catalan 数的表达式 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 例题

[洛谷 P1044 栈](https://www.luogu.com.cn/problem/P1044)

入栈顺序为 1,2,…,𝑛1,2,…,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求所有可能的出栈顺序的总数．

参考代码

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text #include <iostream> using namespace std ; int n ; long long f [ 25 ]; int main () { f [ 0 ] = 1 ; cin >> n ; for ( int i = 1 ; i <= n ; i ++ ) f [ i ] = f [ i \- 1 ] * ( 4 * i \- 2 ) / ( i \+ 1 ); // 这里用的是常见形式 4 cout << f [ n ] << endl ; return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text f = [ 0 ] * 25 f [ 0 ] = 1 n = int ( input ()) for i in range ( 1 , n \+ 1 ): f [ i ] = f [ i \- 1 ] * ( 4 * i \- 2 ) // ( i \+ 1 ) # 这里用的是常见形式 4 print ( f [ n ]) ```   
---|---  
  
## 习题

  * [Luogu P2532 [AHOI2012] 树屋阶梯](https://www.luogu.com.cn/problem/P2532)
  * [Luogu P1641 [SCOI2010] 生成字符串](https://www.luogu.com.cn/problem/P1641)
  * [Luogu P3200 [HNOI2009] 有趣的数列](https://www.luogu.com.cn/problem/P3200)
  * [AtCoder Beginner Contest 205 E - White and Black Balls](https://atcoder.jp/contests/abc205/tasks/abc205_e)
  * [AtCoder Regular Contest 145 C - Split and Maximize](https://www.luogu.com.cn/problem/AT_arc145_c)
  * [Luogu P5014 水の三角（修改版）](https://www.luogu.com.cn/problem/P5014)
  * [Luogu P3978 [TJOI2015] 概率论](https://www.luogu.com.cn/problem/P3978)

## 参考资料与注释

  * [Catalan number - Wikipedia](https://en.wikipedia.org/wiki/Catalan_number)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/catalan.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/catalan.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [NachtgeistW](https://github.com/NachtgeistW), [Xeonacid](https://github.com/Xeonacid), [MegaOwIer](https://github.com/MegaOwIer), [Tiphereth-A](https://github.com/Tiphereth-A), [AngelKitty](https://github.com/AngelKitty), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [Chrogeek](https://github.com/Chrogeek), [Fidelxyz](https://github.com/Fidelxyz), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Great-designer](https://github.com/Great-designer), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [kfy666](https://github.com/kfy666), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [Peanut-Tang](https://github.com/Peanut-Tang), [purple-vine](https://github.com/purple-vine), [refinedcoding](https://github.com/refinedcoding), [shawlleyw](https://github.com/shawlleyw), [ShizuhaAki](https://github.com/ShizuhaAki), [Skyminers](https://github.com/Skyminers), [SukkaW](https://github.com/SukkaW), [ucSec](https://github.com/ucSec), [WFHFAQFXY](https://github.com/WFHFAQFXY), [xglight](https://github.com/xglight), [zryi2003](https://github.com/zryi2003)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
