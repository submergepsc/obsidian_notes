# 回文树 - OI Wiki

- Source: https://oi-wiki.org/string/pam/

# 回文树

## 定义

回文树（EER Tree，Palindromic Tree，也被称为回文自动机）是一种可以存储一个串中所有回文子串的高效数据结构．最初由 Mikhail Rubinchik 和 Arseny M. Shur 在 2015 年发表．它的灵感来源于后缀树等字符串后缀数据结构，使用回文树可以简单高效地解决一系列涉及回文串的问题．

## 结构

回文树大概长这样

![](./images/pam1.png)

和其它自动机类似的，回文树也是由转移边和后缀链接（fail 指针）组成，每个节点都可以代表一个回文子串．

因为回文串长度分为奇数和偶数，我们可以像 manacher 那样加入一个不在字符集中的字符（如 '#'）作为分隔符来将所有回文串的长度都变为奇数，但是这样过于麻烦了．有没有更好的办法呢？

答案自然是有．更好的办法就是建两棵树，一棵树中的节点对应的回文子串长度均为奇数，另一棵树中的节点对应的回文子串长度均为偶数．

和其它的自动机一样，一个节点的 fail 指针指向的是这个节点所代表的回文串的最长回文后缀所对应的节点，但是转移边并非代表在原节点代表的回文串后加一个字符，而是表示在原节点代表的回文串前后各加一个相同的字符（不难理解，因为要保证存的是回文串）．

我们还需要在每个节点上维护此节点对应回文子串的长度 len，这个信息保证了我们可以轻松地构造出回文树．

## 建造

回文树有两个初始状态，分别代表长度为 −1,0−1,0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的回文串．我们可以称它们为奇根，偶根．它们不表示任何实际的字符串，仅作为初始状态存在，这与其他自动机的根节点是异曲同工的．

偶根的 fail 指针指向奇根，而我们并不关心奇根的 fail 指针，因为奇根不可能失配（奇根转移出的下一个状态长度为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即单个字符．一定是回文子串）

类似后缀自动机，我们增量构造回文树．

考虑构造完前 𝑝 −1p−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符的回文树后，向自动机中添加在原串里位置为 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符．

我们从以上一个字符结尾的最长回文子串对应的节点开始，不断沿着 fail 指针走，直到找到一个节点满足 𝑠𝑝 =𝑠𝑝−𝑙𝑒𝑛−1sp=sp−len−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即满足此节点所对应回文子串的上一个字符与待添加字符相同．

这里贴出论文中的那张图

![](./images/pam2.png)

我们通过跳 fail 指针找到 A 所对应的节点，然后两边添加 `X` 就到了现在的回文串了（即 `XAX`），很显然，这个节点就是以 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结尾的最长回文子串对应的树上节点．（同时，这个时候长度 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 节点优势出来了，如果没有 `X` 能匹配条件就是同一个位置的 𝑠𝑝 =𝑠𝑝sp=sp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就自然得到了代表字符 `X` 的节点．）此时要判断一下：没有这个节点，就需要新建．

然后我们还需要求出新建的节点的 fail 指针．具体方法与上面的过程类似，不断跳转 fail 指针，从 `A` 出发，即可找到 `XAX` 的最长回文后缀 `XBX`，将对应节点设为 fail 指针所指的对象即可．

显然，这个节点是不需新建的，`A` 的前 𝑙𝑒𝑛𝐵lenB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位和后 𝑙𝑒𝑛𝐵lenB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位相同，都是 `B`，前 𝑙𝑒𝑛𝐵lenB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的两端根据回文串对应关系，都是 `X`，后面被钦定了是 `X`，于是这个节点 `XBX` 肯定已经被包含了．

如果 fail 没匹配到，那么将它连向长度为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的那个节点，显然这是可行的（因为这是所有节点的后缀）．

## 线性状态数证明

### 定理

对于一个字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它的本质不同回文子串个数最多只有 |𝑠||s|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．

### 证明

