# 贝尔数 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/bell/

# 贝尔数

贝尔数 𝐵𝑛Bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以埃里克·坦普尔·贝尔命名，是组合数学中的一组整数数列，开首是（[OEIS A000110](https://oeis.org/A000110)）：

𝐵0=1,𝐵1=1,𝐵2=2,𝐵3=5,𝐵4=15,𝐵5=52,𝐵6=203,…B0=1,B1=1,B2=2,B3=5,B4=15,B5=52,B6=203,…![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝐵𝑛Bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是基数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合的划分方法的数目．集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个划分是定义为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的两两不相交的非空子集的族，它们的并是 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．例如 𝐵3 =5B3=5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 因为 3 个元素的集合 𝑎,𝑏,𝑐a,b,c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 5 种不同的划分方法：

{{𝑎},{𝑏},{𝑐}}{{𝑎},{𝑏,𝑐}}{{𝑏},{𝑎,𝑐}}{{𝑐},{𝑎,𝑏}}{{𝑎,𝑏,𝑐}}{{a},{b},{c}}{{a},{b,c}}{{b},{a,c}}{{c},{a,b}}{{a,b,c}}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝐵0B0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 1 因为空集正好有 1 种划分方法．

## 递推公式

贝尔数适合递推公式：

𝐵𝑛+1=𝑛∑𝑘=0(𝑛𝑘)𝐵𝑘Bn+1=∑k=0n(nk)Bk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明：

𝐵𝑛+1Bn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是含有 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素集合的划分个数，设 𝐵𝑛Bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合为 {𝑏1,𝑏2,𝑏3,…,𝑏𝑛}{b1,b2,b3,…,bn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐵𝑛+1Bn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合为 {𝑏1,𝑏2,𝑏3,…,𝑏𝑛,𝑏𝑛+1}{b1,b2,b3,…,bn,bn+1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么可以认为 𝐵𝑛+1Bn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是有 𝐵𝑛Bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 增添了一个 𝑏𝑛+1bn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而产生的，考虑元素 𝑏𝑛+1bn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 假如它被单独分到一类，那么还剩下 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素，这种情况下划分数为 (𝑛𝑛)𝐵𝑛(nn)Bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7);

  * 假如它和某 1 个元素分到一类，那么还剩下 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素，这种情况下划分数为 (𝑛𝑛−1)𝐵𝑛−1(nn−1)Bn−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

  * 假如它和某 2 个元素分到一类，那么还剩下 𝑛 −2n−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素，这种情况下划分数为 (𝑛𝑛−2)𝐵𝑛−2(nn−2)Bn−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

  * ……

以此类推就得到了上面的公式．

每个贝尔数都是相应的 [第二类斯特林数](../stirling/#第二类斯特林数stirling-number) 的和． 因为第二类斯特林数是把基数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合划分为正好 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个非空集的方法数目．

𝐵𝑛=𝑛∑𝑘=0{𝑛𝑘}Bn=∑k=0n{nk}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 贝尔三角形

用以下方法构造一个三角矩阵（形式类似杨辉三角形）：

  * 𝑎0,0 =1a0,0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 对于 𝑛 ≥1n≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行首项等于上一行的末项，即 𝑎𝑛,0 =𝑎𝑛−1,𝑛−1an,0=an−1,n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 对于 𝑚,𝑛 ≥1m,n≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行第 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项等于它左边和左上角两个数之和，即 𝑎𝑛,𝑚 =𝑎𝑛,𝑚−1 +𝑎𝑛−1,𝑚−1an,m=an,m−1+an−1,m−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

部分结果如下：

11223557101515202737525267871141512032032553224095236748771122355710151520273752526787114151203203255322409523674877![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

每行的首项是贝尔数．可以利用这个三角形来递推求出贝尔数．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text constexpr int MAXN = 2000 \+ 5 ; int bell [ MAXN ][ MAXN ]; void f ( int n ) { bell [ 0 ][ 0 ] = 1 ; for ( int i = 1 ; i <= n ; i ++ ) { bell [ i ][ 0 ] = bell [ i \- 1 ][ i \- 1 ]; for ( int j = 1 ; j <= i ; j ++ ) bell [ i ][ j ] = bell [ i \- 1 ][ j \- 1 ] \+ bell [ i ][ j \- 1 ]; } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text MAXN = 2000 \+ 5 bell = [[ 0 for i in range ( MAXN \+ 1 )] for j in range ( MAXN \+ 1 )] def f ( n ): bell [ 0 ][ 0 ] = 1 for i in range ( 1 , n \+ 1 ): bell [ i ][ 0 ] = bell [ i \- 1 ][ i \- 1 ] for j in range ( 1 , i \+ 1 ): bell [ i ][ j ] = bell [ i \- 1 ][ j \- 1 ] \+ bell [ i ][ j \- 1 ] ```   
---|---  
  
## 指数生成函数

考虑贝尔数的指数生成函数及其导函数：

ˆ𝐵(𝑥)=+∞∑𝑛=0𝐵𝑛𝑛!𝑥𝑛=1++∞∑𝑛=0𝐵𝑛+1(𝑛+1)!𝑥𝑛+1ˆ𝐵′(𝑥)=+∞∑𝑛=0𝐵𝑛+1𝑛!𝑥𝑛B^(x)=∑n=0+∞Bnn!xn=1+∑n=0+∞Bn+1(n+1)!xn+1B^′(x)=∑n=0+∞Bn+1n!xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据贝尔数的递推公式可以得到：

𝐵𝑛+1𝑛!=𝑛∑𝑘=01(𝑛−𝑘)!𝐵𝑘𝑘!Bn+1n!=∑k=0n1(n−k)!Bkk!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是一个卷积的式子，因此有：

ˆ𝐵′(𝑥)=e𝑥ˆ𝐵(𝑥)B^′(x)=exB^(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是一个微分方程，解得：

ˆ𝐵(𝑥)=exp⁡(e𝑥+𝐶)B^(x)=exp⁡(ex+C)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最后当 𝑥 =0x=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时 ˆ𝐵(𝑥) =1B^(x)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，带入后解得 𝐶 = −1C=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得到贝尔数指数生成函数的封闭形式：

ˆ𝐵(𝑥)=exp⁡(e𝑥−1)B^(x)=exp⁡(ex−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

预处理出 e𝑥 −1ex−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项后做一次 [多项式 exp](../../poly/elementary-func/#多项式对数函数--指数函数) 即可得出贝尔数前 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项，时间复杂度瓶颈在多项式 exp，可做到 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度．

## 参考文献

<https://en.wikipedia.org/wiki/Bell_number>

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/bell.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/bell.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Xeonacid](https://github.com/Xeonacid), [ksyx](https://github.com/ksyx), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [LDlornd](https://github.com/LDlornd), [Menci](https://github.com/Menci), [Running-Turtle1](https://github.com/Running-Turtle1), [ShaoChenHeng](https://github.com/ShaoChenHeng), [shawlleyw](https://github.com/shawlleyw), [StudyingFather](https://github.com/StudyingFather), [untitledunrevised](https://github.com/untitledunrevised), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
