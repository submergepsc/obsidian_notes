# 欧拉函数 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/euler-totient/

# 欧拉函数

## 定义

欧拉函数（Euler's totient function），即 𝜑(𝑛)φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示的是小于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质的数的个数．

比如说 𝜑(1) =1φ(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是质数的时候，显然有 𝜑(𝑛) =𝑛 −1φ(n)=n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 性质

  * 欧拉函数是 [积性函数](../basic/#积性函数)．

即对任意满足 gcd(𝑎,𝑏) =1gcd(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜑(𝑎𝑏) =𝜑(𝑎)𝜑(𝑏)φ(ab)=φ(a)φ(b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

特别地，当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇数时 𝜑(2𝑛) =𝜑(𝑛)φ(2n)=φ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明参见 [剩余系的复合](../basic/#剩余系的复合)．

  * 𝑛 =∑𝑑∣𝑛𝜑(𝑑)n=∑d∣nφ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

利用 [莫比乌斯反演](../mobius/) 相关知识可以得出．

也可以这样考虑：如果 gcd(𝑘,𝑛) =𝑑gcd(k,n)=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 gcd(𝑘𝑑,𝑛𝑑) =1,(𝑘 <𝑛)gcd(kd,nd)=1,(k<n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如果我们设 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 gcd(𝑘,𝑛) =𝑥gcd(k,n)=x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数的个数，那么 𝑛 =∑𝑛𝑖=1𝑓(𝑖)n=∑i=1nf(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

根据上面的证明，我们发现，𝑓(𝑥) =𝜑(𝑛𝑥)f(x)=φ(nx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而 𝑛 =∑𝑑∣𝑛𝜑(𝑛𝑑)n=∑d∣nφ(nd)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意到约数 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛𝑑nd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 具有对称性，所以上式化为 𝑛 =∑𝑑∣𝑛𝜑(𝑑)n=∑d∣nφ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 若 𝑛 =𝑝𝑘n=pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是质数，那么 𝜑(𝑛) =𝑝𝑘 −𝑝𝑘−1φ(n)=pk−pk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． （根据定义可知）

  * 由唯一分解定理，设 𝑛 =∏𝑠𝑖=1𝑝𝑘𝑖𝑖n=∏i=1spiki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是质数，有 𝜑(𝑛) =𝑛 ×∏𝑠𝑖=1𝑝𝑖−1𝑝𝑖φ(n)=n×∏i=1spi−1pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明
    * 引理：设 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为任意质数，那么 𝜑(𝑝𝑘) =𝑝𝑘−1 ×(𝑝 −1)φ(pk)=pk−1×(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明：显然对于从 1 到 𝑝𝑘pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有数中，除了 𝑝𝑘−1pk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数以外其它数都与 𝑝𝑘pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素，故 𝜑(𝑝𝑘) =𝑝𝑘 −𝑝𝑘−1 =𝑝𝑘−1 ×(𝑝 −1)φ(pk)=pk−pk−1=pk−1×(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，证毕．

接下来我们证明 𝜑(𝑛) =𝑛 ×∏𝑠𝑖=1𝑝𝑖−1𝑝𝑖φ(n)=n×∏i=1spi−1pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由唯一分解定理与 𝜑(𝑥)φ(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 函数的积性

𝜑(𝑛)=𝑠∏𝑖=1𝜑(𝑝𝑘𝑖𝑖)=𝑠∏𝑖=1(𝑝𝑖−1)×𝑝𝑖𝑘𝑖−1=𝑠∏𝑖=1𝑝𝑖𝑘𝑖×(1−1𝑝𝑖)=𝑛 𝑠∏𝑖=1(1−1𝑝𝑖)◻φ(n)=∏i=1sφ(piki)=∏i=1s(pi−1)×piki−1=∏i=1spiki×(1−1pi)=n ∏i=1s(1−1pi)◻![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 对任意不全为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑚,𝑛m,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝜑(𝑚𝑛)𝜑(gcd(𝑚,𝑛)) =𝜑(𝑚)𝜑(𝑛)gcd(𝑚,𝑛)φ(mn)φ(gcd(m,n))=φ(m)φ(n)gcd(m,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

可由上一条直接计算得出．

## 实现

如果只要求一个数的欧拉函数值，那么直接根据定义质因数分解的同时求就好了．这个过程可以用 [Pollard Rho](../pollard-rho/) 算法优化．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text #include <cmath> int euler_phi ( int n ) { int ans = n ; for ( int i = 2 ; i * i <= n ; i ++ ) if ( n % i == 0 ) { ans = ans / i * ( i \- 1 ); while ( n % i == 0 ) n /= i ; } if ( n > 1 ) ans = ans / n * ( n \- 1 ); return ans ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text import math def euler_phi ( n ): ans = n for i in range ( 2 , math . isqrt ( n ) \+ 1 ): if n % i == 0 : ans = ans // i * ( i \- 1 ) while n % i == 0 : n = n // i if n > 1 : ans = ans // n * ( n \- 1 ) return ans ```   
---|---  
  
如果是多个数的欧拉函数值，可以利用后面会提到的线性筛法来求得．

详见：[筛法求欧拉函数](../sieve/#筛法求欧拉函数)

## 应用

欧拉函数常常用于化简一列最大公约数的和．国内有些文章称它为 **欧拉反演**1．

在结论

𝑛=∑𝑑|𝑛𝜑(𝑑)n=∑d|nφ(d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

中代入 𝑛 =gcd(𝑎,𝑏)n=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有

gcd(𝑎,𝑏)=∑𝑑|gcd(𝑎,𝑏)𝜑(𝑑)=∑𝑑[𝑑|𝑎][𝑑|𝑏]𝜑(𝑑),gcd(a,b)=∑d|gcd(a,b)φ(d)=∑d[d|a][d|b]φ(d),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 [ ⋅][⋅]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 Iverson 括号．对上式求和，就可以得到

𝑛∑𝑖=1gcd(𝑖,𝑛)=∑𝑑𝑛∑𝑖=1[𝑑|𝑖][𝑑|𝑛]𝜑(𝑑)=∑𝑑⌊𝑛𝑑⌋[𝑑|𝑛]𝜑(𝑑)=∑𝑑|𝑛⌊𝑛𝑑⌋𝜑(𝑑).∑i=1ngcd(i,n)=∑d∑i=1n[d|i][d|n]φ(d)=∑d⌊nd⌋[d|n]φ(d)=∑d|n⌊nd⌋φ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里关键的观察是 ∑𝑛𝑖=1[𝑑|𝑖] =⌊𝑛𝑑⌋∑i=1n[d|i]=⌊nd⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即在 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间能够被 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数是 ⌊𝑛𝑑⌋⌊nd⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

利用这个式子，就可以遍历约数求和了．需要多组查询的时候，可以预处理欧拉函数的前缀和，利用数论分块查询．

[GCD SUM](https://www.luogu.com.cn/problem/P2398)

给定 𝑛 ≤100000n≤100000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求

𝑛∑𝑖=1𝑛∑𝑗=1gcd(𝑖,𝑗).∑i=1n∑j=1ngcd(i,j).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 思路

仿照上文的推导，可以得出

𝑛∑𝑖=1𝑛∑𝑗=1gcd(𝑖,𝑗)=𝑛∑𝑑=1⌊𝑛𝑑⌋2𝜑(𝑑).∑i=1n∑j=1ngcd(i,j)=∑d=1n⌊nd⌋2φ(d).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

此时需要从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求欧拉函数，用线性筛做就可以 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到答案．

## 欧拉定理

与欧拉函数紧密相关的一个定理就是欧拉定理．其描述如下：

若 gcd(𝑎,𝑚) =1gcd(a,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑎𝜑(𝑚) ≡1(mod𝑚)aφ(m)≡1(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 扩展欧拉定理

当然也有扩展欧拉定理，用于处理一般的 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形．

𝑎𝑏≡⎧{ {⎨{ {⎩𝑎𝑏mod𝜑(𝑚),gcd(𝑎,𝑚)=1𝑎𝑏,gcd(𝑎,𝑚)≠1,𝑏<𝜑(𝑚)𝑎𝑏mod𝜑(𝑚)+𝜑(𝑚),gcd(𝑎,𝑚)≠1,𝑏≥𝜑(𝑚)(mod𝑚)ab≡{abmodφ(m),gcd(a,m)=1ab,gcd(a,m)≠1,b<φ(m)abmodφ(m)+φ(m),gcd(a,m)≠1,b≥φ(m)(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明和习题详见 [欧拉定理](../fermat/)．

## 习题

  * [SPOJ ETF. Euler Totient Function](http://www.spoj.com/problems/ETF/)
  * [UVa 10179. Irreducible Basic Fractions](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1120)
  * [UVa 10299. Relatives](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1240)
  * [UVa 11327. Enumerating Rational Numbers](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2302)
  * [TIMUS 1673. Admission to Exam](http://acm.timus.ru/problem.aspx?space=1&num=1673)
  * [Luogu P1390 公约数的和](https://www.luogu.com.cn/problem/P1390)
  * [Luogu P2155 [SDOI2008] 沙拉公主的困惑](https://www.luogu.com.cn/problem/P2155)
  * [Luogu P2568 GCD](https://www.luogu.com.cn/problem/P2568)

## 参考资料与注释

* * *

  1. 这一说法并未见于学术期刊或国外的论坛中，在使用该说法时应当注意． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/euler-totient.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/euler-totient.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [guodong2005](https://github.com/guodong2005), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [iamtwz](https://github.com/iamtwz), [MegaOwIer](https://github.com/MegaOwIer), [StudyingFather](https://github.com/StudyingFather), [Chrogeek](https://github.com/Chrogeek), [mgt](mailto:i@margatroid.xyz), [shuzhouliu](https://github.com/shuzhouliu), [aofall](https://github.com/aofall), [CCXXXI](https://github.com/CCXXXI), [CoelacanthusHex](https://github.com/CoelacanthusHex), [frank-xjh](https://github.com/frank-xjh), [Great-designer](https://github.com/Great-designer), [greyqz](https://github.com/greyqz), [henrytbtrue](https://github.com/henrytbtrue), [kZime](https://github.com/kZime), [lihaoyu1234](https://github.com/lihaoyu1234), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [nalemy](https://github.com/nalemy), [orzAtalod](https://github.com/orzAtalod), [ouuan](https://github.com/ouuan), [Persdre](https://github.com/Persdre), [segment-tree](https://github.com/segment-tree), [ShaoChenHeng](https://github.com/ShaoChenHeng), [Struggler-q](https://github.com/Struggler-q), [yuhuoji](https://github.com/yuhuoji), [ksyx](https://github.com/ksyx), [Pinghigh](https://github.com/Pinghigh), [shawlleyw](https://github.com/shawlleyw), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [TrisolarisHD](https://github.com/TrisolarisHD)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
