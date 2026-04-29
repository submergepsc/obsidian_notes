# 快速幂 - OI Wiki

- Source: https://oi-wiki.org/math/binary-exponentiation/

# 快速幂

## 引入

**快速幂** （fast exponentiation），也称 **二进制取幂** （binary exponentiation）或 **平方取幂法** （exponentiation by squaring），是一个在 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内计算 𝑎𝑛an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的小技巧，而暴力的计算需要 Θ(𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间．

这个技巧可以应用于任何 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘法满足结合律的场景中，例如模意义下取幂、矩阵幂等，详见后文 应用 一节．

## 过程

计算 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次方表示将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘在一起：𝑎𝑛 =𝑎×𝑎⋯×𝑎⏟𝑛 个 aan=a×a⋯×a⏟n 个 a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．然而当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 太大或单次乘法开销太大的时侯，这种方法就不太适用了．二进制取幂的想法是，将取幂的任务按照指数的 **二进制表示** 来分割成更小的任务．

例子

假设要计算 313313![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果将它展开为连乘式，需要 13 −1 =1213−1=12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次乘法．但是，因为

313=3(1101)2=38×34×31,313=3(1101)2=38×34×31,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以，只要能快速计算出 31,32,34,3831,32,34,38![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就能通过 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次乘法计算出 313313![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．于是，只需要知道一个快速的方法来计算上述 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 2𝑘2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂的序列．这是容易的，因为因为序列中（除第一个）任意一个元素都是其前一个元素的平方．

根据这些分析，可以得到 313313![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算过程如下：

31=3,32=(31)2=32=9,34=(32)2=92=81,38=(34)2=812=6561,313=6561×81×3=1594323.31=3,32=(31)2=32=9,34=(32)2=92=81,38=(34)2=812=6561,313=6561×81×3=1594323.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

过程中，只进行了 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次乘法运算．

这就是快速幂的基本想法．至于具体实现，有两种常见的版本．

### 迭代版本

设 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制表示为 (𝑛𝑡𝑛𝑡−1⋯𝑛1𝑛0)2(ntnt−1⋯n1n0)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，有

𝑛=𝑛𝑡2𝑡+𝑛𝑡−12𝑡−1+⋯+𝑛121+𝑛020,n=nt2t+nt−12t−1+⋯+n121+n020,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，𝑛𝑖 ∈{0,1}ni∈{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，就有

𝑎𝑛=𝑎𝑛𝑡2𝑡+𝑛𝑡−12𝑡−1+⋯+𝑛121+𝑛020=𝑎𝑛020×𝑎𝑛121×⋯×𝑎𝑛𝑡−12𝑡−1×𝑎𝑛𝑡2𝑡.an=ant2t+nt−12t−1+⋯+n121+n020=an020×an121×⋯×ant−12t−1×ant2t.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意，只有 𝑛𝑖 =1ni=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的项才会真正出现在乘积的计算中．

根据这一表达式，可以首先在 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内计算出 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 2𝑘2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂的取值，然后花费 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间选择等于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制位对应的幂次乘到最终结果中．这就是快速幂的迭代版本实现．

伪代码如下：

𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 FastPow(𝑎,𝑛):𝐈𝐧𝐩𝐮𝐭. Base 𝑎 and exponent 𝑛.𝐎𝐮𝐭𝐩𝐮𝐭. Power 𝑎𝑛.𝐌𝐞𝐭𝐡𝐨𝐝.1𝑟𝑒𝑠𝑢𝑙𝑡←Id2𝐰𝐡𝐢𝐥𝐞 𝑛>0 𝐝𝐨3𝐢𝐟 𝑛mod2=1 𝐭𝐡𝐞𝐧4𝑟𝑒𝑠𝑢𝑙𝑡←𝑟𝑒𝑠𝑢𝑙𝑡⋅𝑎5𝐞𝐧𝐝 𝐢𝐟6𝑎←𝑎⋅𝑎7𝑛←𝑛/28𝐞𝐧𝐝 𝐰𝐡𝐢𝐥𝐞9𝐫𝐞𝐭𝐮𝐫𝐧 𝑟𝑒𝑠𝑢𝑙𝑡Algorithm FastPow(a,n):Input. Base a and exponent n.Output. Power an.Method.1result←Id2while n>0 do3if nmod2=1 then4result←result⋅a5end if6a←a⋅a7n←n/28end while9return result![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用这一方法计算快速幂，需要进行 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次乘法运算．

### 递归版本

这一过程同样可以通过递归形式实现．注意到，指数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制展开可以递归地写作

(𝑛𝑡𝑛𝑡−1⋯𝑛1𝑛0)2=2×(𝑛𝑡𝑛𝑡−1⋯𝑛1)2+𝑛0.(ntnt−1⋯n1n0)2=2×(ntnt−1⋯n1)2+n0.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，幂次 𝑎𝑛an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以递归地计算为

𝑎𝑛=⎧{ {⎨{ {⎩1,𝑛=0,(𝑎⌊𝑛/2⌋)2,𝑛>0 and 𝑛 is even,(𝑎⌊𝑛/2⌋)2⋅𝑎,𝑛>0 and 𝑛 is odd.an={1,n=0,(a⌊n/2⌋)2,n>0 and n is even,(a⌊n/2⌋)2⋅a,n>0 and n is odd.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这就是快速幂的递归版本实现．

伪代码如下：

𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦 FastPow(𝑎,𝑛):𝐈𝐧𝐩𝐮𝐭. Base 𝑎 and exponent 𝑛.𝐎𝐮𝐭𝐩𝐮𝐭. Power 𝑎𝑛.𝐌𝐞𝐭𝐡𝐨𝐝.1𝐢𝐟 𝑛=0 𝐭𝐡𝐞𝐧2𝐫𝐞𝐭𝐮𝐫𝐧 Id3𝐞𝐧𝐝 𝐢𝐟4𝑟𝑒𝑠𝑢𝑙𝑡←FastPow(𝑎,𝑛/2)5𝐢𝐟 𝑛mod2=0 𝐭𝐡𝐞𝐧6𝐫𝐞𝐭𝐮𝐫𝐧 𝑟𝑒𝑠𝑢𝑙𝑡⋅𝑟𝑒𝑠𝑢𝑙𝑡7𝐞𝐥𝐬𝐞8𝐫𝐞𝐭𝐮𝐫𝐧 𝑟𝑒𝑠𝑢𝑙𝑡⋅𝑟𝑒𝑠𝑢𝑙𝑡⋅𝑎9𝐞𝐧𝐝 𝐢𝐟Algorithm FastPow(a,n):Input. Base a and exponent n.Output. Power an.Method.1if n=0 then2return Id3end if4result←FastPow(a,n/2)5if nmod2=0 then6return result⋅result7else8return result⋅result⋅a9end if![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用这一方法计算快速幂，需要递归 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，同样需要 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次乘法运算．尽管复杂度相同，由于递归本身有一定开销，所以实践中迭代版本的速度更快．

## 应用

### 模意义下取幂

[洛谷 P1226【模板】快速幂](https://www.luogu.com.cn/problem/P1226)

给定三个整数 𝑎,𝑏,𝑝a,b,p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 𝑎𝑏mod𝑝abmodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中 𝑝 ≥2p≥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这是一个非常常见的应用，例如它可以用于计算模意义下的乘法逆元．既然我们知道取模的运算不会干涉乘法运算，因此我们只需要在计算的过程中取模即可．

首先我们可以直接按照上述递归方法实现：

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 ``` |  ```text long long binpow ( long long a , long long b , long long p ) { if ( b == 0 ) return 1 ; long long res = binpow ( a , b / 2 , p ); if ( b % 2 ) return res * res % p * a % p ; else return res * res % p ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text def binpow ( a , b , p ): if b == 0 : return 1 res = binpow ( a , b // 2 , p ) if ( b % 2 ) == 1 : return res * res * a % p else : return res * res % p ```   
---|---  
  
第二种实现方法是非递归式的．它在循环的过程中将二进制位为 1 时对应的幂累乘到答案中．尽管两者的理论复杂度是相同的，但第二种在实践过程中的速度是比第一种更快的，因为递归会花费一定的开销．

参考实现

C++Python

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text long long binpow ( long long a , long long b , long long p ) { long long res = 1 ; while ( b > 0 ) { if ( b & 1 ) res = res * a % p ; a = a * a % p ; b >>= 1 ; } return res ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text def binpow ( a , b , p ): res = 1 while b > 0 : if b & 1 : res = res * a % p a = a * a % p b >>= 1 return res ```   
---|---  
  
注意

  * 模数通常情况下大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在十分特殊的情况下，模数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能等于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时需要特殊考虑 𝑏 =0b=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况．
  * 当指数很大时，需利用 [扩展欧拉定理](../number-theory/fermat/#扩展欧拉定理) 降幂后计算．

### 计算斐波那契数

根据斐波那契数列的递推式 𝐹𝑛 =𝐹𝑛−1 +𝐹𝑛−2Fn=Fn−1+Fn−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以构建一个 2 ×22×2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵来表示从 𝐹𝑖,𝐹𝑖+1Fi,Fi+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝐹𝑖+1,𝐹𝑖+2Fi+1,Fi+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的变换．于是在计算这个矩阵的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂的时侯，我们使用快速幂的思想，可以在 Θ(log⁡𝑛)Θ(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内计算出结果．对于更多的细节参见 [斐波那契数列](../combinatorics/fibonacci/)，矩阵快速幂的实现参见 [矩阵加速递推](../linear-algebra/matrix/#矩阵加速递推) 中的实现．

### 多次置换

问题描述

给你一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列和一个置换，把这个序列置换 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．

简单地把这个置换取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂，然后把它应用到序列上即可．时间复杂度为 𝑂(𝑛log⁡𝑘)O(nlog⁡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于更多的细节参见 [置换的复合](../permutation/#复合)．

注意

对这个置换建图，然后在每一个环上分别做 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂（事实上等价于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对环长取模），可以在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度下解决此问题．

### 加速几何中对点集的操作

[HDU 4087 A Letter to Programmers](https://acm.hdu.edu.cn/showproblem.php?pid=4087)

给定三维空间中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要求将 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个操作都应用于这些点．包含 3 种操作：

  1. 沿某个向量移动点的位置（Shift）．
  2. 按比例缩放这个点的坐标（Scale）．
  3. 绕某条直线旋转（Rotate）．

还有一个特殊的操作，就是将某个操作序列重复 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次（Repeat），Repeat 操作可以嵌套．输出操作结束后每个点的坐标．

参考 [向量与矩阵](../linear-algebra/vector/#向量与矩阵) 中的内容，每一种操作都可以用一个变换矩阵表示，一系列连续的变换可以用矩阵的乘积来表示．一个 Repeat 操作就相当于取一个矩阵的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂．这样可以用 𝑂(𝑚log⁡𝑘)O(mlog⁡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间计算出整个变换序列最终形成的矩阵．最后将它应用到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点上，总复杂度 𝑂(𝑛 +𝑚log⁡𝑘)O(n+mlog⁡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 定长路径计数

问题描述

给一个有向图（边权为 1），求任意两点 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 间从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径的条数．

我们把该图的邻接矩阵 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次幂，那么 𝑀𝑖,𝑗Mi,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就表示从 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径的数目．该算法的复杂度是 𝑂(𝑛3log⁡𝑘)O(n3log⁡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．有关该算法的细节请参见 [矩阵](../linear-algebra/matrix/#定长路径统计) 页面．

### 模意义下的整数乘法

问题描述

给定非负整数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，计算 𝑎 ×𝑏mod𝑚a×bmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑎,𝑏 ≤𝑚 ≤1018a,b≤m≤1018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

与二进制取幂的思想一样，这次我们将其中的一个乘数表示为若干个 2 的整数次幂的和的形式．因为在对一个数做乘 2 并取模的运算的时侯，我们可以转化为加减操作防止整型溢出．这样可以在 𝑂(log⁡𝑚)O(log⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度下解决问题．递归方法如下：

𝑎⋅𝑏=⎧{ {⎨{ {⎩0if 𝑎=02⋅𝑎2⋅𝑏if 𝑎>0 and 𝑎 even2⋅𝑎−12⋅𝑏+𝑏if 𝑎>0 and 𝑎 odda⋅b={0if a=02⋅a2⋅bif a>0 and a even2⋅a−12⋅b+bif a>0 and a odd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但在实际使用中，此方法由于引入了更大的计算复杂度导致时间效率不优．实际编程中通常利用 [快速乘](../number-theory/mod-arithmetic/#快速乘) 来进行模数范围在 `long long` 时的乘法操作．

### 高精度快速幂

前置技能：[大整数乘法](../bignum/#乘法)

[洛谷 P1045 [NOIP 2003 普及组] 麦森数](https://www.luogu.com.cn/problem/P1045)

给定整数 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（1000 <𝑃 <31000001000<P<3100000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），计算 2𝑃 −12P−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位数与最后 500500![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位数字（用十进制数表示），不足 500500![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位时高位补 0．

代码实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 ``` |  ```text #include <cmath> #include <cstring> #include <iostream> using namespace std ; const int M = 500 ; int a [ 505 ], b [ 505 ], t [ 505 ]; // 大整数乘法 void mult ( int x [], int y []) { memset ( t , 0 , sizeof ( t )); for ( int i = 1 ; i <= x [ 0 ]; i ++ ) { for ( int j = 1 ; j <= y [ 0 ]; j ++ ) { if ( i \+ j \- 1 > M ) continue ; t [ i \+ j \- 1 ] += x [ i ] * y [ j ]; t [ i \+ j ] += t [ i \+ j \- 1 ] / 10 ; t [ i \+ j \- 1 ] %= 10 ; t [ 0 ] = i \+ j ; } } memcpy ( b , t , sizeof ( b )); } // 快速幂 void binpow ( int p ) { if ( p == 1 ) { memcpy ( b , a , sizeof ( b )); return ; } binpow ( p / 2 ); // (2^(p/2))^2=2^p mult ( b , b ); // 对 b 平方 if ( p % 2 == 1 ) mult ( b , a ); } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int p ; cin >> p ; a [ 0 ] = 1 ; // 记录 a 数组的位数 a [ 1 ] = 2 ; // 对 2 进行平方 b [ 0 ] = 1 ; // 记录 b 数组的位数 b [ 1 ] = 1 ; // 答案数组 binpow ( p ); cout << ( int )( log10 ( 2 ) * p ) \+ 1 << '\n' ; b [ 1 ] -= 1 ; // 最后一位减 1 for ( int i = M ; i >= 1 ; i \-- ) { cout << b [ i ]; if (( i \- 1 ) % 50 == 0 ) { cout << '\n' ; } } } ```   
---|---  
  
## 底数固定的预处理快速幂

当底数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 固定时，可以利用 [分块思想](../../ds/decompose/)，用一定的时间预处理后用 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间回答一次幂询问．这一算法也常称为光速幂．过程如下：

  1. 选定一个数 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，预处理出 𝑎0,𝑎1,⋯,𝑎𝑠−1a0,a1,⋯,as−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑎0,𝑎𝑠,⋯,𝑎⌊𝑝/𝑠⌋𝑠a0,as,⋯,a⌊p/s⌋s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值并存在两个数组里；
  2. 对于每一次询问 𝑎𝑏ab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拆分成 ⌊𝑏/𝑠⌋𝑠 +(𝑏mod𝑠)⌊b/s⌋s+(bmods)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑎𝑏 =𝑎⌊𝑏/𝑠⌋𝑠 ⋅𝑎𝑏mod𝑠ab=a⌊b/s⌋s⋅abmods![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求出答案．

假设指数 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的范围是 [0,𝑛][0,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么块长 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 经常选择为 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或者与之相近的 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次．选择 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以获得最优的预处理复杂度 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而选择 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次可以使用位操作简化计算．

特别地，对于模意义下幂的计算，底数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同隐含着模数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也要相同这一要求．由于 [扩展欧拉定理](../number-theory/fermat/#扩展欧拉定理)，对于任意模数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，预处理的指数范围上界为 𝑛 =2𝜑(𝑚)n=2φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；对于素模数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，预处理的范围上界为 𝑛 =𝑝 −1n=p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这两种情形预处理的复杂度都是 𝑂(√𝑚)O(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text int a , mod , pow1 [ 65536 ], pow2 [ 65536 ]; void preproc () { pow1 [ 0 ] = pow2 [ 0 ] = 1 ; for ( int i = 1 ; i < 65536 ; i ++ ) pow1 [ i ] = 1L L * pow1 [ i \- 1 ] * a % mod ; int pow65536 = 1L L * pow1 [ 65535 ] * a % mod ; for ( int i = 1 ; i < 65536 ; i ++ ) pow2 [ i ] = 1L L * pow2 [ i \- 1 ] * pow65536 % mod ; } int query ( int pows ) { return 1L L * pow1 [ pows & 65535 ] * pow2 [ pows >> 16 ] % mod ; } ```   
---|---  
  
## 习题

  * [UVa 1230 - MODEX](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671)
  * [UVa 374 - Big Mod](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=310)
  * [UVa 11029 - Leading and Trailing](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1970)
  * [Codeforces - Parking Lot](http://codeforces.com/problemset/problem/630/I)
  * [SPOJ - The last digit](http://www.spoj.com/problems/LASTDIG/)
  * [SPOJ - Locker](http://www.spoj.com/problems/LOCKER/)
  * [SPOJ - Just add it](http://www.spoj.com/problems/ZSUM/)

**本页面部分内容译自博文[Бинарное возведение в степень](http://e-maxx.ru/algo/binary_pow) 与其英文翻译版 [Binary Exponentiation](https://cp-algorithms.com/algebra/binary-exp.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/27 12:26:08，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/binary-exponentiation.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/binary-exponentiation.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [cbw2007](https://github.com/cbw2007), [Enter-tainer](https://github.com/Enter-tainer), [Xeonacid](https://github.com/Xeonacid), [HeRaNO](https://github.com/HeRaNO), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [c-forrest](https://github.com/c-forrest), [Henry-ZHR](https://github.com/Henry-ZHR), [iamtwz](https://github.com/iamtwz), [luoguyuntianming](https://github.com/luoguyuntianming), [Marcythm](https://github.com/Marcythm), [Peanut-Tang](https://github.com/Peanut-Tang), [Aquistcev](https://github.com/Aquistcev), [billchenchina](https://github.com/billchenchina), [CCXXXI](https://github.com/CCXXXI), [chinggg](https://github.com/chinggg), [eyedeng](https://github.com/eyedeng), [FFjet](https://github.com/FFjet), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [hhc0001](https://github.com/hhc0001), [hsfzLZH1](https://github.com/hsfzLZH1), [Hszzzx](https://github.com/Hszzzx), [JEB-Bem](https://github.com/JEB-Bem), [Jude Gao](mailto:jude.gao@faire.com), [kenlig](https://github.com/kenlig), [kfy666](https://github.com/kfy666), [Konano](https://github.com/Konano), [Menci](https://github.com/Menci), [NachtgeistW](https://github.com/NachtgeistW), [qwqAutomaton](https://github.com/qwqAutomaton), [shawlleyw](https://github.com/shawlleyw), [shenshuaijie](https://github.com/shenshuaijie), [StudyingFather](https://github.com/StudyingFather), [TOMWT-qwq](https://github.com/TOMWT-qwq), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [TRSWNCA](https://github.com/TRSWNCA), [uqzjc](https://github.com/uqzjc), [Zhoier](https://github.com/Zhoier)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
