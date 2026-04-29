# 多项式与生成函数简介 - OI Wiki

- Source: https://oi-wiki.org/math/poly/intro/

# 多项式与生成函数简介

## 多项式与生成函数

操纵 有限项/无限项 的多项式是 OI 数学中，尤其是生成函数中的重要内容．

以 [快速傅里叶变换](../fft/) 为基石的多项式算法赋予了算法竞赛选手直接操纵生成函数的能力．

## 基本概念

对于求和式 ∑𝑎𝑛𝑥𝑛∑anxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果是有限项相加，称为多项式，记作 𝑓(𝑥) =∑𝑚𝑛=0𝑎𝑛𝑥𝑛f(x)=∑n=0manxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

可列项相加的求和式称为级数．在和式 ∑∞𝑛=0𝑎𝑛𝑥𝑛∑n=0∞anxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，每项均为非负整数次幂函数乘常数系数，这种形式的级数称为幂级数．

研究多项式算术时先考虑较简单的多项式，幂级数概念仅用于方便理解．到了数学分析中会进一步研究幂级数的敛散性．

环、域及其衍生结构的一般定义详见 [抽象代数基本概念](../../algebra/basic/)．

对于一般环 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的 **多项式环** （polynomial ring）𝑅[𝑥]R[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

每个元素 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的 **多项式** （polynomial），可表示为

𝑓=⟨𝑓0,𝑓1,𝑓2,⋯,𝑓𝑛⟩(𝑓0,𝑓1,𝑓2,⋯,𝑓𝑛∈𝑅)f=⟨f0,f1,f2,⋯,fn⟩(f0,f1,f2,⋯,fn∈R)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

换言之，我们将多项式直接定义为系数序列．也可以表示为

𝑓(𝑥)=𝑓0+𝑓1𝑥+𝑓2𝑥2+⋯+𝑓𝑛𝑥𝑛f(x)=f0+f1x+f2x2+⋯+fnxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此处我们认为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只是一个 **形式符号** ，一个对系数位置的标识符．

如果我们还允许无穷项的存在，即

𝑓(𝑥)=𝑓0+𝑓1𝑥+𝑓2𝑥2+⋯f(x)=f0+f1x+f2x2+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则可得到 **形式幂级数环** （formal power series ring）𝑅[[𝑥]]R[[x]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中的每个元素 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 **形式幂级数** （formal power series），以下简称幂级数．

### 多项式的次数

对于一个多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称其最高次项的次数为该多项式的 **次数（degree）** ，记作 deg⁡𝑓deg⁡f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 多项式的乘法

最核心的操作是两个多项式的乘法，即给定多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑓(𝑥)=𝑎0+𝑎1𝑥+⋯+𝑎𝑛𝑥𝑛(1)𝑔(𝑥)=𝑏0+𝑏1𝑥+⋯+𝑏𝑚𝑥𝑚(2)f(x)=a0+a1x+⋯+anxn(1)g(x)=b0+b1x+⋯+bmxm(2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

要计算多项式 𝑄(𝑥) =𝑓(𝑥) ⋅𝑔(𝑥)Q(x)=f(x)⋅g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑄(𝑥)=𝑛∑𝑖=0𝑚∑𝑗=0𝑎𝑖𝑏𝑗𝑥𝑖+𝑗=𝑐0+𝑐1𝑥+⋯+𝑐𝑛+𝑚𝑥𝑛+𝑚Q(x)=∑i=0n∑j=0maibjxi+j=c0+c1x+⋯+cn+mxn+m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

多项式或幂级数的乘法，满足结合律，关于加法满足分配律．若 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为交换环或幺环，乘法相应的有交换律和单位元．

若 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上存在 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单位根，[快速傅里叶变换](../fft/) 允许我们在 𝑂(𝑛2𝑛)O(n2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而不是 𝑂(22𝑛)O(22n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内计算两个 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次多项式的乘积．

### 复合

定义 𝑅[[𝑥]]R[[x]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘方为

𝑓1=𝑓,𝑓𝑘=𝑓𝑘−1×𝑓f1=f,fk=fk−1×f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在此基础上，定义 𝑅[[𝑥]]R[[x]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中元素 𝑓,𝑔f,g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复合为

(𝑓∘𝑔)(𝑥)=𝑓(𝑔(𝑥))=𝑓0++∞∑𝑘=1𝑓𝑘𝑔𝑘(𝑥)(f∘g)(x)=f(g(x))=f0+∑k=1+∞fkgk(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们规定 𝑓 ∘𝑔f∘g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在当且仅当 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为有限项或 𝑔0 =0g0=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样就不涉及 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的极限了．

∘∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足结合律（(𝑓 ∘𝑔) ∘ℎ(f∘g)∘h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓 ∘(𝑔 ∘ℎ)f∘(g∘h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均存在时），不满足交换律．𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为幺环时 ∘∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在单位元 1 ×𝑥1×x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

多项式复合（与复合逆）有 Θ(𝑛log2⁡𝑛)Θ(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的做法，其由 Yasunori Kinoshita 与李白天于 2024 年提出，详见 [形式幂级数复合 | 复合逆](../comp-rev/)．

### 导数

尽管一般环甚至未必存在极限，  
我们依然可以定义形式幂级数的 **形式导数** （formal derivative）为

(+∞∑𝑘=0𝑓𝑘𝑥𝑘)′=+∞∑𝑘=1𝑘𝑓𝑘𝑥𝑘−1(∑k=0+∞fkxk)′=∑k=1+∞kfkxk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中

𝑘𝑓𝑘=𝑓𝑘+𝑓𝑘+⋯+𝑓𝑘⏟__⏟__⏟𝑘个𝑓𝑘kfk=fk+fk+⋯+fk⏟k个fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

基本求导法则——加法法则、乘法法则、链式法则（复合允许的情况下）依然是正确的．

如果 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上允许作除法，同样可以类似定义形式幂级数的 **形式不定积分** （formal indefinite integral）．

### 乘法逆元

根据例子

11−𝑥=1+𝑥+𝑥2+⋯11−x=1+x+x2+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以知道，多项式的倒数是能展开为无穷级数的．存在倒数，当且仅当常数项不为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且倒数也满足常数项不为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此定义：对于形式幂级数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 𝑓0 ≠0f0≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其 **乘法逆元** （multiplicative inversion）𝑓−1f−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为另一形式幂级数，满足

𝑓×𝑓−1=𝑓−1×𝑓=1f×f−1=f−1×f=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

用形式幂级数乘法定义展开该式，可得 𝑓−1f−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 系数的递推式

𝑓−10=1𝑓0,𝑓−1𝑛=−1𝑓0𝑛−1∑𝑘=0𝑓−1𝑘𝑓𝑛−𝑘f0−1=1f0,fn−1=−1f0∑k=0n−1fk−1fn−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

直接用递推式计算前 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项是 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，[运用 FFT](../elementary-func/#多项式求逆) 可得到 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的算法．

注

容易发现，𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倒数就是 1𝑓(𝑥)1f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的无穷项麦克劳林展开（在 𝑥 =0x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的无穷项泰勒展开）．

### 常见的幂级数展开式

在数学分析中，在某点处或某区间上若干阶可导的一元函数可以在相应范围进行多项式展开，一般统称为泰勒展开，如果在 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处展开，也称为麦克劳林展开．

如果无穷阶可导，则可以进行幂级数展开．最常见的还是在 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处展开．

在复变函数中，一些函数在奇点上虽然不能进行泰勒展开，但是可以进行洛朗展开．

下列等式只在幂级数收敛时成立，在不收敛时不成立．这里只写出展开式，不讨论收敛域．

基本的展开式有以下两个，指数函数和幂函数：

e𝑥=1+𝑥+12!𝑥2+…+1𝑛!𝑥𝑛+…ex=1+x+12!x2+…+1n!xn+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(1+𝑥)𝑎=1+𝑎𝑥+𝑎(𝑎−1)2!𝑥2+…+𝑎(𝑎−1)…(𝑎−𝑛+1)𝑛!𝑥𝑛+…(1+x)a=1+ax+a(a−1)2!x2+…+a(a−1)…(a−n+1)n!xn+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

更多的展开式经常由上述两个变形得到．比如正余弦函数由指数函数代入复数得到：

cos⁡𝑥=1−12!𝑥2+14!𝑥4+…+(−1)𝑛(2𝑛)!𝑥2𝑛+…cos⁡x=1−12!x2+14!x4+…+(−1)n(2n)!x2n+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)sin⁡𝑥=𝑥−13!𝑥3+15!𝑥5+…+(−1)𝑛(2𝑛+1)!𝑥2𝑛+1+…sin⁡x=x−13!x3+15!x5+…+(−1)n(2n+1)!x2n+1+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对数和反正切、反正弦函数由积分得到：

11+𝑥=1−𝑥+𝑥2+…+(−1)𝑛𝑥𝑛+…11+x=1−x+x2+…+(−1)nxn+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)ln⁡(1+𝑥)=𝑥−12𝑥2+13𝑥3+…+(−1)𝑛−1𝑛𝑥𝑛+…ln⁡(1+x)=x−12x2+13x3+…+(−1)n−1nxn+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)11+𝑥2=1−𝑥2+𝑥4+…+(−1)𝑛𝑥2𝑛+…11+x2=1−x2+x4+…+(−1)nx2n+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)arctan⁡𝑥=𝑥−13𝑥3+15𝑥5+…+(−1)𝑛2𝑛+1𝑥2𝑛+1+…arctan⁡x=x−13x3+15x5+…+(−1)n2n+1x2n+1+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)1√1+𝑥=1−12𝑥+38𝑥2+…+(−1)𝑛(2𝑛)!(𝑛!)24𝑛𝑥𝑛+…11+x=1−12x+38x2+…+(−1)n(2n)!(n!)24nxn+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)1√1−𝑥2=1+12𝑥2+38𝑥4+…+(2𝑛)!(𝑛!)24𝑛𝑥2𝑛+…11−x2=1+12x2+38x4+…+(2n)!(n!)24nx2n+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)arcsin⁡𝑥=𝑥+16𝑥3+340𝑥5+…+(2𝑛)!(𝑛!)2(2𝑛+1)4𝑛𝑥2𝑛+1+…arcsin⁡x=x+16x3+340x5+…+(2n)!(n!)2(2n+1)4nx2n+1+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 复合逆

**复合逆** （compound inversion）即反函数概念在形式幂级数环上的推广．

对于满足 𝑓0 =0f0=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓1 ≠0f1≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式幂级数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其复合逆为满足 𝑔(𝑓(𝑥)) =𝑓(𝑔(𝑥)) =𝑥g(f(x))=f(g(x))=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式幂级数 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由拉格朗日反演可得对于任意整数 𝑛,𝑘n,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

𝑛[𝑥𝑛]𝑓𝑘=𝑘[𝑥𝑛−𝑘](𝑥𝑔)𝑛n[xn]fk=k[xn−k](xg)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 [𝑥𝑘]𝑓(𝑥)[xk]f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑥𝑘xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的系数．

### 多项式整除

对于多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和多项式 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果存在一个多项式 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得：

𝑓(𝑥)=𝑔(𝑥)ℎ(𝑥)f(x)=g(x)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则多项式 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

显而易见，多项式 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的根全部为 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的根，并且在 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的重数不超过在 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的相应重数．

### 多项式的余数和商

对于多项式 𝑓(𝑥),𝑔(𝑥)f(x),g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，存在 **唯一** 的 𝑄(𝑥),𝑅(𝑥)Q(x),R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足：

𝑓(𝑥)=𝑄(𝑥)𝑔(𝑥)+𝑅(𝑥)deg⁡𝑅<deg⁡𝑔f(x)=Q(x)g(x)+R(x)deg⁡R<deg⁡g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当 deg⁡𝑓 ≥deg⁡𝑔deg⁡f≥deg⁡g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时有 deg⁡𝑄 =deg⁡𝑓 −deg⁡𝑔deg⁡Q=deg⁡f−deg⁡g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则有 𝑄(𝑥) =0Q(x)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们称 𝑄(𝑥)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 除 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **商（quotient）** ，𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 除 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **余数（remainder）** ．

## 模多项式

模多项式是多项式环的子环，由多项式环除以同余的等价关系得到．

在上文提到的带余除法中，多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与它的余式 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模多项式 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的意义下同余．

𝑓(𝑥)≡𝑅(𝑥)(mod𝑔(𝑥))f(x)≡R(x)(modg(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个同余式也意味着，对于多项式 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的任意一个根 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，代入 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，得到的点值相同．即：

𝑓(𝑥0)=𝑅(𝑥0)f(x0)=R(x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

并且，如果根 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在多项式 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的重数是 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 (𝑥 −𝑥0)𝑘(x−x0)k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对任意大于等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

𝑓𝑡(𝑥0)=𝑅𝑡(𝑥0)ft(x0)=Rt(x0)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里的记号表示 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶导数．

模多项式同余可以应用于幂级数．一个无限项的幂级数，可以在模具体的多项式情形下，和一个有限项的多项式同余．例如：

1+𝑥+𝑥2+𝑥3+…≡1+𝑥+…+𝑥𝑛−1(mod𝑥𝑛)1+x+x2+x3+…≡1+x+…+xn−1(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

显然剩余的所有项都被 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除，因此模 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的操作等价于「截断」，将无穷项的幂级数截断到前 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项，直接将更高位的信息丢失．

在一些特定的情况下，也可以模其他的多项式，下文将解释相应情况．

### 多项式的多点求值和插值

**多项式的多点求值（multi-point evaluation）** 即给出一个多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点 𝑥1,𝑥2,…,𝑥𝑛x1,x2,…,xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求

𝑓(𝑥1),𝑓(𝑥2),…,𝑓(𝑥𝑛)f(x1),f(x2),…,f(xn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**多项式的插值（interpolation）** 即给出 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点

(𝑥0,𝑦0),(𝑥1,𝑦1),…,(𝑥𝑛,𝑦𝑛)(x0,y0),(x1,y1),…,(xn,yn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

求一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得这 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点都在 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上．

这两种操作的实质就是将多项式在 **系数表示** 和 **点值表示** 间转化．多点求值将多项式的系数表示转为点值表示，插值将多项式的点值表示转为系数表示．

注

按照幂级数的观点看，多点求值相当于将无穷项的信息「压缩」到有限个点值表示，因此丢失了一些信息，而插值相当于还原到相应次数的系数表示．

编程常见的求值与插值，例如离散傅里叶变换（及其逆变换）等等，选择的 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点重数均为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即两两不同，免去求导的麻烦．

这种「压缩」只保证了在 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点上的一致．根据上文对模多项式同余的解释，如果幂级数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 经过在 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点处求值再插值，得到多项式 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则作多项式：

𝑔(𝑥)=(𝑥−𝑥0)…(𝑥−𝑥𝑛)g(x)=(x−x0)…(x−xn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就有：

𝑓(𝑥)≡𝑅(𝑥)(mod𝑔(𝑥))f(x)≡R(x)(modg(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的次数严格小于 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以利用求值与插值求出的 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是余式．因此在这种情况下，如果幂级数在根处可以求值，就可以模多项式．一个反例例如：

11−𝑥=1+𝑥+𝑥2+𝑥3+…11−x=1+x+x2+x3+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在 𝑥 =1x=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处不可求值，因此级数 1 +𝑥 +𝑥2 +𝑥3 +…1+x+x2+x3+…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不能模多项式 𝑥 −1x−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于幂级数的任意阶导数，在 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的值总是存在，因此模 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 始终可以计算，与上文「截断」的意义一致．离散傅里叶变换（及其逆变换）相当于模多项式 𝑥𝑛 −1xn−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 因式分解和欧几里得

初等数论中的许多结论可以推广到多项式上．

复数域上，由代数基本定理可得，对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次多项式 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，方程

𝑓(𝑥)=0f(x)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

有且仅有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个解（重根按重数计）．

于是 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在复数域内可唯一因式分解为如下形式

𝑎(𝑥−𝑥1)𝑐1(𝑥−𝑥2)𝑐2⋯(𝑥−𝑥𝑚)𝑐𝑚a(x−x1)c1(x−x2)c2⋯(x−xm)cm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑐1+𝑐2+⋯+𝑐𝑚=𝑛,𝑥1,𝑥2,⋯,𝑥𝑚 互不相同c1+c2+⋯+cm=n,x1,x2,⋯,xm 互不相同![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此时类比正整数的最大公因数，可得多项式的 [**最大公因式**](../../number-theory/gcd/)  
（greatest common divisor, gcd）．其可用欧几里得算法求解

gcd(𝑓,0)=𝑓,gcd(𝑓,𝑔)=gcd(𝑔,𝑓mod𝑔)gcd(f,0)=f,gcd(f,g)=gcd(g,fmodg)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

该性质可以推广到较为一般的情况：

> 对于任意域 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的多项式环 𝑃[𝑥]P[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，  
>  多项式均可唯一因式分解，且可用欧几里得算法计算最大公因式． 需要注意的是，对于一般环上的多项式，该结论未必成立．

欧几里得算法成立时，可用扩展欧几里得给出不定方程

𝑓(𝑥)𝑃(𝑥)+𝑔(𝑥)𝑄(𝑥)=gcd(𝑓(𝑥),𝑔(𝑥))f(x)P(x)+g(x)Q(x)=gcd(f(x),g(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的一组特解 (𝑃(𝑥),𝑄(𝑥))(P(x),Q(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并用 [裴蜀定理](../../number-theory/bezouts/) 判断不定方程

𝑓(𝑥)𝑃(𝑥)+𝑔(𝑥)𝑄(𝑥)=ℎ(𝑥)f(x)P(x)+g(x)Q(x)=h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的可解性．

[HALF-GCD](https://loj.ac/p/172) 允许我们在 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算多项式欧几里得．

### 模多项式的乘法逆元

在模多项式 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下，幂级数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有时存在逆元．逆元就是幂级数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倒数模多项式 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到的余式．

这个定义也等价于，对于多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若存在 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足：

𝑓(𝑥)𝑔(𝑥)≡1(modℎ(𝑥))f(x)g(x)≡1(modh(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则称 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的 **逆元（inverse element）** ．当多项式欧几里得允许时，逆元存在当且仅当 gcd(𝑓,𝑔) =1gcd(f,g)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

模多项式 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下逆元总是唯一的．如果多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的次数也小于 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则得到的 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互为逆元．

考虑「截断」的概念，一般把模 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的逆元记作 𝑓−1(𝑥)f−1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也是后文默认使用的逆元概念．如果不加说明，逆元的模就是指 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注

一个问题是，可不可以用各种插值变换，直接求解「逆元」，比如计算：

𝐼𝐷𝐹𝑇(𝐷𝐹𝑇(1)𝐷𝐹𝑇(𝑓(𝑥)))IDFT(DFT(1)DFT(f(x)))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

答案是否定的，不可以这样做．根据上文的解释，这里利用离散傅里叶变换（及其逆变换）直接求出的逆元是模多项式 𝑥𝑛 −1xn−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆元，不是通常的模多项式 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆元．并且，由于原多项式在各点值处可能为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这个求解未必可以进行．

## 生成函数

生成函数（generating function），又称母函数，是一种形式幂级数，其每一项的系数可以提供关于这个序列的信息．

生成函数有许多不同的种类，但大多可以表示为单一的形式：

𝐹(𝑥)=∑𝑛𝑎𝑛𝑘𝑛(𝑥)F(x)=∑nankn(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑘𝑛(𝑥)kn(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被称为核函数．不同的核函数会导出不同的生成函数，拥有不同的性质．举个例子：

  1. 普通生成函数：𝑘𝑛(𝑥) =𝑥𝑛kn(x)=xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 指数生成函数：𝑘𝑛(𝑥) =𝑥𝑛𝑛!kn(x)=xnn!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. [狄利克雷生成函数](../../number-theory/dirichlet/#dirichlet-生成函数)：𝑘𝑛(𝑥) =1𝑛𝑥kn(x)=1nx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 参考资料与拓展阅读

  * [**Picks's Blog**](https://picks.logdown.com)
  * [**Miskcoo's Space**](https://blog.miskcoo.com)
  * [**Polynomial ring - Wikipedia**](https://en.wikipedia.org/wiki/Polynomial_ring)
  * [**Formal power series - Wikipedia**](https://en.wikipedia.org/wiki/Formal_power_series#The_ring_of_formal_power_series)
  * 《信息学竞赛中的生成函数计算理论框架》

* * *

>  __本页面最近更新： 2026/4/26 00:37:21，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/intro.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/intro.md "edit.link.title")  
>  __本页面贡献者：[fps5283](https://github.com/fps5283), [Tiphereth-A](https://github.com/Tiphereth-A), [Ir1d](https://github.com/Ir1d), [c-forrest](https://github.com/c-forrest), [shuzhouliu](https://github.com/shuzhouliu), [CCXXXI](https://github.com/CCXXXI), [Enter-tainer](https://github.com/Enter-tainer), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [EntropyIncreaser](https://github.com/EntropyIncreaser), [Great-designer](https://github.com/Great-designer), [Menci](https://github.com/Menci), [R-fzx](https://github.com/R-fzx), [SaisycJiang](https://github.com/SaisycJiang), [shq666](https://github.com/shq666), [StudyingFather](https://github.com/StudyingFather), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
