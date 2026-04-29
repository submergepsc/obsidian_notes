# 矩阵 - OI Wiki

- Source: https://oi-wiki.org/math/linear-algebra/matrix/

# 矩阵

本文介绍线性代数中一个非常重要的内容——矩阵（Matrix），主要讲解矩阵的性质、运算，以及矩阵乘法的一些应用．

## 向量与矩阵

在线性代数中，向量分为列向量和行向量．

Warning

在中国台湾地区关于「列」与「行」的翻译，恰好与中国大陆地区相反．在 **OI Wiki** 按照中国大陆地区的习惯，采用列（column）与行（row）的翻译．

线性代数的主要研究对象是列向量，约定使用粗体小写字母表示列向量．在用到大量向量与矩阵的线性代数中，不引起混淆的情况下，在手写时，字母上方的向量记号可以省略不写．

向量也是特殊的矩阵．如果想要表示行向量，需要在粗体小写字母右上方写转置记号．行向量在线性代数中一般表示方程．

## 引入

矩阵的引入来自于线性方程组．与向量类似，矩阵体现了一种对数据「打包处理」的思想．

例如，将线性方程组：

⎧{ {⎨{ {⎩7𝑥1+8𝑥2+9𝑥3=134𝑥1+5𝑥2+6𝑥3=12𝑥1+2𝑥2+3𝑥3=11{7x1+8x2+9x3=134x1+5x2+6x3=12x1+2x2+3x3=11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

一般用圆括号或方括号表示矩阵．将上述系数抽出来，写成矩阵乘法的形式：

⎛⎜ ⎜ ⎜⎝789456123⎞⎟ ⎟ ⎟⎠⎛⎜ ⎜ ⎜⎝𝑥1𝑥2𝑥3⎞⎟ ⎟ ⎟⎠=⎛⎜ ⎜ ⎜⎝131211⎞⎟ ⎟ ⎟⎠(789456123)(x1x2x3)=(131211)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

简记为：

𝐴𝑥=𝑏Ax=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即未知数列向量 x，左乘一个矩阵 A，得到列向量 b．这个式子可以认为是线性代数的基本形式．

线性代数主要研究的运算模型是内积．内积是先相乘再相加，是行向量左乘列向量，得到一个数的过程．

矩阵乘法是内积的拓展．矩阵乘法等价于左边矩阵抽出一行，与右边矩阵抽出一列进行内积，得到结果矩阵的对应元素，口诀「左行右列」．

当研究对象是右边的列向量时，矩阵乘法相当于对列向量进行左乘．在左乘的观点下，矩阵就是对列向量的变换，将矩阵乘法中右边矩阵的每一个列向量进行变换，对应地得到结果矩阵中每一个列向量．

矩阵可以对一个列向量进行变换，也可以对一组列向量进行「打包」变换，甚至可以对整个空间——即全体列向量进行变换．当矩阵被视为对整个空间变换的时候，也就脱离了空间，成为了纯粹变换的存在．

## 定义

对于矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，主对角线是指 𝐴𝑖,𝑖Ai,i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素．

一般用 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来表示单位矩阵，就是主对角线上为 1，其余位置为 0．

### 同型矩阵

两个矩阵，行数与列数对应相同，称为同型矩阵．

### 方阵

行数等于列数的矩阵称为方阵．方阵是一种特殊的矩阵．对于「𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶矩阵」的习惯表述，实际上讲的是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶方阵．阶数相同的方阵为同型矩阵．

研究方程组、向量组、矩阵的秩的时候，使用一般的矩阵．研究特征值和特征向量、二次型的时候，使用方阵．

#### 主对角线

方阵中行数等于列数的元素构成主对角线．

#### 对称矩阵

如果方阵的元素关于主对角线对称，即对于任意的 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的元素与 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的元素相等，则将方阵称为对称矩阵．

#### 对角矩阵

主对角线之外的元素均为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方阵称为对角矩阵，一般记作：

diag⁡{𝜆1,⋯,𝜆𝑛}diag⁡{λ1,⋯,λn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

式中的 𝜆1,⋯,𝜆𝑛λ1,⋯,λn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是主对角线上的元素．

对角矩阵是对称矩阵．

如果对角矩阵的元素均为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称为单位矩阵，记为 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．只要乘法可以进行，无论形状，任何矩阵乘单位矩阵仍然保持不变．

#### 三角矩阵

如果方阵主对角线左下方的元素均为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称为上三角矩阵．如果方阵主对角线右上方的元素均为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称为下三角矩阵．

两个上（下）三角矩阵的乘积仍然是上（下）三角矩阵．如果对角线元素均非 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则上（下）三角矩阵可逆，逆也是上（下）三角矩阵．

#### 单位三角矩阵

如果上三角矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对角线全为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是单位上三角矩阵．如果下三角矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对角线全为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是单位下三角矩阵．

两个单位上（下）三角矩阵的乘积仍然是单位上（下）三角矩阵，单位上（下）三角矩阵的逆也是单位上（下）三角矩阵．

## 运算

### 矩阵的线性运算

矩阵的线性运算分为加减法与数乘，它们均为逐个元素进行．只有同型矩阵之间可以对应相加减．

### 矩阵的转置

矩阵的转置，就是在矩阵的右上角写上转置「T」记号，表示将矩阵的行与列互换．

对称矩阵转置前后保持不变．

### 矩阵乘法

矩阵的乘法是向量内积的推广．

矩阵相乘只有在第一个矩阵的列数和第二个矩阵的行数相同时才有意义．

设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑃 ×𝑀P×M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵，𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑀 ×𝑄M×Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵，设矩阵 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘积，

其中矩阵 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列元素可以表示为：

𝐶𝑖,𝑗=𝑀∑𝑘=1𝐴𝑖,𝑘𝐵𝑘,𝑗Ci,j=∑k=1MAi,kBk,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在矩阵乘法中，结果 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的数，就是由矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数与矩阵 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数分别 **相乘再相加** 得到的．这里的 **相乘再相加** ，就是向量的内积．乘积矩阵中第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的数恰好是乘数矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个行向量与乘数矩阵 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个列向量的内积，口诀为 **左行右列** ．

线性代数研究的向量多为列向量，根据这样的对矩阵乘法的定义方法，经常研究对列向量左乘一个矩阵的左乘运算，同时也可以在这里看出「打包处理」的思想，同时处理很多个向量内积．

矩阵乘法满足结合律，不满足一般的交换律．

利用结合律，矩阵乘法可以利用 [快速幂](../../binary-exponentiation/) 的思想来优化．

在比赛中，由于线性递推式可以表示成矩阵乘法的形式，也通常用矩阵快速幂来求线性递推数列的某一项．

#### 优化

首先对于比较小的矩阵，可以考虑直接手动展开循环以减小常数．

可以重新排列循环以提高空间局部性，这样的优化不会改变矩阵乘法的时间复杂度，但是会得到常数级别的提升．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` |  ```text // 以下文的参考代码为例 mat operator * ( const mat & T ) const { mat res ; for ( int i = 0 ; i < sz ; ++ i ) for ( int j = 0 ; j < sz ; ++ j ) for ( int k = 0 ; k < sz ; ++ k ) { res . a [ i ][ j ] += mul ( a [ i ][ k ], T . a [ k ][ j ]); res . a [ i ][ j ] %= MOD ; } return res ; } // 不如 mat operator * ( const mat & T ) const { mat res ; int r ; for ( int i = 0 ; i < sz ; ++ i ) for ( int k = 0 ; k < sz ; ++ k ) { r = a [ i ][ k ]; for ( int j = 0 ; j < sz ; ++ j ) res . a [ i ][ j ] += T . a [ k ][ j ] * r , res . a [ i ][ j ] %= MOD ; } return res ; } ```   
---|---  
  
### 方阵的逆

方阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆矩阵 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是使得 𝐴 ×𝑃 =𝐼A×P=I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵．

逆矩阵不一定存在．如果存在，可以使用 [高斯消元](../../numerical/gauss/) 进行求解．

### 方阵的行列式

行列式是方阵的一种运算．

## 参考代码

一般来说，可以用一个二维数组来模拟矩阵．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 ``` |  ```text struct mat { LL a [ sz ][ sz ]; mat () { memset ( a , 0 , sizeof a ); } mat operator \- ( const mat & T ) const { mat res ; for ( int i = 0 ; i < sz ; ++ i ) for ( int j = 0 ; j < sz ; ++ j ) { res . a [ i ][ j ] = ( a [ i ][ j ] \- T . a [ i ][ j ]) % MOD ; } return res ; } mat operator \+ ( const mat & T ) const { mat res ; for ( int i = 0 ; i < sz ; ++ i ) for ( int j = 0 ; j < sz ; ++ j ) { res . a [ i ][ j ] = ( a [ i ][ j ] \+ T . a [ i ][ j ]) % MOD ; } return res ; } mat operator * ( const mat & T ) const { mat res ; int r ; for ( int i = 0 ; i < sz ; ++ i ) for ( int k = 0 ; k < sz ; ++ k ) { r = a [ i ][ k ]; for ( int j = 0 ; j < sz ; ++ j ) res . a [ i ][ j ] += T . a [ k ][ j ] * r , res . a [ i ][ j ] %= MOD ; } return res ; } mat operator ^ ( LL x ) const { mat res , bas ; for ( int i = 0 ; i < sz ; ++ i ) res . a [ i ][ i ] = 1 ; for ( int i = 0 ; i < sz ; ++ i ) for ( int j = 0 ; j < sz ; ++ j ) bas . a [ i ][ j ] = a [ i ][ j ] % MOD ; while ( x ) { if ( x & 1 ) res = res * bas ; bas = bas * bas ; x >>= 1 ; } return res ; } }; ```   
---|---  
  
## 看待线性方程组的两种视角

看待矩阵 A，或者变换 A，有两种视角．

第一种观点：按行看，观察 A 的每一行．这样一来把 A 看作方程组．于是就有了消元法解方程的过程．

第二种观点：按列看，观察 A 的每一列．A 本身也是由列向量构成的．此时相当于把变换 A 本身看成了列向量组，而 x 是未知数系数，思考 A 当中的这组列向量能不能配上未知数，凑出列向量 b．

例如，文章开头的例子变为：

⎛⎜ ⎜ ⎜⎝741⎞⎟ ⎟ ⎟⎠𝑥1+⎛⎜ ⎜ ⎜⎝852⎞⎟ ⎟ ⎟⎠𝑥2+⎛⎜ ⎜ ⎜⎝963⎞⎟ ⎟ ⎟⎠𝑥3=⎛⎜ ⎜ ⎜⎝131211⎞⎟ ⎟ ⎟⎠(741)x1+(852)x2+(963)x3=(131211)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

解方程变为研究，是否可以通过调整三个系数 x，使得给定的三个基向量能够凑出结果的向量．

按列看比按行看更新颖．在按列看的视角下，可以研究线性无关与线性相关．

## 矩阵乘法的应用

### 矩阵加速递推

以 [斐波那契数列（Fibonacci Sequence）](../../combinatorics/fibonacci/) 为例．在斐波那契数列当中，𝐹1 =𝐹2 =1F1=F2=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐹𝑖 =𝐹𝑖−1 +𝐹𝑖−2(𝑖 ≥3)Fi=Fi−1+Fi−2(i≥3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如果有一道题目让你求斐波那契数列第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项的值，最简单的方法莫过于直接递推了．但是如果 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的范围达到了 10181018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别，递推就不行了，此时我们可以考虑矩阵加速递推．

根据斐波那契数列 [递推公式的矩阵形式](../../combinatorics/fibonacci/#矩阵形式):

[𝐹𝑛−1𝐹𝑛−2][1110]=[𝐹𝑛𝐹𝑛−1][Fn−1Fn−2][1110]=[FnFn−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定义初始矩阵 ans =[𝐹2𝐹1] =[11],base =[1110]ans=[F2F1]=[11],base=[1110]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．那么，𝐹𝑛Fn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就等于 ansbase𝑛−2ansbasen−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这个矩阵的第一行第一列元素，也就是 [11][1110]𝑛−2[11][1110]n−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第一行第一列元素．

注意

矩阵乘法不满足交换律，所以一定不能写成 [1110]𝑛−2[11][1110]n−2[11]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第一行第一列元素．另外，对于 𝑛 ≤2n≤2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，直接输出 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可，不需要执行矩阵快速幂．

为什么要乘上 basebase![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵的 𝑛 −2n−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次方而不是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次方呢？因为 𝐹1,𝐹2F1,F2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是不需要进行矩阵乘法就能求的．也就是说，如果只进行一次乘法，就已经求出 𝐹3F3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了．如果还不是很理解为什么幂是 𝑛 −2n−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，建议手算一下．

下面是求斐波那契数列第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项对 109 +7109+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模的示例代码（核心部分）．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` |  ```text constexpr int mod = 1000000007 ; struct Matrix { int a [ 3 ][ 3 ]; Matrix () { memset ( a , 0 , sizeof a ); } Matrix operator * ( const Matrix & b ) const { Matrix res ; for ( int i = 1 ; i <= 2 ; ++ i ) for ( int j = 1 ; j <= 2 ; ++ j ) for ( int k = 1 ; k <= 2 ; ++ k ) res . a [ i ][ j ] = ( res . a [ i ][ j ] \+ a [ i ][ k ] * b . a [ k ][ j ]) % mod ; return res ; } } ans , base ; void init () { base . a [ 1 ][ 1 ] = base . a [ 1 ][ 2 ] = base . a [ 2 ][ 1 ] = 1 ; ans . a [ 1 ][ 1 ] = ans . a [ 1 ][ 2 ] = 1 ; } void qpow ( int b ) { while ( b ) { if ( b & 1 ) ans = ans * base ; base = base * base ; b >>= 1 ; } } int main () { int n = read (); if ( n <= 2 ) return puts ( "1" ), 0 ; init (); qpow ( n \- 2 ); println ( ans . a [ 1 ][ 1 ] % mod ); } ```   
---|---  
  
这是一个稍微复杂一些的例子．

𝑓1=𝑓2=0𝑓𝑛=7𝑓𝑛−1+6𝑓𝑛−2+5𝑛+4×3𝑛f1=f2=0fn=7fn−1+6fn−2+5n+4×3n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们发现，𝑓𝑛fn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓𝑛−1,𝑓𝑛−2,𝑛fn−1,fn−2,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有关，于是考虑构造一个矩阵描述状态．

但是发现如果矩阵仅有这三个元素 [𝑓𝑛𝑓𝑛−1𝑛][fnfn−1n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是难以构造出转移方程的，因为乘方运算和 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 无法用矩阵描述．

于是考虑构造一个更大的矩阵．

[𝑓𝑛𝑓𝑛−1𝑛3𝑛1][fnfn−1n3n1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们希望构造一个递推矩阵可以转移到

[𝑓𝑛+1𝑓𝑛𝑛+13𝑛+11][fn+1fnn+13n+11]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

转移矩阵即为

⎡⎢ ⎢ ⎢ ⎢ ⎢⎣71000600005010012003050101⎤⎥ ⎥ ⎥ ⎥ ⎥⎦[71000600005010012003050101]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 矩阵表达修改

[「THUSCH 2017」大魔法师](https://loj.ac/p/2980)

大魔法师小 L 制作了 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个魔力水晶球，每个水晶球有水、火、土三个属性的能量值．小 L 把这 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个水晶球在地上从前向后排成一行，然后开始今天的魔法表演．

我们用 𝐴𝑖, 𝐵𝑖, 𝐶𝑖Ai, Bi, Ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别表示从前向后第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个水晶球（下标从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始）的水、火、土的能量值．

小 L 计划施展 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次魔法．每次，他会选择一个区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后施展以下 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大类、77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种魔法之一：

  1. 魔力激发：令区间里每个水晶球中 **特定属性** 的能量爆发，从而使另一个 **特定属性** 的能量增强．具体来说，有以下三种可能的表现形式：

     * 火元素激发水元素能量：令 𝐴𝑖 =𝐴𝑖 +𝐵𝑖Ai=Ai+Bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
     * 土元素激发火元素能量：令 𝐵𝑖 =𝐵𝑖 +𝐶𝑖Bi=Bi+Ci![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
     * 水元素激发土元素能量：令 𝐶𝑖 =𝐶𝑖 +𝐴𝑖Ci=Ci+Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**需要注意的是，增强一种属性的能量并不会改变另一种属性的能量，例如 𝐴𝑖 =𝐴𝑖 +𝐵𝑖Ai=Ai+Bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并不会使 𝐵𝑖Bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 增加或减少．**

  2. 魔力增强：小 L 挥舞法杖，消耗自身 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 点法力值，来改变区间里每个水晶球的 **特定属性** 的能量．具体来说，有以下三种可能的表现形式：

     * 火元素能量定值增强：令 𝐴𝑖 =𝐴𝑖 +𝑣Ai=Ai+v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
     * 水元素能量翻倍增强：令 𝐵𝑖 =𝐵𝑖 ⋅𝑣Bi=Bi⋅v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
     * 土元素能量吸收融合：令 𝐶𝑖 =𝑣Ci=v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 魔力释放：小 L 将区间里所有水晶球的能量聚集在一起，融合成一个新的水晶球，然后送给场外观众．生成的水晶球每种属性的能量值等于区间内所有水晶球对应能量值的代数和．**需要注意的是，魔力释放的过程不会真正改变区间内水晶球的能量** ．

值得一提的是，小 L 制造和融合的水晶球的原材料都是定制版的 OI 工厂水晶，所以这些水晶球有一个能量阈值 998244353998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．当水晶球中某种属性的能量值大于等于这个阈值时，能量值会自动对阈值取模，从而避免水晶球爆炸．

小 W 为小 L（唯一的）观众，围观了整个表演，并且收到了小 L 在表演中融合的每个水晶球．小 W 想知道，这些水晶球蕴涵的三种属性的能量值分别是多少．

由于矩阵的结合律和分配律成立，单点修改可以自然地推广到区间，即推出矩阵后直接用线段树维护区间矩阵乘积即可．

下面将举几个例子．

𝐴𝑖 =𝐴𝑖 +𝑣Ai=Ai+v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的转移

[𝐴𝐵𝐶1]⎡⎢ ⎢ ⎢ ⎢⎣100001000010𝑣001⎤⎥ ⎥ ⎥ ⎥⎦=[𝐴+𝑣𝐵𝐶1][ABC1][100001000010v001]=[A+vBC1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝐵𝑖 =𝐵𝑖 ⋅𝑣Bi=Bi⋅v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的转移

[𝐴𝐵𝐶1]⎡⎢ ⎢ ⎢ ⎢⎣10000𝑣0000100001⎤⎥ ⎥ ⎥ ⎥⎦=[𝐴𝐵⋅𝑣𝐶1][ABC1][10000v0000100001]=[AB⋅vC1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)[「LibreOJ 6208」树上询问](https://loj.ac/p/6208)

有一棵 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 节点的树，根为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号节点．每个节点有两个权值 𝑘𝑖,𝑡𝑖ki,ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，初始值均为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

给出三种操作：

  1. Add⁡(𝑥,𝑑)Add⁡(x,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 操作：将 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到根的路径上所有点的 𝑘𝑖 ←𝑘𝑖 +𝑑ki←ki+d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. Mul⁡(𝑥,𝑑)Mul⁡(x,d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 操作：将 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到根的路径上所有点的 𝑡𝑖 ←𝑡𝑖 +𝑑 ×𝑘𝑖ti←ti+d×ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  3. Query⁡(𝑥)Query⁡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 操作：询问点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的权值 𝑡𝑥tx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝑛, 𝑚 ≤100000, −10 ≤𝑑 ≤10n, m≤100000, −10≤d≤10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若直接思考，下放操作和维护信息并不是很好想．但是矩阵可以轻松地表达．

[𝑘𝑡1]⎡⎢ ⎢⎣100010𝑑01⎤⎥ ⎥⎦=[𝑘+𝑑𝑡1][𝑘𝑡1]⎡⎢ ⎢⎣1𝑑0010001⎤⎥ ⎥⎦=[𝑘𝑡+𝑑×𝑘1][kt1][100010d01]=[k+dt1][kt1][1d0010001]=[kt+d×k1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 定长路径统计

问题描述

给一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶有向图，每条边的边权均为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后给一个整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，你的任务是对于所有点对 (𝑢,𝑣)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求出从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径的数量（不一定是简单路径，即路径上的点或者边可能走多次）．

我们将这个图用邻接矩阵 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（对于图中的边 (𝑢 →𝑣)(u→v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝐺[𝑢,𝑣] =1G[u,v]=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其余为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵；如果有重边，则设 𝐺[𝑢,𝑣]G[u,v]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为重边的数量）表示这个有向图．下述算法同样适用于图有自环的情况．

显然，该邻接矩阵对应 𝑘 =1k=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时的答案．

假设我们知道长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径条数构成的矩阵，记为矩阵 𝐶𝑘Ck![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们想求 𝐶𝑘+1Ck+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．显然有 DP 转移方程

𝐶𝑘+1[𝑖,𝑗]=𝑛∑𝑝=1𝐶𝑘[𝑖,𝑝]⋅𝐺[𝑝,𝑗]Ck+1[i,j]=∑p=1nCk[i,p]⋅G[p,j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们可以把它看作矩阵乘法的运算，于是上述转移可以描述为

𝐶𝑘+1=𝐶𝑘⋅𝐺Ck+1=Ck⋅G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么把这个递推式展开可以得到

𝐶𝑘=𝐺⋅𝐺⋯𝐺⏟𝑘 次=𝐺𝑘Ck=G⋅G⋯G⏟k 次=Gk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

要计算这个矩阵幂，我们可以使用快速幂（二进制取幂）的思想，在 𝑂(𝑛3log⁡𝑘)O(n3log⁡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度内计算结果．

### 定长最短路

问题描述

给你一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶加权有向图和一个整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于每个点对 (𝑢,𝑣)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 找到从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的恰好包含 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 条边的最短路的长度．（不一定是简单路径，即路径上的点或者边可能走多次）

我们仍构造这个图的邻接矩阵 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐺[𝑖,𝑗]G[i,j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示从 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边权．如果 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两点之间没有边，那么 𝐺[𝑖,𝑗] =∞G[i,j]=∞![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（有重边的情况取边权的最小值）

显然上述矩阵对应 𝑘 =1k=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时问题的答案．我们仍假设我们知道 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的答案，记为矩阵 𝐿𝑘Lk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．现在我们想求 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的答案．显然有转移方程

𝐿𝑘+1[𝑖,𝑗]=min1≤𝑝≤𝑛{𝐿𝑘[𝑖,𝑝]+𝐺[𝑝,𝑗]}Lk+1[i,j]=min1≤p≤n{Lk[i,p]+G[p,j]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

事实上我们可以类比矩阵乘法，你发现上述转移只是把矩阵乘法的乘积求和变成相加取最小值，于是我们定义这个运算为 ⊙⊙![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即

𝐴⊙𝐵=𝐶 ⟺ 𝐶[𝑖,𝑗]=min1≤𝑝≤𝑛{𝐴[𝑖,𝑝]+𝐵[𝑝,𝑗]}A⊙B=C ⟺ C[i,j]=min1≤p≤n{A[i,p]+B[p,j]}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是得到

𝐿𝑘+1=𝐿𝑘⊙𝐺Lk+1=Lk⊙G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

展开递推式得到

𝐿𝑘=𝐺⊙…⊙𝐺⏟𝑘 次=𝐺⊙𝑘Lk=G⊙…⊙G⏟k 次=G⊙k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们仍然可以用矩阵快速幂的方法计算上式，因为它显然是具有结合律的．时间复杂度 𝑂(𝑛3log⁡𝑘)O(n3log⁡k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 限长路径计数/最短路

上述算法只适用于边数固定的情况．然而我们可以改进算法以解决边数小于等于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况．具体地，考虑以下问题：

问题描述

给一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶有向图，边权为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后给一个整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，你的任务是对于每个点对 (𝑢,𝑣)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 找到从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 长度小于等于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径的数量（不一定是简单路径，即路径上的点或者边可能走多次）．

我们对于每个点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，建立一个虚点 𝑣′v′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用于记录答案，并在图中加入 (𝑣,𝑣′)(v,v′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 (𝑣′,𝑣′)(v′,v′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这两条边．那么对于点对 (𝑢,𝑣)(u,v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边数小于等于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径的数量，就和从 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑣′v′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边数恰好等于 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径的数量相等，这是因为对于任意一条边数为 𝑚(𝑚 ≤𝑘)m(m≤k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径 (𝑝0 =𝑢) →𝑝1 →𝑝2 →⋯ →𝑝𝑚−1 →(𝑝𝑚 =𝑣)(p0=u)→p1→p2→⋯→pm−1→(pm=v)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都存在一条边数为 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径 (𝑝0 =𝑢) →𝑝1 →𝑝2 →⋯ →𝑝𝑚−1 →(𝑝𝑚 =𝑣) →𝑣′ →⋯ →𝑣′(p0=u)→p1→p2→⋯→pm−1→(pm=v)→v′→⋯→v′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与之一一对应．

对于求边数小于等于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短路，只需对每个点加一个边权为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的自环即可．

## 习题

  * [洛谷 P1962 斐波那契数列](https://www.luogu.com.cn/problem/P1962)，即上面的例题，同题 POJ3070
  * [洛谷 P1349 广义斐波那契数列](https://www.luogu.com.cn/problem/P1349)，basebase![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵需要变化一下
  * [洛谷 P1939【模板】矩阵加速（数列）](https://www.luogu.com.cn/problem/P1939)，basebase![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵变成了 3 ×33×3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵，推导过程与上面差不多．

**本页面部分内容译自博文[Кратчайшие пути фиксированной длины, количества путей фиксированной длины](http://e-maxx.ru/algo/fixed_length_paths) 与其英文翻译版 [Number of paths of fixed length/Shortest paths of fixed length](https://cp-algorithms.com/graph/fixed_length_paths.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-algebra/matrix.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/linear-algebra/matrix.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [Gesrua](https://github.com/Gesrua), [Anguei](https://github.com/Anguei), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [MegaOwIer](https://github.com/MegaOwIer), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [countercurrent-time](https://github.com/countercurrent-time), [Henry-ZHR](https://github.com/Henry-ZHR), [kxccc](https://github.com/kxccc), [NachtgeistW](https://github.com/NachtgeistW), [369Pai](https://github.com/369Pai), [AngelKitty](https://github.com/AngelKitty), [Chrogeek](https://github.com/Chrogeek), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GavinZhengOI](https://github.com/GavinZhengOI), [GekkaSaori](https://github.com/GekkaSaori), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [HeRaNO](https://github.com/HeRaNO), [InsZVA](https://github.com/InsZVA), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [leoleoasd](https://github.com/leoleoasd), [LovelyBuggies](https://github.com/LovelyBuggies), [lychees](https://github.com/lychees), [Makkiy](https://github.com/Makkiy), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [oldherd](https://github.com/oldherd), [ouuan](https://github.com/ouuan), [P-Y-Y](https://github.com/P-Y-Y), [Peanut-Tang](https://github.com/Peanut-Tang), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [SukkaW](https://github.com/SukkaW), [Suyun514](mailto:suyun514@qq.com), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [weiyong1024](https://github.com/weiyong1024), [xcmvec](https://github.com/xcmvec)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
