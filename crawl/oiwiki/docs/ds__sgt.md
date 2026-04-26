# 替罪羊树 - OI Wiki

- Source: https://oi-wiki.org/ds/sgt/

# 替罪羊树

## 引入

**替罪羊树** 是一种依靠重构操作维持平衡的重量平衡树．替罪羊树会在插入、删除操作后，检测树是否发生失衡；如果失衡，将有针对性地进行重构以恢复平衡．

一般地，替罪羊树不支持区间操作，且无法完全持久化；但它具有实现简单、常数较小的优点．

## 基本结构和操作

替罪羊树的核心操作是重构、插入和删除操作．

### 节点信息

替罪羊树需要存储以下信息，用于树的自平衡操作：

  * 树的结构信息：
    * `id`：已使用节点数目；
    * `rt`：根节点；
    * `lc[x]`，`rc[x]`：左、右子节点；
    * `tot[x]`：以 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树大小（每个节点计数为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）3；
    * `tot_active`：整个树中未删除（即 `cnt[x] != 0`）的节点的数目．

当使用替罪羊树实现平衡树时，还需要存储如下信息：

  * 平衡树的节点信息：
    * `val[x]`：节点存储的值；
    * `cnt[x]`：节点存储的值的计数（可能为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）；
    * `sz[x]`：以 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树存储的值的计数．

为了维护节点信息，可以实现 `push_up` 操作：

参考实现

```text 1 2 3 4 5 ``` |  ```text // Update node info from its children. void push_up ( int x ) { tot [ x ] = 1 \+ tot [ lc [ x ]] \+ tot [ rc [ x ]]; sz [ x ] = cnt [ x ] \+ sz [ lc [ x ]] \+ sz [ rc [ x ]]; } ```   
---|---  
  
应注意 `tot[x]` 和 `sz[x]` 的更新方式的不同．

### 重构操作

当树发生失衡时，需要对某个子树进行重构，使之尽可能平衡．重构分为两步：

  * 对要重构的子树做中序遍历，将所有未删除节点存到序列中；
  * 二分建树，即取中点为根，左右两侧递归地建子树，并更新节点信息．

参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text // Tree -> Array. void flatten ( int x ) { if ( ! x ) return ; flatten ( lc [ x ]); if ( cnt [ x ]) tmp [ n_tmp ++ ] = x ; flatten ( rc [ x ]); } // Array -> Tree. int build ( int ll , int rr ) { if ( ll > rr ) return 0 ; int mm = ( ll \+ rr ) / 2 ; int x = tmp [ mm ]; lc [ x ] = build ( ll , mm \- 1 ); rc [ x ] = build ( mm \+ 1 , rr ); push_up ( x ); return x ; } // Rebuild a subtree. void rebuild ( int & x ) { n_tmp = 0 ; flatten ( x ); x = build ( 0 , n_tmp \- 1 ); } ```   
---|---  
  
建树时注意维护节点信息，包括叶子节点的信息．

