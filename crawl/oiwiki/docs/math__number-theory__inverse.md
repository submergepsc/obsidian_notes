# 模逆元 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/inverse/

# 模逆元

本文介绍模意义下乘法运算的逆元，并讨论它的常见求解方法．

## 基本概念

非零实数 𝑎 ∈𝐑a∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘法逆元就是它的倒数 𝑎−1a−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．类似地，数论中也可以定义一个整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的逆元 𝑎−1mod𝑚a−1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或简单地记作 𝑎−1a−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就是 **模逆元** （modular multiplicative inverse），也称作 **数论倒数** ．

逆元

对于非零整数 𝑎,𝑚a,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果存在 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑎𝑏 ≡1(mod𝑚)ab≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就称 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的 **逆元** （inverse）．

这相当于说，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是线性同余方程 𝑎𝑥 ≡1(mod𝑚)ax≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解．根据 [线性同余方程](../linear-equation/) 的性质可知，当且仅当 gcd(𝑎,𝑚) =1gcd(a,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑎,𝑚a,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素时，逆元 𝑎−1mod𝑚a−1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在，且在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的意义下是唯一的．

## 单个逆元的求法

利用扩展欧几里得算法或快速幂法，可以在 𝑂(log⁡𝑚)O(log⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内求出单个整数的逆元．

### 扩展欧几里得算法

求解逆元，就相当于求解线性同余方程．因此，可以使用 [扩展欧几里得算法](../gcd/#扩展欧几里得算法) 在 𝑂(log⁡min{𝑎,𝑚})O(log⁡min{a,m})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内求解逆元．同时，由于逆元对应的线性方程比较特殊，可以适当地简化相应的步骤．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text // Extended Euclidean algorithm. void ex_gcd ( int a , int b , int & x , int & y ) { if ( ! b ) { x = 1 ; y = 0 ; } else { ex_gcd ( b , a % b , y , x ); y -= a / b * x ; } } // Returns the modular inverse of a modulo m. // Assumes that gcd(a, m) = 1, so the inverse exists. int inverse ( int a , int m ) { int x , y ; ex_gcd ( a , m , x , y ); return ( x % m \+ m ) % m ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text # Extended Euclidean algorithm. def ex_gcd ( a , b ): if b == 0 : return 1 , 0 else : x1 , y1 = ex_gcd ( b , a % b ) x = y1 y = x1 \- ( a // b ) * y1 return x , y # Returns the modular inverse of a modulo m. # Assumes that gcd(a, m) = 1, so the inverse exists. def inverse ( a , m ): x , y = ex_gcd ( a , m ) return ( x % m \+ m ) % m ```   
---|---  
  
这一算法适用于所有逆元存在的情形．

### 快速幂法

这一方法主要适用于模数是素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．此时，由 [费马小定理](../fermat/#费马小定理) 可知对于任意 𝑎 ⟂𝑝a⟂p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有

𝑎⋅𝑎𝑝−2=𝑎𝑝−1≡1(mod𝑝).a⋅ap−2=ap−1≡1(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据逆元的唯一性可知，逆元 𝑎−1mod𝑝a−1modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就等于 𝑎𝑝−2mod𝑝ap−2modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此可以直接使用 [快速幂](../../binary-exponentiation/) 在 𝑂(log⁡𝑝)O(log⁡p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算：

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text // Binary exponentiation. int pow ( int a , int b , int m ) { long long res = 1 , po = a ; for (; b ; b >>= 1 ) { if ( b & 1 ) res = res * po % m ; po = po * po % m ; } return res ; } // Returns the modular inverse of a prime modulo p. int inverse ( int a , int p ) { return pow ( a , p \- 2 , p ); } ```   
---|---  
  
```text 1 2 3 4 ``` |  ```text # Returns the modular inverse of a prime modulo p. # Use built-in pow function. def inverse ( a , p ): return pow ( a , p \- 2 , p ) ```   
---|---  
  
当然，理论上，这一方法可以利用 [欧拉定理](../fermat/#欧拉定理) 推广到一般的模数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，即利用 𝑎𝜑(𝑚)−1mod𝑚aφ(m)−1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算逆元．但是，单次求解 [欧拉函数](../euler-totient/) 𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并不容易，因此该算法在一般情况下效率不高．

## 多个逆元的求法

有些场景下，需要快速处理出多个整数 𝑎1,𝑎2,⋯,𝑎𝑛a1,a2,⋯,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的逆元．此时，逐个求解逆元，总共需要 𝑂(𝑛log⁡𝑚)O(nlog⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间．实际上，如果将它们统一处理，就可以在 𝑂(𝑛 +log⁡𝑚)O(n+log⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内求出所有整数的逆元．

考虑序列 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀积：

𝑆0=1, 𝑆𝑖=𝑎𝑖𝑆𝑖−1, 𝑖=1,2,⋯,𝑛.S0=1, Si=aiSi−1, i=1,2,⋯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

只要每个 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素，它们的乘积 𝑆𝑛Sn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素．因此，可以通过前文所述算法求出 𝑆−1𝑛mod𝑚Sn−1modm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．因为乘积的逆元就是逆元的乘积，所以，从 𝑆−1𝑛Sn−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，反向遍历序列就能求出每个 𝑆𝑖Si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆元：

𝑆−1𝑖−1=𝑎𝑖𝑆−1𝑖mod𝑚, 𝑖=𝑛,𝑛−1,⋯,1.Si−1−1=aiSi−1modm, i=n,n−1,⋯,1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由此，单个 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆元可以通过下式计算：

𝑎−1𝑖=𝑆𝑖−1𝑆−1𝑖mod𝑚, 𝑖=1,2,⋯,𝑛.ai−1=Si−1Si−1modm, i=1,2,⋯,n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

参考实现如下：

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text // Returns the modular inverses for each x in a modulo m. // Assume x mod m exists for each x in a. std :: vector < int > batch_inverse ( const std :: vector < int >& a , int m ) { int n = a . size (); std :: vector < int > prod ( n ); long long s = 1 ; for ( int i = 0 ; i < n ; ++ i ) { // prod[i] = product of a[0...i-1]; prod[0] = 1. prod [ i ] = s ; s = s * a [ i ] % m ; } // s = product of all elements in a. s = inverse ( s , m ); std :: vector < int > res ( n ); for ( int i = n \- 1 ; i >= 0 ; \-- i ) { res [ i ] = s * prod [ i ] % m ; s = s * a [ i ] % m ; } return res ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text # Returns the modular inverses for each x in a modulo m. # Assume x mod m exists for each x in a. def batch_inverse ( a , m ): n = len ( a ) prod = [ 0 ] * n s = 1 for i in range ( n ): # prod[i] = product of a[0...i-1]; prod[0] = 1. prod [ i ] = s s = s * a [ i ] % m # s = product of all elements in a. s = inverse ( s , m ) res = [ 0 ] * n for i in reversed ( range ( n )): res [ i ] = s * prod [ i ] % m s = s * a [ i ] % m return res ```   
---|---  
  
算法中，只求了一次单个元素的逆元，因此总的时间复杂度是 𝑂(𝑛 +log⁡𝑚)O(n+log⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

## 线性时间预处理逆元

如果要预处理前 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个正整数在素数模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的逆元，还可以通过本节将要讨论的递推关系在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算．这一方法常用于组合数计算中前 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个正整数的阶乘的倒数的预处理．

对于 1 <𝑖 <𝑝1<i<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正整数 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考察带余除法：

𝑝=⌊𝑝𝑖⌋𝑖+(𝑝mod𝑖).p=⌊pi⌋i+(pmodi).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将该等式对素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模，就得到

0≡⌊𝑝𝑖⌋𝑖+(𝑝mod𝑖)(mod𝑝).0≡⌊pi⌋i+(pmodi)(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将等式两边同时乘以 𝑖−1(𝑝mod𝑖)−1i−1(pmodi)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就得到

𝑖−1≡−⌊𝑝𝑖⌋(𝑝mod𝑖)−1(mod𝑝).i−1≡−⌊pi⌋(pmodi)−1(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就是用于线性时间递推求逆元的公式．由于 𝑝mod𝑖 <𝑖pmodi<i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这一公式将求解 𝑖−1mod𝑝i−1modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的问题转化为规模更小的问题 (𝑝mod𝑖)−1mod𝑝(pmodi)−1modp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，从 1−1mod𝑝 =11−1modp=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始，对每个 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 顺次应用该公式，就可以在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内获得前 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数的逆元．

参考实现如下：

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // Precomputes modular inverses of all integers from 1 to n modulo prime p. std :: vector < int > precompute_inverses ( int n , int p ) { std :: vector < int > res ( n \+ 1 ); res [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; ++ i ) { res [ i ] = ( long long )( p \- p / i ) * res [ p % i ] % p ; } return res ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text # Precomputes modular inverses of all integers from 1 to n modulo prime p. def precompute_inverses ( n , p ): res = [ 0 ] * ( n \+ 1 ) res [ 1 ] = 1 for i in range ( 2 , n \+ 1 ): res [ i ] = ( p \- p // i ) * res [ p % i ] % p return res ```   
---|---  
  
这一算法只适用于模数是素数的情形．对于模数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是素数的情形，无法保证递推公式中得到的 𝑚mod𝑖mmodi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 仍然与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素，因而递推所需要的 (𝑚mod𝑖)−1(mmodi)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能并不存在．一个这样的例子是 𝑚 =8,𝑖 =3m=8,i=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时，𝑚mod𝑖 =2mmodi=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不存在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆元．

另外，得到该递推公式后，一种自然的想法是直接递归求解任意一个数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆元．每次递归时，都利用递推公式将它转化为更小的余数 𝑝mod𝑎pmoda![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆元，直到余数变为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时停止．目前尚不清楚这样做的复杂度1，因此，推荐使用前文所述的常规方法求解．

## 习题

  * [LOJ 110 乘法逆元](https://loj.ac/problem/110)
  * [LOJ 161 乘法逆元 2](https://loj.ac/problem/161)
  * [LOJ 2605「NOIP2012」同余方程](https://loj.ac/problem/2605)
  * [Luogu P2054「AHOI2005」洗牌](https://www.luogu.com.cn/problem/P2054)
  * [LOJ 2034「SDOI2016」排列计数](https://loj.ac/problem/2034)

## 参考资料与注释

  * [Modular multiplicative inverse - Wikipedia](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)

* * *

  1. [riteme 在知乎上的回答](https://www.zhihu.com/question/59033693/answer/323292359) 中指出，这样做理论上已知的复杂度的上界是 𝑂(𝑝1/3+𝜀)O(p1/3+ε)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而在实际随机数据中的表现接近于 𝑂(log⁡𝑝)O(log⁡p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/inverse.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/inverse.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Xeonacid](https://github.com/Xeonacid), [Enter-tainer](https://github.com/Enter-tainer), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [MegaOwIer](https://github.com/MegaOwIer), [PeterlitsZo](https://github.com/PeterlitsZo), [Tiphereth-A](https://github.com/Tiphereth-A), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [jifbt](https://github.com/jifbt), [Marcythm](https://github.com/Marcythm), [ouuan](https://github.com/ouuan), [stevebraveman](https://github.com/stevebraveman), [abc1763613206](https://github.com/abc1763613206), [buggg-hfc](https://github.com/buggg-hfc), [c-forrest](https://github.com/c-forrest), [Chrogeek](https://github.com/Chrogeek), [Early0v0](https://github.com/Early0v0), [Great-designer](https://github.com/Great-designer), [Henry-ZHR](https://github.com/Henry-ZHR), [hqztrue](https://github.com/hqztrue), [ImpleLee](https://github.com/ImpleLee), [JellyGoat](https://github.com/JellyGoat), [ksyx](https://github.com/ksyx), [lhhxxxxx](https://github.com/lhhxxxxx), [Menci](https://github.com/Menci), [MioChyan](https://github.com/MioChyan), [n-WN](https://github.com/n-WN), [Phemon](mailto:i@phemon.me), [shawlleyw](https://github.com/shawlleyw), [Siyuan](mailto:294873684@qq.com), [skr2005](https://github.com/skr2005), [thredreams](https://github.com/thredreams), [Tiooo111](https://github.com/Tiooo111), [WAAutoMaton](https://github.com/WAAutoMaton), [Zhaoyangzhen](https://github.com/Zhaoyangzhen)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
