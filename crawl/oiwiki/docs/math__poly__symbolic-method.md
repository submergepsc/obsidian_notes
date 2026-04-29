# 符号化方法 - OI Wiki

- Source: https://oi-wiki.org/math/poly/symbolic-method/

# 符号化方法

符号化方法（symbolic method）是将组合对象快速转换成生成函数的一种方法，我们将考虑对于集合上定义的特定运算，然后导出其对应的生成函数的运算．

我们称一个组合类（或简称为类）为 (A,| ⋅|)(A,|⋅|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为组合对象的集合，函数 | ⋅||⋅|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将每一个组合对象映射为一个非负整数，一般称为大小函数．需要注意的是这个非负整数不能是无限大的．例如对于字符集为 {0,1}{0,1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串，可以将字符串的长度设置为其大小函数；对于树或图可将节点的数量设置为其大小函数，注意这并非绝对，也可能将某些特定节点的大小函数设置为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等．

本文是基于 Analytic Combinatorics 一书第一章的简化．

## 无标号体系

在无标号体系中将使用普通生成函数（OGF）．对于集合 AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 其对应 OGF 记为

𝐴(𝑧)=∑𝛼∈A𝑧|𝛼|=∑𝑛≥0𝑎𝑛𝑧𝑛A(z)=∑α∈Az|α|=∑n≥0anzn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们约定使用同一组的字母表示同一个类对应的生成函数等，例如用 𝑎𝑛an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 [𝑧𝑛]𝐴(𝑧)[zn]A(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即 𝐴(𝑧)A(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 𝑧𝑛zn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数，用 A𝑛An![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中大小函数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对象的集合（所以 𝑎𝑛 =card⁡(A𝑛)an=card⁡(An)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 其中 cardcard![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为基数（cardinality））．

本文将不讨论可容许性（admissibility），读者可参考文献中的内容．

下面将引入两种特殊的组合类和组合对象：

  * 记 𝜖ϵ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中性对象（neutral object）和 E ={𝜖}E={ϵ}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中性类（neutral class），中性对象的大小为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，中性类的 OGF 为 𝐸(𝑧) =1E(z)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 记 ∘∘![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 ∙∙![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为原子对象（atom object）和 Z∘ ={ ∘}Z∘={∘}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 Z∙ ={ ∙}Z∙={∙}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或简写为 ZZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为原子类（atom class），原子对象的大小为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，原子类的 OGF 为 𝑍(𝑧) =𝑧Z(z)=z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于两个组合类 AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 BB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在组合意义上同构记为 A =BA=B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 A ≅BA≅B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但仅当该同构不平凡时才使用后者的记号．

我们有

A≅E×A≅A×EA≅E×A≅A×E![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 ××![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为二元运算，表示集合的笛卡尔积．

### 集合的（不相交）并构造

对于类 AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 BB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的并记为

A+B=(E1×A)+(E2×B)A+B=(E1×A)+(E2×B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如此定义可以不违背集合论中集合不相交的要求，我们可以想象成将 AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的对象染色成红色，将 BB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的对象染色成蓝色．

对应 OGF 为

𝐴(𝑧)+𝐵(𝑧)A(z)+B(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

考虑

𝐴(𝑧)+𝐵(𝑧)=∑𝛼∈A𝑧|𝛼|+∑𝛽∈B𝑧|𝛽|=∑𝑛≥0(𝑎𝑛+𝑏𝑛)𝑧𝑛A(z)+B(z)=∑α∈Az|α|+∑β∈Bz|β|=∑n≥0(an+bn)zn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对应形式幂级数的加法．

### 集合的笛卡尔积构造

对于类 AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 BB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的笛卡尔积记为

A×B={(𝛼,𝛽)∣𝛼∈A,𝛽∈B}A×B={(α,β)∣α∈A,β∈B}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对应 OGF 为

𝐴(𝑧)⋅𝐵(𝑧)A(z)⋅B(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们定义 (𝛼,𝛽)(α,β)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小为其组成部分的大小之和，那么显然也有

𝛾=(𝛼1,𝛼2,…,𝛼𝑛)⟹|𝛾|=|𝛼1|+|𝛼2|+⋯+|𝛼𝑛|γ=(α1,α2,…,αn)⟹|γ|=|α1|+|α2|+⋯+|αn|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以

𝐴(𝑧)⋅𝐵(𝑧)=(∑𝛼∈A𝑧|𝛼|)(∑𝛽∈B𝑧|𝛽|)=∑(𝛼,𝛽)∈(A×B)𝑧|𝛼|+|𝛽|=∑𝑛≥0∑𝑖+𝑗=𝑛𝑎𝑖𝑏𝑗𝑧𝑛A(z)⋅B(z)=(∑α∈Az|α|)(∑β∈Bz|β|)=∑(α,β)∈(A×B)z|α|+|β|=∑n≥0∑i+j=naibjzn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对应形式幂级数的乘法．

### 集合的 Sequence 构造

Sequence 构造生成了所有可能的组合．

例 SEQ⁡({𝑎})={𝜖}+{𝑎}+{(𝑎,𝑎)}+{(𝑎,𝑎,𝑎)}+⋯SEQ⁡({𝑎,𝑏})={𝜖}+{𝑎,𝑏}+{(𝑎,𝑏)}+{(𝑏,𝑎)}+{(𝑎,𝑎)}+{(𝑏,𝑏)}+{(𝑎,𝑏,𝑎)}+{(𝑎,𝑏,𝑏)}+{(𝑎,𝑎,𝑏)}+{(𝑏,𝑏,𝑎)}+{(𝑏,𝑎,𝑏)}+{(𝑏,𝑏,𝑏)}+{(𝑎,𝑎,𝑎)}+{(𝑏,𝑎,𝑎)}+⋯SEQ⁡({a})={ϵ}+{a}+{(a,a)}+{(a,a,a)}+⋯SEQ⁡({a,b})={ϵ}+{a,b}+{(a,b)}+{(b,a)}+{(a,a)}+{(b,b)}+{(a,b,a)}+{(a,b,b)}+{(a,a,b)}+{(b,b,a)}+{(b,a,b)}+{(b,b,b)}+{(a,a,a)}+{(b,a,a)}+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以看到 {(𝑎,𝑏)},{(𝑏,𝑎)}{(a,b)},{(b,a)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这样组成部分的顺序不同的元素被生成了，可以认为 Sequence 构造生成了有序的组合．

我们定义

SEQ⁡(A)=E+A+(A×A)+(A×A×A)+⋯SEQ⁡(A)=E+A+(A×A)+(A×A×A)+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且要求 A0 =∅A0=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是 AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中没有大小为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对象．

对应 OGF 为

𝑄(𝐴(𝑧))=1+𝐴(𝑧)+𝐴(𝑧)2+𝐴(𝑧)3+⋯=11−𝐴(𝑧)Q(A(z))=1+A(z)+A(z)2+A(z)3+⋯=11−A(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 Pólya 准逆（quasi-inversion）．

例：有序有根树（ordered rooted tree）

我们可以使用 Sequence 构造来定义有序有根树，即孩子之间的顺序有意义的有根树，设该组合类为 TT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么一棵树为一个根节点和树的 Sequence，即

T={∙}×SEQ⁡(T)T={∙}×SEQ⁡(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对应 OGF 为

𝑇(𝑧)=𝑧1−𝑇(𝑧)T(z)=z1−T(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

前几项系数为 `0 1 1 2 5 14 42 132 429 1430 4862 16796`，忽略常数项即 OEIS [A000108](http://oeis.org/A000108)．

### 集合的 Multiset 构造

Multiset 构造生成了所有可能的组合，但不区分组成部分的元素之间的顺序．

例 MSET⁡({𝑎})={𝜖}+{𝑎}+{(𝑎,𝑎)}+{(𝑎,𝑎,𝑎)}+⋯MSET⁡({𝑎,𝑏})={𝜖}+{𝑎}+{(𝑎,𝑎)}+{(𝑎,𝑎,𝑎)}+⋯+{𝑏}+{(𝑎,𝑏)}+{(𝑎,𝑎,𝑏)}+⋯+{(𝑏,𝑏)}+{(𝑎,𝑏,𝑏)}+{(𝑎,𝑎,𝑏,𝑏)}+⋯+⋯MSET⁡({a})={ϵ}+{a}+{(a,a)}+{(a,a,a)}+⋯MSET⁡({a,b})={ϵ}+{a}+{(a,a)}+{(a,a,a)}+⋯+{b}+{(a,b)}+{(a,a,b)}+⋯+{(b,b)}+{(a,b,b)}+{(a,a,b,b)}+⋯+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到 {(𝑏,𝑎)},{(𝑎,𝑏,𝑎)}{(b,a)},{(a,b,a)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 SEQ⁡({𝑎,𝑏})SEQ⁡({a,b})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中出现，但在 MSET⁡({𝑎,𝑏})MSET⁡({a,b})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有出现，可以认为 Multiset 生成了无序的组合．

我们定义其递推式为

MSET⁡({𝛼0,𝛼1,…,𝛼𝑛})=MSET⁡({𝛼0,𝛼1,…,𝛼𝑛−1})×SEQ⁡({𝛼𝑛})MSET⁡({α0,α1,…,αn})=MSET⁡({α0,α1,…,αn−1})×SEQ⁡({αn})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即

MSET⁡(A)=∏𝛼∈ASEQ⁡({𝛼})MSET⁡(A)=∏α∈ASEQ⁡({α})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且要求 A0 =∅A0=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．或者也可以给出等价的

MSET⁡(A)=SEQ⁡(A)/𝐑MSET⁡(A)=SEQ⁡(A)/R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝐑R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为等价关系，我们说 (𝛼1,…,𝛼𝑛)𝐑(𝛽1,…,𝛽𝑛)(α1,…,αn)R(β1,…,βn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当存在任一置换 𝜎σ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝛽𝑗 =𝛼𝜎(𝑗)βj=ασ(j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对应 OGF 为

Exp⁡(𝐴(𝑧))=∏𝛼∈A(1−𝑧|𝛼|)−1=∏𝑛≥1(1−𝑧𝑛)−𝑎𝑛Exp⁡(A(z))=∏α∈A(1−z|α|)−1=∏n≥1(1−zn)−an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到

ln⁡(1+𝑧)=𝑧1−𝑧22+𝑧33−⋯=∑𝑛≥1(−1)𝑛−1𝑧𝑛𝑛ln⁡(1+z)=z1−z22+z33−⋯=∑n≥1(−1)n−1znn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且 𝐴(𝑧) =exp⁡(ln⁡(𝐴(𝑧)))A(z)=exp⁡(ln⁡(A(z)))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所以

Exp⁡(𝐴(𝑧))=exp⁡(∑𝑛≥1−𝑎𝑛⋅ln⁡(1−𝑧𝑛))=exp⁡(∑𝑛≥1−𝑎𝑛⋅∑𝑚≥1−𝑧𝑛𝑚𝑚)=exp⁡(𝐴(𝑧)1+𝐴(𝑧2)2+𝐴(𝑧3)3+⋯)Exp⁡(A(z))=exp⁡(∑n≥1−an⋅ln⁡(1−zn))=exp⁡(∑n≥1−an⋅∑m≥1−znmm)=exp⁡(A(z)1+A(z2)2+A(z3)3+⋯)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 ExpExp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 Pólya 指数，也被称为 Euler 变换．

例题 [LOJ 6268. 分拆数](https://loj.ac/p/6268)

**题意** ：令 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示将 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行分拆的方案数，求 𝑓(1),𝑓(2),…,𝑓(105)f(1),f(2),…,f(105)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对 998244353998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模的值．

**解** ：设全体正整数类为 II![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 I =SEQ≥1⁡(Z) =Z ×SEQ⁡(Z)I=SEQ≥1⁡(Z)=Z×SEQ⁡(Z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（下标 ≥1≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为有限制的构造，见后文）．所求即

MSET⁡(I)MSET⁡(I)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对应 OGF 前几项系数为 `1 2 3 5 7 11 15 22 30 42`（忽略常数项）即 OEIS [A000041](https://oeis.org/A000041)．

例题 [洛谷 P4389 付公主的背包](https://www.luogu.com.cn/problem/P4389)

**题意** ：给出 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种体积分别为 𝑣1,…,𝑣𝑛v1,…,vn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的商品和正整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求体积为 1,2,…,𝑚1,2,…,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的背包装满的方案数（商品数量不限，有同体积的不同种商品）对 998244353998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模的值．约定 1 ≤𝑛,𝑚 ≤1051≤n,m≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 1 ≤𝑣𝑖 ≤𝑚1≤vi≤m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**解** ：设商品的组合类为 AA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所求即 MSET⁡(A)MSET⁡(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应 OGF 的系数．

例题 [洛谷 P5900 无标号无根树计数](https://www.luogu.com.cn/problem/P5900)

**题意** ：求出 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点的无标号无根树的个数对 998244353998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模的值．约定 1 ≤𝑛 ≤2 ×1051≤n≤2×105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**解** ：设无标号有根树的组合类为 TT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么

T={∙}×MSET⁡(T)T={∙}×MSET⁡(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据 Richard Otter 的论文 [The Number of Trees](https://users.math.msu.edu/users/magyarp/Math482/Otter-Trees.pdf) 中的描述，对应无根树的 OGF 为

𝑇(𝑧)−12𝑇2(𝑧)+12𝑇(𝑧2)T(z)−12T2(z)+12T(z2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

前几项系数为 `1 1 1 2 3 6 11 23 47 106`（忽略常数项）即 OEIS [A000055](https://oeis.org/A000055)．

### 集合的 Powerset 构造

Powerset 构造生成了所有子集．

例 PSET⁡({𝑎})={𝜖}+{𝑎}PSET⁡({𝑎,𝑏})={𝜖}+{𝑎}+{𝑏}+{(𝑎,𝑏)}PSET⁡({𝑎,𝑏,𝑐})={𝜖}+{𝑎}+{𝑏}+{(𝑎,𝑏)}+{𝑐}+{(𝑎,𝑐)}+{(𝑏,𝑐)}+{(𝑎,𝑏,𝑐)}PSET⁡({a})={ϵ}+{a}PSET⁡({a,b})={ϵ}+{a}+{b}+{(a,b)}PSET⁡({a,b,c})={ϵ}+{a}+{b}+{(a,b)}+{c}+{(a,c)}+{(b,c)}+{(a,b,c)}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们定义其递推式为

PSET⁡({𝛼0,𝛼1,…,𝛼𝑛})=PSET⁡({𝛼0,𝛼1,…,𝛼𝑛−1})×({𝜖}+{𝛼𝑛})PSET⁡({α0,α1,…,αn})=PSET⁡({α0,α1,…,αn−1})×({ϵ}+{αn})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即

PSET⁡(A)≅∏𝛼∈A({𝜖}+{𝛼})PSET⁡(A)≅∏α∈A({ϵ}+{α})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

且要求 A0 =∅A0=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对应 OGF 为

―――Exp(𝐴(𝑧))=∏𝛼∈A(1+𝑧|𝛼|)=∏𝑛≥1(1+𝑧𝑛)𝑎𝑛=exp⁡(∑𝑛≥1𝑎𝑛⋅ln⁡(1+𝑧𝑛))=exp⁡(∑𝑛≥1𝑎𝑛⋅∑𝑚≥1(−1)𝑚−1𝑧𝑛𝑚𝑚)=exp⁡(𝐴(𝑧)1−𝐴(𝑧2)2+𝐴(𝑧3)3−⋯)Exp―(A(z))=∏α∈A(1+z|α|)=∏n≥1(1+zn)an=exp⁡(∑n≥1an⋅ln⁡(1+zn))=exp⁡(∑n≥1an⋅∑m≥1(−1)m−1znmm)=exp⁡(A(z)1−A(z2)2+A(z3)3−⋯)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 ―――ExpExp―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 Pólya 指数·改．

容易发现 PSET⁡(A) ⊂MSET⁡(A)PSET⁡(A)⊂MSET⁡(A)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 集合的 Cycle 构造

Cycle 构造生成了所有可能的组合，但不区分仅轮换不同的组合．

我们定义为

CYC⁡(A)=(SEQ⁡(A)∖{𝜖})/𝐒CYC⁡(A)=(SEQ⁡(A)∖{ϵ})/S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝐒S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为等价关系，我们说 (𝛼1,…,𝛼𝑛)𝐒(𝛽1,…,𝛽𝑛)(α1,…,αn)S(β1,…,βn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当且仅当存在任一循环移位 𝜏τ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对于所有 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都满足 𝛽𝑗 =𝛼𝜏(𝑗)βj=ατ(j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

例

为了简便我们令 𝚊,𝚋a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为大小为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符，这里仅列举大小为 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串：

CYC⁡({𝚊,𝚋})3={𝚊𝚊𝚊}+{𝚊𝚊𝚋}+{𝚊𝚋𝚋}+{𝚋𝚋𝚋}CYC⁡({a,b})3={aaa}+{aab}+{abb}+{bbb}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝚊𝚊𝚋𝐒𝚋𝚊𝚊𝐒𝚊𝚋𝚊aabSbaaSaba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只保留其一，同样的 𝚊𝚋𝚋𝐒𝚋𝚊𝚋𝐒𝚋𝚋𝚊abbSbabSbba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只保留其一．

CYC⁡({𝚊,𝚋})4={𝚊𝚊𝚊𝚊}+{𝚊𝚊𝚊𝚋}+{𝚊𝚊𝚋𝚋}+{𝚊𝚋𝚋𝚋}+{𝚋𝚋𝚋𝚋}+{𝚊𝚋𝚊𝚋}CYC⁡({a,b})4={aaaa}+{aaab}+{aabb}+{abbb}+{bbbb}+{abab}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝚊𝚊𝚊𝚋𝐒𝚋𝚊𝚊𝚊𝐒𝚊𝚋𝚊𝚊𝐒𝚊𝚊𝚋𝚊aaabSbaaaSabaaSaaba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝚊𝚊𝚋𝚋𝐒𝚋𝚊𝚊𝚋𝐒𝚋𝚋𝚊𝚊𝐒𝚊𝚋𝚋𝚊aabbSbaabSbbaaSabba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝚊𝚋𝚋𝚋𝐒𝚋𝚊𝚋𝚋𝐒𝚋𝚋𝚊𝚋𝐒𝚋𝚋𝚋𝚊abbbSbabbSbbabSbbba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝚊𝚋𝚊𝚋𝐒𝚋𝚊𝚋𝚊ababSbaba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对应 OGF 为

Log⁡(𝐴(𝑧))=∑𝑛≥1𝜑(𝑛)𝑛ln⁡11−𝐴(𝑧𝑛)Log⁡(A(z))=∑n≥1φ(n)nln⁡11−A(zn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝜑φ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 Euler 函数，LogLog![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 Pólya 对数．

由于证明较复杂，读者可参考 Flajolet 的论文 [The Cycle Construction](https://epubs.siam.org/doi/10.1137/0404006) 或 Analytic Combinatorics 的附录．

### 有限制的构造

对于上述所有构造，我们都没有限制其「组成部分」的个数，若在 SEQSEQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的下标给一个作用于整数的谓词用于约束其组成部分，如

SEQ=𝑘⁡(B),SEQ≥𝑘⁡(B),SEQ1..𝑘⁡(B)SEQ=k⁡(B),SEQ≥k⁡(B),SEQ1..k⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 SEQ=𝑘⁡(B)SEQ=k⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也常简写为 SEQ𝑘⁡(B)SEQk⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，SEQ1..𝑘⁡(B)SEQ1..k⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示在区间 [1..𝑘][1..k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上．

令 𝔎K![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为任意上述 SEQ,PSET,MSET,CYCSEQ,PSET,MSET,CYC![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之一，以及

A=𝔎𝑘(B)A=Kk(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即我们需要对于 𝛼 ∈Aα∈A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有

𝛼={(𝛽1,𝛽2,…,𝛽𝑘)∣𝛽∈B}α={(β1,β2,…,βk)∣β∈B}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

设 𝜒χ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 函数作用于组合对象上为其组成部分的个数，也就是要令 𝜒(𝛼) =𝑘χ(α)=k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不妨增加一元来「跟踪」组成部分的个数．

令

𝐴𝑛,𝑘=card⁡{𝛼∈A∣|𝛼|=𝑛,𝜒(𝛼)=𝑘}An,k=card⁡{α∈A∣|α|=n,χ(α)=k}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么

𝐴(𝑧,𝑢)=∑𝑛,𝑘𝐴𝑛,𝑘𝑢𝑘𝑧𝑛=∑𝛼∈A𝑧|𝛼|𝑢𝜒(𝛼)A(z,u)=∑n,kAn,kukzn=∑α∈Az|α|uχ(α)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后我们只要提取出 𝑢𝑘uk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的系数即可获得对应表达式，例如 A =SEQ𝑘⁡(B)A=SEQk⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可直接导出

𝐴(𝑧,𝑢)=∑𝑘≥0𝑢𝑘𝐵(𝑧)𝑘=11−𝑢𝐵(𝑧)⟹𝐴(𝑧)=𝐵(𝑧)𝑘A(z,u)=∑k≥0ukB(z)k=11−uB(z)⟹A(z)=B(z)k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

显然也有

A=SEQ≥𝑘⁡(B)⟹𝐴(𝑧)=𝐵(𝑧)𝑘1−𝐵(𝑧)A=SEQ≥k⁡(B)⟹A(z)=B(z)k1−B(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

而对于 MSET𝑘⁡(B)MSETk⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 PSET𝑘⁡(B)PSETk⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已经有

𝐴(𝑧,𝑢)=∏𝑛(1−𝑢𝑧𝑛)−𝑏𝑛⟹𝐴(𝑧)=[𝑢𝑘]exp⁡(𝑢1𝐵(𝑧)+𝑢22𝐵(𝑧2)+𝑢33𝐵(𝑧3)+⋯)A(z,u)=∏n(1−uzn)−bn⟹A(z)=[uk]exp⁡(u1B(z)+u22B(z2)+u33B(z3)+⋯)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

和

𝐴(𝑧,𝑢)=∏𝑛(1+𝑢𝑧𝑛)𝑏𝑛⟹𝐴(𝑧)=[𝑢𝑘]exp⁡(𝑢1𝐵(𝑧)−𝑢22𝐵(𝑧2)+𝑢33𝐵(𝑧3)−⋯)A(z,u)=∏n(1+uzn)bn⟹A(z)=[uk]exp⁡(u1B(z)−u22B(z2)+u33B(z3)−⋯)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对于 CYC𝑘⁡(B)CYCk⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同理．

使用上式计算 MSET3⁡(B)MSET3⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 MSET4⁡(B)MSET4⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应 OGF

尝试计算 A =MSET3⁡(B)A=MSET3⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

[𝑢3]𝐴(𝑧,𝑢)=10!([𝑢3]1)+11!([𝑢3](𝑢1𝐵(𝑧)+𝑢22𝐵(𝑧2)+𝑢33𝐵(𝑧3)+⋯))+12!([𝑢3](𝑢1𝐵(𝑧)+𝑢22𝐵(𝑧2)+⋯)2)+13!([𝑢3](𝑢1𝐵(𝑧)+⋯)3)=𝐵(𝑧)36+𝐵(𝑧)𝐵(𝑧2)2+𝐵(𝑧)33[u3]A(z,u)=10!([u3]1)+11!([u3](u1B(z)+u22B(z2)+u33B(z3)+⋯))+12!([u3](u1B(z)+u22B(z2)+⋯)2)+13!([u3](u1B(z)+⋯)3)=B(z)36+B(z)B(z2)2+B(z)33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

尝试计算 A =MSET4⁡(B)A=MSET4⁡(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为

[𝑢4]𝐴(𝑧,𝑢)=10!([𝑢4]1)+11!([𝑢4](𝑢1𝐵(𝑧)+𝑢22𝐵(𝑧2)+𝑢33𝐵(𝑧3)+𝑢44𝐵(𝑧4)+⋯))+12!([𝑢4](𝑢1𝐵(𝑧)+𝑢22𝐵(𝑧2)+𝑢33𝐵(𝑧3)+⋯)2)+13!([𝑢4](𝑢1𝐵(𝑧)+𝑢22𝐵(𝑧2)+⋯)3)+14!([𝑢4](𝑢1𝐵(𝑧)+⋯)4)=𝐵(𝑧4)4+12!(𝐵(𝑧2)24+2𝐵(𝑧)𝐵(𝑧3)3)+13!(3𝐵(𝑧)2𝐵(𝑧2)2)+𝐵(𝑧)44!=𝐵(𝑧)424+𝐵(𝑧)2𝐵(𝑧2)4+𝐵(𝑧)𝐵(𝑧3)3+𝐵(𝑧2)28+𝐵(𝑧4)4[u4]A(z,u)=10!([u4]1)+11!([u4](u1B(z)+u22B(z2)+u33B(z3)+u44B(z4)+⋯))+12!([u4](u1B(z)+u22B(z2)+u33B(z3)+⋯)2)+13!([u4](u1B(z)+u22B(z2)+⋯)3)+14!([u4](u1B(z)+⋯)4)=B(z4)4+12!(B(z2)24+2B(z)B(z3)3)+13!(3B(z)2B(z2)2)+B(z)44!=B(z)424+B(z)2B(z2)4+B(z)B(z3)3+B(z2)28+B(z4)4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们发现 A =𝔎𝑘(B)A=Kk(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中 𝐴(𝑧)A(z)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是关于 𝐵(𝑧),𝐵(𝑧2),…,𝐵(𝑧𝑘)B(z),B(z2),…,B(zk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个表达式．

需要注意的是对于有限制的构造 𝔎𝑘(B)Kk(B)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并没有要求 B0 =∅B0=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

常用有限制的构造 PSET2⁡(A):𝐴(𝑧)22−𝐴(𝑧2)2MSET2⁡(A):𝐴(𝑧)22+𝐴(𝑧2)2CYC2⁡(A):𝐴(𝑧)22+𝐴(𝑧2)2PSET2⁡(A):A(z)22−A(z2)2MSET2⁡(A):A(z)22+A(z2)2CYC2⁡(A):A(z)22+A(z2)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) PSET3⁡(A):𝐴(𝑧)36−𝐴(𝑧)𝐴(𝑧2)2+𝐴(𝑧3)3MSET3⁡(A):𝐴(𝑧)36+𝐴(𝑧)𝐴(𝑧2)2+𝐴(𝑧3)3CYC3⁡(A):𝐴(𝑧)33+2𝐴(𝑧3)3PSET3⁡(A):A(z)36−A(z)A(z2)2+A(z3)3MSET3⁡(A):A(z)36+A(z)A(z2)2+A(z3)3CYC3⁡(A):A(z)33+2A(z3)3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) PSET4⁡(A):𝐴(𝑧)424−𝐴(𝑧)2𝐴(𝑧2)4+𝐴(𝑧)𝐴(𝑧3)3+𝐴(𝑧2)28−𝐴(𝑧4)4MSET4⁡(A):𝐴(𝑧)424+𝐴(𝑧)2𝐴(𝑧2)4+𝐴(𝑧)𝐴(𝑧3)3+𝐴(𝑧2)28+𝐴(𝑧4)4CYC4⁡(A):𝐴(𝑧)44+𝐴(𝑧2)24+𝐴(𝑧4)2PSET4⁡(A):A(z)424−A(z)2A(z2)4+A(z)A(z3)3+A(z2)28−A(z4)4MSET4⁡(A):A(z)424+A(z)2A(z2)4+A(z)A(z3)3+A(z2)28+A(z4)4CYC4⁡(A):A(z)44+A(z2)24+A(z4)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上面的计算方法虽然有效但比较麻烦，读者可阅读 WolframMathWorld 网站的 [Pólya Enumeration Theorem](https://mathworld.wolfram.com/PolyaEnumerationTheorem.html) 和 [Cycle Index](https://mathworld.wolfram.com/CycleIndex.html) 等相关资料，后者 Cycle Index 在 OEIS 的生成函数表达式中也经常出现．

例题 [LOJ 6538. 烷基计数 加强版 加强版](https://loj.ac/p/6538)

**题意** ：求出 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点的有根且根节点度数不超过 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其余节点度数不超过 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的无序树的个数对 998244353998244353![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模的值．约定 1 ≤𝑛 ≤1051≤n≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**解** ：设组合类为 TT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

T={∙}×MSET0,1,2,3⁡(T)T={∙}×MSET0,1,2,3⁡(T)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

或令组合类 ˆT =T +{𝜖}T^=T+{ϵ}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 那么

ˆT={𝜖}+{∙}×MSET3⁡(ˆT)T^={ϵ}+{∙}×MSET3⁡(T^)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可得到相同的结果．

## 参考文献

  * Philippe Flajolet and Robert Sedgewick.[Analytic Combinatorics](http://algo.inria.fr/flajolet/Publications/books.html).

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/poly/symbolic-method.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/poly/symbolic-method.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest), [Great-designer](https://github.com/Great-designer), [hly1204](https://github.com/hly1204), [myeeye](https://github.com/myeeye), [shuzhouliu](https://github.com/shuzhouliu), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