单次重构的复杂度是 Θ(|𝑇𝑥|)Θ(|Tx|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，因此如果每次插入、删除时都进行重构，复杂度将难以接受．替罪羊树的核心思想就在于对重构时机的选择，进而实现了 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的均摊复杂度．

### 插入操作

插入操作时，可能会引起树的失衡．为了判断树的失衡，需要引入参数 𝛼 ∈(0.5,1)α∈(0.5,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，通常的选择在 0.7 ∼0.80.7∼0.8![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间．

如果新插入的节点的深度超过了 ⌊log1/𝛼⁡|𝑇|⌋⌊log1/α⁡|T|⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，|𝑇||T|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为更新后的树的大小，就需要在回溯时寻找失衡发生的节点并进行重构．此时，需要根据如下条件判断以 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树失衡：

max{|𝑇left(𝑥)|,|𝑇right(𝑥)|}>𝛼⋅|𝑇𝑥|,max{|Tleft(x)|,|Tright(x)|}>α⋅|Tx|,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中，left(𝑥)left(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 right(𝑥)right(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左、右子节点，|𝑇𝑥||Tx|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为以 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的子树大小．

插入操作的具体步骤如下：

  * 首先利用二分查找树的性质向下找到插入值的位置，下探时记录深度；
  * 如果已经有节点，直接修改节点信息，否则新建节点；
  * 如果新建节点过深，就需要自下而上回溯到根，更新节点信息，并记录第一个（或任意一个）子树失衡的节点；
  * 如果存在失衡节点，重构失衡节点的子树．

参考实现如下：

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 ``` |  ```text // Insert v into subtree of x. bool insert ( int & x , int v , int dep ) { bool check = false ; if ( ! x ) { x = ++ id ; val [ x ] = v ; check = dep > std :: log ( tot [ rt ] \+ 1 ) / std :: log ( 1 / ALPHA ); } if ( val [ x ] == v ) { if ( ! cnt [ x ]) ++ tot_active ; ++ cnt [ x ]; } else if ( v < val [ x ]) { check = insert ( lc [ x ], v , dep \+ 1 ); } else { check = insert ( rc [ x ], v , dep \+ 1 ); } push_up ( x ); if ( check && ( tot [ lc [ x ]] > ALPHA * tot [ x ] || tot [ rc [ x ]] > ALPHA * tot [ x ])) { rebuild ( x ); return false ; } return check ; } // Insert v into the tree. void insert ( int v ) { insert ( rt , v , 0 ); } ```   
---|---  
  
注意，单次插入至多引起一次重构．如果没有新增节点或是新增节点并没有过深，又或是本次回溯过程中已经执行过重构，就不需要继续判断失衡了．多余的重构可能会导致效率损失1．回溯过程中的第一个失衡节点，就是所谓的「替罪羊」．

### 删除操作

删除操作的处理则非常简单．替罪羊树的删除策略是「懒删除」，即节点为空时，不移除节点，而是留待后续处理．

当然，如果树中空节点过多，树的访问效率会大大下降．因此，替罪羊树维护两个计数，整个树中未删除节点的数目和整个树实际使用的节点数目．对于选定的阈值2 𝛼 ∈(0,1)α∈(0,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当前者与后者的比值下降到 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以下时，就对整个树做一次重构，重构时删除所有空节点．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` |  ```text // Remove v from subtree of x. bool remove ( int x , int v ) { if ( ! x ) return false ; bool succ = true ; if ( v < val [ x ]) { succ = remove ( lc [ x ], v ); } else if ( v > val [ x ]) { succ = remove ( rc [ x ], v ); } else if ( cnt [ x ]) { \-- cnt [ x ]; if ( ! cnt [ x ]) \-- tot_active ; } else { succ = false ; } push_up ( x ); return succ ; } // Remove v from the tree. bool remove ( int v ) { bool succ = remove ( rt , v ); if ( ! tot_active ) { rt = 0 ; } else if ( succ && tot_active < tot [ rt ] * ALPHA ) { rebuild ( rt ); } return succ ; } ```   
---|---  
  
### 时间复杂度

大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的替罪羊树的访问节点的时间复杂度为单次 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，Θ(𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次插入和删除的均摊时间复杂度也是单次 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

本节对替罪羊树的时间复杂度仅做简要论证，详细证明请参考原论文．

替罪羊树的时间复杂度的论证

由于采用懒删除的策略，未删除节点数目为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的替罪羊树可能占用了 𝛼−1𝑛α−1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点．由于仅仅相差一个常数因子，本文在表述中并不区分替罪羊树的未删除节点数目和占用节点数目，而统一称为「树的大小」．

  1. **访问操作** ：访问操作的复杂度得以保证，是因为大小为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的替罪羊树的树高总是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

首先，区分两个概念：

     * 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑重量平衡：所有节点处，左、右子节点的子树的大小均不超过该节点处子树的大小的 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倍；
     * 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑高度平衡：树的高度不超过 ⌊log1/𝛼⁡|𝑇|⌋⌊log1/α⁡|T|⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是树的大小．

𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑重量平衡可以推出 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑高度平衡，因为子节点深度每增加一，大小就减少到原来的 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倍；反过来则不一定成立．更严格地说，每次操作结束后，替罪羊树都总是 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑高度平衡的4，这就保证了访问操作的复杂度．

只有插入操作会改变树的结构，所以只需要说明每次插入操作后，替罪羊树都仍是 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑高度平衡的．如果新插入的节点过深，造成了整个树不再 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑高度平衡，那么自该节点回溯至根时，至少会碰上一个节点，即「替罪羊」，它的子树不再 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑重量平衡．将其重构后，子树的高度将降低至少一，故而新插入的节点将不再过深．

  2. **插入操作** ：插入操作的复杂度是均摊 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

设在某次插入操作后，节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处发生一次子树的重构，时间成本为 Θ(|𝑇𝑥|)Θ(|Tx|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 刚插入时，或者它刚刚经历了（自身或祖先节点的）上一次重构之后，它的左右子树至多只相差一个节点．而在这次重构之前，节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处必然成立

max{|𝑇left(𝑥)|,|𝑇right(𝑥)|}>𝛼⋅|𝑇𝑥|.max{|Tleft(x)|,|Tright(x)|}>α⋅|Tx|.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这一条件保证左右子树的大小的差值至少为 (2𝛼 −1)|𝑇𝑥|(2α−1)|Tx|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．因而，这两次重构之间，子树 𝑇𝑥Tx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中插入了 Ω(|𝑇𝑥|)Ω(|Tx|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点．

利用摊还分析可知5，如果每次插入节点时，都在（可能的重构前）自根到该节点的路径上的每个节点都增加 Θ(1)Θ(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的势能，那么到节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处子树重构前，必然已经在节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处累积了 Ω(|𝑇𝑥|)Ω(|Tx|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的势能，足以用于偿还 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处子树重构的成本 Θ(|𝑇𝑥|)Θ(|Tx|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为树的深度都是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，所以单次插入增加的势能是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的；这说明，Θ(𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次插入操作中势能增加的总和是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．由此，子树重构的总成本也是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，单次插入操作（含重构）的均摊时间复杂度就是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

注意，分析中没有假定在节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的两次重构之间，子树 𝑇𝑥Tx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内部没有发生其它的重构．因此，只要只重构满足失衡条件的节点处的子树，就能保证复杂度正确．

  3. **删除操作** ：删除操作的复杂度也是均摊 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

删除引起的重构会导致整个树不含空节点．而某次删除引起重构之前，整个树中已经有 Θ(𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个空节点，这意味着至少进行了 Θ(𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次删除操作．因为每次删除操作的寻址的复杂度是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，且单次重构的复杂度是 Θ(𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以这 Θ(𝑛)Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次删除操作的实际时间成本为

Θ(𝑛)𝑂(log⁡𝑛)+Θ(𝑛)Θ(n)O(log⁡n)+Θ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的．故而，单次删除的均摊复杂度为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

## 平衡树操作

本节介绍用替罪羊树维护可重集的方法．

除上节介绍的操作外，其余操作均为平衡树的常见操作．但是，因为替罪羊树中可能存在空节点，这些操作也需要相应调整．

### 查询排名

利用二分查找树的性质向下查找节点位置，过程中记录路径左侧存储的值的数目即可．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text // Find the rank of v, i.e., #{val < v} + 1. int find_rank ( int v ) { int res = 0 ; int x = rt ; while ( x && val [ x ] != v ) { if ( v < val [ x ]) { x = lc [ x ]; } else { res += sz [ lc [ x ]] \+ cnt [ x ]; x = rc [ x ]; } } return res \+ sz [ lc [ x ]] \+ 1 ; } ```   
---|---  
  
### 根据排名查询值

利用节点记录的子树存储值的数目信息向下查找即可．注意可能存在计数为零的节点．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text // Find the k-th smallest element. int find_kth ( int k ) { if ( k <= 0 || sz [ rt ] < k ) return -1 ; int x = rt ; for (;;) { if ( k <= sz [ lc [ x ]]) { x = lc [ x ]; } else if ( k <= sz [ lc [ x ]] \+ cnt [ x ]) { return val [ x ]; } else { k -= sz [ lc [ x ]] \+ cnt [ x ]; x = rc [ x ]; } } return -1 ; } ```   
---|---  
  
### 查询前驱、后继

以上两种功能结合即可．

参考实现

```text 1 2 3 4 5 ``` |  ```text // Find predecessor. int find_prev ( int x ) { return find_kth ( find_rank ( x ) \- 1 ); } // Find successor. int find_next ( int x ) { return find_kth ( find_rank ( x \+ 1 )); } ```   
---|---  
  
如果想直接实现，应注意处理计数为零的节点．

### 参考实现

本节的最后，给出模板题 [普通平衡树](https://loj.ac/p/104) 的参考实现．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 ``` |  ```text #include <cmath> #include <iostream> constexpr int N = 2e6 ; constexpr double ALPHA = 0.7 ; int id , rt , lc [ N ], rc [ N ], tot [ N ], tot_active ; // Tree structure info. int tmp [ N ], n_tmp ; // Space for rebuilding trees. int val [ N ], cnt [ N ], sz [ N ]; // Node info. // Update node info from its children. void push_up ( int x ) { tot [ x ] = 1 \+ tot [ lc [ x ]] \+ tot [ rc [ x ]]; sz [ x ] = cnt [ x ] \+ sz [ lc [ x ]] \+ sz [ rc [ x ]]; } // Tree -> Array. void flatten ( int x ) { if ( ! x ) return ; flatten ( lc [ x ]); if ( cnt [ x ]) tmp [ n_tmp ++ ] = x ; flatten ( rc [ x ]); } // Array -> Tree. int build ( int ll , int rr ) { if ( ll > rr ) return 0 ; int mm = ( ll \+ rr ) / 2 ; int x = tmp [ mm ]; lc [ x ] = build ( ll , mm \- 1 ); rc [ x ] = build ( mm \+ 1 , rr ); push_up ( x ); return x ; } // Rebuild a subtree. void rebuild ( int & x ) { n_tmp = 0 ; flatten ( x ); x = build ( 0 , n_tmp \- 1 ); } // Insert v into subtree of x. bool insert ( int & x , int v , int dep ) { bool check = false ; if ( ! x ) { x = ++ id ; val [ x ] = v ; check = dep > std :: log ( tot [ rt ] \+ 1 ) / std :: log ( 1 / ALPHA ); } if ( val [ x ] == v ) { if ( ! cnt [ x ]) ++ tot_active ; ++ cnt [ x ]; } else if ( v < val [ x ]) { check = insert ( lc [ x ], v , dep \+ 1 ); } else { check = insert ( rc [ x ], v , dep \+ 1 ); } push_up ( x ); if ( check && ( tot [ lc [ x ]] > ALPHA * tot [ x ] || tot [ rc [ x ]] > ALPHA * tot [ x ])) { rebuild ( x ); return false ; } return check ; } // Insert v into the tree. void insert ( int v ) { insert ( rt , v , 0 ); } // Remove v from subtree of x. bool remove ( int x , int v ) { if ( ! x ) return false ; bool succ = true ; if ( v < val [ x ]) { succ = remove ( lc [ x ], v ); } else if ( v > val [ x ]) { succ = remove ( rc [ x ], v ); } else if ( cnt [ x ]) { \-- cnt [ x ]; if ( ! cnt [ x ]) \-- tot_active ; } else { succ = false ; } push_up ( x ); return succ ; } // Remove v from the tree. bool remove ( int v ) { bool succ = remove ( rt , v ); if ( ! tot_active ) { rt = 0 ; } else if ( succ && tot_active < tot [ rt ] * ALPHA ) { rebuild ( rt ); } return succ ; } // Find the rank of v, i.e., #{val < v} + 1. int find_rank ( int v ) { int res = 0 ; int x = rt ; while ( x && val [ x ] != v ) { if ( v < val [ x ]) { x = lc [ x ]; } else { res += sz [ lc [ x ]] \+ cnt [ x ]; x = rc [ x ]; } } return res \+ sz [ lc [ x ]] \+ 1 ; } // Find the k-th smallest element. int find_kth ( int k ) { if ( k <= 0 || sz [ rt ] < k ) return -1 ; int x = rt ; for (;;) { if ( k <= sz [ lc [ x ]]) { x = lc [ x ]; } else if ( k <= sz [ lc [ x ]] \+ cnt [ x ]) { return val [ x ]; } else { k -= sz [ lc [ x ]] \+ cnt [ x ]; x = rc [ x ]; } } return -1 ; } // Find predecessor. int find_prev ( int x ) { return find_kth ( find_rank ( x ) \- 1 ); } // Find successor. int find_next ( int x ) { return find_kth ( find_rank ( x \+ 1 )); } int main () { int n ; std :: cin >> n ; for (; n ; \-- n ) { int op , x ; std :: cin >> op >> x ; switch ( op ) { case 1 : insert ( x ); break ; case 2 : remove ( x ); break ; case 3 : std :: cout << find_rank ( x ) << '\n' ; break ; case 4 : std :: cout << find_kth ( x ) << '\n' ; break ; case 5 : std :: cout << find_prev ( x ) << '\n' ; break ; case 6 : std :: cout << find_next ( x ) << '\n' ; break ; } } return 0 ; } ```   
---|---  
  
## 参考资料

  * Galperin, Igal, and Ronald L. Rivest. "Scapegoat trees." Proceedings of the fourth annual ACM-SIAM Symposium on Discrete algorithms. 1993.
  * [Scapegoat Tree - Wikipedia](https://en.wikipedia.org/wiki/Scapegoat_tree)
  * [替罪羊树 - riteme 的博客](https://riteme.site/blog/2016-4-6/scapegoat.html)

* * *

  1. 根据后文的复杂度分析可知，这些效率损失仅意味着更大的常数因子，而复杂度依然是正确的．因为判断树深可能会涉及较多的浮点数对数运算，不判断树深只判断失衡的代码在某些数据中可能更快． ↩

  2. 不必与上文插入操作时选取的参数相同．尽管原论文做了这样的假定，但是选取不同的参数只会导致单次操作的复杂度中常数项的变化，整体复杂度依然是正确的． ↩

  3. 也可以只统计未删除节点数目，此时不再需要统计 `tot_active`，而需要统计所有占用节点数目 `tot_max`，代码相应调整即可． ↩

  4. 按原文定义，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指未删除节点的数目，故而只能保证树高不超过 ⌊log1/𝛼⁡𝑛⌋ +1⌊log1/α⁡n⌋+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这称为弱 𝛼α![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)‑高度平衡．此处没有细究该常数项的差异． ↩

  5. 有些文章会简单分析成 Ω(|𝑇𝑥|)Ω(|Tx|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次插入对应一次重构，故而均摊复杂度为 Ω(|𝑇𝑥|)𝑂(log⁡𝑛)+Θ(|𝑇𝑥|)Ω(|𝑇𝑥|) =𝑂(log⁡𝑛)Ω(|Tx|)O(log⁡n)+Θ(|Tx|)Ω(|Tx|)=O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这样的思路可以辅助理解均摊复杂度为什么正确，但并不严谨．这是因为，一次插入可能对应着多个祖先节点的重构，故而当节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 发生重构时，子树内未引起重构的节点数目并不显然是 Ω(|𝑇𝑥|)Ω(|Tx|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的． ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/sgt.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/sgt.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [countercurrent-time](https://github.com/countercurrent-time), [StudyingFather](https://github.com/StudyingFather), [Early0v0](https://github.com/Early0v0), [H-J-Granger](https://github.com/H-J-Granger), [NachtgeistW](https://github.com/NachtgeistW), [0xis-cn](https://github.com/0xis-cn), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [ezoixx130](https://github.com/ezoixx130), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A), [weiyong1024](https://github.com/weiyong1024), [Backl1ght](https://github.com/Backl1ght), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Peanut-Tang](https://github.com/Peanut-Tang), [SukkaW](https://github.com/SukkaW), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
