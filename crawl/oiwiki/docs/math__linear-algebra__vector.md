# 向量 - OI Wiki

- Source: https://oi-wiki.org/math/linear-algebra/vector/

# 向量

在本文之前，特别说明一下翻译的相关问题．由于历史原因，数学学科和物理学科关于「vector」一词的翻译不同．

在物理学科，一般翻译成「矢量」，并且与「标量」一词相对．在数学学科，一般翻译成「向量」．这种翻译的差别还有「本征」与「特征」、「幺正」与「酉」，等等．

在 **OI Wiki** ，主要面向计算机等工程类相关学科，与数学学科关系更近一些，因此采用「向量」这个词汇．

## 定义及相关概念

**向量** ：既有大小又有方向的量称为向量．数学上研究的向量为 **自由向量** ，即只要不改变它的大小和方向，起点和终点可以任意平行移动的向量．记作 ⃗𝑎a→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**有向线段** ：带有方向的线段称为有向线段．有向线段有三要素：**起点，方向，长度** ，知道了三要素，终点就唯一确定．一般使用有向线段表示向量．

**向量的模** ：有向线段 ⟶𝐴𝐵AB→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的长度称为向量的模，即为这个向量的大小．记为：|⟶𝐴𝐵||AB→|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 |𝒂||a|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**零向量** ：模为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的向量．零向量的方向任意．记为：⃗00→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝟎0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**单位向量** ：模为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的向量称为该方向上的单位向量．一般记为 ⃗𝑒e→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝒆e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**平行向量** ：方向相同或相反的两个 **非零** 向量．记作：𝒂 ∥𝒃a∥b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于多个互相平行的向量，可以任作一条直线与这些向量平行，那么任一组平行向量都可以平移到同一直线上，所以平行向量又叫 **共线向量** ．

**相等向量** ：模相等且方向相同的向量．

**相反向量** ：模相等且方向相反的向量．

**向量的夹角** ：已知两个非零向量 𝒂,𝒃a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，作 ⟶𝑂𝐴 =𝒂,⟶𝑂𝐵 =𝒃OA→=a,OB→=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝜃 =∠𝐴𝑂𝐵θ=∠AOB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是向量 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与向量 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的夹角．记作：⟨𝒂,𝒃⟩⟨a,b⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．显然当 𝜃 =0θ=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时两向量同向，𝜃 =𝜋θ=π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时两向量反向，𝜃 =𝜋2θ=π2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时两向量垂直，记作 𝒂 ⟂𝒃a⟂b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且规定 𝜃 ∈[0,𝜋]θ∈[0,π]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意到平面向量具有方向性，两个向量不能比较大小（但可以比较两向量的模长）．但是两个向量可以相等．

## 向量的线性运算

### 向量的加减法

在定义了一种量之后，就希望让它具有运算．向量的运算可以类比数的运算，从物理学的角度出发也可以研究向量的运算．

类比物理学中的位移概念，假如一个人从 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 经 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 走到 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么他经过的位移为 ⟶𝐴𝐵 +⟶𝐵𝐶AB→+BC→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这其实等价于这个人直接从 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 走到 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 ⟶𝐴𝐵 +⟶𝐵𝐶 =⟶𝐴𝐶AB→+BC→=AC→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意到力的合成法则——平行四边形法则，同样也可以看做一些向量相加．

整理一下向量的加法法则：

  1. **向量加法的三角形法则** ：若要求和的向量首尾顺次相连，那么这些向量的和为第一个向量的起点指向最后一个向量的终点；
  2. **向量加法的平行四边形法则** ：若要求和的两个向量 **共起点** ，那么它们的和向量为以这两个向量为邻边的平行四边形的对角线，起点为两个向量共有的起点，方向沿平行四边形对角线方向．

这样，向量的加法就具有了几何意义．并且可以验证，向量的加法满足 **交换律与结合律** ．

