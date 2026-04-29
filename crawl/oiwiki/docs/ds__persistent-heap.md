# 可持久化可并堆 - OI Wiki

- Source: https://oi-wiki.org/ds/persistent-heap/

# 可持久化可并堆

可持久化可并堆一般用于求解 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 短路问题．

如果一种可并堆的时间复杂度不是均摊的，那么它在可持久化后单次操作的时间复杂度就保证是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，即不会因为特殊数据而使复杂度退化．

## 可持久化左偏树

在学习本内容前，请先了解 [左偏树](../leftist-tree/) 的相关内容．

### 过程

回顾左偏树的合并过程，假设我们要合并分别以 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根节点的两棵左偏树，且维护的左偏树满足小根堆的性质：

  1. 如果 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中有结点为空，返回 𝑥 +𝑦x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  2. 选择 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两结点中权值更小的结点，作为合并后左偏树的根．

  3. 递归合并 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右子树与 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将合并后的根节点作为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右儿子．

  4. 维护当前合并后左偏树的左偏性质，维护 `dist` 值，返回选择的根节点．

由于每次递归都会使 `dist[x]+dist[y]` 减少一，而 `dist[x]` 是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，一次最多只会修改 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点，所以这样做的时间复杂度是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

可持久化要求保留历史信息，使得之后能够访问之前的版本．要将左偏树可持久化，就要将其沿途修改的路径复制一遍．

所以可持久化左偏树的合并过程是这样的：

  1. 如果 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中有结点为空，返回 𝑥 +𝑦x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  2. 选择 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两结点中权值更小的结点，新建该结点的一个复制 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，作为合并后左偏树的根．

  3. 递归合并 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右子树与 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将合并后的根节点作为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右儿子．

  4. 维护以 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的左偏树的左偏性质，维护其 `dist` 值，返回 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于左偏树一次最多只会修改并新建 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点，设操作次数为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则可持久化左偏树的时间复杂度和空间复杂度均为 𝑂(𝑚log⁡𝑛)O(mlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text int merge ( int x , int y ) { if ( ! x || ! y ) return x \+ y ; if ( v [ x ] > v [ y ]) swap ( x , y ); int p = ++ cnt ; lc [ p ] = lc [ x ]; v [ p ] = v [ x ]; rc [ p ] = merge ( rc [ x ], y ); if ( dist [ lc [ p ]] < dist [ rc [ p ]]) swap ( lc [ p ], rc [ p ]); dist [ p ] = dist [ rc [ p ]] \+ 1 ; return p ; } ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/persistent-heap.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/persistent-heap.md "edit.link.title")  
>  __本页面贡献者：[hsfzLZH1](https://github.com/hsfzLZH1), [ouuan](https://github.com/ouuan), [Enter-tainer](https://github.com/Enter-tainer), [iamtwz](https://github.com/iamtwz), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
