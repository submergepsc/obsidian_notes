# 快速傅里叶变换 - OI Wiki

- Source: https://oi-wiki.org/math/poly/fft/

# 快速傅里叶变换

前置知识：[复数](../../complex/)．

本文将介绍一种算法，它支持在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内计算两个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次多项式的乘法，比朴素的 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 算法更高效．由于两个整数的乘法也可以被当作多项式乘法，因此这个算法也可以用来加速大整数的乘法计算．

## 引入

我们现在引入两个多项式 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝐴=5𝑥2+3𝑥+7𝐵=7𝑥2+2𝑥+1A=5x2+3x+7B=7x2+2x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

两个多项式相乘的积 𝐶 =𝐴 ×𝐵C=A×B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以在 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度中解得（这里 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或者 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 多项式的次数）：

𝐶=𝐴×𝐵=35𝑥4+31𝑥3+60𝑥2+17𝑥+7C=A×B=35x4+31x3+60x2+17x+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

很明显，多项式 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数 𝑐𝑖ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑐𝑖 =∑𝑖𝑗=0𝑎𝑗𝑏𝑖−𝑗ci=∑j=0iajbi−j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而对于这种朴素算法而言，计算每一项的时间复杂度都为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一共有 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项，那么时间复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

能否加速使得它的时间复杂度降低呢？如果使用快速傅里叶变换的话，那么我们可以使得其复杂度降低到 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 傅里叶变换

傅里叶变换（Fourier Transform）是一种分析信号的方法，它可分析信号的成分，也可用这些成分合成信号．许多波形可作为信号的成分，傅里叶变换用正弦波作为信号的成分．

