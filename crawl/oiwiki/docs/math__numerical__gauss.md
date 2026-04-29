# 高斯消元 - OI Wiki

- Source: https://oi-wiki.org/math/numerical/gauss/

# 高斯消元

## 引入

高斯消元法（Gauss–Jordan elimination）是求解线性方程组的经典算法，它在当代数学中有着重要的地位和价值，是线性代数课程教学的重要组成部分．

高斯消元法除了用于线性方程组求解外，还可以用于行列式计算、求矩阵的逆，以及其他计算机和工程方面．

## 消元法及高斯消元法思想

### 定义

消元法是将方程组中的一方程的未知数用含有另一未知数的代数式表示，并将其带入到另一方程中，这就消去了一未知数，得到一解；或将方程组中的一方程倍乘某个常数加到另外一方程中去，也可达到消去一未知数的目的．消元法主要用于二元一次方程组的求解．

### 解释

例一：利用消元法求解二元一次线性方程组：

{4𝑥+𝑦=100𝑥−𝑦=100{4x+y=100x−y=100![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

解：将方程组中两方程相加，消元 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可得：

5𝑥=2005x=200![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

解得：

𝑥=40x=40![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将 𝑥 =40x=40![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代入方程组中第二个方程可得：

𝑦=−60y=−60![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 消元法理论的核心

消元法理论的核心主要如下：

  * 两方程互换，解不变；

  * 一方程乘以非零数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，解不变；

  * 一方程乘以数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加上另一方程，解不变．

### 高斯消元法思想概念

德国数学家高斯对消元法进行了思考分析，得出了如下结论：

  * 在消元法中，参与计算和发生改变的是方程中各变量的系数；

  * 各变量并未参与计算，且没有发生改变；

  * 可以利用系数的位置表示变量，从而省略变量；

  * 在计算中将变量简化省略，方程的解不变．

高斯在这些结论的基础上，提出了高斯消元法，首先将方程的增广矩阵利用行初等变换化为行最简形，然后以线性无关为准则对自由未知量赋值，最后列出表达方程组通解．

## 高斯消元五步骤法

## 解释

高斯消元法在将增广矩阵化为最简形后对于自由未知量的赋值，需要掌握线性相关知识，且赋值存在人工经验的因素，使得在学习过程中有一定的困难，将高斯消元法划分为五步骤，从而提出五步骤法，内容如下：

  1. 增广矩阵行初等行变换为行最简形；

  2. 还原线性方程组；

  3. 求解第一个变量；

  4. 补充自由未知量；

  5. 列表示方程组通解．

利用实例进一步说明该算法的运作情况．

## 过程

例二：利用高斯消元法五步骤法求解线性方程组：

⎧{ {⎨{ {⎩2𝑥1+5𝑥3+6𝑥4=9𝑥3+𝑥4=−42𝑥3+2𝑥4=−8{2x1+5x3+6x4=9x3+x4=−42x3+2x4=−8![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 增广矩阵行（初等）变换为行最简形

所谓增广矩阵，即为方程组系数矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与常数列 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的并生成的新矩阵，即 (𝐴|𝑏)(A|b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，增广矩阵行初等变换化为行最简形，即是利用了高斯消元法的思想理念，省略了变量而用变量的系数位置表示变量，增广矩阵中用竖线隔开了系数矩阵和常数列，代表了等于符号．

⎛⎜ ⎜ ⎜⎝205600110022∣9−4−8⎞⎟ ⎟ ⎟⎠(205600110022|9−4−8)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑟3−2𝑟2←←←←←←←←→⎛⎜ ⎜ ⎜⎝205600110000∣9−40⎞⎟ ⎟ ⎟⎠→r3−2r2(205600110000|9−40)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

化为行阶梯形

𝑟12⟶⎛⎜ ⎜ ⎜⎝102.5300110000∣4.5−40⎞⎟ ⎟ ⎟⎠→r12(102.5300110000|4.5−40)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑟1−𝑟2×2.5←←←←←←←←←←←→⎛⎜ ⎜ ⎜⎝1000.500110000∣14.5−40⎞⎟ ⎟ ⎟⎠→r1−r2×2.5(1000.500110000|14.5−40)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

化为最简形

### 还原线性方程组

{𝑥1+0.5𝑥4=14.5𝑥3+𝑥4=−4{x1+0.5x4=14.5x3+x4=−4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)解释

所谓的还原线性方程组，即是在行最简形的基础上，将之重新书写为线性方程组的形式，即将行最简形中各位置的系数重新赋予变量，中间的竖线还原为等号．

### 求解第一个变量

{𝑥1=−0.5𝑥4+14.5𝑥3=−𝑥4−4{x1=−0.5x4+14.5x3=−x4−4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)解释

即是对于所还原的线性方程组而言，将方程组中每个方程的第一个变量，用其他量表达出来．如方程组两方程中的第一个变量 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥3x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 补充自由未知量

⎧{ { {⎨{ { {⎩𝑥1=−0.5𝑥4+14.5𝑥2=𝑥2𝑥3=−𝑥4−4𝑥4=𝑥4{x1=−0.5x4+14.5x2=x2x3=−x4−4x4=x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)解释

第 3 步中，求解出变量 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥3x3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而说明了方程剩余的变量 𝑥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥4x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不受方程组的约束，是自由未知量，可以取任意值，所以需要在第 3 步骤解得基础上进行解得补充，补充的方法为 𝑥2 =𝑥2,𝑥4 =𝑥4x2=x2,x4=x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这种解得补充方式符合自由未知量定义，并易于理解，因为是自由未知量而不受约束，所以只能自己等于自己．

### 列表示方程组的通解

⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝𝑥1𝑥2𝑥3𝑥4⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠=⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝0100⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠𝑥2+⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝−0.50−11⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠𝑥4+⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝14.50−40⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠=⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝0100⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠𝐶1+⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝−0.50−11⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠𝐶2+⎛⎜ ⎜ ⎜ ⎜ ⎜ ⎜⎝14.50−40⎞⎟ ⎟ ⎟ ⎟ ⎟ ⎟⎠(x1x2x3x4)=(0100)x2+(−0.50−11)x4+(14.50−40)=(0100)C1+(−0.50−11)C2+(14.50−40)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝐶1C1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐶2C2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为任意常数．

解释

即在第 4 步的基础上，将解表达为列向量组合的表示形式，同时由于 𝑥2x2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥4x4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是自由未知量，可以取任意值，所以在解得右边，令二者分别为任意常数 𝐶1C1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐶2C2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即实现了对方程组的求解．

## 行列式计算

### 解释

𝑁 ×𝑁N×N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 方阵行列式（Determinant）可以理解为所有列向量所夹的几何体的有向体积．

例如：

∣1001∣=1|1001|=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)∣1221∣=−3|1221|=−3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

行列式有公式

det⁡(𝐴)=∑𝜎∈𝑆𝑛sgn⁡(𝜎)𝑛∏𝑖=1𝑎𝑖,𝜎(𝑖)det⁡(A)=∑σ∈Snsgn⁡(σ)∏i=1nai,σ(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑆𝑛Sn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是指长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全排列的集合，𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是一个全排列，如果 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆序对对数为偶数，则 sgn⁡(𝜎) =1sgn⁡(σ)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，否则 sgn⁡(𝜎) = −1sgn⁡(σ)=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

通过体积概念理解行列式不变性是一个非常简单的办法：

  * 矩阵转置，行列式不变；

  * 矩阵行（列）交换，行列式取反；

  * 矩阵行（列）相加或相减，行列式不变；

  * 矩阵行（列）所有元素同时乘以数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，行列式等比例变大．

由此，对矩阵应用高斯消元之后，我们可以得到一个对角线矩阵，此矩阵的行列式由对角线元素之积所决定．其符号可由交换行的数量来确定（如果为奇数，则行列式的符号应颠倒）．因此，我们可以在 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度下使用高斯算法计算矩阵．

注意，如果在某个时候，我们在当前列中找不到非零单元，则算法应停止并返回 0．

### 实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text constexpr double EPS = 1E-9 ; int n ; vector < vector < double >> a ( n , vector < double > ( n )); double det = 1 ; for ( int i = 0 ; i < n ; ++ i ) { int k = i ; for ( int j = i \+ 1 ; j < n ; ++ j ) if ( abs ( a [ j ][ i ]) > abs ( a [ k ][ i ])) k = j ; if ( abs ( a [ k ][ i ]) < EPS ) { det = 0 ; break ; } swap ( a [ i ], a [ k ]); if ( i != k ) det = \- det ; det *= a [ i ][ i ]; for ( int j = i \+ 1 ; j < n ; ++ j ) a [ i ][ j ] /= a [ i ][ i ]; for ( int j = 0 ; j < n ; ++ j ) if ( j != i && abs ( a [ j ][ i ]) > EPS ) for ( int k = i \+ 1 ; k < n ; ++ k ) a [ j ][ k ] -= a [ i ][ k ] * a [ j ][ i ]; } cout << det ; ```   
---|---  
  
## 矩阵求逆

对于方阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若存在方阵 𝐴−1A−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝐴 ×𝐴−1 =𝐴−1 ×𝐴 =𝐼A×A−1=A−1×A=I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可逆，𝐴−1A−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被称为它的逆矩阵．

给出 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶方阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求解其逆矩阵的方法如下：

  1. 构造 𝑛 ×2𝑛n×2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵 (𝐴,𝐼𝑛)(A,In)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 用高斯消元法将其化简为最简形 (𝐼𝑛,𝐴−1)(In,A−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即可得到 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆矩阵 𝐴−1A−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果最终最简形的左半部分不是单位矩阵 𝐼𝑛In![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不可逆．

该方法的正确性证明需要用到较多线性代数的知识，限于篇幅这里不再给出．感兴趣的读者可以自行查阅相关资料．

## 高斯消元法解异或方程组

异或方程组是指形如

⎧{ { {⎨{ { {⎩𝑎1,1𝑥1⊕𝑎1,2𝑥2⊕⋯⊕𝑎1,𝑛𝑥𝑛=𝑏1𝑎2,1𝑥1⊕𝑎2,2𝑥2⊕⋯⊕𝑎2,𝑛𝑥𝑛=𝑏2⋯⋯𝑎𝑚,1𝑥1⊕𝑎𝑚,2𝑥2⊕⋯⊕𝑎𝑚,𝑛𝑥𝑛=𝑏𝑚{a1,1x1⊕a1,2x2⊕⋯⊕a1,nxn=b1a2,1x1⊕a2,2x2⊕⋯⊕a2,nxn=b2⋯⋯am,1x1⊕am,2x2⊕⋯⊕am,nxn=bm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的方程组，其中 ⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示「按位异或」（即 `xor` 或 C++ 中的 `^`），且式中所有系数/常数（即 𝑎𝑖,𝑗ai,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑏𝑖bi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）均为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于「异或」符合交换律与结合律，故可以按照高斯消元法逐步消元求解．值得注意的是，我们在消元的时候应使用「异或消元」而非「加减消元」，且不需要进行乘除改变系数（因为系数均为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

注意到异或方程组的增广矩阵是 0101![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 矩阵（矩阵中仅含有 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），所以我们可以使用 C++ 中的 `std::bitset` 进行优化，将时间复杂度降为 𝑂(𝑛2𝑚𝜔)O(n2mω)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为元的个数，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为方程条数，𝜔ω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一般为 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（与机器有关）．

参考实现：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text std :: bitset < 1010 > matrix [ 2010 ]; // matrix[1~n]：增广矩阵，0 位置为常数 std :: vector < bool > GaussElimination ( int n , int m ) // n 为未知数个数，m 为方程个数，返回方程组的解 // （多解 / 无解返回一个空的 vector） { for ( int i = 1 ; i <= n ; i ++ ) { int cur = i ; while ( cur <= m && ! matrix [ cur ]. test ( i )) cur ++ ; if ( cur > m ) return std :: vector < bool > ( 0 ); if ( cur != i ) swap ( matrix [ cur ], matrix [ i ]); for ( int j = 1 ; j <= m ; j ++ ) if ( i != j && matrix [ j ]. test ( i )) matrix [ j ] ^= matrix [ i ]; } std :: vector < bool > ans ( n \+ 1 ); for ( int i = 1 ; i <= n ; i ++ ) ans [ i ] = matrix [ i ]. test ( 0 ); return ans ; } ```   
---|---  
  
## 练习题

  * [Codeforces - 巫师和赌注](http://codeforces.com/contest/167/problem/E)
  * [luogu - SDOI2010 外星千足虫](https://www.luogu.com.cn/problem/P2447)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/numerical/gauss.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/numerical/gauss.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [StudyingFather](https://github.com/StudyingFather), [Enter-tainer](https://github.com/Enter-tainer), [H-J-Granger](https://github.com/H-J-Granger), [sshwy](https://github.com/sshwy), [countercurrent-time](https://github.com/countercurrent-time), [Early0v0](https://github.com/Early0v0), [NachtgeistW](https://github.com/NachtgeistW), [Xeonacid](https://github.com/Xeonacid), [CCXXXI](https://github.com/CCXXXI), [MegaOwIer](https://github.com/MegaOwIer), [P-Y-Y](https://github.com/P-Y-Y), [GavinZhengOI](https://github.com/GavinZhengOI), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [Zhoier](https://github.com/Zhoier), [AngelKitty](https://github.com/AngelKitty), [c-forrest](https://github.com/c-forrest), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [henrytbtrue](https://github.com/henrytbtrue), [huayucaiji](https://github.com/huayucaiji), [iamtwz](https://github.com/iamtwz), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [Marcythm](https://github.com/Marcythm), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [PotassiumWings](https://github.com/PotassiumWings), [qwqAutomaton](https://github.com/qwqAutomaton), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [shuzhouliu](https://github.com/shuzhouliu), [shuzhouliu-bot](https://github.com/shuzhouliu-bot), [SukkaW](https://github.com/SukkaW), [Suyun514](mailto:suyun514@qq.com), [tsentau](https://github.com/tsentau), [weiyong1024](https://github.com/weiyong1024), [Yukimaikoriya](https://github.com/Yukimaikoriya), [Alphnia](https://github.com/Alphnia), [firefly-zjyjoe](https://github.com/firefly-zjyjoe), [Gesrua](https://github.com/Gesrua), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [mufanq](https://github.com/mufanq), [Peanut-Tang](https://github.com/Peanut-Tang), [qute-firefly-26710-zjyjoe-lg-592080](https://github.com/qute-firefly-26710-zjyjoe-lg-592080), [Siger Young](mailto:siger-young@users.noreply.github.com), [Siger Young](https://github.com/Siger Young), [WhenMelancholy](https://github.com/WhenMelancholy), [xiaoyezi2007](https://github.com/xiaoyezi2007), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [zyj-111](https://github.com/zyj-111)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