考虑使用数学归纳法．

  * 当 |𝑠| =1|s|=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只有一个字符，同时也只有一个子串，并且这个子串是回文的，因此结论成立．

  * 当 |𝑠| >1|s|>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，设 𝑡 =𝑠𝑐t=sc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最后增加一个字符 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后形成的字符串，假设结论对 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 串成立．考虑以最后一个字符 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结尾的回文子串，假设它们的左端点由小到大排序为 𝑙1,𝑙2,…,𝑙𝑘l1,l2,…,lk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由于 𝑡[𝑙1..|𝑡|]t[l1..|t|]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串，因此对于所有位置 𝑙1 ≤𝑝 ≤|𝑡|l1≤p≤|t|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑡[𝑝..|𝑡|] =𝑡[𝑙1..𝑙1 +|𝑡| −𝑝]t[p..|t|]=t[l1..l1+|t|−p]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．所以，对于 1 <𝑖 ≤𝑘1<i≤k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑡[𝑙𝑖..|𝑡|]t[li..|t|]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已经在 𝑡[1..|𝑡| −1]t[1..|t|−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中出现过．因此，每次增加一个字符，本质不同的回文子串个数最多增加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．

由数学归纳法，可知该定理成立．

因此回文树状态数是 𝑂(|𝑠|)O(|s|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．对于每一个状态，它实际只代表一个本质不同的回文子串，即转移到该节点的状态唯一，因此总转移数也是 𝑂(|𝑠|)O(|s|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

## 正确性证明

以上图为例，增加当前字符 `X`，由线性状态数的证明，我们只需要找到包含最后一个字符 `X` 的最长回文后缀，也就是 `XAX`．继续寻找 `XAX` 的最长回文后缀 `XBX`，建立后缀链接．`XBX` 对应状态已经在回文树中出现，包含最后一个字符的回文后缀就是 `XAX`，`XBX` 本身及其对应状态在 fail 树上的所有祖先．

对于 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 回文树的构造，令 𝑛 =|𝑠|n=|s|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然除了跳 fail 指针的其他操作都是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

加入字符时，在上一次的基础上，每次跳 fail 后对应节点在 fail 树的深度 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而连接 fail 后，仅为深度 + 1（但 fail 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时（即到 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 才符合），深度相当于在 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的基础上 +2+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

因为只加入 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符，所以只会加 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次深度，最多也只会跳 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次 fail．

因此，构造 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的回文树的时间复杂度是 𝑂(|𝑠|)O(|s|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 应用

### 本质不同回文子串个数

由线性状态数的证明，容易知道一个串的本质不同回文子串个数等于回文树的状态数（排除奇根和偶根两个状态）．

### 回文子串出现次数

建出回文树，使用类似后缀自动机统计出现次数的方法．

由于回文树的构造过程中，节点本身就是按照拓扑序插入，因此只需要逆序枚举所有状态，将当前状态的出现次数加到其 fail 指针对应状态的出现次数上即可．

例题：[「APIO2014」回文串](https://www.luogu.com.cn/problem/P3649)

定义 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一个子串的存在值为这个子串在 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中出现的次数乘以这个子串的长度．对于给定的字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求所有回文子串中的最大存在值．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 ``` |  ```text #include <algorithm> #include <cstring> #include <iostream> #include <string> using namespace std ; constexpr int MAXN = 300000 \+ 5 ; namespace pam { int sz , tot , last ; int cnt [ MAXN ], ch [ MAXN ][ 26 ], len [ MAXN ], fail [ MAXN ]; char s [ MAXN ]; int node ( int l ) { // 建立一个新节点，长度为 l sz ++ ; memset ( ch [ sz ], 0 , sizeof ( ch [ sz ])); len [ sz ] = l ; fail [ sz ] = cnt [ sz ] = 0 ; return sz ; } void clear () { // 初始化 sz = -1 ; last = 0 ; s [ tot = 0 ] = '$' ; node ( 0 ); node ( -1 ); fail [ 0 ] = 1 ; } int getfail ( int x ) { // 找后缀回文 while ( s [ tot \- len [ x ] \- 1 ] != s [ tot ]) x = fail [ x ]; return x ; } void insert ( char c ) { // 建树 s [ ++ tot ] = c ; int now = getfail ( last ); if ( ! ch [ now ][ c \- 'a' ]) { int x = node ( len [ now ] \+ 2 ); fail [ x ] = ch [ getfail ( fail [ now ])][ c \- 'a' ]; ch [ now ][ c \- 'a' ] = x ; } last = ch [ now ][ c \- 'a' ]; cnt [ last ] ++ ; } long long solve () { long long ans = 0 ; for ( int i = sz ; i >= 0 ; i \-- ) { cnt [ fail [ i ]] += cnt [ i ]; } for ( int i = 1 ; i <= sz ; i ++ ) { // 更新答案 ans = max ( ans , 1l l * len [ i ] * cnt [ i ]); } return ans ; } } // namespace pam string s ; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); pam :: clear (); cin >> s ; for ( int i = 0 ; i < s . size (); i ++ ) { pam :: insert ( s [ i ]); } cout << pam :: solve () << '\n' ; return 0 ; } ```   
---|---  
  
### 最小回文划分

> 给定一个字符串 𝑠(1 ≤|𝑠| ≤105)s(1≤|s|≤105)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求最小的 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得存在 𝑠1,𝑠2,…,𝑠𝑘s1,s2,…,sk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 𝑠𝑖(1 ≤𝑖 ≤𝑘)si(1≤i≤k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为回文串，且 𝑠1,𝑠2,…,𝑠𝑘s1,s2,…,sk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 依次连接后得到的字符串等于 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑动态规划，记 𝑑𝑝[𝑖]dp[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 长度为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀的最小划分数，转移只需要枚举以第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符结尾的所有回文串

𝑑𝑝[𝑖]=1+min𝑠[𝑗+1..𝑖] 为回文串𝑑𝑝[𝑗]dp[i]=1+mins[j+1..i] 为回文串dp[j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于一个字符串最多会有 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个回文子串，因此上述算法的时间复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，无法接受，为了优化转移过程，下面给出一些引理．

记字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 长度为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀为 𝑝𝑟𝑒(𝑠,𝑖)pre(s,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，长度为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后缀为 𝑠𝑢𝑓(𝑠,𝑖)suf(s,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

周期：若 0 <𝑝 ≤|𝑠|0<p≤|s|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，∀1 ≤𝑖 ≤|𝑠| −𝑝,𝑠[𝑖] =𝑠[𝑖 +𝑝]∀1≤i≤|s|−p,s[i]=s[i+p]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就称 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的周期．

border：若 0 ≤𝑟 <|𝑠|0≤r<|s|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑝𝑟𝑒(𝑠,𝑟) =𝑠𝑢𝑓(𝑠,𝑟)pre(s,r)=suf(s,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就称 𝑝𝑟𝑒(𝑠,𝑟)pre(s,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border．

周期和 border 的关系：𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border，当且仅当 |𝑠| −|𝑡||s|−|t|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的周期．

证明

若 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border，那么 𝑝𝑟𝑒(𝑠,|𝑡|) =𝑠𝑢𝑓(𝑠,|𝑡|)pre(s,|t|)=suf(s,|t|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 ∀1 ≤𝑖 ≤|𝑡|,𝑠[𝑖] =𝑠[|𝑠| −|𝑡| +𝑖]∀1≤i≤|t|,s[i]=s[|s|−|t|+i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 |𝑠| −|𝑡||s|−|t|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的周期．

若 |𝑠| −|𝑡||s|−|t|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 周期，则 ∀1 ≤𝑖 ≤|𝑠| −(|𝑠| −|𝑡|) =|𝑡|,𝑠[𝑖] =𝑠[|𝑠| −|𝑡| +𝑖]∀1≤i≤|s|−(|s|−|t|)=|t|,s[i]=s[|s|−|t|+i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 𝑝𝑟𝑒(𝑠,|𝑡|) =𝑠𝑢𝑓(𝑠,|𝑡|)pre(s,|t|)=suf(s,|t|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border．

#### 引理一

𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后缀，𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border 当且仅当 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串．

证明

对于 1 ≤𝑖 ≤|𝑡|1≤i≤|t|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为回文串，因此有 𝑠[𝑖] =𝑠[|𝑠| −𝑖 +1] =𝑠[|𝑠| −|𝑡| +𝑖]s[i]=s[|s|−i+1]=s[|s|−|t|+i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border．

对于 1 ≤𝑖 ≤|𝑡|1≤i≤|t|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border，有 𝑠[𝑖] =𝑠[|𝑠| −|𝑡| +𝑖]s[i]=s[|s|−|t|+i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串，有 𝑠[𝑖] =𝑠[|𝑠| −𝑖 +1]s[i]=s[|s|−i+1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 𝑠[|𝑠| −𝑖 +1] =𝑠[|𝑠| −|𝑡| +𝑖]s[|s|−i+1]=s[|s|−|t|+i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串．

下图中，相同颜色的位置表示字符对应相同．

![](./images/pam3.png)

#### 引理二

𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border (|𝑠| ≤2|𝑡||s|≤2|t|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))，𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串当且仅当 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串．

证明

若 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串，由引理 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是回文串．

若 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串，由 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border，因此 ∀1 ≤𝑖 ≤|𝑡|,𝑠[𝑖] =𝑠[|𝑠| −|𝑡| +𝑖] =𝑠[|𝑠| −𝑖 +1]∀1≤i≤|t|,s[i]=s[|s|−|t|+i]=s[|s|−i+1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为 |𝑠| ≤2|𝑡||s|≤2|t|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是回文串．

#### 引理三

𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border，则 |𝑠| −|𝑡||s|−|t|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的周期，|𝑠| −|𝑡||s|−|t|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小周期，当且仅当 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最长回文真后缀．

#### 引理四

𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个回文串，𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最长回文真后缀，𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最长回文真后缀．令 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为满足 𝑥 =𝑢𝑦,𝑦 =𝑣𝑧x=uy,y=vz![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串，则有下面三条性质

  1. |𝑢| ≥|𝑣||u|≥|v|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

  2. 如果 |𝑢| >|𝑣||u|>|v|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 |𝑢| >|𝑧||u|>|z|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；

  3. 如果 |𝑢| =|𝑣||u|=|v|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑢 =𝑣u=v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

![](./images/pam4.png)

证明

  1. 由引理 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的推论，|𝑢| =|𝑥| −|𝑦||u|=|x|−|y|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小周期，|𝑣| =|𝑦| −|𝑧||v|=|y|−|z|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小周期．考虑反证法，假设 |𝑢| <|𝑣||u|<|v|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的后缀，所以 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的周期，也是 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的周期，而 |𝑣||v|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小周期，矛盾．所以 |𝑢| ≥|𝑣||u|≥|v|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  2. 因为 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border，所以 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀，设字符串 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 𝑥 =𝑣𝑤x=vw![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（如下图所示），其中 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border．考虑反证法，假设 |𝑢| ≤|𝑧||u|≤|z|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 |𝑧𝑢| ≤2|𝑧||zu|≤2|z|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以由引理 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串，由引理 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border，又因为 |𝑢| >|𝑣||u|>|v|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 |𝑤| >|𝑦||w|>|y|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，矛盾．所以 |𝑢| >|𝑧||u|>|z|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀，|𝑢| =|𝑣||u|=|v|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑢 =𝑣u=v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

![](./images/pam5.png)

#### 推论

𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有回文后缀按照长度排序后，可以划分成 log⁡|𝑠|log⁡|s|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段等差数列．

证明

设 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有回文后缀长度从小到大排序为 𝑙1,𝑙2,…,𝑙𝑘l1,l2,…,lk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．对于任意 2 ≤𝑖 ≤𝑘 −12≤i≤k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 𝑙𝑖 −𝑙𝑖−1 =𝑙𝑖+1 −𝑙𝑖li−li−1=li+1−li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑙𝑖−1,𝑙𝑖,𝑙𝑖+1li−1,li,li+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成一个等差数列．否则 𝑙𝑖 −𝑙𝑖−1 ≠𝑙𝑖+1 −𝑙𝑖li−li−1≠li+1−li![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由引理 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑙𝑖+1 −𝑙𝑖 >𝑙𝑖 −𝑙𝑖−1li+1−li>li−li−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑙𝑖+1 −𝑙𝑖 >𝑙𝑖−1li+1−li>li−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑙𝑖+1 >2𝑙𝑖−1li+1>2li−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，若相邻两对回文后缀的长度之差发生变化，那么这个最大长度一定会相对于最小长度翻一倍．显然，长度翻倍最多只会发生 𝑂(log⁡|𝑠|)O(log⁡|s|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，也就是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的回文后缀长度可以划分成 log⁡|𝑠|log⁡|s|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 段等差数列．

该推论也可以通过使用弱周期引理，对 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最长回文后缀的所有 border 按照长度 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分类，𝑥 ∈[20,21),[21,22),…,[2𝑘,𝑛)x∈[20,21),[21,22),…,[2k,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，考虑这 log⁡|𝑠|log⁡|s|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组内每组的最长 border 进行证明．详细证明可以参考金策的《字符串算法选讲》和陈孙立的 2019 年 IOI 国家候选队论文《子串周期查询问题的相关算法及其应用》．

有了这个结论后，我们现在可以考虑如何优化 𝑑𝑝dp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的转移．

#### 优化

回文树上的每个节点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 需要多维护两个信息，𝑑𝑖𝑓𝑓[𝑢]diff[u]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑠𝑙𝑖𝑛𝑘[𝑢]slink[u]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑑𝑖𝑓𝑓[𝑢]diff[u]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示节点 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓𝑎𝑖𝑙[𝑢]fail[u]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所代表的回文串的长度差，即 𝑙𝑒𝑛[𝑢] −𝑙𝑒𝑛[𝑓𝑎𝑖𝑙[𝑢]]len[u]−len[fail[u]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑠𝑙𝑖𝑛𝑘[𝑢]slink[u]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一直沿着 fail 向上跳到第一个节点 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑑𝑖𝑓𝑓[𝑣] ≠𝑑𝑖𝑓𝑓[𝑢]diff[v]≠diff[u]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也就是 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在等差数列中长度最小的那个节点．

根据上面证明的结论，如果使用 𝑠𝑙𝑖𝑛𝑘slink![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指针向上跳的话，每向后填加一个字符，只需要向上跳 𝑂(log⁡|𝑠|)O(log⁡|s|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．因此，可以考虑将一个等差数列表示的所有回文串的 𝑑𝑝dp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值之和（在原问题中指 minmin![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），记录到最长的那一个回文串对应节点上．

𝑔[𝑣]g[v]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所在等差数列的 𝑑𝑝dp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值之和，且 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是这个等差数列中长度最长的节点，则 𝑔[𝑣] =∑𝑠𝑙𝑖𝑛𝑘[𝑥]=𝑠𝑙𝑖𝑛𝑘[𝑣]𝑑𝑝[𝑖 −𝑙𝑒𝑛[𝑥]]g[v]=∑slink[x]=slink[v]dp[i−len[x]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这里 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是当前枚举到的下标．

下面我们考虑如何更新 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组和 𝑑𝑝dp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组．以下图为例，假设当前枚举到第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符，回文树上对应节点为 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑔[𝑥]g[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为橙色三个位置的 𝑑𝑝dp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值之和（最短的回文串 𝑠𝑙𝑖𝑛𝑘[𝑥]slink[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 算在下一个等差数列中）．𝑓𝑎𝑖𝑙[𝑥]fail[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上一次出现位置是 𝑖 −𝑑𝑖𝑓𝑓[𝑥]i−diff[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（在 𝑖 −𝑑𝑖𝑓𝑓[𝑥]i−diff[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处结束），𝑔[𝑓𝑎𝑖𝑙[𝑥]]g[fail[x]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含的 𝑑𝑝dp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值是蓝色位置．因此，𝑔[𝑥]g[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 实际上等于 𝑔[𝑓𝑎𝑖𝑙[𝑥]]g[fail[x]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和多出来一个位置的 𝑑𝑝dp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值之和，多出来的位置是 𝑖 −(𝑙𝑒𝑛[𝑠𝑙𝑖𝑛𝑘[𝑥]] +𝑑𝑖𝑓𝑓[𝑥])i−(len[slink[x]]+diff[x])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．最后再用 𝑔[𝑥]g[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 去更新 𝑑𝑝[𝑖]dp[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这部分等差数列的贡献就计算完毕了，不断跳 𝑠𝑙𝑖𝑛𝑘[𝑥]slink[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，重复这个过程即可．具体实现方式可参考例题代码．

![](./images/pam6.png)

最后，上述做法的正确性依赖于：如果 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓𝑎𝑖𝑙[𝑥]fail[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 属于同一个等差数列，那么 𝑓𝑎𝑖𝑙[𝑥]fail[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 上一次出现位置是 𝑖 −𝑑𝑖𝑓𝑓[𝑥]i−diff[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

根据引理 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑓𝑎𝑖𝑙[𝑥]fail[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 border，因此其在 𝑖 −𝑑𝑖𝑓𝑓[𝑥]i−diff[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处出现．

假设 𝑓𝑎𝑖𝑙[𝑥]fail[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 (𝑖 −𝑑𝑖𝑓𝑓[𝑥],𝑖)(i−diff[x],i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位置出现．由于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑓𝑎𝑖𝑙[𝑥]fail[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 属于同一个等差数列，因此 2|𝑓𝑎𝑖𝑙[𝑥]| ≥𝑥2|fail[x]|≥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．多余的 𝑓𝑎𝑖𝑙[𝑥]fail[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑖 −𝑑𝑖𝑓𝑓[𝑥]i−diff[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 处的 𝑓𝑎𝑖𝑙[𝑥]fail[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有交集，记交集为 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设串 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑢𝑤 =𝑓𝑎𝑖𝑙[𝑥]uw=fail[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．用类似引理 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的方式可以证明，𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是回文串，而 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀 𝑠[𝑖 −𝑙𝑒𝑛[𝑥] +1..𝑗] =𝑢𝑤𝑢s[i−len[x]+1..j]=uwu![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也是回文串，这与 𝑓𝑎𝑖𝑙[𝑥]fail[x]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最长回文前缀（后缀）矛盾．

例题：[Codeforces 932G Palindrome Partition](https://codeforces.com/problemset/problem/932/G)

给定一个字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要求将 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 划分为 𝑡1,𝑡2,…,𝑡𝑘t1,t2,…,tk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶数，且 𝑡𝑖 =𝑡𝑘−𝑖+1ti=tk−i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求这样的划分方案数．

题解

构造字符串 𝑡 = 𝑠[0]𝑠[𝑛 − 1]𝑠[1]𝑠[𝑛 − 2]𝑠[2]𝑠[𝑛 − 3]…𝑠[𝑛 / 2 − 1]𝑠[𝑛 / 2]t= s[0]s[n − 1]s[1]s[n − 2]s[2]s[n − 3]…s[n / 2 − 1]s[n / 2]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，问题等价于求 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的偶回文划分方案数，把上面的转移方程改成求和形式并且只在偶数位置更新 𝑑𝑝dp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 数组即可．时间复杂度 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，空间复杂度 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 ``` |  ```text #include <cstring> #include <iostream> #include <string> using namespace std ; using ll = long long ; constexpr int mod = 1e9 \+ 7 ; constexpr int MAXN = 1000000 \+ 5 ; int add ( int x , int y ) { x += y ; return x >= mod ? x -= mod : x ; } namespace pam { int sz , tot , last ; int ch [ MAXN ][ 26 ], len [ MAXN ], fail [ MAXN ]; int cnt [ MAXN ], dep [ MAXN ], dif [ MAXN ], slink [ MAXN ]; char s [ MAXN ]; int node ( int l ) { // 建立一个长度为 l 的新节点 sz ++ ; memset ( ch [ sz ], 0 , sizeof ( ch [ sz ])); len [ sz ] = l ; fail [ sz ] = 0 ; cnt [ sz ] = 0 ; dep [ sz ] = 0 ; return sz ; } void clear () { // 初始化 sz = -1 ; last = 0 ; s [ tot = 0 ] = '$' ; node ( 0 ); node ( -1 ); fail [ 0 ] = 1 ; } int getfail ( int x ) { // 找到后缀回文 while ( s [ tot \- len [ x ] \- 1 ] != s [ tot ]) x = fail [ x ]; return x ; } void insert ( char c ) { // 建树 s [ ++ tot ] = c ; int now = getfail ( last ); if ( ! ch [ now ][ c \- 'a' ]) { int x = node ( len [ now ] \+ 2 ); fail [ x ] = ch [ getfail ( fail [ now ])][ c \- 'a' ]; dep [ x ] = dep [ fail [ x ]] \+ 1 ; ch [ now ][ c \- 'a' ] = x ; dif [ x ] = len [ x ] \- len [ fail [ x ]]; if ( dif [ x ] == dif [ fail [ x ]]) slink [ x ] = slink [ fail [ x ]]; else slink [ x ] = fail [ x ]; } last = ch [ now ][ c \- 'a' ]; cnt [ last ] ++ ; } } // namespace pam using pam :: dif ; using pam :: fail ; using pam :: len ; using pam :: slink ; int n , dp [ MAXN ], g [ MAXN ]; string s ; char t [ MAXN ]; int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); pam :: clear (); cin >> s ; n = s . size (); s = " " \+ s ; for ( int i = 1 , j = 0 ; i <= n ; i ++ ) t [ ++ j ] = s [ i ], t [ ++ j ] = s [ n \- i \+ 1 ]; dp [ 0 ] = 1 ; for ( int i = 1 ; i <= n ; i ++ ) { pam :: insert ( t [ i ]); for ( int x = pam :: last ; x > 1 ; x = slink [ x ]) { g [ x ] = dp [ i \- len [ slink [ x ]] \- dif [ x ]]; if ( dif [ x ] == dif [ fail [ x ]]) g [ x ] = add ( g [ x ], g [ fail [ x ]]); if ( i % 2 == 0 ) dp [ i ] = add ( dp [ i ], g [ x ]); // 在偶数位置更新 dp 数组 } } cout << dp [ n ]; return 0 ; } ```   
---|---  
  
## 例题

  * [最长双回文串](https://www.luogu.com.cn/problem/P4555)

  * [拉拉队排练](https://www.luogu.com.cn/problem/P1659)

  * [「SHOI2011」双倍回文](https://www.luogu.com.cn/problem/P4287)

  * [HDU 5421 Victor and String](https://acm.hdu.edu.cn/showproblem.php?pid=5421)

  * [CodeChef Palindromeness](https://www.codechef.com/LTIME23/problems/PALPROB)

## 相关资料

  * [EERTREE: An Efficient Data Structure for Processing Palindromes in Strings](https://arxiv.org/pdf/1506.04862)

  * [Palindromic tree](http://adilet.org/blog/palindromic-tree/)

  * 2017 年 IOI 国家候选队论文集 回文树及其应用 翁文涛

  * 2019 年 IOI 国家候选队论文集 子串周期查询问题的相关算法及其应用 陈孙立

  * 字符串算法选讲 金策

  * [A bit more about palindromes](https://codeforces.com/blog/entry/19193)

  * [A Subquadratic Algorithm for Minimum Palindromic Factorization](https://arxiv.org/pdf/1403.2431.pdf)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/pam.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/pam.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [yjl9903](https://github.com/yjl9903), [H-J-Granger](https://github.com/H-J-Granger), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [Tiphereth-A](https://github.com/Tiphereth-A), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [PotassiumWings](https://github.com/PotassiumWings), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [iamtwz](https://github.com/iamtwz), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [aofall](https://github.com/aofall), [CoelacanthusHex](https://github.com/CoelacanthusHex), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [Henry-ZHR](https://github.com/Henry-ZHR), [huhaoo](https://github.com/huhaoo), [kenlig](https://github.com/kenlig), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [Leasier](https://github.com/Leasier), [lychees](https://github.com/lychees), [Marcythm](https://github.com/Marcythm), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [Persdre](https://github.com/Persdre), [shuzhouliu](https://github.com/shuzhouliu), [SukkaW](https://github.com/SukkaW), [TOMWT-qwq](https://github.com/TOMWT-qwq), [ZXyaang](https://github.com/ZXyaang)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
