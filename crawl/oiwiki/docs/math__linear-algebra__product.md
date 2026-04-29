# 内积和外积 - OI Wiki

- Source: https://oi-wiki.org/math/linear-algebra/product/

# 内积和外积

本文介绍向量之间的简单运算．

在本文之前，特别说明一下翻译的相关问题．由于历史原因，数学学科和物理学科关于「inner product」和「outer product」两个词汇有着五花八门的翻译．

在物理学科，一般翻译成「标积」和「矢积」，表示运算的结果为标量和矢量．高中数学课本上「数量积」和「向量积」也采用了这种意译的办法．

在数学学科，通常也可以翻译成「内积」和「外积」，是两个名词的直译．「点乘」和「叉乘」是根据运算符号得来的俗称，这种俗称也很常见．

在「点乘」运算中，经常省略运算的点符号，在线性代数中更是会直接看作矩阵乘法，不写点符号．

## 内积

内积的概念 **对于任意维数的向量都适用** ．

### 定义

内积有不同但等价的定义方法，下面介绍其中一些．

#### 几何定义

在 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维欧氏空间 𝐑𝑛Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下，已知两个向量 𝒂,𝒃a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它们的夹角为 𝜃θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么：

𝒂⋅𝒃=|𝒂||𝒃|cos⁡𝜃a⋅b=|a||b|cos⁡θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就是这两个向量的 **内积** ，也叫 **点积** 或 **数量积** ．其中称 |𝒃|cos⁡𝜃|b|cos⁡θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 方向上的投影．内积的几何意义即为：内积 𝒂 ⋅𝒃a⋅b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等于 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的模与 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 方向上的投影的乘积．

#### 代数定义

