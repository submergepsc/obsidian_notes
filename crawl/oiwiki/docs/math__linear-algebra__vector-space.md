# 线性空间 - OI Wiki

- Source: https://oi-wiki.org/math/linear-algebra/vector-space/

# 线性空间

线性空间是 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维欧氏空间（0 ≤𝑑 ≤30≤d≤3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）等的推广，相关概念的关系可参照 欧氏空间与线性空间的关系．

前置知识：阿贝尔群、域．

通俗地讲，一个集合关于某运算封闭，满足结合律、单位元与逆元则构成群．如果还满足交换律，则构成阿贝尔群．

如果一个集合关于四则运算封闭，则构成域．相关定义详见 [抽象代数基本概念](../../algebra/basic/#域)．

## 定义

线性空间（向量空间）是线性代数的基本概念与重要研究对象．线性空间是由向量集合 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、加法运算 ++![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和标量乘法（数乘）组成的模类代数结构．

具体来说，设 (𝑉, +)(V,+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个阿贝尔群，ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个域．

定义 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的数与 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素的一种代数运算，称为 **数乘** ：⋅ :ℙ ×𝑉 ↦𝑉⋅:P×V↦V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记为 𝑝 ⋅𝑣p⋅v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑝𝑣pv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在阿贝尔群 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．要求该数乘运算是封闭的，运算结果始终有意义，也在群 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中．

且满足以下条件：

  1. **数乘对向量加法分配律** ：对于 𝐮,𝐯 ∈𝑉,𝑎 ∈ℙu,v∈V,a∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑎(𝐮 +𝐯) =𝑎𝐮 +𝑎𝐯a(u+v)=au+av![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. **数乘对标量加法分配律** ：对于 𝑎,𝑏 ∈ℙ,𝐮 ∈𝑉a,b∈P,u∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，(𝑎 +𝑏)𝐮 =𝑎𝐮 +𝑏𝐮(a+b)u=au+bu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. **数乘结合律（一致于域乘法）** ：对于 𝑎,𝑏 ∈ℙ,𝐮 ∈𝑉a,b∈P,u∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑎(𝑏𝐮) =(𝑎𝑏)𝐮a(bu)=(ab)u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. **标量乘法单位元** ：令 1 ∈ℙ1∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘法单位元，则对于 𝑢 ∈𝑉u∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1𝐮 =𝐮1u=u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则称代数系统 (𝑉, +, ⋅,ℙ)(V,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于 +, ⋅+,⋅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的一个 **线性空间** ，ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为线性空间的 **基域** ，𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素称为 **向量** ，ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素称为 **标量** ．当域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为实数域时，称为实线性空间．当域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为复数域时，称为复线性空间．

不管是一列数还是箭头，或是别的什么东西，只要满足上述公理，都可以认为是向量，也就都可以利用线性代数的理论来研究．

称加法群中的零元为零向量，记作 𝟎0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝜃θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

原阿贝尔群中向量的加减法，与线性空间新定义的数乘，统称为 **线性运算** ．

Note

为行文方便，下文中：

  1. 对 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素不做加粗处理．
  2. 将满足线性空间定义的代数系统 (𝑉, +, ⋅,ℙ)(V,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也称为线性空间．

请注意区分．

### 直观理解

不是很严谨地说，标量乘法对应着一种「**缩放** 」，基域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素就代表着缩放的「**比例** 」，向量加法对应「**叠加** 」．同时，ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素还代表着向量的「**坐标** 」的取值范围．

条件 1-4 描述的是「缩放」与「叠加」的关联．可以结合二维平面上的箭头来理解．

### 简单性质

Note

以下性质可在群论等中找到．

对线性空间 (𝑉, +, ⋅,ℙ)(V,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),

  1. 𝜃θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 唯一
  2. ∀𝛼 ∈𝑉∀α∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),−𝛼−α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 唯一
  3. ∃0 ∈ℙ∃0∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),∀𝛼 ∈𝑉∀α∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 有 0𝛼 =𝜃0α=θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. ∀𝑘 ∈ℙ∀k∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 有 𝑘𝜃 =𝜃kθ=θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  5. ( −1)𝛼 = −𝛼, ∀𝛼 ∈𝑉(−1)α=−α, ∀α∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  6. 无零因子：∀𝛼 ∈𝑉,𝑘 ∈ℙ∀α∈V,k∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 有 𝑘𝛼 =𝜃 ⟹ 𝑘 =0 ∨𝛼 =𝜃kα=θ⟹k=0∨α=θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  7. 加法的消去律：∀𝛼,𝛽,𝛾 ∈𝑉∀α,β,γ∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 有 𝛼 +𝛽 =𝛼 +𝛾 ⟹ 𝛽 =𝛾α+β=α+γ⟹β=γ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

> 实际上，加法的消去律是阿贝尔群的性质．

### 例子

  1. ℙ𝑛Pn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于数域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的加法和乘法构成 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的一个线性空间．例如 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以是 ℝR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),ℂC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),ℕ𝑝Np![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为素数）等．
  2. 数域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶矩阵 ℙ𝑛×𝑚Pn×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于矩阵的加法和数乘构成 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的一个线性空间．
  3. 数域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的一元多项式环 ℙ[𝑥]P[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于多项式的加法和数乘构成 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的一个线性空间．
  4. 区间 [𝑎,𝑏][a,b]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的全体连续函数（记作 𝐶[𝑎,𝑏]C[a,b]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）关于「函数加法」和「值与连续函数的数乘」构成值域上的一个线性空间．

## 相关概念

### 线性相关、线性无关

对线性空间 (𝑉, +, ⋅,ℙ)(V,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

  1. 称 𝑎1,𝑎2,…,𝑎𝑛 ∈𝑉a1,a2,…,an∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个 **向量组** ．
  2. 对于 𝑘1,𝑘2,…,𝑘𝑛 ∈ℙk1,k2,…,kn∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 称 ∑𝑛𝑖=1𝑘𝑖𝑎𝑖∑i=1nkiai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个 **线性组合** ．
  3. 若向量 𝛽 ∈𝑉β∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以表示为向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个线性组合，则称 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能被向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **线性表出** ．
  4. 对于 𝑘1,𝑘2,…,𝑘𝑛 ∈ℙk1,k2,…,kn∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 若向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 ∑𝑛𝑖=1𝑘𝑖𝑎𝑖 =𝜃 ⟺ 𝑘𝑖 =0,𝑖 =1,2,…,𝑛∑i=1nkiai=θ⟺ki=0,i=1,2,…,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则称向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **线性无关** ，否则称向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **线性相关** ．

规定零向量与任意向量线性相关．

线性表示或线性相关的式子，可以写成矩阵乘法的形式：

𝛽=𝑘1𝑎1+𝑘2𝑎2+⋯+𝑘𝑟𝑎𝑟=(𝑎1,𝑎2,⋯,𝑎𝑟)⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝𝑘1𝑘2⋮𝑘𝑟⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠β=k1a1+k2a2+⋯+krar=(a1,a2,⋯,ar)(k1k2⋮kr)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据习惯，把向量 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 按顺序并排写在左边；把标量 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 按顺序竖着写在右边，构成一个「列向量」．

注意：这里标量构成的「列向量」只是方便的形式记号，不在空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，与左边的向量有着本质的区别．左边的向量如果恰好是列向量，并排拼起来就可以形式上构成一个「矩阵」，上述乘积恰好是矩阵中常见的「矩阵左乘列向量」的形式．

下文指出，这里的线性表示也等价于，向量 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 落在矩阵 (𝑎1,𝑎2⋯,𝑎𝑟)(a1,a2⋯,ar)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的像空间里．

根据下文中的定义，零向量一定会落在像空间里．如果用线性变换的观点看，线性相关等价于变换后多个向量变换到零向量，而线性无关等价于只有零向量本身变换到零向量．

#### 性质

对线性空间 (𝑉, +, ⋅,ℙ)(V,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),

  1. 若向量组的一部分线性相关，则向量组线性相关．若向量组线性无关，则其任意非空部分均线性无关．简记为：**「大无关、小无关」；「小相关、大相关」** ．
  2. 含 𝜃θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的向量组线性相关．
  3. 向量组线性相关当且仅当向量组的某个向量可以由其余向量线性表出．
  4. 若向量 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可被向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性表出，则表出方式唯一当且仅当向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性无关．
  5. 若向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性无关，则向量 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可被向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性表出当且仅当向量组 𝑎1,𝑎2,…,𝑎𝑛,𝛽a1,a2,…,an,β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性相关．

### 极大线性无关组、秩

线性相关可以理解为「多余」，说明向量组内部有的向量可以被其他向量表出，可以删去．删完了之后，将剩下极大线性无关组．

对线性空间 (𝑉, +, ⋅,ℙ)(V,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

  1. 对于向量组 𝑏1,𝑏2,…,𝑏𝑚b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 令 {𝑎1,𝑎2,…,𝑎𝑛} ⊆{𝑏1,𝑏2,…,𝑏𝑚}{a1,a2,…,an}⊆{b1,b2,…,bm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 若有：

     * 向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性无关．
     * ∀𝛽 ∈{𝑏1,𝑏2,…,𝑏𝑚} ∖{𝑎1,𝑎2,…,𝑎𝑛}∀β∈{b1,b2,…,bm}∖{a1,a2,…,an}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 向量组 𝑎1,𝑎2,…,𝑎𝑛,𝛽a1,a2,…,an,β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性相关．

则称向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为向量组 𝑏1,𝑏2,…,𝑏𝑚b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的一个 **极大线性无关组** ．类似地，可定义线性空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极大线性无关组．

规定向量组 𝜃,𝜃,…,𝜃θ,θ,…,θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极大线性无关组为空集，于是全 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵对应的向量组没有极大线性无关组．

从向量组删向量的删法不唯一，因此极大线性无关组也不唯一．习惯上从左到右按顺序删．

很巧的是，按顺序删，留下的向量，恰好就是「按行看」观点里面，高斯消元法剩下的行最简形矩阵中，元素 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在的列．

称向量组 𝑏1,𝑏2,…,𝑏𝑚b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极大线性无关组的大小为向量组的 **秩** ，记作 rank⁡{𝑏1,𝑏2,…,𝑏𝑚}rank⁡{b1,b2,…,bm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 规定 rank⁡{𝜃,𝜃,…,𝜃} =0rank⁡{θ,θ,…,θ}=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

于是，向量组的秩的定义与矩阵的秩的定义完全一致．

  2. 若向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能线性表出向量组 𝑏1,𝑏2,…,𝑏𝑚b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的所有向量，称向量组 𝑏1,𝑏2,…,𝑏𝑚b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能被向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性表出．

  3. 若向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能被向量组 𝑏1,𝑏2,…,𝑏𝑚b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性表出，且向量组 𝑏1,𝑏2,…,𝑏𝑚b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能被向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性表出，则称两向量组 **等价** ，记作 {𝑎1,𝑎2,…,𝑎𝑛} ≅{𝑏1,𝑏2,…,𝑏𝑚}{a1,a2,…,an}≅{b1,b2,…,bm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

向量组的 **等价** 就是向量组张成的空间相同．张成空间相同的向量组相互等价，张成空间不同的向量组不等价．

向量组等价比矩阵等价条件更强，不仅要求秩相同，还要求空间完全一样．因此，把两个矩阵 **横向** 拼在一起，秩不能发生变化．

矩阵等价仅要求秩相同，因此矩阵等价表示前一个矩阵或空间，可以通过可逆变换，到达后一个矩阵或空间．

#### 性质

对线性空间 (𝑉, +, ⋅,ℙ)(V,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),

  1. 设向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能被线性表出向量组 𝑏1,𝑏2,…,𝑏𝑚b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性表出．

     * 若 𝑛 >𝑚n>m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性相关．
     * 若向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性无关，则 𝑛 ≤𝑚n≤m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 等价的线性无关向量组的大小相等．

向量组的任意极大线性无关组的大小均相等．

  3. 向量组线性无关当且仅当其秩等于其大小．

  4. 若向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能被线性表出向量组 𝑏1,𝑏2,…,𝑏𝑚b1,b2,…,bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 线性表出，则 rank⁡{𝑎1,𝑎2,…,𝑎𝑛} ≤rank⁡{𝑏1,𝑏2,…,𝑏𝑚}rank⁡{a1,a2,…,an}≤rank⁡{b1,b2,…,bm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  5. 等价的向量组的秩相等．

### 线性包

对于线性空间 (𝑉, +, ⋅,ℙ)(V,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，{𝑣=∑𝑛𝑖=1𝑘𝑖𝑎𝑖:𝑎𝑖∈𝑉,𝑘𝑖∈ℙ,𝑖=1,2,…,𝑛}{v=∑i=1nkiai:ai∈V,ki∈P,i=1,2,…,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也构成一个线性空间，称为由向量组 𝑎1,𝑎2,…,𝑎𝑛a1,a2,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **张成** 的线性空间（或 **线性包** ），记作 span⁡{𝑎1,𝑎2,…,𝑎𝑛}span⁡{a1,a2,…,an}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这里的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个向量 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不一定线性无关．

### 线性子空间

对线性空间 (𝑉, +, ⋅,ℙ)(V,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 若代数系统 (𝑉1, +, ⋅,ℙ)(V1,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足：

  1. ∅ ≠𝑉1∅≠V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 𝑉1 ⊆𝑉V1⊆V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 关于 +, ⋅+,⋅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的线性空间

则称 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性子空间，简称子空间，记作 𝑉1 ≤𝑉V1≤V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

任何空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有两个 **平凡子空间** ：它本身 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与零子空间．零子空间只含零向量，不含有线性无关的向量．

若第 2 条中的 ⊆⊆![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 换为 ⊂⊂![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则称 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性真子空间，记作 𝑉1 <𝑉V1<V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

不难证明：线性空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非空子集 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是其线性子空间当且仅当线性运算在 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上封闭，即：

  1. ∀𝑢,𝑣 ∈𝑉1∀u,v∈V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑢 +𝑣 ∈𝑉1u+v∈V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. ∀𝑣 ∈𝑉1∀v∈V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),∀𝑘 ∈ℙ∀k∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑘𝑣 ∈𝑉1kv∈V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 交、和与直和、直积

对线性空间 (𝑉1, +, ⋅,ℙ)(V1,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 (𝑉2, +, ⋅,ℙ)(V2,+,⋅,P)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

  1. 不难验证：加法和数乘在 𝑉1 ∩𝑉2V1∩V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上封闭，故可称 𝑉1 ∩𝑉2V1∩V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为线性空间 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **交** ．

类似地，可定义多个线性空间的交 ⋂𝑚𝑖=1𝑉𝑖⋂i=1mVi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  2. 若线性空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑉 ={𝑢 +𝑣|𝑢 ∈𝑉1,𝑣 ∈𝑉2}V={u+v|u∈V1,v∈V2}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则称 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为线性空间 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **和** ，记为 𝑉 =𝑉1 +𝑉2V=V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

可以验证：𝑉1 +𝑉2V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是包含 𝑉1 ∪𝑉2V1∪V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小子空间．

类似地，可定义多个线性空间的和 ∑𝑚𝑖=1𝑉𝑖∑i=1mVi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  3. 设 𝑉 =𝑉1 +𝑉2V=V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 若线性空间 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的任意元素 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 均只能找到唯一一组向量 𝑣1,𝑣2v1,v2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑣 =𝑣1 +𝑣2v=v1+v2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则称 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为线性空间 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **直和**(direct sum)，记为 𝑉1 ⊕𝑉2V1⊕V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

类似地，可定义多个线性空间的直和 ⨁𝑚𝑖=1𝑉𝑖⨁i=1mVi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  4. 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **直积** 𝑉1 ×𝑉2V1×V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义为二者的笛卡儿积关于如下的加法和数乘构成 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的线性空间：

     1. + :(𝑉1 ×𝑉2) ×(𝑉1 ×𝑉2) ↦𝑉1 ×𝑉2;((𝑢1,𝑣1),(𝑢2,𝑣2)) →(𝑢1 +𝑢2,𝑣1 +𝑣2)+:(V1×V2)×(V1×V2)↦V1×V2;((u1,v1),(u2,v2))→(u1+u2,v1+v2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
     2. ⋅ :ℙ ×(𝑉1 ×𝑉2) ↦𝑉1 ×𝑉2;(𝑘,(𝑢,𝑣)) →(𝑘𝑢,𝑘𝑣)⋅:P×(V1×V2)↦V1×V2;(k,(u,v))→(ku,kv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

类似地，可定义多个线性空间的直积 ∏𝑚𝑖=1𝑉𝑖∏i=1mVi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 例子

对于线性空间 𝑉 =ℝ3V=R3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设线性空间：

  * 𝑉1 :={(𝑥,0,0)|𝑥 ∈ℝ}V1:={(x,0,0)|x∈R}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑉2 :={(𝑥,𝑦,0)|𝑥,𝑦 ∈ℝ}V2:={(x,y,0)|x,y∈R}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑉3 :={(0,𝑦,𝑧)|𝑦,𝑧 ∈ℝ}V3:={(0,y,z)|y,z∈R}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑉4 :={(𝑥,0,𝑧)|𝑥,𝑧 ∈ℝ}V4:={(x,0,z)|x,z∈R}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则

  1. 𝑉1 <𝑉2 <𝑉V1<V2<V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑉3 <𝑉V3<V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 𝑉2 =𝑉1 +𝑉2V2=V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. 𝑉 =𝑉1 ⊕𝑉3 =𝑉2 +𝑉3V=V1⊕V3=V2+V3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. 𝑉2 ⊕𝑉3 =𝑉4V2⊕V3=V4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑉2 ⊕𝑉4 =𝑉3V2⊕V4=V3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑉3 ⊕𝑉4 =𝑉2V3⊕V4=V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  5. 𝑉2 +𝑉3 ≤𝑉V2+V3≤V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

#### 性质

  1. 令 𝑉1,𝑉2,𝑉3V1,V2,V3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性空间，和集合的交一样，线性空间的交适用如下法则：
     1. 交换律：𝑉1 ∩𝑉2 =𝑉2 ∩𝑉1V1∩V2=V2∩V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
     2. 结合律：𝑉1 ∩(𝑉2 ∩𝑉3) =(𝑉1 ∩𝑉2) ∩𝑉3V1∩(V2∩V3)=(V1∩V2)∩V3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 令 𝑉1,𝑉2,𝑉3V1,V2,V3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性空间，类似于集合的并，线性空间的和适用如下法则：
     1. 交换律：𝑉1 +𝑉2 =𝑉2 +𝑉1V1+V2=V2+V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
     2. 结合律：𝑉1 +(𝑉2 +𝑉3) =(𝑉1 +𝑉2) +𝑉3V1+(V2+V3)=(V1+V2)+V3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. 令 𝑉1,𝑉2,𝑉3V1,V2,V3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性空间，线性空间的交与并有如下关系：
     1. 𝑉1 ∩(𝑉2 +𝑉3) ⊇(𝑉1 ∩𝑉2) +(𝑉1 ∩𝑉3)V1∩(V2+V3)⊇(V1∩V2)+(V1∩V3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
     2. 𝑉1 +(𝑉2 ∩𝑉3) ⊆(𝑉1 +𝑉2) ∩(𝑉1 +𝑉3)V1+(V2∩V3)⊆(V1+V2)∩(V1+V3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. span⁡{𝑎1,𝑎2,…,𝑎𝑛} +span⁡{𝑏1,𝑏2,…,𝑏𝑚} =span⁡{𝑎1,𝑎2,…,𝑎𝑛,𝑏1,𝑏2,…,𝑏𝑚}span⁡{a1,a2,…,an}+span⁡{b1,b2,…,bm}=span⁡{a1,a2,…,an,b1,b2,…,bm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  5. 令 𝑉1,𝑉2V1,V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性空间，则下列诸款等价：

     1. 𝑉1 +𝑉2 =𝑉1 ⊕𝑉2V1+V2=V1⊕V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

     2. ∃𝛽 ∈𝑉1 +𝑉2∃β∈V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 使得拆分为 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的向量和的方式唯一（任意 →→![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在）

     3. 𝜃θ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拆分为 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中向量的和的方式唯一

     4. 𝑉1 ∩𝑉2 ={𝜃}V1∩V2={θ}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明

1 ⟹ 21⟹2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：由定义立得．

2 ⟹ 32⟹3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

令 𝛽 =𝛽1 +𝛽2β=β1+β2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 其中 𝛽1 ∈𝑉1,𝛽2 ∈𝑉2β1∈V1,β2∈V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 若 𝜃 =𝛼1 +𝛼2θ=α1+α2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝜃 ≠𝛼1 ∈𝑉1,𝛼2 ∈𝑉2θ≠α1∈V1,α2∈V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则 𝛽 =𝛽 +𝜃 =(𝛽1 +𝛼1) +(𝛽2 +𝛼2)β=β+θ=(β1+α1)+(β2+α2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

而 𝛽1 ≠𝛽1 +𝛼1β1≠β1+α1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 与条件矛盾．

3 ⟹ 43⟹4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

在 𝑉1V1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑉2V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中取一非零向量 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则 𝜃 =𝛼 +( −𝛼) =( −𝛼) +𝛼θ=α+(−α)=(−α)+α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 这与条件矛盾．

4 ⟹ 14⟹1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

若 𝑉1 +𝑉2V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是直和，则存在 𝛽 ∈𝑉1 +𝑉2β∈V1+V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝛽 =𝛽1 +𝛽2 =𝛾1 +𝛾2β=β1+β2=γ1+γ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 其中 𝛽1,𝛾1 ∈𝑉1,𝛽2,𝛾2 ∈𝑉2β1,γ1∈V1,β2,γ2∈V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝛽1,𝛽2,𝛾1,𝛾2β1,β2,γ1,γ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互不相同．

进而 𝜃 ≠𝛽1 −𝛾1 =𝛾2 −𝛽2 ∈𝑉1 ∩𝑉2θ≠β1−γ1=γ2−β2∈V1∩V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 与条件矛盾．

### 同构

设 𝑉,𝑉′V,V′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的线性空间，若存在双射 𝜎 :𝑉 ↦𝑉′σ:V↦V′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且保持加法与数乘，即 ∀𝑢,𝑣 ∈𝑉∀u,v∈V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),∀𝑘 ∈ℙ∀k∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足：

  1. 𝜎(𝑢 +𝑣) =𝜎(𝑢) +𝜎(𝑣)σ(u+v)=σ(u)+σ(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 𝜎(𝑘𝑢) =𝑘𝜎(𝑢)σ(ku)=kσ(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则称 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑉′V′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **同构映射** ，此时称 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑉′V′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **同构** ，记为 𝑉 ≅𝑉′V≅V′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Note

若 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是单射，则可定义 **单同态** ；若 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是满射，则可定义 **满同态** ．

#### 性质

  1. 域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的两线性空间同构当且仅当其维数相等．（维数的定义参见 [线性基](../basis/)．）
  2. （1 的推论）域 ℙP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维线性空间与线性空间 ℙ𝑛Pn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构．

Note

本性质说明我们基本上可以将坐标和向量等同看待．

## 欧氏空间与线性空间的关系

以我们最熟悉的三维欧氏空间为例，其部分相关概念在线性空间中的对应关系如下表：

三维欧氏空间| 线性空间  
---|---  
向量| 向量  
垂直| 正交（即内积为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）  
三向量共线/共面| 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个向量线性相关  
三向量不共面| 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个向量线性无关  
基向量| [线性基](../basis/)  
空间的维数| 空间的维数  
  
## 应用

从本节开始主要讲述对于线性方程组「按列看」的观点．

矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 本身也是由列向量构成的．把 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 本身看成了列向量组，而 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是未知数系数，思考 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当中的这组列向量能不能配上未知数，凑出列向量 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时列向量 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全未知的．

此时研究的等式 𝐴𝑥 =𝑏Ax=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整理为：

𝛼1𝑥1+𝛼2𝑥2+⋯+𝛼𝑛𝑥𝑛=𝑏α1x1+α2x2+⋯+αnxn=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这时，矩阵乘法中，位于左边的矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以看作向量组，即一组列向量．这组列向量作为一组基，张成一个空间，探讨列向量 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否落在这个空间里．

### 按列看待线性方程组的解

秩是极大线性无关组中向量的个数，代表了「约束」．那么其余的向量将赋予解的自由度，即允许在其他方向赋予冗余的向量．

如果记 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的列数，即含有的列向量个数，记 𝑟(𝐴)r(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为矩阵 A 的秩，则有自由度 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑆=𝑛−𝑟(𝐴)S=n−r(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

方程组的全体解也构成向量组，自由度 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 𝐴𝑥 =0Ax=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 解向量组的秩，即下文核空间的维数．

### 方程组的同解

两个方程组的公共解定义为两组解的交集．

方程组的 **同解** 就是方程组的解的集合相等．解的集合相等的方程组同解，解的集合不相等的方程组不同解．

方程组同解也比矩阵等价条件强，不仅要求秩相等，还要求把两个矩阵 **纵向** 拼在一起之后，秩仍然不改变．

这里与向量组等价对比，向量组等价要求矩阵横向拼接，秩不改变．因此，有如下关系：

矩阵等价，不一定有对应的向量组等价或者方程组同解，但是若有向量组等价或者方程组同解，必然有对应的矩阵等价（秩相同）．

如果矩阵对应的向量组等价，那么将矩阵转置后，对应的方程组同解，反之亦然．

### 矩阵的核空间与像空间

这部分的核空间与像空间是站在线性空间的角度上叙述的．

对于矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为方程 𝐴𝑥 =0Ax=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体解 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成的集合，则 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个线性空间，𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的标量域与 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素所在的域相同．

称此时的 𝑊W![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **核空间** ，记作 𝑁(𝐴)N(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的核空间 𝑁(𝐴)N(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是方程 𝐴𝑥 =0Ax=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **解空间** ．根据后文基的定义，该方程的 **基础解系** 就是核空间的基．

如果矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是可逆矩阵，则 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的核空间 𝑁(𝐴)N(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只含零向量．

对于矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个列为向量 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个列向量 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 张成的空间为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **像空间** ，或者记作 **列空间** ，记作：

𝑅(𝐴)=span⁡{𝛼1,𝛼2,⋯,𝛼𝑛}R(A)=span⁡{α1,α2,⋯,αn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据后文维数的定义，像空间的维数等于矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的秩．

由定义，对于像空间 𝑅(𝐴)R(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的每一个元素 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，均有相应的表示：

𝑦=𝑘1𝛼1+𝑘2𝛼2+⋯+𝑘𝑛𝛼𝑛=(𝛼1,𝛼2,⋯,𝛼𝑛)⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝𝑘1𝑘2⋮𝑘𝑛⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠=𝐴⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝𝑘1𝑘2⋮𝑘𝑛⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠y=k1α1+k2α2+⋯+knαn=(α1,α2,⋯,αn)(k1k2⋮kn)=A(k1k2⋮kn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此像空间 𝑅(𝐴)R(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是对于任意向量 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐴𝑥Ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **值域** ．

同理可以定义 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **行空间** ，即 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的转置的值域 𝑅(𝐴𝑇)R(AT)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于矩阵的行秩等于列秩，行空间的维数也为矩阵的秩，因此转置改变像空间，而不改变像空间的维数．

在这里可以与前文建立对应关系：

向量组等价，等价于对应矩阵的像空间 𝑅(𝐴)R(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同．

方程组同解，等价于对应矩阵的行空间 𝑅(𝐴𝑇)R(AT)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同．

## 参考资料与注释

  1. 丘维声，高等代数（下）．清华大学出版社．
  2. [Vector space](https://en.wikipedia.org/w/index.php?title=Vector_space&oldid=1108546097)._Wikipedia, The Free Encyclopedia_.

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-algebra/vector-space.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/linear-algebra/vector-space.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Great-designer](https://github.com/Great-designer), [aofall](https://github.com/aofall), [CCXXXI](https://github.com/CCXXXI), [codewasp942](https://github.com/codewasp942), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Marcythm](https://github.com/Marcythm), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
