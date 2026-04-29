# 代数基本定理 - OI Wiki

- Source: https://oi-wiki.org/math/poly/fundamental/

# 代数基本定理

## 定义

任何复系数一元 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次多项式（𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至少为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）方程在复数域上至少有一根．

由此推出，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次复系数多项式方程在复数域内有且只有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个根，重根按重数计算．

有时这个定理也表述为：

任何一个非零的一元 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次复系数多项式，都正好有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个复数根．

代数基本定理的证明，一般会用到复变函数或者近世代数，因此往往作为一个熟知结论直接应用．

根据代数基本定理，一个复系数多项式 𝑓(𝑥) =𝑎𝑛𝑥𝑛 +𝑎𝑛−1𝑥𝑛−1 +… +𝑎0f(x)=anxn+an−1xn−1+…+a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定可以唯一地分解为：

𝑓(𝑥)=𝑎𝑛(𝑥−𝑥1)𝑘1(𝑥−𝑥2)𝑘2…(𝑥−𝑥𝑡)𝑘𝑡f(x)=an(x−x1)k1(x−x2)k2…(x−xt)kt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中各个根均为复数，𝑘1 +𝑘2 +… +𝑘𝑡 =𝑛k1+k2+…+kt=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 虚根成对定理

代数基本定理的研究对象是复系数多项式．当对实系数多项式进行研究时，虽然也能分解出复数根，却需要将研究范围扩大，不太方便．

虚根：非实数根．

定理：实系数多项式的根的共轭复数也是该多项式的根．

证明：直接在代数基本定理的等式两端取共轭即证毕．

如果根本身是实数，则取共轭仍为它本身，不受影响．

如果根是虚根，则虚根的共轭复数也是原多项式的根．那么，两个虚根就可以配对．

定理：实数系数方程的共轭虚根一定成对出现，并且共轭虚根的重数相等．

证明：假设一个根为 𝑎 +𝑏ia+bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则另一个根为 𝑎 −𝑏ia−bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这意味着在分解式中存在两项：

(𝑥−𝑎−𝑏i)(𝑥−𝑎+𝑏i)=𝑥2−2𝑎𝑥+𝑎2+𝑏2(x−a−bi)(x−a+bi)=x2−2ax+a2+b2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以看到两项乘在一起，各项系数会全部变为实数．这个等式右端的二次实系数多项式整除原始的多项式．

于是，在代数基本定理的等式中，两遍同时除以这个二次三项式，得到的仍旧是实系数多项式的等式．对新等式重复操作，随着次数的下降，若干次后即不存在虚根．

因此，每对共轭虚根的重数相等．证毕．

以下是虚根成对定理的推论：

  * 实系数奇次多项式至少有一个实根，并且总共有奇数个实根．
  * 实系数偶次多项式可能没有实根，总共有偶数个实根．

称上述二次三项式 𝑥2 −2𝑎𝑥 +𝑎2 +𝑏2 =𝑥2 +𝑝𝑥 +𝑞x2−2ax+a2+b2=x2+px+q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为二次实系数不可约因式．不可约是指它在实数范围内不可约．

定理：实系数多项式一定是一次或者二次实系数不可约因式的积．

证明：

只要实系数多项式有一个实根 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有一个实系数因式 𝑥 −𝑐x−c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和它对应；有一对虚根 𝑎 ±𝑏ia±bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有一个实系数因式 𝑥2 −2𝑎𝑥 +𝑎2 +𝑏2x2−2ax+a2+b2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和它对应．

因此，只要在原始的代数基本定理分解式中，利用虚根成对定理进行配对，即证毕．

根据虚根成对定理，一个实系数多项式 𝑓(𝑥) =𝑎𝑛𝑥𝑛 +𝑎𝑛−1𝑥𝑛−1 +… +𝑎0f(x)=anxn+an−1xn−1+…+a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定可以唯一地分解为：

