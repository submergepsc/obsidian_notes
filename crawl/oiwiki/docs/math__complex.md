# 复数 - OI Wiki

- Source: https://oi-wiki.org/math/complex/

# 复数

如果您已经学习过复数相关知识，请跳过本页面．

学习复数知识需要一部分向量基础，如果并未学习过向量知识请移步 [向量页面](../linear-algebra/vector/)．

## 复数

### 引入

注

下面的引入方法来自人教版高中数学 A 版必修二．

从方程的角度看，负实数能不能开平方，就是方程 𝑥2 +𝑎 =0(𝑎 >0)x2+a=0(a>0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有没有解，进而可以归结为方程 𝑥2 +1 =0x2+1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有没有解．

回顾已有的数集扩充过程，可以看到，每次扩充都与实际需求密切相关．例如，为了解决正方形对角线的度量，以及 𝑥2 −2 =0x2−2=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这样的方程在有理数集中无解的问题，人们把有理数集扩充到了实数集．数集扩充后，在实数集中规定的加法运算、乘法运算，与原来在有理数集中规定的加法运算、乘法运算协调一致，并且加法和乘法都满足交换律和结合律，乘法对加法满足分配律．

依照这种思想，为了解决 𝑥2 +1 =0x2+1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这样的方程在实数系中无解的问题，我们设想引入一个新数 ii![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑥 =ix=i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是方程 𝑥2 +1 =0x2+1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解，即使得 i2 = −1i2=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

思考：把新引进的数 ii![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 添加到实数集中，我们希望数 ii![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和实数之间仍然能像实数那样进行加法和乘法运算，并希望加法和乘法都满足交换律、结合律，以及乘法对加法满足分配律．那么，实数系经过扩充后，得到的新数系由哪些数组成呢？

依照以上设想，把实数 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 ii![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相乘，结果记作 𝑏ibi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；把实数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑏ibi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相加，结果记作 𝑎 +𝑏ia+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意到所有实数以及 ii![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以写成 𝑎 +𝑏i(𝑎,𝑏 ∈𝐑)a+bi(a,b∈R)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，从而这些数都在扩充后的新数集中．

### 定义

我们定义形如 𝑎 +𝑏ia+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑎,𝑏 ∈𝐑a,b∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数叫做 **复数** ，其中 ii![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被称为 **虚数单位** ，全体复数的集合叫做 **复数集** ，记作 𝐂C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

复数通常用 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示，即 𝑧 =𝑎 +𝑏iz=a+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这种形式被称为 **复数的代数形式** ．其中 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为复数 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **实部** ，记作 Re⁡(𝑧)Re⁡(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为复数 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **虚部** ，记作 Im⁡(𝑧)Im⁡(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如无特殊说明，都有 𝑎,𝑏 ∈𝐑a,b∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于一个复数 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当 𝑏 =0b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，它是实数，当 𝑏 ≠0b≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，它是虚数，当 𝑎 =0a=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑏 ≠0b≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，它是纯虚数．

纯虚数，虚数，实数，复数的关系如下图所示．

![](./images/complex-relation.svg)

## 性质与运算

### 几何意义

我们知道了 𝑎 +𝑏ia+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这样类似的形式的数被称为复数，并且给出了定义和分类，我们还可以挖掘一下更深层的性质．

我们把所有实数都放在了数轴上，并且发现数轴上的点与实数一一对应．我们考虑对复数也这样处理．

首先我们定义 **复数相等** ：两个复数 𝑧1 =𝑎 +𝑏i,𝑧2 =𝑐 +𝑑iz1=a+bi,z2=c+di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是相等的，当且仅当 𝑎 =𝑐a=c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑏 =𝑑b=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这么定义是十分自然的，在此不做过多解释．

也就是说，我们可以用唯一的有序实数对 (𝑎,𝑏)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示一个复数 𝑧 =𝑎 +𝑏iz=a+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这样，联想到平面直角坐标系，我们可以发现 **复数集与平面直角坐标系中的点集一一对应** ．好了，我们找到了复数的一种几何意义．

那么这个平面直角坐标系就不再一般，因为平面直角坐标系中的点具有了特殊意义——表示一个复数，所以我们把这样的平面直角坐标系称为 **复平面** ，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴称为 **实轴** ，𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轴称为 **虚轴** ．我们进一步地说：**复数集与复平面内所有的点所构成的集合是一一对应的** ．

我们考虑到学过的平面向量的知识，发现向量的坐标表示也是一个有序实数对 (𝑎,𝑏)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然，复数 𝑧 =𝑎 +𝑏iz=a+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应复平面内的点 𝑍(𝑎,𝑏)Z(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么它还对应平面向量 ⟶𝑂𝑍 =(𝑎,𝑏)OZ→=(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是我们又找到了复数的另一种几何意义：**复数集与复平面内的向量所构成的集合是一一对应的（实数 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与零向量对应）**．

于是，我们由向量的知识迁移到复数上来，定义 **复数的模** 就是复数所对应的向量的模．复数 𝑧 =𝑎 +𝑏iz=a+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的模 |𝑧| =√𝑎2+𝑏2|z|=a2+b2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

于是为了方便，我们常把复数 𝑧 =𝑎 +𝑏iz=a+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为点 𝑍Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或向量 ⟶𝑂𝑍OZ→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并规定相等的向量表示同一个复数．

并且由向量的知识我们发现，虚数不可以比较大小（但是实数是可以的）．

### 加法与减法

对复数 𝑧1 =𝑎 +𝑏i,𝑧2 =𝑐 +𝑑iz1=a+bi,z2=c+di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义加法规则如下：

𝑧1+𝑧2=(𝑎+𝑐)+(𝑏+𝑑)iz1+z2=(a+c)+(b+d)i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

很明显，两个复数的和仍为复数．

考虑到向量的加法运算，我们发现复数的加法运算符合向量的加法运算法则，这同样证明了复数的几何意义的正确性．

同样可以验证，复数的加法满足 **交换律** 和 **结合律** ．即：

𝑧1+𝑧2=𝑧2+𝑧1(𝑧1+𝑧2)+𝑧3=𝑧1+(𝑧2+𝑧3)z1+z2=z2+z1(z1+z2)+z3=z1+(z2+z3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

减法作为加法的逆运算，我们可以通过加法法则与复数相等的定义来推导出减法法则：

𝑧1−𝑧2=(𝑎−𝑐)+(𝑏−𝑑)iz1−z2=(a−c)+(b−d)i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这同样符合向量的减法运算．

### 乘法、除法与共轭

对复数 𝑧1 =𝑎 +𝑏i,𝑧2 =𝑐 +𝑑iz1=a+bi,z2=c+di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义乘法规则如下：

𝑧1𝑧2=(𝑎+𝑏i)(𝑐+𝑑i)=𝑎𝑐+𝑏𝑐i+𝑎𝑑i+𝑏𝑑i2=(𝑎𝑐−𝑏𝑑)+(𝑏𝑐+𝑎𝑑)iz1z2=(a+bi)(c+di)=ac+bci+adi+bdi2=(ac−bd)+(bc+ad)i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以看出，两个复数相乘类似于两个多项式相乘，只需要把 i2i2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 换成 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将实部与虚部分别合并即可．

复数的乘法与向量的向量积形式类似．

易得复数乘法满足 **交换律** ，**结合律** 和 **对加法的分配律** ，即：

  * 𝑧1𝑧2 =𝑧2𝑧1z1z2=z2z1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * (𝑧1𝑧2)𝑧3 =𝑧1(𝑧2𝑧3)(z1z2)z3=z1(z2z3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑧1(𝑧2 +𝑧3) =𝑧1𝑧2 +𝑧1𝑧3z1(z2+z3)=z1z2+z1z3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于满足运算律，我们可以发现实数域中的 **乘法公式在复数域中同样适用** ．

除法运算是乘法运算的逆运算，我们可以推导一下：

𝑎+𝑏i𝑐+𝑑i=(𝑎+𝑏i)(𝑐−𝑑i)(𝑐+𝑑i)(𝑐−𝑑i)=𝑎𝑐+𝑏𝑑𝑐2+𝑑2+𝑏𝑐−𝑎𝑑𝑐2+𝑑2i(𝑐+𝑑i≠0)a+bic+di=(a+bi)(c−di)(c+di)(c−di)=ac+bdc2+d2+bc−adc2+d2i(c+di≠0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于向量没有除法，这里不讨论与向量的关系．

为了分母实数化，我们乘了一个 𝑐 −𝑑ic−di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这个式子很有意义．

对复数 𝑧 =𝑎 +𝑏iz=a+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称 𝑎 −𝑏ia−bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **共轭复数** ，通常记为 ¯𝑧z¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们可以发现，若两个复数互为共轭复数，那么它们 **关于实轴对称** ．

对复数 𝑧,𝑤z,w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，复数共轭有如下性质

  * 𝑧 ⋅¯𝑧 =|𝑧|2z⋅z¯=|z|2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * ――――𝑧 =𝑧z――=z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * Re⁡(𝑧) =𝑧+¯𝑧2Re⁡(z)=z+z¯2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，Im⁡(𝑧) =𝑧−¯𝑧2Im⁡(z)=z−z¯2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * ――――𝑧±𝑤 =¯𝑧 ±¯𝑤z±w―=z¯±w¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * ―――𝑧𝑤 =¯𝑧¯𝑤zw―=z¯w¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * ―――𝑧/𝑤 =¯𝑧/¯𝑤z/w―=z¯/w¯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 辐角和辐角主值

如果设定实数单位 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为水平正方向，虚数单位 ii![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为竖直正方向，得到的就是直角坐标视角下的复平面．

表示复数 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置，也可以借助于极坐标 (𝑟,𝜃)(r,θ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 确定．前文已经提到了 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为复数 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的模．

从实轴正向到 **非零** 复数 𝑧 =𝑥 +i𝑦z=x+iy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应向量的夹角 𝜃θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足关系：

tan⁡𝜃=𝑦𝑥tan⁡θ=yx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

称为复数 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **辐角** ，记为：

𝜃=arg⁡𝑧θ=arg⁡z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

任一个 **非零** 复数 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有无穷多个辐角，故 arg⁡𝑧arg⁡z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 事实上是一个集合．借助开头大写的 Arg⁡𝑧Arg⁡z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 **其中一个特定值** ，满足条件：

−𝜋<Arg⁡𝑧≤𝜋−π<Arg⁡z≤π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

称 Arg⁡𝑧Arg⁡z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **辐角主值** 或 **主辐角** ．辐角就是辐角主值基础上加若干整数个（可以为零或负整数）2𝑘𝜋2kπ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 arg⁡𝑧 ={Arg⁡𝑧 +2𝑘𝜋 ∣𝑘 ∈𝐙}arg⁡z={Arg⁡z+2kπ∣k∈Z}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

需要注意的是两个辐角主值相加后不一定还是辐角主值，而两个辐角相加一定还是合法的辐角．

称模小于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复数，在复平面上构成的图形为 **单位圆** ．称模等于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复数为 **单位复数** ，全体单位复数在复平面上构成的图形为 **单位圆周** ．在不引起混淆的情况下，有时单位圆周也简称单位圆．

在极坐标的视角下，复数的乘除法变得很简单．复数乘法，模相乘，辐角相加．复数除法，模相除，辐角相减．

### 欧拉公式

欧拉公式（Euler's formula）1

对任意实数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

ei𝑥=cos⁡𝑥+isin⁡𝑥eix=cos⁡x+isin⁡x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在补充 复指数函数与复三角函数 的定义后，该公式可推广至全体复数．

### 指数函数与三角函数

对于复数 𝑧 =𝑥 +i𝑦z=x+iy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，函数 𝑓(𝑧) =e𝑥(cos⁡𝑦 +isin⁡𝑦)f(z)=ex(cos⁡y+isin⁡y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑓(𝑧1 +𝑧2) =𝑓(𝑧1)𝑓(𝑧2)f(z1+z2)=f(z1)f(z2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此给出 **复指数函数** 的定义：

exp⁡𝑧=e𝑥(cos⁡𝑦+isin⁡𝑦)exp⁡z=ex(cos⁡y+isin⁡y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

复指数函数在实数集上与实指数函数的定义完全一致．在复平面上拥有性质：

  * 模恒正：|exp⁡𝑧| =exp⁡𝑥 >0|exp⁡z|=exp⁡x>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 辐角：arg⁡(exp⁡𝑧) ={𝑦 +2𝑘𝜋 ∣𝑘 ∈𝐙}arg⁡(exp⁡z)={y+2kπ∣k∈Z}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 加法定理：exp⁡(𝑧1+𝑧2) =exp⁡(𝑧1)exp⁡(𝑧2)exp⁡(z1+z2)=exp⁡(z1)exp⁡(z2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 周期性：exp⁡𝑧exp⁡z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是以 2𝜋i2πi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为基本周期的周期函数．如果一个函数 𝑓(𝑧)f(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的周期是某一周期的整倍数，称该周期为 **基本周期** ．

**复三角函数** （也简称 **三角函数** ）的定义如下：

cos⁡𝑧=exp⁡(i𝑧)+exp⁡(−i𝑧)2cos⁡z=exp⁡(iz)+exp⁡(−iz)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)sin⁡𝑧=exp⁡(i𝑧)−exp⁡(−i𝑧)2isin⁡z=exp⁡(iz)−exp⁡(−iz)2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若取 𝑧 ∈𝐑z∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则由 欧拉公式 有：

cos⁡𝑧=Re⁡(ei𝑧)cos⁡z=Re⁡(eiz)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)sin⁡𝑧=Im⁡(ei𝑧)sin⁡z=Im⁡(eiz)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

复三角函数在实数集上与实三角函数的定义完全一致．在复平面上拥有性质：

  * 奇偶性：正弦函数是奇函数，余弦函数是偶函数．
  * 三角恒等式：通常的三角恒等式都成立，例如平方和为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或者角的和差公式等．
  * 周期性：正弦与余弦函数以 2𝜋2π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为基本周期．
  * 零点：实正弦与实余弦函数的全体零点，构成了复正弦与复余弦函数的全体零点．这个推广没有引进新的零点．
  * 模的无界性：复正弦与复余弦函数，模长可以大于任意给定的正数，不再像实正弦与实余弦函数一样被限制在 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的范围内．

## 复数的三种形式

借助直角坐标系的视角以及极坐标系的视角，可以写出复数的三种形式．

复数的 **代数形式** 用于表示任意复数．

𝑧=𝑥+𝑦iz=x+yi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代数形式用于计算复数的加减乘除四个运算比较方便．

复数的 **三角形式** 和 **指数形式** ，用于表示非零复数．

𝑧=𝑟(cos⁡𝜃+isin⁡𝜃)=𝑟exp⁡(i𝜃)z=r(cos⁡θ+isin⁡θ)=rexp⁡(iθ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这两种形式用于计算复数的乘除两个运算以及后面的运算较为方便．如果只用高中见过的函数，可以使用三角形式．如果引入了复指数函数，写成等价的指数形式会更加方便．

## 单位根

考察方程 𝑥𝑛 =1xn=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在复数意义下的解．显然，这样的解有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，称这 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个解都是 **𝑛 n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位（复）根**（𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)-th root of unity）．根据复平面的知识，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根把单位圆 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等分．

设 𝜔𝑛 =exp⁡2𝜋i𝑛ωn=exp⁡2πin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即幅角为 2𝜋/𝑛2π/n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的单位复数），则 𝑥𝑛 =1xn=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解集表示为 {𝜔𝑘𝑛 ∣𝑘 =0,1⋯,𝑛 −1}{ωnk∣k=0,1⋯,n−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，

𝑤𝑘𝑛=exp⁡2𝜋𝑘i𝑛=cos⁡2𝜋𝑘𝑛+isin⁡2𝜋𝑘𝑛.wnk=exp⁡2πkin=cos⁡2πkn+isin⁡2πkn.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果不加说明，一般叙述中的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根，是指从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始逆时针方向的第一个解，即上述 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其它解均可以用 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂表示．

为什么通常提到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根，总是特指第一个？

主要是为了应用时方便．所有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根都可以表示为第一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次；而且，对于任意 𝑘 <𝑛k<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，复数 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都不是 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根．

### 本原单位根

事实上，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根中满足类似性质的不止 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一个．称集合

{𝜔𝑘𝑛∣0≤𝑘<𝑛, gcd(𝑛,𝑘)=1}{ωnk∣0≤k<n, gcd(n,k)=1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

中的元素为 **𝑛 n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次本原单位根**（𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)-th primitive root of unity）．根据上述表达式可知，全体 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次本原单位根共有 𝜑(𝑛)φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，其中，𝜑(𝑛)φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 [欧拉函数](../number-theory/euler-totient/)．

任意一个本原单位根 𝜔ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都与上述 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 具有相同的性质：对于任意的 0 <𝑘 <𝑛0<k<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝜔ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂不为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，𝜔ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根．因此，借助任意一个本原单位根，都可以生成全体单位根．

为了理解 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次本原单位根的结构，需要考虑单位根的如下性质：

性质

对于整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设 𝑑 =gcd(𝑛,𝑘)d=gcd(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜔𝑘𝑛 =𝜔𝑘/𝑑𝑛/𝑑ωnk=ωn/dk/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

直接计算可知

𝑤𝑘𝑛=exp⁡2𝜋𝑘i𝑛=exp⁡2𝜋(𝑘/𝑑)i𝑛/𝑑=𝜔𝑘/𝑑𝑛/𝑑.wnk=exp⁡2πkin=exp⁡2π(k/d)in/d=ωn/dk/d.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这说明，只要 gcd(𝑛,𝑘) ≠1gcd(n,k)≠1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，𝜔𝑘𝑛ωnk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就一定是 𝑛gcd(𝑛,𝑘)ngcd(n,k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次（本原）单位根．因此，满足前述性质的单位根 𝜔𝑘𝑛ωnk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定是满足 gcd(𝑛,𝑘) =1gcd(n,k)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这正是本原单位根具有上述定义的原因．

另外，作为这些分析的简单推论，有：

定理

当 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的因数，所有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次本原单位根恰构成 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根的一个划分．而且，对于 ℓ ⟂𝑛ℓ⟂n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，映射 𝑥 ↦𝑥ℓx↦xℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 给出 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根之间的双射，且保持上述划分不变：它将 𝑘 ∣𝑛k∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次本原单位根仍然映射到 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次本原单位根．

尽管本原单位根有很多选择，但是由于第一个根 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 形式最为简单，算法竞赛中还是 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最为常用．对于部分场景，为提高计算效率，还可以考虑用某一模数下的 [本原单位根](../number-theory/residue/#单位根) 代替复数域中的 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 编程语言中的复数

### C 中的复数

在 C99 标准中，有 `<complex.h>` 头文件．

在 `<complex.h>` 头文件中，提供了 `double complex`、`float complex` 和 `long double complex` 三种类型．

算术运算符'+'、'-'、'*'和'/'，可以用于浮点数和复数的任意混合．当表达式两端有一个为复数时，计算结果为复数．

头文件 `<complex.h>` 提供了虚数单位 `I`，引入此头文件时，大写字母 `I` 不可以作为变量名使用．

对于单个复数，`<complex.h>` 提供了若干操作：`creal` 函数用于提取实部，`cimag` 函数用于提取虚部，`cabs` 函数用于计算模，`carg` 函数用于计算辐角主值．

所有的函数根据类型不同，都有三个．例如 `creal` 函数有 `creal`、`crealf`、`creall` 三个，用于处理对应的 `double`、`float` 和 `long double` 三种类型．末尾什么都不带的默认处理 `double` 类型．以下所有函数均遵从此规律，不再特别说明．

这些函数返回值都是一般的浮点数．可以将普通浮点数直接赋值给复数，但是不可以将复数直接赋值给浮点数，而是需要使用上述提取操作．

函数 `conj` 用于计算共轭复数，返回值是复数．

函数 `cexp` 计算复指数，`clog` 计算对数主值，`csin` 计算正弦，`ccos` 计算余弦，`ctan` 计算正切．

函数 `cpow` 计算幂函数，`csqrt` 计算平方根，`casin` 计算反正弦，`cacos` 计算反余弦，`catan` 计算反正切．这部分函数计算的全部都是多值函数的主值．

### C++ 中的复数

在 C 里面的 `<ctype.h>`，到 C++ 会变成 `<cctype>`，几乎所有的头文件遵从这个命名规律．

但是，`<complex.h>` 不遵守，C++ 没有 `<ccomplex>` 头文件．C++ 的复数直接是 `<complex>`，并且装的东西和 C 完全不一样．

很有趣．这是因为，在 C++ 的第一个版本 C++98，即已经有了 `<complex>`，而 C 语言在 C99 才添加．

在 C++ 中，复数类型定义使用 `complex<float>`、`complex<double>` 和 `complex<long double>`．由于面向对象的多态性，下面函数的名字都是唯一的，无需 f 或 l 的后缀．

一个复数对象拥有成员函数 `real` 和 `imag`，可以访问实部和虚部．

一个复数对象拥有非成员函数 `real`、`imag`、`abs`、`arg`，返回实部、虚部、模和辐角．

一个复数对象还拥有非成员函数：`norm` 为模的平方，`conj` 为共轭复数．

一个复数对象还拥有非成员函数 `exp`、`log`（底为 ee![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对数主值）、`log10`（底为 10 的对数主值，C 中没有）、`pow`、`sqrt`、`sin`、`cos`、`tan`，含义与 C 中的含义相同．

在 C++14 及以后的版本中，定义了 [字面量运算符 `std::literals::complex_literals::""if, ""i, ""il`](https://zh.cppreference.com/w/cpp/numeric/complex/operator%2522%2522i.html)．例如输入 `100if`、`100i` 和 `100il`，三者将分别返回 `std::complex<float>{0.0f, 100.0f}`、`std::complex<double>{0.0, 100.0}` 以及 `std::complex<long double>{0.0l, 100.0l}`．这使得我们可以方便地书写形如 `auto z = 4.0 + 3i` 的复数声明．

## 参考资料与链接

  * [Complex number - Wikipedia](https://en.wikipedia.org/wiki/Complex_number)
  * [Euler's formula - Wikipedia](https://en.wikipedia.org/wiki/Euler's_formula)
  * [Complex number arithmetic - cppreference.com](https://en.cppreference.com/w/c/numeric/complex)
  * [std::complex - cppreference.com](https://en.cppreference.com/w/cpp/numeric/complex)

* * *

  1. 有关欧拉公式的更多介绍，可以参考两个视频：[欧拉公式与初等群论](https://www.bilibili.com/video/BV1fx41187tZ)、[微分方程概论 - 第五章：在 3.14 分钟内理解 ei𝜋eiπ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://www.bilibili.com/video/BV1G4411D7kZ)． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/complex.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/complex.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [HeRaNO](https://github.com/HeRaNO), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [MegaOwIer](https://github.com/MegaOwIer), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [sshwy](https://github.com/sshwy), [CCXXXI](https://github.com/CCXXXI), [CharlesWuQiushi](https://github.com/CharlesWuQiushi), [chinggg](https://github.com/chinggg), [iamtwz](https://github.com/iamtwz), [mcendu](https://github.com/mcendu), [megakite](https://github.com/megakite), [ouuan](https://github.com/ouuan), [r-value](https://github.com/r-value), [StudyingFather](https://github.com/StudyingFather), [TSStudio](https://github.com/TSStudio)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
