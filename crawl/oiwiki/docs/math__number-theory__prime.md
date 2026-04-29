# 素数 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/prime/

# 素数

素数与合数的定义，见 [数论基础](../basic/)．

素数计数函数：小于或等于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素数的个数，用 𝜋(𝑥)π(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示．随着 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的增大，有这样的近似结果：𝜋(𝑥) ∼𝑥ln⁡(𝑥)π(x)∼xln⁡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 素性测试

**素性测试** （Primality test）可以用于判定所给自然数是否为素数．

素性测试有两种：

  1. 确定性测试：绝对确定一个数是否为素数．常见例子包括试除法、Lucas–Lehmer 测试和椭圆曲线素性证明．
  2. 概率性测试：通常比确定性测试快很多，但有可能（尽管概率很小）错误地将 [合数](../basic/#素数与合数) 识别为质数（尽管反之则不会）．因此，通过概率素性测试的数字被称为 **可能素数** ，直到它们的素数可以被确定性地证明．而通过测试但实际上是合数的数字则被称为 **伪素数** ．有许多特定类型的伪素数，最常见的是费马伪素数，它们是满足费马小定理的合数．概率性测试的常见例子包括 Miller–Rabin 测试．

### 试除法

暴力做法自然可以枚举从小到大的每个数看是否能整除．

参考实现

C++Python

```text 1 2 3 4 5 6 ``` |  ```text bool isPrime ( int a ) { if ( a < 2 ) return false ; for ( int i = 2 ; i < a ; ++ i ) if ( a % i == 0 ) return false ; return true ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text def isPrime ( a ): if a < 2 : return False for i in range ( 2 , a ): if a % i == 0 : return False return True ```   
---|---  
  
这样做是十分稳妥了，但是真的有必要每个数都去判断吗？

很容易发现这样一个事实：如果 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数，那么 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数．

这个结论告诉我们，对于每一对 (𝑥,𝑎𝑥)(x,ax)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只检验其中的一个就足够了．为了方便起见，我们只考察每一对的较小数．不难发现，所有这些较小数都在 [1,√𝑎][1,a]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这个区间里．

由于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 肯定是约数，所以不检验它．

参考实现

C++Python

```text 1 2 3 4 5 6 ``` |  ```text bool isPrime ( int a ) { if ( a < 2 ) return 0 ; for ( int i = 2 ; ( long long ) i * i <= a ; ++ i ) // 防溢出 if ( a % i == 0 ) return 0 ; return 1 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text def isPrime ( a ): if a < 2 : return False for i in range ( 2 , int ( sqrt ( a )) \+ 1 ): if a % i == 0 : return False return True ```   
---|---  
  
### Fermat 素性测试

**Fermat 素性检验** 是最简单的概率性素性检验．

我们可以根据 [费马小定理](../fermat/#费马小定理) 得出一种检验素数的思路：

基本思想是不断地选取在 [2,𝑛 −1][2,n−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的基底 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并检验是否每次都有 𝑎𝑛−1 ≡1(mod𝑛)an−1≡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text bool fermat ( int n ) { if ( n < 3 ) return n == 2 ; // test_time 为测试次数,建议设为不小于 8 // 的整数以保证正确率,但也不宜过大,否则会影响效率 for ( int i = 1 ; i <= test_time ; ++ i ) { int a = rand () % ( n \- 2 ) \+ 2 ; if ( quickPow ( a , n \- 1 , n ) != 1 ) return false ; } return true ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text def fermat ( n ): if n < 3 : return n == 2 # test_time 为测试次数,建议设为不小于 8 # 的整数以保证正确率,但也不宜过大,否则会影响效率 for i in range ( 1 , test_time \+ 1 ): a = random . randint ( 0 , 32767 ) % ( n \- 2 ) \+ 2 if quickPow ( a , n \- 1 , n ) != 1 : return False return True ```   
---|---  
  
如果 𝑎𝑛−1 ≡1(mod𝑛)an−1≡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 但 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是素数，则称 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为以 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为底的 **Fermat 伪素数** ．我们在实践中观察到，如果 𝑎𝑛−1 ≡1(mod𝑛)an−1≡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通常是素数．但其实存在反例：对于 𝑛 =341n=341![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎 =2a=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，虽然有 2340 ≡1(mod341)2340≡1(mod341)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是 341 =11 ⋅31341=11⋅31![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是合数．事实上，对于任何固定的基底 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这样的反例都有无穷多个1．

既然对于单个基底，Fermat 素性测试无法保证正确性，一个自然的想法就是多检查几组基底．但是，即使检查了所有可能的与 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素的基底 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，依然无法保证 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数．也就是说，费马小定理的逆命题并不成立：即使对于所有 𝑎 ⟂𝑛a⟂n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑎𝑛−1 ≡1(mod𝑛)an−1≡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也不一定是素数．这样的数称为 [Carmichael 数](../primitive-root/#carmichael-数)．它也有无穷多个．这迫使我们寻找更为严格的素性测试．

### Miller–Rabin 素性测试

**Miller–Rabin 素性测试** （Miller–Rabin primality test）是更好的素数判定方法．它是由 Miller 和 Rabin 二人根据 Fermat 素性测试优化得到的．和其它概率性素数测试一样，它也只能检测出伪素数．要确保是素数，需要用慢得多的确定性算法．然而，实际上没有已知的数字通过了 Miller–Rabin 测试等高级概率性测试但实际上却是合数，因此我们可以放心使用．

在不考虑乘法的复杂度时，对数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 轮测试的时间复杂度是 𝑂(𝑘log⁡𝑛)O(klog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．Miller–Rabin 素性测试常用于对高精度数进行测试，此时时间复杂度是 𝑂(𝑘log3⁡𝑛)O(klog3⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，利用 FFT 等技术可以优化到 [𝑂(𝑘log2⁡𝑛log⁡log⁡𝑛log⁡log⁡log⁡𝑛)O(klog2⁡nlog⁡log⁡nlog⁡log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Complexity)．

为了解决 Carmichael 数带来的挑战，Miller–Rabin 素性测试进一步考虑了素数的如下性质：

二次探测定理

如果 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇素数，则 𝑥2 ≡1(mod𝑝)x2≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解为 𝑥 ≡1(mod𝑝)x≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或者 𝑥 ≡𝑝 −1(mod𝑝)x≡p−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

容易验证，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为奇素数时，𝑥 ≡1(mod𝑝)x≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥 ≡𝑝 −1(mod𝑝)x≡p−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都可以使得上式成立．由 [Lagrange 定理](../congruence-equation/#定理-3lagrange-定理) 可知，这就是该方程的所有解．

将费马小定理和二次探测定理结合起来使用，就得到 Miller–Rabin 素性测试：

  1. 将 𝑎𝑛−1 ≡1(mod𝑛)an−1≡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的指数 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解为 𝑛 −1 =𝑢 ×2𝑡n−1=u×2t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 在每轮测试中对随机出来的 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 先求出 𝑣 =𝑎𝑢mod𝑛v=aumodn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，之后对这个值执行最多 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次平方操作；
  3. 在整个过程中，如果发现 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非平凡平方根（即除了 ±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之外的其他根），就可以判断该数不是素数；
  4. 否则，再使用 Fermat 素性测试判断．

还有一些实现上的小细节：

  * 对于一轮测试，如果某一时刻 𝑎𝑢×2𝑠 ≡𝑛 −1(mod𝑛)au×2s≡n−1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则之后的平方操作全都会得到 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则可以直接通过本轮测试．
  * 如果找出了一个非平凡平方根 𝑎𝑢×2𝑠 ≢𝑛 −1(mod𝑛)au×2s≢n−1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则之后的平方操作全都会得到 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．可以选择直接返回 `false`，也可以放到 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次平方操作后再返回 `false`．

这样得到了较正确的 Miller Rabin：（来自 fjzzq2002）

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text bool millerRabin ( int n ) { if ( n < 3 || n % 2 == 0 ) return n == 2 ; if ( n % 3 == 0 ) return n == 3 ; int u = n \- 1 , t = 0 ; while ( u % 2 == 0 ) u /= 2 , ++ t ; // test_time 为测试次数，建议设为不小于 8 // 的整数以保证正确率，但也不宜过大，否则会影响效率 for ( int i = 0 ; i < test_time ; ++ i ) { // 0, 1, n-1 可以直接通过测试, a 取值范围 [2, n-2] int a = rand () % ( n \- 3 ) \+ 2 , v = quickPow ( a , u , n ); if ( v == 1 ) continue ; int s ; for ( s = 0 ; s < t ; ++ s ) { if ( v == n \- 1 ) break ; // 得到平凡平方根 n-1，通过此轮测试 v = ( long long ) v * v % n ; } // 如果找到了非平凡平方根，则会由于无法提前 break; 而运行到 s == t // 如果 Fermat 素性测试无法通过，则一直运行到 s == t 前 v 都不会等于 -1 if ( s == t ) return 0 ; } return 1 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` |  ```text def millerRabin ( n ): if n < 3 or n % 2 == 0 : return n == 2 if n % 3 == 0 : return n == 3 u , t = n \- 1 , 0 while u % 2 == 0 : u = u // 2 t = t \+ 1 # test_time 为测试次数,建议设为不小于 8 # 的整数以保证正确率,但也不宜过大,否则会影响效率 for i in range ( test_time ): # 0, 1, n-1 可以直接通过测试, a 取值范围 [2, n-2] a = random . randint ( 2 , n \- 2 ) v = pow ( a , u , n ) if v == 1 : continue s = 0 while s < t : if v == n \- 1 : break v = v * v % n s = s \+ 1 # 如果找到了非平凡平方根，则会由于无法提前 break; 而运行到 s == t # 如果 Fermat 素性测试无法通过，则一直运行到 s == t 前 v 都不会等于 -1 if s == t : return False return True ```   
---|---  
  
可以证明2，奇合数 𝑛 >9n>9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通过随机选取的一个基底 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Miller–Rabin 素性测试的概率至多为四分之一．因此，随机选取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个基底后，仍将合数误判为素数的概率不超过 1/4𝑘1/4k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

设 𝑛 −1 =𝑢2𝑡n−1=u2t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇数且 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是正整数．那么，整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以通过基底为 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Miller–Rabin 素性测试说明

𝑎𝑢≡1(mod𝑛), or 𝑎𝑢2𝑖≡−1(mod𝑛) for some 0≤𝑖<𝑡.au≡1(modn), or au2i≡−1(modn) for some 0≤i<t.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

记这样的 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（的同余类）集合为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要说明的是

|𝑆|≤14𝜑(𝑛).|S|≤14φ(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝜑(𝑛)φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 [欧拉函数](../euler-totient/)．证明分为三步．

**第一步** ：设 ℓℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是使得 2ℓ ∣𝑝 −12ℓ∣p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对所有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立的最大正整数．那么，可以证明

𝑆⊆𝑆′={𝑎mod𝑛:𝑎𝑢2ℓ−1≡±1(mod𝑛)}.S⊆S′={amodn:au2ℓ−1≡±1(modn)}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的元素 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只有两种可能．如果 𝑎𝑢 ≡1(mod𝑛)au≡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，显然 𝑎𝑢2ℓ−1 ≡1(mod𝑛)au2ℓ−1≡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也成立，亦即 𝑎 ∈𝑆′a∈S′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果对于 0 ≤𝑖 <𝑡0≤i<t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立 𝑎𝑢2𝑖 ≡ −1(mod𝑛)au2i≡−1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，对于任意素因子 𝑝 ∣𝑛p∣n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑎𝑢2𝑖 ≡ −1(mod𝑝)au2i≡−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 𝛿𝑝(𝑎)δp(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [阶](../primitive-root/#阶)，那么，显然有 𝛿𝑝(𝑎) ∣𝑢2𝑖+1δp(a)∣u2i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 但是 𝛿𝑝(𝑎) ∤𝑢2𝑖δp(a)∤u2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这说明，𝛿𝑝(𝑎)δp(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素因数分解中，22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的指数恰为 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因而 2𝑖+1 ∣𝛿𝑝(𝑎)2i+1∣δp(a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由费马小定理可知，𝛿𝑝(𝑎) ∣𝑝 −1δp(a)∣p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，2𝑖+1 ∣𝑝 −12i+1∣p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这一点对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有素因子 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．因此，𝑖 +1 ≤ℓi+1≤ℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这说明 𝑎𝑢2ℓ−1 =(𝑎𝑢2𝑖)2ℓ−1−𝑖 ≡ ±1(mod𝑛)au2ℓ−1=(au2i)2ℓ−1−i≡±1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，同样有 𝑎 ∈𝑆′a∈S′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．综合两种可能，就得到 𝑆 ⊆𝑆′S⊆S′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**第二步** ：计算 |𝑆′||S′|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小．

假设 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有素因数分解 𝑛 =𝑝𝑒11𝑝𝑒22⋯𝑝𝑒𝑘𝑘n=p1e1p2e2⋯pkek![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，由 [中国剩余定理](../crt/) 可知，条件 𝑎𝑢2ℓ−1 ≡1(mod𝑛)au2ℓ−1≡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价于 𝑎𝑢2ℓ−1 ≡1(mod𝑝𝑒𝑖𝑖)au2ℓ−1≡1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对所有 𝑝𝑒𝑖𝑖piei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．由于模奇素数幂 𝑝𝑒𝑖𝑖piei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [原根](../primitive-root/#原根) 总是存在的，所以，同余方程 𝑎𝑢2ℓ−1 ≡1(mod𝑝𝑒𝑖𝑖)au2ℓ−1≡1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [解的数量](../residue/#性质) 为

gcd(𝑢2ℓ−1,𝑝𝑒𝑖−1𝑖(𝑝𝑖−1))=gcd(𝑢2ℓ−1,𝑝𝑖−1)=2ℓ−1gcd(𝑢,𝑝𝑖−1).gcd(u2ℓ−1,piei−1(pi−1))=gcd(u2ℓ−1,pi−1)=2ℓ−1gcd(u,pi−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

第一个等号成立，是因为 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的因子，不可能是 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数；第二个等号成立，是因为 ℓℓ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的选取方式．所以，由中国剩余定理可知，同余方程 𝑎𝑢2ℓ−1 ≡1(mod𝑛)au2ℓ−1≡1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解的数量为

∏𝑝∣𝑛2ℓ−1gcd(𝑢,𝑝−1).∏p∣n2ℓ−1gcd(u,p−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

同理，条件 𝑎𝑢2ℓ−1 ≡ −1(mod𝑛)au2ℓ−1≡−1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价于 𝑎𝑢2ℓ−1 ≡ −1(mod𝑝𝑒𝑖𝑖)au2ℓ−1≡−1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对所有 𝑝𝑒𝑖𝑖piei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．对于任意因子 𝑝𝑒𝑖𝑖piei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，条件 𝑎𝑢2ℓ−1 ≡ −1(mod𝑝𝑒𝑖𝑖)au2ℓ−1≡−1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都等价于 𝑎𝑢2ℓ−1 ≢1(mod𝑝𝑒𝑖𝑖)au2ℓ−1≢1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎𝑢2ℓ ≡1(mod𝑝𝑒𝑖𝑖)au2ℓ≡1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．类似上文，可以计算出同余方程 𝑎𝑢2ℓ ≡1(mod𝑝𝑒𝑖𝑖)au2ℓ≡1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解的数量为 2ℓgcd(𝑢,𝑝𝑖 −1)2ℓgcd(u,pi−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此，同余方程 𝑎𝑢2ℓ−1 ≡ −1(mod𝑝𝑒𝑖𝑖)au2ℓ−1≡−1(modpiei)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解的数量也等于

2ℓgcd(𝑢,𝑝𝑖−1)−2ℓ−1gcd(𝑢,𝑝𝑖−1)=2ℓ−1gcd(𝑢,𝑝𝑖−1).2ℓgcd(u,pi−1)−2ℓ−1gcd(u,pi−1)=2ℓ−1gcd(u,pi−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

再次应用中国剩余定理，就得到同余方程 𝑎𝑢2ℓ−1 ≡ −1(mod𝑛)au2ℓ−1≡−1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解的数量等于

∏𝑝∣𝑛2ℓ−1gcd(𝑢,𝑝−1).∏p∣n2ℓ−1gcd(u,p−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，综合两种情形，有

|𝑆′|=2∏𝑝∣𝑛2ℓ−1gcd(𝑢,𝑝−1).|S′|=2∏p∣n2ℓ−1gcd(u,p−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**第三步** ：证明 |𝑆′| ≤𝜑(𝑛)/4|S′|≤φ(n)/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

结合欧拉函数的表达式 𝜑(𝑛) =∏𝑖𝑝𝑒𝑖−1𝑖(𝑝𝑖 −1)φ(n)=∏ipiei−1(pi−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知

𝜑(𝑛)|𝑆′|=12∏𝑖𝑝𝑒𝑖−1𝑖𝑝𝑖−12ℓ−1gcd(𝑢,𝑝𝑖−1).φ(n)|S′|=12∏ipiei−1pi−12ℓ−1gcd(u,pi−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于每一个 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，相应的因子 𝑝𝑒𝑖−1𝑖𝑝𝑖−12ℓ−1gcd(𝑢,𝑝𝑖−1)piei−1pi−12ℓ−1gcd(u,pi−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是一个偶数，所以，𝜑(𝑛)/|𝑆′|φ(n)/|S′|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个整数．假设 |𝑆′| ≤𝜑(𝑛)/4|S′|≤φ(n)/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不成立．必然有 𝜑(𝑛)/|𝑆′| =1,2,3φ(n)/|S′|=1,2,3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即

∏𝑖𝑝𝑒𝑖−1𝑖𝑝𝑖−12ℓ−1gcd(𝑢,𝑝𝑖−1)=2,4,6.∏ipiei−1pi−12ℓ−1gcd(u,pi−1)=2,4,6.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于连乘式中的每个因子都是偶数，所以，这个连乘式要么只有一个因子且这个因子就等于 2,4,62,4,6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要么就只有两个因子且都等于 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

首先考虑有两个因子的情形．此时，两个因子都没有奇素因子，所以，𝑝𝑒𝑖−1𝑖 =1piei−1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有平方因子．不妨设 𝑛 =𝑝1𝑝2n=p1p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑝1 <𝑝2p1<p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是素数．两个因子都等于 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以，总有 𝑝𝑖 −1 =2ℓgcd(𝑢,𝑝𝑖 −1)pi−1=2ℓgcd(u,pi−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，𝑝𝑖 =1 +2ℓ𝑚𝑖pi=1+2ℓmi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑚𝑖mi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇数，而且 𝑚𝑖 ∣𝑢mi∣u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．将 𝑝1𝑝2 =𝑛 =1 +𝑢2𝑡p1p2=n=1+u2t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对 𝑚1m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模就得到 𝑝1𝑝2 ≡1(mod𝑚1)p1p2≡1(modm1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而 𝑝2 ≡1(mod𝑚1)p2≡1(modm1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这说明，𝑚1 ∣𝑚2m1∣m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．反过来也成立．这就说明 𝑚1 =𝑚2m1=m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是 𝑝1 =𝑝2p1=p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这与 𝑝1 <𝑝2p1<p2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矛盾．这一情形不成立．

最后，考虑只有一个因子的情形，亦即合数 𝑛 =𝑝𝑒n=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑒 >1e>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时，必然有 𝑝𝑒−1 ∣2,4,6pe−1∣2,4,6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，唯一的情形是 𝑝 =3,𝑒 =2p=3,e=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即 𝑛 =9n=9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，与命题所设相矛盾．这一情形也不成立．

综合所有情形可知，|𝑆′| ≤𝜑(𝑛)/4|S′|≤φ(n)/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．

结合上述三个步骤可知，|𝑆| ≤|𝑆′| ≤𝜑(𝑛)/4|S|≤|S′|≤φ(n)/4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有奇合数 𝑛 >9n>9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立．

另外，假设 [广义 Riemann 猜想](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis)（generalized Riemann hypothesis, GRH）成立，则对数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最多只需要测试 [2,min{𝑛 −2,⌊2ln2⁡𝑛⌋}][2,min{n−2,⌊2ln2⁡n⌋}]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的全部整数即可 **确定** 数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素性．3

而在 OI 范围内，通常都是对 [1,264)[1,264)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 范围内的数进行素性检验．对于 [1,232)[1,232)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 范围内的数，选取 {2,7,61}{2,7,61}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 三个数作为基底进行 Miller–Rabin 素性检验就可以确定素性；对于 [1,264)[1,264)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 范围内的数，选取 {2,325,9375,28178,450775,9780504,1795265022}{2,325,9375,28178,450775,9780504,1795265022}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 七个数作为基底进行 Miller–Rabin 素性检验就可以确定素性．4

也可以选取 {2,3,5,7,11,13,17,19,23,29,31,37}{2,3,5,7,11,13,17,19,23,29,31,37}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即前 1212![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个素数）检验 [1,264)[1,264)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 范围内的素数．

注意如果要使用上面的数列中的数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为基底判断 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素性：

  * 所有的数都要取一遍，不能只选小于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的；
  * 把 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 换成 𝑎mod𝑛amodn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 如果 𝑎 ≡0(mod𝑛)a≡0(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑎 ≡ ±1(mod𝑛)a≡±1(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则直接通过该轮测试．

## 反素数

顾名思义，素数就是因子只有两个的数，那么反素数，就是因子最多的数（并且因子个数相同的时候值最小），所以反素数是相对于一个集合来说的．

一种符合直觉的反素数定义是：在一个正整数集合中，因子最多并且值最小的数，就是反素数．

反素数

对于某个正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果任何小于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正数的约数个数都小于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数个数，则称为是 **反素数** （anti-prime, a.k.a., highly compositive numbers）．

注意

注意区分 [emirp](https://en.wikipedia.org/wiki/Emirp)，它表示的是逐位反转后是不同素数的素数（如 149 和 941 均为 emirp，101 不是 emirp）．

### 过程

那么，如何来求解反素数呢？

首先，既然要求因子数，首先要做的就是素因子分解．把 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解成 𝑛 =𝑝𝑘11𝑝𝑘22⋯𝑝𝑘𝑛𝑛n=p1k1p2k2⋯pnkn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，其中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数，𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为他的指数．这样的话总因子个数就是 (𝑘1 +1) ×(𝑘2 +1) ×(𝑘3 +1)⋯ ×(𝑘𝑛 +1)(k1+1)×(k2+1)×(k3+1)⋯×(kn+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

但是显然质因子分解的复杂度是很高的，并且前一个数的结果不能被后面利用．所以要换个方法．

我们来观察一下反素数的特点．

  1. 反素数肯定是从 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始的连续素数的幂次形式的乘积．

  2. 数值小的素数的幂次大于等于数值大的素数，即 𝑛 =𝑝𝑘11𝑝𝑘22⋯𝑝𝑘𝑛𝑛n=p1k1p2k2⋯pnkn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，有 𝑘1 ≥𝑘2 ≥𝑘3 ≥⋯ ≥𝑘𝑛k1≥k2≥k3≥⋯≥kn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解释：

  1. 如果不是从 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始的连续素数，那么如果幂次不变，把素数变成数值更小的素数，那么此时因子个数不变，但是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数值变小了．交换到从 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始的连续素数的时候 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值最小．

  2. 如果数值小的素数的幂次小于数值大的素数的幂，那么如果把这两个素数交换位置（幂次不变），那么所得的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 因子数量不变，但是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值变小．

另外还有两个问题，

  1. 对于给定的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要枚举到哪一个素数呢？

最极端的情况大不了就是 𝑛 =𝑝1𝑝2⋯𝑝𝑛n=p1p2⋯pn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以只要连续素数连乘到刚好小于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．如果枚举到更大的素数，则意味这必定某个之前素数的幂次为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么就不可能成为反素数．

  2. 我们要枚举到多少次幂呢？

我们考虑一个极端情况，当我们最小的素数的某个幂次已经比所给的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（的最大值）大的话，那么展开成其他的形式，最大幂次一定小于这个幂次．极端情况下 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的次幂，那么枚举到 ⌊log2⁡𝑛⌋⌊log2⁡n⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

细节有了，那么我们具体如何具体实现呢？

我们可以把当前走到每一个素数前面的时候列举成一棵树的根节点，然后一层层的去找．找到什么时候停止呢？

  1. 当前走到的数字已经大于我们想要的数字了；

  2. 当前枚举的因子已经用不到了；

  3. 当前因子大于我们想要的因子了；

  4. 当前因子正好是我们想要的因子（此时判断是否需要更新最小 ansans![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

然后 dfs 里面不断一层一层枚举次数继续往下迭代可以．

### 例题

[Codeforces 27E. A number with a given number of divisors](https://codeforces.com/problemset/problem/27/E)

求具有给定除数个数的最小自然数．答案保证不超过 10181018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

解题思路

对于这种题，我们只要以因子数为 dfs 的返回条件基准，不断更新找到的最小值就可以了．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text #include <iostream> constexpr int p [ 15 ] = { 2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29 , 31 , 37 , 41 , 43 , 47 }; // p 中的素数乘积超过了 1e18 int n ; long long ans = 2e18 ; // u: 当前考虑的质数在 p 中的下标 // num: 当前构成的数值 // cnt: 当前数值的因数个数 // pre: 上一个因子的幂次，限定本次选择的幂次 void dfs ( int u , long long num , long long cnt , int pre ) { if ( cnt > n || u >= 15 ) return ; if ( cnt == n ) return ans = std :: min ( ans , num ), void (); for ( int i = 1 ; i <= pre ; ++ i ) { if ( num * p [ u ] > ans ) break ; // 剪枝 dfs ( u \+ 1 , num *= p [ u ], cnt * ( i \+ 1 ), i ); } } int main () { std :: cin >> n ; dfs ( 0 , 1 , 1 , 59 ); // floor(log2(1e18))=19 std :: cout << ans << std :: endl ; return 0 ; } ```   
---|---  
  
[ZOJ 2562 More Divisors](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827366061)

求不超过 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数中，除数最多的数．

解题思路

思路同上，只不过要改改 dfs 的返回条件．注意这样的题目的数据范围，32 位整数可能溢出．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` |  ```text #include <iostream> int p [ 16 ] = { 2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29 , 31 , 37 , 41 , 43 , 47 , 53 }; unsigned long long n ; unsigned long long ans , ans_num ; // ans 为 n 以内的最大反素数（会持续更新），ans_sum 为 // ans的因子数。 // depth: 当前在枚举第几个素数 // temp: 当前因子数量为 num 的时候的数值 // num: 当前因子数 // up：上一个素数的幂，限制当前因子幂次上界 void dfs ( int depth , unsigned long long temp , unsigned long long num , int up ) { if ( depth >= 16 || temp > n ) return ; if ( num > ans_num ) { // 更新答案 ans = temp ; ans_num = num ; } if ( num == ans_num && ans > temp ) ans = temp ; // 更新答案 for ( int i = 1 ; i <= up ; i ++ ) { if ( temp * p [ depth ] > n ) break ; // 剪枝：如果加一个这个乘数的结果比ans要大，则必不是最佳方案 dfs ( depth \+ 1 , temp *= p [ depth ], num * ( i \+ 1 ), i ); // 取一个该乘数，进行对下一个乘数的搜索 } return ; } using std :: cin ; using std :: cout ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); while ( cin >> n ) { ans_num = 0 ; dfs ( 0 , 1 , 1 , 60 ); cout << ans << '\n' ; } return 0 ; } ```   
---|---  
  
## 参考资料与注释

  1. Rui-Juan Jing, Marc Moreno-Maza, Delaram Talaashrafi, "[Complexity Estimates for Fourier-Motzkin Elimination](https://arxiv.org/abs/1811.01510)", Journal of Functional Programming 16:2 (2006) pp 197-217.
  2. [数论部分第一节：素数与素性测试](http://www.matrix67.com/blog/archives/234)
  3. [Miller–Rabin 与 Pollard–Rho 学习笔记 - Bill Yang's Blog](https://blog.bill.moe/miller-rabin-notes/)
  4. [Primality test - Wikipedia](https://en.wikipedia.org/wiki/Primality_test)
  5. [Fermat pseudoprime - Wikipedia](https://en.wikipedia.org/wiki/Fermat_pseudoprime)
  6. [桃子的算法笔记——反素数详解（acm/OI）](https://zhuanlan.zhihu.com/p/41759808)
  7. [The Rabin-Miller Primality Test](http://home.sandiego.edu/~dhoffoss/teaching/cryptography/10-Rabin-Miller.pdf)
  8. [Highly composite number - Wikipedia](https://en.wikipedia.org/wiki/Highly_composite_number)

* * *

  1. Pomerance, Carl, John L. Selfridge, and Samuel S. Wagstaff. "The pseudoprimes to 25⋅ 10⁹." Mathematics of Computation 35, no. 151 (1980): 1003-1026. 的定理 1 说明了，对于固定的基底 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，能够通过更强的 Miller–Rabin 素性测试的合数也是无穷多的． ↩

  2. 本结论及其证明参考了 Crandall, Richard, and Carl Pomerance. Prime numbers: a computational perspective. New York, NY: Springer New York, 2005. 的第 3.5 节． ↩

  3. Bach, Eric , "[Explicit bounds for primality testing and related problems](https://doi.org/10.2307%2F2008811)", Mathematics of Computation, 55:191 (1990) pp 355–380. ↩

  4. 更多类似的结果请参考 [Deterministic variant of the Miller–Rabin primality test](https://miller-rabin.appspot.com/#)． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/prime.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/prime.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Xeonacid](https://github.com/Xeonacid), [Enter-tainer](https://github.com/Enter-tainer), [StudyingFather](https://github.com/StudyingFather), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [MegaOwIer](https://github.com/MegaOwIer), [383494](https://github.com/383494), [Alpacabla](https://github.com/Alpacabla), [HeRaNO](https://github.com/HeRaNO), [abc1763613206](https://github.com/abc1763613206), [alphagocc](https://github.com/alphagocc), [Backl1ght](https://github.com/Backl1ght), [CCXXXI](https://github.com/CCXXXI), [drkelo](https://github.com/drkelo), [Early0v0](https://github.com/Early0v0), [Great-designer](https://github.com/Great-designer), [greyqz](https://github.com/greyqz), [GuanghaoYe](https://github.com/GuanghaoYe), [H-J-Granger](https://github.com/H-J-Granger), [HHH2309](https://github.com/HHH2309), [isdanni](https://github.com/isdanni), [kenlig](https://github.com/kenlig), [lazyasn](https://github.com/lazyasn), [Menci](https://github.com/Menci), [ouuan](https://github.com/ouuan), [r-value](https://github.com/r-value), [shawlleyw](https://github.com/shawlleyw), [shopee-jin](https://github.com/shopee-jin), [shuzhouliu](https://github.com/shuzhouliu), [sun2snow](https://github.com/sun2snow), [untitledunrevised](https://github.com/untitledunrevised), [void-mian](https://github.com/void-mian), [Voileexperiments](https://github.com/Voileexperiments), [weilycoder](https://github.com/weilycoder), [xtlsoft](https://github.com/xtlsoft), [yusancky](https://github.com/yusancky), [YuzhenQin1](https://github.com/YuzhenQin1), [Siger Young](mailto:siger-young@users.noreply.github.com), [Siger Young](https://github.com/Siger Young), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [TrisolarisHD](https://github.com/TrisolarisHD)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
