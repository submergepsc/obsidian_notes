# 线性规划基础 - OI Wiki

- Source: https://oi-wiki.org/math/linear-programming/

# 线性规划基础

## 引入

线性规划（linear programming, LP）是研究线性约束条件下线性目标函数最值问题的方法总称，是运筹学的一个分支，在多方面均有应用．线性规划的某些特殊情况，如网络流、多商品流量等问题都有可能在算法竞赛题目中出现．算法竞赛很少会出现只能用线性规划算法解决的问题，绝大多数这类问题可以通过网络流建模等方法更高效地解决．

### 一个简单的例子

一个问题能够写成线性规划的形式，既要有若干个线性约束条件，又要有线性的目标函数．

考虑下面的例子：

例子

早点师傅每天可以制作一定数量的包子和油条，这两种早餐深受顾客喜爱．为了最大化利润，师傅希望尽可能多地制作早点，但在实际操作中受到食材、时间等多种资源的限制．为此，师傅统计了制作每份早点所需的食材用量、制作时间及其对应的利润，具体如下表所示：

早点| 植物油| 面粉| 时间| 利润  
---|---|---|---|---  
包子| 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
油条| 77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
假设师傅每天最多可以购入 6666![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位的植物油和 6060![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位的面粉，并且最多可以投入 9696![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位的制作时间．那么，师傅应如何合理安排包子和油条的生产数量，才能使每天的利润最大化？

用数学语言描述，可以设 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是师傅制作包子和油条的数量．那么，「总共需要的植物油不超过 6666![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位」就可以表示为

4𝑥1+7𝑥2≤66.4x1+7x2≤66.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

类似地，「总共需要的面粉不超过 6060![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位」和「总共需要的时间不超过 9696![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 单位」可以表示为

7𝑥1+3𝑥2≤60,8𝑥1+6𝑥2≤96.7x1+3x2≤60,8x1+6x2≤96.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

另外，师傅不可能生产出负数单位的早点，所以，还有条件

𝑥1,𝑥2≥0.x1,x2≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

师傅就是要在这些限制下，最大化利润：

𝑧=5𝑥1+6𝑥2.z=5x1+6x2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就是一个典型的线性规划问题．它的目标函数是关于决策变量的线性函数，约束条件则由决策变量构成的线性等式或不等式组成．

### 图解法

对于只有两个决策变量的线性规划问题，可以通过图解法直观地解决问题．

考虑本节的问题

max𝑥1,𝑥2𝑧=5𝑥1+6𝑥2subject to 4𝑥1+7𝑥2≤66,7𝑥1+3𝑥2≤60,8𝑥1+6𝑥2≤96,𝑥1,𝑥2≥0maxx1,x2z=5x1+6x2subject to 4x1+7x2≤66,7x1+3x2≤60,8x1+6x2≤96,x1,x2≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对应的几何图像．最后一行约束表示可选的点 (𝑥1,𝑥2)(x1,x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都出现在第一象限，另外的三个约束则表示可选的点一定在直线 4𝑥1 +7𝑥2 =664x1+7x2=66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、直线 7𝑥1 +3𝑥2 =607x1+3x2=60![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和直线 8𝑥1 +6𝑥2 =968x1+6x2=96![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的下方．这些区域的交集（如下图绿色区域所示）就是所有可供选择的点的集合：

![](./images/linear-programming.svg)

接下来要最大化 𝑧 =5𝑥1 +6𝑥2z=5x1+6x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．如果将该等式视作直线 5𝑥1 +6𝑥2 =𝑧5x1+6x2=z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方程，则随着 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的变化，将得到一族平行直线，且 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 越大，直线就越靠近右上方．因此，只需要不断移动直线直至达到某一临界位置，使得再向右上移动一点点，直线就不再和图中所示区域相交，此时直线对应的 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是所求的最大值．

如图所示，这样的情形发生在红点所示位置．它是直线 4𝑥1 +7𝑥2 =664x1+7x2=66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和直线 7𝑥1 +3𝑥2 =607x1+3x2=60![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的交点．联立两直线方程可知，它的坐标是 (6,6)(6,6)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这是本问题唯一的最优解．早点师傅的最大利润是 𝑧 =66z=66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当问题涉及多于两个决策变量时，图解法不再适用．但是，本节的例子中的一些观察仍然有效．线性规划问题中的每个不等式约束都描述了一个「半平面」，所有可行的解的集合就是这些「半平面」的交集，因此，总是一个「凸多边形」．规划问题的最优解总是可以在该「凸多边形」的某个「顶点」处取得．这些「顶点」的坐标可以通过联立这些「半平面」的「边界」的方程求得．将这些观察拓展到高维空间，就发展出了一个高效的求解线性规划问题的方法——单纯形法．这也是算法竞赛中最常应用的方法．

另外一个值得注意的问题是，原则上，早点师傅制作的包子和油条都不是无限可分的，应当是某个整数．虽然本题求解过程中没有明确地限制这一点，但是由于最终的最优解的确是整数，所以，即使加上整数限制，本题的答案仍然是可行的．但是对于很多规划问题，最优解可能无法取得在整点处，这些问题实际上是一类整数规划问题，而非简单的线性规划问题．本文的结尾简单地讨论了这一类问题．

## 基本概念

本节介绍线性规划问题的基本概念．

### 线性规划问题

一个线性规划问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通常由如下两部分组成：

  * 线性目标函数，即形如

𝑓(𝑥1,𝑥2,⋯,𝑥𝑛)=𝑐1𝑥1+𝑐2𝑥2+⋯+𝑐𝑛𝑥𝑛f(x1,x2,⋯,xn)=c1x1+c2x2+⋯+cnxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的函数，其中，𝑐𝑖 ∈𝐑ci∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是常数；

  * 线性约束，即形如

𝑔𝑗(𝑥1,𝑥2,⋯,𝑥𝑛)=𝑎𝑗1𝑥1+𝑎𝑗2𝑥2+⋯+𝑎𝑗𝑛𝑥𝑛≤(=,≥)𝑏𝑗gj(x1,x2,⋯,xn)=aj1x1+aj2x2+⋯+ajnxn≤(=,≥)bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的不等式或等式约束，其中，𝑎𝑗𝑖,𝑏𝑗 ∈𝐑aji,bj∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是常数．

线性规划问题，就是要在满足所给约束的前提下，最大化或者最小化目标函数．满足所给约束的解 (𝑥1,𝑥2,⋯,𝑥𝑛) ∈𝐑𝑛(x1,x2,⋯,xn)∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 **可行解** （feasible solution）；在所有可行解中，使得目标函数取得最值的解称为 **最优解** （optimal solution）．

### 标准形式

为了方便描述和进一步处理，通常需要指定一个线性规划问题的标准形式．不同文献可能有不同的规定方式，本文规定线性规划的标准形式如下：

min{𝑥𝑖}𝑛∑𝑖=1𝑐𝑖𝑥𝑖subject to 𝑛∑𝑖=1𝑎𝑗𝑖𝑥𝑖=𝑏𝑖≥0, 𝑗=1,⋯,𝑚,𝑥𝑖≥0, 𝑖=1,⋯,𝑛.min{xi}∑i=1ncixisubject to ∑i=1najixi=bi≥0, j=1,⋯,m,xi≥0, i=1,⋯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，线性规划问题是最小化问题，所有决策变量都有非负约束，且除此之外只包含若干右侧常量非负的等式约束．利用 [矩阵](../linear-algebra/matrix/) 可以更为简洁地表达这一问题：

max{𝑐𝑇𝑥:𝐴𝑥=𝑏≥0, 𝑥≥0}.max{cTx:Ax=b≥0, x≥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑥 =(𝑥𝑖) ∈𝐑𝑛x=(xi)∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是决策变量，𝑏 =(𝑏𝑗) ∈𝐑𝑚b=(bj)∈Rm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐴 =(𝑎𝑗𝑖) ∈𝐑𝑚×𝑛A=(aji)∈Rm×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是约束中涉及的常量．线性规划问题的规模就是指它的决策变量的数目和它的约束的个数．

向量不等式

本文中会多次出现像 𝑏 ≥0b≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这样的向量不等式．一般地，对于向量 𝑥,𝑦 ∈𝐑𝑛x,y∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不等式 𝑥 ≤𝑦x≤y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 ∀𝑖(𝑥𝑖 ≤𝑦𝑖)∀i(xi≤yi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即逐维地进行实数意义上的比较．这一关系是向量空间上的 [偏序关系](../order-theory/#二元关系)，也就是说，存在两个向量无法比较的情形．

标准形式的选取只是为了行文方便，而并没有任何特别之处，因为任何线性规划问题都可以等价地写成下面的六种形式：

min{𝑐𝑇𝑥:𝐴𝑥=𝑏, 𝑥≥0},min{𝑐𝑇𝑥:𝐴𝑥≥𝑏},min{𝑐𝑇𝑥:𝐴𝑥≥𝑏, 𝑥≥0},max{𝑐𝑇𝑥:𝐴𝑥=𝑏, 𝑥≥0},max{𝑐𝑇𝑥:𝐴𝑥≤𝑏},max{𝑐𝑇𝑥:𝐴𝑥≤𝑏, 𝑥≥0}.min{cTx:Ax=b, x≥0},min{cTx:Ax≥b},min{cTx:Ax≥b, x≥0},max{cTx:Ax=b, x≥0},max{cTx:Ax≤b},max{cTx:Ax≤b, x≥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

下列操作可以将所有线性规划问题都等价地转化为这六种形式之一：

  1. 通过添加负号，即将 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为 −𝑐−c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以完成最大化问题和最小化问题的相互转化．
  2. 通过添加负号，即将 𝑎𝑇𝑗𝑥 ⪋𝑏𝑗ajTx⪋bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替换成 −𝑎𝑇𝑗𝑥 ⪌ −𝑏𝑗−ajTx⪌−bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以完成不等式约束的两种方向的相互转化，或将等式约束的右侧常量变为非负数．
  3. 所有的等式约束 𝑎𝑇𝑗𝑥 =𝑏𝑗ajTx=bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以替换成两个相反方向的不等式约束 𝑎𝑇𝑗𝑥 ≥𝑏𝑗ajTx≥bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑎𝑇𝑗𝑥 ≤𝑏𝑗ajTx≤bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  4. 所有的不等式约束 𝑎𝑇𝑗𝑥 ≤( ≥)𝑏𝑗ajTx≤(≥)bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以通过添加非负松弛变量 𝑠𝑗sj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方式，转化为等式约束 𝑎𝑇𝑗𝑥 +( −)𝑠𝑗 =𝑏𝑗ajTx+(−)sj=bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以及相应的非负约束 𝑠𝑗 ≥0sj≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  5. 如果某个决策变量 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有非负约束，那么，可以将它替换成两个非负变量的差值，即 𝑥𝑗 =𝑥+𝑗 −𝑥−𝑗xj=xj+−xj−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑥+𝑗,𝑥−𝑗 ≥0xj+,xj−≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

通过这些操作转化得到的线性规划问题的规模不超过原问题的规模的二倍，而且这些问题的可行解和最优解都很容易相互转化．因此，对于一般形式的线性规划问题，总是可以首先将它转化为标准形式（或上述六种形式之一）再进行求解．

例子

考虑线性规划问题

max3𝑥1−2𝑥2+𝑥3subject to 2𝑥1+3𝑥2+4𝑥3≥1,3𝑥1+4𝑥2≤5,5𝑥2−𝑥3=−1,𝑥1,𝑥2≥0.max3x1−2x2+x3subject to 2x1+3x2+4x3≥1,3x1+4x2≤5,5x2−x3=−1,x1,x2≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

通过操作 1、2 和 3 可以将它转化为形式 min{𝑐𝑇𝑥 :𝐴𝑥 ≥𝑏}min{cTx:Ax≥b}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即

min−3𝑥1+2𝑥2−𝑥3subject to 2𝑥1+3𝑥2+4𝑥3≥1,−3𝑥1−4𝑥2≥−5,5𝑥2−𝑥3≥−1,−5𝑥2+𝑥3≥1,𝑥1≥0,𝑥2≥0.min−3x1+2x2−x3subject to 2x1+3x2+4x3≥1,−3x1−4x2≥−5,5x2−x3≥−1,−5x2+x3≥1,x1≥0,x2≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

通过操作 4 和 5 可以将它转化为形式 max{𝑐𝑇𝑥 :𝐴𝑥 =𝑏, 𝑥 ≥0}max{cTx:Ax=b, x≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即

max3𝑥1−2𝑥2+𝑥+3−𝑥−3subject to 2𝑥1+3𝑥2+4𝑥+3−4𝑥−3−𝑥4=1,3𝑥1+4𝑥2+𝑥5=5,5𝑥2−𝑥+3+𝑥−3=−1,𝑥1,𝑥2,𝑥+3,𝑥−3,𝑥4,𝑥5≥0.max3x1−2x2+x3+−x3−subject to 2x1+3x2+4x3+−4x3−−x4=1,3x1+4x2+x5=5,5x2−x3++x3−=−1,x1,x2,x3+,x3−,x4,x5≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 可行域与问题的解

所有可行解的集合 D ⊆𝐑𝑛D⊆Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为线性规划问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **可行域** （feasible region）．从几何角度看，每个不等式约束 𝑎𝑇𝑗𝑥 ≤𝑏𝑗ajTx≤bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都描述了一个半空间 {𝑥 ∈𝐑𝑛 :𝑎𝑇𝑗𝑥 ≤𝑏𝑗}{x∈Rn:ajTx≤bj}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每个等式约束 𝑎𝑇𝑗𝑥 =𝑏𝑗ajTx=bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都描述了一个超平面 {𝑥 ∈𝐑𝑛 :𝑎𝑇𝑗𝑥 =𝑏𝑗}{x∈Rn:ajTx=bj}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，可行域一定是有限多个半空间和超平面的交集．在优化领域1，这样的几何体通常称为 𝐑𝑛Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 **多面体** （polyhedron）．多面体一定是闭凸集，但未必是有界的．有界的多面体也称为 **多胞形** （polytope）．多胞形可以看作是平面上的多边形在高维空间的推广，而多面体将它进一步推广到可能无界的情形．

多面体的例子

此处列举了一些常见的多面体：

  1. 空集 ∅∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又称为 **零胞形** （nullitope），维度规定为 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. **仿射子空间** （affine subspace），即若干超平面的交集 {𝑥 ∈𝐑𝑛 :𝐴𝑥 =𝑏}{x∈Rn:Ax=b}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．它相当于线性方程组 𝐴𝑥 =𝑏Ax=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解集：当方程组无解时，它就是空集；否则，它总是可以写成 𝑥0 +𝑉x0+V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，其中，𝑥0 ∈𝐑𝑛x0∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑉 ⊆𝐑𝑛V⊆Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑛 −rank⁡(𝐴)n−rank⁡(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维线性子空间．特别地，超平面也是仿射子空间．
  3. **多面体锥** （polyhedral cone），即空间中有限多个点 {𝑥𝑖}{xi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体非负线性组合 {∑𝑖𝛼𝑖𝑥𝑖 :𝛼𝑖 ≥0}{∑iαixi:αi≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．它是顶点位于原点的凸锥体．等价地，它可以看作是由若干个经过原点的超平面围成的多面体，即 {𝑥 ∈𝐑𝑛 :𝐴𝑥 ≤0}{x∈Rn:Ax≤0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．特别地，半空间也是多面体锥．
  4. 多胞形，即有界的多面体．特别地，−1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维的多胞形就是常见的空集、点、线段、多边形和（通常意义下的）多面体．一个集合是多胞形，当且仅当它是有限多个点 {𝑥𝑖}{xi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的凸包 {∑𝑖𝛼𝑖𝑥𝑖 :𝛼𝑖 ≥0, ∑𝑖𝛼𝑖 =1}{∑iαixi:αi≥0, ∑iαi=1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．一个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维的多胞形至少是由 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点生成的凸包．
  5. **单纯形** （simplex），即恰由 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点生成的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维多胞形．它是最简单的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维多胞形．特别地，−1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维的多胞形分别是空集、点、线段、三角形和四面体．最简单的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维单纯形的例子，就是 {𝑥 ∈𝐑𝑘 :𝑥𝑖 ≥0, ∑𝑖𝑥𝑖 =1}{x∈Rk:xi≥0, ∑ixi=1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．实际上，任何 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维单纯形都可以通过仿射变换（即平移和伸缩）变为这样一种特殊情形．值得注意的是，单纯形法并不是真的在单纯形上进行的．

任何多面体，都可以看作是一个多面体锥和一个多胞形的 [Minkowski 和](../../geometry/convex-hull/#闵可夫斯基和)：前者描述了多面体无界的部分，后者描述了多面体有界部分的形状．这个多面体锥是唯一的：多面体 {𝑥 ∈𝐑𝑛 :𝐴𝑥 ≤𝑏}{x∈Rn:Ax≤b}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解得到的多面体锥一定是 {𝑥 ∈R𝑛 :𝐴𝑥 ≤0}{x∈Rn:Ax≤0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

线性规划的解与多面体的结构紧密相关．对于多面体 D ∈𝐑𝑛D∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和向量 𝑐 ∈𝐑𝑛 ∖{0}c∈Rn∖{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考虑如下的线性规划问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：（对最小化的情形也可以类似地讨论）

max{𝑐𝑇𝑥:𝑥∈D}.max{cTx:x∈D}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从几何角度看，这相当于在超平面 𝐻 :𝑐𝑇𝑥 =𝑧H:cTx=z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与可行域 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至少有一个交点的前提下，沿着向量 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方向移动超平面 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 尽可能大．这就存在三种可能性：

  * 可行域 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是空集．这说明问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有可行解，它的某些约束是相互矛盾的．此时，称问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 **不可行的** （infeasible），它的最优价值规定为 −∞−∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 可行域 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非空，但是它包含一条方向向量为 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的射线，即存在 𝑥0 ∈𝐑𝑛x0∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑥0 +𝑡𝑐 ∈Dx0+tc∈D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑡 ≥0t≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．因为沿着向量 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方向可以不断地移动超平面 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而且移动过程中，集合 𝐻 ∩DH∩D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至少含有这条射线中的某个点，一定是非空的，所以，目标函数 𝑐𝑇𝑥 =𝑐𝑇𝑥0 +𝑡𝑐𝑇𝑐cTx=cTx0+tcTc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以取得任意大的值．此时，称问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 **无界的** （unbounded），它的最优价值规定为 +∞+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 可行域 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非空，且不含有任何方向向量为 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的射线．此时，问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 **有界的** （bounded）．记 𝑧∗ ∈𝐑z∗∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优价值．超平面 𝐻∗ :𝑐𝑇𝑥 =𝑧∗H∗:cTx=z∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处于一种临界位置：它与多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相交，且 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含于半空间 {𝑥 :𝑐𝑇𝑥 ≤𝑧∗}{x:cTx≤z∗}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．这样的超平面称为多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个 **支撑超平面** （supporting hyperlane）．问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优解集就是 𝐻∗ ∩DH∗∩D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．作为支撑超平面和多面体的交集，集合 𝐻∗ ∩DH∗∩D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定是多面体，且包含在 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边界中．它称为多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个 **面** （face）．形象地说，多面体就是由这些面围成的．除了这些由支撑超平面和多面体相交形成的面之外，一般来说，多面体还有两个面：空集和多面体本身．多面体的所有面在集合的包含关系下，形成了 [格](../order-theory/#有向集与格) 的结构．

一个 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维的多面体的面的维度一定是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的整数．维度为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的面（即一个点）称为多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **顶点** （vertex）或 **角点** （corner point），维度为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的面称为多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **边** （edge），维度为 𝑑 −1d−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的面则称为多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **维面** （facet）．但是，并非所有多面体都有顶点．因为多面体的面的面仍然是多面体的面，而只有仿射子空间才没有严格更小的非空面，所以，多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有极小面都是仿射子空间．而且，同一个多面体的极小面的维度是相同的；特别地，多面体 D ={𝑥 ∈𝐑𝑛 :𝐴𝑥 ≤𝑏}D={x∈Rn:Ax≤b}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极小面的维度是 𝑛 −rank⁡𝐴n−rank⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因为多面体的面就是有界线性规划问题的解集，所以，需要搞清楚如何确定多面体的面的方程．设多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 由若干个约束 𝑎𝑇𝑗𝑥 ⪋𝑏𝑗ajTx⪋bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 描述，且 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个面．如果某个约束在所有 𝑥 ∈𝐹x∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处都取得等号，就称该约束在面 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上是 **紧的** （tight）．面 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的点显然满足这些紧约束取等号得到的方程组，而这个方程组确定的仿射子空间和多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的交集，就是面 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．反过来，任意选取多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约束的一个子集，将这些约束取等、联立、求解得到的仿射子空间和多面体的交集，就是 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个面．而且，选取的紧约束越多，得到的面（在包含意义下）就越小．

特别地，标准形式的线性规划的可行域 D ={𝑥 ∈𝐑𝑛 :𝐴𝑥 =𝑏, 𝑥 ≥0}D={x∈Rn:Ax=b, x≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数矩阵 (𝐴𝐼)(AI)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的秩是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此，它的极小面就是它的顶点．也就是说，如果问题有界，那么它的最优解一定可以选取为某个顶点．而且，这个顶点可以通过选取 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个线性独立的紧约束联立得到．这正是线性规划的标准形式的方便之处．

例子

下图中，DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为可行域．目标函数中的系数是 𝑐1,𝑐2,𝑐3c1,c2,c3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，分别对应着唯一最优解、多组最优解和无界三种情形．对于前两种情形，相应的红色粗实线就是解集对应的支撑超平面（之一），最优解集分别是多面体 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的顶点 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和边 ―――𝐶𝐷CD―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于第三种情形，因为可行域 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中包含方向为 𝑐3c3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的射线，所以，以 𝑐3c3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为法向量的超平面可以不断沿着 𝑐3c3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 方向移动，进而问题是无界的．

![](./images/lp-feasible.svg)

这些讨论忽略了 𝑐 =0c=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．此时，线性规划问题显然不能是无界的，所以要么问题本身是不可行的，要么最优价值等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且最优解集就是 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 本身．这类特殊的线性规划也称为 **可行性线性规划** （feasibility linear programming）．

值得指出的是，判定线性规划问题是否可行、是否有界，以及求出不等式组的可行解等问题，都和解线性规划问题本身同样困难2．比如说，下文中强对偶定理的证明就说明，解一个有界的线性规划问题，就相当于寻找一组不等式的可行解．因此，对于判断不等式组是否有解和判断方程组是否有非负解等任务，最有效的方式就是求解相应的可行性线性规划3．

另外，如果线性规划问题的一个约束，在可行域的所有面上都不是紧的，那么这个约束就是 **冗余的** （redundant）．本文开头早点师傅的例子中，工作时间的约束就是一个冗余约束．在给定的不等式组中判定某个不等式 𝑎𝑇𝑗𝑥 ≤𝑏𝑗ajTx≤bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否冗余这一问题，可以通过求解线性规划问题 max{𝑎𝑇𝑗𝑥 :𝑥 ∈D}max{ajTx:x∈D}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将它与 𝑏𝑗bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相比较来解决．

## 常见算法

算法竞赛中，很少有问题只能通过线性规划的算法解决．大多数可以用线性规划方法求解的题目，通常也可以通过网络流等更为专门也更为高效的算法来解决．

解决线性规划问题的常见算法如下：

  * [单纯形法](../simplex/)
  * 椭球法
  * 内点法

尽管单纯形法的最差情形复杂度是指数级的，而内点法的复杂度是多项式的，但这两类算法在大多数实际问题中的表现都非常出色．相比之下，虽然椭球法的理论复杂度是多项式级别的，但是通常运行缓慢，并不实用．

目前尚不清楚线性规划问题是否存在强多项式复杂度的算法．

## 对偶问题

每个线性规划问题都对应着一个对偶问题．原问题和对偶问题的解有着紧密的联系．通过对偶问题，不仅有助于更深入地理解问题的结构，还常常可以提升原问题的求解效率．

对于线性规划问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（所涉小写字母变量均为向量）

min𝑥1,𝑥2,𝑥3𝑐𝑇1𝑥1+𝑐𝑇2𝑥2+𝑐𝑇3𝑥3subject to 𝐴11𝑥1+𝐴12𝑥2+𝐴13𝑥3≥𝑏1,𝐴21𝑥1+𝐴22𝑥2+𝐴23𝑥3=𝑏2,𝐴31𝑥1+𝐴32𝑥2+𝐴33𝑥3≤𝑏3,𝑥1≥0, 𝑥3≤0,minx1,x2,x3c1Tx1+c2Tx2+c3Tx3subject to A11x1+A12x2+A13x3≥b1,A21x1+A22x2+A23x3=b2,A31x1+A32x2+A33x3≤b3,x1≥0, x3≤0,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它的对偶问题 𝐷D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是指线性规划问题

max𝑦1,𝑦2,𝑦3𝑏𝑇1𝑦1+𝑏𝑇2𝑦2+𝑏𝑇3𝑦3subject to 𝐴𝑇11𝑦1+𝐴𝑇21𝑦2+𝐴𝑇31𝑦3≤𝑐1,𝐴𝑇12𝑦1+𝐴𝑇22𝑦2+𝐴𝑇32𝑦3=𝑐2,𝐴𝑇13𝑦1+𝐴𝑇23𝑦2+𝐴𝑇33𝑦3≥𝑐3,𝑦1≥0, 𝑦3≤0.maxy1,y2,y3b1Ty1+b2Ty2+b3Ty3subject to A11Ty1+A21Ty2+A31Ty3≤c1,A12Ty1+A22Ty2+A32Ty3=c2,A13Ty1+A23Ty2+A33Ty3≥c3,y1≥0, y3≤0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，对偶问题的决策变量 𝑦1,𝑦2,𝑦3y1,y2,y3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是原问题的三类约束的 Lagrange 乘子；反过来，原问题的决策变量 𝑥1,𝑥2,𝑥3x1,x2,x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也分别是对偶问题的三类约束的 Lagrange 乘子．容易验证，对偶问题的对偶问题就是原问题．

原问题 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和对偶问题 𝐷D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对应关系如下：

最小化问题| 最大化问题  
---|---  
大于等于约束| 非负变量  
小于等于约束| 非正变量  
等式约束| 无约束变量  
非负变量| 小于等于约束  
非正变量| 大于等于约束  
无约束变量| 等式约束  
目标函数系数| 约束右侧常量  
约束右侧常量| 目标函数系数  
  
特别地，标准形式的线性规划问题

min{𝑐𝑇𝑥:𝐴𝑥=𝑏, 𝑥≥0}min{cTx:Ax=b, x≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的对偶问题是

max{𝑏𝑇𝑦:𝐴𝑇𝑦≤𝑐}.max{bTy:ATy≤c}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 对偶原理

原问题和对偶问题不仅在形式上互为镜像，而且两者的解也紧密相关．这称为 **对偶原理** （duality principal）．为表述方便，本节在叙述和证明定理时，将采用标准形式的原问题．

首先，**弱对偶定理** （weak duality theorem）说明，对偶问题的最大值不超过原问题的最小值．

弱对偶定理

对于所有 𝐴 ∈𝐑𝑚×𝑛A∈Rm×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏 ∈𝐑𝑚b∈Rm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐 ∈𝐑𝑛c∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，总有

max{𝑏𝑇𝑦:𝐴𝑇𝑦≤𝑐}≤min{𝑐𝑇𝑥:𝐴𝑥=𝑏, 𝑥≥0}.max{bTy:ATy≤c}≤min{cTx:Ax=b, x≥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

如果原问题和对偶问题中的任何一个不可行，那么该不等式就是平凡的．假设两个问题都是可行的．那么，对于所有可行的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

𝑏𝑇𝑦=𝑥𝑇𝐴𝑇𝑦≤𝑥𝑇𝑐.bTy=xTATy≤xTc.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，将两侧取最值，就得到弱对偶定理成立．

基于弱对偶定理，原问题和对偶问题的解的情况只能有下面四种情形：

  1. 原问题和对偶问题均不可行，即 −∞ ≤ +∞−∞≤+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 原问题不可行，对偶问题无界，即 +∞ ≤ +∞+∞≤+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  3. 原问题无界，对偶问题不可行，即 −∞ ≤ −∞−∞≤−∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  4. 原问题和对偶问题均有界．

弱对偶定理有很多推论．例如，它实际上给出了利用原问题和对偶问题的可行性判定原问题无界的方法．

推论

线性规划问题无界，当且仅当它可行，且它的对偶问题不可行．

将弱对偶定理应用于可行性线性规划问题，就得到 Farkas 引理（和它的各种变体）．

Farkas 引理

对于 𝐴 ∈𝐑𝑚×𝑛A∈Rm×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏 ∈𝐑𝑛b∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，下列情形中恰有一种成立：

  1. 存在 𝑥 ∈𝐑𝑛x∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝐴𝑥 =𝑏Ax=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑥 ≥0x≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 存在 𝑦 ∈𝐑𝑚y∈Rm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝐴𝑇𝑦 ≥0ATy≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑏𝑇𝑦 <0bTy<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

考虑线性规划问题 max{0 :𝐴𝑥 =𝑏, 𝑥 ≥0}max{0:Ax=b, x≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的对偶问题是 min{𝑏𝑇𝑦 :𝐴𝑇𝑦 ≥0}min{bTy:ATy≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对偶问题显然是可行的，因为至少 0 ∈𝐑𝑚0∈Rm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一组可行解．因此，根据弱对偶定理，要么原问题可行，要么对偶问题无界，二者必择其一．原问题可行就是 Farkas 引理中的情形 1，而对偶问题无界就等价于 Farkas 引理中的情形 2．这就证明了 Farkas 引理．

Farkas 实际上是一种 [超平面分离定理](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem)．情形 1 是在说，点 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位于 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的列向量生成的多面体锥 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 里；因此，Farkas 引理说明，当且仅当点 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不在这一凸锥 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中时，存在经过原点且法向量为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的超平面 𝐻 :𝑦𝑇𝑥 =0H:yTx=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 强分离了点 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和多面体锥 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

事实上，对于弱对偶定理允许的第四种情形，有更强的结论成立：原问题和对偶问题的最优值是相等的．将后三种情形合在一起，就得到 **强对偶定理** （strong duality theorem）：只要原问题或对偶问题之一是可行的，它们的最优值就必然相等．

强对偶定理

对于所有 𝐴 ∈𝐑𝑚×𝑛A∈Rm×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏 ∈𝐑𝑚b∈Rm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐 ∈𝐑𝑛c∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

max{𝑏𝑇𝑦:𝐴𝑇𝑦≤𝑐}=min{𝑐𝑇𝑥:𝐴𝑥=𝑏, 𝑥≥0}.max{bTy:ATy≤c}=min{cTx:Ax=b, x≥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

只要两个集合之一非空．

证明

弱对偶定理唯一没有包含的情形，就是原问题和对偶问题都可行的情形．此时，考虑如下可行性线性规划问题 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

max{0:𝑐𝑇𝑥≤𝑏𝑇𝑦, 𝐴𝑥=𝑏, 𝑥≥0, 𝐴𝑇𝑦≤𝑐}.max{0:cTx≤bTy, Ax=b, x≥0, ATy≤c}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果问题 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有可行解 (𝑥∗,𝑦∗) ∈𝐑𝑛 ×𝐑𝑚(x∗,y∗)∈Rn×Rm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，由弱对偶定理和最优性可知

𝑏𝑇𝑦∗≤max{𝑏𝑇𝑦:𝐴𝑇𝑦≤𝑐}≤min{𝑐𝑇𝑥:𝐴𝑥=𝑏, 𝑥≥0}≤𝑐𝑇𝑥∗,bTy∗≤max{bTy:ATy≤c}≤min{cTx:Ax=b, x≥0}≤cTx∗,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但是 𝑐𝑇𝑥∗ ≤𝑏𝑇𝑦∗cTx∗≤bTy∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而所有这些不等式都可以取得等号，也就是说，不仅强对偶成立，而且 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦∗y∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是原问题和对偶问题的最优解．

因此，只需要证明问题 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是可行的．假设不然．仿照 Farkas 引理的证明，可以考虑问题 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对偶问题 𝐷𝑄DQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

min{𝑐𝑇𝜇−𝑏𝑇𝜆:𝑐𝑡−𝐴𝑇𝜆≥0, −𝑏𝑡+𝐴𝜇=0, 𝑡≥0, 𝜇≥0}.min{cTμ−bTλ:ct−ATλ≥0, −bt+Aμ=0, t≥0, μ≥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 (𝑡,𝜆,𝜇) =(0,0,0)(t,λ,μ)=(0,0,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是对偶问题 𝐷𝑄DQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组可行解，所以由弱对偶定理可知，问题 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不可行，就意味着对偶问题 𝐷𝑄DQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无界，即存在一组 (𝑡∗,𝜆∗,𝜇∗)(t∗,λ∗,μ∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝑐𝑇𝜇∗−𝑏𝑇𝜆∗<0, 𝑐𝑡∗−𝐴𝑇𝜆∗≥0, −𝑏𝑡∗+𝐴𝜇∗=0, 𝑡∗≥0, 𝜇∗≥0.cTμ∗−bTλ∗<0, ct∗−ATλ∗≥0, −bt∗+Aμ∗=0, t∗≥0, μ∗≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此时，如果 𝑡∗ >0t∗>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么这些不等式实际说明 (𝑥,𝑦) =(𝜇∗/𝑡∗,𝜆∗/𝑡∗)(x,y)=(μ∗/t∗,λ∗/t∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是前述问题的一组可行解，与假设矛盾．所以，只能有 𝑡∗ =0t∗=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这说明

𝑐𝑇𝜇∗<𝑏𝑇𝜆∗, 𝐴𝑇𝜆∗≤0, 𝐴𝜇∗=0, 𝜇∗≥0.cTμ∗<bTλ∗, ATλ∗≤0, Aμ∗=0, μ∗≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但是，因为已经假设定理中的原问题和对偶问题都可行，也就是说，存在 (𝑥0,𝑦0)(x0,y0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝐴𝑥0=𝑏, 𝑥0≥0, 𝐴𝑇𝑦0≤𝑐Ax0=b, x0≥0, ATy0≤c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

成立，所以，有

0=(𝐴𝜇∗)𝑇𝑦0=(𝐴𝑇𝑦0)𝑇𝜇∗≤𝑐𝑇𝜇∗<𝑏𝑇𝜆∗=𝑥𝑇0𝐴𝑇𝜆∗≤0.0=(Aμ∗)Ty0=(ATy0)Tμ∗≤cTμ∗<bTλ∗=x0TATλ∗≤0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这显然矛盾．这一矛盾说明问题 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是可行的，进而说明强对偶成立．

从强对偶定理的证明过程还能得到如下推论：

推论

设原问题和对偶问题的一组可行解 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦∗y∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足强对偶性，即 𝑐𝑇𝑥∗ =𝑏𝑇𝑦∗cTx∗=bTy∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，它们同样分别是原问题和对偶问题的最优解．

强对偶定理说明，对于可行的线性规划问题，只需要求解它的对偶问题，就能够得到原问题的最优价值．

### 互补松弛条件

和其它的优化问题一样，互补松弛条件是线性规划问题的最优性条件的一部分．而且，因为目标函数是线性的，所以对于线性规划问题来说，互补松弛条件是可行解成为最优解的充分必要条件．

所谓 **互补松弛** （complementary slackness）条件，就是指只有在原问题（对偶问题）中的约束取得等号（即约束是紧的）的时候，对偶问题（原问题）中与之对应的变量才能取非零值．如果将变量取非零值也当成一条松弛的约束，那么这就相当于说，原问题和对偶问题中相对应的变量和约束不能同时是松弛的．因此，这一条件称为互补松弛条件．

以标准形式的线性规划问题为例，如下结论成立：

定理

假设 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦∗y∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是原问题 min{𝑐𝑇𝑥 :𝐴𝑥 =𝑏, 𝑥 ≥0}min{cTx:Ax=b, x≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和对偶问题 max{𝑏𝑇𝑦 :𝐴𝑇𝑦 ≤𝑐}max{bTy:ATy≤c}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的可行解．那么，当且仅当互补松弛条件成立，即

𝑥𝑇(𝐴𝑇𝑦−𝑐)=0xT(ATy−c)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时，𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦∗y∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也分别是原问题和对偶问题的最优解．

证明

因为 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦∗y∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是可行解，所以，有

𝑏𝑇𝑦∗−𝑐𝑇𝑥∗=(𝑥∗)𝑇(𝐴𝑇𝑦∗−𝑐).bTy∗−cTx∗=(x∗)T(ATy∗−c).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，互补松弛条件成立，当且仅当 𝑏𝑇𝑦∗ =𝑐𝑇𝑥∗bTy∗=cTx∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据强对偶定理的推论，这一条件成立，当且仅当 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦∗y∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是原问题的最优解．

标准形式可能太过特殊．该定理的稍微一般的形式如下：

定理

假设 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦∗y∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是原问题 min{𝑐𝑇𝑥 :𝐴𝑥 ≥𝑏, 𝑥 ≥0}min{cTx:Ax≥b, x≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和对偶问题 max{𝑏𝑇𝑦 :𝐴𝑇𝑦 ≤𝑐, 𝑦 ≥0}max{bTy:ATy≤c, y≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的可行解．那么，当且仅当互补松弛条件成立，即

𝑥𝑇(𝐴𝑇𝑦−𝑐)=𝑦𝑇(𝐴𝑥−𝑏)=0xT(ATy−c)=yT(Ax−b)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时，𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦∗y∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也分别是原问题和对偶问题的最优解．

证明

证明基本同上，只是这次要将差值写成

𝑏𝑇𝑦∗−𝑐𝑇𝑥∗=(𝑥∗)𝑇(𝐴𝑇𝑦∗−𝑐)−(𝑦∗)𝑇(𝐴𝑥∗−𝑏).bTy∗−cTx∗=(x∗)T(ATy∗−c)−(y∗)T(Ax∗−b).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

互补松弛条件提供了判断线性规划问题的可行解的最优性的简单条件．

### 原始‑对偶方法

对偶问题可以辅助原问题的求解．在解决线性规划问题时，常常会用到的一种方法是 **原始‑对偶方法** （primal-dual method）．它通过求解一系列相对简单的辅助问题，逐步改进对偶问题的解，进而获得原始问题的最优解．

对于标准形式的原问题

(𝑃)min{𝑐𝑇𝑥:𝐴𝑥=𝑏≥0, 𝑥≥0}(P)min{cTx:Ax=b≥0, x≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

和它的对偶问题

(𝐷)max{𝑏𝑇𝑦:𝐴𝑇𝑦≤𝑐},(D)max{bTy:ATy≤c},![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上一节已经说明，要找到它们的最优解，只需要找到问题 (𝑃)(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝐷)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组可行解，使得它们满足互补松弛条件 𝑥𝑇(𝐴𝑇𝑦 −𝑐) =0xT(ATy−c)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那不妨考虑如下流程：

  1. 从对偶问题 (𝐷)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个可行解 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，计算对偶问题的紧约束的集合

𝐼={𝑖:(𝐴𝑇𝑦−𝑐)𝑖=0}.I={i:(ATy−c)i=0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 根据互补松弛条件，如果存在问题 (𝑃)(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的可行解 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑥𝑖 >0xi>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仅在 𝑖 ∈𝐼i∈I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上成立，就意味着已经找到一组最优解．因此，考虑线性规划问题

(𝑅𝑃)min𝑥,𝑠𝟏𝑇𝑠subject to 𝐴𝑥+𝑠=𝑏,𝑥𝑖≥0, ∀𝑖∈𝐼,𝑥𝑖=0, ∀𝑖∉𝐼,𝑠≥0.(RP)minx,s1Tssubject to Ax+s=b,xi≥0, ∀i∈I,xi=0, ∀i∉I,s≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. 如果问题 (𝑅𝑃)(RP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小值是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么最优解 (𝑥∗,0)(x∗,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝑥∗x∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是原问题 (𝑃)(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最优解．否则，可以求出它的对偶问题 (𝐷𝑅𝑃)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解 ¯𝑦y¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

(𝐷𝑅𝑃)max𝑦𝑏𝑇𝑦subject to ∑𝑗𝑎𝑗𝑖𝑦𝑗≤0, ∀𝑖∈𝐼,𝑦≤1.(DRP)maxybTysubject to ∑jajiyj≤0, ∀i∈I,y≤1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据强对偶定理可知，𝑏𝑇¯𝑦 =1𝑇𝑠∗ >0bTy¯=1Ts∗>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  4. 根据问题 (𝐷𝑅𝑃)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解改进对偶问题 (𝐷)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的可行解．设 𝑦′ =𝑦 +𝜀¯𝑦y′=y+εy¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝜀 >0ε>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则一定有 𝑏𝑇𝑦′ =𝑏𝑇𝑦 +𝜀𝑏𝑇¯𝑦 >𝑏𝑇𝑦bTy′=bTy+εbTy¯>bTy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，只要保证 𝑦′y′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然是对偶问题的可行解 (𝐷)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就要尽可能大地选取 𝜀ε![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

对于 𝑖 ∈𝐼i∈I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

∑𝑗𝑎𝑗𝑖𝑦′𝑗=∑𝑗𝑎𝑗𝑖𝑦𝑗+𝜀∑𝑗𝑎𝑗𝑖¯𝑦𝑗≤𝑐𝑖,∑jajiyj′=∑jajiyj+ε∑jajiy¯j≤ci,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，问题 (𝐷)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的这些约束总是可以满足的．

对于剩下的约束，即 𝑖 ∉𝐼i∉I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，只需要取

𝜀=min{𝑐𝑖−∑𝑗𝑎𝑗𝑖𝑦𝑗∑𝑗𝑎𝑗𝑖¯𝑦𝑗:𝑖∉𝐼, ∑𝑗𝑎𝑗𝑖¯𝑦𝑗>0}ε=min{ci−∑jajiyj∑jajiy¯j:i∉I, ∑jajiy¯j>0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就可以在保证可行性的前提下，尽可能大地改进对偶问题的解，然后回到步骤 1 继续迭代．特别地，如果上式中的集合为空集，即 𝜀 = +∞ε=+∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，对偶问题 (𝐷)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无界，原问题 (𝑃)(P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不可行．

这个过程中其实只有问题 (𝐷𝑅𝑃)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是确实需要求解的，它与问题 (𝑅𝑃)(RP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通过强对偶定理相互联系．问题 (𝐷𝑅𝑃)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 提供了一个改进对偶问题解的方向，而且相对于对偶问题 (𝐷)(D)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 本身，问题 (𝐷𝑅𝑃)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式更加简单．问题 (𝐷𝑅𝑃)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的可行性由 Farkas 引理保证，而约束 𝑦 ≤1y≤1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只是一组规范化条件，保证了问题 (𝐷𝑅𝑃)(DRP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有界．

算法竞赛中，原始‑对偶方法广泛地应用于各类组合优化问题．例如二分图最大权匹配的 [匈牙利算法](../../graph/graph-matching/bigraph-weight-match/#hungarian-algorithmkuhnmunkres-algorithm)、最小费用流的 [消圈算法](../../graph/flow/min-cost/) 和 [SSP 算法（原始‑对偶算法）](../../graph/flow/min-cost/#ssp-算法)、最短路的 [Dijkstra 算法](../../graph/shortest-path/#dijkstra-算法)、最大流的 [Ford–Fulkerson 增广算法](../../graph/flow/max-flow/#fordfulkerson-增广) 等，都可以看作是原始‑对偶方法的直接应用．

## 整数规划

**整数规划** （integer programming）通常指 **整数线性规划** （integer linear programming, ILP）．标准形式的整数线性规划如下：

min𝑥𝑐𝑇𝑥subject to 𝐴𝑥=𝑏≥0,𝑥≥0,𝑥∈𝐙𝑛,minxcTxsubject to Ax=b≥0,x≥0,x∈Zn,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝐴 ∈𝐑𝑚×𝑛A∈Rm×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏 ∈𝐑𝑚b∈Rm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑐 ∈𝐑𝑛c∈Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，整数线性规划是在线性规划问题上添加决策变量必须为整数这一约束条件所得到的问题．

整数约束显著增加了整数规划问题的复杂性．许多组合优化问题，例如背包问题、适定性问题以及众多图论中的优化问题，都可以表示为整数规划模型，而这些问题中的多数被证明是 NP 困难的．

### 全幺模矩阵

正因如此，对于很多大规模的整数优化问题，有时候会考虑将它的整数约束松弛掉，转而求解一个线性规划问题．通常来说，松弛后的线性规划问题的最优价值只是原来的整数规划问题的一个下界估计（假设问题是最小化问题）．但是，如果松弛后的线性规划问题的最优解恰好是整数解，那么，它也一定是原来的整数规划问题的最优解．

一个自然的问题是，是否存在条件，能够保证线性规划问题的最优解都是整数解？全幺模矩阵的概念就提供了这样的一个条件．

全幺模矩阵

如果矩阵 𝐴 ∈𝐑𝑚×𝑛A∈Rm×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有子方阵的行列式都是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就称为一个 **全幺模矩阵** （totally unimodular matrix）．

特别地，全幺模矩阵的所有元素都是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．利用全幺模矩阵的概念，可以叙述如下结论：

定理

对于全幺模矩阵 𝐴 ∈𝐙𝑚×𝑛A∈Zm×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏 ∈𝐙𝑚b∈Zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑐 ∈𝐙𝑛c∈Zn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，线性规划问题及其对偶问题

min{𝑐𝑇𝑥:𝐴𝑥=𝑏,𝑥≥0}=max{𝑏𝑇𝑦:𝐴𝑇𝑦≤𝑐}min{cTx:Ax=b,x≥0}=max{bTy:ATy≤c}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

都有整数最优解，只要它们都有界．

证明

前文已经说明，线性规划问题的最优解集可以取作它的一个极小面，而后者是由若干线性独立的紧约束作为等式联立得到的方程组的解：

{𝑥∈𝐑𝑛:𝑎𝑇𝑗𝑥=𝑏𝑗, ∀𝑗∈𝐽}.{x∈Rn:ajTx=bj, ∀j∈J}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

记这个方程组为 𝐴𝐽𝑥 =𝑏𝐽AJx=bJ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝐴𝐽 =(𝐴1,𝐴2)AJ=(A1,A2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝐴1A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是满秩的方阵，行列式为 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，由 Cramer 法则，解

𝑥=(𝐴−11𝑏𝐽0)x=(A1−1bJ0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就是极小面上的一个整数解．

常见的图论模型中，网络流、最短路、二分图等对应的线性规划问题的系数矩阵都是全幺模矩阵．因此，只需要这些问题仅涉及整数参数，它们的最优解就可以取作整数，而不用担心线性规划问题的解对应着分数流、分数匹配等情形．所以，[最大流](../../graph/flow/max-flow/)、[最小割](../../graph/flow/min-cut/)、[最小费用流](../../graph/flow/min-cost/)、[最短路](../../graph/shortest-path/)、[差分约束](../../graph/diff-constraints/)、[二分图最大（权）匹配和最小点覆盖](../../graph/graph-matching/bigraph-match/#线性规划形式) 等问题，都可以转化为线性规划问题求解．而且，最大流与最小割、最短路与差分约束、二分图最大匹配和最小点覆盖，两两互为对偶问题．

除此之外，还有一些常见的图论模型，它所有的可行解恰巧是某个顶点均为整点的多胞形的全体顶点．因此，可以通过巧妙地选取约束，使得相应的组合优化问题的解，恰为某个线性规划问题的最优解．例如，一般图匹配和生成树等图论模型都属于这种情况，因此 [一般图最大（权）匹配](../../graph/graph-matching/general-weight-match/) 和 [最小生成树](../../graph/mst/) 等问题同样可以转化为线性规划问题．

## 参考文献与注释

  * Schrijver, Alexander. Theory of linear and integer programming. John Wiley & Sons, 1998.
  * Papadimitriou, Christos H., and Kenneth Steiglitz. Combinatorial optimization: algorithms and complexity. Courier Corporation, 1998.
  * [Duality in linear programming. Part 1—definition and construction. by adamant - Codeforces blog](https://codeforces.com/blog/entry/105049)
  * [Duality in linear programming. Part 2—in competitive programming. by adamant - Codeforces blog](https://codeforces.com/blog/entry/105789)

* * *

  1. 不同文献可能对这两个名词的定义有着不同的定义：有些文献会将有界的情形称作「多面体」，而将无界的情形称作「多胞形」；有些文献不会假定它们一定是凸集；有些文献会用「多面体」称呼三维空间中的多胞形．本文采取了与 Schrijver (1998) 和 Boyd and Vandenberghe (2004) 等文献一致的定义． ↩

  2. 更严格的表述是，它们之间可以在多项式时间内相互归约． ↩

  3. 其它用于解决不等式组的方法还包括 Fourier–Motzkin 消元法和 Agmon–Motzkin–Schoenberg 松弛法等．它们更为直接，但是效率往往不高． ↩

* * *

>  __本页面最近更新： 2026/3/9 02:30:31，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-programming.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/linear-programming.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [H-J-Granger](https://github.com/H-J-Granger), [zryi2003](https://github.com/zryi2003), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [huhaoo](https://github.com/huhaoo), [Konano](https://github.com/Konano), [NachtgeistW](https://github.com/NachtgeistW), [CCXXXI](https://github.com/CCXXXI), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [MegaOwIer](https://github.com/MegaOwIer), [partychicken](https://github.com/partychicken), [Suyun514](mailto:suyun514@qq.com), [AngelKitty](https://github.com/AngelKitty), [baker221](https://github.com/baker221), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [isdanni](https://github.com/isdanni), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [QAQAutoMaton](https://github.com/QAQAutoMaton), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Tiphereth-A](https://github.com/Tiphereth-A), [weiyong1024](https://github.com/weiyong1024), [c-forrest](https://github.com/c-forrest), [eleven-mile](https://github.com/eleven-mile), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Peanut-Tang](https://github.com/Peanut-Tang), [SukkaW](https://github.com/SukkaW), [xiaodong2077](https://github.com/xiaodong2077), [yusancky](https://github.com/yusancky), [YZircon](https://github.com/YZircon), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
