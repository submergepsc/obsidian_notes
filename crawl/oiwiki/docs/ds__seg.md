# 线段树基础 - OI Wiki

- Source: https://oi-wiki.org/ds/seg/

# 线段树基础

## 引入

线段树是算法竞赛中常用的用来维护 **区间信息** 的数据结构．

线段树可以在 𝑂(log⁡𝑁)O(log⁡N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间复杂度内实现单点修改、区间修改、区间查询（区间求和，求区间最大值，求区间最小值）等操作．

## 线段树的基本结构与建树

### 过程

线段树将每个长度不为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的区间划分成左右两个区间递归求解，把整个线段划分为一个树形结构，通过合并左右两区间信息来求得该区间的信息．这种数据结构可以方便的进行大部分的区间操作．

有个大小为 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数组 𝑎 ={10,11,12,13,14}a={10,11,12,13,14}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要将其转化为线段树，有以下做法：设线段树的根节点编号为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用数组 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来保存我们的线段树，𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 用来保存线段树上编号为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的节点的值（这里每个节点所维护的值就是这个节点所表示的区间总和）．

我们先给出这棵线段树的形态，如图所示：

![](./images/segt1.svg)

图中每个节点中用红色字体标明的区间，表示该节点管辖的 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组上的位置区间．如 𝑑1d1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所管辖的区间就是 [1,5][1,5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑎1,𝑎2,⋯,𝑎5a1,a2,⋯,a5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），即 𝑑1d1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所保存的值是 𝑎1 +𝑎2 +⋯ +𝑎5a1+a2+⋯+a5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑑1 =60d1=60![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示的是 𝑎1 +𝑎2 +⋯ +𝑎5 =60a1+a2+⋯+a5=60![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

通过观察不难发现，𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左儿子节点就是 𝑑2×𝑖d2×i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右儿子节点就是 𝑑2×𝑖+1d2×i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示的是区间 [𝑠,𝑡][s,t]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即 𝑑𝑖 =𝑎𝑠 +𝑎𝑠+1 +⋯ +𝑎𝑡di=as+as+1+⋯+at![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的话，那么 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左儿子节点表示的是区间 [𝑠,𝑠+𝑡2][s,s+t2]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右儿子表示的是区间 [𝑠+𝑡2 +1,𝑡][s+t2+1,t]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在实现时，我们考虑递归建树．设当前的根节点为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果根节点管辖的区间长度已经是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则可以直接根据 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组上相应位置的值初始化该节点．否则我们将该区间从中点处分割为两个子区间，分别进入左右子节点递归建树，最后合并两个子节点的信息．

### 实现

此处给出代码实现，可参考注释理解：

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text void build ( int s , int t , int p ) { // 对 [s,t] 区间建立线段树,当前根的编号为 p if ( s == t ) { d [ p ] = a [ s ]; return ; } int m = s \+ (( t \- s ) >> 1 ); // 移位运算符的优先级小于加减法，所以加上括号 // 如果写成 (s + t) >> 1 可能会超出 int 范围 build ( s , m , p * 2 ), build ( m \+ 1 , t , p * 2 \+ 1 ); // 递归对左右区间建树 d [ p ] = d [ p * 2 ] \+ d [( p * 2 ) \+ 1 ]; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text def build ( s , t , p ): # 对 [s,t] 区间建立线段树,当前根的编号为 p if s == t : d [ p ] = a [ s ] return m = s \+ (( t \- s ) >> 1 ) # 移位运算符的优先级小于加减法，所以加上括号 # 如果写成 (s + t) >> 1 可能会超出 int 范围 build ( s , m , p * 2 ) build ( m \+ 1 , t , p * 2 \+ 1 ) # 递归对左右区间建树 d [ p ] = d [ p * 2 ] \+ d [( p * 2 ) \+ 1 ] ```   
---|---  
  
关于线段树的空间：如果采用堆式存储（2𝑝2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的左儿子，2𝑝 +12p+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的右儿子），若有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个叶子结点，则 d 数组的范围最大为 2⌈log⁡𝑛⌉+12⌈log⁡n⌉+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

分析：容易知道线段树的深度是 ⌈log⁡𝑛⌉⌈log⁡n⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，则在堆式储存情况下叶子节点（包括无用的叶子节点）数量为 2⌈log⁡𝑛⌉2⌈log⁡n⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，又由于其为一棵完全二叉树，则其总节点个数 2⌈log⁡𝑛⌉+1 −12⌈log⁡n⌉+1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．当然如果你懒得计算的话可以直接把数组长度设为 4𝑛4n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为 2⌈log⁡𝑛⌉+1−1𝑛2⌈log⁡n⌉+1−1n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大值在 𝑛 =2𝑥 +1(𝑥 ∈𝑁+)n=2x+1(x∈N+)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时取到，此时节点数为 2⌈log⁡𝑛⌉+1 −1 =2𝑥+2 −1 =4𝑛 −52⌈log⁡n⌉+1−1=2x+2−1=4n−5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

而堆式存储存在无用的叶子节点，可以考虑使用内存池管理线段树节点，每当需要新建节点时从池中获取．自底向上考虑，必有每两个底层节点合并为一个上层节点，因此可以类似哈夫曼树地证明，如果有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个叶子节点，这样的线段树总共有 2𝑛 −12n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个节点．其空间效率优于堆式存储，并且是可能的最优情况．

这样的线段树可以自底向上维护，参考「[统计的力量 - 张昆玮](https://github.com/hzwer/shareOI/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/%E7%BB%9F%E8%AE%A1%E7%9A%84%E5%8A%9B%E9%87%8F%E2%80%94%E2%80%94%E7%BA%BF%E6%AE%B5%E6%A0%91%E5%85%A8%E6%8E%A5%E8%A7%A6_%E5%BC%A0%E6%98%86%E7%8E%AE.pptx)」．

## 线段树的区间查询

### 过程

区间查询，比如求区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的总和（即 𝑎𝑙 +𝑎𝑙+1 +⋯ +𝑎𝑟al+al+1+⋯+ar![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）、求区间最大值/最小值等操作．

![](./images/segt1.svg)

仍然以最开始的图为例，如果要查询区间 [1,5][1,5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的和，那直接获取 𝑑1d1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值（6060![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）即可．

如果要查询的区间为 [3,5][3,5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时就不能直接获取区间的值，但是 [3,5][3,5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以拆成 [3,3][3,3]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 [4,5][4,5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以通过合并这两个区间的答案来求得这个区间的答案．

一般地，如果要查询的区间是 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则可以将其拆成最多为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 **极大** 的区间，合并这些区间即可求出 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的答案．

### 实现

此处给出代码实现，可参考注释理解：

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text int getsum ( int l , int r , int s , int t , int p ) { // [l, r] 为查询区间, [s, t] 为当前节点包含的区间, p 为当前节点的编号 if ( l <= s && t <= r ) return d [ p ]; // 当前区间为询问区间的子集时直接返回当前区间的和 int m = s \+ (( t \- s ) >> 1 ), sum = 0 ; if ( l <= m ) sum += getsum ( l , r , s , m , p * 2 ); // 如果左儿子代表的区间 [s, m] 与询问区间有交集, 则递归查询左儿子 if ( r > m ) sum += getsum ( l , r , m \+ 1 , t , p * 2 \+ 1 ); // 如果右儿子代表的区间 [m + 1, t] 与询问区间有交集, 则递归查询右儿子 return sum ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text def getsum ( l , r , s , t , p ): # [l, r] 为查询区间, [s, t] 为当前节点包含的区间, p 为当前节点的编号 if l <= s and t <= r : return d [ p ] # 当前区间为询问区间的子集时直接返回当前区间的和 m = s \+ (( t \- s ) >> 1 ) sum = 0 if l <= m : sum = sum \+ getsum ( l , r , s , m , p * 2 ) # 如果左儿子代表的区间 [s, m] 与询问区间有交集, 则递归查询左儿子 if r > m : sum = sum \+ getsum ( l , r , m \+ 1 , t , p * 2 \+ 1 ) # 如果右儿子代表的区间 [m + 1, t] 与询问区间有交集, 则递归查询右儿子 return sum ```   
---|---  
  
## 线段树的区间修改与懒惰标记

### 过程

如果要求修改区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，把所有包含在区间 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的节点都遍历一次、修改一次，时间复杂度无法承受．我们这里要引入一个叫做 **「懒惰标记」** 的东西．

懒惰标记，简单来说，就是通过延迟对节点信息的更改，从而减少可能不必要的操作次数．每次执行修改时，我们通过打标记的方法表明该节点对应的区间在某一次操作中被更改，但不更新该节点的子节点的信息．实质性的修改则在下一次访问带有标记的节点时才进行．

仍然以最开始的图为例，我们将执行若干次给区间内的数加上一个值的操作．我们现在给每个节点增加一个 𝑡𝑖ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，表示该节点带的标记值．

最开始时的情况是这样的（为了节省空间，这里不再展示每个节点管辖的区间）：

![](./images/segt2.svg)

现在我们准备给 [3,5][3,5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上的每个数都加上 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据前面区间查询的经验，我们很快找到了两个极大区间 [3,3][3,3]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 [4,5][4,5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（分别对应线段树上的 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号点和 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号点）．

我们直接在这两个节点上进行修改，并给它们打上标记：

![](./images/segt3.svg)

我们发现，33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 号节点的信息虽然被修改了（因为该区间管辖两个数，所以 𝑑3d3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加上的数是 5 ×2 =105×2=10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），但它的两个子节点却还没更新，仍然保留着修改之前的信息．不过不用担心，虽然修改目前还没进行，但当我们要查询这两个子节点的信息时，我们会利用标记修改这两个子节点的信息，使查询的结果依旧准确．

接下来我们查询一下 [4,4][4,4]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 区间上各数字的和．

我们通过递归找到 [4,5][4,5]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 区间，发现该区间并非我们的目标区间，且该区间上还存在标记．这时候就到标记下放的时间了．我们将该区间的两个子区间的信息更新，并清除该区间上的标记．

![](./images/segt4.svg)

现在 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两个节点的值变成了最新的值，查询的结果也是准确的．

### 实现

接下来给出在存在标记的情况下，区间修改和查询操作的参考实现．

区间修改（区间加上某个值）：

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text // [l, r] 为修改区间, c 为被修改的元素的变化量, [s, t] 为当前节点包含的区间, p // 为当前节点的编号 void update ( int l , int r , int c , int s , int t , int p ) { // 当前区间为修改区间的子集时直接修改当前节点的值,然后打标记,结束修改 if ( l <= s && t <= r ) { d [ p ] += ( t \- s \+ 1 ) * c , b [ p ] += c ; return ; } int m = s \+ (( t \- s ) >> 1 ); if ( b [ p ] && s != t ) { // 如果当前节点的懒标记非空,则更新当前节点两个子节点的值和懒标记值 d [ p * 2 ] += b [ p ] * ( m \- s \+ 1 ), d [ p * 2 \+ 1 ] += b [ p ] * ( t \- m ); b [ p * 2 ] += b [ p ], b [ p * 2 \+ 1 ] += b [ p ]; // 将标记下传给子节点 b [ p ] = 0 ; // 清空当前节点的标记 } if ( l <= m ) update ( l , r , c , s , m , p * 2 ); if ( r > m ) update ( l , r , c , m \+ 1 , t , p * 2 \+ 1 ); d [ p ] = d [ p * 2 ] \+ d [ p * 2 \+ 1 ]; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text def update ( l , r , c , s , t , p ): # [l, r] 为修改区间, c 为被修改的元素的变化量, [s, t] 为当前节点包含的区间, p # 为当前节点的编号 if l <= s and t <= r : d [ p ] = d [ p ] \+ ( t \- s \+ 1 ) * c b [ p ] = b [ p ] \+ c return # 当前区间为修改区间的子集时直接修改当前节点的值, 然后打标记, 结束修改 m = s \+ (( t \- s ) >> 1 ) if b [ p ] and s != t : # 如果当前节点的懒标记非空, 则更新当前节点两个子节点的值和懒标记值 d [ p * 2 ] = d [ p * 2 ] \+ b [ p ] * ( m \- s \+ 1 ) d [ p * 2 \+ 1 ] = d [ p * 2 \+ 1 ] \+ b [ p ] * ( t \- m ) # 将标记下传给子节点 b [ p * 2 ] = b [ p * 2 ] \+ b [ p ] b [ p * 2 \+ 1 ] = b [ p * 2 \+ 1 ] \+ b [ p ] # 清空当前节点的标记 b [ p ] = 0 if l <= m : update ( l , r , c , s , m , p * 2 ) if r > m : update ( l , r , c , m \+ 1 , t , p * 2 \+ 1 ) d [ p ] = d [ p * 2 ] \+ d [ p * 2 \+ 1 ] ```   
---|---  
  
区间查询（区间求和）：

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text int getsum ( int l , int r , int s , int t , int p ) { // [l, r] 为查询区间, [s, t] 为当前节点包含的区间, p 为当前节点的编号 if ( l <= s && t <= r ) return d [ p ]; // 当前区间为询问区间的子集时直接返回当前区间的和 int m = s \+ (( t \- s ) >> 1 ); if ( b [ p ]) { // 如果当前节点的懒标记非空,则更新当前节点两个子节点的值和懒标记值 d [ p * 2 ] += b [ p ] * ( m \- s \+ 1 ), d [ p * 2 \+ 1 ] += b [ p ] * ( t \- m ); b [ p * 2 ] += b [ p ], b [ p * 2 \+ 1 ] += b [ p ]; // 将标记下传给子节点 b [ p ] = 0 ; // 清空当前节点的标记 } int sum = 0 ; if ( l <= m ) sum = getsum ( l , r , s , m , p * 2 ); if ( r > m ) sum += getsum ( l , r , m \+ 1 , t , p * 2 \+ 1 ); return sum ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text def getsum ( l , r , s , t , p ): # [l, r] 为查询区间, [s, t] 为当前节点包含的区间, p为当前节点的编号 if l <= s and t <= r : return d [ p ] # 当前区间为询问区间的子集时直接返回当前区间的和 m = s \+ (( t \- s ) >> 1 ) if b [ p ]: # 如果当前节点的懒标记非空, 则更新当前节点两个子节点的值和懒标记值 d [ p * 2 ] = d [ p * 2 ] \+ b [ p ] * ( m \- s \+ 1 ) d [ p * 2 \+ 1 ] = d [ p * 2 \+ 1 ] \+ b [ p ] * ( t \- m ) # 将标记下传给子节点 b [ p * 2 ] = b [ p * 2 ] \+ b [ p ] b [ p * 2 \+ 1 ] = b [ p * 2 \+ 1 ] \+ b [ p ] # 清空当前节点的标记 b [ p ] = 0 sum = 0 if l <= m : sum = getsum ( l , r , s , m , p * 2 ) if r > m : sum = sum \+ getsum ( l , r , m \+ 1 , t , p * 2 \+ 1 ) return sum ```   
---|---  
  
如果你是要实现区间修改为某一个值而不是加上某一个值的话，代码如下：

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``` |  ```text void update ( int l , int r , int c , int s , int t , int p ) { if ( l <= s && t <= r ) { d [ p ] = ( t \- s \+ 1 ) * c , b [ p ] = c , v [ p ] = 1 ; return ; } int m = s \+ (( t \- s ) >> 1 ); // 额外数组储存是否修改值 if ( v [ p ]) { d [ p * 2 ] = b [ p ] * ( m \- s \+ 1 ), d [ p * 2 \+ 1 ] = b [ p ] * ( t \- m ); b [ p * 2 ] = b [ p * 2 \+ 1 ] = b [ p ]; v [ p * 2 ] = v [ p * 2 \+ 1 ] = 1 ; v [ p ] = 0 ; } if ( l <= m ) update ( l , r , c , s , m , p * 2 ); if ( r > m ) update ( l , r , c , m \+ 1 , t , p * 2 \+ 1 ); d [ p ] = d [ p * 2 ] \+ d [ p * 2 \+ 1 ]; } int getsum ( int l , int r , int s , int t , int p ) { if ( l <= s && t <= r ) return d [ p ]; int m = s \+ (( t \- s ) >> 1 ); if ( v [ p ]) { d [ p * 2 ] = b [ p ] * ( m \- s \+ 1 ), d [ p * 2 \+ 1 ] = b [ p ] * ( t \- m ); b [ p * 2 ] = b [ p * 2 \+ 1 ] = b [ p ]; v [ p * 2 ] = v [ p * 2 \+ 1 ] = 1 ; v [ p ] = 0 ; } int sum = 0 ; if ( l <= m ) sum = getsum ( l , r , s , m , p * 2 ); if ( r > m ) sum += getsum ( l , r , m \+ 1 , t , p * 2 \+ 1 ); return sum ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``` |  ```text def update ( l , r , c , s , t , p ): if l <= s and t <= r : d [ p ] = ( t \- s \+ 1 ) * c b [ p ] = c v [ p ] = 1 return m = s \+ (( t \- s ) >> 1 ) if v [ p ]: d [ p * 2 ] = b [ p ] * ( m \- s \+ 1 ) d [ p * 2 \+ 1 ] = b [ p ] * ( t \- m ) b [ p * 2 ] = b [ p * 2 \+ 1 ] = b [ p ] v [ p * 2 ] = v [ p * 2 \+ 1 ] = 1 v [ p ] = 0 if l <= m : update ( l , r , c , s , m , p * 2 ) if r > m : update ( l , r , c , m \+ 1 , t , p * 2 \+ 1 ) d [ p ] = d [ p * 2 ] \+ d [ p * 2 \+ 1 ] def getsum ( l , r , s , t , p ): if l <= s and t <= r : return d [ p ] m = s \+ (( t \- s ) >> 1 ) if v [ p ]: d [ p * 2 ] = b [ p ] * ( m \- s \+ 1 ) d [ p * 2 \+ 1 ] = b [ p ] * ( t \- m ) b [ p * 2 ] = b [ p * 2 \+ 1 ] = b [ p ] v [ p * 2 ] = v [ p * 2 \+ 1 ] = 1 v [ p ] = 0 sum = 0 if l <= m : sum = getsum ( l , r , s , m , p * 2 ) if r > m : sum = sum \+ getsum ( l , r , m \+ 1 , t , p * 2 \+ 1 ) return sum ```   
---|---  
  
## 动态开点线段树

前面讲到堆式储存的情况下，需要给线段树开 4𝑛4n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 大小的数组．为了节省空间，我们可以不一次性建好树，而是在最初只建立一个根结点代表整个区间．当我们需要访问某个子区间时，才建立代表这个区间的子结点．这样我们不再使用 2𝑝2p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 2𝑝 +12p+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结点的儿子，而是用 lsls![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 rsrs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 记录儿子的编号．总之，动态开点线段树的核心思想就是：**结点只有在有需要的时候才被创建** ．

单次操作的时间复杂度是不变的，为 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于每次操作都有可能创建并访问全新的一系列结点，因此 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次单点操作后结点的数量规模是 𝑂(𝑚log⁡𝑛)O(mlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．最多也只需要 2𝑛 −12n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个结点，没有浪费．

单点修改：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text // root 表示整棵线段树的根结点；cnt 表示当前结点个数 int n , cnt , root ; int sum [ n * 2 ], ls [ n * 2 ], rs [ n * 2 ]; // 用法：update(root, 1, n, x, f); 其中 x 为待修改节点的编号 void update ( int & p , int s , int t , int x , int f ) { // 引用传参 if ( ! p ) p = ++ cnt ; // 当结点为空时，创建一个新的结点 if ( s == t ) { sum [ p ] += f ; return ; } int m = s \+ (( t \- s ) >> 1 ); if ( x <= m ) update ( ls [ p ], s , m , x , f ); else update ( rs [ p ], m \+ 1 , t , x , f ); sum [ p ] = sum [ ls [ p ]] \+ sum [ rs [ p ]]; // pushup } ```   
---|---  
  
区间询问：

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // 用法：query(root, 1, n, l, r); int query ( int p , int s , int t , int l , int r ) { if ( ! p ) return 0 ; // 如果结点为空，返回 0 if ( s >= l && t <= r ) return sum [ p ]; int m = s \+ (( t \- s ) >> 1 ), ans = 0 ; if ( l <= m ) ans += query ( ls [ p ], s , m , l , r ); if ( r > m ) ans += query ( rs [ p ], m \+ 1 , t , l , r ); return ans ; } ```   
---|---  
  
区间修改也是一样的，不过下放标记时要注意如果缺少孩子，就直接创建一个新的孩子．或者使用标记永久化技巧．

## 一些优化

这里总结几个线段树的优化：

  * 在叶子节点处无需下放懒惰标记，所以懒惰标记可以不下传到叶子节点．

  * 下放懒惰标记可以写一个专门的函数 `pushdown`，从儿子节点更新当前节点也可以写一个专门的函数 `maintain`（或者对称地用 `pushup`），降低代码编写难度．

  * 标记永久化：如果确定懒惰标记不会在中途被加到溢出（即超过了该类型数据所能表示的最大范围），那么就可以将标记永久化．标记永久化可以避免下传懒惰标记，只需在进行询问时把标记的影响加到答案当中，从而降低程序常数．具体如何处理与题目特性相关，需结合题目来写．这也是树套树和可持久化数据结构中会用到的一种技巧．

## C++ 模板

SegTreeLazyRangeAdd 可以区间加/求和的线段树模板

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 ``` |  ```text #include <bits/stdc++.h> using namespace std ; template < typename T > class SegTreeLazyRangeAdd { vector < T > tree , lazy ; vector < T > * arr ; int n , root , n4 , end ; void maintain ( int cl , int cr , int p ) { int cm = cl \+ ( cr \- cl ) / 2 ; if ( cl != cr && lazy [ p ]) { lazy [ p * 2 ] += lazy [ p ]; lazy [ p * 2 \+ 1 ] += lazy [ p ]; tree [ p * 2 ] += lazy [ p ] * ( cm \- cl \+ 1 ); tree [ p * 2 \+ 1 ] += lazy [ p ] * ( cr \- cm ); lazy [ p ] = 0 ; } } T range_sum ( int l , int r , int cl , int cr , int p ) { if ( l <= cl && cr <= r ) return tree [ p ]; int m = cl \+ ( cr \- cl ) / 2 ; T sum = 0 ; maintain ( cl , cr , p ); if ( l <= m ) sum += range_sum ( l , r , cl , m , p * 2 ); if ( r > m ) sum += range_sum ( l , r , m \+ 1 , cr , p * 2 \+ 1 ); return sum ; } void range_add ( int l , int r , T val , int cl , int cr , int p ) { if ( l <= cl && cr <= r ) { lazy [ p ] += val ; tree [ p ] += ( cr \- cl \+ 1 ) * val ; return ; } int m = cl \+ ( cr \- cl ) / 2 ; maintain ( cl , cr , p ); if ( l <= m ) range_add ( l , r , val , cl , m , p * 2 ); if ( r > m ) range_add ( l , r , val , m \+ 1 , cr , p * 2 \+ 1 ); tree [ p ] = tree [ p * 2 ] \+ tree [ p * 2 \+ 1 ]; } void build ( int s , int t , int p ) { if ( s == t ) { tree [ p ] = ( * arr )[ s ]; return ; } int m = s \+ ( t \- s ) / 2 ; build ( s , m , p * 2 ); build ( m \+ 1 , t , p * 2 \+ 1 ); tree [ p ] = tree [ p * 2 ] \+ tree [ p * 2 \+ 1 ]; } public : explicit SegTreeLazyRangeAdd < T > ( vector < T > v ) { n = v . size (); n4 = n * 4 ; tree = vector < T > ( n4 , 0 ); lazy = vector < T > ( n4 , 0 ); arr = & v ; end = n \- 1 ; root = 1 ; build ( 0 , end , 1 ); arr = nullptr ; } void show ( int p , int depth = 0 ) { if ( p > n4 || tree [ p ] == 0 ) return ; show ( p * 2 , depth \+ 1 ); for ( int i = 0 ; i < depth ; ++ i ) putchar ( '\t' ); printf ( "%d:%d \n " , tree [ p ], lazy [ p ]); show ( p * 2 \+ 1 , depth \+ 1 ); } T range_sum ( int l , int r ) { return range_sum ( l , r , 0 , end , root ); } void range_add ( int l , int r , T val ) { range_add ( l , r , val , 0 , end , root ); } }; ```   
---|---  
  
SegTreeLazyRangeSet 可以区间修改/求和的线段树模板

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 ``` |  ```text #include <bits/stdc++.h> using namespace std ; template < typename T > class SegTreeLazyRangeSet { vector < T > tree , lazy ; vector < T > * arr ; vector < bool > ifLazy ; int n , root , n4 , end ; void maintain ( int cl , int cr , int p ) { int cm = cl \+ ( cr \- cl ) / 2 ; if ( cl != cr && ifLazy [ p ]) { lazy [ p * 2 ] = lazy [ p ], ifLazy [ p * 2 ] = 1 ; lazy [ p * 2 \+ 1 ] = lazy [ p ], ifLazy [ p * 2 \+ 1 ] = 1 ; tree [ p * 2 ] = lazy [ p ] * ( cm \- cl \+ 1 ); tree [ p * 2 \+ 1 ] = lazy [ p ] * ( cr \- cm ); lazy [ p ] = 0 ; ifLazy [ p ] = 0 ; } } T range_sum ( int l , int r , int cl , int cr , int p ) { if ( l <= cl && cr <= r ) return tree [ p ]; int m = cl \+ ( cr \- cl ) / 2 ; T sum = 0 ; maintain ( cl , cr , p ); if ( l <= m ) sum += range_sum ( l , r , cl , m , p * 2 ); if ( r > m ) sum += range_sum ( l , r , m \+ 1 , cr , p * 2 \+ 1 ); return sum ; } void range_set ( int l , int r , T val , int cl , int cr , int p ) { if ( l <= cl && cr <= r ) { lazy [ p ] = val ; ifLazy [ p ] = 1 ; tree [ p ] = ( cr \- cl \+ 1 ) * val ; return ; } int m = cl \+ ( cr \- cl ) / 2 ; maintain ( cl , cr , p ); if ( l <= m ) range_set ( l , r , val , cl , m , p * 2 ); if ( r > m ) range_set ( l , r , val , m \+ 1 , cr , p * 2 \+ 1 ); tree [ p ] = tree [ p * 2 ] \+ tree [ p * 2 \+ 1 ]; } void build ( int s , int t , int p ) { if ( s == t ) { tree [ p ] = ( * arr )[ s ]; return ; } int m = s \+ ( t \- s ) / 2 ; build ( s , m , p * 2 ); build ( m \+ 1 , t , p * 2 \+ 1 ); tree [ p ] = tree [ p * 2 ] \+ tree [ p * 2 \+ 1 ]; } public : explicit SegTreeLazyRangeSet < T > ( vector < T > v ) { n = v . size (); n4 = n * 4 ; tree = vector < T > ( n4 , 0 ); lazy = vector < T > ( n4 , 0 ); ifLazy = vector < bool > ( n4 , 0 ); arr = & v ; end = n \- 1 ; root = 1 ; build ( 0 , end , 1 ); arr = nullptr ; } void show ( int p , int depth = 0 ) { if ( p > n4 || tree [ p ] == 0 ) return ; show ( p * 2 , depth \+ 1 ); for ( int i = 0 ; i < depth ; ++ i ) putchar ( '\t' ); printf ( "%d:%d \n " , tree [ p ], lazy [ p ]); show ( p * 2 \+ 1 , depth \+ 1 ); } T range_sum ( int l , int r ) { return range_sum ( l , r , 0 , end , root ); } void range_set ( int l , int r , T val ) { range_set ( l , r , val , 0 , end , root ); } }; ```   
---|---  
  
## 例题

[luogu P3372【模板】线段树 1](https://www.luogu.com.cn/problem/P3372)

已知一个数列，你需要进行下面两种操作：

  * 将某区间每一个数加上 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 求出某区间每一个数的和．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 ``` |  ```text #include <iostream> using LL = long long ; LL n , a [ 100005 ], d [ 270000 ], b [ 270000 ]; void build ( LL l , LL r , LL p ) { // l:区间左端点 r:区间右端点 p:节点标号 if ( l == r ) { d [ p ] = a [ l ]; // 将节点赋值 return ; } LL m = l \+ (( r \- l ) >> 1 ); build ( l , m , p << 1 ), build ( m \+ 1 , r , ( p << 1 ) | 1 ); // 分别建立子树 d [ p ] = d [ p << 1 ] \+ d [( p << 1 ) | 1 ]; } void update ( LL l , LL r , LL c , LL s , LL t , LL p ) { if ( l <= s && t <= r ) { d [ p ] += ( t \- s \+ 1 ) * c , b [ p ] += c ; // 如果区间被包含了，直接得出答案 return ; } LL m = s \+ (( t \- s ) >> 1 ); if ( b [ p ]) d [ p << 1 ] += b [ p ] * ( m \- s \+ 1 ), d [( p << 1 ) | 1 ] += b [ p ] * ( t \- m ), b [ p << 1 ] += b [ p ], b [( p << 1 ) | 1 ] += b [ p ]; b [ p ] = 0 ; if ( l <= m ) update ( l , r , c , s , m , p << 1 ); // 本行和下面的一行用来更新p*2和p*2+1的节点 if ( r > m ) update ( l , r , c , m \+ 1 , t , ( p << 1 ) | 1 ); d [ p ] = d [ p << 1 ] \+ d [( p << 1 ) | 1 ]; // 计算该节点区间和 } LL getsum ( LL l , LL r , LL s , LL t , LL p ) { if ( l <= s && t <= r ) return d [ p ]; LL m = s \+ (( t \- s ) >> 1 ); if ( b [ p ]) d [ p << 1 ] += b [ p ] * ( m \- s \+ 1 ), d [( p << 1 ) | 1 ] += b [ p ] * ( t \- m ), b [ p << 1 ] += b [ p ], b [( p << 1 ) | 1 ] += b [ p ]; b [ p ] = 0 ; LL sum = 0 ; if ( l <= m ) sum = getsum ( l , r , s , m , p << 1 ); // 本行和下面的一行用来更新p*2和p*2+1的答案 if ( r > m ) sum += getsum ( l , r , m \+ 1 , t , ( p << 1 ) | 1 ); return sum ; } int main () { std :: ios :: sync_with_stdio ( false ); LL q , i1 , i2 , i3 , i4 ; std :: cin >> n >> q ; for ( LL i = 1 ; i <= n ; i ++ ) std :: cin >> a [ i ]; build ( 1 , n , 1 ); while ( q \-- ) { std :: cin >> i1 >> i2 >> i3 ; if ( i1 == 2 ) std :: cout << getsum ( i2 , i3 , 1 , n , 1 ) << std :: endl ; // 直接调用操作函数 else std :: cin >> i4 , update ( i2 , i3 , i4 , 1 , n , 1 ); } return 0 ; } ```   
---|---  
  
[luogu P3373【模板】线段树 2](https://www.luogu.com.cn/problem/P3373)

已知一个数列，你需要进行下面三种操作：

  * 将某区间每一个数乘上 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 将某区间每一个数加上 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 求出某区间每一个数的和．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 ``` |  ```text #include <iostream> using ll = long long ; int n , m ; ll mod ; ll a [ 100005 ], sum [ 400005 ], mul [ 400005 ], laz [ 400005 ]; void up ( int i ) { sum [ i ] = ( sum [( i << 1 )] \+ sum [( i << 1 ) | 1 ]) % mod ; } void pd ( int i , int s , int t ) { int l = ( i << 1 ), r = ( i << 1 ) | 1 , mid = ( s \+ t ) >> 1 ; if ( mul [ i ] != 1 ) { // 懒标记传递，两个懒标记 mul [ l ] *= mul [ i ]; mul [ l ] %= mod ; mul [ r ] *= mul [ i ]; mul [ r ] %= mod ; laz [ l ] *= mul [ i ]; laz [ l ] %= mod ; laz [ r ] *= mul [ i ]; laz [ r ] %= mod ; sum [ l ] *= mul [ i ]; sum [ l ] %= mod ; sum [ r ] *= mul [ i ]; sum [ r ] %= mod ; mul [ i ] = 1 ; } if ( laz [ i ]) { // 懒标记传递 sum [ l ] += laz [ i ] * ( mid \- s \+ 1 ); sum [ l ] %= mod ; sum [ r ] += laz [ i ] * ( t \- mid ); sum [ r ] %= mod ; laz [ l ] += laz [ i ]; laz [ l ] %= mod ; laz [ r ] += laz [ i ]; laz [ r ] %= mod ; laz [ i ] = 0 ; } return ; } void build ( int s , int t , int i ) { mul [ i ] = 1 ; if ( s == t ) { sum [ i ] = a [ s ]; return ; } int mid = s \+ (( t \- s ) >> 1 ); build ( s , mid , i << 1 ); // 建树 build ( mid \+ 1 , t , ( i << 1 ) | 1 ); up ( i ); } void chen ( int l , int r , int s , int t , int i , ll z ) { int mid = s \+ (( t \- s ) >> 1 ); if ( l <= s && t <= r ) { mul [ i ] *= z ; mul [ i ] %= mod ; // 这是取模的 laz [ i ] *= z ; laz [ i ] %= mod ; // 这是取模的 sum [ i ] *= z ; sum [ i ] %= mod ; // 这是取模的 return ; } pd ( i , s , t ); if ( mid >= l ) chen ( l , r , s , mid , ( i << 1 ), z ); if ( mid \+ 1 <= r ) chen ( l , r , mid \+ 1 , t , ( i << 1 ) | 1 , z ); up ( i ); } void add ( int l , int r , int s , int t , int i , ll z ) { int mid = s \+ (( t \- s ) >> 1 ); if ( l <= s && t <= r ) { sum [ i ] += z * ( t \- s \+ 1 ); sum [ i ] %= mod ; // 这是取模的 laz [ i ] += z ; laz [ i ] %= mod ; // 这是取模的 return ; } pd ( i , s , t ); if ( mid >= l ) add ( l , r , s , mid , ( i << 1 ), z ); if ( mid \+ 1 <= r ) add ( l , r , mid \+ 1 , t , ( i << 1 ) | 1 , z ); up ( i ); } ll getans ( int l , int r , int s , int t , int i ) { // 得到答案，可以看下上面懒标记助于理解 int mid = s \+ (( t \- s ) >> 1 ); ll tot = 0 ; if ( l <= s && t <= r ) return sum [ i ]; pd ( i , s , t ); if ( mid >= l ) tot += getans ( l , r , s , mid , ( i << 1 )); tot %= mod ; if ( mid \+ 1 <= r ) tot += getans ( l , r , mid \+ 1 , t , ( i << 1 ) | 1 ); return tot % mod ; } using std :: cin ; using std :: cout ; int main () { // 读入 cin . tie ( nullptr ) -> sync_with_stdio ( false ); int i , j , x , y , bh ; ll z ; cin >> n >> m >> mod ; for ( i = 1 ; i <= n ; i ++ ) cin >> a [ i ]; build ( 1 , n , 1 ); // 建树 for ( i = 1 ; i <= m ; i ++ ) { cin >> bh ; if ( bh == 1 ) { cin >> x >> y >> z ; chen ( x , y , 1 , n , 1 , z ); } else if ( bh == 2 ) { cin >> x >> y >> z ; add ( x , y , 1 , n , 1 , z ); } else if ( bh == 3 ) { cin >> x >> y ; cout << getans ( x , y , 1 , n , 1 ) << '\n' ; } } return 0 ; } ```   
---|---  
  
[HihoCoder 1078 线段树的区间修改](https://vjudge.net/problem/HihoCoder-1078)

假设货架上从左到右摆放了 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种商品，并且依次标号为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中标号为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的商品的价格为 𝑃𝑖Pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．小 Hi 的每次操作分为两种可能，第一种是修改价格：小 Hi 给出一段区间 [𝐿,𝑅][L,R]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一个新的价格 𝑁𝑒𝑤𝑃NewP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所有标号在这段区间中的商品的价格都变成 𝑁𝑒𝑤𝑃NewP![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．第二种操作是询问：小 Hi 给出一段区间 [𝐿,𝑅][L,R]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而小 Ho 要做的便是计算出所有标号在这段区间中的商品的总价格，然后告诉小 Hi．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` |  ```text #include <iostream> int n , a [ 100005 ], d [ 270000 ], b [ 270000 ]; void build ( int l , int r , int p ) { // 建树 if ( l == r ) { d [ p ] = a [ l ]; return ; } int m = l \+ (( r \- l ) >> 1 ); build ( l , m , p << 1 ), build ( m \+ 1 , r , ( p << 1 ) | 1 ); d [ p ] = d [ p << 1 ] \+ d [( p << 1 ) | 1 ]; } void update ( int l , int r , int c , int s , int t , int p ) { // 更新，可以参考前面两个例题 if ( l <= s && t <= r ) { d [ p ] = ( t \- s \+ 1 ) * c , b [ p ] = c ; return ; } int m = s \+ (( t \- s ) >> 1 ); if ( b [ p ]) { d [ p << 1 ] = b [ p ] * ( m \- s \+ 1 ), d [( p << 1 ) | 1 ] = b [ p ] * ( t \- m ); b [ p << 1 ] = b [( p << 1 ) | 1 ] = b [ p ]; b [ p ] = 0 ; } if ( l <= m ) update ( l , r , c , s , m , p << 1 ); if ( r > m ) update ( l , r , c , m \+ 1 , t , ( p << 1 ) | 1 ); d [ p ] = d [ p << 1 ] \+ d [( p << 1 ) | 1 ]; } int getsum ( int l , int r , int s , int t , int p ) { // 取得答案，和前面一样 if ( l <= s && t <= r ) return d [ p ]; int m = s \+ (( t \- s ) >> 1 ); if ( b [ p ]) { d [ p << 1 ] = b [ p ] * ( m \- s \+ 1 ), d [( p << 1 ) | 1 ] = b [ p ] * ( t \- m ); b [ p << 1 ] = b [( p << 1 ) | 1 ] = b [ p ]; b [ p ] = 0 ; } int sum = 0 ; if ( l <= m ) sum = getsum ( l , r , s , m , p << 1 ); if ( r > m ) sum += getsum ( l , r , m \+ 1 , t , ( p << 1 ) | 1 ); return sum ; } int main () { std :: ios :: sync_with_stdio ( false ); std :: cin >> n ; for ( int i = 1 ; i <= n ; i ++ ) std :: cin >> a [ i ]; build ( 1 , n , 1 ); int q , i1 , i2 , i3 , i4 ; std :: cin >> q ; while ( q \-- ) { std :: cin >> i1 >> i2 >> i3 ; if ( i1 == 0 ) std :: cout << getsum ( i2 , i3 , 1 , n , 1 ) << std :: endl ; else std :: cin >> i4 , update ( i2 , i3 , i4 , 1 , n , 1 ); } return 0 ; } ```   
---|---  
  
[2018 Multi-University Training Contest 5 Problem G. Glad You Came](https://acm.hdu.edu.cn/showproblem.php?pid=6356) 解题思路

维护一下每个区间的永久标记就可以了，最后在线段树上跑一边 DFS 统计结果即可．注意打标记的时候加个剪枝优化，否则会 TLE．

## 拓展

线段树应用十分广泛，常见的拓展和变体如下：

  * [可持久化线段树](../persistent-seg/)
  * 各类树套树：
    * [线段树套线段树](../seg-in-seg/)
    * [树状数组套线段树](../seg-in-bit/)
    * [线段树套平衡树](../balanced-in-seg/)
    * [平衡树套树状数组](../seg-in-balanced/)
  * [李超线段树](../li-chao-tree/)
  * [猫树](../cat-tree/)
  * [吉司机线段树](../seg-beats/)

详细内容请参阅相关页面．

## 应用：线段树优化建图

在建图连边的过程中，我们有时会碰到这种题目，一个点向一段连续的区间中的点连边或者一个连续的区间向一个点连边，如果我们真的一条一条连过去，那一旦点的数量多了复杂度就爆炸了，这里就需要用线段树的区间性质来优化我们的建图了．

下面是一个线段树．

![](./images/segt5.svg)

每个节点都代表了一个区间，假设我们要向区间 [2,4][2,4]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连边．

![](./images/segt6.svg)

在一些题目中，还会出现一个区间连向一个点的情况，则我们将上面第一张图的有向边全部反过来即可，上面的树叫做入树，下面这个叫做出树．

![](./images/segt7.svg)

[Legacy](https://codeforces.com/problemset/problem/786/B)

题目大意：有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个点、𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次操作．每一种操作为以下三种类型中的一种：

  * 操作一：连一条 𝑢 →𝑣u→v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有向边，权值为 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 操作二：对于所有 𝑖 ∈[𝑙,𝑟]i∈[l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条 𝑢 →𝑖u→i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有向边，权值为 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 操作三：对于所有 𝑖 ∈[𝑙,𝑟]i∈[l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连一条 𝑖 →𝑢i→u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的有向边，权值为 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

求从点 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到其他点的最短路．

1 ≤𝑛,𝑞 ≤105,1 ≤𝑤 ≤1091≤n,q≤105,1≤w≤109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 ``` |  ```text #include <bitset> #include <iostream> #include <queue> #include <vector> using namespace std ; using ll = long long ; constexpr int N = 1e5 \+ 5 ; using pil = pair < int , ll > ; using pli = pair < ll , int > ; int n , q , s , tot , rt1 , rt2 ; int pos [ N ]; ll dis [ N << 3 ]; vector < pil > e [ N << 3 ]; bitset < ( N << 3 ) > vis ; struct seg { int l , r , lson , rson ; } t [ N << 3 ]; int ls ( int u ) { // 左儿子 return t [ u ]. lson ; } int rs ( int u ) { // 右儿子 return t [ u ]. rson ; } void build ( int & u , int l , int r ) { // 动态开点建造入树 u = ++ tot ; t [ u ] = seg { l , r }; if ( l == r ) { pos [ l ] = u ; return ; } int mid = ( l \+ r ) >> 1 ; build ( t [ u ]. lson , l , mid ); build ( t [ u ]. rson , mid \+ 1 , r ); e [ u ]. emplace_back ( ls ( u ), 0 ); e [ u ]. emplace_back ( rs ( u ), 0 ); } void build2 ( int & u , int l , int r ) { // 动态开点建造出树 if ( l == r ) { u = pos [ l ]; return ; } u = ++ tot ; t [ u ] = seg { l , r }; int mid = ( l \+ r ) >> 1 ; build2 ( t [ u ]. lson , l , mid ); build2 ( t [ u ]. rson , mid \+ 1 , r ); e [ ls ( u )]. emplace_back ( u , 0 ); e [ rs ( u )]. emplace_back ( u , 0 ); } void add1 ( int u , int lr , int rr , int v , ll w ) { // 点向区间连边 if ( lr <= t [ u ]. l && t [ u ]. r <= rr ) { e [ v ]. emplace_back ( u , w ); return ; } int mid = ( t [ u ]. l \+ t [ u ]. r ) >> 1 ; if ( lr <= mid ) { add1 ( ls ( u ), lr , rr , v , w ); } if ( rr > mid ) { add1 ( rs ( u ), lr , rr , v , w ); } } void add2 ( int u , int lr , int rr , int v , ll w ) { // 区间向点连边 if ( lr <= t [ u ]. l && t [ u ]. r <= rr ) { e [ u ]. emplace_back ( v , w ); return ; } int mid = ( t [ u ]. l \+ t [ u ]. r ) >> 1 ; if ( lr <= mid ) { add2 ( ls ( u ), lr , rr , v , w ); } if ( rr > mid ) { add2 ( rs ( u ), lr , rr , v , w ); } } void dij ( int S ) { priority_queue < pli , vector < pli > , greater < pli >> q ; int tot = ( n << 2 ); for ( int i = 1 ; i <= tot ; ++ i ) { dis [ i ] = 1e18 ; } dis [ S ] = 0 ; q . emplace ( dis [ S ], S ); while ( ! q . empty ()) { pli fr = q . top (); q . pop (); int u = fr . second ; if ( vis [ u ]) continue ; for ( pil it : e [ u ]) { int v = it . first ; ll w = it . second ; if ( dis [ v ] > dis [ u ] \+ w ) { dis [ v ] = dis [ u ] \+ w ; q . emplace ( dis [ v ], v ); } } } } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n >> q >> s ; build ( rt1 , 1 , n ); build2 ( rt2 , 1 , n ); for ( int i = 1 , op , u ; i <= q ; ++ i ) { cin >> op >> u ; if ( op == 1 ) { int v ; ll w ; cin >> v >> w ; e [ pos [ u ]]. emplace_back ( pos [ v ], w ); } else if ( op == 2 ) { int l , r ; ll w ; cin >> l >> r >> w ; add1 ( rt1 , l , r , pos [ u ], w ); } else { int l , r ; ll w ; cin >> l >> r >> w ; add2 ( rt2 , l , r , pos [ u ], w ); } } dij ( pos [ s ]); for ( int i = 1 ; i <= n ; ++ i ) { if ( dis [ pos [ i ]] == 1e18 ) { cout << "-1 " ; } else { cout << dis [ pos [ i ]] << ' ' ; } } return 0 ; } ```   
---|---  
  
## 练习题目

  * [luogu P3372【模板】线段树 1](https://www.luogu.com.cn/problem/P3372)
  * [luogu P13825 线段树 1.5【动态开点线段树】](https://www.luogu.com.cn/problem/P13825)
  * [luogu P3373【模板】线段树 2](https://www.luogu.com.cn/problem/P3373)
  * [luogu P4588【TJOI2018】数学计算](https://www.luogu.com.cn/problem/P4588)
  * [luogu P5490【模板】扫描线 & 矩形面积并](https://www.luogu.com.cn/problem/P5490)
  * [luogu P1471 方差](https://www.luogu.com.cn/problem/P1471)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/ds/seg.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/ds/seg.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [hsfzLZH1](https://github.com/hsfzLZH1), [Tiphereth-A](https://github.com/Tiphereth-A), [ksyx](https://github.com/ksyx), [Marcythm](https://github.com/Marcythm), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid), [ChungZH](https://github.com/ChungZH), [Early0v0](https://github.com/Early0v0), [chenryang](https://github.com/chenryang), [Enter-tainer](https://github.com/Enter-tainer), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [HeRaNO](https://github.com/HeRaNO), [konnyakuxzy](https://github.com/konnyakuxzy), [NachtgeistW](https://github.com/NachtgeistW), [orzAtalod](https://github.com/orzAtalod), [wy-luke](https://github.com/wy-luke), [amlhdsan](https://github.com/amlhdsan), [billchenchina](https://github.com/billchenchina), [c-forrest](https://github.com/c-forrest), [Chrogeek](https://github.com/Chrogeek), [countercurrent-time](https://github.com/countercurrent-time), [ethan-enhe](https://github.com/ethan-enhe), [GavinZhengOI](https://github.com/GavinZhengOI), [H-J-Granger](https://github.com/H-J-Granger), [iamtwz](https://github.com/iamtwz), [luoguojie](https://github.com/luoguojie), [AKindMouse](https://github.com/AKindMouse), [AngelKitty](https://github.com/AngelKitty), [chenzheAya](https://github.com/chenzheAya), [CJSoft](https://github.com/CJSoft), [DawnMagnet](https://github.com/DawnMagnet), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Gesrua](https://github.com/Gesrua), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [Henry-ZHR](https://github.com/Henry-ZHR), [hjsjhn](https://github.com/hjsjhn), [hly1204](https://github.com/hly1204), [jaxvanyang](https://github.com/jaxvanyang), [Jebearssica](https://github.com/Jebearssica), [kenlig](https://github.com/kenlig), [Konano](https://github.com/Konano), [kxccc](https://github.com/kxccc), [LovelyBuggies](https://github.com/LovelyBuggies), [lychees](https://github.com/lychees), [Makkiy](https://github.com/Makkiy), [megakite](https://github.com/megakite), [Menci](https://github.com/Menci), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [moon-dim](https://github.com/moon-dim), [onelittlechildawa](https://github.com/onelittlechildawa), [ouuan](https://github.com/ouuan), [P-Y-Y](https://github.com/P-Y-Y), [Peanut-Tang](https://github.com/Peanut-Tang), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [shadowice1984](https://github.com/shadowice1984), [shawlleyw](https://github.com/shawlleyw), [shuzhouliu](https://github.com/shuzhouliu), [sshwy](https://github.com/sshwy), [SukkaW](https://github.com/SukkaW), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [x2e6](https://github.com/x2e6), [Ycrpro](https://github.com/Ycrpro), [yifan0305](https://github.com/yifan0305), [zeningc](https://github.com/zeningc)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
