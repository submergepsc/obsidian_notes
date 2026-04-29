# 快速数论变换 - OI Wiki

- Source: https://oi-wiki.org/math/poly/ntt/

# 快速数论变换

## 简介

**数论变换** （number-theoretic transform, NTT）是离散傅里叶变换（DFT）在数论基础上的实现；**快速数论变换** （fast number-theoretic transform, FNTT）是 [快速傅里叶变换](../fft/)（FFT）在数论基础上的实现．

**数论变换** 是一种计算卷积（convolution）的快速算法．最常用算法就包括了前文提到的快速傅里叶变换．然而快速傅立叶变换具有一些实现上的缺点，举例来说，资料向量必须乘上复数系数的矩阵加以处理，而且每个复数系数的实部和虚部是一个正弦及余弦函数，因此大部分的系数都是浮点数，也就是说，必须做复数而且是浮点数的运算，因此计算量会比较大，而且浮点数运算产生的误差会比较大．

NTT 解决的是多项式乘法带模数的情况，可以说有些受模数的限制，数也比较大．目前最常见的模数是 998244353．

## 前置知识

学习数论变换需要前置知识：离散傅里叶变换、生成子群、[原根](../../number-theory/primitive-root/)、离散对数．相关知识可以在对应页面中学习，此处不再赘述．

## 定义

### 数论变换

