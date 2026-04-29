# 卢卡斯定理 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/lucas/

# 卢卡斯定理

前置知识：[阶乘取模](../factorial/)

## 引入

本文讨论大组合数取模的求解．组合数，又称二项式系数，指表达式：

(𝑛𝑘)=𝑛!𝑘!(𝑛−𝑘)!.(nk)=n!k!(n−k)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

规模不大时，组合数可以通过 [递推公式](../../combinatorics/combination/#组合数性质--二项式推论) 求解，时间复杂度为 𝑂(𝑛𝑘)O(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；也可以在较大的素数模数 𝑝 >𝑛p>n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下，通过计算分子和分母的阶乘在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内求解．但当问题规模很大（𝑛 ∼1018n∼1018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）时，这些方法不再适用．

基于 Lucas 定理及其推广，本文讨论一种可以在模数不太大 (𝑚 ∼106m∼106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)) 时求解组合数的方法．更准确地说，只要模数的唯一分解 𝑚 =∏𝑝𝑒𝑖𝑖m=∏piei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有素数幂的和（即 ∑𝑝𝑒𝑖𝑖∑piei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）在 106106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 规模时就可以使用该方法，因为算法的预处理大致相当于这一规模．

## Lucas 定理

首先讨论模数为素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．此时，有 Lucas 定理：

Lucas 定理

对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

