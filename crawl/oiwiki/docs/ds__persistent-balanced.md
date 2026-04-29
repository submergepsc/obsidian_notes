# 可持久化平衡树 - OI Wiki

- Source: https://oi-wiki.org/ds/persistent-balanced/

# 可持久化平衡树

## 可持久化无旋转 Treap

### 前置知识

**OI 常用的可持久化平衡树** 一般就是 **可持久化无旋转 Treap** 所以推荐首先学习 [**无旋转 Treap**](../treap/)．

### 思想/做法

对于非旋转 Treap，可通过 **Merge** 和 **Split** 操作过程中复制路径上经过的节点（一般在 **Split** 操作中复制，确保不影响以前的版本）就可完成可持久化．

对于旋转 Treap，在复制路径上经过的节点同时，还需复制受旋转影响的节点（若其已为这次操作中复制的节点，则无需再复制），对于一次旋转一般只影响两个节点，那么不会增加其时间复杂度．

上述方法一般被称为 path copying．

「一切可支持操作都可以通过 **Merge Split Newnode Build** 完成」，而 **Build** 操作只用于建造无需理会，**Newnode** （新建节点）就是用来可持久化的工具．

我们来观察一下 **Merge** 和 **Split** ，我们会发现它们都是由上而下的操作！

因此我们完全可以 **参考线段树的可持久化操作** 对它进行可持久化．

### 可持久化操作

**可持久化** 是对 **数据结构** 的一种操作，即保留历史信息，使得在后面可以调用之前的历史版本．

对于 **可持久化线段树** 来说，每一次新建历史版本就是把 **沿途的修改路径** 复制出来

那么对可持久化 Treap（目前国内 OI 常用的版本）来说：