因为实数的减法可以写成加上相反数的形式，考虑在向量做减法时也这么写．即：𝒂 −𝒃 =𝒂 +( −𝒃)a−b=a+(−b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这样，考虑共起点的向量，按照平行四边形法则做出它们的差，经过平移后可以发现 **「共起点向量的差向量」是由「减向量」指向「被减向量」的有向线段** ．这也是向量减法的几何意义．

有时候有两点 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，想知道 ⟶𝐴𝐵AB→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以利用减法运算 ⟶𝐴𝐵 =⟶𝑂𝐵 −⟶𝑂𝐴AB→=OB→−OA→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 获得．

### 向量的数乘

规定「实数 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与向量 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的积」为一个向量，这种运算就是向量的 **数乘运算** ，记作 𝜆𝒂λa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的长度与方向规定如下：

  1. |𝜆𝒂| =|𝜆||𝒂||λa|=|λ||a|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 当 𝜆 >0λ>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝜆𝒂λa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同向，当 𝜆 =0λ=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝜆𝒂 =𝟎λa=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当 𝜆 <0λ<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝜆𝒂λa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 方向相反．

根据数乘的定义，可以验证有如下运算律：

𝜆(𝜇𝒂)=(𝜆𝜇)𝒂(𝜆+𝜇)𝒂=𝜆𝒂+𝜇𝒂𝜆(𝒂+𝒃)=𝜆𝒂+𝜆𝒃λ(μa)=(λμ)a(λ+μ)a=λa+μaλ(a+b)=λa+λb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

特别地：

(−𝜆)𝒂=−(𝜆𝒂)=−𝜆(𝒂)𝜆(𝒂−𝒃)=𝜆𝒂−𝜆𝒃(−λ)a=−(λa)=−λ(a)λ(a−b)=λa−λb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 判定两向量共线

两个 **非零** 向量 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共线  ⟺ ⟺![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有唯一实数 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝒃 =𝜆𝒂b=λa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明：由数乘的定义可知，对于 **非零** 向量 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果存在实数 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝒃 =𝜆𝒂b=λa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝒂 ∥𝒃a∥b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

反过来，如果 𝒂 ∥𝒃a∥b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝒂 ≠𝟎a≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 |𝒃| =𝜇|𝒂||b|=μ|a|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么当 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同向时，𝒃 =𝜇𝒂b=μa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，反向时 𝒃 = −𝜇𝒂b=−μa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后，向量的加，减，数乘统称为向量的线性运算．

## 平面向量的基本定理及坐标表示

### 平面向量基本定理

定理内容：如果两个向量 𝒆𝟏,𝒆𝟐e1,e2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不共线，那么存在唯一实数对 (𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得与 𝒆𝟏,𝒆𝟐e1,e2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共面的任意向量 𝒑p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝐩 =𝑥𝒆𝟏 +𝑦𝒆𝟐p=xe1+ye2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

平面向量那么多，怎样用尽可能少的量表示出所有平面向量？

只用一个向量表示出所有向量显然是不可能的，最多只能表示出某条直线上的向量．

再加入一个向量，用两个 **不共线** 向量表示（两个共线向量在此可以看成同一个向量），这样可以把任意一个平面向量分解到这两个向量的方向上了．

在同一平面内的两个不共线的向量称为 **基底** ．如果基底相互垂直，那么在分解的时候就是对向量 **正交分解** ．

### 平面向量的坐标表示

如果取与横轴与纵轴方向相同的单位向量 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为一组基底，根据平面向量基本定理，平面上的所有向量与有序实数对 (𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一一对应．

而有序实数对 (𝑥,𝑦)(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与平面直角坐标系上的点一一对应，于是作 ⟶𝑂𝑃 =𝒑OP→=p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么终点 𝑃(𝑥,𝑦)P(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是唯一确定的．由于研究的对象是自由向量，可以自由平移起点，这样，在平面直角坐标系里，每一个向量都可以用有序实数对唯一表示．

## 平面向量的坐标运算

### 平面向量线性运算

由平面向量的线性运算可以推导其坐标运算，主要方法是将坐标全部化为用基底表示，然后利用运算律进行合并，之后表示出运算结果的坐标形式．

若两向量 𝒂 =(𝑚,𝑛)a=(m,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝒃 =(𝑝,𝑞)b=(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则：

𝒂+𝒃=(𝑚+𝑝,𝑛+𝑞)𝒂−𝒃=(𝑚−𝑝,𝑛−𝑞)𝑘𝒂=(𝑘𝑚,𝑘𝑛)a+b=(m+p,n+q)a−b=(m−p,n−q)ka=(km,kn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 求一个向量的坐标表示

已知两点 𝐴(𝑎,𝑏),𝐵(𝑐,𝑑)A(a,b),B(c,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，易证 ⟶𝐴𝐵 =(𝑐 −𝑎,𝑑 −𝑏)AB→=(c−a,d−b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 平移一点

有时需要将一个点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 沿一定方向平移某单位长度，这样把要平移的方向和距离组合成一个向量，利用向量加法的三角形法则，将 ⟶𝑂𝑃OP→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加上这个向量，得到的向量终点即为平移后的点．

### 三点共线的判定

若 𝐴,𝐵,𝐶A,B,C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 三点共线，则 ⟶𝑂𝐵 =𝜆⟶𝑂𝐴 +(1 −𝜆)⟶𝑂𝐶OB→=λOA→+(1−λ)OC→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 三点共线判定的拓展

在三角形 𝐴𝐵𝐶ABC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，若 𝐷D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐵𝐶BC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等分点（𝑛 𝐵𝐷 =𝑘 𝐷𝐶n BD=k DC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），则有：⟶𝐴𝐷 =𝑛𝑘+𝑛⟶𝐴𝐵 +𝑘𝑘+𝑛⟶𝐴𝐶AD→=nk+nAB→+kk+nAC→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 在三维空间中的拓展（立体几何/空间向量）

在空间中，以上部分所述的所有内容均成立．更有：

### 空间向量基本定理

定理内容：如果三个向量 𝒆𝟏,𝒆𝟐,𝒆𝟑e1,e2,e3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不共面，那么存在唯一实数对 (𝑥,𝑦,𝑧)(x,y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得空间中任意向量 𝒑p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝐩 =𝑥𝒆𝟏 +𝑦𝒆𝟐 +𝑧𝒆𝟑p=xe1+ye2+ze3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． 根据空间向量基本定理，我们同样可以使用三个相互垂直的基底 𝒆𝟏,𝒆𝟐,𝒆𝟑e1,e2,e3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为正交基底，建立 **空间直角坐标系** 并用一个三元组 (𝑥,𝑦,𝑧)(x,y,z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为坐标表示空间向量．

### 共面向量基本定理

如果存在两个不共线的向量 𝒙,𝒚x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则向量 𝒑p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝒙,𝒚x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共面的充要条件是存在唯一实数对 (𝑎,𝑏)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝒑 =𝑎𝒙 +𝑏𝒚p=ax+by![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 方向向量

空间直线的方向用一个与该直线平行的非零向量来表示，该向量称为这条直线的一个方向向量．直线在空间中的位置，由它经过的空间一点及它的一个方向向量 **完全确定** ．

注意，平面中的直线也有方向向量．

对于 **空间** 中的直线，对其方向向量有以下求法：

  * 若有 𝐴(𝑥1,𝑦1,𝑧1),𝐵(𝑥2,𝑦2,𝑧2)A(x1,y1,z1),B(x2,y2,z2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝐴𝐵AB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在直线的一个方向向量为 𝒔 =(𝑥2 −𝑥1,𝑦2 −𝑦1,𝑧2 −𝑧1)s=(x2−x1,y2−y1,z2−z1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 若已知一个与所求直线 **垂直** 的平面，该平面一般方程为 𝑎𝑥 +𝑏𝑦 +𝑐𝑧 +𝑑 =0ax+by+cz+d=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么垂直于该平面的直线的一个方向向量为 𝒔 =(𝑎,𝑏,𝑐)s=(a,b,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，该方向向量也是该平面的 **一个法向量** ．

### 法向量

对于一个面 𝐴𝐵𝐶𝐷ABCD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其法向量 𝒏n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与这个面垂直．

计算方法：任取两个面内直线 ⟶𝐴𝐵,⟶𝐴𝐷AB→,AD→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 ⟶𝐴𝐵 ⋅𝒏 =𝟎AB→⋅n=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 ⟶𝐴𝐷 ⋅𝒏 =𝟎AD→⋅n=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，利用坐标法即可计算．

## 向量与矩阵

线性代数中，线性变换可以用矩阵表示．令 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示一个将 𝐑𝑛Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 映射到 𝐑𝑚Rm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性变换，𝐱x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维列向量，则存在一个 𝑚 ×𝑛m×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得

𝑇(𝐱)=𝐴𝐱.T(x)=Ax.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为线性变换 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的变换矩阵．在算法问题中，一般情况下线性变换在相同维度下进行，因此 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个方阵．这样，对向量的线性变换问题可以转化为矩阵乘法问题．

接下来我们探讨三种竞赛中较为常见的变换与其对应的变换矩阵：放缩变换（变换矩阵用 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示）、旋转变换（变换矩阵用 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示）和平移变换（变换矩阵用 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示）．

### 放缩变换

对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维列向量 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将其每一维放缩 𝑣1,𝑣2,…,𝑣𝑛v1,v2,…,vn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倍．很容易发现放缩操作的变换矩阵 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对角矩阵，即 𝑆 =diag⁡{𝑣1,𝑣2,…,𝑣𝑛}S=diag⁡{v1,v2,…,vn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 旋转变换

向量的旋转是相对复杂的操作，我们仅限于讨论二维和三维的情况．

#### 向量绕点旋转

对于向量绕点旋转，一般指的是向量绕原点旋转．对于某一点绕另一点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 旋转，可以利用平移变换使得点 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位于原点，进行向量旋转后再将坐标系平移回原位置即可．设平移操作的变换矩阵为 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，绕原点旋转操作的变换矩阵为 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则整个过程的变换矩阵为 𝑇𝑅𝑇−1TRT−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据几何意义，𝑇−1T−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定存在．

对于二维空间，设 𝒂 =(𝑥,𝑦)a=(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，倾角为 𝜃θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，长度为 𝑙 =√𝑥2+𝑦2l=x2+y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．则 𝑥 =𝑙cos⁡𝜃,𝑦 =𝑙sin⁡𝜃x=lcos⁡θ,y=lsin⁡θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．令其绕原点逆时针旋转 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 角，得到向量 𝒃 =(𝑙cos⁡(𝜃+𝛼),𝑙sin⁡(𝜃+𝛼))b=(lcos⁡(θ+α),lsin⁡(θ+α))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

![](./images/vector-rotation.svg)

由三角恒等变换得，

𝒃=(𝑙(cos⁡𝜃cos⁡𝛼−sin⁡𝜃sin⁡𝛼),𝑙(sin⁡𝜃cos⁡𝛼+cos⁡𝜃sin⁡𝛼))b=(l(cos⁡θcos⁡α−sin⁡θsin⁡α),l(sin⁡θcos⁡α+cos⁡θsin⁡α))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

化简，

𝒃=(𝑙cos⁡𝜃cos⁡𝛼−𝑙sin⁡𝜃sin⁡𝛼,𝑙sin⁡𝜃cos⁡𝛼+𝑙cos⁡𝜃sin⁡𝛼)b=(lcos⁡θcos⁡α−lsin⁡θsin⁡α,lsin⁡θcos⁡α+lcos⁡θsin⁡α)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

把上面的 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代回来得

𝒃=(𝑥cos⁡𝛼−𝑦sin⁡𝛼,𝑦cos⁡𝛼+𝑥sin⁡𝛼)b=(xcos⁡α−ysin⁡α,ycos⁡α+xsin⁡α)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此二维空间下，变换矩阵 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

𝑅=[cos⁡𝛼−sin⁡𝛼sin⁡𝛼cos⁡𝛼].R=[cos⁡α−sin⁡αsin⁡αcos⁡α].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于三维空间，向量旋转需要使用两个角度参量，即天顶角旋转角度与方向角旋转角度，可以利用 [空间球坐标系](../../coordinate/#空间球坐标系) 进行旋转操作．

#### 向量绕直线旋转

对于三维向量，更常见的是绕某直线旋转．同样为了方便，此直线是过原点的．如果直线不过原点，我们仍可以平移坐标系进行转化．

取直线的方向向量 𝒖 =(𝑢𝑥,𝑢𝑦,𝑢𝑧)u=(ux,uy,uz)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设三维向量绕其逆时针旋转 𝜃θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 角．则对应的变换矩阵 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为1

𝑅=⎡⎢ ⎢ ⎢⎣𝑢2𝑥(1−cos⁡𝜃)+cos⁡𝜃𝑢𝑥𝑢𝑦(1−cos⁡𝜃)−𝑢𝑧sin⁡𝜃𝑢𝑥𝑢𝑧(1−cos⁡𝜃)+𝑢𝑦sin⁡𝜃𝑢𝑥𝑢𝑦(1−cos⁡𝜃)+𝑢𝑧sin⁡𝜃𝑢2𝑦(1−cos⁡𝜃)+cos⁡𝜃𝑢𝑦𝑢𝑧(1−cos⁡𝜃)−𝑢𝑥sin⁡𝜃𝑢𝑥𝑢𝑧(1−cos⁡𝜃)−𝑢𝑦sin⁡𝜃𝑢𝑦𝑢𝑧(1−cos⁡𝜃)+𝑢𝑥sin⁡𝜃𝑢2𝑧(1−cos⁡𝜃)+cos⁡𝜃⎤⎥ ⎥ ⎥⎦.R=[ux2(1−cos⁡θ)+cos⁡θuxuy(1−cos⁡θ)−uzsin⁡θuxuz(1−cos⁡θ)+uysin⁡θuxuy(1−cos⁡θ)+uzsin⁡θuy2(1−cos⁡θ)+cos⁡θuyuz(1−cos⁡θ)−uxsin⁡θuxuz(1−cos⁡θ)−uysin⁡θuyuz(1−cos⁡θ)+uxsin⁡θuz2(1−cos⁡θ)+cos⁡θ].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 平移变换

平移变换并非线性变换，而是仿射变换．但 𝐑𝑛Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的仿射变换仍可以用 𝐑𝑛+1Rn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的线性变换表示．

考虑 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维向量 𝒂 =(𝑎1,𝑎2,…,𝑎𝑛)a=(a1,a2,…,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，现在要将其沿向量 𝒕 =(𝑡1,𝑡2,…,𝑡𝑛)t=(t1,t2,…,tn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 平移．我们对列向量 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 添加一维并置为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得到新列向量 𝒂′ =(𝑎1,𝑎2,…,𝑎𝑛,1)a′=(a1,a2,…,an,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．则变换矩阵 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以写作

𝑇=⎡⎢ ⎢ ⎢ ⎢ ⎢⎣1𝑡11𝑡2⋱⋮1𝑡𝑛1⎤⎥ ⎥ ⎥ ⎥ ⎥⎦.T=[1t11t2⋱⋮1tn1].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于其他线性变换矩阵，在矩阵中增加一列与一行，除右下角的元素为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 外其它部分填充为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，通过这种方法，所有的线性变换矩阵都可以转换为仿射变换矩阵．例如，对于二维向量旋转，变换矩阵可以变为

𝑅′=⎡⎢ ⎢⎣cos⁡𝛼−sin⁡𝛼0sin⁡𝛼cos⁡𝛼0001⎤⎥ ⎥⎦.R′=[cos⁡α−sin⁡α0sin⁡αcos⁡α0001].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 向量的更严格定义

上文中，向量被定义为了空间中的有向线段．但是严格来说，向量不仅是有向线段．要作出向量的更严格定义，需要先定义 [线性空间](../vector-space/)，具体内容参见 [线性空间](../vector-space/) 页面的介绍．

* * *

  1. 参见 [Rotation matrix from axis and angle - Wikipedia](https://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle) ↩

* * *

>  __本页面最近更新： 2026/4/23 03:45:48，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-algebra/vector.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/linear-algebra/vector.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [HeRaNO](https://github.com/HeRaNO), [Xeonacid](https://github.com/Xeonacid), [Great-designer](https://github.com/Great-designer), [MegaOwIer](https://github.com/MegaOwIer), [ouuan](https://github.com/ouuan), [aofall](https://github.com/aofall), [CCXXXI](https://github.com/CCXXXI), [chenmingwangOI](https://github.com/chenmingwangOI), [ChungZH](https://github.com/ChungZH), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Early0v0](https://github.com/Early0v0), [iamtwz](https://github.com/iamtwz), [Marcythm](https://github.com/Marcythm), [mgt](mailto:i@margatroid.xyz), [Ohnmaches](mailto:qingdkj@outlook.com), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu), [StudyingFather](https://github.com/StudyingFather), [wjy-yy](https://github.com/wjy-yy), [yusancky](https://github.com/yusancky), [2008verser](https://github.com/2008verser), [66Leo66](https://github.com/66Leo66), [abc1763613206](https://github.com/abc1763613206), [aberter0x3f](https://github.com/aberter0x3f), [Ayx03](https://github.com/Ayx03), [Backl1ght](https://github.com/Backl1ght), [chieh2lu2](https://github.com/chieh2lu2), [Chrogeek](https://github.com/Chrogeek), [codewasp942](https://github.com/codewasp942), [CSPNOIP](https://github.com/CSPNOIP), [DawnMagnet](https://github.com/DawnMagnet), [dong628](https://github.com/dong628), [EarthMessenger](https://github.com/EarthMessenger), [Enonya](https://github.com/Enonya), [F1shAndCat](https://github.com/F1shAndCat), [future-re](https://github.com/future-re), [fyulingi](https://github.com/fyulingi), [greyqz](https://github.com/greyqz), [HeliumOI](https://github.com/HeliumOI), [henrytbtrue](https://github.com/henrytbtrue), [hly1204](https://github.com/hly1204), [Junyan721113](https://github.com/Junyan721113), [kenlig](https://github.com/kenlig), [krn1pnc](https://github.com/krn1pnc), [ksyx](https://github.com/ksyx), [lailai0916](https://github.com/lailai0916), [lrherqwq](https://github.com/lrherqwq), [LTHAndy](https://github.com/LTHAndy), [lychees](https://github.com/lychees), [Menci](https://github.com/Menci), [minghu6](https://github.com/minghu6), [Nanarikom](https://github.com/Nanarikom), [opsiff](https://github.com/opsiff), [panjd123](https://github.com/panjd123), [Pinghigh](https://github.com/Pinghigh), [Planet6174](https://github.com/Planet6174), [Polaris3003](https://github.com/Polaris3003), [purple-vine](https://github.com/purple-vine), [qiqistyle](https://github.com/qiqistyle), [ree-chee](https://github.com/ree-chee), [RuiYu2021](https://github.com/RuiYu2021), [SaisycJiang](https://github.com/SaisycJiang), [Sheng-Horizon](https://github.com/Sheng-Horizon), [tsawke](https://github.com/tsawke), [TSStudio](https://github.com/TSStudio), [WAAutoMaton](https://github.com/WAAutoMaton), [WillHouMoe](https://github.com/WillHouMoe), [YanWQ-monad](https://github.com/YanWQ-monad)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
