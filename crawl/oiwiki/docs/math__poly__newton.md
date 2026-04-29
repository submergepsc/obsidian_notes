# 多项式牛顿迭代 - OI Wiki

- Source: https://oi-wiki.org/math/poly/newton/

# 多项式牛顿迭代

## 描述

给定多项式 𝐺(𝑥,𝑦)G(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，已知多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足：

𝐺(𝑥,𝑓(𝑥))≡0(mod𝑥𝑛)G(x,f(x))≡0(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且存在数值 𝑓1f1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使 𝐺(𝑥,𝑦)G(x,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足以下条件：

  * 𝐺(0,𝑓1) =0G(0,f1)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 𝜕𝐺𝜕𝑦(0,𝑓1) ≠0∂G∂y(0,f1)≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

求出模 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## Newton's Method

考虑倍增．

首先当 𝑛 =1n=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，[𝑥0]𝐺(𝑥,𝑓(𝑥)) =0[x0]G(x,f(x))=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解需要单独求出，假设中的 𝑓1f1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为一个解．

假设现在已经得到了模 𝑥⌈𝑛2⌉x⌈n2⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的解 𝑓⌈𝑛2⌉(𝑥)f⌈n2⌉(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要求模 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的解 𝑓(𝑥) =𝑓𝑛(𝑥)f(x)=fn(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

将 𝐺(𝑥,𝑓(𝑥))G(x,f(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑓(𝑥) =𝑓⌈𝑛2⌉(𝑥)f(x)=f⌈n2⌉(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处进行泰勒展开，有：

+∞∑𝑖=0𝜕𝑖𝐺𝜕𝑦𝑖(𝑥,𝑓⌈𝑛2⌉(𝑥))𝑖!(𝑓(𝑥)−𝑓⌈𝑛2⌉(𝑥))𝑖≡0(mod𝑥𝑛)∑i=0+∞∂iG∂yi(x,f⌈n2⌉(x))i!(f(x)−f⌈n2⌉(x))i≡0(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝑓(𝑥) −𝑓⌈𝑛2⌉(𝑥)f(x)−f⌈n2⌉(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最低非零项次数最低为 ⌈𝑛2⌉⌈n2⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故有：

∀2⩽𝑖:(𝑓(𝑥)−𝑓⌈𝑛2⌉(𝑥))𝑖≡0(mod𝑥𝑛)∀2⩽i:(f(x)−f⌈n2⌉(x))i≡0(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则：

+∞∑𝑖=0𝜕𝑖𝐺𝜕𝑦𝑖(𝑥,𝑓⌈𝑛2⌉(𝑥))𝑖!(𝑓(𝑥)−𝑓⌈𝑛2⌉(𝑥))𝑖≡𝐺(𝑥,𝑓⌈𝑛2⌉(𝑥))+𝜕𝐺𝜕𝑦(𝑥,𝑓⌈𝑛2⌉(𝑥))[𝑓(𝑥)−𝑓⌈𝑛2⌉(𝑥)]≡0(mod𝑥𝑛)∑i=0+∞∂iG∂yi(x,f⌈n2⌉(x))i!(f(x)−f⌈n2⌉(x))i≡G(x,f⌈n2⌉(x))+∂G∂y(x,f⌈n2⌉(x))[f(x)−f⌈n2⌉(x)]≡0(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑓𝑛(𝑥)≡𝑓⌈𝑛2⌉(𝑥)−𝐺(𝑥,𝑓⌈𝑛2⌉(𝑥))𝜕𝐺𝜕𝑦(𝑥,𝑓⌈𝑛2⌉(𝑥))(mod𝑥𝑛)fn(x)≡f⌈n2⌉(x)−G(x,f⌈n2⌉(x))∂G∂y(x,f⌈n2⌉(x))(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

或者

𝑓2𝑛(𝑥)≡𝑓𝑛(𝑥)−𝐺(𝑥,𝑓𝑛(𝑥))𝜕𝐺𝜕𝑦(𝑥,𝑓𝑛(𝑥))(mod𝑥2𝑛)f2n(x)≡fn(x)−G(x,fn(x))∂G∂y(x,fn(x))(modx2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 例题

### [多项式求逆](../elementary-func/#多项式求逆)

设给定函数为 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

𝐺(𝑥,𝑦)=1𝑦−ℎ(𝑥)G(x,y)=1y−h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

应用 Newton's Method 可得：

𝑓2𝑛(𝑥)≡𝑓𝑛(𝑥)−1/𝑓𝑛(𝑥)−ℎ(𝑥)−1/𝑓2𝑛(𝑥)(mod𝑥2𝑛)≡2𝑓𝑛(𝑥)−𝑓2𝑛(𝑥)ℎ(𝑥)(mod𝑥2𝑛)f2n(x)≡fn(x)−1/fn(x)−h(x)−1/fn2(x)(modx2n)≡2fn(x)−fn2(x)h(x)(modx2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时间复杂度

𝑇(𝑛)=𝑇(𝑛2)+𝑂(𝑛log⁡𝑛)=𝑂(𝑛log⁡𝑛)T(n)=T(n2)+O(nlog⁡n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### [多项式开方](../elementary-func/#多项式开方)

设给定函数为 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

𝐺(𝑥,𝑦)=𝑦2−ℎ(𝑥)≡0G(x,y)=y2−h(x)≡0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

应用 Newton's Method 可得：

𝑓2𝑛(𝑥)≡𝑓𝑛(𝑥)−𝑓2𝑛(𝑥)−ℎ(𝑥)2𝑓𝑛(𝑥)(mod𝑥2𝑛)≡𝑓2𝑛(𝑥)+ℎ(𝑥)2𝑓𝑛(𝑥)(mod𝑥2𝑛)f2n(x)≡fn(x)−fn2(x)−h(x)2fn(x)(modx2n)≡fn2(x)+h(x)2fn(x)(modx2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时间复杂度

𝑇(𝑛)=𝑇(𝑛2)+𝑂(𝑛log⁡𝑛)=𝑂(𝑛log⁡𝑛)T(n)=T(n2)+O(nlog⁡n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### [多项式指数函数](../elementary-func/#多项式对数函数--指数函数)

设给定函数为 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

𝐺(𝑥,𝑦)=ln⁡𝑦−ℎ(𝑥)G(x,y)=ln⁡y−h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

应用 Newton's Method 可得：

𝑓2𝑛(𝑥)≡𝑓𝑛(𝑥)−ln⁡𝑓𝑛(𝑥)−ℎ(𝑥)1/𝑓𝑛(𝑥)(mod𝑥2𝑛)≡𝑓𝑛(𝑥)(1−ln⁡𝑓𝑛(𝑥)+ℎ(𝑥))(mod𝑥2𝑛)f2n(x)≡fn(x)−ln⁡fn(x)−h(x)1/fn(x)(modx2n)≡fn(x)(1−ln⁡fn(x)+h(x))(modx2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

时间复杂度

𝑇(𝑛)=𝑇(𝑛2)+𝑂(𝑛log⁡𝑛)=𝑂(𝑛log⁡𝑛)T(n)=T(n2)+O(nlog⁡n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 手算演示

为了方便理解，这里举几个例子演示一下算法流程．

### 复数多项式模多项式的平方根

假设 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个不被 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除（有常数项）的复数多项式，求它对模 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的平方根．

我们有方程：

𝐺(𝑓(𝑥))=𝑓2(𝑥)−ℎ(𝑥)≡0(mod𝑥𝑛)G(f(x))=f2(x)−h(x)≡0(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Taylor 展开 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到下式．注意这里是对 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的展开，所以导数都是对 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的偏导数，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在这里是当成常数算的．

𝐺(𝑓(𝑥))=+∞∑𝑖=0𝐺(𝑖)(𝑓0(𝑥))𝑖!(𝑓(𝑥)−𝑓0(𝑥))𝑖=𝐺(𝑓0(𝑥))+2𝑓0(𝑥)(𝑓(𝑥)−𝑓0(𝑥))+(𝑓(𝑥)−𝑓0(𝑥))2G(f(x))=∑i=0+∞G(i)(f0(x))i!(f(x)−f0(x))i=G(f0(x))+2f0(x)(f(x)−f0(x))+(f(x)−f0(x))2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

用倍增计算．假设倍增中的中间结果是 𝑓0(𝑥),𝑓1(𝑥),…,𝑓𝑗(𝑥)f0(x),f1(x),…,fj(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或者数学严谨地说 𝑓𝑗(𝑥)fj(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是满足 𝐺(𝑓𝑗(𝑥)) ≡0(mod𝑥2𝑗)G(fj(x))≡0(modx2j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个复数多项式，且为了唯一性它同时满足以下两个条件：

  * 𝑓𝑗(𝑥)fj(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次数不超过 𝑥2𝑗x2j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 𝑓𝑗+𝑘(𝑥) −𝑓𝑗(𝑥) ≡0(mod𝑥2𝑗)fj+k(x)−fj(x)≡0(modx2j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对所有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

把 𝑓𝑗+1(𝑥)fj+1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓𝑗(𝑥)fj(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代入上面的式子就有：

𝐺(𝑓𝑗+1(𝑥))=𝐺(𝑓𝑗(𝑥))+2𝑓𝑗(𝑓𝑗+1(𝑥)−𝑓𝑗(𝑥))+(𝑓𝑗+1(𝑥)−𝑓𝑗(𝑥))2≡0(mod𝑥2𝑗+1)G(fj+1(x))=G(fj(x))+2fj(fj+1(x)−fj(x))+(fj+1(x)−fj(x))2≡0(modx2j+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

显然 𝑓𝑗+1(𝑥) −𝑓𝑗(𝑥)fj+1(x)−fj(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然是 𝑥2𝑗x2j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数．于是得到

𝑓𝑗+1(𝑥)≡𝑓𝑗(𝑥)−𝑓2𝑗(𝑥)−ℎ(𝑥)2𝑓𝑗(𝑥)≡𝑓𝑗(𝑥)2+ℎ(𝑥)2𝑓𝑗(𝑥)(mod𝑥2𝑗+1)fj+1(x)≡fj(x)−fj2(x)−h(x)2fj(x)≡fj(x)2+h(x)2fj(x)(modx2j+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果 𝑓𝑗(𝑥)fj(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在，那么 2𝑓𝑗(𝑥)2fj(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不被 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除（有常数项），所以必然有模 𝑥2𝑗+1x2j+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆元．因此数列 𝑓0,𝑓1…,𝑓𝑗f0,f1…,fj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在当且仅当 𝑓0f0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在．不被 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除的复数多项式 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的平方根是一定存在的，因为 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模掉 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是个普通非零复数，一定有两个平方根．所以可以对所有有常数项的 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用这个算法．

选 ℎ(𝑥) =𝑥 +1h(x)=x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 举例计算如下：

  * 𝑓0(𝑥) =1f0(x)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑓1(𝑥) =12+𝑥+12×1mod 𝑥2 =12𝑥 +1f1(x)=12+x+12×1modx2=12x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑓2(𝑥) =(12𝑥+1)2+𝑥+12×(12𝑥+1)mod 𝑥4 =116𝑥3 −18𝑥2 +12𝑥 +1f2(x)=(12x+1)2+x+12×(12x+1)modx4=116x3−18x2+12x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),……![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑓0(𝑥) = −1f0(x)=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑓1(𝑥) =(−1)2+𝑥+12×(−1)mod 𝑥2 = −12𝑥 −1f1(x)=(−1)2+x+12×(−1)modx2=−12x−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),……![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（等于前一个取负）

可以验证两个都是正确的模平方根多项式列．

### 整数模素数幂的平方根

牛顿迭代算法还可以迁移到整数模素数的幂的情况． 假设 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个不被 3 整除的「方便的」整数．（「方便」指「必然有解」，具体条件后文再言）假设要算 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 3𝑛3n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的平方根 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．有方程：

𝐺(𝑓)=𝑓2−ℎ≡0(mod3𝑛)G(f)=f2−h≡0(mod3n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Taylor 展开 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到：

𝐺(𝑓)=+∞∑𝑖=0𝐺(𝑖)(𝑓0)𝑖!(𝑓−𝑓0)𝑖=𝐺(𝑓0)+2𝑓0(𝑓−𝑓0)+(𝑓−𝑓0)2G(f)=∑i=0+∞G(i)(f0)i!(f−f0)i=G(f0)+2f0(f−f0)+(f−f0)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

用倍增计算．假设倍增中得到的中间结果是 𝑓0,𝑓1,…,𝑓𝑗f0,f1,…,fj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或者严谨地说 𝑓𝑗fj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是满足 𝐺(𝑓𝑗) ≡0(mod32𝑗)G(fj)≡0(mod32j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个整数，且为了唯一性它同时满足以下两个条件：

  * 0 <𝑓𝑗 <32𝑗0<fj<32j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 𝑓𝑗+𝑘 −𝑓𝑗 ≡0(mod32𝑗)fj+k−fj≡0(mod32j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对所有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

把 𝑓𝑗+1fj+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓𝑗fj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代入上面的式子就有：

𝐺(𝑓𝑗+1)=𝐺(𝑓𝑗)+2𝑓𝑗(𝑓𝑗+1−𝑓𝑗)+(𝑓𝑗+1−𝑓𝑗)2≡0(mod32𝑗+1)G(fj+1)=G(fj)+2fj(fj+1−fj)+(fj+1−fj)2≡0(mod32j+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

显然 𝑓𝑗+1 −𝑓𝑗fj+1−fj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必然是 32𝑗32j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数．于是得到

𝑓𝑗+1≡𝑓𝑗−𝑓2𝑗−ℎ2𝑓𝑗≡𝑓2𝑗+ℎ2𝑓𝑗(mod32𝑗+1)fj+1≡fj−fj2−h2fj≡fj2+h2fj(mod32j+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果 𝑓𝑗fj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在，那么 2𝑓𝑗2fj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不被 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除，所以必然有模 32𝑗+132j+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆元．因此数列 𝑓0,𝑓1…,𝑓𝑗f0,f1…,fj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在当且仅当 𝑓0f0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在．不被 3 整除的整数 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的平方根要么不存在，要么有两个．所以 ℎh![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有模 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 平方根就是整个算法能跑的唯一条件．

这里选 ℎ =46h=46![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 实际计算示例．

  * 𝑓0 =1f0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑓1 =12+462×1mod 9 =1f1=12+462×1mod9=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑓2 =12+462×1mod 81 =64f2=12+462×1mod81=64![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑓3 =642+462×64mod 6561 =955f3=642+462×64mod6561=955![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),……![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑓0 =2f0=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑓1 =22+462×2mod 9 =8f1=22+462×2mod9=8![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑓2 =82+462×8mod 81 =17f2=82+462×8mod81=17![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑓3 =172+462×17mod 6561 =5606f3=172+462×17mod6561=5606![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),……![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（等于前一个取负）

可以验证一下两个都是正确的模平方根数列．

## 代数证明

这一节对前文进行引申，用抽象代数的语言证明只要 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足初始解条件，牛顿法对所有的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都能给出解，并且可以得到全部的解．

### 有解的证明

引理 1

设 [整环](../../algebra/ring-theory/#整环) 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有多项式或 [形式幂级数](../../algebra/ring-theory/#形式幂级数环) 𝑓(𝑋) =∑𝑖≥0𝑎𝑖𝑋𝑖f(X)=∑i≥0aiXi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟,𝑝 ∈𝑅r,p∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑓(𝑟) ∈𝑅𝑝f(r)∈Rp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（亦即 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑓(𝑋)f(X)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的根）且 𝑓′(𝑟) ∈𝑅f′(r)∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下是可逆的．这里 𝑓′(𝑋) :=∑𝑖≥0(𝑖 +1)𝑎𝑖+1𝑋𝑖f′(X):=∑i≥0(i+1)ai+1Xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑓(𝑋)f(X)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **形式导数** ．那么 𝑓(𝑟−𝑓(𝑟)𝑓′(𝑟)) ≡0(mod𝑝2)f(r−f(r)f′(r))≡0(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

对所有 𝑠 ∈𝑅s∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，

𝑓(𝑟+𝑠𝑝)=∑𝑖≥0𝑎𝑖(𝑟+𝑠𝑝)𝑖=∑𝑖≥0𝑎𝑖𝑟𝑖+𝑠𝑝∑𝑖≥1𝑖𝑎𝑖𝑟𝑖−1+𝑠2𝑝2(…)=𝑓(𝑟)+𝑠𝑝𝑓′(𝑟)+𝑠2𝑝2(𝑓″(𝑟)2!+⋯),f(r+sp)=∑i≥0ai(r+sp)i=∑i≥0airi+sp∑i≥1iairi−1+s2p2(…)=f(r)+spf′(r)+s2p2(f″(r)2!+⋯),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以

𝑓(𝑟+𝑠𝑝)∈𝑅𝑝2⟺𝑓(𝑟)+𝑓′(𝑟)𝑠𝑝∈𝑅𝑝2f(r+sp)∈Rp2⟺f(r)+f′(r)sp∈Rp2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝑓(𝑟) ∈𝑅𝑝f(r)∈Rp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑓′(𝑟)f′(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可逆，所以取 𝑠𝑝 = −𝑓(𝑟)𝑓′(𝑟)sp=−f(r)f′(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可，这里 1𝑓′(𝑟)1f′(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑝2p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的逆元．因为 𝑓′(𝑟)f′(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下可逆，所以它在模 𝑝2p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下也必定存在逆元：设有 𝑎,𝑏,𝑐 ∈𝑅a,b,c∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使 𝑎𝑓′(𝑟) =𝑏𝑝 +1af′(r)=bp+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(𝑟) =𝑐𝑝f(r)=cp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 (𝑎2𝑓′(𝑟)−2)𝑓′(𝑟) =𝑏2𝑝2 +1(a2f′(r)−2)f′(r)=b2p2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故可以取 𝑠 =𝑐(2 −𝑎2𝑓′(𝑟))s=c(2−a2f′(r))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于域 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的多项式环 𝑘[𝑋]k[X]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设有 𝐺(𝑋,𝑌) ∈𝑘[𝑋,𝑌]G(X,Y)∈k[X,Y]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓𝑛 ∈𝑘[𝑋]fn∈k[X]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使 𝐺(𝑋,𝑓𝑛(𝑋)) ∈𝑘[𝑋]𝑋𝑛G(X,fn(X))∈k[X]Xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么应用引理 1 就可得到

𝐺(𝑋,𝑓𝑛(𝑋)−𝐺(𝑋,𝑓𝑛(𝑋))𝜕𝐺𝜕𝑌(𝑋,𝑓𝑛(𝑋)))≡0(mod𝑋2𝑛)G(X,fn(X)−G(X,fn(X))∂G∂Y(X,fn(X)))≡0(modX2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而倍增的初始条件只要有 𝑓1 ∈𝑘f1∈k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝐺(𝑋,𝑓1) ≡0(mod𝑋)G(X,f1)≡0(modX)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜕𝐺𝜕𝑌(𝑋,𝑓1) ≢0(mod𝑋)∂G∂Y(X,f1)≢0(modX)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．后一个条件保证了 𝜕𝐺𝜕𝑌∂G∂Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有非零常数项，同时因为 𝑋∣𝐺(𝑋,𝑓𝑛(𝑋))𝜕𝐺𝜕𝑌(𝑋,𝑓𝑛(𝑋))X|G(X,fn(X))∂G∂Y(X,fn(X))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而对所有的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝜕𝐺𝜕𝑌(𝑋,𝑓𝑛)∂G∂Y(X,fn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是模 𝑋𝑛Xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下可逆的，也就满足了下一次迭代的条件．

### 得到全部解的证明

引理 2

若 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 [UFD](../../algebra/ring-theory/#唯一分解整环)，𝑓,𝑟,𝑝f,r,p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义同引理 1．则引理 1 给出的 𝑟 −𝑓(𝑟)𝑓′(𝑟)r−f(r)f′(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑝2p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下唯一满足以下两条件的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值：

  * 𝑓(𝑥) ∈𝑅𝑝2f(x)∈Rp2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑥 −𝑟 ∈𝑅𝑝x−r∈Rp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

亦即

∀𝑥∈𝑅,𝑝2∣𝑓(𝑥)∧𝑝∣(𝑥−𝑟)⟹𝑥≡𝑟−𝑓(𝑟)𝑓′(𝑟)(mod𝑝2)∀x∈R,p2∣f(x)∧p∣(x−r)⟹x≡r−f(r)f′(r)(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

令 𝑠 = −𝑓(𝑟)𝑓′(𝑟)𝑝s=−f(r)f′(r)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑢 =𝑟 +𝑠𝑝u=r+sp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，引理 1 保证 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足两个条件，且 𝑓(𝑟) +𝑓′(𝑟)𝑠𝑝 ∈𝑅𝑝2f(r)+f′(r)sp∈Rp2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． 设 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是满足上述条件的值，则有 𝑣 =𝑟 +𝑡𝑝v=r+tp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓(𝑟) +𝑓′(𝑟)𝑡𝑝 ∈𝑅𝑝2f(r)+f′(r)tp∈Rp2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． 于是有 𝑓′(𝑟)(𝑡 −𝑠)𝑝 ∈𝑅𝑝2f′(r)(t−s)p∈Rp2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣 −𝑢 ∈𝑅𝑝2v−u∈Rp2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

牛顿法可以保证得到模 𝑋2𝑛X2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全部解．假设 𝐺(𝑋,ℎ) ≡0(mod𝑋2𝑛)G(X,h)≡0(modX2n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么令 ℎ2𝑖 :=ℎ(mod𝑋2𝑖)h2i:=h(modX2i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后取 𝑓1 =ℎ1f1=h1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并用牛顿法，根据引理 2 可得 𝑓2𝑖 ≡ℎ2𝑖(mod𝑋2𝑖)f2i≡h2i(modX2i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以一定有 𝑓2𝑛 =ℎf2n=h![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

上面的论证也说明了，在 𝜕𝐺𝜕𝑦(0,𝑦)∂G∂y(0,y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 永远可逆时，𝐺(𝑋,𝑓) ≡0(mod𝑋𝑛)G(X,f)≡0(modXn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解的个数等于 𝐺(0,𝑓) ≡0(mod𝑋)G(0,f)≡0(modX)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解的个数．这个结论并非平凡．请看下面的例子．

牛顿法无效时解的个数随次数而变多的例子

模 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下 𝑋2X2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的平方根只有 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是模 𝑋4X4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下 𝑋2X2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的平方根有 𝑋, −𝑋,𝑋3 +𝑋,…X,−X,X3+X,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/newton.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/newton.md "edit.link.title")  
>  __本页面贡献者：[fps5283](https://github.com/fps5283), [Marcythm](https://github.com/Marcythm), [97littleleaf11](https://github.com/97littleleaf11), [shuzhouliu](https://github.com/shuzhouliu), [Enter-tainer](https://github.com/Enter-tainer), [H-J-Granger](https://github.com/H-J-Granger), [Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [abc1763613206](https://github.com/abc1763613206), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [EndlessCheng](https://github.com/EndlessCheng), [Great-designer](https://github.com/Great-designer), [hly1204](https://github.com/hly1204), [hsfzLZH1](https://github.com/hsfzLZH1), [huayucaiji](https://github.com/huayucaiji), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [test12345-pupil](https://github.com/test12345-pupil), [untitledunrevised](https://github.com/untitledunrevised), [zjkmxy](https://github.com/zjkmxy)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
