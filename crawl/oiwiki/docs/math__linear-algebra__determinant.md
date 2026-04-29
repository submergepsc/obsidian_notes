# 行列式 - OI Wiki

- Source: https://oi-wiki.org/math/linear-algebra/determinant/

# 行列式

行列式，是方阵的一种运算．对于方阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，det⁡𝐴det⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示方阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行列式．

本文介绍行列式的三种定义．可以证明，本文中的定义方法是等价的．

## 全排列方法定义

前置知识：[置换](../../permutation/)、[逆序数](../../permutation/#逆序数)．

手动计算较低阶的行列式可以采用这种方法，它的时间复杂度为阶乘量级．

使用记号 𝜋(𝑗1𝑗2⋯𝑗𝑛)π(j1j2⋯jn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示排列 𝑗1𝑗2⋯𝑗𝑛j1j2⋯jn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆序数，𝑆𝑛Sn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为全体长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排列构成的集合．记号：

det⁡𝐴=∣ ∣ ∣ ∣ ∣𝑎11𝑎12⋯𝑎1𝑛𝑎21𝑎22⋯𝑎2𝑛⋮⋮⋮𝑎𝑛1𝑎𝑛2⋯𝑎𝑛𝑛∣ ∣ ∣ ∣ ∣=∑(𝑗1𝑗2⋯𝑗𝑛)∈𝑆𝑛(−1)𝜋(𝑗1𝑗2⋯𝑗𝑛)𝑎1𝑗1𝑎2𝑗2…𝑎𝑛𝑗𝑛det⁡A=|a11a12⋯a1na21a22⋯a2n⋮⋮⋮an1an2⋯ann|=∑(j1j2⋯jn)∈Sn(−1)π(j1j2⋯jn)a1j1a2j2…anjn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

表示的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶行列式是指 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项的代数和，这些项是一切可能的取自方阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中不同的行与不同的列上的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的乘积 𝑎1𝑗1𝑎2𝑗2⋯𝑎𝑛𝑗𝑛a1j1a2j2⋯anjn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

项 𝑎1𝑗1𝑎2𝑗2⋯𝑎𝑛𝑗𝑛a1j1a2j2⋯anjn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前面的符号是 (−1)𝜋(𝑗1𝑗2⋯𝑗𝑛)(−1)π(j1j2⋯jn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是说，当 𝑗1𝑗2⋯𝑗𝑛j1j2⋯jn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶排列时，符号为正，当 𝑗1𝑗2⋯𝑗𝑛j1j2⋯jn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是奇排列时，符号为负．

对于二三阶行列式的对角线法则，事实上就是采用了全排列定义．四阶以上行列式不再适用于对角线法则，也是同样的原因．特别地，一阶行列式就是元素本身．

定理：从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶行列式的第 𝑖1,𝑖2,⋯,𝑖𝑛i1,i2,⋯,in![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行和第 𝑗1,𝑗2,⋯,𝑗𝑛j1,j2,⋯,jn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列取出元素做乘积

𝑎𝑖1𝑗1𝑎𝑖2𝑗2⋯𝑎𝑖𝑛𝑗𝑛ai1j1ai2j2⋯ainjn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这里 𝑖1,𝑖2,⋯,𝑖𝑛i1,i2,⋯,in![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑗1,𝑗2,⋯,𝑗𝑛j1,j2,⋯,jn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是 1,2,⋯,𝑛1,2,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数的排列．那么这一项在行列式中的符号是 (−1)𝑠+𝑡(−1)s+t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中

𝑠=𝜋(𝑖1𝑖2⋯𝑖𝑛)s=π(i1i2⋯in)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑡=𝜋(𝑗1𝑗2⋯𝑗𝑛)t=π(j1j2⋯jn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定理：行列式和它的转置行列式相等．

定理：设行列式 det⁡𝐴det⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行的所有元素都可以表示成两项的和：

∣ ∣ ∣ ∣ ∣𝑎11𝑎12⋯𝑎1𝑛⋮⋮⋮𝑏𝑖1+𝑐𝑖1𝑏𝑖2+𝑐𝑖2⋯𝑏𝑖𝑛+𝑐𝑖𝑛⋮⋮⋮𝑎𝑛1𝑎𝑛2⋯𝑎𝑛𝑛∣ ∣ ∣ ∣ ∣|a11a12⋯a1n⋮⋮⋮bi1+ci1bi2+ci2⋯bin+cin⋮⋮⋮an1an2⋯ann|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么该行列式等于两个行列式 det⁡𝐴1det⁡A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 det⁡𝐴2det⁡A2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的和．其中 𝐴1A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行是 𝑏𝑖1,𝑏𝑖2,⋯,𝑏𝑖𝑛bi1,bi2,⋯,bin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐴2A2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行是 𝑐𝑖1,𝑐𝑖2,⋯,𝑐𝑖𝑛ci1,ci2,⋯,cin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐴1A1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐴2A2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的其余各行都和 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同．同样的性质对于列来说也成立．

## 归纳方法定义

这种方法只是描述了行列式的一种代数性质，时间复杂度也为阶乘量级，不适合用于计算．

### 代数余子式

在 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶行列式 det⁡𝐴det⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，任意取定矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行和 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列．位于这些行列相交处的元素构成的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶矩阵叫做 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶子矩阵，其行列式称为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶子式．

对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶行列式 det⁡𝐴det⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，某一元素 𝑎𝑖𝑗aij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的余子阵 𝑀𝑖𝑗Mij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指的是原矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，划去 𝑎𝑖𝑗aij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在的行和列后，余下的 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶子矩阵；其行列式 det⁡𝑀𝑖𝑗det⁡Mij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为余子式．

对于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶行列式 det⁡𝐴det⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，元素 𝑎𝑖𝑗aij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的余子式 det⁡𝑀𝑖𝑗det⁡Mij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 附以符号 (−1)𝑖+𝑗(−1)i+j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之后，叫做元素 𝑎𝑖𝑗aij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的代数余子式，用符号 𝐴𝑖𝑗Aij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示．

从上一节全排列方法的定义可以推出结论：

定理：若在一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶行列式 det⁡𝐴det⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行或第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的元素除了 𝑎𝑖𝑗aij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么这个行列式等于 𝑎𝑖𝑗aij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和它的代数余子式 𝐴𝑖𝑗Aij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的乘积．

### 行列式展开

由于方阵转置，行列式不变，只需介绍按行展开或按列展开之一即可．

行列式 det⁡𝐴det⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定义为它任意一行（或一列）的所有元素与它们的对应代数余子式乘积的和．

换句话说，行列式可以使用按行（或按列）的展开式递归定义：

det⁡𝐴=𝑎𝑖1𝐴𝑖1+𝑎𝑖2𝐴𝑖2+⋯+𝑎𝑖𝑛𝐴𝑖𝑛=𝑛∑𝑗=1𝑎𝑖𝑗𝐴𝑖𝑗=𝑛∑𝑗=1(−1)𝑖+𝑗𝑎𝑖𝑗det⁡𝑀𝑖𝑗det⁡A=ai1Ai1+ai2Ai2+⋯+ainAin=∑j=1naijAij=∑j=1n(−1)i+jaijdet⁡Mij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)det⁡𝐴=𝑎1𝑗𝐴1𝑗+𝑎2𝑗𝐴2𝑗+⋯+𝑎𝑛𝑗𝐴𝑛𝑗=𝑛∑𝑖=1𝑎𝑖𝑗𝐴𝑖𝑗=𝑛∑𝑖=1(−1)𝑖+𝑗𝑎𝑖𝑗det⁡𝑀𝑖𝑗det⁡A=a1jA1j+a2jA2j+⋯+anjAnj=∑i=1naijAij=∑i=1n(−1)i+jaijdet⁡Mij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

递归终点为一阶矩阵的行列式，其即为该矩阵包含的唯一一个元素．

于是有结论：

定理：行列式 det⁡𝐴det⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的某一行（或某一列）的元素与另外一行（或另外一列）对应元素的代数余子式的乘积之和等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

换句话说，当 𝑖 ≠𝑗i≠j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时：

𝑎𝑖1𝐴𝑗1+𝑎𝑖2𝐴𝑗2+⋯+𝑎𝑖𝑛𝐴𝑗𝑛=0ai1Aj1+ai2Aj2+⋯+ainAjn=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑎1𝑖𝐴1𝑗+𝑎2𝑖𝐴2𝑗+⋯+𝑎𝑛𝑖𝐴𝑛𝑗=0a1iA1j+a2iA2j+⋯+aniAnj=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 公理化定义

公理化定义是说，满足了某些性质的运算只能是行列式．

前置知识：[初等变换](../elementary-operations/)．

记 𝐷𝑖(𝑘)Di(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 [倍乘矩阵](../elementary-operations/#倍乘矩阵)、𝑃𝑖𝑗Pij![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 [对换矩阵](../elementary-operations/#对换矩阵)、𝑇𝑖𝑗(𝑘)Tij(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 [倍加矩阵](../elementary-operations/#倍加矩阵)．

对于一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的运算 detdet![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果满足以下四个性质，称为行列式：

  * 把一个行列式的某一行或某一列的所有元素同时乘以一个数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，等于用 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘这个行列式．

det⁡(𝐷𝑖(𝑘)𝐴)=det⁡(𝐴𝐷𝑖(𝑘))=𝑘det⁡𝐴det⁡(Di(k)A)=det⁡(ADi(k))=kdet⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 交换一个行列式的两行或两列，行列式改变符号．

det⁡(𝑃𝑖𝑗𝐴)=det⁡(𝐴𝑃𝑖𝑗)=−det⁡𝐴det⁡(PijA)=det⁡(APij)=−det⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 把行列式的某一行或某一列的元素乘以同一数后加到另一行或另一列的对应元素上，行列式不变．

det⁡(𝑇𝑖𝑗(𝑘)𝐴)=det⁡(𝐴𝑇𝑖𝑗(𝑘))=det⁡𝐴det⁡(Tij(k)A)=det⁡(ATij(k))=det⁡A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 单位矩阵的行列式为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

det⁡𝐼=1det⁡I=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用行列式有关初等变换的性质，可以方便手动计算更高阶的行列式．[「高斯消元」法计算行列式](../../numerical/gauss/#行列式计算)，也用到了这个性质，时间复杂度为 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

上述性质也有若干推论：

  * 一个行列式中某一行或某一列的公因子可以提到行列式符号的外边．
  * 如果一个行列式的某一行或某一列的元素全部是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么这个行列式等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 如果一个行列式有两行或两列的对应元素成比例，那么这个行列式等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 如果一个行列式有两行或两列完全相同，那么这个行列式等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这些推论在手算行列式的时候非常常用．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-algebra/determinant.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/linear-algebra/determinant.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [CCXXXI](https://github.com/CCXXXI), [Great-designer](https://github.com/Great-designer), [myeeye](https://github.com/myeeye), [untitledunrevised](https://github.com/untitledunrevised)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
