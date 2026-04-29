# 基本概念 - OI Wiki

- Source: https://oi-wiki.org/math/algebra/basic/

# 基本概念

本章节将简要介绍抽象代数的相关知识．现阶段算法竞赛的主要内容并不直接考察抽象代数的知识，但是在算法的描述或是问题的题解中常常会牵涉一些抽象函数的基本概念，这使得掌握了基础抽象代数概念的读者能够更快速理解一些算法．因此，这部分内容并不是任何选手的必修知识，而仅供那些感兴趣或者可能从中受益的读者参考使用．同时，本章节将避免过全过深的介绍抽象代数的知识1，而会集中在基础概念以及与 OI 其他部分知识联系最为紧密的部分．想系统学习抽象代数知识的读者，应当参考专业的抽象代数教科书学习．

为了更好帮助读者理解阅读本部分内容可能的收获，列举一些算法竞赛中可能牵涉到抽象代数知识的例子：

  * 数论和多项式的很多定理是抽象代数中结论的特例；
  * 数据结构中，[线段树](../../../ds/seg/) 等结构可以维护幺半群的信息，而很多 DP 问题的递推关系可以抽象成这样的幺半群结构；
  * 组合数学中，[Pólya 计数原理](../../combinatorics/polya/) 的严格表述和证明需要用到群论的相关概念．

基于此，本章节将着重介绍无法跳过的基础知识和与这些应用直接相关的部分．作为开始，本文介绍群、环、域的基本概念．

## 群

群的定义如下．

群

