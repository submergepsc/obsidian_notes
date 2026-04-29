# 模算术简介 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/mod-arithmetic/

# 模算术简介

算法竞赛中，数论部分的一个重要组成部分就是 **模算术** （modular arithmetic），也就是在某一模数下进行各种整数运算．除了基础的四则运算和求幂外，还可以方便地进行取对数、开各次方、求阶乘和组合数等运算．

模算术常见于各类问题中，而不仅仅局限于数论部分．很多问题的实际答案可能非常大，超过了常见的整型变量的存储范围．此时，为了避免引入大整数运算和输出长数字，题目常常要求对答案取模后输出．这就要求熟练掌握各类模算术技巧．

## C/C++ 的整数除法和取模运算

在 C/C++ 中，整数除法和取模运算，与数学上习惯的取模和除法不一致．

对于所有标准版本的 C/C++，规定在整数除法中：

  1. 当除数为 0 时，行为未定义；
  2. 否则 `(a / b) * b + a % b` 的运算结果与 `a` 相等．

也就是说，取模运算的符号取决于除法如何取整；而除法如何取整，这是实现定义的（由编译器决定）．

从 [C99](https://en.cppreference.com/w/c/language/operator_arithmetic) 和 [C++11](https://en.cppreference.com/w/cpp/language/operator_arithmetic) 标准版本起，规定 **商向零取整** （舍弃小数部分）；取模的符号就与被除数相同．从此，以下断言保证为真：

```text 1 2 3 4 ``` |  ```text assert ( 5 % 3 == 2 ); assert ( 5 % -3 == 2 ); assert ( -5 % 3 == -2 ); assert ( -5 % -3 == -2 ); ```   
---|---  
  
## 模整数类

模算术可以看做是对某模数下的 [同余类](../basic/#同余类与剩余系) 进行各种运算．如果用一个结构体来表示一个同余类，并且将同余类之间的加、减、乘等运算封装为结构体的方法或运算符重载，那么模算术就可以自然地实现为一个模整数类．下面给出一个简单的例子，它支持模数 𝑀 <230M<230![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位带符号整数的加法、减法、乘法以及快速幂运算：

一个简单的模整数类

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 ``` |  ```text // A simple ModInt implementation. template < int M > struct ModInt { struct skip_mod {}; ModInt ( int v , skip_mod ) : v ( v ) {} int v ; ModInt () : v ( 0 ) {} // Initialization: find remainder. // Equivalent to: v = int((x % M + M) % M) ModInt ( long long x ) { x %= M ; if ( x < 0 ) x += M ; v = int ( x ); } // Addition. // Equivalent to: ModInt((l.v + r.v) % M) friend ModInt operator \+ ( ModInt l , ModInt r ) { int res = l . v \+ r . v ; if ( res >= M ) res -= M ; return ModInt ( res , skip_mod {}); } // Subtraction. // Equivalent to: ModInt((l.v - r.v + M) % M) friend ModInt operator \- ( ModInt l , ModInt r ) { int res = l . v \- r . v ; if ( res < 0 ) res += M ; return ModInt ( res , skip_mod {}); } // Multiplication. friend ModInt operator * ( ModInt l , ModInt r ) { return ModInt ( 1L L * l . v * r . v % M , skip_mod {}); } // Exponentiation. ModInt pow ( long long b ) const { ModInt res { 1 }, po { * this }; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * po ; po = po * po ; } return res ; } }; ```   
---|---  
  
这个实现有意地减少了取模运算的次数，因为取模操作通常比普通的加、减、乘或比较运算要耗时得多．代码注释中提供了等价且更为直接的实现方式．这些简单优化的主要思路是，两个 [0,𝑀)[0,M)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的整数做加减运算时，结果一定落在区间 ( −𝑀,2𝑀)(−M,2M)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内，因此可以通过一次加减法调整回区间 [0,𝑀)[0,M)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．该实现中的取幂运算用到了 [快速幂](../../binary-exponentiation/#模意义下取幂) 的技巧．

除了这些基础运算外，还可以在各种模数下做如下运算：

  * [逆元](../inverse/)
  * [除法](../linear-equation/)
  * [阶乘](../factorial/)
  * [组合数](../lucas/)
  * [开平方](../quad-residue/#模意义下开平方)
  * [取对数](../discrete-logarithm/)
  * [开方](../residue/#模意义下开方)

这些运算通常在素数模数下比较容易．对于合数模数，往往需要用到对应算法的扩展版本和 [中国剩余定理](../crt/)．这些模意义下的运算大多可以看作求解某种同余方程．对于求解同余方程的一般方法，可以参考 [同余方程](../congruence-equation/) 页面．

## 相关算法

本节将介绍几种在模意义下优化取模、乘法和快速幂运算的方法．对于绝大多数题目来说，前文提供的简单实现已经足够高效．然而，当题目对算法常数有严格要求时，这些优化方法就可以发挥作用，通过减少不必要的计算和取模操作，进一步降低算法的时间开销．

### 快速乘

在素性测试与质因数分解中，经常会遇到模数在 `long long` 范围内的乘法取模运算．为了避免运算中的整型溢出问题，本节介绍一种可以处理模数在 `long long` 范围内，不需要使用 `__int128` 且复杂度为 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的「快速乘」．本算法要求测评系统中，`long double` 至少表示为 8080![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位扩展精度浮点数1．

假设 0 ≤𝑎,𝑏 <𝑚0≤a,b<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要计算 𝑎𝑏mod𝑚abmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意到：

𝑎𝑏mod𝑚=𝑎𝑏−⌊𝑎𝑏𝑚⌋𝑚.abmodm=ab−⌊abm⌋m.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用 `unsigned long long` 的自然溢出：

𝑎𝑏mod𝑚=𝑎𝑏−⌊𝑎𝑏𝑚⌋𝑚=(𝑎𝑏−⌊𝑎𝑏𝑚⌋𝑚)mod264.abmodm=ab−⌊abm⌋m=(ab−⌊abm⌋m)mod264.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

只要能算出商 ⌊𝑎𝑏𝑚⌋⌊abm⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最右侧表达式中的乘法和减法运算都可以使用 `unsigned long long` 直接计算．

接下来，只需要考虑如何计算 ⌊𝑎𝑏𝑚⌋⌊abm⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．解决方案是先使用 `long double` 算出 𝑎𝑚am![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再乘上 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．既然使用了 `long double`，就无疑会有精度误差．假设 `long double` 表示为 8080![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位扩展精度浮点数（即符号为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，指数为 1515![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，尾数为 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位），那么 `long double` 最多能精确表示的有效位数为 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)2．所以 𝑎𝑚am![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最差从第 6565![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位开始出错，误差范围3为 (−2−64,2−64)(−2−64,2−64)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．乘上 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这个 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位带符号整数，误差范围为 ( −0.5,0.5)(−0.5,0.5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．为了简化后续讨论，可以先加一个 0.50.5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再取整，最后的误差范围是 {0,1}{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后，代入上式计算时，需要乘以 −𝑚−m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以最后的误差范围是 {0, −𝑚}{0,−m}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 `long long` 范围内，所以当结果 𝑟 ∈[0,𝑚)r∈[0,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，直接返回 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则返回 𝑟 +𝑚r+m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

代码实现如下：

参考实现

```text 1 2 3 4 5 ``` |  ```text long long mul ( long long a , long long b , long long m ) { long long c = ( unsigned long long ) a * b \- ( unsigned long long )(( long double ) a / m * b \+ 0.5L ) * m ; return c < 0 ? c \+ m : c ; } ```   
---|---  
  
如今，绝大多数测评系统所配备的 C/C++ 编译器已支持 `__int128` 类型4，因此也可以直接将乘数类型提升至 `__int128` 后取模计算：

参考实现

```text 1 2 3 ``` |  ```text long long mul ( long long a , long long b , long long m ) { return ( __int128 ) a * b % m ; } ```   
---|---  
  
当然，`__int128` 的取模运算耗时并不少．如果需要进一步卡常，可以考虑接下来两节介绍的方法．

### Barrett 约减

前文提到，除法和取模运算通常比其他四则运算更为耗时．为了减少取模运算的开销，有一些算法可以在不直接做取模的情况下得到相同的结果．本节要介绍的 Barrett 约减算法就是其中之一．

设 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为固定模数，假设要对不同的 𝑎 >0a>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 多次计算 𝑎mod𝑚amodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由带余除法可知

𝑧=𝑎mod𝑚=𝑎−⌊𝑎𝑚⌋𝑚.z=amodm=a−⌊am⌋m.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

关键在于商数 ⌊𝑎𝑚⌋⌊am⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算．设 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是某个常数，就有5

⌊𝑎𝑚⌋=⌊𝑎𝑅𝑚/𝑅⌋≈⌊𝑎⌊𝑅𝑚⌋/𝑅⌋.⌊am⌋=⌊aRm/R⌋≈⌊a⌊Rm⌋/R⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果选取 𝑅 =2𝑘R=2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，右式中 ⌊𝑅𝑚⌋⌊Rm⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以预处理，除以 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的操作可以通过移位运算进行．所以，用右式计算商数，仅需要一次乘法和一次移位操作．再代入 𝑎mod𝑚amodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式，就得到所求余数的估计 𝑧′z′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

现在分析这样做的误差．[取整函数](../basic/#取整函数) 具有性质：对于 𝑥 >𝑦 >0x>y>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 ⌊𝑥⌋ −⌊𝑦⌋ ≤⌈𝑥 −𝑦⌉⌊x⌋−⌊y⌋≤⌈x−y⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，误差

Δ=|𝑧′−𝑧|=𝑚∣⌊𝑎𝑚⌋−⌊𝑎⌊𝑅𝑚⌋/𝑅⌋∣≤𝑚⌈𝑎(𝑅𝑚−⌊𝑅𝑚⌋)/𝑅⌉≤𝑚⌈𝑎𝑅⌉.Δ=|z′−z|=m|⌊am⌋−⌊a⌊Rm⌋/R⌋|≤m⌈a(Rm−⌊Rm⌋)/R⌉≤m⌈aR⌉.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

只要 𝑎 ≤𝑅a≤R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，误差 ΔΔ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就不超过 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于 𝑧′ ≥𝑧z′≥z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以估计值 𝑧′z′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只能是 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑧 +𝑚z+m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．只要在得到估计值后，在 𝑧′ ≥𝑚z′≥m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时再减去多余的 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以保证答案正确．

在 Barrett 约减的计算过程中，仅使用了两次乘法、一次移位操作和至多两次减法，就完成了整数取模．但效率的提升并非毫无成本，实际上，Barrett 约减涉及的中间变量长度往往长于输入变量长度．容易发现，Barrett 约减中涉及的最长中间变量为 𝑎⌊𝑅𝑚⌋a⌊Rm⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 ℓ(𝑥)ℓ(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为整数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制表示长度．那么，有

ℓ(𝑎⌊𝑅𝑚⌋)≈ℓ(𝑎)+ℓ(𝑅)−ℓ(𝑚).ℓ(a⌊Rm⌋)≈ℓ(a)+ℓ(R)−ℓ(m).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选取需要满足条件 𝑎 <𝑅a<R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这一长度至少为 2ℓ(𝑎) −ℓ(𝑚)2ℓ(a)−ℓ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，需要取模时，一般都有 ℓ(𝑚) ≤ℓ(𝑎)ℓ(m)≤ℓ(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此，这一中间变量的长度可能大于输入长度 ℓ(𝑎)ℓ(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．例如，如果需要将 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位整数对 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位整数取模，实际上中间变量需要 64 ×2 −32 =9664×2−32=96![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位整数．

Barrett 约减的一个应用场景就是计算乘积的余数 𝑎𝑏mod𝑚abmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果其中一个乘数固定，比如 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 固定时，可以通过

𝑎𝑏mod𝑚=𝑎𝑏−⌊𝑎⌊𝑏𝑅𝑚⌋/𝑅⌋𝑚abmodm=ab−⌊a⌊bRm⌋/R⌋m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进行与上文类似的估计，只要预处理出 ⌊𝑏𝑅𝑚⌋⌊bRm⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值即可．这种 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 固定的情形有时也称为 Shoup 模乘6．

更为常见的情形是 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都不固定．此时，需要首先计算 𝑎𝑏ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，再利用 Barrett 约减得到 𝑎𝑏mod𝑚abmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．例如，实现模意义下乘法时，需要对 0 ≤𝑎,𝑏 <𝑚0≤a,b<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算 𝑎𝑏mod𝑚abmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时，选取的 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要满足 𝑎𝑏 <𝑅ab<R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据前文分析，计算过程涉及的最长中间变量长度为 2ℓ(𝑎𝑏) −ℓ(𝑚)2ℓ(ab)−ℓ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．当 ℓ(𝑎) ≈ℓ(𝑏) ≈ℓ(𝑚)ℓ(a)≈ℓ(b)≈ℓ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，该长度为 3ℓ(𝑚)3ℓ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，如果要用 Barrett 约减实现 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位整数的模乘，中间变量需要 9696![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位整数．这也是 Barrett 约减在算法竞赛中实际应用时的一个限制．

作为示例，利用 Barrett 约减实现 32 位有符号整数模乘的参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text // Modular multiplication of int32_t using Barrett reduction. class Barrett { int32_t m ; uint64_t r ; public : Barrett ( int32_t m ) : m ( m ), r (( uint64_t )( \- m ) / m \+ 1 ) {} // Barrett reduction: a % m. int32_t reduce ( int64_t a ) const { int64_t q = ( __int128 ) a * r >> 64 ; a -= q * m ; return a >= m ? a \- m : a ; } // Modular multiplication: (a * b) % m; // Assume that 0 <= a, b < m. int32_t mul ( int32_t a , int32_t b ) const { return reduce (( int64_t ) a * b ); } }; ```   
---|---  
  
实现中需要用到 128 位整数4．

### Montgomery 模乘

Montgomery 模乘算法的功能和 Barrett 算法十分类似，它同样可以减少模整数运算过程中取模运算的开销．与前两个算法都是在近似计算商数不同，Montgomery 模乘将所有整数都映射到 Montgomery 空间上，而 Montgomery 空间中的运算相对容易，进而降低了整体计算成本．

设模数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为奇数，并选取 𝑅 =2𝑘 >𝑚R=2k>m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，同余类 𝑎mod𝑚amodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的 Montgomery 形式就是

𝑎𝑅mod𝑚.aRmodm.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝑅 ⟂𝑚R⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以同余类 𝑎mod𝑚amodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与它的 Montgomery 形式 𝑎𝑅mod𝑚aRmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间存在双射．因此，可以将整数转换为 Montgomery 形式后，进行若干模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的运算，再将得到的 Montgomery 形式转换回整数，结果总是正确的．

利用 Montgomery 形式可以方便地进行很多模整数的运算．刚刚已经说明，比较两个同余类是否相同，只要比较它们的 Montgomery 形式．又因为

(𝑎+𝑏)𝑅mod𝑚=((𝑎𝑅mod𝑚)±(𝑏𝑅mod𝑚))mod𝑚,(a+b)Rmodm=((aRmodm)±(bRmodm))modm,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以同余类的加法、减法就对应它们的 Montgomery 形式的加法、减法．但是，要计算同余类的乘法，并不能直接将两个 Montgomery 形式相乘．因为

(𝑎𝑏)𝑅mod𝑚=((𝑎𝑅mod𝑚)(𝑏𝑅mod𝑚)𝑅−1)mod𝑚,(ab)Rmodm=((aRmodm)(bRmodm)R−1)modm,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，计算两个 Montgomery 形式的乘法时，需要对它们的乘积 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作如下 **Montgomery 约减** （Montgomery reduction）操作：

REDC:𝑥↦𝑥𝑅−1mod𝑚.REDC:x↦xR−1modm.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用这一操作，乘积 𝑎𝑏ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Montgomery 形式就是 REDC⁡((𝑎𝑅mod𝑚)(𝑏𝑅mod𝑚))REDC⁡((aRmodm)(bRmodm))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．Montgomery 约减操作是 Montgomery 模乘的核心操作：

  * 将 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转换为它的 Montgomery 形式就是 REDC⁡((𝑎mod𝑚)(𝑅2mod𝑚))REDC⁡((amodm)(R2modm))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 将 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Montgomery 形式转换回 𝑎mod𝑚amodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 REDC⁡(𝑎𝑅mod𝑚)REDC⁡(aRmodm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 模逆元 𝑎−1mod𝑚a−1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的 Montgomery 形式就是 REDC⁡((𝑎𝑅mod𝑚)−1(𝑅3mod𝑚))REDC⁡((aRmodm)−1(R3modm))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

现在讨论 Montgomery 约减操作 REDCREDC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的实现方法．在计算 REDC⁡(𝑥)REDC⁡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，总是假定 0 ≤𝑥 <𝑚20≤x<m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这对于以上情形都是成立的．因为 𝑅 ⟂𝑚R⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以由 [裴蜀定理](../bezouts/)，存在整数 𝑅−1,𝑚′R−1,m′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝑅𝑅−1+𝑚𝑚′=1.RR−1+mm′=1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，设 𝑞 =⌊𝑥𝑚′/𝑅⌋q=⌊xm′/R⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有

𝑥𝑅−1=𝑥1−𝑚𝑚′𝑅≡𝑥−𝑥𝑚𝑚′+𝑞𝑚𝑅𝑅=𝑥−𝑚(𝑥𝑚′mod𝑅)𝑅(mod𝑚).xR−1=x1−mm′R≡x−xmm′+qmRR=x−m(xm′modR)R(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 0 ≤𝑥 <𝑚2 <𝑚𝑅0≤x<m2<mR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 0 ≤𝑥𝑚′mod𝑅 <𝑅0≤xm′modR<R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以

−𝑚<𝑥−𝑚(𝑥𝑚′mod𝑅)𝑅<𝑚.−m<x−m(xm′modR)R<m.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，这个商和 𝑥𝑅−1mod𝑚xR−1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间至多差一个 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．只要在商小于零时，再加上 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以得到 REDC⁡(𝑥)REDC⁡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．计算这个商，只需要两次整数乘法、一次整数减法和两次位操作（分别是对 𝑅 =2𝑘R=2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模和做除法）．因此，Montgomery 约减操作可以高效进行．

为了进行 Montgomery 模乘操作，需要预处理出一系列常数．首先，Montgomery 约减中会用到 𝑚′ =𝑚−1mod𝑅m′=m−1modR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以通过 下文 介绍的 Newton–Hensel 方法计算．其次，将不同操作归约为 Montgomery 约减操作时，还涉及诸如 𝑅2mod𝑚R2modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这样的常数．为了得到它，需要计算一次 𝑅mod𝑚Rmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将它与自身相加就得到 2𝑅mod𝑚2Rmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．随后，将它看作 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Montgomery 形式，直接计算快速幂，就可以得到 2𝑘𝑅mod𝑚 =𝑅2mod𝑚2kRmodm=R2modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

作为示例，3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位有符号整数的 Montgomery 模乘实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` |  ```text // Montgomery modular multiplication. // The modulus m must be odd. The constant r is 2^32. class Montgomery { int32_t m ; uint32_t mm , r2 ; public : Montgomery ( int32_t m ) : m ( m ), mm ( 1 ), r2 ( \- m ) { // Compute mm as inv(m) mod r. for ( int i = 0 ; i < 5 ; ++ i ) { mm *= 2 \- mm * m ; } // Compute r2 as r * r mod m. // If allowed to use modular operation for uint64_t, simply use: // r2 = (uint64_t)(-m) % m; r2 %= m ; r2 <<= 1 ; if ( r2 >= ( uint32_t ) m ) r2 -= m ; for ( int i = 0 ; i < 5 ; ++ i ) { r2 = mul ( r2 , r2 ); } } // Montgomery reduction: x * inv(r) % m. // Also used to transform x from Montgomery space to the normal space. int32_t reduce ( int64_t x ) { uint32_t u = ( uint32_t ) x * mm ; int32_t ans = ( x \- ( int64_t ) m * u ) >> 32 ; return ans < 0 ? ans \+ m : ans ; } // Multiplication in Montgomery space: x * y * inv(r) % m. int32_t mul ( int32_t x , int32_t y ) { return reduce (( int64_t ) x * y ); } // Transform x from the normal space to Montgomery space. int32_t init ( int32_t x ) { return mul ( x , r2 ); } }; ```   
---|---  
  
相对于 Barrett 约减实现模意义下乘法，Montgomery 模乘的计算涉及转换、Montgomery 形式的乘法、逆转换等多个步骤．因此，只有在转换和逆转换之间的模运算次数足够多时，转换和逆转换的成本才可以摊平，进而获得较高的整体效率．但是，由于 Montgomery 模乘的实现过程中只涉及长度为 2ℓ(𝑚)2ℓ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的中间变量，所以实现起来更为灵活．例如，3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位整数的模乘仅需要 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位整数的中间变量．所以，如果需要实现一个模整数类用于各种数论计算，Montgomery 模乘更为合适．

### 模 2 的幂次的整数类

本节讨论模数是 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次时，模整数类的实现．在这一特殊情形中，除法和取模运算可以通过位操作实现，计算效率很高．Barrett 约减和 Montgomery 模乘都是利用了 2𝑒2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为除数和模数时的这一特性来加速运算．特别地，当模数恰为 232232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 264264![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等特殊数字时，可以利用相应位长的无符号整数结合自然溢出实现模整数类，无需任何显式的取模运算．即使模数并非恰好如此，也可以转化为这些特殊模数的情形．例如模数为 258258![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，可以在模数 264264![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下完成中间计算，最后再将结果对 258258![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模．除了取模方便外，模 2𝑒2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整数类的其他操作也有很多特殊实现．本节重点介绍逆元和取幂操作的实现方式．

首先是取逆操作：给定奇数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和模数 𝑚 =2𝑒 (𝑒 >2)m=2e (e>2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，需要求出 𝑎−1mod𝑚a−1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．求逆元的常见方法包括扩展欧几里得算法和快速幂法．扩展欧几里得算法的过程涉及对一般模数取模；普通的快速幂法需要计算 𝑎𝜑(𝑚)−1mod𝑚aφ(m)−1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这需要 Θ(𝑒)Θ(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次整数乘法．更为高效的方法是 [Newton–Hensel 方法](../../poly/newton/)．具体地，考虑应用如下结论：7

𝑚𝑥≡1(mod2𝑒)⟹𝑚𝑥(2−𝑚𝑥)≡1(mod22𝑒).mx≡1(mod2e)⟹mx(2−mx)≡1(mod22e).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据这一表达式，只要从 𝑥 =1x=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始，反复应用 𝑥 ←𝑥(2 −𝑚𝑥)x←x(2−mx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以在 ⌈log2⁡𝑒⌉⌈log2⁡e⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次迭代后得到 𝑚−1mod𝑅m−1modR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

作为示例，模 232232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整数取逆操作参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 ``` |  ```text // Compute 1/v mod 2^32 for odd v. uint32_t inv_mod_2_32 ( uint32_t v ) { uint32_t x = 1 ; for ( int i = 0 ; i != 5 ; ++ i ) { x *= 2 \- v * x ; } return x ; } ```   
---|---  
  
接下来，讨论取幂操作：给定 𝑥,𝑎,𝑏x,a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和模数 𝑚 =2𝑒 (𝑒 >2)m=2e (e>2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，需要求出 𝑥𝑎𝑏mod𝑚xabmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇数．根据对模 2𝑒2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整数乘法结构的 [分析](../primitive-root/#mod-pow-2) 可知，𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是可以写成 ±𝑔ℓ±gℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式8，且负号出现且仅出现在 𝑎 ≡3(mod4)a≡3(mod4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．对于这种情况，可以将 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替换成 −𝑎−a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将最终结果再乘上 ( −1)𝑏(−1)b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，接下来不妨假设 𝑎 ≡1(mod4)a≡1(mod4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．此时，算法的核心想法是，将 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 写成 𝑔𝐿(𝑎)mod𝑚gL(a)modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，然后用 𝑥𝑔𝑏𝐿(𝑎)mod𝑚xgbL(a)modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算所求的幂．

计算 𝐿(𝑎)L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是计算离散对数 ind𝑔⁡𝑎indg⁡a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意到，只要 𝑎 ≡1(mod4)a≡1(mod4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总能写成如下形式：

𝑎≡(2𝑒1+1)(2𝑒2+1)⋯(2𝑒𝑠+1)(mod𝑚),a≡(2e1+1)(2e2+1)⋯(2es+1)(modm),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，1 <𝑒1 <𝑒2 <⋯ <𝑒𝑠 <𝑒1<e1<e2<⋯<es<e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这是因为直接将这一乘积展开可以发现，𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制表示中等于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的次低位就是第 𝑒1e1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位（下标从 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始），由此就可以递归地找到这一表示．根据离散对数的 [性质](../discrete-logarithm/#性质) 可知，有

4𝐿(𝑎)≡4𝐿(2𝑒1+1)+4𝐿(2𝑒2+1)+⋯+4𝐿(2𝑒𝑠+1)(mod𝑚).4L(a)≡4L(2e1+1)+4L(2e2+1)+⋯+4L(2es+1)(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于离散对数的模数等于阶 𝛿𝑚(𝑔) =2𝑒−2 =𝑚/4δm(g)=2e−2=m/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以此处直接将整个同余式都乘以 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以保证计算可以在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 剩余类中进行．由此，只需要对 1 <𝑑 <𝑒1<d<e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 预处理出所有的 4𝐿(2𝑑 +1)4L(2d+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以快速计算 4𝐿(𝑎)4L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

反过来，从 𝐿(𝑎)L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也很容易得到 𝑔𝑎mod𝑚gamodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．根据 [二项式定理](../../combinatorics/combination/#二项式定理) 可知，对于 1 <𝑑 <𝑒1<d<e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

(2𝑑+1)2𝑒−𝑑≡1(mod𝑚),(2𝑑+1)2𝑒−𝑑−1≡1+2𝑒−1(mod𝑚),(2d+1)2e−d≡1(modm),(2d+1)2e−d−1≡1+2e−1(modm),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，𝛿𝑚(2𝑑 +1) =2𝑒−𝑑δm(2d+1)=2e−d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据阶的性质可知

𝛿𝑚(2𝑑+1)=𝛿𝑚(𝑔)gcd(𝛿𝑚(𝑔),ind𝑔⁡(2𝑑+1)).δm(2d+1)=δm(g)gcd(δm(g),indg⁡(2d+1)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，gcd(𝛿𝑚(𝑔),ind𝑔⁡(2𝑑 +1)) =2𝑑−2gcd(δm(g),indg⁡(2d+1))=2d−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这说明 𝐿(2𝑑 +1) =ind𝑔⁡(2𝑑 +1) =2𝑑−2𝑟L(2d+1)=indg⁡(2d+1)=2d−2r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，2 ∤𝑟2∤r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，4𝐿(2𝑑 +1)4L(2d+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制表示中等于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最低位恰为第 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位（下标从 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始）．因此，同样可以通过二进制表示递归地将 4𝐿(𝑎)4L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解为形如 4𝐿(2𝑑 +1)4L(2d+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的和．由此，就可以得到 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

具体实现时，有一些可以进一步优化的点．首先，将 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解为乘积形式时，还是需要用到除法．更方便的是计算 𝑎−1a−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分解，即寻找 1 <𝑒1 <𝑒2 <⋯ <𝑒𝑠 <𝑒1<e1<e2<⋯<es<e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝑎(2𝑒1+1)(2𝑒2+1)⋯(2𝑒𝑠+1)≡1(mod𝑚)a(2e1+1)(2e2+1)⋯(2es+1)≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

成立．同样是通过寻找等于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的次低位来确定 𝑒1e1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是要在 𝑎−1a−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中消去 2𝑒1 +12e1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 因子，只需要在 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上乘以 2𝑒1 +12e1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可，这可以通过位操作进行．又因为 4𝐿(𝑎−1) = −4𝐿(𝑎)4L(a−1)=−4L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以统计 4𝐿(𝑎)4L(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，需要用减法代替加法．其次，对于特殊选择的基底 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，迭代无需进行到 𝑑 =𝑒 −1d=e−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而只要进行到 𝑑 =⌈𝑒/2⌉ −1d=⌈e/2⌉−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．为此，需要选择 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

4𝐿(2⌈𝑒/2⌉+1)=2⌈𝑒/2⌉.4L(2⌈e/2⌉+1)=2⌈e/2⌉.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于 𝑑 ≥𝑒/2d≥e/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

(2𝑑+1)2=22𝑑+2𝑑+1+1≡2𝑑+1+1(mod𝑚).(2d+1)2=22d+2d+1+1≡2d+1+1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，从 𝑑 =⌈𝑒/2⌉d=⌈e/2⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始归纳可知，𝐿(2𝑑 +1) =2𝑑L(2d+1)=2d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑑 ≥𝑒/2d≥e/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．进而，只要 𝑒/2 ≤𝑒1 <𝑒2 <⋯ <𝑒𝑠 <𝑒e/2≤e1<e2<⋯<es<e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有

(2𝑒1+1)(2𝑒2+1)⋯(2𝑒𝑠+1)≡1+2𝑒1+2𝑒2+⋯+2𝑒𝑠(mod𝑚)(2e1+1)(2e2+1)⋯(2es+1)≡1+2e1+2e2+⋯+2es(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

以及

4𝐿((2𝑒1+1)(2𝑒2+1)⋯(2𝑒𝑠+1))=2𝑒1+2𝑒2+⋯+2𝑒𝑠.4L((2e1+1)(2e2+1)⋯(2es+1))=2e1+2e2+⋯+2es.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，处理完所有 𝑑 <𝑒/2d<e/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制位后，可以直接得到剩余部分的离散对数，而无需逐位计算．应用第一个优化后，整个取幂操作只需要 𝑂(𝑒)O(e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次加减法和位操作和 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次乘法操作；应用第二个优化后，可以省去约一半的加减法和位操作，但需要额外 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次乘法操作．

作为示例，模 232232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整数取幂操作参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 ``` |  ```text // Store 4L(a) for a = 2^d + 1, where L(a) is disc. log. base 388251981. // The first two values are never used and thus set to zero. // The base is chosen such that 4L(2^16+1) = 2^16. constexpr uint32_t log_table [ 16 ] = { 0x00000000 , 0x00000000 , 0xbba0267c , 0x49b9d1e8 , 0xf0026f90 , 0xd6e17e20 , 0xe78bf840 , 0x039fe080 , 0xaf7f8100 , 0x60fe0200 , 0xd1f80400 , 0x23e00800 , 0x47801000 , 0x8e002000 , 0x18004000 , 0x20008000 , }; // Compute 4L(v). uint32_t log_mod_2_32 ( uint32_t x , uint32_t v ) { for ( int i = 2 ; i != 16 ; ++ i ) { if (( v >> i ) & 1 ) { v += v << i ; x -= log_table [ i ]; } } x += v ^ 1 ; return x ; } // Compute x*a for 4L(a) = v. uint32_t exp_mod_2_32 ( uint32_t x , uint32_t v ) { for ( int i = 2 ; i != 16 ; ++ i ) { if (( v >> i ) & 1 ) { x += x << i ; v -= log_table [ i ]; } } x *= v ^ 1 ; return x ; } // Compute x*a^b for odd a. uint32_t pow_odd_mod_2_32 ( uint32_t a , uint32_t b , uint32_t x ) { if ( a & 2 ) { a = \- a ; if ( b & 1 ) { x = \- x ; } } return exp_mod_2_32 ( x , log_mod_2_32 ( 0 , a ) * b ); } // Compute x*a^b mod 2^32. uint32_t pow_mod_2_32 ( uint32_t a , uint32_t b , uint32_t x = 1 ) { if ( ! a ) return b == 0 ? x : 0 ; auto d = __builtin_ctz ( a ); if (( uint64_t ) d * b >= 32 ) return 0 ; return pow_odd_mod_2_32 ( a >> d , b , x ) << ( d * b ); } ```   
---|---  
  
离散对数的预处理可以通过 Pohlig–Hellman 算法进行，基底 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以选择为

5ind5⁡(2⌈𝑒/2⌉)/2⌈𝑒/2⌉−2mod2𝑒.5ind5⁡(2⌈e/2⌉)/2⌈e/2⌉−2mod2e.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 参考资料与注释

  * [Fast modular multiplication by orz - Codeforces](https://codeforces.com/blog/entry/96759)
  * [Barrett Reduction - Wikipedia](https://en.wikipedia.org/wiki/Barrett_reduction)
  * [Barrett Reduction - A41](https://encrypt.a41.io/primitives/modular-arithmetic/modular-reduction/barrett-reduction#cost-analysis-of-modular-multiplication)
  * [Barrett 约减原理及正确性证明 by Chen - 知乎专栏](https://zhuanlan.zhihu.com/p/690876166)
  * [Montgomery Multiplication - CP Algorithms](https://cp-algorithms.com/algebra/montgomery_multiplication.html)
  * [Montgomery 模乘 by Chen - 知乎专栏](https://zhuanlan.zhihu.com/p/645428404)
  * [Binary Exponentiation by Factoring - CP Algorithms](https://cp-algorithms.com/algebra/factoring-exp.html)
  * Barrett, Paul. "Implementing the Rivest Shamir and Adleman public key encryption algorithm on a standard digital signal processor." In Conference on the Theory and Application of Cryptographic Techniques, pp. 311-323. Berlin, Heidelberg: Springer Berlin Heidelberg, 1986.
  * Becker, Hanno, Vincent Hwang, Matthias J. Kannwischer, Bo-Yin Yang, and Shang-Yi Yang. "Neon NTT: Faster Dilithium, Kyber, and Saber on Cortex-A72 and Apple M1." IACR Transactions on Cryptographic Hardware and Embedded Systems (2022): 221-244.
  * Montgomery, Peter L. "Modular multiplication without trial division." Mathematics of computation 44, no. 170 (1985): 519-521.

* * *

  1. 这适用于大多数 64 位系统上的 GCC 或 Clang 编译器． ↩

  2. 参见 [Double-precision floating-point format - Wikipedia](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)． ↩

  3. 此处用到了条件 𝑎 <𝑚a<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑎/𝑚 ∈[0,1)a/m∈[0,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． ↩

  4. 在目前的主流编译环境中，只有 Windows 平台上的 MSVC 不支持 `__int128` 类型．若需要编写可在多平台上兼容的代码，可以通过宏 `_MSC_VER` 检测 MSVC 编译环境，并在该条件下包含 [`<intrin.h>`](https://learn.microsoft.com/en-us/cpp/intrinsics/x64-amd64-intrinsics-list?view=msvc-170) 头文件，利用其提供的内建函数（如 `_umul128` 等）来间接实现 128 位整数运算（仅在 64 位平台上可用）． ↩↩

  5. 此处 ⌊𝑟𝑚⌋⌊rm⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也可以替换成 𝑟𝑚rm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的其他整数估计，例如上取整函数 ⌈𝑟𝑚⌉⌈rm⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和四舍五入取整函数 ⌊𝑟𝑚⌉⌊rm⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等，只要相应地调整对估计值的误差修正步骤． ↩

  6. Shoup 在他的数论计算库 [NTL](https://libntl.org/) 中实现了 Barrett 约减的这一扩展，因此得名． ↩

  7. 直接验证：由 𝑚𝑥 ≡1(mod2𝑒)mx≡1(mod2e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以设 𝑚𝑥 =1 +𝜆2𝑒mx=1+λ2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么就有 𝑚𝑥(2 −𝑚𝑥) =(1 +𝜆2𝑒)(1 −𝜆2𝑒) =1 −𝜆222𝑒 ≡1(mod22𝑒)mx(2−mx)=(1+λ2e)(1−λ2e)=1−λ222e≡1(mod22e)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． ↩

  8. 文中所引页面仅证明了 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以取 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．实际上，完全重复该证明，可以说明 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以取任何模 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 余 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数．后文会讨论 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选取方法． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/mod-arithmetic.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/mod-arithmetic.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest), [HeRaNO](https://github.com/HeRaNO), [Tiphereth-A](https://github.com/Tiphereth-A), [383494](https://github.com/383494), [buuzzing](https://github.com/buuzzing), [cr4c1an](https://github.com/cr4c1an), [Emp7iness](https://github.com/Emp7iness), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [jifbt](https://github.com/jifbt), [Kaiser-Yang](https://github.com/Kaiser-Yang), [Koishilll](https://github.com/Koishilll), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [Qiu-Quanzhi](https://github.com/Qiu-Quanzhi), [Saisyc](https://github.com/Saisyc), [sshwy](https://github.com/sshwy), [StarryReverie](https://github.com/StarryReverie), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid), [xyf007](https://github.com/xyf007)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
