# 弦图 - OI Wiki

- Source: https://oi-wiki.org/graph/chord/

# 弦图

弦图是一种特殊的图，很多在一般图上的 NP-Hard 问题在弦图上都有优秀的线性时间复杂度算法．

## 一些定义与性质

**子图** ：点集和边集均为原图点集和边集子集的图．

**导出子图（诱导子图）** ：点集为原图点集子集，边集为所有满足 **两个端点均在选定点集中** 的图．

**团** ：完全子图．

**极大团** ：不是其他团子图的图．

**最大团** ：点数最大的团．

**团数** ：最大团的点数，记为 𝜔(𝐺)ω(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**最小染色** ：用最少的颜色给点染色使得所有边连接的两点颜色不同．

**色数** ：最小染色的颜色数，记为 𝜒(𝐺)χ(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**最大独立集** ：最大的点集使得点集中任意两点都没有边直接相连．该集合的大小记为 𝛼(𝐺)α(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**最小团覆盖** ：用最少的团覆盖所有的点．使用团的数量记为 𝜅(𝐺)κ(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**弦** ：连接环中不相邻两点的边．

**弦图** ：任意长度大于 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的环都有一个弦的图称为弦图．

**Lemma 1** ：团数 𝜔(𝐺) ≤𝜒(𝐺)ω(G)≤χ(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 色数

证明：考虑单独对最大团的导出子图进行染色，至少需要 𝜔(𝐺)ω(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种颜色．

**Lemma 2** ：最大独立集数 𝛼(𝐺) ≤𝜅(𝐺)α(G)≤κ(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小团覆盖数

证明：每个团中至多选择一个点．

**Lemma 3** ：弦图的任意导出子图一定是弦图．

证明：如果弦图有导出子图不是弦图，说明在这个导出子图上存在大于 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的无弦环，则无论原图如何（怎么加边）都不会使得原图是弦图，矛盾．

**Lemma 4** ：弦图的任意导出子图一定不可能是一个点数大于 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的环．

证明：一个点数大于 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的环不是弦图，用以上定理即可．

## 弦图的判定

### 问题描述

给定一个无向图，判断其是否为弦图．

### 点割集

对于图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的两点 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义这两点间的 **点割集** 为满足删除这一集合后，𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两点之间不连通．如果关于 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两点间的一个点割集的任意子集都不是点割集，则称这个点割集为 **极小点割集** ．

**Lemma 5** ：图关于 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极小点割集将原图分成了若干个连通块，设包含 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连通块为 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，包含 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连通块为 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对于极小点割集上的任意一点 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑁(𝑎)N(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定包含 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的点．

证明：若 𝑁(𝑎)N(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只包含 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的至多一个连通块中的点，从点割集中删去 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点，仍不连通，则原点割集不是最小点割集．

**Lemma 6** ：弦图上任意两点间的极小点割集的导出子图一定为一个团．

证明：极小点割集大小 ≤1≤1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，导出子图一定为一个团．

否则，设极小点割集上有两点为 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 **Lemma 5** 得，𝑁(𝑥)N(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中有 𝑉1,𝑉2V1,V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的点，设为 𝑥1,𝑥2x1,x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，同样的，设 𝑦1,𝑦2y1,y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，注意，可能有 𝑥1 =𝑦1,𝑥2 =𝑦2x1=y1,x2=y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于 𝑉1,𝑉2V1,V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为连通块，则在 𝑥1,𝑦1x1,y1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥2,𝑦2x2,y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两个点对之间存在最短路径．设 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑉1,𝑉2V1,V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内部的最短路为 𝑥 −𝑥1 ∼𝑦1 −𝑦,𝑥 −𝑥2 ∼𝑦2 −𝑦x−x1∼y1−y,x−x2∼y2−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则图上存在一个环 𝑥 −𝑥1 ∼𝑦1 −𝑦 −𝑦2 ∼𝑥2 −𝑥x−x1∼y1−y−y2∼x2−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，该环的大小一定 ≥4≥4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据弦图的定义，此时该环上一定存在一条弦．

若这条弦连接了 𝑉1,𝑉2V1,V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两个连通块，则点集不是点割集．若这条弦连接了单个连通块内部的两个点或一个连通块内部的一个点和一个点割集上的点，都不满足最短路的性质．所以这条弦只能连接 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两点．

由此，可证弦图中每个极小点割集中的两点都有边直接相连，故性质得证．

### 单纯点

设 𝑁(𝑥)N(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示与点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相邻的点集．若点集 {𝑥} +𝑁(𝑥){x}+N(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的导出子图为一个团，则称点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为单纯点．

**Lemma 7** ：任何一个弦图都至少有一个单纯点，不是完全图的弦图至少有两个不相邻的单纯点．

证明：数学归纳法．单独考虑每一连通块．

归纳基底：当图与完全图同构时，图上任意一点都是单纯点．当图的点数 ≤3≤3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，引理成立．

若图上的点数 ≥4≥4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且图不为完全图，可知必然存在 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 (𝑢,𝑣) ∉𝐸(u,v)∉E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是图关于 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极小点割集．设 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是删去 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后的导出子图上 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在的连通块．由于问题的对称性，我们只考虑 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一侧的情况，设 𝐿 =𝐴 +𝐼L=A+I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为完全图，则 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为单纯点；若不是，因为 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是原图的导出子图，一定也是弦图，所以有两个不相邻的单纯点，因为 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个团，其上两点都相邻，所以 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中一定有一个单纯点．该单纯点扩展到全图也为单纯点．

由于每次将整个图分成若干个连通块证明，大小一定减小，且都满足性质，故归纳成立．

### 完美消除序列

令 𝑛 =|𝑉|n=|V|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，完美消除序列 𝑣1,𝑣2,…,𝑣𝑛v1,v2,…,vn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 1,2,…,𝑛1,2,…,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个排列，满足 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 {𝑣𝑖,𝑣𝑖+1,…,𝑣𝑛}{vi,vi+1,…,vn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的导出子图中为单纯点．

**Lemma 8** ：一个无向图是弦图当且仅当其有一个完全消除序列．

充分性：点数为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的弦图有完全消除序列．由 **Lemma 3** 和 **Lemma 7** ，点数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的弦图的完美消除序列可以由点数为 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的弦图的完美消除序列加上一个单纯点得到．

必要性：假设有无向图存在结点数 >3>3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的环且拥有完美消除序列，设在完美消除序列中出现的第一个环上的点为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在环上与 𝑣1,𝑣2v1,v2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连，则有完美消除序列的性质即单纯点的定义可得 𝑣1,𝑣2v1,v2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 直接有边相连，矛盾．

### 朴素算法

每次找到一个 **单纯点** 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，加入到完美消除序列中．

将点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与其相邻的边从图上删除．

重复以上过程，若所有点都被删除，则原图是弦图且求得了一个完美消除序列；若图上不存在单纯点，则原图不是弦图．

时间复杂度 𝑂(𝑛4)O(n4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### MCS 算法

**最大势算法** （Maximum Cardinality Search）是一种可以在 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内求出无向图的完美消除序列的方法．

逆序给结点编号，即按从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的顺序给点标号．

设 𝑙𝑎𝑏𝑒𝑙𝑥labelx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点与多少个已经标号的点相邻，每次选择 𝑙𝑎𝑏𝑒𝑙label![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值最大的未标号结点进行标号．

用链表维护对于每个 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 𝑙𝑎𝑏𝑒𝑙𝑥 =𝑖labelx=i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于每条边对 ∑𝑛𝑖=1𝑙𝑎𝑏𝑒𝑙𝑖∑i=1nlabeli![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的贡献最多是 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时间复杂度 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**正确性证明** ：

设 𝛼(𝑥)α(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在这个序列中的位置． 我们需要证明对于任何一个弦图，算法求出的序列一定是一个完美消除序列，即在序列中位于某个点后面且与这个点相连的所有点两两相连．

**Lemma 9** ：考虑三个点 𝑢,𝑣,𝑤u,v,w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝛼(𝑢) <𝛼(𝑣) <𝛼(𝑤)α(u)<α(v)<α(w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果 𝑢𝑤uw![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连，𝑣𝑤vw![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不相连，则 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只给 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑙𝑎𝑏𝑒𝑙label![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 贡献，不给 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 贡献．为了让 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 先加入序列，需要一个 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝛼(𝑣) <𝛼(𝑥)α(v)<α(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑣𝑥vx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连，𝑢𝑥ux![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不相连，即 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只给 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 贡献而不给 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 贡献．

**Lemma 10** ：任意一个弦图一定不存在一个序列 𝑣0,𝑣1,…,𝑣𝑘(𝑘 ≥2)v0,v1,…,vk(k≥2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足下列性质：

  1. 𝑣𝑖𝑣𝑗vivj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连当且仅当 |𝑖 −𝑗| =1|i−j|=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 𝛼(𝑣0) >𝛼(𝑣𝑖)(𝑖 ∈[1,𝑘])α(v0)>α(vi)(i∈[1,k])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 存在 𝑖 ∈[1,𝑘 −1]i∈[1,k−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 𝛼(𝑣𝑖) <𝛼(𝑣𝑖+1) <⋯ <𝛼(𝑣𝑘)α(vi)<α(vi+1)<⋯<α(vk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝛼(𝑣𝑖) <𝛼(𝑣𝑖−1) <⋯ <𝛼(𝑣1) <𝛼(𝑣𝑘) <𝛼(𝑣0)α(vi)<α(vi−1)<⋯<α(v1)<α(vk)<α(v0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明：

由于 𝛼(𝑣1) <𝛼(𝑣𝑘) <𝛼(𝑣0)α(v1)<α(vk)<α(v0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑣1𝑣0v1v0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连，𝑣𝑘𝑣0vkv0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不相连，所以由性质一，存在 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝛼(𝑣𝑘) <𝛼(𝑥)α(vk)<α(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑣𝑘𝑥vkx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连，𝑣1𝑥v1x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不相连．

考虑最小的 𝑗 ∈(1,𝑘]j∈(1,k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑣𝑗𝑥vjx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连，我们可以推出 𝑣0𝑥v0x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不相连，否则 𝑣0𝑣1⋯𝑣𝑗𝑥v0v1⋯vjx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成了一个长度 ≥4≥4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且无弦的环．

如果 𝑥 <𝑣0x<v0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑣0,𝑣1,…,𝑣𝑗,𝑥v0,v1,…,vj,x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是一个满足性质的序列；如果 𝑣0 <𝑥v0<x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则 𝑥,𝑣𝑗,…,𝑣1,𝑣0x,vj,…,v1,v0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是一个满足性质的序列．

在上面的推导中，我们扩大了 min(𝑣0,𝑣𝑘)min(v0,vk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是一直推下去，一定会产生矛盾．

**Theorem 1** ：对于任何一个弦图，最大势算法求出的序列一定是一个完美消除序列．

证明：考虑任意三个点 𝑢,𝑣,𝑤u,v,w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝛼(𝑢) <𝛼(𝑣) <𝛼(𝑤)α(u)<α(v)<α(w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们需要证明若 𝑢𝑣uv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连，𝑢𝑤uw![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连，则 𝑣𝑤vw![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定相连．

考虑反证法，假设不相连，那么 𝑤,𝑢,𝑣w,u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是一个满足 **Lemma 10** 中性质的序列，我们证明了这样序列不存在，所以矛盾，𝑣𝑤vw![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连．

参考代码：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text while ( cur ) { p [ cur ] = h [ nww ]; rnk [ p [ cur ]] = cur ; h [ nww ] = nxt [ h [ nww ]]; lst [ h [ nww ]] = 0 ; lst [ p [ cur ]] = nxt [ p [ cur ]] = 0 ; tf [ p [ cur ]] = true ; for ( vector < int >:: iterator it = G [ p [ cur ]]. begin (); it != G [ p [ cur ]]. end (); it ++ ) if ( ! tf [ * it ]) { if ( h [ deg [ * it ]] == * it ) h [ deg [ * it ]] = nxt [ * it ]; nxt [ lst [ * it ]] = nxt [ * it ]; lst [ nxt [ * it ]] = lst [ * it ]; lst [ * it ] = nxt [ * it ] = 0 ; deg [ * it ] ++ ; nxt [ * it ] = h [ deg [ * it ]]; lst [ h [ deg [ * it ]]] = * it ; h [ deg [ * it ]] = * it ; } cur \-- ; if ( h [ nww \+ 1 ]) nww ++ ; while ( nww && ! h [ nww ]) nww \-- ; } ```   
---|---  
  
如果此时原图是弦图，此时求出的就是完美消除序列；但是由于原图可能不是弦图，此时求出的一定不是完美消除序列，所以问题转化为 **判断求出的序列是否是原图的完美消除序列** ．

### 判断一个序列是否是完美消除序列

#### 朴素算法

根据定义，依次判断完美消除序列 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上 {𝑣𝑖,𝑣𝑖+1,…,𝑣𝑛}{vi,vi+1,…,vn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中与 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相邻的点是否构成了一个团．时间复杂度 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 优化后的算法

根据完美消除序列的定义，设 𝑣𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑣𝑖,𝑣𝑖+1,…,𝑣𝑛vi,vi+1,…,vn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中相邻的点从小到大为 {𝑣𝑐1,𝑣𝑐2,…,𝑣𝑐𝑘}{vc1,vc2,…,vck}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则只需判断 𝑣𝑐1vc1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与其他点是否直接连通即可．时间复杂度 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text jud = true ; for ( int i = 1 ; i <= n ; i ++ ) { cur = 0 ; for ( vector < int >:: iterator it = G [ p [ i ]]. begin (); it != G [ p [ i ]]. end (); it ++ ) if ( rnk [ p [ i ]] < rnk [ * it ]) { s [ ++ cur ] = * it ; if ( rnk [ s [ cur ]] < rnk [ s [ 1 ]]) swap ( s [ 1 ], s [ cur ]); } for ( int j = 2 ; j <= cur ; j ++ ) if ( ! st [ s [ 1 ]]. count ( s [ j ])) { jud = false ; break ; } } if ( ! jud ) printf ( "Imperfect \n " ); else printf ( "Perfect \n " ); ```   
---|---  
  
至此，**弦图判定问题** 可以在 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内解决．

## 弦图的极大团

令 𝑁(𝑥)N(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为满足与 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 直接有边相连且在完美消除序列上的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之后的序列．则弦图的极大团一定为 {𝑥} +𝑁(𝑥){x}+N(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明：考虑弦图的一个极大团 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中的点在完美消除序列中出现的第一个点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一定有 𝑉 ⊆{𝑥} +𝑁(𝑥)V⊆{x}+N(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又因为 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是极大团，所以 𝑉 ={𝑥} +𝑁(𝑥)V={x}+N(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

弦图最多有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个极大团．求出弦图的每个极大团，可以判断每个 {𝑥} +𝑁(𝑥){x}+N(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否为极大团．

设 𝐴 ={𝑥} +𝑁(𝑥),𝐵 ={𝑦} +𝑁(𝑦)A={x}+N(x),B={y}+N(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 𝐴 ⫋𝐵A⫋B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是极大团．此时在完美消除序列上显然有 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前．

设 𝑛𝑥𝑡𝑥nxtx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑁(𝑥)N(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中在完美消除序列上最靠前的点，𝑦 ∗y∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示所有满足 𝐴 ⊆𝐵A⊆B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的最靠后的点．此时必然有 𝑛𝑥𝑡𝑦∗ =𝑥nxty∗=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则 𝑦 ∗y∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是最靠后的，令 𝑦 ∗ =𝑛𝑥𝑡𝑦∗y∗=nxty∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然满足条件．

𝐴 ⫋𝐵A⫋B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当 |𝐴| +1 ≤|𝐵||A|+1≤|B|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

问题转化为判断是否存在 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 𝑛𝑥𝑡𝑦 =𝑥nxty=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 |𝑁(𝑥)| +1 ≤|𝑁(𝑦)||N(x)|+1≤|N(y)|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．时间复杂度 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text for ( int i = 1 ; i <= n ; i ++ ) { cur = 0 ; for ( vector < int >:: iterator it = G [ p [ i ]]. begin (); it != G [ p [ i ]]. end (); it ++ ) if ( rnk [ p [ i ]] < rnk [ * it ]) { s [ ++ cur ] = * it ; if ( rnk [ s [ cur ]] < rnk [ s [ 1 ]]) swap ( s [ 1 ], s [ cur ]); } fst [ p [ i ]] = s [ 1 ]; N [ p [ i ]] = cur ; } for ( int i = 1 ; i <= n ; i ++ ) { if ( ! vis [ p [ i ]]) ans ++ ; if ( N [ p [ i ]] >= N [ fst [ p [ i ]]] \+ 1 ) vis [ fst [ p [ i ]]] = true ; } ```   
---|---  
  
## 弦图的色数/弦图的团数

一种构造方法：按完美消除序列从后往前依次给每个点染色，给每个点染上可以染的最小颜色．时间复杂度 𝑂(𝑚 +𝑛)O(m+n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

正确性证明：设以上方法使用了 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种颜色，则 𝑡 ≥𝜒(𝐺)t≥χ(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于团上每个点都是不同的颜色，所以 𝑡 =𝜔(𝐺)t=ω(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 **Lemma 1** ，𝑡 =𝜔(𝐺) ≤𝜒(𝐺)t=ω(G)≤χ(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．综上，可得 𝑡 =𝜒(𝐺) =𝜔(𝐺)t=χ(G)=ω(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

无需染色方案，只需求出弦图的色数/团数时，可以取 |{𝑥} +𝑁(𝑥)||{x}+N(x)|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大值得到．

```text 1 ``` |  ```text for ( int i = 1 ; i <= n ; i ++ ) ans = max ( ans , deg [ i ] \+ 1 ); ```   
---|---  
  
## 弦图的最大独立集/最小团覆盖

最大独立集：完美消除序列从前往后，选择所有没有与已经选择的点有直接连边的点．

最小团覆盖：设最大独立集为 {𝑣1,𝑣2,…,𝑣𝑡}{v1,v2,…,vt}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则团的集合 {{𝑣1 +𝑁(𝑣1)},{𝑣2 +𝑁(𝑣2)},…,{𝑣𝑡 +𝑁(𝑣𝑡)}}{{v1+N(v1)},{v2+N(v2)},…,{vt+N(vt)}}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为图的最小团覆盖．时间复杂度均为 𝑂(𝑛 +𝑚)O(n+m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

正确性证明：设以上方案独立集数和团覆盖数为 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由定义得 𝑡 ≤𝛼(𝐺),𝑡 ≥𝜅(𝐺)t≤α(G),t≥κ(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 **Lemma 2** 得，𝛼(𝐺) ≤𝜅(𝐺)α(G)≤κ(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑡 =𝛼(𝐺) =𝜅(𝐺)t=α(G)=κ(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

```text 1 2 3 4 5 6 ``` |  ```text for ( int i = 1 ; i <= n ; i ++ ) if ( ! vis [ p [ i ]]) { ans ++ ; for ( vector < int >:: iterator it = G [ p [ i ]]. begin (); it != G [ p [ i ]]. end (); it ++ ) vis [ * it ] = true ; } ```   
---|---  
  
## 习题

[SPOJ FISHNET - Fishing Net](https://www.spoj.com/problems/FISHNET)

[P3196[HNOI2008] 神奇的国度](https://www.luogu.com.cn/problem/P3196)

[P3852[TJOI2007] 小朋友](https://www.luogu.com.cn/problem/P3852)

## 参考资料

[弦图相关](https://yhx-12243.github.io/OI-transit/memos/15.html)

[2009 WC 讲稿](https://github.com/hzwer/shareOI/blob/master/%E5%9B%BE%E8%AE%BA/%E5%BC%A6%E5%9B%BE%E4%B8%8E%E5%8C%BA%E9%97%B4%E5%9B%BE_%E9%99%88%E4%B8%B9%E7%90%A6.pptx)

[弦图总结 - 租酥雨](https://www.cnblogs.com/zhoushuyu/p/8716935.html)

[R. E. Tarjan and M. Yannakakis, Simple linear-time algorithms to test chordality of graphs,test acyclicity of hypergraphs,and selectively reduce acyclic hypergraphs, SIAM J. Comput., 13 (1984), pp. 566–579.](https://dl.acm.org/doi/abs/10.1137/0213035)

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/chord.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/chord.md "edit.link.title")  
>  __本页面贡献者：[StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [chenjy2003](https://github.com/chenjy2003), [Enter-tainer](https://github.com/Enter-tainer), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [hsfzLZH1](https://github.com/hsfzLZH1), [ImpleLee](https://github.com/ImpleLee), [TianyiQ](https://github.com/TianyiQ)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