𝑓(𝑥)=𝑎𝑛(𝑥−𝑥1)𝑘1(𝑥−𝑥2)𝑘2…(𝑥−𝑥𝑡)𝑘𝑡(𝑥2+𝑝1𝑥+𝑞1)𝑙1(𝑥2+𝑝2𝑥+𝑞2)𝑙2…(𝑥2+𝑝𝑠𝑥+𝑞𝑠)𝑙𝑠f(x)=an(x−x1)k1(x−x2)k2…(x−xt)kt(x2+p1x+q1)l1(x2+p2x+q2)l2…(x2+psx+qs)ls![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中各项系数均为实数，𝑘1 +𝑘2 +… +𝑘𝑡 +2(𝑙1 +𝑙2 +… +𝑙𝑠) =𝑛k1+k2+…+kt+2(l1+l2+…+ls)=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 林士谔算法

### 简介

怎样对实系数多项式进行代数基本定理的分解？如果将数域扩充至复数会很复杂．

如果只在实数范围内进行分解，只能保证，当次数大于 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候，一定存在实系数二次三项式因式．

这是因为，如果该多项式有虚根，直接凑出一对共轭虚根即可．如果该多项式只有实根，任取两个实根对应的一次因式乘在一起，也能得到实系数二次三项式因式．

找到二次三项式因式之后，再从二次式中解实根或复根就极为容易．于是便有逐次 **找出一个二次因子** 来求得方程的复根的计算方法，这种方法避免了复数运算．

在 1940 年 8 月、1943 年 8 月和 1947 年 7 月，林士谔先后在 MIT 出版的《数学物理》杂志上接连正式发表了 3 篇关于解算高阶方程式复根方法的论文1，每次均有改进．

这个方法今天还在现代计算机中进行快速运算，计算机程序包（如 MATLAB）中的多项式求根程序依据的原理也是这个算法．

### 过程

要想找到一个二次三项式因子，就要将多项式分解为：

𝑓(𝑥)=(𝑥2+𝑝1𝑥+𝑞1)𝑔(𝑥)f(x)=(x2+p1x+q1)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于无法一下子找到二次三项式因子，按照迭代求解的思路，对于初始值有：

𝑓(𝑥)=(𝑥2+𝑝𝑥+𝑞)𝑔(𝑥)+𝑟𝑥+𝑠f(x)=(x2+px+q)g(x)+rx+s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

会产生一个一次式作为余项．只要余项足够小，即可近似地找到待求因子．

我们希望最终解是初始值加一个偏移修正：

𝑝1=𝑝+𝑑𝑝p1=p+dp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑞1=𝑞+𝑑𝑞q1=q+dq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

余式中的两个数 (𝑟,𝑠)(r,s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 由除式的给定系数 (𝑝,𝑞)(p,q)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 决定．有偏导数关系：

𝑑𝑟=𝜕𝑟𝜕𝑝𝑑𝑝+𝜕𝑟𝜕𝑞𝑑𝑞dr=∂r∂pdp+∂r∂qdq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑑𝑠=𝜕𝑠𝜕𝑝𝑑𝑝+𝜕𝑠𝜕𝑞𝑑𝑞ds=∂s∂pdp+∂s∂qdq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在初始的等式中，被除式 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是给定的，商式 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和余式 𝑟𝑥 +𝑠rx+s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 随着除式 𝑥2 +𝑝𝑥 +𝑞x2+px+q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的变化而变化．因此有偏导数关系

0=𝑥𝑔(𝑥)+𝜕𝑔(𝑥)𝜕𝑝(𝑥2+𝑝𝑥+𝑞)+𝜕𝑟𝜕𝑝𝑥+𝜕𝑠𝜕𝑝0=xg(x)+∂g(x)∂p(x2+px+q)+∂r∂px+∂s∂p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)0=𝑔(𝑥)+𝜕𝑔(𝑥)𝜕𝑞(𝑥2+𝑝𝑥+𝑞)+𝜕𝑟𝜕𝑞𝑥+𝜕𝑠𝜕𝑞0=g(x)+∂g(x)∂q(x2+px+q)+∂r∂qx+∂s∂q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到，偏导数只是一个数值，与变元 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无关．因此有整除关系

𝑥𝑔(𝑥)=−𝜕𝑔(𝑥)𝜕𝑝(𝑥2+𝑝𝑥+𝑞)−𝜕𝑟𝜕𝑝𝑥−𝜕𝑠𝜕𝑝xg(x)=−∂g(x)∂p(x2+px+q)−∂r∂px−∂s∂p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑔(𝑥)=−𝜕𝑔(𝑥)𝜕𝑞(𝑥2+𝑝𝑥+𝑞)−𝜕𝑟𝜕𝑞𝑥−𝜕𝑠𝜕𝑞g(x)=−∂g(x)∂q(x2+px+q)−∂r∂qx−∂s∂q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里的结论是，待求的偏导数，恰好是对商式继续做除法的余式．多项式对给定二次三项式的除法，直接计算即可．这里就求得了四个偏导数．

我们希望 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加上偏移 𝑑𝑠ds![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑑𝑟dr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑑𝑠ds![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑑𝑟dr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的相反数．因此要解方程：

−𝜕𝑟𝜕𝑝𝑑𝑝−𝜕𝑟𝜕𝑞𝑑𝑞=𝑟−∂r∂pdp−∂r∂qdq=r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)−𝜕𝑠𝜕𝑝𝑑𝑝−𝜕𝑠𝜕𝑞𝑑𝑞=𝑠−∂s∂pdp−∂s∂qdq=s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从上述方程组中解得 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相应的偏移 𝑑𝑝dp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑑𝑞dq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直接用二阶行列式求解即可．

### 实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 ``` |  ```text // a 是原始的多项式，n 是多项式次数，p 是待求的一次项，q 是待求的常数项 void Shie ( double a [], int n , double * p , double * q ) { // 数组 b 是多项式 a 除以当前迭代二次三项式的商 memset ( b , 0 , sizeof ( b )); // 数组 c 是多项式 b 乘以 x 平方再除以当前迭代二次三项式的商 memset ( c , 0 , sizeof ( c )); * p = 0 ; * q = 0 ; double dp = 1 ; double dq = 1 ; while ( dp > eps || dp < \- eps || dq > eps || dq < \- eps ) // eps 自行设定 { double p0 = p ; double q0 = q ; b [ n \- 2 ] = a [ n ]; c [ n \- 2 ] = b [ n \- 2 ]; b [ n \- 3 ] = a [ n \- 1 ] \- p0 * b [ n \- 2 ]; c [ n \- 3 ] = b [ n \- 3 ] \- p0 * b [ n \- 2 ]; int j ; for ( j = n \- 4 ; j >= 0 ; j \-- ) { b [ j ] = a [ j \+ 2 ] \- p0 * b [ j \+ 1 ] \- q0 * b [ j \+ 2 ]; c [ j ] = b [ j ] \- p0 * c [ j \+ 1 ] \- q0 * c [ j \+ 2 ]; } double r = a [ 1 ] \- p0 * b [ 0 ] \- q0 * b [ 1 ]; double s = a [ 0 ] \- q0 * b [ 0 ]; double rp = c [ 1 ]; double sp = b [ 0 ] \- q0 * c [ 2 ]; double rq = c [ 0 ]; double sq = \- q0 * c [ 1 ]; dp = ( rp * s \- r * sp ) / ( rp * sq \- rq * sp ); dq = ( r * sq \- rq * s ) / ( rp * sq \- rq * sp ); * p += dp ; * q += dq ; } } ```   
---|---  
  
## 参考资料与注释

* * *

  1. [林士谔．论劈因法解高阶特征方程根值的应用问题．数学进展，1963(03):207-217.](https://cnki.net/kcms/detail/detail.aspx?filename=SXJZ196303000&dbcode=CJFD&dbname=CJFD1979) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/fundamental.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/fundamental.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Jijidawang](https://github.com/Jijidawang)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
