# 基本概念 - OI Wiki

- Source: https://oi-wiki.org/math/probability/basic-conception/

# 基本概念

## 概述

在研究具体的随机现象时我们通常着重关注以下要素：

  * 样本空间 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，指明随机现象所有可能出现的结果．
  * 事件域 FF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示我们所关心的所有事件．
  * 概率 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，描述每一个事件发生的可能性大小．

## 样本空间、随机事件

### 定义

一个随机现象中可能发生的不能再细分的结果被称为 **样本点** ．所有样本点的集合称为 **样本空间** ，通常用 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来表示．

一个 **随机事件** 是样本空间 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集，它由若干样本点构成，用大写字母 𝐴,𝐵,𝐶,⋯A,B,C,⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示．

对于一个随机现象的结果 𝜔ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一个随机事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们称事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **发生了** 当且仅当 𝜔 ∈𝐴ω∈A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

例如，掷一次骰子得到的点数是一个随机现象，其样本空间可以表示为 Ω ={1,2,3,4,5,6}Ω={1,2,3,4,5,6}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设随机事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为「获得的点数大于 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」，则 𝐴 ={5,6}A={5,6}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若某次掷骰子得到的点数 𝜔 =3ω=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由于 𝜔 ∉𝐴ω∉A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有发生．

### 事件的运算

由于我们将随机事件定义为了样本空间 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集，故我们可以将集合的运算（如交、并、补等）移植到随机事件上．记号与集合运算保持一致．

特别的，事件的并 𝐴 ∪𝐵A∪B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也可记作 𝐴 +𝐵A+B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，事件的交 𝐴 ∩𝐵A∩B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也可记作 𝐴𝐵AB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时也可分别称作 **和事件** 和 **积事件** ．

## 事件域

研究具体的随机现象时我们需要明确哪些事件是我们感兴趣的．根据随机事件的定义，显然有 F ⊂2ΩF⊂2Ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（记号 2Ω2Ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂集），但 F =2ΩF=2Ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 却不是必须的．这在样本空间 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有限时可能有些难以理解，毕竟 2Ω2Ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 尽管更大了但仍然有限．而当 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为无穷集时，2Ω2Ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的势变得更大，其中也难免会出现一些「性质不太好」且我们不关心的事件，这时为了兼顾这些事件而放弃一些性质就显得得不偿失了．

尽管 F =2ΩF=2Ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是必须的，这并不代表 2Ω2Ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的任一子集都能成为事件域．我们通常会对一些事件进行运算得到的结果事件的概率感兴趣，因此我们希望事件域 FF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足下列条件：

  * ∅ ∈F∅∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 若 𝐴 ∈FA∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则补事件 ¯𝐴 ∈FA¯∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 若有一列事件 𝐴𝑛 ∈F,𝑛 =1,2,3…An∈F,n=1,2,3…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 ⋃𝐴𝑛 ∈F⋃An∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

简言之，就是事件域 FF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对在补运算、和可数并下是封闭的，且包含元素 ∅∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

可以证明满足上述三个条件的事件域 FF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对可数交也是封闭的．

以掷骰子为例，当样本空间记为 Ω ={1,2,3,4,5,6}Ω={1,2,3,4,5,6}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，以下两个集合能够成为事件域：

  * F1 ={∅,Ω}F1={∅,Ω}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * F2 ={∅,{1,3,5},{2,4,6},Ω}F2={∅,{1,3,5},{2,4,6},Ω}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但以下两个集合则不能

  * F3 ={∅,{1},Ω}F3={∅,{1},Ω}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（对补不封闭）
  * F4 ={{1,3,5},{2,4,6}}F4={{1,3,5},{2,4,6}}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（不含有 ∅∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且对并不封闭）

## 概率

### 定义

#### 古典定义

在概率论早期实践中，由于涉及到的随机现象都比较简单，具体表现为样本空间 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是有限集，且直观上所有样本点是等可能出现的，因此人们便总结出了下述定义：

如果一个随机现象满足：

  * 只有有限个基本结果；
  * 每个基本结果出现的可能性是一样的；

那么对于每个事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义它的概率为

𝑃(𝐴)=#(𝐴)#(Ω)P(A)=#(A)#(Ω)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 #( ⋅)#(⋅)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示对随机事件（一个集合）大小的度量．

后来人们发现这一定义可以直接推广到 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无限的一部分情景中，于是就有了所谓 [几何概型](https://baike.baidu.com/item/%E5%87%A0%E4%BD%95%E6%A6%82%E5%9E%8B/4035773)．

#### 公理化定义

上述基于直观认识的定义在逻辑上有一个很大的漏洞：在定义「概率」这一概念时用到了「可能性」这一说法，产生了循环定义的问题．同时「等可能」在样本空间无限时会产生歧义，由此产生了包括 [Bertrand 悖论](https://baike.baidu.com/item/%E8%B4%9D%E7%89%B9%E6%9C%97%E6%82%96%E8%AE%BA/9241081) 在内的一系列问题．

经过不断探索，苏联数学家柯尔莫哥洛夫于 1933 年在他的《概率论基础》一书中第一次给出了概率的公理化定义：

概率函数 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个从事件域 FF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到闭区间 [0,1][0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的映射，且满足：

  * **规范性** ：事件 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率值为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑃(Ω) =1P(Ω)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * **可数可加性** ：若一列事件 𝐴1,𝐴2,⋯A1,A2,⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两不交，则 𝑃(⋃𝑖≥1𝐴𝑖) =∑𝑖≥1𝑃(𝐴𝑖)P(⋃i≥1Ai)=∑i≥1P(Ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 概率函数的性质

对于任意随机事件 𝐴,𝐵 ∈FA,B∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

  * **单调性** ：若 𝐴 ⊂𝐵A⊂B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有 𝑃(𝐴) ≤𝑃(𝐵)P(A)≤P(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * **容斥原理** ：𝑃(𝐴 +𝐵) =𝑃(𝐴) +𝑃(𝐵) −𝑃(𝐴𝐵)P(A+B)=P(A)+P(B)−P(AB)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑃(𝐴 −𝐵) =𝑃(𝐴) −𝑃(𝐴𝐵)P(A−B)=P(A)−P(AB)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这里 𝐴 −𝐵A−B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示差集．

## 概率空间

我们在一开始提到，研究具体的随机现象时我们通常关注样本空间 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、事件域 FF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以及概率函数 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们将三元组 (Ω,F,𝑃)(Ω,F,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为一个概率空间．

概率只有在确定的概率空间下讨论才有意义．我们前面提到的 Bertrand 悖论归根结底就是因对样本空间 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义不明确而产生的．

## 参考资料与注释

  * [概率论（数学分支）_百度百科](https://baike.baidu.com/item/概率论/829122)
  * [Probability - Wikipedia](https://en.wikipedia.org/wiki/Probability)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/probability/basic-conception.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/probability/basic-conception.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [MegaOwIer](https://github.com/MegaOwIer), [aofall](https://github.com/aofall), [billchenchina](https://github.com/billchenchina), [CCXXXI](https://github.com/CCXXXI), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Marcythm](https://github.com/Marcythm), [ouuan](https://github.com/ouuan), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
