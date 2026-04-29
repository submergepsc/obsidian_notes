# 图论计数 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/graph-enumeration/

# 图论计数

在组合数学中，图论计数（Graph Enumeration）是研究满足特定性质的图的计数问题的分支．[生成函数](../../poly/intro/)、[波利亚计数定理](../polya/) 与 [符号化方法](../../poly/symbolic-method/#%E9%9B%86%E5%90%88%E7%9A%84-cycle-%E6%9E%84%E9%80%A0) 和 [OEIS](https://oeis.org/) 是解决这类问题时最重要的数学工具．图论计数可分为有标号和无标号两大类问题，大多数情况下1有标号版本的问题都比其对应的无标号问题更加简单，因此我们将先考察有标号问题的计数．

## 有标号树

即 Cayley 公式，参见 [Prüfer 序列](../../../graph/prufer/) 一文，我们也可以使用 [Kirchhoff 矩阵树定理](../../../graph/matrix-tree/) 或 [生成函数](../../poly/intro/#生成函数) 和 [拉格朗日定理](https://codeforces.com/blog/entry/104184) 得到这一结果．

### 习题

  * [Hihocoder 1047. Random Tree](https://vjudge.net/problem/HihoCoder-1047)

## 有标号连通图

### 例题「POJ 1737」Connected Graph

例题 [「POJ 1737」Connected Graph](http://poj.org/problem?id=1737)

题目大意：求有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点的有标号连通图的方案数（𝑛 ≤50n≤50![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

这类问题最早出现于楼教主的男人八题系列中，我们设 𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点有标号图的方案数，𝑐𝑛cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为待求序列．𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点的图至多有 (𝑛2)(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边，每条边根据其出现与否有两种状态，每种状态之间独立，因而有 𝑔𝑛 =2(𝑛2)gn=2(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们固定其中一个节点，枚举其所在连通块的大小，那么还需要从剩下的 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点中选择 𝑖 −1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点组成一个连通块．连通块之外的节点可以任意连边，因而有如下递推关系：

𝑛∑𝑖=1(𝑛−1𝑖−1)𝑐𝑖𝑔𝑛−𝑖=𝑔𝑛𝑐𝑛=𝑔𝑛−𝑛−1∑𝑖=1(𝑛−1𝑖−1)𝑐𝑖𝑔𝑛−𝑖∑i=1n(n−1i−1)cign−i=gncn=gn−∑i=1n−1(n−1i−1)cign−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

移项得到 𝑐𝑛cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 序列的 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递推公式，可以通过此题．

### 例题「集训队作业 2013」城市规划

例题 [「集训队作业 2013」城市规划](https://www.luogu.com.cn/problem/P4841)

题目大意：求有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点的有标号连通图的方案数（𝑛 ≤130000n≤130000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

对于数据范围更大的序列问题，往往我们需要构造这些序列的生成函数，以使用高效的多项式算法．

#### 方法一：分治 FFT

上述的递推式可以看作一种自卷积形式，因而可以使用分治 FFT 进行计算，复杂度 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 方法二：多项式求逆

我们将上述递推式中的组合数展开，并进行变形：

𝑛∑𝑖=1(𝑛−1𝑖−1)𝑐𝑖𝑔𝑛−𝑖=𝑔𝑛𝑛∑𝑖=1𝑐𝑖(𝑖−1)!𝑔𝑛−𝑖(𝑛−𝑖)!=𝑔𝑛(𝑛−1)!∑i=1n(n−1i−1)cign−i=gn∑i=1nci(i−1)!gn−i(n−i)!=gn(n−1)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

构造多项式：

𝐶(𝑥)=∑𝑛=1𝑐𝑛(𝑛−1)!𝑥𝑛𝐺(𝑥)=∑𝑛=0𝑔𝑛𝑛!𝑥𝑛𝐻(𝑥)=∑𝑛=1𝑔𝑛(𝑛−1)!𝑥𝑛C(x)=∑n=1cn(n−1)!xnG(x)=∑n=0gnn!xnH(x)=∑n=1gn(n−1)!xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

代换进上式得到 𝐶𝐺 =𝐻CG=H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使用 [多项式求逆](../../poly/elementary-func/#%E5%A4%9A%E9%A1%B9%E5%BC%8F%E6%B1%82%E9%80%86) 后再卷积解出 𝐶(𝑥)C(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

#### 方法三：多项式 exp

另一种做法是使用 [EGF 中多项式 exp 的组合意义](../../poly/egf/#egf-%E4%B8%AD%E5%A4%9A%E9%A1%B9%E5%BC%8F-exp-%E7%9A%84%E7%BB%84%E5%90%88%E6%84%8F%E4%B9%89)，我们设有标号连通图和简单图序列的 EGF 分别为 𝐶(𝑥)C(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐺(𝑥)G(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么它们将有下列关系：

exp⁡(𝐶(𝑥))=𝐺(𝑥)𝐶(𝑥)=ln⁡(𝐺(𝑥))exp⁡(C(x))=G(x)C(x)=ln⁡(G(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

使用 [多项式 ln](../../poly/elementary-func/#多项式对数函数--指数函数) 解出 𝐶(𝑥)C(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

## 有标号欧拉图、二分图

### 例题「SPOJ KPGRAPHS」Counting Graphs

例题 [「SPOJ KPGRAPHS」Counting Graphs](http://www.spoj.com/problems/KPGRAPHS/)

题目大意：求有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点的分别满足下列性质的有标号图的方案数（𝑛 ≤1000n≤1000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

  * 连通图 [A001187](https://oeis.org/A001187)．
  * 欧拉图 [A033678](https://oeis.org/A033678)．
  * 二分图 [A047864](https://oeis.org/A047864)．

本题限制代码长度，因而无法直接使用多项式模板，但生成函数依然可以帮助我们进行分析．

连通图问题在之前的例题中已被解决，考虑欧拉图．注意到上述对连通图计数的几种方法，均可以在满足任意性质的有标号连通图进行推广．例如我们可以将连通图递推公式中的 𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从任意图替换成满足顶点度数均为偶数的图，此时得到的 𝑐𝑛cn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为欧拉图．

我们将 POJ 1737 的递推过程封装成连通化函数，

```text 1 2 3 4 5 6 7 ``` |  ```text void ln ( Int C [], Int G []) { for ( int i = 1 ; i <= n ; ++ i ) { C [ i ] = G [ i ]; for ( int j = 1 ; j <= i \- 1 ; ++ j ) C [ i ] -= binom [ i \- 1 ][ j \- 1 ] * C [ j ] * G [ i \- j ]; } } ```   
---|---  
  
前两问即可轻松解决：

```text 1 2 3 4 ``` |  ```text for ( int i = 1 ; i <= n ; ++ i ) G [ i ] = pow ( 2 , binom [ i ][ 2 ]); ln ( C , G ); for ( int i = 1 ; i <= n ; ++ i ) G [ i ] = pow ( 2 , binom [ i \- 1 ][ 2 ]); ln ( E , G ); ```   
---|---  
  
注意到这里的连通化递推过程其实等价于对其 EGF 求多项式 ln，同理我们也可以写出逆连通化函数，它等价于对其 EGF 求多项式 exp．

```text 1 2 3 4 5 6 7 ``` |  ```text void exp ( Int G [], Int C []) { for ( int i = 1 ; i <= n ; ++ i ) { G [ i ] = C [ i ]; for ( int j = 1 ; j <= i \- 1 ; ++ j ) G [ i ] += binom [ i \- 1 ][ j \- 1 ] * C [ j ] * G [ i \- j ]; } } ```   
---|---  
  
下面讨论有标号二分图计数，

我们设 𝑏𝑛bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 n 个结点的二分图方案数，𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点对结点进行 2 染色，满足相同颜色的结点之间不存在边的图的方案数．枚举其中一种颜色节点的数量，有2：

𝑔𝑛=𝑛∑𝑖=0(𝑛𝑖)2𝑖(𝑛−𝑖)gn=∑i=0n(ni)2i(n−i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

接下来我们用两种不同的方法建立 𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑏𝑛bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的关系．

#### 方法一：算两次

我们设 𝑐𝑛,𝑘cn,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示有 k 个连通分量的二分图方案数，那么不难得到如下关系：

𝑏𝑛=𝑛∑𝑖=1𝑐𝑛,𝑖𝑔𝑛=𝑛∑𝑖=1𝑐𝑛,𝑖2𝑖bn=∑i=1ncn,ign=∑i=1ncn,i2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

比较两种 𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的表达式，展开得：

𝑛∑𝑖=0(𝑛𝑖)2𝑖(𝑛−𝑖)=𝑛∑𝑖=1𝑐𝑛,𝑖2𝑖𝑐𝑛,𝑖=∑𝑖=0𝑛−1(𝑛−1𝑖−1)𝑐𝑛,1𝑐𝑛−𝑖,𝑘−1∑i=0n(ni)2i(n−i)=∑i=1ncn,i2icn,i=∑i=0n−1(n−1i−1)cn,1cn−i,k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

不难得到 𝑏𝑛bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递推关系，复杂度 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进一步使用容斥原理，可以优化到 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通过本题．

#### 方法二：连通化递推

方法二和方法三均使用连通二分图 𝑏1𝑛b1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) [A001832](https://oeis.org/A001832) 来建立 𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑏𝑛bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的桥梁．

注意到对于每个连通二分图，我们恰好有两种不同的染色方法，对应到两组不同的连通 2 染色图， 因而对 𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行连通化，得到的序列恰好是 𝑏1𝑛b1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的两倍，而 𝑏𝑛bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则由 𝑏1𝑛b1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行逆连通化得到．

因此：

```text 1 2 3 4 5 6 7 ``` |  ```text for ( int i = 1 ; i <= n ; ++ i ) { G [ i ] = 0 ; for ( int j = 0 ; j < i \+ 1 ; ++ j ) G [ i ] += binom [ i ][ j ] * pow ( 2 , j * ( i \- j )); } ln ( B1 , G ); for ( int i = 1 ; i <= n ; ++ i ) B1 [ i ] /= 2 ; exp ( B , B1 ); ```   
---|---  
  
两种递推的过程复杂度均为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以通过本题．

#### 方法三：多项式 exp

我们注意到也可以使用 EGF 理解上面的递推过程．

设 𝐺(𝑥)G(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 EGF，𝐵1(𝑥)B1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑏1𝑛b1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 EGF，𝐵(𝑥)B(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑏𝑛bn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 EGF，应用做法二的方法，我们有：

𝐺(𝑥)=exp⁡(2𝐵1(𝑥))𝐵(𝑥)=exp⁡(𝐵1(𝑥))=exp⁡(ln⁡𝐺(𝑥)2)=√𝐺G(x)=exp⁡(2B1(x))B(x)=exp⁡(B1(x))=exp⁡(ln⁡G(x)2)=G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们可以对等式两边分别进行求导并比较两边系数，以得到易于编码的递推公式，通过此题． 注意到做法二与做法三本质相同，且一般情况下做法三可以得到更优的时间复杂度．

𝐵2𝑛=𝐺2𝐵𝑛𝐵′𝑛=𝐺′Bn2=G2BnBn′=G′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 ``` |  ```text #include <iostream> using namespace std ; using LL = long long ; constexpr int MOD = int ( 1e9 ) \+ 7 ; // <<= '2. Number Theory .,//{ namespace NT { void INC ( int & a , int b ) { a += b ; if ( a >= MOD ) a -= MOD ; } int sum ( int a , int b ) { a += b ; if ( a >= MOD ) a -= MOD ; return a ; } void DEC ( int & a , int b ) { a -= b ; if ( a < 0 ) a += MOD ; } int dff ( int a , int b ) { a -= b ; if ( a < 0 ) a += MOD ; return a ; } void MUL ( int & a , int b ) { a = ( LL ) a * b % MOD ; } int pdt ( int a , int b ) { return ( LL ) a * b % MOD ; } int _I ( int b ) { int a = MOD , x1 = 0 , x2 = 1 , q ; while ( 1 ) { q = a / b , a %= b ; if ( ! a ) return x2 ; DEC ( x1 , pdt ( q , x2 )); q = b / a , b %= a ; if ( ! b ) return x1 ; DEC ( x2 , pdt ( q , x1 )); } } void DIV ( int & a , int b ) { MUL ( a , _I ( b )); } int qtt ( int a , int b ) { return pdt ( a , _I ( b )); } int pow ( int a , LL b ) { int c ( 1 ); while ( b ) { if ( b & 1 ) MUL ( c , a ); MUL ( a , a ), b >>= 1 ; } return c ; } template < class T > T pow ( T a , LL b ) { T c ( 1 ); while ( b ) { if ( b & 1 ) c *= a ; a *= a , b >>= 1 ; } return c ; } template < class T > T pow ( T a , int b ) { return pow ( a , ( LL ) b ); } struct Int { int val ; operator int () const { return val ; } Int ( int _val = 0 ) : val ( _val ) { val %= MOD ; if ( val < 0 ) val += MOD ; } Int ( LL _val ) : val ( _val ) { _val %= MOD ; if ( _val < 0 ) _val += MOD ; val = _val ; } Int & operator += ( const int & rhs ) { INC ( val , rhs ); return * this ; } Int operator \+ ( const int & rhs ) const { return sum ( val , rhs ); } Int & operator -= ( const int & rhs ) { DEC ( val , rhs ); return * this ; } Int operator \- ( const int & rhs ) const { return dff ( val , rhs ); } Int & operator *= ( const int & rhs ) { MUL ( val , rhs ); return * this ; } Int operator * ( const int & rhs ) const { return pdt ( val , rhs ); } Int & operator /= ( const int & rhs ) { DIV ( val , rhs ); return * this ; } Int operator / ( const int & rhs ) const { return qtt ( val , rhs ); } Int operator \- () const { return MOD \- * this ; } }; } // namespace NT using namespace NT ; constexpr int N = int ( 1e3 ) \+ 9 ; Int binom [ N ][ N ], C [ N ], E [ N ], B [ N ], B1 [ N ], G [ N ]; int n ; void ln ( Int C [], Int G []) { for ( int i = 1 ; i <= n ; ++ i ) { C [ i ] = G [ i ]; for ( int j = 1 ; j <= i \- 1 ; ++ j ) C [ i ] -= binom [ i \- 1 ][ j \- 1 ] * C [ j ] * G [ i \- j ]; } } void exp ( Int G [], Int C []) { for ( int i = 1 ; i <= n ; ++ i ) { G [ i ] = C [ i ]; for ( int j = 1 ; j <= i \- 1 ; ++ j ) G [ i ] += binom [ i \- 1 ][ j \- 1 ] * C [ j ] * G [ i \- j ]; } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); n = 1000 ; for ( int i = 0 ; i < n \+ 1 ; ++ i ) { binom [ i ][ 0 ] = 1 ; for ( int j = 0 ; j < i ; ++ j ) binom [ i ][ j \+ 1 ] = binom [ i \- 1 ][ j ] \+ binom [ i \- 1 ][ j \+ 1 ]; } for ( int i = 1 ; i <= n ; ++ i ) G [ i ] = pow ( 2 , binom [ i ][ 2 ]); ln ( C , G ); for ( int i = 1 ; i <= n ; ++ i ) G [ i ] = pow ( 2 , binom [ i \- 1 ][ 2 ]); ln ( E , G ); for ( int i = 1 ; i <= n ; ++ i ) { G [ i ] = 0 ; for ( int j = 0 ; j < i \+ 1 ; ++ j ) G [ i ] += binom [ i ][ j ] * pow ( 2 , j * ( i \- j )); } ln ( B1 , G ); for ( int i = 1 ; i <= n ; ++ i ) B1 [ i ] /= 2 ; exp ( B , B1 ); int T ; cin >> T ; while ( T \-- ) { cin >> n ; cout << "Connected: " << C [ n ] << '\n' << "Eulerian: " << E [ n ] << '\n' << "Bipartite: " << B [ n ] << " \n\n " ; } } ```   
---|---  
  
### 习题

  * [UOJ Goodbye Jihai D. 新年的追逐战](https://uoj.ac/contest/50/problem/498)
  * [BZOJ 3864. 大朋友和多叉树](https://hydro.ac/p/bzoj-P3864)
  * [BZOJ 2863. 愤怒的元首](https://hydro.ac/p/bzoj-P2863)
  * [Luogu P6295. 有标号 DAG 计数](https://www.luogu.com.cn/problem/P6295)
  * [LOJ 6569. 仙人掌计数](https://loj.ac/p/6569)
  * [LOJ 6570. 毛毛虫计数](https://loj.ac/p/6570)
  * [Luogu P5434. 有标号荒漠计数](https://www.luogu.com.cn/problem/P5434)
  * [Luogu P3343. [ZJOI2015] 地震后的幻想乡](https://www.luogu.com.cn/problem/P3343)
  * [HDU 5279. YJC plays Minecraft](https://acm.hdu.edu.cn/showproblem.php?pid=5279)
  * [Luogu P7364. 有标号二分图计数](https://www.luogu.com.cn/problem/P7364)
  * [Luogu P5827. 点双连通图计数](https://www.luogu.com.cn/problem/P5827)
  * [Luogu P5827. 边双连通图计数](https://www.luogu.com.cn/problem/P5828)
  * [Luogu P6596. How Many of Them](https://www.luogu.com.cn/problem/P6596)
  * [Luogu U152448. 有标号强连通图计数](https://www.luogu.com.cn/problem/U152448)
  * [Project Euler 434. Rigid graphs](https://projecteuler.net/problem=434)

## Riddell's Formula

上述关于 EGF 的 exp 的用法，有时又被称作 Riddell's formula for labeled graphs，生成函数的 [欧拉变换](../../poly/symbolic-method/#%E9%9B%86%E5%90%88%E7%9A%84-multiset-%E6%9E%84%E9%80%A0)，有时也被称为 Riddell's formula for unlabeled graphs，后者最早出现在欧拉对分拆数的研究中，除了解决图论计数问题之外，也在完全背包问题中出现．

对于给定序列 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，和对应的 OGF 𝐴(𝑥)A(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义 𝐴(𝑥)A(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的欧拉变换为：

E(𝐴(𝑥))=∏𝑖(1−𝑥𝑖)−𝑎𝑖=exp⁡(∑𝑖𝐴(𝑥𝑖)𝑖)E(A(x))=∏i(1−xi)−ai=exp⁡(∑iA(xi)i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 E(𝐴(𝑥))E(A(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的各项系数为 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义辅助数组 𝑐𝑖 =∑𝑑|𝑛𝑑𝑎𝑑ci=∑d|ndad![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有递推公式

𝑛𝑏𝑛=𝑐𝑛+𝑛−1∑𝑖=1𝑐𝑖𝑏𝑛−𝑖nbn=cn+∑i=1n−1cibn−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 无标号树

### 例题「SPOJ PT07D」Let us count 1 2 3

例题 [「SPOJ PT07D」Let us count 1 2 3](https://www.spoj.com/problems/PT07D/)

题目大意：求有 n 个结点的分别满足下列性质的树的方案数．

  * 有标号有根树 [A000169](https://oeis.org/A000169)．
  * 有标号无根树 [A000272](https://oeis.org/A000272)．
  * 无标号有根树 [A000081](https://oeis.org/A000081)．
  * 无标号无根树 [A000055](https://oeis.org/A000055)．

#### 有根树

有标号情况以在前文中解决，下面考察无标号有根树，设其 OGF 为 𝐹(𝑥)F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，应用欧拉变换，可得：

𝐹(𝑥)=𝑥E(𝐹(𝑥))F(x)=xE(F(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

取出系数即可．

#### 无根树

考虑容斥，我们用有根树的方案中减去根不是重心的方案，并对 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的奇偶性进行讨论．

当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇数时：

必然存在一棵子树大小 ≥⌈𝑛2⌉≥⌈n2⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，枚举这棵子树的大小有．

𝑔𝑛=𝑓𝑛−𝑛−1∑𝑖=⌈𝑛2⌉𝑓𝑖𝑓𝑛−𝑖gn=fn−∑i=⌈n2⌉n−1fifn−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶数时：

注意到当有两个重心的情况时，上面的过程只会减去一次，因此还需要减去

𝑔𝑛=𝑓𝑛−𝑛−1∑𝑖=⌈𝑛2⌉𝑓𝑖𝑓𝑛−𝑖−(𝑓𝑛22)gn=fn−∑i=⌈n2⌉n−1fifn−i−(fn22)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 例题「Luogu P5900」无标号无根树计数

例题 [「Luogu P5900」无标号无根树计数](https://www.luogu.com.cn/problem/P5900)

题目大意：求有 n 个结点的无标号无根树的方案数（𝑛 ≤200000n≤200000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

对于数据范围更大的情况，做法同理，欧拉变换后使用多项式模板即可．

## 无标号简单图

### 例题「SGU 282. Isomorphism」Isomorphism

例题 [「SGU 282. Isomorphism」Isomorphism](https://codeforces.com/problemsets/acmsguru/problem/99999/282)

题目大意：求有 n 个结点的无标号完全图的边进行 m 染色的方案数．

注意到当 m = 2 时，所求对象就是无标号简单图 [A000088](https://oeis.org/A000088)，考察波利亚计数定理，

1|𝐺|∑𝑔∈𝐺𝑚𝑐(𝑔)1|G|∑g∈Gmc(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

本题中置换群 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为顶点的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶对称群生成的边集置换群，但暴力做法的枚举量为 𝑂(𝑛!)O(n!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，无法通过此题．

考虑根据按照置换的循环结构进行分类，每种循环结构对应一种数的分拆，我们用 dfs() 生成分拆，那么问题即转化为求每一种分拆 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所对应的置换数目 𝑤(𝑝)w(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和每一类置换中的循环个数 𝑐(𝑝)c(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，答案为

1|𝐺|∑𝑝∈𝑃𝑤(𝑝)𝑚𝑐(𝑝)1|G|∑p∈Pw(p)mc(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑 𝑤(𝑝)w(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每一个分拆对应一个循环排列，同时同一种大小的分拆之间的顺序无关，因而我们有：

𝑤(𝑝)=𝑛!∏𝑖(𝑝𝑖)∏𝑖(𝑞𝑖!)w(p)=n!∏i(pi)∏i(qi!)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里 𝑞𝑖qi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示大小为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的分拆在 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中出现的次数．

考虑 𝑐(𝑝)c(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所影响的点集的循环即为 |𝑝||p|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但题目考察的是边染色，所以还需要考察点置换所生成的边置换，

如果一条边关联的顶点处在同一个循环内，设该循环大小为 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么边所生成的循环数恰好为 ⌊𝑝𝑖2⌋⌊pi2⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如果一条边关联的顶点处在两个不同的循环中，设分别为 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7),𝑝𝑗pj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每个循环节的长度均为 lcm⁡(𝑝𝑖,𝑝𝑗)lcm⁡(pi,pj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因而边所生成的循环数恰好为 𝑝𝑖𝑝𝑗lcm⁡(𝑝𝑖,𝑝𝑗) =gcd(𝑝𝑖,𝑝𝑗)pipjlcm⁡(pi,pj)=gcd(pi,pj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 ``` |  ```text #include <iostream> #include <vector> using namespace std ; using LL = long long ; int MOD = int ( 1e9 ) \+ 7 ; namespace NT { void INC ( int & a , int b ) { a += b ; if ( a >= MOD ) a -= MOD ; } int sum ( int a , int b ) { a += b ; if ( a >= MOD ) a -= MOD ; return a ; } void DEC ( int & a , int b ) { a -= b ; if ( a < 0 ) a += MOD ; } int dff ( int a , int b ) { a -= b ; if ( a < 0 ) a += MOD ; return a ; } void MUL ( int & a , int b ) { a = ( LL ) a * b % MOD ; } int pdt ( int a , int b ) { return ( LL ) a * b % MOD ; } int _I ( int b ) { int a = MOD , x1 = 0 , x2 = 1 , q ; while ( 1 ) { q = a / b , a %= b ; if ( ! a ) return x2 ; DEC ( x1 , pdt ( q , x2 )); q = b / a , b %= a ; if ( ! b ) return x1 ; DEC ( x2 , pdt ( q , x1 )); } } void DIV ( int & a , int b ) { MUL ( a , _I ( b )); } int qtt ( int a , int b ) { return pdt ( a , _I ( b )); } int pow ( int a , LL b ) { int c ( 1 ); while ( b ) { if ( b & 1 ) MUL ( c , a ); MUL ( a , a ), b >>= 1 ; } return c ; } template < class T > T pow ( T a , LL b ) { T c ( 1 ); while ( b ) { if ( b & 1 ) c *= a ; a *= a , b >>= 1 ; } return c ; } template < class T > T pow ( T a , int b ) { return pow ( a , ( LL ) b ); } struct Int { int val ; operator int () const { return val ; } Int ( int _val = 0 ) : val ( _val ) { val %= MOD ; if ( val < 0 ) val += MOD ; } Int ( LL _val ) : val ( _val ) { _val %= MOD ; if ( _val < 0 ) _val += MOD ; val = _val ; } Int & operator += ( const int & rhs ) { INC ( val , rhs ); return * this ; } Int operator \+ ( const int & rhs ) const { return sum ( val , rhs ); } Int & operator -= ( const int & rhs ) { DEC ( val , rhs ); return * this ; } Int operator \- ( const int & rhs ) const { return dff ( val , rhs ); } Int & operator *= ( const int & rhs ) { MUL ( val , rhs ); return * this ; } Int operator * ( const int & rhs ) const { return pdt ( val , rhs ); } Int & operator /= ( const int & rhs ) { DIV ( val , rhs ); return * this ; } Int operator / ( const int & rhs ) const { return qtt ( val , rhs ); } Int operator \- () const { return MOD \- * this ; } }; } // namespace NT using namespace NT ; constexpr int N = int ( 5e1 ) \+ 9 ; Int Fact [ N ]; vector < vector < int >> Partition ; vector < int > cur ; int n , m ; void gen ( int n = :: n , int s = 1 ) { if ( ! n ) { Partition . push_back ( cur ); } else if ( n >= s ) { cur . push_back ( s ); gen ( n \- s , s ); cur . pop_back (); gen ( n , s \+ 1 ); } } Int w ( const vector < int > P ) { Int z = Fact [ n ]; int c = 0 , l = P . front (); for ( auto p : P ) { z /= p ; if ( p != l ) { z /= Fact [ c ]; l = p ; c = 1 ; } else { ++ c ; } } z /= Fact [ c ]; return z ; } int gcd ( int x , int y ) { return y ? gcd ( y , x % y ) : x ; } int c ( const vector < int > P ) { int z = 0 ; for ( int i = 0 ; i < P . size (); ++ i ) { z += P [ i ] / 2 ; for ( int j = 0 ; j < i ; ++ j ) z += gcd ( P [ i ], P [ j ]); } return z ; } int main () { cin >> n >> m >> MOD ; Fact [ 0 ] = 1 ; for ( int i = 1 ; i <= n ; ++ i ) Fact [ i ] = Fact [ i \- 1 ] * i ; gen (); Int res = 0 ; for ( auto P : Partition ) { res += w ( P ) * pow ( m , c ( P )); } res /= Fact [ n ]; cout << res << endl ; } ```   
---|---  
  
## 习题

  * [CodeForces 438 E. The Child and Binary Tree](https://codeforces.com/problemset/problem/438/E)
  * [Luogu P5448. [THUPC2018] 好图计数](https://www.luogu.com.cn/problem/P5448)
  * [Luogu P5818. [JSOI2011] 同分异构体计数](https://www.luogu.com.cn/problem/P5818)
  * [Luogu P6597. 烯烃计数](https://www.luogu.com.cn/problem/P6597)
  * [Luogu P6598. 烷烃计数](https://www.luogu.com.cn/problem/P6598)
  * [Luogu P4128. [SHOI2006] 有色图](https://www.luogu.com.cn/problem/P4128)
  * [Luogu P4727. [HNOI2009] 图的同构计数](https://www.luogu.com.cn/problem/P4727)
  * [AtCoder Beginner Contest 222 H. Binary Tree](https://atcoder.jp/contests/abc222/tasks/abc222_h)
  * [AtCoder Beginner Contest 284 Ex. Count Unlabeled Graphs](https://atcoder.jp/contests/abc284/tasks/abc284_h)
  * [Luogu P4708. 画画](https://www.luogu.com.cn/problem/P4708)
  * [Luogu P7592. 数树（2021 CoE-II E）](https://www.luogu.com.cn/problem/P7592)
  * [Luogu P5206. [WC2019] 数树](https://www.luogu.com.cn/problem/P5206)

## 参考资料与注释

  1. [WC2015, 顾昱洲营员交流资料 Graphical Enumeration](https://github.com/lychees/ACM-Training/blob/master/Note/%E5%86%AC%E4%BB%A4%E8%90%A5/2015/%E9%A1%BE%E6%98%B1%E6%B4%B2%E8%90%A5%E5%91%98%E4%BA%A4%E6%B5%81%E8%B5%84%E6%96%99%20Graphical%20Enumeration.pdf)
  2. [WC2019, 生成函数，多项式算法与图的计数](https://github.com/lychees/ACM-Training/tree/master/Note/%E5%86%AC%E4%BB%A4%E8%90%A5/2019/d4)
  3. [Counting labeled graphs - Algorithms for Competitive Programming](https://cp-algorithms.com/combinatorics/counting_labeled_graphs.html)
  4. [Graphical Enumeration Paperback, Frank Harary, Edgar M. Palmer](https://github.com/lychees/ACM-Training/blob/master/Note/Book/)
  5. [The encyclopedia of integer sequences, N. J. A. Sloane, Simon Plouffe](https://github.com/lychees/ACM-Training/blob/master/Note/Book/The%20encyclopedia%20of%20integer%20sequences%20\\\\\(N.%20J.A.%20Sloane%2C%20Simon%20Plouffe\\\\\).pdf)
  6. [Combinatorial Problems and Exercises, László Lovász](https://github.com/lychees/ACM-Training/blob/master/Note/Book/Combinatorial%20Problems%20and%20Exercises_L%C3%A1szl%C3%B3%20Lov%C3%A1sz.pdf)
  7. [Graph Theory and Additive Combinatorics](https://yufeizhao.com/gtacbook/)

* * *

  1. 也许无标号二叉树是一个反例，在结构简单的情况下，对应的置换群是恒等群（Identity Group），此时有标号版本可以直接通过乘以 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到． ↩

  2. [粉兔的 blog](https://www.luogu.com.cn/blog/PinkRabbit/solution-sp4420) 告诉我们，这个序列也可以使用 [Chirp Z-Transform](../../poly/czt/) 优化． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/graph-enumeration.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/graph-enumeration.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [lychees](https://github.com/lychees), [c-forrest](https://github.com/c-forrest), [ComeIntoCalm](https://github.com/ComeIntoCalm), [GoodCoder666](https://github.com/GoodCoder666), [HeRaNO](https://github.com/HeRaNO), [megakite](https://github.com/megakite), [Molmin](https://github.com/Molmin)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
