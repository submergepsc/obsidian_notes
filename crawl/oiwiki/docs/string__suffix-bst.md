# 后缀平衡树 - OI Wiki

- Source: https://oi-wiki.org/string/suffix-bst/

# 后缀平衡树

## 定义

后缀之间的大小由字典序定义，后缀平衡树就是一个维护这些后缀顺序的平衡树，即字符串 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后缀平衡树是 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所有后缀的有序集合．后缀平衡树上的一个节点相当于原字符串的一个后缀．

特别地，后缀平衡树的中序遍历即为后缀数组．

## 构造过程

对长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 建立其后缀平衡树，考虑逆序将其后缀加入后缀平衡树．

记后缀平衡树维护的集合为 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当前添加的后缀为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则添加下一个后缀就是向 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中加入 𝚌𝑆cS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（亦可理解为后缀平衡树维护的字符串为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，下一步往 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 前加入一个字符 𝚌c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．这一操作其实就是向平衡树中插入节点．

这里使用期望树高为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的平衡树，例如替罪羊树或 Treap 等．

### 做法 1

插入时，暴力比较两个后缀之间的大小关系，从而判断之后是往哪一个子树添加．这样子，单次插入至多比较 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，单次比较的时间复杂度至多为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一共 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

一共会插入 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，所以该做法的时间复杂度存在上界 𝑂(𝑛2log⁡𝑛)O(n2log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 做法 2

注意到 𝚌𝑆cS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的区别仅在于 𝚌c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已经属于 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了，可以利用这一点来优化插入操作．

假设当前要比较 𝚌𝑆cS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两个字符串的大小，且 𝐴,𝑆 ∈𝑋A,S∈X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每次比较时，首先比较两串的首字符．若首字符不等，则两串的大小关系就已经确定了；若首字符相等，那么就只需要判断去除首字符后两字符串的大小关系．而两串去除首字符后都已经属于 𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了，这时候可以借助平衡树 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求排名的操作来完成后续的比较．这样，单次插入的操作至多 𝑂(log2⁡𝑛)O(log2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

一共会插入 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，所以该做法的时间复杂度存在上界 𝑂(𝑛log2⁡𝑛)O(nlog2⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 做法 3

根据做法 2，如果能够 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 判断平衡树中两个节点之间的大小关系，那么就可以在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内完成后缀平衡树的构造．

记 𝑣𝑎𝑙𝑖vali![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示节点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．如果在建平衡树时，每个节点多维护一个标记 𝑡𝑎𝑔𝑖tagi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得若 𝑡𝑎𝑔𝑖 >𝑡𝑎𝑔𝑗 ⟺ 𝑣𝑎𝑙𝑖 >𝑣𝑎𝑙𝑗tagi>tagj⟺vali>valj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么就可以根据 𝑡𝑎𝑔𝑖tagi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的大小 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 判断平衡树中两个节点的大小．

不妨令平衡树中每个节点对应一个实数区间，令根节点对应 (0,1)(0,1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于节点 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，记其对应的实数区间为 (𝑙,𝑟)(l,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑡𝑎𝑔𝑖 =𝑙+𝑟2tagi=l+r2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其左子树对应实数区间 (𝑙,𝑡𝑎𝑔𝑖)(l,tagi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其右子树对应实数区间 (𝑡𝑎𝑔𝑖,𝑟)(tagi,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．易证 𝑡𝑎𝑔𝑖tagi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足上述要求．

由于使用了期望树高为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的平衡树，所以精度是有一定保证的．实际实现时也可以用一个较大的区间来做，例如让根对应 (0,1018)(0,1018)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 做法 4

其实可以先构建出后缀数组，然后再根据后缀数组构建后缀平衡树．这样做的复杂度瓶颈在于后缀数组的构建复杂度或者所用平衡树一次性插入 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的复杂度．

## 删除操作

假设当前添加的后缀为 𝚌𝑆cS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，上一个添加的后缀为 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．后缀平衡树还支持删除后缀 𝚌𝑆cS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的操作（亦可理解为后缀平衡树维护的字符串为 𝚌𝑆cS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将开头的 𝚌c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 删除）．

类似于插入操作，借助平衡树的删除节点操作可以完成删除 𝚌𝑆cS![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的操作．

## 后缀平衡树的优点

  * 后缀平衡树的思路比较清晰，相比后缀自动机等后缀结构更好理解，会写平衡树就能写．
  * 后缀平衡树的复杂度不依赖于字符集的大小
  * 后缀平衡树支持在字符串开头删除一个字符
  * 如果使用支持可持久化的平衡树，那么后缀平衡树也能可持久化

## 例题

### [P3809【模板】后缀排序](https://www.luogu.com.cn/problem/P3809)

后缀数组的模板题，建出后缀平衡树之后，通过中序遍历得到后缀数组．

SGT 版本的参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 ``` |  ```text #include <algorithm> #include <iostream> #include <string> using namespace std ; constexpr int N = 1e6 \+ 5 ; constexpr double INF = 1e18 ; int n , m , sa [ N ]; string t ; // SuffixBST(SGT Ver) // 顺序加入，查询时将询问串翻转 // 以i开始的后缀，对应节点的编号为i constexpr double alpha = 0.75 ; int root ; int sz [ N ], L [ N ], R [ N ]; double tag [ N ]; int buffer_size , buffer [ N ]; bool cmp ( int x , int y ) { if ( t [ x ] != t [ y ]) return t [ x ] < t [ y ]; return tag [ x \+ 1 ] < tag [ y \+ 1 ]; } void init () { root = 0 ; } void new_node ( int & rt , int p , double lv , double rv ) { rt = p ; sz [ rt ] = 1 ; tag [ rt ] = ( lv \+ rv ) / 2 ; L [ rt ] = R [ rt ] = 0 ; } void push_up ( int x ) { if ( ! x ) return ; sz [ x ] = sz [ L [ x ]] \+ 1 \+ sz [ R [ x ]]; } bool balance ( int rt ) { return alpha * sz [ rt ] > max ( sz [ L [ rt ]], sz [ R [ rt ]]); } void flatten ( int rt ) { if ( ! rt ) return ; flatten ( L [ rt ]); buffer [ ++ buffer_size ] = rt ; flatten ( R [ rt ]); } void build ( int & rt , int l , int r , double lv , double rv ) { if ( l > r ) { rt = 0 ; return ; } int mid = ( l \+ r ) >> 1 ; double mv = ( lv \+ rv ) / 2 ; rt = buffer [ mid ]; tag [ rt ] = mv ; build ( L [ rt ], l , mid \- 1 , lv , mv ); build ( R [ rt ], mid \+ 1 , r , mv , rv ); push_up ( rt ); } void rebuild ( int & rt , double lv , double rv ) { buffer_size = 0 ; flatten ( rt ); build ( rt , 1 , buffer_size , lv , rv ); } void insert ( int & rt , int p , double lv , double rv ) { if ( ! rt ) { new_node ( rt , p , lv , rv ); return ; } if ( cmp ( p , rt )) insert ( L [ rt ], p , lv , tag [ rt ]); else insert ( R [ rt ], p , tag [ rt ], rv ); push_up ( rt ); if ( ! balance ( rt )) rebuild ( rt , lv , rv ); } void inorder ( int rt ) { if ( ! rt ) return ; inorder ( L [ rt ]); sa [ ++ m ] = rt ; inorder ( R [ rt ]); } void solve ( int Case ) { cin >> t ; n = t . size (); t = " " \+ t ; init (); for ( int i = n ; i >= 1 ; \-- i ) { insert ( root , i , 0 , INF ); } // 后缀平衡树的中序遍历即为后缀数组 m = 0 ; inorder ( root ); for ( int i = 1 ; i <= n ; ++ i ) cout << sa [ i ] << ' ' ; cout << '\n' ; } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); solve ( 1 ); return 0 ; } ```   
---|---  
  
### [P6164【模板】后缀平衡树](https://www.luogu.com.cn/problem/P6164)

题意

给定初始字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个操作：

  1. 在当前字符串的后面插入若干个字符．
  2. 在当前字符串的后面删除若干个字符．
  3. 询问字符串 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为连续子串在当前字符串中出现了几次？

题目 **强制在线** ，字符串变化长度以及初始长度 ≤8 ×105≤8×105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑞 ≤105q≤105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，询问的总长度 ≤3 ×106≤3×106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于操作 1 和操作 2，由于后缀平衡树维护头插和头删操作比较方便，所以想到把尾插和尾删操作搞成头插和头删．这里如果维护 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的反串的后缀平衡树，而非 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后缀平衡树，就可以完成上述转换．平衡树的添加和删除都是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，所以添加或者删除一个字符的时间复杂度为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．记添加和删除的总字符数为 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么这一部分总的时间复杂度为 𝑂(𝑁log⁡𝑛)O(Nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于操作 3，𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的出现次数等于以 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为前缀的后缀数量，而以 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为前缀的后缀数量等于其后继的排名减去其前驱的排名．在 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后面加入一个极大的字符，就可以构造出 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个后继．将 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最后一个字符减小 1，就可以构造出 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个前驱．

现在要查询某一个串 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在后缀平衡树中排名，由于不能保证 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在后缀平衡树中出现过，所以每次只能暴力比较字符串大小．单次比较的时间复杂度为 𝑂(|𝑡|)O(|t|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每次查询至多比较 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，所以单次查询的复杂度为 𝑂(|𝑡|log⁡𝑛)O(|t|log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．记所有询问串的长度和为 𝐿L![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么这一部分总的时间复杂度为 𝑂(𝐿log⁡𝑛)O(Llog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

SGT 版本的参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 ``` |  ```text #include <algorithm> #include <iostream> #include <string> using namespace std ; constexpr int N = 8e5 \+ 5 ; constexpr double INF = 1e18 ; void decode ( string & s , int len , int mask ) { for ( int i = 0 ; i < len ; ++ i ) { mask = ( mask * 131 \+ i ) % len ; swap ( s [ i ], s [ mask ]); } } int q , n , na ; string a ; char t [ N ]; // SuffixBST(SGT Ver) // 顺序加入，查询时将询问串翻转 // 以i结束的前缀，对应节点的编号为i // 注意：不能写懒惰删除，否则可能会破坏树的结构 constexpr double alpha = 0.75 ; int root ; int sz [ N ], L [ N ], R [ N ]; double tag [ N ]; int buffer_size , buffer [ N ]; bool cmp ( int x , int y ) { if ( t [ x ] != t [ y ]) return t [ x ] < t [ y ]; return tag [ x \- 1 ] < tag [ y \- 1 ]; } void init () { root = 0 ; } void new_node ( int & rt , int p , double lv , double rv ) { rt = p ; sz [ rt ] = 1 ; tag [ rt ] = ( lv \+ rv ) / 2 ; L [ rt ] = R [ rt ] = 0 ; } void push_up ( int x ) { if ( ! x ) return ; sz [ x ] = sz [ L [ x ]] \+ 1 \+ sz [ R [ x ]]; } bool balance ( int rt ) { return alpha * sz [ rt ] > max ( sz [ L [ rt ]], sz [ R [ rt ]]); } void flatten ( int rt ) { if ( ! rt ) return ; flatten ( L [ rt ]); buffer [ ++ buffer_size ] = rt ; flatten ( R [ rt ]); } void build ( int & rt , int l , int r , double lv , double rv ) { if ( l > r ) { rt = 0 ; return ; } int mid = ( l \+ r ) >> 1 ; double mv = ( lv \+ rv ) / 2 ; rt = buffer [ mid ]; tag [ rt ] = mv ; build ( L [ rt ], l , mid \- 1 , lv , mv ); build ( R [ rt ], mid \+ 1 , r , mv , rv ); push_up ( rt ); } void rebuild ( int & rt , double lv , double rv ) { buffer_size = 0 ; flatten ( rt ); build ( rt , 1 , buffer_size , lv , rv ); } void insert ( int & rt , int p , double lv , double rv ) { if ( ! rt ) { new_node ( rt , p , lv , rv ); return ; } if ( cmp ( p , rt )) insert ( L [ rt ], p , lv , tag [ rt ]); else insert ( R [ rt ], p , tag [ rt ], rv ); push_up ( rt ); if ( ! balance ( rt )) rebuild ( rt , lv , rv ); } void remove ( int & rt , int p , double lv , double rv ) { if ( ! rt ) return ; if ( rt == p ) { if ( ! L [ rt ] || ! R [ rt ]) { rt = ( L [ rt ] | R [ rt ]); rebuild ( rt , lv , rv ); } else { // 找到rt的前驱来替换rt int nrt = L [ rt ]; while ( R [ nrt ]) { nrt = R [ nrt ]; } remove ( L [ rt ], nrt , lv , tag [ rt ]); L [ nrt ] = L [ rt ]; R [ nrt ] = R [ rt ]; rt = nrt ; tag [ rt ] = ( lv \+ rv ) / 2 ; } } else { double mv = ( lv \+ rv ) / 2 ; if ( cmp ( p , rt )) remove ( L [ rt ], p , lv , mv ); else remove ( R [ rt ], p , mv , rv ); } push_up ( rt ); if ( ! balance ( rt )) rebuild ( rt , lv , rv ); } bool cmp1 ( const string & s , int len , int p ) { for ( int i = 1 ; i <= len ; ++ i , \-- p ) { if ( s [ i ] < t [ p ]) return true ; if ( s [ i ] > t [ p ]) return false ; } return false ; } int query ( int rt , const string & s , int len ) { if ( ! rt ) return 0 ; if ( cmp1 ( s , len , rt )) return query ( L [ rt ], s , len ); else return sz [ L [ rt ]] \+ 1 \+ query ( R [ rt ], s , len ); } void solve () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); n = 0 ; cin >> q ; init (); cin >> a ; na = a . size (); a = " " \+ a ; for ( int i = 1 ; i <= na ; ++ i ) { t [ ++ n ] = a [ i ]; insert ( root , n , 0 , INF ); } int mask = 0 ; char op [ 10 ]; for ( int i = 1 ; i <= q ; ++ i ) { cin >> op ; // 三种情况分别处理 if ( op [ 0 ] == 'A' ) { // ADD cin >> a ; na = a . size (); decode ( a , na , mask ); a = " " \+ a ; for ( int i = 1 ; i <= na ; ++ i ) { t [ ++ n ] = a [ i ]; insert ( root , n , 0 , INF ); } } else if ( op [ 0 ] == 'D' ) { // DEL int x ; cin >> x ; while ( x ) { remove ( root , n , 0 , INF ); \-- n ; \-- x ; } } else if ( op [ 0 ] == 'Q' ) { // QUERY cin >> a ; na = a . size (); decode ( a , na , mask ); a = " " \+ a ; reverse ( a . begin () \+ 1 , a . begin () \+ 1 \+ na ); a . push_back ( 'Z' \+ 1 ); int ans = query ( root , a , na \+ 1 ); \-- a [ na ]; ans -= query ( root , a , na \+ 1 ); cout << ans << '\n' ; mask ^= ans ; } } } int main () { solve (); return 0 ; } ```   
---|---  
  
## 参考资料

  * 陈立杰 -《重量平衡树和后缀平衡树在信息学奥赛中的应用》

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/suffix-bst.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/suffix-bst.md "edit.link.title")  
>  __本页面贡献者：[Enter-tainer](https://github.com/Enter-tainer), [Backl1ght](https://github.com/Backl1ght), [billchenchina](https://github.com/billchenchina), [Ir1d](https://github.com/Ir1d), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [ouuan](https://github.com/ouuan), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