在数学中，NTT 是关于任意 [环](../../algebra/basic/#环) 上的离散傅立叶变换（DFT）．在有限域的情况下，通常称为数论变换（NTT）．

**数论变换** （NTT）是通过将离散傅立叶变换化为 𝐹 =ℤ/𝑝F=Z/p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，整数模质数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这是一个 **有限域** ，只要 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可除 𝑝 −1p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就存在本原 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次方根，所以我们有 𝑝 =𝜉𝑛 +1p=ξn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于 正整数 𝜉ξ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．具体来说，对于质数 𝑝 =𝑞𝑛 +1,(𝑛 =2𝑚)p=qn+1,(n=2m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，原根 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑔𝑞𝑛 ≡1(mod𝑝)gqn≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 将 𝑔𝑛 =𝑔𝑞(mod𝑝)gn=gq(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 看做 𝜔𝑛ωn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的等价，则其满足相似的性质，比如 𝑔𝑛𝑛 ≡1(mod𝑝),𝑔𝑛/2𝑛 ≡ −1(mod𝑝)gnn≡1(modp),gnn/2≡−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因为这里涉及到数论变化，所以 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（为了区分 FFT 中的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们把这里的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）可以比 FFT 中的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大，但是只要把 𝑞𝑁𝑛qNn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 看做这里的 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就行了，能够避免大小问题．

常见的有：

𝑝=167772161=5×225+1,𝑔=3p=167772161=5×225+1,g=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑝=469762049=7×226+1,𝑔=3p=469762049=7×226+1,g=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑝=754974721=32×5×224+1,𝑔=11p=754974721=32×5×224+1,g=11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑝=998244353=7×17×223+1,𝑔=3p=998244353=7×17×223+1,g=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑝=1004535809=479×221+1,𝑔=3p=1004535809=479×221+1,g=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

就是 𝑔𝑞𝑛gqn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的等价 e2𝜋i𝑛e2πin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

迭代到长度 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时 𝑔𝑙 =𝑔𝑝−1𝑙gl=gp−1l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或者 𝜔𝑛 =𝑔𝑙 =𝑔𝑁𝑙𝑁 =𝑔𝑝−1𝑙𝑁ωn=gl=gNNl=gNp−1l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 快速数论变换

**快速数论变换** （FNTT）是数论变换（NTT）增加分治操作之后的快速算法．

快速数论变换使用的分治办法，与快速傅里叶变换使用的分治办法完全一致．这意味着，只需在快速傅里叶变换的代码基础上进行简单修改，即可得到快速数论变换的代码．

在算法竞赛中常提到的 NTT 一词，往往实际指的是快速数论变换，一般默认「数论变换」是指「快速数论变换」．

这样简写的逻辑与快速傅里叶变换相似．事实上，「快速傅里叶变换」（FFT）一词指的是「快速离散傅里叶变换」（FDFT），但由于「快速」只能作用于离散，甚至是本原单位根阶数为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂的特殊情形，不能作用于连续，因此「离散」一词被省略掉，FDFT 变为 FFT，即 FFT 永远指的是特殊的离散情形．

数论变换或快速数论变换是在取模意义下进行的操作，不存在连续的情形，永远是离散的，自然也无需提到离散一词．

在算法领域，不进行提速的操作是无意义的．在快速傅里叶变换中介绍 DFT 一词，是因为 DFT 在信号处理、图像处理领域也有其他的具体应用，同时 DFT 也是 FFT 的原理或前置知识．

在不引起混淆的情形下，常用 NTT 来代指 FNTT．为了不引起下文进一步介绍的混淆，下文的 NTT 与 FNTT 两个词进行了分离．

DFT、FFT、NTT、FNTT 的具体关系是：

  * 在 DFT 与 NTT 的基础上，增加分治操作，得到 FFT 与 FNTT．分治操作的办法与原理，可以参见快速傅里叶变换一文．

  * 在 DFT 与 FFT 的基础上，将复数加法与复数乘法替换为模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的加法和乘法，一般大小限制在 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑝 −1p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间；将本原单位根改为模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的相同阶数的本原单位根，阶数为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂，即可得到 NTT 与 FNTT．

由于替换的运算只涉及加法和乘法，因此 DFT、FFT、NTT、FNTT 拥有相同的原理，均在满足加法与乘法的环上进行，无需域上满足除法运算的更加严格的条件．

事实上，只要拥有原根，即群论中的生成元，该模数下的 NTT 或 FNTT 即可进行．考虑到模数为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形太小，不具有实际意义，对于奇素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正整数 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只要给出模数为 𝑝𝛼pα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 2𝑝𝛼2pα![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的原根 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，采用同样的办法，则 NTT 或 FNTT 仍然可以进行．

## 模板

[Library Checker - Convolution](https://judge.yosupo.jp/problem/convolution_mod)

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 ``` |  ```text #include <algorithm> #include <cstdio> using namespace std ; constexpr int N = 1 << 20 , P = 998244353 ; int qpow ( int x , int y ) { int res = 1 ; while ( y ) { if ( y & 1 ) res = 1l l * res * x % P ; x = 1l l * x * x % P ; y >>= 1 ; } return res ; } int r [ N ]; void ntt ( int * x , int lim , int opt ) { for ( int i = 0 ; i < lim ; ++ i ) if ( r [ i ] < i ) swap ( x [ i ], x [ r [ i ]]); for ( int m = 2 ; m <= lim ; m <<= 1 ) { int k = m >> 1 ; int gn = qpow ( 3 , ( P \- 1 ) / m ); for ( int i = 0 ; i < lim ; i += m ) { int g = 1 ; for ( int j = 0 ; j < k ; ++ j , g = 1l l * g * gn % P ) { int tmp = 1l l * x [ i \+ j \+ k ] * g % P ; x [ i \+ j \+ k ] = ( x [ i \+ j ] \- tmp \+ P ) % P ; x [ i \+ j ] = ( x [ i \+ j ] \+ tmp ) % P ; } } } if ( opt == -1 ) { reverse ( x \+ 1 , x \+ lim ); int inv = qpow ( lim , P \- 2 ); for ( int i = 0 ; i < lim ; ++ i ) x [ i ] = 1l l * x [ i ] * inv % P ; } } int A [ N ], B [ N ], C [ N ]; int main () { int n , m ; scanf ( "%d %d" , & n , & m ); for ( int i = 0 ; i < n ; i ++ ) scanf ( "%d" , & A [ i ]); for ( int i = 0 ; i < m ; i ++ ) scanf ( "%d" , & B [ i ]); int N = max ( n , m ), lim = 1 ; while ( lim < ( N << 1 )) lim <<= 1 ; for ( int i = 0 ; i < lim ; ++ i ) r [ i ] = ( i & 1 ) * ( lim >> 1 ) \+ ( r [ i >> 1 ] >> 1 ); ntt ( A , lim , 1 ); ntt ( B , lim , 1 ); for ( int i = 0 ; i < lim ; ++ i ) C [ i ] = 1l l * A [ i ] * B [ i ] % P ; ntt ( C , lim , -1 ); for ( int i = 0 ; i < n \+ m \- 1 ; i ++ ) printf ( "%d%c" , C [ i ], " \n " [ i == n \+ m \- 2 ]); return 0 ; } ```   
---|---  
  
## 参考资料与拓展阅读

  1. [FWT（快速沃尔什变换）零基础详解 qaq（ACM/OI）](https://zhuanlan.zhihu.com/p/41867199)
  2. [FFT（快速傅里叶变换）0 基础详解！附 NTT（ACM/OI）](https://zhuanlan.zhihu.com/p/40505277)
  3. [Number-theoretic transform(NTT) - Wikipedia](https://en.wikipedia.org/wiki/Discrete_Fourier_transform_%28general%29#Number-theoretic_transform)
  4. [Tutorial on FFT/NTT—The tough made simple. (Part 1)](https://codeforces.com/blog/entry/43499)
  5. [NTT 模板 - BlackJack_ CSDN 博客](https://blog.csdn.net/blackjack_/article/details/79346433)

* * *

>  __本页面最近更新： 2026/3/15 04:24:59，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/ntt.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/ntt.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [Xeonacid](https://github.com/Xeonacid), [ChungZH](https://github.com/ChungZH), [isdanni](https://github.com/isdanni), [ouuan](https://github.com/ouuan), [shuzhouliu](https://github.com/shuzhouliu), [XuYueming520](https://github.com/XuYueming520), [Yukimaikoriya](https://github.com/Yukimaikoriya), [383494](https://github.com/383494), [billchenchina](https://github.com/billchenchina), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [GeZiyue](https://github.com/GeZiyue), [Great-designer](https://github.com/Great-designer), [henryrabbit](https://github.com/henryrabbit), [HeRaNO](https://github.com/HeRaNO), [killcerr](https://github.com/killcerr), [ksyx](https://github.com/ksyx), [O-Omega](https://github.com/O-Omega), [ranwen](https://github.com/ranwen), [Saisyc](https://github.com/Saisyc), [sshwy](https://github.com/sshwy), [tigerruanyifan](https://github.com/tigerruanyifan), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [weiwch](https://github.com/weiwch), [YifanRuan](https://github.com/YifanRuan)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
