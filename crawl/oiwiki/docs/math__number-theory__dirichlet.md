# 狄利克雷卷积 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/dirichlet/

# 狄利克雷卷积

本文介绍 Dirichlet 卷积和 Dirichlet 生成函数．

## Dirichlet 卷积

数论函数 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **Dirichlet 卷积** （Dirichlet convolution），记作 𝑓 ∗𝑔f∗g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义为数论函数

(𝑓∗𝑔)(𝑛)=∑𝑘∣𝑛𝑓(𝑘)𝑔(𝑛𝑘)=∑𝑘ℓ=𝑛𝑓(𝑘)𝑔(ℓ).(f∗g)(n)=∑k∣nf(k)g(nk)=∑kℓ=nf(k)g(ℓ).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Dirichlet 卷积是数论函数的重要运算．数论函数的许多性质都是通过这个运算挖掘出来的．

例子

  1. 单位函数 𝜀ε![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是莫比乌斯函数 𝜇μ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和常数函数 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Dirichlet 卷积：

𝜀=𝜇∗1⟺𝜀(𝑛)=∑𝑑∣𝑛𝜇(𝑑).ε=μ∗1⟺ε(n)=∑d∣nμ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 除数个数函数 𝜏τ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是常数函数 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和它自身的 Dirichlet 卷积：

𝜏=1∗1⟺𝜏(𝑛)=∑𝑑∣𝑛1.τ=1∗1⟺τ(n)=∑d∣n1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. 除数和函数 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是恒等函数 idid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和常数函数 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Dirichlet 卷积：

𝜎=id∗1⟺𝜎(𝑛)=∑𝑑∣𝑛𝑑.σ=id∗1⟺σ(n)=∑d∣nd.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. 欧拉函数 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是恒等函数 idid![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和莫比乌斯函数 𝜇μ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Dirichlet 卷积：

𝜑=id∗𝜇⟺𝜑(𝑛)=∑𝑑∣𝑛𝑑⋅𝜇(𝑛𝑑).φ=id∗μ⟺φ(n)=∑d∣nd⋅μ(nd).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

[莫比乌斯反演](../mobius/) 就是利用 𝜀 =𝜇 ∗1ε=μ∗1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对数论函数恒等式进行变形．

### 性质

Dirichlet 卷积具有一系列代数性质．

定理

设 𝑓,𝑔,ℎf,g,h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是数论函数．那么，有：

  1. **交换律** ：𝑓 ∗𝑔 =𝑔 ∗𝑓f∗g=g∗f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. **结合律** ：(𝑓 ∗𝑔) ∗ℎ =𝑓 ∗(𝑔 ∗ℎ)(f∗g)∗h=f∗(g∗h)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. **分配律** ：(𝑓 +𝑔) ∗ℎ =𝑓 ∗ℎ +𝑔 ∗ℎ(f+g)∗h=f∗h+g∗h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  4. **单位元** ：𝑓 ∗𝜀 =𝜀 ∗𝑓 =𝑓f∗ε=ε∗f=f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝜀(𝑛) =[𝑛 =1]ε(n)=[n=1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是卷积单位元，[ ⋅][⋅]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Iverson 括号．
  5. **逆元** ：当且仅当 𝑓(1) ≠0f(1)≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，存在 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑓 ∗𝑔 =𝑔 ∗𝑓 =𝜀f∗g=g∗f=ε![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **Dirichlet 逆元** （Dirichlet inverse），可以记作 𝑓−1f−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而且，逆元 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足递推公式

𝑔(𝑛)=𝜀(𝑛)−∑𝑘ℓ=𝑛, 𝑘≠1𝑓(𝑘)𝑔(ℓ)𝑓(1).g(n)=ε(n)−∑kℓ=n, k≠1f(k)g(ℓ)f(1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明

为验证交换律，直接计算可知

(𝑓∗𝑔)(𝑛)=∑𝑘ℓ=𝑛𝑓(𝑘)𝑔(ℓ)=(𝑔∗𝑓)(𝑛).(f∗g)(n)=∑kℓ=nf(k)g(ℓ)=(g∗f)(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为验证结合律，直接计算可知

((𝑓∗𝑔)∗ℎ)(𝑛)=∑𝑘ℓ𝑚=𝑛𝑓(𝑘)𝑔(ℓ)ℎ(𝑚)=(𝑓∗(𝑔∗ℎ))(𝑛).((f∗g)∗h)(n)=∑kℓm=nf(k)g(ℓ)h(m)=(f∗(g∗h))(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为验证分配律，直接计算可知

((𝑓+𝑔)∗ℎ)(𝑛)=∑𝑘ℓ=𝑛(𝑓(𝑘)+𝑔(𝑘))ℎ(ℓ)=∑𝑘ℓ=𝑛𝑓(𝑘)ℎ(ℓ)+∑𝑘ℓ=𝑛𝑔(𝑘)ℎ(ℓ)=(𝑓∗ℎ+𝑔∗ℎ)(𝑛).((f+g)∗h)(n)=∑kℓ=n(f(k)+g(k))h(ℓ)=∑kℓ=nf(k)h(ℓ)+∑kℓ=ng(k)h(ℓ)=(f∗h+g∗h)(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为验证 𝜀(𝑛)ε(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是单位元，直接计算可知

(𝑓∗𝜀)(𝑛)=∑𝑘ℓ=𝑛𝑓(𝑘)𝜀(ℓ)=𝑓(𝑛).(f∗ε)(n)=∑kℓ=nf(k)ε(ℓ)=f(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

第二个等号是因为 𝜀(ℓ)ε(ℓ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仅在 ℓ =1ℓ=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即 𝑘 =𝑛k=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时取得非零值．

最后，需要证明 𝑓−1f−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在，当且仅当 𝑓(1) ≠0f(1)≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于任意 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，假设存在 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑓 ∗𝑔 =𝜀f∗g=ε![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这意味着

(𝑓∗𝑔)(𝑛)=∑𝑘ℓ=𝑛𝑓(𝑘)𝑔(ℓ)=𝜀(𝑛).(f∗g)(n)=∑kℓ=nf(k)g(ℓ)=ε(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这实际上给出了一系列关于 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取值的方程组，从中可以直接求出 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．特别地，当 𝑛 =1n=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，等式变为 𝑓(1)𝑔(1) =1f(1)g(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在，至少要求 𝑓(1) ≠0f(1)≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而只要 𝑓(1) ≠0f(1)≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以直接解出

𝑔(𝑛)=𝜀(𝑛)−∑𝑘ℓ=𝑛, 𝑘≠1𝑓(𝑘)𝑔(ℓ)𝑓(1).g(n)=ε(n)−∑kℓ=n, k≠1f(k)g(ℓ)f(1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它可以用于递归计算 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．因此，逆元 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在，当且仅当 𝑓(1) ≠0f(1)≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

用抽象代数的语言说，这些代数性质说明，全体数论函数在（逐点）加法运算和 Dirichlet 卷积运算下构成 [交换环](../../algebra/basic/#环)，且它的全体可逆元就是那些在 𝑛 =1n=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处取非零值的函数．这个环称为 **Dirichlet 环** （Dirichlet ring）．

积性函数是一类特殊的数论函数．它对于 Dirichlet 卷积和 Dirichlet 逆都是封闭的．

定理

设 𝑓,𝑔f,g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数，那么，𝑓 ∗𝑔f∗g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是积性函数．而且，逆元 𝑓−1f−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定存在，它也是积性函数．

证明

对于第一点，设 ℎ =𝑓 ∗𝑔h=f∗g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直接验证可知，对于 𝑛1 ⟂𝑛2n1⟂n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

ℎ(𝑛1)ℎ(𝑛2)=(∑𝑘1ℓ1=𝑛1𝑓(𝑘1)𝑔(ℓ1))(∑𝑘2ℓ2=𝑛2𝑓(𝑘2)𝑔(ℓ2))=∑𝑘1ℓ1=𝑛1, 𝑘2ℓ2=𝑛2𝑓(𝑘1)𝑓(𝑘2)𝑔(ℓ1)𝑔(ℓ2)=∑𝑘ℓ=𝑛1𝑛2𝑓(𝑘)𝑔(ℓ)=ℎ(𝑛1𝑛2).h(n1)h(n2)=(∑k1ℓ1=n1f(k1)g(ℓ1))(∑k2ℓ2=n2f(k2)g(ℓ2))=∑k1ℓ1=n1, k2ℓ2=n2f(k1)f(k2)g(ℓ1)g(ℓ2)=∑kℓ=n1n2f(k)g(ℓ)=h(n1n2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，第三个等号改变求和顺序的逻辑是：当 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历 𝑛1𝑛2n1n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的因数时，𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素因子可以根据它是 𝑛1n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还是 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素因子分为两类，将两类中的素因子（计重复）分别乘起来得到 𝑘1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑘2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它们将分别遍历 𝑛1n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的因数；反过来，根据 𝑛1n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的因数 𝑘1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑘2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，总是可以得到 𝑛1𝑛2n1n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的因数 𝑘 =𝑘1𝑘2k=k1k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于第二点，设 𝑔 =𝑓−1g=f−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考虑应用数学归纳法．首先，𝑔(1) =1/𝑓(1) =1g(1)=1/f(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时，逆元的递归公式可以写作

𝑔(𝑛)=𝜀(𝑛)−∑𝑘ℓ=𝑛, 𝑘≠1𝑓(𝑘)𝑔(ℓ).g(n)=ε(n)−∑kℓ=n, k≠1f(k)g(ℓ).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，对于 𝑛1 ⟂𝑛2n1⟂n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑛1𝑛2 >1n1n2>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝑔(𝑛1𝑛2)=−∑𝑘ℓ=𝑛1𝑛2, 𝑘≠1𝑓(𝑘)𝑔(ℓ)=−∑𝑘1ℓ1=𝑛1, 𝑘2ℓ2=𝑛2, 𝑘1𝑘2≠1𝑓(𝑘1)𝑓(𝑘2)𝑔(ℓ1)𝑔(ℓ2)=𝑓(1)𝑓(1)𝑔(𝑛1)𝑔(𝑛2)−∑𝑘1ℓ1=𝑛1, 𝑘2ℓ2=𝑛2𝑓(𝑘1)𝑓(𝑘2)𝑔(ℓ1)𝑔(ℓ2)=𝑔(𝑛1)𝑔(𝑛2)−(∑𝑘1ℓ1=𝑛1𝑓(𝑘1)𝑔(ℓ1))(∑𝑘2ℓ2=𝑛2𝑓(𝑘2)𝑔(ℓ2))=𝑔(𝑛1)𝑔(𝑛2)−𝜀(𝑛1)𝜀(𝑛2)=𝑔(𝑛1)𝑔(𝑛2).g(n1n2)=−∑kℓ=n1n2, k≠1f(k)g(ℓ)=−∑k1ℓ1=n1, k2ℓ2=n2, k1k2≠1f(k1)f(k2)g(ℓ1)g(ℓ2)=f(1)f(1)g(n1)g(n2)−∑k1ℓ1=n1, k2ℓ2=n2f(k1)f(k2)g(ℓ1)g(ℓ2)=g(n1)g(n2)−(∑k1ℓ1=n1f(k1)g(ℓ1))(∑k2ℓ2=n2f(k2)g(ℓ2))=g(n1)g(n2)−ε(n1)ε(n2)=g(n1)g(n2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，第二个等号用到了归纳假设，即对于 ℓ1ℓ2 <𝑛1𝑛2ℓ1ℓ2<n1n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 ℓ1 ⟂ℓ2ℓ1⟂ℓ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，条件 𝑔(ℓ1ℓ2) =𝑔(ℓ1)𝑔(ℓ2)g(ℓ1ℓ2)=g(ℓ1)g(ℓ2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．

用抽象代数的语言说，全体积性函数在 Dirichlet 卷积运算下构成 Dirichlet 环乘法群的 [子群](../../algebra/group-theory/#子群)．

更为特殊的是完全积性函数．

定理

设 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数，𝑓,𝑔f,g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是数论函数．那么，有：

  1. 分配律：(𝛼𝑓) ∗(𝛼𝑔) =𝛼 ⋅(𝑓 ∗𝑔)(αf)∗(αg)=α⋅(f∗g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 逆元：(𝛼𝑓)−1 =𝛼𝑓−1(αf)−1=αf−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只要 𝑓−1f−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在．
  3. 积性函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数，当且仅当 𝑓−1 =𝜇𝑓f−1=μf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝜇μ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 [莫比乌斯函数](../mobius/#莫比乌斯函数)．

证明

对于第一条，直接验证可知

((𝛼𝑓)∗(𝛼𝑔))(𝑛)=∑𝑘ℓ=𝑛(𝛼𝑓)(𝑘)(𝛼𝑔)(ℓ)=∑𝑘ℓ=𝑛𝛼(𝑘)𝑓(𝑘)𝛼(ℓ)𝑔(ℓ)=∑𝑘ℓ=𝑛𝛼(𝑛)𝑓(𝑘)𝑔(ℓ)=𝛼(𝑛)(𝑓∗𝑔)(𝑛).((αf)∗(αg))(n)=∑kℓ=n(αf)(k)(αg)(ℓ)=∑kℓ=nα(k)f(k)α(ℓ)g(ℓ)=∑kℓ=nα(n)f(k)g(ℓ)=α(n)(f∗g)(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，第三个等号用到了完全积性函数的性质：𝛼(𝑛) =𝛼(𝑘)𝛼(ℓ)α(n)=α(k)α(ℓ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对所有 𝑛 =𝑘ℓn=kℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．

对于第二条，利用第一条就有

(𝛼𝑓)∗(𝛼𝑓−1)=𝛼(𝑓∗𝑓−1)=𝛼𝜀=𝜀.(αf)∗(αf−1)=α(f∗f−1)=αε=ε.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，最后一个等号只利用了 𝛼(1) =1α(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由逆元定义，(𝛼𝑓)−1 =𝛼𝑓−1(αf)−1=αf−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于第三条，利用第二条和 1−1 =𝜇1−1=μ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知，如果 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数，那么

𝑓−1=(1𝑓)−1=1−1⋅𝑓=𝜇𝑓.f−1=(1f)−1=1−1⋅f=μf.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是常数函数．反过来，如果 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数且 𝑓−1 =𝜇𝑓f−1=μf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么只需要证明对于所有素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑓(𝑝𝑒) =𝑓(𝑝)𝑒f(pe)=f(p)e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立，就能证明 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数．为此，对 𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应用数学归纳法．归纳起点 𝑒 =1e=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处命题显然成立．对于任意 𝑒 >1e>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，应用逆元递推公式，都有

𝑓−1(𝑝𝑒)=−𝑒∑𝑖=1𝑓(𝑝𝑖)𝑓−1(𝑝𝑒−𝑖)=−𝑒∑𝑖=1𝑓(𝑝𝑖)𝜇(𝑝𝑒−𝑖)𝑓(𝑝𝑒−𝑖)=−𝑓(𝑝𝑒)𝑓(1)𝜇(1)−𝑓(𝑝𝑒−1)𝜇(𝑝)𝑓(𝑝)=−𝑓(𝑝𝑒)+𝑓(𝑝)𝑒.f−1(pe)=−∑i=1ef(pi)f−1(pe−i)=−∑i=1ef(pi)μ(pe−i)f(pe−i)=−f(pe)f(1)μ(1)−f(pe−1)μ(p)f(p)=−f(pe)+f(p)e.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，最后一个等号用到了归纳假设 𝑓(𝑝𝑒−1) =𝑓(𝑝)𝑒−1f(pe−1)=f(p)e−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．应用 𝑓−1 =𝜇𝑓f−1=μf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到

𝑓−1(𝑝𝑒)=𝜇(𝑝𝑒)𝑓(𝑝𝑒)=0.f−1(pe)=μ(pe)f(pe)=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入前式，就得到

𝑓(𝑝𝑒)=𝑓(𝑝)𝑒.f(pe)=f(p)e.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，归纳步骤成立．原命题得证．

用抽象代数的语言说，如果 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数，映射 𝑓 ↦𝛼𝑓f↦αf![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Dirichlet 环的 [自同态](../../algebra/ring-theory/#理想)．

## Dirichlet 生成函数

与 Dirichlet 卷积紧密相关的是 Dirichlet 生成函数．

数论函数 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)——也就是数列 {𝑓(𝑛)}{f(n)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)——对应的 **Dirichlet 生成函数** （Dirichlet series generating function，DGF）定义为形式 Dirichlet 级数（formal Dirichlet series）：

𝐹(𝑠)=∞∑𝑛=1𝑓(𝑛)𝑛𝑠.F(s)=∑n=1∞f(n)ns.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

级数中的 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是形式变元．常见的 Dirichlet 生成函数中，𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 往往可以看作是复变量，进而讨论 Dirichlet 级数的解析性质，但这超出了算法竞赛的范围．

Dirichlet 生成函数的乘积对应着相应的数论函数的 Dirichlet 卷积：

定理

对于数论函数 𝑓,𝑔f,g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 及其 Dirichlet 生成函数 𝐹,𝐺F,G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它们的 Dirichlet 卷积 𝑓 ∗𝑔f∗g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成函数等于 𝐹 ⋅𝐺F⋅G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

直接验证：

𝐹(𝑠)𝐺(𝑠)=(∞∑𝑘=1𝑓(𝑘)𝑘𝑠)(∞∑ℓ=1𝑔(ℓ)ℓ𝑠)=∞∑𝑘=1∞∑ℓ=1𝑓(𝑘)𝑔(ℓ)(𝑘ℓ)𝑠=∞∑𝑛=1∑𝑘ℓ=𝑛𝑓(𝑘)𝑔(ℓ)𝑛𝑠=∞∑𝑛=1(𝑓∗𝑔)(𝑛)𝑛𝑠.F(s)G(s)=(∑k=1∞f(k)ks)(∑ℓ=1∞g(ℓ)ℓs)=∑k=1∞∑ℓ=1∞f(k)g(ℓ)(kℓ)s=∑n=1∞∑kℓ=nf(k)g(ℓ)ns=∑n=1∞(f∗g)(n)ns.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用 Dirichlet 卷积和 Dirichlet 生成函数乘积之间的对应关系，可以从 Dirichlet 生成函数的角度理解 Dirichlet 卷积的性质．由于形式 Dirichlet 级数的乘法运算满足交换律、结合律、对加法的分配律，数论函数的 Dirichlet 卷积运算满足同样的代数性质．

### Euler 乘积

积性函数的特殊性同样反映在 Dirichlet 生成函数上．由于整数有 [唯一分解定理](../basic/#算术基本定理)，积性函数 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的生成函数 𝐹(𝑠)F(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可写成如下形式：

𝐹(𝑠)=∞∑𝑛=1𝑓(𝑛)𝑛𝑠=∞∑𝑛=1∏𝑝∈𝐏𝑓(𝑝𝑒)𝑝𝑒𝑠=∏𝑝∈𝐏∞∑𝑒=0𝑓(𝑝𝑒)𝑝𝑒𝑠=∏𝑝∈𝐏(1+𝑓(𝑝)𝑝𝑠+𝑓(𝑝2)𝑝2𝑠+𝑓(𝑝3)𝑝3𝑠+⋯).F(s)=∑n=1∞f(n)ns=∑n=1∞∏p∈Pf(pe)pes=∏p∈P∑e=0∞f(pe)pes=∏p∈P(1+f(p)ps+f(p2)p2s+f(p3)p3s+⋯).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这意味着，𝐹(𝑠)F(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以分解为若干 𝐹𝑝(𝑠)Fp(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘积，且每个 𝐹𝑝(𝑠)Fp(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的数论函数都只在 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次处可能取非零值．这一无穷乘积也称为 **Euler 乘积** （Euler product）．如果 𝐹(𝑠)F(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺(𝑠)G(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都能分解成类似的形式，那么它们的乘积同样如此；将这一观察对应到数论函数上，就是积性函数的 Dirichlet 卷积仍然是积性函数．

进一步地，如果 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还是完全积性函数，那么 𝑓(𝑝𝑒) =𝑓(𝑝)𝑒f(pe)=f(p)e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，上式可以继续简化：

𝐹(𝑠)=∏𝑝∈𝐏∞∑𝑒=0𝑓(𝑝)𝑒𝑝𝑒𝑠=∏𝑝∈𝐏(1−𝑓(𝑝)𝑝𝑠)−1.F(s)=∏p∈P∑e=0∞f(p)epes=∏p∈P(1−f(p)ps)−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

与积性函数不同，完全积性函数的 Dirichlet 生成函数的形式在乘法运算下并不具有封闭性，因此，完全积性函数的 Dirichlet 卷积和 Dirichlet 逆都未必是完全积性函数，但一定是积性函数．

例子

  1. 单位函数 𝜀(𝑛)ε(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数．它的 Dirichlet 生成函数是关于不定元 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的常值函数

𝐸(𝑠)=∞∑𝑛=1𝜀(𝑛)𝑛𝑠=1.E(s)=∑n=1∞ε(n)ns=1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 常数函数 1(𝑛)1(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数．它的 Dirichlet 生成函数是 Riemann 函数

𝐼(𝑠)=∞∑𝑛=11𝑛𝑠=∏𝑝∈𝐏11−𝑝−𝑠=𝜁(𝑠).I(s)=∑n=1∞1ns=∏p∈P11−p−s=ζ(s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. 莫比乌斯函数 𝜇(𝑛)μ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是常数函数的 Dirichlet 逆．它的 Dirichlet 生成函数是 𝜁(𝑠)ζ(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倒数：

𝑀(𝑠)=∞∑𝑛=1𝜇(𝑛)𝑛𝑠=∏𝑝∈𝐏(1−𝑝−𝑠)=1𝜁(𝑠).M(s)=∑n=1∞μ(n)ns=∏p∈P(1−p−s)=1ζ(s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. 幂函数 id𝑘⁡(𝑛) =𝑛𝑘idk⁡(n)=nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数．特别地，当 𝑘 =0k=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，它就是常数函数；当 𝑘 =1k=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，它就是恒等函数．它的 Dirichlet 生成函数是

𝐼𝑘(𝑠)=∞∑𝑛=1𝑛𝑘𝑛𝑠=∏𝑝∈𝐏11−𝑝𝑘−𝑠=𝜁(𝑠−𝑘).Ik(s)=∑n=1∞nkns=∏p∈P11−pk−s=ζ(s−k).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  5. 欧拉函数 𝜑(𝑛)φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数．它的 Dirichlet 生成函数是

Φ(𝑠)=∏𝑝∈𝐏(1+𝑝−1𝑝𝑠+𝑝(𝑝−1)𝑝2𝑠+𝑝2(𝑝−1)𝑝3𝑠+⋯)=∏𝑝∈𝐏(11−𝑝1−𝑠−1𝑝𝑠11−𝑝1−𝑠)=∏𝑝∈𝐏1−𝑝−𝑠1−𝑝1−𝑠=𝜁(𝑠−1)𝜁(𝑠).Φ(s)=∏p∈P(1+p−1ps+p(p−1)p2s+p2(p−1)p3s+⋯)=∏p∈P(11−p1−s−1ps11−p1−s)=∏p∈P1−p−s1−p1−s=ζ(s−1)ζ(s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

结合幂函数的 Dirichlet 函数表达式，就得到 id =𝜑 ∗1id=φ∗1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  6. 约数函数 𝜎𝑘(𝑛) =∑𝑑∣𝑛𝑑𝑘σk(n)=∑d∣ndk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数．它的 Dirichlet 生成函数是

Σ𝑘(𝑠)=∏𝑝∈𝐏(1+1+𝑝𝑘𝑝𝑠+1+𝑝𝑘+𝑝2𝑘𝑝2𝑠+1+𝑝𝑘+𝑝2𝑘+𝑝3𝑘𝑝3𝑠+⋯)=∏𝑝∈𝐏11−𝑝𝑘((1−𝑝𝑘)+1−𝑝2𝑘𝑝𝑠+1−𝑝3𝑘𝑝2𝑠+1−𝑝4𝑘𝑝3𝑘+⋯)=∏𝑝∈𝐏11−𝑝𝑘(11−𝑝−𝑠−𝑝𝑘1−𝑝𝑘−𝑠)=∏𝑝∈𝐏1(1−𝑝−𝑠)(1−𝑝𝑘−𝑠)=𝜁(𝑠−𝑘)𝜁(𝑠).Σk(s)=∏p∈P(1+1+pkps+1+pk+p2kp2s+1+pk+p2k+p3kp3s+⋯)=∏p∈P11−pk((1−pk)+1−p2kps+1−p3kp2s+1−p4kp3k+⋯)=∏p∈P11−pk(11−p−s−pk1−pk−s)=∏p∈P1(1−p−s)(1−pk−s)=ζ(s−k)ζ(s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

结合幂函数的 Dirichlet 表达式，就得到 𝜎𝑘 =id𝑘 ∗1σk=idk∗1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这正是 𝜎𝑘σk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义式．

  7. 无平方因子数的指示函数 𝑢(𝑛) =|𝜇(𝑛)|u(n)=|μ(n)|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数．它的 Dirichlet 生成函数是

𝑈(𝑠)=∏𝑝∈𝐏(1+𝑝−𝑠)=∏𝑝∈𝐏1−𝑝−2𝑠1−𝑝−𝑠=𝜁(𝑠)𝜁(2𝑠).U(s)=∏p∈P(1+p−s)=∏p∈P1−p−2s1−p−s=ζ(s)ζ(2s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 应用

Dirichlet 生成函数可以用于将积性函数表示为 Dirichlet 卷积．

例如在杜教筛的过程中，要计算积性函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和，需要找到另一个积性函数 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑓 ∗𝑔f∗g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以快速求前缀和．可以利用 Dirichlet 生成函数推导这一过程．

以杜教筛一节的例题 [Luogu P3768 简单的数学题](../du/#问题二) 为例，需要对 𝑓(𝑛) =𝑛2𝜑(𝑛)f(n)=n2φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构造满足上述条件的数论函数 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数，它的 Dirichlet 生成函数为

𝐹(𝑠)=∏𝑝∈𝐏(1+∞∑𝑘=1𝑝3𝑘−1(𝑝−1)𝑝𝑘𝑠)=∏𝑝∈𝐏1−𝑝2−𝑠1−𝑝3−𝑠=𝜁(𝑠−3)𝜁(𝑠−2).F(s)=∏p∈P(1+∑k=1∞p3k−1(p−1)pks)=∏p∈P1−p2−s1−p3−s=ζ(s−3)ζ(s−2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对比幂函数的 Dirichlet 生成函数可知，只要取 𝑔 =id2g=id2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有 𝑓 ∗𝑔 =id3f∗g=id3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．两者都是可以快速计算前缀和的．

## Dirichlet 卷积的计算

本节讨论 Dirichlet 卷积的计算问题，即给定序列 {𝑓(𝑘)}𝑛𝑘=1{f(k)}k=1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 {𝑔(𝑘)}𝑛𝑘=1{g(k)}k=1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求解 Dirichlet 卷积 ℎ =𝑓 ∗𝑔h=f∗g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前若干项 {ℎ(𝑘)}𝑛𝑘=1{h(k)}k=1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题．根据涉及到的函数性质，算法的复杂度也略有不同．

### 一般情形

如果 𝑓,𝑔,ℎf,g,h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都没有特殊性质，那么 Dirichlet 卷积的计算只能利用其定义：

ℎ(𝑛)=∑𝑘ℓ=𝑛𝑓(𝑘)𝑔(ℓ).h(n)=∑kℓ=nf(k)g(ℓ).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

枚举 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ℓℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将贡献 𝑓(𝑘)𝑔(ℓ)f(k)g(ℓ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 累加到 ℎ(𝑘ℓ)h(kℓ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上即可．枚举复杂度为

𝑂(𝑛∑𝑘=1𝑛𝑘)=𝑂(𝑛log⁡𝑛).O(∑k=1nnk)=O(nlog⁡n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text // Compute the Dirichlet convolution h = f * g. auto dirichlet_convolute ( const std :: vector < int >& f , const std :: vector < int >& g ) { int n = f . size () \- 1 ; std :: vector < int > h ( n \+ 1 ); for ( int k = 1 ; k <= n ; ++ k ) { for ( int d = 1 ; k * d <= n ; ++ d ) { h [ k * d ] += f [ k ] * g [ d ]; } } return h ; } ```   
---|---  
  
### 与积性函数卷积的情形

如果 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数，那么可以利用 Euler 乘积加速 Dirichlet 卷积的计算．计算 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相当于计算它的 Dirichlet 生成函数 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中各项的系数．由于

𝐻(𝑠)=𝐹(𝑠)𝐺(𝑠)=𝐹(𝑠)∏𝑝∈𝐏𝐺𝑝(𝑠).H(s)=F(s)G(s)=F(s)∏p∈PGp(s).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝐺𝑝(𝑠)Gp(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐺(𝑠)G(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Euler 乘积分解中的因式，它只包含 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次处的系数：

𝐺𝑝(𝑠)=∑𝑝𝑘≤𝑛𝑓(𝑝𝑘)𝑝𝑘𝑠=1+𝑓(𝑝)𝑝𝑠+𝑓(𝑝2)𝑝2𝑠+⋯.Gp(s)=∑pk≤nf(pk)pks=1+f(p)ps+f(p2)p2s+⋯.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么，从 𝐹(𝑠)F(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始，遍历所有不超过 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将 𝐺𝑝(𝑠)Gp(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 逐一乘上去，同样可以得到最终结果 𝐻(𝑠)H(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．将 𝐺𝑝(𝑠)Gp(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘上去时，直接应用一般情形中的暴力枚举算法即可．总枚举次数

∑𝑝∈𝐏, 𝑝≤𝑛∞∑𝑘=1⌊𝑛𝑝𝑘⌋≤∑𝑝∈𝐏, 𝑝≤𝑛𝑛𝑝−1≤∑𝑝∈𝐏, 𝑝≤𝑛2𝑛𝑝∈𝑂(𝑛log⁡log⁡𝑛).∑p∈P, p≤n∑k=1∞⌊npk⌋≤∑p∈P, p≤nnp−1≤∑p∈P, p≤n2np∈O(nlog⁡log⁡n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最后一步复杂度的估计与 [Eratosthenes 筛法](../sieve/#埃拉托斯特尼筛法) 复杂度的证明一致．所以，本算法的时间复杂度为 𝑂(𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text // Compute the Dirichlet convolution h = f * g. // Assume that g is multiplicative. auto dirichlet_convolute ( const std :: vector < int >& f , const std :: vector < int >& g ) { int n = f . size () \- 1 ; std :: vector < int > h ( f ); std :: vector < bool > vis ( n \+ 1 ); for ( int i = 2 ; i <= n ; ++ i ) { if ( vis [ i ]) continue ; // Reverse the order for in-place computation. for ( int k = n / i * i ; k ; k -= i ) { vis [ k ] = true ; int d = k ; while ( true ) { d /= i ; h [ k ] += h [ d ] * g [ k / d ]; if ( d % i ) break ; } } } return h ; } ```   
---|---  
  
特别地，当积性函数 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数或其 Dirichlet 逆时，例如当 𝑔 =1g=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑔 =𝜇g=μ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，那么算法可以进一步简化．此时，Dirichlet 卷积 ℎ =𝑓 ∗𝑔h=f∗g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算可以采用常数更小的 [Dirichlet 前缀和/差分](../mobius/#dirichlet-前缀和) 算法，但是算法时间复杂度仍为 𝑂(𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 结果为积性函数的情形

最后，考虑 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数的情形．特别地，当 𝑓,𝑔f,g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是积性函数时，ℎ =𝑓 ∗𝑔h=f∗g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是积性函数．要计算 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只需要确定它在素数幂处的取值，就可以通过 [线性筛](../sieve/#线性筛法) 在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算．而对于素数幂 𝑝𝑒pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的取值 ℎ(𝑝𝑒)h(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 直接暴力计算即可：

ℎ(𝑝𝑒)=𝑒∑𝑖=0𝑓(𝑝𝑖)𝑔(𝑝𝑒−𝑖).h(pe)=∑i=0ef(pi)g(pe−i).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这些暴力计算需要的枚举次数为

∑𝑝∈𝐏, 𝑝≤𝑛⌊log𝑝⁡𝑛⌋∑𝑒=1(𝑒+1)≤∑𝑝∈𝐏, 𝑝≤√𝑛⌊log𝑝⁡𝑛⌋2+∑𝑝∈𝐏, √𝑛<𝑝≤𝑛1≤√𝑛(log2⁡𝑛)2+𝑛∈𝑂(𝑛).∑p∈P, p≤n∑e=1⌊logp⁡n⌋(e+1)≤∑p∈P, p≤n⌊logp⁡n⌋2+∑p∈P, n<p≤n1≤n(log2⁡n)2+n∈O(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，这一算法的总时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 ``` |  ```text // Compute the Dirichlet convolution h = f * g. // Assume that h is multiplicative. auto dirichlet_convolute ( const std :: vector < int >& f , const std :: vector < int >& g ) { int n = f . size () \- 1 ; std :: vector < int > h ( n \+ 1 ), primes , rem ( n \+ 1 ), lpf ( n \+ 1 ); std :: vector < bool > vis ( n \+ 1 ); h [ 1 ] = 1 ; for ( int x = 2 ; x <= n ; ++ x ) { if ( ! vis [ x ]) { primes . push_back ( x ); rem [ x ] = 1 ; lpf [ x ] = x ; } for ( int p : primes ) { if ( x * p > n ) break ; vis [ x * p ] = true ; rem [ x * p ] = x % p ? x : rem [ x ]; lpf [ x * p ] = p ; if ( x % p == 0 ) break ; } if ( rem [ x ] == 1 ) { // prime powers. for ( int k = x ; k ; k /= lpf [ x ]) { h [ x ] += f [ k ] * g [ x / k ]; } } else { // other cases. h [ x ] = h [ rem [ x ]] * h [ x / rem [ x ]]; } } return h ; } ```   
---|---  
  
## 参考资料与注释

  * [Dirichlet convolution - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_convolution)
  * [Dirichlet series - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_series)
  * [Euler product - Wikipedia](https://en.wikipedia.org/wiki/Euler_product)
  * [Dirichlet 積と、数論関数の累積和 by maspy](https://maspypy.com/dirichlet-%e7%a9%8d%e3%81%a8%e3%80%81%e6%95%b0%e8%ab%96%e9%96%a2%e6%95%b0%e3%81%ae%e7%b4%af%e7%a9%8d%e5%92%8c)

* * *

>  __本页面最近更新： 2026/3/25 15:00:02，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/dirichlet.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/dirichlet.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [billchenchina](https://github.com/billchenchina), [CCXXXI](https://github.com/CCXXXI), [danielqfmai](https://github.com/danielqfmai), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [lychees](https://github.com/lychees), [Menci](https://github.com/Menci), [Nanarikom](https://github.com/Nanarikom), [ouuan](https://github.com/ouuan), [shuzhouliu](https://github.com/shuzhouliu), [sshwy](https://github.com/sshwy)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