设 𝑓(𝑡)f(t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于时间 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的函数，则傅里叶变换可以检测频率 𝜔ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的周期在 𝑓(𝑡)f(t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出现的程度：

𝐹(𝜔)=𝔽[𝑓(𝑡)]=∫∞−∞𝑓(𝑡)e−i𝜔𝑡𝑑𝑡F(ω)=F[f(t)]=∫−∞∞f(t)e−iωtdt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它的逆变换是

𝑓(𝑡)=𝔽−1[𝐹(𝜔)]=12𝜋∫∞−∞𝐹(𝜔)ei𝜔𝑡𝑑𝜔f(t)=F−1[F(ω)]=12π∫−∞∞F(ω)eiωtdω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

逆变换的形式与正变换非常类似，分母 2𝜋2π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 恰好是指数函数的周期．

傅里叶变换相当于将时域的函数与周期为 2𝜋2π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复指数函数进行连续的内积．逆变换仍旧为一个内积．

傅里叶变换有相应的卷积定理，可以将时域的卷积转化为频域的乘积，也可以将频域的卷积转化为时域的乘积．

## 离散傅里叶变换

**离散傅里叶变换** （Discrete Fourier transform，DFT）是傅里叶变换在时域和频域上都呈离散的形式，将信号的时域采样变换为其 DTFT（discrete-time Fourier transform）的频域采样．

傅里叶变换是积分形式的连续的函数内积，离散傅里叶变换是求和形式的内积．

设 {𝑥𝑛}𝑁−1𝑛=0{xn}n=0N−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是某一满足有限性条件的序列，它的离散傅里叶变换（DFT）为：

𝑋𝑘=𝑁−1∑𝑛=0𝑥𝑛e−i2𝜋𝑁𝑘𝑛Xk=∑n=0N−1xne−i2πNkn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 ee![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是自然对数的底数，𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是虚数单位．通常以符号 FF![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示这一变换，即

ˆ𝑥=F𝑥x^=Fx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

类似于积分形式，它的 **逆离散傅里叶变换** （IDFT）为：

𝑥𝑛=1𝑁𝑁−1∑𝑘=0𝑋𝑘ei2𝜋𝑁𝑘𝑛xn=1N∑k=0N−1Xkei2πNkn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以记为：

𝑥=F−1ˆ𝑥x=F−1x^![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

实际上，DFT 和 IDFT 变换式中和式前面的归一化系数并不重要．在上面的定义中，DFT 和 IDFT 前的系数分别为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 1𝑁1N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．有时我们会将这两个系数都改 1√𝑁1N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

离散傅里叶变换仍旧是时域到频域的变换．由于求和形式的特殊性，可以有其他的解释方法．

如果把序列 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 看作多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项系数，则计算得到的 𝑋𝑘Xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 恰好是多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代入单位根 e−2𝜋i𝑘𝑁e−2πikN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点值 𝑓(e−2𝜋i𝑘𝑁)f(e−2πikN)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这便构成了卷积定理的另一种解释办法，即对多项式进行特殊的求值操作．离散傅里叶变换恰好是多项式在单位根处进行求值．

例如计算：

(𝑛3)+(𝑛7)+(𝑛11)+(𝑛15)+…(n3)+(n7)+(n11)+(n15)+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定义函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为：

𝑓(𝑥)=(1+𝑥)𝑛=(𝑛0)𝑥0+(𝑛1)𝑥1+(𝑛2)𝑥2+(𝑛3)𝑥3+…f(x)=(1+x)n=(n0)x0+(n1)x1+(n2)x2+(n3)x3+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后可以发现，代入四次单位根 𝑓(i)f(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到这样的序列：

𝑓(i)=(1+i)𝑛=(𝑛0)+(𝑛1)i−(𝑛2)−(𝑛3)i+…f(i)=(1+i)n=(n0)+(n1)i−(n2)−(n3)i+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是下面的求和恰好可以把其余各项消掉：

𝑓(1)+i𝑓(i)−𝑓(−1)−i𝑓(−i)=4(𝑛3)+4(𝑛7)+4(𝑛11)+4(𝑛15)+…f(1)+if(i)−f(−1)−if(−i)=4(n3)+4(n7)+4(n11)+4(n15)+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此这道数学题的答案为：

(𝑛3)+(𝑛7)+(𝑛11)+(𝑛15)+…=2𝑛+i(1+i)𝑛−i(1−i)𝑛4(n3)+(n7)+(n11)+(n15)+…=2n+i(1+i)n−i(1−i)n4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这道数学题在单位根处求值，恰好构成离散傅里叶变换．

### 矩阵公式

由于离散傅立叶变换是一个 **线性** 算子，所以它可以用矩阵乘法来描述．在矩阵表示法中，离散傅立叶变换表示如下：

⎡⎢ ⎢ ⎢ ⎢ ⎢⎣𝑋0𝑋1𝑋2⋮𝑋𝑁−1⎤⎥ ⎥ ⎥ ⎥ ⎥⎦=⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣111⋯11𝛼𝛼2⋯𝛼𝑁−11𝛼2𝛼4⋯𝛼2(𝑁−1)⋮⋮⋮⋱⋮1𝛼𝑁−1𝛼2(𝑁−1)⋯𝛼(𝑁−1)(𝑁−1)⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦⎡⎢ ⎢ ⎢ ⎢ ⎢⎣𝑥0𝑥1𝑥2⋮𝑥𝑁−1⎤⎥ ⎥ ⎥ ⎥ ⎥⎦[X0X1X2⋮XN−1]=[111⋯11αα2⋯αN−11α2α4⋯α2(N−1)⋮⋮⋮⋱⋮1αN−1α2(N−1)⋯α(N−1)(N−1)][x0x1x2⋮xN−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝛼 =e−i2𝜋𝑁α=e−i2πN![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 快速傅里叶变换

FFT 是一种高效实现 DFT 的算法，称为快速傅立叶变换（Fast Fourier Transform，FFT）．它对傅里叶变换的理论并没有新的发现，但是对于在计算机系统或者说数字系统中应用离散傅立叶变换，可以说是进了一大步．快速数论变换（NTT）是快速傅里叶变换（FFT）在数论基础上的实现．

在 1965 年，Cooley 和 Tukey 发表了快速傅里叶变换算法．事实上 FFT 早在这之前就被发现过了，但是在当时现代计算机并未问世，人们没有意识到 FFT 的重要性．一些调查者认为 FFT 是由 Runge 和 König 在 1924 年发现的．但事实上高斯早在 1805 年就发明了这个算法，但一直没有发表．

### 分治法实现

FFT 算法的基本思想是分治．就 DFT 来说，它分治地来求当 𝑥 =𝜔𝑘𝑛x=ωnk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．基 - 2 FFT 的分治思想体现在将多项式分为奇次项和偶次项处理．

举个例子，对于一共 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项的多项式：

𝑓(𝑥)=𝑎0+𝑎1𝑥+𝑎2𝑥2+𝑎3𝑥3+𝑎4𝑥4+𝑎5𝑥5+𝑎6𝑥6+𝑎7𝑥7f(x)=a0+a1x+a2x2+a3x3+a4x4+a5x5+a6x6+a7x7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

按照次数的奇偶来分成两组，然后右边提出来一个 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑓(𝑥)=(𝑎0+𝑎2𝑥2+𝑎4𝑥4+𝑎6𝑥6)+(𝑎1𝑥+𝑎3𝑥3+𝑎5𝑥5+𝑎7𝑥7)=(𝑎0+𝑎2𝑥2+𝑎4𝑥4+𝑎6𝑥6)+𝑥(𝑎1+𝑎3𝑥2+𝑎5𝑥4+𝑎7𝑥6)f(x)=(a0+a2x2+a4x4+a6x6)+(a1x+a3x3+a5x5+a7x7)=(a0+a2x2+a4x4+a6x6)+x(a1+a3x2+a5x4+a7x6)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

分别用奇偶次次项数建立新的函数：

𝐺(𝑥)=𝑎0+𝑎2𝑥+𝑎4𝑥2+𝑎6𝑥3𝐻(𝑥)=𝑎1+𝑎3𝑥+𝑎5𝑥2+𝑎7𝑥3G(x)=a0+a2x+a4x2+a6x3H(x)=a1+a3x+a5x2+a7x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么原来的 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用新函数表示为：

𝑓(𝑥)=𝐺(𝑥2)+𝑥×𝐻(𝑥2)f(x)=G(x2)+x×H(x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用偶数次单位根的性质 𝜔𝑖𝑛 = −𝜔𝑖+𝑛/2𝑛ωni=−ωni+n/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，和 𝐺(𝑥2)G(x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐻(𝑥2)H(x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶函数，我们知道在复平面上 𝜔𝑖𝑛ωni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜔𝑖+𝑛/2𝑛ωni+n/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝐺(𝑥2)G(x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝐻(𝑥2)H(x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的值相同．得到：

𝑓(𝜔𝑘𝑛)=𝐺((𝜔𝑘𝑛)2)+𝜔𝑘𝑛×𝐻((𝜔𝑘𝑛)2)=𝐺(𝜔2𝑘𝑛)+𝜔𝑘𝑛×𝐻(𝜔2𝑘𝑛)=𝐺(𝜔𝑘𝑛/2)+𝜔𝑘𝑛×𝐻(𝜔𝑘𝑛/2)f(ωnk)=G((ωnk)2)+ωnk×H((ωnk)2)=G(ωn2k)+ωnk×H(ωn2k)=G(ωn/2k)+ωnk×H(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

和：

𝑓(𝜔𝑘+𝑛/2𝑛)=𝐺(𝜔2𝑘+𝑛𝑛)+𝜔𝑘+𝑛/2𝑛×𝐻(𝜔2𝑘+𝑛𝑛)=𝐺(𝜔2𝑘𝑛)−𝜔𝑘𝑛×𝐻(𝜔2𝑘𝑛)=𝐺(𝜔𝑘𝑛/2)−𝜔𝑘𝑛×𝐻(𝜔𝑘𝑛/2)f(ωnk+n/2)=G(ωn2k+n)+ωnk+n/2×H(ωn2k+n)=G(ωn2k)−ωnk×H(ωn2k)=G(ωn/2k)−ωnk×H(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此我们求出了 𝐺(𝜔𝑘𝑛/2)G(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐻(𝜔𝑘𝑛/2)H(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，就可以同时求出 𝑓(𝜔𝑘𝑛)f(ωnk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(𝜔𝑘+𝑛/2𝑛)f(ωnk+n/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．于是对 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别递归 DFT 即可．

考虑到分治 DFT 能处理的多项式长度只能是 2𝑚(𝑚 ∈𝐍∗)2m(m∈N∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则在分治的时候左右不一样长，右边就取不到系数了．所以要在第一次 DFT 之前就把序列向上补成长度为 2𝑚(𝑚 ∈𝐍∗)2m(m∈N∗)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（高次系数补 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）、最高项次数为 2𝑚 −12m−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的多项式．

在代入值的时候，因为要代入 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同值，所以我们代入 𝜔0𝑛,𝜔1𝑛,𝜔2𝑛,⋯,𝜔𝑛−1𝑛(𝑛 =2𝑚(𝑚 ∈𝐍∗))ωn0,ωn1,ωn2,⋯,ωnn−1(n=2m(m∈N∗))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一共 2𝑚2m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同值．

代码实现方面，STL 提供了复数的模板，当然也可以手动实现．两者区别在于，使用 STL 的 `complex` 可以调用 `exp` 函数求出 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但事实上使用欧拉公式得到的虚数来求 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是等价的．

以上就是 FFT 算法中 DFT 的介绍，它将一个多项式从系数表示法变成了点值表示法．

值的注意的是，因为是单位复根，所以说我们需要令 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项式的高位补为零，使得 𝑛 =2𝑘,𝑘 ∈𝐍∗n=2k,k∈N∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

递归版 FFT

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``` |  ```text #include <cmath> #include <complex> using Comp = std :: complex < double > ; // STL complex constexpr Comp I ( 0 , 1 ); // i constexpr int MAX_N = 1 << 20 ; Comp tmp [ MAX_N ]; // rev=1, DFT; rev=-1, IDFT // 应用完本函数后需要注意归一化系数的处理 void DFT ( Comp * f , int n , int rev ) { if ( n == 1 ) return ; for ( int i = 0 ; i < n ; ++ i ) tmp [ i ] = f [ i ]; // 偶数放左边，奇数放右边 for ( int i = 0 ; i < n ; ++ i ) { if ( i & 1 ) f [ n / 2 \+ i / 2 ] = tmp [ i ]; else f [ i / 2 ] = tmp [ i ]; } Comp * g = f , * h = f \+ n / 2 ; // 递归 DFT DFT ( g , n / 2 , rev ), DFT ( h , n / 2 , rev ); // cur 是当前单位复根，对于 k = 0 而言，它对应的单位复根 omega^0_n = 1． // step 是两个单位复根的差，即满足 omega^k_n = step*omega^{k-1}*n， // 定义等价于 exp(I*(-2*M_PI/n*rev)) Comp cur ( 1 , 0 ), step ( cos ( 2 * M_PI / n ), sin ( -2 * M_PI * rev / n )); for ( int k = 0 ; k < n / 2 ; ++ k ) { // F(omega^k_n) = G(omega^k*{n/2}) + omega^k*n\\*H(omega^k*{n/2}) tmp [ k ] = g [ k ] \+ cur * h [ k ]; // F(omega^{k+n/2}*n) = G(omega^k*{n/2}) - omega^k_n*H(omega^k\\_{n/2}) tmp [ k \+ n / 2 ] = g [ k ] \- cur * h [ k ]; cur *= step ; } for ( int i = 0 ; i < n ; ++ i ) f [ i ] = tmp [ i ]; } ```   
---|---  
  
时间复杂度 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 倍增法实现

这个算法还可以从「分治」的角度继续优化．对于基 - 2 FFT，我们每一次都会把整个多项式的奇数次项和偶数次项系数分开，一直分到只剩下一个系数．但是，这个递归的过程需要更多的内存．因此，我们可以先「模仿递归」把这些系数在原数组中「拆分」，然后再「倍增」地去合并这些算出来的值．

对于「拆分」，可以使用位逆序置换实现．

对于「合并」，使用蝶形运算优化可以做到只用 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的额外空间来完成．

#### 位逆序置换

以 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项多项式为例，模拟拆分的过程：

  * 初始序列为 {𝑥0,𝑥1,𝑥2,𝑥3,𝑥4,𝑥5,𝑥6,𝑥7}{x0,x1,x2,x3,x4,x5,x6,x7}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 一次二分之后 {𝑥0,𝑥2,𝑥4,𝑥6},{𝑥1,𝑥3,𝑥5,𝑥7}{x0,x2,x4,x6},{x1,x3,x5,x7}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 两次二分之后 {𝑥0,𝑥4}{𝑥2,𝑥6},{𝑥1,𝑥5},{𝑥3,𝑥7}{x0,x4}{x2,x6},{x1,x5},{x3,x7}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 三次二分之后 {𝑥0}{𝑥4}{𝑥2}{𝑥6}{𝑥1}{𝑥5}{𝑥3}{𝑥7}{x0}{x4}{x2}{x6}{x1}{x5}{x3}{x7}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

规律：其实就是原来的那个序列，每个数用二进制表示，然后把二进制翻转对称一下，就是最终那个位置的下标．比如 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 001，翻转是 100，也就是 4，而且最后那个位置确实是 4．我们称这个变换为位逆序置换（bit-reversal permutation），证明留给读者自证．

根据它的定义，我们可以在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内求出每个数变换后的结果：

位逆序置换实现（𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text /* * 进行 FFT 和 IFFT 前的反置变换 * 位置 i 和 i 的二进制反转后的位置互换 * len 必须为 2 的幂 */ void change ( Complex y [], int len ) { // 一开始 i 是 0...01，而 j 是 10...0，在二进制下相反对称． // 之后 i 逐渐加一，而 j 依然维持着和 i 相反对称，一直到 i = 1...11． for ( int i = 1 , j = len / 2 , k ; i < len \- 1 ; i ++ ) { // 交换互为小标反转的元素，i < j 保证交换一次 if ( i < j ) swap ( y [ i ], y [ j ]); // i 做正常的 + 1，j 做反转类型的 + 1，始终保持 i 和 j 是反转的． // 这里 k 代表了 0 出现的最高位．j 先减去高位的全为 1 的数字， // 直到遇到了 0，之后再加上即可． // 考虑 j 中比特位的翻转次数，最高位将会翻转 n 次， // 第二高位将会翻转 n/2 次，以此类推，所以时间复杂度为： // T(n) = n + n/2 + n/4 + ... = O(n) k = len / 2 ; while ( j >= k ) { j = j \- k ; k = k / 2 ; } j += k ; } } ```   
---|---  
  
位逆序置换也可以 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从小到大递推实现，设 𝑙𝑒𝑛 =2𝑘len=2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示二进制数的长度，设 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 翻转后的数（高位补 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．我们要求的是 𝑅(0),𝑅(1),⋯,𝑅(𝑛 −1)R(0),R(1),⋯,R(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

首先 𝑅(0) =0R(0)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们从小到大求 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此在求 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑅(⌊𝑥2⌋)R(⌊x2⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值是已知的．因此我们把 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 右移一位（除以 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），然后翻转，再右移一位，就得到了 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **除了（二进制）个位** 之外其它位的翻转结果．

考虑个位的翻转结果：如果个位是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，翻转之后最高位就是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果个位是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则翻转后最高位是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此还要加上 𝑙𝑒𝑛2 =2𝑘−1len2=2k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．综上

𝑅(𝑥)=⌊𝑅(⌊𝑥2⌋)2⌋+(𝑥mod2)×𝑙𝑒𝑛2R(x)=⌊R(⌊x2⌋)2⌋+(xmod2)×len2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

举个例子：设 𝑘 =5k=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑙𝑒𝑛 =(100000)2len=(100000)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．为了翻转 (11001)2(11001)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

  1. 考虑 (1100)2(1100)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们知道 𝑅((1100)2) =𝑅((01100)2) =(00110)2R((1100)2)=R((01100)2)=(00110)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再右移一位就得到了 (00011)2(00011)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 考虑个位，如果是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它就要翻转到数的最高位，即翻转数加上 (10000)2 =2𝑘−1(10000)2=2k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则不用更改．

位逆序置换实现（𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text // 同样需要保证 len 是 2 的幂 // 记 rev[i] 为 i 翻转后的值 void change ( Complex y [], int len ) { for ( int i = 0 ; i < len ; ++ i ) { rev [ i ] = rev [ i >> 1 ] >> 1 ; if ( i & 1 ) { // 如果最后一位是 1，则翻转成 len/2 rev [ i ] |= len >> 1 ; } } for ( int i = 0 ; i < len ; ++ i ) { if ( i < rev [ i ]) { // 保证每对数只翻转一次 swap ( y [ i ], y [ rev [ i ]]); } } return ; } ```   
---|---  
  
#### 蝶形运算优化

已知 𝐺(𝜔𝑘𝑛/2)G(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐻(𝜔𝑘𝑛/2)H(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，需要使用下面两个式子求出 𝑓(𝜔𝑘𝑛)f(ωnk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(𝜔𝑘+𝑛/2𝑛)f(ωnk+n/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑓(𝜔𝑘𝑛)=𝐺(𝜔𝑘𝑛/2)+𝜔𝑘𝑛×𝐻(𝜔𝑘𝑛/2)𝑓(𝜔𝑘+𝑛/2𝑛)=𝐺(𝜔𝑘𝑛/2)−𝜔𝑘𝑛×𝐻(𝜔𝑘𝑛/2)f(ωnk)=G(ωn/2k)+ωnk×H(ωn/2k)f(ωnk+n/2)=G(ωn/2k)−ωnk×H(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

使用位逆序置换后，对于给定的 𝑛,𝑘n,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

  * 𝐺(𝜔𝑘𝑛/2)G(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值存储在数组下标为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置，𝐻(𝜔𝑘𝑛/2)H(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值存储在数组下标为 𝑘 +𝑛2k+n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置．
  * 𝑓(𝜔𝑘𝑛)f(ωnk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值将存储在数组下标为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置，𝑓(𝜔𝑘+𝑛/2𝑛)f(ωnk+n/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值将存储在数组下标为 𝑘 +𝑛2k+n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置．

因此可以直接在数组下标为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑘 +𝑛2k+n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置进行覆写，而不用开额外的数组保存值．此方法即称为 **蝶形运算** ，或更准确的，基 - 2 蝶形运算．

再详细说明一下如何借助蝶形运算完成所有段长度为 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的合并操作：

  1. 令段长度为 𝑠 =𝑛2s=n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 同时枚举序列 {𝐺(𝜔𝑘𝑛/2)}{G(ωn/2k)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左端点 𝑙𝑔 =0,2𝑠,4𝑠,⋯,𝑁 −2𝑠lg=0,2s,4s,⋯,N−2s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和序列 {𝐻(𝜔𝑘𝑛/2)}{H(ωn/2k)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左端点 𝑙ℎ =𝑠,3𝑠,5𝑠,⋯,𝑁 −𝑠lh=s,3s,5s,⋯,N−s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  3. 合并两个段时，枚举 𝑘 =0,1,2,⋯,𝑠 −1k=0,1,2,⋯,s−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时 𝐺(𝜔𝑘𝑛/2)G(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存储在数组下标为 𝑙𝑔 +𝑘lg+k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置，𝐻(𝜔𝑘𝑛/2)H(ωn/2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存储在数组下标为 𝑙ℎ +𝑘lh+k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置；
  4. 使用蝶形运算求出 𝑓(𝜔𝑘𝑛)f(ωnk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(𝜔𝑘+𝑛/2𝑛)f(ωnk+n/2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后直接在原位置覆写．

## 快速傅里叶逆变换

傅里叶逆变换可以用傅里叶变换表示．对此我们有两种理解方式．

### 线性代数角度

IDFT（傅里叶反变换）的作用，是把目标多项式的点值形式转换成系数形式．而 DFT 本身是个线性变换，可以理解为将目标多项式当作向量，左乘一个矩阵得到变换后的向量，以模拟把单位复根代入多项式的过程：

⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣𝑦0𝑦1𝑦2𝑦3⋮𝑦𝑛−1⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦=⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣1111⋯11𝜔1𝑛𝜔2𝑛𝜔3𝑛⋯𝜔𝑛−1𝑛1𝜔2𝑛𝜔4𝑛𝜔6𝑛⋯𝜔2(𝑛−1)𝑛1𝜔3𝑛𝜔6𝑛𝜔9𝑛⋯𝜔3(𝑛−1)𝑛⋮⋮⋮⋮⋱⋮1𝜔𝑛−1𝑛𝜔2(𝑛−1)𝑛𝜔3(𝑛−1)𝑛⋯𝜔(𝑛−1)2𝑛⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣𝑎0𝑎1𝑎2𝑎3⋮𝑎𝑛−1⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦[y0y1y2y3⋮yn−1]=[1111⋯11ωn1ωn2ωn3⋯ωnn−11ωn2ωn4ωn6⋯ωn2(n−1)1ωn3ωn6ωn9⋯ωn3(n−1)⋮⋮⋮⋮⋱⋮1ωnn−1ωn2(n−1)ωn3(n−1)⋯ωn(n−1)2][a0a1a2a3⋮an−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

现在我们已经得到最左边的结果了，中间的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值在目标多项式的点值表示中也是一一对应的，所以，根据矩阵的基础知识，我们只要在式子两边左乘中间那个大矩阵的逆矩阵就行了．

由于这个矩阵的元素非常特殊，它的逆矩阵也有特殊的性质，就是每一项 **取倒数** ，再 **除以变换的长度 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)**，就能得到它的逆矩阵．

注意：傅里叶变换的长度，并不是多项式的长度，变换的长度应比乘积多项式的长度长．待相乘的多项式不够长，需要在高次项处补 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

为了使计算的结果为原来的倒数，根据欧拉公式，可以得到

1𝜔𝑘=𝜔−1𝑘=e−2𝜋i𝑘=cos⁡(2𝜋𝑘)+isin⁡(−2𝜋𝑘)1ωk=ωk−1=e−2πik=cos⁡(2πk)+isin⁡(−2πk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此我们可以尝试着把单位根 𝜔𝑘ωk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取成 e−2𝜋i𝑘e−2πik![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样我们的计算结果就会变成原来的倒数，之后唯一多的操作就只有再 **除以它的长度 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)**，而其它的操作过程与 DFT 是完全相同的．我们可以定义一个函数，在里面加一个参数 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或者是 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后把它乘到 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上．传入 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 DFT，传入 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 IDFT．

### 单位复根周期性

利用单位复根的周期性同样可以理解 IDFT 与 DFT 之间的关系．

考虑原本的多项式是 𝑓(𝑥) =𝑎0 +𝑎1𝑥 +𝑎2𝑥2 +⋯ +𝑎𝑛−1𝑥𝑛−1 =∑𝑛−1𝑖=0𝑎𝑖𝑥𝑖f(x)=a0+a1x+a2x2+⋯+an−1xn−1=∑i=0n−1aixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而 IDFT 就是把你的点值表示还原为系数表示．

考虑 **构造法** ．我们已知 𝑦𝑖 =𝑓(𝜔𝑖𝑛),𝑖 ∈{0,1,⋯,𝑛 −1}yi=f(ωni),i∈{0,1,⋯,n−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 {𝑎0,𝑎1,⋯,𝑎𝑛−1}{a0,a1,⋯,an−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．构造多项式如下

𝐴(𝑥)=𝑛−1∑𝑖=0𝑦𝑖𝑥𝑖A(x)=∑i=0n−1yixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

相当于把 {𝑦0,𝑦1,𝑦2,⋯,𝑦𝑛−1}{y0,y1,y2,⋯,yn−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当做多项式 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数表示法．

这时我们有两种推导方式，这对应了两种实现方法．

#### 方法一

设 𝑏𝑖 =𝜔−𝑖𝑛bi=ωn−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则多项式 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥 =𝑏0,𝑏1,⋯,𝑏𝑛−1x=b0,b1,⋯,bn−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的点值表示法为 {𝐴(𝑏0),𝐴(𝑏1),⋯,𝐴(𝑏𝑛−1)}{A(b0),A(b1),⋯,A(bn−1)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对 𝐴(𝑥)A(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义式做一下变换，可以将 𝐴(𝑏𝑘)A(bk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示为

𝐴(𝑏𝑘)=𝑛−1∑𝑖=0𝑓(𝜔𝑖𝑛)𝜔−𝑖𝑘𝑛=𝑛−1∑𝑖=0𝜔−𝑖𝑘𝑛𝑛−1∑𝑗=0𝑎𝑗(𝜔𝑖𝑛)𝑗=𝑛−1∑𝑖=0𝑛−1∑𝑗=0𝑎𝑗𝜔𝑖(𝑗−𝑘)𝑛=𝑛−1∑𝑗=0𝑎𝑗𝑛−1∑𝑖=0(𝜔𝑗−𝑘𝑛)𝑖A(bk)=∑i=0n−1f(ωni)ωn−ik=∑i=0n−1ωn−ik∑j=0n−1aj(ωni)j=∑i=0n−1∑j=0n−1ajωni(j−k)=∑j=0n−1aj∑i=0n−1(ωnj−k)i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

记 𝑆(𝜔𝑎𝑛) =∑𝑛−1𝑖=0(𝜔𝑎𝑛)𝑖S(ωna)=∑i=0n−1(ωna)i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当 𝑎 =0(mod𝑛)a=0(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑆(𝜔𝑎𝑛) =𝑛S(ωna)=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当 𝑎 ≠0(mod𝑛)a≠0(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，我们错位相减

𝑆(𝜔𝑎𝑛)=𝑛−1∑𝑖=0(𝜔𝑎𝑛)𝑖𝜔𝑎𝑛𝑆(𝜔𝑎𝑛)=𝑛∑𝑖=1(𝜔𝑎𝑛)𝑖𝑆(𝜔𝑎𝑛)=(𝜔𝑎𝑛)𝑛−(𝜔𝑎𝑛)0𝜔𝑎𝑛−1=0S(ωna)=∑i=0n−1(ωna)iωnaS(ωna)=∑i=1n(ωna)iS(ωna)=(ωna)n−(ωna)0ωna−1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说

𝑆(𝜔𝑎𝑛)={𝑛,𝑎=00,𝑎≠0S(ωna)={n,a=00,a≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么代回原式

𝐴(𝑏𝑘)=𝑛−1∑𝑗=0𝑎𝑗𝑆(𝜔𝑗−𝑘𝑛)=𝑎𝑘⋅𝑛A(bk)=∑j=0n−1ajS(ωnj−k)=ak⋅n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说给定点 𝑏𝑖 =𝜔−𝑖𝑛bi=ωn−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点值表示法为

{(𝑏0,𝐴(𝑏0)),(𝑏1,𝐴(𝑏1)),⋯,(𝑏𝑛−1,𝐴(𝑏𝑛−1))}={(𝑏0,𝑎0⋅𝑛),(𝑏1,𝑎1⋅𝑛),⋯,(𝑏𝑛−1,𝑎𝑛−1⋅𝑛)}{(b0,A(b0)),(b1,A(b1)),⋯,(bn−1,A(bn−1))}={(b0,a0⋅n),(b1,a1⋅n),⋯,(bn−1,an−1⋅n)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

综上所述，我们取单位根为其倒数，对 {𝑦0,𝑦1,𝑦2,⋯,𝑦𝑛−1}{y0,y1,y2,⋯,yn−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 跑一遍 FFT，然后除以 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可得到 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数表示．

#### 方法二

我们直接将 𝜔𝑖𝑛ωni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代入 𝐴(𝑥)A(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

推导的过程与方法一大同小异，最终我们得到 𝐴(𝜔𝑘𝑛) =∑𝑛−1𝑗=0𝑎𝑗𝑆(𝜔𝑗+𝑘𝑛)A(ωnk)=∑j=0n−1ajS(ωnj+k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当且仅当 𝑗 +𝑘 =0(mod𝑛)j+k=0(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时有 𝑆(𝜔𝑗+𝑘𝑛) =𝑛S(ωnj+k)=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此 𝐴(𝜔𝑘𝑛) =𝑎𝑛−𝑘 ⋅𝑛A(ωnk)=an−k⋅n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这意味着我们将 {𝑦0,𝑦1,𝑦2,⋯,𝑦𝑛−1}{y0,y1,y2,⋯,yn−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做 DFT 变换后除以 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再反转后 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素，同样可以还原 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数表示．

### 代码实现

所以我们 FFT 函数可以集 DFT 和 IDFT 于一身．代码实现如下：

非递归版 FFT（对应方法一）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` |  ```text /* * 做 FFT * len 必须是 2^k 形式 * on == 1 时是 DFT，on == -1 时是 IDFT */ void fft ( Complex y [], int len , int on ) { // 位逆序置换 change ( y , len ); // 模拟合并过程，一开始，从长度为一合并到长度为二，一直合并到长度为 len． for ( int h = 2 ; h <= len ; h <<= 1 ) { // wn：当前单位复根的间隔：w^1_h Complex wn ( cos ( 2 * PI / h ), sin ( on * 2 * PI / h )); // 合并，共 len / h 次． for ( int j = 0 ; j < len ; j += h ) { // 计算当前单位复根，一开始是 1 = w^0_n，之后是以 wn 为间隔递增： w^1_n // ... Complex w ( 1 , 0 ); for ( int k = j ; k < j \+ h / 2 ; k ++ ) { // 左侧部分和右侧是子问题的解 Complex u = y [ k ]; Complex t = w * y [ k \+ h / 2 ]; // 这就是把两部分分治的结果加起来 y [ k ] = u \+ t ; y [ k \+ h / 2 ] = u \- t ; // 后半个 「step」 中的ω一定和 「前半个」 中的成相反数 // 「红圈」上的点转一整圈「转回来」，转半圈正好转成相反数 // 一个数相反数的平方与这个数自身的平方相等 w = w * wn ; } } } // 如果是 IDFT，它的逆矩阵的每一个元素不只是原元素取倒数，还要除以长度 len． if ( on == -1 ) { for ( int i = 0 ; i < len ; i ++ ) { y [ i ]. x /= len ; y [ i ]. y /= len ; } } } ```   
---|---  
  
非递归版 FFT（对应方法二）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 ``` |  ```text /* * 做 FFT * len 必须是 2^k 形式 * on == 1 时是 DFT，on == -1 时是 IDFT */ void fft ( Complex y [], int len , int on ) { change ( y , len ); for ( int h = 2 ; h <= len ; h <<= 1 ) { // 模拟合并过程 Complex wn ( cos ( 2 * PI / h ), sin ( 2 * PI / h )); // 计算当前单位复根 for ( int j = 0 ; j < len ; j += h ) { Complex w ( 1 , 0 ); // 计算当前单位复根 for ( int k = j ; k < j \+ h / 2 ; k ++ ) { Complex u = y [ k ]; Complex t = w * y [ k \+ h / 2 ]; y [ k ] = u \+ t ; // 这就是把两部分分治的结果加起来 y [ k \+ h / 2 ] = u \- t ; // 后半个 「step」 中的ω一定和 「前半个」 中的成相反数 // 「红圈」上的点转一整圈「转回来」，转半圈正好转成相反数 // 一个数相反数的平方与这个数自身的平方相等 w = w * wn ; } } } if ( on == -1 ) { reverse ( y \+ 1 , y \+ len ); for ( int i = 0 ; i < len ; i ++ ) { y [ i ]. x /= len ; y [ i ]. y /= len ; } } } ```   
---|---  
  
FFT 模板（[HDU 1402 - A * B Problem Plus](http://acm.hdu.edu.cn/showproblem.php?pid=1402)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 ``` |  ```text #include <cmath> #include <cstring> #include <iostream> const double PI = acos ( -1.0 ); struct Complex { double x , y ; Complex ( double _x = 0.0 , double _y = 0.0 ) { x = _x ; y = _y ; } Complex operator \- ( const Complex & b ) const { return Complex ( x \- b . x , y \- b . y ); } Complex operator \+ ( const Complex & b ) const { return Complex ( x \+ b . x , y \+ b . y ); } Complex operator * ( const Complex & b ) const { return Complex ( x * b . x \- y * b . y , x * b . y \+ y * b . x ); } }; /* * 进行 FFT 和 IFFT 前的反置变换 * 位置 i 和 i 的二进制反转后的位置互换 *len 必须为 2 的幂 */ void change ( Complex y [], int len ) { int i , j , k ; for ( int i = 1 , j = len / 2 ; i < len \- 1 ; i ++ ) { if ( i < j ) std :: swap ( y [ i ], y [ j ]); // 交换互为小标反转的元素，i<j 保证交换一次 // i 做正常的 + 1，j 做反转类型的 + 1，始终保持 i 和 j 是反转的 k = len / 2 ; while ( j >= k ) { j = j \- k ; k = k / 2 ; } if ( j < k ) j += k ; } } /* * 做 FFT *len 必须是 2^k 形式 *on == 1 时是 DFT，on == -1 时是 IDFT */ void fft ( Complex y [], int len , int on ) { change ( y , len ); for ( int h = 2 ; h <= len ; h <<= 1 ) { Complex wn ( cos ( 2 * PI / h ), sin ( on * 2 * PI / h )); for ( int j = 0 ; j < len ; j += h ) { Complex w ( 1 , 0 ); for ( int k = j ; k < j \+ h / 2 ; k ++ ) { Complex u = y [ k ]; Complex t = w * y [ k \+ h / 2 ]; y [ k ] = u \+ t ; y [ k \+ h / 2 ] = u \- t ; w = w * wn ; } } } if ( on == -1 ) { for ( int i = 0 ; i < len ; i ++ ) { y [ i ]. x /= len ; } } } constexpr int MAXN = 200020 ; Complex x1 [ MAXN ], x2 [ MAXN ]; char str1 [ MAXN / 2 ], str2 [ MAXN / 2 ]; int sum [ MAXN ]; using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); while ( cin >> str1 >> str2 ) { int len1 = strlen ( str1 ); int len2 = strlen ( str2 ); int len = 1 ; while ( len < len1 * 2 || len < len2 * 2 ) len <<= 1 ; for ( int i = 0 ; i < len1 ; i ++ ) x1 [ i ] = Complex ( str1 [ len1 \- 1 \- i ] \- '0' , 0 ); for ( int i = len1 ; i < len ; i ++ ) x1 [ i ] = Complex ( 0 , 0 ); for ( int i = 0 ; i < len2 ; i ++ ) x2 [ i ] = Complex ( str2 [ len2 \- 1 \- i ] \- '0' , 0 ); for ( int i = len2 ; i < len ; i ++ ) x2 [ i ] = Complex ( 0 , 0 ); fft ( x1 , len , 1 ); fft ( x2 , len , 1 ); for ( int i = 0 ; i < len ; i ++ ) x1 [ i ] = x1 [ i ] * x2 [ i ]; fft ( x1 , len , -1 ); for ( int i = 0 ; i < len ; i ++ ) sum [ i ] = int ( x1 [ i ]. x \+ 0.5 ); for ( int i = 0 ; i < len ; i ++ ) { sum [ i \+ 1 ] += sum [ i ] / 10 ; sum [ i ] %= 10 ; } len = len1 \+ len2 \- 1 ; while ( sum [ len ] == 0 && len > 0 ) len \-- ; for ( int i = len ; i >= 0 ; i \-- ) cout << char ( sum [ i ] \+ '0' ); cout << '\n' ; } return 0 ; } ```   
---|---  
  
## 参考文献

  1. [桃酱的算法笔记](https://zhuanlan.zhihu.com/p/41867199).

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/fft.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/fft.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [H-J-Granger](https://github.com/H-J-Granger), [StudyingFather](https://github.com/StudyingFather), [Early0v0](https://github.com/Early0v0), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [ouuan](https://github.com/ouuan), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [AngelKitty](https://github.com/AngelKitty), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [Great-designer](https://github.com/Great-designer), [greyqz](https://github.com/greyqz), [ranwen](https://github.com/ranwen), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [billchenchina](https://github.com/billchenchina), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [hly1204](https://github.com/hly1204), [Xeonacid](https://github.com/Xeonacid), [abc1763613206](https://github.com/abc1763613206), [Ahacad](https://github.com/Ahacad), [Allenyou1126](https://github.com/Allenyou1126), [AndrewWayne](https://github.com/AndrewWayne), [AtomAlpaca](https://github.com/AtomAlpaca), [Backl1ght](https://github.com/Backl1ght), [Cheuring](https://github.com/Cheuring), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [cjsoft](https://github.com/cjsoft), [DepletedPrism](https://github.com/DepletedPrism), [diauweb](https://github.com/diauweb), [EarthMessenger](https://github.com/EarthMessenger), [ezoixx130](https://github.com/ezoixx130), [F1shAndCat](https://github.com/F1shAndCat), [GekkaSaori](https://github.com/GekkaSaori), [henryrabbit](https://github.com/henryrabbit), [heroming](https://github.com/heroming), [isdanni](https://github.com/isdanni), [jiang1997](https://github.com/jiang1997), [kenlig](https://github.com/kenlig), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [lucifer1004](https://github.com/lucifer1004), [Makkiy](https://github.com/Makkiy), [Menci](https://github.com/Menci), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [muoshuosha](https://github.com/muoshuosha), [needtocalmdown](https://github.com/needtocalmdown), [opsiff](https://github.com/opsiff), [P-Y-Y](https://github.com/P-Y-Y), [partychicken](https://github.com/partychicken), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [schtonn](https://github.com/schtonn), [SukkaW](https://github.com/SukkaW), [Suyun514](mailto:suyun514@qq.com), [Taoran-01](https://github.com/Taoran-01), [untitledunrevised](https://github.com/untitledunrevised), [weiyong1024](https://github.com/weiyong1024), [YouXam](https://github.com/YouXam), [Yukimaikoriya](https://github.com/Yukimaikoriya), [Haohu Shen](https://github.com/Haohu Shen), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [Lewy Zeng](mailto:zengxingchen@csu.edu.cn), [Lewy Zeng](https://github.com/Lewy Zeng), [lychees](https://github.com/lychees), [ouuan](mailto:1609483441@qq.com), [Peanut-Tang](https://github.com/Peanut-Tang), [shuzhouliu](https://github.com/shuzhouliu), [Sshwy](mailto:hwy1272918035@outlook.com), [Sshwy](https://github.com/Sshwy), [TrisolarisHD](https://github.com/TrisolarisHD), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
