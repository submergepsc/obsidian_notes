# 多项式初等函数 - OI Wiki

- Source: https://oi-wiki.org/math/poly/elementary-func/

# 多项式初等函数

本页面包含多项式常见的初等函数操作．具体而言，本页面包含如下内容：

  1. 多项式求逆
  2. 多项式开方
  3. 多项式除法
  4. 多项式取模
  5. 多项式指数函数
  6. 多项式对数函数
  7. 多项式三角函数
  8. 多项式反三角函数

初等函数与非初等函数

初等函数的定义如下1：

若域 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中存在映射 𝑢 →𝜕𝑢u→∂u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足：

  1. 𝜕(𝑢 +𝑣) =𝜕𝑢 +𝜕𝑣∂(u+v)=∂u+∂v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 𝜕(𝑢𝑣) =𝑢𝜕𝑣 +𝑣𝜕𝑢∂(uv)=u∂v+v∂u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则称这个域为 **微分域** ．

若微分域 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的函数 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足以下的任意一条条件，则称该函数 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为初等函数：

  1. 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的代数函数．
  2. 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的指数性函数，即存在 𝑎 ∈𝐹a∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝜕𝑢 =𝑢𝜕𝑎∂u=u∂a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).
  3. 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的对数性函数，即存在 𝑎 ∈𝐹a∈F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝜕𝑢 =𝜕𝑎𝑎∂u=∂aa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

以下是常见的初等函数：

  1. 代数函数：存在有限次多项式 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑃(𝑓(𝑥)) =0P(f(x))=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的函数 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如 2𝑥 +12x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),√𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),(1 +𝑥2)−1(1+x2)−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),|𝑥||x|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).
  2. 指数函数
  3. 对数函数
  4. 三角函数
  5. 反三角函数
  6. 双曲函数
  7. 反双曲函数
  8. 以上函数的复合，如：

