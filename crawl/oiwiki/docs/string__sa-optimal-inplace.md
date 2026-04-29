# 最优原地后缀排序算法 - OI Wiki

- Source: https://oi-wiki.org/string/sa-optimal-inplace/

# 最优原地后缀排序算法

本章介绍线性时间复杂度的后缀排序的就地算法1（Optimal In-Place Suffix Sorting）．

Warning

本章 **只建议** 在 **非常非常熟悉** SA-IS45的前提下阅读．

## 全局设定

目标字符串 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，后缀数组 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，串的序号从 0 开始，结尾字符是警戒哨，不妨设为 0．

## 在整形字母表上的后缀排序

事实上这一部分可以看成是原地版本的 SA-IS 算法．

因为是原文中细节相对最清楚，实现也较为简单的算法，也是了解后续算法的基础，是本文介绍的重点．

原地化的原理是用重命名的 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代替 S、L 桶，用额外 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的操作代替类型桶．

### 重命名目标串 Pat

简单来说，我们会在不改变后缀大小的相对顺序的前提下，重命名 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用重命名后的 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来取代原来 S、L 桶，来指明桶头或者桶尾．

重命名的方法是将 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 S 型字符替换为所在桶的桶尾索引，L 型字符替换为所在桶的桶头索引．

如下图所示：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝙿𝚊𝚝: 𝟸 𝟷 𝟷 𝟹 𝟹 𝟷 𝟷 𝟹 𝟹 𝟷 𝟸 𝟷 𝟶𝚃𝚢𝚙𝚎: 𝙻 𝚂 𝚂 𝙻 𝙻 𝚂 𝚂 𝙻 𝙻 𝚂 𝙻 𝙻 𝚂𝙱𝚞𝚌𝚔𝚎𝚝:(𝟶) (𝟷 𝟷 𝟷 𝟷 𝟷 𝟷) (𝟸 𝟸) (𝟹 𝟹 𝟹 𝟹)Index: 0 1 2 3 4 5 6 7 8 9 10 11 12Pat: 2 1 1 3 3 1 1 3 3 1 2 1 0Type: L S S L L S S L L S L L SBucket:(0) (1 1  1  1  1  1) (2  2) (3 3  3  3)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

