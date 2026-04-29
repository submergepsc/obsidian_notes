# 随机变量的数字特征 - OI Wiki

- Source: https://oi-wiki.org/math/probability/exp-var/

# 随机变量的数字特征

本文将介绍随机变量的期望、方差等数字特征．

## 期望

### 定义

#### 离散型随机变量

设离散型随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率分布为 𝑝𝑖 =𝑃{𝑋 =𝑥𝑖}pi=P{X=xi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若和式

∑𝑥𝑖𝑝𝑖∑xipi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

绝对收敛，则称其值为 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **期望** ，记作 𝐸𝑋EX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 连续型随机变量

设连续型随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的密度函数为 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若积分

∫ℝ𝑥𝑓(𝑥)d𝑥∫Rxf(x)dx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

绝对收敛，则称其值为 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **期望** ，记作 𝐸𝑋EX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 统一定义

设随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分布函数为 𝐹(𝑥)F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 [Stieltjes 积分](https://en.wikipedia.org/wiki/Riemann%E2%80%93Stieltjes_integral)

∫ℝ𝑥d𝐹(𝑥)∫RxdF(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

绝对收敛，则称其值为 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **期望** ，记作 𝐸𝑋EX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

期望不存在的例子

考虑有如下分布的离散型随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝑃{𝑋=(−1)𝑘2𝑘𝑘}=12𝑘,𝑘=1,2,⋯P{X=(−1)k2kk}=12k,k=1,2,⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

尽管和式 ∑𝑥𝑖𝑝𝑖∑xipi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 收敛于 −ln⁡2−ln⁡2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但由于其不是绝对收敛的，故 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望不存在．

再考虑有如下密度函数的连续型随机变量 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝑓(𝑦)=1𝜋⋅11+𝑦2,𝑦∈(−∞,+∞)f(y)=1π⋅11+y2,y∈(−∞,+∞)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

容易验证 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望也不存在．

### 期望的性质

#### 线性性

若随机变量 𝑋,𝑌X,Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望存在，则

  * 对任意实数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝐸(𝑎𝑋 +𝑏) =𝑎 ⋅𝐸𝑋 +𝑏E(aX+b)=a⋅EX+b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝐸(𝑋 +𝑌) =𝐸𝑋 +𝐸𝑌E(X+Y)=EX+EY![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 随机变量乘积的期望

若随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望存在且 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相互独立，则有

𝐸(𝑋𝑌)=𝐸𝑋⋅𝐸𝑌E(XY)=EX⋅EY![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意：上述性质中的独立性 **并非** 必要条件．

反例

考察随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 服从 [ −1,1][−1,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的均匀分布，𝑌 =𝑋2Y=X2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 期望与概率的转化

对于随机事件 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考虑其示性函数 𝐼𝐴IA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝐼𝐴(𝜔)={1,𝜔∈𝐴0,𝜔∉𝐴IA(ω)={1,ω∈A0,ω∉A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据定义可以求得其期望 𝐸𝐼𝐴 =𝑃(𝐴)EIA=P(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这一转化在实际应用中非常常见．

例子

假设对于一个长为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 𝑝𝑘pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以 1 −𝑝𝑘1−pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率取 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考虑如何求 𝑆 =∑𝑛𝑖=1𝑎𝑖S=∑i=1nai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望．

如果使用定义直接求，需要求出 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在每个可能取值处的概率，这个计算过程比较繁琐，这里不展开叙述．

另一方面，用 𝐼𝑘Ik![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示随机事件 𝑎𝑘 =𝑘ak=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的示性函数，则有

𝑆=𝑛∑𝑘=1𝑘⋅𝐼𝑘S=∑k=1nk⋅Ik![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而不难求出

𝐸𝑆=𝐸(𝑛∑𝑘=1𝑘⋅𝐼𝑘)=𝑛∑𝑘=1𝑘⋅𝐸[𝐼𝑘]=𝑛∑𝑘=1𝑘⋅𝑝𝑘ES=E(∑k=1nk⋅Ik)=∑k=1nk⋅E[Ik]=∑k=1nk⋅pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 条件分布与条件期望

我们之前研究过条件概率，类似的也可以提出所谓条件期望的概念．

### 定义

对于两个随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在已知 𝑌 =𝑦Y=y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的条件下 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率分布（密度函数）称之为 **条件概率分布（条件概率密度）** ，分别记作

𝑃(𝑋=𝑥𝑖|𝑌=𝑦)𝑓𝑋|𝑌(𝑥|𝑦)P(X=xi|Y=y)fX|Y(x|y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在此条件下，𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望称为 **条件期望** ，记作 𝐸[𝑋|𝑌 =𝑦]E[X|Y=y]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 条件期望的性质

条件期望的诸多性质可由条件概率推知，在此不做赘述．

值得一提的是 𝐸[𝑋|𝑌]E[X|Y]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一般是随机变量 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的函数，且这个函数通常不是线性的．但实际上有

𝐸[𝐸[𝑋|𝑌]]=𝐸𝑋E[E[X|Y]]=EX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上式称作 **全期望公式** ．

### 应用

[HDU 5984 Pocky](https://acm.hdu.edu.cn/showproblem.php?pid=5984)

有一根长为 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Pocky，每次随机折成两段．若右边一段的长度不大于 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则停止，否则对右边一段重复上述过程．求重复次数的期望．

题解

记 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示长度为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望次数．𝑥 ≤𝑑x≤d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形平凡．

当 𝑥 >𝑑x>d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，不妨设折断的位置距右端的长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则显然 𝑘 ∼𝑈[0,𝑥]k∼U[0,x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时期望的重复次数为

𝑔(𝑘)={1,𝑘≤𝑑1+𝑓(𝑘),𝑘>𝑑g(k)={1,k≤d1+f(k),k>d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由全期望公式可知

𝑓(𝑥)=𝐸𝑔(𝑘)=1+1𝑥⋅∫𝑥𝑑𝑓(𝑡)d𝑡f(x)=Eg(k)=1+1x⋅∫dxf(t)dt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

解上述积分方程并代入初值条件得

𝑓(𝑥)=1+ln⁡𝑥𝑑f(x)=1+ln⁡xd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 方差

### 定义

设随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的期望 𝐸𝑋EX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在且期望

𝐸(𝑋−𝐸𝑋)2E(X−EX)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也存在，则称上式的值为随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **方差** ，记作 𝐷𝑋DX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑉𝑎𝑟(𝑥)Var(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．方差的算术平方根称为 **标准差** ，记作 𝜎(𝑋) =√𝐷𝑋σ(X)=DX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 方差的性质

若随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方差存在，则

  * 对任意常数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 𝐷(𝑎𝑋 +𝑏) =𝑎2 ⋅𝐷𝑋D(aX+b)=a2⋅DX![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝐷𝑋 =𝐸(𝑋2) −(𝐸𝑋)2DX=E(X2)−(EX)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 协方差与相关系数

一般来说，等式 𝐷(𝑋 +𝑌) =𝐷𝑋 +𝐷𝑌D(X+Y)=DX+DY![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并不成立，我们自然会提出两个问题：

  * 𝐷(𝑋 +𝑌)D(X+Y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐷𝑋 +𝐷𝑌DX+DY![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间相差的部分到底是什么．
  * 𝐷(𝑋 +𝑌)D(X+Y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐷𝑋 +𝐷𝑌DX+DY![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在什么情况下相等．

对于第一个问题，我们引入协方差作为解答．

### 协方差的定义

对于随机变量 𝑋,𝑌X,Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称

𝐸((𝑋−𝐸𝑋)(𝑌−𝐸𝑌))E((X−EX)(Y−EY))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **协方差** ，记作 Cov⁡(𝑋,𝑌)Cov⁡(X,Y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 协方差的性质

对于随机变量 𝑋,𝑌,𝑍X,Y,Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

  * Cov⁡(𝑋,𝑌) =Cov⁡(𝑌,𝑋)Cov⁡(X,Y)=Cov⁡(Y,X)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 对任意常数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 Cov⁡(𝑎𝑋 +𝑏𝑌,𝑍) =𝑎 ⋅Cov⁡(𝑋,𝑍) +𝑏 ⋅Cov⁡(𝑌,𝑍)Cov⁡(aX+bY,Z)=a⋅Cov⁡(X,Z)+b⋅Cov⁡(Y,Z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

同时协方差与方差也有如下联系：

  * 𝐷𝑋 =Cov⁡(𝑋,𝑋)DX=Cov⁡(X,X)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝐷(𝑋 +𝑌) =𝐷𝑋 +2Cov⁡(𝑋,𝑌) +𝐷𝑌D(X+Y)=DX+2Cov⁡(X,Y)+DY![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

关于协方差

你可能会发现协方差的性质与向量内积的运算性质在形式上高度一致．

在泛函分析的视角下，对于给定的概率空间，其上的全体随机变量构成一个线性空间，而协方差是这个空间上的一个内积，标准差则是由该内积导出的范数．

对于刚才提出的第二个问题，不难看出 𝐷(𝑋 +𝑌) =𝐷𝑋 +𝐷𝑌D(X+Y)=DX+DY![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当 Cov⁡(𝑋,𝑌) =0Cov⁡(X,Y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．一个直观的必要条件是 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 独立，因为此时有

Cov⁡(𝑋,𝑌)=𝐸((𝑋−𝐸𝑋)(𝑌−𝐸𝑌))=𝐸(𝑋−𝐸𝑋)𝐸(𝑌−𝐸𝑌)=0Cov⁡(X,Y)=E((X−EX)(Y−EY))=E(X−EX)E(Y−EY)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但这个条件并不是充分的．为了描述满足 Cov⁡(𝑋,𝑌) =0Cov⁡(X,Y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的关系，我们引入相关系数

### 相关系数

对于随机变量 𝑋,𝑌X,Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称

Cov⁡(𝑋,𝑌)𝜎(𝑋)𝜎(𝑌)Cov⁡(X,Y)σ(X)σ(Y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **Pearson 相关系数** ，记作 𝜌𝑋,𝑌ρX,Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Pearson 相关系数描述了两个随机变量之间线性关联的紧密程度．|𝜌𝑋,𝑌||ρX,Y|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 越大，则 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的线性关联程度越强．不难证明 |𝜌𝑋,𝑌| ≤1|ρX,Y|≤1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 |𝜌𝑋,𝑌| =1|ρX,Y|=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仅可能出现在以下两种情况

  * 当存在实数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正实数 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑃(𝑋 =𝑎 +𝑏𝑌) =1P(X=a+bY)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有 𝜌𝑋,𝑌 =1ρX,Y=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 当存在实数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和负实数 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑃(𝑋 =𝑎 +𝑏𝑌) =1P(X=a+bY)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有 𝜌𝑋,𝑌 = −1ρX,Y=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当 𝜌𝑋,𝑌 =0ρX,Y=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时我们称随机变量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **不相关** ，此时 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间不存在线性关系．

「不相关」与「独立」

两随机变量不相关只是表明他们之间没有线性关联，并不代表没有其他形式的联系．

因此两随机变量 𝑋,𝑌X,Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不相关是他们相互独立的 **必要而不充分** 条件．

对于这一小节开头提到的第二个问题，我们给出结论：Cov⁡(𝑋,𝑌) =0Cov⁡(X,Y)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的充要条件就是 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的某一个以概率 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取常值，或 𝑋,𝑌X,Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不相关．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/probability/exp-var.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/probability/exp-var.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [MegaOwIer](https://github.com/MegaOwIer), [c-forrest](https://github.com/c-forrest), [HeRaNO](https://github.com/HeRaNO), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