etan⁡𝑥1+𝑥2sin⁡(√1+ln2⁡𝑥)etan⁡x1+x2sin⁡(1+ln2⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) −iln⁡(𝑥+i√1−𝑥2)−iln⁡(x+i1−x2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

以下是常见的非初等函数：

  1. 误差函数：

erf⁡(𝑥):=2√𝜋∫𝑥0exp⁡(−𝑡2)d𝑡erf⁡(x):=2π∫0xexp⁡(−t2)dt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 多项式求逆

给定多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 𝑓−1(𝑥)f−1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 解法

#### 倍增法

首先，易知

[𝑥0]𝑓−1(𝑥)=([𝑥0]𝑓(𝑥))−1[x0]f−1(x)=([x0]f(x))−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

假设现在已经求出了 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑥⌈𝑛2⌉x⌈n2⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的逆元 𝑓−10(𝑥)f0−1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． 有：

𝑓(𝑥)𝑓−10(𝑥)≡1(mod𝑥⌈𝑛2⌉)𝑓(𝑥)𝑓−1(𝑥)≡1(mod𝑥⌈𝑛2⌉)𝑓−1(𝑥)−𝑓−10(𝑥)≡0(mod𝑥⌈𝑛2⌉)f(x)f0−1(x)≡1(modx⌈n2⌉)f(x)f−1(x)≡1(modx⌈n2⌉)f−1(x)−f0−1(x)≡0(modx⌈n2⌉)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

两边平方可得：

𝑓−2(𝑥)−2𝑓−1(𝑥)𝑓−10(𝑥)+𝑓−20(𝑥)≡0(mod𝑥𝑛)f−2(x)−2f−1(x)f0−1(x)+f0−2(x)≡0(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

两边同乘 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并移项可得：

𝑓−1(𝑥)≡𝑓−10(𝑥)(2−𝑓(𝑥)𝑓−10(𝑥))(mod𝑥𝑛)f−1(x)≡f0−1(x)(2−f(x)f0−1(x))(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

递归计算即可．

**时间复杂度**

𝑇(𝑛)=𝑇(𝑛2)+𝑂(𝑛log⁡𝑛)=𝑂(𝑛log⁡𝑛)T(n)=T(n2)+O(nlog⁡n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

#### Newton's Method

参见 [Newton's Method](../newton/#newtons-method).

#### Graeffe 法

欲求 𝑓−1(𝑥)mod𝑥2𝑛f−1(x)modx2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 考虑

𝑓−1(𝑥)mod𝑥2𝑛=𝑓(−𝑥)(𝑓(𝑥)𝑓(−𝑥))−1mod𝑥2𝑛=𝑓(−𝑥)𝑔−1(𝑥2)mod𝑥2𝑛f−1(x)modx2n=f(−x)(f(x)f(−x))−1modx2n=f(−x)g−1(x2)modx2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

只需求出 𝑔−1(𝑥)mod𝑥𝑛g−1(x)modxn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可还原出 𝑔−1(𝑥2)mod𝑥2𝑛g−1(x2)modx2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 因为 𝑓(𝑥)𝑓( −𝑥)f(x)f(−x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶函数，时间复杂度同上．

### 代码

多项式求逆

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text constexpr int MAXN = 262144 ; constexpr int mod = 998244353 ; using i64 = long long ; using poly_t = int [ MAXN ]; using poly = int * const ; void polyinv ( const poly & h , const int n , poly & f ) { /* f = 1 / h = f_0 (2 - f_0 h) */ static poly_t inv_t ; std :: fill ( f , f \+ n \+ n , 0 ); f [ 0 ] = fpow ( h [ 0 ], mod \- 2 ); for ( int t = 2 ; t <= n ; t <<= 1 ) { const int t2 = t << 1 ; std :: copy ( h , h \+ t , inv_t ); std :: fill ( inv_t \+ t , inv_t \+ t2 , 0 ); DFT ( f , t2 ); DFT ( inv_t , t2 ); for ( int i = 0 ; i != t2 ; ++ i ) f [ i ] = ( i64 ) f [ i ] * sub ( 2 , ( i64 ) f [ i ] * inv_t [ i ] % mod ) % mod ; IDFT ( f , t2 ); std :: fill ( f \+ t , f \+ t2 , 0 ); } } ```   
---|---  
  
### 例题

  1. 有标号简单无向连通图计数：[「POJ 1737」Connected Graph](http://poj.org/problem?id=1737)

## 多项式开方

给定多项式 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足：

𝑓2(𝑥)≡𝑔(𝑥)(mod𝑥𝑛)f2(x)≡g(x)(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 解法

#### 倍增法

首先讨论 [𝑥0]𝑔(𝑥)[x0]g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况．

易知：

[𝑥0]𝑓(𝑥)=√[𝑥0]𝑔(𝑥)[x0]f(x)=[x0]g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若 [𝑥0]𝑔(𝑥)[x0]g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有平方根，则多项式 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有平方根．

> [𝑥0]𝑔(𝑥)[x0]g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能有多个平方根，选取不同的根会求出不同的 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

假设现在已经求出了 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑥⌈𝑛2⌉x⌈n2⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的平方根 𝑓0(𝑥)f0(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有：

𝑓20(𝑥)≡𝑔(𝑥)(mod𝑥⌈𝑛2⌉)𝑓20(𝑥)−𝑔(𝑥)≡0(mod𝑥⌈𝑛2⌉)(𝑓20(𝑥)−𝑔(𝑥))2≡0(mod𝑥𝑛)(𝑓20(𝑥)+𝑔(𝑥))2≡4𝑓20(𝑥)𝑔(𝑥)(mod𝑥𝑛)(𝑓20(𝑥)+𝑔(𝑥)2𝑓0(𝑥))2≡𝑔(𝑥)(mod𝑥𝑛)𝑓20(𝑥)+𝑔(𝑥)2𝑓0(𝑥)≡𝑓(𝑥)(mod𝑥𝑛)2−1𝑓0(𝑥)+2−1𝑓−10(𝑥)𝑔(𝑥)≡𝑓(𝑥)(mod𝑥𝑛)f02(x)≡g(x)(modx⌈n2⌉)f02(x)−g(x)≡0(modx⌈n2⌉)(f02(x)−g(x))2≡0(modxn)(f02(x)+g(x))2≡4f02(x)g(x)(modxn)(f02(x)+g(x)2f0(x))2≡g(x)(modxn)f02(x)+g(x)2f0(x)≡f(x)(modxn)2−1f0(x)+2−1f0−1(x)g(x)≡f(x)(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

倍增计算即可．

**时间复杂度**

𝑇(𝑛)=𝑇(𝑛2)+𝑂(𝑛log⁡𝑛)=𝑂(𝑛log⁡𝑛)T(n)=T(n2)+O(nlog⁡n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

还有一种常数较小的写法就是在倍增维护 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候同时维护 𝑓−1(𝑥)f−1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而不是每次都求逆．

> 当 [𝑥0]𝑔(𝑥) ≠1[x0]g(x)≠1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，可能需要使用二次剩余来计算 [𝑥0]𝑓(𝑥)[x0]f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

上述方法需要知道 𝑓0(𝑥)f0(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆，所以常数项不能为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

若 [𝑥0]𝑔(𝑥) =0[x0]g(x)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则将 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解成 𝑥𝑘ℎ(𝑥)xkh(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 [𝑥0]ℎ(𝑥) ≠0[x0]h(x)≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 若 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇数，则 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有平方根．

  * 若 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶数，则求出 ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的平方根 √ℎ(𝑥)h(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后得到 𝑓(𝑥) ≡𝑥𝑘/2√ℎ(𝑥)(mod𝑥𝑛)f(x)≡xk/2h(x)(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

洛谷模板题 [P5205【模板】多项式开根](https://www.luogu.com.cn/problem/P5205) 参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 ``` |  ```text #include <algorithm> #include <iostream> using namespace std ; constexpr int MAXN = 1 << 20 , mod = 998244353 ; int a [ MAXN ], b [ MAXN ], g [ MAXN ], gg [ MAXN ]; int qpow ( int x , int y ) { // 快速幂 int ans = 1 ; while ( y ) { if ( y & 1 ) { ans = ( long long ) 1 * ans * x % mod ; } x = ( long long ) 1 * x * x % mod ; y >>= 1 ; } return ans ; } int inv2 = qpow ( 2 , mod \- 2 ); // 逆元 void change ( int * f , int len ) { for ( int i = 1 , j = len / 2 ; i < len \- 1 ; i ++ ) { if ( i < j ) { swap ( f [ i ], f [ j ]); } int k = len / 2 ; while ( j >= k ) { j -= k ; k /= 2 ; } if ( j < k ) { j += k ; } } } void NTT ( int * f , int len , int type ) { // NTT change ( f , len ); for ( int q = 2 ; q <= len ; q <<= 1 ) { int nxt = qpow ( 3 , ( mod \- 1 ) / q ); for ( int i = 0 ; i < len ; i += q ) { int w = 1 ; for ( int k = i ; k < i \+ ( q >> 1 ); k ++ ) { int x = f [ k ]; int y = ( long long ) 1 * w * f [ k \+ ( q / 2 )] % mod ; f [ k ] = ( x \+ y ) % mod ; f [ k \+ ( q / 2 )] = ( x \- y \+ mod ) % mod ; w = ( long long ) 1 * w * nxt % mod ; } } } if ( type == -1 ) { reverse ( f \+ 1 , f \+ len ); int iv = qpow ( len , mod \- 2 ); for ( int i = 0 ; i < len ; i ++ ) { f [ i ] = ( long long ) 1 * f [ i ] * iv % mod ; } } } void inv ( int deg , int * f , int * h ) { // 求逆元 if ( deg == 1 ) { h [ 0 ] = qpow ( f [ 0 ], mod \- 2 ); return ; } inv (( deg \+ 1 ) >> 1 , f , h ); int len = 1 ; while ( len < deg * 2 ) { // 倍增 len *= 2 ; } copy ( f , f \+ deg , gg ); fill ( gg \+ deg , gg \+ len , 0 ); NTT ( gg , len , 1 ); NTT ( h , len , 1 ); for ( int i = 0 ; i < len ; i ++ ) { h [ i ] = ( long long ) 1 * ( 2 \- ( long long ) 1 * gg [ i ] * h [ i ] % mod \+ mod ) % mod * h [ i ] % mod ; } NTT ( h , len , -1 ); fill ( h \+ deg , h \+ len , 0 ); } int n , t [ MAXN ]; // deg:次数 // f:被开根数组 // h:答案数组 void sqrt ( int deg , int * f , int * h ) { if ( deg == 1 ) { h [ 0 ] = 1 ; return ; } sqrt (( deg \+ 1 ) >> 1 , f , h ); int len = 1 ; while ( len < deg * 2 ) { // 倍增 len *= 2 ; } fill ( g , g \+ len , 0 ); inv ( deg , h , g ); copy ( f , f \+ deg , t ); fill ( t \+ deg , t \+ len , 0 ); NTT ( t , len , 1 ); NTT ( g , len , 1 ); NTT ( h , len , 1 ); for ( int i = 0 ; i < len ; i ++ ) { h [ i ] = ( long long ) 1 * inv2 * (( long long ) 1 * h [ i ] % mod \+ ( long long ) 1 * g [ i ] * t [ i ] % mod ) % mod ; } NTT ( h , len , -1 ); fill ( h \+ deg , h \+ len , 0 ); } int main () { cin >> n ; for ( int i = 0 ; i < n ; i ++ ) { cin >> a [ i ]; } sqrt ( n , a , b ); for ( int i = 0 ; i < n ; i ++ ) { cout << b [ i ] << ' ' ; } return 0 ; } ```   
---|---  
  
#### Newton's Method

参见 [Newton's Method](../newton/#newtons-method).

### 例题

  1. [「Codeforces Round #250」E. The Child and Binary Tree](https://codeforces.com/contest/438/problem/E)

## 多项式除法 & 取模

给定多项式 𝑓(𝑥),𝑔(𝑥)f(x),g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 除 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的商 𝑄(𝑥)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和余数 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 解法

发现若能消除 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的影响则可直接 多项式求逆 解决．

考虑构造变换

𝑓𝑅(𝑥)=𝑥deg⁡𝑓𝑓(1𝑥)fR(x)=xdeg⁡ff(1x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

观察可知其实质为反转 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数．

设 𝑛 =deg⁡𝑓,𝑚 =deg⁡𝑔n=deg⁡f,m=deg⁡g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

将 𝑓(𝑥) =𝑄(𝑥)𝑔(𝑥) +𝑅(𝑥)f(x)=Q(x)g(x)+R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替换成 1𝑥1x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并将其两边都乘上 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得到：

𝑥𝑛𝑓(1𝑥)=𝑥𝑛−𝑚𝑄(1𝑥)𝑥𝑚𝑔(1𝑥)+𝑥𝑛−𝑚+1𝑥𝑚−1𝑅(1𝑥)𝑓𝑅(𝑥)=𝑄𝑅(𝑥)𝑔𝑅(𝑥)+𝑥𝑛−𝑚+1𝑅𝑅(𝑥)xnf(1x)=xn−mQ(1x)xmg(1x)+xn−m+1xm−1R(1x)fR(x)=QR(x)gR(x)+xn−m+1RR(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到上式中 𝑅𝑅(𝑥)RR(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数为 𝑥𝑛−𝑚+1xn−m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则将其放到模 𝑥𝑛−𝑚+1xn−m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下即可消除 𝑅𝑅(𝑥)RR(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 带来的影响．

又因 𝑄𝑅(𝑥)QR(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的次数为 (𝑛−𝑚) <(𝑛−𝑚+1)(n−m)<(n−m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故 𝑄𝑅(𝑥)QR(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不会受到影响．

则：

𝑓𝑅(𝑥)≡𝑄𝑅(𝑥)𝑔𝑅(𝑥)(mod𝑥𝑛−𝑚+1)fR(x)≡QR(x)gR(x)(modxn−m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

使用多项式求逆即可求出 𝑄(𝑥)Q(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将其反代即可得到 𝑅(𝑥)R(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**时间复杂度** 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 多项式对数函数 & 指数函数

给定多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求模 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的 ln⁡𝑓(𝑥)ln⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 exp⁡𝑓(𝑥)exp⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 解法

#### 普通方法

多项式对数函数多项式指数函数

首先，对于多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 ln⁡𝑓(𝑥)ln⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在，则由其 [定义](../intro/#复合)，其必须满足：

[𝑥0]𝑓(𝑥)=1[x0]f(x)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对 ln⁡𝑓(𝑥)ln⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求导再积分，可得：

dln⁡𝑓(𝑥)d𝑥≡𝑓′(𝑥)𝑓(𝑥)(mod𝑥𝑛)ln⁡𝑓(𝑥)≡∫dln⁡𝑓(𝑥)≡∫𝑓′(𝑥)𝑓(𝑥)d𝑥(mod𝑥𝑛)dln⁡f(x)dx≡f′(x)f(x)(modxn)ln⁡f(x)≡∫dln⁡f(x)≡∫f′(x)f(x)dx(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

多项式的求导，积分时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求逆时间复杂度为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故多项式求 lnln![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间复杂度 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

首先，对于多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 exp⁡𝑓(𝑥)exp⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存在，则其必须满足：

[𝑥0]𝑓(𝑥)=0[x0]f(x)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

否则 exp⁡𝑓(𝑥)exp⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的常数项不收敛．

对 exp⁡𝑓(𝑥)exp⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求导，可得：

dexp⁡𝑓(𝑥)d𝑥≡exp⁡𝑓(𝑥)𝑓′(𝑥)(mod𝑥𝑛)dexp⁡f(x)dx≡exp⁡f(x)f′(x)(modxn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

比较两边系数可得：

[𝑥𝑛−1]dexp⁡𝑓(𝑥)d𝑥=𝑛−1∑𝑖=0([𝑥𝑖]exp⁡𝑓(𝑥))([𝑥𝑛−𝑖−1]𝑓′(𝑥))[xn−1]dexp⁡f(x)dx=∑i=0n−1([xi]exp⁡f(x))([xn−i−1]f′(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑛[𝑥𝑛]exp⁡𝑓(𝑥)=𝑛−1∑𝑖=0([𝑥𝑖]exp⁡𝑓(𝑥))((𝑛−𝑖)[𝑥𝑛−𝑖]𝑓(𝑥))n[xn]exp⁡f(x)=∑i=0n−1([xi]exp⁡f(x))((n−i)[xn−i]f(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

使用分治 FFT 即可解决．

**时间复杂度** 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### Newton's Method

使用 [Newton's Method](../newton/#newtons-method) 即可在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内解决多项式 expexp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 代码

多项式 ln/exp

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 ``` |  ```text constexpr int MAXN = 262144 ; constexpr int mod = 998244353 ; using i64 = long long ; using poly_t = int [ MAXN ]; using poly = int * const ; void derivative ( const poly & h , const int n , poly & f ) { for ( int i = 1 ; i != n ; ++ i ) f [ i \- 1 ] = ( i64 ) h [ i ] * i % mod ; f [ n \- 1 ] = 0 ; } void integrate ( const poly & h , const int n , poly & f ) { for ( int i = n \- 1 ; i ; \-- i ) f [ i ] = ( i64 ) h [ i \- 1 ] * inv [ i ] % mod ; f [ 0 ] = 0 ; /* C */ } void polyln ( const poly & h , const int n , poly & f ) { /* f = ln h = ∫ h' / h dx */ assert ( h [ 0 ] == 1 ); static poly_t ln_t ; const int t = n << 1 ; derivative ( h , n , ln_t ); std :: fill ( ln_t \+ n , ln_t \+ t , 0 ); polyinv ( h , n , f ); DFT ( ln_t , t ); DFT ( f , t ); for ( int i = 0 ; i != t ; ++ i ) ln_t [ i ] = ( i64 ) ln_t [ i ] * f [ i ] % mod ; IDFT ( ln_t , t ); integrate ( ln_t , n , f ); } void polyexp ( const poly & h , const int n , poly & f ) { /* f = exp(h) = f_0 (1 - ln f_0 + h) */ assert ( h [ 0 ] == 0 ); static poly_t exp_t ; std :: fill ( f , f \+ n \+ n , 0 ); f [ 0 ] = 1 ; for ( int t = 2 ; t <= n ; t <<= 1 ) { const int t2 = t << 1 ; polyln ( f , t , exp_t ); exp_t [ 0 ] = sub ( pls ( h [ 0 ], 1 ), exp_t [ 0 ]); for ( int i = 1 ; i != t ; ++ i ) exp_t [ i ] = sub ( h [ i ], exp_t [ i ]); std :: fill ( exp_t \+ t , exp_t \+ t2 , 0 ); DFT ( f , t2 ); DFT ( exp_t , t2 ); for ( int i = 0 ; i != t2 ; ++ i ) f [ i ] = ( i64 ) f [ i ] * exp_t [ i ] % mod ; IDFT ( f , t2 ); std :: fill ( f \+ t , f \+ t2 , 0 ); } } ```   
---|---  
  
### 例题

  1. 计算 𝑓𝑘(𝑥)fk(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

普通做法为多项式快速幂，时间复杂度 𝑂(𝑛log⁡𝑛log⁡𝑘)O(nlog⁡nlog⁡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当 [𝑥0]𝑓(𝑥) =1[x0]f(x)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有：

𝑓𝑘(𝑥)=exp⁡(𝑘ln⁡𝑓(𝑥))fk(x)=exp⁡(kln⁡f(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当 [𝑥0]𝑓(𝑥) ≠1[x0]f(x)≠1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，设 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最低次项为 𝑓𝑖𝑥𝑖fixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则：

𝑓𝑘(𝑥)=𝑓𝑘𝑖𝑥𝑖𝑘exp⁡(𝑘ln⁡𝑓(𝑥)𝑓𝑖𝑥𝑖)fk(x)=fikxikexp⁡(kln⁡f(x)fixi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**时间复杂度** 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 多项式三角函数

给定多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求模 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的 sin⁡𝑓(𝑥),cos⁡𝑓(𝑥)sin⁡f(x),cos⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 tan⁡𝑓(𝑥)tan⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 解法

首先由 [Euler's formula](../../complex/#欧拉公式) (ei𝑥=cos⁡𝑥+isin⁡𝑥)(eix=cos⁡x+isin⁡x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以得到 [三角函数的另一个表达式](https://en.wikipedia.org/wiki/Trigonometric_functions#Relationship_to_exponential_function_and_complex_numbers)：

sin⁡𝑥=ei𝑥−e−i𝑥2icos⁡𝑥=ei𝑥+e−i𝑥2sin⁡x=eix−e−ix2icos⁡x=eix+e−ix2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么代入 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就有：

sin⁡𝑓(𝑥)=exp⁡(i𝑓(𝑥))−exp⁡(−i𝑓(𝑥))2icos⁡𝑓(𝑥)=exp⁡(i𝑓(𝑥))+exp⁡(−i𝑓(𝑥))2sin⁡f(x)=exp⁡(if(x))−exp⁡(−if(x))2icos⁡f(x)=exp⁡(if(x))+exp⁡(−if(x))2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

直接按上述表达式编写程序即可得到模 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的 sin⁡𝑓(𝑥)sin⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 cos⁡𝑓(𝑥)cos⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．再由 tan⁡𝑓(𝑥) =sin⁡𝑓(𝑥)cos⁡𝑓(𝑥)tan⁡f(x)=sin⁡f(x)cos⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可求得 tan⁡𝑓(𝑥)tan⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 代码

多项式三角函数

注意到我们是在 ℤ998244353Z998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上做 NTT，那么相应地，虚数单位 ii![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应该被换成 8658371886583718![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 911660635911660635![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

i=√−1≡√998244352(mod998244353)⟹ori≡86583718(mod998244353)ori≡911660635(mod998244353)i=−1≡998244352(mod998244353)⟹ori≡86583718(mod998244353)ori≡911660635(mod998244353)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` |  ```text constexpr int MAXN = 262144 ; constexpr int mod = 998244353 ; constexpr int imgunit = 86583718 ; /* sqrt(-1) = sqrt(998233452) */ using i64 = long long ; using poly_t = int [ MAXN ]; using poly = int * const ; void polytri ( const poly & h , const int n , poly & sin_t , poly & cos_t ) { /* sin(f) = (exp(i * f) - exp(- i * f)) / 2i */ /* cos(f) = (exp(i * f) + exp(- i * f)) / 2 */ /* tan(f) = sin(f) / cos(f) */ assert ( h [ 0 ] == 0 ); static poly_t tri1_t , tri2_t ; for ( int i = 0 ; i != n ; ++ i ) tri2_t [ i ] = ( i64 ) h [ i ] * imgunit % mod ; polyexp ( tri2_t , n , tri1_t ); polyinv ( tri1_t , n , tri2_t ); if ( sin_t != nullptr ) { const int invi = fpow ( pls ( imgunit , imgunit ), mod \- 2 ); for ( int i = 0 ; i != n ; ++ i ) sin_t [ i ] = ( i64 )( tri1_t [ i ] \- tri2_t [ i ] \+ mod ) * invi % mod ; } if ( cos_t != nullptr ) { for ( int i = 0 ; i != n ; ++ i ) cos_t [ i ] = div2 ( pls ( tri1_t [ i ], tri2_t [ i ])); } } ```   
---|---  
  
## 多项式反三角函数

给定多项式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求模 𝑥𝑛xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的 arcsin⁡𝑓(𝑥),arccos⁡𝑓(𝑥)arcsin⁡f(x),arccos⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 arctan⁡𝑓(𝑥)arctan⁡f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 解法

仿照求多项式 lnln![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方法，对反三角函数求导再积分可得：

dd𝑥arcsin⁡𝑥=1√1−𝑥2arcsin⁡𝑥=∫1√1−𝑥2d𝑥dd𝑥arccos⁡𝑥=−1√1−𝑥2arccos⁡𝑥=−∫1√1−𝑥2d𝑥dd𝑥arctan⁡𝑥=11+𝑥2arctan⁡𝑥=∫11+𝑥2d𝑥ddxarcsin⁡x=11−x2arcsin⁡x=∫11−x2dxddxarccos⁡x=−11−x2arccos⁡x=−∫11−x2dxddxarctan⁡x=11+x2arctan⁡x=∫11+x2dx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么代入 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就有：

dd𝑥arcsin⁡𝑓(𝑥)=𝑓′(𝑥)√1−𝑓2(𝑥)arcsin⁡𝑓(𝑥)=∫𝑓′(𝑥)√1−𝑓2(𝑥)d𝑥dd𝑥arccos⁡𝑓(𝑥)=−𝑓′(𝑥)√1−𝑓2(𝑥)arccos⁡𝑓(𝑥)=−∫𝑓′(𝑥)√1−𝑓2(𝑥)d𝑥dd𝑥arctan⁡𝑓(𝑥)=𝑓′(𝑥)1+𝑓2(𝑥)arctan⁡𝑓(𝑥)=∫𝑓′(𝑥)1+𝑓2(𝑥)d𝑥ddxarcsin⁡f(x)=f′(x)1−f2(x)arcsin⁡f(x)=∫f′(x)1−f2(x)dxddxarccos⁡f(x)=−f′(x)1−f2(x)arccos⁡f(x)=−∫f′(x)1−f2(x)dxddxarctan⁡f(x)=f′(x)1+f2(x)arctan⁡f(x)=∫f′(x)1+f2(x)dx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

直接按式子求就可以了．

### 代码

多项式反三角函数

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 ``` |  ```text constexpr int MAXN = 262144 ; constexpr int mod = 998244353 ; using i64 = long long ; using poly_t = int [ MAXN ]; using poly = int * const ; void derivative ( const poly & h , const int n , poly & f ) { for ( int i = 1 ; i != n ; ++ i ) f [ i \- 1 ] = ( i64 ) h [ i ] * i % mod ; f [ n \- 1 ] = 0 ; } void integrate ( const poly & h , const int n , poly & f ) { for ( int i = n \- 1 ; i ; \-- i ) f [ i ] = ( i64 ) h [ i \- 1 ] * inv [ i ] % mod ; f [ 0 ] = 0 ; /* C */ } void polyarcsin ( const poly & h , const int n , poly & f ) { /* arcsin(f) = ∫ f' / sqrt(1 - f^2) dx */ static poly_t arcsin_t ; const int t = n << 1 ; std :: copy ( h , h \+ n , arcsin_t ); std :: fill ( arcsin_t \+ n , arcsin_t \+ t , 0 ); DFT ( arcsin_t , t ); for ( int i = 0 ; i != t ; ++ i ) arcsin_t [ i ] = sqr ( arcsin_t [ i ]); IDFT ( arcsin_t , t ); arcsin_t [ 0 ] = sub ( 1 , arcsin_t [ 0 ]); for ( int i = 1 ; i != n ; ++ i ) arcsin_t [ i ] = arcsin_t [ i ] ? mod \- arcsin_t [ i ] : 0 ; polysqrt ( arcsin_t , n , f ); polyinv ( f , n , arcsin_t ); derivative ( h , n , f ); DFT ( f , t ); DFT ( arcsin_t , t ); for ( int i = 0 ; i != t ; ++ i ) arcsin_t [ i ] = ( i64 ) f [ i ] * arcsin_t [ i ] % mod ; IDFT ( arcsin_t , t ); integrate ( arcsin_t , n , f ); } void polyarccos ( const poly & h , const int n , poly & f ) { /* arccos(f) = - ∫ f' / sqrt(1 - f^2) dx */ polyarcsin ( h , n , f ); for ( int i = 0 ; i != n ; ++ i ) f [ i ] = f [ i ] ? mod \- f [ i ] : 0 ; } void polyarctan ( const poly & h , const int n , poly & f ) { /* arctan(f) = ∫ f' / (1 + f^2) dx */ static poly_t arctan_t ; const int t = n << 1 ; std :: copy ( h , h \+ n , arctan_t ); std :: fill ( arctan_t \+ n , arctan_t \+ t , 0 ); DFT ( arctan_t , t ); for ( int i = 0 ; i != t ; ++ i ) arctan_t [ i ] = sqr ( arctan_t [ i ]); IDFT ( arctan_t , t ); inc ( arctan_t [ 0 ], 1 ); std :: fill ( arctan_t \+ n , arctan_t \+ t , 0 ); polyinv ( arctan_t , n , f ); derivative ( h , n , arctan_t ); DFT ( f , t ); DFT ( arctan_t , t ); for ( int i = 0 ; i != t ; ++ i ) arctan_t [ i ] = ( i64 ) f [ i ] * arctan_t [ i ] % mod ; IDFT ( arctan_t , t ); integrate ( arctan_t , n , f ); } ```   
---|---  
  
## 参考资料与链接

* * *

  1. [Elementary function——Wikipedia](https://en.wikipedia.org/wiki/Elementary_function) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/elementary-func.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/elementary-func.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Marcythm](https://github.com/Marcythm), [97littleleaf11](https://github.com/97littleleaf11), [shuzhouliu](https://github.com/shuzhouliu), [abc1763613206](https://github.com/abc1763613206), [CCXXXI](https://github.com/CCXXXI), [EndlessCheng](https://github.com/EndlessCheng), [Enter-tainer](https://github.com/Enter-tainer), [fps5283](https://github.com/fps5283), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [hly1204](https://github.com/hly1204), [hsfzLZH1](https://github.com/hsfzLZH1), [huayucaiji](https://github.com/huayucaiji), [Ir1d](https://github.com/Ir1d), [kenlig](https://github.com/kenlig), [ouuan](https://github.com/ouuan), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [test12345-pupil](https://github.com/test12345-pupil), [untitledunrevised](https://github.com/untitledunrevised), [c-forrest](https://github.com/c-forrest), [ksyx](https://github.com/ksyx), [shawlleyw](https://github.com/shawlleyw), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [TrisolarisHD](https://github.com/TrisolarisHD), [xiaoyezi2007](https://github.com/xiaoyezi2007), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
