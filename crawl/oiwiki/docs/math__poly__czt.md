# Chirp Z 变换 - OI Wiki

- Source: https://oi-wiki.org/math/poly/czt/

# Chirp Z 变换

与离散傅里叶变换类似，Chirp Z 变换是给出多项式 𝑓(𝑥) =∑𝑚−1𝑖=0𝑓𝑖𝑥𝑖 ∈ℂ[𝑥]f(x)=∑i=0m−1fixi∈C[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑞 ∈ℂ ∖{0}q∈C∖{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求出 𝑓(1),𝑓(𝑞),…,𝑓(𝑞𝑛−1)f(1),f(q),…,f(qn−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一种算法，不要求 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为单位根．也可用于数论变换．后文将介绍 Chirp Z 变换与其逆变换．

## Chirp Z 变换

根据定义，Chirp Z 变换可以写作

𝖢𝖹𝖳𝑛:(𝑓(𝑥),𝑞)↦[𝑓(1)𝑓(𝑞)⋯𝑓(𝑞𝑛−1)]CZTn:(f(x),q)↦[f(1)f(q)⋯f(qn−1)]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑓(𝑥) :=∑𝑚−1𝑖=0𝑓𝑖𝑥𝑖 ∈ℂ[𝑥]f(x):=∑i=0m−1fixi∈C[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑞 ∈ℂ ∖{0}q∈C∖{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### Bluestein 算法

考虑

𝑖𝑗=(𝑖2)+(−𝑗2)−(𝑖−𝑗2)ij=(i2)+(−j2)−(i−j2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑖,𝑗 ∈ℤi,j∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以构造

𝐺(𝑥):=𝑛−1∑𝑖=−(𝑚−1)𝑞−(𝑖2)𝑥𝑖,𝐹(𝑥):=𝑚−1∑𝑖=0𝑓𝑖𝑞(−𝑖2)𝑥𝑖.G(x):=∑i=−(m−1)n−1q−(i2)xi,F(x):=∑i=0m−1fiq(−i2)xi.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝐺(𝑥) ∈ℂ[𝑥,𝑥−1]G(x)∈C[x,x−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且对于 𝑖 =0,…,𝑛 −1i=0,…,n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 我们有

[𝑥𝑖](𝐺(𝑥)𝐹(𝑥))=𝑚−1∑𝑗=0(([𝑥𝑖−𝑗]𝐺(𝑥))([𝑥𝑗]𝐹(𝑥)))=𝑚−1∑𝑗=0𝑓𝑗𝑞(−𝑗2)−(𝑖−𝑗2)=𝑞−(𝑖2)𝑓(𝑞𝑖)[xi](G(x)F(x))=∑j=0m−1(([xi−j]G(x))([xj]F(x)))=∑j=0m−1fjq(−j2)−(i−j2)=q−(i2)f(qi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且 𝑞(𝑖+12) =𝑞(𝑖2) ⋅𝑞𝑖q(i+12)=q(i2)⋅qi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，(−𝑖2) =(𝑖+12)(−i2)=(i+12)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．可以由一次多项式乘法完成求算，该算法被称为 Bluestein 算法．

模板（[P6800【模板】Chirp Z-Transform](https://www.luogu.com.cn/problem/P6800)）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``` |  ```text std :: vector < uint > CZT ( const std :: vector < uint >& f , uint q , int n ) { if ( f . empty () || n == 0 ) return std :: vector < uint > ( n ); const int m = f . size (); if ( q == 0 ) { std :: vector < uint > res ( n , f [ 0 ]); for ( int i = 1 ; i < m ; ++ i ) if (( res [ 0 ] += f [ i ]) >= MOD ) res [ 0 ] -= MOD ; return res ; } // H[i] = q^(binom(i + 1, 2)) std :: vector < uint > H ( std :: max ( m , n \- 1 )); H [ 0 ] = 1 ; // H[0] = q^0 uint qi = 1 ; // qi = q^i for ( int i = 1 ; i < ( int ) H . size (); ++ i ) { qi = ( ull ) qi * q % MOD ; // H[i] = q^(binom(i, 2)) * q^i H [ i ] = ( ull ) H [ i \- 1 ] * qi % MOD ; } // F[i] = f[i] * q^(binom(i + 1, 2)) std :: vector < uint > F ( m ); for ( int i = 0 ; i < m ; ++ i ) F [ i ] = ( ull ) f [ i ] * H [ i ] % MOD ; std :: vector < uint > G_p ( m \+ n \- 1 ); // G[i] = q^(-binom(i, 2)), -(m - 1) ≤ i < n uint * const G = G_p . data () \+ ( m \- 1 ); const uint iq = InvMod ( q ); // G[-(m - 1)] = q^(-binom(-(m - 1), 2)), // binom(-(m - 1), 2) = (-(m - 1)) * (-(m - 1) - 1) / 2 // = (m - 1) * m / 2 G [ \- ( m \- 1 )] = PowMod ( iq , ( ull )( m \- 1 ) * m / 2 ); uint qmi = PowMod ( q , m \- 1 ); // q^(-i), -(m - 1) ≤ i < n for ( int i = \- ( m \- 1 ) \+ 1 ; i < n ; ++ i ) { // q^(-binom(i, 2)) = q^(-binom(i - 1, 2)) * q^(-(i - 1)) G [ i ] = ( ull ) G [ i \- 1 ] * qmi % MOD ; // q^(-i) = q^(-(i - 1)) * q^(-1) qmi = ( ull ) qmi * iq % MOD ; } // res[i] = q^(-binom(i, 2)) * f(q^i), 0 ≤ i < n std :: vector < uint > res = MiddleProduct ( G_p , F ); for ( int i = 1 ; i < n ; ++ i ) res [ i ] = ( ull ) res [ i ] * H [ i \- 1 ] % MOD ; return res ; } ```   
---|---  
  
## 逆 Chirp Z 变换

逆 Chirp Z 变换可以写作

𝖨𝖢𝖹𝖳𝑛:([𝑓(1)𝑓(𝑞)⋯𝑓(𝑞𝑛−1)],𝑞)↦𝑓(𝑥)ICZTn:([f(1)f(q)⋯f(qn−1)],q)↦f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑓(𝑥) ∈ℂ[𝑥]<𝑛f(x)∈C[x]<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑞 ∈ℂ ∖{0}q∈C∖{0}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且 𝑞𝑖 ≠𝑞𝑗qi≠qj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑖 ≠𝑗i≠j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立，这是多项式插值的条件．

### Bostan–Schost 算法

回顾 [Lagrange 插值公式](../../numerical/interp/#lagrange-插值法) 为

𝑓(𝑥)=𝑛−1∑𝑖=0⎛⎜ ⎜ ⎜ ⎜⎝𝑓(𝑥𝑖)∏0≤𝑗<𝑛𝑗≠𝑖𝑥−𝑥𝑗𝑥𝑖−𝑥𝑗⎞⎟ ⎟ ⎟ ⎟⎠f(x)=∑i=0n−1(f(xi)∏0≤j<nj≠ix−xjxi−xj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且 𝑥𝑖 ≠𝑥𝑗xi≠xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑖 ≠𝑗i≠j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．与 [多项式的快速插值](../multipoint-eval-interpolation/#多项式的快速插值) 中相同，我们令 𝑀(𝑥) :=∏𝑛−1𝑖=0(𝑥−𝑥𝑖)M(x):=∏i=0n−1(x−xi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据洛必达法则，有

𝑀′(𝑥𝑖)=lim𝑥→𝑥𝑖𝑀(𝑥)𝑥−𝑥𝑖=∏0≤𝑗<𝑛𝑗≠𝑖(𝑥𝑖−𝑥𝑗)M′(xi)=limx→xiM(x)x−xi=∏0≤j<nj≠i(xi−xj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**修正 Lagrange 插值公式** 就是

𝑓(𝑥)=𝑀(𝑥)(𝑛−1∑𝑖=0𝑓(𝑥𝑖)/𝑀′(𝑥𝑖)𝑥−𝑥𝑖)f(x)=M(x)(∑i=0n−1f(xi)/M′(xi)x−xi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么现在我们有

𝑓(𝑥)=𝑀(𝑥)(𝑛−1∑𝑖=0𝑓(𝑞𝑖)/𝑀′(𝑞𝑖)𝑥−𝑞𝑖)f(x)=M(x)(∑i=0n−1f(qi)/M′(qi)x−qi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑀(𝑥) =∏𝑛−1𝑗=0(𝑥−𝑞𝑗)M(x)=∏j=0n−1(x−qj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若我们设 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为偶数，令 𝑛 =2𝑘n=2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐻(𝑥) :=∏𝑘−1𝑗=0(𝑥−𝑞𝑗)H(x):=∏j=0k−1(x−qj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么

𝑀(𝑥)=𝐻(𝑥)⋅𝑞𝑘2⋅𝐻(𝑥𝑞𝑘)M(x)=H(x)⋅qk2⋅H(xqk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这使得我们可以快速计算 𝑀(𝑥)M(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．然后用 Bluestein 算法来计算 𝑀′(1),…,𝑀′(𝑞𝑛−1)M′(1),…,M′(qn−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．令 𝑐𝑖 :=𝑓(𝑞𝑖)/𝑀′(𝑞𝑖)ci:=f(qi)/M′(qi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们有

𝑓(𝑥)=𝑀(𝑥)(𝑛−1∑𝑖=0𝑐𝑖𝑥−𝑞𝑖)f(x)=M(x)(∑i=0n−1cix−qi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 deg⁡𝑓(𝑥) <𝑛deg⁡f(x)<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们只需计算 ∑𝑛−1𝑖=0𝑐𝑖𝑥−𝑞𝑖mod𝑥𝑛∑i=0n−1cix−qimodxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑐𝑖𝑥−𝑞𝑖 ∈ℂ[[𝑥]]cix−qi∈C[[x]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是

𝑛−1∑𝑖=0𝑐𝑖𝑥−𝑞𝑖mod𝑥𝑛=−𝑛−1∑𝑖=0(𝑛−1∑𝑗=0𝑐𝑖𝑞−𝑖(𝑗+1)𝑥𝑗)=−𝑛−1∑𝑗=0𝐶(𝑞−𝑗−1)𝑥𝑗∑i=0n−1cix−qimodxn=−∑i=0n−1(∑j=0n−1ciq−i(j+1)xj)=−∑j=0n−1C(q−j−1)xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝐶(𝑥) =∑𝑛−1𝑖=0𝑐𝑖𝑥𝑖C(x)=∑i=0n−1cixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们可以用 Bluestein 算法来计算 𝐶(𝑞−1),…,𝐶(𝑞−𝑛)C(q−1),…,C(q−n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

简单来说，我们分别进行下面的计算：

  1. 用减治法（decrease and conquer）计算 𝑀(𝑥)M(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 用 Bluestein 算法计算 𝑀′(1),…,𝑀′(𝑞𝑛−1)M′(1),…,M′(qn−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  3. 用 Bluestein 算法计算 𝐶(𝑞−1),…,𝐶(𝑞−𝑛)C(q−1),…,C(q−n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  4. 用一次多项式乘法计算 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

其中每一步的时间复杂度都等于两个次数小于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的多项式相乘的时间复杂度．

模板实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 ``` |  ```text std :: vector < uint > InvCZT ( const std :: vector < uint >& f , uint q ) { if ( f . empty ()) return {}; const int n = f . size (); if ( q == 0 ) { // f[0] = f(1), f[1] = f(0) assert ( n <= 2 ); if ( n == 1 ) return { f [ 0 ]}; // deg(f) < 1 return { f [ 1 ], ( f [ 0 ] \+ MOD \- f [ 1 ]) % MOD }; // deg(f) < 2 } // prod[0 ≤ i < n] (x - q^i) const auto DaC = [ q ]( auto && DaC , int n ) -> std :: vector < uint > { if ( n == 1 ) return { MOD \- 1 , 1u }; // H = prod[0 ≤ i < ⌊n/2⌋] (x - q^i) const std :: vector < uint > H = DaC ( DaC , n / 2 ); // HH = H(x / q^(⌊n/2⌋)) * q^(⌊n/2⌋^2) std :: vector < uint > HH = H ; const uint iqn = InvMod ( PowMod ( q , n / 2 )); uint qq = PowMod ( q , ( ull )( n / 2 ) * ( n / 2 )); for ( int i = 0 ; i <= n / 2 ; ++ i ) HH [ i ] = ( ull ) HH [ i ] * qq % MOD , qq = ( ull ) qq * iqn % MOD ; std :: vector < uint > res = Product ( H , HH ); if ( n & 1 ) { res . resize ( n \+ 1 ); const uint qnm1 = MOD \- PowMod ( q , n \- 1 ); for ( int i = n ; i > 0 ; \-- i ) { if (( res [ i ] += res [ i \- 1 ]) >= MOD ) res [ i ] -= MOD ; res [ i \- 1 ] = ( ull ) res [ i \- 1 ] * qnm1 % MOD ; } } return res ; }; const std :: vector < uint > M = DaC ( DaC , n ); // C[i] = (M'(q^i))^(-1) std :: vector < uint > C = InvModBatch ( CZT ( Deriv ( M ), q , n )); // C[i] = f(q^i) / M'(q^i) for ( int i = 0 ; i < n ; ++ i ) C [ i ] = ( ull ) f [ i ] * C [ i ] % MOD ; // C(x) ← C(q^(-1)x) const uint iq = InvMod ( q ); uint qmi = 1 ; for ( int i = 0 ; i < n ; ++ i ) C [ i ] = ( ull ) C [ i ] * qmi % MOD , qmi = ( ull ) qmi * iq % MOD ; C = CZT ( C , iq , n ); for ( int i = 0 ; i < n ; ++ i ) if ( C [ i ] != 0 ) C [ i ] = MOD \- C [ i ]; std :: vector < uint > res = Product ( M , C ); res . resize ( n ); return res ; } ```   
---|---  
  
## 参考文献

  1. [Bostan, A. (2010). Fast algorithms for polynomials and matrices. JNCF 2010. Algorithms Project, INRIA.](https://specfun.inria.fr/bostan/publications/exposeJNCF.pdf)

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/czt.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/czt.md "edit.link.title")  
>  __本页面贡献者：[hly1204](https://github.com/hly1204), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [CornWorld](https://github.com/CornWorld), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