在 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维欧氏空间 𝐑𝑛Rn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下，已知两个向量 𝒂 =(𝑎1,𝑎2,…,𝑎𝑛),𝒃 =(𝑏1,𝑏2,…,𝑏𝑛)a=(a1,a2,…,an),b=(b1,b2,…,bn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么：

𝒂⋅𝒃=𝑛∑𝑖=1𝑎𝑖𝑏𝑖a⋅b=∑i=1naibi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就是这两个向量的 **内积** ，也叫 **点积** 或 **数量积** ．内积的几何定义与代数定义在欧氏空间下是等价的，而后者更方便使用．

在不引起混淆的情况下，内积的点号可以省略不写．如果在向量的右上角有上角标 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示向量与自身内积的简写，即 **向量模长的平方** ，省略模长记号．该上角标 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不可以理解为向量的平方，这是因为，向量内积的结果为标量，不存在除了 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以外任何个数的向量的内积．同理，向量模长平方的平方，不可以简写为上角标 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而是必须将上角标 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结果视为一个整体，以此类推．

### 性质

可以发现，内积得到的结果是一个标量，其特别之处在于，它是关于两个向量分别都线性的双线性运算．具体而言，内积满足：

(𝒂+𝒃)⋅𝒄=𝒂⋅𝒄+𝒃⋅𝒄𝒂⋅(𝒃+𝒄)=𝒂⋅𝒃+𝒂⋅𝒄(𝜆𝒂)⋅𝒃=𝜆(𝒂⋅𝒃)𝒂⋅(𝜆𝒃)=𝜆(𝒂⋅𝒃)(a+b)⋅c=a⋅c+b⋅ca⋅(b+c)=a⋅b+a⋅c(λa)⋅b=λ(a⋅b)a⋅(λb)=λ(a⋅b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

内积还满足交换律，即：

𝒂⋅𝒃=𝒃⋅𝒂a⋅b=b⋅a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 应用

下面介绍内积运算的一些常见应用．

  1. 判定两向量垂直：

𝒂⟂𝒃⟺𝒂⋅𝒃=0a⟂b⟺a⋅b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即互相垂直的两个向量的内积，结果为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；向量与零向量内积，结果为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果使用内积为零作为垂直的定义，则可以得出零向量与任何向量都垂直．

  2. 判定两向量共线：

∃𝜆∈𝐑(𝒂=𝜆𝒃)⟺|𝒂⋅𝒃|=|𝒂||𝒃|∃λ∈R(a=λb)⟺|a⋅b|=|a||b|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. 计算向量的模：

|𝒂|=√𝒂⋅𝒂|a|=a⋅a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. 计算两向量的夹角：

𝜃=arccos⁡𝒂⋅𝒃|𝒂||𝒃|θ=arccos⁡a⋅b|a||b|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 二阶与三阶行列式

二阶与三阶行列式，可以作为行列式的较为简单的情形特殊定义．在微积分的最后一个部分场论部分，格林公式用到了二阶行列式，高斯公式用到了点乘，斯托克斯公式用到了三阶行列式．

二阶行列式可以视为四元函数，其定义为：

∣𝑎𝑏𝑐𝑑∣=𝑎𝑑−𝑏𝑐|abcd|=ad−bc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

三阶行列式可以视为九元函数，其定义为：

∣𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖∣=𝑎𝑒𝑖+𝑑ℎ𝑐+𝑔𝑏𝑓−𝑎ℎ𝑓−𝑑𝑏𝑖−𝑔𝑒𝑐|abcdefghi|=aei+dhc+gbf−ahf−dbi−gec![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

一种特殊的记忆方法是采用「对角线法则」，对角线法则只适用于二阶与三阶行列式．

特别注意：四阶行列式展开后共有 24 项，并且副对角线一项的符号为正．如果强行应用三阶行列式的「对角线法则」，不仅项数不够，副对角线一项的符号也不正确，因此三阶行列式的「对角线法则」不适用于更高阶的行列式，更高阶的行列式也不适合使用直接展开法计算．

## 外积

外积是 **三维向量特有的运算** ．

在物理学中，三维向量为默认与空间位置相关的向量，一律采用粗体表示．然而，物理学中与相对论相关的四维向量不会采用粗体，而是使用特殊的记号与下标．

在线性代数中，所有的向量都会用粗体表示，并且由于麻烦，并且线性代数中大多为向量与矩阵的运算，很难造成歧义，在手写时可以省略向量记号不写．

### 定义

外积有不同但等价的定义方法，下面介绍其中一些．

#### 几何定义

在三维欧氏空间 𝐑3R3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下，定义向量 𝒂,𝒃a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的外积为一个向量，记为 𝒂 ×𝒃a×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其模与方向定义如下：

  1. |𝒂 ×𝒃| =|𝒂||𝒃|sin⁡⟨𝒂,𝒃⟩|a×b|=|a||b|sin⁡⟨a,b⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 𝒂 ×𝒃a×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝒂,𝒃a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都垂直，且 𝒂,𝒃,𝒂 ×𝒃a,b,a×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方向符合右手法则．

注意到外积的模，联想到三角形面积计算公式 𝑆 =12𝑎𝑏sin⁡𝐶S=12absin⁡C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以发现外积的几何意义是：**| 𝒂 ×𝒃||a×b|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是以 𝒂,𝒃a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为邻边的平行四边形的面积**．

#### 代数定义

在三维欧氏空间 𝐑3R3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下，定义向量 𝒂 =(𝑥1,𝑦1,𝑧1),𝒃 =(𝑥2,𝑦2,𝑧2)a=(x1,y1,z1),b=(x2,y2,z2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的外积为一个向量 𝒄c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记作 𝒄 =𝒂 ×𝒃c=a×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其结果可以使用三阶行列式表示：

∣𝒊𝒋𝒌𝑥1𝑦1𝑧1𝑥2𝑦2𝑧2∣|ijkx1y1z1x2y2z2|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝒊,𝒋,𝒌i,j,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示朝向为坐标轴 𝑥,𝑦,𝑧x,y,z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的单位向量，并写在对应坐标处．展开得

𝒄=𝒂×𝒃=(𝑦1𝑧2−𝑦2𝑧1)𝒊+(𝑧1𝑥2−𝑧2𝑥1)𝒋+(𝑥1𝑦2−𝑥2𝑦1)𝒌=(𝑦1𝑧2−𝑦2𝑧1,𝑧1𝑥2−𝑧2𝑥1,𝑥1𝑦2−𝑥2𝑦1)c=a×b=(y1z2−y2z1)i+(z1x2−z2x1)j+(x1y2−x2y1)k=(y1z2−y2z1,z1x2−z2x1,x1y2−x2y1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 性质

  1. 外积是关于两个向量分别都线性的双线性运算．具体而言，外积满足：

(𝒂+𝒃)×𝒄=𝒂×𝒄+𝒃×𝒄𝒂×(𝒃+𝒄)=𝒂×𝒃+𝒂×𝒄(𝜆𝒂)×𝒃=𝜆(𝒂×𝒃)𝒂×(𝜆𝒃)=𝜆(𝒂×𝒃)(a+b)×c=a×c+b×ca×(b+c)=a×b+a×c(λa)×b=λ(a×b)a×(λb)=λ(a×b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

前两行性质亦可称为分配律，即外积对于向量加法满足乘法分配律．

  2. 外积满足反交换律，即：

𝒂×𝒃=−𝒃×𝒂a×b=−b×a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. 根据上文内积与外积的几何定义：

|𝒂×𝒃|=|𝒂||𝒃|sin⁡⟨𝒂,𝒃⟩𝒂⋅𝒃=|𝒂||𝒃|cos⁡𝜃=|𝒂||𝒃|cos⁡⟨𝒂,𝒃⟩|a×b|=|a||b|sin⁡⟨a,b⟩a⋅b=|a||b|cos⁡θ=|a||b|cos⁡⟨a,b⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以写出恒等式：

(𝒂×𝒃)⋅(𝒂×𝒃)=|𝒂|2|𝒃|2−(𝒂⋅𝒃)2(a×b)⋅(a×b)=|a|2|b|2−(a⋅b)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. 外积满足 Jacobi 恒等式：

𝒂×(𝒃×𝒄)+𝒃×(𝒄×𝒂)+𝒄×(𝒂×𝒃)=𝟎a×(b×c)+b×(c×a)+c×(a×b)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 应用

下面介绍外积运算的一些常见应用．

  1. 判定两向量是否共线：

∃𝜆∈𝐑(𝒂=𝜆𝒃)⟺𝒂×𝒃=𝟎∃λ∈R(a=λb)⟺a×b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即共线的两个三维向量的外积，结果为 𝟎0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；三维向量与自身外积，结果为 𝟎0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；三维向量与零向量外积，结果为 𝟎0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若使用外积为零作为两向量共线的定义，则可以得出零向量与任何向量都共线．

  2. 计算两向量张成的平行四边形面积：

𝑆⟨𝒂,𝒃⟩=|𝒂×𝒃|S⟨a,b⟩=|a×b|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

#### 二维向量的情形

对于二维向量，无法计算外积，但是仍然可以计算两向量张成的平行四边形面积：

记 𝒂 =(𝑚,𝑛),𝒃 =(𝑝,𝑞)a=(m,n),b=(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将平面直角坐标系扩充为空间直角坐标系，原平面位于新坐标系的 𝑥𝑂𝑦xOy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 平面，原本的坐标 (𝑚,𝑛)(m,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑝,𝑞)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为 (𝑚,𝑛,0)(m,n,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑝,𝑞,0)(p,q,0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

那么两个向量的外积为 (0,0,𝑚𝑞 −𝑛𝑝)(0,0,mq−np)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此平行四边形的面积为 |𝑚𝑞 −𝑛𝑝||mq−np|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以视为二阶行列式运算结果的绝对值．

此时，根据右手法则和 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 坐标的符号，可以推断出 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相对于 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方向，若在逆时针方向则 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 坐标为正值，反之为负值，简记为 **顺负逆正** ．

## 混合积

与外积一样，向量的混合积是 **三维向量特有的运算** ．

### 定义

设 𝒂,𝒃,𝒄a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是三维空间中的三个向量，则 (𝒂 ×𝒃) ⋅𝒄(a×b)⋅c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为三个向量 𝒂,𝒃,𝒄a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的混合积，记作 [𝒂𝒃𝒄][abc]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 (𝒂,𝒃,𝒄)(a,b,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 (𝒂𝒃𝒄)(abc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 det⁡(𝒂,𝒃,𝒄)det⁡(a,b,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．混合积的绝对值 |(𝒂 ×𝒃) ⋅𝒄||(a×b)⋅c|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的几何意义表示以 𝒂,𝒃,𝒄a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为棱的平行六面体的体积．

向量的混合积可以使用三阶行列式表示：

(𝒂×𝒃)⋅𝒄=det⁡(𝒂,𝒃,𝒄)=∣𝑎𝑥𝑏𝑥𝑐𝑥𝑎𝑦𝑏𝑦𝑐𝑦𝑎𝑧𝑏𝑧𝑐𝑧∣=𝑎𝑥𝑏𝑦𝑐𝑧+𝑎𝑦𝑏𝑧𝑐𝑥+𝑎𝑧𝑏𝑥𝑐𝑦−𝑎𝑧𝑏𝑦𝑐𝑥−𝑎𝑦𝑏𝑥𝑐𝑧−𝑎𝑥𝑏𝑧𝑐𝑦(a×b)⋅c=det⁡(a,b,c)=|axbxcxaybycyazbzcz|=axbycz+aybzcx+azbxcy−azbycx−aybxcz−axbzcy![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 性质

  1. 混合积关于三个向量都分别线性，具体而言，有：

det⁡(𝜆𝒖+𝜇𝒗,𝒃,𝒄)=𝜆det⁡(𝒖,𝒃,𝒄)+𝜇det⁡(𝒗,𝒃,𝒄)det⁡(𝒂,𝜆𝒖+𝜇𝒗,𝒄)=𝜆det⁡(𝒂,𝒖,𝒄)+𝜇det⁡(𝒂,𝒗,𝒄)det⁡(𝒂,𝒃,𝜆𝒖+𝜇𝒗)=𝜆det⁡(𝒂,𝒃,𝒖)+𝜇det⁡(𝒂,𝒃,𝒗)det⁡(λu+μv,b,c)=λdet⁡(u,b,c)+μdet⁡(v,b,c)det⁡(a,λu+μv,c)=λdet⁡(a,u,c)+μdet⁡(a,v,c)det⁡(a,b,λu+μv)=λdet⁡(a,b,u)+μdet⁡(a,b,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 混合积具有反对称性，交换两个向量的位置会使混合积变成其相反数，因此有：

det⁡(𝒂,𝒃,𝒄)=det⁡(𝒃,𝒄,𝒂)=det⁡(𝒄,𝒂,𝒃)=−det⁡(𝒃,𝒂,𝒄)=−det⁡(𝒂,𝒄,𝒃)=−det⁡(𝒄,𝒃,𝒂)det⁡(a,b,c)=det⁡(b,c,a)=det⁡(c,a,b)=−det⁡(b,a,c)=−det⁡(a,c,b)=−det⁡(c,b,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

据此还可以得到内积与外积有如下关系：

(𝒂×𝒃)⋅𝒄=𝒂⋅(𝒃×𝒄)(a×b)⋅c=a⋅(b×c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 应用

向量的混合积有如下常见应用．

  1. 计算四面体 𝐴𝐵𝐶𝐷ABCD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的体积：

𝑉=16∣det⁡(⟶𝐴𝐵,⟶𝐴𝐶,⟶𝐴𝐷)∣V=16|det⁡(AB→,AC→,AD→)|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 判定 𝒂,𝒃,𝒄a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否共面；

三个三维向量 𝒂,𝒃,𝒄a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共面的充分必要条件是 det⁡(𝒂,𝒃,𝒄) =0det⁡(a,b,c)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  3. 判定 𝒂,𝒃,𝒄a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成的坐标系的手性；

混合积 det⁡(𝒂,𝒃,𝒄)det⁡(a,b,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的符号是正还是负，取决于 𝒂 ×𝒃a×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝒄c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 形成的夹角是锐角还是钝角，即指向 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 张成平面的同侧还是异侧，这相当于 𝒂,𝒃,𝒄a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 三个向量依序构成右手系还是左手系．具体而言：

     * det⁡(𝒂,𝒃,𝒄) <0det⁡(a,b,c)<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价于 𝒂,𝒃,𝒄a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 依序构成左手系；
     * det⁡(𝒂,𝒃,𝒄) >0det⁡(a,b,c)>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价于 𝒂,𝒃,𝒄a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 依序构成右手系．

## 二重外积

三维向量的混合积是内积与外积的混搭，具有轮换对称性．三维向量和三维向量的外积还是三维向量，那么外积的外积是否存在相关结论？

先证明一个引理．

(𝒂×𝒃)×𝒂=(𝒂⋅𝒂)𝒃−(𝒂⋅𝒃)𝒂(a×b)×a=(a⋅a)b−(a⋅b)a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明：由右手定则，𝒂 ×𝒃a×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都垂直，待证等式左端与 𝒂 ×𝒃a×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 垂直，因此待证等式左端与 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共面．

因此可以假设：

(𝒂×𝒃)×𝒂=𝜆𝒂+𝜇𝒃(a×b)×a=λa+μb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据混合积的相关结论，上式两端同时对于 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别做内积，有：

𝜆(𝒂⋅𝒂)+𝜇(𝒂⋅𝒃)=0𝜆(𝒂⋅𝒃)+𝜇(𝒃⋅𝒃)=det⁡(𝒃,𝒂×𝒃,𝒂)=(𝒂×𝒃)⋅(𝒂×𝒃)λ(a⋅a)+μ(a⋅b)=0λ(a⋅b)+μ(b⋅b)=det⁡(b,a×b,a)=(a×b)⋅(a×b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由前文推出的恒等式：

(𝒂×𝒃)⋅(𝒂×𝒃)=|𝒂|2|𝒃|2−(𝒂⋅𝒃)2(a×b)⋅(a×b)=|a|2|b|2−(a⋅b)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以解得：

𝜆=−𝒂⋅𝒃𝜇=𝒂⋅𝒂λ=−a⋅bμ=a⋅a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证毕．

在上文的证明中提到，𝒂 ×𝒃a×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与任意向量叉乘，得到的向量与 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共面．接下来证明 **二重外积** 的结论：

(𝒂×𝒃)×𝒄=(𝒂⋅𝒄)𝒃−(𝒃⋅𝒄)𝒂(a×b)×c=(a⋅c)b−(b⋅c)a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上述共面性有助于二重外积结论的记忆．可见，上文的引理为二重外积的特殊情况．

证明：这里只需考虑三个向量均为非零且不共线的情况，其他特例为显然的．

三维向量 𝒂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝒃b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝒂 ×𝒃a×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不共面，因此可以假设：

𝒄=𝛼𝒂+𝛽𝒃+𝛾(𝒂×𝒃)c=αa+βb+γ(a×b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以有：

(𝒂×𝒃)×𝒄=(𝒂×𝒃)×(𝛼𝒂+𝛽𝒃+𝛾(𝒂×𝒃))=𝛼(𝒂×𝒃)×𝒂+𝛽(𝒂×𝒃)×𝒃(a×b)×c=(a×b)×(αa+βb+γ(a×b))=α(a×b)×a+β(a×b)×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据上文的引理有：

(𝒂×𝒃)×𝒂=(𝒂⋅𝒂)𝒃−(𝒂⋅𝒃)𝒂(𝒂×𝒃)×𝒃=−(𝒃×𝒂)×𝒃=−(𝒃⋅𝒃)𝒂+(𝒂⋅𝒃)𝒃(a×b)×a=(a⋅a)b−(a⋅b)a(a×b)×b=−(b×a)×b=−(b⋅b)a+(a⋅b)b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此有：

(𝒂×𝒃)×𝒄=𝛼((𝒂⋅𝒂)𝒃−(𝒂⋅𝒃)𝒂)+𝛽((𝒂⋅𝒃)𝒃−(𝒃⋅𝒃)𝒂)=(𝛼(−𝒂⋅𝒃)+𝛽(−𝒃⋅𝒃))𝒂+(𝛼𝒂⋅𝒂+𝛽𝒂⋅𝒃)𝒃=(𝒂⋅𝒄)𝒃−(𝒃⋅𝒄)𝒂(a×b)×c=α((a⋅a)b−(a⋅b)a)+β((a⋅b)b−(b⋅b)a)=(α(−a⋅b)+β(−b⋅b))a+(αa⋅a+βa⋅b)b=(a⋅c)b−(b⋅c)a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证毕．

根据外积的反交换性，可以得到二重外积的两个公式：

(𝒂×𝒃)×𝒄=(𝒂⋅𝒄)𝒃−(𝒃⋅𝒄)𝒂𝒂×(𝒃×𝒄)=(𝒂⋅𝒄)𝒃−(𝒂⋅𝒃)𝒄(a×b)×c=(a⋅c)b−(b⋅c)aa×(b×c)=(a⋅c)b−(a⋅b)c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可见，二重外积对于运算顺序有着严格的要求．

借助混合积与二重外积，还可以证明拉格朗日的恒等式．

(𝒂×𝒃)⋅(𝒄×𝒅)=(𝒂⋅𝒄)(𝒃⋅𝒅)−(𝒂⋅𝒅)(𝒃⋅𝒄)(a×b)⋅(c×d)=(a⋅c)(b⋅d)−(a⋅d)(b⋅c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明：

(𝒂×𝒃)⋅(𝒄×𝒅)=det⁡(𝒄,𝒅,𝒂×𝒃)=det⁡(𝒂×𝒃,𝒄,𝒅)=((𝒂×𝒃)×𝒄)⋅𝒅=(𝒃(𝒂⋅𝒄)−𝒂(𝒃⋅𝒄))⋅𝒅=(𝒂⋅𝒄)(𝒃⋅𝒅)−(𝒂⋅𝒅)(𝒃⋅𝒄)(a×b)⋅(c×d)=det⁡(c,d,a×b)=det⁡(a×b,c,d)=((a×b)×c)⋅d=(b(a⋅c)−a(b⋅c))⋅d=(a⋅c)(b⋅d)−(a⋅d)(b⋅c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可见，前文的恒等式

(𝒂×𝒃)⋅(𝒂×𝒃)=|𝒂|2|𝒃|2−(𝒂⋅𝒃)2(a×b)⋅(a×b)=|a|2|b|2−(a⋅b)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

是拉格朗日的恒等式的特殊情形．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-algebra/product.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/linear-algebra/product.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Great-designer](https://github.com/Great-designer), [CCXXXI](https://github.com/CCXXXI), [Nanarikom](https://github.com/Nanarikom), [untitledunrevised](https://github.com/untitledunrevised)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
