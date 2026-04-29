# Schreier–Sims 算法 - OI Wiki

- Source: https://oi-wiki.org/math/algebra/schreier-sims/

# Schreier–Sims 算法

前置知识：[抽象代数基本概念](../basic/)、[群论](../group-theory/)、[置换与排列](../../permutation/)

## 引入

**Schreier–Sims 算法** 是计算群论（computational group theory）的一种算法，以数学家 Otto Schreier 和 Charles Sims 的名字命名．该算法能够在多项式时间内解决诸如找到有限置换群的阶数、查看给定置换是否包含在所给群中等许多问题．Schreier–Sims 算法最早由 Sims 在 1970 年基于 Schreier 引理引入．在 1981 年1，Donald Knuth 进一步改进了该算法的运行时间．后来，该算法又发展出来一种更快的随机化版本．计算机代数系统（例如 GAP 和 Magma）通常使用该算法的高度优化过的 Monte Carlo 版本2．

记号

本文依照计算群论文献的惯例，将群作用记作右作用，这意味着置换的复合由左向右进行．本文涉及的群作用都可以视为置换作用，尽管部分算法对于更广泛的群作用也成立．相应地，群作用的集合默认为 𝑋 ={1,2,⋯,𝑛}X={1,2,⋯,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中的元素则称为点．置换 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作用在点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上得到的结果记作 𝑥𝑔xg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有时也称置换 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 移动到点 𝑥𝑔xg![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．最后，置换群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作用下，点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的轨道记作 𝑥𝐺 ={𝑥𝑔 :𝑔 ∈𝐺}xG={xg:g∈G}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的稳定化子则记作 𝐺𝑥 ={𝑔 ∈𝐺 :𝑥𝑔 =𝑥}Gx={g∈G:xg=x}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．稳定化子的概念还可以推广到集合 𝐵 ⊆𝑋B⊆X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的稳定化子定义为 𝐺𝐵 =⋂𝑥∈𝐵𝐺𝑥GB=⋂x∈BGx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 概述

Schreier–Sims 算法主要试图解决这样一个问题：

  * 给定大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的一些置换组成的集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如何在计算机中高效地存储由 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 生成的置换群 𝐺 =⟨𝑆⟩G=⟨S⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并完成一系列对该群的查询任务？

显然，这样的群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的规模可能很大，且远远大于集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和生成集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的规模．比如，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次对称群 𝑆𝑛 =⟨(123⋯𝑛),(12)⟩Sn=⟨(123⋯n),(12)⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小为 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是它可以仅由两个置换生成．存储群中的每一个元素是不现实的．

类似于利用 [Gauss 消元法](../../numerical/gauss/) 构建出向量空间的一组 [线性基](../../linear-algebra/basis/)，Schreier–Sims 算法的思路是找到有限置换群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组「基」：

  1. 算法的输入是 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个生成集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中有若干个置换；
  2. 如果群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不平凡，总能找到在群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作用下位置会发生变化的点 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 |𝛽𝐺| >1|βG|>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  3. 找到点 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的轨道 Δ =𝛽𝐺Δ=βG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并对轨道中的每个点 𝛿 ∈Δδ∈Δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都找到群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中一个置换 𝑡𝛿tδ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它能够将点 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 移动到 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  4. 找到点 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的稳定化子 𝐺𝛽Gβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个生成集 𝑆′S′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  5. 递归地对 𝐺′ =⟨𝑆′⟩G′=⟨S′⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 调用该算法，直到得到平凡的群 {𝑒}{e}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这个思路的合理性在于，点 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的稳定化子 𝐺𝛽Gβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子群，它的全体（右）陪集构成群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分划，且这些陪集和点 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的轨道 𝛽𝐺βG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一一对应，步骤 3 中求得的那些置换 𝑡𝛿tδ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是这些陪集的代表元．这个陪集代表元的集合 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为稳定化子 𝐺𝛽Gβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **陪集代表系** （transversal）．换句话说，群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的每个元素 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都和唯一的一对元素 (ℎ,𝑡) ∈𝐺𝛽 ×𝑇(h,t)∈Gβ×T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应，且 𝑔 =ℎ𝑡g=ht![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因而，只要能想办法存储子群 𝐺𝛽Gβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和相应的陪集代表系 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以存储整个群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．然而，存储子群 𝐺𝛽Gβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题也已经解决了——只要递归调用算法即可．

当然，算法的实现还有很多细节需要梳理，这是本文的主要内容．但是在那之前，首先要考察调用该算法之后得到的结果，看看算法将群存储为怎样的结构，能够解决怎样的查询问题．为此，应当明晰一些概念．

### 稳定化子链

假设对群 𝐺 ={𝑆}G={S}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 调用该算法，共进行了 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次；且在第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次调用该算法时，输入是置换的集合 𝑆(𝑖−1)S(i−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，找到的点是 𝛽𝑖βi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得到的陪集代表系是 𝑇𝑖Ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得到的稳定化子的生成集是 𝑆(𝑖)S(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果记 𝐺(𝑖) =⟨𝑆(𝑖)⟩G(i)=⟨S(i)⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，算法实际上得到了子群链

𝐺=𝐺(0)>𝐺(1)>⋯>𝐺(𝑘−1)>𝐺(𝑘)={𝑒}.G=G(0)>G(1)>⋯>G(k−1)>G(k)={e}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而且，每一个链中的子群都是一个稳定化子

𝐺(𝑖)=𝐺𝛽1,⋯,𝛽𝑖.G(i)=Gβ1,⋯,βi.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因而，Schreier–Sims 算法可以看作就是在计算这样一个 **稳定化子链** （stabilizer chain）．

### 基和强生成集

如果集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝐺𝐵 ={𝑒}GB={e}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就称 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是置换群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组 **基** （base）．显然，上述算法得到了一组基 𝐵 ={𝛽1,⋯,𝛽𝑘}B={β1,⋯,βk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这意味着，置换 𝑔 ∈𝐺g∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对这些点作用的结果在群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中唯一地确定了这个置换．而且，算法输出的这个基还满足条件

𝐺(𝑖−1)=𝐺𝛽1,⋯,𝛽𝑖−1>𝐺𝛽1,⋯,𝛽𝑖−1,𝛽𝑖=𝐺(𝑖).G(i−1)=Gβ1,⋯,βi−1>Gβ1,⋯,βi−1,βi=G(i).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就是说，基中的每个点都蕴含着关于群中的元素的有效信息．这样的基称为 **无冗余的** （nonredundant）．算法总是输出无冗余的基．这样的基对应的稳定化子链是严格递降的．

同时，算法得到的生成集的并集

¯𝑆=𝑘⋃𝑖=0𝑆𝑖S¯=⋃i=0kSi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也是群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成集，且成立 ⟨¯𝑆 ∩𝐺(𝑖)⟩ =𝐺(𝑖)⟨S¯∩G(i)⟩=G(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．满足这个条件的生成集称为群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相对于基 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **强生成集** （strong generating set）．因而，Schreier–Sims 算法也可以看作是在计算群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **基和强生成集** （base and strong generating set, BSGS）．这个说法和稳定化子链的说法是等价的，本文不加以区分．

当然，算法还得到了一系列轨道 Δ𝑖 =𝛽𝐺(𝑖−1)𝑖Δi=βiG(i−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和相应的陪集代表系 𝑇𝑖Ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这些轨道称为群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **基础轨道** （fundamental orbits）．当本文提及群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的稳定化子链或者基和强生成集时，总是默认相应的基础轨道和陪集代表系都已经一并求出．

### 数据结构

本文会提供一系列伪代码．伪代码中，群的稳定化子链（或基和强生成集）存储在数据结构 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中：

𝐶=(𝑆,Δ,𝑇,𝐶′).C=(S,Δ,T,C′).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个结构中的数据成员分别是当前群的生成集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、基础轨道 ΔΔ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、相应的陪集代表系 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和存储为嵌套子结构的稳定化子 𝐶′C′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．当然，稳定化子 𝐶′C′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是这样的一个结构．整个群实际存储在一个层状结构中，每层都描述了稳定化子链中的一个群．最内层是空的结构体，表示 𝐺(𝑘) ={𝑒}G(k)={e}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在伪代码中，该数据结构中的成员可以分别由 𝐶.𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟𝑠C.generators![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐶.𝑜𝑟𝑏𝑖𝑡C.orbit![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙C.transversal![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐶.𝑛𝑒𝑥𝑡C.next![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 访问．轨道的首个元素 𝐶.𝑜𝑟𝑏𝑖𝑡[0]C.orbit[0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 默认是基中的点 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而相应的陪集代表元 𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛽]C.transversal[β]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 默认是恒等变换 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意，虽然此处用数组下标访问了轨道和陪集代表系中的元素，但是它们未必存储为数组，而应当理解为它们提供了访问轨道首元素和根据轨道中的点查询相应的陪集代表元的方法．下文会讨论具体的实现细节．

### 应用

在获得群的基和强生成集后，能够解决一系列关于群的查询问题．其中，最基础的，也是算法竞赛中最常遇到的，是查询群的阶数和查询某个置换是否属于给定群的问题．

#### 群的阶数

如果已知群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基和强生成集，那么应用 Lagrange 定理和轨道稳定化子定理可知，群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶数可以计算为

|𝐺|=𝑘∏𝑖=1[𝐺(𝑖−1):𝐺(𝑖)]=𝑘∏𝑖=1[𝐺(𝑖−1):𝐺(𝑖−1)𝛽𝑖]=𝑘∏𝑖=1|𝑇𝑖|.|G|=∏i=1k[G(i−1):G(i)]=∏i=1k[G(i−1):Gβi(i−1)]=∏i=1k|Ti|.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，只要将所有陪集代表系 𝑇𝑖Ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小（或者等价地，基础轨道 Δ𝑖Δi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的长度）乘起来就可以得到群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶数．

#### 成员判定

已知群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基和强生成集，也可以判定某个置换 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否属于群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这称为 **成员判定** （membership testing）问题．

这个问题可以递归地解决．要判定 ℎ ∈𝐺(𝑖−1)h∈G(i−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，首先要找到 𝐺(𝑖)G(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的包含 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的陪集的代表元 𝑡 ∈𝑇𝑖t∈Ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果能够找到，那么设 ℎ′ =ℎ𝑡−1h′=ht−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有 ℎ =ℎ′𝑡h=h′t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 ℎ ∈𝐺(𝑖−1)h∈G(i−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价于 ℎ′ ∈𝐺(𝑖)h′∈G(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；问题就转化为判定 ℎ′ ∈𝐺(𝑖)h′∈G(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果找不到这样的 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或者已经递归到了 𝐺(𝑘) ={𝑒}G(k)={e}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 但是 ℎ ≠𝑒h≠e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以得出结论，ℎ ∉𝐺h∉G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其实，这个过程不仅判定了 ℎ ∈𝐺h∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而且在 ℎ ∈𝐺h∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形下，还能够将 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示为一系列陪集代表元的乘积 𝑡𝑘⋯𝑡2𝑡1tk⋯t2t1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑡𝑖 ∈𝑇𝑖ti∈Ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素，这样的表示存在且唯一．这再次证明了上面关于群的阶数的公式是正确的．

现在将该过程写成如下伪代码：

𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 MembershipTest(𝐶,ℎ):𝐈𝐧𝐩𝐮𝐭. A stabilizer chain 𝐶 for a group 𝐺 and a permutation ℎ.𝐎𝐮𝐭𝐩𝐮𝐭. Whether ℎ∈𝐺.𝐌𝐞𝐭𝐡𝐨𝐝.1𝐰𝐡𝐢𝐥𝐞 𝐶 is not empty 2𝛽←𝐶.𝑜𝑟𝑏𝑖𝑡[0]3𝛿←𝛽ℎ4𝐢𝐟 𝛿∈𝐶.𝑜𝑟𝑏𝑖𝑡 𝐭𝐡𝐞𝐧5𝑡←𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛿]6ℎ←ℎ𝑡−17𝐞𝐥𝐬𝐞 8𝐫𝐞𝐭𝐮𝐫𝐧 false9𝐞𝐧𝐝 𝐢𝐟10𝐶←𝐶.𝑛𝑒𝑥𝑡11𝐞𝐧𝐝 𝐰𝐡𝐢𝐥𝐞12𝐫𝐞𝐭𝐮𝐫𝐧 ℎ=𝑒Algorithm MembershipTest(C,h):Input. A stabilizer chain C for a group G and a permutation h.Output. Whether h∈G.Method.1while C is not empty 2β←C.orbit[0]3δ←βh4if δ∈C.orbit then5t←C.transversal[δ]6h←ht−17else 8return false9end if10C←C.next11end while12return h=e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

下文会看到，成员判定问题也是本文所讨论的 Schreier–Sims 算法的实现中的一个重要组成部分．

## 轨道、陪集代表系和稳定化子的计算

要实现 Schreier–Sims 算法，首先要解决如下子问题：3

  * 给定群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一个点 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如何求出轨道 𝛽𝐺βG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、相应的陪集代表系 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和稳定化子 𝐺𝛽Gβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成集？

这就是本节要解决的问题．

### 轨道和陪集代表系的存储

要求得轨道和陪集代表系，只要直接搜索就好了．伪代码如下：

𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 OrbitTransversal(𝑆,𝛽):𝐈𝐧𝐩𝐮𝐭. A generating set 𝑆 for a group 𝐺 and a point 𝛽.𝐎𝐮𝐭𝐩𝐮𝐭. The orbit Δ=𝛽𝐺 and the transversal 𝑇.𝐌𝐞𝐭𝐡𝐨𝐝.1Δ←[𝛽]2𝑇[𝛽]←𝑒3𝐟𝐨𝐫 𝛿∈Δ4𝐟𝐨𝐫 𝑠∈𝑆5𝛾←𝛿𝑠6𝐢𝐟 𝛾∉Δ 𝐭𝐡𝐞𝐧7append 𝛾 to Δ8𝑇[𝛾]←𝑇[𝛿]⋅𝑠9𝐞𝐧𝐝 𝐢𝐟10𝐞𝐧𝐝 𝐟𝐨𝐫11𝐞𝐧𝐝 𝐟𝐨𝐫12𝐫𝐞𝐭𝐮𝐫𝐧 Δ,𝑇Algorithm OrbitTransversal(S,β):Input. A generating set S for a group G and a point β.Output. The orbit Δ=βG and the transversal T.Method.1Δ←[β]2T[β]←e3for δ∈Δ4for s∈S5γ←δs6if γ∉Δ then7append γ to Δ8T[γ]←T[δ]⋅s9end if10end for11end for12return Δ,T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

具体实现的时候，使用广度优先搜索和深度优先搜索都是可以的．搜索遍历到的状态数目是 |𝑆||𝑇||S||T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只要能合理地存储轨道和陪集代表系，时间复杂度是完全可以接受的．

由于在置换群的语境下，轨道无非是至多 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的集合，为了高效完成查找和添加操作，可以使用布尔值数组或是无序集合存储．这样两个操作的时间复杂度都是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，整体的空间占用是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．当然，取决于陪集代表系的实现，可能还需要额外标记首元素的位置．

问题在于使用什么样的数据结构存储相应的陪集代表系 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 直接存储

最简单的方法，当然是直接存储陪集代表系 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的每一个元素 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．单个置换存储为 [单行记号](../../permutation/#单行记号)，需要的空间恰为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以存储这样的陪集代表系的空间复杂度是 𝑂(|𝑇|𝑛)O(|T|n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．这样做的好处是访问单个陪集代表元的时间复杂度是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，代价是初次计算这些陪集代表元的时间复杂度是 𝑂(|𝑇|𝑛)O(|T|n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

#### Schreier 树

另外一种常见的做法是实现一个树形结构用于存储陪集代表系．它称为 **Schreier 树** （Schreier tree）或 **Schreier 向量** （Schreier vector）4．它以 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根，以轨道 ΔΔ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为顶点．每次在搜索过程中得到新的顶点 𝛾 =𝛿𝑠γ=δs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，就从旧的顶点 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到新的顶点 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条边，边上记录生成集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中置换 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序号（或指针）．因为已经存储了生成集，存储陪集代表系的额外空间复杂度是 𝑂(|𝑇|)O(|T|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的规模很大的情形，这样做可以有效地节约空间，而且初次计算的时候复杂度是 𝑂(|𝑇|)O(|T|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．但是，副作用就是每次需要获得陪集代表元的时候，需要遍历顶点到根的路径上的边，重新计算陪集代表元，因而时间复杂度高度依赖于 Schreier 树的深度．对于一般的情形，树的深度可能达到 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别．

在具体实现的时候，需要根据实际情况权衡算法的时空复杂度．对于算法竞赛可能涉及的情形，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通常都不大，空间充足，而时间复杂度常常成为瓶颈．稍后会看到，Schreier–Sims 算法最耗时的步骤恰好需要多次访问陪集代表元，因而使用直接存储的方式往往更优．但是对于某些应用场景，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能很大，存储空间可能更为紧张，就有可能需要使用 Schreier 树的方式存储陪集代表系．对于这种情况，为避免 Schreier 树深度过深，研究者提出了很多方法，可以在树的深度过深的时候重构出浅的 Schreier 树．有兴趣的读者可以参考文末的文献．

在伪代码中，本文不会区分具体的陪集代表系的实现，而只假设存储陪集代表系 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数据结构实现了根据轨道元素 𝛿 ∈Δδ∈Δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 访问和修改对应陪集代表元 𝑇[𝛿]T[δ]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的操作．

### Schreier 引理

在获得了轨道 𝛽𝐺βG![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和陪集代表系 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，Schreier 引理继而提供了获得稳定化子 𝐺𝛽Gβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成集的方法．

Schreier 引理

设群 𝐺 =⟨𝑆⟩G=⟨S⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有子群 𝐻 ≤𝐺H≤G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是子群 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的（右）陪集代表系，且 𝑒 ∈𝑇e∈T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)9，并记 𝑔 ∈𝐺g∈G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在陪集的代表元 𝑡 ∈𝑇t∈T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 ――𝑔g―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，集合

𝑈={𝑡𝑠(――𝑡𝑠)−1:𝑡∈𝑇,𝑠∈𝑆}U={ts(ts―)−1:t∈T,s∈S}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

是子群 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个生成集．它的元素称为子群 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **Schreier 生成元** （Schreier generator）．

证明

首先，根据陪集代表元的定义可知，𝑡𝑠(――𝑡𝑠)−1 ∈𝐻ts(ts―)−1∈H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对所有 𝑡 ∈𝑇,𝑠 ∈𝑆t∈T,s∈S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立，故而 ⟨𝑈⟩ ⊆𝐻⟨U⟩⊆H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

反过来，对于任何 ℎ ∈𝐻h∈H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐺 ≥𝐻G≥H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成集，必然存在一列 𝑠𝑖 ∈𝑆 ∪𝑆−1si∈S∪S−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

ℎ=𝑠1𝑠2⋯𝑠𝑟h=s1s2⋯sr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

成立．令 𝑡1 =𝑒t1=e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并递归地定义 𝑡𝑖+1 =―――𝑠𝑖𝑡𝑖 ∈𝑇ti+1=siti―∈T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是，有

ℎ=(𝑡1𝑠1𝑡−12)(𝑡2𝑠2𝑡−13)⋯(𝑡𝑟𝑠𝑟𝑡𝑟+1)−1𝑡𝑟+1.h=(t1s1t2−1)(t2s2t3−1)⋯(trsrtr+1)−1tr+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而对于每个 𝑖 =1,2,⋯,𝑟i=1,2,⋯,r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 𝑡𝑖𝑠𝑖𝑡−1𝑖+1 =𝑡𝑖𝑠𝑖(―――𝑡𝑖𝑠𝑖)−1 ∈𝑈 ∪𝑈−1 ⊆𝐻tisiti+1−1=tisi(tisi―)−1∈U∪U−1⊆H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而有 𝑡𝑟+1 ∈𝐻tr+1∈H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，𝐻 ∩𝑇 ={𝑒}H∩T={e}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以有 𝑡𝑟+1 =𝑒tr+1=e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就说明，任意 ℎ ∈𝐻h∈H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以写作一列 𝑢𝑖 =𝑡𝑖𝑠𝑖𝑡−1𝑖+1 ∈𝑈 ∪𝑈−1ui=tisiti+1−1∈U∪U−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘积，亦即 𝑈U![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 生成 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因为陪集代表系 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的子群就是稳定化子 𝐺𝛽Gβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以求出陪集代表系 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后再结合群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就能得到稳定化子 𝐺𝛽Gβ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成集．

### 算法

只要对上面的伪代码稍作修改，就能在计算轨道和陪集代表系的同时得到相应的稳定化子的生成集：

𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 OrbitTransversalStabilizer(𝑆,𝛽):𝐈𝐧𝐩𝐮𝐭. A generating set 𝑆 for a group 𝐺 and a point 𝛽.𝐎𝐮𝐭𝐩𝐮𝐭. The orbit Δ=𝛽𝐺, the transversal 𝑇, and a generating set 𝑆′ for the stabilizer 𝐺𝛽.𝐌𝐞𝐭𝐡𝐨𝐝.1Δ←[𝛽]2𝑇[𝛽]←𝑒3𝑆′←[𝑒]4𝐟𝐨𝐫 𝛿∈Δ5𝐟𝐨𝐫 𝑠∈𝑆6𝛾←𝛿𝑠7𝐢𝐟 𝛾∉Δ 𝐭𝐡𝐞𝐧8append 𝛾 to Δ9𝑇[𝛾]←𝑇[𝛿]⋅𝑠10𝐞𝐥𝐬𝐞11append 𝑇[𝛿]⋅𝑠⋅𝑇[𝛾]−1 to 𝑆′12𝐞𝐧𝐝 𝐢𝐟13𝐞𝐧𝐝 𝐟𝐨𝐫14𝐞𝐧𝐝 𝐟𝐨𝐫15𝐫𝐞𝐭𝐮𝐫𝐧 Δ,𝑇,𝑆′Algorithm OrbitTransversalStabilizer(S,β):Input. A generating set S for a group G and a point β.Output. The orbit Δ=βG, the transversal T, and a generating set S′ for the stabilizer Gβ.Method.1Δ←[β]2T[β]←e3S′←[e]4for δ∈Δ5for s∈S6γ←δs7if γ∉Δ then8append γ to Δ9T[γ]←T[δ]⋅s10else11append T[δ]⋅s⋅T[γ]−1 to S′12end if13end for14end for15return Δ,T,S′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

伪代码中，对于每对 (𝛿,𝑠)(δ,s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只有轨道中不产生新的元素时，𝑡𝛿𝑠𝑡−1𝛿𝑠tδstδs−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 才是新的 Schreier 生成元；否则，它就是恒等变换 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因而，算法中实际生成的 Schreier 生成元（包括最初的恒等变换）最多只有

|𝑆||𝑇|−(|𝑇|−1)=|𝑆|(|𝑇|−1)+1|S||T|−(|T|−1)=|S|(|T|−1)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

个．对于一般的情形，这个上界是紧的．5但是，对于实际要处理的有限群，这个上界相当地宽松：这些新得到的 Schreier 生成元大多数并都是之前得到的生成元的重复，或者可以由之前的生成元复合而成．

因为 Schreier–Sims 算法的基本流程可以实现为递归地调用上述计算轨道和稳定化子的算法，所以其实此时就已经得到了 Schreier–Sims 算法的一种朴素实现．但是，如果不加以筛选，Schreier 生成元的规模的增长速度是指数级的：反复应用 𝑂(|𝑆𝑖|) =𝑂(|𝑆𝑖−1||𝑇𝑖|)O(|Si|)=O(|Si−1||Ti|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知，最内层的稳定化子的生成集的规模将达到 𝑂(|𝑆||𝐺|)O(|S||G|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这显然低效得荒诞，因为最内层的稳定化子是 {𝑒}{e}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Sims 的工作提供了限制 Schreier 生成元的规模的增长速度的方法，它能够保证最终得到的强生成集 ¯𝑆S¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小是 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．这样就可以在多项式时间内计算基和强生成集．

## Schreier–Sims 算法

为解决上述问题，本节讨论 Schreier–Sims 算法的一种增量实现，它得到的强生成集的大小是 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

### 筛选

Schreier–Sims 算法对上述朴素算法的核心优化十分简明：它要求在向稳定化子的生成集添加任何 Schreier 生成元之前，都首先需要经过 **筛选** （sifting）．所谓筛选，就是首先判定新的 Schreier 生成元是否已经存在于已有的生成元生成的子群中，然后只添加那些尚不存在的生成元．为此，只需要使用前文的成员判定算法 MembershipTest(𝐶,ℎ)MembershipTest(C,h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

但是，能够这样做的前提是，基于当前群的已经产生了的 Schreier 生成元，早就构建好了它们生成的群的稳定化子链（或基和强生成集）．这意味着，每次向稳定化子的生成集中添加一个新的 Schreier 生成元，都需要动态地维护内层的稳定化子链，以用于之后的筛选．但是，当前层每插入一个生成元，可能会产生多个 Schreier 生成元，也就可能会多次更新内层结构；而内层结构的每次更新，都可能会引发更内层结构的多次更新．

似乎之前提到的指数级爆炸的问题依然存在．其实不然．因为提前做好了筛选，只有待添加的生成元真的会引发某一层结构的扩大的时候，该层结构才会更新．这说明，单层结构更新的次数实际上等于该层结构存储的群严格增长的次数．但是，大小为 |𝐺||G|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的群至多有长度为 log⁡|𝐺|log⁡|G|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子群链；因为 Lagrange 定理保证，子群链长度每增加一，群的大小至少要翻倍．这就说明，单层结构至多只会更新 log⁡|𝐺|log⁡|G|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，因而最后得到的强生成集 ¯𝑆S¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小就是 |𝐵|log⁡|𝐺||B|log⁡|G|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

这个估计还可以进一步改进．因为此处出现的群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已知是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次对称群 𝑆𝑛Sn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子群，所以 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子群链长度不会超过 𝑆𝑛Sn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子群链长度．可以证明6，𝑆𝑛Sn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的严格递增子群链长度不会超过 3𝑛/23n/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这说明，单层结构更新的次数其实是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．显然，基的大小也不超过 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．故而，最后得到的强生成集 ¯𝑆S¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小就是 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

此处提到的筛选方法是 Sims 提出的，也称为 Sims 筛（Sims filter）．还有一种更为复杂的筛选方法，是由 Jerrum 提出的，也称为 [Jerrum 筛](https://groupprops.subwiki.org/w/index.php?title=Jerrum%27s_filter)（Jerrum filter），它能够保证得到的强生成集的大小是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．有兴趣的读者可以自行学习．

对于筛选过程，有一个小优化是，在 MembershipTest(𝐶,ℎ)MembershipTest(C,h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的实现中，并不输出布尔值，而是输出最后得到的「筛渣」7ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即用 𝐫𝐞𝐭𝐮𝐫𝐧 ℎreturn h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代替伪代码中的第 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和第 1414![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行）．如果「筛渣」ℎ ≠𝑒h≠e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就说明成员判定失败，此时可以直接将「筛渣」ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而不是原来的 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 添加到当前层．此处的「筛渣」ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已经除去了若干个陪集代表元的因子，因而移动了更少的元素，所以会减少局部的计算量．这个优化对于整体的复杂度没有任何影响．

### 过程

现在可以描述 Schreier–Sims 算法的具体过程：首先，初始化一个空结构 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用于存储群的稳定化子链．然后，逐个向结构 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中添加生成集 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的生成元，最后得到的结构 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是群 ⟨𝑆⟩⟨S⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的稳定化子链．伪代码如下：

𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 SchreierSims(𝑆):𝐈𝐧𝐩𝐮𝐭. A generating set 𝑆 for a group 𝐺.𝐎𝐮𝐭𝐩𝐮𝐭. The stabilizer chain 𝐶 for the group 𝐺.𝐌𝐞𝐭𝐡𝐨𝐝.1𝐶←[]2𝐟𝐨𝐫 𝑠∈𝑆3𝐶←Extend(𝐶,𝑠)4𝐞𝐧𝐝 𝐟𝐨𝐫5𝐫𝐞𝐭𝐮𝐫𝐧 𝐶Algorithm SchreierSims(S):Input. A generating set S for a group G.Output. The stabilizer chain C for the group G.Method.1C←[]2for s∈S3C←Extend(C,s)4end for5return C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

算法的核心在于向当前的 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中添加新的生成元 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这一步，即子程序 Extend(𝐶,𝑠)Extend(C,s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．正如前文所述，添加置换 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之前和之后，都需要保证 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是稳定化子链．这样，在添加置换 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之前，可以首先做筛选．如果发现 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不在已有的群中，就 **增量地** 计算轨道、陪集代表元和 Schreier 生成元．此处的「增量」的含义是，已经计算过的，不要重复计算．这样才能保证正确的复杂度．

考虑如何将 OrbitTransversalStabilizer(𝑆,𝛽)OrbitTransversalStabilizer(S,β)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 改造为增量版本．算法搜索的状态空间是 Δ ×𝑆Δ×S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在添加新的生成元 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之后，状态空间将变成 Δ′ ×(𝑆∪{𝑠})Δ′×(S∪{s})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．两者的差集就是

(Δ×{𝑠})∪((Δ′∖Δ)×(𝑆∪{𝑠})).(Δ×{s})∪((Δ′∖Δ)×(S∪{s})).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这意味着，当加入新的生成元 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候，首先需要计算新的生成元 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与旧的轨道和相应的陪集代表元的组合；如果在这个过程中还得到了新的轨道的元素，就再考虑这些元素与所有生成元（无论新旧）的组合；过程重复到轨道不再延长为止．

向结构 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中添加置换 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的伪代码如下：

𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 Extend(𝐶,𝑔):𝐈𝐧𝐩𝐮𝐭. A stabilizer chain 𝐶 for the group generated by 𝑆 and apermutation 𝑔.𝐎𝐮𝐭𝐩𝐮𝐭. A stabilizer chain 𝐶 for the group generated by 𝑆∪{𝑔}.𝐌𝐞𝐭𝐡𝐨𝐝.1𝐢𝐟 MembershipTest(𝐶,𝑔) is passed 𝐭𝐡𝐞𝐧2𝐫𝐞𝐭𝐮𝐫𝐧 𝐶3𝐞𝐧𝐝 𝐢𝐟4𝐢𝐟 𝐶 is empty 𝐭𝐡𝐞𝐧5𝛽←an element moved by 𝑔6𝐶.𝑜𝑟𝑏𝑖𝑡[0]←𝛽7𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛽]←𝑒8𝐞𝐧𝐝 𝐢𝐟9append 𝑔 to 𝐶.𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟𝑠10Δ←𝐶.𝑜𝑟𝑏𝑖𝑡11𝐟𝐨𝐫 𝛿∈Δ12𝛾←𝛿𝑔13𝐢𝐟 𝛾∉𝐶.𝑜𝑟𝑏𝑖𝑡 𝐭𝐡𝐞𝐧14append 𝛾 to 𝐶.𝑜𝑟𝑏𝑖𝑡15𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛾]←𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛿]⋅𝑔16𝐞𝐥𝐬𝐞17𝑠′←𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛿]⋅𝑔⋅𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛾]−118𝐶.𝑛𝑒𝑥𝑡←Extend(𝐶.𝑛𝑒𝑥𝑡,𝑠′)19𝐞𝐧𝐝 𝐢𝐟20𝐞𝐧𝐝 𝐟𝐨𝐫21𝐟𝐨𝐫 𝛿∈𝐶.𝑜𝑟𝑏𝑖𝑡∖Δ22𝐟𝐨𝐫 𝑠∈𝐶.𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟𝑠23𝛾←𝛿𝑠24𝐢𝐟 𝛾∉𝐶.𝑜𝑟𝑏𝑖𝑡 𝐭𝐡𝐞𝐧25append 𝛾 to 𝐶.𝑜𝑟𝑏𝑖𝑡26𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛾]←𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛿]⋅𝑠27𝐞𝐥𝐬𝐞28𝑠′←𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛿]⋅𝑠⋅𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛾]−129Extend(𝐶.𝑛𝑒𝑥𝑡,𝑠′)30𝐞𝐧𝐝 𝐢𝐟31𝐞𝐧𝐝 𝐟𝐨𝐫32𝐞𝐧𝐝 𝐟𝐨𝐫33𝐫𝐞𝐭𝐮𝐫𝐧 𝐶Algorithm Extend(C,g):Input. A stabilizer chain C for the group generated by S and apermutation g.Output. A stabilizer chain C for the group generated by S∪{g}.Method.1if MembershipTest(C,g) is passed then2return C3end if4if C is empty then5β←an element moved by g6C.orbit[0]←β7C.transversal[β]←e8end if9append g to C.generators10Δ←C.orbit11for δ∈Δ12γ←δg13if γ∉C.orbit then14append γ to C.orbit15C.transversal[γ]←C.transversal[δ]⋅g16else17s′←C.transversal[δ]⋅g⋅C.transversal[γ]−118C.next←Extend(C.next,s′)19end if20end for21for δ∈C.orbit∖Δ22for s∈C.generators23γ←δs24if γ∉C.orbit then25append γ to C.orbit26C.transversal[γ]←C.transversal[δ]⋅s27else28s′←C.transversal[δ]⋅s⋅C.transversal[γ]−129Extend(C.next,s′)30end if31end for32end for33return C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样就得到了完整的 Schreier–Sims 算法．

### 另一种实现

上述的实现已经是正确的，但是 12 ∼1912∼19![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行和 23 ∼3023∼30![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行略显重复．基于此，Knuth 在论文中提出了一种递归实现，更为简明．他的做法是，将这个重复的部分视作是对陪集剩余系（和轨道）的更新．每次更新陪集剩余系都要和所有的生成元组合，根据是否产生了新的陪集代表元，决定是递归地调用自身还是添加生成元的程序．伪代码如下：

𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 Extend(𝐶,𝑔):𝐈𝐧𝐩𝐮𝐭. A stabilizer chain 𝐶 for the group generated by 𝑆 and apermutation 𝑔.𝐎𝐮𝐭𝐩𝐮𝐭. A stabilizer chain 𝐶 for the group generated by 𝑆∪{𝑔}.𝐌𝐞𝐭𝐡𝐨𝐝.1𝐢𝐟 MembershipTest(𝐶,𝑔) is passed 𝐭𝐡𝐞𝐧2𝐫𝐞𝐭𝐮𝐫𝐧 𝐶3𝐞𝐧𝐝 𝐢𝐟4𝐢𝐟 𝐶 is empty 𝐭𝐡𝐞𝐧5𝛽←an element moved by 𝑔6𝐶.𝑜𝑟𝑏𝑖𝑡[0]←𝛽7𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛽]←𝑒8𝐞𝐧𝐝 𝐢𝐟9append 𝑔 to 𝐶.𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟𝑠10𝐟𝐨𝐫 𝑡∈𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙11ExtendTranserversal(𝐶,𝑡⋅𝑔)12𝐞𝐧𝐝 𝐟𝐨𝐫13𝐫𝐞𝐭𝐮𝐫𝐧 𝐶𝐒𝐮𝐛-𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 ExtendTranserversal(𝐶,𝑡):𝐌𝐞𝐭𝐡𝐨𝐝.1𝛽←𝐶.𝑜𝑟𝑏𝑖𝑡[0]2𝛾←𝛽𝑡3𝐢𝐟 𝛾∉𝐶.𝑜𝑟𝑏𝑖𝑡 𝐭𝐡𝐞𝐧4append 𝛾 to 𝐶.𝑜𝑟𝑏𝑖𝑡5𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛾]←𝑡6𝐟𝐨𝐫 𝑠∈𝐶.𝑔𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟𝑠7ExtendTranserversal(𝐶,𝑡⋅𝑠)8𝐞𝐧𝐝 𝐟𝐨𝐫9𝐞𝐥𝐬𝐞10𝑠′←𝑡⋅𝐶.𝑡𝑟𝑎𝑛𝑠𝑣𝑒𝑟𝑠𝑎𝑙[𝛾]−111Extend(𝐶.𝑛𝑒𝑥𝑡,𝑠′)12𝐞𝐧𝐝 𝐢𝐟Algorithm Extend(C,g):Input. A stabilizer chain C for the group generated by S and apermutation g.Output. A stabilizer chain C for the group generated by S∪{g}.Method.1if MembershipTest(C,g) is passed then2return C3end if4if C is empty then5β←an element moved by g6C.orbit[0]←β7C.transversal[β]←e8end if9append g to C.generators10for t∈C.transversal11ExtendTranserversal(C,t⋅g)12end for13return CSub-Algorithm ExtendTranserversal(C,t):Method.1β←C.orbit[0]2γ←βt3if γ∉C.orbit then4append γ to C.orbit5C.transversal[γ]←t6for s∈C.generators7ExtendTranserversal(C,t⋅s)8end for9else10s′←t⋅C.transversal[γ]−111Extend(C.next,s′)12end if![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将此处的伪代码和上节的相比，就可以知道它是正确的．而且，两者复杂度并无差异．

### 复杂度

为了分析 Schreier–Sims 算法的复杂度，需要一些记号．设置换的长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，生成集的大小 |𝑆||S|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．得到的（无冗余）基的长度记为 |𝐵||B|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而且，最后得到的自外向内第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的稳定化子 𝐺𝑖Gi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，生成元的数目记为 |𝑆𝑖−1||Si−1|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，陪集代表系的大小（或轨道的长度）记为 |𝑇𝑖||Ti|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．下面分析利用上述 Schreier–Sims 算法的增量实现所需要的时间复杂度．算法主要分为两部分：筛选，以及对轨道、陪集代表系和 Schreider 生成元的计算．

最初输入的生成元和算法中得到的 Schreider 生成元都需要进行筛选，因而筛选过程执行的总次数是 𝑂(∑|𝐵|𝑖=1|𝑆𝑖−1||𝑇𝑖| +|𝑆|)O(∑i=1|B||Si−1||Ti|+|S|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．单次筛选需要与 𝑂(|𝐵|)O(|B|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个陪集代表元计算置换乘积．设计算与单个陪集代表元的乘积的时间是 𝜏τ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．直接存储陪集代表元时，𝜏 ∈𝑂(𝑛)τ∈O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；而用 Schreier 树存储陪集代表元时，𝜏 ∈𝑂(𝑛2)τ∈O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．执行筛选过程的时间复杂度总共为 𝑂(𝜏|𝐵|∑|𝐵|𝑖=1|𝑆𝑖−1||𝑇𝑖| +𝜏|𝐵||𝑆|)O(τ|B|∑i=1|B||Si−1||Ti|+τ|B||S|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于轨道等信息的计算，因为是增量实现，状态空间中的每对 (𝛿,𝑠) ∈Δ𝑖 ×𝑆𝑖−1(δ,s)∈Δi×Si−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都只计算了至多一次．对于轨道和陪集代表系的计算，根据存储方式不同，单次计算陪集代表元的时间复杂度可能是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的或是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．但是，无论如何，这都不超过计算 Schreider 生成元的复杂度．直接存储时，它是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的；使用 Schreier 树时，它是 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．与筛选过程的总时间复杂度比较，会发现计算这些信息的时间复杂度都不会超过筛选需要的时间复杂度．所以，Schreier–Sims 算法的时间复杂度就是上一段得到的 𝑂(𝜏|𝐵|∑|𝐵|𝑖=1|𝑆𝑖−1||𝑇𝑖| +𝜏|𝐵||𝑆|)O(τ|B|∑i=1|B||Si−1||Ti|+τ|B||S|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

至于空间复杂度，算法最后得到的数据结构中存储了 𝑂(∑|𝐵|𝑖=1|𝑆𝑖−1|)O(∑i=1|B||Si−1|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个生成元和 𝑂(∑|𝐵|𝑖=1|𝑇𝑖|)O(∑i=1|B||Ti|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个陪集代表元．如果使用直接存储，生成元和陪集代表元都需要 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的空间；如果使用 Schreiner 树，生成元需要 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的空间，而陪集代表元只需要 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的空间．

前文已经说明，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次对称群中严格递增子群链的长度是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，这对 |𝐵||B|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 |𝑆𝑖||Si|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都适用．因而，使用直接存储陪集代表系的方式实现的 Schreier–Sims 算法，时间复杂度是 𝑂(𝑛5 +𝑚𝑛2)O(n5+mn2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，空间复杂度是 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．当然对于 log⁡|𝐺| ∈𝑂(𝑛)log⁡|G|∈O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，一个更好的估计是时间复杂度8 𝑂(𝑛2log3⁡|𝐺| +𝑚𝑛log⁡|𝐺|)O(n2log3⁡|G|+mnlog⁡|G|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和空间复杂度 𝑂(𝑛2log⁡|𝐺|)O(n2log⁡|G|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于随机的生成集的情形，实际测试发现算法的复杂度明显低于 Θ(𝑛5)Θ(n5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而大致是 Θ(𝑛4)Θ(n4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

虽然相较于直接存储，用 Schreiner 树会在时间复杂度中引入额外的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的指数，但对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 很大，但是群本身远小于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次对称群的情形，它的空间复杂度是 𝑂(𝑛log2⁡|𝐺|)O(nlog2⁡|G|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，远小于直接存储的 𝑂(𝑛2log⁡|𝐺|)O(n2log⁡|G|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是在算法竞赛中，很难遇到这样使用 Schreiner 树存储更优的情形．

### 参考实现

此处提供一个 Schreier–Sims 算法的参考实现．因为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 规模较小，实现中直接指定基 𝐵 ={𝑛,𝑛 −1,⋯,1}B={n,n−1,⋯,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而不是通过算法选择它．这样做的好处是，自内向外第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层（不计空结构体）的群中的置换只就会改变前 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素，方便后续计算．代码中的另一项优化是，在存储陪集代表元的时候，存储的实际上是它的逆置换，这简化了置换的运算．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 ``` |  ```text #include <iostream> #include <vector> // A permutation. class Permutation { std :: vector < int > perm ; void shrink () { int m = perm . size (); for (; m && perm [ m \- 1 ] == m \- 1 ; \-- m ); perm . resize ( m ); } public : Permutation () {} Permutation ( const std :: vector < int >& vec ) : perm ( vec ) { shrink (); } int operator []( int i ) const { return i < perm . size () ? perm [ i ] : i ; } bool empty () const { return perm . empty (); } // First LHS then RHS. Permutation operator * ( const Permutation & rhs ) const { Permutation res ; res . perm . resize ( std :: max ( perm . size (), rhs . perm . size ())); for ( int i = 0 ; i < res . perm . size (); ++ i ) { res . perm [ i ] = rhs [( * this )[ i ]]; } res . shrink (); return res ; } // First LHS^{-1} then RHS. Permutation operator / ( const Permutation & rhs ) const { Permutation res ; res . perm . resize ( std :: max ( perm . size (), rhs . perm . size ())); for ( int i = 0 ; i < res . perm . size (); ++ i ) { res . perm [( * this )[ i ]] = rhs [ i ]; } res . shrink (); return res ; } // Inverse. Permutation inv () const { Permutation res ; res . perm . resize ( perm . size ()); for ( int i = 0 ; i < res . perm . size (); ++ i ) { res . perm [( * this )[ i ]] = i ; } return res ; } }; // A stabilizer chain (a.k.a., BSGS) for a group. class PermutationGroup { size_t n , k ; std :: vector < bool > orbit ; // Orbit of the n-th point. std :: vector < Permutation > generators ; // Generators. std :: vector < Permutation > transversal ; // Inverse of coset representatives. PermutationGroup * next ; // Stabilizer. // Sift a permutation. void sift ( Permutation & h ) const { if ( ! n ) return ; int i = h [ n \- 1 ]; if ( ! orbit [ i ]) return ; h = h * transversal [ i ]; next -> sift ( h ); } // Add one more element into the transversal. void extend_transversal ( Permutation t ) { int i = t [ n \- 1 ]; if ( ! orbit [ i ]) { ++ k ; orbit [ i ] = true ; transversal [ i ] = t . inv (); for ( const auto & s : generators ) { extend_transversal ( t * s ); } } else { next -> extend ( t * transversal [ i ]); } } public : PermutationGroup ( int n ) : n ( n ), k ( 1 ), orbit ( n ), transversal ( n ), next ( nullptr ) { if ( ! n ) return ; // Initialize the current layer. orbit [ n \- 1 ] = true ; next = new PermutationGroup ( n \- 1 ); } // Destructor. ~ PermutationGroup () { if ( next ) delete next ; } // Add one more permutation into the group. void extend ( Permutation g ) { sift ( g ); if ( g . empty ()) return ; generators . emplace_back ( g ); for ( int i = 0 ; i < n ; ++ i ) { if ( orbit [ i ]) { extend_transversal ( transversal [ i ] / g ); } } } // Check whether a permutation belongs to the group. bool membership_test ( Permutation h ) const { sift ( h ); return h . empty (); } // Return the size of the group. long long size () const { return n ? next -> size () * k : 1L L ; } }; int main () { int n , m ; std :: cin >> n >> m ; PermutationGroup group ( n ); // Read permutations and insert them to the group. std :: vector < int > vec ( n ); for (; m ; \-- m ) { for ( int & x : vec ) { std :: cin >> x ; \-- x ; // Index starting at 0. } group . extend ( Permutation ( vec )); } // Output the size of the group. std :: cout << group . size (); return 0 ; } ```   
---|---  
  
## 习题

  * [LOJ 177. 生成子群阶数](https://loj.ac/p/177)
  * [[WC2017] 棋盘](https://uoj.ac/problem/287)
  * [Permutations](https://codeforces.com/gym/421334/problem/A)
  * [[Grand Prix of Yekaterinburg 2015] Problem H. Heimdall](https://disk.yandex.com/i/OfEXXcu-anMHuw)

## 参考资料与注释

  * [Schreier–Sims algorithm - Wikipedia](https://en.wikipedia.org/wiki/Schreier%E2%80%93Sims_algorithm)
  * [Sims, Charles C, Computational methods in the study of permutation groups, Computational Problems in Abstract Algebra, pp. 169–183, Pergamon, Oxford, 1970.](https://www.sciencedirect.com/science/article/pii/B9780080129754500205)
  * [Knuth, Donald E. Efficient representation of perm groups, Combinatorica 11 (1991), no. 1, 33–43.](https://arxiv.org/abs/math/9201304)
  * [Ákos Seress, Permutation Group Algorithms, Cambridge University Press](https://www.cambridge.org/core/books/permutation-group-algorithms/199629665EC545A10BCB99FFE6AAFD25)
  * [Alexander Hulpke's Notes on Computational Group Theory](https://www.math.colostate.edu/%7Ehulpke/CGT/cgtnotes.pdf)
  * [Derek Holt's Slides on The Schreier–Sims algorithm for finite permutation groups](https://blogs.cs.st-andrews.ac.uk/codima/files/2015/11/CoDiMa2015_Holt.pdf)
  * [Martin Jaggi, Implementations of 3 Types of the Schreier–Sims Algorithm, MAS334 - Mathematics Computing Project, 2005](https://www.m8j.net/data/List/Files-118/Documentation.pdf)
  * [Henrik Bäärnhielm. The Schreier–Sims algorithm for matrix groups](https://henrik.baarnhielm.net/schreiersims.pdf)

* * *

  1. Knuth 的论文是在 1991 年发表的，但是他的改进在 1981 年就通过会议广泛地宣传．论文是基于他的会议讲稿写作的． ↩

  2. 不要与 Monto Carlo 方法混淆．此处的 Monte Carlo 算法是指出错概率恒定且任意小的随机算法． ↩

  3. 这个问题以及本节的算法都并不需要假设所讨论的群作用是置换作用，因而可以应用于更广泛的场景．比如，如果将这些算法应用于共轭作用，同样可以求得轨道（共轭类）、陪集代表系和稳定化子（中心化子）． ↩

  4. 因为这个树形结构可以通过一列指向父节点的指针来实现，所以也称作 Schreier 向量． ↩

  5. [Nielsen–Schreier 定理](https://en.wikipedia.org/wiki/Nielsen%E2%80%93Schreier_theorem) 说明，对于由 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个生成元生成的 [自由群](https://en.wikipedia.org/wiki/Free_group)，它的指数为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子群是由 𝑘(𝑛 −1) +1k(n−1)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个生成元生成的自由群． ↩

  6. 参见 [Cameron, P. J., Solomon, R., & Turull, A. (1989). Chains of subgroups in symmetric groups. Journal of algebra, 127(2), 340-352.](https://www.sciencedirect.com/science/article/pii/0021869389902561) ↩

  7. 这并不是什么严格的术语，在不同的英文文献中可能称作 siftee 或者 sifted element． ↩

  8. Knuth 的论文给出的上界还要再少一个对数因子，这需要对群的稳定化子链的基础轨道长度做更仔细的估计． ↩

  9. 这个 𝑒 ∈𝑇e∈T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的条件对于 Schreier 引理的成立不是必要的． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/algebra/schreier-sims.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/algebra/schreier-sims.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [isdanni](https://github.com/isdanni), [ksyx](https://github.com/ksyx), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
