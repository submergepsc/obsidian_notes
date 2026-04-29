# 单纯形法 - OI Wiki

- Source: https://oi-wiki.org/math/simplex/

# 单纯形法

前置知识：[线性规划基础](../linear-programming/)

## 引入

算法竞赛中，经常使用单纯形法解决线性规划问题．但是，由于算法竞赛中遇到的线性规划问题大多有着更特殊的结构，常常可以转化为网络流问题，因此，单纯形法并不常用，效率也不如专门为网络流问题设计的算法．

## 基本概念

假设要求解如下一个有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个决策变量和 𝑚 +𝑛m+n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个约束的 [标准形式](../linear-programming/#标准形式) 线性规划问题：

min𝑥𝑧=𝑐𝑇𝑥subject to 𝐴𝑥=𝑏,𝑥≥0.minxz=cTxsubject to Ax=b,x≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

不妨假设这 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个等式约束确定的线性方程组有解，且 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满秩，则 rank⁡𝐴 =𝑚 ≤𝑛rank⁡A=m≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 一个例子

在严格叙述单纯形法的步骤之前，本节首先考察一个具体的例子，以方便理解．

例子

考虑线性规划问题

max10𝑥1+12𝑥2+12𝑥3subject to 𝑥1+2𝑥2+2𝑥3≤20,2𝑥1+𝑥2+2𝑥3≤20,2𝑥1+2𝑥2+𝑥3≤20,𝑥1,𝑥2,𝑥3≥0.max10x1+12x2+12x3subject to x1+2x2+2x3≤20,2x1+x2+2x3≤20,2x1+2x2+x3≤20,x1,x2,x3≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

通过添加松弛变量，就得到它的标准形式：

min−10𝑥1−12𝑥2−12𝑥3subject to 𝑥1+2𝑥2+2𝑥3+𝑥4=20,2𝑥1+𝑥2+2𝑥3+𝑥5=20,2𝑥1+2𝑥2+𝑥3+𝑥6=20,𝑥1,𝑥2,𝑥3,𝑥4,𝑥5,𝑥6≥0.min−10x1−12x2−12x3subject to x1+2x2+2x3+x4=20,2x1+x2+2x3+x5=20,2x1+2x2+x3+x6=20,x1,x2,x3,x4,x5,x6≥0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

观察该问题的等式约束，它们其实相当于将变量 𝑥4,𝑥5,𝑥6x4,x5,x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 由变量 𝑥1,𝑥2,𝑥3x1,x2,x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示．将原问题稍微整理一下，就有

min𝑥𝑖≥0𝑧=0−10𝑥1−12𝑥2−12𝑥3subject to𝑥4=20−𝑥1−2𝑥2−2𝑥3,𝑥5=20−2𝑥1−𝑥2−2𝑥3,𝑥6=20−2𝑥1−2𝑥2−𝑥3.minxi≥0z=0−10x1−12x2−12x3subject tox4=20−x1−2x2−2x3,x5=20−2x1−x2−2x3,x6=20−2x1−2x2−x3.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从这个形式中，可以清楚地看到，如果令 𝑥1 =𝑥2 =𝑥3 =0x1=x2=x3=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以得到原问题的一组可行解

𝑥=(0,0,0,20,20,20)𝑇.x=(0,0,0,20,20,20)T.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且它对应的价值为 𝑧 =0z=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．为方便叙述，称那些设为零的变量 𝑥1,𝑥2,𝑥3x1,x2,x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为非基变量，剩下的变量 𝑥4,𝑥5,𝑥6x4,x5,x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为基变量．

这组可行解显然不是最优解．只要适当地增加 𝑥1,𝑥2,𝑥3x1,x2,x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，使得 𝑥4,𝑥5,𝑥6x4,x5,x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然是非负数，就可以保持解仍然可行．而且，因为目标函数中，𝑥1,𝑥2,𝑥3x1,x2,x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数都是严格的负数，所以，增加它们的值一定会降低目标函数的值．比如说，可以选择增加 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．为了尽可能多地降低目标函数的值，需要尽可能多地增加 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．但是，为了保证解仍然是可行的，就需要保证 𝑥4,𝑥5,𝑥6 ≥0x4,x5,x6≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最多可以增加到

min{201,202,202}=10.min{201,202,202}=10.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此时，可行解变为

𝑥=(10,0,0,10,0,0)𝑇.x=(10,0,0,10,0,0)T.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成为了基变量，为了回到最初的情形（即三个基变量由三个非基变量表示），需要选择一个新的非基变量．因为 𝑥5,𝑥6x5,x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是零，所以，可以选择它们其中的任何一个作为非基变量，设为零．不妨选择 𝑥5x5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为非基变量．而且，将

𝑥1=10−0.5𝑥5−0.5𝑥2−𝑥3x1=10−0.5x5−0.5x2−x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入到原来的问题中，就可以将原问题改写作

min𝑥𝑖≥0𝑧=−100+5𝑥5−7𝑥2−2𝑥3subject to𝑥4=10+0.5𝑥5−1.5𝑥2−𝑥3,𝑥1=10−0.5𝑥5−0.5𝑥2−𝑥3,𝑥6=0+𝑥5−𝑥2+𝑥3.minxi≥0z=−100+5x5−7x2−2x3subject tox4=10+0.5x5−1.5x2−x3,x1=10−0.5x5−0.5x2−x3,x6=0+x5−x2+x3.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就回到了初始的情形．

继续观察当前的目标函数．非基变量 𝑥3x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数仍然是负数．可以考虑增加 𝑥3x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．为了保证 𝑥4,𝑥1,𝑥6 ≥0x4,x1,x6≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，变量 𝑥3x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最多只能增加到

min{101,101}=10.min{101,101}=10.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到，因为 𝑥6x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式中，𝑥3x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数是正数，所以，无论怎么增加 𝑥3x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，都不会使得 𝑥6x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为负数．这就是这次大括号中只有两项的原因．因为 𝑥3x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 增加到 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候，𝑥1,𝑥4x1,x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都变为零，所以，可以任选其中一个作为新的非基变量．不妨选择 𝑥4x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．就可以将

𝑥3=10+0.5𝑥5−1.5𝑥2−𝑥4x3=10+0.5x5−1.5x2−x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入上述问题中，问题变形为

min𝑥𝑖≥0𝑧=−120+4𝑥5−4𝑥2+2𝑥4subject to𝑥3=10+0.5𝑥5−1.5𝑥2−𝑥4,𝑥1=0−𝑥5+𝑥2+𝑥4,𝑥6=10+1.5𝑥5−2.5𝑥2−𝑥4.minxi≥0z=−120+4x5−4x2+2x4subject tox3=10+0.5x5−1.5x2−x4,x1=0−x5+x2+x4,x6=10+1.5x5−2.5x2−x4.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

只需要代入 𝑥5 =𝑥2 =𝑥4 =0x5=x2=x4=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就能从这个形式中读出当前的可行解是

𝑥=(0,0,10,0,0,10)𝑇,x=(0,0,10,0,0,10)T,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

以及它对应的价值为 𝑧 = −120z=−120![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

重复之前的操作．因为 𝑥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数是负数，可以增加它的值；但为了保持 𝑥3,𝑥6x3,x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然是非负数，只能增加到

min{101.5,102.5}=4.min{101.5,102.5}=4.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为大括号中的最小值出现在变量 𝑥6x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式中，所以，它将在 𝑥2 =4x2=4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时变为零．将表达式

𝑥2=4+0.6𝑥5−0.4𝑥6−0.4𝑥4x2=4+0.6x5−0.4x6−0.4x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入上述问题，就可以将原问题改写为

min𝑥𝑖≥0𝑧=−136+1.6𝑥5+1.6𝑥6+3.6𝑥4subject to𝑥3=4−0.4𝑥5+0.6𝑥6−0.4𝑥4,𝑥1=4−0.4𝑥5−0.4𝑥6+0.6𝑥4,𝑥2=4+1.5𝑥5−2.5𝑥6−𝑥4.minxi≥0z=−136+1.6x5+1.6x6+3.6x4subject tox3=4−0.4x5+0.6x6−0.4x4,x1=4−0.4x5−0.4x6+0.6x4,x2=4+1.5x5−2.5x6−x4.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

仍然令非基变量 𝑥5,𝑥6,𝑥4x5,x6,x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为零，就可以得到当前的可行解为

𝑥=(4,4,4,0,0,0)𝑇.x=(4,4,4,0,0,0)T.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对应的价值为 𝑧 = −136z=−136![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因为目标函数中所有非基变量的系数都是正数，无法继续前文所述过程以改进目标函数，所以，当前的可行解就是最优解．算法终止．

这个例子中，算法从一组可行解出发，不断地改进目标函数，直到无法继续改进．这就是单纯形法的基本思想．

### 基本可行解

由于 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是满秩的，所以，总是可以选取大小为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集 𝐵 ⊆{1,2,⋯,𝑛}B⊆{1,2,⋯,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝐴𝐵AB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是可逆方阵．由此，可以将 𝑥𝐵xB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 由剩下的变量 𝑥𝑁xN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示：

𝑥𝐵=𝐴−1𝐵𝑏−𝐴−1𝐵𝐴𝑁𝑥𝑁.xB=AB−1b−AB−1ANxN.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑁 ={1,2,⋯,𝑛} ∖𝐵N={1,2,⋯,n}∖B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，矩阵 𝐴𝐵,𝐴𝑁AB,AN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中标号 𝑖 ∈𝐵i∈B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和标号 𝑖 ∈𝑁i∈N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的列组成的子矩阵，向量 𝑥𝐵,𝑥𝑁xB,xN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为向量 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中标号 𝑖 ∈𝐵i∈B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和标号 𝑖 ∈𝑁i∈N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分量组成的子向量．如果 𝑖 ∈𝐵i∈B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，称 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **基变量** （basic variable）；否则，称 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **非基变量** （non-basic variable）．基变量的全体称为一组 **基** （basis），本文用对应的标号集合 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示一组基．

「基」

「基」这个名称，可以从线性代数的角度理解．设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体列向量张成的线性空间为 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，基 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的列向量就是空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组基．

在基变量 𝑥𝐵xB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式中，令 𝑥𝑁 =0xN=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到全体等式约束的一组解1

𝑥=(𝑥𝐵,𝑥𝑁)=(𝐴−1𝐵𝑏,0).x=(xB,xN)=(AB−1b,0).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样得到的解称为线性规划问题的一个 **基本解** （basic solution）．如果它还满足所有非负约束，即 𝑥 ≥0x≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，它也是原问题的一个可行解，也称为 **基本可行解** （basic feasible solution, BFS）．在单纯形法的迭代过程中，需要始终保持当前的解为一组基本可行解．

### 转轴

单纯形法的每次迭代就称为一次 **转轴** （pivoting）．从结果上看，每次转轴总是移除一个旧的基变量，再添加一个新的基变量，进而改进目标函数的值．

「转轴」

「转轴」这个名称，同样可以从线性代数的角度理解．如上文所述，基 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的列向量是空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组基，它们也就对应着对应基的表示下空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组坐标轴．因此，转轴的过程，就是将某条坐标轴旋转到新的位置的过程．

为了确定需要添加的基变量，可以将目标函数利用非基变量表示为

𝑐𝑇𝑥=𝑐𝑇𝐵𝑥𝐵+𝑐𝑇𝑁𝑥𝑁=𝑐𝑇𝐵𝐴−1𝐵𝑏+(𝑐𝑇𝑁−𝑐𝑇𝐵𝐴−1𝐵𝐴𝑁)𝑥𝑁.cTx=cBTxB+cNTxN=cBTAB−1b+(cNT−cBTAB−1AN)xN.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 𝑥𝑁 =0xN=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到目标函数在当前基本可行解处的价值 𝑧 =𝑐𝑇𝐵𝐴−1𝐵𝑏z=cBTAB−1b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．表达式中的第二项的系数则表示 𝑥𝑁xN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 改变时，目标函数的改变为

˜𝑐𝑁=𝜕𝑧𝜕𝑥𝑁=𝑐𝑁−𝐴𝑇𝑁(𝐴−1𝐵)𝑇𝑐𝐵.c~N=∂z∂xN=cN−ANT(AB−1)TcB.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到 𝑐𝐵 −𝐴𝑇𝐵(𝐴−1𝐵)𝑇𝑐𝐵 =0cB−ABT(AB−1)TcB=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，可以记向量

˜𝑐=(˜𝑐𝑇𝐵,˜𝑐𝑇𝑁)𝑇=𝑐−𝐴𝑇(𝐴−1𝐵)𝑇𝑐𝐵c~=(c~BT,c~NT)T=c−AT(AB−1)TcB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为线性规划问题在可行基本解 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的 **约化成本** （reduced cost）．分量 ˜𝑐𝑖 <0c~i<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 说明增加变量 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值可以改进原问题的目标函数．这样的变量只能是一个非基变量，它称为本次转轴的 **入基变量** （entering variable）．因为在转轴后，𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将变为基变量，不再恒设为零（但依然有可能等于零）．

选择完入基变量后，还需要选择需要移除的旧的基变量．为此，只需要确定，在增加 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的过程中，哪个现有的基变量最先变为零．将 𝑥𝑁 =(𝑥𝑖,𝑥𝑁∖{𝑖}) =(𝑥𝑖,0)xN=(xi,xN∖{i})=(xi,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代入 𝑥𝐵xB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式，就有

𝑥𝐵=𝐴−1𝐵𝑏−𝐴−1𝐵𝐴𝑖𝑥𝑖.xB=AB−1b−AB−1Aixi.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以增加的最大量就等于

𝜃=min{(𝐴−1𝐵𝑏)𝑗(𝐴−1𝐵𝐴𝑖)𝑗:(𝐴−1𝐵𝐴𝑖)𝑗>0}.θ=min{(AB−1b)j(AB−1Ai)j:(AB−1Ai)j>0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最先变为零的变量就是使得该表达式取得最小值的下标 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的基变量 𝑥𝐵𝑗xBj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．它也是增加 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的过程中的「瓶颈」——继续增加 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将使得 𝑥𝐵𝑗xBj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成为负值．这一变量就是本次转轴的 **出基变量** （leaving variable）．确定出基变量的方法称为 **最小比值检验** （minimum ratio test）．

设入基变量为 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，出基变量为 𝑥𝑖′xi′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．转轴之后，基变量就是 𝑥𝐵∖{𝑖}∪{𝑖′}xB∖{i}∪{i′}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，非基变量就是 𝑥𝑁∖{𝑖′}∪{𝑖}xN∖{i′}∪{i}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 终止条件

单纯形法，就是从一组基本可行解出发，不断进行转轴的过程．上一节对转轴的讨论并不是完整的，它忽略了一些特殊的情形．有些特殊情形对应着算法的终止，有些则需要额外的处理．

首先，入基变量未必存在，即 ˜𝑐 ≥0c~≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时，没有进一步改进最优价值的方法，这说明当前基本可行解就是最优解，算法终止．要严格地证明这一点，需要用到 [互补松弛条件](../linear-programming/#互补松弛条件)．令 𝑦 =(𝐴−1𝐵)𝑇𝑐𝐵y=(AB−1)TcB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意到，在算法的整个过程中，始终保持 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是可行解，且互补松弛条件成立，即

𝑥𝑇(𝑐−𝐴𝑇𝑦)=˜𝑐𝑇𝑥=˜𝑐𝑇𝐵𝑥𝐵+˜𝑐𝑇𝑁𝑥𝑁=0.xT(c−ATy)=c~Tx=c~BTxB+c~NTxN=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，只需要 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是对偶问题的可行解，即 𝐴𝑇𝑦 ≤𝑐ATy≤c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就能得到 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是原问题和对偶问题的最优解这一结论．这个条件就是 ˜𝑐 ≥0c~≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即不存在入基变量．

「影子价格」

向量 𝑦 =(𝐴−1𝐵)𝑇𝑐𝐵y=(AB−1)TcB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 常称为 **对偶向量** （dual vector）．当 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的基本可行解是原问题的最优解时，向量 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是对偶问题的最优解．因此，利用单纯形法求解原问题的最优解时，也会获得对偶问题的最优解．因为向量 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是当前价值关于约束常量的偏导数，即

𝜕(𝑐𝑇𝑥)𝜕𝑏=(𝐴−1𝐵)𝑇𝑐𝐵=𝑦,∂(cTx)∂b=(AB−1)TcB=y,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它也称为 **影子价格** （shadow price）．

其次，出基变量未必存在，即 𝐴−1𝐵𝐴𝑖 ≤0AB−1Ai≤0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时，转轴的过程不存在任何「瓶颈」，也就是说，可以不断地通过增加 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值来改进目标函数，直到它等于 −∞−∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这说明给定的线性规划问题是无界的，算法终止．

最后，入基变量和出基变量的选择可能并非是唯一的．不恰当的选择方式可能会导致过多地转轴，甚至使得算法陷入循环，无法正常终止．这类情形的处理稍微复杂，需要应用一些 转轴规则 以防止陷入循环并减少转轴次数．

### 单纯形表

具体实现转轴过程时，只需要维护每次转轴之后，线性规划问题的系数矩阵：

˜𝑇𝐵=(−𝑧𝐵˜𝑐𝑇𝑁𝑥𝐴−1𝐵𝐴𝑁)=(−𝑐𝑇𝐵𝐴−1𝐵𝑏𝑐𝑇−𝑐𝑇𝐵𝐴−1𝐵𝐴𝑁𝐴−1𝐵𝑏𝐴−1𝐵𝐴𝑁).T~B=(−zBc~NTxAB−1AN)=(−cBTAB−1bcT−cBTAB−1ANAB−1bAB−1AN).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它对应着线性规划问题：

min𝑥≥0𝑐𝑇𝐵𝐴−1𝐵𝑏+˜𝑐𝑇𝑁𝑥𝑁subject to𝑥𝐵=𝐴−1𝐵𝑏−𝐴−1𝐵𝐴𝑁𝑥𝑁.minx≥0cBTAB−1b+c~NTxNsubject toxB=AB−1b−AB−1ANxN.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

矩阵 ˜𝑇𝐵T~B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为该线性规划问题相对于基 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **压缩单纯形表** （condensed simplex tableau）．表的左上角 (˜𝑇𝐵)00(T~B)00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为当前解的价值（的相反数），第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行、第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的量 (˜𝑇𝐵)0𝑖(T~B)0i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个非基变量 𝑥𝑁𝑖xNi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约化成本，第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行、第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的量 (˜𝑇𝐵)𝑗0(T~B)j0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个基变量 𝑥𝐵𝑗xBj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，而 𝐴−1𝐵𝐴𝑁AB−1AN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是用非基变量 𝑥𝑁xN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示基变量 𝑥𝐵xB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到的表达式中的系数．

容易看出，转轴需要的所有信息都可以从压缩单纯形表中直接获得．具体地，利用压缩单纯形表，单次转轴包括如下操作：

  1. 选取列 𝑖 =1,⋯,𝑛 −𝑚i=1,⋯,n−m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 (˜𝑇𝐵)0𝑖 <0(T~B)0i<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果不存在这样的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么当前解就是最优解，量 −(˜𝑇𝐵)00−(T~B)00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是最优价值．
  2. 选取行 𝑗 =1,⋯,𝑚j=1,⋯,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 (˜𝑇𝐵)𝑗𝑖 >0(T~B)ji>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 (˜𝑇𝐵)𝑗0/(˜𝑇𝐵)𝑗𝑖(T~B)j0/(T~B)ji![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小．如果不存在这样的 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么原问题无界．
  3. 令变量 𝑥𝑁𝑖xNi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 入基，变量 𝑥𝐵𝑗xBj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出基，并更新单纯形表．

现在，具体地讨论一下如何更新单纯形表．在更新单纯形表之前，第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行表示等式

𝑥𝐵𝑗=(˜𝑇𝐵)𝑗0−𝑛−𝑚∑𝑖=1(˜𝑇𝐵)𝑗𝑖𝑥𝑁𝑖.xBj=(T~B)j0−∑i=1n−m(T~B)jixNi.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为了更新单纯形表，需要用 𝑥𝑁∖{𝑁𝑖}∪{𝐵𝑗}xN∖{Ni}∪{Bj}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑥𝑁𝑖xNi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是：

𝑥𝑁𝑖=(˜𝑇𝐵)𝑗0(˜𝑇𝐵)𝑗𝑖−1(˜𝑇𝐵)𝑗𝑖𝑥𝐵𝑗−∑𝑖′≠𝑖(˜𝑇𝐵)𝑗𝑖′(˜𝑇𝐵)𝑗𝑖𝑥𝑁𝑖′.xNi=(T~B)j0(T~B)ji−1(T~B)jixBj−∑i′≠i(T~B)ji′(T~B)jixNi′.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将它代入其余的式子中，就得到

𝑥𝐵𝑗′=((˜𝑇𝐵)𝑗′0−(˜𝑇𝐵)𝑗′𝑖(˜𝑇𝐵)𝑗0(˜𝑇𝐵)𝑗𝑖)+(˜𝑇𝐵)𝑗′𝑖(˜𝑇𝐵)𝑗𝑖𝑥𝐵𝑗−∑𝑖′≠𝑖((˜𝑇𝐵)𝑗′𝑖′−(˜𝑇𝐵)𝑗′𝑖(˜𝑇𝐵)𝑗𝑖′(˜𝑇𝐵)𝑗𝑖)𝑥𝑁𝑖.xBj′=((T~B)j′0−(T~B)j′i(T~B)j0(T~B)ji)+(T~B)j′i(T~B)jixBj−∑i′≠i((T~B)j′i′−(T~B)j′i(T~B)ji′(T~B)ji)xNi.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行类似，只是等式左侧变为 −𝑧−z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．虽然式子看起来复杂，但是实现时，只需要分两步：

  1. 更新第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行，即令 𝛼 =(˜𝑇𝐵)𝑗𝑖α=(T~B)ji![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再令第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列数字为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后将整行所有数字同除以 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 更新第 𝑗′ ≠𝑗j′≠j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行，即令 𝛽 =(˜𝑇𝐵)𝑗′𝑖β=(T~B)j′i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再令第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列数字为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后将整行数字同时减去 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倍的第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行数字．

「单纯形表」

**单纯形表** （simplex tableau）指矩阵

𝑇𝐵=(−𝑧˜𝑐𝑇𝑥𝐴−1𝐵𝐴)=(−𝑐𝑇𝐵𝐴−1𝐵𝑏𝑐𝑇−𝑐𝑇𝐵𝐴−1𝐵𝐴𝐴−1𝐵𝑏𝐴−1𝐵𝐴).TB=(−zc~TxAB−1A)=(−cBTAB−1bcT−cBTAB−1AAB−1bAB−1A).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

相较于压缩单纯形表，它多了 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列，分别对应 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个基变量；而且，对应着第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个基变量的列一定是 𝑒𝑗ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即该向量只在第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行处取值为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其余行均为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为这些列并没有提供多余的信息，所以在实现单纯形法时，常常省略这些列，这就得到了压缩单纯形表．

利用单纯形表可以更方便地理解更新单纯形表的步骤．因为所有的单纯形表 𝑇𝐵TB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以由同一个矩阵 𝑇0T0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 左乘一个与基有关的可逆矩阵 𝐿𝐵LB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到，即

𝑇𝐵=(−𝑐𝑇𝐵𝐴−1𝐵𝑏𝑐𝑇−𝑐𝑇𝐵𝐴−1𝐵𝐴𝐴−1𝐵𝑏𝐴−1𝐵𝐴)=(1−𝑐𝑇𝐵𝐴−1𝐵𝑂𝐴−1𝐵)(0𝑐𝑇𝑏𝐴)=𝐿𝐵𝑇0,TB=(−cBTAB−1bcT−cBTAB−1AAB−1bAB−1A)=(1−cBTAB−1OAB−1)(0cTbA)=LBT0,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，这些单纯形表和 𝑇0T0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间可以通过若干次 [初等行变换](../linear-algebra/elementary-operations/) 相互转化．因此，在更新单纯形表时，只需要施行初等行变换，使得入基变量对应列变为 𝑒𝑗ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．由此，所需要的操作迁移到压缩单纯形表上，就是上文给出的步骤．

更新压缩单纯形表的参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text // Pivot on (N[x], B[y]). void pivot ( int x , int y ) { std :: swap ( N [ x ], B [ y ]); long double v = -1 / tab [ x ][ y ]; for ( int j = 0 ; j <= m \+ 1 ; ++ j ) { tab [ x ][ j ] = j == y ? \- v : v * tab [ x ][ j ]; } for ( int i = 0 ; i <= n ; ++ i ) { if ( i == x ) continue ; v = tab [ i ][ y ]; tab [ i ][ y ] = 0 ; for ( int j = 0 ; j <= m \+ 1 ; ++ j ) { tab [ i ][ j ] += v * tab [ x ][ j ]; } } } ```   
---|---  
  
由该实现可知，单次更新单纯形表的时间复杂度为 𝑂(𝑚𝑛)O(mn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．稍后讨论 转轴规则 时会说明，确定出基变量和入基变量的复杂度同样不会超过 𝑂(𝑚𝑛)O(mn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此，单次转轴的时间复杂度就是 𝑂(𝑚𝑛)O(mn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

为方便理解，此处列出前文所示例子中，利用压缩单纯形表计算的详细步骤．

例子（续）

初始时，压缩单纯形表如下所示：

𝑥1𝑥2𝑥30−10−12−12𝑥4=20122𝑥5=20212𝑥6=20221x1x2x30−10−12−12x4=20122x5=20212x6=20221![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的约化成本，可以选择 𝑥1,𝑥2,𝑥3x1,x2,x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 入基．令 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 入基．再根据根据最小比值检验，可以选择 𝑥5,𝑥6x5,x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出基．令 𝑥5x5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出基．相应地，更新压缩单纯形表如下：

𝑥5𝑥2𝑥31005−7−2𝑥4=10−0.51.51𝑥1=100.50.51𝑥6=0−11−1x5x2x31005−7−2x4=10−0.51.51x1=100.50.51x6=0−11−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的约化成本，可以选择 𝑥2,𝑥3x2,x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 入基．令 𝑥3x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 入基．再根据根据最小比值检验，可以选择 𝑥4,𝑥1x4,x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出基．令 𝑥4x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出基．相应地，更新压缩单纯形表如下：

𝑥5𝑥2𝑥41204−42𝑥3=10−0.51.51𝑥1=01−1−1𝑥6=10−1.52.51x5x2x41204−42x3=10−0.51.51x1=01−1−1x6=10−1.52.51![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的约化成本，只能选择 𝑥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 入基．令 𝑥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 入基．再根据根据最小比值检验，只能选择 𝑥6x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出基．令 𝑥6x6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出基．利用前述初等行变换更新单纯形表如下：

𝑥5𝑥4𝑥61361.63.61.6𝑥3=40.40.4−0.6𝑥1=40.4−0.60.4𝑥2=4−0.60.40.4x5x4x61361.63.61.6x3=40.40.4−0.6x1=40.4−0.60.4x2=4−0.60.40.4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的约化成本，不存在入基变量．因此，当前解

𝑥=(4,4,4,0,0,0)𝑇x=(4,4,4,0,0,0)T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就是最优解，（最小化问题的）最优价值为 −136−136![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

除了利用单纯形表实现单纯形法之外，还可以使用修正单纯形法（revised simplex method），它进一步改进了算法的时空复杂度，将单次更新的复杂度进一步降低到了 𝑂(𝑚2)O(m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在 𝑚 ≪𝑛m≪n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是稀疏矩阵的情形下尤为高效．

## 几何背景

本节介绍单纯形法的几何背景．

对线性规划问题的可行域

D={𝑥∈𝐑𝑛:𝐴𝑥=𝑏, 𝑥≥0}D={x∈Rn:Ax=b, x≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的 [分析](../linear-programming/#可行域与问题的解) 指出：

  * 线性规划问题的最优解（如果存在）必然可以选取为可行域 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的顶点．求解线性规划问题，就转化于在所有顶点解里找到价值函数最优的那个．
  * 每一个顶点的坐标，都可以通过 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个紧约束联立得到的方程组求解得到．对于标准形式的约束，所有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个等式约束一定是紧的，剩下的 𝑛 −𝑚n−m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个约束只能从非负约束中选取．选取这些非负约束作为紧约束，就相当于将相应的决策变量 𝑥𝑁xN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 设为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；相应地，方程组 𝐴𝑥 =𝑏Ax=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 退化为关于剩余 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个决策变量 𝑥𝐵xB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性方程组 𝐴𝐵𝑥𝐵 =𝑏ABxB=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．只要 𝐴𝐵AB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可逆，就可以解得 𝑥𝐵 =𝐴−1𝐵𝑏xB=AB−1b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就得到了一个解 (𝑥𝐵,𝑥𝑁) =(𝐴−1𝐵𝑏,0)(xB,xN)=(AB−1b,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；如果 𝑥𝐵 ≥0xB≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这就是 DD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个顶点坐标．

容易看出，顶点解的概念，和前文定义的基本可行解是一致的．因此，只要在所有基本可行解内找到最优的那个，就能获得原问题的最优解．虽然这大幅简化了问题，但是，可行域的顶点的个数是指数级的，穷举并不现实．

为了解决这一困难，可以考虑沿着可行域的 [边](../linear-programming/#可行域与问题的解) 移动，从一个顶点移动到与之相邻的顶点．因为相邻的顶点必定位于同一条边上，所以，它们至少满足 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条相同的紧约束．也就是说，相邻的顶点对应的紧约束能且仅能相差一个．因此，对于一个基本可行解 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只要将它的一个基变量换成一个非基变量，就能得到一个 **相邻的** （adjacent）的基本可行解 𝑥′x′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这正是转轴操作．

因此，单纯形法从一个基本可行解出发，不断进行转轴，改进目标函数的过程，其实就是在相应的可行域上，从一个顶点出发，不断向相邻顶点移动，进而改进目标函数的过程．

例子（续）

本文讨论的例子中，可行域是一个有五个顶点的三维多面体，如下图所示：

![](./images/simplex-geo.svg)

前述求解过程，从几何直观上看，就对应着多面体的顶点间的如下路径：

(0,0,0)→(0,0,10)→(10,0,0)→(4,4,4).(0,0,0)→(0,0,10)→(10,0,0)→(4,4,4).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 实现细节

利用单纯形表，已经能够求解许多线性规划问题．然而，对于最一般的情形，单纯形法中仍有许多细节值得深入探讨．

### 松弛形式

将一般形式的线性规划问题转化为标准形式的 [方法](../linear-programming/#标准形式) 已经讨论过了．但是，为了方便利用单纯形法求解，还需要保证系数矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满秩．虽然先转换为标准形式再消去线性相关的约束的方法是可行的，但是为了求解简便，通常采用如下策略：

  1. 将线性规划问题转化为 **不等式形式** （inequality form），即 min{𝑐𝑇𝑥 :𝐴𝑥 ≤𝑏, 𝑥 ≥0}min{cTx:Ax≤b, x≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式；
  2. 通过添加松弛变量 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将问题转化为标准形式：min{𝑐𝑇𝑥 :𝐴𝑥 +𝑠 =𝑏, 𝑥 ≥0, 𝑠 ≥0}min{cTx:Ax+s=b, x≥0, s≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这样做的好处是，最终得到的标准形式的系数矩阵 (𝐴,𝐼)(A,I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是满秩的，且总是存在（未必可行的）基本解 (𝑥,𝑠) =(0,𝑏)(x,s)=(0,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这种特殊的标准形式也称为 **松弛形式** （slack form）．

### 初始基本可行解

前文描述的单纯形法总是假定已知一组基本可行解．有些时候，很容易找到一组基本可行解．例如，如果上述松弛形式中 𝑏 ≥0b≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，(𝑥,𝑠) =(0,𝑏)(x,s)=(0,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是一组基本可行解．这就是前文的数值例子里遇到的情形．

对于一般的情形，可以采用 **两阶段法** （two-phase method）．两阶段法中，需要做两次单纯形法．第一阶段求解一个可行性线性规划问题，获得原问题的一个基本可行解．第二阶段从这个基本可行解出发，应用单纯形法求解原问题．

假设有标准形式的问题 min{𝑐𝑇𝑥 :𝐴𝑥 =𝑏 ≥0, 𝑥 ≥0}min{cTx:Ax=b≥0, x≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在第一阶段中，需要求解问题

min{1𝑇𝑥𝑎:𝐴𝑥+𝑥𝑎=𝑏, 𝑥≥0, 𝑠≥0}.min{1Txa:Ax+xa=b, x≥0, s≥0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这本质是可行性线性规划问题，其中，新添加的变量 𝑥𝑎xa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也称为 **人工变量** （artificial variable）．它一定有基本可行解 (𝑥,𝑥𝑎) =(0,𝑏)(x,xa)=(0,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以可以直接用单纯形法求解．如果该问题的最优价值严格大于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，就不存在 𝑥 ≥0x≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝐴𝑥 =𝑏Ax=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，原问题不可行．如果该问题的最优价值等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，它的最优解中人工变量只能是零．如果仍有一些人工变量是基变量，可以通过若干次转轴将它们出基．最后，当所有人工变量都是非基变量时，第一阶段得到的基本解就可以用作第二阶段的初始基本可行解．

不显式引入人工变量的第一阶段实现

实现第一阶段时，没有必要显式地引入人工变量．对于任意选取的初始基 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝑥𝐵+𝐴−1𝐵𝐴𝑁𝑥𝑁=𝐴−1𝐵𝑏.xB+AB−1ANxN=AB−1b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果 (𝐴−1𝐵𝑏)𝑗 ≥0(AB−1b)j≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么无需引入人工变量；否则，需要额外引入人工变量 𝑥−𝐵𝑗xBj−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即

𝑥𝐵𝑗−𝑥−𝐵𝑗+(𝐴−1𝐵𝐴𝑁)(𝑗)𝑥𝑁=(𝐴−1𝐵𝑏)𝑗.xBj−xBj−+(AB−1AN)(j)xN=(AB−1b)j.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

记下标集合 𝐿 :={𝑗 :(𝐴−1𝐵𝑏)𝑗 <0}L:={j:(AB−1b)j<0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么一阶段的单纯形表都是如下单纯形表经过若干初等行变换得到的：

𝑥𝑁𝑥𝐵∼𝐿𝑥𝐵𝐿𝑥−𝐵𝐿00𝑇0𝑇0𝑇1𝑇𝑥𝐵∼𝐿=(𝐴−1𝐵𝑏)∼𝐿(𝐴−1𝐵𝐴𝑁)(∼𝐿)𝐼𝑂𝑂𝑥−𝐵𝐿=(𝐴−1𝐵𝑏)𝐿(𝐴−1𝐵𝐴𝑁)(𝐿)𝑂𝐼−𝐼xNxB∼LxBLxBL−00T0T0T1TxB∼L=(AB−1b)∼L(AB−1AN)(∼L)IOOxBL−=(AB−1b)L(AB−1AN)(L)OI−I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

类似于将单纯形表简化为压缩单纯形表，可以将其适当地简化：（将 𝑥−𝐵𝐿xBL−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行左乘以 1𝑇1T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 然后加到第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行上，然后略去后三列）

𝑥𝑁1𝑇𝑏𝐿1𝑇(𝐴−1𝐵𝐴𝑁)𝐿𝑥𝐵∼𝐿=(𝐴−1𝐵𝑏)∼𝐿(𝐴−1𝐵𝐴𝑁)(∼𝐿)−𝑥𝐵𝐿=(𝐴−1𝐵𝑏)𝐿(𝐴−1𝐵𝐴𝑁)𝐿xN1TbL1T(AB−1AN)LxB∼L=(AB−1b)∼L(AB−1AN)(∼L)−xBL=(AB−1b)L(AB−1AN)L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这与正常的压缩单纯形表大体一致，只是最后一行的变量上标记了负号，表示该行仍然含有人工变量，即原来的松弛变量仍然不可行．利用该表，转轴过程如下：

  1. 如果 𝐿 =∅L=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，算法终止．
  2. 否则，根据第 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的约化成本为负这一条件选取入基变量 𝑥𝑁𝑖xNi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果不存在，则原问题不可行，算法终止．
  3. 再根据第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列选取出基变量 𝑥𝐵𝑗xBj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．仍然利用最小比值检验，但是要求同时保证当前的可行变量可行和当前的不可行变量不可行，即选取

arg⁡min𝑗{(˜𝑇𝐵)𝑗0(˜𝑇𝐵)𝑗𝑖:(𝑗∉𝐿∧(˜𝑇𝐵)𝑗𝑖>0)∨(𝑗∈𝐿∧(˜𝑇𝐵)𝑗𝑖<0)}arg⁡minj{(T~B)j0(T~B)ji:(j∉L∧(T~B)ji>0)∨(j∈L∧(T~B)ji<0)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

作为出基变量所在行．如果存在多个这样的出基变量，优先选取不可行的出基变量．

  4. 令 𝑥𝑁𝑖xNi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 入基，𝑥𝐵𝑗xBj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出基，并更新单纯形表．

  5. 如果 𝑗 ∈𝐿j∈L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么将 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 移出 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即取消该行的负号标记），并且将 (˜𝑇𝐵)0𝑖(T~B)0i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加一．

之所以可以略去人工变量所在列，是因为如果它们仍然是基变量，那么它们对应的列就是 𝑒𝑗ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，无需记录，而如果它们不再是基变量，那么它们就不会再次入基，也无需记录．人工变量出基时，需要替换成相应的非人工变量，这正是上述过程中最后一步的目的．

参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 ``` |  ```text // First phase: find an initial BFS. // Return false if no feasible solution. bool initialize () { int neg_count = 0 ; for ( int j = 0 ; j < m ; ++ j ) { if ( tab [ n ][ j ] < \- eps ) { for ( int i = 0 ; i <= n ; ++ i ) { tab [ i ][ m \+ 1 ] += tab [ i ][ j ]; } B [ j ] = ~ B [ j ]; ++ neg_count ; } } while ( neg_count ) { int x = -1 ; long double mi = \- eps ; for ( int i = 0 ; i < n ; ++ i ) { if ( tab [ i ][ m \+ 1 ] < mi ) { x = i ; mi = tab [ i ][ m \+ 1 ]; } } if ( x == -1 ) return false ; int y = -1 ; mi = INFINITY ; for ( int j = 0 ; j < m ; ++ j ) { if (( B [ j ] < 0 && tab [ x ][ j ] < \- eps ) || ( B [ j ] >= 0 && tab [ x ][ j ] > eps )) { auto tmp = tab [ n ][ j ] / tab [ x ][ j ] \+ ( B [ j ] < 0 ? \- eps : eps ); if ( tmp < mi ) { y = j ; mi = tmp ; } } } if ( B [ y ] < 0 ) { \-- neg_count ; B [ y ] = ~ B [ y ]; pivot ( x , y ); tab [ x ][ m \+ 1 ] += 1 ; } else { pivot ( x , y ); } } return true ; } ```   
---|---  
  
在一阶段开始前，额外添加一行用于记录一阶段的目标函数．转轴时，对整个表进行转轴，包括第二阶段的目标函数．这样，在第一阶段完成时，第二阶段的目标函数也一并相应地更新，可以直接开始二阶段的单纯形法．

两阶段法也可以通过一次单纯形法实现．只需要取充分大的正数 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以通过直接求解问题

min{𝑐𝑇𝑥+𝑀1𝑇𝑥𝑎:𝐴𝑥+𝑥𝑎=𝑏, 𝑥≥0, 𝑠≥0}min{cTx+M1Txa:Ax+xa=b, x≥0, s≥0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

得到原问题的最优解．实现时，并不会赋予 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 具体的数值，而是将它视为一个未知的充分大的正数进行运算．这种方法称为 **大 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 法**（big 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) method）．

朴素算法的实际效率是指数级的

因为松弛形式总是存在初始基本解，只是未必是可行的，所以，一种简单的寻找初始基本可行解的想法是，从一个不可行的基本解出发，反复利用转轴操作，将不可行的基变量出基，并选择对应行中同样为负的数字对应列的非基变量入基，直到所有基变量都是非负数为止．参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text // First phase: find an initial BFS. // Return false if no feasible solution. bool initialize () { while ( true ) { int y = -1 ; long double mi = \- eps ; for ( int j = 0 ; j < m ; ++ j ) { if ( tab [ n ][ j ] <= mi ) { y = j ; mi = tab [ n ][ j ]; } } // No row with a negative basic variable => Feasible. if ( y == -1 ) break ; int x = -1 ; for ( int i = 0 ; i < n ; ++ i ) { if ( tab [ i ][ y ] < \- eps && ( x == -1 || N [ i ] > N [ x ])) { x = i ; } } // No column with a negative entry => Infeasible. if ( x == -1 ) return false ; pivot ( x , y ); } return true ; } ```   
---|---  
  
这样做虽然简单，但是相较于二阶段法，它没有一个描述当前基的不可行程度的目标函数，所以缺乏明确的改进方向．实际测试可以发现，相较于通常只需要 𝑂(𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的转轴次数的二阶段法或大 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 法，这一朴素算法通常需要 𝑂(2𝑚)O(2m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的转轴次数，且当 𝑛,𝑚n,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 较大时容易陷入循环．虽然朴素算法的转轴次数中的常数很小，但是仅仅适用于 𝑛,𝑚 <50n,m<50![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．

### 转轴规则

转轴时，如果出现多个可选的入基变量或出基变量，就需要用到 **转轴规则** （pivot rule）来决定选择哪个变量入基或出基．利用单纯形表，本节讨论的所有规则都能够在 𝑂(𝑚𝑛)O(mn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内找到入基和出基变量，因此，单次转轴的时间复杂度仍然是 𝑂(𝑚𝑛)O(mn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

入基变量的选择往往决定了算法终止前转轴的次数．常见的规则如下：

  * 选择最先找到的入基变量；
  * 选择标号最小的入基变量；（Bland 规则的一部分）
  * 选择约化成本绝对值（即 |𝑐𝑖||ci|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）最大的入基变量；（Dantzig 规则）
  * 选择单次转轴价值函数改进（即 |𝑐𝑖|𝜃𝑖|ci|θi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）最大的入基变量；
  * 选择对应着最陡的边的入基变量，即沿着边移动单位长度引起的价值函数改进（即 |𝑐𝑖|/‖𝐴−1𝐵𝐴𝑖‖|ci|/‖AB−1Ai‖![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）最大；
  * 随机选择一个入基变量．

实践中，最陡边规则的效率最高2．通常认为，适当的转轴规则可以在大致 2𝑚2m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次转轴内得到大多数问题的最优解．但是，对于目前所有已知的转轴规则，都存在特殊构造的例子3，能够将转轴次数卡到指数级．这也正是单纯形法实践中运行效率相当优秀，但是理论最差复杂度是指数级的原因．

出基变量的选择往往决定了算法是否会陷入循环．如果存在多个最优价值相同的基本可行解，那么，算法就有可能一直在这些基本可行解之间循环．这些情形并不常见，因此很多单纯形法的实现并不会指定出基变量的选择规则．常见的避免循环的规则有两种：

  * Bland 规则：总是选择标号最小的入基变量和出基变量．
  * 字典序规则：总是选择 (𝐴−1𝐵𝐴𝑖)𝑗 >0(AB−1Ai)j>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且

((𝐴−1𝐵𝑏)𝑗(𝐴−1𝐵𝐴𝑖)𝑗,(𝐴−1𝐵)𝑗1(𝐴−1𝐵𝐴𝑖)𝑗,⋯,(𝐴−1𝐵)𝑗𝑚(𝐴−1𝐵𝐴𝑖)𝑗)((AB−1b)j(AB−1Ai)j,(AB−1)j1(AB−1Ai)j,⋯,(AB−1)jm(AB−1Ai)j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

字典序最小的行号 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的出基变量 𝑥𝐵𝑗xBj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．入基变量的选择不重要．

注意，如果线性规划问题是松弛形式的，那么这些量都可以从前文所述形式的单纯形表 𝑇𝐵TB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中直接找到；否则，可以在找到一组初始基本解（未必可行）后，利用这些初始基中的基变量对应列（顺序保持固定）的系数作为 𝐴−1𝐵AB−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数．

Bland 规则效率很低，因为规则本身对入基和出基变量的选择方法是一样的，这很容易造成同一个变量反复入基再出基．相对来说，字典序规则更为实用．字典序规则相当于对线性规划问题中的参数进行微扰4，使得不存在最优价值相同的基本可行解，也就不存在循环的可能性．

## 参考实现

本节提供一个基于压缩单纯形表的二阶段单纯形法的参考实现．

[Luogu P13337【模板】线性规划](https://www.luogu.com.cn/problem/P13337)

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 ``` |  ```text #include <algorithm> #include <climits> #include <cmath> #include <iomanip> #include <iostream> #include <numeric> #include <vector> int m , n ; // Number of constraints and variables. std :: vector < std :: vector < long double >> tab ; // Compressed tableau (transposed) with // first-phase objective attached. std :: vector < int > B , N ; // Basic and nonbasic variables. constexpr long double eps = 1e-12l ; // Precision. // Pivot on (N[x], B[y]). void pivot ( int x , int y ) { std :: swap ( N [ x ], B [ y ]); long double v = -1 / tab [ x ][ y ]; for ( int j = 0 ; j <= m \+ 1 ; ++ j ) { tab [ x ][ j ] = j == y ? \- v : v * tab [ x ][ j ]; } for ( int i = 0 ; i <= n ; ++ i ) { if ( i == x ) continue ; v = tab [ i ][ y ]; tab [ i ][ y ] = 0 ; for ( int j = 0 ; j <= m \+ 1 ; ++ j ) { tab [ i ][ j ] += v * tab [ x ][ j ]; } } } // First phase: find an initial BFS. // Return false if no feasible solution. bool initialize () { int neg_count = 0 ; for ( int j = 0 ; j < m ; ++ j ) { if ( tab [ n ][ j ] < \- eps ) { for ( int i = 0 ; i <= n ; ++ i ) { tab [ i ][ m \+ 1 ] += tab [ i ][ j ]; } B [ j ] = ~ B [ j ]; ++ neg_count ; } } while ( neg_count ) { int x = -1 ; long double mi = \- eps ; for ( int i = 0 ; i < n ; ++ i ) { if ( tab [ i ][ m \+ 1 ] < mi ) { x = i ; mi = tab [ i ][ m \+ 1 ]; } } if ( x == -1 ) return false ; int y = -1 ; mi = INFINITY ; for ( int j = 0 ; j < m ; ++ j ) { if (( B [ j ] < 0 && tab [ x ][ j ] < \- eps ) || ( B [ j ] >= 0 && tab [ x ][ j ] > eps )) { auto tmp = tab [ n ][ j ] / tab [ x ][ j ] \+ ( B [ j ] < 0 ? \- eps : eps ); if ( tmp < mi ) { y = j ; mi = tmp ; } } } if ( B [ y ] < 0 ) { \-- neg_count ; B [ y ] = ~ B [ y ]; pivot ( x , y ); tab [ x ][ m \+ 1 ] += 1 ; } else { pivot ( x , y ); } } return true ; } // Second phase: find an optimal BFS. // Return false if the problem is unbounded. bool simplex () { while ( true ) { int x = -1 ; long double mi = \- eps ; for ( int i = 0 ; i < n ; ++ i ) { if ( tab [ i ][ m ] < mi ) { x = i ; mi = tab [ i ][ m ]; } } // No column with a negative reduced cost => Optimal. if ( x == -1 ) break ; int y = -1 ; mi = INFINITY ; for ( int j = 0 ; j < m ; ++ j ) { if ( tab [ x ][ j ] <= eps ) continue ; if ( tab [ n ][ j ] / tab [ x ][ j ] < mi ) { y = j ; mi = tab [ n ][ j ] / tab [ x ][ j ]; } } // No row with a positive ratio => Unbounded. if ( y == -1 ) return false ; pivot ( x , y ); } return true ; } int solve () { B . resize ( m ); N . resize ( n ); std :: iota ( B . begin (), B . end (), n ); std :: iota ( N . begin (), N . end (), 0 ); return initialize () ? ( simplex () ? 0 : 1 ) : -1 ; } int main () { std :: ios :: sync_with_stdio ( false ), std :: cin . tie ( nullptr ); std :: cout << std :: fixed << std :: setprecision ( 8 ); std :: cin >> n >> m ; tab . assign ( n \+ 1 , std :: vector < long double > ( m \+ 2 )); for ( int i = 0 ; i < n ; ++ i ) { std :: cin >> tab [ i ][ m ]; tab [ i ][ m ] = \- tab [ i ][ m ]; } for ( int j = 0 ; j < m ; ++ j ) { for ( int i = 0 ; i <= n ; ++ i ) { std :: cin >> tab [ i ][ j ]; } } switch ( solve ()) { case -1 : std :: cout << "Infeasible" << std :: endl ; break ; case 1 : std :: cout << "Unbounded" << std :: endl ; break ; case 0 : { std :: cout << tab [ n ][ m ] << std :: endl ; std :: vector < long double > x ( n ); for ( int j = 0 ; j < m ; ++ j ) { if ( B [ j ] < n ) x [ B [ j ]] = tab [ n ][ j ]; } for ( int i = 0 ; i < n ; ++ i ) { std :: cout << x [ i ] << ' ' ; } std :: cout << std :: endl ; break ; } } return 0 ; } ```   
---|---  
  
## 例题

[「NOI2008」志愿者招募](https://www.luogu.com.cn/problem/P3980)

总共 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 天活动需要招募志愿者，其中，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 天至少需要 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位志愿者．总有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类志愿者，其中，第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类志愿者可以服务的日期为连续区间 [𝑙𝑗,𝑟𝑗][lj,rj]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且单位招募成本为 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．求最优的招募方案，使得招募志愿者的成本最低．

解答

设第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类志愿者招募 𝑥𝑗xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位．那么，可以列出线性规划问题为

max𝑥𝑚∑𝑗=1𝑐𝑗𝑥𝑗subject to 𝑛∑𝑖=1𝑎𝑖𝑗𝑥𝑗≥𝑏𝑖, 𝑖=1,⋯,𝑛,𝑥𝑗≥0, 𝑗=1,⋯,𝑚.maxx∑j=1mcjxjsubject to ∑i=1naijxj≥bi, i=1,⋯,n,xj≥0, j=1,⋯,m.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，系数

𝑎𝑖𝑗={1,𝑙𝑗≤𝑖≤𝑟𝑗,0,otherwise.aij={1,lj≤i≤rj,0,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

原问题没有显然的初始可行解．因此，不妨考虑其 [对偶问题](../linear-programming/#对偶问题)：

min𝑦𝑛∑𝑖=1𝑏𝑖𝑦𝑖subject to 𝑛∑𝑗=1𝑎𝑖𝑗𝑦𝑖≤𝑐𝑗, 𝑗=1,⋯,𝑚,𝑦𝑖≥0, 𝑖=1,⋯,𝑛.miny∑i=1nbiyisubject to ∑j=1naijyi≤cj, j=1,⋯,m,yi≥0, i=1,⋯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

通过添加松弛变量，容易得到一组初始可行解，可以直接略过一阶段，通过单纯形法求解．根据对偶原理，得到的解就是原问题的解．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` |  ```text #include <cmath> #include <cstring> #include <iostream> using namespace std ; constexpr int M = 10005 , N = 1005 , INF = 1e9 ; int n , m ; double a [ M ][ N ], b [ M ], c [ N ], v ; void pivot ( int l , int e ) { // 转轴操作函数 b [ l ] /= a [ l ][ e ]; for ( int j = 1 ; j <= n ; j ++ ) if ( j != e ) a [ l ][ j ] /= a [ l ][ e ]; a [ l ][ e ] = 1 / a [ l ][ e ]; for ( int i = 1 ; i <= m ; i ++ ) if ( i != l && fabs ( a [ i ][ e ]) > 0 ) { b [ i ] -= a [ i ][ e ] * b [ l ]; for ( int j = 1 ; j <= n ; j ++ ) if ( j != e ) a [ i ][ j ] -= a [ i ][ e ] * a [ l ][ j ]; a [ i ][ e ] = \- a [ i ][ e ] * a [ l ][ e ]; } v += c [ e ] * b [ l ]; for ( int j = 1 ; j <= n ; j ++ ) if ( j != e ) c [ j ] -= c [ e ] * a [ l ][ j ]; c [ e ] = \- c [ e ] * a [ l ][ e ]; // swap(B[l],N[e]) } double simplex () { while ( true ) { int e = 0 , l = 0 ; for ( e = 1 ; e <= n ; e ++ ) if ( c [ e ] > ( double ) 0 ) break ; if ( e == n \+ 1 ) return v ; // 此时v即为最优解 double mn = INF ; for ( int i = 1 ; i <= m ; i ++ ) { if ( a [ i ][ e ] > ( double ) 0 && mn > b [ i ] / a [ i ][ e ]) { mn = b [ i ] / a [ i ][ e ]; // 找对这个e限制最紧的l l = i ; } } if ( mn == INF ) return INF ; // unbounded pivot ( l , e ); // 转动l,e } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> m ; for ( int i = 1 ; i <= n ; i ++ ) cin >> c [ i ]; for ( int i = 1 ; i <= m ; i ++ ) { int s , t ; cin >> s >> t ; for ( int j = s ; j <= t ; j ++ ) a [ i ][ j ] = 1 ; // 表示第i种志愿者在j时间可以服务 cin >> b [ i ]; } cout << ( int )( simplex () \+ 0.5 ); } ```   
---|---  
  
## 习题

  * [Luogu P13337【模板】线性规划](https://www.luogu.com.cn/problem/P13337)
  * [UOJ#179. 线性规划](https://uoj.ac/problem/179)
  * [Luogu P4232 无意识之外的捉迷藏](https://www.luogu.com.cn/problem/P4232)
  * [Codeforces 1430 G. Yet Another DAG Problem](https://codeforces.com/problemset/problem/1430/G)
  * [AtCoder Beginner Contest 231 H - Minimum Coloring](https://atcoder.jp/contests/abc231/tasks/abc231_h)

## 参考资料

  * [线性规划之单纯形法【超详解 + 图解】](https://www.cnblogs.com/ECJTUACM-873284962/p/7097864.html)
  * [2016 国家集训队论文](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2016%E8%AE%BA%E6%96%87%E9%9B%86.pdf)
  * 算法导论
  * Matoušek, Jiří, and Bernd Gärtner. Understanding and using linear programming. Vol. 1. Berlin: Springer, 2007.
  * Inayatullah, Syed, Nasir Touheed, and Muhammad Imtiaz. "A streamlined artificial variable free version of simplex method." PloS one 10, no. 3 (2015): e0116156.
  * Floudas, Christodoulos A., and Panos M. Pardalos, eds. Encyclopedia of optimization. Springer Science & Business Media, 2008.

* * *

  1. 原则上，因为所有向量默认为列向量，(𝑥𝐵,𝑥𝑁)(xB,xN)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应该写作 (𝑥𝑇𝐵,𝑥𝑇𝑁)𝑇(xBT,xNT)T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是为了简化记号，本文所有类似的情形都直接写作 (𝑥𝐵,𝑥𝑁)(xB,xN)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而省略转置符号． ↩

  2. 测试结果参见 Forrest, John J., and Donald Goldfarb. "Steepest-edge simplex algorithms for linear programming." Mathematical programming 57, no. 1 (1992): 341-374． ↩

  3. 一个经典的反例可以参见 Klee, Victor, and George J. Minty. "How good is the simplex algorithm." Inequalities 3, no. 3 (1972): 159-175． ↩

  4. 详细的解释可以看 [这份讲义](https://facultyweb.kennesaw.edu/mlavrov/courses/lp/lecture8.pdf)． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/simplex.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/simplex.md "edit.link.title")  
>  __本页面贡献者：[StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [NachtgeistW](https://github.com/NachtgeistW), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [Early0v0](https://github.com/Early0v0), [MegaOwIer](https://github.com/MegaOwIer), [sshwy](https://github.com/sshwy), [Xeonacid](https://github.com/Xeonacid), [ZnPdCo](https://github.com/ZnPdCo), [c-forrest](https://github.com/c-forrest), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Gesrua](https://github.com/Gesrua), [Henry-ZHR](https://github.com/Henry-ZHR), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [LovelyBuggies](https://github.com/LovelyBuggies), [lychees](https://github.com/lychees), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [orzzzjq](https://github.com/orzzzjq), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [Backl1ght](https://github.com/Backl1ght), [baker221](https://github.com/baker221), [Chrogeek](https://github.com/Chrogeek), [FFjet](https://github.com/FFjet), [GavinZhengOI](https://github.com/GavinZhengOI), [Han-Yu-Meng](https://github.com/Han-Yu-Meng), [HeRaNO](https://github.com/HeRaNO), [HomuraCat](https://github.com/HomuraCat), [iamtwz](https://github.com/iamtwz), [ImpleLee](https://github.com/ImpleLee), [kenlig](https://github.com/kenlig), [kxccc](https://github.com/kxccc), [Marcythm](https://github.com/Marcythm), [Molmin](https://github.com/Molmin), [opsiff](https://github.com/opsiff), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [Raisetsu41](https://github.com/Raisetsu41), [SukkaW](https://github.com/SukkaW), [yusancky](https://github.com/yusancky)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
