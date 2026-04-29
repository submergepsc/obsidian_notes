# Splay 树 - OI Wiki

- Source: https://oi-wiki.org/ds/splay/

# Splay 树

本页面将简要介绍如何用 Splay 维护二叉查找树．

## 定义

**Splay 树** ，或 **伸展树** ，是一种平衡二叉查找树，它通过 **伸展（splay）操作** 不断将某个节点旋转到根节点，使得整棵树仍然满足二叉查找树的性质，能够在均摊 𝑂(log⁡𝑁)O(log⁡N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内完成插入、查找和删除操作，并且保持平衡而不至于退化为链．

Splay 树由 Daniel Sleator 和 Robert Tarjan 于 1985 年发明．

## 基本结构与操作

本节讨论 Splay 树的基本结构和它的核心操作，其中最为重要的是伸展操作．

Splay 树是一棵二叉查找树，查找某个值时满足性质：左子树任意节点的值 <<![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 根节点的值 <<![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 右子树任意节点的值．

### 维护信息

本文使用数组模拟指针来实现 Splay 树，需要维护如下信息：

rt| id| fa[i]| ch[i][0/1]| val[i]| cnt[i]| sz[i]  
---|---|---|---|---|---|---  
根节点编号| 已使用节点个数| 父亲| 左右儿子编号| 节点权值| 权值出现次数| 子树大小  
  
初始化时，所有信息都置零即可．

### 辅助操作

首先是一些简单的辅助操作：

  * `dir(x)`：判断节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是父亲节点的左儿子还是右儿子；
  * `push_up(x)`：在改变节点位置后，根据子节点信息更新节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的信息．

实现

```text 1 2 3 ``` |  ```text bool dir ( int x ) { return x == ch [ fa [ x ]][ 1 ]; } void push_up ( int x ) { sz [ x ] = cnt [ x ] \+ sz [ ch [ x ][ 0 ]] \+ sz [ ch [ x ][ 1 ]]; } ```   
---|---  
  
### 旋转操作

为了使 Splay 保持平衡，需要进行旋转操作．旋转的作用是将某个节点上移一个位置．

旋转需要保证：

  * 整棵 Splay 的中序遍历不变（不能破坏二叉查找树的性质）；
  * 受影响的节点维护的信息依然正确有效；
  * `rt` 必须指向旋转后的根节点．

在 Splay 中旋转分为两种：左旋和右旋．

![](./images/splay-rotate.svg)

观察图示可知，如果要通过旋转将节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（左旋时的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和右旋时的 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）上移，则旋转的方向由该节点是其父节点的左节点还是右节点唯一确定．因此，实现旋转操作时，只需要将要上移的节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 传入即可．

具体分析旋转步骤：（假设需要上移的节点为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以右旋为例）

  1. 首先，记录节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父节点 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以及 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父节点 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（可能为空），并记录 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左子节点还是右子节点；
  2. 按照旋转后的树中自下向上的顺序，依次更新 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左子节点为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右子节点，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右子节点为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以及若 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 非空，𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子节点为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  3. 按照同样的顺序，依次更新当前 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左子节点（若存在）的父节点为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父节点为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以及 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父节点为 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  4. 自下而上维护节点信息．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text void rotate ( int x ) { int y = fa [ x ], z = fa [ y ]; bool r = dir ( x ); ch [ y ][ r ] = ch [ x ][ ! r ]; ch [ x ][ ! r ] = y ; if ( z ) ch [ z ][ dir ( y )] = x ; if ( ch [ y ][ r ]) fa [ ch [ y ][ r ]] = y ; fa [ y ] = x ; fa [ x ] = z ; push_up ( y ); push_up ( x ); } ```   
---|---  
  
在所有函数的实现时，都应注意不要修改节点 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的信息．

### 伸展操作

Splay 树要求每访问一个节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后都要强制将其旋转到根节点．该操作也称为伸展操作．

设刚访问的节点为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．要做伸展操作，就是要对 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做一系列的 **伸展步骤** ．每次对 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做一次伸展步骤，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到根节点的距离都会更近．定义 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父节点．伸展步骤有三种：

  1. **zig** : 在 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是根节点时操作．Splay 树会根据 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 间的边旋转．**zig** 存在是用于处理奇偶校验问题，仅当 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在伸展操作开始时具有奇数深度时作为伸展操作的最后一步执行．

![splay-zig](./images/splay-zig.svg)

即直接将 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 右旋或左旋（图 1, 2）．

![图 1](./images/splay-rotate1.svg)![图 2](./images/splay-rotate2.svg)

  2. **zig-zig** : 在 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是根节点且 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是右侧子节点或都是左侧子节点时操作．下方例图显示了 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是左侧子节点时的情况．Splay 树首先按照连接 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与其父节点 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 边旋转，然后按照连接 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边旋转．

![splay-zig-zig](./images/splay-zig-zig.svg)

即首先将 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 右旋或左旋，然后将 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 右旋或左旋（图 3, 4）．

![图 3](./images/splay-rotate3.svg)![图 4](./images/splay-rotate4.svg)

  3. **zig-zag** : 在 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是根节点且 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一个是右侧子节点一个是左侧子节点时操作．Splay 树首先按 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间的边旋转，然后按 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 新生成的结果边旋转．

![splay-zig-zag](./images/splay-zig-zag.svg)

即将 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 先左旋再右旋或先右旋再左旋（图 5, 6）．

![图 5](./images/splay-rotate5.svg)![图 6](./images/splay-rotate6.svg)

Tip

请读者尝试自行模拟 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种旋转情况，以理解伸展操作的基本思想．

比较三种伸展步骤可知，要区分此时应使用哪种操作，关键是要判断 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否是根节点的子节点，以及 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和它父节点是否在各自的父节点同侧．

此处提供的实现，可以指定任意根节点 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并将它的子树内任意节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上移至 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处：

  1. 首先记录根节点 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父节点 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而可以利用 `fa[x] == w` 判断 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已经位于根结点处；
  2. 记录 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 当前的父节点 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 相同，说明 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已经到达根节点；
  3. 否则，利用 `fa[y] == w` 判断 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否是根节点．如果是，直接做 zig 操作将 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 旋转；如果不是，利用 `dir(x) == dir(y)` 判断使用 zig-zig 还是 zig-zag，前者先旋转 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 再旋转 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，后者直接旋转两次 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实现

```text 1 2 3 4 5 6 7 ``` |  ```text void splay ( int & z , int x ) { int w = fa [ z ]; for ( int y ; ( y = fa [ x ]) != w ; rotate ( x )) { if ( fa [ y ] != w ) rotate ( dir ( x ) == dir ( y ) ? y : x ); } z = x ; } ```   
---|---  
  
伸展操作是 Splay 树的核心操作，也是它的时间复杂度能够得到保证的关键步骤．请务必保证每次向下访问节点后，都进行一次伸展操作．

另外，伸展操作会将当前节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到根节点 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的路径上的所有节点信息自下而上地更新一遍．正是因为这一点，才可以修改非根节点，再通过伸展操作将它上移至根来完成整个树的信息更新．

### 时间复杂度

对大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Splay 树做 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次伸展操作的复杂度是 𝑂((𝑛 +𝑚)log⁡𝑛)O((n+m)log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，单次均摊复杂度是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

基于势能分析的复杂度证明

为此只需分析 **zig** 、**zig-zig** 和 **zig-zag** 三种操作的复杂度．为此，我们采用 **势能分析法** ，通过研究势能的变化来推导操作的均摊复杂度．假设对一棵包含 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点的 Splay 树进行了 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次伸展操作，可以通过如下方式进行分析：

**定义** ：

  1. **单个节点的势能** ：𝑤(𝑥) =log⁡(size(𝑥))w(x)=log⁡(size(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 size(𝑥)size(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示以节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树大小．
  2. **整棵树的势能** ：𝜑 =∑𝑤(𝑥)φ=∑w(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即树中所有节点势能的总和，初始势能满足 𝜑0 ≤𝑛log⁡𝑛φ0≤nlog⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. **第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次操作的均摊成本**：𝑐𝑖 =𝑡𝑖 +𝜑𝑖 −𝜑𝑖−1ci=ti+φi−φi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑡𝑖ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为实际操作代价，𝜑𝑖φi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝜑𝑖−1φi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为操作后和操作前的势能．

**性质** ：

  1. 如果 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父节点，则有 𝑤(𝑝) ≥𝑤(𝑥)w(p)≥w(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即父节点的势能不小于子节点的势能．

  2. 由于根节点的子树大小在操作前后保持不变，因此根节点的势能在操作过程中不变．

  3. 如果 size(𝑝) ≥size(𝑥) +size(𝑦)size(p)≥size(x)+size(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么有 2𝑤(𝑝) −𝑤(𝑥) −𝑤(𝑦) ≥22w(p)−w(x)−w(y)≥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

性质 3 的证明

根据均值不等式可知

2𝑤(𝑝)−𝑤(𝑥)−𝑤(𝑦)=log⁡size(𝑝)2size(𝑥)⋅size(𝑦)>log⁡(size(𝑥)+size(𝑦))2size(𝑥)⋅size(𝑦)≥log⁡4=2.2w(p)−w(x)−w(y)=log⁡size(p)2size(x)⋅size(y)>log⁡(size(x)+size(y))2size(x)⋅size(y)≥log⁡4=2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

接下来，分别对 **zig** 、**zig-zig** 和 **zig-zag** 操作进行势能分析．设操作前后的节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的势能分别是 𝑤(𝑥)w(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑤′(𝑥)w′(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．节点的记号与 上文 一致．

**zig** ：根据性质 1 和 2，有 𝑤(𝑝) =𝑤′(𝑥)w(p)=w′(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑤′(𝑥) ≥𝑤′(𝑝)w′(x)≥w′(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由此，均摊成本为

𝑐𝑖=1+𝑤′(𝑥)+𝑤′(𝑝)−𝑤(𝑥)−𝑤(𝑝)=1+𝑤′(𝑝)−𝑤(𝑥)≤1+𝑤′(𝑥)−𝑤(𝑥).ci=1+w′(x)+w′(p)−w(x)−w(p)=1+w′(p)−w(x)≤1+w′(x)−w(x).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**zig-zig** ：根据性质 1 和 2，有 𝑤(𝑔) =𝑤′(𝑥)w(g)=w′(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑤′(𝑥) ≥𝑤′(𝑝)w′(x)≥w′(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑤(𝑥) ≤𝑤(𝑝)w(x)≤w(p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为

size′(𝑥)=3+size(𝐴)+size(𝐵)+size(𝐶)+size(𝐷)>(1+size(𝐴)+size(𝐵))+(1+size(𝐶)+size(𝐷))=size(𝑥)+size′(𝑔),size′(x)=3+size(A)+size(B)+size(C)+size(D)>(1+size(A)+size(B))+(1+size(C)+size(D))=size(x)+size′(g),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据性质 3 可得

2𝑤′(𝑥)−𝑤(𝑥)−𝑤′(𝑔)≥2.2w′(x)−w(x)−w′(g)≥2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由此，均摊成本为

𝑐𝑖=2+𝑤′(𝑥)+𝑤′(𝑝)+𝑤′(𝑔)−𝑤(𝑥)−𝑤(𝑝)−𝑤(𝑔)=2+𝑤′(𝑝)+𝑤′(𝑔)−𝑤(𝑥)−𝑤(𝑝)≤(2𝑤′(𝑥)−𝑤(𝑥)−𝑤′(𝑔))+𝑤′(𝑝)+𝑤′(𝑔)−𝑤(𝑥)−𝑤(𝑝)=2(𝑤′(𝑥)−𝑤(𝑥))+𝑤′(𝑝)−𝑤(𝑝)≤3(𝑤′(𝑥)−𝑤(𝑥)).ci=2+w′(x)+w′(p)+w′(g)−w(x)−w(p)−w(g)=2+w′(p)+w′(g)−w(x)−w(p)≤(2w′(x)−w(x)−w′(g))+w′(p)+w′(g)−w(x)−w(p)=2(w′(x)−w(x))+w′(p)−w(p)≤3(w′(x)−w(x)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**zig-zag** ：根据性质 1 和 2，有 𝑤(𝑔) =𝑤′(𝑥)w(g)=w′(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑤(𝑝) ≥𝑤(𝑥)w(p)≥w(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 size′(𝑥) >size′(𝑝) +size′(𝑔)size′(x)>size′(p)+size′(g)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据性质 3，可得

2⋅𝑤′(𝑥)−𝑤′(𝑔)−𝑤′(𝑝)≥2.2⋅w′(x)−w′(g)−w′(p)≥2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由此，均摊成本为

𝑐𝑖=2+𝑤′(𝑥)+𝑤′(𝑝)+𝑤′(𝑔)−𝑤(𝑥)−𝑤(𝑝)−𝑤(𝑔)=2+𝑤′(𝑝)+𝑤′(𝑔)−𝑤(𝑥)−𝑤(𝑝)≤(2𝑤′(𝑥)−𝑤′(𝑔)−𝑤′(𝑝))+𝑤′(𝑝)+𝑤′(𝑔)−𝑤(𝑥)−𝑤(𝑝)=2𝑤′(𝑥)−𝑤(𝑥)−𝑤(𝑝)≤2(𝑤′(𝑥)−𝑤(𝑥)).ci=2+w′(x)+w′(p)+w′(g)−w(x)−w(p)−w(g)=2+w′(p)+w′(g)−w(x)−w(p)≤(2w′(x)−w′(g)−w′(p))+w′(p)+w′(g)−w(x)−w(p)=2w′(x)−w(x)−w(p)≤2(w′(x)−w(x)).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

**单次伸展操作** ：

令 𝑤(𝑛)(𝑥) =(𝑤(𝑛−1))′(𝑥)w(n)(x)=(w(n−1))′(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑤(0)(𝑥) =𝑤(𝑥)w(0)(x)=w(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．假设一次伸展操作依次访问了 𝑥1,𝑥2,⋯,𝑥𝑛x1,x2,⋯,xn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等节点，最终 𝑥1x1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成为根节点．这必然经过若干次 **zig-zig** 和 **zig-zag** 操作和至多一次 **zig** 操作，前两种操作的均摊成本均不超过 3(𝑤′(𝑥) −𝑤(𝑥))3(w′(x)−w(x))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而最后一次操作的均摊成本不超过 3(𝑤′(𝑥) −𝑤(𝑥)) +13(w′(x)−w(x))+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以总的均摊成本不超过

3(𝑤(𝑛)(𝑥1)−𝑤(0)(𝑥1))+1≤3log⁡𝑛+1.3(w(n)(x1)−w(0)(x1))+1≤3log⁡n+1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，一次伸展操作的均摊复杂度是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．从而，基于伸展的插入、查询、删除等操作的时间复杂度也为均摊 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**结论** ：

在进行 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次伸展操作之后，实际成本

𝑚∑𝑖=1𝑡𝑖=𝑚∑𝑖=1(𝑐𝑖+𝜑𝑖−1−𝜑𝑖)=𝑚∑𝑖=1𝑐𝑖+𝜑0−𝜑𝑚≤𝑚(3log⁡𝑛+1)+𝑛log⁡𝑛.∑i=1mti=∑i=1m(ci+φi−1−φi)=∑i=1mci+φ0−φm≤m(3log⁡n+1)+nlog⁡n.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次伸展操作的实际时间复杂度为 𝑂((𝑚 +𝑛)log⁡𝑛)O((m+n)log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

为什么 Splay 树的再平衡操作可以获得 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的均摊复杂度？

朴素的再平衡思路就是对节点反复进行旋转操作使其上升，直到它成为根节点．这种朴素思路的问题在于，对于所有子节点都是左（右）节点的链状树来说，它相当于反复进行 **zig** 操作，因而 **zig** 操作的均摊复杂度中的常数项 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 会不断累积，造成最终的均摊复杂度达到 𝑂(log⁡𝑛 +𝑛)O(log⁡n+n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 级别．Splay 树的再平衡操作的设计，避免了连续 **zig** 的情形中的常数累积，使得一次完整的伸展操作中，至多进行一次单独的 **zig** 操作，从而优化了时间复杂度．

## 平衡树操作

本节讨论基于 Splay 树实现平衡树的常见操作的方法．其中，较为重要的是按照值或排名查找元素，它们可以将某个特定的元素找到，并上移至根节点处，以便后续处理．

作为例子，本节将讨论模板题目 [普通平衡树](https://loj.ac/problem/104) 的实现．

### 按照值查找

作为二叉查找树，可以通过值 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 查找到相应的节点，只需要将待查找的值 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和当前节点的值比较即可，找到后将该元素上移至根部即可．

应注意，经常存在树中不存在相应的节点的情形．对于这种情形，要记录最后一个访问的节点（即实现中的 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），并将 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上移至根部．此时，节点 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 存储的值必然要么是所有小于 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素中最大的（即 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前驱），要么是所有大于 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的元素中最小的（即 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后继）．这是因为查找过程保证，左子树总是存储小于 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值，而右子树总是存储大于 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

实现

```text 1 2 3 4 5 ``` |  ```text void find ( int & z , int v ) { int x = z , y = fa [ x ]; for (; x && val [ x ] != v ; x = ch [ y = x ][ v > val [ x ]]); splay ( z , x ? x : y ); } ```   
---|---  
  
该实现允许指定任何节点 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为根节点，并在它的子树内按值查找．

### 按照排名访问

因为记录了子树大小信息，所以 Splay 树还可以通过排名访问元素，即查找树中第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小的元素．

设 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为剩余排名，具体步骤如下：

  * 如果左子树非空且剩余排名 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不大于左子树的大小，那么向左子树查找；
  * 否则，如果 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不大于左子树加上根的大小，那么根节点就是要寻找的；
  * 否则，将 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 减去左子树的和根的大小，继续向右子树查找；
  * 将最终找到的元素上移至根部．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text void loc ( int & z , int k ) { int x = z ; for (;;) { if ( sz [ ch [ x ][ 0 ]] >= k ) { x = ch [ x ][ 0 ]; } else if ( sz [ ch [ x ][ 0 ]] \+ cnt [ x ] >= k ) { break ; } else { k -= sz [ ch [ x ][ 0 ]] \+ cnt [ x ]; x = ch [ x ][ 1 ]; } } splay ( z , x ); } ```   
---|---  
  
该实现需要保证排名 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不超过根 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的树大小．

模板题目中操作 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 要求按照排名返回值，直接调用该方法，并返回值即可．

实现

```text 1 2 3 4 5 ``` |  ```text int find_kth ( int k ) { if ( k > sz [ rt ]) return -1 ; loc ( rt , k ); return val [ rt ]; } ```   
---|---  
  
### 合并操作

有些时候需要合并两棵 Splay 树．

设两棵树的根节点分别为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么为了保证结果仍是二叉查找树，需要要求 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 树中的最大值小于 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 树中的最小值．这条件通常都可以满足，因为两棵树往往是从更大的子树中分裂出的．

合并操作如下：

  * 如果 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 其中之一或两者都为空树，直接返回不为空的那一棵树的根节点或空树；
  * 否则，通过 `loc(y, 1)` 将 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 树中的最小值上移至根 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处，再将它的左节点（此时必然为空）设置为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并更新节点信息，返回节点 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实现

```text 1 2 3 4 5 6 7 8 ``` |  ```text int merge ( int x , int y ) { if ( ! x || ! y ) return x | y ; loc ( y , 1 ); ch [ y ][ 0 ] = x ; fa [ x ] = y ; push_up ( y ); return y ; } ```   
---|---  
  
分裂操作类似．因而，Splay 树可以模拟 [无旋 treap](../treap/#无旋-treap) 的思路做各种操作，包括区间操作．后文 会介绍更具有 Splay 树风格的区间操作处理方法．

### 插入操作

插入操作是一个比较复杂的过程．具体步骤如下：（假设插入的值为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

  * 类似按值查找的过程，根据 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向下查找到存储 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的节点或者空节点，过程中记录父节点 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 如果存在存储 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直接更新信息，否则就新建节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 做伸展操作，将最后一个节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上移至根部．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text void insert ( int v ) { int x = rt , y = 0 ; for (; x && val [ x ] != v ; x = ch [ y = x ][ v > val [ x ]]); if ( x ) { ++ cnt [ x ]; ++ sz [ x ]; } else { x = ++ id ; val [ x ] = v ; cnt [ x ] = sz [ x ] = 1 ; fa [ x ] = y ; if ( y ) ch [ y ][ v > val [ y ]] = x ; } splay ( rt , x ); } ```   
---|---  
  
该实现允许直接向空树内插入值．若不想处理空树，可以在树中提前插入哑节点．

### 删除操作

删除操作也是一个比较复杂的操作．具体步骤如下：（假设删除的值为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

  * 首先按照值 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 查找存储它的节点，并上移至根部；
  * 如果不存在存储它的节点，直接返回；（上一步已经做了伸展操作）
  * 否则，更新节点信息；
  * 如果得到的根节点为空节点，就合并左右子树作为新的根节点，注意合并前需要更新两个子树的根的父节点为空．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text bool remove ( int v ) { find ( rt , v ); if ( ! rt || val [ rt ] != v ) return false ; \-- cnt [ rt ]; \-- sz [ rt ]; if ( ! cnt [ rt ]) { int x = ch [ rt ][ 0 ]; int y = ch [ rt ][ 1 ]; fa [ x ] = fa [ y ] = 0 ; rt = merge ( x , y ); } return true ; } ```   
---|---  
  
### 查询排名

直接按照值 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 访问节点（并上移至根），然后返回相应的值即可．

注意，当 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不存在时，方法 `find(rt, v)` 返回的根和 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小关系无法确定，需要单独讨论．

实现

```text 1 2 3 4 ``` |  ```text int find_rank ( int v ) { find ( rt , v ); return sz [ ch [ rt ][ 0 ]] \+ ( val [ rt ] < v ? cnt [ rt ] : 0 ) \+ 1 ; } ```   
---|---  
  
### 查询前驱

前驱定义为小于 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大的数．具体步骤如下：

  * 按照值 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 访问节点（并上移至根部）；
  * 如果根部的值小于 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么它必然是最大的那个，直接返回；
  * 否则，在左子树中找到最大值，并上移至根部．

最后一步相当于直接调用 `loc(ch[rt][0], sz[ch[rt][0]])`，只是省去了不必要的判断．

实现

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text int find_prev ( int v ) { find ( rt , v ); if ( rt && val [ rt ] < v ) return val [ rt ]; int x = ch [ rt ][ 0 ]; if ( ! x ) return -1 ; for (; ch [ x ][ 1 ]; x = ch [ x ][ 1 ]); splay ( rt , x ); return val [ rt ]; } ```   
---|---  
  
该实现允许前驱不存在，此时返回 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 查询后继

后继定义为大于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小的数．查询方法和前驱类似，只是将左子树的最大值换成了右子树的最小值，即调用 `loc(ch[rt][1], 1)`．

实现

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text int find_next ( int v ) { find ( rt , v ); if ( rt && val [ rt ] > v ) return val [ rt ]; int x = ch [ rt ][ 1 ]; if ( ! x ) return -1 ; for (; ch [ x ][ 0 ]; x = ch [ x ][ 0 ]); splay ( rt , x ); return val [ rt ]; } ```   
---|---  
  
### 参考实现

本节的最后，给出模板题目 [普通平衡树](https://loj.ac/problem/104) 的参考实现．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 ``` |  ```text #include <iostream> constexpr int N = 2e6 ; int id , rt ; int fa [ N ], val [ N ], cnt [ N ], sz [ N ], ch [ N ][ 2 ]; bool dir ( int x ) { return x == ch [ fa [ x ]][ 1 ]; } void push_up ( int x ) { sz [ x ] = cnt [ x ] \+ sz [ ch [ x ][ 0 ]] \+ sz [ ch [ x ][ 1 ]]; } void rotate ( int x ) { int y = fa [ x ], z = fa [ y ]; bool r = dir ( x ); ch [ y ][ r ] = ch [ x ][ ! r ]; ch [ x ][ ! r ] = y ; if ( z ) ch [ z ][ dir ( y )] = x ; if ( ch [ y ][ r ]) fa [ ch [ y ][ r ]] = y ; fa [ y ] = x ; fa [ x ] = z ; push_up ( y ); push_up ( x ); } void splay ( int & z , int x ) { int w = fa [ z ]; for ( int y ; ( y = fa [ x ]) != w ; rotate ( x )) { if ( fa [ y ] != w ) rotate ( dir ( x ) == dir ( y ) ? y : x ); } z = x ; } void find ( int & z , int v ) { int x = z , y = fa [ x ]; for (; x && val [ x ] != v ; x = ch [ y = x ][ v > val [ x ]]); splay ( z , x ? x : y ); } void loc ( int & z , int k ) { int x = z ; for (;;) { if ( sz [ ch [ x ][ 0 ]] >= k ) { x = ch [ x ][ 0 ]; } else if ( sz [ ch [ x ][ 0 ]] \+ cnt [ x ] >= k ) { break ; } else { k -= sz [ ch [ x ][ 0 ]] \+ cnt [ x ]; x = ch [ x ][ 1 ]; } } splay ( z , x ); } int merge ( int x , int y ) { if ( ! x || ! y ) return x | y ; loc ( y , 1 ); ch [ y ][ 0 ] = x ; fa [ x ] = y ; push_up ( y ); return y ; } void insert ( int v ) { int x = rt , y = 0 ; for (; x && val [ x ] != v ; x = ch [ y = x ][ v > val [ x ]]); if ( x ) { ++ cnt [ x ]; ++ sz [ x ]; } else { x = ++ id ; val [ x ] = v ; cnt [ x ] = sz [ x ] = 1 ; fa [ x ] = y ; if ( y ) ch [ y ][ v > val [ y ]] = x ; } splay ( rt , x ); } bool remove ( int v ) { find ( rt , v ); if ( ! rt || val [ rt ] != v ) return false ; \-- cnt [ rt ]; \-- sz [ rt ]; if ( ! cnt [ rt ]) { int x = ch [ rt ][ 0 ]; int y = ch [ rt ][ 1 ]; fa [ x ] = fa [ y ] = 0 ; rt = merge ( x , y ); } return true ; } int find_rank ( int v ) { find ( rt , v ); return sz [ ch [ rt ][ 0 ]] \+ ( val [ rt ] < v ? cnt [ rt ] : 0 ) \+ 1 ; } int find_kth ( int k ) { if ( k > sz [ rt ]) return -1 ; loc ( rt , k ); return val [ rt ]; } int find_prev ( int v ) { find ( rt , v ); if ( rt && val [ rt ] < v ) return val [ rt ]; int x = ch [ rt ][ 0 ]; if ( ! x ) return -1 ; for (; ch [ x ][ 1 ]; x = ch [ x ][ 1 ]); splay ( rt , x ); return val [ rt ]; } int find_next ( int v ) { find ( rt , v ); if ( rt && val [ rt ] > v ) return val [ rt ]; int x = ch [ rt ][ 1 ]; if ( ! x ) return -1 ; for (; ch [ x ][ 0 ]; x = ch [ x ][ 0 ]); splay ( rt , x ); return val [ rt ]; } int main () { int n ; std :: cin >> n ; for (; n ; \-- n ) { int op , x ; std :: cin >> op >> x ; switch ( op ) { case 1 : insert ( x ); break ; case 2 : remove ( x ); break ; case 3 : std :: cout << find_rank ( x ) << '\n' ; break ; case 4 : std :: cout << find_kth ( x ) << '\n' ; break ; case 5 : std :: cout << find_prev ( x ) << '\n' ; break ; case 6 : std :: cout << find_next ( x ) << '\n' ; break ; } } return 0 ; } ```   
---|---  
  
## 序列操作

Splay 树也可以运用在序列上，用于维护区间信息．与线段树对比，Splay 树常数较大，但是支持更复杂的序列操作，如区间翻转等．上文提到 Splay 树同样支持分裂和合并操作，因而可以模拟 [无旋 treap](../treap/#无旋-treap) 进行区间操作，在此不再过多讨论．本节主要讨论基于伸展操作的区间操作实现方法．

将序列建成的 Splay 树有如下性质：

  * Splay 树的中序遍历相当于原序列从左到右的遍历；
  * Splay 树上的一个节点代表原序列的一个元素；
  * Splay 树上的一颗子树，代表原序列的一段区间．

因为有伸展操作，可以快速提取出代表某个区间的 Splay 子树．

作为例子，本节将讨论模板题目 [文艺平衡树](https://loj.ac/problem/105) 的实现．

### 根据序列建树

在操作之前，需要根据所给的序列先把 Splay 树建出来．根据 Splay 树的特性，直接建出一颗只有左儿子的链即可．时间复杂度是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text void build ( int n ) { for ( int i = 1 ; i <= n \+ 2 ; ++ i ) { ++ id ; ch [ id ][ 0 ] = rt ; if ( rt ) fa [ rt ] = id ; rt = id ; val [ id ] = i \- 1 ; } splay ( rt , 1 ); } ```   
---|---  
  
最后的伸展操作自下而上地更新了节点信息．为了后文区间操作方便，序列左右两侧添加了两个哨兵节点．

### 区间翻转

以区间翻转为例，可以理解区间操作的方法：（设区间为 [𝐿,𝑅][L,R]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

  * 首先将节点 𝐿 −1L−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上移到根节点，再在其右子树中，将节点 𝑅 +1R+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上移到右子树的根节点；
  * 此时，设 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根节点的右子节点的左子节点，则以 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树就对应着区间 [𝐿,𝑅][L,R]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 在 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处对区间 [𝐿,𝑅][L,R]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做操作，并打上懒标记；
  * 在 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处将标记下传一次，然后利用伸展操作将 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上移到根．

第一步需要的操作就是前文平衡树操作中的「按照排名访问」，因为元素的标号就是它的排名．因为涉及懒标记的管理，它的实现与上文略有不同．

参考实现

```text 1 2 3 4 5 6 7 8 ``` |  ```text void reverse ( int l , int r ) { loc ( rt , l ); loc ( ch [ rt ][ 1 ], r \- l \+ 2 ); int x = ch [ ch [ rt ][ 1 ]][ 0 ]; lazy_reverse ( x ); push_down ( x ); splay ( rt , x ); } ```   
---|---  
  
最后一步的伸展操作并非为了保证复杂度正确，而是为了更新节点信息．因为伸展操作涉及到节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左右子节点，所以之前需要将节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的标记先下传一次．当然，仅对于区间翻转操作而言，子区间的翻转不会对祖先节点产生影响，所以省去这一步骤也是正确的．此处实现保留这两行，是为了说明一般的情形下的操作方法．

### 懒标记管理

首先，需要辅助函数 `lazy_reverse(x)` 和 `push_down(x)`．前者交换左右节点，并更新懒标记；后者将标记下传．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text void lazy_reverse ( int x ) { std :: swap ( ch [ x ][ 0 ], ch [ x ][ 1 ]); lz [ x ] ^= 1 ; } void push_down ( int x ) { if ( lz [ x ]) { if ( ch [ x ][ 0 ]) lazy_reverse ( ch [ x ][ 0 ]); if ( ch [ x ][ 1 ]) lazy_reverse ( ch [ x ][ 1 ]); lz [ x ] = 0 ; } } ```   
---|---  
  
然后，只需要在向下经过节点时下传标记即可．模板题要求的操作比较简单，只有按照排名寻找的操作（即 `loc`）涉及向下访问节点．注意，需要在函数每次访问一个新的节点 **前** 下传标记．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text void loc ( int & z , int k ) { int x = z ; for ( push_down ( x ); sz [ ch [ x ][ 0 ]] != k \- 1 ; push_down ( x )) { if ( sz [ ch [ x ][ 0 ]] >= k ) { x = ch [ x ][ 0 ]; } else { k -= sz [ ch [ x ][ 0 ]] \+ 1 ; x = ch [ x ][ 1 ]; } } splay ( z , x ); } ```   
---|---  
  
因为向下访问节点时已经移除了经过的路径的所有懒标记，所以利用伸展操作上移节点时不再需要处理懒标记．但是，对于区间操作的那一个节点要谨慎处理：因为它同样位于伸展操作的路径上，但是刚刚操作完，可能存在尚未下传的标记，需要首先下传再做伸展操作，正如同上文所做的那样．

### 参考实现

本节的最后，给出模板题目 [文艺平衡树](https://loj.ac/problem/105) 的参考实现．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 ``` |  ```text #include <iostream> constexpr int N = 2e6 ; int id , rt ; int fa [ N ], val [ N ], sz [ N ], lz [ N ], ch [ N ][ 2 ]; bool dir ( int x ) { return x == ch [ fa [ x ]][ 1 ]; } void push_up ( int x ) { sz [ x ] = 1 \+ sz [ ch [ x ][ 0 ]] \+ sz [ ch [ x ][ 1 ]]; } void lazy_reverse ( int x ) { std :: swap ( ch [ x ][ 0 ], ch [ x ][ 1 ]); lz [ x ] ^= 1 ; } void push_down ( int x ) { if ( lz [ x ]) { if ( ch [ x ][ 0 ]) lazy_reverse ( ch [ x ][ 0 ]); if ( ch [ x ][ 1 ]) lazy_reverse ( ch [ x ][ 1 ]); lz [ x ] = 0 ; } } void rotate ( int x ) { int y = fa [ x ], z = fa [ y ]; bool r = dir ( x ); ch [ y ][ r ] = ch [ x ][ ! r ]; ch [ x ][ ! r ] = y ; if ( z ) ch [ z ][ dir ( y )] = x ; if ( ch [ y ][ r ]) fa [ ch [ y ][ r ]] = y ; fa [ y ] = x ; fa [ x ] = z ; push_up ( y ); push_up ( x ); } void splay ( int & z , int x ) { int w = fa [ z ]; for ( int y ; ( y = fa [ x ]) != w ; rotate ( x )) { if ( fa [ y ] != w ) rotate ( dir ( x ) == dir ( y ) ? y : x ); } z = x ; } void loc ( int & z , int k ) { int x = z ; for ( push_down ( x ); sz [ ch [ x ][ 0 ]] != k \- 1 ; push_down ( x )) { if ( sz [ ch [ x ][ 0 ]] >= k ) { x = ch [ x ][ 0 ]; } else { k -= sz [ ch [ x ][ 0 ]] \+ 1 ; x = ch [ x ][ 1 ]; } } splay ( z , x ); } void build ( int n ) { for ( int i = 1 ; i <= n \+ 2 ; ++ i ) { ++ id ; ch [ id ][ 0 ] = rt ; if ( rt ) fa [ rt ] = id ; rt = id ; val [ id ] = i \- 1 ; } splay ( rt , 1 ); } void reverse ( int l , int r ) { loc ( rt , l ); loc ( ch [ rt ][ 1 ], r \- l \+ 2 ); int x = ch [ ch [ rt ][ 1 ]][ 0 ]; lazy_reverse ( x ); push_down ( x ); splay ( rt , x ); } void print ( int x ) { if ( ! x ) return ; push_down ( x ); print ( ch [ x ][ 0 ]); std :: cout << val [ x ] << ' ' ; print ( ch [ x ][ 1 ]); } void print () { loc ( rt , 1 ); loc ( ch [ rt ][ 1 ], sz [ rt ] \- 1 ); print ( ch [ ch [ rt ][ 1 ]][ 0 ]); } int main () { int n , m ; std :: cin >> n >> m ; build ( n ); for (; m ; \-- m ) { int l , r ; std :: cin >> l >> r ; reverse ( l , r ); } print (); return 0 ; } ```   
---|---  
  
## 习题

这些题目都是裸的 Splay 树维护二叉查找树：

  * [【模板】普通平衡树](https://loj.ac/problem/104)
  * [【模板】文艺平衡树](https://loj.ac/problem/105)
  * [「HNOI2002」营业额统计](https://loj.ac/problem/10143)
  * [「HNOI2004」宠物收养所](https://loj.ac/problem/10144)

Splay 树还出现在更复杂的应用场景中：

  * [「Cerc2007」robotic sort 机械排序](https://www.luogu.com.cn/problem/P4402)
  * [「HNOI2011」括号修复/「JSOI2011」括号序列](https://www.luogu.com.cn/problem/P3215)
  * [二逼平衡树（树套树）](https://loj.ac/problem/106)
  * [BZOJ 2827 千山鸟飞绝](https://hydro.ac/p/bzoj-P2827)
  * [「Lydsy1706 月赛」K 小值查询](https://hydro.ac/p/bzoj-P4923)
  * [POJ3580 SuperMemo](http://poj.org/problem?id=3580)

## 参考资料与注释

本文部分内容引用于 algocode 算法博客，特别鸣谢！

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/splay.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/splay.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [c-forrest](https://github.com/c-forrest), [StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [Tiphereth-A](https://github.com/Tiphereth-A), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [sshwy](https://github.com/sshwy), [Xeonacid](https://github.com/Xeonacid), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [ezoixx130](https://github.com/ezoixx130), [yyyu-star](https://github.com/yyyu-star), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [GavinZhengOI](https://github.com/GavinZhengOI), [GekkaSaori](https://github.com/GekkaSaori), [Gesrua](https://github.com/Gesrua), [Henry-ZHR](https://github.com/Henry-ZHR), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [shuzhouliu](https://github.com/shuzhouliu), [Siyuan](mailto:294873684@qq.com), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [zzxLLLL](https://github.com/zzxLLLL), [abc1763613206](https://github.com/abc1763613206), [Alpacabla](https://github.com/Alpacabla), [aofall](https://github.com/aofall), [Catreap](https://github.com/Catreap), [CoelacanthusHex](https://github.com/CoelacanthusHex), [GrapeLemonade](https://github.com/GrapeLemonade), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [hly1204](https://github.com/hly1204), [hsfzLZH1](https://github.com/hsfzLZH1), [iamtwz](https://github.com/iamtwz), [isdanni](https://github.com/isdanni), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [longlongzhu123](https://github.com/longlongzhu123), [lychees](https://github.com/lychees), [Macesuted](https://github.com/Macesuted), [Marcythm](https://github.com/Marcythm), [mcendu](https://github.com/mcendu), [Molmin](https://github.com/Molmin), [ouuan](https://github.com/ouuan), [partychicken](https://github.com/partychicken), [Peanut-Tang](https://github.com/Peanut-Tang), [Persdre](https://github.com/Persdre), [saigonoinorio](https://github.com/saigonoinorio), [SukkaW](https://github.com/SukkaW), [xiaofu-15191](https://github.com/xiaofu-15191), [yuhuoji](https://github.com/yuhuoji), [zcz0263](https://github.com/zcz0263), [代建杉](mailto:wood3s@foxmail.com)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
