# 同余方程 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/congruence-equation/

# 同余方程

## 定义

同余方程

对正整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一元整系数多项式 𝑓(𝑥) =∑𝑛𝑖=0𝑎𝑖𝑥𝑖f(x)=∑i=0naixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中未知数 𝑥 ∈𝐙𝑚x∈Zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称形如

𝑓(𝑥)≡0(mod𝑚)(1)(1)f(x)≡0(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的方程为关于未知数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一元 **同余方程** （Congruence Equation）．

若 𝑎𝑛 ≢0(mod𝑚)an≢0(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称上式为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次同余方程．

类似可定义同余方程组．

关于一次同余方程与方程组的相关内容请参见 [线性同余方程](../linear-equation/) 与 [中国剩余定理](../crt/)．

本文首先研究同余方程的可解性和解集结构，之后会简要介绍高次同余方程的解法．

由 [中国剩余定理](../crt/) 可知，求解关于模合数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的同余方程可转化为求解模素数幂次的情况．故以下只介绍素数幂模同余方程和素数模同余方程的相关理论．

## 素数幂模同余方程

以下假设模数 𝑚 =𝑝𝑒 (𝑝 ∈𝐏, 𝑒 ∈𝐙>1)m=pe (p∈P, e∈Z>1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意到，若 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是方程

𝑓(𝑥)≡0(mod𝑝𝑒)f(x)≡0(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的解，则 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是方程

𝑓(𝑥)≡0(mod𝑝𝑒−1)f(x)≡0(modpe−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的解．这启发我们尝试通过较低的模幂次的解去构造较高的模幂次的解．我们有如下定理：

定理 1（Hensel 引理）

对素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和整数 𝑒 >1e>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，取整系数多项式 𝑓(𝑥) =∑𝑛𝑖=0𝑎𝑖𝑥𝑖 (𝑝𝑒 ∤𝑎𝑛)f(x)=∑i=0naixi (pe∤an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝑓′(𝑥) =∑𝑛𝑖=1𝑖𝑎𝑖𝑥𝑖−1f′(x)=∑i=1niaixi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为其导数．令 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为方程

𝑓(𝑥)≡0(mod𝑝𝑒−1)(2)(2)f(x)≡0(modpe−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的解，则：

  1. 若 𝑓′(𝑥0) ≢0(mod𝑝)f′(x0)≢0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则存在整数 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝑥=𝑥0+𝑝𝑒−1𝑡(3)(3)x=x0+pe−1t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

是方程

𝑓(𝑥)≡0(mod𝑝𝑒)(4)(4)f(x)≡0(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的解．

  2. 若 𝑓′(𝑥0) ≡0(mod𝑝)f′(x0)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓(𝑥0) ≡0(mod𝑝𝑒)f(x0)≡0(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对 𝑡 =0,1,…,𝑝 −1t=0,1,…,p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由式 (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 确定的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为方程 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解．

  3. 若 𝑓′(𝑥0) ≡0(mod𝑝)f′(x0)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓(𝑥0) ≢0(mod𝑝𝑒)f(x0)≢0(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则不能由式 (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构造方程 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解．

证明

我们假设式 (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是方程 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解，即

𝑓(𝑥0+𝑝𝑒−1𝑡)≡0(mod𝑝𝑒)f(x0+pe−1t)≡0(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

整理后可得

𝑓(𝑥0)+𝑝𝑒−1𝑡𝑓′(𝑥0)≡0(mod𝑝𝑒)f(x0)+pe−1tf′(x0)≡0(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是

𝑡𝑓′(𝑥0)≡−𝑓(𝑥0)𝑝𝑒−1(mod𝑝)(5)(5)tf′(x0)≡−f(x0)pe−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  1. 若 𝑓′(𝑥0) ≢0(mod𝑝)f′(x0)≢0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则关于 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方程 (5)(5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有唯一解 𝑡0t0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，代入式 (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可验证其为方程 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解．
  2. 若 𝑓′(𝑥0) ≡0(mod𝑝)f′(x0)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓(𝑥0) ≡0(mod𝑝𝑒)f(x0)≡0(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则任意 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均能使方程 (5)(5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立，代入式 (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可验证其均为方程 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解．
  3. 若 𝑓′(𝑥0) ≡0(mod𝑝)f′(x0)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓(𝑥0) ≢0(mod𝑝𝑒)f(x0)≢0(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则方程 (5)(5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无解，从而不能由式 (3)(3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构造方程 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解．

进而我们有推论：

推论 1

对 定理 1 的 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，

  1. 若 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是方程 𝑓(𝑥) ≡0(mod𝑝)f(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解，且 𝑓′(𝑠) ≢0(mod𝑝)f′(s)≢0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则存在 𝑥𝑠 ∈𝐙𝑝𝑒xs∈Zpe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥𝑠 ≡𝑠(mod𝑝)xs≡s(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑥𝑠xs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是方程 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解．
  2. 若方程 𝑓(𝑥) ≡0(mod𝑝)f(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑓′(𝑥) ≡0(mod𝑝)f′(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无公共解，则方程 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和方程 𝑓(𝑥) ≡0(mod𝑝)f(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解数相同．

从而我们可以将素数幂模同余方程化归到素数模同余方程的情况．

## 素数模同余方程

以下令 𝑝 ∈𝐏p∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，整系数多项式 𝑓(𝑥) =∑𝑛𝑖=0𝑎𝑖𝑥𝑖f(x)=∑i=0naixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝 ∤𝑎𝑛p∤an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥 ∈𝐙𝑝x∈Zp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

定理 2

若方程

𝑓(𝑥)≡0(mod𝑝)(6)(6)f(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同的解 𝑥1,𝑥2,…,𝑥𝑘 (𝑘 ≤𝑛)x1,x2,…,xk (k≤n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则

𝑓(𝑥)≡𝑔(𝑥)𝑘∏𝑖=1(𝑥−𝑥𝑖)(mod𝑝),f(x)≡g(x)∏i=1k(x−xi)(modp),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 deg⁡𝑔 =𝑛 −𝑘deg⁡g=n−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 [𝑥𝑛−𝑘]𝑔(𝑥) =𝑎𝑛[xn−k]g(x)=an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

对 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应用数学归纳法．

  * 当 𝑘 =1k=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，做多项式带余除法，有 𝑓(𝑥) =(𝑥 −𝑥1)𝑔(𝑥) +𝑟f(x)=(x−x1)g(x)+r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑟 ∈𝐙r∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由 𝑓(𝑥1) ≡0(mod𝑝)f(x1)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知 𝑟 ≡0(mod𝑝)r≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而 𝑓(𝑥) ≡(𝑥 −𝑥1)𝑔(𝑥)(mod𝑝)f(x)≡(x−x1)g(x)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 假设命题对 𝑘 −1k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(𝑘 >1k>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)) 时的情况成立，现在设 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同的解 𝑥1,𝑥2,…,𝑥𝑘x1,x2,…,xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑓(𝑥) ≡(𝑥 −𝑥1)ℎ(𝑥)(mod𝑝)f(x)≡(x−x1)h(x)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进而有

(∀𝑖=2,3,…,𝑘), 0≡𝑓(𝑥𝑖)≡(𝑥𝑖−𝑥1)ℎ(𝑥𝑖)(mod𝑝)(∀i=2,3,…,k), 0≡f(xi)≡(xi−x1)h(xi)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从而 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑘 −1k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同的解 𝑥2,𝑥3,…,𝑥𝑘x2,x3,…,xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由归纳假设有

ℎ(𝑥)≡𝑔(𝑥)𝑘∏𝑖=2(𝑥−𝑥𝑖)(mod𝑝)h(x)≡g(x)∏i=2k(x−xi)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 deg⁡𝑔 =𝑛 −𝑘deg⁡g=n−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 [𝑥𝑛−𝑘]𝑔(𝑥) =𝑎𝑛[xn−k]g(x)=an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此命题得证．

推论 2

对素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，

  * (∀𝑥 ∈𝐙), 𝑥𝑝−1 −1 ≡∏𝑝−1𝑖=1(𝑥 −𝑖)(mod𝑝)(∀x∈Z), xp−1−1≡∏i=1p−1(x−i)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * （[Wilson 定理](../factorial/#wilson-定理)）(𝑝 −1)! ≡ −1(mod𝑝)(p−1)!≡−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

定理 3（Lagrange 定理）

方程 (6)(6)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至多有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同解．

证明

假设 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同解 𝑥1,𝑥2,…,𝑥𝑛+1x1,x2,…,xn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则由 定理 2，对 𝑥1,𝑥2,…,𝑥𝑛x1,x2,…,xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

𝑓(𝑥)≡𝑎𝑛𝑛∏𝑖=1(𝑥−𝑥𝑖)(mod𝑝)f(x)≡an∏i=1n(x−xi)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 𝑥 =𝑥𝑛+1x=xn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则

0≡𝑓(𝑥𝑛+1)≡𝑎𝑛𝑛∏𝑖=1(𝑥𝑛+1−𝑥𝑖)(mod𝑝)0≡f(xn+1)≡an∏i=1n(xn+1−xi)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而右侧显然不是 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数，因此假设矛盾．

推论 3

若同余方程 ∑𝑛𝑖=0𝑏𝑖𝑥𝑖 ≡0(mod𝑝)∑i=0nbixi≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解数大于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则

(∀𝑖=0,1,…,𝑛), 𝑝∣𝑏𝑖.(∀i=0,1,…,n), p∣bi.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定理 4

方程 (6)(6)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 若解的个数不为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则必存在满足 deg⁡𝑟 <𝑝deg⁡r<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整系数多项式 𝑟(𝑥)r(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑓(𝑥) ≡0(mod𝑝)f(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟(𝑥) ≡0(mod𝑝)r(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解集相同．

证明

不妨设 𝑛 ≥𝑝n≥p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做多项式带余除法

𝑓(𝑥)=𝑔(𝑥)(𝑥𝑝−𝑥)+𝑟(𝑥)f(x)=g(x)(xp−x)+r(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 deg⁡𝑟 <𝑝deg⁡r<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由 [Fermat 小定理](../fermat/) 知对任意整数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑥𝑝 ≡𝑥(mod𝑝)xp≡x(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而

  * 若 𝑟(𝑥) ≡0(mod𝑝)r(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则由 推论 2 可知 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同的解．
  * 若 𝑟(𝑥) ≢0(mod𝑝)r(x)≢0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则由 𝑓(𝑥) ≡𝑟(𝑥)(mod𝑝)f(x)≡r(x)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟(𝑥)r(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解集相同．

我们可以通过这个定理对同余方程降次．

定理 5

设 𝑛 ≤𝑝n≤p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则方程

𝑥𝑛+𝑛−1∑𝑖=0𝑎𝑖𝑥𝑖≡0(mod𝑝)(7)(7)xn+∑i=0n−1aixi≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个解当且仅当存在整系数多项式 𝑞(𝑥)q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑟(𝑥) (deg⁡𝑟 <𝑛)r(x) (deg⁡r<n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝑥𝑝−𝑥=𝑓(𝑥)𝑞(𝑥)+𝑝𝑟(𝑥).(8)(8)xp−x=f(x)q(x)+pr(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

  * 必要性：由多项式除法知存在整系数多项式 𝑞(𝑥)q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑟1(𝑥) (deg⁡𝑟1 <𝑛)r1(x) (deg⁡r1<n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝑥𝑝−𝑥=𝑓(𝑥)𝑞(𝑥)+𝑟1(𝑥).xp−x=f(x)q(x)+r1(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若方程 (7)(7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个解，则 𝑟1 ≡0(mod𝑝)r1≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个相同的解，进而由 推论 3 可知存在整系数多项式 𝑟(𝑥)r(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑟1(𝑥) =𝑝𝑟(𝑥)r1(x)=pr(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而命题得证．

  * 充分性：若式 (8)(8)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立，则由 [Fermat 小定理](../fermat/) 可知，对任意整数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),

0≡𝑥𝑝−𝑥≡𝑓(𝑥)𝑞(𝑥)(mod𝑝).0≡xp−x≡f(x)q(x)(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即方程 𝑓(𝑥)𝑞(𝑥) ≡0(mod𝑝)f(x)q(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个解．

设方程 (7)(7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解数为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则由 Lagrange 定理 可知 𝑠 ≤𝑛s≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

又由于 deg⁡𝑞 =𝑝 −𝑛deg⁡q=p−n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则由 Lagrange 定理 可知 𝑞(𝑥) ≡0(mod𝑝)q(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解数不超过 𝑝 −𝑛p−n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而方程 𝑓(𝑥)𝑞(𝑥) ≡0(mod𝑝)f(x)q(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解集是 𝑓(𝑥) ≡0(mod𝑝)f(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 解集和 𝑞(𝑥) ≡0(mod𝑝)q(x)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 解集的并集，故 𝑠 +(𝑝 −𝑛) ≥𝑝s+(p−n)≥p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑠 ≥𝑛s≥n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此 𝑠 =𝑛s=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于非首一多项式，由于 𝐙𝑝Zp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是域，故可以将其化为首一多项式，从而适用该定理．

定理 6

设 𝑛 ∣𝑝 −1n∣p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑝 ∤𝑎p∤a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则方程

𝑥𝑛≡𝑎(mod𝑝)(9)(9)xn≡a(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

有解当且仅当

𝑎𝑝−1𝑛≡1(mod𝑝).ap−1n≡1(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而且，若 (9)(9)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有解，则解数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Note

方程 (9)(9)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 解集的具体结构可参见 [k 次剩余](../residue/)．

证明

  * 必要性：若方程 (9)(9)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有解 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则

𝑎𝑝−1𝑛≡(𝑥𝑛0)𝑝−1𝑛≡1(mod𝑝)ap−1n≡(x0n)p−1n≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 充分性：若 𝑎𝑝−1𝑛 ≡1(mod𝑝)ap−1n≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则

𝑥𝑝−𝑥=𝑥(𝑥𝑝−1−1)=𝑥((𝑥𝑛)𝑝−1𝑛−𝑎𝑝−1𝑛+𝑎𝑝−1𝑛−1)=(𝑥𝑛−𝑎)𝑃(𝑥)+𝑥(𝑎𝑝−1𝑛−1)xp−x=x(xp−1−1)=x((xn)p−1n−ap−1n+ap−1n−1)=(xn−a)P(x)+x(ap−1n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑃(𝑥)P(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是某个整系数多项式，因此由 定理 5 可知方程 (9)(9)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个解．

## 高次同余方程（组）的求解方法

首先我们可以借助 [中国剩余定理](../crt/) 将求解 **同余方程组** 转为求解 **同余方程** ，以及将求解模 **合数** 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的同余方程转化为求解模 **素数幂次** 的同余方程．之后我们借助 定理 1 将求解模 **素数幂次** 的同余方程转化为求解模 **素数** 的同余方程．

结合模素数同余方程的若干定理，我们只需考虑方程

𝑥𝑛+𝑛−1∑𝑖=0𝑎𝑖𝑥𝑖≡0(mod𝑝)xn+∑i=0n−1aixi≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的求法，其中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数，𝑛 <𝑝n<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们可以通过将 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代换为 𝑥 −𝑎𝑛−1𝑛x−an−1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来消去 𝑥𝑛−1xn−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项，从而我们只需考虑方程

𝑥𝑛+𝑛−2∑𝑖=0𝑎𝑖𝑥𝑖≡0(mod𝑝)(10)(10)xn+∑i=0n−2aixi≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的求法，其中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数，𝑛 <𝑝n<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 若 𝑛 =1n=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则求法参见 [线性同余方程](../linear-equation/)．
  * 若 𝑛 =2n=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则求法参见 [二次剩余](../quad-residue/)．
  * 若方程 (10)(10)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可化为

𝑥𝑛≡𝑎(mod𝑝),xn≡a(modp),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则求法参见 [k 次剩余](../residue/)．

## 参考资料

  1. [Congruence Equation -- from Wolfram MathWorld](https://mathworld.wolfram.com/CongruenceEquation.html)
  2. [Lagrange's theorem (number theory) - Wikipedia](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_%28number_theory%29)
  3. 潘承洞，潘承彪．初等数论．
  4. 冯克勤．初等数论及其应用．
  5. 闵嗣鹤，严士健．初等数论．

* * *

>  __本页面最近更新： 2025/10/17 00:19:19，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/congruence-equation.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/congruence-equation.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [aofall](https://github.com/aofall), [CCXXXI](https://github.com/CCXXXI), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Marcythm](https://github.com/Marcythm), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