重命名后的 𝙿𝚊𝚝'Pat'![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（之后直接将重命名后的 𝙿𝚊𝚝'Pat'![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称做 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝙿𝚊𝚝': 𝟽 𝟼 𝟼 𝟿 𝟿 𝟼 𝟼 𝟿 𝟿 𝟼 𝟽 𝟷 𝟶Index: 0 1 2 3 4 5 6 7 8 9 10 11 12Pat': 7 6 6 9 9 6 6 9 9 6 7 1 0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于桶内的字符，L 型字符后缀小，作为桶头；而 S 型字符后缀大，作为桶尾，因此保持了后缀大小的相对顺序．

描述一下重命名的具体步骤：

  1. 和 SA-IS 一样，对 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中每个字符计数，计算其前缀和（计数排序），来构建 S/L 桶，只不过这里用 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 盛放这个前缀和；
  2. 从尾到头，扫描 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每个字符，这样只需记录上一个字符的类型，就可以动态地判断每个字符的类型，然后依据前缀和将其重命名．

### 对 LMS 字符排序

这里重点是使用了一个内部计数器的技巧．

#### 初始化

初始的时候将 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 每一项设为 E（EMPTY）．

从尾到头扫描 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果发现是 LMS 字符，𝙿𝚊𝚝[𝚒]Pat[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么就设置 𝚂𝙰[𝙿𝚊𝚝[𝚒]]SA[Pat[i]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的标记：

如果 𝚂𝙰[𝙿𝚊𝚝[𝚒]]SA[Pat[i]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 E，就将其设为 U（UNIQUE）；

如果 𝚂𝙰[𝙿𝚊𝚝[𝚒]]SA[Pat[i]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 U，就将其设为 M（MULTIPLE）；

其他情况，不做处理．

结果如下图所示：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝙿𝚊𝚝: 𝟽 𝟼 𝟼 𝟿 𝟿 𝟼 𝟼 𝟿 𝟿 𝟼 𝟽 𝟷 𝟶𝙻𝙼𝚂: ∗ * * * 𝚂𝙰:(𝚄――) (𝙴) (𝙴 𝙴 𝙴 𝙴 𝙼――) (𝙴 𝙴) (𝙴 𝙴 𝙴 𝙴)Index: 0 1 2 3 4 5 6 7 8 9 10 11 12Pat: 7 6 6 9 9 6 6 9 9 6 7 1 0LMS: ∗  *  *  * SA:(U―) (E) (E  E  E  E  M―) (E  E) (E E  E  E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

#### 把 LMS 字符的索引放入 SA

从尾到头扫描 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，对于 LMS 字符 𝙿𝚊𝚝[𝚒]Pat[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据 𝚂𝙰[𝙿𝚊𝚝[𝚒]]SA[Pat[i]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的符号进行分类讨论：

U：直接让 𝚂𝙰[𝙿𝚊𝚝[𝚒]] = 𝚒SA[Pat[i]] = i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

M：意味着桶中有至少两个 LMS 字符．

  1. 如果桶中有至少三个 LMS 字符： 就把桶中倒数第二个位置作为临时计数器，标志桶中已填充的 LMS 字符数（桶中倒数第一位就是标志 M） 将新的 LMS 字符从倒数第三个位置开始插入，让临时计数器自增 1． 如果发现桶已经满了，就把桶中从桶头到倒数第三个的所有元素向右平移 2 个位置，然后把新元素插入到桶中第二个位置（桶中第一个位置填为 E）

  2. 如果桶中有且只有 2 个 LMS 字符，显然不需要计数器，直接从右到左顺序插入即可．

正常的值：

```text 1 2 3 ``` |  ```text 根据我们之前的讨论，此时不管桶中有两个还是两个以上的 LMS 字符，这都意味着 $\texttt{i}$ 是桶中最后一个待插入的 LMS 字符的位置， 只需要从桶头开始向左扫描，找到第一个标记为 E 的位置，将其设为 $\texttt{i}$． ```   
---|---  
  
最后要从尾到头扫描一遍 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，清除可能残余的特殊符号 M（桶中未被填满，所以 M 和计数器未被覆盖）．

方法是将桶中 LMS 字符如上述步骤一样向右平移 2 位，将左边空出来的位置填为 E．

如下图所示：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝙿𝚊𝚝: 𝟽 𝟼 𝟼 𝟿 𝟿 𝟼 𝟼 𝟿 𝟿 𝟼 𝟽 𝟷 𝟶𝚂𝙰:(𝟷𝟸―――) (𝙴) (𝙴 𝙴 𝙴 𝙴 𝙼) (𝙴 𝙴) (𝙴 𝙴 𝙴 𝙴)𝚂𝙰:(𝟷𝟸) (𝙴) (𝙴 𝙴 𝟿―― 𝟷 𝙼) (𝙴 𝙴) (𝙴 𝙴 𝙴 𝙴)𝚂𝙰:(𝟷𝟸) (𝙴) (𝙴 𝟻―― 𝟿 𝟸 𝙼) (𝙴 𝙴) (𝙴 𝙴 𝙴 𝙴)𝚂𝙰:(𝟷𝟸) (𝙴) (𝟷―― 𝟻 𝟿 𝟹 𝙼) (𝙴 𝙴) (𝙴 𝙴 𝙴 𝙴)𝚂𝙰:(𝟷𝟸) (𝙴) (𝙴 𝙴 𝟷 𝟻 𝟿) (𝙴 𝙴) (𝙴 𝙴 𝙴 𝙴)Index: 0 1 2 3 4 5 6 7 8 9 10 11 12Pat: 7 6 6 9 9 6 6 9 9 6 7 1 0SA:(12―) (E) (E  E  E  E  M) (E  E) (E E  E  E)SA:(12) (E) (E  E  9― 1  M) (E  E) (E E  E  E)SA:(12) (E) (E  5― 9 2  M) (E  E) (E E  E  E)SA:(12) (E) (1― 5 9 3  M) (E  E) (E E  E  E)SA:(12) (E) (E  E  1  5  9) (E  E) (E E  E  E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个阶段，由于每个桶只需要被移动和扫描一次，所以时间复杂度是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 诱导排序 LMS 子串

#### 诱导排序 LMS 前缀

将 LMS 前缀进行诱导排序，同 SA-IS 一样，这部分同后面对后缀的诱导排序完全一样（使用同一个函数），因此这里直接跳过．

这里直接给出排序结果：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝚂𝙰:(𝟷𝟸)(𝟷𝟷) (𝟷 𝟻 𝟿 𝟸 𝟼) (𝟷𝟶 𝟶) (𝟺 𝟾 𝟹 𝟽)Index: 0 1 2 3 4 5 6 7 8 9 10 11 12SA:(12)(11) (1  5  9  2  6) (10  0) (4 8  3  7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

#### 将已排序的 LMS 子串放到 SA 尾部

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝚂𝙰: 𝙴 𝙴 𝙴 𝙴 𝙴 𝙴 𝙴 𝙴 𝙴 𝟷𝟸――― 𝟷―― 𝟻―― 𝟿――Index: 0 1 2 3 4 5 6 7 8 9 10 11 12SA: E  E  E  E  E  E  E  E  E  12― 1― 5― 9―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 构建规模缩减的子目标串 Pat1

从左到右扫描 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 尾部的 LMS 子串，确定其大小关系「重命名」，将 𝚂𝙰[𝚒]SA[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 重命名的值存储在 𝚂𝙰[⌊𝚂𝙰[𝑖]2⌋]SA[⌊SA[i]2⌋]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因为 LMS 字符并不相邻，所以不会有冲突，这样做是将重命名后的值按照所代表的子串在 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的原顺序放置：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝚂𝙰: 𝟷―― 𝙴 𝟷―― 𝙴 𝟸―― 𝙴 𝟶―― 𝙴 𝙴 𝟷𝟸 𝟷 𝟻 𝟿 Index: 0 1 2 3 4 5 6 7 8 9 10 11 12SA: 1― E  1― E  2― E  0― E  E  12  1  5  9 ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后扫描 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，收集这些重命名的值到 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 头部：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝚂𝙰: 𝟷―― 𝟷―― 𝟸―― 𝟶―― 𝙴 𝙴 𝙴 𝙴 𝙴 𝟷𝟸 𝟷 𝟻 𝟿 Index: 0 1 2 3 4 5 6 7 8 9 10 11 12SA: 1― 1― 2― 0― E  E  E  E  E  12  1  5  9 ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 通过递归解决 Pat1，完成对 LMS 后缀的排序

同 SA-IS 一样，递归解决 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 头部的规模缩减的 𝙿𝚊𝚝𝟷Pat1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后缀排序，结果存到 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 尾部：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝚂𝙰: 𝟷 𝟷 𝟸 𝟶 𝙴 𝙴 𝙴 𝙴 𝙴 𝟹―― 𝟶―― 𝟷―― 𝟸――Index: 0 1 2 3 4 5 6 7 8 9 10 11 12SA: 1  1  2  0  E  E  E  E  E  3― 0― 1― 2―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 尾部的 𝚂𝙰𝟷SA1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 挪到 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 头部，重新从尾到头扫描 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将其中 LMS 字符按照在 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的顺序放到 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 尾部：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝚂𝙰: 𝟹―― 𝟶―― 𝟷―― 𝟸―― 𝙴 𝙴 𝙴 𝙴 𝙴 𝟷―― 𝟻―― 𝟿―― 𝟷𝟸―――Index: 0 1 2 3 4 5 6 7 8 9 10 11 12SA: 3― 0― 1― 2― E  E  E  E  E  1― 5― 9― 12―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

依照 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 尾部的「对照表」，将 𝚂𝙰𝟷SA1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 头部的 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 还原为 𝙿𝚊𝚝Pat![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中对应的 LMS 后缀的索引位置：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝚂𝙰:𝟷𝟸――― 𝟷―― 𝟻―― 𝟿―― 𝙴 𝙴 𝙴 𝙴 𝙴 𝟷 𝟻 𝟿 𝟷𝟸 Index: 0 1 2 3 4 5 6 7 8 9 10 11 12SA:12― 1― 5― 9― E  E  E  E  E  1  5  9  12 ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 头部的排好序的 LMS 后缀按顺序放入到对应的桶中（从尾部开始放）：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝚂𝙰:(𝟷𝟸―――) (𝙴) (𝙴 𝙴 𝟷―― 𝟻―― 𝟿――) (𝙴 𝙴) (𝙴 𝙴 𝙴 𝙴)Index: 0 1 2 3 4 5 6 7 8 9 10 11 12SA:(12―) (E) (E  E  1― 5― 9―) (E  E) (E E  E  E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 对 Pat1 中所有的后缀进行诱导排序

这一部分就是利用前面用过的内部计数器技巧，进行原地版的诱导排序．

假如我们已经有排好序的 LMS 后缀（在桶尾），来诱导 L 型后缀2：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝙿𝚊𝚝: 𝟽 𝟼 𝟼 𝟿 𝟿 𝟼 𝟼 𝟿 𝟿 𝟼 𝟽 𝟷 𝟶𝚂𝙰:(𝟷𝟸) (𝙴) (𝙴 𝙴 𝟷 𝟻 𝟿) (𝙴 𝙴) (𝙴 𝙴 𝙴 𝙴)Index: 0 1 2 3 4 5 6 7 8 9 10 11 12Pat: 7 6 6 9 9 6 6 9 9 6 7 1 0SA:(12) (E) (E  E  1  5  9) (E  E) (E E  E  E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如同排序 LMS 字符一样，先对 L 型字符用特殊符号计数：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝙿𝚊𝚝: 𝟽 𝟼 𝟼 𝟿 𝟿 𝟼 𝟼 𝟿 𝟿 𝟼 𝟽 𝟷 𝟶𝚂𝙰:(𝟷𝟸) (𝚄――) (𝙴 𝙴 𝟷 𝟻 𝟿) (𝙼―― 𝙴) (𝙼―― 𝙴 𝙴 𝙴)Index: 0 1 2 3 4 5 6 7 8 9 10 11 12Pat: 7 6 6 9 9 6 6 9 9 6 7 1 0SA:(12) (U―) (E  E  1  5  9) (M― E) (M― E  E  E)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

从左到右扫描 SA，同对 LMS 字符排序一样，复杂一点的是判断 𝚜𝚞𝚏[𝚂𝙰[𝚒] - 𝟷]suf[SA[i] - 1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的类型，需要分类讨论（详情参考代码）：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝚂𝙰:(→𝟷𝟸)(𝟷𝟷―――) (𝙴 𝙴 𝟷 𝟻 𝟿) (𝙼 𝙴) (𝙼 𝙴 𝙴 𝙴)𝚂𝙰:(𝟷𝟸)(→𝟷𝟷) (𝙴 𝙴 𝟷 𝟻 𝟿)(𝟷𝟶――― 𝙴) (𝙼 𝙴 𝙴 𝙴)𝚂𝙰:(𝟷𝟸)(𝟷𝟷) (𝙴 𝙴 →𝟷 𝟻 𝟿)(𝟷𝟶 𝟶――) (𝙼 𝙴 𝙴 𝙴)𝚂𝙰:(𝟷𝟸)(𝟷𝟷) (𝙴 𝙴 𝟷 →𝟻 𝟿)(𝟷𝟶 𝟶) (𝙼 𝟷 𝟺―― 𝙴)𝚂𝙰:(𝟷𝟸)(𝟷𝟷) (𝙴 𝙴 𝟷 𝟻 →𝟿)(𝟷𝟶 𝟶) (𝙼 𝟸 𝟺 𝟾――)𝚂𝙰:(𝟷𝟸)(𝟷𝟷) (𝙴 𝙴 𝟷 𝟻 𝟿)(𝟷𝟶 𝟶) (→𝟺 𝟾 𝟹―― 𝙴)𝚂𝙰:(𝟷𝟸)(𝟷𝟷) (𝙴 𝙴 𝟷 𝟻 𝟿)(𝟷𝟶 𝟶) (𝟺 →𝟾 𝟹 𝟽――)Index: 0 1 2 3 4 5 6 7 8 9 10 11 12SA:(12→)(11―) (E E 1 5 9) (M E) (M E E E)SA:(12)(11→) (E E 1 5 9)(10― E) (M E E E)SA:(12)(11) (E E  1→ 5 9)(10  0―) (M E E E)SA:(12)(11) (E E 1  5→ 9)(10 0) (M 1 4― E)SA:(12)(11) (E E 1 5 9→)(10 0) (M 2 4  8―)SA:(12)(11) (E E 1 5 9)(10 0) (4→ 8  3― E)SA:(12)(11) (E E 1 5 9)(10 0) (4  8→ 3  7―)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

区别于 SA-IS 的是，对一个类型字符诱导排序后，需要清理 LMS 字符以免对后面的原地诱导排序：

𝙸𝚗𝚍𝚎𝚡: 𝟶 𝟷 𝟸 𝟹 𝟺 𝟻 𝟼 𝟽 𝟾 𝟿 𝟷𝟶 𝟷𝟷 𝟷𝟸𝚂𝙰:(𝟷𝟸)(𝟷𝟷) (𝙴 𝙴 𝙴―― 𝙴―― 𝙴――)(𝟷𝟶 𝟶) (𝟺 𝟾 𝟹 𝟽)Index: 0 1 2 3 4 5 6 7 8 9 10 11 12SA:(12)(11) (E E  E― E― E―)(10 0) (4 8 3 7)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

至于从 L 后缀诱导 S 后缀与从 LMS 后缀诱导 L 后缀完全对称，这里就不做多余介绍．

到这儿为止，诱导排序就完成了．

#### 实现

时间性能上和 SA-IS 没有显著差别，空间占用变为不到原来的 1313![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（代码量多 1 倍），算是不愧为原文 Optimal In-Place Suffix Sorting1的标题．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 ``` |  ```text use std :: cmp :: max ; use std :: cmp :: Ordering ; use std :: slice :: from_raw_parts_mut ; const LTYPE : bool = false ; const STYPE : bool = true ; const MAX_SA_VALUE : usize = usize :: MAX / 2 ; const EMPTY : usize = MAX_SA_VALUE \+ 1 ; const UNIQUE : usize = MAX_SA_VALUE \+ 2 ; const MULTI : usize = MAX_SA_VALUE \+ 3 ; // >= 258 fn lms_str_cmp < E : Ord > ( l1 : & [ E ], l2 : & [ E ]) -> Ordering { for ( x , y ) in l1 . iter (). zip ( l2 . iter ()) { let cmp_res = x . cmp ( & y ); if cmp_res != Ordering :: Equal { return cmp_res ; } } Ordering :: Equal } #[inline] fn pat_char_type ( cur : usize , prev : usize , last_scanned_type : bool ) -> bool { if cur < prev || cur == prev && last_scanned_type == STYPE { STYPE } else { LTYPE } } fn rename_pat ( pat : & mut [ usize ], sa : & mut [ usize ]) { let patlastpos = pat . len () \- 1 ; // 全部刷成bucket head //sa.fill(0); for i in 0 .. sa . len () { sa [ i ] = 0 } for i in 0 .. pat . len () { sa [ pat [ i ]] += 1 } for i in 1 .. sa . len () { sa [ i ] += sa [ i \- 1 ] } for i in 0 .. pat . len () \- 1 { pat [ i ] = sa [ pat [ i ]] \- 1 ; }; // 将L-suffix刷成bucket head //sa.fill(0); for i in 0 .. sa . len () { sa [ i ] = 0 } for i in 0 .. pat . len () { sa [ pat [ i ]] += 1 } let mut last_scanned_type = STYPE ; pat [ patlastpos ] = 0 ; for i in ( 0 .. pat . len () \- 1 ). rev () { if pat_char_type ( pat [ i ], pat [ i \+ 1 ], last_scanned_type ) == STYPE { last_scanned_type = STYPE ; } else { pat [ i ] -= sa [ pat [ i ]] \- 1 ; last_scanned_type = LTYPE ; } } } fn sort_lms_char ( pat : & mut [ usize ], sa : & mut [ usize ]) -> usize { //sa.fill(EMPTY); for i in 0 .. sa . len () { sa [ i ] = EMPTY } let mut last_scanned_type = STYPE ; for i in ( 0 .. pat . len () \- 1 ). rev () { if pat_char_type ( pat [ i ], pat [ i \+ 1 ], last_scanned_type ) == STYPE { last_scanned_type = STYPE ; } else { if last_scanned_type == STYPE { // pat[i + 1] is LMS type sa [ pat [ i \+ 1 ]] += 1 ; } last_scanned_type = LTYPE ; } } let mut lms_cnt = 0 ; last_scanned_type = STYPE ; for i in ( 0 .. pat . len () \- 1 ). rev () { if pat_char_type ( pat [ i ], pat [ i \+ 1 ], last_scanned_type ) == STYPE { last_scanned_type = STYPE ; } else { let e_i = i \+ 1 ; let e = pat [ e_i ]; if last_scanned_type == STYPE { // pat[i + 1] is LMS type lms_cnt += 1 ; if sa [ e ] == UNIQUE { sa [ e ] = e_i ; } else if sa [ e ] >= MULTI && sa [ e \- 1 ] == EMPTY { if sa [ e \- 2 ] == EMPTY { sa [ e \- 2 ] = e_i ; sa [ e \- 1 ] = 1 ; // set counter } else { // MUL = 2 sa [ e ] = e_i ; sa [ e \- 1 ] = EMPTY ; } } else if sa [ e ] >= MULTI && sa [ e \- 1 ] != EMPTY { let c = sa [ e \- 1 ]; // get counter if sa [ e \- 2 \- c ] == EMPTY { sa [ e \- 2 \- c ] = e_i ; sa [ e \- 1 ] += 1 ; // update counter } else { for j in ( 1 .. c \+ 1 ). rev () { sa [ e \- c \+ j ] = sa [ e \- 2 \- c \+ j ] } sa [ e \- c ] = e_i ; sa [ e \- c \- 1 ] = EMPTY ; } } else if sa [ e ] < EMPTY { for j in ( 0 .. e ). rev () { if sa [ j ] == EMPTY { sa [ j ] = e_i ; break ; } } } } last_scanned_type = LTYPE ; } } for i in ( 0 .. pat . len ()). rev () { if sa [ i ] >= MULTI { let c = sa [ i \- 1 ]; for j in ( 1 .. c \+ 1 ). rev () { // 逆序防止前面的覆盖后面的 sa [ i \- c \+ j ] = sa [ i \- 2 \- c \+ j ]; } sa [ i \- c \- 1 ] = EMPTY ; sa [ i \- c ] = EMPTY ; } } lms_cnt } fn sort_lms_substr ( pat : & mut [ usize ], sa : & mut [ usize ]) { // step 1 induced_sort ( pat , sa ); // step 2 let pat_last_pos = pat . len () \- 1 ; let mut lms_cnt = 0 ; let mut i = pat_last_pos ; let mut bucket_tail_ptr = pat_last_pos \+ 1 ; // for renamed bucket ver let mut bucket = EMPTY ; // 可以省略，但是为了书写代码方便 let mut num = 0 ; // S type number of bucket while i > 0 { if pat [ sa [ i ]] != bucket { // reach new bucket num = 0 ; let mut l = 0 ; while pat [ sa [ i \- l ]] == pat [ sa [ i ]] { // 扫描桶来计算桶中S字符数量，根据定义 当l=i时循环必然终止 let pat_i = sa [ i \- l ]; // l < i, 即 i - l > 0, 0 <= pat_i < patlen - 1 if pat [ pat_i ] < pat [ pat_i \+ 1 ] { let mut k = pat_i ; while k > 0 && pat [ k \- 1 ] == pat [ pat_i ] { k -= 1 } num += pat_i \- k \+ 1 ; } else { break ; // bucket不含S字符，结束扫描 } l += 1 ; } bucket_tail_ptr = i ; bucket = pat [ sa [ bucket_tail_ptr ]]; } if num > 0 && i > bucket_tail_ptr \- num && sa [ i ] > 0 && pat [ sa [ i ]] < pat [ sa [ i ] \- 1 ] { sa [ pat_last_pos \- lms_cnt ] = sa [ i ]; lms_cnt += 1 ; } i -= 1 ; } sa [ pat_last_pos \- lms_cnt ] = sa [ i ]; // i = 0 lms_cnt += 1 ; //sa[0..pat_last_pos - lms_cnt + 1].fill(EMPTY); for i in 0 .. pat_last_pos \- lms_cnt \+ 1 { sa [ i ] = EMPTY } } fn construct_pat1 ( pat : & mut [ usize ], sa : & mut [ usize ], lms_cnt : usize ) -> bool { let patlen = pat . len (); let mut prev_lms_str_len = 1 ; let mut rank = 0 ; sa [( patlen \- 1 ) / 2 ] = rank ; let mut has_duplicated_char = false ; for i in patlen \- lms_cnt \+ 1 .. patlen { // 从警戒哨字符的下一个字符开始 let mut j = sa [ i ]; while pat [ j ] <= pat [ j \+ 1 ] { j += 1 } // 寻找suf(sa[i])右边第一个L字符，因为排除了警戒哨这个LMS后缀，所以必然不会越界 let mut k = j ; while k \+ 1 < patlen && pat [ k ] >= pat [ k \+ 1 ] { k += 1 } // 找到suf(sa[i])右边第一个LMS字符 let cur_lms_str_len = k \+ 1 \- sa [ i ]; let cmp_res = lms_str_cmp ( & pat [ sa [ i ] .. sa [ i ] \+ cur_lms_str_len ], & pat [ sa [ i \- 1 ] .. sa [ i \- 1 ] \+ prev_lms_str_len ]); if cmp_res != Ordering :: Equal { rank += 1 } if rank == sa [ sa [ i \- 1 ] / 2 ] { has_duplicated_char = true ; } let rank_index = sa [ i ] / 2 ; sa [ rank_index ] = rank ; // 整除 prev_lms_str_len = cur_lms_str_len ; } // move to head of sa let mut j = 0 ; for i in 0 .. patlen \- lms_cnt { if sa [ i ] != EMPTY { sa [ j ] = sa [ i ]; if i > j { sa [ i ] = EMPTY ; } j += 1 ; } } //sa[lms_cnt..patlen].fill(EMPTY); for i in lms_cnt .. patlen { sa [ i ] = EMPTY } has_duplicated_char } fn sort_lms_suf ( pat : & mut [ usize ], sa : & mut [ usize ], lms_cnt : usize , has_duplicated_char : bool ) { // solve T1 recursively let patlen = pat . len (); let salen = sa . len (); unsafe { let sa_ptr = sa . as_mut_ptr (); let mut pat1 = from_raw_parts_mut ( sa_ptr , lms_cnt ); let mut sa1 = from_raw_parts_mut ( sa_ptr . offset (( patlen \- lms_cnt ) as isize ), salen \- ( patlen \- lms_cnt )); if has_duplicated_char { _compute_suffix_array_16_1 ( & mut pat1 , & mut sa1 ); } else { for i in 0 .. lms_cnt { sa1 [ pat1 [ i ]] = i } } } // move SA1 to SA[0...n1-1] for i in 0 .. lms_cnt { sa [ i ] = sa [ patlen \- lms_cnt \+ i ]; } // put all LMS-suffixes in SA tail let mut last_scanned_type = STYPE ; let mut j = 0 ; for i in ( 0 .. pat . len () \- 1 ). rev () { if pat [ i ] < pat [ i \+ 1 ] || pat [ i ] == pat [ i \+ 1 ] && last_scanned_type == STYPE { last_scanned_type = STYPE ; } else { if last_scanned_type == STYPE { sa [ patlen \- 1 \- j ] = i \+ 1 ; j += 1 ; } last_scanned_type = LTYPE ; } } // backward map the LMS-suffixes rank for i in 0 .. lms_cnt { let relative_rank = sa [ i ]; sa [ i ] = sa [ patlen \- lms_cnt \+ relative_rank ]; sa [ patlen \- lms_cnt \+ relative_rank ] = EMPTY ; } let mut tail = EMPTY ; let mut rfp = EMPTY ; for i in ( 1 .. lms_cnt ). rev () { // sa[0] 保持原位 if pat [ sa [ i ]] != tail { tail = pat [ sa [ i ]]; rfp = tail ; } sa [ rfp ] = sa [ i ]; if rfp != i { sa [ i ] = EMPTY } rfp -= 1 ; } } // PASS! fn induced_sort ( pat : & mut [ usize ], sa : & mut [ usize ]) { let patlen = pat . len (); // place L-suff in SA // init let mut last_scanned_type = STYPE ; for i in ( 0 .. patlen \- 1 ). rev () { if pat_char_type ( pat [ i ], pat [ i \+ 1 ], last_scanned_type ) == LTYPE { sa [ pat [ i ]] += 1 ; // >= EMPTY last_scanned_type = LTYPE ; } else { last_scanned_type = STYPE ; } } //place let mut i = 0 ; while i < patlen { if sa [ i ] < EMPTY && sa [ i ] > 0 { let j = sa [ i ] \- 1 ; let mut is_ltype = false ; if pat [ j ] > pat [ j \+ 1 ] { is_ltype = true ; } else if pat [ j ] == pat [ j \+ 1 ] { // 判断sa[i]是否是L后缀的编号 let next_i = sa [ pat [ sa [ i ]]]; if next_i >= MULTI { is_ltype = true ; } else if next_i < EMPTY && pat [ sa [ i ]] \+ 1 < patlen { if sa [ pat [ sa [ i ]] \+ 1 ] == EMPTY { is_ltype = true ; } else if sa [ pat [ sa [ i ]] \+ 1 ] < EMPTY { if pat [ sa [ pat [ sa [ i ]] \+ 1 ]] == pat [ sa [ i ]] { is_ltype = true ; } } } } if is_ltype { if sa [ pat [ j ]] == UNIQUE { sa [ pat [ j ]] = j ; } else if sa [ pat [ j ]] >= MULTI && sa [ pat [ j ] \+ 1 ] == EMPTY { if sa [ pat [ j ]] \- EMPTY > 2 { sa [ pat [ j ] \+ 2 ] = j ; sa [ pat [ j ] \+ 1 ] = 1 ; // set counter } else { sa [ pat [ j ]] = j ; } } else if sa [ pat [ j ]] >= MULTI && sa [ pat [ j ] \+ 1 ] != EMPTY { let e = pat [ j ]; let c = sa [ e \+ 1 ]; let lfp = e \+ c \+ 2 ; if c \+ 2 < sa [ pat [ j ]] \- EMPTY { // 没到bucket尾部 sa [ lfp ] = j ; sa [ e \+ 1 ] += 1 ; // update counter } else { for k in 1 .. c \+ 1 { sa [ e \+ k \- 1 ] = sa [ e \+ k \+ 1 ]; } sa [ e \+ c ] = j ; sa [ e \+ c \+ 1 ] = EMPTY ; if i >= e \+ 2 && i <= e \+ c \+ 1 { i -= 2 ; } } } else if sa [ pat [ j ]] < EMPTY { for k in pat [ j ] .. patlen { if sa [ k ] == EMPTY { sa [ k ] = j ; break ; } } } } } else if sa [ i ] >= MULTI { i += 1 ; } i += 1 ; } // remove LMS-suff form SA, 一个桶里可能有多个LMS后缀 last_scanned_type = STYPE ; for i in ( 0 .. pat . len () \- 1 ). rev () { if pat_char_type ( pat [ i ], pat [ i \+ 1 ], last_scanned_type ) == STYPE { last_scanned_type = STYPE ; } else { if last_scanned_type == STYPE { // pat[i + 1] is LMS type if sa [ pat [ i \+ 1 ]] <= EMPTY { sa [ pat [ i \+ 1 ]] = UNIQUE ; } else { sa [ pat [ i \+ 1 ]] += 1 ; } } last_scanned_type = LTYPE ; } } i = patlen \- 1 ; while i > 0 { if sa [ i ] > EMPTY { let c = sa [ i ] \- EMPTY ; for k in 0 .. c { sa [ i \- k ] = EMPTY ; } i -= c \- 1 ; } i -= 1 ; } sa [ 0 ] = pat . len () \- 1 ; // place S-suff in SA // init let mut last_scanned_type = STYPE ; for i in ( 0 .. patlen \- 1 ). rev () { if pat_char_type ( pat [ i ], pat [ i \+ 1 ], last_scanned_type ) == STYPE { if sa [ pat [ i ]] >= EMPTY { sa [ pat [ i ]] += 1 ; } else { sa [ pat [ i ]] = UNIQUE ; } last_scanned_type = STYPE ; } else { last_scanned_type = LTYPE ; } } i = patlen \- 1 ; while i > 0 { if sa [ i ] < EMPTY && sa [ i ] > 0 { let j = sa [ i ] \- 1 ; let mut is_stype = false ; if pat [ j ] < pat [ j \+ 1 ] { is_stype = true ; } else if pat [ j ] == pat [ j \+ 1 ] { // 判断sa[i]是否是S后缀的编号 let next_i = sa [ pat [ sa [ i ]]]; if next_i >= MULTI { is_stype = true ; } else if next_i < EMPTY && pat [ sa [ i ]] \- 1 > 0 { if sa [ pat [ sa [ i ]] \- 1 ] == EMPTY { is_stype = true ; } else if sa [ pat [ sa [ i ]] \- 1 ] < EMPTY { if pat [ sa [ pat [ sa [ i ]] \- 1 ]] == pat [ sa [ i ]] { is_stype = true ; } } } } if is_stype { if sa [ pat [ j ]] == UNIQUE { sa [ pat [ j ]] = j ; } else if sa [ pat [ j ]] >= MULTI && sa [ pat [ j ] \- 1 ] == EMPTY { if sa [ pat [ j ]] \- EMPTY > 2 { sa [ pat [ j ] \- 2 ] = j ; sa [ pat [ j ] \- 1 ] = 1 ; // set counter } else { sa [ pat [ j ]] = j ; } } else if sa [ pat [ j ]] >= MULTI && sa [ pat [ j ] \- 1 ] != EMPTY { let e = pat [ j ]; let c = sa [ e \- 1 ]; let num = sa [ pat [ j ]] \- EMPTY ; if c \+ 2 < num { // 没到bucket头部 let rfp = e \- c \- 2 ; sa [ rfp ] = j ; sa [ e \- 1 ] += 1 ; } else { for k in 1 .. c \+ 1 { sa [ e \- k \+ 1 ] = sa [ e \- k \- 1 ]; } sa [ e \- c ] = j ; sa [ e \- c \- 1 ] = EMPTY ; if i >= e \- num \+ 1 && i <= e \- 2 { i += 2 ; } } } else if sa [ pat [ j ]] < EMPTY { for k in ( 0 .. pat [ j ]). rev () { if sa [ k ] == EMPTY { sa [ k ] = j ; break ; } } } } } else if sa [ i ] >= MULTI { i -= 1 ; } i -= 1 ; } } fn _compute_suffix_array_16_1 ( pat : & mut [ usize ], sa : & mut [ usize ]) { rename_pat ( pat , sa ); let lms_cnt = sort_lms_char ( pat , sa ); sort_lms_substr ( pat , sa ); let has_duplicated_char = construct_pat1 ( pat , sa , lms_cnt ); sort_lms_suf ( pat , sa , lms_cnt , has_duplicated_char ); induced_sort ( pat , sa ); } pub fn suffix_array_16 ( pat : & [ u8 ]) -> Vec < usize > { let mut pat = pat . into_iter (). map ( | x | * x as usize ). collect :: < Vec < usize >> (); pat . push ( 0 ); let mut sa = vec! [ 0 ; max ( pat . len (), 256 ) * 1 ]; _compute_suffix_array_16_1 ( & mut pat [ .. ], & mut sa [ .. ]); sa } fn input () -> String { use std :: io ; let mut input = String :: new (); io :: stdin (). read_line ( & mut input ). unwrap (); String :: from ( input . trim ()) } fn main () { let pat = input (); let sa_16 = suffix_array_16 ( pat . as_bytes ()); for i in 1 .. pat . len () \+ 1 { print! ( "{} " , sa_16 [ i ] \+ 1 ) } } ```   
---|---  
  
## 在只读的整形字母表上的后缀排序

使用复杂方法解决复杂问题，通过分治，解决空间紧张的问题．

算法实现的难点在于在 𝚂𝙰SA![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上构建 BitMaps3，来替代本来由重命名后的 T 所指示的指示桶尾/桶头的位置．

这里的 BitMaps 指得是使用比特向量（bit vector）表示的有序字典（multiset），是一种紧凑型结构（compact data structure）．

有兴趣了解的暂时只能阅读原文以及本文引用的 BitMaps 的有关论文自行了解．

## 在只读的一般字母表上的后缀排序

前置知识是归并排序和堆排序．

由于笔者对于其中确定字符类型的方法的时间复杂度有疑问，这里也不再介绍，建议阅读原文自行了解．

## 注解

* * *

  1. Li, Zhize; Li, Jian; Huo, Hongwei (2016)._Optimal In-Place Suffix Sorting_. Proceedings of the 25th International Symposium on String Processing and Information Retrieval (SPIRE). Lecture Notes in Computer Science. 11147. Springer. pp. 268–284. arXiv:1610.08305. doi:10.1007/978-3-030-00479-8_22. ISBN:978-3-030-00478-1. ↩↩

  2. 如果是 LML 后缀，就先诱导 S 型后缀，唯一区别是计算 LML 后缀时需要将警戒哨也算进去． ↩

  3. Gonzalo Navarro and Eliana Providel. Fast, small, simple rank/select on bitmaps. In Proc. 11th International Symposium on Experimental Algorithms (SEA), pages 295–306, 2012. ↩

  4. Ge Nong, Sen Zhang, and Wai Hong Chan. Linear suffix array construction by almost pure induced-sorting. In Data Compression Conference (DCC), pages 193–202. IEEE, 2009. ↩

  5. 推荐阅读 [博文](https://riteme.site/blog/2016-6-19/sais.html) 和它的 [issue 列表](https://github.com/riteme/riteme.github.io/issues/28) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/sa-optimal-inplace.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/sa-optimal-inplace.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [billchenchina](https://github.com/billchenchina), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [ksyx](https://github.com/ksyx), [minghu6](https://github.com/minghu6), [ouuan](https://github.com/ouuan), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
