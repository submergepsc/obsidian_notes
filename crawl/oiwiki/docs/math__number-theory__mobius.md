# 莫比乌斯反演 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/mobius/

# 莫比乌斯反演

前置知识：[数论分块](../sqrt-decomposition/)、[狄利克雷卷积](../dirichlet/#dirichlet-卷积)

莫比乌斯反演是数论中的重要内容．对于一些函数 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果很难直接求出它的值，而容易求出其倍数和或约数和 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么可以通过莫比乌斯反演简化运算，求得 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

## 莫比乌斯函数

莫比乌斯函数（Möbius 函数）定义为

𝜇(𝑛)=⎧{ {⎨{ {⎩1,𝑛=1,0,𝑛 is divisible by a square >1,(−1)𝑘,𝑛 is the product of 𝑘 distinct primes.μ(n)={1,n=1,0,n is divisible by a square >1,(−1)k,n is the product of k distinct primes.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

具体地，假设正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有素因数分解 𝑛 =∏𝑘𝑖=1𝑝𝑒𝑖𝑖n=∏i=1kpiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数，𝑒𝑖ei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是正整数．那么，三种情形分别对应：

  1. 𝜇(1) =1μ(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 当存在 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑒𝑖 >1ei>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即存在任何素因数出现超过一次时，𝜇(𝑛) =0μ(n)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  3. 否则，对于所有 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 𝑒𝑖 =1ei=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即任何素因数都只出现一次时，𝜇(𝑛) =( −1)𝑘μ(n)=(−1)k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是互异素因子的个数．

### 性质

根据定义容易验证，莫比乌斯函数 𝜇(𝑛)μ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数，但不是完全积性函数．除此之外，最为重要的性质是下述恒等式：

性质

对于正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

∑𝑑∣𝑛𝜇(𝑑)=[𝑛=1]={1,𝑛=1,0,𝑛≠1.∑d∣nμ(d)=[n=1]={1,n=1,0,n≠1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 [ ⋅][⋅]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Iverson 括号．

证明

令 𝑛 =∏𝑘𝑖=1𝑝𝑒𝑖𝑖n=∏i=1kpiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设 𝑛′ =∏𝑘𝑖=1𝑝𝑖n′=∏i=1kpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据 [二项式定理](../../combinatorics/combination/#二项式定理)，有

∑𝑑∣𝑛𝜇(𝑑)=∑𝑑∣𝑛′𝜇(𝑑)=𝑘∑𝑖=0(𝑘𝑖)(−1)𝑖=(1+(−1))𝑘=[𝑘=0]=[𝑛=1].∑d∣nμ(d)=∑d∣n′μ(d)=∑i=0k(ki)(−1)i=(1+(−1))k=[k=0]=[n=1].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用 Dirichlet 卷积，该表达式可以写作 𝜀 =1 ∗𝜇ε=1∗μ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．也就是说，莫比乌斯函数是常值函数 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Dirichlet 逆．

这一性质有一个很常见的应用：

[𝑖⟂𝑗]=[gcd(𝑖,𝑗)=1]=∑𝑑∣gcd(𝑖,𝑗)𝜇(𝑑)=∑𝑑[𝑑∣𝑖][𝑑∣𝑗]𝜇(𝑑).[i⟂j]=[gcd(i,j)=1]=∑d∣gcd(i,j)μ(d)=∑d[d∣i][d∣j]μ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它将互素的条件转化为关于莫比乌斯函数的求和式，方便进一步推导．

### 求法

如果需要对单个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算莫比乌斯函数 𝜇(𝑛)μ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，可以利用它的 [质因数分解](../pollard-rho/)．例如，在 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不太大时，可以在 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内求出 𝜇(𝑛)μ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text int mu ( int n ) { int res = 1 ; for ( int i = 2 ; i * i <= n ; ++ i ) { if ( n % i == 0 ) { n /= i ; // Check if square-free. if ( n % i == 0 ) return 0 ; res = \- res ; } } // The remaining factor must be prime. if ( n > 1 ) res = \- res ; return res ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text def mu ( n ): res = 1 i = 2 while i * i <= n : if n % i == 0 : n //= i # Check if square-free if n % i == 0 : return 0 res = \- res i += 1 # The remaining factor must be prime if n > 1 : res = \- res return res ```   
---|---  
  
如果需要对前 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个正整数预处理出 𝜇(𝑛)μ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，可以利用它是积性函数，通过 [线性筛](../sieve/#筛法求莫比乌斯函数) 在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text std :: vector < int > get_mu ( int n ) { std :: vector < int > mu ( n \+ 1 ), primes ; std :: vector < bool > not_prime ( n \+ 1 ); primes . reserve ( n ); mu [ 1 ] = 1 ; for ( int x = 2 ; x <= n ; ++ x ) { if ( ! not_prime [ x ]) { primes . push_back ( x ); mu [ x ] = -1 ; } for ( int p : primes ) { if ( x * p > n ) break ; not_prime [ x * p ] = true ; if ( x % p == 0 ) { mu [ x * p ] = 0 ; break ; } else { mu [ x * p ] = \- mu [ x ]; } } } return mu ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text def get_mu ( n ): mu = [ 0 ] * ( n \+ 1 ) primes = [] not_prime = [ False ] * ( n \+ 1 ) mu [ 1 ] = 1 for x in range ( 2 , n \+ 1 ): if not not_prime [ x ]: primes . append ( x ) mu [ x ] = \- 1 for p in primes : if x * p > n : break not_prime [ x * p ] = True if x % p == 0 : mu [ x * p ] = 0 break else : mu [ x * p ] = \- mu [ x ] return mu ```   
---|---  
  
## 莫比乌斯反演

莫比乌斯函数最重要的应用就是莫比乌斯反演．

莫比乌斯反演

设 𝑓(𝑛),𝑔(𝑛)f(n),g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是两个数论函数．那么，有

𝑓(𝑛)=∑𝑑∣𝑛𝑔(𝑑)⟺𝑔(𝑛)=∑𝑑∣𝑛𝜇(𝑛𝑑)𝑓(𝑑).f(n)=∑d∣ng(d)⟺g(n)=∑d∣nμ(nd)f(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明一

直接验证，有：

∑𝑑∣𝑛𝜇(𝑛𝑑)𝑓(𝑑)=∑𝑑∣𝑛𝜇(𝑛𝑑)∑𝑘∣𝑑𝑔(𝑘)=∑𝑘∣𝑛𝑔(𝑘)∑𝑑[𝑘∣𝑑∣𝑛]𝜇(𝑛𝑑)=∑𝑘∣𝑛𝑔(𝑘)∑𝑑∣𝑛[𝑛𝑑∣𝑛𝑘]𝜇(𝑛𝑑)=∑𝑘∣𝑛𝑔(𝑘)[𝑛𝑘=1]=𝑔(𝑛).∑d∣nμ(nd)f(d)=∑d∣nμ(nd)∑k∣dg(k)=∑k∣ng(k)∑d[k∣d∣n]μ(nd)=∑k∣ng(k)∑d∣n[nd∣nk]μ(nd)=∑k∣ng(k)[nk=1]=g(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

式子变形的关键在于交换求和次序，并注意到 𝑘 ∣𝑑 ∣𝑛k∣d∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就等价于 𝑛𝑑 ∣𝑛𝑘nd∣nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．倒数第二个等号相当于对 𝑛𝑘nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的因子 𝑛𝑑nd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的莫比乌斯函数求和，所以就等于 [𝑛𝑘=1][nk=1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这一表达式仅在 𝑛 =𝑘n=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处不是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，最后就会得到 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明二

利用 Dirichlet 卷积，命题等价于

𝑓=1∗𝑔⟺𝑔=𝜇∗𝑓.f=1∗g⟺g=μ∗f.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用 1 ∗𝜇 =𝜀1∗μ=ε![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在左式的等号两侧同时对 𝜇μ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做卷积，就得到

𝑓∗𝜇=(1∗𝑔)∗𝜇=(1∗𝜇)∗𝑔=𝜀∗𝑔=𝑔.f∗μ=(1∗g)∗μ=(1∗μ)∗g=ε∗g=g.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在涉及各种整除关系的数论函数求和中，莫比乌斯反演是有力的变形工具．

例子

  1. [欧拉函数](../euler-totient/) 𝜑(𝑛)φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足关系式 𝑛 =∑𝑑∣𝑛𝜑(𝑑)n=∑d∣nφ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即 id =1 ∗𝜑id=1∗φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对它进行反演，就得到 𝜑 =𝜇 ∗idφ=μ∗id![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即

𝜑(𝑛)=∑𝑑∣𝑛𝑑𝜇(𝑛𝑑).φ(n)=∑d∣ndμ(nd).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 除数函数 𝜎𝑘(𝑛) =∑𝑑∣𝑛𝑑𝑘σk(n)=∑d∣ndk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即 𝜎𝑘 =1 ∗id𝑘σk=1∗idk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对它进行反演，就得到 id𝑘 =𝜇 ∗𝜎𝑘idk=μ∗σk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即

𝑛𝑘=∑𝑑∣𝑛𝜇(𝑛𝑑)𝜎𝑘(𝑑).nk=∑d∣nμ(nd)σk(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. 互异素因子数目函数 𝜔(𝑛) =∑𝑑∣𝑛[𝑑 ∈𝐏]ω(n)=∑d∣n[d∈P]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即 𝜔 =1 ∗𝟏𝐏ω=1∗1P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝟏𝐏1P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数集 𝐏P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的指示函数．对它进行反演，就得到 𝟏𝐏 =𝜇 ∗𝜔1P=μ∗ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即

[𝑛∈𝐏]=∑𝑑∣𝑛𝜇(𝑛𝑑)𝜔(𝑑).[n∈P]=∑d∣nμ(nd)ω(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  4. 考察满足 log⁡𝑛 =∑𝑑∣𝑛Λ(𝑑)log⁡n=∑d∣nΛ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数论函数 Λ(𝑛)Λ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．它就是对数函数的莫比乌斯反演，也称为 von Mangoldt 函数：

Λ(𝑛)=∑𝑑∣𝑛𝜇(𝑛𝑑)log⁡𝑑={log⁡𝑝,𝑛=𝑝𝑒, 𝑝∈𝐏, 𝑒∈𝐍+,0,otherwise.Λ(n)=∑d∣nμ(nd)log⁡d={log⁡p,n=pe, p∈P, e∈N+,0,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

附：Λ(𝑛)Λ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表达式的证明

对于素数幂 𝑛 =𝑝𝑒 (𝑒 ∈𝐍+)n=pe (e∈N+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

Λ(𝑛)=𝑒∑𝑖=0𝜇(𝑝𝑒−𝑖)log⁡𝑝𝑖=log⁡𝑝𝑒−log⁡𝑝𝑒−1=log⁡𝑝.Λ(n)=∑i=0eμ(pe−i)log⁡pi=log⁡pe−log⁡pe−1=log⁡p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于 𝑛 =1n=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然有 Λ(𝑛) =log⁡1 =0Λ(n)=log⁡1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于其他合数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

Λ(𝑛)=∑𝑑∣𝑛𝜇(𝑑)(log⁡𝑛−log⁡𝑑)=⎛⎜ ⎜⎝∑𝑑∣𝑛𝜇(𝑑)⎞⎟ ⎟⎠log⁡𝑛−∑𝑑∣𝑛𝜇(𝑑)log⁡𝑑.Λ(n)=∑d∣nμ(d)(log⁡n−log⁡d)=(∑d∣nμ(d))log⁡n−∑d∣nμ(d)log⁡d.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据莫比乌斯函数的性质，log⁡𝑛log⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一项的系数为 [𝑛 =1] =0[n=1]=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于后面的一项，可以进一步将 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解为素因数之积．对于任何素数 𝑝 ∣𝑛p∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考察 log⁡𝑝log⁡p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数，都有：

−∑𝑝∣𝑑∣𝑛𝜇(𝑑)=∑(𝑑/𝑝)∣(𝑛/𝑝)𝜇(𝑑𝑝)=[𝑛𝑝=1]=0.−∑p∣d∣nμ(d)=∑(d/p)∣(n/p)μ(dp)=[np=1]=0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由此，对于不止一个素因子的合数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 Λ(𝑛) =0Λ(n)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 拓展形式

除了上述基本形式外，莫比乌斯反演还有一些常见的拓展形式．首先，可以考虑它的倍数和形式．

拓展一

设 𝑓(𝑛),𝑔(𝑛)f(n),g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是两个数论函数．那么，有

𝑓(𝑛)=∑𝑛∣𝑑𝑔(𝑑)⟺𝑔(𝑛)=∑𝑛∣𝑑𝜇(𝑑𝑛)𝑓(𝑑).f(n)=∑n∣dg(d)⟺g(n)=∑n∣dμ(dn)f(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

直接验证，有：

∑𝑛∣𝑑𝜇(𝑑𝑛)𝑓(𝑑)=∑𝑛∣𝑑𝜇(𝑑𝑛)∑𝑑∣𝑘𝑔(𝑘)=∑𝑛∣𝑘𝑔(𝑘)∑𝑑[𝑛∣𝑑∣𝑘]𝜇(𝑑𝑛)=∑𝑛∣𝑘𝑔(𝑘)∑𝑛∣𝑑[𝑑𝑛∣𝑘𝑛]𝜇(𝑑𝑛)=∑𝑛∣𝑘𝑔(𝑘)[𝑘𝑛=1]=𝑔(𝑛).∑n∣dμ(dn)f(d)=∑n∣dμ(dn)∑d∣kg(k)=∑n∣kg(k)∑d[n∣d∣k]μ(dn)=∑n∣kg(k)∑n∣d[dn∣kn]μ(dn)=∑n∣kg(k)[kn=1]=g(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这和基本形式的推导完全对偶．

其次，莫比乌斯反演并不仅限于加法，它实际上对于任何 [Abel 群](../../algebra/basic/#群) 中的运算都成立．例如，它有如下的乘法形式：

拓展二

设 𝑓(𝑛),𝑔(𝑛)f(n),g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是两个数论函数．那么，有

𝑓(𝑛)=∏𝑑∣𝑛𝑔(𝑑)⟺𝑔(𝑛)=∏𝑑∣𝑛𝑓(𝑑)𝜇(𝑛/𝑑).f(n)=∏d∣ng(d)⟺g(n)=∏d∣nf(d)μ(n/d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

直接验证，有：

∏𝑑∣𝑛𝑓(𝑑)𝜇(𝑛/𝑑)=∏𝑑∣𝑛⎛⎜ ⎜⎝∏𝑘∣𝑑𝑔(𝑘)⎞⎟ ⎟⎠𝜇(𝑛/𝑑)=∏𝑘∣𝑛𝑔(𝑘)↑(∑𝑑[𝑘∣𝑑∣𝑛]𝜇(𝑛𝑑))=∏𝑘∣𝑛𝑔(𝑘)↑⎛⎜ ⎜⎝∑𝑑∣𝑛[𝑛𝑑∣𝑛𝑘]𝜇(𝑛𝑑)⎞⎟ ⎟⎠=∏𝑘∣𝑛𝑔(𝑘)↑[𝑛𝑘=1]=𝑔(𝑛).∏d∣nf(d)μ(n/d)=∏d∣n(∏k∣dg(k))μ(n/d)=∏k∣ng(k)↑(∑d[k∣d∣n]μ(nd))=∏k∣ng(k)↑(∑d∣n[nd∣nk]μ(nd))=∏k∣ng(k)↑[nk=1]=g(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑎 ↑𝑏 =𝑎𝑏a↑b=ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Knuth 箭头．对比基本形式的证明可以发现，唯一的区别就是加法换成了乘法，且乘法换成了取幂．

从 Dirichlet 卷积的角度看，莫比乌斯反演只是利用了「莫比乌斯函数是常值函数的 Dirichlet 逆」这一点．容易想象，类似莫比乌斯反演的关系对于一般的 [Dirichlet 逆](../dirichlet/#dirichlet-卷积) 同样成立．

拓展三

设 𝑓(𝑛),𝑔(𝑛),𝛼(𝑛)f(n),g(n),α(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是数论函数，且 𝛼−1(𝑛)α−1(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝛼(𝑛)α(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Dirichlet 逆，即

[𝑛=1]=∑𝑑∣𝑛𝛼(𝑛𝑑)𝛼−1(𝑑).[n=1]=∑d∣nα(nd)α−1(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么，有

𝑓(𝑛)=∑𝑑∣𝑛𝛼(𝑛𝑑)𝑔(𝑑)⟺𝑔(𝑛)=∑𝑑∣𝑛𝛼−1(𝑛𝑑)𝑓(𝑑).f(n)=∑d∣nα(nd)g(d)⟺g(n)=∑d∣nα−1(nd)f(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

直接验证，有：

∑𝑑∣𝑛𝛼−1(𝑛𝑑)𝑓(𝑑)=∑𝑑∣𝑛𝛼−1(𝑛𝑑)∑𝑘∣𝑑𝛼(𝑑𝑘)𝑔(𝑘)=∑𝑘∣𝑛𝑔(𝑘)∑𝑑[𝑘∣𝑑∣𝑛]𝛼(𝑑𝑘)𝛼−1(𝑛𝑑)=∑𝑘∣𝑛𝑔(𝑘)∑𝑑∣𝑛[𝑛𝑑∣𝑛𝑘]𝛼(𝑑𝑘)𝛼−1(𝑛/𝑘𝑑/𝑘)=∑𝑘∣𝑛𝑔(𝑘)[𝑛𝑘=1]=𝑔(𝑛).∑d∣nα−1(nd)f(d)=∑d∣nα−1(nd)∑k∣dα(dk)g(k)=∑k∣ng(k)∑d[k∣d∣n]α(dk)α−1(nd)=∑k∣ng(k)∑d∣n[nd∣nk]α(dk)α−1(n/kd/k)=∑k∣ng(k)[nk=1]=g(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

和基本形式的证明相比较，只需要将倒数第二个等号替换成 Dirichlet 逆的定义式．

推论

设 𝑓(𝑛),𝑔(𝑛)f(n),g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是数论函数，且 𝑡(𝑛)t(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是完全积性函数．那么，有

𝑓(𝑛)=∑𝑑∣𝑛𝑡(𝑛𝑑)𝑔(𝑑)⟺𝑔(𝑛)=∑𝑑∣𝑛𝜇(𝑛𝑑)𝑡(𝑛𝑑)𝑓(𝑑).f(n)=∑d∣nt(nd)g(d)⟺g(n)=∑d∣nμ(nd)t(nd)f(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

由 Dirichlet 卷积的 [性质](../dirichlet/#性质) 可知，对于完全积性函数 𝑡(𝑛)t(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的 Dirichlet 逆就是 𝜇(𝑛)𝑡(𝑛)μ(n)t(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后，莫比乌斯反演还可以推广到 [1, +∞)[1,+∞)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的复值函数，而不仅仅局限于数论函数．基本形式的莫比乌斯反演可以看作是复值函数在所有非整数点处均取零值的特殊情形．

拓展四

设 𝐹(𝑥)F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺(𝑥)G(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是 [1, +∞)[1,+∞)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的复值函数．那么，有

𝐹(𝑥)=⌊𝑥⌋∑𝑛=1𝐺(𝑥𝑛)⟺𝐺(𝑥)=⌊𝑥⌋∑𝑛=1𝜇(𝑛)𝐹(𝑥𝑛).F(x)=∑n=1⌊x⌋G(xn)⟺G(x)=∑n=1⌊x⌋μ(n)F(xn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

不妨对 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 补充定义，设当 𝑥 <1x<1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，恒有 𝐹(𝑥) =𝐺(𝑥) =0F(x)=G(x)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，命题就等价于：

𝐹(𝑥)=∑𝑛𝐺(𝑥𝑛)⟺𝐺(𝑥)=∑𝑛𝜇(𝑛)𝐹(𝑥𝑛).F(x)=∑nG(xn)⟺G(x)=∑nμ(n)F(xn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这些求和式都是对 𝑛 ∈𝐍+n∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求和．

直接验证，有：

∑𝑛𝜇(𝑛)𝐹(𝑥𝑛)=∑𝑛𝜇(𝑛)∑𝑑𝐺(𝑥/𝑛𝑑)=∑𝑘𝐺(𝑥𝑘)∑𝑛∣𝑘𝜇(𝑛)=∑𝑘𝐺(𝑥𝑘)[𝑘=1]=𝐺(𝑥).∑nμ(n)F(xn)=∑nμ(n)∑dG(x/nd)=∑kG(xk)∑n∣kμ(n)=∑kG(xk)[k=1]=G(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，为得到第二个等号，需要令 𝑘 =𝑛𝑑k=nd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

推论

设 𝑓(𝑛),𝑔(𝑛)f(n),g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是数论函数．那么，有

𝑓(𝑛)=𝑛∑𝑘=1𝑔(⌊𝑛𝑘⌋)⟺𝑔(𝑛)=𝑛∑𝑘=1𝜇(𝑘)𝑓(⌊𝑛𝑘⌋).f(n)=∑k=1ng(⌊nk⌋)⟺g(n)=∑k=1nμ(k)f(⌊nk⌋).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

只需要取 𝐹(𝑥) =𝑓(⌊𝑥⌋)F(x)=f(⌊x⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺(𝑥) =𝑔(⌊𝑥⌋)G(x)=g(⌊x⌋)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

这些拓展形式之间可以互相组合，进而得到更为复杂的反演关系．

### Dirichlet 前缀和

前置知识：[前缀和与差分](../../../basic/prefix-sum/)

考虑基本形式的莫比乌斯反演关系：

𝑓(𝑛)=∑𝑑∣𝑛𝑔(𝑑)⟺𝑔(𝑛)=∑𝑑∣𝑛𝜇(𝑛𝑑)𝑓(𝑑).f(n)=∑d∣ng(d)⟺g(n)=∑d∣nμ(nd)f(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

左侧等式中，𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有因数处 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值之和．如果将 𝑎 ∣𝑏a∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 理解为 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 排在 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之前，那么 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以理解为某种意义下 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和．因此，在国内竞赛圈，由 {𝑔(𝑘)}𝑛𝑘=1{g(k)}k=1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求出 {𝑓(𝑘)}𝑛𝑘=1{f(k)}k=1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的过程也称为 **Dirichlet 前缀和** ，相应的逆过程则称为 Dirichlet 差分．这些方法大多出现在需要预处理某个数论函数在前 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点处取值的情形．

接下来，讨论 Dirichlet 前缀和的计算．如果将每一个素数都看作一个维度，这就是一种高维前缀和．回忆高维前缀和的 [逐维前缀和算法](../../../basic/prefix-sum/#逐维前缀和)：逐个遍历所有的维度，并将每个位置的值都累加到该位置在该维度上的后继位置．对于数论函数，这相当于说，从小到大遍历所有素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的函数值累加到 𝑛𝑝np![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处．这和 [Eratosthenes 筛法](../sieve/#埃拉托斯特尼筛法) 的遍历顺序是一致的．因此，这一算法可以在 𝑂(𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算出长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数列的 Dirichlet 前缀和．类似地，利用逐维差分就可以在相同时间复杂度内求出数列的 Dirichlet 差分．

参考实现

Dirichlet 前缀和Dirichlet 差分

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text std :: vector < int > dirichlet_presum ( const std :: vector < int >& g ) { int n = g . size () \- 1 ; std :: vector < int > f ( g ); std :: vector < bool > vis ( n \+ 1 ); for ( int x = 2 ; x <= n ; ++ x ) { if ( vis [ x ]) continue ; for ( int y = 1 , xy = x ; xy <= n ; ++ y , xy += x ) { vis [ xy ] = true ; f [ xy ] += f [ y ]; } } return f ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text std :: vector < int > dirichlet_diff ( const std :: vector < int >& f ) { int n = f . size () \- 1 ; std :: vector < int > g ( f ); std :: vector < int > vis ( n \+ 1 ); for ( int x = 2 ; x <= n ; ++ x ) { if ( vis [ x ]) continue ; for ( int y = n / x , xy = x * y ; y ; \-- y , xy -= x ) { vis [ xy ] = true ; g [ xy ] -= g [ y ]; } } return g ; } ```   
---|---  
  
这一计算方法可以推广到倍数和（拓展一）、乘积形式（拓展二）、利用完全积性函数代替常值函数（拓展三的推论）等拓展形式中．

## 例题

本节通过例题展示莫比乌斯反演的应用方法以及一些常见变形技巧．首先，通过一道例题熟悉处理求和式中最大公因数条件的基本技巧．

[Luogu P2522 [HAOI 2011] Problem b](https://www.luogu.com.cn/problem/P2522)

𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组数据．对每组数据，求值：

𝑛∑𝑖=𝑥𝑚∑𝑗=𝑦[gcd(𝑖,𝑗)=𝑘].∑i=xn∑j=ym[gcd(i,j)=k].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

数据范围：1 ≤𝑇,𝑥,𝑦,𝑛,𝑚,𝑘 ≤5 ×1041≤T,x,y,n,m,k≤5×104![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答

根据容斥原理，原式可以分成 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块来处理，且每一块的式子都具有形式

𝑓(𝑛,𝑚,𝑘)=𝑛∑𝑖=1𝑚∑𝑗=1[gcd(𝑖,𝑗)=𝑘].f(n,m,k)=∑i=1n∑j=1m[gcd(i,j)=k].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于这类式子，接下来是一段标准的推导流程：提取公因数，应用莫比乌斯函数性质，交换求和次序．

首先，由于 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都只能取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数，可以先将这个因子提出来——这相当于代入 𝑖 =𝑘𝑖′i=ki′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑗 =𝑘𝑗′j=kj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就得到：

𝑓(𝑛,𝑚,𝑘)=⌊𝑛/𝑘⌋∑𝑖=1⌊𝑚/𝑘⌋∑𝑗=1[gcd(𝑖,𝑗)=1].f(n,m,k)=∑i=1⌊n/k⌋∑j=1⌊m/k⌋[gcd(i,j)=1].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再利用莫比乌斯函数的性质可知：

[gcd(𝑖,𝑗)=1]=∑𝑑∣gcd(𝑖,𝑗)𝜇(𝑑)=∑𝑑[𝑑∣𝑖][𝑑∣𝑗]𝜇(𝑑).[gcd(i,j)=1]=∑d∣gcd(i,j)μ(d)=∑d[d∣i][d∣j]μ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将它代入表达式，并交换求和次序，就得到：

𝑓(𝑛,𝑚,𝑘)=∑𝑑𝜇(𝑑)(⌊𝑛/𝑘⌋∑𝑖=1[𝑑∣𝑖])(⌊𝑚/𝑘⌋∑𝑗=1[𝑑∣𝑗]).f(n,m,k)=∑dμ(d)(∑i=1⌊n/k⌋[d∣i])(∑j=1⌊m/k⌋[d∣j]).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样一段操作的好处是，固定 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，求和式中关于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的项相互分离，可以分别求和．接下来，因为

⌊𝑛/𝑘⌋∑𝑖=1[𝑑∣𝑖]=⌊⌊𝑛/𝑘⌋𝑑⌋, ⌊𝑚/𝑘⌋∑𝑗=1[𝑑∣𝑗]=⌊⌊𝑚/𝑘⌋𝑑⌋,∑i=1⌊n/k⌋[d∣i]=⌊⌊n/k⌋d⌋, ∑j=1⌊m/k⌋[d∣j]=⌊⌊m/k⌋d⌋,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，有

𝑓(𝑛,𝑚,𝑘)=∑𝑑𝜇(𝑑)⌊⌊𝑛/𝑘⌋𝑑⌋⌊⌊𝑚/𝑘⌋𝑑⌋.f(n,m,k)=∑dμ(d)⌊⌊n/k⌋d⌋⌊⌊m/k⌋d⌋.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

用线性筛预处理完 𝜇(𝑑)μ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并预处理其前缀和后，就可以通过数论分块求解．总的时间复杂度为 𝑂(𝑁 +𝑇√𝑁)O(N+TN)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑛,𝑚n,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的上界，𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为数据组数．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 ``` |  ```text #include <algorithm> #include <iostream> using namespace std ; constexpr int N = 50000 ; int mu [ N \+ 5 ], p [ N \+ 5 ]; bool flg [ N \+ 5 ]; void init () { int tot = 0 ; mu [ 1 ] = 1 ; for ( int i = 2 ; i <= N ; ++ i ) { if ( ! flg [ i ]) { p [ ++ tot ] = i ; mu [ i ] = -1 ; } for ( int j = 1 ; j <= tot && i * p [ j ] <= N ; ++ j ) { flg [ i * p [ j ]] = true ; if ( i % p [ j ] == 0 ) { mu [ i * p [ j ]] = 0 ; break ; } mu [ i * p [ j ]] = \- mu [ i ]; } } for ( int i = 1 ; i <= N ; ++ i ) mu [ i ] += mu [ i \- 1 ]; } int solve ( int n , int m ) { int res = 0 ; for ( int i = 1 , j ; i <= min ( n , m ); i = j \+ 1 ) { j = min ( n / ( n / i ), m / ( m / i )); res += ( mu [ j ] \- mu [ i \- 1 ]) * ( n / i ) * ( m / i ); // 代推出来的式子 } return res ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int T , a , b , c , d , k ; init (); // 预处理mu数组 cin >> T ; for ( int i = 1 ; i <= T ; i ++ ) { cin >> a >> b >> c >> d >> k ; // 根据容斥原理，1<=x<=b&&1<=y<=d范围中的答案数减去1<=x<=b&&1<=y<=c-1范围中的答案数和 // 1<=x<=a-1&&1<=y<=d范围中的答案数再加上1<=x<=a-1&&1<=y<=c-1范围中的答案数 // 即可得到a<=x<=b&&c<=y<=d范围中的答案数 // 这一步如果不懂可以画坐标图进行理解 cout << solve ( b / k , d / k ) \- solve ( b / k , ( c \- 1 ) / k ) \- solve (( a \- 1 ) / k , d / k ) \+ solve (( a \- 1 ) / k , ( c \- 1 ) / k ) << '\n' ; } return 0 ; } ```   
---|---  
  
接下来的两道例题展示了枚举公因数的处理方法，并利用 [筛法](../sieve/#一般的积性函数) 计算一般积性函数的值．

[SPOJ LCMSUM](https://www.spoj.com/problems/LCMSUM/)

𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组数据．对每组数据，求值：

𝑛∑𝑖=1lcm⁡(𝑖,𝑛).∑i=1nlcm⁡(i,n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

数据范围：1 ≤𝑇 ≤3 ×105, 1 ≤𝑛 ≤1061≤T≤3×105, 1≤n≤106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答一

题目提供的是最小公倍数，但往往最大公因数更容易处理．所以，首先做变形：

𝑓(𝑛)=𝑛∑𝑖=1lcm⁡(𝑖,𝑛)=𝑛∑𝑖=1𝑖⋅𝑛gcd(𝑖,𝑛).f(n)=∑i=1nlcm⁡(i,n)=∑i=1ni⋅ngcd(i,n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 提出，并枚举最大公因数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑓(𝑛)=𝑛∑𝑘∣𝑛𝑛∑𝑖=1𝑖𝑘[gcd(𝑖,𝑛)=𝑘].f(n)=n∑k∣n∑i=1nik[gcd(i,n)=k].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于内层的求和式，这是最常见的含有最大公因数的情形，重复标准的处理流程，就有：

𝑓(𝑛)=𝑛∑𝑘∣𝑛𝑛/𝑘∑𝑖=1𝑖[gcd(𝑖,𝑛𝑘)=1]=𝑛∑𝑘∣𝑛𝑛/𝑘∑𝑖=1𝑖∑𝑑𝜇(𝑑)[𝑑∣𝑖][𝑑∣𝑛𝑘]=𝑛∑𝑘∣𝑛∑𝑑𝜇(𝑑)[𝑑∣𝑛𝑘](𝑛/𝑘∑𝑖=1𝑖[𝑑∣𝑖]).f(n)=n∑k∣n∑i=1n/ki[gcd(i,nk)=1]=n∑k∣n∑i=1n/ki∑dμ(d)[d∣i][d∣nk]=n∑k∣n∑dμ(d)[d∣nk](∑i=1n/ki[d∣i]).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再次地，关于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的求和式与其他部分分离，可以单独处理．最后的求和式实际上是一个等差数列求和：（取 𝑖 =𝑑𝑖′i=di′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

𝑛/𝑘∑𝑖=1𝑖[𝑑∣𝑖]=𝑑12(𝑛𝑘𝑑+1)𝑛𝑘𝑑=:𝑑𝐺(𝑛𝑘𝑑).∑i=1n/ki[d∣i]=d12(nkd+1)nkd=:dG(nkd).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由此，就得到如下表达式：

𝑓(𝑛)=𝑛∑𝑘∣𝑛∑𝑑𝜇(𝑑)[𝑑∣𝑛𝑘]𝑑𝐺(𝑛𝑘𝑑).f(n)=n∑k∣n∑dμ(d)[d∣nk]dG(nkd).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在枚举公因数之后，这样形式的二重求和式很常见．对于它，同样有固定的处理方法：将乘积设为新变量 ℓ =𝑘𝑑ℓ=kd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后再次交换求和次序．因为 𝑑 ∣(𝑛/𝑘)d∣(n/k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就相当于 𝑑 ∣ℓ ∣𝑛d∣ℓ∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，原式变形为：

𝑓(𝑛)=𝑛∑ℓ∣𝑛𝐺(𝑛ℓ)∑𝑑∣ℓ𝜇(𝑑)𝑑.f(n)=n∑ℓ∣nG(nℓ)∑d∣ℓμ(d)d.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 𝐹(ℓ) =∑𝑑∣ℓ𝜇(𝑑)𝑑F(ℓ)=∑d∣ℓμ(d)d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则原式具有形式：

𝑓(𝑛)=𝑛∑ℓ∣𝑛𝐺(𝑛ℓ)𝐹(ℓ).f(n)=n∑ℓ∣nG(nℓ)F(ℓ).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝜇(𝑑)𝑑μ(d)d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数，所以它和常值函数 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的卷积 𝐹(𝑛)F(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是积性函数．尽管上述表达式中，求和式呈现 Dirichlet 卷积的形式，但是 𝐺(𝑛)G(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并非积性函数，所以这一求和式的整体并非积性函数．但是，𝐺(𝑛)G(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是多项式，所以它其实是若干完全积性函数的线性组合．所以，有

𝑓(𝑛)=12𝑛(∑ℓ(𝑛ℓ)2𝐹(ℓ)+∑ℓ𝑛ℓ𝐹(ℓ)).f(n)=12n(∑ℓ(nℓ)2F(ℓ)+∑ℓnℓF(ℓ)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这两项（不包含系数）都是积性函数，可以直接通过线性筛预处理（或者也可以线性筛出内层函数后，用 Dirichlet 前缀和在 𝑂(𝑁log⁡log⁡𝑁)O(Nlog⁡log⁡N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内预处理）．具体地，设

𝐻𝑠(𝑛)=∑ℓ(𝑛ℓ)𝑠𝐹(ℓ), 𝑠=1,2.Hs(n)=∑ℓ(nℓ)sF(ℓ), s=1,2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

要推导它们的表达式，只需要确定它们在素数幂处的取值即可．为此，对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正指数 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝐹(𝑝𝑒)=𝜇(1)+𝜇(𝑝)𝑝+𝑒∑𝑗=2𝜇(𝑝𝑗)𝑝𝑗=1−𝑝,𝐻𝑠(𝑝𝑒)=(𝑝𝑒)𝑠𝐹(1)+𝑒∑𝑗=1(𝑝𝑒−𝑗)𝑠𝐹(𝑝𝑗)=𝑝𝑒𝑠+(1−𝑝)1−𝑝𝑒𝑠1−𝑝𝑠, 𝑠=1,2.F(pe)=μ(1)+μ(p)p+∑j=2eμ(pj)pj=1−p,Hs(pe)=(pe)sF(1)+∑j=1e(pe−j)sF(pj)=pes+(1−p)1−pes1−ps, s=1,2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

特别地，𝐻1(𝑝𝑒) ≡1H1(pe)≡1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是常值函数，而

𝐻2(𝑝𝑒)=𝑝2𝑒+(1−𝑝)1−𝑝2𝑒1−𝑝2=𝐻2(𝑝𝑒−1)+𝑝2𝑒−𝑝2𝑒−1.H2(pe)=p2e+(1−p)1−p2e1−p2=H2(pe−1)+p2e−p2e−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就很容易通过线性筛求解．在线性筛预处理出 𝐻2(𝑛)H2(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，单次询问可以通过表达式 𝑓(𝑛) =(𝑛/2)(𝐻2(𝑛) +1)f(n)=(n/2)(H2(n)+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内求解．总的时间复杂度为 𝑂(𝑁 +𝑇)O(N+T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的上界，𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为数据组数．

参考实现中，利用本题表达式的特殊性，对线性筛部分做了进一步推导，这并非必须的．仅利用素数幂处的取值，仍然可以在 𝑂(𝑁)O(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内完成预处理．这些推导详见解答二．

解答二

就本题而言，有着更为灵活的处理方法．从解答一可以看出

𝑓(𝑛)=𝑛∑𝑘∣𝑛𝑛/𝑘∑𝑖=1𝑖[gcd(𝑖,𝑛𝑘)=1]=𝑛∑𝑘∣𝑛𝐹(𝑛𝑘).f(n)=n∑k∣n∑i=1n/ki[gcd(i,nk)=1]=n∑k∣nF(nk).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如果在这一步不继续做莫比乌斯反演，而是观察后面的求和式实际上是不超过 𝑑 =𝑛/𝑘d=n/k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且与之互素的整数之和．对于 𝑑 >1d>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为与 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素的整数成对出现，即 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑑 −𝑖d−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必定同时与 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素，所以，有

𝐹(𝑑)=𝑛′∑𝑖=1𝑖[𝑖⟂𝑑]=𝑑∑𝑖=1(𝑑−𝑖)[𝑖⟂𝑑]=12𝑑𝑑∑𝑖=1[𝑖⟂𝑑]=12𝑑𝜑(𝑑).F(d)=∑i=1n′i[i⟂d]=∑i=1d(d−i)[i⟂d]=12d∑i=1d[i⟂d]=12dφ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于 𝑑 =1d=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有

𝐹(𝑑)=1=12+12𝑑𝜑(𝑑).F(d)=1=12+12dφ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而，原式可以表示为

𝑓(𝑛)=12𝑛⎛⎜ ⎜⎝∑𝑑∣𝑛𝑑𝜑(𝑑)+1⎞⎟ ⎟⎠.f(n)=12n(∑d∣ndφ(d)+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于 𝐺(𝑛) =∑𝑑∣𝑛𝑑𝜑(𝑑)G(n)=∑d∣ndφ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数 𝑛𝜑(𝑛)nφ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与常值函数 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Dirichlet 卷积，所以它也是积性函数，可以通过线性筛预处理．为此，只需要确定它在素数幂处的取值．对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正指数 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝐺(𝑝𝑒)=1+𝑒∑𝑖=1𝑝𝑒(𝑝𝑒−1)=𝐺(𝑝𝑒−1)+𝑝2𝑒−𝑝2𝑒−1.G(pe)=1+∑i=1epe(pe−1)=G(pe−1)+p2e−p2e−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以看出，这一表达式和解答一推导的结果是一致的．这一方法的总时间复杂度仍然是 𝑂(𝑁 +𝑇)O(N+T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后，利用本题积性函数的表达式，可以进一步优化线性筛的计算过程．对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝐺(𝑝)=1−𝑝+𝑝2.G(p)=1−p+p2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

线性筛的关键在于对于一般的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，需要求出 𝐺(𝑝𝑛)G(pn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．这进一步分为两种情形．当 𝑝 ⟂𝑛p⟂n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，因为 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数，所以

𝐺(𝑝𝑛)=𝐺(𝑝)𝐺(𝑛).G(pn)=G(p)G(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

否则，当 𝑝 ∣𝑛p∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，设 𝑛 =𝑝𝑒𝑚n=pem![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑝 ⟂𝑚p⟂m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有

𝐺(𝑝𝑛)=𝐺(𝑝𝑒+1)𝐺(𝑚)=𝐺(𝑝𝑒)𝐺(𝑚)+(𝑝2𝑒+2−𝑝2𝑒+1)𝐺(𝑚)=𝐺(𝑛)+(𝑝2𝑒+2−𝑝2𝑒+1)𝐺(𝑚).G(pn)=G(pe+1)G(m)=G(pe)G(m)+(p2e+2−p2e+1)G(m)=G(n)+(p2e+2−p2e+1)G(m).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

直接验证可知，这一表达式对于 𝑝 ⟂𝑛p⟂n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形也成立．因此，就有

𝐺(𝑛)−𝐺(𝑛𝑝)=(𝑝2𝑒−𝑝2𝑒−1)𝐺(𝑚).G(n)−G(np)=(p2e−p2e−1)G(m).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入上式，就得到

𝐺(𝑝𝑛)=𝐺(𝑛)+𝑝2(𝐺(𝑛)−𝐺(𝑛𝑝)).G(pn)=G(n)+p2(G(n)−G(np)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这简化了线性筛部分的计算．当然，这一推导并非必需，对于没有特殊性质的积性函数，直接利用 𝐺(𝑝𝑛) =𝐺(𝑝𝑒+1)𝐺(𝑚)G(pn)=G(pe+1)G(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就可以完成线性筛的计算．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` |  ```text #include <iostream> constexpr int N = 1000000 ; int tot , p [ N \+ 5 ]; long long g [ N \+ 5 ]; bool flg [ N \+ 5 ]; // 标记数组 void solve () { g [ 1 ] = 1 ; for ( int i = 2 ; i <= N ; ++ i ) { if ( ! flg [ i ]) { p [ ++ tot ] = i ; g [ i ] = ( long long ) 1 * i * ( i \- 1 ) \+ 1 ; } for ( int j = 1 ; j <= tot && i * p [ j ] <= N ; ++ j ) { flg [ i * p [ j ]] = true ; if ( i % p [ j ] == 0 ) { g [ i * p [ j ]] = g [ i ] \+ ( g [ i ] \- g [ i / p [ j ]]) * p [ j ] * p [ j ]; // 代入推出来的式子 break ; } g [ i * p [ j ]] = g [ i ] * g [ p [ j ]]; } } } using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int T , n ; solve (); // 预处理g数组 cin >> T ; for ( int i = 1 ; i <= T ; ++ i ) { cin >> n ; cout << ( g [ n ] \+ 1 ) * n / 2 << '\n' ; } return 0 ; } ```   
---|---  
  
[BZOJ 2154 [国家集训队] Crash 的数字表格](https://hydro.ac/p/bzoj-P2154)

求值：

𝑛∑𝑖=1𝑚∑𝑗=1lcm⁡(𝑖,𝑗)mod20101009.∑i=1n∑j=1mlcm⁡(i,j)mod20101009.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

数据范围：1 ≤𝑛,𝑚 ≤1071≤n,m≤107![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答

推导过程中忽略模数．设

𝑓(𝑛,𝑚)=𝑛∑𝑖=1𝑚∑𝑗=1lcm⁡(𝑖,𝑗).f(n,m)=∑i=1n∑j=1mlcm⁡(i,j).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

依然是将最小公倍数转换为最大公因数，枚举公因数，并应用标准的处理流程，就得到

𝑓(𝑛,𝑚)=∑𝑘𝑛∑𝑖=1𝑚∑𝑗=1𝑖𝑗𝑘[gcd(𝑖,𝑗)=𝑘]=∑𝑘⌊𝑛/𝑘⌋∑𝑖=1⌊𝑚/𝑘⌋∑𝑗=1𝑘𝑖𝑗[gcd(𝑖,𝑗)=1]=∑𝑘⌊𝑛/𝑘⌋∑𝑖=1⌊𝑚/𝑘⌋∑𝑗=1𝑘𝑖𝑗∑𝑑𝜇(𝑑)[𝑑∣𝑖][𝑑∣𝑗]=∑𝑘𝑘∑𝑑𝜇(𝑑)(⌊𝑛/𝑘⌋∑𝑖=1𝑖[𝑑∣𝑖])(⌊𝑚/𝑘⌋∑𝑗=1𝑗[𝑑∣𝑗]).f(n,m)=∑k∑i=1n∑j=1mijk[gcd(i,j)=k]=∑k∑i=1⌊n/k⌋∑j=1⌊m/k⌋kij[gcd(i,j)=1]=∑k∑i=1⌊n/k⌋∑j=1⌊m/k⌋kij∑dμ(d)[d∣i][d∣j]=∑kk∑dμ(d)(∑i=1⌊n/k⌋i[d∣i])(∑j=1⌊m/k⌋j[d∣j]).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再次地，求和式对于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分离．首先计算这些内层的求和式，提取因数（即取 𝑖 =𝑑𝑖′i=di′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），就有

⌊𝑛/𝑘⌋∑𝑖=1𝑖[𝑑∣𝑖]=𝑑⌊⌊𝑛/𝑘⌋/𝑑⌋∑𝑖=1𝑖=𝑑𝐺(⌊⌊𝑛/𝑘⌋𝑑⌋)=𝑑𝐺(⌊𝑛𝑘𝑑⌋).∑i=1⌊n/k⌋i[d∣i]=d∑i=1⌊⌊n/k⌋/d⌋i=dG(⌊⌊n/k⌋d⌋)=dG(⌊nkd⌋).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝐺(𝑛) =12𝑛(𝑛 +1)G(n)=12n(n+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是等差数列求和，最后一个等号利用了 [下取整函数](../basic/#取整函数) 的性质．对称地，对于另一个和式可以类似计算．代回前文表达式，就有

𝑓(𝑛,𝑚)=∑𝑘𝑘∑𝑑𝜇(𝑑)𝑑2𝐺(⌊𝑛𝑘𝑑⌋)𝐺(⌊𝑚𝑘𝑑⌋).f(n,m)=∑kk∑dμ(d)d2G(⌊nkd⌋)G(⌊mkd⌋).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

和前文的情形一致，对于这类枚举公因数的式子，往往都需要枚举乘积 ℓ =𝑘𝑑ℓ=kd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再次交换求和次序：

𝑓(𝑛,𝑚)=∑ℓ⎛⎜ ⎜⎝∑𝑑∣ℓ𝜇(𝑑)𝑑ℓ⎞⎟ ⎟⎠𝐺(⌊𝑛ℓ⌋)𝐺(⌊𝑚ℓ⌋).f(n,m)=∑ℓ(∑d∣ℓμ(d)dℓ)G(⌊nℓ⌋)G(⌊mℓ⌋).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设

𝐹(ℓ)=∑𝑑∣ℓ𝜇(𝑑)𝑑ℓ.F(ℓ)=∑d∣ℓμ(d)dℓ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是积性函数 ℓℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与积性函数 ∑𝑑∣ℓ𝜇(𝑑)𝑑∑d∣ℓμ(d)d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘积，所以也是积性函数，可以直接用线性筛预处理，并预处理出它的前缀和．然后，就可以用数论分块计算 𝑓(𝑛,𝑚)f(n,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．总的时间复杂度为 𝑂(min{𝑛,𝑚})O(min{n,m})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` |  ```text #include <algorithm> #include <iostream> #include <vector> int main () { constexpr int M = 20101009 ; int n , m ; std :: cin >> n >> m ; if ( n > m ) std :: swap ( n , m ); std :: vector < int > f ( n \+ 1 ), vis ( n \+ 1 ), prime ; prime . reserve ( n ); f [ 1 ] = 1 ; for ( int x = 2 ; x <= n ; ++ x ) { if ( ! vis [ x ]) { prime . emplace_back ( x ); f [ x ] = 1 \- x ; } for ( int p : prime ) { if ( 1L L * p * x > n ) break ; vis [ x * p ] = 1 ; f [ x * p ] = x % p ? ( 1 \- p ) * f [ x ] : f [ x ]; if ( x % p == 0 ) break ; } } for ( int x = 1 ; x <= n ; ++ x ) { f [ x ] = 1L L * x * f [ x ] % M \+ M ; f [ x ] = ( f [ x ] \+ f [ x \- 1 ]) % M ; } long long res = 0 ; for ( int l = 1 , r ; l <= n ; l = r \+ 1 ) { int nn = n / l , mm = m / l ; r = std :: min ( n / nn , m / mm ); int g_n = ( 1L L * nn * ( nn \+ 1 ) / 2 ) % M ; int g_m = ( 1L L * mm * ( mm \+ 1 ) / 2 ) % M ; res += 1L L * g_n * g_m % M * ( f [ r ] \- f [ l \- 1 ] \+ M ) % M ; } std :: cout << ( res % M ) << '\n' ; return 0 ; } ```   
---|---  
  
接下来的一道例题较为特殊，需要对乘积的约数个数函数进行转换．

[LOJ 2185. [SDOI2015] 约数个数和](https://loj.ac/problem/2185)

𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组数据．对每组数据，求值：

𝑛∑𝑖=1𝑚∑𝑗=1𝜎0(𝑖𝑗).∑i=1n∑j=1mσ0(ij).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝜎0(𝑛) =∑𝑑∣𝑛1σ0(n)=∑d∣n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数个数．

数据范围：1 ≤𝑛,𝑚,𝑇 ≤5 ×1041≤n,m,T≤5×104![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答

这道题目的难点在于将 𝜎0(𝑖𝑗)σ0(ij)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转换为关于最大公因数的表达式．由于 𝜎0σ0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数，可以首先考虑素数幂的情形．对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和非负指数 𝑒1,𝑒2e1,e2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设 𝑖 =𝑝𝑒1, 𝑗 =𝑝𝑒2i=pe1, j=pe2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有

𝜎0(𝑖𝑗)=1+𝑒1+𝑒2=∑𝑥∣𝑖∑𝑦∣𝑗[𝑥⟂𝑦].σ0(ij)=1+e1+e2=∑x∣i∑y∣j[x⟂y].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于一般情形，不妨设 𝑖 =∏𝑝𝑖𝑝i=∏pip![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑗 =∏𝑝𝑗𝑝j=∏pjp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑖𝑝,𝑗𝑝ip,jp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别是 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素因数分解中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次．进而，有

𝜎0(𝑖𝑗)=∏𝑝𝜎0(𝑖𝑝𝑗𝑝)=∏𝑝∑𝑥𝑝∣𝑖𝑝∑𝑦𝑝∣𝑗𝑝[𝑥𝑝⟂𝑦𝑝].σ0(ij)=∏pσ0(ipjp)=∏p∑xp∣ip∑yp∣jp[xp⟂yp].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到，对于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每个素数幂因子 𝑖𝑝ip![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都枚举它的因数 𝑥𝑝xp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就相当于对 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚举它的因数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再分解出所有素数幂因子 𝑥𝑝xp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；对 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同理．因此，利用乘法分配律，该式就有

𝜎0(𝑖𝑗)=∑𝑥∣𝑖∑𝑦∣𝑗∏𝑝[𝑥𝑝⟂𝑦𝑝]=∑𝑥∣𝑖∑𝑦∣𝑗[𝑥⟂𝑦].σ0(ij)=∑x∣i∑y∣j∏p[xp⟂yp]=∑x∣i∑y∣j[x⟂y].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最后一步用到了结论：𝑥 ⟂𝑦x⟂y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当且仅当对于每个素因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑥𝑝 ⟂𝑦𝑝xp⟂yp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．

得到这一表达式后，就可以应用标准的处理流程：

𝜎0(𝑖𝑗)=∑𝑥∣𝑖∑𝑦∣𝑗[𝑥⟂𝑦]=∑𝑥∣𝑖∑𝑦∣𝑗∑𝑑𝜇(𝑑)[𝑑∣𝑥][𝑑∣𝑦]=∑𝑑𝜇(𝑑)(∑𝑥[𝑑∣𝑥∣𝑖])(∑𝑦[𝑑∣𝑦∣𝑗])=∑𝑑𝜇(𝑑)[𝑑∣𝑖][𝑑∣𝑗]𝜎0(𝑖𝑑)𝜎0(𝑗𝑑).σ0(ij)=∑x∣i∑y∣j[x⟂y]=∑x∣i∑y∣j∑dμ(d)[d∣x][d∣y]=∑dμ(d)(∑x[d∣x∣i])(∑y[d∣y∣j])=∑dμ(d)[d∣i][d∣j]σ0(id)σ0(jd).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最后一步推导的含义是：函数只有在 𝑑 ∣𝑖d∣i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑑 ∣𝑗d∣j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时才取非零值，且此时，枚举满足 𝑑 ∣𝑥 ∣𝑖d∣x∣i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就相当于枚举 𝑖𝑑id![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的因数 𝑥𝑑xd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，枚举满足 𝑑 ∣𝑦 ∣𝑗d∣y∣j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同理．

将这一表达式再代回原式，并交换求和次序：

𝑓(𝑛,𝑚)=𝑛∑𝑖=1𝑚∑𝑗=1𝜎0(𝑖𝑗)=𝑛∑𝑖=1𝑚∑𝑗=1∑𝑑𝜇(𝑑)[𝑑∣𝑖][𝑑∣𝑗]𝜎0(𝑖𝑑)𝜎0(𝑗𝑑)=∑𝑑𝜇(𝑑)(𝑛∑𝑖=1[𝑑∣𝑖]𝜎0(𝑖𝑑))(𝑚∑𝑗=1[𝑑∣𝑗]𝜎0(𝑗𝑑))=∑𝑑𝜇(𝑑)(⌊𝑛/𝑑⌋∑𝑖=1𝜎0(𝑖))(⌊𝑚/𝑑⌋∑𝑗=1𝜎0(𝑗)).f(n,m)=∑i=1n∑j=1mσ0(ij)=∑i=1n∑j=1m∑dμ(d)[d∣i][d∣j]σ0(id)σ0(jd)=∑dμ(d)(∑i=1n[d∣i]σ0(id))(∑j=1m[d∣j]σ0(jd))=∑dμ(d)(∑i=1⌊n/d⌋σ0(i))(∑j=1⌊m/d⌋σ0(j)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 𝐺(𝑛) =∑𝑛𝑖=1𝜎0(𝑖)G(n)=∑i=1nσ0(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有

𝑓(𝑛,𝑚)=∑𝑑𝜇(𝑑)𝐺(⌊𝑛𝑑⌋)𝐺(⌊𝑚𝑑⌋).f(n,m)=∑dμ(d)G(⌊nd⌋)G(⌊md⌋).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这可以通过数论分块求解．只需要预处理出 𝜇(𝑛)μ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜎0(𝑛)σ0(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀和即可．总时间复杂度为 𝑂(𝑁 +𝑇√𝑁)O(N+TN)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑛,𝑚n,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的上界，𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为数据组数．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 ``` |  ```text #include <algorithm> #include <iostream> using namespace std ; constexpr long long N = 5e4 \+ 5 ; long long n , m , T , pr [ N ], mu [ N ], d [ N ], t [ N ], cnt ; // t 表示 i 的最小质因子出现的次数 bool bp [ N ]; void prime_work ( long long k ) { bp [ 0 ] = bp [ 1 ] = true , mu [ 1 ] = 1 , d [ 1 ] = 1 ; for ( long long i = 2 ; i <= k ; i ++ ) { // 线性筛 if ( ! bp [ i ]) pr [ ++ cnt ] = i , mu [ i ] = -1 , d [ i ] = 2 , t [ i ] = 1 ; for ( long long j = 1 ; j <= cnt && i * pr [ j ] <= k ; j ++ ) { bp [ i * pr [ j ]] = true ; if ( i % pr [ j ] == 0 ) { mu [ i * pr [ j ]] = 0 ; d [ i * pr [ j ]] = d [ i ] / ( t [ i ] \+ 1 ) * ( t [ i ] \+ 2 ); t [ i * pr [ j ]] = t [ i ] \+ 1 ; break ; } else { mu [ i * pr [ j ]] = \- mu [ i ]; d [ i * pr [ j ]] = d [ i ] << 1 ; t [ i * pr [ j ]] = 1 ; } } } for ( long long i = 2 ; i <= k ; i ++ ) mu [ i ] += mu [ i \- 1 ], d [ i ] += d [ i \- 1 ]; // 求前缀和 } long long solve () { long long res = 0 , mxi = min ( n , m ); for ( long long i = 1 , j ; i <= mxi ; i = j \+ 1 ) { // 整除分块 j = min ( n / ( n / i ), m / ( m / i )); res += d [ n / i ] * d [ m / i ] * ( mu [ j ] \- mu [ i \- 1 ]); } return res ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> T ; prime_work ( 50000 ); // 预处理 while ( T \-- ) { cin >> n >> m ; cout << solve () << '\n' ; } return 0 ; } ```   
---|---  
  
最后一道例题展示了如何应用乘法版本的莫比乌斯反演．

[Luogu P5221 Product](https://www.luogu.com.cn/problem/P5221)

求值：

𝑛∏𝑖=1𝑛∏𝑗=1lcm⁡(𝑖,𝑗)gcd(𝑖,𝑗)(mod104857601).∏i=1n∏j=1nlcm⁡(i,j)gcd(i,j)(mod104857601).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

数据范围：1 ≤𝑛 ≤1 ×1061≤n≤1×106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解答一

推导过程中忽略模数．设

𝑓(𝑛)=𝑛∏𝑖=1𝑛∏𝑗=1lcm⁡(𝑖,𝑗)gcd(𝑖,𝑗).f(n)=∏i=1n∏j=1nlcm⁡(i,j)gcd(i,j).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

依然是将最小公倍数转换为最大公因数：

𝑓(𝑛)=𝑛∏𝑖=1𝑛∏𝑗=1𝑖𝑗(gcd(𝑖,𝑗))2.f(n)=∏i=1n∏j=1nij(gcd(i,j))2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意，对这些因子的乘积是相互独立的，可以分别计算．令

𝑔(𝑛)=𝑛∏𝑖=1𝑛∏𝑗=1gcd(𝑖,𝑗).g(n)=∏i=1n∏j=1ngcd(i,j).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

原式就等于：

𝑓(𝑛)=(𝑛!)2𝑛𝑔(𝑛)2.f(n)=(n!)2ng(n)2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

重点是解决 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算问题．对它的处理流程和前文描述的相仿，但是需要换成相应的乘法版本．首先，枚举并提取公因数：

𝑔(𝑛)=∏𝑘𝑛∏𝑖=1𝑛∏𝑗=1𝑘↑[gcd(𝑖,𝑗)=𝑘]=∏𝑘⌊𝑛/𝑘⌋∏𝑖=1⌊𝑛/𝑘⌋∏𝑗=1𝑘↑[gcd(𝑖,𝑗)=1].g(n)=∏k∏i=1n∏j=1nk↑[gcd(i,j)=k]=∏k∏i=1⌊n/k⌋∏j=1⌊n/k⌋k↑[gcd(i,j)=1].![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑎 ↑𝑏 =𝑎𝑏a↑b=ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 Knuth 箭头．然后，代入 [gcd(𝑖,𝑗) =1] =∑𝑑𝜇(𝑑)[𝑑 ∣𝑖][𝑑 ∣𝑗][gcd(i,j)=1]=∑dμ(d)[d∣i][d∣j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将指数上的和式转换为幂的乘积式，得到：

𝑔(𝑛)=∏𝑘∏𝑑⌊𝑛/𝑘⌋∏𝑖=1⌊𝑛/𝑘⌋∏𝑗=1𝑘↑(𝜇(𝑑)[𝑑∣𝑖][𝑑∣𝑗]).g(n)=∏k∏d∏i=1⌊n/k⌋∏j=1⌊n/k⌋k↑(μ(d)[d∣i][d∣j]).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进一步地提取因数（即令 𝑖 =𝑑𝑖′i=di′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑗 =𝑑𝑗′j=dj′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），并应用 [下取整函数](../basic/#取整函数) 的性质，就得到：

𝑔(𝑛)=∏𝑘∏𝑑⌊𝑛/(𝑘𝑑)⌋∏𝑖=1⌊𝑛/(𝑘𝑑)⌋∏𝑗=1𝑘↑𝜇(𝑑).g(n)=∏k∏d∏i=1⌊n/(kd)⌋∏j=1⌊n/(kd)⌋k↑μ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后分离关于 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘积，就发现乘式中并不含有 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此它就相当于对乘式取幂：

𝑔(𝑛)=∏𝑘∏𝑑𝑘↑(𝜇(𝑑)⌊𝑛𝑘𝑑⌋2).g(n)=∏k∏dk↑(μ(d)⌊nkd⌋2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为前面枚举了公因数，所以对于这个式子需要再次交换求乘积的次序．令 ℓ =𝑘𝑑ℓ=kd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

𝑔(𝑛)=∏ℓ∏𝑑∣ℓ(ℓ𝑑)↑(𝜇(𝑑)⌊𝑛ℓ⌋2)=∏ℓ⎛⎜ ⎜⎝∏𝑑∣ℓ(ℓ𝑑)↑𝜇(𝑑)⎞⎟ ⎟⎠↑⌊𝑛ℓ⌋2.g(n)=∏ℓ∏d∣ℓ(ℓd)↑(μ(d)⌊nℓ⌋2)=∏ℓ(∏d∣ℓ(ℓd)↑μ(d))↑⌊nℓ⌋2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设

𝐹(𝑛)=∏𝑑∣𝑛(𝑛𝑑)↑𝜇(𝑑).F(n)=∏d∣n(nd)↑μ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

容易发现这是关于 ˜𝐹(𝑛) =𝑛F~(n)=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘积形式莫比乌斯反演．即使不知道它的表达式，也可以应用 Dirichlet 差分 方法在 𝑂(𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内预处理．当然，由于 ˜𝐹(𝑛)F~(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式非常简单，𝐹(𝑛)F(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式可以直接求出：

𝐹(𝑛)={𝑝,𝑛=𝑝𝑒, 𝑝∈𝐏, 𝑒∈𝐍+,1,otherwise.F(n)={p,n=pe, p∈P, e∈N+,1,otherwise.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

von Mangoldt 函数 就是它的自然对数．得到 𝐹(𝑛)F(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值后，直接应用乘积版本的数论分块就可以在 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内求出 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值，进而得到 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．总的时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

值得注意的是，涉及乘积的计算时，往往需要用到 [欧拉定理](../fermat/)，因此指数部分取模用到的模数与题目所给的模数并不相同．

解答二

乘积版本推导的难点在于对乘积和幂次的处理相对陌生，因此，对于这类问题，也可以取对数后再推导．对于本题，仅考虑 𝑔(𝑛)g(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的推导．将它取对数后，有：

log⁡𝑔(𝑛)=𝑛∑𝑖=1𝑛∑𝑗=1log⁡gcd(𝑖,𝑗).log⁡g(n)=∑i=1n∑j=1nlog⁡gcd(i,j).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于这类含有最大公因数的式子，直接应用标准的推导流程，就得到：

log⁡𝑔(𝑛)=∑𝑘log⁡𝑘𝑛∑𝑖=1𝑛∑𝑗=1[gcd(𝑖,𝑗)=𝑘]=∑𝑘log⁡𝑘⌊𝑛/𝑘⌋∑𝑖=1⌊𝑛/𝑘⌋∑𝑗=1[gcd(𝑖,𝑗)=1]=∑𝑘log⁡𝑘∑𝑑𝜇(𝑑)(⌊𝑛/𝑘⌋∑𝑖=1[𝑖∣𝑑])(⌊𝑛/𝑘⌋∑𝑗=1[𝑗∣𝑑])=∑𝑘log⁡𝑘∑𝑑𝜇(𝑑)⌊𝑛𝑘𝑑⌋2=∑ℓ(∑𝑑𝜇(𝑑)log⁡ℓ𝑑)⌊𝑛ℓ⌋2=∑ℓΛ(ℓ)⌊𝑛ℓ⌋2.log⁡g(n)=∑klog⁡k∑i=1n∑j=1n[gcd(i,j)=k]=∑klog⁡k∑i=1⌊n/k⌋∑j=1⌊n/k⌋[gcd(i,j)=1]=∑klog⁡k∑dμ(d)(∑i=1⌊n/k⌋[i∣d])(∑j=1⌊n/k⌋[j∣d])=∑klog⁡k∑dμ(d)⌊nkd⌋2=∑ℓ(∑dμ(d)log⁡ℓd)⌊nℓ⌋2=∑ℓΛ(ℓ)⌊nℓ⌋2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，Λ(𝑛)Λ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 von Mangoldt 函数．将这一推导结果取幂，就得到解答一的结果．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 ``` |  ```text #include <algorithm> #include <iostream> #include <vector> int pow ( int a , int b , int m ) { int res = 1 ; for ( int po = a ; b ; b >>= 1 ) { if ( b & 1 ) res = 1L L * res * po % m ; po = 1L L * po * po % m ; } return res ; } int main () { constexpr int M = 104857601 ; int n ; std :: cin >> n ; // Get F(n), i.e., exp(Lambda(n)). std :: vector < int > vis ( n \+ 1 ), prime , pf ( n \+ 1 ), rem ( n \+ 1 ); prime . reserve ( n ); for ( int x = 2 ; x <= n ; ++ x ) { if ( ! vis [ x ]) { prime . emplace_back ( x ); pf [ x ] = x ; rem [ x ] = 1 ; } for ( int p : prime ) { if ( 1L L * p * x > n ) break ; vis [ x * p ] = 1 ; pf [ x * p ] = p ; rem [ x * p ] = x % p ? x : rem [ x ]; if ( x % p == 0 ) break ; } } pf [ 1 ] = 1 ; for ( int x = 2 ; x <= n ; ++ x ) { pf [ x ] = rem [ x ] == 1 ? pf [ x ] : 1 ; } // Prefix products and their inverses. std :: vector < int > pm ( n \+ 1 ), ip ( n \+ 1 ); pm [ 0 ] = 1 ; for ( int x = 1 ; x <= n ; ++ x ) { pm [ x ] = 1L L * pm [ x \- 1 ] * pf [ x ] % M ; } int inv = pow ( pm [ n ], M \- 2 , M ); ip [ 0 ] = 1 ; for ( int x = n ; x >= 1 ; \-- x ) { ip [ x ] = inv ; inv = 1L L * inv * pf [ x ] % M ; } // Calculate g(n). int res = 1 ; for ( int l = 1 , r ; l <= n ; l = r \+ 1 ) { r = n / ( n / l ); int a = 1L L * pm [ r ] * ip [ l \- 1 ] % M ; int b = 1L L * ( n / l ) * ( n / l ) % ( M \- 1 ); res = 1L L * res * pow ( a , b , M ) % M ; } // Take square and then inverse. res = pow ( res , M \- 3 , M ); // Get factorials. int fac = 1 ; for ( int x = 1 ; x <= n ; ++ x ) { fac = 1L L * fac * x % M ; } // Final answer. res = 1L L * res * pow ( fac , 2 * n , M ) % M ; std :: cout << res << std :: endl ; return 0 ; } ```   
---|---  
  
## 习题

  * [Luogu P3312 [SDOI2014] 数表](https://www.luogu.com.cn/problem/P3312)
  * [Luogu P3700 [CQOI2017] 小 Q 的表格](https://www.luogu.com.cn/problem/P3700)
  * [Luogu P3704 [SDOI2017] 数字表格](https://www.luogu.com.cn/problem/P3704)
  * [Luogu P3768 简单的数学题](https://www.luogu.com.cn/problem/P3768)
  * [Luogu P4464 [国家集训队] JZPKIL](https://www.luogu.com.cn/problem/P4464)
  * [Luogu P4619 [SDOI2018] 旧试题](https://www.luogu.com.cn/problem/P4619)
  * [Luogu P5518 [MtOI2019] 幽灵乐团](https://www.luogu.com.cn/problem/P5518)
  * [Luogu P6222 简单题 加强版](https://www.luogu.com.cn/problem/P6222)
  * [Luogu P6825「EZEC-4」求和](https://www.luogu.com.cn/problem/P6825)
  * [Luogu P7486「Stoi2031」彩虹](https://www.luogu.com.cn/problem/P7486)
  * [AtCoder Grand Contest 038 C - LCMs](https://atcoder.jp/contests/agc038/tasks/agc038_c)
  * [Codeforeces 1139 D. Steps to One](https://codeforces.com/problemset/problem/1139/D)

## 参考文献

  * [Möbius function - Wikipedia](https://en.wikipedia.org/wiki/M%C3%B6bius_function)
  * [Möbius inversion formula - Wikipedia](https://en.wikipedia.org/wiki/M%C3%B6bius_inversion_formula)
  * [Von Mangoldt function - Wikipedia](https://en.wikipedia.org/wiki/Von_Mangoldt_function)
  * [algocode 算法博客](https://web.archive.org/web/20190523150159/https://algocode.net/2018/04/18/20180418-KB-Mobius-Inversion-Formula/)

* * *

>  __本页面最近更新： 2025/10/31 16:20:06，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/mobius.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/mobius.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [Enter-tainer](https://github.com/Enter-tainer), [mgt](mailto:i@margatroid.xyz), [ShaoChenHeng](https://github.com/ShaoChenHeng), [H-J-Granger](https://github.com/H-J-Granger), [Marcythm](https://github.com/Marcythm), [orzAtalod](https://github.com/orzAtalod), [Siyuan](mailto:294873684@qq.com), [sshwy](https://github.com/sshwy), [Early0v0](https://github.com/Early0v0), [Peanut-Tang](https://github.com/Peanut-Tang), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [countercurrent-time](https://github.com/countercurrent-time), [ezoixx130](https://github.com/ezoixx130), [hyp1231](https://github.com/hyp1231), [NachtgeistW](https://github.com/NachtgeistW), [ranwen](https://github.com/ranwen), [GekkaSaori](https://github.com/GekkaSaori), [ksyx](https://github.com/ksyx), [MegaOwIer](https://github.com/MegaOwIer), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Tiphereth-A](https://github.com/Tiphereth-A), [Vxlimo](https://github.com/Vxlimo), [383494](https://github.com/383494), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Gesrua](https://github.com/Gesrua), [Great-designer](https://github.com/Great-designer), [guodong2005](https://github.com/guodong2005), [Henry-ZHR](https://github.com/Henry-ZHR), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [Konano](https://github.com/Konano), [Lcyanstars](https://github.com/Lcyanstars), [LovelyBuggies](https://github.com/LovelyBuggies), [Luckyblock233](https://github.com/Luckyblock233), [Makkiy](https://github.com/Makkiy), [Menci](https://github.com/Menci), [minghu6](https://github.com/minghu6), [mxr612](mailto:m_gt_@outlook.com), [ouuan](https://github.com/ouuan), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [Chrogeek](https://github.com/Chrogeek), [CyaceQuious](https://github.com/CyaceQuious), [FFjet](https://github.com/FFjet), [frank-xjh](https://github.com/frank-xjh), [GavinZhengOI](https://github.com/GavinZhengOI), [hehelego](mailto:2364261262@qq.com), [hjsjhn](https://github.com/hjsjhn), [hydingsy](https://github.com/hydingsy), [i-yyi](https://github.com/i-yyi), [kenlig](https://github.com/kenlig), [kxccc](https://github.com/kxccc), [luojiny1](https://github.com/luojiny1), [lychees](https://github.com/lychees), [nalemy](https://github.com/nalemy), [qwqAutomaton](https://github.com/qwqAutomaton), [shawlleyw](https://github.com/shawlleyw), [Sshwy](mailto:hwy1272918035@outlook.com), [SukkaW](https://github.com/SukkaW), [UserUnauthorized](https://github.com/UserUnauthorized), [WineChord](https://github.com/WineChord), [yjl9903](https://github.com/yjl9903)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
