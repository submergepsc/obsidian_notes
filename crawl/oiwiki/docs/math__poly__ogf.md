# 普通生成函数 - OI Wiki

- Source: https://oi-wiki.org/math/poly/ogf/

# 普通生成函数

序列 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的普通生成函数（ordinary generating function，OGF）定义为形式幂级数：

𝐹(𝑥)=∑𝑛𝑎𝑛𝑥𝑛F(x)=∑nanxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既可以是有穷序列，也可以是无穷序列．常见的例子（假设 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为起点）：

  1. 序列 𝑎 =⟨1,2,3⟩a=⟨1,2,3⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的普通生成函数是 1 +2𝑥 +3𝑥21+2x+3x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 序列 𝑎 =⟨1,1,1,⋯⟩a=⟨1,1,1,⋯⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的普通生成函数是 ∑𝑛≥0𝑥𝑛∑n≥0xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 序列 𝑎 =⟨1,2,4,8,16,⋯⟩a=⟨1,2,4,8,16,⋯⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成函数是 ∑𝑛≥02𝑛𝑥𝑛∑n≥02nxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  4. 序列 𝑎 =⟨1,3,5,7,9,⋯⟩a=⟨1,3,5,7,9,⋯⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成函数是 ∑𝑛≥0(2𝑛 +1)𝑥𝑛∑n≥0(2n+1)xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

换句话说，如果序列 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有通项公式，那么它的普通生成函数的系数就是通项公式．

## 基本运算

