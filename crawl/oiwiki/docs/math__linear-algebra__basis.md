# 线性基 - OI Wiki

- Source: https://oi-wiki.org/math/linear-algebra/basis/

# 线性基

回想高中数学立体几何中基向量的概念，我们可以在三维欧氏空间中找到一组基向量 𝒊i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝒋j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝒌k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，之后空间中任意一个向量都可以由这组基向量表示．换句话说，我们可以 **通过有限的基向量来描述无限的三维空间** ，这足以体现基向量的重要性．

三维欧氏空间是特殊的 [线性空间](../vector-space/)，三维欧氏空间的基向量在线性空间中就被推广为了线性基．

OI 中有关线性基的应用一般只涉及两类线性空间：𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维实线性空间 𝐑𝑛Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维 [布尔域](https://en.wikipedia.org/wiki/Boolean_domain) 线性空间 𝐙𝑛2Z2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们会在 应用 一节中详细介绍．若您不熟悉线性代数，则推荐从应用部分开始阅读．

以下会从一般的线性空间出发来介绍线性基，并给出线性基的常见性质．

前置知识：[线性空间](../vector-space/)．

线性基是线性空间的一组基，是研究线性空间的重要工具．

## 定义

称线性空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个极大线性无关组为 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组 **Hamel 基** 或 **线性基** ，简称 **基** ．

规定线性空间 {𝜃}{θ}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基为空集．

可以证明任意线性空间均存在线性基1，我们定义线性空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **维数** 为线性基的元素个数（或势），记作 dim⁡𝑉dim⁡V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 性质

  1. 对于有限维线性空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 设其维数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则：

     1. 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的任意 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个向量线性相关．

     2. 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的任意 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个线性无关的向量均为 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基．

     3. 若 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的任意向量均可被向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性表出，则其是 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个基．

证明

任取 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的一组基 𝑏1,𝑏2,…,𝑏𝑛b1,b2,…,bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 由已知条件，向量组 𝑏1,𝑏2,…,𝑏𝑛b1,b2,…,bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可被 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性表出，故

𝑛=rank⁡{𝑏1,𝑏2,…,𝑏𝑛}≤rank⁡{𝑎1,𝑎2,…,𝑎𝑛}≤𝑛n=rank⁡{b1,b2,…,bn}≤rank⁡{a1,a2,…,an}≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此 rank⁡{𝑎1,𝑎2,…,𝑎𝑛} =𝑛rank⁡{a1,a2,…,an}=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

     4. 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中任意线性无关向量组 𝑎1,𝑎2,…,𝑎𝑚a1,a2,…,am![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均可通过插入一些向量使得其变为 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个基．

  2. （子空间维数公式）令 𝑉1,𝑉2V1,V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有限维线性空间，且 𝑉1 +𝑉2V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉1 ∩𝑉2V1∩V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是有限维的，则 dim⁡𝑉1 +dim⁡𝑉2 =dim⁡(𝑉1 +𝑉2) +dim⁡(𝑉1 ∩𝑉2)dim⁡V1+dim⁡V2=dim⁡(V1+V2)+dim⁡(V1∩V2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明

设 dim⁡𝑉1 =𝑛1dim⁡V1=n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),dim⁡𝑉2 =𝑛2dim⁡V2=n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),dim⁡(𝑉1 ∩𝑉2) =𝑚dim⁡(V1∩V2)=m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

取 𝑉1 ∩𝑉2V1∩V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组基 𝑎1,𝑎2,…,𝑎𝑚a1,a2,…,am![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 将其分别扩充为 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的基：𝑎1,𝑎2,…,𝑎𝑚,𝑏1,𝑏2,…,𝑏𝑛1−𝑚a1,a2,…,am,b1,b2,…,bn1−m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑎1,𝑎2,…,𝑎𝑚,𝑐1,𝑐2,…,𝑐𝑛2−𝑚a1,a2,…,am,c1,c2,…,cn2−m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

接下来只需证明向量组 𝑎1,𝑎2,…,𝑎𝑚,𝑏1,𝑏2,…,𝑏𝑛1−𝑚,𝑐1,𝑐2,…,𝑐𝑛2−𝑚a1,a2,…,am,b1,b2,…,bn1−m,c1,c2,…,cn2−m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性无关即可．

设 ∑𝑚𝑖=1𝑟𝑖𝑎𝑖 +∑𝑛1−𝑚𝑖=1𝑠𝑖𝑏𝑖 +∑𝑛2−𝑚𝑖=1𝑡𝑖𝑐𝑖 =𝜃∑i=1mriai+∑i=1n1−msibi+∑i=1n2−mtici=θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

则 ∑𝑛2−𝑚𝑖=1𝑡𝑖𝑐𝑖 = −∑𝑚𝑖=1𝑟𝑖𝑎𝑖 −∑𝑛1−𝑚𝑖=1𝑠𝑖𝑏𝑖∑i=1n2−mtici=−∑i=1mriai−∑i=1n1−msibi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

注意到上式左边在 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，右边在 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，故两边均在 𝑉1 ∩𝑉2V1∩V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，因此 ∑𝑛2−𝑚𝑖=1𝑡𝑖𝑐𝑖 =∑𝑚𝑖=1𝑘𝑖𝑎𝑖∑i=1n2−mtici=∑i=1mkiai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

故 𝑡1 =𝑡2 =⋯ =𝑡𝑛2−𝑚 =𝑘1 =𝑘2 =⋯ =𝑘𝑚 =0t1=t2=⋯=tn2−m=k1=k2=⋯=km=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 进而 𝑟1 =𝑟2 =⋯ =𝑟𝑚 =𝑠1 =𝑠2 =⋯ =𝑠𝑛1−𝑚 =𝑡1 =𝑡2 =⋯ =𝑡𝑛2−𝑚 =0r1=r2=⋯=rm=s1=s2=⋯=sn1−m=t1=t2=⋯=tn2−m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  3. 令 𝑉1,𝑉2V1,V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有限维线性空间，且 𝑉1 +𝑉2V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉1 ∩𝑉2V1∩V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是有限维的，则下列诸款等价：

     1. 𝑉1 +𝑉2 =𝑉1 ⊕𝑉2V1+V2=V1⊕V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

     2. dim⁡𝑉1 +dim⁡𝑉2 =dim⁡(𝑉1 +𝑉2)dim⁡V1+dim⁡V2=dim⁡(V1+V2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

     3. 若 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组基，𝑏1,𝑏2,…,𝑏𝑚b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组基，则 𝑎1,𝑎2,…,𝑎𝑛,𝑏1,𝑏2,…,𝑏𝑚a1,a2,…,an,b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑉1 +𝑉2V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组基．

Note

1,3 两条可推广到无限维线性空间中

## 例子

考虑 ℝ2R2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基．

  1. 如图

![](./images/basis-1.svg)

𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一组基．

  2. 如图

![](./images/basis-2.svg)

𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一组基．

  3. 如图

![](./images/basis-3.svg)

𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是一组基，因为 𝑢 = −𝑣u=−v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

  4. 如图

![](./images/basis-4.svg)

𝑢,𝑣,𝑤u,v,w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是一组基，因为 𝑢 +4𝑣 +6𝑤 =𝜃u+4v+6w=θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

## 正交基与单位正交基

若线性空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组基 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 ∀𝑏,𝑏′ ∈𝐵, (𝑏,𝑏′) ≠0 ⟺ 𝑏 =𝑏′∀b,b′∈B, (b,b′)≠0⟺b=b′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即两两正交），则称这组基是 **正交基** ．

若线性空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组正交基 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还满足 ∀𝑏 ∈𝐵, |𝑏| =√(𝑏,𝑏) =1∀b∈B, |b|=(b,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称这组基是 **单位正交基** ．

任意有限维线性空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基都可以通过 [Schmidt 正交化](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process) 变换为正交基．

## 应用

根据前文内容，我们可以利用线性基实现：

  1. 求给定向量组的秩；
  2. 对给定的向量组，找到一组极大线性无关组（或其张成的线性空间的一组基）；
  3. 向给定的向量组插入某些向量，在插入操作后的向量组中找到一组极大线性无关组（或其张成的线性空间的一组基）；
  4. 对找到的一组极大线性无关组（或基），判断某向量能否被其线性表出；
  5. 对找到的一组极大线性无关组（或基），求其张成的线性空间中的特殊元素（如最大元、最小元等）．

在 OI 中，我们一般将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维实线性空间 𝐑𝑛Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的线性基称为 **实数线性基** ，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维布尔域线性空间 𝐙𝑛2Z2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的线性基称为 **异或线性基** ．

Tip

𝐙2Z2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的加法为异或，乘法为与，可以证明 𝐙2Z2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是域．

可以证明代数系统 (𝐙𝑛2, +, ⋅,𝐙2)(Z2n,+,⋅,Z2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是线性空间，其中：

(𝑎1,…,𝑎𝑛)+(𝑏1,…,𝑏𝑛):=(𝑎1+𝑏1,…,𝑎𝑛+𝑏𝑛),(a1,…,an)+(b1,…,bn):=(a1+b1,…,an+bn),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 𝑘⋅(𝑎1,…,𝑎𝑛):=(𝑘𝑎1,…,𝑘𝑎𝑛).k⋅(a1,…,an):=(ka1,…,kan).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即加法是异或，数乘是与．

以异或线性基为例，我们可以根据给定的一组布尔序列 𝑋 ={𝑥1,…,𝑥𝑚}X={x1,…,xm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构造出一组异或线性基 𝐵 ={𝑏1,…,𝑏𝑛}B={b1,…,bn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这组基有如下性质：

  1. 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中任意非空子集的异或和不为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 对 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的任意元素 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都可在 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中取出若干元素使其异或和为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  3. 对任意满足上两条的集合 𝐵′B′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其元素个数不会小于 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素个数．

我们可以利用异或线性基实现：

  1. 判断一个数能否表示成某数集子集的异或和；
  2. 求一个数表示成某数集子集异或和的方案数；
  3. 求某数集子集的最大/最小/第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大/第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小异或和；
  4. 求一个数在某数集子集异或和中的排名．

### 构造方法

因为异或线性基与实数线性基没有本质差别，所以接下来以异或线性基为例，实数线性基版本的代码只需做一点简单修改即可．

#### 贪心法

对原集合的每个数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转为二进制，从高位向低位扫，对于第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，如果 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不存在，那么令 𝑎𝑥 ←𝑝ax←p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并结束扫描，如果存在，令 𝑝 ←𝑝 xor 𝑎𝑥p←p xor ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

查询原集合内任意几个元素 xorxor![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大值，只需将线性基从高位向低位扫，若 xorxor![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上当前扫到的 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 答案变大，就把答案异或上 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

为什么能行呢？因为从高往低位扫，若当前扫到第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，意味着可以保证答案的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且后面没有机会改变第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位．

查询原集合内任意几个元素 xorxor![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小值，就是线性基集合所有元素中最小的那个．

查询某个数是否能被异或出来，类似于插入，如果最后插入的数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被异或成了 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则能被异或出来．

代码（洛谷 P3812 [【模板】线性基](https://www.luogu.com.cn/problem/P3812)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``` |  ```text #include <algorithm> #include <iostream> using ull = unsigned long long ; ull p [ 64 ]; void insert ( ull x ) { for ( int i = 63 ; ~ i ; \-- i ) { if ( ! ( x >> i )) // x 的第 i 位是 0 continue ; if ( ! p [ i ]) { p [ i ] = x ; break ; } x ^= p [ i ]; } } using std :: cin ; using std :: cout ; int main () { int n ; cin >> n ; ull a ; for ( int i = 1 ; i <= n ; ++ i ) { cin >> a ; insert ( a ); } ull ans = 0 ; for ( int i = 63 ; ~ i ; \-- i ) { ans = std :: max ( ans , ans ^ p [ i ]); } cout << ans << '\n' ; return 0 ; } ```   
---|---  
  
#### 高斯消元法

高斯消元法相当于从线性方程组的角度去构造线性基，正确性显然．

代码（洛谷 P3812 [【模板】线性基](https://www.luogu.com.cn/problem/P3812)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` |  ```text #include <iostream> using ull = unsigned long long ; constexpr int MAXN = 1e5 \+ 5 ; ull deg ( ull num , int deg ) { return num & ( 1ull << deg ); } ull a [ MAXN ]; using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int n ; cin >> n ; for ( int i = 1 ; i <= n ; ++ i ) cin >> a [ i ]; int row = 1 ; for ( int col = 63 ; ~ col && row <= n ; \-- col ) { for ( int i = row ; i <= n ; ++ i ) { if ( deg ( a [ i ], col )) { std :: swap ( a [ row ], a [ i ]); break ; } } if ( ! deg ( a [ row ], col )) continue ; for ( int i = 1 ; i <= n ; ++ i ) { if ( i == row ) continue ; if ( deg ( a [ i ], col )) { a [ i ] ^= a [ row ]; } } ++ row ; } ull ans = 0 ; for ( int i = 1 ; i < row ; ++ i ) { ans ^= a [ i ]; } cout << ans << '\n' ; return 0 ; } ```   
---|---  
  
### 性质

贪心法构造的线性基具有如下性质：

  * 线性基没有异或和为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子集．
  * 线性基中各数二进制最高位不同．

高斯消元法构造出的线性基满足如下性质：

  * 高斯消元后的矩阵是一个行简化阶梯形矩阵．

> 该性质包含了贪心法构造的线性基满足的两条性质

如果不理解这条性质的正确性，可以跳转 [高斯消元](../../numerical/gauss/)．

提供一组样例：

```text 1 2 ``` |  ```text 5 633 211 169 841 1008 ```   
---|---  
  
二进制表示：

```text 1 2 3 4 5 ``` |  ```text 1001111001 0011010011 0010101001 1101001001 1111110000 ```   
---|---  
  
贪心法生成的线性基：

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text 1001111001 0100110000 0011010011 0001111010 0000000000 0000010000 0000000000 0000000000 0000000000 0000000000 ```   
---|---  
  
高斯消元法生成的线性基：

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text 1000000011 0100100000 0010101001 0001101010 0000010000 0000000000 0000000000 0000000000 0000000000 0000000000 ```   
---|---  
  
这是一条非常好的性质，能帮我们更方便的解决很多问题．比如：给定一些数，选其中一些异或起来，求异或最大值，如果用贪心法构造线性基，需要再做一遍贪心，如果 `ans` 的当前位是 `0`，那么异或一定会更优，否则当前位如果为 `1`，则一定不会更优；而使用高斯消元法构造线性基后直接将线性基中所有元素都异或起来输出即可．

对于其他比较经典的问题（查询一个数能否被异或得到，查询能被异或得到的第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大数等），高斯消元法得到的线性基也能更加方便地解决．

### 时间复杂度

设向量长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 总数为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则时间复杂度为 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 其中高斯消元法的常数略大．

若是实数线性基，则时间复杂度为 𝑂(𝑛2𝑚)O(n2m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

### 线性基合并

线性基的合并只需要暴力处理，即将要合并的一组线性基暴力地插入到另一组线性基即可．单次合并的时间复杂度是 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（异或线性基）或 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（实数线性基）．

### 线性基求交

线性基求交，严格地说就是求它们张成的两个线性空间的交空间的一组线性基．本节介绍两种算法．这两种算法，单次求交的时间复杂度都是 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（异或线性基）或 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（实数线性基）．

#### 朴素算法

设要求交的线性基分别是 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．线性基求交的算法只需要对线性基暴力合并的算法做如下调整：（以异或线性基为例）

  * 将线性基 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的向量 𝛽𝑗βj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 利用 贪心法 尝试插入到 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，并初始化线性基的交 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为空集；
  * 在插入时，需要记录要插入的向量中，线性基 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的贡献．具体地，维持一个新向量 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，初始化为 𝛽𝑗βj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而且，如果正在插入的向量与线性基中第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的向量取了异或，那么贡献 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也要与第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位记录的贡献 𝑏𝑥bx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取一次异或；
  * 如果插入成功，在线性基的第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位插入了向量 𝛽′𝑗βj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就将第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位记录的 𝑏𝑥bx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 改为得到 𝛽′𝑗βj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的过程中线性基 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的贡献 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 如果插入不成功，就将过程中记录到的线性基 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的贡献 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 插入到 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．

这样得到的线性基 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是所求的交，当然，该算法同时也求出了线性基的并．

对算法的解释

设合并后的线性基为 {𝛼1,⋯,𝛼𝑚,𝛽′𝑗1,⋯,𝛽′𝑗ℓ}{α1,⋯,αm,βj1′,⋯,βjℓ′}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝛽′𝑗𝑘βjk′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是插入 𝛽𝑗𝑘βjk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时最后得到的向量．那么，{𝛼1,⋯,𝛼𝑚,𝛽𝑗1,⋯,𝛽𝑗ℓ}{α1,⋯,αm,βj1,⋯,βjℓ}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同样是一组合并后的线性基．记 𝛽+β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为集合 {𝛽𝑗1,⋯,𝛽𝑗ℓ}{βj1,⋯,βjℓ}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则合并后的基可以写作 𝛼 ∪𝛽+α∪β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而且，和空间中的每个向量 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以唯一地表示成

𝑐=𝑎⊕𝑏c=a⊕b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的形式，其中，𝑎 ∈span⁡𝛼a∈span⁡α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑏 ∈span⁡𝛽+b∈span⁡β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这个分解中的 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是前文算法所 **试图** 记录的「线性基 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的贡献」．严格地说，只是 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中最后成功插入的那些向量的贡献．

对于成功的插入，最后记录的 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是该分解中的 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项．设 𝛽𝑗 ∈𝛽+βj∈β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．初始时，𝛽𝑗 =0 ⊕𝛽𝑗βj=0⊕βj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，已经是 𝛽𝑗βj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在基 𝛼 ∪𝛽+α∪β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的正确的分解．在更新 𝛽′𝑗 =𝑎 ⊕𝑏βj′=a⊕b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝛽′𝑗 ⊕𝑐𝑥βj′⊕cx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，因为 𝛽′𝑗 ⊕𝑐𝑥 =(𝑎 ⊕𝑎𝑥) ⊕(𝑏 ⊕𝑏𝑥)βj′⊕cx=(a⊕ax)⊕(b⊕bx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，只需要更新 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑏 ⊕𝑏𝑥b⊕bx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以保证分解依然正确．因此，归纳可知，最后插入 𝛽′𝑗βj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到合并后的线性基中时，记录的贡献 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是上述分解中的 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项．

对于不成功的插入，最后要插入的变量一定会变成 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而此时的贡献 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 要插入到 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．此时，如果重复上面的论证，会发现仍然能够保证在插入过程中总是有 𝛽′𝑗 =𝑎 ⊕𝑏βj′=a⊕b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑎 ∈span⁡𝛼a∈span⁡α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只是 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不再属于 span⁡𝛽+span⁡β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这是因为初始化时，𝛽𝑗 =0 ⊕𝛽𝑗βj=0⊕βj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝛽𝑗 ∉𝛽+βj∉β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．除此之外，贡献更新时异或的项都属于 span⁡𝛽+span⁡β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，实际上，有 𝑏 ⊕𝛽𝑗 ∈span⁡𝛽+b⊕βj∈span⁡β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

那么，为什么将这些插入不成功时的 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都插入到 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，就能得到交空间的线性基呢？首先，插入 𝛽𝑗βj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不成功，最后一定会得到 0 =𝑎 ⊕𝑏0=a⊕b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑎 ∈span⁡𝛼a∈span⁡α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑏 ∈span⁡(𝛽+ ∪{𝛽𝑗}) ⊆span⁡𝛽b∈span⁡(β+∪{βj})⊆span⁡β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，𝑏 =𝑎b=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然位于交空间 span⁡𝛼 ∩span⁡𝛽span⁡α∩span⁡β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．反过来，设 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是交空间中的任意元素，因为 𝑐 ∈span⁡𝛽c∈span⁡β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以表示为 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的线性组合（异或和）：

𝑐=⨁𝛽𝑗∈𝛽𝜆𝑗𝛽𝑗,c=⨁βj∈βλjβj,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝜆𝑗 ∈{0,1}λj∈{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于每一个 𝛽𝑗 ∉𝛽+βj∉β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记相应的插入到 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的贡献为 𝑏𝑗bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有

𝑐⊕⨁𝛽𝑗∉𝛽+𝜆𝑗𝑏𝑗=⨁𝛽𝑗∈𝛽+𝜆𝑗𝛽𝑗+⨁𝛽𝑗∉𝛽+𝜆𝑗(𝛽𝑗⊕𝑏𝑗),c⊕⨁βj∉β+λjbj=⨁βj∈β+λjβj+⨁βj∉β+λj(βj⊕bj),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到，𝑏𝑗bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都位于交空间中，因而左侧必然也位于交空间中，故而左侧可以写成 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的线性组合；同时，右侧所有项，要么 𝛽𝑗 ∈𝛽+βj∈β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要么 𝛽𝑗 ∉𝛽+βj∉β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝛽𝑗 ⊕𝑏𝑗 ∈𝛽+βj⊕bj∈β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而，右侧实际上是 𝛽+β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的线性组合．但是，𝛼 ∪𝛽+α∪β+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性无关，故而所有的系数都是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说 𝑐 =⨁𝛽𝑗∉𝛽+𝜆𝑗𝑏𝑗 ∈span⁡{𝑏1,⋯,𝑏𝑗}c=⨁βj∉β+λjbj∈span⁡{b1,⋯,bj}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就说明了，这些无法插入的向量的贡献 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共同张成了交空间．

根据这一解释，过程中维护贡献 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的目的，实际上是为了维护分解 𝑎 ⊕𝑏a⊕b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；而且，最后向 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 插入贡献时也总有 𝑎 =𝑏a=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，无论维护 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还是 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的贡献（即无论维护 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还是 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），得到的结果都是正确的．如果要维护线性基 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的贡献，只需要修改初始化时相应贡献的取值：每个 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的向量 𝛼𝑖αi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 初始就有贡献 𝛼𝑖αi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而插入的 𝛽𝑗βj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 初始贡献为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

模板题代码如下：

代码（Library Checker [Intersection of 𝐅2F2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 ``` |  ```text #include <array> #include <iostream> class LinearBasis { static constexpr int K = 30 ; std :: array < int , K > a ; // Size of basis. int size () const { int res = 0 ; for ( auto x : a ) { if ( x ) { ++ res ; } } return res ; } public : LinearBasis () : a {} {} // Insert vector x. void insert ( int x ) { for ( int k = K \- 1 ; ~ k && x ; \-- k ) { if (( x >> k ) & 1 ) { if ( ! a [ k ]) { a [ k ] = x ; } x ^= a [ k ]; } } } // Return a basis for *THIS intersecting RHS. LinearBasis intersect ( const LinearBasis & rhs ) const { LinearBasis res ; std :: array < int , K > c = a , b_parts = {}; for ( int i = K \- 1 ; ~ i ; \-- i ) { int x = rhs . a [ i ], b_part = x ; for ( int k = i ; ~ k && x ; \-- k ) { if (( x >> k ) & 1 ) { if ( ! c [ k ]) { c [ k ] = x ; b_parts [ k ] = b_part ; } x ^= c [ k ]; b_part ^= b_parts [ k ]; } } res . insert ( b_part ); } return res ; } // Output. void print () const { std :: cout << size (); for ( auto x : a ) { if ( x ) { std :: cout << ' ' << x ; } } std :: cout << '\n' ; } }; int main () { int t ; std :: cin >> t ; for (; t ; \-- t ) { LinearBasis a , b ; int n ; std :: cin >> n ; for (; n ; \-- n ) { int x ; std :: cin >> x ; a . insert ( x ); } int m ; std :: cin >> m ; for (; m ; \-- m ) { int x ; std :: cin >> x ; b . insert ( x ); } a . intersect ( b ). print (); } return 0 ; } ```   
---|---  
  
#### Zassenhaus 算法

另一种等价的做法是 Zassenhaus 算法，它同样可以同时计算出两个线性基的并和交．复杂度和上文完全一致．

具体步骤如下：

  * 初始化一个向量长度为 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性基 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为空，其中的向量写成 (𝑎,𝑏)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，且 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 长度均为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 将 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素 𝛼𝑖αi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 (𝛼𝑖,𝛼𝑖)(αi,αi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式插入 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中；
  * 将 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素 𝛽𝑗βj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 (𝛽𝑗,0)(βj,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式插入 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中；
  * 最后得到的线性基 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的所有非零元素 (𝑐𝑘,𝑑𝑘)(ck,dk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，𝑐𝑘ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非零的那些向量中项 𝑐𝑘ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体组成了 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的并的线性基，𝑐𝑘ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为零的那些向量中项 𝑑𝑘dk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体组成了 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的交的线性基．

算法中的构造线性基的方法可以是 贪心法 或 高斯消元法，只要保证 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的线性基组成行阶梯型矩阵即可．

将 Zassenhaus 算法中的消元的步骤与上面的朴素算法相比较，很容易发现，基于贪心法的 Zassenhaus 算法相当于维护 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的贡献的朴素算法．如果转而先插入所有 (𝛼𝑖,0)(αi,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再插入所有 (𝛽𝑗,𝛽𝑗)(βj,βj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么基于贪心法的 Zassenhaus 算法就相当于维护 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素贡献的朴素算法．根据消元步骤的等价性，Zassenhaus 算法的正确性也是成立的．

除此之外，还可以再提供一个独立且更为一般的代数证明：

正确性证明

设 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一线性空间，且有子空间 𝑈 =span⁡𝛼U=span⁡α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑊 =span⁡𝛽W=span⁡β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．算法本身相当于通过化简为行阶梯型来求子空间

𝐻=span⁡({(𝛼𝑖,𝛼𝑖):𝛼𝑖∈𝛼}∪{(𝛽𝑗,0):𝛽𝑗∈𝛽})H=span⁡({(αi,αi):αi∈α}∪{(βj,0):βj∈β})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的一组基 𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．算法最后，𝛾γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素 (𝑐𝑘,𝑑𝑘)(ck,dk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 根据 𝑐𝑘 ≠0ck≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与否需要分为两类，所以不妨考察投影映射 𝜋 :𝐻 →𝑉π:H→V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝜋(𝑎,𝑏) =𝑎π(a,b)=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．于是，𝜋(𝐻) =𝑈 +𝑊π(H)=U+W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且容易验证

ker⁡𝜋=𝐻∩({0}×𝑉)={0}×(𝑈×𝑊).ker⁡π=H∩({0}×V)={0}×(U×W).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据 [线性映射的相关定理](../linear-mapping/#线性映射的核空间与像空间)，有 dim⁡𝐻 =dim⁡𝜋(𝐻) +dim⁡ker⁡𝜋 =dim⁡(𝑈 +𝑊) +dim⁡(𝑈 ∩𝑊)dim⁡H=dim⁡π(H)+dim⁡ker⁡π=dim⁡(U+W)+dim⁡(U∩W)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

行阶梯型矩阵的前几列仍然是行阶梯型矩阵，因而 𝑐𝑘 ≠0ck≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行的数目，恰好等于 𝛼 ∪𝛽α∪β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行秩，亦即 dim⁡(𝑈 +𝑊)dim⁡(U+W)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；而且，这些行中 𝑐𝑘ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合就形成了 𝑈 +𝑊U+W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组基．剩下的非零行恰好有 dim⁡(𝑈 ∩𝑊)dim⁡(U∩W)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，且都满足 𝑐𝑘 =0ck=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于这些行中的 𝑑𝑘dk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为有 (0,𝑑𝑘) ∈ker⁡𝜋(0,dk)∈ker⁡π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑑𝑘 ∈𝑈 ∩𝑊dk∈U∩W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；而且，(0,𝑑𝑘)(0,dk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为行阶梯型矩阵的行，必然线性无关，这就说明这些 𝑑𝑘dk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都线性无关．综合起来，这些 𝑑𝑘dk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是交空间 𝑈 ∩𝑊U∩W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中大小为 dim⁡(𝑈 ∩𝑊)dim⁡(U∩W)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性无关组，所以也必然是该空间的一组基．

模板题代码如下：

代码（Library Checker [Intersection of 𝐅2F2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 ``` |  ```text #include <iostream> #include <vector> class LinearBasis { int K ; std :: vector < long long > a ; public : LinearBasis ( int K ) : K ( K ), a ( K ) {} // Insert vector x. void insert ( long long x ) { for ( int k = K \- 1 ; ~ k && x ; \-- k ) { if (( x >> k ) & 1 ) { if ( ! a [ k ]) { a [ k ] = x ; } x ^= a [ k ]; } } } // Output those not exceeding 2^k. void print ( int k ) const { int sz = 0 ; for ( int i = 0 ; i < k ; ++ i ) { if ( a [ i ]) { ++ sz ; } } std :: cout << sz ; for ( int i = 0 ; i < k ; ++ i ) { if ( a [ i ]) { std :: cout << ' ' << a [ i ]; } } std :: cout << '\n' ; } }; int main () { constexpr int K = 30 ; int t ; std :: cin >> t ; for (; t ; \-- t ) { LinearBasis c ( K << 1 ); int n ; std :: cin >> n ; for (; n ; \-- n ) { int x ; std :: cin >> x ; c . insert ((( long long ) x << K ) | x ); } int m ; std :: cin >> m ; for (; m ; \-- m ) { int x ; std :: cin >> x ; c . insert (( long long ) x << K ); } c . print ( K ); } return 0 ; } ```   
---|---  
  
注意，输出时只需要考虑前 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位均为零的向量即可．

### 拓展：前缀线性基

本节只讨论异或线性基的情形，并假设单个向量可以存储在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的空间内，且单次操作复杂度总是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

对于需要多次查询区间异或最大值的情形，一种常见的做法是 [猫树](../../../ds/cat-tree/) 配合线性基，时间复杂度为 𝑂(𝑛𝑚log⁡𝑚 +𝑛2𝑞)O(nmlog⁡m+n2q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是向量长度，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是序列长度，𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是询问次数．另一种可行的做法是利用前缀线性基（或称时间戳线性基），可以将复杂度降低到 𝑂(𝑛(𝑚 +𝑞))O(n(m+q))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

前缀线性基允许对于序列的每个前缀，都维护该前缀的所有后缀的线性基，这样就可以支持查询每个区间的线性基．注意到序列的某个前缀 [1,𝑖][1,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有后缀 [𝑗,𝑖][j,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性基是相互包含的，即 [𝑗,𝑖][j,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性基总是包含着 [𝑗 +1,𝑖][j+1,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性基，所以，这些后缀的线性基中互不相同的至多只有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种，而且总是可以通过向空集中逐步添加新的向量来得到自 [𝑖,𝑖][i,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 [1,𝑖][1,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所有这些后缀的线性基．因此，利用这个单调性，只需要为添加的每个向量 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都标记它出现的最大下标 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的空间内存储所有后缀的线性基．而且，查询区间 [𝑗,𝑖][j,i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的线性基时，只需要在 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的前缀线性基中仅保留标记 𝑡 ≥𝑗t≥j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的那些向量即可．

不妨将每个向量 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的标记 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为它的时间戳．线性基中的向量 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是可以表示为原序列中某些元素的异或和，比如 𝑣𝑖1 ⊕𝑣𝑖2 ⊕⋯ ⊕𝑣𝑖𝑘vi1⊕vi2⊕⋯⊕vik![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而在所有这样的可能的表示中，最小下标的最大值就是 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即

𝑡(𝑣)=max{𝑗:∃𝑖1,⋯,𝑖𝑘∈[𝑗,𝑖] s.t. 𝑣=𝑣𝑖1⊕𝑣𝑖2⊕⋯⊕𝑣𝑖𝑘}.t(v)=max{j:∃i1,⋯,ik∈[j,i] s.t. v=vi1⊕vi2⊕⋯⊕vik}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个表达式不过是将上一段的叙述用形式的语言写出来而已．它给我们带来的启发是，要维护线性基中每个向量 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间戳，只需要贪心地选取尽可能新的向量替换掉旧的向量即可．

基于上文提到的 贪心法 构造线性基，前缀线性基在构造过程中做了如下调整：

  * 为线性基中保留的每个向量 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都保存一个时间戳 𝑡𝑥tx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，初始时均设为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 要添加序列中第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个向量 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，仍然从高位向低位扫，但同时需要记录当前时间 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 如果 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位是一，就比较线性基中已有的向量 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间戳 𝑡𝑥tx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和当前时间 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：
    * 如果 𝑖 >𝑡𝑥i>tx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即要添加的向量时间更晚，就将 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 设为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并更新时间戳为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将旧的 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 异或 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结果 𝑎𝑥 ⊕𝑣ax⊕v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 按照之前记录的时间 𝑡𝑥tx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 继续添加过程；
    * 如果 𝑖 <𝑡𝑥i<tx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即要添加的向量时间更早，不更新 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑡𝑥tx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 异或 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后继续添加即可．

也就是说，如果当前位可以通过较新的向量表示，就直接用较新的向量；否则，保留原来的向量．在更新位置 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的向量时，不能将异或的结果 𝑎𝑥 ⊕𝑣ax⊕v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存入位置 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为异或的结果 𝑎𝑥 ⊕𝑣ax⊕v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间戳为 min{𝑡(𝑎𝑥) =𝑡(𝑣)} =𝑡(𝑎𝑥)min{t(ax)=t(v)}=t(ax)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，小于要添加的变量 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间戳 𝑡(𝑣)t(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．同样的原因，高斯消元法 构造线性基的过程中向上更新时可能会破坏时间戳的性质，所以不再适用于构造前缀线性基．

模板题代码如下：

代码（Codeforces [1100F Ivan and Burgers](https://codeforces.com/problemset/problem/1100/F)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 ``` |  ```text #include <algorithm> #include <array> #include <iostream> #include <numeric> #include <vector> class LinearBasis { static constexpr int K = 20 ; std :: array < int , K > a , t ; public : LinearBasis () : a {}, t {} {} // Insert vector x at time i. void insert ( int x , int i ) { for ( int k = K \- 1 ; ~ k && x ; \-- k ) { if ((( x >> k ) & 1 )) { if ( i > t [ k ]) { std :: swap ( a [ k ], x ); std :: swap ( t [ k ], i ); } x ^= a [ k ]; } } } // Find max xor of subsets of elements from time i till now. int query ( int i ) const { int res = 0 ; for ( int k = K \- 1 ; ~ k ; \-- k ) { if ( t [ k ] >= i && ( res ^ a [ k ]) > res ) { res ^= a [ k ]; } } return res ; } }; int main () { int n ; std :: cin >> n ; std :: vector < int > c ( n \+ 1 ); for ( int i = 1 ; i <= n ; ++ i ) std :: cin >> c [ i ]; int q ; std :: cin >> q ; std :: vector < std :: array < int , 2 >> qu ( q ); for ( auto & v : qu ) std :: cin >> v [ 0 ] >> v [ 1 ]; std :: vector < int > ids ( q ); std :: iota ( ids . begin (), ids . end (), 0 ); std :: sort ( ids . begin (), ids . end (), [ & ]( int l , int r ) -> bool { return qu [ l ][ 1 ] < qu [ r ][ 1 ]; }); LinearBasis lb ; std :: vector < int > res ( q ); for ( int i = 1 , j = 0 ; i <= n ; ++ i ) { lb . insert ( c [ i ], i ); for (; j < q && qu [ ids [ j ]][ 1 ] == i ; ++ j ) { res [ ids [ j ]] = lb . query ( qu [ ids [ j ]][ 0 ]); } } for ( int x : res ) std :: cout << x << '\n' ; return 0 ; } ```   
---|---  
  
如果需要在线询问，也可以用 𝑂(𝑚𝑛)O(mn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的空间将每个前缀处的前缀线性基都存下来再查询，这可以看作是一种「可持久化」线性基．如果需要用到高斯消元法得到的线性基的性质，可以在查询时另行处理．

### 练习题

  * [Luogu P3812【模板】线性基](https://www.luogu.com.cn/problem/P3812)
  * [Acwing 3164. 线性基](https://www.acwing.com/problem/content/description/3167)
  * [SGU 275 to xor or not xor](https://codeforces.com/problemsets/acmsguru/problem/99999/275)
  * [HDU 3949 XOR](https://acm.hdu.edu.cn/showproblem.php?pid=3949)
  * [HDU 6579 Operation](https://acm.hdu.edu.cn/showproblem.php?pid=6579)
  * [Luogu P4151 [WC2011] 最大 XOR 和路径](https://www.luogu.com.cn/problem/P4151)
  * [Library Checker - Intersection of 𝐅2F2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces)
  * [AtCoder Grand Contest 045 A - Xor Battle](https://atcoder.jp/contests/agc045/tasks/agc045_a)
  * [Codeforces 1100F Ivan and Burgers](https://codeforces.com/problemset/problem/1100/F)
  * [Luogu P3292 [SCOI2016] 幸运数字](https://www.luogu.com.cn/problem/P3292)

## 参考资料与注释

  1. 丘维声，高等代数（下）．清华大学出版社．
  2. [Basis (linear algebra) - Wikipedia](https://en.wikipedia.org/wiki/Basis_%28linear_algebra%29)
  3. [Vector Basis -- from Wolfram MathWorld](https://mathworld.wolfram.com/VectorBasis.html)
  4. [Zassenhaus algorithm - Wikipedia](https://en.wikipedia.org/wiki/Zassenhaus_algorithm)

* * *

  1. [Proof that every vector space has a basis](https://en.wikipedia.org/wiki/Basis_%28linear_algebra%29#Proof_that_every_vector_space_has_a_basis) ↩

* * *

>  __本页面最近更新： 2026/2/25 17:11:23，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-algebra/basis.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/linear-algebra/basis.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Ir1d](https://github.com/Ir1d), [c-forrest](https://github.com/c-forrest), [MegaOwIer](https://github.com/MegaOwIer), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [cesonic](https://github.com/cesonic), [ksyx](https://github.com/ksyx), [lychees](https://github.com/lychees), [RUIN-RISE](https://github.com/RUIN-RISE), [wjy-yy](https://github.com/wjy-yy), [aofall](https://github.com/aofall), [CoelacanthusHex](https://github.com/CoelacanthusHex), [hensier](https://github.com/hensier), [iamtwz](https://github.com/iamtwz), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [ouuan](https://github.com/ouuan), [Persdre](https://github.com/Persdre), [rsdbkhusky](https://github.com/rsdbkhusky), [shuzhouliu](https://github.com/shuzhouliu), [Xeonacid](https://github.com/Xeonacid), [yusancky](https://github.com/yusancky)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
