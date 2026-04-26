# 矩阵树定理 - OI Wiki

- Source: https://oi-wiki.org/graph/matrix-tree/

# 矩阵树定理

矩阵树定理解决了一张图的生成树个数计数问题．

## 本篇记号声明

本篇中的图，无论无向还是有向，都允许重边，但是默认没有自环．

有自环的情形

自环并不影响生成树的个数，也不影响下文中 Laplace 矩阵的计算，故而矩阵树定理对有自环的情形依然成立．计算时不必删去自环．如果删去自环，会影响根据 BEST 定理应用矩阵树定理统计有向图的欧拉回路个数．

### 无向图情况

设 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个顶点的无向图．定义度数矩阵 𝐷(𝐺)D(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

𝐷𝑖𝑖(𝐺)=deg(𝑖), 𝐷𝑖𝑗=0, 𝑖≠𝑗.Dii(G)=deg(i), Dij=0, i≠j.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 #𝑒(𝑖,𝑗)#e(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与点 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相连的边数，并定义邻接矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

𝐴𝑖𝑗(𝐺)=𝐴𝑗𝑖(𝐺)=#𝑒(𝑖,𝑗), 𝑖≠𝑗.Aij(G)=Aji(G)=#e(i,j), i≠j.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定义 Laplace 矩阵（亦称 Kirchhoff 矩阵）𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

𝐿(𝐺)=𝐷(𝐺)−𝐴(𝐺).L(G)=D(G)−A(G).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

记图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有生成树个数为 𝑡(𝐺)t(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 有向图情况

设 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个顶点的有向图．定义出度矩阵 𝐷𝑜𝑢𝑡(𝐺)Dout(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

𝐷out𝑖𝑖(𝐺)=degout(𝑖), 𝐷out𝑖𝑗=0, 𝑖≠𝑗.Diiout(G)=degout(i), Dijout=0, i≠j.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

类似地定义入度矩阵 𝐷in(𝐺)Din(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

设 #𝑒(𝑖,𝑗)#e(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指向点 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有向边数，并定义邻接矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

𝐴𝑖𝑗(𝐺)=#𝑒(𝑖,𝑗), 𝑖≠𝑗.Aij(G)=#e(i,j), i≠j.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定义出度 Laplace 矩阵 𝐿outLout![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

𝐿out(𝐺)=𝐷out(𝐺)−𝐴(𝐺).Lout(G)=Dout(G)−A(G).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定义入度 Laplace 矩阵 𝐿inLin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

𝐿in(𝐺)=𝐷in(𝐺)−𝐴(𝐺).Lin(G)=Din(G)−A(G).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

记图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的所有根向树形图个数为 𝑡root(𝐺,𝑘)troot(G,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所谓根向树形图，是说这张图的基图是一棵树，所有的边全部指向父亲．

记图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的所有叶向树形图个数为 𝑡leaf(𝐺,𝑘)tleaf(G,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所谓叶向树形图，是说这张图的基图是一棵树，所有的边全部指向儿子．

## 定理叙述

矩阵树定理具有多种形式．

定义 [𝑛] ={1,2,⋯,𝑛}[n]={1,2,⋯,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子矩阵 𝐴𝑆,𝑇AS,T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为选取 𝐴𝑖,𝑗(𝑖 ∈𝑆,𝑗 ∈𝑇)Ai,j(i∈S,j∈T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素得到的子矩阵．

定理 1（矩阵树定理，无向图，行列式形式）

对于无向图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和任意的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

𝑡(𝐺)=det⁡𝐿(𝐺)[𝑛]∖{𝑘},[𝑛]∖{𝑘}.t(G)=det⁡L(G)[n]∖{k},[n]∖{k}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，无向图的 Laplace 矩阵所有 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶主子式都相等，且都等于图的生成树的个数．

推论 1（矩阵树定理，无向图，特征值形式）

设 𝜆1 ≥𝜆2 ≥⋯ ≥𝜆𝑛−1 ≥𝜆𝑛 =0λ1≥λ2≥⋯≥λn−1≥λn=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐿(𝐺)L(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个特征值，那么有

𝑡(𝐺)=1𝑛𝜆1𝜆2⋯𝜆𝑛−1.t(G)=1nλ1λ2⋯λn−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)定理 2（矩阵树定理，有向图根向树，行列式形式）

对于有向图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和任意的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

𝑡root(𝐺,𝑘)=det⁡𝐿out(𝐺)[𝑛]∖{𝑘},[𝑛]∖{𝑘}.troot(G,k)=det⁡Lout(G)[n]∖{k},[n]∖{k}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，有向图的出度 Laplace 矩阵删去第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列得到的主子式等于以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向树形图的个数．

因此如果要统计一张图所有的根向树形图，只要枚举所有的根 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并对 𝑡root(𝐺,𝑘)troot(G,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求和即可．

定理 3（矩阵树定理，有向图叶向树，行列式形式）

对于有向图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和任意的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

𝑡leaf(𝐺,𝑘)=det⁡𝐿in(𝐺)[𝑛]∖{𝑘},[𝑛]∖{𝑘}.tleaf(G,k)=det⁡Lin(G)[n]∖{k},[n]∖{k}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，有向图的入度 Laplace 矩阵删去第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列得到的主子式等于以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的叶向树形图的个数．

因此如果要统计一张图所有的叶向树形图，只要枚举所有的根 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并对 𝑡leaf(𝐺,𝑘)tleaf(G,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求和即可．

注

根向树形图也被称为内向树形图，但因为计算内向树形图用的是出度，为了不引起 inin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 outout![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的混淆，所以采用了根向这一说法．

## 定理证明

观察上述定理形式极为相似，这里给出一种统一的证明方式，并且将之前的结论拓展到带权的图上．

证明的大致思路如下：

  * 首先，所有情形都可以转化为计数有向图上根向树形图的情形；
  * 利用矩阵语言给出选出的若干边可以构成根向树形图的充要条件；
  * 将选边的操作利用 Cauchy–Binet 公式和 Laplace 矩阵的行列式联系起来；
  * 最后，将行列式形式的结论转化为特征值形式的结论．

### 引理：Cauchy–Binet 公式

引理 1（Cauchy–Binet）

给定 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚 ×𝑛m×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有

det⁡(𝐴𝐵)=∑𝑆⊂[𝑚]; |𝑆|=𝑛det⁡𝐴[𝑛],𝑆det⁡𝐵𝑆,[𝑛],det⁡(AB)=∑S⊂[m]; |S|=ndet⁡A[n],Sdet⁡BS,[n],![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里求和记号的含义是，𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取遍所有 [𝑚][m]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集．如果 𝑛 >𝑚n>m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必然有 det⁡(𝐴𝐵) =0det⁡(AB)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明（组合视角）

参考 [「NOI2021」路径交点](https://loj.ac/p/3533) 的模型，首先考虑行列式的如下组合意义．对于 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶矩阵 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，建立有向无环图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中，顶点集为 𝑉 =[2] ×[𝑛] ⊂ℝ2V=[2]×[n]⊂R2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即平面上的两列点．记左侧一列点为 𝐿 ={𝑙𝑖 =(1,𝑖) :𝑖 ∈[𝑛]}L={li=(1,i):i∈[n]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，右侧的一列点为 𝑅 ={𝑟𝑖 =(2,𝑖) :𝑖 ∈[𝑛]}R={ri=(2,i):i∈[n]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；而有向边集为 𝐸 ={(𝑙𝑖,𝑟𝑗) :𝑖,𝑗 ∈[𝑛]}E={(li,rj):i,j∈[n]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并赋有边权 𝑤(𝑙𝑖,𝑟𝑗) =𝐶𝑖,𝑗w(li,rj)=Ci,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在图中，称大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边的子集 𝐸𝜎 ⊂𝐸Eσ⊂E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一个路径组，如果它的起点互不相同，且终点也互不相同．显然，路径组 𝐸𝜎Eσ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 [𝑛][n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以一一对应．注意到，如果将一个路径组在平面上画出，这些边之间可能会两两相交，而这些交点的数目（计重数）就等于 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆序数．这是因为边 (𝑙𝑖,𝑟𝜎(𝑖))(li,rσ(i))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和边 (𝑙𝑗,𝑟𝜎(𝑗))(lj,rσ(j))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相交，当且仅当 (𝑖 −𝑗)(𝜎(𝑖) −𝜎(𝑗)) <0(i−j)(σ(i)−σ(j))<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即这是一个逆序对．为方便，称对应置换的逆序数的奇偶性，亦即该路径组交点个数的奇偶性，为该路径组的奇偶性．所以，如果将这些路径组按照权重计数，且用偶数交点的路径组数减去奇数交点的路径组数，就会得到行列式的 Leibniz 展开：

det⁡(𝐶)=∑𝜎∈𝑆𝑛sgn(𝜎)∏𝑖∈[𝑛]𝐶𝑖,𝜎(𝑖),det⁡(C)=∑σ∈Snsgn(σ)∏i∈[n]Ci,σ(i),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑆𝑛Sn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 [𝑛][n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的置换群，而 sgn(𝜎)sgn(σ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的符号（当逆序数为偶数时，它等于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；当逆序数为奇数时，它等于 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

在理解行列式的组合意义后，可以利用如下的组合模型证明 Cauchy–Binet 公式．对于 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚 ×𝑛m×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶矩阵 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，建立有向无环图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中，顶点集为 𝑉 =𝐿 ∪𝐷 ∪𝑅V=L∪D∪R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这里，𝐿 ={𝑙𝑖 =(1,𝑖) :𝑖 ∈[𝑛]}L={li=(1,i):i∈[n]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐷 ={𝑑𝑖 =(2,𝑖) :𝑖 ∈[𝑚]}D={di=(2,i):i∈[m]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅 ={𝑟𝑖 =(3,𝑖) :𝑖 ∈[𝑛]}R={ri=(3,i):i∈[n]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；而有向边集为 𝐸 =𝐸𝐿 ∪𝐸𝑅E=EL∪ER![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝐸𝐿 ={(𝑙𝑖,𝑑𝑗) :𝑖 ∈[𝑛],𝑗 ∈[𝑚]}EL={(li,dj):i∈[n],j∈[m]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐸𝑅 ={(𝑑𝑗,𝑟𝑖) :𝑗 ∈[𝑚],𝑖 ∈[𝑛]}ER={(dj,ri):j∈[m],i∈[n]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，分别赋以边权 𝑤(𝑙𝑖,𝑑𝑗) =𝐴𝑖,𝑗w(li,dj)=Ai,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑤(𝑑𝑗,𝑟𝑖) =𝐵𝑗,𝑖w(dj,ri)=Bj,i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．同样考虑自 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 经 𝐷D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径组（路径间两两不共用顶点），按照权重计数，并用偶数交点的路径组数减去奇数交点的路径组数．下面说明，Cauchy–Binet 公式的左右两侧分别用两种方式计算了这一数目．

对于左侧，基于上面描述的图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，建立新图 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其顶点集为 𝑉′ =𝐿 ∪𝑅V′=L∪R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，边集为 𝐸′ ={(𝑙𝑖,𝑟𝑗) :𝑖,𝑗 ∈[𝑛]}E′={(li,rj):i,j∈[n]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且对于边 (𝑙𝑖,𝑟𝑗)(li,rj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 赋以边权 ∑𝑘∈[𝑚]𝐴𝑖,𝑘𝐵𝑘,𝑗∑k∈[m]Ai,kBk,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即在原图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中自 𝑙𝑖li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑟𝑗rj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的简单路径的加权计数．这一边权正是 (𝐴𝐵)𝑖,𝑗(AB)i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这相当于把上述的三层图简化成了两层图．但是，两层图 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的路径组（按权重计）并非和三层图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的路径组一一对应．由于在两层图中，每个路径都对应三层图中若干条简单路径，在对两层图进行路径组的计数时，需要将权重相乘，这相当于对它们对应的三层图中的路径集合两两组合，这必然会造成出现共用中间经停点的情形．但是，这些共用中间经停点的路径对并不会对最后的答案有贡献，因为对于 𝑖1 <𝑖2i1<i2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑗1 <𝑗2j1<j2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和任意中间点 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都存在两种简单路径对 (𝑙𝑖1 →𝑑 →𝑟𝑗1,𝑙𝑖2 →𝑑 →𝑟𝑗2)(li1→d→rj1,li2→d→rj2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑙𝑖1 →𝑑 →𝑟𝑗2,𝑙𝑖2 →𝑑 →𝑟𝑗1)(li1→d→rj2,li2→d→rj1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是这两组路径在三层图中的交点数目奇偶性必然相反，因为如果只看起点和终点，两组路径交换了终点．所以，这些共用中间经停点的路径在简化后的两层图计数时，贡献会两两抵消．对于剩下的情形，如果给定两条路径的起点和终点，那么无论中间的点如何如何选取（只要不选择同一个点），则这两条路径的交点个数的奇偶性不会变．故而，𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中每一个路径组对应的所有原图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的路径组都具有相同的奇偶性．因而，det⁡(𝐴𝐵)det⁡(AB)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 提供了前文所述路径组数差值的一种计算方式．

对于右侧，它相当于枚举了所有可能的中间点的组合．给定任何中间点集合 𝑆 ⊂𝐷 =[𝑚]S⊂D=[m]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 |𝑆| =𝑛|S|=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，分别考虑自 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径组和自 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径组，可以连接得到 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径组，且前两个路径组对应的置换的复合就等于之后的路径组对应的置换，故而前两个路径的奇偶性的乘积等于之后的路径组的奇偶性．所以，所有中间点集合为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径组的计数的差值正等于自 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径组的计数的差值和自 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径组的计数的差值的乘积．对所有可能的 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求和，即得到右式，故而它正是前文所述路径组数差值．

证明（代数视角）

上述组合证明其实可以逐字逐句地翻译成代数证明．这里转而提供另一种技巧性较强的代数证明，但用到了几个常见结论．当 𝑚 <𝑛m<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，行列式为零，因为

rank(𝐴𝐵)≤min{rank(𝐴),rank(𝐵)}≤𝑚<𝑛.rank(AB)≤min{rank(A),rank(B)}≤m<n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当 𝑚 =𝑛m=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，Cauchy–Binet 公式就是，方阵的积的行列式等于方阵的行列式的积．

当 𝑚 >𝑛m>n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，注意到

𝑥𝑚−𝑛det⁡(𝑥𝐼𝑛+𝐴𝐵)=det⁡(𝑥𝐼𝑚+𝐵𝐴).xm−ndet⁡(xIn+AB)=det⁡(xIm+BA).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

又已知结论，det⁡(𝑥𝐼𝑛+𝐶)det⁡(xIn+C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 𝑥𝑛−𝑘xn−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数是 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶主子式的和．故而，比较上式中两侧系数，有

det⁡(𝐴𝐵)=∑𝑆⊂[𝑚]; |𝑆|=𝑛det⁡(𝐵𝐴)𝑆,𝑆=∑𝑆⊂[𝑚]; |𝑆|=𝑛det⁡(𝐵)𝑆,[𝑛]det⁡(𝐴)[𝑛],𝑆=∑𝑆⊂[𝑚]; |𝑆|=𝑛det⁡(𝐴)[𝑛],𝑆det⁡(𝐵)𝑆,[𝑛].det⁡(AB)=∑S⊂[m]; |S|=ndet⁡(BA)S,S=∑S⊂[m]; |S|=ndet⁡(B)S,[n]det⁡(A)[n],S=∑S⊂[m]; |S|=ndet⁡(A)[n],Sdet⁡(B)S,[n].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，第二个等号用到了 𝑚 =𝑛m=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形的结论．

### 用关联矩阵刻画图的结构

对于有向图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，顶点数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，边数为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且边 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 赋有边权 𝑤(𝑒)w(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，可以定义 𝑚 ×𝑛m×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶出度关联矩阵

𝑀out𝑖𝑗={√𝑤(𝑒𝑖),∃𝑢(𝑒𝑖=(𝑣𝑗,𝑢)),0,otherwise,Mijout={w(ei),∃u(ei=(vj,u)),0,otherwise,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

和 𝑚 ×𝑛m×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶入度关联矩阵

𝑀in𝑖𝑗={√𝑤(𝑒𝑖),∃𝑢(𝑒𝑖=(𝑢,𝑣𝑗)),0,otherwise.Mijin={w(ei),∃u(ei=(u,vj)),0,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它们每行都记录了一条边：出度关联矩阵 𝑀outMout![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记录了边的起点，入度关联矩阵 𝑀inMin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记录了边的终点．

简单计算可知

𝐷out(𝐺)=(𝑀out)𝑇𝑀out, 𝐴(𝐺)=(𝑀out)𝑇𝑀in, 𝐷in(𝐺)=(𝑀in)𝑇𝑀in.Dout(G)=(Mout)TMout, A(G)=(Mout)TMin, Din(G)=(Min)TMin.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而有

𝐿out(𝐺)=(𝑀out)𝑇(𝑀out−𝑀in), 𝐿in(𝐺)=(𝑀in−𝑀out)𝑇𝑀in.Lout(G)=(Mout)T(Mout−Min), Lin(G)=(Min−Mout)TMin.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

前文的 Cauchy–Binet 公式表明，Laplace 矩阵的主子式其实是一系列子结构的和．每个子结构都反映了对应的子图的性质．

引理 2

对于 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个子图 (𝑊,𝑆)(W,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若它满足 |𝑊| =|𝑆| ≤𝑛|W|=|S|≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则子图 𝑇 =(𝑉,𝑆)T=(V,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个以 𝑉 ∖𝑊V∖W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向森林，当且仅当对应的算式

det⁡(𝑀out𝑆,𝑊)det⁡(𝑀out𝑆,𝑊−𝑀in𝑆,𝑊)det⁡(MS,Wout)det⁡(MS,Wout−MS,Win)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

不为零．而且，该式当不为零时，必然等于 ∏𝑒∈𝑆𝑤(𝑒)∏e∈Sw(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记作 𝑤(𝑇)w(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

不妨设 𝑤(𝑒) =1w(e)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这是根据行列式的多重线性，每个行列式的每行都可以提取因子 √𝑤(𝑒)w(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这些因子的乘积为 𝑤(𝑇)w(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

首先分析两个因子等于零的条件．前一个因子 det⁡(𝑀out𝑆,𝑊)det⁡(MS,Wout)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 每行至多一个不为零的数字，即 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果有任何一行全为零，则该行列式必然为零．所以，该行列式不为零，当且仅当每行恰好一个 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中每个点都恰好是 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中一条边的起点，且没有两个边共用同一个起点．已知 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成为以 𝑉 ∖𝑊V∖W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向森林，一个必要条件就是除了根之外，所有顶点有且只有一个父节点，这必然使得该因子不为零；但反过来并不一定成立，因为不能保证不存在环，所以还需要考察第二个因子．注意，𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的终点未必在 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．

假定前一个因子不为零，则此时子图 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成为根向森林，当且仅当 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中没有环．此时，后一项 det⁡(𝑀out𝑆,𝑊−𝑀in𝑆,𝑊)det⁡(MS,Wout−MS,Win)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 每行中都有一个 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但可能有一个或零个 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于终点也在 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的边，如果 𝑒𝑖ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的终点是 𝑒𝑗ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的起点，则将 𝑒𝑖ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的行加上 𝑒𝑗ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的行，可以消去 𝑒𝑖ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行中的 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．可以想象，此时该行描述的是 𝑒𝑖ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑒𝑗ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 首尾相接的简单路径．如果该行出现了新的 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么说明 𝑒𝑗ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的终点也在 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内，−1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置就是 𝑒𝑗ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的终点，于事，可以继续找到以 𝑒𝑗ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的终点为起点的边，再次加到该行上．这样的边总是存在的，因为上一段论述说明，𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中每个点都恰好是 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中一条边的起点．这一过程一直持续到该行不在出现 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为止，相当于不断添加新的边到简单路径 𝑒𝑖 →𝑒𝑗 →⋯ →𝑒𝑘ei→ej→⋯→ek![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．此时，如果该行只剩下一个 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么说明 𝑒𝑘ek![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的终点不在所选顶点 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，过程终止；如果上次加入的边恰巧抵消了现有的 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即该行只剩下零，那么说明新边 𝑒𝑘ek![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的终点就是最开始的边 𝑒𝑖ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的起点，即出现了一个环．所以，没有环的充要条件是该一行列式经上述操作可以变形成每行都恰好只有一个 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式．由于这些 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置是各行对应边的起点，此时得到的矩阵实际上就是 det⁡(𝑀out𝑆,𝑊)det⁡(MS,Wout)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

综上所述，如果 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是根向森林，则要么 det⁡(𝑀out𝑆,𝑊) =0det⁡(MS,Wout)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要么 det⁡(𝑀out𝑆,𝑊−𝑀in𝑆,𝑊) =0det⁡(MS,Wout−MS,Win)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；否则，两者均不为零，且乘积等于 (det⁡(𝑀out𝑆,𝑊))2 =1(det⁡(MS,Wout))2=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 带权有向图的矩阵树定理

现在可以证明本文的主要结果．前文所述矩阵树定理均为该定理的特殊情形．

定理 4（矩阵树定理，带权有向图根向树，行列式形式）

对于任意的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

∑𝑇∈Troot(𝐺,𝑘)𝑤(𝑇)=det⁡𝐿out(𝐺)[𝑛]∖{𝑘},[𝑛]∖{𝑘}.∑T∈Troot(G,k)w(T)=det⁡Lout(G)[n]∖{k},[n]∖{k}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，Troot(𝐺,𝑘)Troot(G,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向树形图的集合．

证明

记 𝑊 =[𝑛] ∖{𝑘}W=[n]∖{k}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为除去 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点外的剩余顶点的集合．那么，根据 Cauchy–Binet 公式，右式可以写作

det⁡𝐿out(𝐺)𝑊,𝑊=∑𝑆⊂[𝑚]; |𝑆|=𝑛−1det⁡(𝑀out𝑆,𝑊)det⁡(𝑀out𝑆,𝑊−𝑀in𝑆,𝑊).det⁡Lout(G)W,W=∑S⊂[m]; |S|=n−1det⁡(MS,Wout)det⁡(MS,Wout−MS,Win).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

遍历所有的 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由引理 2，当且仅当 𝑇 =(𝑉,𝑆)T=(V,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成一个以 𝑉 ∖𝑊 ={𝑘}V∖W={k}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向森林时，亦即 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向树形图时，右侧累加一个 𝑤(𝑇)w(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当 𝑤(𝑒) =1w(e)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，每个树的权值都是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则左侧就是所有树的计数，即 𝑡root(𝐺,𝑘)troot(G,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这就得到定理 2．类比上文，可以将结论直接推广于叶向树形图，这就得到定理 3．最后，要得到无向图上的生成树计数，可以应用如下推论．

推论 4（矩阵树定理，带权无向图，行列式形式）

对于无向图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和任意的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

∑𝑇∈T(𝐺)𝑤(𝑇)=det⁡𝐿(𝐺)[𝑛]∖{𝑘},[𝑛]∖{𝑘}.∑T∈T(G)w(T)=det⁡L(G)[n]∖{k},[n]∖{k}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，T(𝐺)T(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成树的集合．这也说明，𝐿(𝐺)L(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有 (𝑛 −1)(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶主子式都相等．

证明

对于无向图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以构建有向图 𝐺′ =(𝑉,𝐸′)G′=(V,E′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝐸′ ={(𝑣𝑖,𝑣𝑗) :(𝑣𝑖,𝑣𝑗) ∈𝐸} ∪{(𝑣𝑗,𝑣𝑖) :(𝑣𝑖,𝑣𝑗) ∈𝐸}E′={(vi,vj):(vi,vj)∈E}∪{(vj,vi):(vi,vj)∈E}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即每条 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的无向边都拆成有向图中方向相反的两条有向边．任取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝐺′G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向树形图和 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的生成树一一对应．由前者向后者，只需要移除边的定向和根的选取；由后者向前者，只需要从选定的根 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始逐边选取根向作为边的定向．所以，此时有

∑𝑇∈T(𝐺)𝑤(𝑇)=∑𝑇∈Troot(𝐺′,𝑘)𝑤(𝑇)=det⁡𝐿out(𝐺′)[𝑛]∖{𝑘},[𝑛]∖{𝑘}=det⁡𝐿(𝐺)[𝑛]∖{𝑘},[𝑛]∖{𝑘}.∑T∈T(G)w(T)=∑T∈Troot(G′,k)w(T)=det⁡Lout(G′)[n]∖{k},[n]∖{k}=det⁡L(G)[n]∖{k},[n]∖{k}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此处用到了结论 𝐿out(𝐺′) =𝐿(𝐺)Lout(G′)=L(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这容易直接验证．

### 特征值形式

仍然首先考虑有向图上的结论．

定理 5

对于有向图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义多元多项式

𝜒(𝑥1,⋯,𝑥𝑛)=det⁡(diag(𝑥1,⋯,𝑥𝑛)−𝐿out(𝐺)).χ(x1,⋯,xn)=det⁡(diag(x1,⋯,xn)−Lout(G)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，diag(𝑥1,⋯,𝑥𝑛)diag(x1,⋯,xn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是指以 𝑥1,⋯,𝑥𝑛x1,⋯,xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为对角线元素的对角矩阵．那么，

(−1)𝑛−𝑟[𝑥𝑘1,⋯,𝑥𝑘𝑟]𝜒(𝑥1,⋯,𝑥𝑛)(−1)n−r[xk1,⋯,xkr]χ(x1,⋯,xn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就等于 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的以 {𝑘1,⋯,𝑘𝑟}{k1,⋯,kr}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向森林的（带权的）计数．

证明

仿照定理 4 的证明，注意到如果令 𝑊 =[𝑛] ∖{𝑘1,⋯,𝑘𝑟}W=[n]∖{k1,⋯,kr}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，定理中的系数就是 det⁡𝐿out(𝐺)𝑊,𝑊det⁡Lout(G)W,W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（这一点不妨直接观察行列式的 Leibniz 展开式）．根据 Cauchy–Binet 公式，它等于

det⁡𝐿out(𝐺)𝑊,𝑊=∑𝑆⊂[𝑚]; |𝑆|=𝑛−𝑟det⁡(𝑀out𝑆,𝑊)det⁡(𝑀out𝑆,𝑊−𝑀in𝑆,𝑊).det⁡Lout(G)W,W=∑S⊂[m]; |S|=n−rdet⁡(MS,Wout)det⁡(MS,Wout−MS,Win).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

遍历所有的 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由引理 2，当且仅当 𝑇 =(𝑉,𝑆)T=(V,S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成一个以 𝑉 ∖𝑊 ={𝑘1,⋯,𝑘𝑟}V∖W={k1,⋯,kr}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向森林时，右侧累加一个 𝑤(𝑇)w(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

将 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代入所有的未知元，得到 Laplace 矩阵的特征多项式

𝑃(𝑥)=det⁡(𝑥𝐼−𝐿out(𝐺))=𝜒(𝑥,⋯,𝑥).P(x)=det⁡(xI−Lout(G))=χ(x,⋯,x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)引理 3

Laplace 矩阵 𝐿out(𝐺)Lout(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至少有一个特征值为零．

证明

只要证明它的行列式为零即可．仿照定理 4 和 5 的证明，取 𝑊 =∅W=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则这个行列式的大小应该等于有零棵树的根向森林的数目．这并不存在，所以该行列式等于零．

推论 5

对于有向图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所有由 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树构成的根向森林的权值的总和等于系数

(−1)𝑛−𝑘[𝑥𝑘]𝑃(𝑥).(−1)n−k[xk]P(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

对所有可能的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个根的选择求和即可．

定义 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)\- 生成森林 是图的一个生成子图，使得这个子图有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个连通分量且无环．

推论 6

记无向图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)\- 生成森林 的集合为 T𝑘(𝐺)Tk(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则

∑𝑇∈T𝑘(𝐺)𝑤(𝑇)𝑄(𝑇)=(−1)𝑛−𝑘[𝑥𝑘]𝑃(𝑥).∑T∈Tk(G)w(T)Q(T)=(−1)n−k[xk]P(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，𝑄(𝑇)Q(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为森林 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中每个连通分量的顶点数目的乘积．特别地，当 𝑘 =1k=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有 𝑄(𝑇) =𝑛Q(T)=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而

𝑛∑𝑇∈T(𝐺)𝑤(𝑇)=𝜆1𝜆2⋯𝜆𝑛−1.n∑T∈T(G)w(T)=λ1λ2⋯λn−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

仿照推论 4 的证明，可以直接利用推论 5 的结论．有向图中每一个由 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 棵树构成的根向森林都对应一个无向图中的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)\- 生成森林．但是，由于每个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)\- 生成森林 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑄(𝑇)Q(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种选择根的方法，它会出现在 𝑄(𝑇)Q(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个有向图的根向森林中．

## 应用

### Cayley 公式

推论 7（Cayley）

大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的带标号的无根树有 𝑛𝑛−2nn−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．

证明

等价地，只要求得 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个顶点的完全图的生成树的数目为 𝑛𝑛−2nn−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．为此，写出 Laplace 矩阵

𝐿(𝐺)=⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝𝑛−1−1⋯−1−1𝑛−1⋯−1⋮⋮⋱⋮−1−1⋯𝑛−1⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠𝑛×𝑛.L(G)=(n−1−1⋯−1−1n−1⋯−1⋮⋮⋱⋮−1−1⋯n−1)n×n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

计算它的任意主子式，有

det⁡(𝑛𝐼𝑛−1−𝟏𝟏𝑇)=𝑛𝑛−1det⁡(𝐼𝑛−1−𝑛−1𝟏𝟏𝑇)=𝑛𝑛−1(1−𝑛−1𝟏𝑇𝟏)=𝑛𝑛−1(1−(𝑛−1)/𝑛)=𝑛𝑛−2.det⁡(nIn−1−11T)=nn−1det⁡(In−1−n−111T)=nn−1(1−n−11T1)=nn−1(1−(n−1)/n)=nn−2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

应用定理 1 即得到结论．

### BEST 定理

前置知识：[欧拉图](../euler/)

这一定理将有向欧拉图中欧拉回路的数目和该图的根向树形图的数目联系起来，从而解决了有向图中的欧拉回路的计数问题．注意，任意无向图中的欧拉回路的计数问题是 NP 完全的．

在实现该算法时，应当首先判定给定图是否是欧拉图，移除所有零度顶点，然后建图计算根向树形图的个数，并由 BEST 定理得到欧拉回路的计数．注意，如果所求欧拉回路个数要求以给定点作为起点，需要将答案再乘上该点出度，相当于枚举回路中首条边．

在证明 BEST 定理之前，需要知道如下结论．

性质（有向图具有欧拉回路的判定）

一个有向图具有欧拉回路，当且仅当非零度顶点是强连通的，且所有顶点的出度和入度相等．

对于欧拉图，因为出度和入度相等，可以将它们略去上标，记作 deg(𝑣)deg(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．BEST 定理可以叙述如下．

定理 6（BEST 定理）

设 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是有向欧拉图，𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为任意顶点，那么 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的不同欧拉回路总数 ec(𝐺)ec(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是

ec(𝐺)=𝑡root(𝐺,𝑘)∏𝑣∈𝑉(deg⁡(𝑣)−1)!.ec(G)=troot(G,k)∏v∈V(deg⁡(v)−1)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这也说明，对欧拉图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的任意两个节点 𝑘,𝑘′k,k′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑡root(𝐺,𝑘) =𝑡root(𝐺,𝑘′)troot(G,k)=troot(G,k′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

证明的大致思路是建立以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为起点的欧拉回路和以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向树形图以及各个顶点处出边的排列的对应关系．在指定欧拉回路的顶点后，需要证明的计数应当等于

deg(𝑘)ec(𝐺)=𝑡root(𝐺,𝑘)deg⁡(𝑘)!∏𝑣≠𝑘(deg⁡(𝑣)−1)!.deg(k)ec(G)=troot(G,k)deg⁡(k)!∏v≠k(deg⁡(v)−1)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这一计数的组合含义对应的构造如下．对于起点为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的欧拉回路，根据回路中每条边的出现顺序，可以构造出

  * 一个以 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的根向树形图，由所有非根顶点处的最后一条出边组成，即 𝑡root(𝐺,𝑘)troot(G,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 根 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处所有出边的排列顺序，即 deg(𝑘)!deg(k)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，和
  * 非根顶点 𝑣 ≠𝑘v≠k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处除去最后一条出边之外的其他所有出边的排列顺序，即 (deg(𝑣) −1)!(deg(v)−1)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

下面说明，这样的构造得到的映射是双射．

一方面，给定欧拉回路，要证明所有非根顶点处的最后一条出边组成了一个根向树形图．根据构造，树中每个非根顶点的确只有一条出边，所以只需要证明这些出边不会成环．注意到，如果将所有顶点根据它在欧拉回路最后一次出现的顺序排序，那么非根顶点的最后一次出边必然指向顺序严格更靠后的顶点．如果存在环，那么环中就有一个顺序最靠后的顶点，因为它在环中，所以它指向了一个顺序并不靠后的点，这与上文矛盾．所以，非根顶点的最后一次出边必然构成根向树形图．

另一方面，给定任意根向树形图和其余出边的排列顺序，可以复原出一条欧拉回路，使得该欧拉回路经上述构造后可以得到给定的根向树形图和其余出边的排列顺序．对此，只需要从根 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，每当到达一个顶点时，都根据给定的该顶点的出边排列顺序，选择顺序最靠前的、尚未经过的出边作为欧拉回路中本次的出边；如果该顶点处的排列中所有出边都已经经过了，就选择根向树形图中该顶点的出边作为欧拉回路中本次的出边．因为图是欧拉图，每个顶点的入度都等于出度，所以，这一过程不会在非根顶点处终止，即所得路径的确是回路．要证明所得路径是合法的欧拉回路，只需要证明这一过程能够遍历所有边就可以．

如果不能，则必然有某个顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的某个出边没有遍历到．考察顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不能是根，因为最后会终止在根，如果根仍有出边剩余，这与过程终止矛盾．所以，𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然不是根．根据前文描述的过程，只要非根顶点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有任何出边剩余，那么非根顶点在树中的出边 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然剩余．记 𝑒 =(𝑣,𝑢)e=(v,u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的某个入边没有遍历到，根据 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的出度等于入度，必然有 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的某条出边没有遍历到．然后，可以类似地考察顶点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这些推理将考察的顶点从 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 移动到了 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即沿着根向树形图向树的根移动了一步．可以归纳地证明，此时必有根 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的某个出边没有遍历到．前文已经说明这不可能，故得到矛盾．这说明，上一段所得路径的确是合法的欧拉回路．

可以验证这些映射都是单射，则必然同为双射．原命题得证．

## 实现

根据图写出 Laplace 矩阵，删去一行一列，求所得矩阵的行列式即可．求行列式可以使用 Gauss–Jordan 消元法．

例如，一个正方形图的生成树个数

⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝2000020000200002⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠−⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝0101101001011010⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠=⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝2−10−1−12−100−12−1−10−12⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠(2000020000200002)−(0101101001011010)=(2−10−1−12−100−12−1−10−12)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)∣2−10−12−10−12∣=4|2−10−12−10−12|=4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以用 Gauss–Jordan 消元解决，时间复杂度为 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 ``` |  ```text #include <algorithm> #include <cassert> #include <cmath> #include <cstdio> #include <cstring> #include <iostream> using namespace std ; constexpr int MOD = 100000007 ; constexpr double eps = 1e-7 ; struct matrix { static constexpr int MAXN = 20 ; int n , m ; double mat [ MAXN ][ MAXN ]; matrix () { memset ( mat , 0 , sizeof ( mat )); } void print () { cout << "MATRIX " << n << " " << m << endl ; for ( int i = 0 ; i < n ; i ++ ) { for ( int j = 0 ; j < m ; j ++ ) { cout << mat [ i ][ j ] << " \t " ; } cout << endl ; } } void random ( int n ) { this -> n = n ; this -> m = n ; for ( int i = 0 ; i < n ; i ++ ) for ( int j = 0 ; j < n ; j ++ ) mat [ i ][ j ] = rand () % 100 ; } void initSquare () { this -> n = 4 ; this -> m = 4 ; memset ( mat , 0 , sizeof ( mat )); mat [ 0 ][ 1 ] = mat [ 0 ][ 3 ] = 1 ; mat [ 1 ][ 0 ] = mat [ 1 ][ 2 ] = 1 ; mat [ 2 ][ 1 ] = mat [ 2 ][ 3 ] = 1 ; mat [ 3 ][ 0 ] = mat [ 3 ][ 2 ] = 1 ; mat [ 0 ][ 0 ] = mat [ 1 ][ 1 ] = mat [ 2 ][ 2 ] = mat [ 3 ][ 3 ] = -2 ; this -> n \-- ; // 去一行 this -> m \-- ; // 去一列 } double gauss () { double ans = 1 ; for ( int i = 0 ; i < n ; i ++ ) { int sid = -1 ; for ( int j = i ; j < n ; j ++ ) if ( abs ( mat [ j ][ i ]) > eps ) { sid = j ; break ; } if ( sid == -1 ) continue ; if ( sid != i ) { for ( int j = 0 ; j < n ; j ++ ) { swap ( mat [ sid ][ j ], mat [ i ][ j ]); ans = \- ans ; } } for ( int j = i \+ 1 ; j < n ; j ++ ) { double ratio = mat [ j ][ i ] / mat [ i ][ i ]; for ( int k = 0 ; k < n ; k ++ ) { mat [ j ][ k ] -= mat [ i ][ k ] * ratio ; } } } for ( int i = 0 ; i < n ; i ++ ) ans *= mat [ i ][ i ]; return abs ( ans ); } }; int main () { srand ( 1 ); matrix T ; // T.random(2); T . initSquare (); T . print (); double ans = T . gauss (); T . print (); cout << ans << endl ; } ```   
---|---  
  
## 例题

例题 1：[「HEOI2015」小 Z 的房间](https://loj.ac/problem/2122)

**解** 矩阵树定理的裸题．将每个空房间看作一个结点，根据输入的信息建图，得到 Laplace 矩阵后，任意删掉 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列，求这个子式的行列式即可．求行列式的方法就是高斯消元成上三角阵然后算对角线积．另外本题需要在模 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数子环 ℤ𝑘Zk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上进行高斯消元，采用辗转相除法即可．

例题 2：[「FJOI2007」轮状病毒](https://www.luogu.com.cn/problem/P2144)

**解** 本题的解法很多，这里用矩阵树定理是最直接的解法．当输入为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，容易写出其 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶的 Laplace 矩阵为：

𝐿𝑛=⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣𝑛−1−1−1⋯−1−1−13−10⋯0−1−1−13−1⋯00−10−13⋯00⋮⋮⋮⋮⋱⋮⋮−1000⋯3−1−1−100⋯−13⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦𝑛+1Ln=[n−1−1−1⋯−1−1−13−10⋯0−1−1−13−1⋯00−10−13⋯00⋮⋮⋮⋮⋱⋮⋮−1000⋯3−1−1−100⋯−13]n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

求出它的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶子式的行列式即可，剩下的只有高精度计算了．

例题 2+

将例题 2 的数据加强，要求 𝑛 ≤100000n≤100000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是答案对 1000007 取模．（本题求解需要一些线性代数知识）

**解** 推导递推式后利用矩阵快速幂即可求得．

推导递推式的过程：

注意到 𝐿𝑛Ln![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 删掉第 1 行第 1 列以后得到的矩阵很有规律，因此其实就是在求矩阵

𝑀𝑛=⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣3−10⋯0−1−13−1⋯000−13⋯00⋮⋮⋮⋱⋮⋮000⋯3−1−100⋯−13⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦𝑛Mn=[3−10⋯0−1−13−1⋯000−13⋯00⋮⋮⋮⋱⋮⋮000⋯3−1−100⋯−13]n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的行列式．对 𝑀𝑛Mn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行列式按第一列展开，得到

det⁡𝑀𝑛=3det⁡⎡⎢ ⎢ ⎢ ⎢ ⎢⎣3−1⋯00−13⋯00⋮⋮⋱⋮⋮00⋯3−100⋯−13⎤⎥ ⎥ ⎥ ⎥ ⎥⎦𝑛−1+det⁡⎡⎢ ⎢ ⎢ ⎢ ⎢⎣−10⋯0−1−13⋯00⋮⋮⋱⋮⋮00⋯3−100⋯−13⎤⎥ ⎥ ⎥ ⎥ ⎥⎦𝑛−1+(−1)𝑛det⁡⎡⎢ ⎢ ⎢ ⎢ ⎢⎣−10⋯0−13−1⋯00−13⋯00⋮⋮⋱⋮⋮00⋯3−1⎤⎥ ⎥ ⎥ ⎥ ⎥⎦𝑛−1det⁡Mn=3det⁡[3−1⋯00−13⋯00⋮⋮⋱⋮⋮00⋯3−100⋯−13]n−1+det⁡[−10⋯0−1−13⋯00⋮⋮⋱⋮⋮00⋯3−100⋯−13]n−1+(−1)ndet⁡[−10⋯0−13−1⋯00−13⋯00⋮⋮⋱⋮⋮00⋯3−1]n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上述三个矩阵的行列式记为 𝑑𝑛−1,𝑎𝑛−1,𝑏𝑛−1dn−1,an−1,bn−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．  
注意到 𝑑𝑛dn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是三对角行列式，采用类似的展开的方法可以得到 𝑑𝑛dn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 具有递推公式 𝑑𝑛 =3𝑑𝑛−1 −𝑑𝑛−2dn=3dn−1−dn−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．类似地，采用展开的方法可以得到 𝑎𝑛−1 = −𝑑𝑛−2 −1an−1=−dn−2−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以及 ( −1)𝑛𝑏𝑛−1 = −𝑑𝑛−2 −1(−1)nbn−1=−dn−2−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．  
将这些递推公式代入上式，得到：

det⁡𝑀𝑛=3𝑑𝑛−1−2𝑑𝑛−2−2det⁡Mn=3dn−1−2dn−2−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 𝑑𝑛=3𝑑𝑛−1−𝑑𝑛−2dn=3dn−1−dn−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是猜测 det⁡𝑀𝑛det⁡Mn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是非齐次的二阶线性递推．采用待定系数法可以得到最终的递推公式为

det⁡𝑀𝑛=3det⁡𝑀𝑛−1−det⁡𝑀𝑛−2+2det⁡Mn=3det⁡Mn−1−det⁡Mn−2+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

改写成 (det⁡𝑀𝑛 +2) =3(det⁡𝑀𝑛−1 +2) −(det⁡𝑀𝑛−2 +2)(det⁡Mn+2)=3(det⁡Mn−1+2)−(det⁡Mn−2+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，采用矩阵快速幂即可求出答案．

例题 3：[「BZOJ3659」WHICH DREAMED IT](https://hydro.ac/p/bzoj-P3659)

**解** 本题是 BEST 定理的直接应用，但是要注意，由于题目规定「两种完成任务的方式算作不同当且仅当使用钥匙的顺序不同」，对每个欧拉回路，1 号房间可以沿着任意一条出边出发，从而答案还要乘以 1 号房间的出度．

例题 4：[「联合省选 2020 A」作业题](https://loj.ac/p/3304)

**解** 首先需要用莫比乌斯反演转化成计算所有生成树的边权和，因为与本文关系不大所以略去．

将行列式的项写成 𝑤𝑖𝑥 +1wix+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最后答案是行列式的一次项系数，因为答案实际上是钦定一条边之后的生成树个数 ××![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这条边的边权之和，那么被乘上一次项系数的边就是被钦定的边．此时可以把高于一次的项忽略掉，复杂度 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

[「北京省选集训 2019」生成树计数](https://www.luogu.com.cn/problem/P5296) 是较为一般化的情况：计算生成树权值之和的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次方之和，用类似方法构造行列式的项即可，具体见洛谷题解．

例题 5：[AGC051D C4](https://atcoder.jp/contests/agc051/tasks/agc051_d)

**解** 无向图欧拉回路计数是 NPC 问题，但这题的图较为简单，确定了 𝑆 −𝑇S−T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边中从 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指向 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有多少条，就可以确定其他三条边的定向方案，然后直接套用 BEST 定理就得到 𝑂(𝑎 +𝑏 +𝑐 +𝑑)O(a+b+c+d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的做法．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/matrix-tree.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/matrix-tree.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Early0v0](https://github.com/Early0v0), [pw384](mailto:pw384@pku.edu.cn), [Enter-tainer](https://github.com/Enter-tainer), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [Watersail2005](https://github.com/Watersail2005), [Xeonacid](https://github.com/Xeonacid), [369Pai](https://github.com/369Pai), [ayuusweetfish](https://github.com/ayuusweetfish), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [Great-designer](https://github.com/Great-designer), [Henry-ZHR](https://github.com/Henry-ZHR), [Menci](https://github.com/Menci), [Molmin](https://github.com/Molmin), [ouuan](https://github.com/ouuan), [pare1lel](https://github.com/pare1lel), [pw384](https://github.com/pw384), [s0cks5](https://github.com/s0cks5), [StudyingFather](https://github.com/StudyingFather), [TianyiQ](https://github.com/TianyiQ), [warzone-oier](https://github.com/warzone-oier), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
