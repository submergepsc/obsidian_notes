# 跳表 - OI Wiki

- Source: https://oi-wiki.org/ds/skiplist/

# 跳表

跳表 (Skip List) 是由 William Pugh 发明的一种查找数据结构，支持对数据的快速查找，插入和删除．

跳表的期望空间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，跳表的查询，插入和删除操作的期望时间复杂度都为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 基本思想

顾名思义，跳表是一种类似于链表的数据结构．更加准确地说，跳表是对有序链表的改进．

为方便讨论，后续所有有序链表默认为 **升序** 排序．

一个有序链表的查找操作，就是从头部开始逐个比较，直到当前节点的值大于或者等于目标节点的值．很明显，这个操作的复杂度是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

跳表在有序链表的基础上，引入了 **分层** 的概念．首先，跳表的每一层都是一个有序链表，特别地，最底层是初始的有序链表．每个位于第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的节点有 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率出现在第 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为常数．

记在 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点的跳表中，期望包含 1𝑝1p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的层为第 𝐿(𝑛)L(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层，易得 𝐿(𝑛) =log1𝑝⁡𝑛L(n)=log1p⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在跳表中查找，就是从第 𝐿(𝑛)L(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层开始，水平地逐个比较直至当前节点的下一个节点大于等于目标节点，然后移动至下一层．重复这个过程直至到达第一层且无法继续进行操作．此时，若下一个节点是目标节点，则成功查找；反之，则元素不存在．这样一来，查找的过程中会跳过一些没有必要的比较，所以相比于有序链表的查询，跳表的查询更快．可以证明，跳表查询的平均复杂度为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 复杂度证明

### 空间复杂度

对于一个节点而言，节点的最高层数为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率为 𝑝𝑖−1(1 −𝑝)pi−1(1−p)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，跳表的期望层数为 ∑𝑖≥1𝑖𝑝𝑖−1(1 −𝑝) =11−𝑝∑i≥1ipi−1(1−p)=11−p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且因为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为常数，所以跳表的 **期望空间复杂度** 为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在最坏的情况下，每一层有序链表等于初始有序链表，即跳表的 **最差空间复杂度** 为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 时间复杂度

从后向前分析查找路径，这个过程可以分为从最底层爬到第 𝐿(𝑛)L(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层和后续操作两个部分．在分析时，假设一个节点的具体信息在它被访问之前是未知的．

假设当前我们处于一个第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的节点 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们并不知道 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大层数和 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 左侧节点的最大层数，只知道 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大层数至少为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大层数大于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么下一步应该是向上走，这种情况的概率为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；如果 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大层数等于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么下一步应该是向左走，这种情况概率为 1 −𝑝1−p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

令 𝐶(𝑖)C(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为在一个无限长度的跳表中向上爬 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的期望代价，那么有：

𝐶(0)=0𝐶(𝑖)=(1−𝑝)(1+𝐶(𝑖))+𝑝(1+𝐶(𝑖−1))C(0)=0C(i)=(1−p)(1+C(i))+p(1+C(i−1))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

解得 𝐶(𝑖) =𝑖𝑝C(i)=ip![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由此可以得出：在长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的跳表中，从最底层爬到第 𝐿(𝑛)L(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层的期望步数存在上界 𝐿(𝑛)−1𝑝L(n)−1p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

现在只需要分析爬到第 𝐿(𝑛)L(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层后还要再走多少步．易得，到了第 𝐿(𝑛)L(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层后，向左走的步数不会超过第 𝐿(𝑛)L(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层及更高层的节点数总和，而这个总和的期望为 1𝑝1p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以到了第 𝐿(𝑛)L(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层后向左走的期望步数存在上界 1𝑝1p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．同理，到了第 𝐿(𝑛)L(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 层后向上走的期望步数存在上界 1𝑝1p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

所以，跳表查询的期望查找步数为 𝐿(𝑛)−1𝑝 +2𝑝L(n)−1p+2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，又因为 𝐿(𝑛) =log1𝑝⁡𝑛L(n)=log1p⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以跳表查询的 **期望时间复杂度** 为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在最坏的情况下，每一层有序链表等于初始有序链表，查找过程相当于对最高层的有序链表进行查询，即跳表查询操作的 **最差时间复杂度** 为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

插入操作和删除操作就是进行一遍查询的过程，途中记录需要修改的节点，最后完成修改．易得每一层至多只需要修改一个节点，又因为跳表期望层数为 log1𝑝⁡𝑛log1p⁡n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以插入和修改的 **期望时间复杂度** 也为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 具体实现

### 获取节点的最大层数

模拟以 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率往上加一层，最后和上限值取最小．

```text 1 2 3 4 5 6 ``` |  ```text int randomLevel () { int lv = 1 ; // MAXL = 32, S = 0xFFFF, PS = S * P, P = 1 / 4 while (( rand () & S ) < PS ) ++ lv ; return min ( MAXL , lv ); } ```   
---|---  
  
### 查询

查询跳表中是否存在键值为 `key` 的节点．具体实现时，可以设置两个哨兵节点以减少边界条件的讨论．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text V & find ( const K & key ) { SkipListNode < K , V >* p = head ; // 找到该层最后一个键值小于 key 的节点，然后走向下一层 for ( int i = level ; i >= 0 ; \-- i ) { while ( p -> forward [ i ] -> key < key ) { p = p -> forward [ i ]; } } // 现在是小于，所以还需要再往后走一步 p = p -> forward [ 0 ]; // 成功找到节点 if ( p -> key == key ) return p -> value ; // 节点不存在，返回 INVALID return tail -> value ; } ```   
---|---  
  
### 插入

插入节点 `(key, value)`．插入节点的过程就是先执行一遍查询的过程，中途记录新节点是要插入哪一些节点的后面，最后再执行插入．每一层最后一个键值小于 `key` 的节点，就是需要进行修改的节点．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ``` |  ```text void insert ( const K & key , const V & value ) { // 用于记录需要修改的节点 SkipListNode < K , V > * update [ MAXL \+ 1 ]; SkipListNode < K , V > * p = head ; for ( int i = level ; i >= 0 ; \-- i ) { while ( p -> forward [ i ] -> key < key ) { p = p -> forward [ i ]; } // 第 i 层需要修改的节点为 p update [ i ] = p ; } p = p -> forward [ 0 ]; // 若已存在则修改 if ( p -> key == key ) { p -> value = value ; return ; } // 获取新节点的最大层数 int lv = randomLevel (); if ( lv > level ) { lv = ++ level ; update [ lv ] = head ; } // 新建节点 SkipListNode < K , V > * newNode = new SkipListNode < K , V > ( key , value , lv ); // 在第 0~lv 层插入新节点 for ( int i = lv ; i >= 0 ; \-- i ) { p = update [ i ]; newNode -> forward [ i ] = p -> forward [ i ]; p -> forward [ i ] = newNode ; } ++ length ; } ```   
---|---  
  
### 删除

删除键值为 `key` 的节点．删除节点的过程就是先执行一遍查询的过程，中途记录要删的节点是在哪一些节点的后面，最后再执行删除．每一层最后一个键值小于 `key` 的节点，就是需要进行修改的节点．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` |  ```text bool erase ( const K & key ) { // 用于记录需要修改的节点 SkipListNode < K , V > * update [ MAXL \+ 1 ]; SkipListNode < K , V > * p = head ; for ( int i = level ; i >= 0 ; \-- i ) { while ( p -> forward [ i ] -> key < key ) { p = p -> forward [ i ]; } // 第 i 层需要修改的节点为 p update [ i ] = p ; } p = p -> forward [ 0 ]; // 节点不存在 if ( p -> key != key ) return false ; // 从最底层开始删除 for ( int i = 0 ; i <= level ; ++ i ) { // 如果这层没有 p 删除就完成了 if ( update [ i ] -> forward [ i ] != p ) { break ; } // 断开 p 的连接 update [ i ] -> forward [ i ] = p -> forward [ i ]; } // 回收空间 delete p ; // 删除节点可能导致最大层数减少 while ( level > 0 && head -> forward [ level ] == tail ) \-- level ; // 跳表长度 \-- length ; return true ; } ```   
---|---  
  
### 完整代码

下列代码是用跳表实现的 map．未经正经测试，仅供参考．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 ``` |  ```text #include <cassert> #include <climits> #include <ctime> #include <iostream> #include <map> using namespace std ; template < typename K , typename V > struct SkipListNode { int level ; K key ; V value ; SkipListNode ** forward ; SkipListNode () {} SkipListNode ( K k , V v , int l , SkipListNode * nxt = NULL ) { key = k ; value = v ; level = l ; forward = new SkipListNode * [ l \+ 1 ]; for ( int i = 0 ; i <= l ; ++ i ) forward [ i ] = nxt ; } ~ SkipListNode () { if ( forward != NULL ) delete [] forward ; } }; template < typename K , typename V > struct SkipList { static constexpr int MAXL = 32 ; static constexpr int P = 4 ; static constexpr int S = 0xFFFF ; static constexpr int PS = S / P ; static constexpr int INVALID = INT_MAX ; SkipListNode < K , V > * head , * tail ; int length ; int level ; SkipList () { srand ( time ( nullptr )); level = length = 0 ; tail = new SkipListNode < K , V > ( INVALID , 0 , 0 ); head = new SkipListNode < K , V > ( INVALID , 0 , MAXL , tail ); } ~ SkipList () { delete head ; delete tail ; } int randomLevel () { int lv = 1 ; while (( rand () & S ) < PS ) ++ lv ; return MAXL > lv ? lv : MAXL ; } void insert ( const K & key , const V & value ) { SkipListNode < K , V > * update [ MAXL \+ 1 ]; SkipListNode < K , V > * p = head ; for ( int i = level ; i >= 0 ; \-- i ) { while ( p -> forward [ i ] -> key < key ) { p = p -> forward [ i ]; } update [ i ] = p ; } p = p -> forward [ 0 ]; if ( p -> key == key ) { p -> value = value ; return ; } int lv = randomLevel (); if ( lv > level ) { lv = ++ level ; update [ lv ] = head ; } SkipListNode < K , V > * newNode = new SkipListNode < K , V > ( key , value , lv ); for ( int i = lv ; i >= 0 ; \-- i ) { p = update [ i ]; newNode -> forward [ i ] = p -> forward [ i ]; p -> forward [ i ] = newNode ; } ++ length ; } bool erase ( const K & key ) { SkipListNode < K , V > * update [ MAXL \+ 1 ]; SkipListNode < K , V > * p = head ; for ( int i = level ; i >= 0 ; \-- i ) { while ( p -> forward [ i ] -> key < key ) { p = p -> forward [ i ]; } update [ i ] = p ; } p = p -> forward [ 0 ]; if ( p -> key != key ) return false ; for ( int i = 0 ; i <= level ; ++ i ) { if ( update [ i ] -> forward [ i ] != p ) { break ; } update [ i ] -> forward [ i ] = p -> forward [ i ]; } delete p ; while ( level > 0 && head -> forward [ level ] == tail ) \-- level ; \-- length ; return true ; } V & operator []( const K & key ) { V v = find ( key ); if ( v == tail -> value ) insert ( key , 0 ); return find ( key ); } V & find ( const K & key ) { SkipListNode < K , V > * p = head ; for ( int i = level ; i >= 0 ; \-- i ) { while ( p -> forward [ i ] -> key < key ) { p = p -> forward [ i ]; } } p = p -> forward [ 0 ]; if ( p -> key == key ) return p -> value ; return tail -> value ; } bool count ( const K & key ) { return find ( key ) != tail -> value ; } }; int main () { SkipList < int , int > L ; map < int , int > M ; clock_t s = clock (); for ( int i = 0 ; i < 1e5 ; ++ i ) { int key = rand (), value = rand (); L [ key ] = value ; M [ key ] = value ; } for ( int i = 0 ; i < 1e5 ; ++ i ) { int key = rand (); if ( i & 1 ) { L . erase ( key ); M . erase ( key ); } else { int r1 = L . count ( key ) ? L [ key ] : 0 ; int r2 = M . count ( key ) ? M [ key ] : 0 ; assert ( r1 == r2 ); } } clock_t e = clock (); cout << "Time elapsed: " << ( double )( e \- s ) / CLOCKS_PER_SEC << endl ; // about 0.2s return 0 ; } ```   
---|---  
  
## 跳表的随机访问优化

访问跳表中第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点，相当于访问初始有序链表中的第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点，很明显这个操作的时间复杂度是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，并不足够优秀．

跳表的随机访问优化就是对每一个前向指针，再多维护这个前向指针的长度．假设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是跳表中的节点，其中 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为跳表的第 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点，𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为跳表的第 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点 (𝑎 <𝑏)(a<b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且在跳表的某一层中 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前向指针指向 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么这个前向指针的长度为 𝑏 −𝑎b−a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

现在访问跳表中的第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点，就可以从顶层开始，水平地遍历该层的链表，直到当前节点的位置加上当前节点在该层的前向指针长度大于等于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后移动至下一层．重复这个过程直至到达第一层且无法继续行操作．此时，当前节点就是跳表中第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点．

这样，就可以快速地访问到跳表的第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素．可以证明，这个操作的时间复杂度为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 参考资料

  1. [Skip Lists: A Probabilistic Alternative to Balanced Trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
  2. [Skip List](https://en.wikipedia.org/wiki/Skip_list)
  3. [A Skip List Cookbook](http://cglab.ca/~morin/teaching/5408/refs/p90b.pdf)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/skiplist.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/skiplist.md "edit.link.title")  
>  __本页面贡献者：[Backl1ght](https://github.com/Backl1ght), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [CookiePieWw](https://github.com/CookiePieWw), [HeRaNO](https://github.com/HeRaNO), [ksyx](https://github.com/ksyx), [Xeonacid](https://github.com/Xeonacid)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
