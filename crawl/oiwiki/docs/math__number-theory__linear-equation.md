# 线性同余方程 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/linear-equation/

# 线性同余方程

本文讨论线性同余方程的求解．

## 基本概念

设 𝑎,𝑏,𝑛a,b,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为整数，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为未知数，那么，形如

𝑎𝑥≡𝑏(mod𝑛)ax≡b(modn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的方程称为 **线性同余方程** （linear congruence equation）．

求解线性同余方程，需要找到区间 [0,𝑛 −1][0,n−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全部解．当然，将它们加减 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的任意倍数，依然是方程的解．在模 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的意义下，这些就是该方程的全部解．

本文接下来介绍了两种求解线性同余方程的思路，分别利用了逆元和不定方程．对于一般的情形，逆元和不定方程的求解都需要用到 [扩展欧几里得算法](../gcd/#扩展欧几里得算法)，因此，这两种思路其实是一致的．

## 用逆元求解

首先，考虑 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素的情形，即 gcd(𝑎,𝑛) =1gcd(a,n)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．此时，可以计算 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [逆元](../inverse/) 𝑎−1a−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将方程两边同乘以 𝑎−1a−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这就得到方程的唯一解：

𝑥≡𝑏𝑎−1(mod𝑛).x≡ba−1(modn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

紧接着，考虑 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不互素的情形，即 gcd(𝑎,𝑛) =𝑑 >1gcd(a,n)=d>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．此时，原方程不一定有解．例如，2𝑥 ≡1(mod4)2x≡1(mod4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就没有解．因此，需要考虑两种情形：

  * 当 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不能整除 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，方程无解．对于任意的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，方程左侧 𝑎𝑥ax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数，但是方程右侧 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数．因此，它们不可能相差 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数，因为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数也一定是 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数．因此，方程无解．

  * 当 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以整除 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，可以将方程的参数 𝑎,𝑏,𝑛a,b,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都同除以 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得到一个新的方程：

𝑎′𝑥≡𝑏′(mod𝑛′).a′x≡b′(modn′).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，gcd(𝑎′,𝑛′) =1gcd(a′,n′)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，𝑎′a′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛′n′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素．这种情形已经在前文解决，所以，可以通过求解逆元得到方程的一个解 𝑥′x′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

显然，𝑥′x′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是原方程的一个解．但这并非原方程唯一的解．由于转化后的方程的全体解为

{𝑥′+𝑘𝑛′:𝑘∈𝐙}.{x′+kn′:k∈Z}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这些解中落在区间 [0,𝑛 −1][0,n−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的那些，就是原方程在区间 [0,𝑛 −1][0,n−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的全部解：

𝑥≡(𝑥′+𝑘𝑛′)(mod𝑛),𝑘=0,1,⋯,𝑑−1.x≡(x′+kn′)(modn),k=0,1,⋯,d−1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

总结这两种情形，线性同余方程的 **解的数量** 等于 𝑑 =gcd(𝑎,𝑛)d=gcd(a,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 用不定方程求解

线性同余方程等价于关于 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [二元一次不定方程](../bezouts/#两个变量的情形)：

𝑎𝑥+𝑛𝑦=𝑏.ax+ny=b.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用所引页面的讨论，方程有解当且仅当 gcd(𝑎,𝑛) ∣𝑏gcd(a,n)∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而且该方程的一组通解是

𝑥=𝑥0+𝑡𝑛𝑑,𝑦=𝑦0−𝑡𝑎𝑑,x=x0+tnd,y=y0−tad,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑑 =gcd(𝑎,𝑛)d=gcd(a,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是它们的最大公约数，𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是任意整数．

进而，线性同余方程的通解就是

𝑥≡(𝑥0+𝑡𝑛𝑑)(mod𝑛),𝑡∈𝐙.x≡(x0+tnd)(modn),t∈Z.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将 𝑥0x0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对 𝑛/𝑑n/d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模就得到同余方程的最小（非负）整数解，也就是上文的 𝑥′x′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

## 参考实现

本节提供的参考实现可以得到同余方程的最小非负整数解．如果解不存在，则输出 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text // Extended Euclidean Algorithm. // Finds integers x, y such that a*x + b*y = gcd(a, b), // and returns gcd(a, b). int ex_gcd ( int a , int b , int & x , int & y ) { if ( ! b ) { x = 1 ; y = 0 ; return a ; } else { int d = ex_gcd ( b , a % b , y , x ); y -= a / b * x ; return d ; } } // Solves the linear congruence equation: // a * x ≡ b (mod n), where n > 0\. // Returns the smallest non-negative solution x, // or -1 if there is no solution. int solve_linear_congruence_equation ( int a , int b , int n ) { int x , y ; int d = ex_gcd ( a , n , x , y ); if ( b % d ) return -1 ; n /= d ; return (( long long ) x * ( b / d ) % n \+ n ) % n ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text def ex_gcd ( a , b ): """ Extended Euclidean Algorithm. Finds integers x, y such that a*x + b*y = gcd(a, b), and returns (gcd, x, y). """ if b == 0 : return a , 1 , 0 d , x1 , y1 = ex_gcd ( b , a % b ) x = y1 y = x1 \- ( a // b ) * y1 return d , x , y def solve_linear_congruence_equation ( a , b , n ): """ Solves the linear congruence equation: a * x ≡ b (mod n), where n > 0\. Returns the smallest non-negative solution x, or -1 if there is no solution. """ d , x , y = ex_gcd ( a , n ) if b % d != 0 : return \- 1 n //= d return ( x * ( b // d ) % n \+ n ) % n ```   
---|---  
  
## 习题

  * [「NOIP2012」同余方程](https://loj.ac/problem/2605)

**本页面主要译自博文[Модульное линейное уравнение первого порядка](http://e-maxx.ru/algo/diofant_1_equation) 与其英文翻译版 [Linear Congruence Equation](https://cp-algorithms.com/algebra/linear_congruence_equation.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．内容有改动．**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/linear-equation.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/linear-equation.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [MegaOwIer](https://github.com/MegaOwIer), [Xeonacid](https://github.com/Xeonacid), [Great-designer](https://github.com/Great-designer), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [kZime](https://github.com/kZime), [ouuan](https://github.com/ouuan), [stevebraveman](https://github.com/stevebraveman), [aofall](https://github.com/aofall), [c-forrest](https://github.com/c-forrest), [CoelacanthusHex](https://github.com/CoelacanthusHex), [leoleoasd](https://github.com/leoleoasd), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [Persdre](https://github.com/Persdre), [Phemon](mailto:i@phemon.me), [shawlleyw](https://github.com/shawlleyw), [shuzhouliu](https://github.com/shuzhouliu), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [tsentau](https://github.com/tsentau)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
