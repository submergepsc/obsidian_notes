# 阶乘取模 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/factorial/

# 阶乘取模

## 引入

本文讨论了某一模数下阶乘计算的相关结论，并提供一种时间复杂度线性相关于模数大小的计算方法，因而该方法主要适用于模数不太大（∼106∼106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的情形．除了本文介绍的方法外，根据场景不同，还可以应用 [多项式技术](../../poly/shift/#模素数意义下阶乘) 进行快速计算．

根据 [中国剩余定理](../crt/)，阶乘取模问题可以转化为模数为素数幂 𝑝𝛼pα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．在处理这类问题时，常常需要对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将阶乘 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的所有因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都提取出来，进而得到分解：

𝑛!=𝑝𝜈𝑝(𝑛!)(𝑛!)𝑝.n!=pνp(n!)(n!)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝜈𝑝(𝑛!)νp(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示阶乘 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素因数分解中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次，(𝑛!)𝑝(n!)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示在阶乘 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的结果中去除所有 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次得到的整数．本文将讨论 (𝑛!)𝑝(n!)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在素数（幂）模下的余数以及幂次 𝜈𝑝(𝑛!)νp(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的具体计算方法．

这种分解在解决阶乘同时出现在所求表达式的分子和分母的问题时尤为有用，比如 [计算某一模数下的二项式系数](../lucas/)．对于这类问题，分子和分母中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次可以直接相减，而与 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素的部分 (𝑛!)𝑝(n!)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则可以利用 [乘法逆元](../inverse/) 计算．

本文还介绍了与上述问题相关的 Wilson 定理及其推广、Legendre 公式和 Kummer 定理等内容．

## Wilson 定理

Wilson 定理给出了判断某个自然数是素数的一个充分必要条件．

Wilson 定理

对于自然数 𝑛 >1n>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数时，(𝑛 −1)! ≡ −1(mod𝑛)(n−1)!≡−1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

首先，证明对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 (𝑝 −1)! ≡ −1(mod𝑝)(p−1)!≡−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于这一点，可以利用 [同余方程](../congruence-equation/#推论-2) 或 [原根](../primitive-root/) 得到两种简洁的证明，此处略去不表．下面提供前置知识较少的一种证明方法：

当 𝑝 =2p=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，命题显然成立．下面设 𝑝 ≥3p≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，继而要证明 𝐙𝑝Zp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有非零元素（即同余类）的积为 ―――−1−1―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 𝐙𝑝Zp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有非零元素 ――𝑎a―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有逆元 ――𝑎−1a―−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是 𝐙𝑝Zp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中彼此互逆的元素乘积为 ――11―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是要注意 ――𝑎a―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ――𝑎−1a―−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能相等：――𝑎 =――𝑎−1a―=a―−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当 𝑎2 ≡1(mod𝑝)a2≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即

0≡𝑎2−1≡(𝑎+1)(𝑎−1),(mod𝑝)0≡a2−1≡(a+1)(a−1),(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从而，𝑎 ≡1(mod𝑝)a≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑎 ≡ −1(mod𝑝)a≡−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这说明 𝐙𝑝 ∖{――0,――1,―――−1}Zp∖{0―,1―,−1―}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有元素的乘积为 ――11―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进而 𝐙𝑝Zp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有非零元素的积为 ―――−1−1―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

反过来，对于合数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，要证明 (𝑛 −1)! ≢ −1(mod𝑛)(n−1)!≢−1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．利用反证法，不妨设 (𝑛 −1)! ≡ −1(mod𝑛)(n−1)!≡−1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即存在整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 (𝑛 −1)! =𝑘𝑛 −1(n−1)!=kn−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．因为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是合数，必然存在素数 𝑝 <𝑛p<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑛 =𝑝𝑚n=pm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 (𝑛 −1)! =𝑘𝑝𝑚 −1 ≡ −1(mod𝑝)(n−1)!=kpm−1≡−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，乘积 (𝑛 −1)!(n−1)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中必然已经出现 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而一定有 (𝑛 −1)! ≡0(mod𝑝)(n−1)!≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这一矛盾就说明了 (𝑛 −1)! ≢ −1(mod𝑛)(n−1)!≢−1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

利用本文的记号，Wilson 定理可以写作 (𝑝!)𝑝 ≡ −1(mod𝑝)(p!)p≡−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 推广

Wilson 定理可以推广到一般模数的情形．

定理（Gauss）

对于自然数 𝑚 >1m>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

∏1≤𝑘<𝑚, 𝑘⟂𝑚𝑘≡±1(mod𝑚).∏1≤k<m, k⟂mk≡±1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而且，余数中的 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取值为 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [原根存在](../primitive-root/#原根存在定理)，即 𝑚 =2,4,𝑝𝛼,2𝑝𝛼m=2,4,pα,2pα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，其中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇素数且 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是正整数．

证明

这个定理可以通过 [模 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整数乘法群](../../algebra/ring-theory/#应用整数同余类的乘法群) 的结构简单地证明．此处给出思路相仿，但是较为初等的证明．

对于 𝑚 =2m=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，有 1! =1 ≡ −1(mod2)1!=1≡−1(mod2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于其他存在原根的情形，设原根为 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则所有满足小于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且与它互素的正整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以唯一地表示为 𝑔𝑖mod𝑚gimodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，其中 0 ≤𝑖 <𝜑(𝑚)0≤i<φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 [Euler 函数](../euler-totient/)．直接验证可知，𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定是偶数．因为 𝑔𝑖gi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔𝜑(𝑚)−𝑖gφ(m)−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互为乘法逆元，所以在乘积中将它们两两配对，就有

∏1≤𝑘<𝑚, 𝑘⟂𝑚𝑘≡𝜑(𝑚)−1∏𝑖=0𝑔𝑖=𝑔𝜑(𝑚)/2𝜑(𝑚)/2−1∏𝑖=1𝑔𝑖𝑔𝜑(𝑚)−𝑖≡𝑔𝜑(𝑚)/2(mod𝑚).∏1≤k<m, k⟂mk≡∏i=0φ(m)−1gi=gφ(m)/2∏i=1φ(m)/2−1gigφ(m)−i≡gφ(m)/2(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝑔𝜑(𝑚)/2mod𝑚gφ(m)/2modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是唯一的不等于 1mod𝑚1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且乘法逆元就是它自身的元素，所以它就等于 −1mod𝑚−1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就说明了此时的余数等于 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根不存在的情形，要证明余数等于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．为此，可以首先做质因数分解 𝑚 =𝑝𝑒11𝑝𝑒22⋯𝑝𝑒𝑠𝑠m=p1e1p2e2⋯pses![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后应用 [中国剩余定理](../crt/) 可知，只需要证明

∏1≤𝑘<𝑚, 𝑘⟂𝑚𝑘≡1(mod𝑝𝑒𝑗𝑗)∏1≤k<m, k⟂mk≡1(modpjej)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对所有因子 𝑝𝑒𝑗𝑗pjej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．中国剩余定理说明，每一个可能的余数组合 (𝑟1,𝑟2,⋯,𝑟𝑠)(r1,r2,⋯,rs)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，1 ≤𝑟𝑗 <𝑝𝑒𝑗𝑗1≤rj<pjej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑝𝑗 ⟂𝑟𝑗pj⟂rj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都唯一地对应着一个 1 ≤𝑘 <𝑚1≤k<m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑘 ⟂𝑚k⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑘 ≡𝑟𝑗(mod𝑝𝑒𝑗𝑗)k≡rj(modpjej)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．所以，对于某个余数 𝑟𝑗rj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都恰好有 𝜑(𝑚)/𝜑(𝑝𝑒𝑗𝑗)φ(m)/φ(pjej)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑘 ≡𝑟𝑗(mod𝑝𝑒𝑗𝑗)k≡rj(modpjej)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．利用这一点，可以对乘积进行分组，就有

∏1≤𝑘<𝑚, 𝑘⟂𝑚𝑘≡⎛⎜ ⎜ ⎜ ⎜⎝∏1≤𝑟𝑗<𝑝𝑒𝑗𝑗, 𝑟𝑗⟂𝑝𝑗𝑟𝑗⎞⎟ ⎟ ⎟ ⎟⎠𝜑(𝑚)/𝜑(𝑝𝑒𝑗𝑗)(mod𝑝𝑒𝑗𝑗).∏1≤k<m, k⟂mk≡(∏1≤rj<pjej, rj⟂pjrj)φ(m)/φ(pjej)(modpjej).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此处的指数 𝜑(𝑚)/𝜑(𝑝𝑒𝑗𝑗) =𝜑(𝑚/𝑝𝑒𝑗𝑗)φ(m)/φ(pjej)=φ(m/pjej)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 要成为奇数，必然要求 𝑚/𝑝𝑒𝑗𝑗 =1,2m/pjej=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为欧拉函数 𝜑(𝑛)φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于 𝑛 ≥3n≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是偶数．如果 𝑝𝑗pj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇素数，因为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根不存在，必然有 𝑚/𝑝𝑒𝑗𝑗 ≠1,2m/pjej≠1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；如果 𝑝𝑒𝑗𝑗 =2,4pjej=2,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根不存在，必然有 𝑚/𝑝𝑒𝑗𝑗m/pjej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 含有某个奇素因子，故而大于 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：这两种情形指数 𝜑(𝑚)/𝜑(𝑝𝑒𝑗𝑗)φ(m)/φ(pjej)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是偶数．而上式中括号里的项已经证明是模 𝑝𝑒𝑗𝑗pjej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 余 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，所以这个幂模 𝑝𝑒𝑗𝑗pjej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的余数一定是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．剩余的情形只有 𝑝𝑗 =2pj=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑒𝑗 >2ej>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，对于这个情形，可以直接证明 `

∏1≤𝑟𝑗<2𝑒𝑗, 𝑟𝑗⟂2𝑟𝑗≡1(mod2𝑒𝑗).∏1≤rj<2ej, rj⟂2rj≡1(mod2ej).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

仿照前文的证明思路，可以将所有 1 ≤𝑟𝑗 <2𝑒𝑗1≤rj<2ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的奇数 𝑟𝑗rj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两配对而消去，那些无法配对的必然是方程 𝑥2 ≡1(mod2𝑒𝑗)x2≡1(mod2ej)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解．该方程意味着 2𝑒𝑗 ∣(𝑥 −1)(𝑥 +1)2ej∣(x−1)(x+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．令 𝑥 =2𝑦 +1x=2y+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就必然有 2𝑒𝑗−2 ∣𝑦(𝑦 +1)2ej−2∣y(y+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦 +1y+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然一奇一偶，所以 𝑦 =𝑡2𝑒𝑗−2y=t2ej−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑦 =𝑡2𝑒𝑗−2 −1y=t2ej−2−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．故而，有 𝑥 =𝑡2𝑒𝑗−1 ±1x=t2ej−1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是整数．模 2𝑒𝑗2ej![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的余数中，只有 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 2𝑒𝑗−1 ±12ej−1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 四个．因此，有

∏1≤𝑟𝑗<2𝑒𝑗, 𝑟𝑗⟂2𝑟𝑗≡(−1)(2𝑒𝑗−1−1)(2𝑒𝑗−1+1)≡1(mod2𝑒𝑗).∏1≤rj<2ej, rj⟂2rj≡(−1)(2ej−1−1)(2ej−1+1)≡1(mod2ej).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就完成了所有情形的证明．

在计算中，尤为重要的是模数为素数幂的情形：

推论

对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正整数 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

∏1≤𝑘<𝑝𝛼, 𝑘⟂𝑝𝑘≡{1,𝑝=2 and 𝛼≥3,−1,otherwise(mod𝑝𝛼).∏1≤k<pα, k⟂pk≡{1,p=2 and α≥3,−1,otherwise(modpα).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意，左侧并非 (𝑝𝛼!)𝑝(pα!)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为后者还需要统计 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数的贡献．

## 阶乘余数的计算

本节讨论余数 (𝑛!)𝑝mod𝑝𝛼(n!)pmodpα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算．

### 素数模的情形

算式 (𝑛!)𝑝(n!)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有明显的递归结构．为注意到这一点，首先考察一个具体的例子：

例子

要计算 (32!)5mod5(32!)5mod5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以做如下递归计算：

(32!)5=1×2×3×4×1⏟5×6×7×8×9×2⏟10×11×12×13×14×3⏟15×16×17×18×19×4⏟20×21×22×23×24×1⏟25×26×27×28×29×6⏟30×31×32≡1×2×3×4×1⏟5×1×2×3×4×2⏟10×1×2×3×4×3⏟15×1×2×3×4×4⏟20×1×2×3×4×1⏟25×1×2×3×4×1⏟30×1×2=(1×2×3×4)6×(1×2)×(1⏟5×2⏟10×3⏟15×4⏟20×1⏟25×1⏟30)(mod5)(32!)5=1×2×3×4×1⏟5×6×7×8×9×2⏟10×11×12×13×14×3⏟15×16×17×18×19×4⏟20×21×22×23×24×1⏟25×26×27×28×29×6⏟30×31×32≡1×2×3×4×1⏟5×1×2×3×4×2⏟10×1×2×3×4×3⏟15×1×2×3×4×4⏟20×1×2×3×4×1⏟25×1×2×3×4×1⏟30×1×2=(1×2×3×4)6×(1×2)×(1⏟5×2⏟10×3⏟15×4⏟20×1⏟25×1⏟30)(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以看出，利用模 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 余数的周期性，可以将这一乘积划分为若干个长度为 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的块，每一块的唯一差异就是最后一个元素的余数．因为 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 除以 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到的商是 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且余数是 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，该乘积可以划分为 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个完整的块和最后一段长度为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的不完整的块．因此，可以将前 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个块除了最后一个元素之外的部分提取出来（这一部分恰好是 Wilson 定理能够解决的），再乘上最后一个不完整的块的乘积，最后乘上前 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个块的最后一个元素的连乘积．每个块的最后一个元素都是 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数，去掉 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次后，它们的连乘积恰好是 (6!)5(mod5)(6!)5(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就将原来的问题转化为了规模更小的问题．

将该例子中的递归的结构一般化，就得到如下递推公式：

递推公式

对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

(𝑛!)𝑝≡(−1)⌊𝑛/𝑝⌋⋅(𝑛mod𝑝)!⋅(⌊𝑛/𝑝⌋!)𝑝(mod𝑝).(n!)p≡(−1)⌊n/p⌋⋅(nmodp)!⋅(⌊n/p⌋!)p(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

记 (𝑛)𝑝(n)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素因数分解中去除所有 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次的结果．于是，有

(𝑛!)𝑝=𝑛∏𝑘=1(𝑘)𝑝=(∏1≤𝑘≤𝑛, 𝑘⟂𝑝(𝑘)𝑝)⎛⎜ ⎜⎝∏1≤𝑘≤⌊𝑛/𝑝⌋(𝑝𝑘)𝑝⎞⎟ ⎟⎠=(⌊𝑛/𝑝⌋−1∏𝑖=0𝑝−1∏𝑗=1(𝑖𝑝+𝑗))(𝑛mod𝑝∏𝑗=1(⌊𝑛/𝑝⌋𝑝+𝑗))⎛⎜ ⎜⎝∏1≤𝑘≤⌊𝑛/𝑝⌋(𝑘)𝑝⎞⎟ ⎟⎠≡(𝑝−1∏𝑗=1𝑗)⌊𝑛/𝑝⌋(𝑛mod𝑝∏𝑗=1𝑗)(⌊𝑛/𝑝⌋!)𝑝≡(−1)⌊𝑛/𝑝⌋⋅(𝑛mod𝑝)!⋅(⌊𝑛/𝑝⌋!)𝑝(mod𝑝).(n!)p=∏k=1n(k)p=(∏1≤k≤n, k⟂p(k)p)(∏1≤k≤⌊n/p⌋(pk)p)=(∏i=0⌊n/p⌋−1∏j=1p−1(ip+j))(∏j=1nmodp(⌊n/p⌋p+j))(∏1≤k≤⌊n/p⌋(k)p)≡(∏j=1p−1j)⌊n/p⌋(∏j=1nmodpj)(⌊n/p⌋!)p≡(−1)⌊n/p⌋⋅(nmodp)!⋅(⌊n/p⌋!)p(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就完成了证明．下面对于该形式证明提供具体的解释．

要计算 (𝑛!)𝑝mod𝑝(n!)pmodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．仿照上面的例子，有

(𝑛!)𝑝=1⋅2⋅3⋅…⋅(𝑝−2)⋅(𝑝−1)⋅1⏟𝑝⋅(𝑝+1)⋅(𝑝+2)⋅…⋅(2𝑝−1)⋅2⏟2𝑝⋅(2𝑝+1)⋅…⋅(𝑝2−1)⋅1⏟𝑝2⋅(𝑝2+1)⋅…⋅𝑛(mod𝑝)=1⋅2⋅3⋅…⋅(𝑝−2)⋅(𝑝−1)⋅1⏟𝑝⋅1⋅2⋅…⋅(𝑝−1)⋅2⏟2𝑝⋅1⋅2⋅…⋅(𝑝−1)⋅1⏟𝑝2⋅1⋅2⋅…⋅(𝑛mod𝑝)(mod𝑝).(n!)p=1⋅2⋅3⋅…⋅(p−2)⋅(p−1)⋅1⏟p⋅(p+1)⋅(p+2)⋅…⋅(2p−1)⋅2⏟2p⋅(2p+1)⋅…⋅(p2−1)⋅1⏟p2⋅(p2+1)⋅…⋅n(modp)=1⋅2⋅3⋅…⋅(p−2)⋅(p−1)⋅1⏟p⋅1⋅2⋅…⋅(p−1)⋅2⏟2p⋅1⋅2⋅…⋅(p−1)⋅1⏟p2⋅1⋅2⋅…⋅(nmodp)(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以清楚地看到，除了最后一个块外，阶乘被划分为几个长度相同的完整的块．

(𝑛!)𝑝=1⋅2⋅3⋅…⋅(𝑝−2)⋅(𝑝−1)⋅1⏟____⏟____⏟1st⋅1⋅2⋅3⋅…⋅(𝑝−2)⋅(𝑝−1)⋅2⏟____⏟____⏟2nd⋅…⋅1⋅2⋅3⋅…⋅(𝑝−2)⋅(𝑝−1)⋅1⏟____⏟____⏟𝑝th⋅…⋅1⋅2⋅⋅…⋅(𝑛mod𝑝)⏟___⏟___⏟tail(mod𝑝).(n!)p=1⋅2⋅3⋅…⋅(p−2)⋅(p−1)⋅1⏟1st⋅1⋅2⋅3⋅…⋅(p−2)⋅(p−1)⋅2⏟2nd⋅…⋅1⋅2⋅3⋅…⋅(p−2)⋅(p−1)⋅1⏟pth⋅…⋅1⋅2⋅⋅…⋅(nmodp)⏟tail(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

除了块的最后一个元素外，完整的块的主要部分 (𝑝 −1)! mod 𝑝(p−1)! mod p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 很容易计算，可以应用 Wilson 定理：

(𝑝−1)!≡−1(mod𝑝).(p−1)!≡−1(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

总共有 ⌊𝑛𝑝⌋⌊np⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个完整的块，因此需要将 ⌊𝑛𝑝⌋⌊np⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 写到 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的指数上．

最后一个部分块的值就是 (𝑛mod𝑝)!mod𝑝(nmodp)!modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以单独计算．

剩下的就是每个块的最后一个元素．如果隐藏已处理的元素，可以看到以下模式：

(𝑛!)𝑝=…⋅1⏟⋅…⋅2⏟⋅…⋅…⋅(𝑝−1)⏟__⏟__⏟⋅…⋅1⏟⋅…⋅1⏟⋅…⋅2⏟⋯(n!)p=…⋅1⏟⋅…⋅2⏟⋅…⋅…⋅(p−1)⏟⋅…⋅1⏟⋅…⋅1⏟⋅…⋅2⏟⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这也是一个修正的阶乘，只是长度短得多．它是：

(⌊𝑛𝑝⌋!)𝑝.(⌊np⌋!)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将各部分乘起来，就得到上面的递推公式．

利用该递推式做计算，递归深度为 𝑂(log𝑝⁡𝑛)O(logp⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果每次都重新计算中间那一项，那么每层计算的复杂度都是 𝑂(𝑝)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，总的时间复杂度是 𝑂(𝑝log𝑝⁡𝑛)O(plogp⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；如果对所有 𝑛 =1,2,⋯,𝑝 −1n=1,2,⋯,p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都预先处理了 𝑛!mod𝑝n!modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么预处理的复杂度是 𝑂(𝑝)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，每层计算的复杂度都是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，总的时间复杂度是 𝑂(𝑝 +log𝑝⁡𝑛)O(p+logp⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

在实现时，因为是尾递归，可以用迭代实现．下面的实现对前 𝑝 −1p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个阶乘做了预计算，如果需要多次调用，可以将预计算放到函数外进行．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text // Calculate (n!)_p mod p. int factmod ( int n , int p ) { // Pretreatment. std :: vector < int > f ( p ); f [ 0 ] = 1 ; for ( int i = 1 ; i < p ; ++ i ) { f [ i ] = ( long long ) f [ i \- 1 ] * i % p ; } // Recursion. int res = 1 ; while ( n > 1 ) { if (( n / p ) & 1 ) res = p \- res ; res = ( long long ) res * f [ n % p ] % p ; n /= p ; } return res ; } ```   
---|---  
  
如果空间有限，无法存储所有阶乘，也可以将函数调用中实际用到的阶乘 𝑛!mod𝑝n!modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都计算出来，然后对它们进行排序，从而可以在最后一次性计算出来这些阶乘的值，汇总到最终结果中，而避免存储所有阶乘的值．

### 素数幂模的情形

对于素数幂模的情形，可以仿照素数模的情形解决，只需要将 Wilson 定理替换成它的推广形式．本节两个结论中的 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，均特指这样的定义：当模数 𝑝 =2p=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝛼 ≥3α≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时取 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其余情形取 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

递推公式

对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正整数 𝛼,𝑛α,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

(𝑛!)𝑝≡(±1)⌊𝑛/𝑝𝛼⌋⋅⎛⎜ ⎜⎝∏1≤𝑗≤(𝑛mod𝑝𝛼), 𝑗⟂𝑝𝑗⎞⎟ ⎟⎠⋅(⌊𝑛/𝑝⌋!)𝑝(mod𝑝𝛼).(n!)p≡(±1)⌊n/pα⌋⋅(∏1≤j≤(nmodpα), j⟂pj)⋅(⌊n/p⌋!)p(modpα).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值如同 Wilson 定理的推广 中规定的那样．

证明

证明思路和素数模的情形完全一致．记 (𝑘)𝑝(k)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为去除 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素因数分解中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全部幂次的结果，则

(𝑛!)𝑝=∏1≤𝑘≤𝑛(𝑘)𝑝=(∏1≤𝑘≤𝑛, 𝑘⟂𝑝(𝑘)𝑝)⎛⎜ ⎜⎝∏1≤𝑘≤⌊𝑛/𝑝⌋(𝑝𝑘)𝑝⎞⎟ ⎟⎠=(⌊𝑛/𝑝𝛼⌋−1∏𝑖=0∏1≤𝑗≤𝑝𝛼, 𝑗⟂𝑝(𝑖𝑝𝛼+𝑗)𝑝)⎛⎜ ⎜⎝∏1≤𝑗≤(𝑛mod𝑝𝛼), 𝑗⟂𝑝(⌊𝑛/𝑝𝛼⌋𝑝𝛼+𝑗)𝑝⎞⎟ ⎟⎠⎛⎜ ⎜⎝∏1≤𝑘≤⌊𝑛/𝑝⌋(𝑘)𝑝⎞⎟ ⎟⎠≡(∏1≤𝑗≤𝑝𝛼, 𝑗⟂𝑝𝑗)⌊𝑛/𝑝𝛼⌋⋅⎛⎜ ⎜⎝∏1≤𝑗≤(𝑛mod𝑝𝛼), 𝑗⟂𝑝𝑗⎞⎟ ⎟⎠⋅(⌊𝑛/𝑝⌋!)𝑝≡(±1)⌊𝑛/𝑝𝛼⌋⋅⎛⎜ ⎜⎝∏1≤𝑗≤(𝑛mod𝑝𝛼), 𝑗⟂𝑝𝑗⎞⎟ ⎟⎠⋅(⌊𝑛/𝑝⌋!)𝑝(mod𝑝𝛼).(n!)p=∏1≤k≤n(k)p=(∏1≤k≤n, k⟂p(k)p)(∏1≤k≤⌊n/p⌋(pk)p)=(∏i=0⌊n/pα⌋−1∏1≤j≤pα, j⟂p(ipα+j)p)(∏1≤j≤(nmodpα), j⟂p(⌊n/pα⌋pα+j)p)(∏1≤k≤⌊n/p⌋(k)p)≡(∏1≤j≤pα, j⟂pj)⌊n/pα⌋⋅(∏1≤j≤(nmodpα), j⟂pj)⋅(⌊n/p⌋!)p≡(±1)⌊n/pα⌋⋅(∏1≤j≤(nmodpα), j⟂pj)⋅(⌊n/p⌋!)p(modpα).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

与素数模的情形不同之处，除了 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能需要替换为 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之外，还需要注意预处理的数据的不同．对于素数幂模的情形，需要对所有不超过 𝑝𝛼pα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 预处理自 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 但并非 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数的所有整数的乘积，即

∏1≤𝑘≤𝑛, 𝑘⟂𝑝𝑘mod𝑝𝛼.∏1≤k≤n, k⟂pkmodpα.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在素数模的情形，它退化为 𝑛!mod𝑝n!modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是该表达式在一般的素数幂的情形不再适用．

下面提供了在素数幂模的情形下计算阶乘余数的例子，以便理解上述方法：

例子

要计算 (32!)3mod9(32!)3mod9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以做如下递归计算：

(32!)3=1×2×1⏟3×4×5×2⏟6×7×8×1⏟9×10×11×4⏟12×13×14×5⏟15×16×17×2⏟18×19×20×7⏟21×22×23×8⏟24×25×26×1⏟27×28×29×10⏟30×31×32≡1×2×1⏟3×4×5×2⏟6×7×8×1⏟9×1×2×4⏟12×4×5×5⏟15×7×8×2⏟18×1×2×7⏟21×4×5×8⏟24×7×8×1⏟27×1×2×1⏟30×4×5=(1×2×4×5×7×8)3×(1×2×4×5)×⎛⎜ ⎜ ⎜ ⎜⎝1⏟3×2⏟6×1⏟9×4⏟12×5⏟15×2⏟18×7⏟21×8⏟24×1⏟27×1⏟30⎞⎟ ⎟ ⎟ ⎟⎠(mod9).(32!)3=1×2×1⏟3×4×5×2⏟6×7×8×1⏟9×10×11×4⏟12×13×14×5⏟15×16×17×2⏟18×19×20×7⏟21×22×23×8⏟24×25×26×1⏟27×28×29×10⏟30×31×32≡1×2×1⏟3×4×5×2⏟6×7×8×1⏟9×1×2×4⏟12×4×5×5⏟15×7×8×2⏟18×1×2×7⏟21×4×5×8⏟24×7×8×1⏟27×1×2×1⏟30×4×5=(1×2×4×5×7×8)3×(1×2×4×5)×(1⏟3×2⏟6×1⏟9×4⏟12×5⏟15×2⏟18×7⏟21×8⏟24×1⏟27×1⏟30)(mod9).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将 (32!)3mod9(32!)3mod9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的算式分解的结果同样可以分为三部分：

  * 完整的块：由 1 ∼91∼9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间所有不被 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除的整数的乘积，共 ⌊32/9⌋ =3⌊32/9⌋=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块；
  * 尾部不完整的块：所有不被 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除的整数从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一直乘到 32mod932mod9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 所有被 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除的整数的乘积，对比倒数第二个等号的结果可知，这就是它的前 ⌊32/3⌋ =10⌊32/3⌋=10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项，亦即 (⌊32/3⌋!)3mod9(⌊32/3⌋!)3mod9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后一个括号里的递归求解即可，这样就将原问题转化为了更小的问题．

由此，就可以得到如下递推结果：

递推结果

对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正整数 𝛼,𝑛α,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

(𝑛!)𝑝≡(±1)∑𝑗≥𝛼⌊𝑛/𝑝𝑗⌋∏𝑗≥0𝐹(⌊𝑛/𝑝𝑗⌋mod𝑝𝛼),(n!)p≡(±1)∑j≥α⌊n/pj⌋∏j≥0F(⌊n/pj⌋modpα),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝐹(𝑚) =∏1≤𝑘≤𝑚, 𝑘⟂𝑝𝑘mod𝑝𝛼F(m)=∏1≤k≤m, k⟂pkmodpα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值与上文所述相同．

素数幂模的情形的实现和素数模的情形类似，只有一些细节上的区别．与上文类似，同样可以将预处理放到函数外进行．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text // Calculate (n!)_p mod pa. int factmod ( int n , int p , int pa ) { // Pretreatment. std :: vector < int > f ( pa ); f [ 0 ] = 1 ; for ( int i = 1 ; i < pa ; ++ i ) { f [ i ] = i % p ? ( long long ) f [ i \- 1 ] * i % pa : f [ i \- 1 ]; } // Recursion. bool neg = p != 2 || pa <= 4 ; int res = 1 ; while ( n > 1 ) { if (( n / pa ) & neg ) res = pa \- res ; res = ( long long ) res * f [ n % pa ] % pa ; n /= p ; } return res ; } ```   
---|---  
  
预处理的时间复杂度为 𝑂(𝑝𝛼)O(pα)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，单次询问的时间复杂度为 𝑂(log𝑝⁡𝑛)O(logp⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 幂次的计算

本节讨论阶乘 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次 𝜈𝑝(𝑛!)νp(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算，它可以用于计算二项式系数的余数．因为二项式系数中，分子和分母都会出现阶乘，而分子和分母中素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能否互相抵消，就成为了决定最后的余数的重要因素．

### Legendre 公式

阶乘 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次可以通过 Legendre 公式计算，而且与 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的表示有关．

Legendre 公式

对于正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，阶乘 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中含有的素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次 𝜈𝑝(𝑛!)νp(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

𝜈𝑝(𝑛!)=∞∑𝑖=1⌊𝑛𝑝𝑖⌋=𝑛−𝑆𝑝(𝑛)𝑝−1,νp(n!)=∑i=1∞⌊npi⌋=n−Sp(n)p−1,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑆𝑝(𝑛)Sp(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的各个数位的和．特别地，阶乘中 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次是 𝜈2(𝑛!) =𝑛 −𝑆2(𝑛)ν2(n!)=n−S2(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

因为

𝑛!=1×2×⋯×𝑝×⋯×2𝑝×⋯×⌊𝑛/𝑝⌋𝑝×⋯×𝑛.n!=1×2×⋯×p×⋯×2p×⋯×⌊n/p⌋p×⋯×n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数的乘积为 𝑝 ×2𝑝 ×⋯ ×⌊𝑛/𝑝⌋𝑝 =𝑝⌊𝑛/𝑝⌋⌊𝑛/𝑝⌋!p×2p×⋯×⌊n/p⌋p=p⌊n/p⌋⌊n/p⌋!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 ⌊𝑛/𝑝⌋!⌊n/p⌋!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能继续出现 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数．所以，对于幂次，有递推关系：

𝜈𝑝(𝑛!)=⌊𝑛/𝑝⌋+𝜈𝑝(⌊𝑛/𝑝⌋!).νp(n!)=⌊n/p⌋+νp(⌊n/p⌋!).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将它展开就得到 Legendre 公式．

要证明第二个等号，首先将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 展开为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制，这相当于将它写作如下和式：

𝑛=𝑛ℓ𝑝ℓ+⋯+𝑛1𝑝+𝑛0=ℓ∑𝑘=0𝑛𝑘𝑝𝑘.n=nℓpℓ+⋯+n1p+n0=∑k=0ℓnkpk.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，有

𝜈𝑝(𝑛!)=ℓ∑𝑖=1⌊𝑛𝑝𝑖⌋=ℓ∑𝑖=1ℓ∑𝑘=𝑖𝑛𝑘𝑝𝑘−𝑖=ℓ∑𝑘=1𝑛𝑘𝑘∑𝑖=1𝑝𝑘−𝑖=ℓ∑𝑘=1𝑛𝑘𝑝𝑘−1𝑝−1=∑ℓ𝑘=0𝑛𝑘𝑝𝑘−∑ℓ𝑘=0𝑛𝑘𝑝−1=𝑛−𝑆𝑝(𝑛)𝑝−1.νp(n!)=∑i=1ℓ⌊npi⌋=∑i=1ℓ∑k=iℓnkpk−i=∑k=1ℓnk∑i=1kpk−i=∑k=1ℓnkpk−1p−1=∑k=0ℓnkpk−∑k=0ℓnkp−1=n−Sp(n)p−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

求阶乘中素数幂次的参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // Obtain multiplicity of p in n!. int multiplicity_factorial ( int n , int p ) { int count = 0 ; do { n /= p ; count += n ; } while ( n ); return count ; } ```   
---|---  
  
它的时间复杂度为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### Kummer 定理

组合数对一个数取模的结果，往往构成分形结构，例如谢尔宾斯基三角形就可以通过组合数模 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到．

如果仔细分析，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否整除组合数其实和上下标在 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下减法是否需要借位有关．这就有了 **Kummer 定理** ．

Kummer 定理

素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在组合数 (𝑚𝑛)(mn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的幂次，恰好是 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 减掉 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要借位的次数，亦即

𝜈𝑝((𝑚𝑛))=𝑆𝑝(𝑛)+𝑆𝑝(𝑚−𝑛)−𝑆𝑝(𝑚)𝑝−1.νp((mn))=Sp(n)+Sp(m−n)−Sp(m)p−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

特别地，组合数中 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次是 𝜈2((𝑚𝑛)) =𝑆2(𝑛) +𝑆2(𝑚 −𝑛) −𝑆2(𝑚)ν2((mn))=S2(n)+S2(m−n)−S2(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

证明

首先证明下面的表达式．为此，利用 Legendre 公式，有

𝜈𝑝((𝑚𝑛))=𝜈𝑝(𝑚!)−𝜈𝑝(𝑛!)−𝜈𝑝((𝑚−𝑛)!)=∞∑𝑖=1(⌊𝑚𝑝𝑖⌋−⌊𝑛𝑝𝑖⌋−⌊𝑚−𝑛𝑝𝑖⌋)=𝑆𝑝(𝑛)+𝑆𝑝(𝑚−𝑛)−𝑆𝑝(𝑚)𝑝−1.νp((mn))=νp(m!)−νp(n!)−νp((m−n)!)=∑i=1∞(⌊mpi⌋−⌊npi⌋−⌊m−npi⌋)=Sp(n)+Sp(m−n)−Sp(m)p−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

该表达式可以理解为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 减掉 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要借位的次数．因为如果在计算第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位（最低位下标是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）时存在不够减需要借位的情况，那么相减的结果中第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位之前的数字 ⌊𝑚−𝑛𝑝𝑖⌋⌊m−npi⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其实是 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位之前的数字 ⌊𝑚𝑝𝑖⌋⌊mpi⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，减去一（即借掉的一），再减去 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位之前的数字得到的差值 ⌊𝑛𝑝𝑖⌋⌊npi⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，差值

⌊𝑚𝑝𝑖⌋−⌊𝑛𝑝𝑖⌋−⌊𝑚−𝑛𝑝𝑖⌋=1⌊mpi⌋−⌊npi⌋−⌊m−npi⌋=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当且仅当发生了一次借位；否则，该差值为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，上述表达式中的求和式就可以理解为借位发生的次数．这就得到了 Kummer 定理的文字表述．

## 例题

例题 [HDU 2973 - YAPTCHA](https://acm.hdu.edu.cn/showproblem.php?pid=2973)

给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 计算

𝑛∑𝑘=1⌊(3𝑘+6)!+13𝑘+7−⌊(3𝑘+6)!3𝑘+7⌋⌋∑k=1n⌊(3k+6)!+13k+7−⌊(3k+6)!3k+7⌋⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)解题思路

若 3𝑘 +73k+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是质数，则

(3𝑘+6)!≡−1(mod3𝑘+7)(3k+6)!≡−1(mod3k+7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 (3𝑘 +6)! +1 =𝑘(3𝑘 +7)(3k+6)!+1=k(3k+7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则

⌊(3𝑘+6)!+13𝑘+7−⌊(3𝑘+6)!3𝑘+7⌋⌋=⌊𝑘−⌊𝑘−13𝑘+7⌋⌋=1⌊(3k+6)!+13k+7−⌊(3k+6)!3k+7⌋⌋=⌊k−⌊k−13k+7⌋⌋=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若 3𝑘 +73k+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是质数，则有 (3𝑘 +7) ∣(3𝑘 +6)!(3k+7)∣(3k+6)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即

(3𝑘+6)!≡0(mod3𝑘+7)(3k+6)!≡0(mod3k+7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 (3𝑘 +6)! =𝑘(3𝑘 +7)(3k+6)!=k(3k+7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则

⌊(3𝑘+6)!+13𝑘+7−⌊(3𝑘+6)!3𝑘+7⌋⌋=⌊𝑘+13𝑘+7−𝑘⌋=0⌊(3k+6)!+13k+7−⌊(3k+6)!3k+7⌋⌋=⌊k+13k+7−k⌋=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此

𝑛∑𝑘=1⌊(3𝑘+6)!+13𝑘+7−⌊(3𝑘+6)!3𝑘+7⌋⌋=𝑛∑𝑘=1[3𝑘+7 is prime]∑k=1n⌊(3k+6)!+13k+7−⌊(3k+6)!3k+7⌋⌋=∑k=1n[3k+7 is prime]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text #include <iostream> constexpr int M = 1e6 \+ 5 , N = 3 * M \+ 7 ; bool not_prime [ N ]; int sum [ M ]; int main () { for ( int i = 2 ; i < N ; ++ i ) if ( ! not_prime [ i ]) for ( int j = 2 ; j * i < N ; ++ j ) not_prime [ j * i ] = true ; for ( int i = 1 ; i < M ; ++ i ) sum [ i ] = sum [ i \- 1 ] \+ ! not_prime [ 3 * i \+ 7 ]; int t ; std :: cin >> t ; while ( t \-- ) { int n ; std :: cin >> n ; std :: cout << sum [ n ] << std :: endl ; } } ```   
---|---  
  
## 参考资料

  * 冯克勤．《初等数论及其应用》．
  * [Wilson's theorem - Wikipedia](https://en.wikipedia.org/wiki/Wilson%27s_theorem)
  * [Legendre's formula - Wikipedia](https://en.wikipedia.org/wiki/Legendre%27s_formula)

**本页面主要译自博文[Вычисление факториала по модулю](http://e-maxx.ru/algo/modular_factorial) 与其英文翻译版 [Factorial modulo p](https://cp-algorithms.com/algebra/factorial-modulo.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．内容有改动．**

* * *

>  __本页面最近更新： 2026/2/11 21:19:06，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/factorial.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/factorial.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest), [Tiphereth-A](https://github.com/Tiphereth-A), [aofall](https://github.com/aofall), [CoelacanthusHex](https://github.com/CoelacanthusHex), [DanJoshua](https://github.com/DanJoshua), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Marcythm](https://github.com/Marcythm), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu), [wsyhb](https://github.com/wsyhb), [Xeonacid](https://github.com/Xeonacid), [yuyang0974](https://github.com/yuyang0974)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
