# 多项式平移|连续点值平移 - OI Wiki

- Source: https://oi-wiki.org/math/poly/shift/

# 多项式平移|连续点值平移

## 多项式平移

多项式平移是简单情况的多项式复合变换，给出 𝑓(𝑥) =∑𝑛𝑖=0𝑓𝑖𝑥𝑖f(x)=∑i=0nfixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数和一个常数 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 𝑓(𝑥 +𝑐)f(x+c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数，即 𝑓(𝑥) ↦𝑓(𝑥 +𝑐)f(x)↦f(x+c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 分治法

令

𝑓(𝑥)=𝑓0(𝑥)+𝑥⌊𝑛/2⌋𝑓1(𝑥)f(x)=f0(x)+x⌊n/2⌋f1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么

𝑓(𝑥+𝑐)=𝑓0(𝑥+𝑐)+(𝑥+𝑐)⌊𝑛/2⌋𝑓1(𝑥+𝑐)f(x+c)=f0(x+c)+(x+c)⌊n/2⌋f1(x+c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

(𝑥 +𝑐)⌊𝑛/2⌋(x+c)⌊n/2⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数为二项式系数，那么

𝑇(𝑛)=2𝑇(𝑛/2)+𝑂(𝑛log⁡𝑛)=𝑂(𝑛log2⁡𝑛)T(n)=2T(n/2)+O(nlog⁡n)=O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为多项式乘法的时间．

### Taylor 公式法

对 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处应用 Taylor 公式，有

𝑓(𝑥)=𝑓(𝑐)+𝑓′(𝑐)1!(𝑥−𝑐)+𝑓″(𝑐)2!(𝑥−𝑐)2+⋯+𝑓(𝑛)(𝑐)𝑛!(𝑥−𝑐)𝑛f(x)=f(c)+f′(c)1!(x−c)+f″(c)2!(x−c)2+⋯+f(n)(c)n!(x−c)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么

𝑓(𝑥+𝑐)=𝑓(𝑐)+𝑓′(𝑐)1!𝑥+𝑓″(𝑐)2!𝑥2+⋯+𝑓(𝑛)(𝑐)𝑛!𝑥𝑛f(x+c)=f(c)+f′(c)1!x+f″(c)2!x2+⋯+f(n)(c)n!xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

观察到对于 𝑡 ≥0t≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

𝑡![𝑥𝑡]𝑓(𝑥+𝑐)=𝑓(𝑡)(𝑐)=𝑛∑𝑖=𝑡𝑓𝑖𝑖!𝑐𝑖−𝑡(𝑖−𝑡)!=𝑛−𝑡∑𝑖=0𝑓𝑖+𝑡(𝑖+𝑡)!𝑐𝑖𝑖!t![xt]f(x+c)=f(t)(c)=∑i=tnfii!ci−t(i−t)!=∑i=0n−tfi+t(i+t)!cii!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令

𝐴0(𝑥)=𝑛∑𝑖=0𝑓𝑛−𝑖(𝑛−𝑖)!𝑥𝑖𝐵0(𝑥)=𝑛∑𝑖=0𝑐𝑖𝑖!𝑥𝑖A0(x)=∑i=0nfn−i(n−i)!xiB0(x)=∑i=0ncii!xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么

[𝑥𝑛−𝑡](𝐴0(𝑥)𝐵0(𝑥))=𝑛−𝑡∑𝑖=0([𝑥𝑛−𝑡−𝑖]𝐴0(𝑥))([𝑥𝑖]𝐵0(𝑥))=𝑛−𝑡∑𝑖=0𝑓𝑖+𝑡(𝑖+𝑡)!𝑐𝑖𝑖!=𝑡![𝑥𝑡]𝑓(𝑥+𝑐)[xn−t](A0(x)B0(x))=∑i=0n−t([xn−t−i]A0(x))([xi]B0(x))=∑i=0n−tfi+t(i+t)!cii!=t![xt]f(x+c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 二项式定理法

考虑二项式定理 (𝑎 +𝑏)𝑛 =𝑛∑𝑖=0(𝑛𝑖)𝑎𝑖𝑏𝑛−𝑖(a+b)n=∑i=0n(ni)aibn−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

𝑓(𝑥+𝑐)=𝑛∑𝑖=0𝑓𝑖(𝑥+𝑐)𝑖=𝑛∑𝑖=0𝑓𝑖(𝑖∑𝑗=0(𝑖𝑗)𝑥𝑗𝑐𝑖−𝑗)=𝑛∑𝑖=0𝑓𝑖𝑖!(𝑖∑𝑗=0𝑥𝑗𝑗!𝑐𝑖−𝑗(𝑖−𝑗)!)=𝑛∑𝑖=0𝑥𝑖𝑖!(𝑛∑𝑗=𝑖𝑓𝑗𝑗!𝑐𝑗−𝑖(𝑗−𝑖)!)f(x+c)=∑i=0nfi(x+c)i=∑i=0nfi(∑j=0i(ij)xjci−j)=∑i=0nfii!(∑j=0ixjj!ci−j(i−j)!)=∑i=0nxii!(∑j=infjj!cj−i(j−i)!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

得到的结果与上述方法相同．

## 连续点值平移

例题 [LOJ 166 拉格朗日插值 2](https://loj.ac/p/166)

给出度数小于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的多项式 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连续点值 𝑓(0),𝑓(1),…,𝑓(𝑛)f(0),f(1),…,f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在模 998244353998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下计算 𝑓(𝑐),𝑓(𝑐 +1),…,𝑓(𝑐 +𝑛)f(c),f(c+1),…,f(c+n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 1 ≤𝑛 ≤105,𝑛 <𝑚 ≤1081≤n≤105,n<m≤108![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### Lagrange 插值公式法

考虑 [Lagrange 插值公式](../../numerical/interp/#lagrange-插值法)

𝑓(𝑥)=∑0≤𝑖≤𝑛𝑓(𝑖)∏0≤𝑗≤𝑛∧𝑗≠𝑖𝑥−𝑗𝑖−𝑗=∑0≤𝑖≤𝑛𝑓(𝑖)𝑥!(𝑥−𝑛−1)!(𝑥−𝑖)(−1)𝑛−𝑖𝑖!(𝑛−𝑖)!=𝑥!(𝑥−𝑛−1)!∑0≤𝑖≤𝑛𝑓(𝑖)(𝑥−𝑖)(−1)𝑛−𝑖𝑖!(𝑛−𝑖)!f(x)=∑0≤i≤nf(i)∏0≤j≤n∧j≠ix−ji−j=∑0≤i≤nf(i)x!(x−n−1)!(x−i)(−1)n−ii!(n−i)!=x!(x−n−1)!∑0≤i≤nf(i)(x−i)(−1)n−ii!(n−i)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上式虽然是卷积形式但不能保证分母上 𝑥 −𝑖 ≠0x−i≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以下面仅考虑 𝑐 >𝑛c>n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，其他情况（如系数在模素数意义下时须避免 𝐵0(𝑥)B0(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 系数的分母出现零）可以分类讨论解决，令

𝐴0(𝑥)=∑0≤𝑖≤𝑛𝑓(𝑖)(−1)𝑛−𝑖𝑖!(𝑛−𝑖)!𝑥𝑖𝐵0(𝑥)=∑𝑖≥01𝑐−𝑛+𝑖𝑥𝑖A0(x)=∑0≤i≤nf(i)(−1)n−ii!(n−i)!xiB0(x)=∑i≥01c−n+ixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么对于 𝑡 ≥0t≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

[𝑥𝑛+𝑡](𝐴0(𝑥)𝐵0(𝑥))=𝑛+𝑡∑𝑖=0([𝑥𝑖]𝐴0(𝑥))([𝑥𝑛+𝑡−𝑖]𝐵0(𝑥))=𝑛∑𝑖=0𝑓(𝑖)(−1)𝑛−𝑖𝑖!(𝑛−𝑖)!1𝑐+𝑡−𝑖=(𝑐+𝑡−𝑛−1)!(𝑐+𝑡)!𝑓(𝑐+𝑡)[xn+t](A0(x)B0(x))=∑i=0n+t([xi]A0(x))([xn+t−i]B0(x))=∑i=0nf(i)(−1)n−ii!(n−i)!1c+t−i=(c+t−n−1)!(c+t)!f(c+t)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

实现中取 𝐵0(𝑥)B0(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要的部分截断可求出更多点值，且可利用循环卷积．

对问题稍加修改，假设对于某个 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 给出的点值为 𝑓(𝑑),𝑓(𝑑 +𝑘),…,𝑓(𝑑 +𝑛𝑘)f(d),f(d+k),…,f(d+nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以计算 𝑓(𝑐 +𝑑),𝑓(𝑐 +𝑑 +𝑘),…,𝑓(𝑐 +𝑑 +𝑛𝑘)f(c+d),f(c+d+k),…,f(c+d+nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，视作平移 𝑔(𝑥) =𝑓(𝑑 +𝑘𝑥)g(x)=f(d+kx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点值 𝑔(0),𝑔(1),…,𝑔(𝑛)g(0),g(1),…,g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑔(𝑐/𝑘),𝑔(𝑐/𝑘 +1),…,𝑔(𝑐/𝑘 +𝑛)g(c/k),g(c/k+1),…,g(c/k+n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

Lagrange 插值公式也给出了通过维护一些前后缀积的线性计算单个点值的方法．

## 应用

### 同一行第一类无符号 Stirling 数

例题 [P5408 第一类斯特林数·行](https://www.luogu.com.cn/problem/P5408)

在模素数 167772161167772161![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下求 [𝑛0],[𝑛1],…,[𝑛𝑛][n0],[n1],…,[nn]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 1 ≤𝑛 <2621441≤n<262144![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑

𝑥――𝑛=𝑛∑𝑖=0[𝑛𝑖]𝑥𝑖,𝑛≥0xn―=∑i=0n[ni]xi,n≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑥――𝑛 =𝑥 ⋅(𝑥 +1)⋯(𝑥 +𝑛 −1)xn―=x⋅(x+1)⋯(x+n−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为上升阶乘幂，令 𝑓𝑛(𝑥) =𝑥――𝑛fn(x)=xn―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

𝑓2𝑛(𝑥)=𝑥――𝑛⋅(𝑥+𝑛)――𝑛=𝑓𝑛(𝑥)𝑓𝑛(𝑥+𝑛)f2n(x)=xn―⋅(x+n)n―=fn(x)fn(x+n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

通过多项式平移可在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求出 𝑓𝑛(𝑥 +𝑛)fn(x+n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，问题被缩小为原先的一半即求出 𝑓𝑛(𝑥)fn(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数，那么

𝑇(𝑛)=𝑇(𝑛/2)+𝑂(𝑛log⁡𝑛)=𝑂(𝑛log⁡𝑛)T(n)=T(n/2)+O(nlog⁡n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 模素数意义下阶乘

例题 [P5282【模板】快速阶乘算法](https://www.luogu.com.cn/problem/P5282)

求 𝑛!mod𝑝n!modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为素数且 1 ≤𝑛 <𝑝 ≤231 −11≤n<p≤231−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

令 𝑣 =⌊√𝑛⌋v=⌊n⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔(𝑥) =∏𝑣𝑖=1(𝑥 +𝑖)g(x)=∏i=1v(x+i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

𝑛!≡(𝑣−1∏𝑖=0𝑔(𝑖𝑣))⋅𝑛∏𝑖=𝑣2+1𝑖(mod𝑝)n!≡(∏i=0v−1g(iv))⋅∏i=v2+1ni(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 ∏𝑛𝑖=𝑣2+1𝑖∏i=v2+1ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可在 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间计算，我们希望可以快速计算上式的前半部分．

#### 多项式多点求值

𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 系数的计算可用上述多项式平移算法在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间得到，但多点求值计算 𝑔(0),𝑔(𝑣),𝑔(2𝑣),…,𝑔(𝑣2 −𝑣)g(0),g(v),g(2v),…,g(v2−v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要 𝑂(√𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间．

#### 连续点值平移

令 𝑔𝑑(𝑥) =∏𝑑𝑖=1(𝑥 +𝑖)gd(x)=∏i=1d(x+i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以用 𝑑 +1d+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点值 𝑔𝑑(0),𝑔𝑑(𝑣),…,𝑔𝑑(𝑑𝑣)gd(0),gd(v),…,gd(dv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 唯一确定这个次数为 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的多项式，又

𝑔2𝑑(𝑥)=𝑔𝑑(𝑥)𝑔𝑑(𝑥+𝑑)g2d(x)=gd(x)gd(x+d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以只需 2𝑑 +12d+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点值可以唯一确定 𝑔2𝑑(𝑥)g2d(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么使用连续点值平移计算 𝑔𝑑((𝑑 +1)𝑣),𝑔𝑑((𝑑 +2)𝑣),…,𝑔𝑑(2𝑑𝑣)gd((d+1)v),gd((d+2)v),…,gd(2dv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即平移 ℎ(𝑥) =𝑔𝑑(𝑣𝑥)h(x)=gd(vx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点值 ℎ(0),ℎ(1),…,ℎ(𝑑)h(0),h(1),…,h(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 ℎ(𝑑 +1),ℎ(𝑑 +2),…,ℎ(2𝑑)h(d+1),h(d+2),…,h(2d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）和 𝑔𝑑(𝑑),𝑔𝑑(𝑣 +𝑑),…,𝑔𝑑(2𝑑𝑣 +𝑑)gd(d),gd(v+d),…,gd(2dv+d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即平移 ℎ(𝑥) =𝑔𝑑(𝑣𝑥)h(x)=gd(vx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的点值 ℎ(0),ℎ(1),…,ℎ(𝑑)h(0),h(1),…,h(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 ℎ(𝑑/𝑣),ℎ(𝑑/𝑣 +1),ℎ(𝑑/𝑣 +2),…,ℎ(𝑑/𝑣 +2𝑑)h(d/v),h(d/v+1),h(d/v+2),…,h(d/v+2d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）后将这两者的对应点值相乘即得 𝑔2𝑑(0),𝑔2𝑑(𝑣),…,𝑔2𝑑(2𝑑𝑣)g2d(0),g2d(v),…,g2d(2dv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由 𝑔𝑑(0),𝑔𝑑(𝑣),…,𝑔𝑑(𝑑𝑣)gd(0),gd(v),…,gd(dv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算 𝑔𝑑+1(0),𝑔𝑑+1(𝑣),…,𝑔𝑑+1(𝑑𝑣),𝑔𝑑+1((𝑑 +1)𝑣)gd+1(0),gd+1(v),…,gd+1(dv),gd+1((d+1)v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 考虑

𝑔𝑑+1(𝑥)=(𝑥+𝑑+1)⋅𝑔𝑑(𝑥)gd+1(x)=(x+d+1)⋅gd(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

额外增加的一个点值使用线性时间的算法即可．那么在开始时维护 𝑔1(0) =1,𝑔1(𝑣) =𝑣 +1g1(0)=1,g1(v)=v+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后使用连续点值平移来倍增地维护这些点值，有

𝑇(𝑛)=𝑇(𝑛/2)+𝑂(𝑛log⁡𝑛)=𝑂(𝑛log⁡𝑛)T(n)=T(n/2)+O(nlog⁡n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而我们只需要约 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点值，所以时间复杂度为 𝑂(√𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 模素数意义下二项式系数前缀和

例题 [LOJ 6386 组合数前缀和](https://loj.ac/p/6386)

求 𝑚∑𝑖=0(𝑛𝑖)mod998244353∑i=0m(ni)mod998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 0 ≤𝑚 ≤𝑛 ≤9 ×1080≤m≤n≤9×108![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑使用矩阵描述 𝑛! =𝑛 ⋅(𝑛 −1)!n!=n⋅(n−1)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这一步递推，我们有

[𝑛!]=(𝑛−1∏𝑖=0[𝑖+1])[1][n!]=(∏i=0n−1[i+1])[1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

类似的可以将二项式系数前缀和的递推描述为

[(𝑛𝑚+1)∑𝑚𝑖=0(𝑛𝑖)]=[(𝑛−𝑚)/(𝑚+1)011][(𝑛𝑚)∑𝑚−1𝑖=0(𝑛𝑖)][(nm+1)∑i=0m(ni)]=[(n−m)/(m+1)011][(nm)∑i=0m−1(ni)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意矩阵乘法的顺序，那么

[(𝑛𝑚+1)∑𝑚𝑖=0(𝑛𝑖)]=(𝑚∏𝑖=0[(𝑛−𝑖)/(𝑖+1)011])[10]=1(𝑚+1)!(𝑚∏𝑖=0[𝑛−𝑖0𝑖+1𝑖+1])[10][(nm+1)∑i=0m(ni)]=(∏i=0m[(n−i)/(i+1)011])[10]=1(m+1)!(∏i=0m[n−i0i+1i+1])[10]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 𝑣 =⌊√𝑚⌋v=⌊m⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考虑维护矩阵

𝑀𝑑(𝑥)=𝑑∏𝑖=1[−𝑥+𝑛+1−𝑖0𝑥+𝑖𝑥+𝑖]=[𝑓𝑑(𝑥)0𝑔𝑑(𝑥)ℎ𝑑(𝑥)]Md(x)=∏i=1d[−x+n+1−i0x+ix+i]=[fd(x)0gd(x)hd(x)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的点值 𝑀𝑑(0),𝑀𝑑(𝑣),…,𝑀𝑑(𝑑𝑣)Md(0),Md(v),…,Md(dv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即 𝑓𝑑(0),𝑓𝑑(𝑣),…,𝑓𝑑(𝑑𝑣)fd(0),fd(v),…,fd(dv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、ℎ𝑑(0),…,ℎ𝑑(𝑑𝑣)hd(0),…,hd(dv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔𝑑(0),…,𝑔𝑑(𝑑𝑣)gd(0),…,gd(dv)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又

𝑀2𝑑(𝑥)=2𝑑∏𝑖=1[−𝑥+𝑛+1−𝑖0𝑥+𝑖𝑥+𝑖]=(𝑑∏𝑖=1[−𝑥−𝑑+𝑛+1−𝑖0𝑥+𝑑+𝑖𝑥+𝑑+𝑖])(𝑑∏𝑖=1[−𝑥+𝑛+1−𝑖0𝑥+𝑖𝑥+𝑖])=[𝑓𝑑(𝑥+𝑑)0𝑔𝑑(𝑥+𝑑)ℎ𝑑(𝑥+𝑑)][𝑓𝑑(𝑥)0𝑔𝑑(𝑥)ℎ𝑑(𝑥)]=[𝑓𝑑(𝑥+𝑑)𝑓𝑑(𝑥)0𝑔𝑑(𝑥+𝑑)𝑓𝑑(𝑥)+ℎ𝑑(𝑥+𝑑)𝑔𝑑(𝑥)ℎ𝑑(𝑥+𝑑)ℎ𝑑(𝑥)]M2d(x)=∏i=12d[−x+n+1−i0x+ix+i]=(∏i=1d[−x−d+n+1−i0x+d+ix+d+i])(∏i=1d[−x+n+1−i0x+ix+i])=[fd(x+d)0gd(x+d)hd(x+d)][fd(x)0gd(x)hd(x)]=[fd(x+d)fd(x)0gd(x+d)fd(x)+hd(x+d)gd(x)hd(x+d)hd(x)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且矩阵右下角元素恰为我们在阶乘算法中所维护的，那么

𝑚∏𝑖=0[𝑛−𝑖0𝑖+1𝑖+1]=⎛⎜ ⎜⎝𝑚∏𝑖=(𝑘+1)𝑣[𝑛−𝑖0𝑖+1𝑖+1]⎞⎟ ⎟⎠[𝑓𝑣(𝑘𝑣)0𝑔𝑣(𝑘𝑣)ℎ𝑣(𝑘𝑣)]⋯[𝑓𝑣(0)0𝑔𝑣(0)ℎ𝑣(0)]∏i=0m[n−i0i+1i+1]=(∏i=(k+1)vm[n−i0i+1i+1])[fv(kv)0gv(kv)hv(kv)]⋯[fv(0)0gv(0)hv(0)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可在 𝑂(√𝑚log⁡𝑚)O(mlog⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间完成计算．

### 模素数意义下调和数

例题 [P5702 调和级数求和](https://www.luogu.com.cn/problem/P5702)

求 ∑𝑛𝑖=1𝑖−1mod𝑝∑i=1ni−1modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为素数且 1 ≤𝑛 <𝑝 <2301≤n<p<230![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

记 𝐻𝑛 =∑𝑛𝑘=1𝑘−1Hn=∑k=1nk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一步递推为

[(𝑛+1)!(𝑛+1)!𝐻𝑛+1]=[𝑛+101𝑛+1][𝑛!𝑛!𝐻𝑛][(n+1)!(n+1)!Hn+1]=[n+101n+1][n!n!Hn]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么

[[𝑛+11][𝑛+12]]=[𝑛!𝑛!𝐻𝑛]=(𝑛−1∏𝑖=0[𝑖+101𝑖+1])[10][[n+11][n+12]]=[n!n!Hn]=(∏i=0n−1[i+101i+1])[10]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在这里 [𝑛+11][n+11]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 [𝑛+12][n+12]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为第一类无符号 Stirling 数．维护点值矩阵的方法同上．

## 整式递推

对于更一般的情况，类似于上述快速阶乘算法的案例，我们期望得到一个怎么样的算法？

例题 [P6115【模板】整式递推](https://www.luogu.com.cn/problem/P6115)

现有数列 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 ∀𝑛 ≥𝑚,∑𝑚𝑘=0𝑎𝑛−𝑘𝑃𝑘(𝑛) =0∀n≥m,∑k=0man−kPk(n)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑃𝑘Pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为不超过 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次的多项式．  
给定所有 𝑃𝑘Pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数，和 𝑎0,𝑎1,…,𝑎𝑚−1a0,a1,…,am−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 𝑎𝑛an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． 对 998244353998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模．𝑛 ≤6 ×108n≤6×108![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，1 ≤𝑚,𝑑 ≤71≤m,d≤7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时限 7𝑠7s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

为了更系统地描述上述几道例题中构造矩阵的过程，我们引入 [𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵](../../linear-algebra/jordan/#lambda-%E7%9F%A9%E9%98%B5) 的概念．

为了实现整式递推，我们应当注意到快速阶乘算法过程中，我们维护的点值其实并不是 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而是 ∏𝑇−1𝑖=0(𝑎𝑇 +𝑖)∏i=0T−1(aT+i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 **一对点值之间的倍数关系** ．

由于整式递推阶数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不止是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了，我们就 **不能直接维护一对数之间的倍数关系了** ；而是维护出 **一对 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维向量之间的线性变换**，即 𝑚 ×𝑚m×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个矩阵，**矩阵的每一项对应于某个多项式的一个点值** ．

容易发现，对于一般的整式递推远处系数求值问题，我们可以构造

−1𝑃0(𝑛)⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣𝑃1(𝑛)𝑃2(𝑛)𝑃3(𝑛)⋯𝑃𝑚−1(𝑛)𝑃𝑚(𝑛)−𝑃0(𝑛)−𝑃0(𝑛)−𝑃0(𝑛)⋱−𝑃0(𝑛)⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣𝑎𝑛−1𝑎𝑛−2𝑎𝑛−3⋮𝑎𝑛−𝑚+1𝑎𝑛−𝑚⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦=⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣𝑎𝑛𝑎𝑛−1𝑎𝑛−2⋮𝑎𝑛−𝑚+2𝑎𝑛−𝑚+1⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦−1P0(n)[P1(n)P2(n)P3(n)⋯Pm−1(n)Pm(n)−P0(n)−P0(n)−P0(n)⋱−P0(n)][an−1an−2an−3⋮an−m+1an−m]=[anan−1an−2⋮an−m+2an−m+1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设

𝐵(𝜆)=⎡⎢ ⎢ ⎢ ⎢ ⎢ ⎢ ⎢⎣𝑃1(𝜆)𝑃2(𝜆)𝑃3(𝜆)⋯𝑃𝑚−1(𝜆)𝑃𝑚(𝜆)−𝑃0(𝜆)−𝑃0(𝜆)−𝑃0(𝜆)⋱−𝑃0(𝜆)⎤⎥ ⎥ ⎥ ⎥ ⎥ ⎥ ⎥⎦B(λ)=[P1(λ)P2(λ)P3(λ)⋯Pm−1(λ)Pm(λ)−P0(λ)−P0(λ)−P0(λ)⋱−P0(λ)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们先撇开前面的 −1𝑃0(𝑛)−1P0(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 因子不论，我们现在要维护 ∏𝑇−1𝑖=0𝐵(𝑎𝑇 +𝑚 +𝑖)∏i=0T−1B(aT+m+i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这种形式的量，其中乘法自右往左．

容易发现 𝐵𝑇(𝜆) =∏𝑇−1𝑖=0𝐵(𝜆 +𝑖)BT(λ)=∏i=0T−1B(λ+i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个各项次数不高于 𝑑𝑇dT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵，只用 𝑑𝑇 +1dT+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个值即可维护．

于是我们维护出 𝐵𝑇(𝑚)BT(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑚 +𝑇)BT(m+T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑚 +2𝑇)BT(m+2T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，……![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑚 +(𝑑𝑇 −1)𝑇)BT(m+(dT−1)T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑚 +𝑑𝑇2)BT(m+dT2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这几个 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵的 **点值** ，然后用类似于快速阶乘算法的方式暴力进行多项式点值平移和倍增就好了．

具体地，为了让 𝑡 =log2⁡𝑇t=log2⁡T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 抬高 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们这么干：

  1. 在 𝑂(𝑚2𝑑𝑇log⁡(𝑑𝑇))O(m2dTlog⁡(dT))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内获取 𝐵𝑇(𝑝 +𝑑𝑇2)BT(p+dT2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(𝑑𝑇 +1)𝑇)BT(p+(dT+1)T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(𝑑𝑇 +2)𝑇)BT(p+(dT+2)T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，⋯⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(2𝑑𝑇 −1)𝑇)BT(p+(2dT−1)T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(2𝑑𝑇)𝑑𝑇)BT(p+(2dT)dT)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 在 𝑂(𝑚2𝑑𝑇log⁡(𝑑𝑇))O(m2dTlog⁡(dT))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内获取 𝐵𝑇(𝑝 +2𝑑𝑇2)BT(p+2dT2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(2𝑑𝑇 +1)𝑇)BT(p+(2dT+1)T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(2𝑑𝑇 +2)𝑇)BT(p+(2dT+2)T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，⋯⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(3𝑑𝑇 −1)𝑇)BT(p+(3dT−1)T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(3𝑑𝑇)𝑑𝑇)BT(p+(3dT)dT)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 在 𝑂(𝑚2𝑑𝑇log⁡(𝑑𝑇))O(m2dTlog⁡(dT))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内获取 𝐵𝑇(𝑝 +3𝑑𝑇2)BT(p+3dT2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(3𝑑𝑇 +1)𝑇)BT(p+(3dT+1)T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(3𝑑𝑇 +2)𝑇)BT(p+(3dT+2)T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，⋯⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(4𝑑𝑇 −1)𝑇)BT(p+(4dT−1)T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑇(𝑝 +(4𝑑𝑇)𝑑𝑇)BT(p+(4dT)dT)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  4. 计算 𝐵2𝑇(𝑣) =𝐵𝑇(𝑣 +𝑇)𝐵𝑇(𝑣)B2T(v)=BT(v+T)BT(v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们每轮花费 𝑂(𝑚2𝑑𝑇log⁡(𝑑𝑇))O(m2dTlog⁡(dT))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度进行平移；同时，我们每轮只用做 Θ(𝑑𝑇)Θ(dT)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次矩阵乘法，复杂度可以认为是 𝑂(𝑚3𝑑𝑇)O(m3dT)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后，我们只用做到 𝑇 ≥√𝑛/𝑑T≥n/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

之前的 −1𝑃0(𝑛)−1P0(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 因子可以用类似的方法解决．

这样，我们预处理的复杂度即为 Θ(√𝑛𝑑(𝑚3 +𝑚2log⁡(𝑛𝑑)))Θ(nd(m3+m2log⁡(nd)))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑查询，我们只用 Θ(𝑛/𝑇)Θ(n/T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次向量与矩阵的乘法，以及 𝑂(𝑇)O(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次暴力转移．

容易发现这部分计算并不是复杂度瓶颈．

因此，该算法的总复杂度为 Θ(√𝑛𝑑(𝑚3 +𝑚2log⁡(𝑛𝑑)))Θ(nd(m3+m2log⁡(nd)))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

编码时，我们可以使用循环卷积的技巧来减小 NTT 的常数．

在实际应用时，我们往往是对一个已知的微分有限的 GF 提取其远处系数，从而 𝑚,𝑑m,d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为常数，也即做到了 Θ(√𝑛log⁡𝑛)Θ(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的远处系数求值．

## 参考文献

  * Alin Bostan, Pierrick Gaudry, and Eric Schost. Linear recurrences with polynomial coefficients and application to integer factorization and Cartier–Manin operator.
  * Min_25 的博客
  * [ZZQ 的博客 - 阶乘模大质数](https://www.cnblogs.com/zzqsblog/p/8408691.html)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/shift.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/shift.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [c-forrest](https://github.com/c-forrest), [hly1204](https://github.com/hly1204), [Konano](https://github.com/Konano), [myeeye](https://github.com/myeeye)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
