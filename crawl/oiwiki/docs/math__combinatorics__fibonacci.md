# 斐波那契数列 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/fibonacci/

# 斐波那契数列

斐波那契数列（The Fibonacci sequence，[OEIS A000045](http://oeis.org/A000045)）的定义如下：

𝐹0=0,𝐹1=1,𝐹𝑛=𝐹𝑛−1+𝐹𝑛−2F0=0,F1=1,Fn=Fn−1+Fn−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

该数列的前几项如下：

0,1,1,2,3,5,8,13,21,34,55,89,…0,1,1,2,3,5,8,13,21,34,55,89,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 卢卡斯数列

卢卡斯数列（The Lucas sequence，[OEIS A000032](http://oeis.org/A000032)）的定义如下：

𝐿0=2,𝐿1=1,𝐿𝑛=𝐿𝑛−1+𝐿𝑛−2L0=2,L1=1,Ln=Ln−1+Ln−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

该数列的前几项如下：

2,1,3,4,7,11,18,29,47,76,123,199,…2,1,3,4,7,11,18,29,47,76,123,199,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

研究斐波那契数列，很多时候需要借助卢卡斯数列为工具．

## 斐波那契数列通项公式

第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个斐波那契数可以在 Θ(𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内使用递推公式计算．但我们仍有更快速的方法计算．

### 解析解

解析解即公式解．我们有斐波那契数列的通项公式（Binet's Formula）：

𝐹𝑛=(1+√52)𝑛−(1−√52)𝑛√5Fn=(1+52)n−(1−52)n5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个公式可以很容易地用归纳法证明，当然也可以通过生成函数的概念推导，或者解一个方程得到．

当然你可能发现，这个公式分子的第二项总是小于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且它以指数级的速度减小．因此我们可以把这个公式写成

𝐹𝑛=⎡⎢ ⎢ ⎢⎣(1+√52)𝑛√5⎤⎥ ⎥ ⎥⎦Fn=[(1+52)n5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里的中括号表示取离它最近的整数．

这两个公式在计算的时候要求极高的精确度，因此在实践中很少用到．但是请不要忽视！结合模意义下二次剩余和逆元的概念，在 OI 中使用这个公式仍是有用的．

### 卢卡斯数列通项公式

我们有卢卡斯数列的通项公式：

𝐿𝑛=(1+√52)𝑛+(1−√52)𝑛Ln=(1+52)n+(1−52)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

与斐波那契数列非常相似．事实上有：

𝐿𝑛+𝐹𝑛√52=(1+√52)𝑛Ln+Fn52=(1+52)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，𝐿𝑛Ln![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐹𝑛Fn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 恰好构成 (1+√52)𝑛(1+52)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 二项式展开再合并同类项后的分子系数．也就是说，Pell 方程

𝑥2−5𝑦2=−4x2−5y2=−4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的全体解，恰好是

𝑥𝑛+𝑦𝑛√52=𝐿𝑛+𝐹𝑛√52xn+yn52=Ln+Fn52![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

恰好是卢卡斯数列和斐波那契数列．因此有

𝐿𝑛2−5𝐹𝑛2=−4Ln2−5Fn2=−4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 矩阵形式

斐波那契数列的递推可以用矩阵乘法的形式表达：

[𝐹𝑛−1𝐹𝑛]=[𝐹𝑛−2𝐹𝑛−1][0111][Fn−1Fn]=[Fn−2Fn−1][0111]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 𝑃 =[0111]P=[0111]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们得到

[𝐹𝑛𝐹𝑛+1]=[𝐹0𝐹1]𝑃𝑛[FnFn+1]=[F0F1]Pn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是我们可以用矩阵乘法在 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内计算斐波那契数列．此外，前一节讲述的公式也可通过矩阵对角化的技巧来得到．

### 快速倍增法

使用上面的方法我们可以得到以下等式：

𝐹2𝑘=𝐹𝑘(2𝐹𝑘+1−𝐹𝑘)𝐹2𝑘+1=𝐹2𝑘+1+𝐹2𝑘F2k=Fk(2Fk+1−Fk)F2k+1=Fk+12+Fk2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是可以通过这样的方法快速计算两个相邻的斐波那契数（常数比矩乘小）．代码如下，返回值是一个二元组 (𝐹𝑛,𝐹𝑛+1)(Fn,Fn+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text pair < int , int > fib ( int n ) { if ( n == 0 ) return { 0 , 1 }; auto p = fib ( n >> 1 ); int c = p . first * ( 2 * p . second \- p . first ); int d = p . first * p . first \+ p . second * p . second ; if ( n & 1 ) return { d , c \+ d }; else return { c , d }; } ```   
---|---  
  
## 性质

斐波那契数列拥有许多有趣的性质，这里列举出一部分简单的性质：

  1. 卡西尼性质（Cassini's identity）：𝐹𝑛−1𝐹𝑛+1 −𝐹2𝑛 =( −1)𝑛Fn−1Fn+1−Fn2=(−1)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 附加性质：𝐹𝑛+𝑘 =𝐹𝑘𝐹𝑛+1 +𝐹𝑘−1𝐹𝑛Fn+k=FkFn+1+Fk−1Fn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 取上一条性质中 𝑘 =𝑛k=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们得到 𝐹2𝑛 =𝐹𝑛(𝐹𝑛+1 +𝐹𝑛−1)F2n=Fn(Fn+1+Fn−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  4. 由上一条性质可以归纳证明，∀𝑘 ∈ℕ,𝐹𝑛|𝐹𝑛𝑘∀k∈N,Fn|Fnk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  5. 上述性质可逆，即 ∀𝐹𝑎|𝐹𝑏,𝑎|𝑏∀Fa|Fb,a|b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  6. GCD 性质：(𝐹𝑚,𝐹𝑛) =𝐹(𝑚,𝑛)(Fm,Fn)=F(m,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  7. 以斐波那契数列相邻两项作为输入会使欧几里德算法达到最坏复杂度（具体参见 [维基 - 拉梅](https://en.wikipedia.org/wiki/Gabriel_Lam%C3%A9)）．

### 斐波那契数列与卢卡斯数列的关系

不难发现，关于卢卡斯数列与斐波那契数列的等式，与三角函数公式具有很高的相似性．比如：

𝐿𝑛+𝐹𝑛√52=(1+√52)𝑛Ln+Fn52=(1+52)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

与

cos⁡𝑛𝑥+𝑖sin⁡𝑛𝑥=(cos⁡𝑥+𝑖sin⁡𝑥)𝑛cos⁡nx+isin⁡nx=(cos⁡x+isin⁡x)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

很像．以及

𝐿𝑛2−5𝐹𝑛2=−4Ln2−5Fn2=−4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

与

cos2⁡𝑥+sin2⁡𝑥=1cos2⁡x+sin2⁡x=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

很像．因此，卢卡斯数列与余弦函数很像，而斐波那契数列与正弦函数很像．比如，根据

(1+√52)𝑚(1+√52)𝑛=(1+√52)𝑚+𝑛(1+52)m(1+52)n=(1+52)m+n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以得到两下标之和的等式：

2𝐿𝑚+𝑛=5𝐹𝑚𝐹𝑛+𝐿𝑚𝐿𝑛2Lm+n=5FmFn+LmLn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)2𝐹𝑚+𝑛=𝐹𝑚𝐿𝑛+𝐿𝑚𝐹𝑛2Fm+n=FmLn+LmFn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是推论就有二倍下标的等式：

𝐿2𝑛=𝐿𝑛2−2(−1)𝑛L2n=Ln2−2(−1)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝐹2𝑛=𝐹𝑛𝐿𝑛F2n=FnLn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这也是一种快速倍增下标的办法．同样地，也可以仿照三角函数的公式，比如奇偶性、和差化积、积化和差、半角、万能代换等等，推理出更多有关卢卡斯数列与斐波那契数列的相应等式．

## 斐波那契编码

我们可以利用斐波那契数列为正整数编码．根据 [齐肯多夫定理](https://zh.wikipedia.org/wiki/%E9%BD%8A%E8%82%AF%E5%A4%9A%E5%A4%AB%E5%AE%9A%E7%90%86)，任何自然数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以被唯一地表示成一些斐波那契数的和：

𝑁=𝐹𝑘1+𝐹𝑘2+…+𝐹𝑘𝑟N=Fk1+Fk2+…+Fkr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

并且 𝑘1 ≥𝑘2 +2, 𝑘2 ≥𝑘3 +2, …, 𝑘𝑟 ≥2k1≥k2+2, k2≥k3+2, …, kr≥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即不能使用两个相邻的斐波那契数）

于是我们可以用 𝑑0𝑑1𝑑2…𝑑𝑠1d0d1d2…ds1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的编码表示一个正整数，其中 𝑑𝑖 =1di=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则表示 𝐹𝑖+2Fi+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被使用．编码末位我们强制给它加一个 1（这样会出现两个相邻的 1），表示这一串编码结束．举几个例子：

1=1=𝐹2=(11)𝐹2=2=𝐹3=(011)𝐹6=5+1=𝐹5+𝐹2=(10011)𝐹8=8=𝐹6=(000011)𝐹9=8+1=𝐹6+𝐹2=(100011)𝐹19=13+5+1=𝐹7+𝐹5+𝐹2=(1001011)𝐹1=1=F2=(11)F2=2=F3=(011)F6=5+1=F5+F2=(10011)F8=8=F6=(000011)F9=8+1=F6+F2=(100011)F19=13+5+1=F7+F5+F2=(1001011)F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

给 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 编码的过程可以使用贪心算法解决：

  1. 从大到小枚举斐波那契数 𝐹𝑖Fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直到 𝐹𝑖 ≤𝑛Fi≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 把 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 减掉 𝐹𝑖Fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在编码的 𝑖 −2i−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置上放一个 1（编码从左到右以 0 为起点）．
  3. 如果 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为正，回到步骤 1．
  4. 最后在编码末位添加一个 1，表示编码的结束位置．

解码过程同理，先删掉末位的 1，对于编码为 1 的位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（编码从左到右以 0 为起点），累加一个 𝐹𝑖+2Fi+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到答案．最后的答案就是原数字．

## 模意义下周期性

对于模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下的斐波那契数列，可以容易地使用抽屉原理证明，该数列是有周期性的．由于斐波那契数每一项的计算都依赖于前两项的取值，所以需要用相邻斐波那契数组成的数对描述数列当且所处的状态．考虑模意义下前 𝑚2 +1m2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个斐波那契数对：

(𝐹0, 𝐹1), (𝐹1, 𝐹2), …, (𝐹𝑚2, 𝐹𝑚2+1)(F0, F1), (F1, F2), …, (Fm2, Fm2+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的剩余系大小为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这意味着至多只可能有 𝑚2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种互不相同的数对．因此，在前 𝑚2 +1m2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数对中必有两个相同的数对，于是从这两个数对可以往后生成相同的斐波那契数列．那么，斐波那契数列就是周期性的，且（最小正）周期不会超过 𝑚2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### Pisano 周期

模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 意义下斐波那契数列的最小正周期被称为 **Pisano 周期** （Pisano period，皮萨诺周期，[OEIS A001175](http://oeis.org/A001175)）．本文中用 𝜋(𝑚)π(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Pisano 周期．

这一观察可以用于计算第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项斐波那契数模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．如果 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非常大，就需要计算斐波那契数模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的周期．当然，只需要计算周期，不一定是最小正周期．

为此，有如下结论：

  1. 对于互素的模数 𝑚1,𝑚2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜋(𝑚1𝑚2) =lcm⁡(𝜋(𝑚1),𝜋(𝑚2))π(m1m2)=lcm⁡(π(m1),π(m2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 对于素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正整数 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜋(𝑝𝑒) ∣𝑝𝑒−1𝜋(𝑝)π(pe)∣pe−1π(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 对于 𝑚 =2𝑒 (𝑒 ∈𝐍+)m=2e (e∈N+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜋(𝑚) =3 ⋅2𝑒−1π(m)=3⋅2e−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  4. 对于 𝑚 =5𝑒 (𝑒 ∈𝐍+)m=5e (e∈N+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜋(𝑚) =4 ⋅5𝑒π(m)=4⋅5e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  5. 最后，对于素数 𝑝 ≡ ±1(mod10)p≡±1(mod10)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜋(𝑝) ∣(𝑝 −1)π(p)∣(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；对于素数 𝑝 ≡ ±3(mod10)p≡±3(mod10)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝜋(𝑝) ∣2(𝑝 +1)π(p)∣2(p+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

综合这些情形，可以说明：模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Pisano 周期不会超过 6𝑚6m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，等号当且仅当 𝑚 =2 ×5𝑒 (𝑒 ∈𝐍+)m=2×5e (e∈N+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时取得．

利用上述结论，可以基于素因数分解算法，得到如下快速计算 Pisano 周期的方法：

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text // Get a period of Fibonacci sequence mod m. // Not necessarily be the exact Pisano period. uint32_t calc_cycle_from_mod ( uint32_t m ) { uint32_t res = 1 ; for ( auto pe : factorize ( m )) { auto p = pe . first ; auto e = pe . second ; uint64_t cur = pow ( p , e \- 1 ); if ( p == 2 ) { cur *= 3 ; } else if ( p == 5 ) { cur *= 20 ; } else if ( p % 5 == 1 || p % 5 == 4 ) { cur *= p \- 1 ; } else { cur *= 2 * ( p \+ 1 ); } res = lcm ( res , cur ); } return res ; } ```   
---|---  
  
这样得到的周期可能只是 Pisano 周期的一个倍数．要得到精确的 Pisano 周期，可以进一步考察该周期的因数；或者，可以直接通过 [BSGS 算法](../../number-theory/discrete-logarithm/#大步小步算法) 以 𝑂(√𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度计算．

### 证明

最后，本文简要证明上述关于 Pisano 周期的结论．值得说明的是，利用下文说明的方法，类似的结论可以推广到一般的二阶常系数线性齐次递推数列．尽管具体的常数有所差异，这些数列模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Pisano 周期都是 𝑂(𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

第一个观察是：利用 [中国剩余定理](../../number-theory/crt/)，可以将讨论限制在素数幂模的情形．设 𝑚1,𝑚2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是两个互素的模数．斐波那契数列在模 𝑚1m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的周期是 𝜋(𝑚1)π(m1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 及其倍数，在模 𝑚2m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的周期是 𝜋(𝑚2)π(m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 及其倍数，所以它在模 𝑚1𝑚2m1m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的最小正周期则恰为 𝜋(𝑚1)π(m1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜋(𝑚2)π(m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小公倍数．这就是前文的结论 1．

另一个观察是：模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下的 Pisano 周期，其实是最小的正整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得

𝐴𝑘=(1110)𝑘≡𝐼(mod𝑚).Ak=(1110)k≡I(modm).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，它其实是矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 下1的 [阶](../../algebra/group-theory/#阶)．

对于素数幂模 𝑚 =𝑝𝑒m=pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，可以通过经典的升幂论证联系到相应的素数模的情形．设 𝑘 =𝜋(𝑝𝑒)k=π(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就存在二阶方阵 ΛΛ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得

𝐴𝑘=𝑝𝑒Λ+𝐼Ak=peΛ+I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

成立．故而，由 [二项式定理](../combination/#二项式定理) 可知

𝐴𝑘𝑝=(𝑝𝑒Λ+𝐼)𝑝=𝐼+𝑝∑𝑖=1(𝑝𝑖)(𝑝𝑒Λ)𝑖≡𝐼(mod𝑝𝑒+1).Akp=(peΛ+I)p=I+∑i=1p(pi)(peΛ)i≡I(modpe+1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，由 [阶的性质](../../number-theory/primitive-root/#幂的循环结构)，有 𝜋(𝑝𝑒+1) ∣𝑘𝑝 =𝑝𝜋(𝑝𝑒)π(pe+1)∣kp=pπ(pe)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 归纳可知，𝜋(𝑝𝑒) ∣𝑝𝑒−1𝜋(𝑝)π(pe)∣pe−1π(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是成立．

对于素数模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情形，本文讨论两种证明方式．

利用通项公式利用扩域

一种是利用斐波那契数列的通项公式：

𝐹𝑛=1√5(1+√52)𝑛−1√5(1−√52)𝑛.Fn=15(1+52)n−15(1−52)n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将它用二项式定理展开，并消去根式项：

𝐹𝑛=12𝑛−1⌊(𝑛−1)/2⌋∑𝑖=0(𝑛2𝑖+1)5𝑖.Fn=12n−1∑i=0⌊(n−1)/2⌋(n2i+1)5i.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于 𝑝 =2p=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这一表达式无法直接取模，但可以验证对应的 Pisano 周期为 𝜋(2) =3π(2)=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于 𝑝 =5p=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝐹𝑛 ≡𝑛 ⋅3𝑛−1(mod𝑝)Fn≡n⋅3n−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以直接验证对应的 Pisano 周期为 𝜋(5) =20π(5)=20![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于剩余的奇素模数，可以分为两种情形：

  * 如果 𝑝 ≡1,4(mod5)p≡1,4(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有

𝐹𝑝≡12𝑝−1(𝑝𝑝)5(𝑝−1)/2≡1(mod𝑝),𝐹𝑝+1≡12𝑝((𝑝+11)+(𝑝+1𝑝)5(𝑝−1)/2)≡1(mod𝑝).Fp≡12p−1(pp)5(p−1)/2≡1(modp),Fp+1≡12p((p+11)+(p+1p)5(p−1)/2)≡1(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

化简过程中，利用了如下结论：由 [Lucas 定理](../../number-theory/lucas/)，对于 0 <𝑘 <𝑝0<k<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 (𝑝𝑘) ≡0(mod𝑝)(pk)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而对于 1 <𝑘 <𝑝1<k<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 (𝑝+1𝑘) ≡0(mod𝑝)(p+1k)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；由 [Fermat 小定理](../../number-theory/fermat/#费马小定理)，有 2𝑝−1 ≡5𝑝−1 ≡1(mod𝑝)2p−1≡5p−1≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；对于 𝑝 ≡1,4(mod5)p≡1,4(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二次剩余，利用 [二次互反律](../../number-theory/quad-residue/#二次互反律)，也有 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二次剩余，故而 5(𝑝−1)/2 ≡1(mod𝑝)5(p−1)/2≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，有 (𝐹𝑝,𝐹𝑝+1) ≡(𝐹1,𝐹2)(mod𝑝)(Fp,Fp+1)≡(F1,F2)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 (𝑝 −1)(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个周期．所以，𝜋(𝑝) ∣(𝑝 −1)π(p)∣(p−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 如果 𝑝 ≡2,3(mod5)p≡2,3(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有

𝐹2𝑝≡122𝑝−1(2𝑝𝑝)5(𝑝−1)/2≡−1(mod𝑝),𝐹2𝑝+1≡122𝑝((2𝑝+11)+(2𝑝+1𝑝)5(𝑝−1)/2+(2𝑝+12𝑝+1)5𝑝)≡−1(mod𝑝).F2p≡122p−1(2pp)5(p−1)/2≡−1(modp),F2p+1≡122p((2p+11)+(2p+1p)5(p−1)/2+(2p+12p+1)5p)≡−1(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

化简过程中，利用了如下结论：由 Lucas 定理，对于 0 <𝑘 <𝑝0<k<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑝 <𝑘 <2𝑝p<k<2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 (𝑝𝑘) ≡0(mod𝑝)(pk)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以及 (2𝑝𝑝) ≡2(mod𝑝)(2pp)≡2(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而对于 1 <𝑘 <𝑝1<k<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑝 +1 <𝑘 <2𝑝p+1<k<2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都有 (𝑝𝑘) ≡0(mod𝑝)(pk)≡0(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以及 (2𝑝+1𝑝) ≡2(mod𝑝)(2p+1p)≡2(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；由 Fermat 小定理，有 2𝑝−1 ≡5𝑝−1 ≡1(mod𝑝)2p−1≡5p−1≡1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；对于 𝑝 ≡2,3(mod5)p≡2,3(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二次非剩余，利用二次互反律，也有 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二次非剩余，故而 5(𝑝−1)/2 ≡ −1(mod𝑝)5(p−1)/2≡−1(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，有 (𝐹2𝑝,𝐹2𝑝+1) ≡(𝐹−2,𝐹−1)(mod𝑝)(F2p,F2p+1)≡(F−2,F−1)(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 2(𝑝 +1)2(p+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个周期．所以，𝜋(𝑝) ∣2(𝑝 +1)π(p)∣2(p+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这就完成了证明．这一方法的局限性在于它高度依赖于斐波那契数列的通项公式，所以较难直接推广到一般的情形．

另一种证明方式则是试图直接计算矩阵 𝐴 =(1110)A=(1110)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶．它的 [特征多项式](../../linear-algebra/char-poly/) 是 𝑓(𝑥) =𝑥2 −𝑥 −1f(x)=x2−x−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对应的判别式为 Δ =5Δ=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于模 𝑝 =5p=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 Δ ≡0(mod5)Δ≡0(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有两个相同特征值 𝜆 =3λ=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且不能对角化，需要单独计算．对于模 𝑝 ≡1,4(mod5)p≡1,4(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由二次互反律可知，判别式 Δ =5Δ=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二次剩余，矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在域 𝐅𝑝Fp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内有两个相异特征值 𝜆1 ≠𝜆2λ1≠λ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶就是 lcm⁡(ord⁡(𝜆1),ord⁡(𝜆2))lcm⁡(ord⁡(λ1),ord⁡(λ2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必然整除 |𝐅×𝑝| =𝑝 −1|Fp×|=p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于模 𝑝 ≡2,3(mod5)p≡2,3(mod5)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由二次互反律可知，判别式 Δ =5Δ=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是模 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二次非剩余，矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在域 𝐅𝑝Fp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内没有特征值，而只有在 [扩域](../../algebra/field-theory/#域的扩张) 𝐅𝑝[√5]Fp[5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内才有两个相异特征值 𝜆1 ≠𝜆2λ1≠λ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由于 Frobenius 自同态 𝑥 ↦𝑥𝑝x↦xp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将两根交换，有 𝜆2 =𝜆𝑝1λ2=λ1p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故而 𝜆𝑝+11 =𝜆𝑝+12 =𝜆1𝜆2 = −1λ1p+1=λ2p+1=λ1λ2=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，亦即 𝜆2(𝑝+1)1 =𝜆2(𝑝+1)2 =1λ12(p+1)=λ22(p+1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由此，矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶就是 lcm⁡(ord⁡(𝜆1),ord⁡(𝜆2))lcm⁡(ord⁡(λ1),ord⁡(λ2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必然整除 2(𝑝 +1)2(p+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就得到了与前种方法一致的结论．

综上，对于不同的情形，相应地有：

  * 𝜋(2𝑒) =32 ⋅2𝑒, 14𝜋(5𝑒) =5𝑒π(2e)=32⋅2e, 14π(5e)=5e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 当 𝑝 ≡ ±1(mod10)p≡±1(mod10)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝜋(𝑝𝑒) ∣(𝑝 −1)𝑝𝑒−1π(pe)∣(p−1)pe−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝜋(𝑝𝑒) ≤𝑝𝑒π(pe)≤pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 当 𝑝 ≡ ±3(mod10)p≡±3(mod10)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，14𝜋(𝑝𝑒) ∣𝑝+12𝑝𝑒−114π(pe)∣p+12pe−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 14𝜋(𝑝𝑒) ≤𝑝𝑒14π(pe)≤pe![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

所以，利用结论 1，对于一般的模数 𝑚 =∏𝑖𝑝𝑒𝑖𝑖m=∏ipiei![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝜋(𝑚)=lcm⁡{𝜋(𝑝𝑒𝑖𝑖):𝑝𝑖∈𝐏}≤lcm⁡{𝜋(𝑝𝑒𝑖𝑖):𝑝𝑖=2 or 𝑝𝑖≡±1 (mod⁡10)}⋅4⋅lcm⁡{𝜋(𝑝𝑒𝑖𝑖)/4:𝑝𝑖=5 or 𝑝𝑖≡±3 (mod⁡10)}≤∏{𝜋(𝑝𝑒𝑖𝑖):𝑝𝑖=2 or 𝑝𝑖≡±1 (mod⁡10)}⋅4⋅∏{𝜋(𝑝𝑒𝑖𝑖)/4:𝑝𝑖=5 or 𝑝𝑖≡±3 (mod⁡10)}≤32⋅∏{𝑝𝑒𝑖𝑖:𝑝𝑖=2 or 𝑝𝑖≡±1 (mod⁡10)}⋅4⋅∏{𝑝𝑒𝑖𝑖:𝑝𝑖=5 or 𝑝𝑖≡±3 (mod⁡10)}=6𝑚.π(m)=lcm⁡{π(piei):pi∈P}≤lcm⁡{π(piei):pi=2 or pi≡±1 (mod⁡10)}⋅4⋅lcm⁡{π(piei)/4:pi=5 or pi≡±3 (mod⁡10)}≤∏{π(piei):pi=2 or pi≡±1 (mod⁡10)}⋅4⋅∏{π(piei)/4:pi=5 or pi≡±3 (mod⁡10)}≤32⋅∏{piei:pi=2 or pi≡±1 (mod⁡10)}⋅4⋅∏{piei:pi=5 or pi≡±3 (mod⁡10)}=6m.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就说明了斐波那契数列模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Pisano 周期总是不超过 6𝑚6m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而且等号当且仅当在 𝑚 =2 ⋅5𝑒m=2⋅5e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处取得．

## 习题

  * [SPOJ - Euclid Algorithm Revisited](http://www.spoj.com/problems/MAIN74/)
  * [SPOJ - Fibonacci Sum](http://www.spoj.com/problems/FIBOSUM/)
  * [HackerRank - Is Fibo](https://www.hackerrank.com/challenges/is-fibo/problem)
  * [Project Euler - Even Fibonacci numbers](https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem)
  * [洛谷 P4000 斐波那契数列](https://www.luogu.com.cn/problem/P4000)

## 参考文献与注释

  * [Fibonacci sequence - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_sequence)
  * [Zeckendorf's theorem - Wikipedia](https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem)
  * [Pisano period - Wikipedia](https://en.wikipedia.org/wiki/Pisano_period)

**本页面主要译自博文[Числа Фибоначчи](http://e-maxx.ru/algo/fibonacci_numbers) 与其英文翻译版 [Fibonacci Numbers](https://cp-algorithms.com/algebra/fibonacci-numbers.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．内容有改动．**

* * *

  1. 严格来说，它是矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在一般线性群 𝐺𝐿2(𝐙𝑚)GL2(Zm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的阶． ↩

* * *

>  __本页面最近更新： 2026/2/1 11:46:32，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/fibonacci.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/fibonacci.md "edit.link.title")  
>  __本页面贡献者：[Great-designer](https://github.com/Great-designer), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [jifbt](https://github.com/jifbt), [Chrogeek](https://github.com/Chrogeek), [Enter-tainer](https://github.com/Enter-tainer), [EntropyIncreaser](https://github.com/EntropyIncreaser), [FFjet](https://github.com/FFjet), [gsjz](https://github.com/gsjz), [HeRaNO](https://github.com/HeRaNO), [ImpleLee](https://github.com/ImpleLee), [Junyan721113](https://github.com/Junyan721113), [ouuan](https://github.com/ouuan), [untitledunrevised](https://github.com/untitledunrevised), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