考虑两个序列 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的普通生成函数，分别为 𝐹(𝑥),𝐺(𝑥)F(x),G(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么有

𝐹(𝑥)±𝐺(𝑥)=∑𝑛(𝑎𝑛±𝑏𝑛)𝑥𝑛F(x)±G(x)=∑n(an±bn)xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此 𝐹(𝑥) ±𝐺(𝑥)F(x)±G(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是序列 ⟨𝑎𝑛 ±𝑏𝑛⟩⟨an±bn⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的普通生成函数．

考虑乘法运算，也就是卷积：

𝐹(𝑥)𝐺(𝑥)=∑𝑛𝑥𝑛𝑛∑𝑖=0𝑎𝑖𝑏𝑛−𝑖F(x)G(x)=∑nxn∑i=0naibn−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此 𝐹(𝑥)𝐺(𝑥)F(x)G(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是序列 ⟨∑𝑛𝑖=0𝑎𝑖𝑏𝑛−𝑖⟩⟨∑i=0naibn−i⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的普通生成函数．

## 封闭形式

在运用生成函数的过程中，我们不会一直使用形式幂级数的形式，而会适时地转化为封闭形式以更好地化简．

例如 ⟨1,1,1,⋯⟩⟨1,1,1,⋯⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的普通生成函数 𝐹(𝑥) =∑𝑛≥0𝑥𝑛F(x)=∑n≥0xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以发现

𝐹(𝑥)𝑥+1=𝐹(𝑥)F(x)x+1=F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么解这个方程得到

𝐹(𝑥)=11−𝑥F(x)=11−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就是 ∑𝑛≥0𝑥𝑛∑n≥0xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的封闭形式．

考虑等比数列 ⟨1,𝑝,𝑝2,𝑝3,𝑝4,⋯⟩⟨1,p,p2,p3,p4,⋯⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成函数 𝐹(𝑥) =∑𝑛≥0𝑝𝑛𝑥𝑛F(x)=∑n≥0pnxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝐹(𝑥)𝑝𝑥+1=𝐹(𝑥)𝐹(𝑥)=11−𝑝𝑥F(x)px+1=F(x)F(x)=11−px![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

等比数列的封闭形式与展开形式是常用的变换手段．

小练习

请求出下列数列的普通生成函数（形式幂级数形式和封闭形式）．难度是循序渐进的．

  1. 𝑎 =⟨0,1,1,1,1,⋯⟩a=⟨0,1,1,1,1,⋯⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 𝑎 =⟨1,0,1,0,1,⋯⟩a=⟨1,0,1,0,1,⋯⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 𝑎 =⟨1,2,3,4,⋯⟩a=⟨1,2,3,4,⋯⟩![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  4. 𝑎𝑛 =(𝑚𝑛)an=(mn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是常数，𝑛 ≥0n≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．
  5. 𝑎𝑛 =(𝑚+𝑛𝑛)an=(m+nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是常数，𝑛 ≥0n≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

答案

第一个：

𝐹(𝑥)=∑𝑛≥1𝑥𝑛=𝑥1−𝑥F(x)=∑n≥1xn=x1−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

第二个：

𝐹(𝑥)=∑𝑛≥0𝑥2𝑛=∑𝑛≥0(𝑥2)𝑛=11−𝑥2F(x)=∑n≥0x2n=∑n≥0(x2)n=11−x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

第三个（求导）：

𝐹(𝑥)=∑𝑛≥0(𝑛+1)𝑥𝑛=∑𝑛≥1𝑛𝑥𝑛−1=∑𝑛≥0(𝑥𝑛)′=(11−𝑥)′=1(1−𝑥)2F(x)=∑n≥0(n+1)xn=∑n≥1nxn−1=∑n≥0(xn)′=(11−x)′=1(1−x)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

第四个（二项式定理）：

𝐹(𝑥)=∑𝑛≥0(𝑚𝑛)𝑥𝑛=(1+𝑥)𝑚F(x)=∑n≥0(mn)xn=(1+x)m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

第五个：

𝐹(𝑥)=∑𝑛≥0(𝑚+𝑛𝑛)𝑥𝑛=1(1−𝑥)𝑚+1F(x)=∑n≥0(m+nn)xn=1(1−x)m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以使用归纳法证明．

首先当 𝑚 =0m=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有 𝐹(𝑥) =11−𝑥F(x)=11−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

而当 𝑚 >0m>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有

1(1−𝑥)𝑚+1=1(1−𝑥)𝑚11−𝑥=(∑𝑛≥0(𝑚+𝑛−1𝑛)𝑥𝑛)(∑𝑛≥0𝑥𝑛)=∑𝑛≥0𝑥𝑛𝑛∑𝑖=0(𝑚+𝑖−1𝑖)=∑𝑛≥0(𝑚+𝑛𝑛)𝑥𝑛1(1−x)m+1=1(1−x)m11−x=(∑n≥0(m+n−1n)xn)(∑n≥0xn)=∑n≥0xn∑i=0n(m+i−1i)=∑n≥0(m+nn)xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 斐波那契数列的生成函数

接下来我们来推导斐波那契数列的生成函数．

斐波那契数列定义为 𝑎0 =0,𝑎1 =1,𝑎𝑛 =𝑎𝑛−1 +𝑎𝑛−2 (𝑛 >1)a0=0,a1=1,an=an−1+an−2(n>1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设它的普通生成函数是 𝐹(𝑥)F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么根据它的递推式，我们可以类似地列出关于 𝐹(𝑥)F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方程：

𝐹(𝑥)=𝑥𝐹(𝑥)+𝑥2𝐹(𝑥)−𝑎0𝑥+𝑎1𝑥+𝑎0F(x)=xF(x)+x2F(x)−a0x+a1x+a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么解得

𝐹(𝑥)=𝑥1−𝑥−𝑥2F(x)=x1−x−x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么接下来的问题是，如何求出它的展开形式？

### 展开方式一

不妨将 𝑥 +𝑥2x+x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当作一个整体，那么可以得到

𝐹(𝑥)=𝑥1−(𝑥+𝑥2)=𝑥∞∑𝑘=0(𝑥+𝑥2)𝑘=𝑥∞∑𝑘=0𝑘∑𝑖=0(𝑘𝑖)𝑥𝑘−𝑖(𝑥2)𝑖=∞∑𝑘=0𝑘∑𝑖=0(𝑘𝑖)𝑥𝑘+𝑖+1=∞∑𝑛=1⌊(𝑛−1)/2⌋∑𝑖=0(𝑛−𝑖−1𝑖)𝑥𝑛.F(x)=x1−(x+x2)=x∑k=0∞(x+x2)k=x∑k=0∞∑i=0k(ki)xk−i(x2)i=∑k=0∞∑i=0k(ki)xk+i+1=∑n=1∞∑i=0⌊(n−1)/2⌋(n−i−1i)xn.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最后一步中，令 𝑛 =𝑘 +𝑖 +1n=k+i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并更换求和顺序．由此，可以得到通项公式：

𝑎𝑛=⌊(𝑛−1)/2⌋∑𝑖=0(𝑛−𝑖−1𝑖).an=∑i=0⌊(n−1)/2⌋(n−i−1i).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这并不是我们熟知的有关黄金分割比的形式．

### 展开方式二

考虑求解一个待定系数的方程：

𝐴1−𝑎𝑥+𝐵1−𝑏𝑥=𝑥1−𝑥−𝑥2A1−ax+B1−bx=x1−x−x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

通分得到

𝐴−𝐴𝑏𝑥+𝐵−𝑎𝐵𝑥(1−𝑎𝑥)(1−𝑏𝑥)=𝑥1−𝑥−𝑥2A−Abx+B−aBx(1−ax)(1−bx)=x1−x−x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

待定项系数相等，我们得到

⎧{ { {⎨{ { {⎩𝐴+𝐵=0−𝐴𝑏−𝑎𝐵=1𝑎+𝑏=1𝑎𝑏=−1{A+B=0−Ab−aB=1a+b=1ab=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

解得

⎧{ { { {⎨{ { { {⎩𝐴=1√5𝐵=−1√5𝑎=1+√52𝑏=1−√52{A=15B=−15a=1+52b=1−52![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么我们根据等比数列的展开式，就可以得到斐波那契数列的通项公式：

𝑥1−𝑥−𝑥2=∑𝑛≥0𝑥𝑛1√5((1+√52)𝑛−(1−√52)𝑛)x1−x−x2=∑n≥0xn15((1+52)n−(1−52)n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这也被称为斐波那契数列的另一个封闭形式（𝑥1−𝑥−𝑥2x1−x−x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个封闭形式）．

对于任意多项式 𝑃(𝑥),𝑄(𝑥)P(x),Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，生成函数 𝑃(𝑥)𝑄(𝑥)P(x)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的展开式都可以使用上述方法求出．在实际运用的过程中，我们往往先求出 𝑄(𝑥)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的根，把分母表示为 ∏(1 −𝑝𝑖𝑥)𝑑𝑖∏(1−pix)di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，然后再求分子．

当对分母进行因式分解但有重根时，每有一个重根就要多一个分式，如考虑生成函数

𝐺(𝑥)=1(1−𝑥)(1−2𝑥)2G(x)=1(1−x)(1−2x)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的系数的通项公式，那么有

𝐺(𝑥)=𝑐01−𝑥+𝑐11−2𝑥+𝑐2(1−2𝑥)2G(x)=c01−x+c11−2x+c2(1−2x)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

解得

⎧{ {⎨{ {⎩𝑐0=1𝑐1=−2𝑐2=2{c0=1c1=−2c2=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么

[𝑥𝑛]𝐺(𝑥)=1−2𝑛+1+(𝑛+1)⋅2𝑛+1[xn]G(x)=1−2n+1+(n+1)⋅2n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 牛顿二项式定理

我们重新定义组合数的运算：

(𝑟𝑘)=𝑟𝑘――𝑘!(𝑟∈𝐂,𝑘∈𝐍)(rk)=rk―k!(r∈C,k∈N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的范围是复数域．在这种情况下．对于 𝛼 ∈𝐂α∈C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

(1+𝑥)𝛼=∑𝑛≥0(𝛼𝑛)𝑥𝑛(1+x)α=∑n≥0(αn)xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

二项式定理其实是牛顿二项式定理的一个特殊情况．

## 卡特兰数的生成函数

参考 [Catalan 数形式的代数推演](../../combinatorics/catalan/#代数推演)．

## 应用

接下来给出一些例题，来介绍生成函数在 OI 中的具体应用．

### 食物

[食物](https://hydro.ac/p/bzoj-P3028)

在许多不同种类的食物中选出 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，每种食物的限制如下：

  1. 承德汉堡：偶数个
  2. 可乐：0 个或 1 个
  3. 鸡腿：0 个，1 个或 2 个
  4. 蜜桃多：奇数个
  5. 鸡块：4 的倍数个
  6. 包子：0 个，1 个，2 个或 3 个
  7. 土豆片炒肉：不超过一个．
  8. 面包：3 的倍数个

每种食物都是以「个」为单位，只要总数加起来是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就算一种方案．对于给出的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 你需要计算出方案数，对 1000710007![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模．

这是一道经典的生成函数题．对于一种食物，我们可以设 𝑎𝑛an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示这种食物选 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个的方案数，并求出它的生成函数．而两种食物一共选 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个的方案数的生成函数，就是它们生成函数的卷积．多种食物选 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个的方案数的生成函数也是它们生成函数的卷积．

在理解了方案数可以用卷积表示以后，我们就可以构造生成函数（标号对应题目中食物的标号）：

  1. ∑𝑛≥0𝑥2𝑛 =11−𝑥2∑n≥0x2n=11−x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 1 +𝑥1+x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 1 +𝑥 +𝑥2 =1−𝑥31−𝑥1+x+x2=1−x31−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  4. 𝑥1−𝑥2x1−x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  5. ∑𝑛≥0𝑥4𝑛 =11−𝑥4∑n≥0x4n=11−x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  6. 1 +𝑥 +𝑥2 +𝑥3 =1−𝑥41−𝑥1+x+x2+x3=1−x41−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  7. 1 +𝑥1+x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  8. 11−𝑥311−x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

那么全部乘起来，得到答案的生成函数：

𝐹(𝑥)=(1+𝑥)(1−𝑥3)𝑥(1−𝑥4)(1+𝑥)(1−𝑥2)(1−𝑥)(1−𝑥2)(1−𝑥4)(1−𝑥)(1−𝑥3)=𝑥(1−𝑥)4F(x)=(1+x)(1−x3)x(1−x4)(1+x)(1−x2)(1−x)(1−x2)(1−x4)(1−x)(1−x3)=x(1−x)4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后将它转化为展开形式（使用封闭形式练习中第五个练习）：

𝐹(𝑥)=∑𝑛≥1(𝑛+2𝑛−1)𝑥𝑛F(x)=∑n≥1(n+2n−1)xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此答案就是 (𝑛+2𝑛−1) =(𝑛+23)(n+2n−1)=(n+23)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### Sweet

[「CEOI2004」Sweet](https://hydro.ac/p/bzoj-P3027)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆糖果．不同的堆里糖果的种类不同（即同一个堆里的糖果种类是相同的，不同的堆里的糖果的种类是不同的）．第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个堆里有 𝑚𝑖mi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个糖果．现在要吃掉至少 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个糖果，但不超过 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．求有多少种方案．

两种方案不同当且仅当吃的个数不同，或者吃的糖果中，某一种糖果的个数在两个方案中不同．

𝑛 ≤10,0 ≤𝑎 ≤𝑏 ≤107,𝑚𝑖 ≤106n≤10,0≤a≤b≤107,mi≤106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 堆吃 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个糖果的方案数（显然为 1）的生成函数为

𝐹𝑖(𝑥)=𝑚𝑖∑𝑗=0𝑥𝑗=1−𝑥𝑚𝑖+11−𝑥Fi(x)=∑j=0mixj=1−xmi+11−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此总共吃 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个糖果的方案数的生成函数就是

𝐺(𝑥)=𝑛∏𝑖=1𝐹𝑖(𝑥)=(1−𝑥)−𝑛𝑛∏𝑖=1(1−𝑥𝑚𝑖+1)G(x)=∏i=1nFi(x)=(1−x)−n∏i=1n(1−xmi+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

现在我们要求的是 ∑𝑏𝑖=𝑎[𝑥𝑖]𝐺(𝑥)∑i=ab[xi]G(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于 𝑛 ≤10n≤10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此我们可以暴力展开 ∏𝑛𝑖=1(1 −𝑥𝑚𝑖+1)∏i=1n(1−xmi+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（最多只有 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项）．

然后对 (1 −𝑥)−𝑛(1−x)−n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使用牛顿二项式定理：

(1−𝑥)−𝑛=∑𝑖≥0(−𝑛𝑖)(−𝑥)𝑖=∑𝑖≥0(𝑛−1+𝑖𝑖)𝑥𝑖(1−x)−n=∑i≥0(−ni)(−x)i=∑i≥0(n−1+ii)xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们枚举 ∏𝑛𝑖=1(1 −𝑥𝑚𝑖+1)∏i=1n(1−xmi+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 𝑥𝑘xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项的系数，假设为 𝑐𝑘ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么它和 (1 −𝑥)−𝑛(1−x)−n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相乘后，对答案的贡献就是

𝑐𝑘𝑏−𝑘∑𝑖=𝑎−𝑘(𝑛−1+𝑖𝑖)=𝑐𝑘((𝑛+𝑏−𝑘𝑏−𝑘)−(𝑛+𝑎−𝑘−1𝑎−𝑘−1))ck∑i=a−kb−k(n−1+ii)=ck((n+b−kb−k)−(n+a−k−1a−k−1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样就可以 𝑂(𝑏)O(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 地求出答案了．

时间复杂度 𝑂(2𝑛 +𝑏)O(2n+b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/ogf.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/ogf.md "edit.link.title")  
>  __本页面贡献者：[sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [H-J-Granger](https://github.com/H-J-Granger), [NachtgeistW](https://github.com/NachtgeistW), [CCXXXI](https://github.com/CCXXXI), [AngelKitty](https://github.com/AngelKitty), [c-forrest](https://github.com/c-forrest), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Ir1d](https://github.com/Ir1d), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [hly1204](https://github.com/hly1204), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Molmin](https://github.com/Molmin), [Peanut-Tang](https://github.com/Peanut-Tang), [purple-vine](https://github.com/purple-vine), [Revltalize](https://github.com/Revltalize), [schtonn](https://github.com/schtonn), [shuzhouliu](https://github.com/shuzhouliu), [skylee03](https://github.com/skylee03), [SukkaW](https://github.com/SukkaW), [Tiphereth-A](https://github.com/Tiphereth-A), [xglight](https://github.com/xglight)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