(𝑛𝑘)≡(⌊𝑛/𝑝⌋⌊𝑘/𝑝⌋)(𝑛mod𝑝𝑘mod𝑝)(mod𝑝).(nk)≡(⌊n/p⌋⌊k/p⌋)(nmodpkmodp)(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，当 𝑛 <𝑘n<k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，二项式系数 (𝑛𝑘)(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 规定为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

利用生成函数证明

考虑 (𝑝𝑛)mod𝑝(pn)modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．因为

(𝑝𝑛)=𝑝!𝑛!(𝑝−𝑛)!,(pn)=p!n!(p−n)!,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，当 𝑛 ≠0,𝑝n≠0,p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，分母中都没有因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但分子中有因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以分式一定是 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数，模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的余数是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；当 𝑛 =0,𝑝n=0,p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，分式就是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，

(𝑝𝑛)≡[𝑛=0∨𝑛=𝑝](mod𝑝).(pn)≡[n=0∨n=p](modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

记 𝑓(𝑥) =𝑎𝑥𝑛 +𝑏𝑥𝑚f(x)=axn+bxm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．一般地，由 [二项式展开](../../combinatorics/combination/#二项式定理) 和 [费马小定理](../fermat/#费马小定理) 有

(𝑓(𝑥))𝑝=(𝑎𝑥𝑛+𝑏𝑥𝑚)𝑝=𝑝∑𝑘=0(𝑝𝑘)(𝑎𝑥𝑛)𝑘(𝑏𝑥𝑚)𝑝−𝑘≡𝑎𝑝𝑥𝑝𝑛+𝑏𝑝𝑥𝑝𝑚≡𝑎(𝑥𝑝)𝑛+𝑏(𝑥𝑝)𝑚=𝑓(𝑥𝑝)(mod𝑝).(f(x))p=(axn+bxm)p=∑k=0p(pk)(axn)k(bxm)p−k≡apxpn+bpxpm≡a(xp)n+b(xp)m=f(xp)(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，第三行的同余利用了前文说明的结论，即只有 𝑘 =0,𝑝k=0,p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，组合数才不是 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数．

利用这一结论，考察二项式展开：

(1+𝑥)𝑛=(1+𝑥)𝑝⌊𝑛/𝑝⌋(1+𝑥)𝑛mod𝑝≡(1+𝑥𝑝)⌊𝑛/𝑝⌋(1+𝑥)𝑛mod𝑝(mod𝑝).(1+x)n=(1+x)p⌊n/p⌋(1+x)nmodp≡(1+xp)⌊n/p⌋(1+x)nmodp(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

等式左侧中，项 𝑥𝑘xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数为

(𝑛𝑘)mod𝑝.(nk)modp.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

转而计算等式右侧中项 𝑥𝑘xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数．第一个因子中各项的次数必然是 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数，第二个因子中各项的次数必然小于 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解成这样两部分的和的方式是唯一的，即带余除法：𝑘 =𝑝⌊𝑘/𝑝⌋ +(𝑘mod𝑝)k=p⌊k/p⌋+(kmodp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，第一个因子只能贡献其 𝑝⌊𝑘/𝑝⌋p⌊k/p⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次项，第二个因子只能贡献其 𝑘mod𝑝kmodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次项．所以，右侧等式中 𝑥𝑘xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 系数为两个因子各自贡献的项的系数的乘积：

(⌊𝑛/𝑝⌋⌊𝑘/𝑝⌋)(𝑛mod𝑝𝑘mod𝑝)mod𝑝.(⌊n/p⌋⌊k/p⌋)(nmodpkmodp)modp.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令两侧系数相等，就得到 Lucas 定理．

利用阶乘取模的结论证明

此处提供一种基于 [阶乘取模](../factorial/#素数模的情形) 相关结论的证明方法，以方便和后文 exLucas 部分的方法建立联系．已知二项式系数

(𝑛𝑘)=𝑛!𝑘!(𝑛−𝑘)!.(nk)=n!k!(n−k)!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将阶乘 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次和其他因子分离，得到分解：

𝑛!=𝑝𝜈𝑝(𝑛!)(𝑛!)𝑝.n!=pνp(n!)(n!)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就得到二项式系数的表达式：

(𝑛𝑘)=𝑝𝜈𝑝(𝑛!)−𝜈𝑝(𝑘!)−𝜈𝑝((𝑛−𝑘)!)(𝑛!)𝑝(𝑘!)𝑝((𝑛−𝑘)!)𝑝.(nk)=pνp(n!)−νp(k!)−νp((n−k)!)(n!)p(k!)p((n−k)!)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

幂次 𝜈𝑝(𝑛!)νp(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和阶乘余数 (𝑛!)𝑝mod𝑝(n!)pmodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有递推公式：

𝜈𝑝(𝑛!)=⌊𝑛/𝑝⌋+𝜈𝑝(⌊𝑛/𝑝⌋!),(𝑛!)𝑝≡(−1)⌊𝑛/𝑝⌋⋅(𝑛mod𝑝)!⋅(⌊𝑛/𝑝⌋!)𝑝(mod𝑝).νp(n!)=⌊n/p⌋+νp(⌊n/p⌋!),(n!)p≡(−1)⌊n/p⌋⋅(nmodp)!⋅(⌊n/p⌋!)p(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

前者是 Legendre 公式的推论，后者是 Wilson 定理的推论．

将递推公式代入二项式系数的表达式并整理，就得到：

(𝑛𝑘)≡(−𝑝)⌊𝑛/𝑝⌋−⌊𝑘/𝑝⌋−⌊(𝑛−𝑘)/𝑝⌋⋅(𝑛mod𝑝)!(𝑘mod𝑝)!((𝑛−𝑘)mod𝑝)!⋅𝑝𝜈𝑝(⌊𝑛/𝑝⌋!)−𝜈𝑝(⌊𝑘/𝑝⌋!)−𝜈𝑝(⌊(𝑛−𝑘)/𝑝⌋!)(⌊𝑛/𝑝⌋!)𝑝(⌊𝑘/𝑝⌋!)𝑝(⌊(𝑛−𝑘)/𝑝⌋!)𝑝(mod𝑝).(nk)≡(−p)⌊n/p⌋−⌊k/p⌋−⌊(n−k)/p⌋⋅(nmodp)!(kmodp)!((n−k)modp)!⋅pνp(⌊n/p⌋!)−νp(⌊k/p⌋!)−νp(⌊(n−k)/p⌋!)(⌊n/p⌋!)p(⌊k/p⌋!)p(⌊(n−k)/p⌋!)p(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

现在考察 ⌊𝑛/𝑝⌋ −⌊𝑘/𝑝⌋ −⌊(𝑛 −𝑘)/𝑝⌋⌊n/p⌋−⌊k/p⌋−⌊(n−k)/p⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．因为有

𝑛=⌊𝑛/𝑝⌋𝑝+(𝑛mod𝑝),𝑘=⌊𝑘/𝑝⌋𝑝+(𝑘mod𝑝),𝑛−𝑘=⌊(𝑛−𝑘)/𝑝⌋𝑝+((𝑛−𝑘)mod𝑝),n=⌊n/p⌋p+(nmodp),k=⌊k/p⌋p+(kmodp),n−k=⌊(n−k)/p⌋p+((n−k)modp),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，利用第一式减去后两式，就得到

(⌊𝑛/𝑝⌋−⌊𝑘/𝑝⌋−⌊(𝑛−𝑘)/𝑝⌋)𝑝=(𝑘mod𝑝)+((𝑛−𝑘)mod𝑝)−(𝑛mod𝑝).(⌊n/p⌋−⌊k/p⌋−⌊(n−k)/p⌋)p=(kmodp)+((n−k)modp)−(nmodp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

等式右侧，前两项的和严格小于 2𝑝2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而第三项 𝑛mod𝑝nmodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 正是前两项的和的余数，所以右侧必然非负，但小于 2𝑝2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又需要是 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数，就只能是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这说明 ⌊𝑛/𝑝⌋ −⌊𝑘/𝑝⌋ −⌊(𝑛 −𝑘)/𝑝⌋⌊n/p⌋−⌊k/p⌋−⌊(n−k)/p⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只能是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

  * 如果它是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么此时也成立 (𝑛mod𝑝) =(𝑘mod𝑝) +((𝑛 −𝑘)mod𝑝)(nmodp)=(kmodp)+((n−k)modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，上式中的第一个因子的指数为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，该因子就等于一；第二个因子就是 (𝑛mod𝑝𝑘mod𝑝)(nmodpkmodp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；第三个因子则由前文的展开式可知，就等于 (⌊𝑛/𝑝⌋⌊𝑘/𝑝⌋)(⌊n/p⌋⌊k/p⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时，Lucas 公式成立；
  * 如果它是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么第一个因子的指数为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，该因子就等于零，所以二项式系数的余数为零．同时，Lucas 定理所要证明的等式右侧的 (𝑛mod𝑝𝑘mod𝑝)(nmodpkmodp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也必然是零，因为此时必然有 (𝑛mod𝑝) <(𝑘mod𝑝)(nmodp)<(kmodp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；否则，将有

((𝑛−𝑘)mod𝑝)=𝑝+(𝑛mod𝑝)−(𝑘mod𝑝)≥𝑝.((n−k)modp)=p+(nmodp)−(kmodp)≥p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这显然与余数的定义矛盾．

综合两种情形，就得到了所要求证的 Lucas 定理．这一证明说明，在求解素数模下组合数时，利用 Lucas 定理和利用 exLucas 算法得到的结果是等价的．

Lucas 定理指出，模数为素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，大组合数的计算可以转化为规模更小的组合数的计算．在右式中，第一个组合数可以继续递归，直到 𝑛,𝑘 <𝑝n,k<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为止；第二个组合数则可以直接计算，或者提前预处理出来．写成代码的形式就是：

示意

```text 1 2 3 4 ``` |  ```text long long Lucas ( long long n , long long k , long long p ) { if ( k == 0 ) return 1 ; return ( C ( n % p , k % p , p ) * Lucas ( n / p , k / p , p )) % p ; } ```   
---|---  
  
其中，`C(n, k, p)` 用于计算小规模的组合数．

递归至多进行 𝑂(log𝑝⁡𝑛)O(logp⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，因而算法的复杂度为 𝑂(𝑓(𝑝) +𝑔(𝑝)log𝑝⁡𝑛)O(f(p)+g(p)logp⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑓(𝑝)f(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为预处理组合数的复杂度，𝑔(𝑝)g(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为单次计算组合数的复杂度．

### 参考实现

此处给出的参考实现在 𝑂(𝑝)O(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内预处理 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以内的阶乘及其逆元后，可以在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算单个组合数：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 ``` |  ```text #include <iostream> #include <vector> class BinomModPrime { int p ; std :: vector < int > fa , ifa ; // Calculate binom(n, k) mod p for n, k < p. int calc ( int n , int k ) { if ( n < k ) return 0 ; long long res = fa [ n ]; res = ( res * ifa [ k ]) % p ; res = ( res * ifa [ n \- k ]) % p ; return res ; } public : BinomModPrime ( int p ) : p ( p ), fa ( p ), ifa ( p ) { // Factorials mod p till p. fa [ 0 ] = 1 ; for ( int i = 1 ; i < p ; ++ i ) { fa [ i ] = ( long long ) fa [ i \- 1 ] * i % p ; } // Inverse of factorials mod p till p. ifa [ p \- 1 ] = p \- 1 ; // Wilson's theorem. for ( int i = p \- 1 ; i ; \-- i ) { ifa [ i \- 1 ] = ( long long ) ifa [ i ] * i % p ; } } // Calculate binom(n, k) mod p. int binomial ( long long n , long long k ) { long long res = 1 ; while ( n || k ) { res = ( res * calc ( n % p , k % p )) % p ; n /= p ; k /= p ; } return res ; } }; int main () { int t , p ; std :: cin >> t >> p ; BinomModPrime bm ( p ); for (; t ; \-- t ) { long long n , k ; std :: cin >> n >> k ; std :: cout << bm . binomial ( n , k ) << '\n' ; } return 0 ; } ```   
---|---  
  
该实现的时间复杂度为 𝑂(𝑝 +𝑇log𝑝⁡𝑛)O(p+Tlogp⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为询问次数．

## exLucas 算法

Lucas 定理中对于模数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 要求必须为素数，那么对于 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是素数的情况，就需要用到 exLucas 算法．虽然名字如此，该算法实际操作时并没有用到 Lucas 定理．它的关键步骤是 [计算素数幂模下的阶乘](../factorial/)．上文的第二个证明指出了它与 Lucas 定理的联系．

### 素数幂模的情形

首先考虑模数为素数幂 𝑝𝛼pα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．将阶乘 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次和其他幂次分开，可以得到分解：

𝑛!=𝑝𝜈𝑝(𝑛!)(𝑛!)𝑝.n!=pνp(n!)(n!)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝜈𝑝(𝑛!)νp(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素因数分解中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次，而 (𝑛!)𝑝(n!)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 显然与 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素．因此，组合数可以写作：

(𝑛𝑘)=𝑝𝜈𝑝(𝑛!)−𝜈𝑝(𝑘!)−𝜈𝑝((𝑛−𝑘)!)(𝑛!)𝑝(𝑘!)𝑝((𝑛−𝑘)!)𝑝.(nk)=pνp(n!)−νp(k!)−νp((n−k)!)(n!)p(k!)p((n−k)!)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

式子中的 𝜈𝑝(𝑛!)νp(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等可以通过 [Legendre 公式](../factorial/#legendre-公式) 计算，(𝑛!)𝑝(n!)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等则可以通过 [递推关系](../factorial/#素数幂模的情形) 计算．因为后者与 𝑝𝛼pα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素，所以分母上的乘积的逆元可以通过 [扩展欧几里得算法](../inverse/#扩展欧几里得算法) 计算．问题就得以解决．

注意，如果幂次 𝜈𝑝(𝑛!) −𝜈𝑝(𝑘!) −𝜈𝑝((𝑛 −𝑘)!) ≥𝛼νp(n!)−νp(k!)−νp((n−k)!)≥α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，余数一定为零，不必再做更多计算．

### 一般模数的情形

对于 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一般的合数的情形，只需要首先对它做 [素因数分解](../pollard-rho/)：

𝑚=𝑝𝛼11𝑝𝛼22⋯𝑝𝛼𝑠𝑠.m=p1α1p2α2⋯psαs.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后，分别计算出模 𝑝𝛼𝑖𝑖piαi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下组合数 (𝑛𝑘)(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的余数，就得到 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个同余方程：

⎧{ { { { {⎨{ { { { {⎩(𝑛𝑘)≡𝑟1,(mod𝑝𝛼11),(𝑛𝑘)≡𝑟2,(mod𝑝𝛼22),⋯(𝑛𝑘)≡𝑟𝑠,(mod𝑝𝛼𝑠𝑠).{(nk)≡r1,(modp1α1),(nk)≡r2,(modp2α2),⋯(nk)≡rs,(modpsαs).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最后，利用 [中国剩余定理](../crt/) 求出模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的余数．

### 参考实现

最后，给出模板题目 [二项式系数](https://loj.ac/p/181) 的参考实现．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 ``` |  ```text #include <iostream> #include <vector> // Extended Euclid. void ex_gcd ( int a , int b , int & x , int & y ) { if ( ! b ) { x = 1 ; y = 0 ; } else { ex_gcd ( b , a % b , y , x ); y -= a / b * x ; } } // Inverse of a mod m. int inverse ( int a , int m ) { int x , y ; ex_gcd ( a , m , x , y ); return ( x % m \+ m ) % m ; } // Coefficient in CRT. int crt_coeff ( int m_i , int m ) { long long mm = m / m_i ; mm *= inverse ( mm , m_i ); return mm % m ; } // Binominal Coefficient Calculator Modulo Prime Power. class BinomModPrimePower { int p , a , pa ; std :: vector < int > f ; // Obtain multiplicity of p in n!. long long nu ( long long n ) { long long count = 0 ; do { n /= p ; count += n ; } while ( n ); return count ; } // Calculate (n!)_p mod pa. long long fact_mod ( long long n ) { bool neg = p != 2 || pa <= 4 ; long long res = 1 ; while ( n > 1 ) { if (( n / pa ) & neg ) res = pa \- res ; res = res * f [ n % pa ] % pa ; n /= p ; } return res ; } public : BinomModPrimePower ( int p , int a , int pa ) : p ( p ), a ( a ), pa ( pa ), f ( pa ) { // Pretreatment. f [ 0 ] = 1 ; for ( int i = 1 ; i < pa ; ++ i ) { f [ i ] = i % p ? ( long long ) f [ i \- 1 ] * i % pa : f [ i \- 1 ]; } } // Calculate Binom(n, k) mod pa. int binomial ( long long n , long long k ) { long long v = nu ( n ) \- nu ( n \- k ) \- nu ( k ); if ( v >= a ) return 0 ; auto res = fact_mod ( n \- k ) * fact_mod ( k ) % pa ; res = fact_mod ( n ) * inverse ( res , pa ) % pa ; for (; v ; \-- v ) res *= p ; return res % pa ; } }; // Binominal Coefficient Calculator. class BinomMod { int m ; std :: vector < BinomModPrimePower > bp ; std :: vector < long long > crt_m ; public : BinomMod ( int n ) : m ( n ) { // Factorize. for ( int p = 2 ; p * p <= n ; ++ p ) { if ( n % p == 0 ) { int a = 0 , pa = 1 ; for (; n % p == 0 ; n /= p , ++ a , pa *= p ); bp . emplace_back ( p , a , pa ); crt_m . emplace_back ( crt_coeff ( pa , m )); } } if ( n > 1 ) { bp . emplace_back ( n , 1 , n ); crt_m . emplace_back ( crt_coeff ( n , m )); } } // Calculate Binom(n, k) mod m. int binomial ( long long n , long long k ) { long long res = 0 ; for ( size_t i = 0 ; i != bp . size (); ++ i ) { res = ( bp [ i ]. binomial ( n , k ) * crt_m [ i ] \+ res ) % m ; } return res ; } }; int main () { int t , m ; std :: cin >> t >> m ; BinomMod bm ( m ); for (; t ; \-- t ) { long long n , k ; std :: cin >> n >> k ; std :: cout << bm . binomial ( n , k ) << '\n' ; } return 0 ; } ```   
---|---  
  
该算法在预处理时将模数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解为素数幂，然后对所有 𝑝𝛼pα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 预处理了自 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至 𝑝𝛼pα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所有非 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倍数的自然数的乘积，以及它在中国剩余定理合并答案时对应的系数．预处理的时间复杂度为 𝑂(√𝑚 +∑𝑖𝑝𝛼𝑖𝑖)O(m+∑ipiαi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每次询问时，复杂度为 𝑂(log⁡𝑚 +∑𝑖log𝑝𝑖⁡𝑛)O(log⁡m+∑ilogpi⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，复杂度中的两项分别是计算逆元和计算幂次、阶乘余数的复杂度．

## 习题

  * [Luogu3807【模板】卢卡斯定理](https://www.luogu.com.cn/problem/P3807)
  * [SDOI2010 古代猪文 卢卡斯定理](https://loj.ac/problem/10229)
  * [Luogu4720【模板】扩展卢卡斯](https://www.luogu.com.cn/problem/P4720)
  * [Ceizenpok’s formula](http://codeforces.com/gym/100633/problem/J)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/lucas.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/lucas.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [c-forrest](https://github.com/c-forrest), [GitPinkRabbit](https://github.com/GitPinkRabbit), [Great-designer](https://github.com/Great-designer), [TonyYin0418](https://github.com/TonyYin0418), [Xeonacid](https://github.com/Xeonacid), [EntropyIncreaser](https://github.com/EntropyIncreaser), [ksyx](https://github.com/ksyx), [MegaOwIer](https://github.com/MegaOwIer), [sshwy](https://github.com/sshwy), [Henry-ZHR](https://github.com/Henry-ZHR), [iamtwz](https://github.com/iamtwz), [ouuan](https://github.com/ouuan), [Sheng-Horizon](https://github.com/Sheng-Horizon), [Tiphereth-A](https://github.com/Tiphereth-A), [CornWorld](https://github.com/CornWorld), [IceySakura](https://github.com/IceySakura), [Ir1d](https://github.com/Ir1d), [LuoYisu](https://github.com/LuoYisu), [Marcythm](https://github.com/Marcythm), [megakite](https://github.com/megakite), [Menci](https://github.com/Menci), [shawlleyw](https://github.com/shawlleyw), [StudyingFather](https://github.com/StudyingFather), [whongzhong](https://github.com/whongzhong), [YOYO-UIAT](https://github.com/YOYO-UIAT)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
