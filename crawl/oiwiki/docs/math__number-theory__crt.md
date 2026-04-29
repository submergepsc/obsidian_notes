# 中国剩余定理 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/crt/

# 中国剩余定理

## 引入

> 「物不知数」问题：有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二．问物几何？

即求满足以下条件的整数：除以 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 余 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，除以 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 余 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，除以 77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 余 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

该问题最早见于《孙子算经》中，并有该问题的具体解法．宋朝数学家秦九韶于 1247 年《数书九章》卷一、二《大衍类》对「物不知数」问题做出了完整系统的解答．上面具体问题的解答口诀由明朝数学家程大位在《算法统宗》中给出：

> 三人同行七十希，五树梅花廿一支，七子团圆正半月，除百零五便得知．

2 ×70 +3 ×21 +2 ×15 =233 =2 ×105 +232×70+3×21+2×15=233=2×105+23![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故答案为 2323![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 定义

中国剩余定理 (Chinese Remainder Theorem, CRT) 可求解如下形式的一元线性同余方程组（其中 𝑛1,𝑛2,⋯,𝑛𝑘n1,n2,⋯,nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两两互质）：

⎧{ { {⎨{ { {⎩𝑥≡𝑎1(mod𝑛1)𝑥≡𝑎2(mod𝑛2)⋮𝑥≡𝑎𝑘(mod𝑛𝑘){x≡a1(modn1)x≡a2(modn2)⋮x≡ak(modnk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上面的「物不知数」问题就是一元线性同余方程组的一个实例．

## 过程

  1. 计算所有模数的积 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 对于第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个方程：
     1. 计算 𝑚𝑖 =𝑛𝑛𝑖mi=nni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
     2. 计算 𝑚𝑖mi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑛𝑖ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的 [逆元](../inverse/) 𝑚−1𝑖mi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
     3. 计算 𝑐𝑖 =𝑚𝑖𝑚−1𝑖ci=mimi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（**不要对 𝑛𝑖ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模**）．
  3. 方程组在模 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的唯一解为：𝑥 =∑𝑘𝑖=1𝑎𝑖𝑐𝑖(mod𝑛)x=∑i=1kaici(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text LL CRT ( int k , LL * a , LL * r ) { LL n = 1 , ans = 0 ; for ( int i = 1 ; i <= k ; i ++ ) n = n * r [ i ]; for ( int i = 1 ; i <= k ; i ++ ) { LL m = n / r [ i ], b , y ; exgcd ( m , r [ i ], b , y ); // b * m mod r[i] = 1 ans = ( ans \+ a [ i ] * m * b % n ) % n ; } return ( ans % n \+ n ) % n ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text def CRT ( k , a , r ): n = 1 ans = 0 for i in range ( 1 , k \+ 1 ): n = n * r [ i ] for i in range ( 1 , k \+ 1 ): m = n // r [ i ] b = y = 0 exgcd ( m , r [ i ], b , y ) # b * m mod r[i] = 1 ans = ( ans \+ a [ i ] * m * b % n ) % n return ( ans % n \+ n ) % n ```   
---|---  
  
## 证明

我们需要证明上面算法计算所得的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于任意 𝑖 =1,2,⋯,𝑘i=1,2,⋯,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑥 ≡𝑎𝑖(mod𝑛𝑖)x≡ai(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当 𝑖 ≠𝑗i≠j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，有 𝑚𝑗 ≡0(mod𝑛𝑖)mj≡0(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故 𝑐𝑗 ≡𝑚𝑗 ≡0(mod𝑛𝑖)cj≡mj≡0(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．又有 𝑐𝑖 ≡𝑚𝑖 ⋅(𝑚−1𝑖mod𝑛𝑖) ≡1(mod𝑛𝑖)ci≡mi⋅(mi−1modni)≡1(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以我们有：

𝑥≡𝑘∑𝑗=1𝑎𝑗𝑐𝑗(mod𝑛𝑖)≡𝑎𝑖𝑐𝑖(mod𝑛𝑖)≡𝑎𝑖⋅𝑚𝑖⋅(𝑚−1𝑖mod𝑛𝑖)(mod𝑛𝑖)≡𝑎𝑖(mod𝑛𝑖)x≡∑j=1kajcj(modni)≡aici(modni)≡ai⋅mi⋅(mi−1modni)(modni)≡ai(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即对于任意 𝑖 =1,2,⋯,𝑘i=1,2,⋯,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，上面算法得到的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是满足 𝑥 ≡𝑎𝑖(mod𝑛𝑖)x≡ai(modni)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即证明了解同余方程组的算法的正确性．

因为我们没有对输入的 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作特殊限制，所以任何一组输入 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都对应一个解 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．另外，若 𝑥 ≠𝑦x≠y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则总存在 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑛𝑖ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下不同余．故系数列表 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与解 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间是一一映射关系，方程组总是有唯一解．

## 解释

下面演示 CRT 如何解「物不知数」问题．

  1. 𝑛 =3 ×5 ×7 =105n=3×5×7=105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 三人同行 **七十** 希：𝑛1 =3,𝑚1 =𝑛/𝑛1 =35,𝑚−11 ≡2(mod3)n1=3,m1=n/n1=35,m1−1≡2(mod3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故 𝑐1 =35 ×2 =70c1=35×2=70![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  3. 五树梅花 **廿一** 支：𝑛2 =5,𝑚2 =𝑛/𝑛2 =21,𝑚−12 ≡1(mod5)n2=5,m2=n/n2=21,m2−1≡1(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故 𝑐2 =21 ×1 =21c2=21×1=21![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  4. 七子团圆正 **半月** ：𝑛3 =7,𝑚3 =𝑛/𝑛3 =15,𝑚−13 ≡1(mod7)n3=7,m3=n/n3=15,m3−1≡1(mod7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故 𝑐3 =15 ×1 =15c3=15×1=15![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  5. 所以方程组的唯一解为 𝑥 ≡2 ×70 +3 ×21 +2 ×15 ≡233 ≡23(mod105)x≡2×70+3×21+2×15≡233≡23(mod105)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（除 **百零五** 便得知）

## Garner 算法

CRT 的另一个用途是用一组比较小的质数表示一个大的整数．

例如，若 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足如下线性方程组，且 𝑎 <∏𝑘𝑖=1𝑝𝑖a<∏i=1kpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（其中 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为质数）：

⎧{ { {⎨{ { {⎩𝑎≡𝑎1(mod𝑝1)𝑎≡𝑎2(mod𝑝2)⋮𝑎≡𝑎𝑘(mod𝑝𝑘){a≡a1(modp1)a≡a2(modp2)⋮a≡ak(modpk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们可以用以下形式的式子（称作 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的混合基数表示）表示 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑎=𝑥1+𝑥2𝑝1+𝑥3𝑝1𝑝2+…+𝑥𝑘𝑝1…𝑝𝑘−1a=x1+x2p1+x3p1p2+…+xkp1…pk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**Garner 算法** 将用来计算系数 𝑥1,…,𝑥𝑘x1,…,xk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

令 𝑟𝑖𝑗rij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑝𝑗pj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的 [逆](../inverse/)：

𝑝𝑖⋅𝑟𝑖,𝑗≡1(mod𝑝𝑗)pi⋅ri,j≡1(modpj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

把 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代入我们得到的第一个方程：

𝑎1≡𝑥1(mod𝑝1)a1≡x1(modp1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代入第二个方程得出：

𝑎2≡𝑥1+𝑥2𝑝1(mod𝑝2)a2≡x1+x2p1(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

方程两边减 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，除 𝑝1p1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后得

𝑎2−𝑥1≡𝑥2𝑝1(mod𝑝2)(𝑎2−𝑥1)𝑟1,2≡𝑥2(mod𝑝2)𝑥2≡(𝑎2−𝑥1)𝑟1,2(mod𝑝2)a2−x1≡x2p1(modp2)(a2−x1)r1,2≡x2(modp2)x2≡(a2−x1)r1,2(modp2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

类似地，我们可以得到：

𝑥𝑘=(…((𝑎𝑘−𝑥1)𝑟1,𝑘−𝑥2)𝑟2,𝑘)−…)𝑟𝑘−1,𝑘mod𝑝𝑘xk=(…((ak−x1)r1,k−x2)r2,k)−…)rk−1,kmodpk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)实现

C++Python

```text 1 2 3 4 5 6 7 8 ``` |  ```text for ( int i = 0 ; i < k ; ++ i ) { x [ i ] = a [ i ]; for ( int j = 0 ; j < i ; ++ j ) { x [ i ] = r [ j ][ i ] * ( x [ i ] \- x [ j ]); x [ i ] = x [ i ] % p [ i ]; if ( x [ i ] < 0 ) x [ i ] += p [ i ]; } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text for i in range ( 0 , k ): x [ i ] = a [ i ] for j in range ( 0 , i ): x [ i ] = r [ j ][ i ] * ( x [ i ] \- x [ j ]) x [ i ] = x [ i ] % p [ i ] if x [ i ] < 0 : x [ i ] = x [ i ] \+ p [ i ] ```   
---|---  
  
该算法的时间复杂度为 𝑂(𝑘2)O(k2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．实际上 Garner 算法并不要求模数为质数，只要求模数两两互质，我们有如下伪代码：

𝐂𝐡𝐢𝐧𝐞𝐬𝐞 𝐑𝐞𝐦𝐚𝐢𝐧𝐝𝐞𝐫 𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 cra⁡(𝐯,𝐦):𝐈𝐧𝐩𝐮𝐭: 𝐦=(𝑚0,𝑚1,…,𝑚𝑛−1), 𝑚𝑖∈ℤ+∧gcd(𝑚𝑖,𝑚𝑗)=1 for all 𝑖≠𝑗,𝐯=(𝑣0,…,𝑣𝑛−1) where 𝑣𝑖=𝑥mod𝑚𝑖.𝐎𝐮𝐭𝐩𝐮𝐭: 𝑥mod∏𝑛−1𝑖=0𝑚𝑖.1𝐟𝐨𝐫 𝑖 from 1 to (𝑛−1) 𝐝𝐨2𝐶𝑖←(∏𝑖−1𝑗=0𝑚𝑗)−1mod𝑚𝑖3𝑥←𝑣04𝐟𝐨𝐫 𝑖 from 1 to (𝑛−1) 𝐝𝐨5𝑢←(𝑣𝑖−𝑥)⋅𝐶𝑖mod𝑚𝑖6𝑥←𝑥+𝑢∏𝑖−1𝑗=0𝑚𝑗7𝐫𝐞𝐭𝐮𝐫𝐧 (𝑥)Chinese Remainder Algorithm cra⁡(v,m):Input: m=(m0,m1,…,mn−1), mi∈Z+∧gcd(mi,mj)=1 for all i≠j,v=(v0,…,vn−1) where vi=xmodmi.Output: xmod∏i=0n−1mi.1for i from 1 to (n−1) do2Ci←(∏j=0i−1mj)−1modmi3x←v04for i from 1 to (n−1) do5u←(vi−x)⋅Cimodmi6x←x+u∏j=0i−1mj7return (x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以发现在第六行中的计算过程对应上述混合基数的表示．

## 应用

某些计数问题或数论问题出于加长代码、增加难度、或者是一些其他原因，给出的模数：**不是质数** ！

但是对其质因数分解会发现它没有平方因子，也就是该模数是由一些不重复的质数相乘得到．

那么我们可以分别对这些模数进行计算，最后用 CRT 合并答案．

下面这道题就是一个不错的例子．

[洛谷 P2480 [SDOI2010] 古代猪文](https://www.luogu.com.cn/problem/P2480)

给出 𝐺,𝑛G,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（1 ≤𝐺,𝑛 ≤1091≤G,n≤109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），求：

𝐺∑𝑘∣𝑛(𝑛𝑘)mod999 911 659G∑k∣n(nk)mod999 911 659![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

首先，当 𝐺 =999 911 659G=999 911 659![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，所求显然为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

否则，根据 [欧拉定理](../fermat/)，可知所求为：

𝐺∑𝑘∣𝑛(𝑛𝑘)mod999 911 658mod999 911 659G∑k∣n(nk)mod999 911 658mod999 911 659![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

现在考虑如何计算：

∑𝑘∣𝑛(𝑛𝑘)mod999 911 658∑k∣n(nk)mod999 911 658![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 999 911 658999 911 658![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是质数，无法保证 ∀𝑥 ∈[1,999 911 657]∀x∈[1,999 911 657]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有逆元存在，上面这个式子我们无法直接计算．

注意到 999 911 658 =2 ×3 ×4679 ×35617999 911 658=2×3×4679×35617![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中每个质因子的最高次数均为一，我们可以考虑分别求出 ∑𝑘∣𝑛(𝑛𝑘)∑k∣n(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，46794679![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，3561735617![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这几个质数下的结果，最后用中国剩余定理来合并答案．

也就是说，我们实际上要求下面一个线性方程组的解：

⎧{ { {⎨{ { {⎩𝑥≡𝑎1(mod2)𝑥≡𝑎2(mod3)𝑥≡𝑎3(mod4679)𝑥≡𝑎4(mod35617){x≡a1(mod2)x≡a2(mod3)x≡a3(mod4679)x≡a4(mod35617)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而计算一个组合数对较小的质数取模后的结果，可以利用 [卢卡斯定理](../lucas/)．

## 扩展：模数不互质的情况

### 两个方程

设两个方程分别是 𝑥 ≡𝑎1(mod𝑚1)x≡a1(modm1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝑥 ≡𝑎2(mod𝑚2)x≡a2(modm2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

将它们转化为不定方程：𝑥 =𝑚1𝑝 +𝑎1 =𝑚2𝑞 +𝑎2x=m1p+a1=m2q+a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝,𝑞p,q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是整数，则有 𝑚1𝑝 −𝑚2𝑞 =𝑎2 −𝑎1m1p−m2q=a2−a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由 [裴蜀定理](../bezouts/)，当 𝑎2 −𝑎1a2−a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不能被 gcd(𝑚1,𝑚2)gcd(m1,m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除时，无解；

其他情况下，可以通过 [扩展欧几里得算法](../gcd/) 解出来一组可行解 (𝑝,𝑞)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

则原来的两方程组成的模方程组的解为 𝑥 ≡𝑏(mod𝑀)x≡b(modM)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑏 =𝑚1𝑝 +𝑎1b=m1p+a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑀 =lcm(𝑚1,𝑚2)M=lcm(m1,m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 多个方程

用上面的方法两两合并即可．

## 习题

  * [【模板】中国剩余定理（CRT）/曹冲养猪](https://www.luogu.com.cn/problem/P1495)
  * [【模板】扩展中国剩余定理](https://www.luogu.com.cn/problem/P4777)
  * [「NOI2018」屠龙勇士](https://uoj.ac/problem/396)
  * [「TJOI2009」猜数字](https://www.luogu.com.cn/problem/P3868)

**本页面部分内容译自博文[Китайская теорема об остатках](http://e-maxx.ru/algo/chinese_theorem) 与其英文翻译版 [Chinese Remainder Theorem](https://cp-algorithms.com/algebra/chinese-remainder-theorem.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/crt.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/crt.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [Enter-tainer](https://github.com/Enter-tainer), [H-J-Granger](https://github.com/H-J-Granger), [sshwy](https://github.com/sshwy), [Chrogeek](https://github.com/Chrogeek), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [Xeonacid](https://github.com/Xeonacid), [Early0v0](https://github.com/Early0v0), [Great-designer](https://github.com/Great-designer), [MegaOwIer](https://github.com/MegaOwIer), [Tiphereth-A](https://github.com/Tiphereth-A), [383494](https://github.com/383494), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Henry-ZHR](https://github.com/Henry-ZHR), [iamtwz](https://github.com/iamtwz), [Konano](https://github.com/Konano), [kzoacn](https://github.com/kzoacn), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [stevebraveman](https://github.com/stevebraveman), [Suyun514](mailto:suyun514@qq.com), [Unnamed2964](https://github.com/Unnamed2964), [weiyong1024](https://github.com/weiyong1024), [ChungZH](https://github.com/ChungZH), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [HeRaNO](https://github.com/HeRaNO), [hly1204](https://github.com/hly1204), [ImpleLee](https://github.com/ImpleLee), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [little-cindy](https://github.com/little-cindy), [lychees](https://github.com/lychees), [Menci](https://github.com/Menci), [namasikanam](https://github.com/namasikanam), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [Phemon](mailto:i@phemon.me), [renbaoshuo](https://github.com/renbaoshuo), [shawlleyw](https://github.com/shawlleyw), [SukkaW](https://github.com/SukkaW), [xyf007](https://github.com/xyf007)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
