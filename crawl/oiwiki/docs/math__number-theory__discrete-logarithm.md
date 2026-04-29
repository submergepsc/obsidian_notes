# 离散对数 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/discrete-logarithm/

# 离散对数

## 定义

前置知识：[阶与原根](../primitive-root/)．

离散对数的定义方式和对数类似．取有原根的正整数模数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设其一个原根为 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 对满足 (𝑎,𝑚) =1(a,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们知道必存在唯一的整数 0 ≤𝑘 <𝜑(𝑚)0≤k<φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝑔𝑘≡𝑎(mod𝑚)gk≡a(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们称这个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为以 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为底，模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的离散对数，记作 𝑘 =ind𝑔⁡𝑎k=indg⁡a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在不引起混淆的情况下可记作 ind⁡𝑎ind⁡a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

显然 ind𝑔⁡1 =0indg⁡1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，ind𝑔⁡𝑔 =1indg⁡g=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

## 性质

离散对数的性质也和对数有诸多类似之处．

性质

设 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根，(𝑎,𝑚) =(𝑏,𝑚) =1(a,m)=(b,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则：

  1. ind𝑔⁡(𝑎𝑏) ≡ind𝑔⁡𝑎 +ind𝑔⁡𝑏(mod𝜑(𝑚))indg⁡(ab)≡indg⁡a+indg⁡b(modφ(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而 (∀𝑛 ∈𝐍), ind𝑔⁡𝑎𝑛 ≡𝑛ind𝑔⁡𝑎(mod𝜑(𝑚))(∀n∈N), indg⁡an≡nindg⁡a(modφ(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  2. 若 𝑔1g1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根，则 ind𝑔⁡𝑎 ≡ind𝑔1⁡𝑎 ⋅ind𝑔⁡𝑔1(mod𝜑(𝑚))indg⁡a≡indg1⁡a⋅indg⁡g1(modφ(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  3. 𝑎 ≡𝑏(mod𝑚) ⟺ ind𝑔⁡𝑎 =ind𝑔⁡𝑏a≡b(modm)⟺indg⁡a=indg⁡b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明

  1. 𝑔ind𝑔⁡(𝑎𝑏) ≡𝑎𝑏 ≡𝑔ind𝑔⁡𝑎𝑔ind𝑔⁡𝑏 ≡𝑔ind𝑔⁡𝑎+ind𝑔⁡𝑏(mod𝑚)gindg⁡(ab)≡ab≡gindg⁡agindg⁡b≡gindg⁡a+indg⁡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 令 𝑥 =ind𝑔1⁡𝑎x=indg1⁡a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑎 ≡𝑔𝑥1(mod𝑚)a≡g1x(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 又令 𝑦 =ind𝑔⁡𝑔1y=indg⁡g1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑔1 ≡𝑔𝑦(mod𝑚)g1≡gy(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

故 𝑎 ≡𝑔𝑥𝑦(mod𝑚)a≡gxy(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 ind𝑔⁡𝑎 ≡𝑥𝑦 ≡ind𝑔1⁡𝑎 ⋅ind𝑔⁡𝑔1(mod𝜑(𝑚))indg⁡a≡xy≡indg1⁡a⋅indg⁡g1(modφ(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  3. 注意到

ind𝑔⁡𝑎=ind𝑔⁡𝑏⟺ind𝑔⁡𝑎≡ind𝑔⁡𝑏(mod𝜑(𝑚))⟺𝑔ind𝑔⁡𝑎≡𝑔ind𝑔⁡𝑏(mod𝑚)⟺𝑎≡𝑏(mod𝑚)indg⁡a=indg⁡b⟺indg⁡a≡indg⁡b(modφ(m))⟺gindg⁡a≡gindg⁡b(modm)⟺a≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 大步小步算法

目前离散对数问题仍不存在多项式时间经典算法（离散对数问题的输入规模是输入数据的位数）．在密码学中，基于这一点人们设计了许多非对称加密算法，如 [Ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519)．

在算法竞赛中，BSGS（baby-step giant-step，大步小步算法）常用于求解离散对数问题．形式化地说，对 𝑎,𝑏,𝑚 ∈𝐙+a,b,m∈Z+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，该算法可以在 𝑂(√𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内求解

𝑎𝑥≡𝑏(mod𝑚)ax≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．方程的解 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 0 ≤𝑥 <𝑚0≤x<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).（注意 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不一定是素数）

### 算法描述

令 𝑥 =𝐴⌈√𝑚⌉ −𝐵x=A⌈m⌉−B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 0 ≤𝐴,𝐵 ≤⌈√𝑚⌉0≤A,B≤⌈m⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有 𝑎𝐴⌈√𝑚⌉−𝐵 ≡𝑏(mod𝑚)aA⌈m⌉−B≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，稍加变换，则有 𝑎𝐴⌈√𝑚⌉ ≡𝑏𝑎𝐵(mod𝑚)aA⌈m⌉≡baB(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

我们已知的是 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以我们可以先算出等式右边的 𝑏𝑎𝐵baB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有取值，枚举 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用 `hash`/`map` 存下来，然后逐一计算 𝑎𝐴⌈√𝑚⌉aA⌈m⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，枚举 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，寻找是否有与之相等的 𝑏𝑎𝐵baB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而我们可以得到所有的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥 =𝐴⌈√𝑚⌉ −𝐵x=A⌈m⌉−B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

注意到 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均小于 ⌈√𝑚⌉⌈m⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以时间复杂度为 Θ(√𝑚)Θ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用 `map` 则多一个 loglog![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

为什么要求 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质

注意到我们求出的是 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们需要保证从 𝑎𝐴⌈√𝑚⌉ ≡𝑏𝑎𝐵(mod𝑚)aA⌈m⌉≡baB(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以推回 𝑎𝐴⌈√𝑚⌉−𝐵 ≡𝑏(mod𝑚)aA⌈m⌉−B≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，后式是前式左右两边除以 𝑎𝐵aB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到，所以必须有 𝑎𝐵 ⟂𝑚aB⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

## 扩展 BSGS 算法

对 𝑎,𝑏,𝑚 ∈𝐙+a,b,m∈Z+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求解

𝑎𝑥≡𝑏(mod𝑚)ax≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑎,𝑚a,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不一定互质．

当 (𝑎,𝑚) =1(a,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在逆元，因此可以使用 BSGS 算法求解．于是我们想办法让他们变得互质．

具体地，设 𝑑1 =(𝑎,𝑚)d1=(a,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 如果 𝑑1 ∤𝑏d1∤b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则原方程无解．否则我们把方程同时除以 𝑑1d1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得到

𝑎𝑑1⋅𝑎𝑥−1≡𝑏𝑑1(mod𝑚𝑑1)ad1⋅ax−1≡bd1(modmd1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚𝑑1md1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍不互质就再除，设 𝑑2 =(𝑎,𝑚𝑑1)d2=(a,md1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 如果 𝑑2 ∤𝑏𝑑1d2∤bd1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则方程无解；否则同时除以 𝑑2d2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到

𝑎2𝑑1𝑑2⋅𝑎𝑥−2≡𝑏𝑑1𝑑2(mod𝑚𝑑1𝑑2)a2d1d2⋅ax−2≡bd1d2(modmd1d2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

同理，这样不停的判断下去，直到 𝑎 ⟂𝑚𝑑1𝑑2⋯𝑑𝑘a⟂md1d2⋯dk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

记 𝐷 =∏𝑘𝑖=1𝑑𝑖D=∏i=1kdi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是方程就变成了这样：

𝑎𝑘𝐷⋅𝑎𝑥−𝑘≡𝑏𝐷(mod𝑚𝐷)akD⋅ax−k≡bD(modmD)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于 𝑎 ⟂𝑚𝐷a⟂mD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是推出 𝑎𝑘𝐷 ⟂𝑚𝐷akD⟂mD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). 这样 𝑎𝑘𝐷akD![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就有逆元了，于是把它丢到方程右边，这就是一个普通的 BSGS 问题了，于是求解 𝑥 −𝑘x−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后再加上 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是原方程的解啦．

注意，不排除解小于等于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，所以在消因子之前做一下 Θ(𝑘)Θ(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚举，直接验证 𝑎𝑖 ≡𝑏(mod𝑚)ai≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样就能避免这种情况．

## 基于值域预处理的快速离散对数

前文的 BSGS 算法时间复杂度为单次 𝑂(√𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在询问量级较大的时候效率较低．若每次求解的模数是一个固定的质数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们就有一个基于值域预处理的快速算法．

我们已经知道 ind𝑔⁡(𝑎𝑏) ≡ind𝑔⁡𝑎 +ind𝑔⁡𝑏(mod𝑝 −1)indg⁡(ab)≡indg⁡a+indg⁡b(modp−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以我们可以只对所有质数通过 BSGS 算法计算离散对数，合数的离散对数则可通过该式转化为若干已知的质数离散对数值之和．此时复杂度仍然不优，我们考虑只预处理一部分的离散对数，具体来说，我们预处理 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝐿 =⌊√𝑝⌋ +1L=⌊p⌋+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的离散对数．注意此时的 BSGS 块长 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **不能取** 𝑂(√𝐿)O(L)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为 BSGS 预处理（插入哈希表）部分的复杂度是 𝑂(𝐵)O(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而查询一共需要 𝑂(𝜋(𝐿))O(π(L))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，则总时间复杂度为 𝑂(𝐵+𝜋(𝐿)𝑝𝐵)O(B+π(L)pB)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时取 𝐵 =𝑂(√𝜋(𝐿)𝑝)B=O(π(L)p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 才是最优．由 [素数定理](../prime/) 𝜋(𝑛) ∼𝑛log⁡𝑛π(n)∼nlog⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则总的预处理时间复杂度可以平衡为 𝑂(𝑝3/4log1/2⁡𝑝)O(p3/4log1/2⁡p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

接下来是如何求答案．假设当前要求的是 ind𝑔⁡𝑦indg⁡y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 𝑦 ≤𝐿y≤L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则直接返回，否则设 𝑝 =𝑣𝑦 +𝑟p=vy+r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑣 =⌊𝑝𝑦⌋ <𝐿v=⌊py⌋<L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑟 =𝑝mod𝑦r=pmody![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑦 =𝑝−𝑟𝑣y=p−rv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而

ind𝑔⁡𝑦≡ind𝑔⁡(𝑝−𝑟)−ind𝑔⁡𝑣≡ind𝑔⁡(−𝑟)−ind𝑔⁡𝑣≡ind𝑔⁡(𝑝−1)+ind𝑔⁡𝑟−ind𝑔⁡𝑣(mod𝑝−1).indg⁡y≡indg⁡(p−r)−indg⁡v≡indg⁡(−r)−indg⁡v≡indg⁡(p−1)+indg⁡r−indg⁡v(modp−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到 ind𝑔⁡(𝑝 −1) =(𝑝 −1)/2indg⁡(p−1)=(p−1)/2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此只需递归计算 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的离散对数即可．

我们还可以考虑 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的另一种表达方式，注意到 𝑝 =𝑣𝑦 +𝑟 =(𝑣 +1)𝑦 +𝑟 −𝑦p=vy+r=(v+1)y+r−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑦 =𝑝−𝑟+𝑦𝑣+1y=p−r+yv+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而

ind𝑔⁡𝑦≡ind𝑔⁡(𝑦−𝑟)−ind𝑔⁡(𝑣+1)(mod𝑝−1).indg⁡y≡indg⁡(y−r)−indg⁡(v+1)(modp−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们有 𝑣 +1 ≤𝐿v+1≤L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此只需要递归计算 𝑦 −𝑟y−r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的离散对数即可．

综合这两种计算方式，我们有 min{𝑟,𝑦 −𝑟} ≤𝑦2min{r,y−r}≤y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以递归计算较小的一方即可达到 𝑂(log⁡𝑝)O(log⁡p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的查询复杂度．

至此我们得到了一个时间复杂度为 𝑂(𝑝3/4log1/2⁡𝑝) −𝑂(log⁡𝑝)O(p3/4log1/2⁡p)−O(log⁡p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的算法．

[Luogu11175【模板】基于值域预处理的快速离散对数](https://www.luogu.com.cn/problem/P11175)

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 ``` |  ```text #include <cmath> #include <iostream> #include <unordered_map> using namespace std ; const int N = 1'000'000 ; // sqrt(P * sqrt(P) / ln(P)) unordered_map < int , int > M ; int Lg [ N ], p [ N ], t ; bool vis [ N ]; int P , g , B , sq , LP_1 , inv ; int fadd ( int x , int y , int P ) { x += y ; if ( x >= P ) x -= P ; return x ; } int fsub ( int x , int y , int P ) { x -= y ; if ( x < 0 ) x += P ; return x ; } int fmul ( int x , int y , int P ) { return 1l l * x * y % P ; } int qpow ( int x , int y ) { int ans = 1 ; while ( y ) { if ( y & 1 ) ans = fmul ( ans , x , P ); x = fmul ( x , x , P ); y >>= 1 ; } return ans ; } int calc ( int x ) { int s = x ; for ( int i = 0 ; i <= P / B ; ++ i ) { if ( M . find ( s ) != M . end ()) return i * B \+ M [ s ]; s = fmul ( s , inv , P ); } return -1 ; } void init () { int s = 1 ; for ( int i = 0 ; i < B ; ++ i ) { if ( M . find ( s ) != M . end ()) break ; M [ s ] = i , s = fmul ( s , g , P ); } inv = qpow ( qpow ( g , B ), P \- 2 ); for ( int i = 2 ; i <= sq ; ++ i ) { if ( ! vis [ i ]) { p [ ++ t ] = i ; Lg [ i ] = calc ( i ); } for ( int j = 1 ; j <= t && p [ j ] * i <= sq ; ++ j ) { vis [ p [ j ] * i ] = true ; Lg [ p [ j ] * i ] = fadd ( Lg [ p [ j ]], Lg [ i ], P \- 1 ); if ( i % p [ j ] == 0 ) break ; } } } int solve ( int y ) { if ( y <= sq ) return Lg [ y ]; int v = P / y , r = P % y ; if ( r < y \- r ) return fadd ( fsub ( solve ( r ), Lg [ v ], P \- 1 ), LP_1 , P \- 1 ); return fsub ( solve ( y \- r ), Lg [ v \+ 1 ], P \- 1 ); } int main () { ios :: sync_with_stdio ( false ); cin . tie ( nullptr ); cin >> P >> g ; sq = sqrt ( P ) \+ 1 ; B = sqrt ( 1l l * P * sqrt ( P ) / log ( P )); init (); LP_1 = ( P \- 1 ) / 2 ; // g ^ LP_1 = P - 1 (mod P) int T ; cin >> T ; while ( T \-- ) { int x ; cin >> x ; cout << solve ( x ) << '\n' ; } return 0 ; } ```   
---|---  
  
## 习题

  * [SPOJ MOD](https://www.spoj.com/problems/MOD/) 模板
  * [SDOI2013 随机数生成器](https://www.luogu.com.cn/problem/P3306)
  * [SGU261 Discrete Roots](https://codeforces.com/problemsets/acmsguru/problem/99999/261) 模板
  * [SDOI2011 计算器](https://loj.ac/problem/10214) 模板
  * [Luogu4195【模板】exBSGS/Spoj3105 Mod](https://www.luogu.com.cn/problem/P4195) 模板
  * [Codeforces - Lunar New Year and a Recursive Sequence](https://codeforces.com/contest/1106/problem/F)
  * [LOJ6542 离散对数](https://loj.ac/problem/6542) index calculus 方法，非模板

**本页面部分内容以及代码译自博文[Дискретное извлечение корня](http://e-maxx.ru/algo/discrete_root) 与其英文翻译版 [Discrete Root](https://cp-algorithms.com/algebra/discrete-root.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

## 参考资料

  1. [Discrete logarithm - Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm)
  2. 潘承洞，潘承彪．初等数论．
  3. 冯克勤．初等数论及其应用．

* * *

>  __本页面最近更新： 2026/4/27 16:47:43，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/discrete-logarithm.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/discrete-logarithm.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [sshwy](https://github.com/sshwy), [Steaunk](https://github.com/Steaunk), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [MegaOwIer](https://github.com/MegaOwIer), [countercurrent-time](https://github.com/countercurrent-time), [Henry-ZHR](https://github.com/Henry-ZHR), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [stevebraveman](https://github.com/stevebraveman), [Xeonacid](https://github.com/Xeonacid), [Alpha1022](https://github.com/Alpha1022), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [FFjet](https://github.com/FFjet), [GavinZhengOI](https://github.com/GavinZhengOI), [GekkaSaori](https://github.com/GekkaSaori), [Gesrua](https://github.com/Gesrua), [HeRaNO](https://github.com/HeRaNO), [hly1204](https://github.com/hly1204), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [isdanni](https://github.com/isdanni), [Kelatte](https://github.com/Kelatte), [kxccc](https://github.com/kxccc), [Lampese](https://github.com/Lampese), [LovelyBuggies](https://github.com/LovelyBuggies), [lychees](https://github.com/lychees), [Makkiy](https://github.com/Makkiy), [Marcythm](https://github.com/Marcythm), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [Peanut-Tang](https://github.com/Peanut-Tang), [PotassiumWings](https://github.com/PotassiumWings), [purple-vine](https://github.com/purple-vine), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Ssfz202601](https://github.com/Ssfz202601), [SukkaW](https://github.com/SukkaW), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [xyf007](https://github.com/xyf007), [YOYO-UIAT](https://github.com/YOYO-UIAT)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
