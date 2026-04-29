# AHU 算法 - OI Wiki

- Source: https://oi-wiki.org/graph/tree-ahu/

# AHU 算法

AHU 算法用于判断两棵有根树是否同构．

判断树同构外还有一种常见的做法是 [树哈希](../tree-hash/)．

前置知识：[树基础](../tree-basic/)，[树的重心](../tree-centroid/)

建议配合参考资料里给的例子观看．

## 树同构的定义

### 有根树同构

对于两棵有根树 𝑇1(𝑉1,𝐸1,𝑟1)T1(V1,E1,r1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2(𝑉2,𝐸2,𝑟2)T2(V2,E2,r2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果存在一个双射 𝜑 :𝑉1 →𝑉2φ:V1→V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得

∀𝑢,𝑣∈𝑉1,(𝑢,𝑣)∈𝐸1⟺(𝜑(𝑢),𝜑(𝑣))∈𝐸2∀u,v∈V1,(u,v)∈E1⟺(φ(u),φ(v))∈E2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**且** 𝜑(𝑟1) =𝑟2φ(r1)=r2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立，那么称有根树 𝑇1(𝑉1,𝐸1,𝑟1)T1(V1,E1,r1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2(𝑉2,𝐸2,𝑟2)T2(V2,E2,r2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构．

### 无根树同构

对于两棵无根树 𝑇1(𝑉1,𝐸1)T1(V1,E1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2(𝑉2,𝐸2)T2(V2,E2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果存在一个双射 𝜑 :𝑉1 →𝑉2φ:V1→V2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得

∀𝑢,𝑣∈𝑉1,(𝑢,𝑣)∈𝐸1⟺(𝜑(𝑢),𝜑(𝑣))∈𝐸2∀u,v∈V1,(u,v)∈E1⟺(φ(u),φ(v))∈E2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

成立，那么称无根树 𝑇1(𝑉1,𝐸1)T1(V1,E1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2(𝑉2,𝐸2)T2(V2,E2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构．

简单的说就是，如果能够通过把树 𝑇1T1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有节点重新标号，使得树 𝑇1T1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和树 𝑇2T2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **完全相同** ，那么称这两棵树同构．

## 问题的转化

无根树同构问题可以转化为有根树同构问题．具体方法如下：

对于无根树 𝑇1(𝑉1,𝐸1)T1(V1,E1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2(𝑉2,𝐸2)T2(V2,E2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，先分别找出它们的 **所有** 重心．

  * 如果这两棵无根树重心数量不同，那么这两棵树不同构．
  * 如果这两颗无根树重心数量都为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，分别记为 𝑐1c1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐2c2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么如果有根树 𝑇1(𝑉1,𝐸1,𝑐1)T1(V1,E1,c1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和有根树 𝑇2(𝑉2,𝐸2,𝑐2)T2(V2,E2,c2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构，那么无根树 𝑇1(𝑉1,𝐸1)T1(V1,E1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2(𝑉2,𝐸2)T2(V2,E2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构，反之则不同构．
  * 如果这两颗无根树重心数量都为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，分别记为 𝑐1,𝑐′1c1,c1′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑐2,𝑐′2c2,c2′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么如果有根树 𝑇1(𝑉1,𝐸1,𝑐1)T1(V1,E1,c1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和有根树 𝑇2(𝑉2,𝐸2,𝑐2)T2(V2,E2,c2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构 **或者** 有根树 𝑇1(𝑉1,𝐸1,𝑐′1)T1(V1,E1,c1′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2(𝑉2,𝐸2,𝑐2)T2(V2,E2,c2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构，那么无根树 𝑇1(𝑉1,𝐸1)T1(V1,E1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2(𝑉2,𝐸2)T2(V2,E2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构，反之则不同构．

所以，只要解决了有根树同构问题，我们就可以把无根树同构问题根据上述方法转化成有根树同构的问题，进而解决无根树同构的问题．

假设有一个可以 𝑂(|𝑉|)O(|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 解决有根树同构问题的算法，那么根据上述方法我们也可以在 𝑂(|𝑉|)O(|V|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内解决无根树同构问题．

## 朴素的 AHU 算法

朴素的 AHU 算法是基于括号序的．

### 原理 1

我们知道一段合法的括号序和一棵有根树唯一对应，而且一棵树的括号序是由它的子树的括号序拼接而成的．如果我们通过改变子树括号序拼接的顺序，从而获得了一段新的括号序，那么新括号序对应的树和原括号序对应的树同构．

### 原理 2

树的同构关系是传递的．既如果 𝑇1T1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2T2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构，𝑇2T2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇3T3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构，那么 𝑇1T1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇3T3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构．

### 推论

考虑求树括号序的递归算法，我们在回溯时拼接子树的括号序．如果在拼接的时候将字典序小的序列先拼接，并将最后的结果记为 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

将以节点 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树的 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为节点 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记为 𝑁𝐴𝑀𝐸(𝑟)NAME(r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么对于有根树 𝑇1(𝑉1,𝐸1,𝑟1)T1(V1,E1,r1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2(𝑉2,𝐸2,𝑟2)T2(V2,E2,r2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果 𝑁𝐴𝑀𝐸(𝑟1) =𝑁𝐴𝑀𝐸(𝑟2)NAME(r1)=NAME(r2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑇1T1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2T2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同构．

### 命名算法

实现 1𝐈𝐧𝐩𝐮𝐭. A rooted tree 𝑇2𝐎𝐮𝐭𝐩𝐮𝐭. The name of rooted tree 𝑇3ASSIGN-NAME(u)4if 𝑢 is a leaf5NAME(𝑢) = (0)6else 7for all child 𝑣 of 𝑢8ASSIGN-NAME(𝑣)9sort the names of the children of 𝑢10concatenate the names of all children 𝑢 to temp11NAME(𝑢) = (temp)1Input. A rooted tree T2Output. The name of rooted tree T3ASSIGN-NAME(u)4if u is a leaf5NAME(u) = (0)6else 7for all child v of u8ASSIGN-NAME(v)9sort the names of the children of u10concatenate the names of all children u to temp11NAME(u) = (temp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### AHU 算法

实现 1𝐈𝐧𝐩𝐮𝐭. Two rooted trees 𝑇1(𝑉1,𝐸1,𝑟1) and 𝑇2(𝑉2,𝐸2,𝑟2)2𝐎𝐮𝐭𝐩𝐮𝐭. Whether these two trees are isomorphic3AHU(𝑇1(𝑉1,𝐸1,𝑟1),𝑇2(𝑉2,𝐸2,𝑟2))4ASSIGN-NAME(𝑟1)5ASSIGN-NAME(𝑟2)6if NAME(𝑟1)=NAME(𝑟2)7return true8else10return false1Input. Two rooted trees T1(V1,E1,r1) and T2(V2,E2,r2)2Output. Whether these two trees are isomorphic3AHU(T1(V1,E1,r1),T2(V2,E2,r2))4ASSIGN-NAME(r1)5ASSIGN-NAME(r2)6if NAME(r1)=NAME(r2)7return true8else10return false![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 复杂度证明

对于一颗有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点的有根树，假设他是链状的，那么节点名字长度最长可以是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 ASSIGN-NAME 算法的复杂度是 1 +2 +⋯ +𝑛1+2+⋯+n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的常数倍，即 Θ(𝑛2)Θ(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，朴素 AHU 算法的复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 优化的 AHU 算法

朴素的 AHU 算法的缺点是树的 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的长度可能会过长，我们可以针对这一点做一些优化．

### 原理 1

对树进行层次划分，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的节点到根的最短距离为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．位于第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的节点的 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以 **只** 由位于第 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的节点的 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拼接得到．

### 原理 2

在同一层内，节点的 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以由其在层内的排名唯一标识．

**注意** ，这里的排名是对两棵树而言的，假设节点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位于第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层，那么节点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的排名等于所有 𝑇1T1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇2T2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的节点中 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比 𝑁𝐴𝑀𝐸(𝑢)NAME(u)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小的节点的个数．

### 推论

我们可以将节点原来的 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用其在层内的排名代替，然后把原来拼接节点 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用向数组加入元素代替．

这样用整数和数组来代替字符串，既不会影响算法的正确性，又很大的降低了算法的复杂度．

### 复杂度证明

首先注意到第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层由拼接得到的 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的总长度为第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层点的度数之和，即第 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的总点数，以下用 𝐿𝑖Li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示．算法的下一步会将这些 𝑁𝐴𝑀𝐸NAME![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 看成字符串（数组）并排序，然后将它们替换为其在层内的排名（即重新映射为一个数）．以下引理表明了对总长为 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符串排序的复杂度：

  1. 我们可以使用基数排序在 𝑂(𝐿 +|Σ|)O(L+|Σ|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内完成排序，其中 |Σ||Σ|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为字符集的大小．（有一些实现细节，参见参考资料）
  2. 我们可以使用快速排序在 𝑂(𝐿log⁡𝑚)O(Llog⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内完成排序．证明的大致思路为快排递归树的高度为 𝑂(log⁡𝑚)O(log⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且暴力比较长度为 ℓ1ℓ1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ℓ2ℓ2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的两个字符串的复杂度为 𝑂(min{ℓ1,ℓ2})O(min{ℓ1,ℓ2})![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在 AHU 算法中，第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层字符串的字符集大小最多为第 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的点数，即 𝐿𝑖Li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以基数排序的复杂度是线性的．根据 ∑𝑖𝐿𝑖 =𝑂(𝑛)∑iLi=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将每层的复杂度相加后可以看出，若使用字符串的基数排序，则算法的总复杂度为 𝑇(𝑛) =𝑂(𝑛)T(n)=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．同理，如果使用快排排序字符串，那么 𝑇(𝑛) =𝑂(𝑛log⁡𝑛)T(n)=O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 例题

[SPOJ-TREEISO](https://www.spoj.com/problems/TREEISO/en/)

题意翻译：给你两颗无根树，判断两棵树是否同构．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 ``` |  ```text // Tree Isomorphism, O(nlogn) // replace quick sort with radix sort ==> O(n) // Author: _Backl1ght #include <algorithm> #include <iostream> #include <vector> using namespace std ; using ll = long long ; constexpr int N = 1e5 \+ 5 ; constexpr int MAXN = N << 1 ; int n ; struct Edge { int v , nxt ; } e [ MAXN << 1 ]; int head [ MAXN ], sz [ MAXN ], f [ MAXN ], maxv [ MAXN ], tag [ MAXN ], tot , Max ; vector < int > center [ 2 ], L [ MAXN ], subtree_tags [ MAXN ]; void addedge ( int u , int v ) { // 建图 e [ tot ]. v = v ; e [ tot ]. nxt = head [ u ]; head [ u ] = tot ++ ; e [ tot ]. v = u ; e [ tot ]. nxt = head [ v ]; head [ v ] = tot ++ ; } void dfs_size ( int u , int fa ) { // 找到 size 值 sz [ u ] = 1 ; maxv [ u ] = 0 ; for ( int i = head [ u ]; i ; i = e [ i ]. nxt ) { int v = e [ i ]. v ; if ( v == fa ) continue ; dfs_size ( v , u ); sz [ u ] += sz [ v ]; maxv [ u ] = max ( maxv [ u ], sz [ v ]); } } void dfs_center ( int rt , int u , int fa , int id ) { maxv [ u ] = max ( maxv [ u ], sz [ rt ] \- sz [ u ]); if ( Max > maxv [ u ]) { center [ id ]. clear (); Max = maxv [ u ]; } if ( Max == maxv [ u ]) center [ id ]. push_back ( u ); // 如果相等就 push_back for ( int i = head [ u ]; i ; i = e [ i ]. nxt ) { int v = e [ i ]. v ; if ( v == fa ) continue ; dfs_center ( rt , v , u , id ); } } int dfs_height ( int u , int fa , int depth ) { // 递归查找 height L [ depth ]. push_back ( u ); f [ u ] = fa ; int h = 0 ; for ( int i = head [ u ]; i ; i = e [ i ]. nxt ) { int v = e [ i ]. v ; if ( v == fa ) continue ; h = max ( h , dfs_height ( v , u , depth \+ 1 )); } return h \+ 1 ; } void init ( int n ) { // 一开始的处理 for ( int i = 1 ; i <= 2 * n ; i ++ ) head [ i ] = 0 ; tot = 1 ; center [ 0 ]. clear (); center [ 1 ]. clear (); int u , v ; for ( int i = 1 ; i <= n \- 1 ; i ++ ) { cin >> u >> v ; addedge ( u , v ); } dfs_size ( 1 , -1 ); Max = n ; dfs_center ( 1 , 1 , -1 , 0 ); for ( int i = 1 ; i <= n \- 1 ; i ++ ) { cin >> u >> v ; addedge ( u \+ n , v \+ n ); } dfs_size ( 1 \+ n , -1 ); Max = n ; dfs_center ( 1 \+ n , 1 \+ n , -1 , 1 ); } bool cmp ( int u , int v ) { return subtree_tags [ u ] < subtree_tags [ v ]; } bool rootedTreeIsomorphism ( int rt1 , int rt2 ) { for ( int i = 0 ; i <= 2 * n \+ 1 ; i ++ ) L [ i ]. clear (), subtree_tags [ i ]. clear (); int h1 = dfs_height ( rt1 , -1 , 0 ); int h2 = dfs_height ( rt2 , -1 , 0 ); if ( h1 != h2 ) return false ; int h = h1 \- 1 ; for ( int j = 0 ; j < ( int ) L [ h ]. size (); j ++ ) tag [ L [ h ][ j ]] = 0 ; for ( int i = h \- 1 ; i >= 0 ; i \-- ) { for ( int j = 0 ; j < ( int ) L [ i \+ 1 ]. size (); j ++ ) { int v = L [ i \+ 1 ][ j ]; subtree_tags [ f [ v ]]. push_back ( tag [ v ]); } sort ( L [ i ]. begin (), L [ i ]. end (), cmp ); for ( int j = 0 , cnt = 0 ; j < ( int ) L [ i ]. size (); j ++ ) { if ( j && subtree_tags [ L [ i ][ j ]] != subtree_tags [ L [ i ][ j \- 1 ]]) ++ cnt ; tag [ L [ i ][ j ]] = cnt ; } } return subtree_tags [ rt1 ] == subtree_tags [ rt2 ]; } bool treeIsomorphism () { if ( center [ 0 ]. size () == center [ 1 ]. size ()) { if ( rootedTreeIsomorphism ( center [ 0 ][ 0 ], center [ 1 ][ 0 ])) return true ; if ( center [ 0 ]. size () > 1 ) return rootedTreeIsomorphism ( center [ 0 ][ 0 ], center [ 1 ][ 1 ]); } return false ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); int T ; cin >> T ; while ( T \-- ) { cin >> n ; init ( n ); cout << ( treeIsomorphism () ? "YES" : "NO" ) << '\n' ; } return 0 ; } ```   
---|---  
  
## 参考资料

本文大部分内容译自 [Paper](http://wwwmayr.in.tum.de/konferenzen/Jass08/courses/1/smal/Smal_Paper.pdf) 和 [Slide](https://logic.pdmi.ras.ru/~smal/files/smal_jass08_slides.pdf)．参考资料里的证明会更加全面和严谨，本文做了一定的简化．

对 AHU 算法的复杂度分析，以及字符串的线性时间基数排序算法可以参见 The Design and Analysis of Computer Algorithms 的 3.2 节 Radix sorting，以及其中的 Example 3.2．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/tree-ahu.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/tree-ahu.md "edit.link.title")  
>  __本页面贡献者：[Backl1ght](https://github.com/Backl1ght), [Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [FinParker](https://github.com/FinParker), [hqztrue](https://github.com/hqztrue), [iamtwz](https://github.com/iamtwz), [kenlig](https://github.com/kenlig), [Menci](https://github.com/Menci)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
