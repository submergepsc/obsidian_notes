# 阶 & 原根 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/primitive-root/

# 阶 & 原根

前置知识：[费马小定理](../fermat/#费马小定理)、[欧拉定理](../fermat/#欧拉定理)、[拉格朗日定理](../congruence-equation/#定理-3lagrange-定理)

阶和原根，是理解模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) [既约剩余系](../basic/#同余类与剩余系) 𝐙∗𝑚Zm∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘法结构的重要工具．基于此，可以定义 [离散对数](../discrete-logarithm/) 等概念．更为一般的讨论可以参见抽象代数部分 [群论](../../algebra/group-theory/#阶) 和 [环论](../../algebra/ring-theory/#应用整数同余类的乘法群) 等页面相关章节．

## 阶

本节中，总是假设模数 𝑚 ∈𝐍+m∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和底数 𝑎 ∈𝐙a∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素，即 (𝑎,𝑚) =1(a,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也记作 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于 𝑛 ∈𝐙n∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，幂次 𝑎𝑛mod𝑚anmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 呈现一种循环结构．这个循环节的最小长度，就是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶．阶就定义为幂 𝑎𝑛mod𝑚anmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 第一次回到起点 𝑎0mod𝑚 =1a0modm=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时的指数：

阶

对于 𝑎 ∈𝐙,𝑚 ∈𝐍+a∈Z,m∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足同余式 𝑎𝑛 ≡1(mod𝑚)an≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称作 **𝑎 a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶**（the order of 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) modulo 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），记作 𝛿𝑚(𝑎)δm(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 ord𝑚⁡(𝑎)ordm⁡(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注

在 [抽象代数](../../algebra/group-theory/#阶) 中，这里的「阶」就是模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既约剩余系关于乘法形成的群中，元素 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶．用记号 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示阶只适用于这个特殊的群．下面的诸多性质可以直接推广到抽象代数中群元素的阶的性质．

另外还有「半阶」的概念，在数论中会用 𝛿−δ−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记号表示．它是满足同余式 𝑎𝑛 ≡ −1(mod𝑚)an≡−1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小正整数．半阶不是群论中的概念．阶一定存在，半阶不一定存在．

### 幂的循环结构

利用阶，可以刻画幂的循环结构．对于幂 𝑎𝑛mod𝑚anmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以将指数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对阶 𝛿𝑚(𝑎)δm(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做带余除法：

𝑛=𝛿𝑚(𝑎)𝑞+𝑟, 0≤𝑟<𝛿𝑚(𝑎).n=δm(a)q+r, 0≤r<δm(a).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而，利用幂的运算律，就得到

𝑎𝑛=𝑎𝛿𝑚(𝑎)𝑞+𝑟=(𝑎𝛿𝑚(𝑎))𝑞⋅𝑎𝑟≡𝑎𝑟(mod𝑚).an=aδm(a)q+r=(aδm(a))q⋅ar≡ar(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这说明，对于任意指数的幂，可以将它平移到第一个非负的循环节．由此，可以得到一系列关于阶的性质．

性质 1

对于 𝑎 ∈𝐙,𝑚 ∈𝐍+a∈Z,m∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，幂次 𝑎0( =1),𝑎,𝑎2,⋯,𝑎𝛿𝑚(𝑎)−1a0(=1),a,a2,⋯,aδm(a)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两不同余．

证明

考虑反证．假设存在两个数 0 ≤𝑖 <𝑗 <𝛿𝑚(𝑎)0≤i<j<δm(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑎𝑖 ≡𝑎𝑗(mod𝑚)ai≡aj(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有 𝑎𝑗−𝑖 ≡1(mod𝑚)aj−i≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，0 <𝑗 −𝑖 <𝛿𝑚(𝑎)0<j−i<δm(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这与阶的最小性矛盾，故原命题成立．

性质 2

对于 𝑎,𝑛 ∈𝐙,𝑚 ∈𝐍+a,n∈Z,m∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，同余关系 𝑎𝑛 ≡1(mod𝑚)an≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立，当且仅当 𝛿𝑚(𝑎) ∣𝑛δm(a)∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

如前文所述，𝑎𝑛 ≡𝑎𝑛mod𝛿𝑚(𝑎)(mod𝑚)an≡anmodδm(a)(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由 性质 1 可知，0 ≤𝑟 <𝛿𝑚(𝑎)0≤r<δm(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中唯一一个使得 𝑎𝑟 ≡1(mod𝑚)ar≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立的 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 𝑟 =0r=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，𝑎𝑛 ≡1(mod𝑚)an≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当 𝑛mod𝛿𝑚(𝑎) =0nmodδm(a)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是 𝛿𝑚(𝑎) ∣𝑛δm(a)∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

[欧拉定理](../fermat/#欧拉定理) 中，同余关系 𝑎𝜑(𝑚) ≡1(mod𝑚)aφ(m)≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．结合 性质 2，这说明对于所有 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝛿𝑚(𝑎) ∣𝜑(𝑚)δm(a)∣φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．换句话说，𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是所有 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶的一个公倍数．对于一个正整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所有 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶 𝛿𝑚(𝑎)δm(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小公倍数，记作 𝜆(𝑚)λ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就是 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Carmichael 函数．后文会详细讨论它的性质．

和其他的循环结构类似，可以根据 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶计算 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶．

性质 3

对于 𝑘,𝑎 ∈𝐙,𝑚 ∈𝐍+k,a∈Z,m∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝛿𝑚(𝑎𝑘)=𝛿𝑚(𝑎)(𝛿𝑚(𝑎),𝑘).δm(ak)=δm(a)(δm(a),k).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

由 性质 2，同余关系 (𝑎𝑘)𝑛 =𝑎𝑘𝑛 ≡1(mod𝑚)(ak)n=akn≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立，当且仅当 𝛿𝑚(𝑎) ∣𝑘𝑛δm(a)∣kn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这一条件就等价于

𝛿𝑚(𝑎)(𝛿𝑚(𝑎),𝑘)∣𝑛.δm(a)(δm(a),k)∣n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

使得这一条件成立的最小正整数就是

𝛿𝑚(𝑎𝑘)=𝛿𝑚(𝑎)(𝛿𝑚(𝑎),𝑘).δm(ak)=δm(a)(δm(a),k).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 乘积的阶

设 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素的不同整数．如果已知阶 𝛿𝑚(𝑎)δm(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛿𝑚(𝑏)δm(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，同样可以获得一些关于它们乘积 𝑎𝑏ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶 𝛿𝑚(𝑎𝑏)δm(ab)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的信息．

性质 4

对于 𝑎,𝑏 ∈𝐙,𝑚 ∈𝐍+a,b∈Z,m∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎,𝑏 ⟂𝑚a,b⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，有

[𝛿𝑚(𝑎),𝛿𝑚(𝑏)](𝛿𝑚(𝑎),𝛿𝑚(𝑏))∣𝛿𝑚(𝑎𝑏)∣[𝛿𝑚(𝑎),𝛿𝑚(𝑏)].[δm(a),δm(b)](δm(a),δm(b))∣δm(ab)∣[δm(a),δm(b)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

因为 [𝛿𝑚(𝑎),𝛿𝑚(𝑏)][δm(a),δm(b)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝛿𝑚(𝑎)δm(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛿𝑚(𝑏)δm(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数，所以，由 性质 2 可知

(𝑎𝑏)[𝛿𝑚(𝑎),𝛿𝑚(𝑏)]=𝑎[𝛿𝑚(𝑎),𝛿𝑚(𝑏)]𝑏[𝛿𝑚(𝑎),𝛿𝑚(𝑏)]≡1(mod𝑚).(ab)[δm(a),δm(b)]=a[δm(a),δm(b)]b[δm(a),δm(b)]≡1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再次应用性质 2，就得到

𝛿𝑚(𝑎𝑏)∣[𝛿𝑚(𝑎),𝛿𝑚(𝑏)].δm(ab)∣[δm(a),δm(b)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就得到右侧的整除关系．

反过来，由于

1≡(𝑎𝑏)𝛿𝑚(𝑎𝑏)𝛿𝑚(𝑏)≡𝑎𝛿𝑚(𝑎𝑏)𝛿𝑚(𝑏)(mod𝑚),1≡(ab)δm(ab)δm(b)≡aδm(ab)δm(b)(modm),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，应用性质 2，就得到 𝛿𝑚(𝑎) ∣𝛿𝑚(𝑎𝑏)𝛿𝑚(𝑏)δm(a)∣δm(ab)δm(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．两侧消去 (𝛿𝑚(𝑎),𝛿𝑚(𝑏))(δm(a),δm(b))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到

𝛿𝑚(𝑎)(𝛿𝑚(𝑎),𝛿𝑚(𝑏))∣𝛿𝑚(𝑎𝑏)𝛿𝑚(𝑏)(𝛿𝑚(𝑎),𝛿𝑚(𝑏)).δm(a)(δm(a),δm(b))∣δm(ab)δm(b)(δm(a),δm(b)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

消去公因子后，两个分式互素，这就得到

𝛿𝑚(𝑎)(𝛿𝑚(𝑎),𝛿𝑚(𝑏))∣𝛿𝑚(𝑎𝑏).δm(a)(δm(a),δm(b))∣δm(ab).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

同理，也有

𝛿𝑚(𝑏)(𝛿𝑚(𝑎),𝛿𝑚(𝑏))∣𝛿𝑚(𝑎𝑏).δm(b)(δm(a),δm(b))∣δm(ab).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于两个整除关系的左侧互素，有

[𝛿𝑚(𝑎),𝛿𝑚(𝑏)](𝛿𝑚(𝑎),𝛿𝑚(𝑏))=𝛿𝑚(𝑎)𝛿𝑚(𝑏)(𝛿𝑚(𝑎),𝛿𝑚(𝑏))2∣𝛿𝑚(𝑎𝑏).[δm(a),δm(b)](δm(a),δm(b))=δm(a)δm(b)(δm(a),δm(b))2∣δm(ab).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就得到左侧的整除关系．

对于 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶互素的情形，这一结论有着更为简单的形式．

性质 4'

对于 𝑎,𝑏 ∈𝐙,𝑚 ∈𝐍+a,b∈Z,m∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎,𝑏 ⟂𝑚a,b⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，有

𝛿𝑚(𝑎𝑏)=𝛿𝑚(𝑎)𝛿𝑚(𝑏)⟺𝛿𝑚(𝑎)⟂𝛿𝑚(𝑏).δm(ab)=δm(a)δm(b)⟺δm(a)⟂δm(b).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

如果 𝛿𝑚(𝑎) ⟂𝛿𝑚(𝑏)δm(a)⟂δm(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 性质 4 中所有整除关系都是等式，所以有

𝛿𝑚(𝑎𝑏)=[𝛿𝑚(𝑎),𝛿𝑚(𝑏)]=𝛿𝑚(𝑎)𝛿𝑚(𝑏).δm(ab)=[δm(a),δm(b)]=δm(a)δm(b).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

反过来，如果 𝛿𝑚(𝑎𝑏) =𝛿𝑚(𝑎)𝛿𝑚(𝑏)δm(ab)=δm(a)δm(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么根据性质 4，就有

𝛿𝑚(𝑎)𝛿𝑚(𝑏)=𝛿𝑚(𝑎𝑏)∣[𝛿𝑚(𝑎),𝛿𝑚(𝑏)].δm(a)δm(b)=δm(ab)∣[δm(a),δm(b)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这立马说明 (𝛿𝑚(𝑎),𝛿𝑚(𝑏)) =1(δm(a),δm(b))=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝛿𝑚(𝑎) ⟂𝛿𝑚(𝑏)δm(a)⟂δm(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

一般情形中，性质 4 得到的界已经是紧的．乘积的阶取得下界的情形很容易构造：例如 (𝑎,𝑏,𝑚) =(3,5,7)(a,b,m)=(3,5,7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝛿𝑚(𝑎) =𝛿𝑚(𝑏) =6δm(a)=δm(b)=6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是它们的乘积的阶 𝛿𝑚(𝑎𝑏) =1δm(ab)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

尽管一般情形中，乘积 𝑎𝑏ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶未必是它们的阶的最小公倍数，但是总能找到一个元素使得它的阶等于这个最小公倍数．

性质 5

对于 𝑎,𝑏 ∈𝐙,𝑚 ∈𝐍+a,b∈Z,m∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎,𝑏 ⟂𝑚a,b⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，总是存在 𝑐 ∈𝐙c∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑐 ⟂𝑚c⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝛿𝑚(𝑐)=[𝛿𝑚(𝑎),𝛿𝑚(𝑏)].δm(c)=[δm(a),δm(b)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

考虑素因数分解：

𝛿𝑚(𝑎)=∏𝑝𝑝𝛼𝑝, 𝛿𝑚(𝑏)=∏𝑝𝑝𝛽𝑝.δm(a)=∏ppαp, δm(b)=∏ppβp.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用 𝛼𝑝αp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛽𝑝βp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小关系，可以将所有素因子分为两类：

𝐴={𝑝:𝛼𝑝≥𝛽𝑝}, 𝐵={𝑝:𝛼𝑝<𝛽𝑝}.A={p:αp≥βp}, B={p:αp<βp}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由此，分别设

𝛾𝐴=∏𝑝∈𝐴𝑝𝛼𝑝, 𝛾𝐵=∏𝑝∈𝐵𝑝𝛼𝑝, 𝜂𝐴=∏𝑝∈𝐴𝑝𝛽𝑝, 𝜂𝐵=∏𝑝∈𝐵𝑝𝛽𝑝,γA=∏p∈Apαp, γB=∏p∈Bpαp, ηA=∏p∈Apβp, ηB=∏p∈Bpβp,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就有 𝛿𝑚(𝑎) =𝛾𝐴𝛾𝐵δm(a)=γAγB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝛿𝑚(𝑏) =𝜂𝐴𝜂𝐵δm(b)=ηAηB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据 性质 3，可知

𝛿𝑚(𝑎𝛾𝐵)=𝛿𝑚(𝑎)(𝛿𝑚(𝑎),𝛾𝐵)=𝛿𝑚(𝑎)𝛾𝐵=𝛾𝐴,𝛿𝑚(𝑏𝜂𝐴)=𝛿𝑚(𝑏)(𝛿𝑚(𝑏),𝜂𝐴)=𝛿𝑚(𝑏)𝜂𝐴=𝜂𝐵.δm(aγB)=δm(a)(δm(a),γB)=δm(a)γB=γA,δm(bηA)=δm(b)(δm(b),ηA)=δm(b)ηA=ηB.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝛾𝐴 ⟂𝜂𝐵γA⟂ηB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 性质 4'，就有

𝛿𝑚(𝑎𝛾𝐵𝑏𝜂𝐴)=𝛾𝐴𝜂𝐵=∏𝑝𝑝max{𝛼𝑝,𝛽𝑝}=[𝛿𝑚(𝑎),𝛿𝑚(𝑏)].δm(aγBbηA)=γAηB=∏ppmax{αp,βp}=[δm(a),δm(b)].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，𝑐 =𝑎𝛾𝐵𝑏𝜂𝐴c=aγBbηA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是阶为 [𝛿𝑚(𝑎),𝛿𝑚(𝑏)][δm(a),δm(b)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素．

这一结论常用于构造出指定阶的元素．

## 原根

原根是一些特殊元素——它的阶就等于所有模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既约剩余系的个数．

原根

对于 𝑚 ∈𝐍+m∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果存在 𝑔 ∈𝐙g∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑔 ⟂𝑚g⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝛿𝑚(𝑔) =|𝐙∗𝑚| =𝜑(𝑚)δm(g)=|Zm∗|=φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就称 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根**（primitive root modulo 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．其中，𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 [欧拉函数](../euler-totient/)．

并非所有正整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都存在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根．由上文的 性质 1，如果模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在，那么，𝑔,𝑔2,⋯,𝑔𝜑(𝑚)g,g2,⋯,gφ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在的同余类互不相同，构成模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既约剩余系．特别地，对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，余数 𝑔𝑖mod𝑝gimodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于 𝑖 =1,2,⋯,𝑝 −1i=1,2,⋯,p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两不同．

注

在 [抽象代数](../../algebra/ring-theory/#应用整数同余类的乘法群) 中，原根就是循环群的生成元．这个概念只在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既约剩余系关于乘法形成的群中有「原根」这个名字，在一般的循环群中都称作「生成元」．并非每个模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既约剩余系关于乘法形成的群都是循环群，存在原根就表明它同构于循环群，如果不存在原根就表明不同构．

模为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，模 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整数乘法群就是 {0}{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这显然是循环群，所以原根就是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 原根判定定理

如果已知模数 𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体素因子，那么很容易判断模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根是否存在．

定理

对于整数 𝑚 ≥3m≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔 ⟂𝑚g⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根，当且仅当对于 𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每个素因数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有

𝑔𝜑(𝑚)𝑝≢1(mod𝑚).gφ(m)p≢1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

必要性显然．为证明充分性，考虑使用反证法．如果 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根，那么一定有 𝛿𝑚(𝑔) <𝜑(𝑚)δm(g)<φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由 性质 2 和欧拉定理可知，𝛿𝑚(𝑔) ∣𝜑(𝑚)δm(g)∣φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，设 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝜑(𝑚)𝛿𝑚(𝑔)φ(m)δm(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个素因子，就有 𝛿𝑚(𝑔) ∣𝜑(𝑚)𝑝δm(g)∣φ(m)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．再次应用性质 2 就得到

𝑔𝜑(𝑚)𝑝≡1(mod𝑚).gφ(m)p≡1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但是，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是 𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个因子，这就与题设条件矛盾．由此，原命题的充分性成立．

### 原根个数

原根如果存在，也未必唯一．一般地，对于模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既约剩余系中所有元素可能的阶和某个阶的元素数量，有如下结论：

定理

如果正整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有原根 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，当且仅当 𝑑 ∣𝜑(𝑚)d∣φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶元素存在，且恰有 𝜑(𝑑)φ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．特别地，模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根个数为 𝜑(𝜑(𝑚))φ(φ(m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

根据原根的定义，所有模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的既约同余类都可以写作 𝑔𝑘mod𝑚gkmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，且 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 1,2,⋯,𝜑(𝑚)1,2,⋯,φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之一．由 性质 3，这些元素的阶等于

𝛿𝑚(𝑔𝑘)=𝜑(𝑚)(𝜑(𝑚),𝑘).δm(gk)=φ(m)(φ(m),k).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶元素存在，当且仅当 𝑑 ∣𝜑(𝑚)d∣φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．而且，对于 𝑑 ∣𝜑(𝑚)d∣φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝑑′ =𝜑(𝑚)/𝑑d′=φ(m)/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这些元素的集合就是

𝐴={𝑔𝑘:(𝜑(𝑚),𝑘)=𝑑′, 1≤𝑘≤𝜑(𝑚)}={𝑔𝑘:𝑑′∣𝑘, (𝑑,𝑘/𝑑′)=1, 1≤𝑘/𝑑′≤𝑑}.A={gk:(φ(m),k)=d′, 1≤k≤φ(m)}={gk:d′∣k, (d,k/d′)=1, 1≤k/d′≤d}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这些元素对应的 𝑘′ =𝑘/𝑑′k′=k/d′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 恰为那些不超过 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且与 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素的正整数．由欧拉函数的定义，这就是 𝜑(𝑑)φ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 原根存在定理

本节将建立如下原根存在定理：

定理

模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根存在，当且仅当 𝑚 =1,2,4,𝑝𝑒,2𝑝𝑒m=1,2,4,pe,2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇素数且 𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

为说明这一结论，需要分别讨论如下四种情形：

  1. 𝑚 =1,2,4m=1,2,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，原根分别是 𝑔 =0,1,3g=0,1,3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然存在．

  2. 𝑚 =𝑝𝑒m=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇素数的幂，其中，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为奇素数，𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

引理 1

对于奇素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根存在．

证明

证明分为两步．

**第一步** ：对于 𝑑 ∣(𝑝 −1)d∣(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，同余方程 𝑥𝑑 ≡1(mod𝑝)xd≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 恰有 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个互不相同的解．

令 𝑝 −1 =𝑘𝑑p−1=kd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，多项式

𝑓(𝑥)=𝑥𝑑(𝑘−1)+𝑥𝑑(𝑘−2)+⋯+𝑥𝑑+1.f(x)=xd(k−1)+xd(k−2)+⋯+xd+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据 [欧拉定理](../fermat/#欧拉定理)，同余方程 (𝑥𝑑 −1)𝑓(𝑥) =𝑥𝑝−1 −1 ≡0(mod𝑝)(xd−1)f(x)=xp−1−1≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 恰有 𝑝 −1p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个互不相同的解．这些解分别是 𝑥𝑑 −1xd−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的零点．由 [Lagrange 定理](../congruence-equation/#定理-3lagrange-定理)，它们分别至多只能有 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个和 𝑑(𝑘 −1)d(k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个互不相同的零点．由于 𝑑 +𝑑(𝑘 −1) =𝑝 −1d+d(k−1)=p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，前者只能恰好有 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个互不相同的零点．这说明同余方程 𝑥𝑑 ≡1(mod𝑝)xd≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 恰有 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个互不相同的解．

**第二步** ：对于 𝑑 ∣(𝑝 −1)d∣(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶元素恰好有 𝜑(𝑑)φ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．

对于 𝜑(𝑝)φ(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有因子排序，然后应用归纳法．因为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶元素只能是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只有一个，归纳起点成立．对于 𝑑 ∣(𝑝 −1)d∣(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据前文的 性质 2，同余方程 𝑥𝑑 ≡1(mod𝑝)xd≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解一定满足 𝛿𝑝(𝑥) ∣𝑑δp(x)∣d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，其中 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶元素个数为

𝑁(𝑑)=𝑑−∑𝑒∣𝑑, 𝑒≠𝑑𝑁(𝑒)=𝑑−∑𝑒∣𝑑, 𝑒≠𝑑𝜑(𝑒)=𝜑(𝑑).N(d)=d−∑e∣d, e≠dN(e)=d−∑e∣d, e≠dφ(e)=φ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

第二个等号是归纳假设，第三个等号是欧拉函数的性质．由数学归纳法，就知道对于所有 𝑑 ∣(𝑝 −1)d∣(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都恰有 𝜑(𝑑)φ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶元素．

特别地，对于 𝑑 =𝑝 −1d=p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，恰有 𝜑(𝑝 −1)φ(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 (𝑝 −1)(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶元素．因此，模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根存在．

引理 2

对于奇素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，模 𝑝𝑒pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根存在．

证明

证明分为三步．

**第一步** ：存在模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑔𝑝−1 ≢1(mod𝑝2)gp−1≢1(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

任取一个模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果它不符合条件，即 𝑔𝑝−1 ≡1(mod𝑝2)gp−1≡1(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，可以证明 𝑔 +𝑝g+p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符合条件：𝑔 +𝑝g+p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根，且

(𝑔+𝑝)𝑝−1≡(𝑝−10)𝑔𝑝−1+(𝑝−11)𝑔𝑝−2𝑝=𝑔𝑝−1+𝑔𝑝−2𝑝(𝑝−1)≡1−𝑝𝑔𝑝−2≢1(mod𝑝2).(g+p)p−1≡(p−10)gp−1+(p−11)gp−2p=gp−1+gp−2p(p−1)≡1−pgp−2≢1(modp2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**第二步** ：上文选取的 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对于任意 𝑒 ≥1e≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑔𝜑(𝑝𝑒) ≢1(mod𝑝𝑒+1)gφ(pe)≢1(modpe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选取保证了 𝑒 =1e=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，该式成立．假设该式对于 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形成立，现要证明 𝑒 +1e+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形也成立．对于任意 𝑒 ≥1e≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由欧拉定理可知，存在 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得

𝑔𝜑(𝑝𝑒)=1+𝜆𝑝𝑒gφ(pe)=1+λpe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

成立．由归纳假设，𝜆 ⟂𝑝λ⟂p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 𝜑(𝑝𝑒+1) =𝑝𝜑(𝑝𝑒)φ(pe+1)=pφ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以

𝑔𝜑(𝑝𝑒+1)=(𝑔𝜑(𝑝𝑒))𝑝=(1+𝜆𝑝𝑒)𝑝≡1+𝜆𝑝𝑒+1(mod𝑝𝑒+2).gφ(pe+1)=(gφ(pe))p=(1+λpe)p≡1+λpe+1(modpe+2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

结合 𝜆 ⟂𝑝λ⟂p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知，𝑔𝜑(𝑝𝑒+1) ≢1(mod𝑝𝑒+2)gφ(pe+1)≢1(modpe+2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由数学归纳法可知，命题成立．

**第三步** ：上文选取的 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对于任意 𝑒 ≥1e≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都是模 𝑝𝑒pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根．

对 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选取保证了 𝑒 =1e=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，命题成立．假设命题对于 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立，现在要证明命题对于 𝑒 +1e+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也成立．将 𝛿𝑝𝑒+1(𝑔)δpe+1(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 简记为 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于 𝑔𝛿 ≡1(mod𝑝𝑒+1)gδ≡1(modpe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必然也有 𝑔𝛿 ≡1(mod𝑝𝑒)gδ≡1(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由归纳假设可知，𝛿𝑝𝑒(𝑔) =𝜑(𝑝𝑒)δpe(g)=φ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，由前文阶的 性质 2，就有 𝜑(𝑝𝑒) ∣𝛿φ(pe)∣δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．又由欧拉定理可知，𝛿 ∣𝜑(𝑝𝑒+1)δ∣φ(pe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，𝜑(𝑝𝑒+1) =𝑝𝜑(𝑝𝑒)φ(pe+1)=pφ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，只有两种可能：𝛿 =𝜑(𝑝𝑒)δ=φ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝛿 =𝜑(𝑝𝑒+1)δ=φ(pe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，第二步的结论说明，𝑔𝜑(𝑝𝑒) ≢1(mod𝑝𝑒+1)gφ(pe)≢1(modpe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，可能性 𝛿 =𝜑(𝑝𝑒)δ=φ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并不成立．唯一的可能性就是 𝛿 =𝜑(𝑝𝑒+1)δ=φ(pe+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就说明 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑝𝑒+1pe+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根．由数学归纳法，命题对于所有 𝑒 ≥1e≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．

  3. 𝑚 =2𝑝𝑒m=2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为奇素数，𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

引理 3

对于奇素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，模 2𝑝𝑒2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根存在．

证明

设 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑝𝑒pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根，则 𝑔 +𝑝𝑒g+pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是模 𝑝𝑒pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根．两者之间必然有一个是奇数，不妨设它就是 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．显然，(𝑔,2𝑝𝑒) =1(g,2pe)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 𝛿 =𝛿2𝑝𝑒(𝑔)δ=δ2pe(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，需要证明 𝛿 =𝜑(2𝑝𝑒)δ=φ(2pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由欧拉定理，𝛿 ∣𝜑(2𝑝𝑒)δ∣φ(2pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．同时，根据定义 𝑔𝛿 ≡1(mod2𝑝𝑒)gδ≡1(mod2pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，𝑔𝛿 ≡1(mod𝑝𝑒)gδ≡1(modpe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此，由阶的 性质 2 和 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选取可知，𝛿𝑝𝑒(𝑔) =𝜑(𝑝𝑒) ∣𝛿δpe(g)=φ(pe)∣δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由欧拉函数表达式可知，𝜑(2𝑝𝑒) =𝜑(𝑝𝑒)φ(2pe)=φ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，𝛿 =𝛿2𝑝𝑒(𝑔) =𝜑(𝑝𝑒)δ=δ2pe(g)=φ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就说明 𝛿δ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 2𝑝𝑒2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根．

  4. 𝑚 ≠1,2,4,𝑝𝑒,2𝑝𝑒m≠1,2,4,pe,2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为奇素数，𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

引理 4

假设 𝑚 ≠1,2,4m≠1,2,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且不存在奇素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正整数 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑚 =𝑝𝑒m=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑚 =2𝑝𝑒m=2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根不存在．

证明

对于 𝑚 =2𝑒m=2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑒 ≥3e≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，假设模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在．由于 𝑔 ⟂𝑚g⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它一定是奇数．假设 𝑔 =2𝑘 +1g=2k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑘 ∈𝐍k∈N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，有

𝑔2𝑒−2=(2𝑘+1)2𝑒−2≡1+(2𝑒−21)(2𝑘)+(2𝑒−22)(2𝑘)2=1+2𝑒−1𝑘+2𝑒−1(2𝑒−2−1)𝑘2=1+2𝑒−1(𝑘+(2𝑒−2−1)𝑘2)≡1(mod2𝑒).g2e−2=(2k+1)2e−2≡1+(2e−21)(2k)+(2e−22)(2k)2=1+2e−1k+2e−1(2e−2−1)k2=1+2e−1(k+(2e−2−1)k2)≡1(mod2e).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

倒数第二行中，因为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 (2𝑒−2 −1)𝑘2(2e−2−1)k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 奇偶性相同，所以它们的和是偶数．由阶的定义可知，𝛿2𝑒(𝑔) ≤2𝑒−2 <𝜑(2𝑒) =2𝑒−1δ2e(g)≤2e−2<φ(2e)=2e−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这与假设中 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是原根矛盾．由反证法，这样的原根并不存在．

假设 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足所述条件，且不是 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂，那么，一定存在 2 <𝑚1 <𝑚22<m1<m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑚1 ⟂𝑚2m1⟂m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑚 =𝑚1𝑚2m=m1m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．假设模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在．因为 𝑔 ⟂𝑚g⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以对于 𝑖 =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑔 ⟂𝑚𝑖g⟂mi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由欧拉定理可知，

𝑔𝜑(𝑚𝑖)≡1(mod𝑚𝑖).gφ(mi)≡1(modmi).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于 𝑚𝑖 >2mi>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝜑(𝑚𝑖)φ(mi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为偶数，所以，对于 𝑖 =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝑔12𝜑(𝑚1)𝜑(𝑚2)≡1(mod𝑚𝑖).g12φ(m1)φ(m2)≡1(modmi).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由 [中国剩余定理](../crt/) 可知

𝑔12𝜑(𝑚1)𝜑(𝑚2)≡1(mod𝑚).g12φ(m1)φ(m2)≡1(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

又因为 𝜑(𝑚) =𝜑(𝑚1)𝜑(𝑚2)φ(m)=φ(m1)φ(m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以由阶的定义可知

𝛿𝑚(𝑔)≤12𝜑(𝑚1)𝜑(𝑚2)=12𝜑(𝑚)<𝜑(𝑚).δm(g)≤12φ(m1)φ(m2)=12φ(m)<φ(m).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这与 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根的假设矛盾．故而，由反证法知，模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根不存在．

综合以上四个引理，我们便给出了一个数存在原根的充要条件．

### 求原根的算法

对于任何存在原根的模数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要求得它的原根 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只需要枚举可能的正整数，并逐个判断它是否为原根即可．枚举时，通常有两种处理方式：从小到大逐一枚举、随机生成一些正整数．这两种枚举方式的实际效率相当．

从小到大逐一枚举时，得到的是模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小原根 𝑔𝑚gm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此，枚举部分的复杂度取决于 𝑔𝑚gm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小．对此，有如下估计：

  * 上界的估计：王元5和 Burgess6证明了素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小原根 𝑔𝑝 =𝑂(𝑝0.25+𝜖)gp=O(p0.25+ϵ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝜖 >0ϵ>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．Cohen, Odoni, and Stothers7和 Elliott and Murata8分别证明了该估计对于模数 𝑝2p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 2𝑝22p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也成立，其中，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇素数．由于对于 𝑒 >2e>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，模 𝑝2p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（或 2𝑝22p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的原根也是模 𝑝𝑒pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（或 2𝑝𝑒2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的原根，所以，最小原根的上界 𝑂(𝑝0.25+𝜖)O(p0.25+ϵ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有情形都成立．
  * 下界的估计：Fridlander9和 Salié10证明了存在 𝐶 >0C>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得对于无穷多素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有最小原根 𝑔𝑝 >𝐶log⁡𝑝gp>Clog⁡p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．
  * 平均情形的估计：Burgess and Elliott11证明了平均情形下素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小原根 𝑔𝑝 =𝑂((log⁡𝑝)2(log⁡log⁡𝑝)4)gp=O((log⁡p)2(log⁡log⁡p)4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．Elliott and Murata12进一步猜想素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小原根的平均值是一个常数，且通过数值验证13得到它大概为 4.9264.926![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．随后，Elliott and Murata8将这一猜想推广到模 2𝑝22p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．

根据这些分析，暴力寻找最小原根时，枚举部分的复杂度 𝑂(𝑔𝑚(log⁡𝑚)2)O(gm(log⁡m)2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是可以接受的．

除了从小到大枚举外，还可以通过随机生成正整数并验证的方法寻找原根．原根的密度并不低：1

𝜑(𝜑(𝑚))𝑚=Ω(1log⁡log⁡𝑚).φ(φ(m))m=Ω(1log⁡log⁡m).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，通过随机方法寻找原根时，枚举部分的期望复杂度为 𝑂((log⁡𝑚)2log⁡log⁡𝑚)O((log⁡m)2log⁡log⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

需要注意的是，判定原根时需要已知 𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的质因数分解．算法竞赛 [常用质因数分解算法](../pollard-rho/) 中，复杂度最优的 Pollard Rho 算法也需要 𝑂(𝑚1/4+𝜀)O(m1/4+ε)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间．因此，只要 𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的质因数分解是未知的，无论采用哪种枚举方式，求原根的复杂度瓶颈都在于质因数分解这一步，而非枚举验证的部分．

## Carmichael 函数

相对于模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 元素的阶这一局部概念，Carmichael 函数是一个全局概念．它是所有与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素的整数的幂次的最小公共循环节．

Carmichael 函数

对于 𝑚 ∈𝐍+m∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义 𝜆(𝑚)λ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为能够使得同余关系 𝑎𝑛 ≡1(mod𝑚)an≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立的最小正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．函数 𝜆 :𝐍+ →𝐍+λ:N+→N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就称为 **Carmichael 函数** ．

根据 性质 2，能够使得 𝑎𝑛 ≡1(mod𝑚)an≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立，意味着 𝛿𝑚(𝑎) ∣𝑛δm(a)∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．也就是说，符合这一条件的正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一定是全体 𝛿𝑚(𝑎)δm(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的公倍数．因此，最小的这样的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是它们的最小公倍数：

𝜆(𝑚)=lcm⁡{𝛿𝑚(𝑎):𝑎⟂𝑚}.λ(m)=lcm⁡{δm(a):a⟂m}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这也常用作 Carmichael 函数的等价定义．

反复应用 性质 5 可知，一定存在某个元素 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝛿𝑚(𝑎) =𝜆(𝑚)δm(a)=λ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，上式也可以写作

𝜆(𝑚)=max{𝛿𝑚(𝑎):𝑎⟂𝑚}.λ(m)=max{δm(a):a⟂m}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

取得这一最值的元素 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也称为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **𝜆 λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑原根**．它对于所有模数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都存在．

### 递推公式

Carmichael 函数是一个 [数论函数](../basic/#数论函数)．本节讨论它的一个递推公式，并由此给出原根存在定理的另一个证明．

虽然不是积性函数，但是计算 Carmichael 函数时，同样可以对互素的因子分别处理．

引理

对于互素的正整数 𝑚1,𝑚2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜆(𝑚1𝑚2) =[𝜆(𝑚1),𝜆(𝑚2)]λ(m1m2)=[λ(m1),λ(m2)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

设 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为模 𝑚1m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和模 𝑚2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑原根．令 𝑚 =𝑚1𝑚2m=m1m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 [中国剩余定理](../crt/) 可知，存在 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑎 ≡𝑎𝑖(mod𝑚𝑖)a≡ai(modmi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于 𝑖 =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．由于 𝑎𝜆(𝑚) ≡1(mod𝑚)aλ(m)≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以对于 𝑖 =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑎𝜆(𝑚)𝑖 ≡1(mod𝑚𝑖)aiλ(m)≡1(modmi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进而由 性质 2 和 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选取可知，𝜆(𝑚𝑖) =𝛿𝑚𝑖(𝑎𝑖) ∣𝜆(𝑚)λ(mi)=δmi(ai)∣λ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就说明 [𝜆(𝑚1),𝜆(𝑚2)] ∣𝜆(𝑚)[λ(m1),λ(m2)]∣λ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

反过来，对于任意 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑖 =1,2i=1,2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑎[𝜆(𝑚1),𝜆(𝑚2)] ≡1(mod𝑚𝑖)a[λ(m1),λ(m2)]≡1(modmi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．应用中国剩余定理，就得到 𝑎[𝜆(𝑚1),𝜆(𝑚2)] ≡1(mod𝑚)a[λ(m1),λ(m2)]≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑎 ⟂𝑚a⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．根据 Carmichael 函数的定义可知，𝜆(𝑚) ∣[𝜆(𝑚1),𝜆(𝑚2)]λ(m)∣[λ(m1),λ(m2)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由此，命题中的等式成立．

因此，接下来只要计算 Carmichael 函数在素数幂处的取值．首先，处理 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次的情形．

引理

对于 𝑚 =2𝑒m=2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜆(2) =1λ(2)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝜆(4) =2λ(4)=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且对于 𝑒 ≥3e≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 𝜆(𝑚) =2𝑒−2λ(m)=2e−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

对于 𝑚 =2,4m=2,4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，单独讨论即可．对于 𝑚 =2𝑒m=2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑒 ≥3e≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，首先重复前文 引理 4 的证明的第一部分，就得到 𝜆(𝑚) ≤2𝑒−2λ(m)≤2e−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而，只需要证明存在 2𝑒−22e−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶元素即可．为此，有

52𝑒−3=(1+22)2𝑒−3=1+22×2𝑒−3=1+2𝑒−1≢1(mod2𝑒).52e−3=(1+22)2e−3=1+22×2e−3=1+2e−1≢1(mod2e).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这说明 𝛿𝑚(5) ∤2𝑒−3δm(5)∤2e−3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又因为 𝛿𝑚(5) ∣2𝑒−2δm(5)∣2e−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只能是 2𝑒−22e−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶元素．这就说明，𝜆(𝑚) =2𝑒−2λ(m)=2e−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在这个引理的证明过程中，实际上得到了关于模 2𝑒2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既约剩余系结构的刻画：

推论

设模数为 2𝑒2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑒 ≥2e≥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，所有奇数都同余于唯一一个 ±5𝑘±5k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 形式的整数同余，其中，𝑘 ∈𝐍k∈N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑘 <2𝑒−2k<2e−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，±1, ±5,⋯, ±52𝑒−2−1±1,±5,⋯,±52e−2−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两不同余，且构成一个既约剩余系．

证明

容易验证，𝑒 =2e=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形成立．对于 𝑒 ≥3e≥3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，由于前述证明中已经得到 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 2𝑒2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶是 2𝑒−22e−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，1,5,⋯,52𝑒−2−11,5,⋯,52e−2−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两不同余．因为这些整数都模 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 余 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它们的相反数都模 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 余 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 ±1, ±5,⋯, ±52𝑒−2−1±1,±5,⋯,±52e−2−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 2𝑒2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两不同余．由于它们共计 2𝑒−12e−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，恰为模 2𝑒2e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的既约剩余系的大小，所以，它们就构成了既约剩余系本身．

然后，处理奇素数幂的情形．

引理

对于 𝑚 =𝑝𝑒m=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇素数且 𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜆(𝑚) =𝑝𝑒−1(𝑝 −1)λ(m)=pe−1(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

首先证明命题对于 𝑒 =1e=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑚 =𝑝m=p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇素数的情形成立．为此，由 Carmichael 函数的定义可知，与 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素的所有整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是同余方程 𝑥𝜆(𝑝) ≡1(mod𝑝)xλ(p)≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解．在模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的意义下，该方程共有 𝑝 −1p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个互不相同的解．根据 [Lagrange 定理](../congruence-equation/#定理-3lagrange-定理) 可知，𝑝 −1 ≤𝜆(𝑝)p−1≤λ(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．同时，欧拉定理要求，𝜆(𝑝) ∣𝜑(𝑝) =𝑝 −1λ(p)∣φ(p)=p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，𝜆(𝑝) =𝑝 −1λ(p)=p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于 𝑚 =𝑝𝑒m=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑒 >1e>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，可以从证明 1 +𝑝1+p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑝𝑒−1pe−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶元开始．为此，有

(1+𝑝)𝑝𝑒−1≡1,(1+𝑝)𝑝𝑒−2≡1+𝑝𝑒−1≢1(mod𝑝𝑒).(1+p)pe−1≡1,(1+p)pe−2≡1+pe−1≢1(modpe).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，𝛿𝑚(1 +𝑝) =𝑝𝑒−1δm(1+p)=pe−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．另外，设模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根为 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，由于 𝑔𝛿𝑚(𝑔) ≡1(mod𝑝)gδm(g)≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，由阶的 性质 2 可知，𝑝 −1 ∣𝛿𝑚(𝑝)p−1∣δm(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由 Carmichael 函数的定义和欧拉定理可知

𝑝𝑒−1(𝑝−1)=[𝛿𝑚(𝑝),𝑝𝑒−1]∣𝜆(𝑚)∣𝜑(𝑚)=𝑝𝑒−1(𝑝−1).pe−1(p−1)=[δm(p),pe−1]∣λ(m)∣φ(m)=pe−1(p−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，𝜆(𝑚) =𝑝𝑒−1(𝑝 −1)λ(m)=pe−1(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

将本节的结果简单归纳，就得到 Carmichael 函数的递推公式：

定理

对于任意正整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝜆(𝑚)=⎧{ {⎨{ {⎩𝜑(𝑚),if 𝑚=1,2,4,𝑝𝑒 for odd prime 𝑝 and 𝑒≥1,12𝜑(𝑚),if 𝑚=2𝑒, 𝑒≥3,lcm⁡{𝜆(𝑝𝑒11),𝜆(𝑝𝑒22),⋯,𝜆(𝑝𝑒𝑠𝑠)},if 𝑚=𝑝𝑒11𝑝𝑒22⋯𝑝𝑒𝑠𝑠 for distinct 𝑝1,𝑝2,⋯,𝑝𝑠.λ(m)={φ(m),if m=1,2,4,pe for odd prime p and e≥1,12φ(m),if m=2e, e≥3,lcm⁡{λ(p1e1),λ(p2e2),⋯,λ(pses)},if m=p1e1p2e2⋯pses for distinct p1,p2,⋯,ps.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用该递推公式可以加强前文的结果：

推论

对于正整数 𝑚1,𝑚2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜆([𝑚1,𝑚2]) =[𝜆(𝑚1),𝜆(𝑚2)]λ([m1,m2])=[λ(m1),λ(m2)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

比较原根和 Carmichael 函数的定义可知，模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根存在，当且仅当 𝜆(𝑚) =𝜑(𝑚)λ(m)=φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．从 Carmichael 函数的递推公式中，容易归纳出如下结果：

推论

模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根存在，当且仅当 𝑚 =1,2,4,𝑝𝑒,2𝑝𝑒m=1,2,4,pe,2pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇素数且 𝑒 ∈𝐍+e∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于本节对于递推公式的证明并没有用到原根存在定理，因此，这就构成了对该定理的又一个证明．

### Carmichael 数

利用 Carmichael 函数，可以讨论 Carmichael 数（卡迈克尔数，OEIS:[A002997](https://oeis.org/A002997)）的性质与分布．这是 [Fermat 素性测试](../prime/#fermat-素性测试) 一定无法正确排除的合数．

Carmichael 数

对于合数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果对于所有整数 𝑎 ⟂𝑛a⟂n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有同余式 𝑎𝑛−1 ≡1(mod𝑛)an−1≡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立，就称 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **Carmichael 数** ．

最小的 Carmichael 数是 561 =3 ×11 ×17561=3×11×17![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由 Carmichael 函数的定义可知，合数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Carmichael 数当且仅当 𝜆(𝑛) ∣𝑛 −1λ(n)∣n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝜆(𝑛)λ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 Carmichael 函数．进一步地，可以得到如下判断合数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否为 Carmichael 数的方法：

Korselt 判别法14

合数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Carmichael 数当且仅当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无平方因子且对 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的任意质因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均有 (𝑝 −1) ∣(𝑛 −1)(p−1)∣(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

首先证明条件的必要性．假设 𝜆(𝑛) ∣(𝑛 −1)λ(n)∣(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．检查 Carmichael 函数的递推公式可知，如果 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有平方因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，一定有 𝑝 ∣𝜆(𝑛)p∣λ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是 𝑝 ∤(𝑛 −1)p∤(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，矛盾．同理，Carmichael 函数的递推公式说明，(𝑝 −1) ∣𝜆(𝑛)(p−1)∣λ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，也有 (𝑝 −1) ∣(𝑛 −1)(p−1)∣(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

然后证明条件的充分性．因为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是合数，所以它一定有奇素因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶数，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也就一定是奇数．对于无平方因子的奇合数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 Carmichael 函数的递推公式可知，𝜆(𝑛) =lcm⁡{𝑝 −1 :𝑝 ∣𝑛}λ(n)=lcm⁡{p−1:p∣n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，只要 (𝑝 −1) ∣(𝑛 −1)(p−1)∣(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有素因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立，就一定有 𝜆(𝑛) ∣(𝑛 −1)λ(n)∣(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

从这一判别法出发，可以建立 Carmichael 数的一些简单性质：

推论

Carmichael 数是奇数，没有平方因子，而且至少有 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同的素因子．

证明

前两条性质可以直接从 Korselt 判别法及其证明中得到．要得到第三条性质，只需要再证明：互异素数 𝑝1,𝑝2p1,p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘积 𝑛 =𝑝1𝑝2n=p1p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定不是 Carmichael 数．假设 𝑛 =𝑝1𝑝2n=p1p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Carmichael 数．由 Korselt 判别法可知，(𝑝𝑖 −1) ∣(𝑛 −1)(pi−1)∣(n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是，有

𝑛−1=𝑝1𝑝2−1≡𝑝2−1(mod𝑝1−1).n−1=p1p2−1≡p2−1(modp1−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，(𝑝1 −1) ∣(𝑝2 −1)(p1−1)∣(p2−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．同理，(𝑝2 −1) ∣(𝑝1 −1)(p2−1)∣(p1−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，𝑝1 =𝑝2p1=p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这与假设矛盾．因此，Carmichael 数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至少有 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个互异素因子．

利用解析数论还可以得到 Carmichael 数分布的一些性质．设 𝐶(𝑛)C(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为小于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Carmichael 数个数．Alford, Granville, and Pomerance2证明，对于充分大的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝐶(𝑛) >𝑛2/7C(n)>n2/7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，Carmichael 数有无限多个．在这之前，Erdős3已经证明，𝐶(𝑛) <𝑛exp⁡(−𝑐ln⁡𝑛ln⁡ln⁡ln⁡𝑛ln⁡ln⁡𝑛)C(n)<nexp⁡(−cln⁡nln⁡ln⁡ln⁡nln⁡ln⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为常数．因此，Carmichael 数的分布（相对于素数来说）十分稀疏．实际上，有4 𝐶(109) =646C(109)=646![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐶(1018) =1 401 644C(1018)=1 401 644![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 参考资料与注释

  * [Primitive root modulo n - Wikipedia](https://en.wikipedia.org/wiki/Primitive_root_modulo_n)
  * [The order of a unit - Course Notes](https://crypto.stanford.edu/pbc/notes/numbertheory/order.html)
  * [The primitive root theorem - Amin Witno's notes](http://witno.com/philadelphia/notes/won5.pdf)
  * [Carmichael function - Wikipedia](https://en.wikipedia.org/wiki/Carmichael_function)
  * [Carmichael's Lambda Function - Brilliant Math & Science Wiki](https://brilliant.org/wiki/carmichaels-lambda-function/)
  * [Carmichael number - Wikipedia](https://en.wikipedia.org/wiki/Carmichael_number)
  * [Carmichael Number - Wolfram MathWorld](https://mathworld.wolfram.com/CarmichaelNumber.html)

* * *

  1. 如果模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根存在，那么，𝜑(𝑚) ≥13𝑚φ(m)≥13m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且等号仅在 𝑚 =2 ×3𝑒 (𝑒 ∈𝐍+)m=2×3e (e∈N+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处取得．进一步地，当 𝑚 >2m>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，对欧拉函数 𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有估计：𝜑(𝑚) >𝑚𝑒𝛾log⁡log⁡𝑚+3log⁡log⁡𝑚φ(m)>meγlog⁡log⁡m+3log⁡log⁡m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．将这两者结合，就得到文中的表达式．关于欧拉函数的该估计，可以参考论文 Rosser, J. Barkley, and Lowell Schoenfeld. "Approximate formulas for some functions of prime numbers." Illinois Journal of Mathematics 6, no. 1 (1962): 64-94． ↩

  2. W. R. Alford; Andrew Granville; Carl Pomerance (1994). "There are Infinitely Many Carmichael Numbers." Annals of Mathematics. 140 (3): 703–722. ↩

  3. Erdős, P. (1956). "On pseudoprimes and Carmichael numbers." Publ. Math. Debrecen. 4 (3–4): 201–206. ↩

  4. PINCH, Richard GE. The Carmichael numbers up to 10201020![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7). ↩

  5. Wang Y. "On the least primitive root of a prime." (in Chinese). Acta Math Sinica, 1959, 4: 432–441; English transl. in _Sci. Sinica_ , 1961, 10: 1–14. ↩

  6. BURGESS, David A. "On character sums and primitive roots." Proceedings of the London Mathematical Society, 1962, 3.1: 179-192. ↩

  7. Cohen, S. D., R. W. K. Odoni, and W. W. Stothers. "On the least primitive root modulo p 2." Bulletin of the London Mathematical Society 6, no. 1 (1974): 42-46. ↩

  8. Elliott, P. D. T. A., and L. Murata. "The least primitive root mod 2p2." Mathematika 45, no. 2 (1998): 371-379. ↩↩

  9. FRIDLENDER, V. R. "On the least n-th power non-residue." Dokl. Akad. Nauk SSSR. 1949. p. 351-352. ↩

  10. SALIÉ, Hans. "Über den kleinsten positiven quadratischen Nichtrest nach einer Primzahl." Mathematische Nachrichten, 1949, 3.1: 7-8. ↩

  11. Burgess, D. A., and P. D. T. A. Elliott. "The average of the least primitive root." Mathematika 15, no. 1 (1968): 39-50. ↩

  12. Elliott, Peter DTA, and Leo Murata. "On the average of the least primitive root modulo p." Journal of The london Mathematical Society 56, no. 3 (1997): 435-454. ↩

  13. 更多结果可以参考 [Least prime primitive root of prime numbers](https://sweet.ua.pt/tos/p_roots.html)． ↩

  14. Korselt, A. R. (1899). "Problème chinois." L'Intermédiaire des Mathématiciens. 6: 142–143. ↩

* * *

>  __本页面最近更新： 2025/11/1 11:21:19，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/primitive-root.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/primitive-root.md "edit.link.title")  
>  __本页面贡献者：[Peanut-Tang](https://github.com/Peanut-Tang), [c-forrest](https://github.com/c-forrest), [Early0v0](https://github.com/Early0v0), [Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [StudyingFather](https://github.com/StudyingFather), [Great-designer](https://github.com/Great-designer), [MegaOwIer](https://github.com/MegaOwIer), [Xeonacid](https://github.com/Xeonacid), [2008verser](https://github.com/2008verser), [Enter-tainer](https://github.com/Enter-tainer), [bobhan1](https://github.com/bobhan1), [CCXXXI](https://github.com/CCXXXI), [chuxin0816](https://github.com/chuxin0816), [CroMarmot](https://github.com/CroMarmot), [GavinZhengOI](https://github.com/GavinZhengOI), [GeorgePlover](https://github.com/GeorgePlover), [hhc0001](https://github.com/hhc0001), [huhaoo](https://github.com/huhaoo), [Larry0716](https://github.com/Larry0716), [Marcythm](https://github.com/Marcythm), [opsiff](https://github.com/opsiff), [ouuan](https://github.com/ouuan), [PeterlitsZo](https://github.com/PeterlitsZo), [ShelpAm](https://github.com/ShelpAm), [tml104](https://github.com/tml104), [wty-yy](https://github.com/wty-yy)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
