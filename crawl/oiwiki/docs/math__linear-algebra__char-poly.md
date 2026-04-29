# 特征多项式 - OI Wiki

- Source: https://oi-wiki.org/math/linear-algebra/char-poly/

# 特征多项式

特征的这部分只研究方阵，即矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的线性变换将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个向量映射到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个向量．

由于在实际问题中，经常要考虑连续进行重复的变换，如果只用「矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的线性变换将单位阵 𝐼I![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变换为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」的描述，就会很抽象．此时最好的办法是找「不动点」，即变换当中不动的部分．

然而事实上，矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的线性变换很可能没有不动点，于是退而求其次，寻找共线或者类似于简单变形的部分．

## 特征值与特征向量

在矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的线性变换作用下，一些向量的方向不改变，只是伸缩了．

设 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的线性空间，𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的线性变换．若存在 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 **非零向量** 𝜉ξ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得：

𝑇𝜉=𝜆𝜉Tξ=λξ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则称 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个 **特征值** ，而 𝜉ξ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **属于特征值 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个特征向量**．

特征向量在同一直线上，在线性变换作用下保持方向不改变（压缩到零也认为是方向不改变）．特征向量不唯一，与特征向量共线的向量都是特征向量，但是规定零向量不是特征向量，拥有方向的向量自然是非零向量．特征向量的特征值就是它伸缩的倍数．

在实际应用中，一般对于拥有相同特征值的特征向量，会选取一组基作为它们全体的代表．

设 𝛼1,𝛼2,⋯,𝛼𝑛α1,α2,⋯,αn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组基，𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在这组基下的矩阵为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即：

𝑇(𝛼1,𝛼2,⋯,𝛼𝑛)=(𝛼1,𝛼2,⋯,𝛼𝑛)𝐴T(α1,α2,⋯,αn)=(α1,α2,⋯,αn)A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 𝜆0λ0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个特征值，𝜉ξ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的属于特征值 𝜆0λ0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个特征向量，且有非零向量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足：

𝜉=(𝛼1,𝛼2,⋯,𝛼𝑛)𝑋ξ=(α1,α2,⋯,αn)X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是有：

𝑇𝜉=𝜆0𝜉Tξ=λ0ξ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝑇(𝛼1,𝛼2,⋯,𝛼𝑛)𝑋=𝜆0(𝛼1,𝛼2,⋯,𝛼𝑛)𝑋T(α1,α2,⋯,αn)X=λ0(α1,α2,⋯,αn)X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(𝛼1,𝛼2,⋯,𝛼𝑛)𝐴𝑋=𝜆0(𝛼1,𝛼2,⋯,𝛼𝑛)𝑋(α1,α2,⋯,αn)AX=λ0(α1,α2,⋯,αn)X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝐴𝑋=𝜆0𝑋AX=λ0X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(𝐴−𝜆0𝐼)𝑋=0(A−λ0I)X=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以相应的行列式也为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 特征多项式

考虑一个 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑛 ≥0 ∧𝑛 ∈ℤn≥0∧n∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一个参量，矩阵 𝜆𝐼 −𝐴λI−A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **特征矩阵** ．

特征矩阵的行列式称为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **特征多项式** ，展开为一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次多项式，根为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征值，记为 𝑝𝐴(𝜆)pA(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑝𝐴(𝜆)=det⁡(𝜆𝐼𝑛−𝐴)=∣ ∣ ∣ ∣ ∣𝜆−𝑎11−𝑎12⋯−𝑎1𝑛−𝑎21𝜆−𝑎22⋯−𝑎2𝑛⋮⋮⋮−𝑎𝑛1−𝑎𝑛2⋯𝜆−𝑎𝑛𝑛∣ ∣ ∣ ∣ ∣pA(λ)=det⁡(λIn−A)=|λ−a11−a12⋯−a1n−a21λ−a22⋯−a2n⋮⋮⋮−an1−an2⋯λ−ann|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝐼𝑛In![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一个 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的单位矩阵．一些地方会定义为 𝑝𝐴(𝜆) =det⁡(𝐴−𝜆𝐼𝑛)pA(λ)=det⁡(A−λIn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与我们的定义仅相差了一个符号 ( −1)𝑛(−1)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但采用这种定义得到的 𝑝𝐴(𝜆)pA(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定为首一多项式，而另外的定义则仅当 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为偶数时才是首一多项式．需要注意的是 0 ×00×0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵行列式为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是良定义的．

相应于 (𝜆0𝐼 −𝐴)𝑋 =0(λ0I−A)X=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非零解向量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的属于 𝜆0λ0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征向量．

线性变换 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有特征值 𝜆0λ0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价于矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有特征值 𝜆0λ0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

线性变换 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有特征向量 𝜉ξ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价于矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有特征向量 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中有：

𝜉=(𝛼1,⋯,𝛼𝑛)𝑋ξ=(α1,⋯,αn)X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据代数基本定理，特征多项式可以分解为：

𝑓(𝜆)=|𝜆𝐼−𝐴|=(𝜆−𝜆1)𝑑1⋯(𝜆−𝜆𝑚)𝑑𝑚f(λ)=|λI−A|=(λ−λ1)d1⋯(λ−λm)dm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

称 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为特征值 𝜆𝑖λi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **代数重数** ．全体代数重数的和为空间维数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 求解矩阵的全部特征值及特征向量

分为以下步骤：

  * 计算行列式 |𝜆𝐼 −𝐴||λI−A|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 求出多项式 𝑓(𝜆) =|𝜆𝐼 −𝐴|f(λ)=|λI−A|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在域 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的全部根，即 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征值．
  * 对 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每个特征值 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，解齐次线性方程组 (𝜆𝐼 −𝐴)𝑋 =0(λI−A)X=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求出它的一组基础解系 𝑋1,⋯,𝑋𝑡X1,⋯,Xt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的属于 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全部特征向量为：

𝑘1𝑋1+𝑘2𝑋2+⋯+𝑘𝑡𝑋𝑡k1X1+k2X2+⋯+ktXt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

该表达式中的 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不全为零．

  * 线性变换 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的属于 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征向量为：

𝜉𝑖=(𝛼1,⋯,𝛼𝑛)𝑋𝑖ξi=(α1,⋯,αn)Xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，属于 𝜆λ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全部特征向量为：

𝑘1𝜉1+𝑘2𝜉2+⋯+𝑘𝑡𝜉𝑡k1ξ1+k2ξ2+⋯+ktξt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

该表达式中的 𝑘𝑖ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不全为零．

特征值与特征向量是否存在，依赖于 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在的域．

## 相似变换

### 引入

若 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为上三角矩阵如

𝐴=⎡⎢ ⎢ ⎢ ⎢⎣𝑎1,1𝑎1,2⋯𝑎1,𝑛𝑎2,2⋯𝑎2,𝑛⋱⋮𝑎𝑛,𝑛⎤⎥ ⎥ ⎥ ⎥⎦A=[a1,1a1,2⋯a1,na2,2⋯a2,n⋱⋮an,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么

𝑝𝐴(𝑥)=det⁡(𝑥𝐼𝑛−𝐴)=⎡⎢ ⎢ ⎢ ⎢⎣𝑥−𝑎1,1−𝑎1,2⋯−𝑎1,𝑛𝑥−𝑎2,2⋯−𝑎2,𝑛⋱⋮𝑥−𝑎𝑛,𝑛⎤⎥ ⎥ ⎥ ⎥⎦=𝑛∏𝑖=1(𝑥−𝑎𝑖,𝑖)pA(x)=det⁡(xIn−A)=[x−a1,1−a1,2⋯−a1,nx−a2,2⋯−a2,n⋱⋮x−an,n]=∏i=1n(x−ai,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可轻松求得，下三角矩阵也是类似的．但如果 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不属于这两种矩阵，则需要使用相似变换，使得矩阵变为容易求得特征多项式的形式．

### 定义

对于 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当存在 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的可逆矩阵 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足

𝐵=𝑃−1𝐴𝑃B=P−1AP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相似，记变换 𝐴 ↦𝑃−1𝐴𝑃A↦P−1AP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为相似变换．且 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑃−1𝐴𝑃P−1AP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有相同的特征多项式．

考虑

det⁡(𝑥𝐼𝑛−𝑃−1𝐴𝑃)=det⁡(𝑥𝑃−1𝐼𝑛𝑃−𝑃−1𝐴𝑃)=det⁡(𝑃−1𝑥𝐼𝑛𝑃−𝑃−1𝐴𝑃)=det⁡(𝑃−1)⋅det⁡(𝑃)⋅det⁡(𝑥𝐼𝑛−𝐴)=det⁡(𝑥𝐼𝑛−𝐴)=𝑝𝐴(𝑥)det⁡(xIn−P−1AP)=det⁡(xP−1InP−P−1AP)=det⁡(P−1xInP−P−1AP)=det⁡(P−1)⋅det⁡(P)⋅det⁡(xIn−A)=det⁡(xIn−A)=pA(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

得证，对于 𝐴 ↦𝑃𝐴𝑃−1A↦PAP−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是一样的．另外 𝑝𝐴(0) =( −1)𝑛 ⋅det⁡(𝐴)pA(0)=(−1)n⋅det⁡(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为 𝑝𝐴(0) =det⁡(−1⋅𝐼𝑛𝐴) =det⁡(−1⋅𝐼𝑛) ⋅det⁡(𝐴)pA(0)=det⁡(−1⋅InA)=det⁡(−1⋅In)⋅det⁡(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 故 det⁡(𝐴) =det⁡(𝑃−1𝐴𝑃)det⁡(A)=det⁡(P−1AP)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

定理：相似矩阵有相同的特征多项式及特征值，反之不然．

定理表明，线性变换的矩阵的特征多项式与基的选取无关，而直接由线性变换决定，故可称之为线性变换的特征多项式．

矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征多项式 𝑓(𝜆) =|𝜆𝐼 −𝐴|f(λ)=|λI−A|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个首一的多项式．根据韦达定理，它的 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次系数为：

−(𝜆1+⋯+𝜆𝑛)=−(𝑎11+⋯+𝑎𝑛𝑛)=−𝑡𝑟𝐴−(λ1+⋯+λn)=−(a11+⋯+ann)=−trA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑡𝑟𝐴trA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的迹，为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的主对角线元素之和．

根据韦达定理，特征多项式的常数项为：

(−1)𝑛|𝐴|=(−1)𝑛(𝜆1⋯𝜆𝑛)(−1)n|A|=(−1)n(λ1⋯λn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

定理：相似的矩阵有相同的迹．

### 换位公式

定理：无论矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和矩阵 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否方阵，只要乘法能进行，则矩阵 𝐴𝐵AB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的迹等于矩阵 𝐵𝐴BA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的迹．

一种证法是直接展开，即证毕．另一种证法用到换位公式．

定理：设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列矩阵，设 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列矩阵，则有：

𝜆𝑛|𝜆𝐼𝑚−𝐴𝐵|=𝜆𝑚|𝜆𝐼𝑛−𝐵𝐴|λn|λIm−AB|=λm|λIn−BA|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

该公式表明 𝐴𝐵AB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐵𝐴BA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有相同的非零特征值．

### 舒尔（Schur）引理

任意的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都相似于一个上三角阵，即存在满秩阵 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑃−1𝐴𝑃P−1AP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为上三角阵，它的主对角线上元素为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全部特征值．

推论：设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个特征值为 𝜆1,⋯,𝜆𝑛λ1,⋯,λn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝜙(𝑥)ϕ(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为任一多项式，则矩阵多项式 𝜙(𝐴)ϕ(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个特征值为：

𝜙(𝜆1),⋯,𝜙(𝜆𝑛)ϕ(λ1),⋯,ϕ(λn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

特别地，𝑘𝐴kA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征值为 𝑘𝜆1,⋯,𝑘𝜆𝑛kλ1,⋯,kλn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝐴𝑚Am![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征值为 𝜆1𝑚,⋯,𝜆𝑛𝑚λ1m,⋯,λnm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 使用高斯消元进行相似变换

对 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以进行高斯消元，其基本操作为初等行变换．

在对矩阵使用上述操作（左乘初等矩阵）后再右乘其逆矩阵即相似变换，左乘为行变换，易发现右乘即列变换．

若能将矩阵通过相似变换变为上三角或下三角的形式，那么可以轻松求出其特征多项式．但若对主对角线上的元素应用变换 𝐴 ↦𝑇𝑖𝑗(𝑘)𝐴𝑇𝑖𝑗( −𝑘)A↦Tij(k)ATij(−k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后会导致原本通过 𝐴 ↦𝑇𝑖𝑗(𝑘)𝐴A↦Tij(k)A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的元素消为零后右乘 𝑇𝑖𝑗( −𝑘)Tij(−k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即将 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的 −𝑘−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倍加到第 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列这一操作使得之前消为零的元素现在可能不为零，可能不能将其变为上三角或下三角形式．

后文将说明对次对角线上的元素应用变换后得到的矩阵依然可以轻松得到其特征多项式．

### 上 Hessenberg 矩阵

对于 𝑛 >2n>2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形如

𝐻=⎡⎢ ⎢ ⎢ ⎢ ⎢⎣𝛼1ℎ12……ℎ1𝑛𝛽2𝛼2ℎ23…⋮⋱⋱⋱⋮⋱⋱ℎ(𝑛−1)𝑛𝛽𝑛𝛼𝑛⎤⎥ ⎥ ⎥ ⎥ ⎥⎦H=[α1h12……h1nβ2α2h23…⋮⋱⋱⋱⋮⋱⋱h(n−1)nβnαn]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的矩阵我们称为上 Hessenberg 矩阵，其中 𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为次对角线．

我们使用相似变换将次对角线以下的元素消为零后即能得到上 Hessenberg 矩阵，而求出一个 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上 Hessenberg 矩阵的特征多项式则可在 𝑂(𝑛3)O(n3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间完成．

我们记 𝐻𝑖Hi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为只保留 𝐻H![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 行和前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 列的矩阵，记 𝑝𝑖(𝑥) =det⁡(𝑥𝐼𝑖−𝐻𝑖)pi(x)=det⁡(xIi−Hi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

𝐻0=[],𝑝0(𝑥)=1H0=[],p0(x)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝐻1=[𝛼1],𝑝1(𝑥)=det⁡(𝑥𝐼1−𝐻1)=𝑥−𝛼1H1=[α1],p1(x)=det⁡(xI1−H1)=x−α1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)𝐻2=[𝛼1ℎ12𝛽2𝛼2],𝑝2(𝑥)=det⁡(𝑥𝐼2−𝐻2)=(𝑥−𝛼2)𝑝1(𝑥)−𝛽2ℎ12𝑝0(𝑥)H2=[α1h12β2α2],p2(x)=det⁡(xI2−H2)=(x−α2)p1(x)−β2h12p0(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在计算行列式时我们一般选择按零最多的行或列余子式展开，余子式即删除了当前选择的元素所在行和列之后的矩阵，在这里我们选择按最后一行进行展开，有

𝑝3(𝑥)=det⁡(𝑥𝐼3−𝐻3)=∣𝑥−𝛼1−ℎ12−ℎ13−𝛽2𝑥−𝛼2−ℎ23−𝛽3𝑥−𝛼3∣=(𝑥−𝛼3)⋅(−1)3+3𝑝2(𝑥)−𝛽3⋅(−1)3+2∣𝑥−𝛼1−ℎ13−𝛽2−ℎ23∣=(𝑥−𝛼3)𝑝2(𝑥)−𝛽3(ℎ23𝑝1(𝑥)+𝛽2ℎ13𝑝0(𝑥))p3(x)=det⁡(xI3−H3)=|x−α1−h12−h13−β2x−α2−h23−β3x−α3|=(x−α3)⋅(−1)3+3p2(x)−β3⋅(−1)3+2|x−α1−h13−β2−h23|=(x−α3)p2(x)−β3(h23p1(x)+β2h13p0(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

观察并归纳，对 2 ≤𝑖 ≤𝑛2≤i≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

𝑝𝑖(𝑥)=(𝑥−𝛼𝑖)𝑝𝑖−1(𝑥)−𝑖−1∑𝑚=1ℎ𝑖−𝑚,𝑖(𝑖∏𝑗=𝑖−𝑚+1𝛽𝑗)𝑝𝑖−𝑚−1(𝑥)pi(x)=(x−αi)pi−1(x)−∑m=1i−1hi−m,i(∏j=i−m+1iβj)pi−m−1(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

至此完成了整个算法，该算法一般被称为 Hessenberg 算法．

## Cayley–Hamilton 定理

对于任意的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，特征多项式为 𝑓(𝜆) =|𝜆𝐼 −𝐴|f(λ)=|λI−A|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则必有 𝑓(𝐴) =0f(A)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于线性变换 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有平行的结果：如果 𝑓(𝜆)f(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征多项式，则 𝑓(𝑇)f(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为零变换．

由本定理可知，对于任意的矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必有可以使其零化的多项式．

## 最小多项式

设 𝑉V![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维向量空间，由于线性变换对应的矩阵有 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素，一切线性变换构成 𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维线性空间．

对于一个特定的线性变换 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从作用 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次到作用 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，总共 𝑛2 +1n2+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个线性变换，它们对应的矩阵一定线性相关．于是存在非零多项式 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑓(𝑇)f(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为零变换，称变换 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足多项式 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足的所有多项式 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，存在次数最低的．

可以将矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 零化的最小次数的首一多项式称为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小多项式，记为 𝑚𝐴(𝜆)mA(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

根据多项式的辗转相除法，最小多项式是唯一的，且可整除任一 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的零化多项式．特别地，最小多项式整除特征多项式．

定理：在不计重数的情况下，矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征多项式 𝑓(𝜆)f(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与最小多项式 𝑚𝐴(𝜆)mA(λ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有相同的根．

定理：矩阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的属于不同特征值的特征向量线性无关．

## 应用

在信息学中我们一般考虑 (ℤ/𝑚ℤ)𝑛×𝑛(Z/mZ)n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的矩阵，通常 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为素数，进行上述相似变换是简单的，当 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为合数时，我们可以考虑类似辗转相除的方法来进行．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 ``` |  ```text #include <cassert> #include <iostream> #include <random> #include <vector> using Matrix = std :: vector < std :: vector < int >> ; using i64 = int64_t ; Matrix to_upper_Hessenberg ( const Matrix & M , int mod ) { Matrix H ( M ); int n = H . size (); for ( int i = 0 ; i < n ; ++ i ) { for ( int j = 0 ; j < n ; ++ j ) { if (( H [ i ][ j ] %= mod ) < 0 ) H [ i ][ j ] += mod ; } } for ( int i = 0 ; i < n \- 1 ; ++ i ) { int pivot = i \+ 1 ; for (; pivot < n ; ++ pivot ) { if ( H [ pivot ][ i ] != 0 ) break ; } if ( pivot == n ) continue ; if ( pivot != i \+ 1 ) { for ( int j = i ; j < n ; ++ j ) std :: swap ( H [ i \+ 1 ][ j ], H [ pivot ][ j ]); for ( int j = 0 ; j < n ; ++ j ) std :: swap ( H [ j ][ i \+ 1 ], H [ j ][ pivot ]); } for ( int j = i \+ 2 ; j < n ; ++ j ) { for (;;) { if ( H [ j ][ i ] == 0 ) break ; if ( H [ i \+ 1 ][ i ] == 0 ) { for ( int k = i ; k < n ; ++ k ) std :: swap ( H [ i \+ 1 ][ k ], H [ j ][ k ]); for ( int k = 0 ; k < n ; ++ k ) std :: swap ( H [ k ][ i \+ 1 ], H [ k ][ j ]); break ; } if ( H [ j ][ i ] >= H [ i \+ 1 ][ i ]) { int q = H [ j ][ i ] / H [ i \+ 1 ][ i ], mq = mod \- q ; for ( int k = i ; k < n ; ++ k ) H [ j ][ k ] = ( H [ j ][ k ] \+ i64 ( mq ) * H [ i \+ 1 ][ k ]) % mod ; for ( int k = 0 ; k < n ; ++ k ) H [ k ][ i \+ 1 ] = ( H [ k ][ i \+ 1 ] \+ i64 ( q ) * H [ k ][ j ]) % mod ; } else { int q = H [ i \+ 1 ][ i ] / H [ j ][ i ], mq = mod \- q ; for ( int k = i ; k < n ; ++ k ) H [ i \+ 1 ][ k ] = ( H [ i \+ 1 ][ k ] \+ i64 ( mq ) * H [ j ][ k ]) % mod ; for ( int k = 0 ; k < n ; ++ k ) H [ k ][ j ] = ( H [ k ][ j ] \+ i64 ( q ) * H [ k ][ i \+ 1 ]) % mod ; } } } } return H ; } std :: vector < int > get_charpoly ( const Matrix & M , int mod ) { Matrix H ( to_upper_Hessenberg ( M , mod )); int n = H . size (); std :: vector < std :: vector < int >> p ( n \+ 1 ); p [ 0 ] = { 1 % mod }; for ( int i = 1 ; i <= n ; ++ i ) { const std :: vector < int > & pi_1 = p [ i \- 1 ]; std :: vector < int > & pi = p [ i ]; pi . resize ( i \+ 1 , 0 ); int v = mod \- H [ i \- 1 ][ i \- 1 ]; if ( v == mod ) v -= mod ; for ( int j = 0 ; j < i ; ++ j ) { pi [ j ] = ( pi [ j ] \+ i64 ( v ) * pi_1 [ j ]) % mod ; if (( pi [ j \+ 1 ] += pi_1 [ j ]) >= mod ) pi [ j \+ 1 ] -= mod ; } int t = 1 ; for ( int j = 1 ; j < i ; ++ j ) { t = i64 ( t ) * H [ i \- j ][ i \- j \- 1 ] % mod ; int prod = i64 ( t ) * H [ i \- j \- 1 ][ i \- 1 ] % mod ; if ( prod == 0 ) continue ; prod = mod \- prod ; for ( int k = 0 ; k <= i \- j \- 1 ; ++ k ) pi [ k ] = ( pi [ k ] \+ i64 ( prod ) * p [ i \- j \- 1 ][ k ]) % mod ; } } return p [ n ]; } bool verify ( const Matrix & M , const std :: vector < int > & charpoly , int mod ) { if ( mod == 1 ) return true ; int n = M . size (); std :: vector < int > randvec ( n ), sum ( n , 0 ); std :: mt19937 gen ( std :: random_device {}()); std :: uniform_int_distribution < int > dis ( 1 , mod \- 1 ); for ( int i = 0 ; i < n ; ++ i ) randvec [ i ] = dis ( gen ); for ( int i = 0 ; i <= n ; ++ i ) { int v = charpoly [ i ]; for ( int j = 0 ; j < n ; ++ j ) sum [ j ] = ( sum [ j ] \+ i64 ( v ) * randvec [ j ]) % mod ; std :: vector < int > prod ( n , 0 ); for ( int j = 0 ; j < n ; ++ j ) { for ( int k = 0 ; k < n ; ++ k ) { prod [ j ] = ( prod [ j ] \+ i64 ( M [ j ][ k ]) * randvec [ k ]) % mod ; } } randvec . swap ( prod ); } for ( int i = 0 ; i < n ; ++ i ) if ( sum [ i ] != 0 ) return false ; return true ; } int main () { std :: ios :: sync_with_stdio ( false ); std :: cin . tie ( nullptr ); int n , mod ; std :: cin >> n >> mod ; Matrix M ( n , std :: vector < int > ( n )); for ( int i = 0 ; i < n ; ++ i ) for ( int j = 0 ; j < n ; ++ j ) std :: cin >> M [ i ][ j ]; std :: vector < int > charpoly ( get_charpoly ( M , mod )); for ( int i = 0 ; i <= n ; ++ i ) std :: cout << charpoly [ i ] << ' ' ; assert ( verify ( M , charpoly , mod )); return 0 ; } ```   
---|---  
  
上述 Hessenberg 算法不具有数值的稳定性，所以 ℝ𝑛×𝑛Rn×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的矩阵在使用前需要其他算法进行调整或改用其他具有数值稳定性的算法．

我们可以将特征多项式与常系数齐次线性递推联系起来，也可结合 Cayley–Hamilton 定理、多项式取模加速一些域上求矩阵幂次的算法．

Cayley–Hamilton 定理指出

𝑝𝐴(𝐴)=𝐴𝑛+𝑐1𝐴𝑛−1+⋯+𝑐𝑛−1𝐴+𝑐𝑛𝐼=𝑂pA(A)=An+c1An−1+⋯+cn−1A+cnI=O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的零矩阵，𝐴 ∈ℂ𝑛×𝑛A∈Cn×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑝𝐴(𝑥) =𝑥𝑛 +∑𝑛𝑖=1𝑐𝑖𝑥𝑛−𝑖 ∈ℂ[𝑥]pA(x)=xn+∑i=1ncixn−i∈C[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征多项式．

若我们要求 𝐴𝐾AK![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 其中 𝐾K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 较大，那么可以求出 𝑓(𝑥) =𝑥𝐾mod𝑝𝐴(𝑥)f(x)=xKmodpA(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后利用 𝑓(𝐴) =𝐴𝐾f(A)=AK![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

而 deg⁡(𝑓(𝑥)) <𝑛deg⁡(f(x))<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 显然．我们令 𝑓(𝑥) =∑𝑛−1𝑖=0𝑓𝑖𝑥𝑖f(x)=∑i=0n−1fixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑛 =𝑘𝑚n=km![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

𝑓𝑘𝑚−1𝑥𝑘𝑚−1+⋯+𝑓1𝑥+𝑓0=(⋯(𝑓𝑘𝑚−1𝑥𝑘−1+⋯+𝑓𝑘(𝑚−1))𝑥𝑘+𝑓𝑘(𝑚−1)−1𝑥𝑘−1+⋯+𝑓𝑘(𝑚−2))𝑥𝑘+⋯+𝑓𝑘−1𝑥𝑘−1+⋯+𝑓1𝑥+𝑓0fkm−1xkm−1+⋯+f1x+f0=(⋯(fkm−1xk−1+⋯+fk(m−1))xk+fk(m−1)−1xk−1+⋯+fk(m−2))xk+⋯+fk−1xk−1+⋯+f1x+f0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 𝑘 =√𝑛k=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以发现计算 𝑓(𝐴)f(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大约需要 𝑂(√𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次矩阵与矩阵的乘法．

## 参考文献

  * Rizwana Rehman, Ilse C.F. Ipsen.[La Budde’s Method for Computing Characteristic Polynomials](https://ipsen.math.ncsu.edu/ps/charpoly3.pdf).
  * Marshall Law.[Computing Characteristic Polynomials of Matrices of Structured Polynomials](http://summit.sfu.ca/system/files/iritems1/17301/etd10125_.pdf).
  * Mike Paterson.[On the Number of Nonscalar Multiplications Necessary to Evaluate Polynomials](https://epubs.siam.org/doi/10.1137/0202007).

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/linear-algebra/char-poly.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/linear-algebra/char-poly.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Great-designer](https://github.com/Great-designer), [hly1204](https://github.com/hly1204), [Xeonacid](https://github.com/Xeonacid), [CCXXXI](https://github.com/CCXXXI), [iamtwz](https://github.com/iamtwz), [lyccrius](https://github.com/lyccrius)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
