# 条件概率与独立性 - OI Wiki

- Source: https://oi-wiki.org/math/probability/conditional-probability/

# 条件概率与独立性

## 概述

当某事件已经发生时，一些随机事件的概率会因为已知信息的增加发生变化．例如在手游抽卡时，我们可能会认为单次抽卡出六星与不出六星是等概率的，但随着我们连抽 5050![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 发一个六星都没有，再固执地认为「出六星与不出六星等概率」就显得不是那么明智．

总之，研究在某些已知条件下事件发生的概率是必要的．

## 条件概率

### 定义

若已知事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 发生，在此条件下事件 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 发生的概率称为 **条件概率** ，记作 𝑃(𝐵|𝐴)P(B|A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在概率空间 (Ω,F,𝑃)(Ω,F,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，若事件 𝐴 ∈FA∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑃(𝐴) >0P(A)>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则条件概率 𝑃( ⋅|𝐴)P(⋅|A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义为

𝑃(𝐵|𝐴)=𝑃(𝐴𝐵)𝑃(𝐴)∀𝐵∈FP(B|A)=P(AB)P(A)∀B∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以验证根据上式定义出的 𝑃( ⋅|𝐴)P(⋅|A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 (Ω,F)(Ω,F)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的概率函数．

根据条件概率的定义可以直接推出下面两个等式：

  * **概率乘法公式** ：在概率空间 (Ω,F,𝑃)(Ω,F,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，若 𝑃(𝐴) >0P(A)>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对任意事件 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有

𝑃(𝐴𝐵)=𝑃(𝐴)𝑃(𝐵|𝐴)P(AB)=P(A)P(B|A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * **全概率公式** ：在概率空间 (Ω,F,𝑃)(Ω,F,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，若一组事件 𝐴1,⋯,𝐴𝑛A1,⋯,An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两不交且和为 ΩΩ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对任意事件 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有

𝑃(𝐵)=𝑛∑𝑖=1𝑃(𝐴𝑖)𝑃(𝐵|𝐴𝑖)P(B)=∑i=1nP(Ai)P(B|Ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### Bayes 公式

一般来说，设可能导致事件 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 发生的原因为 𝐴1,𝐴2,⋯,𝐴𝑛A1,A2,⋯,An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则在 𝑃(𝐴𝑖)P(Ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑃(𝐵|𝐴𝑖)P(B|Ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已知时可以通过全概率公式计算事件 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 发生的概率．但在很多情况下，我们需要根据「事件 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 发生」这一结果反推其各个原因事件的发生概率．于是有

𝑃(𝐴𝑖|𝐵)=𝑃(𝐴𝑖𝐵)𝑃(𝐵)=𝑃(𝐴𝑖)𝑃(𝐵|𝐴𝑖)∑𝑛𝑗=1𝑃(𝐴𝑗)𝑃(𝐵|𝐴𝑗)P(Ai|B)=P(AiB)P(B)=P(Ai)P(B|Ai)∑j=1nP(Aj)P(B|Aj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上式即 Bayes 公式．

## 事件的独立性

在研究条件概率的过程中，可能会出现 𝑃(𝐵|𝐴) =𝑃(𝐵)P(B|A)=P(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况．从直观上讲就是事件 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否发生并不会告诉我们关于事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的任何信息，即事件 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)「无关」．于是我们就有了下面的定义

### 定义

若同一概率空间中的事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足

𝑃(𝐴𝐵)=𝑃(𝐴)𝑃(𝐵)P(AB)=P(A)P(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则称 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **独立** ．对于多个事件 𝐴1,𝐴2,⋯,𝐴𝑛A1,A2,⋯,An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们称其独立，当且仅当对任意一组事件 {𝐴𝑖𝑘 :1 ≤𝑖1 <𝑖2 <⋯ <𝑖𝑘 ≤𝑛}{Aik:1≤i1<i2<⋯<ik≤n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有

𝑃(𝐴𝑖1𝐴𝑖2⋯𝐴𝑖𝑟)=𝑟∏𝑘=1𝑃(𝐴𝑖𝑘)P(Ai1Ai2⋯Air)=∏k=1rP(Aik)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 多个事件的独立性

对于多个事件，一般不能从两两独立推出这些事件独立．考虑以下反例：

有一个正四面体骰子，其中三面被分别涂成红色、绿色、蓝色，另一面则三色皆有．现在扔一次该骰子，令事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别表示与桌面接触的一面包含红色、绿色、蓝色．

不难计算 𝑃(𝐴) =𝑃(𝐵) =𝑃(𝐶) =12P(A)=P(B)=P(C)=12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 𝑃(𝐴𝐵) =𝑃(𝐵𝐶) =𝑃(𝐶𝐴) =𝑃(𝐴𝐵𝐶) =14P(AB)=P(BC)=P(CA)=P(ABC)=14![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

显然 𝐴,𝐵,𝐶A,B,C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两独立，但由于 𝑃(𝐴𝐵𝐶) ≠𝑃(𝐴)𝑃(𝐵)𝑃(𝐶)P(ABC)≠P(A)P(B)P(C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故 𝐴,𝐵,𝐶A,B,C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不独立．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/probability/conditional-probability.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/probability/conditional-probability.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [MegaOwIer](https://github.com/MegaOwIer), [Tiphereth-A](https://github.com/Tiphereth-A), [aofall](https://github.com/aofall), [CCXXXI](https://github.com/CCXXXI), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Marcythm](https://github.com/Marcythm), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu), [yusancky](https://github.com/yusancky)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
