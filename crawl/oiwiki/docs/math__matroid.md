# 拟阵 - OI Wiki

- Source: https://oi-wiki.org/math/matroid/

# 拟阵

## 引言

**拟阵（Matroid）** 是哈斯勒·惠特尼（Hassler Whitney）于 1935 年提出的一种抽象代数结构，旨在统一和推广关于独立性的概念，例如线性代数中的线性无关性和图论中的无环性．

拟阵为处理与独立性相关的优化问题提供了强大的理论工具，广泛应用于组合数学、图论、算法设计等领域，尤其在为贪心算法等优化方法提供数学理论支持方面发挥了重要作用．

## 定义

### 拟阵

一个 **拟阵（Matroid）** 可以表示为 𝑀 =(𝐸,I)M=(E,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中：

  * 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个有限集，称为 **基础集（Ground Set）** ．
  * II![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集族，称为 **独立集族（Family of Independent Sets）** ，其中的集合称为 **独立集（Independent Set）** ．有以下三个性质：

    * **非空性** ：空集是独立的，即 ∅ ∈I∅∈I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

    * **遗传性** ：独立集的任意子集也是独立集．若 𝐼 ∈II∈I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对于任意 𝐼′ ⊆𝐼I′⊆I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝐼′ ∈II′∈I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

    * **扩张性** ：若 𝐼,𝐽 ∈II,J∈I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 |𝐼| <|𝐽||I|<|J|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则存在 𝑗 ∈𝐽 ∖𝐼j∈J∖I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝐼 ∪{𝑗} ∈II∪{j}∈I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如果一个形如 (𝐸,I)(E,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结构满足上述三个性质，则称其为一个拟阵．

### 基

**基（Basis）** 是拟阵中极大的独立集，即无法再添加元素而保持独立性的独立集．所有基的集合称为 **基集族** ，记为 BB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**性质** ：

  1. **等基数性** ：所有基的大小都相同，称为拟阵的 **秩（Rank）** ．

  2. **扩张性** ：任何独立集通过添加基中的元素都可以扩张为一个基．

### 圈

**圈（Circuit）** 是拟阵中最小的依赖集，即其所有真子集都是独立的，但自身不是独立集，任意两个圈之间不存在包含关系．

### 秩

**秩函数（Rank Function）** 𝑟 :2𝐸 →ℤ≥0r:2E→Z≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将基础集 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集映射到非负整数．对于任意 𝑆 ⊆𝐸S⊆E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑟(𝑆)r(S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中最大独立集的大小，即

𝑟(𝑆)=max{|𝐼|∣𝐼⊆𝑆∧𝐼∈I}.r(S)=max{|I|∣I⊆S∧I∈I}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**性质** ：

  1. **非负性** ：对于任意 𝑆 ⊆𝐸S⊆E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 0 ≤𝑟(𝑆) ≤|𝑆|0≤r(S)≤|S|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  2. **单调性** ：若 𝐴 ⊆𝐵 ⊆𝐸A⊆B⊆E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑟(𝐴) ≤𝑟(𝐵)r(A)≤r(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  3. **次模性** ：对于任意 𝐴,𝐵 ⊆𝐸A,B⊆E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑟(𝐴 ∪𝐵) +𝑟(𝐴 ∩𝐵) ≤𝑟(𝐴) +𝑟(𝐵)r(A∪B)+r(A∩B)≤r(A)+r(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 典型示例

### 1\. 均匀拟阵（Uniform Matroid）

**定义** ：给定基础集 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和非负整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，均匀拟阵 𝑈𝑘,𝐸Uk,E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的独立集族是所有大小不超过 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集，表示为：

I={𝐼⊆𝐸∣|𝐼|≤𝑘}．I={I⊆E∣|I|≤k}．![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * **基（Bases）** ：所有大小为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集．

  * **圈（Circuits）** ：所有大小为 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集．

  * **秩（Rank）** ：𝑟(𝐸) =min(𝑘,|𝐸|)r(E)=min(k,|E|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即独立集中最多能有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素．

### 2\. 图拟阵（Graphical Matroid）

**定义** ：给定一个无向图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，图拟阵 𝑀(𝐺)M(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基础集是边集 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其独立集族是所有不包含环的边集，即所有的森林．

  * **基** ：图中的生成树（在连通图的情况下）．生成树是极大的独立集，无法再增加边而不形成环．

  * **圈** ：图中的简单环，去掉环中的任意一条边，剩余部分都为独立集．

  * **秩** ：𝑟(𝐸) =|𝑉| −𝑐r(E)=|V|−c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是图的连通分支数．对于一个连通的无向图，其秩等于顶点数减一，即 |𝑉| −1|V|−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 3\. 线性拟阵（Linear Matroid）

**定义** ：线性拟阵基于向量空间．给定向量空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，基础集 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的一组有限向量，其独立集族是 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有线性无关的向量子集．

  * **基** ：极大的线性无关向量集，其大小等于向量空间的维数．

  * **圈** ：最小的线性相关向量集合，其任意真子集都是独立的，而自身是线性相关的．

  * **秩** ：线性拟阵的秩 𝑟(𝐸) =dim⁡(𝑉)r(E)=dim⁡(V)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即向量空间的维数．独立集的大小不能超过向量空间的维数．

### 4\. 划分拟阵（Partition Matroid）

**定义** ：将基础集 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 划分为不相交的子集 𝐸1,𝐸2,…,𝐸𝑚E1,E2,…,Em![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并为每个子集 𝐸𝑖Ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指定一个非负整数 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．划分拟阵的独立集族由满足每个部分选取元素数量不超过 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集组成，表示为：

I={𝐼⊆𝐸∣∀𝑖,|𝐼∩𝐸𝑖|≤𝑘𝑖}．I={I⊆E∣∀i,|I∩Ei|≤ki}．![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * **基** ：满足 |𝐼 ∩𝐸𝑖| =𝑘𝑖|I∩Ei|=ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的独立集是划分拟阵的基．每个基在每个子集中选取了恰好 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素．

  * **圈** ：划分拟阵的圈是最小的依赖集，即包含至少一个元素数量超过 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集．

  * **秩** ：划分拟阵的秩为 𝑟(𝐸) =∑𝑚𝑖=1𝑘𝑖r(E)=∑i=1mki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即最大独立集的大小等于每个子集中允许选取的最大元素数的总和．

### 5\. 有色拟阵（Colored Matroid）

**定义** ：有色拟阵是划分拟阵的一种特殊形式，其中每个元素都赋予了颜色．给定基础集 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和颜色集 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每个元素 𝑒 ∈𝐸e∈E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都与某个颜色 𝑐 ∈𝐶c∈C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相关联．有色拟阵的独立集不仅需要满足普通拟阵的独立性条件，还必须遵守颜色上指定的限制，例如同一种颜色的元素在独立集中最多选取一定数量．

  * **基** ：有色拟阵的基是符合颜色限制和独立性条件的极大独立集．

  * **圈** ：圈是最小的依赖集，包含至少一个违反独立性或颜色限制的元素集合．

  * **秩** ：有色拟阵的秩是满足颜色限制条件下的最大独立集大小．它既依赖于拟阵的结构，也依赖于颜色限制的具体规定．

## 构造和运算

### 对偶

给定拟阵 𝑀 =(𝐸,I)M=(E,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其 **对偶拟阵** 𝑀∗ =(𝐸,I∗)M∗=(E,I∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义为：

I∗={𝐼∗⊆𝐸∣∃𝐵∈I,|𝐵|=𝑟(𝐸),𝐵⊆𝐸∖𝐼∗}．I∗={I∗⊆E∣∃B∈I,|B|=r(E),B⊆E∖I∗}．![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**性质** ：

  * **基** ：对偶拟阵 𝑀∗M∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基是 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基在基础集 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的补集．换句话说，如果 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基，那么 𝐸 ∖𝐵E∖B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 𝑀∗M∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基．

  * **秩函数** ：对偶拟阵的秩函数为 𝑟∗(𝑆) =|𝑆| −𝑟(𝐸) +𝑟(𝐸 ∖𝑆)r∗(S)=|S|−r(E)+r(E∖S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐸E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集．这意味着对偶拟阵的秩可以通过基础集的大小、原拟阵的秩以及从基础集中移除 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后的秩来计算．

  * **自反性** ：对偶拟阵的对偶仍是原拟阵，即 (𝑀∗)∗ =𝑀(M∗)∗=M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**示例** ：

对于一个无向图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，图拟阵 𝑀(𝐺)M(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对偶 𝑀(𝐺)∗M(G)∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是由图的割集组成的拟阵．图拟阵 𝑀(𝐺)M(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基是图中的生成树，而其对偶 𝑀(𝐺)∗M(G)∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基是这些生成树的补集，对偶 𝑀(𝐺)∗M(G)∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的圈则是图的最小割集，即将图分成两个不连通部分的最小边集．

例如，考虑一个简单的三角形图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其边集为 𝐸 ={𝑒1,𝑒2,𝑒3}E={e1,e2,e3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．图拟阵 𝑀(𝐺)M(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基是两条边的集合（如 {𝑒1,𝑒2}{e1,e2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），而对偶拟阵 𝑀(𝐺)∗M(G)∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基是单条边的集合（如 {𝑒3}{e3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），𝑀(𝐺)∗M(G)∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的圈是两条边的集合（即最小割集，如 {𝑒2,𝑒3}{e2,e3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），因为移除其中的一条边就会将图分割为两个连通分支．

### 删除和收缩

**删除（Deletion）** ：

对于 𝐴 ⊆𝐸A⊆E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，拟阵 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 删除 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后得到新的拟阵 𝑀 ∖𝐴M∖A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其独立集族 I′I′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义为：

I′={𝐼⊆𝐸∖𝐴∣𝐼∈I}．I′={I⊆E∖A∣I∈I}．![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以看出，删除操作就是从拟阵中移除某些元素，并保留剩余元素形成的独立集，其保持原独立集不变，只是移除了元素．

**收缩（Contraction）** ：

对于 𝐴 ⊆𝐸A⊆E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，拟阵 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 收缩 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后得到拟阵 𝑀/𝐴M/A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其独立集族 I″I″![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义为：

I″={𝐼⊆𝐸∖𝐴∣∃𝐵⊆𝐴,𝐵∈I,𝑟(𝐵)=𝑟(𝐴),𝐼∪𝐵∈I}I″={I⊆E∖A|∃B⊆A,B∈I,r(B)=r(A),I∪B∈I}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

收缩操作可以理解为将集合 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素缩约，并考虑剩下的元素与 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基一起形成的独立集．收缩的结果依赖于集合 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基，缩约后的独立集实际上是对原拟阵中更高秩的子集进行约简后得到的独立集．

**示例 - 图拟阵** ：

  * **删除** ：在图拟阵中，删除操作即从图中删除一些边．一个图 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 删除某条边后，考虑的是剩余边所形成的独立集，即那些不包含环的边集．例如，如果从一个三角形图中删除一条边，剩下的两个边仍然是一个森林．

  * **收缩** ：收缩操作则是将某条边收缩为一个顶点．对于图拟阵，收缩一条边相当于将这条边的两个顶点合并成一个顶点，并删除该边，合并顶点后，图中的其他边仍然可以形成独立集．例如，在一个三角形图中，收缩任意一条边将把两个顶点合并成一个，剩下的两条边将构成一个新的拟阵．

## 拟阵和贪心

**问题描述** ：

拟阵的应用之一是解决贪心算法中的最优化问题．具体而言，给定一个拟阵 𝑀 =(𝑆,I)M=(S,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是基础集，II![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是独立集族．对于每个元素 𝑥 ∈𝑆x∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，赋予一个正整数权值 𝑤(𝑥)w(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，目标是找到权值最大的独立集，形式化为：

max𝐴∈I𝑤(𝐴)=max𝐴∈I∑𝑥∈𝐴𝑤(𝑥)maxA∈Iw(A)=maxA∈I∑x∈Aw(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

显然，权值最大独立集必须是极大独立集．如果一个独立集 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是极大独立集，则存在一个可以加入 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且由于 𝑤(𝑥) >0w(x)>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，加入该元素后权值会增加，说明 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是权值最大的独立集．

### 步骤

贪心算法求解权值最大独立集的步骤如下：

  1. **元素排序** ：将基础集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 按照权值从大到小排序，记为序列 𝑒1,𝑒2,…,𝑒𝑛e1,e2,…,en![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. **初始化** ：设独立集 𝐴 =∅A=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. **构建独立集** ：依次考虑排序后的元素 𝑒𝑖ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果 𝐴 ∪{𝑒𝑖} ∈IA∪{ei}∈I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则更新 𝐴 =𝐴 ∪{𝑒𝑖}A=A∪{ei}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  4. **输出结果** ：最终的集合 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为权值最大的独立集．

**复杂度分析** ：

设 𝑛 =|𝑆|n=|S|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为基础集的大小，𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示判断一个集合是否为独立集的复杂度．贪心算法的时间复杂度为：

𝑂(𝑛log⁡𝑛+𝑛𝑓(𝑛))O(nlog⁡n+nf(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是排序的复杂度，𝑂(𝑛𝑓(𝑛))O(nf(n))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是逐一判断独立性的复杂度．

备注

  * 在图拟阵中，可以使用 [并查集](../../ds/dsu/) 来高效检测是否形成环，从而使 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 接近常数时间．
  * 在线性拟阵中，独立性检测通常涉及矩阵运算，其复杂度依赖于具体实现方式．

**正确性证明** ：

设 𝑀 =(𝑆,I)M=(S,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个拟阵，𝐴 ∈IA∈I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个独立集，且 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是某个权值最大独立集 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集．定义集合 𝑃 ={𝑥 ∈𝑆 ∖𝐴 ∣𝐴 ∪{𝑥} ∈I}P={x∈S∖A∣A∪{x}∈I}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即所有加入 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，仍然使 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 保持独立性的元素所构成的集合．

设 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中权值最大的元素，则 𝐴′ =𝐴 ∪{𝑦}A′=A∪{y}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是某个权值最大独立集的子集，证明如下：

假设 𝐴′ =𝐴 ∪{𝑦}A′=A∪{y}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是任何权值最大独立集的子集，则存在一个权值最大的独立集 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 |𝐴′| <|𝑇||A′|<|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于 |𝐴′| <|𝑇||A′|<|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据拟阵的 **扩张性** ，存在 𝑥 ∈𝑇 ∖𝐴′x∈T∖A′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝐴′ ∪{𝑥} ∈IA′∪{x}∈I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

利用 **扩张性** ，不断将 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加入 𝐴′A′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最终构造出一个新的独立集 𝐴″A″![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 |𝐴″| =|𝑇||A″|=|T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

设 𝐾 =𝐴″ ∩𝑇K=A″∩T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时有 𝑥 =𝑇 ∖𝐾x=T∖K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑦 =𝐴″ ∖𝐾y=A″∖K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中权值最大的元素，有 𝑤(𝑥) ≤𝑤(𝑦)w(x)≤w(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此，𝑤(𝐴″) =𝑤(𝐾) +𝑤(𝑦) ≥𝑤(𝐾) +𝑤(𝑥) =𝑤(𝑇)w(A″)=w(K)+w(y)≥w(K)+w(x)=w(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时：

  * 若 𝑤(𝐴″) >𝑤(𝑇)w(A″)>w(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是权值最大独立集，与假设矛盾．
  * 若 𝑤(𝐴″) =𝑤(𝑇)w(A″)=w(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝐴″A″![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为权值最大独立集，且 𝐴′A′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为其子集，与假设 𝐴′A′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是任何权值最大独立集的子集矛盾．

综上，假设不成立，即 𝐴′ =𝐴 ∪{𝑦}A′=A∪{y}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必须是某个权值最大独立集的子集，因此通过不断使用贪心策略，最终可以找到权值最大的独立集．

### 示例

**最小生成树** ：

给定一个连通无向图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每条边 𝑒 ∈𝐸e∈E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都具有权值 𝑤(𝑒)w(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．目标为找到一棵生成树，使其包含所有顶点且总权值最小．

**拟阵的构建** ：

为了将最小生成树问题形式化为拟阵问题，可以构建图拟阵 𝑀(𝐺)M(G)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

  * **基础集** ：𝑆 =𝐸S=E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即图中的所有边．
  * **独立集族** ：II![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为所有不包含环的边集（即所有森林）．

**贪心算法** ：

在图拟阵的框架下，[Kruskal 算法](../../graph/mst/#kruskal-算法) 是一个典型的基于拟阵理论的贪心算法，可以用于构建最小生成树．虽然 [Prim 算法](../../graph/mst/#prim-算法) 也是一种有效的贪心算法，同样能够找到最小生成树，但它并不严格依赖于拟阵的贪心．因此，在拟阵理论的讨论中，Kruskal 算法是主要的贪心算法实例．

  * **Kruskal 算法** ：

    1. **边排序** ：将所有边按权值从小到大排序．
    2. **逐步选择** ：依次选择权值最小的边，若加入后不形成环，则将其加入生成树．
    3. **终止条件** ：重复上述过程，直到生成树包含 |𝑉| −1|V|−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边．
  * **Prim 算法** ：

    * **原理** ：Prim 算法通过从一个起始顶点开始，逐步扩展生成树，每次选择连接树内与树外的最小权值边．
    * 虽然 Prim 算法也是贪心的，但其选择策略不同于其他基于拟阵扩张性质的贪心算法．因此，在拟阵理论的严格意义下，Prim 算法不被视为典型的拟阵贪心算法．

## 拟阵交

对于定义在同一基础集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的两个拟阵 𝑀1 =(𝑆,I1)M1=(S,I1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑀2 =(𝑆,I2)M2=(S,I2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 I =I1 ∩I2I=I1∩I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足拟阵独立集族的三条性质，则称 𝑀 =(𝑆,I)M=(S,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑀1M1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑀2M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **交** ．

**注意** ：并非任意两个拟阵的交都是一个拟阵，只有当其独立集族的交集满足拟阵独立集族定义中的三条性质时，其交才构成一个拟阵．

### 问题描述

  1. **最大独立集** ：在 I1 ∩I2I1∩I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中找到最大的独立集（即具有最大基数的独立集）．
  2. **加权最大独立集** ：给定权值函数 𝑤 :𝑆 →ℝw:S→R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在 I1 ∩I2I1∩I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中找到权值和最大的独立集．

### 算法

**无权版本** ：

  1. **初始化** ：选择一个初始独立集 𝐼 ∈I1 ∩I2I∈I1∩I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，通常设定 𝐼 =∅I=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. **迭代** ：
     * **构建交换图** ：根据当前独立集 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构建交换图 𝐷𝑀1,𝑀2(𝐼)DM1,M2(I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
     * **路径选择** ：在交换图中，寻找从源点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到汇点 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的增广路径 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
     * **增广** ：沿路径 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历每一个节点：
       * 如果节点属于左部顶点（即 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素），则将该元素从 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中移除．
       * 如果节点属于右部顶点（即 𝑆 ∖𝐼S∖I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素），则将该元素加入 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．
     * **重复** ：更新独立集 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，重复上述步骤，直到无法找到新的增广路径为止．
  3. **结果** ：最终得到的独立集 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为拟阵交 𝑀 =𝑀1 ∩𝑀2M=M1∩M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的一个最大独立集．

**加权版本** ：

为了找到权值和最大的独立集，算法需要在增广路径的选择上进行优化．

  1. **权值设置** ：对于每个元素 𝑒 ∈𝑆e∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义其在交换图中的权值 𝑤′(𝑒)w′(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：
     * **左部顶点** （𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素）：𝑤′(𝑒) = −𝑤(𝑒)w′(e)=−w(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
     * **右部顶点** （𝑆 ∖𝐼S∖I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素）：𝑤′(𝑒) =𝑤(𝑒)w′(e)=w(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. **路径选择** ：在交换图 𝐷𝑀1,𝑀2(𝐼)DM1,M2(I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，寻找一条从源点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到汇点 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **增广路径** 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得沿路径进行增广操作后，独立集 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的总权值增加最大．
     * **增广条件** ：路径 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上加入的元素的权值总和大于移除的元素的权值总和，即 ∑𝑦∈加入的元素𝑤(𝑦) >∑𝑥∈移除的元素𝑤(𝑥)∑y∈加入的元素w(y)>∑x∈移除的元素w(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. **增广操作** ：沿路径 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历每一个节点：
     * 如果节点属于左部顶点（即 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素），则将该元素从 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中移除．
     * 如果节点属于右部顶点（即 𝑆 ∖𝐼S∖I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素），则将该元素加入 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．
  4. **迭代** ：重复步骤 1 至 3，不断构建交换图并寻找增广路径，逐步优化独立集 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的总权值．
  5. **终止条件** ：当无法在交换图中找到满足增广条件的路径时，算法终止．
  6. **结果** ：最终得到的独立集 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为拟阵交 𝑀 =𝑀1 ∩𝑀2M=M1∩M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的一个 **权值最大独立集** ．

**复杂度** ：

  * **增广次数** ：设两个拟阵的最大秩分别为 𝑟1r1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟2r2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则最大增广次数为 min(𝑟1,𝑟2)min(r1,r2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * **每次增广的复杂度** ：

    * 构建交换图的复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑛 =|𝑆|n=|S|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
    * 寻找增广路径的复杂度取决于路径搜索策略，通常为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，例如使用广度优先搜索．
  * **总时间复杂度** ：总体的时间复杂度为 𝑂(𝑟 ⋅𝑛2)O(r⋅n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑟 =min(𝑟1,𝑟2)r=min(r1,r2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 例题

**最小生成树** ：

给定一个无向图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每条边 𝑒 ∈𝐸e∈E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有一个权值 𝑤(𝑒)w(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．寻找一棵生成树，使其包含所有顶点且总权值最小．

  * 详细介绍：[最小生成树](../../graph/mst/)．
  * 题目模板：[洛谷 P3366【模板】最小生成树](https://www.luogu.com.cn/problem/P3366)．

解题思路

使用 Kruskal 算法，将所有边按权值从小到大排序，然后逐步选择边，若加入后不形成环，则将其加入生成树，最终得到的生成树即为最小生成树．

**Colorful Graph** ：

给定一张带有多种颜色的无向图 𝐺 =(𝑉,𝐸)G=(V,E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每条边有一个颜色属性．寻找一个最大的边集，使得：

  1. 所选边不形成任何环．
  2. 每种颜色的边数不超过 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条（𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为给定的正整数）．

解题思路

  1. **拟阵建模** ：

     * **图拟阵 ( 𝑀1M1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))**：定义为所有不形成环的边集，即独立集族 I1I1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含所有不构成环的边集合．
     * **颜色拟阵 ( 𝑀2M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))**：定义为每种颜色的边数不超过 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边集，即独立集族 I2I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含所有满足每种颜色边数 ≤𝑘≤k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边集合．
  2. **求解拟阵交** ：通过求解 𝑀 =𝑀1 ∩𝑀2M=M1∩M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，找到既不形成环又满足每种颜色边数不超过 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大边集．

**约束的资源分配问题** :

在一个资源分配问题中，有一组资源 𝑅 ={𝑟1,𝑟2,…,𝑟𝑛}R={r1,r2,…,rn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一组项目 𝑃 ={𝑝1,𝑝2,…,𝑝𝑚}P={p1,p2,…,pm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每个项目 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要分配一定数量的资源，且每种资源的总分配量不能超过其供应量．

**目标** ：寻找一个资源分配方案，使其满足所有项目需求且不超过资源供应量．

解题思路

  1. **拟阵建模** ：

     * **需求拟阵 ( 𝑀1M1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))**：定义为满足各项目资源需求的分配方案，即独立集族 I1I1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含所有满足项目需求的资源分配集合．
     * **供应拟阵 ( 𝑀2M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))**：定义为不超过每种资源供应量的分配方案，即独立集族 I2I2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含所有满足资源供应限制的资源分配集合．
  2. **求解拟阵交** ：通过求解 𝑀 =𝑀1 ∩𝑀2M=M1∩M2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，找到既满足所有项目需求又不超过资源供应量的资源分配方案．

## 参考资料与注释

  1. [Wikipedia - Matroid](https://en.wikipedia.org/wiki/Matroid)
  2. [百度百科 - 拟阵](https://baike.baidu.com/item/%E6%8B%9F%E9%98%B5)
  3. [洛谷 - 拟阵与最优化问题](https://www.luogu.com.cn/article/87d02q9f)
  4. [洛谷 - 从拟阵基础到 Shannon 开关游戏](https://www.luogu.com.cn/article/fuj3x886)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/matroid.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/matroid.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest), [Tiphereth-A](https://github.com/Tiphereth-A), [yyyu-star](https://github.com/yyyu-star)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