设 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是非空集合，其上有二元运算 ⋅ :𝐺 ×𝐺 →𝐺⋅:G×G→G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果它们满足以下性质，则称 (𝐺, ⋅)(G,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **群** （group）：

  1. 结合律（associative property）：对于所有 𝑎,𝑏,𝑐 ∈𝐺a,b,c∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，成立 𝑎 ⋅(𝑏 ⋅𝑐) =(𝑎 ⋅𝑏) ⋅𝑐a⋅(b⋅c)=(a⋅b)⋅c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 有单位元：存在 𝑒 ∈𝐺e∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得对于任意 𝑎 ∈𝐺a∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都成立 𝑎 ⋅𝑒 =𝑒 ⋅𝑎 =𝑎a⋅e=e⋅a=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这里，𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **单位元** （identity element），也称幺元；
  3. 存在逆元：对于所有 𝑎 ∈𝐺a∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都存在相应的 𝑏 ∈𝐺b∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑎 ⋅𝑏 =𝑏 ⋅𝑎 =𝑒a⋅b=b⋅a=e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这里，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **逆元** （inverse element）．

关于定义中的封闭性条件

这里的二元运算就隐含了所谓的封闭性条件，即对于任何 𝑎,𝑏 ∈𝐺a,b∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑎 ⋅𝑏 ∈𝐺a⋅b∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．有些文章会将其单独列出．

群的基本性质

对于群 (𝐺, ⋅)(G,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以下性质总是成立：

  1. 对于任何有限长的列 {𝑔𝑖}𝑘𝑖=1 ⊆𝐺{gi}i=1k⊆G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，乘积 𝑔1 ⋅𝑔2 ⋅⋯ ⋅𝑔𝑘g1⋅g2⋅⋯⋅gk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的运算结果与加括号的方式无关；
  2. 单位元 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是唯一的；
  3. 对于任何元素 𝑎 ∈𝐺a∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的逆 𝑎−1a−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是唯一的；
  4. 消去律（cancellation law）：对于 𝑎,𝑏,𝑐 ∈𝐺a,b,c∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果 𝑎 ⋅𝑐 =𝑏 ⋅𝑐a⋅c=b⋅c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑐 ⋅𝑎 =𝑐 ⋅𝑏c⋅a=c⋅b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么有 𝑎 =𝑏a=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

群相当常见．通俗地说，所有不损失结构的变换都自动构成群．以常见的几种类型的群为例．

群的例子

  * **对称群** （symmetric group）：集合 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的所有 [置换](../../permutation/)，即自 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 自身的双射，就在映射的复合下构成群 𝑆𝑀SM![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．单位元是恒等变换，逆元是逆映射（双射必然存在逆映射）．如果集合 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有限，大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也常记作 𝑆𝑛Sn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称作 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次对称群．
  * 空间对称群（symmetry group）：对于一个几何图形，能够使其与自身重合的变换全体也在映射的复合下构成群．这描述了该几何图形的空间对称性．具体例子可以参考 [常见空间对称群](../../combinatorics/polya/#常见空间对称群)．
  * 整数的加法群：整数集 𝐙Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在加法 ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 运算下构成群 (𝐙, +)(Z,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．单位元是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，逆元是相反数．
  * 整数模 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘法群（multiplicative group of integers modulo 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）：对于一个模数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所有与 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质的整数对应的 [同余类](../../number-theory/basic/#同余类与剩余系)，在乘法运算下构成群 ((𝐙/𝑛𝐙)×, ×)((Z/nZ)×,×)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．单位元是 ¯11¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，逆元就是模 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [乘法逆元](../../number-theory/inverse/)（对应的同余类），其存在性由 [裴蜀定理](../../number-theory/bezouts/) 保证．具体结构分析参考 [整数模 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘法群](../ring-theory/#应用整数同余类的乘法群)．
  * 一般线性群（general linear group）：数域 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维的全体可逆方阵在乘法运算下构成群 𝐺𝐿𝑛(𝐹)GLn(F)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．单位元是单位矩阵，逆元是逆矩阵．

要更好地理解群的定义，不妨对比着看几个不属于群的例子．

不是群的例子

  * 所有 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到自身的映射（不一定是双射），并不构成群．因为那些不是双射的映射不存在逆元．
  * 整数在乘法下并不构成群，因为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在整数范围内没有乘法逆元．
  * 正整数在加法下也不构成群，因为正整数没有加法单位元．
  * 模 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有非零同余类在乘法意义下往往不构成群．比如说 (𝐙/6𝐙) ∖{――0}(Z/6Z)∖{0―}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，――2 ×――3 =――02―×3―=0―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不属于这个集合，这意味着乘法都不是这个集合上良定义的二元运算（或者说，它不满足封闭性）．

有时，也需要讨论这些更不完善的结构的性质．因此，可以定义如下概念，它们比群更宽泛．

半群

对于非空集合 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和其上的二元运算 ⋅⋅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果该运算满足结合律，则称 (𝐺, ⋅)(G,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **半群** （semigroup）．

幺半群

对于半群 (𝐺, ⋅)(G,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果它还存在单位元，则称 (𝐺, ⋅)(G,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **幺半群** （monoid）．

幺半群和半群的例子

上面的例子中，(𝐍+, +)(N+,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是半群，而 (𝐙, ×)(Z,×)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是幺半群．

最后，很多熟悉的群上的运算除了满足结合律外，还满足交换律．这类群的结构相对简单，它们称作 Abel 群，也称作交换群．

Abel 群

对于群 (𝐺, ⋅)(G,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果运算 ⋅⋅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还满足交换律（commutative property），即对于所有 𝑎,𝑏 ∈𝐺a,b∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都成立 𝑎 ⋅𝑏 =𝑏 ⋅𝑎a⋅b=b⋅a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称 (𝐺, ⋅)(G,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **Abel 群** （Abelian group）或 **交换群** （communicate group）．

Abel 群和非 Abel 群的例子

  * 整数加法群 (𝐙, +)(Z,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是一个 Abel 群．
  * 当 𝑛 ≥3n≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，对称群 𝑆𝑛Sn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并不是 Abel 群．

这些就是群论相关的基本定义．群论的更多内容，可以参考 [群论](../group-theory/) 或相关书籍．

## 环

环的定义如下．

环

对于非空集合 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和其上的两个二元运算 + :𝑅 ×𝑅 →𝑅+:R×R→R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ⋅ :𝑅 ×𝑅 →𝑅⋅:R×R→R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果它们满足以下性质，则称 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **环** （ring）：

  1. (𝑅, +)(R,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成 Abel 群，其单位元记作 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，元素 𝑎 ∈𝑅a∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的逆元记作 −𝑎−a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. (𝑅, ⋅)(R,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成半群，即 ⋅⋅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足结合律．
  3. 分配律（distributive property）：对于所有 𝑎,𝑏,𝑐 ∈𝑅a,b,c∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，成立 𝑎 ⋅(𝑏 +𝑐) =𝑎 ⋅𝑏 +𝑎 ⋅𝑐a⋅(b+c)=a⋅b+a⋅c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑎 +𝑏) ⋅𝑐 =𝑎 ⋅𝑐 +𝑏 ⋅𝑐(a+b)⋅c=a⋅c+b⋅c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

为表述方便，这两个二元运算 ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ⋅⋅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 常称作该环的加法和乘法，相应地，加法单位元称作 **零元** （zero），乘法单位元（如果存在）称作 **幺元** （identity）．应避免和具体的数集中的加法、乘法，以及自然数零和一产生混淆．

关于定义中是否要求乘法单位元

在有的定义中，环必须存在乘法单位元；相对地，不存在乘法单位元的则被称为 **伪环** （rng 或 pseudo-ring）．遇到的时候需根据上下文加以判断．维基百科采用的就是这种定义3．

环的加法结构相当简单，但是乘法结构十分原始．因而如果类比群，在乘法上做更多要求，可以得到如下相关定义．

幺环

对于环 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果它含幺，即存在乘法单位元，记作 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **幺环** （ring with identity）．

除环

对于非零幺环 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果对于所有非 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元素 𝑎 ∈𝑅a∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都存在乘法逆元（记作 𝑎−1a−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），则称 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **除环** （division ring）．

交换环

对于环 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果它的乘法满足交换律，则称 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **交换环** （commutative ring）．

这里除环的定义中有趣的一点是，它将 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 视为乘法结构中的特殊元素．这是因为 0 =0 ⋅𝑎 =𝑎 ⋅00=0⋅a=a⋅0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)2．也就是说，环中加法单位元乘以任何元素都得到其自身．这样，它自然不会存在乘法逆元，除非它本身就是乘法单位元．这样的环只有零环（见下面的例子）．

这里的启示是，理解一般的环的乘法结构时，要去除加法单位元的影响，考察 𝑅 ∖{0}R∖{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．基于这一想法，有如下定义．

零因子

对于环 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果存在 𝑏 ∈𝑅b∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑏 ≠0b≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，成立 𝑎 ⋅𝑏 =0a⋅b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑏 ⋅𝑎 =0b⋅a=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称非零元素 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一个 **零因子** （zero divisor）．

可逆元（单位）

对于环 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果元素 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有乘法逆元，即存在 𝑏 ∈𝑅b∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，成立 𝑎 ⋅𝑏 =𝑏 ⋅𝑎 =1a⋅b=b⋅a=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称元素 𝑎 ∈𝑅a∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **可逆元** ，或称 **单位** （unit）．

「单位」与「单位元」

请不要混淆这两个概念．为避免混淆，抽象代数部分将使用「可逆元」的名称代替「单位」．

零因子不可能是可逆元，可逆元不可能是零因子．但是，一个非零元素可以既不是零因子，也不是可逆元．

如果一个环没有零因子，就说明所有非零元素的集合在乘法运算下封闭，即 (𝑅 ∖{0}, ⋅)(R∖{0},⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成半群．进一步地，如果还要求它成为交换幺半群，就可以得到整环的定义．

整环

对于非零环 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果它是交换环，有乘法单位元，且无零因子，则称它为整环（integral domain）．

虽然整环中的元素不一定存在逆元，但是没有零因子这一特性已经足够在整环上建立消去律．

整环的消去律

设整环 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有元素 𝑎,𝑏,𝑐 ∈𝑅a,b,c∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎 ≠0a≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果 𝑎𝑏 =𝑎𝑐ab=ac![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则必然有 𝑏 =𝑐b=c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于一般的幺环，如果只考虑它的全体可逆元，那么同样可以得到群结构．这称为环的乘法群或是单位群．

乘法群（单位群）

对于幺环 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设 𝑅×R×![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中全体可逆元的集合，则 (𝑅×, ⋅)(R×,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成群，称为幺环 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **乘法群** （multiplicative group），或是 **单位群** （unit group）．

最简单的一些环的例子如下．

环的例子

  * 零环（zero ring）：集合 {0}{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在通常意义的加法 ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和乘法 ××![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下构成环，称为零环．它是唯一的只有一个元素的环，也是唯一的加法单位元和乘法单位元相等的环．
  * 整数环：整数集 𝐙Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和其上通常定义的加法 ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和乘法 ××![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成了环 (𝐙, +, ×)(Z,+,×)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．实际上，这是一个整环，但是它不是除环．
  * 多项式环：对于一个环 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以在上面定义 [多项式环](../ring-theory/#多项式环) 𝑅[𝑥]R[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是整环，则该多项式环必然是整环．
  * 四元数（quaternion）：类比复数，可以考虑集合 𝐇 ={𝑎 +𝑏i +𝑐j +𝑑k :𝑎,𝑏,𝑐,𝑑 ∈𝐑}H={a+bi+cj+dk:a,b,c,d∈R}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且定义其上的加法和乘法，这里，i,j,ki,j,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘法运算满足

i2=j2=k2=−1, ij=−ji=k, jk=−kj=i, ki=−ik=j.i2=j2=k2=−1, ij=−ji=k, jk=−kj=i, ki=−ik=j.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么可以验证，𝐇H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成环，而且，它是一个非交换的除环．

  * 整数集的子集 2𝐙2Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在通常意义的加法和乘法下构成环，它是交换环，没有零因子，但是并不含幺．

  * 整数模 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同余类 𝐙/𝑛𝐙Z/nZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在同余类的加法和乘法运算下构成环，它是交换环，含幺（即 ¯11¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．这样的环含有零因子，当且仅当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是合数．所以，当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数时，环 (𝐙/𝑛𝐙, +, ×)(Z/nZ,+,×)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是整环；而且，此时它也是除环，所以它实际构成为了一个域．它的乘法群 ((𝐙/𝑛𝐙)×, ×)((Z/nZ)×,×)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是整数模 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘法群．
  * 矩阵环：环 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的全体 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维方阵在矩阵的加法和乘法下构成一个环 𝑀𝑛(𝑅)Mn(R)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．一般地，这个环有零因子，且不是交换环．
  * 对于一个集合 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体子集 P(𝐴)P(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果定义集合的对称差 △△![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和交 ∩∩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为其加法和乘法运算，则 (P(𝐴),△, ∩)(P(A),△,∩)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成环．一般地，这个环含幺，有零因子，且是交换环．

当然，对于环的结构的讨论远不止这些，要了解更多内容，可以参考 [环论](../ring-theory/) 或相关书籍．

## 域

域是一个比环性质更强的代数结构．具体地，域是交换除环．当然也可以写出它完整的定义．

域

对于非空集合 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和其上的两个二元运算 + :𝐹 ×𝐹 →𝐹+:F×F→F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ⋅ :𝐹 ×𝐹 →𝐹⋅:F×F→F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果它们满足以下性质，则称 (𝐹, +, ⋅)(F,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 **域** （field）：

  1. (𝐹, +)(F,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成 Abel 群，其单位元记作 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，元素 𝑎 ∈𝐹a∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的逆元记作 −𝑎−a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. (𝐹 ∖{0}, ⋅)(F∖{0},⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成 Abel 群，其单位元记作 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，元素 𝑎 ∈𝐹 ∖{0}a∈F∖{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 ⋅⋅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的逆元记作 𝑎−1a−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

换句话说，域是对加、减、乘、除四则运算都封闭的代数结构．

常见的域的例子如下．

域的例子

  * 数域：有理数集 𝐐Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，实数集 𝐑R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和复数集 𝐂C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在通常意义的加法和乘法下都构成域．
  * 有限域（finite field）：以质数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为模的整数同余类的集合 𝐙/𝑝𝐙Z/pZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在同余类的加法和乘法下构成域．当然，除此之外还有其他的有限域，它们的结构由其大小唯一确定，且大小必然是质数幂的形式．
  * **分式域** （fraction field）：设 (𝑅, +, ⋅)(R,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为整环，可以考虑形如 𝑎𝑏−1ab−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素构成的集合 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．严格地说，在集合 𝑅 ×(𝑅 ∖{0})R×(R∖{0})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上定义等价关系：(𝑎1,𝑏1) ∼(𝑎2,𝑏2)(a1,b1)∼(a2,b2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当 𝑎1𝑏2 =𝑎2𝑏1a1b2=a2b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，集合 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是这一关系下的等价类构成的集合 𝑅 ×(𝑅 ∖{0})/ ∼R×(R∖{0})/∼![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，(𝑎,𝑏)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在等价类就记作 𝑎𝑏−1ab−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果定义它上面的运算为

𝑎1𝑏−11+𝑎2𝑏−12=(𝑎1⋅𝑏2+𝑎2⋅𝑏1)(𝑏1⋅𝑏2)−1,(𝑎1𝑏−11)⋅(𝑎2𝑏−12)=(𝑎1⋅𝑎2)(𝑏1⋅𝑏2)−1a1b1−1+a2b2−1=(a1⋅b2+a2⋅b1)(b1⋅b2)−1,(a1b1−1)⋅(a2b2−1)=(a1⋅a2)(b1⋅b2)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则 (𝑄, +, ⋅)(Q,+,⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成域，称为 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分式域．例如，有理数域 (𝐐, +, ×)(Q,+,×)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是整数环 (𝐙, +, ×)(Z,+,×)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分式域．

  * 二次域（quadratic field）：它是在有理数域 𝐐Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中添加了 √𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而扩张成的，这里 𝑑 ≠0,1d≠0,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且没有平方因子．相关内容可以参考 [二次域](../../number-theory/quadratic/)．

域相较于环，拥有着非常简单的加法和乘法结构．所以，域本身的结构往往很简单．这使得域的研究和环的研究大不相同，通常会转而研究域的扩张，以及相应的 Galois 理论．在算法竞赛中，有时会需要在有理数域或者有限域的扩域上进行计算．域论的相关内容，可以参考 [域论](../field-theory/) 或相关书籍．

## 应用

最后，以下面的题目为例，说明抽象的代数对象是怎样辅助分析具体的问题的．

[【模板】"动态 DP"& 动态树分治（加强版）](https://www.luogu.com.cn/problem/P4751)

给定大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的带点权的树，进行 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次点权修改．每次修改后要输出树上最大带权独立集的权值之和．问题强制在线．

思路分析

这道题是动态 DP 模板，一种复杂度正确的代码实现需要用到 [全局平衡二叉树](../../../ds/global-bst/)，具体样例代码也在对应页面．这里仅仅结合该题情景，分析建模的过程．

为了突出重点，这里暂不考虑全局平衡二叉树对于树形结构的处理，转而考虑链上的最大带权独立集的 DP 问题．顺次考虑链 [1,𝑛][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的每个点，对于点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以选（11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）或不选（00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．分别设这两种情形下，[1,𝑖][1,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上子问题的最优解为 𝑓𝑖,1fi,1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓𝑖,0fi,0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，可以写出 DP 方程为

𝑓𝑖,1=𝑤𝑖+𝑓𝑖−1,0,𝑓𝑖,0=max{𝑓𝑖−1,1,𝑓𝑖−1,0}.fi,1=wi+fi−1,0,fi,0=max{fi−1,1,fi−1,0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它的初值为 (𝑓0,1,𝑓0,0) =(0,0)(f0,1,f0,0)=(0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而最终答案就是 max{𝑓𝑛,1,𝑓𝑛,0}max{fn,1,fn,0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．要表示点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于最终结果的影响，只需要注意到这一递归关系可以写作

(𝑓𝑖,1,𝑓𝑖,0)=𝑔(𝑓𝑖−1,1,𝑓𝑖−1,0;𝑤𝑖).(fi,1,fi,0)=g(fi−1,1,fi−1,0;wi).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是一连串 𝐑2R2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝐑2R2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的映射，它将 (𝑓𝑖−1,1,𝑓𝑖−1,0)(fi−1,1,fi−1,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 映射到 (𝑓𝑖,1,𝑓𝑖,0)(fi,1,fi,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用群的语言描述，这些变换在映射的复合之下构成幺半群．这正是线段树可以维护的．

但是，这样的含参变换 𝑔( ⋅;𝑤𝑖)g(⋅;wi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 如果没有特殊的结构，一般的 𝐑2R2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝐑2R2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的映射是不可能用有限维的数据描述的．这里就需要另一项观察，即如果在 𝐑 ∪{ −∞}R∪{−∞}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上，定义 maxmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为加法、++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为乘法，那么 𝐑 ∪{ −∞}R∪{−∞}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成一种类似环的结构，这里，−∞−∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是加法单位元，00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是乘法单位元．但是它不是环，因为其中的元素并非都有加法逆元．这样的结构叫做半环4，这里 (𝐑 ∪{ −∞},max, +)(R∪{−∞},max,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 形成的半环叫做 **热带半环** （tropical semiring）．

基于热带半环 (𝑅, ⊕, ⊗)(R,⊕,⊗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以定义它上面的矩阵乘法．即对于 𝑚 ×𝑛m×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维矩阵 𝐴 =(𝑎𝑖𝑗)A=(aij)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛 ×𝑝n×p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维矩阵 𝐵 =(𝑏𝑗𝑘)B=(bjk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以定义其乘积 𝐴𝐵AB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 (𝑐𝑖𝑘)(cik)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的每项元素等于

𝑐𝑖𝑘=𝑛⨁𝑗=1(𝑏𝑖𝑗⊗𝑐𝑗𝑘)=max1≤𝑗≤𝑛(𝑏𝑖𝑗+𝑐𝑗𝑘).cik=⨁j=1n(bij⊗cjk)=max1≤j≤n(bij+cjk).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

有了这些记号，可以将上述递推关系看作是热带半环上的线性变换，并用矩阵语言写作

(𝑓𝑖,1𝑓𝑖,0)=(−∞𝑤𝑖00)(𝑓𝑖−1,1𝑓𝑖−1,0).(fi,1fi,0)=(−∞wi00)(fi−1,1fi−1,0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由此，只要用线段树维护这一热带半环上的矩阵的乘积就可以回答多次修改的链上的动态 DP 问题．

现在回到该问题的树上版本．对于树上的节点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其子节点集合记作 𝑆(𝑖)S(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则该处的 DP 方程为

𝑓𝑖,1=𝑤𝑖+∑𝑗∈𝑆(𝑖)𝑓𝑗,0,𝑓𝑖,0=∑𝑗∈𝑆(𝑖)max{𝑓𝑗,1,𝑓𝑗,0}.fi,1=wi+∑j∈S(i)fj,0,fi,0=∑j∈S(i)max{fj,1,fj,0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

首先，通过树链剖分将问题转化为链上版本．设 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的重子节点，那么上述递推方程可以写作

𝑓𝑖,1=𝑤𝑖+𝑓ℎ,0+𝑔𝑖,1,𝑓𝑖,0=max{𝑓𝑗,0,𝑓𝑗,1}+𝑔𝑖,0,fi,1=wi+fh,0+gi,1,fi,0=max{fj,0,fj,1}+gi,0,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里，

𝑔𝑖,1=∑𝑗∈𝑆(𝑖), 𝑗≠ℎ𝑓𝑗,0,𝑔𝑖,0=∑𝑗∈𝑆(𝑖), 𝑗≠ℎmax{𝑓𝑗,1,𝑓𝑗,0}gi,1=∑j∈S(i), j≠hfj,0,gi,0=∑j∈S(i), j≠hmax{fj,1,fj,0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

总结了轻子节点的贡献．根据上文描述，这些变换都可以写作热带半环上的矩阵形式，所以，整个问题也就可以在树剖后的线段树上维护．但是，直接用树剖加线段树的单次修改是 𝑂(log2⁡𝑛)O(log2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，所以需要用到上文提到的全局平衡二叉树优化到 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当然也可以用 LCT 维护．

这里提到的热带半环以及上面的矩阵运算其实并不罕见．如果将上文中的 maxmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 换作 minmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则相应的热带半环常用于最短路问题中．如果 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维方阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 给出了顶点数目为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的某个图的两点间的（最短）边权，那么，𝐴𝑘Ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的元素就是自点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 经至多 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边到点 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短距离；特别地，𝐴𝑛An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是该图的距离矩阵．当然实际实现的时候并不会真的暴力计算这一矩阵的幂，而是使用复杂度为 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Floyd 算法．

## 参考资料与注释

  * Dummitt, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
  * [Tropical semiring - Wikipedia](https://en.wikipedia.org/wiki/Tropical_semiring)

* * *

  1. 因为 [OI Wiki 不是百科全书](../../../intro/what-oi-wiki-is-not/#oi-wiki-不是百科全书)． ↩

  2. 该式的推导即 0 ⋅𝑎 +0 =0 ⋅𝑎 =(0 +0) ⋅𝑎 =0 ⋅𝑎 +0 ⋅𝑎0⋅a+0=0⋅a=(0+0)⋅a=0⋅a+0⋅a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这里，第一个等号和第二个等号是加法单位元的定义，第三个等号是分配律，最后的蕴涵关系是加法的消去律．另一侧的乘法类似． ↩

  3. [Ring（mathematics）- Wikipedia](https://en.wikipedia.org/wiki/Ring_%28mathematics%29) ↩

  4. 半环（semiring）是在幺环的定义中放松了加法运算一定存在逆元的要求，即加法结构是交换幺半群、乘法结构是幺半群的代数结构．更多信息参见 [Wikipedia](https://en.wikipedia.org/wiki/Semiring)． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/algebra/basic.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/algebra/basic.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest), [Tiphereth-A](https://github.com/Tiphereth-A), [billchenchina](https://github.com/billchenchina), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [ImpleLee](https://github.com/ImpleLee), [isdanni](https://github.com/isdanni), [jifbt](https://github.com/jifbt), [Menci](https://github.com/Menci), [ouuan](https://github.com/ouuan), [warzone-oier](https://github.com/warzone-oier), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