在复制一个节点 𝑋𝑎Xa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 节点的第 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个版本）的新版本 𝑋𝑎+1Xa+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑋X![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 节点的第 𝑎 +1a+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个版本）以后：

  * 如果某个儿子节点 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不用修改信息，那么就把 𝑋𝑎+1Xa+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的指针直接指向 𝑌𝑎Ya![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 节点的第 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个版本）即可．
  * 反之，如果要修改 𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么就在 **递归到下层** 时 **新建** 𝑌𝑎+1Ya+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 节点的第 𝑎 +1a+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个版本）这个新节点用于 **存储新的信息** ，同时把 𝑋𝑎+1Xa+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的指针指向 𝑌𝑎+1Ya+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑌Y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 节点的第 𝑎 +1a+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个版本）．

### 可持久化

需要的东西：

  * 一个 `struct` 数组 存 **每个节点** 的信息（一般叫做 `tree` 数组）；（当然写 **指针版** 平衡树的大佬就可以考虑不用这个数组了）

  * 一个 **根节点数组** ，存每个版本的 _树根_ ，每次查询版本信息时就从 **根数组存的节点** 开始；

  * `split()` 分裂 **从树中分裂出两棵树**

  * `merge()` 合并 **把两棵树按照随机权值合并**

  * `newNode()` 新建一个节点

  * `build()` 建树

#### Split

对于 **分裂操作** ，每次分裂路径时 **新建节点** 指向分出来的路径，用 `std::pair` 存新分裂出来的两棵树的根．

`split(x,k)` 返回一个 `std::pair`;

表示把 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为根的树的前 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素放在 **一棵树** 中，剩下的节点构成在另一棵树中，返回这两棵树的根（first 是第一棵树的根，second 是第二棵树的）．

  * 如果 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **左子树** 的 𝑘𝑒𝑦 ≥𝑘key≥k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 **直接递归进左子树** ，把左子树分出来的第二颗树和当前的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **右子树** 合并．
  * 否则递归 **右子树** ．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text static std :: pair < int , int > _split ( int _x , int k ) { if ( _x == 0 ) return std :: make_pair ( 0 , 0 ); else { int _vs = ++ _cnt ; // 新建节点（可持久化的精髓） _trp [ _vs ] = _trp [ _x ]; std :: pair < int , int > _y ; if ( _trp [ _vs ]. key <= k ) { _y = _split ( _trp [ _vs ]. leaf [ 1 ], k ); _trp [ _vs ]. leaf [ 1 ] = _y . first ; _y . first = _vs ; } else { _y = _split ( _trp [ _vs ]. leaf [ 0 ], k ); _trp [ _vs ]. leaf [ 0 ] = _y . second ; _y . second = _vs ; } _trp [ _vs ]. _update (); return _y ; } } ```   
---|---  
  
#### Merge

`merge(x,y)` 返回 merge 出的树的根．

同样递归实现．如果 **x 的随机权值** >**y 的随机权值** ，则 `merge(x_{rc},y)`，否则 `merge(x,y_{lc})`．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text static int _merge ( int _x , int _y ) { if ( _x == 0 || _y == 0 ) return _x ^ _y ; else { if ( _trp [ _x ]. fix < _trp [ _y ]. fix ) { _trp [ _x ]. leaf [ 1 ] = _merge ( _trp [ _x ]. leaf [ 1 ], _y ); _trp [ _x ]. _update (); return _x ; } else { _trp [ _y ]. leaf [ 0 ] = _merge ( _x , _trp [ _y ]. leaf [ 0 ]); _trp [ _y ]. _update (); return _y ; } } } ```   
---|---  
  
## 可持久化 WBLT

### 前置知识

可持久化 WBLT 由 WBLT 改动而来，所以首先学习 [WBLT](../wblt/)．

### 思想/做法

使用 **路径复制** 的方法，将一次操作中 **修改过** 的节点复制下来，不能影响之前的节点．

### 处理懒标记

为了处理懒标记，我们这样考虑：在一棵持久化的 WBLT 上，一个点可能有多个父亲，但是儿子数量只能是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．pushdown 的下放懒标记的操作，只会影响它的儿子，我们对一个点进行 pushdown，是没有影响的；反而是它的儿子，它的儿子可能不止它一个父亲，将它的标记下放到儿子，可能导致在别的父亲的版本上，多了一个不属于那个版本的懒标记，这就错了；除非它的儿子只有它一个父亲．所以我们应该在 pushdown 的时候，复制一遍儿子，把懒标记打到新的儿子上．

### 实现路径复制

在进行路径复制的时候，我们可以定义一个 refresh 函数，它接受一个节点 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的引用，表示把节点 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 复制一下，产生一个新的节点，重新赋值给 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．使用 refresh 函数的原则是，如果它将要被修改，或者它拥有的儿子即将发生变动（而不是它的儿子的信息将要被修改），那么就 refresh 它，否则不需要．

对于静态的查询，除了 pushdown 之外都不用 refresh．如果保证什么操作都做路径复制，那么 pushdown 和 refresh 的顺序是无所谓的．

### 针对持久化 WBLT 的小优化

这里有一个优化．观察到 pushdown 的时候要复制两个节点，可以写标记永久化，但是刚才说了，如果它的儿子只有它一个父亲，可以不用复制．针对这一个性质，可以进行优化，以减少复制多余的节点．

考虑记录每个节点有多少个父亲（认为每个版本的根都有一个父亲），记为 𝑢𝑠𝑒use![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．每次 refresh 的时候，如果 𝑢𝑠𝑒 ≤1use≤1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则不需要重新复制节点，否则新建节点，并且 𝑢𝑠𝑒use![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 自减 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示父亲带着这个儿子跑了，这样父亲就可以随意修改新的节点而不影响其它版本．另外每次复制节点的时候，如果节点有儿子，那么两个儿子的 𝑢𝑠𝑒use![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 自增 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；合并两个子树时，返回的节点对两个儿子也有一个父亲的 𝑢𝑠𝑒use![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；删除节点时，两个子节点都丢失一个父亲：这样能优化一些时空．

### 代码实现

完整代码（可持久化文艺平衡树）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 ``` |  ```text #include <cstring> #include <iostream> #include <utility> using namespace std ; using LL = long long ; template < int N > struct WBLT { static constexpr double alpha = 0.292 ; int ch [ N << 1 ][ 2 ], siz [ N << 1 ], tot , root , tsh [ N << 1 ], tct ; int val [ N << 1 ]; LL sum [ N << 1 ]; bool rev [ N << 1 ]; int use [ N << 1 ]; WBLT () { root = newnode ( \- ( int )(( 1u << 31 ) \- 1 )); } bool isleaf ( int p ) { return ! ch [ p ][ 0 ]; } void destroy ( int p ) { tsh [ ++ tct ] = p ; } void clone ( int p , int q ) { memcpy ( ch [ p ], ch [ q ], sizeof ch [ 0 ]); val [ p ] = val [ q ]; siz [ p ] = siz [ q ]; sum [ p ] = sum [ q ]; rev [ p ] = rev [ q ]; if ( ! isleaf ( p )) { use [ ch [ p ][ 0 ]] += 1 ; use [ ch [ p ][ 1 ]] += 1 ; } } int newnode ( LL v ) { int p = tct ? tsh [ tct \-- ] : ++ tot ; memset ( ch [ p ], 0 , sizeof ch [ p ]); val [ p ] = v ; siz [ p ] = 1 ; sum [ p ] = v ; rev [ p ] = false ; use [ p ] = 1 ; return p ; } void refresh ( int & p ) { if ( use [ p ] <= 1 ) return ; use [ p ] -= 1 ; int q = exchange ( p , newnode ( 0 )); clone ( p , q ); } void maintain ( int p ) { // also known as: pushup if ( isleaf ( p )) return ; val [ p ] = val [ ch [ p ][ 1 ]]; sum [ p ] = sum [ ch [ p ][ 0 ]] \+ sum [ ch [ p ][ 1 ]]; siz [ p ] = siz [ ch [ p ][ 0 ]] \+ siz [ ch [ p ][ 1 ]]; } void spread ( int & p ) { if ( isleaf ( p )) return ; refresh ( p ); rev [ p ] ^= 1 ; } void pushdown ( int p ) { if ( ! rev [ p ] || isleaf ( p )) return ; spread ( ch [ p ][ 0 ]), spread ( ch [ p ][ 1 ]); swap ( ch [ p ][ 0 ], ch [ p ][ 1 ]); rev [ p ] = false ; } void rotate ( int p , int r ) { if ( isleaf ( p ) || isleaf ( ch [ p ][ r ])) return ; refresh ( ch [ p ][ r ]); pushdown ( ch [ p ][ r ]); int q = ch [ p ][ r ]; swap ( ch [ p ][ 0 ], ch [ p ][ 1 ]); swap ( ch [ p ][ r ], ch [ q ][ r ]); swap ( ch [ q ][ 0 ], ch [ q ][ 1 ]); maintain ( q ); maintain ( p ); } void update ( int p ) { // also known as: maintain if ( isleaf ( p )) return ; int r = siz [ ch [ p ][ 0 ]] < siz [ ch [ p ][ 1 ]]; if ( siz [ ch [ p ][ ! r ]] >= siz [ p ] * alpha ) return ; refresh ( ch [ p ][ r ]); pushdown ( ch [ p ][ r ]); if ( siz [ ch [ ch [ p ][ r ]][ ! r ]] >= siz [ ch [ p ][ r ]] * ( 1 \- alpha * 2 ) / ( 1 \- alpha )) rotate ( ch [ p ][ r ], ! r ); rotate ( p , r ); } void insert ( int & p , int v , int k ) { refresh ( p ); pushdown ( p ); int r = siz [ ch [ p ][ 0 ]] < k ; if ( isleaf ( p )) { ch [ p ][ 0 ] = newnode ( val [ p ]); ch [ p ][ 1 ] = newnode ( v ); } else { if ( r ) k -= siz [ ch [ p ][ 0 ]]; insert ( ch [ p ][ r ], v , k ); } maintain ( p ); update ( p ); } void erase ( int & p , int k ) { refresh ( p ); pushdown ( p ); int r = siz [ ch [ p ][ 0 ]] < k ; if ( isleaf ( ch [ p ][ r ])) { use [ ch [ p ][ 0 ]] -= 1 ; use [ ch [ p ][ 1 ]] -= 1 ; clone ( p , ch [ p ][ ! r ]); } else { if ( r ) k -= siz [ ch [ p ][ 0 ]]; erase ( ch [ p ][ r ], k ); } maintain ( p ); update ( p ); } int merge ( int p , int q ) { if ( ! p || ! q ) return p \+ q ; if ( min ( siz [ p ], siz [ q ]) >= alpha * ( siz [ p ] \+ siz [ q ])) { int t = newnode ( 0 ); ch [ t ][ 0 ] = p , use [ p ] += 1 ; ch [ t ][ 1 ] = q , use [ q ] += 1 ; maintain ( t ); return t ; } if ( siz [ p ] >= siz [ q ]) { pushdown ( p ); if ( siz [ ch [ p ][ 0 ]] >= alpha * ( siz [ p ] \+ siz [ q ])) { return merge ( ch [ p ][ 0 ], merge ( ch [ p ][ 1 ], q )); } else { pushdown ( ch [ p ][ 1 ]); return merge ( merge ( ch [ p ][ 0 ], ch [ ch [ p ][ 1 ]][ 0 ]), merge ( ch [ ch [ p ][ 1 ]][ 1 ], q )); } } else { pushdown ( q ); if ( siz [ ch [ q ][ 1 ]] >= alpha * ( siz [ p ] \+ siz [ q ])) { return merge ( merge ( p , ch [ q ][ 0 ]), ch [ q ][ 1 ]); } else { pushdown ( ch [ q ][ 0 ]); return merge ( merge ( p , ch [ ch [ q ][ 0 ]][ 0 ]), merge ( ch [ ch [ q ][ 0 ]][ 1 ], ch [ q ][ 1 ])); } } } void split ( int p , int k , int & x , int & y ) { if ( ! k ) return x = 0 , y = p , void (); if ( isleaf ( p )) return x = p , y = 0 , void (); pushdown ( p ); if ( k <= siz [ ch [ p ][ 0 ]]) { split ( ch [ p ][ 0 ], k , x , y ); y = merge ( y , ch [ p ][ 1 ]); } else { split ( ch [ p ][ 1 ], k \- siz [ ch [ p ][ 0 ]], x , y ); x = merge ( ch [ p ][ 0 ], x ); } } LL getsum ( int L , int R , int & p , int l , int r ) { if ( L <= l && r <= R ) return sum [ p ]; pushdown ( p ); int mid = l \+ siz [ ch [ p ][ 0 ]] \- 1 ; LL ret = 0 ; if ( L <= mid ) ret += getsum ( L , R , ch [ p ][ 0 ], l , mid ); if ( mid < R ) ret += getsum ( L , R , ch [ p ][ 1 ], mid \+ 1 , r ); return ret ; } LL getsum ( int & p , int L , int R ) { return getsum ( L \+ 1 , R \+ 1 , p , 1 , siz [ p ]); } }; WBLT < 6400010 > t ; int m ; int root [ 500010 ]; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> m ; root [ 0 ] = t . root ; LL lastans = 0 ; for ( int i = 1 ; i <= m ; i ++ ) { LL op , l , r ; int v ; cin >> v >> op >> l ; t . use [ root [ i ] = root [ v ]] += 1 ; if ( op != 2 ) cin >> r ; l ^= lastans , r ^= lastans ; int x , y , z ; switch ( op ) { case 1 : t . insert ( root [ i ], r , l \+ 1 ); break ; case 2 : t . erase ( root [ i ], l \+ 1 ); break ; case 3 : t . split ( root [ i ], l , x , y ); t . split ( y , r \- l \+ 1 , y , z ); t . spread ( y ); root [ i ] = t . merge ( x , t . merge ( y , z )); break ; case 4 : cout << ( lastans = t . getsum ( root [ i ], l , r )) << endl ; break ; } } return 0 ; } ```   
---|---  
  
## 例题

[洛谷 P3835【模版】可持久化平衡树](https://www.luogu.com.cn/problem/P3835)

你需要实现一个数据结构，要求提供如下操作（最开始时数据结构内无数据）：

  1. 插入 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数；
  2. 删除 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数（若有多个相同的数，应只删除一个，如果没有请忽略该操作）；
  3. 查询 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数的排名（排名定义为比当前数小的数的个数 + 1）；
  4. 查询排名为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数；
  5. 求 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前驱（前驱定义为小于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且最大的数，如不存在输出 −2 147 483 647−2147483647![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）；
  6. 求 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后继（后继定义为大于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且最小的数，如不存在输出 2 147 483 6472147483647![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

以上操作均基于某一个历史版本，同时生成一个新的版本（操作 3, 4, 5, 6 即保持原版本无变化）．而每个版本的编号则为操作的序号．特别地，最初的版本编号为 0．

就是 **普通平衡树** 一题的可持久化版，操作和该题类似．

只是使用了可持久化的 merge 和 split 操作．

## 推荐的练手题

  1. [「Luogu P3919」可持久化数组（模板题）](https://www.luogu.com.cn/problem/P3919)

  2. [「Codeforces 702F」T-shirt](http://codeforces.com/problemset/problem/702/F)

  3. [「Luogu P5055」可持久化文艺平衡树](https://www.luogu.com.cn/problem/P5055)

  4. [「Luogu P5350」序列](https://www.luogu.com.cn/problem/P5350)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/persistent-balanced.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/persistent-balanced.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [H-J-Granger](https://github.com/H-J-Granger), [sshwy](https://github.com/sshwy), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [NachtgeistW](https://github.com/NachtgeistW), [Konano](https://github.com/Konano), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Henry-ZHR](https://github.com/Henry-ZHR), [ksyx](https://github.com/ksyx), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [Alpha1022](https://github.com/Alpha1022), [Backl1ght](https://github.com/Backl1ght), [caijianhong](https://github.com/caijianhong), [cbioo](https://github.com/cbioo), [Chrogeek](https://github.com/Chrogeek), [ChungZH](https://github.com/ChungZH), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [hly1204](https://github.com/hly1204), [isdanni](https://github.com/isdanni), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Marcythm](https://github.com/Marcythm), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [SukkaW](https://github.com/SukkaW), [Tiphereth-A](https://github.com/Tiphereth-A), [VirtualHawthorn](https://github.com/VirtualHawthorn)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
