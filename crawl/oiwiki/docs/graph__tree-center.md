# 树的中心 - OI Wiki

- Source: https://oi-wiki.org/graph/tree-center/

# 树的中心

## 定义

在树中，如果节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为根节点时，从 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发的最长链最短，那么称 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为这棵树的中心．

## 性质

  * 树的中心不一定唯一，但最多有 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，且这两个中心是相邻的．
  * 树的中心一定位于树的直径上．
  * 树上所有点到其最远点的路径一定交会于树的中心．
  * 当树的中心为根节点时，其到达直径端点的两条链分别为最长链和次长链．
  * 当通过在两棵树间连一条边以合并为一棵树时，连接两棵树的中心可以使新树的直径最小．
  * 树的中心到其他任意节点的距离不超过树直径的一半．

## 求法

寻找一个点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使其作为根节点时，最长链的长度最短．

### 具体步骤

  1. 维护 𝑙𝑒𝑛1𝑥len1x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 子树内的最长链．
  2. 维护 𝑙𝑒𝑛2𝑥len2x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示不与 𝑙𝑒𝑛1𝑥len1x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 重叠的最长链．
  3. 维护 𝑢𝑝𝑥upx![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 子树外的最长链，该链必定经过 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的父节点．
  4. 找到点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 max(𝑙𝑒𝑛1𝑥,𝑢𝑝𝑥)max(len1x,upx)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最小，那么 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为树的中心．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 ``` |  ```text // 这份代码默认节点编号从 1 开始，即 i ∈ [1,n]，使用vector存图 int d1 [ N ], d2 [ N ], up [ N ], x , y , mini = 1e9 ; // d1,d2对应上文中的len1,len2 struct node { int to , val ; // to为边指向的节点，val为边权 }; vector < node > nbr [ N ]; void dfsd ( int cur , int fa ) { // 求取len1和len2 for ( node nxtn : nbr [ cur ]) { int nxt = nxtn . to , w = nxtn . val ; // nxt为这条边通向的节点，val为边权 if ( nxt == fa ) { continue ; } dfsd ( nxt , cur ); if ( d1 [ nxt ] \+ w > d1 [ cur ]) { // 可以更新最长链 d2 [ cur ] = d1 [ cur ]; d1 [ cur ] = d1 [ nxt ] \+ w ; } else if ( d1 [ nxt ] \+ w > d2 [ cur ]) { // 不能更新最长链，但可更新次长链 d2 [ cur ] = d1 [ nxt ] \+ w ; } } } void dfsu ( int cur , int fa ) { for ( node nxtn : nbr [ cur ]) { int nxt = nxtn . to , w = nxtn . val ; if ( nxt == fa ) { continue ; } up [ nxt ] = up [ cur ] \+ w ; if ( d1 [ nxt ] \+ w != d1 [ cur ]) { // 如果自己子树里的最长链不在nxt子树里 up [ nxt ] = max ( up [ nxt ], d1 [ cur ] \+ w ); } else { // 自己子树里的最长链在nxt子树里，只能使用次长链 up [ nxt ] = max ( up [ nxt ], d2 [ cur ] \+ w ); } dfsu ( nxt , cur ); } } void GetTreeCenter () { // 统计树的中心，记为x和y（若存在） dfsd ( 1 , 0 ); dfsu ( 1 , 0 ); for ( int i = 1 ; i <= n ; i ++ ) { if ( max ( d1 [ i ], up [ i ]) < mini ) { // 找到了当前max(len1[x],up[x])最小点 mini = max ( d1 [ i ], up [ i ]); x = i ; y = 0 ; } else if ( max ( d1 [ i ], up [ i ]) == mini ) { // 另一个中心 y = i ; } } } ```   
---|---  
  
### 示例

假设我们有一棵树，如下所示：

```text 1 2 3 4 5 ``` |  ```text A / \ B C / \ \ D E F ```   
---|---  
  
  * 树的直径为 𝐷 →𝐵 →𝐴 →𝐶 →𝐹D→B→A→C→F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．直径长度为 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 树的中心为节点 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为从 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出发的最长链（到 𝐷D![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）均为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 如果将 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝐶C![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为树的根，则从这些节点出发的最长链将增加，因此它们不是树的中心．

### 时间复杂度

上述算法的时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是树中节点的数量．

## 参考

  * [TutorialsPoint: Centers of a Tree](https://www.tutorialspoint.com/centers-of-a-tree)
  * [ProofWiki: Definition of Center of Tree](https://proofwiki.org/wiki/Definition:Center_of_Tree)
  * [Wikipedia: Tree (graph theory)](https://en.wikipedia.org/wiki/Tree_%28graph_theory%29#Properties)

* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/graph/tree-center.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/graph/tree-center.md "edit.link.title")  
>  __本页面贡献者：[littleparrot12345](https://github.com/littleparrot12345), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
