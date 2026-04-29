# 置换和排列 - OI Wiki

- Source: https://oi-wiki.org/math/permutation/

# 置换和排列

置换和排列是各类问题中都很常见的概念．

本文讨论的不是排列数

本文讨论的主题是全排列，而不是排列组合中的排列数．排列数的相关内容应当参考 [排列组合](../combinatorics/combination/)．

约定

本文中如果不加说明，总是讨论有限的集合．

## 定义

一个集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到自身的双射（即一一对应）𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个 **置换** （permutation）．如果集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上还具有 [全序](../order-theory/#二元关系) 关系，则它的一个置换也常称作一个 **（全）排列** ．这个全序关系称为集合上的自然顺序．

「置换」与「排列」

在中文语境下，「置换」通常指改变元素顺序，而「排列」通常指将元素排成一列．当元素之间存在自然的顺序时，这两个概念是一回事：「排列」可以看作「置换」的结果；而相较于元素的自然顺序，「排列」中元素的顺序就指定了「置换」．因为本文使用「排列」一词时，总假定集合上存在自然顺序，故而本文中不会特意区分这两个概念．

当然，没有自然顺序的元素也可以进行「排列」．这种「排列」常常出现在组合计数问题中．这超出了本文讨论的范畴．

设集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么，𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的全体置换的数目就是 𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．特别地，0! =10!=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即空集合上有且只有一个置换，也就是空置换．

记号

置换讨论的是元素间的对应关系，而并不关心元素具体是什么．因而，当讨论大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合时，通常假定讨论的集合就是 {1,2,⋯,𝑛}{1,2,⋯,n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；当集合上需要自然顺序的时候，通常假定使用自然数上的自然顺序．

## 表示方法

置换有多种表示方法．这里，以如下置换为例，讨论不同的置换表示方法．

𝜎(1)=2, 𝜎(2)=6, 𝜎(3)=5, 𝜎(4)=4, 𝜎(5)=3, 𝜎(6)=1.σ(1)=2, σ(2)=6, σ(3)=5, σ(4)=4, σ(5)=3, σ(6)=1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 双行记号

集合 𝑋 ={𝑥1,𝑥2,⋯,𝑥𝑛}X={x1,x2,⋯,xn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的置换可以表示为

𝜎=(𝑥1𝑥2⋯𝑥𝑛𝑥𝑝1𝑥𝑝2⋯𝑥𝑝𝑛).σ=(x1x2⋯xnxp1xp2⋯xpn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它表示置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将元素 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 映射到 𝑥𝑝𝑖xpi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这里，当然需要 𝑋 ={𝑥𝑝1,𝑥𝑝2,⋯,𝑥𝑝𝑛}X={xp1,xp2,⋯,xpn}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．置换的双行记号表示中，首行的元素出现顺序并不重要，重要的是两行之间的对应关系．

比如说，前文的例子可以按照双行记号写作

𝜎=(123456265431),σ=(123456265431),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当然，也可以写作

𝜎=(654321134562).σ=(654321134562).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 单行记号

很多时候，集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上有自然顺序．如果在双行记号中默认首行按照自然的顺序书写，并省略首行，那么，置换可以表示为

𝜎=𝜎(1)𝜎(2)⋯𝜎(𝑛).σ=σ(1)σ(2)⋯σ(n).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这更像自然语言中排列的概念．所以，有时候排列会用来称呼这个有序组．

前文的例子利用单行记号可以写作

𝜎=265431.σ=265431.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这种单行的记号，常用来比较不同排列的大小．

### 轮换表示

置换还有一种更为紧凑的表达方式，称为置换的轮换表示．它将置换表示为一系列不相交的轮换的乘积．下面描述将给定置换写成轮换表示的步骤．

给定一个置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以通过如下步骤写成轮换表示：

  1. 如果 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中还有未曾写下的元素，就写下一个左括号，并写下任意一个这样的元素；
  2. 当前一个写下的元素是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，
     * 如果 𝜎(𝑥)σ(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已经在前面写下过，就写上右括号，并返回步骤 1；
     * 如果 𝜎(𝑥)σ(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还没有写下过，就写下 𝜎(𝑥)σ(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并继续步骤 2；
  3. 直到 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有元素都已经写下，结束．

每一对括号中，都是一个轮换．括号中的元素个数，称为对应轮换的长度．实践中，常常省略掉长度为一的轮换．

前文的例子利用轮换表示可以写作

𝜎=(126)(35)(4)=(126)(35).σ=(126)(35)(4)=(126)(35).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

恒等变换中所有的轮换长度都是一，常常记作 (1)(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 而不是全部省略．

## 复合

置换的复合就是映射的复合．置换的复合也常常称作置换的乘法．

给定两个置换

𝜎=(𝑥1𝑥2⋯𝑥𝑛𝑥𝑝1𝑥𝑝2⋯𝑥𝑝𝑛), 𝜋=(𝑥𝑝1𝑥𝑝2⋯𝑥𝑝𝑛𝑥𝑞1𝑥𝑞2⋯𝑥𝑞𝑛),σ=(x1x2⋯xnxp1xp2⋯xpn), π=(xp1xp2⋯xpnxq1xq2⋯xqn),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么，它们的乘积 𝜋 ∘𝜎π∘σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值为

𝜋∘𝜎=(𝑥1𝑥2⋯𝑥𝑛𝑥𝑞1𝑥𝑞2⋯𝑥𝑞𝑛).π∘σ=(x1x2⋯xnxq1xq2⋯xqn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

简单来说就是先经过 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的映射，再经过 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的映射．注意在上面的双行记号中，内层映射 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第二行的顺序和外层映射 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第一行的顺序一致．

因为置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜋π![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 本质是两个映射，所以 (𝜋 ∘𝜎)(𝑥) =𝜋(𝜎(𝑥))(π∘σ)(x)=π(σ(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．置换的复合的运算顺序是自右向左的．置换的乘法并不满足交换律，所以使用错误的顺序计算可能会导致错误的结果．

连续多个置换的乘积称作排列的幂，可以使用 [快速幂](../binary-exponentiation/#多次置换) 加速计算．

### 逆置换

因为置换是双射，所以置换总有相应的逆置换．

给定置换

𝜎=(𝑥1𝑥2⋯𝑥𝑛𝑥𝑝1𝑥𝑝2⋯𝑥𝑝𝑛),σ=(x1x2⋯xnxp1xp2⋯xpn),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它的逆置换就是

𝜎−1=(𝑥𝑝1𝑥𝑝2⋯𝑥𝑝𝑛𝑥1𝑥2⋯𝑥𝑛).σ−1=(xp1xp2⋯xpnx1x2⋯xn).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在轮换表示中，只要对每个轮换取逆，就能得到原来的置换的逆；而对每个轮换取逆，只要把元素的书写顺序倒过来就可以了．比如说，上文中的例子 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的逆置换的轮换表示是

𝜎−1=(621)(53)=(162)(35).σ−1=(621)(53)=(162)(35).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

给定 1 ∼𝑛1∼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个排列和它的每个元素的排名的序列，就互为逆排列．

## 轮换

**轮换** （cycle）本身是特殊的置换．轮换的特性是，从轮换中的任何一点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发，都能通过反复应用置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方式得到轮换中的另一点 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的轮换也称作 **𝑘 k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑轮换**（𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)-cycle）．反复应用 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑轮换 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，将得到恒等变换，即每个元素都回到了最开始的位置．

置换的轮换表示可以看作将置换写成这些特殊置换（即轮换）的乘积，因而置换的轮换表示也可以看作是置换的 **轮换分解** （cycle decomposition）．对于每个置换，它分解成轮换乘积的方式在不计顺序后都是唯一的．轮换可以看作是构成置换的基本单元．

置换的轮换分解有着清晰的几何意义．如果将集合 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的置换中的每个有序对 (𝑥,𝜎(𝑥))(x,σ(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都看成以 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为顶点的有向图的边，那么这些轮换就是这个图上面的环路．如果置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能够分解为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个轮换，就意味着对应的有向图中共计有 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个环路（包括自环）．这些环路自然互不相交．

### 不动点

11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑轮换就是置换的 **不动点** （fixed point）．对于集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，通常用 𝑋𝜎Xσ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的不动点集合，即 𝑋𝜎 ={𝑥 ∈𝑋 :𝜎(𝑥) =𝑥}Xσ={x∈X:σ(x)=x}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 对换

22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑轮换也称作 **对换** （transposition）．也就是说，对换就是只交换了一对元素位置的置换．它的轮换表示是 (𝑥𝑖𝑥𝑗)(xixj)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示它交换了 𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥𝑗xj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置．

任何置换都可以写作一系列对换的乘积．这相当于说，任何顺序的排列都可以通过一系列交换两个元素的操作恢复成指定的正序排列．这正是基于交换的排序算法在做的事情．

更进一步，[冒泡排序算法](../../basic/bubble-sort/) 的正确性其实说明，任何置换都可以写作一系列相邻对换的乘积．这里的 **相邻对换** （adjacent transposition）指的是只交换相邻元素的对换．

## 性质

在应用中，常常需要关注单个置换的性质．

### 奇偶性

将轮换分解成对换的方式并不是唯一的．比如，

(123)=(13)(12)=(12)(23)=(12)(13)(12)(13).(123)=(13)(12)=(12)(23)=(12)(13)(12)(13).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但是，置换分解成一系列对换时，需要的对换的数目的奇偶性是固定的．一个置换的对换分解的数目的奇偶性也称作置换的 **奇偶性** （parity）．

能够分解成偶数个对换的乘积的置换叫做偶置换，能够分解成奇数个对换的乘积的置换叫做奇置换．当 𝑛 ≥2n≥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的奇置换和偶置换的数目相同．

### 符号

根据置换的奇偶性，还可以定义置换的 **符号** （sign），记作 sgn⁡𝜎sgn⁡σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．偶置换的符号定义为 +1+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，奇置换的符号定义为 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

置换的乘积的符号，等于它们的符号的乘积，即

sgn⁡(𝜋∘𝜎)=sgn⁡𝜋⋅sgn⁡𝜎.sgn⁡(π∘σ)=sgn⁡π⋅sgn⁡σ.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是说，两个奇偶性相同的置换的复合是偶置换，两个奇偶性不同的置换的复合是奇置换．这一结论，从对换分解的角度看是显然的．

特别地，单次对换必然改变置换的奇偶性．这也正解释了为什么虽然分解成对换的方式不唯一，但是所需的对换的数目的奇偶性是确定的．

置换的符号出现在 [行列式的 Leibniz 展开](../linear-algebra/determinant/#全排列方法定义) 中．

### 置换的阶

置换的 **阶** （order）是指满足如下条件的最小正整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：重复该置换 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次后，所有元素都回到了原位．即

ord⁡𝜎=min{𝑎∈𝐍+:𝜎𝑎=(1)}.ord⁡σ=min{a∈N+:σa=(1)}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

有限集合上，所有置换的阶都是有限的．这意味着，从起始顺序出发，只要重复按照固定模式打乱给定序列，在有限时间内，总可以将排列恢复原样．

### 置换的型

将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的置换做轮换分解，置换的 **型** （cycle type）就是分解中轮换长度的可重集合．这些轮换的长度构成了一个置换长度 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数分划．如果得到的分解中长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的轮换共计 𝛼𝑘αk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，那么置换的型常记作

1𝛼12𝛼2⋯𝑛𝛼𝑛,1α12α2⋯nαn,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且这些系数满足 ∑𝑛𝑘=1𝑘𝛼𝑘 =𝑛∑k=1nkαk=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

给定置换的型，不同的置换的数目为

𝑛!1𝛼12𝛼2⋯𝑛𝛼𝑛𝛼1!𝛼2!⋯𝛼𝑛!.n!1α12α2⋯nαnα1!α2!⋯αn!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)分析

这是因为，给定任何 1 ∼𝑛1∼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排列，都可以按照置换的型分割成相应的轮换分解．但是，长度相同的轮换之间的顺序并不影响置换，所以总数需要除以 ∏𝑘𝛼𝑘!∏kαk!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．另外，同一轮换内部实际是圆排列，起点的选取也不影响置换，所以需要除以 ∏𝑘𝑘𝛼𝑘∏kkαk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这就得到上式．

如果仅仅给定置换分解成的轮换个数 𝑐(𝜎)c(σ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则不同的置换的数目为 [第一类斯特林数](../combinatorics/stirling/#第一类斯特林数stirling-number) [𝑛𝑘][nk]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．不同的型的个数为置换长度 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 [分拆数](../combinatorics/partition/) 𝑝𝑛pn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

从置换的型，可以方便地确定置换的阶和奇偶性等性质．

因为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑轮换的阶是 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不同的轮换又互不相交，所以置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶就是

lcm⁡{𝑘:𝛼𝑘>0}.lcm⁡{k:αk>0}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

同样地，因为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑轮换的奇偶性与 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的奇偶性相反，所以置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的奇偶性就是

∑𝑘(𝑘−1)𝛼𝑘=∑𝑘𝑘𝛼𝑘−∑𝑘𝛼𝑘=𝑛−𝑐(𝜎)∑k(k−1)αk=∑kkαk−∑kαk=n−c(σ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的奇偶性．这里，𝑐(𝜎)c(σ)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是轮换的个数（包括 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑轮换，即不动点）．

置换的型在 [Pólya 计数](../combinatorics/polya/) 中有重要作用．

## 排列相关

如果集合 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 本身具有自然顺序，此时置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 常称作排列，并用单行记号

𝜎(1)𝜎(2)⋯𝜎(𝑛)σ(1)σ(2)⋯σ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

表示．注意不要同轮换混淆．

### 逆序数

在一个排列中，如果某一个较大的数排在某一个较小的数前面，就说这两个数构成一个 **逆序** （inversion）或反序．这里的比较是在自然顺序下进行的．

在一个排列里出现的逆序的总个数，叫做这个置换的 **逆序数** ．排列的逆序数是它恢复成正序序列所需要做相邻对换的最少次数．因而，排列的逆序数的奇偶性和相应的置换的奇偶性一致．这可以作为置换的奇偶性的等价定义．

求解逆序数的算法，可以使用 [归并排序](../../basic/merge-sort/#逆序对) 或 [树状数组](../../ds/fenwick/#全局逆序对全局二维偏序)，时间复杂度均为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．两种算法的解释详见对应章节，这里给出它们的参考实现．

参考实现

归并排序树状数组

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 ``` |  ```text #include <iostream> #include <vector> // Merge sort and count inversions. long long merge_sort ( std :: vector < int >& nums , int b , int e ) { // Return 0 when length <= 1. if ( e \- b <= 1 ) return 0 ; long long res = 0 ; int m = ( b \+ e ) / 2 ; // Merge_sort two halves. res += merge_sort ( nums , b , m ); res += merge_sort ( nums , m , e ); // Temporary vector to store sorted array. std :: vector < int > tmp ( e \- b ); int i = b , j = m , k = 0 ; while ( i < m && j < e ) { if ( nums [ j ] < nums [ i ]) { tmp [ k ] = nums [ j ++ ]; // In this case, all elements in [i,m) are larger than element j. res += m \- i ; } else { tmp [ k ] = nums [ i ++ ]; } ++ k ; } // Deal with remaining elements. for (; i < m ; ++ i , ++ k ) { tmp [ k ] = nums [ i ]; } for (; j < e ; ++ j , ++ k ) { tmp [ k ] = nums [ j ]; } // Copy back to original vector. for ( i = b , k = 0 ; i < e ; ++ i , ++ k ) { nums [ i ] = tmp [ k ]; } return res ; } int main () { int n ; std :: cin >> n ; std :: vector < int > nums ( n ); for ( int & num : nums ) { std :: cin >> num ; } std :: cout << merge_sort ( nums , 0 , n ); return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 ``` |  ```text #include <algorithm> #include <iostream> #include <unordered_map> #include <vector> // A simple BIT implementation. class BIT { int n ; std :: vector < int > su ; public : BIT ( int n ) : n ( n ), su ( n \+ 1 ) {} // Add v to the x-th number. void add ( int x , int v ) { for (; x <= n ; x += x & ( \- x )) { su [ x ] += v ; } } // Get the cumulative sum till the x-th number. int query ( int x ) { int res = 0 ; for (; x ; x &= x \- 1 ) { res += su [ x ]; } return res ; } }; // Count inversions. long long solve ( const std :: vector < int >& nums ) { // Discretization. std :: vector < int > sorted ( nums ); std :: sort ( sorted . begin (), sorted . end ()); sorted . erase ( std :: unique ( sorted . begin (), sorted . end ()), sorted . end ()); std :: unordered_map < int , int > ids ; int m = sorted . size (); for ( int i = 0 ; i < m ; ++ i ) { // Reverse the order. // Now a smaller id means a larger element. ids [ sorted [ i ]] = m \- i ; } // Main part. BIT bit ( m ); long long res = 0 ; for ( int num : nums ) { int id = ids [ num ]; // Get inversion pair (i,j) with j the current element. // Namely, count the number of elements larger than // the current one but located before it. res += bit . query ( id \- 1 ); // Insert the current element to the BIT. bit . add ( id , 1 ); } return res ; } int main () { int n ; std :: cin >> n ; std :: vector < int > nums ( n ); for ( int & num : nums ) { std :: cin >> num ; } std :: cout << solve ( nums ); return 0 ; } ```   
---|---  
  
### 顺序

排列之间是可以比较大小的．因为每个单行记号就是一个字符串，排列的顺序就是这个字符串上的 [字典序](../../string/basic/#字典序)．

在 C++ 的 STL 库 `<algorithm>` 中可以使用 `prev_permutation` 和 `next_permutation` 分别找到当前排列按照字典序的上一个和下一个排列．

### 排名

将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的排列按照字典序从小到大列举出来，则某一排列在这个序列中的位次就是该排列的排名．它建立了排列和正整数之间的一一对应，常常用于排列相关问题的状态压缩．

在中文竞赛圈，这个排名常称作排列的「康托展开」，但这种名称并不规范．更为严谨的说法是，一个排列的排名的 **康托展开** （Cantor expansion），对应着该排列的 **Lehmer 码** （Lehmer code）．

关于「康托展开」

正如名字所暗示的那样，康托展开是指一种将自然数展开为数列的方法．它可以看作是一种特殊的进制，也叫做 [阶乘进制](../numeral-sys/base/#混合基数进制)．这种进制中，不同的数位对应的底数（radix）并不相同．比如，十进制数 4631046310![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以在阶乘进制中表示为

46310=341010!.46310=341010!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

它表示如下含义

463=3×5!+4×4!+1×3!+0×2!+1×1!+0×0!.463=3×5!+4×4!+1×3!+0×2!+1×1!+0×0!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

康托对于这类混合底数的进制进行了研究，故而自然数在这种进制下的数码表示也常称作自然数的康托展开．

示例

不熟悉排名的计算方法的读者，可以通过这个简单的例子理解下面的算法的基本思路．

要计算排列 𝜎 =452631σ=452631![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排名，就是要计算有多少排列的字典序小于 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再加一．这里的思想类似于 [数位 DP](../../dp/number/)，都是逐位讨论．

  * 第 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的选取要小于 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只能取自 {1,2,3}{1,2,3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，后面 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位可以任意选取，共 3 ×5!3×5!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个可选的排列；
  * 如果第 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位也选择 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么第 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的选取要小于 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只能取自 {1,2,3}{1,2,3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（这里，44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已经选过了），后面的 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位可以任意选取，共 3 ×4!3×4!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个可选的排列；
  * 类似地，前 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的选取和 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同时，第 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的选取要小于 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只能取自 {1}{1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，后面的 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位可以任意选取，共 1 ×3!1×3!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个可选的排列；
  * 前 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的选取和 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同时，第 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的选取要小于 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只能取自 {1,3}{1,3}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，后面的 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位可以任意选取，共 2 ×2!2×2!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个可选的排列；
  * 前 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的选取和 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同时，第 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的选取要小于 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只能取自 {1}{1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，后面的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位可以任意选取，共 1 ×1!1×1!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个可选的排列；
  * 前 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的选取和 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同时，第 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的选择无法得到比 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更小的排列，所以共 0 ×0!0×0!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个可选的排列．

因此，排列 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排名为

1+3×5!+3×4!+1×3!+2×2!+1×1!+0×0!=444.1+3×5!+3×4!+1×3!+2×2!+1×1!+0×0!=444.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于不同的排列，关键的点在于确定阶乘前面的系数．实际上，这些系数正是排在该位置之后却小于该位置元素的元素数目．

从例子中可以知道，求解给定排列的排名的算法，可以分为两步：

  1. 将给定的长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排列转化为它的 Lehmer 码，即长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的序列 𝐿𝜎Lσ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位是

𝐿𝜎(𝑖)=#{𝑗>𝑖:𝜎(𝑗)<𝜎(𝑖)},Lσ(i)=#{j>i:σ(j)<σ(i)},![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

也就是在排列中，排在第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位后面，但是却比 𝜎(𝑖)σ(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小的元素个数．它等于尚未使用的元素中给定元素的排名（减一）．

  2. 将 Lehmar 码看作是自然数的康托展开，求出原来的自然数，并加一．也就是说，最终的排名等于

rank⁡𝜎=1+𝐿𝜎(1)(𝑛−1)!+𝐿𝜎(2)(𝑛−2)!+⋯+𝐿𝜎(𝑛)0!.rank⁡σ=1+Lσ(1)(n−1)!+Lσ(2)(n−2)!+⋯+Lσ(n)0!.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

要求解这一问题的逆问题，即给定排名求解相应的排列，只要将上述过程反过来操作即可．在这一过程中求得的 Lehmer 码中的数字之和，就是排列的逆序数．

编程实现时，关键是要能够快速计算「尚未使用的元素中给定元素的排名」（求排名时）和「尚未使用的元素中给定排名的元素」（求排列时），这些都可以通过 [树状数组](../../ds/fenwick/) 或 [线段树](../../ds/seg/) 等数据结构维护．正反操作的时间复杂度均为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考实现

求给定排列的排名求给定排名的排列

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 ``` |  ```text #include <iostream> #include <vector> // A simple BIT implementation. class BIT { int n ; std :: vector < int > su ; public : BIT ( int n ) : n ( n ), su ( n \+ 1 ) {} // Add v to the x-th number. void add ( int x , int v ) { for (; x <= n ; x += x & ( \- x )) { su [ x ] += v ; } } // Get the cumulative sum till the x-th number. int query ( int x ) { int res = 0 ; for (; x ; x &= x \- 1 ) { res += su [ x ]; } return res ; } }; // Get the rank of a permutation of 1~n. long long find_rank ( const std :: vector < int >& nums ) { int n = nums . size (); BIT bit ( n ); long long fac = 1 ; long long res = 0 ; // Reverse iteration. for ( int i = n \- 1 ; i >= 0 ; \-- i ) { // Count the number of elements smaller than the current one. res += bit . query ( nums [ i ] \- 1 ) * fac ; // Insert the current element into the BIT. bit . add ( nums [ i ], 1 ); // Update the factorial. fac *= n \- i ; } return res \+ 1 ; } int main () { int n ; std :: cin >> n ; std :: vector < int > nums ( n ); for ( int & num : nums ) { std :: cin >> num ; } std :: cout << find_rank ( nums ); return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 ``` |  ```text #include <cmath> #include <iostream> #include <vector> // A simple BIT implementation. class BIT { int n ; std :: vector < int > su ; public : BIT ( int n ) : n ( n ), su ( n \+ 1 ) {} // Fill the BIT with one. void fill () { for ( int x = 1 ; x <= n ; ++ x ) { su [ x ] += x & ( \- x ); } } // Add v to the x-th number. void add ( int x , int v ) { for (; x <= n ; x += x & ( \- x )) { su [ x ] += v ; } } // Get the k-th smallest element. int find_kth ( int k ) { int ps = 0 , x = 0 ; for ( int i = log2 ( n ); i >= 0 ; \-- i ) { x += 1 << i ; if ( x >= n || ps \+ su [ x ] >= k ) { x -= 1 << i ; } else { ps += su [ x ]; } } return x \+ 1 ; } }; // Find the k-th permutation of 1~n. std :: vector < int > find_permutation ( int n , long long k ) { \-- k ; // Expand rank to Lehmer code. std :: vector < int > lehmer ( n ); for ( int i = 1 ; i <= n ; ++ i ) { lehmer [ n \- i ] = k % i ; k /= i ; } BIT bit ( n ); // Set all values in BIT to one. bit . fill (); std :: vector < int > res ( n ); for ( int i = 0 ; i < n ; ++ i ) { // Find the lehmer[i]-th smallest unused element. res [ i ] = bit . find_kth ( lehmer [ i ] \+ 1 ); // Remove it from the BIT. bit . add ( res [ i ], -1 ); } return res ; } int main () { int n ; long long k ; std :: cin >> n >> k ; auto res = find_permutation ( n , k ); for ( int num : res ) { std :: cout << num << ' ' ; } return 0 ; } ```   
---|---  
  
## 参考资料与注释

  * [Permutation - Wikipedia](https://en.wikipedia.org/wiki/Permutation)
  * [Lehmer code - Wikipedia](https://en.wikipedia.org/wiki/Lehmer_code)
  * [Factorial number system - Wikipedia](https://en.wikipedia.org/wiki/Factorial_number_system)

* * *

>  __本页面最近更新： 2026/1/30 14:50:40，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/permutation.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/permutation.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [2008verser](https://github.com/2008verser), [aofall](https://github.com/aofall), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Early0v0](https://github.com/Early0v0), [Great-designer](https://github.com/Great-designer), [Marcythm](https://github.com/Marcythm), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu), [Enter-tainer](https://github.com/Enter-tainer), [gavinliu266](https://github.com/gavinliu266), [gi-b716](https://github.com/gi-b716), [hjsjhn](https://github.com/hjsjhn), [Ir1d](https://github.com/Ir1d), [MegaOwIer](https://github.com/MegaOwIer), [wjy-yy](https://github.com/wjy-yy)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
