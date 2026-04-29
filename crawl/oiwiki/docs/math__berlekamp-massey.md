# Berlekamp–Massey 算法 - OI Wiki

- Source: https://oi-wiki.org/math/berlekamp-massey/

# Berlekamp–Massey 算法

Berlekamp–Massey 算法是一种用于求数列的最短递推式的算法．给定一个长为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数列，如果它的最短递推式的阶数为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 Berlekamp–Massey 算法能够在 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内求出数列的每个前缀的最短递推式．最坏情况下 𝑚 =𝑂(𝑛)m=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此算法的最坏复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 定义

定义一个数列 {𝑎0…𝑎𝑛−1}{a0…an−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递推式为满足下式的序列 {𝑟0…𝑟𝑚}{r0…rm}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

∑𝑚𝑗=0𝑟𝑗𝑎𝑖−𝑗 =0,∀𝑖 ≥𝑚∑j=0mrjai−j=0,∀i≥m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑟0 =1r0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为该递推式的 **阶数** ．

数列 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短递推式即为阶数最小的递推式．

### 做法

与上面定义的稍有不同，这里定义一个新的递推系数 {𝑓0…𝑓𝑚−1}{f0…fm−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足：

𝑎𝑖 =∑𝑚−1𝑗=0𝑓𝑗𝑎𝑖−𝑗−1,∀𝑖 ≥𝑚ai=∑j=0m−1fjai−j−1,∀i≥m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

容易看出 𝑓𝑖 = −𝑟𝑖+1fi=−ri+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且阶数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与之前的定义是相同的．

我们可以增量地求递推式，按顺序考虑 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每一位，并在递推结果出现错误时对递推系数 {𝑓𝑖}{fi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行调整．方便起见，以下将前 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的最短递推式记为 𝐹𝑖 ={𝑓𝑖,𝑗}Fi={fi,j}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

显然初始时有 𝐹0 ={}F0={}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．假设递推系数 𝐹𝑖−1Fi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对数列 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前 𝑖 −1i−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项均成立，这时对第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项就有两种情况：

  1. 递推系数对 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也成立，这时不需要进行任何调整，直接令 𝐹𝑖 =𝐹𝑖−1Fi=Fi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．
  2. 递推系数对 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不成立，这时需要对 𝐹𝑖−1Fi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行调整，得到新的 𝐹𝑖Fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

设 Δ𝑖 =𝑎𝑖 −∑𝑚𝑗=0𝑓𝑖−1,𝑗𝑎𝑖−𝑗−1Δi=ai−∑j=0mfi−1,jai−j−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐹𝑖−1Fi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的递推结果的差值．

如果这是第一次对递推系数进行修改，则说明 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是序列中的第一个非零项．这时直接令 𝐹𝑖Fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可，显然这是一个合法的最短递推式．

否则设上一次对递推系数进行修改时，已考虑的 {𝑎𝑖}{ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的项数为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果存在一个序列 𝐺 ={𝑔0…𝑔𝑚′−1}G={g0…gm′−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足：

∑𝑚′−1𝑗=0𝑔𝑗𝑎𝑖′−𝑗−1 =0,∀𝑖′ ∈[𝑚′,𝑖)∑j=0m′−1gjai′−j−1=0,∀i′∈[m′,i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

并且 ∑𝑚′−1𝑗=0𝑔𝑗𝑎𝑖−𝑗−1 =Δ𝑖∑j=0m′−1gjai−j−1=Δi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么不难发现将 𝐹𝑘Fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 按位分别相加之后即可得到一个合法的递推系数 𝐹𝑖Fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑如何构造 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．一种可行的构造方案是令

𝐺 ={0,0,…,0,Δ𝑖Δ𝑘, −Δ𝑖Δ𝑘𝐹𝑘−1}G={0,0,…,0,ΔiΔk,−ΔiΔkFk−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中前面一共有 𝑖 −𝑘 −1i−k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且最后的 −Δ𝑖Δ𝑘𝐹𝑘−1−ΔiΔkFk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示将 𝐹𝑘−1Fk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 每项乘以 −Δ𝑖Δ𝑘−ΔiΔk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后接在序列后面．

不难验证此时 ∑𝑚′−1𝑗=0𝑔𝑗𝑎𝑖−𝑗−1 =Δ𝑘Δ𝑖Δ𝑘 =Δ𝑖∑j=0m′−1gjai−j−1=ΔkΔiΔk=Δi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此这样构造出的是一个合法的 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．将 𝐹𝑖Fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 赋值为 𝐹𝑘Fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝐺G![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 逐项相加后的结果即可．

如果要求的是符合最开始定义的递推式 {𝑟𝑖}{ri}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则将 {𝑓𝑗}{fj}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 全部取相反数后在最开始插入 𝑟0 =1r0=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

从上述算法流程中可以看出，如果数列的最短递推式的阶数为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则算法的复杂度为 𝑂(𝑛𝑚)O(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．最坏情况下 𝑚 =𝑂(𝑛)m=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此算法的最坏复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在实现算法时，由于每次调整递推系数时都只需要用到上次调整时的递推系数 𝐹𝑘Fk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此如果只需要求整个数列的最短递推式，可以只存储当前递推系数和上次调整时的递推系数，空间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` |  ```text vector < int > berlekamp_massey ( const vector < int > & a ) { vector < int > v , last ; // v is the answer, 0-based, p is the module int k = -1 , delta = 0 ; for ( int i = 0 ; i < ( int ) a . size (); i ++ ) { int tmp = 0 ; for ( int j = 0 ; j < ( int ) v . size (); j ++ ) tmp = ( tmp \+ ( long long ) a [ i \- j \- 1 ] * v [ j ]) % p ; if ( a [ i ] == tmp ) continue ; if ( k < 0 ) { k = i ; delta = ( a [ i ] \- tmp \+ p ) % p ; v = vector < int > ( i \+ 1 ); continue ; } vector < int > u = v ; int val = ( long long )( a [ i ] \- tmp \+ p ) * power ( delta , p \- 2 ) % p ; if ( v . size () < last . size () \+ i \- k ) v . resize ( last . size () \+ i \- k ); ( v [ i \- k \- 1 ] += val ) %= p ; for ( int j = 0 ; j < ( int ) last . size (); j ++ ) { v [ i \- k \+ j ] = ( v [ i \- k \+ j ] \- ( long long ) val * last [ j ]) % p ; if ( v [ i \- k \+ j ] < 0 ) v [ i \- k \+ j ] += p ; } if (( int ) u . size () \- i < ( int ) last . size () \- k ) { last = u ; k = i ; delta = a [ i ] \- tmp ; if ( delta < 0 ) delta += p ; } } for ( auto & x : v ) x = ( p \- x ) % p ; v . insert ( v . begin (), 1 ); return v ; // $\forall i, \sum_{j = 0} ^ m a_{i - j} v_j = 0$ } ```   
---|---  
  
朴素的 Berlekamp–Massey 算法求解的是有限项数列的最短递推式．如果待求递推式的序列有无限项，但已知最短递推式的阶数上界，则只需取出序列的前 2𝑚2m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 项即可求出整个序列的最短递推式．（证明略）

### 应用

由于 Berlekamp–Massey 算法的数值稳定性比较差，在处理实数问题时一般很少使用．为了叙述方便，以下均假定在某个质数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的剩余系下进行运算．

#### 求向量列或矩阵列的最短递推式

如果要求向量列 𝒗𝑖vi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短递推式，设向量的维数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以随机一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维行向量 𝐮𝑇uT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并计算标量序列 {𝒖𝑇𝒗𝑖}{uTvi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短递推式．由 Schwartz–Zippel 引理，二者的最短递推式有至少 1 −𝑛𝑝1−np![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率相同．

求矩阵列 {𝐴𝑖}{Ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短递推式也是类似的，设矩阵的大小为 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则只需随机一个 1 ×𝑛1×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的行向量 𝐮𝑇uT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一个 𝑚 ×1m×1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的列向量 𝒗v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并计算标量序列 {𝒖𝑇𝐴𝑖𝒗}{uTAiv}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短递推式即可．由 Schwartz–Zippel 引理可以类似地得到二者相同的概率至少为 1 −𝑛+𝑚𝑝1−n+mp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 优化矩阵快速幂

设 𝒇𝑖fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 维列向量，并且转移满足 𝒇𝑖 =𝐴𝒇𝑖−1fi=Afi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则可以发现 {𝒇𝑖}{fi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个不超过 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶的线性递推向量列．（证明略）

我们可以直接暴力求出 𝒇0…𝒇2𝑛−1f0…f2n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后用前面提到的做法求出 {𝒇𝑖}{fi}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短递推式，再调用 [常系数齐次线性递推](../poly/linear-recurrence/) 即可．

如果要求的向量是 𝒇𝑚fm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则算法的复杂度是 𝑂(𝑛3 +𝑛log⁡𝑛log⁡𝑚)O(n3+nlog⁡nlog⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个只有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个非零项的稀疏矩阵，则复杂度可以降为 𝑂(𝑛𝑘 +𝑛log⁡𝑛log⁡𝑚)O(nk+nlog⁡nlog⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但由于算法至少需要 𝑂(𝑛𝑘)O(nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间预处理，因此在压力不大的情况下也可以使用 𝑂(𝑛2log⁡𝑚)O(n2log⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的线性递推算法，复杂度同样是可以接受的．

#### 求矩阵的最小多项式

方阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小多项式是次数最小的并且满足 𝑓(𝐴) =0f(A)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的多项式 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实际上最小多项式就是 {𝐴𝑖}{Ai}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小递推式，所以直接调用 Berlekamp–Massey 算法就可以了．如果 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶方阵，则显然最小多项式的次数不超过 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

瓶颈在于求出 𝐴𝑖Ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为如果直接每次做矩阵乘法的话复杂度会达到 𝑂(𝑛4)O(n4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但考虑到求矩阵列的最短递推式时实际上求的是 {𝒖𝑇𝐴𝑖𝒗}{uTAiv}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最短递推式，因此我们只要求出 𝐴𝑖𝒗Aiv![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就行了．

假设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个非零项，则复杂度为 𝑂(𝑘𝑛 +𝑛2)O(kn+n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 求稀疏矩阵行列式

如果能求出方阵 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特征多项式，则常数项乘上 ( −1)𝑛(−1)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是行列式．但是最小多项式不一定就是特征多项式．

实际上如果把 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘上一个随机对角阵 𝐵B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝐴𝐵AB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小多项式有至少 1 −2𝑛2−𝑛𝑝1−2n2−np![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的概率就是特征多项式．最后再除掉 det 𝐵detB![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就行了．

设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 阶方阵，且有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个非零项，则复杂度为 𝑂(𝑘𝑛 +𝑛2)O(kn+n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 求稀疏矩阵的秩

设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 𝑛 ×𝑚n×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的矩阵，首先随机一个 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对角阵 𝑃P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和一个 𝑚 ×𝑚m×m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的对角阵 𝑄Q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 然后计算 𝑄𝐴𝑃𝐴𝑇𝑄QAPATQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小多项式即可．

实际上不用调用矩阵乘法，因为求最小多项式时要用 𝑄𝐴𝑃𝐴𝑇𝑄QAPATQ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 乘一个向量，所以我们依次把这几个矩阵乘到向量里就行了．答案就是最小多项式除掉所有 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 因子后剩下的次数．

设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个非零项，且 𝑛 ≤𝑚n≤m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则复杂度为 𝑂(𝑘𝑛 +𝑛2)O(kn+n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 解稀疏方程组

**问题** ：已知 𝐴𝐱 =𝐛Ax=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 其中 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 𝑛 ×𝑛n×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **满秩** 稀疏矩阵，𝐛b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝐱x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 1 ×𝑛1×n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的列向量．𝐴,𝐛A,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 已知，需要在低于 𝑛𝜔nω![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度内解出 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**做法** ：显然 𝐱 =𝐴−1𝐛x=A−1b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果我们能求出 {𝐴𝑖𝐛}{Aib}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(𝑖 ≥0i≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)) 的最小递推式 {𝑟0…𝑟𝑚−1}{r0…rm−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(𝑚 ≤𝑛m≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)), 那么就有结论

𝐴−1𝐛 = −1𝑟𝑚−1∑𝑚−2𝑖=0𝐴𝑖𝐛𝑟𝑚−2−𝑖A−1b=−1rm−1∑i=0m−2Aibrm−2−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

（证明略）

因为 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是稀疏矩阵，直接按定义递推出 𝐛…𝐴2𝑛−1𝐛b…A2n−1b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

同样地，设 𝐴A![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个非零项，则复杂度为 𝑂(𝑘𝑛 +𝑛2)O(kn+n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 ``` |  ```text vector < int > solve_sparse_equations ( const vector < tuple < int , int , int >> & A , const vector < int > & b ) { int n = ( int ) b . size (); // 0-based vector < vector < int >> f ({ b }); for ( int i = 1 ; i < 2 * n ; i ++ ) { vector < int > v ( n ); auto & u = f . back (); for ( auto [ x , y , z ] : A ) // [x, y, value] v [ x ] = ( v [ x ] \+ ( long long ) u [ y ] * z ) % p ; f . push_back ( v ); } vector < int > w ( n ); mt19937 gen ; for ( auto & x : w ) x = uniform_int_distribution < int > ( 1 , p \- 1 )( gen ); vector < int > a ( 2 * n ); for ( int i = 0 ; i < 2 * n ; i ++ ) for ( int j = 0 ; j < n ; j ++ ) a [ i ] = ( a [ i ] \+ ( long long ) f [ i ][ j ] * w [ j ]) % p ; auto c = berlekamp_massey ( a ); int m = ( int ) c . size (); vector < int > ans ( n ); for ( int i = 0 ; i < m \- 1 ; i ++ ) for ( int j = 0 ; j < n ; j ++ ) ans [ j ] = ( ans [ j ] \+ ( long long ) c [ m \- 2 \- i ] * f [ i ][ j ]) % p ; int inv = power ( p \- c [ m \- 1 ], p \- 2 ); for ( int i = 0 ; i < n ; i ++ ) ans [ i ] = ( long long ) ans [ i ] * inv % p ; return ans ; } ```   
---|---  
  
### 例题

  1. [LibreOJ #163. 高斯消元 2](https://loj.ac/p/163)
  2. [ICPC2021 台北 Gym103443E. Composition with Large Red Plane, Yellow, Black, Gray, and Blue](https://codeforces.com/gym/103443/problem/E)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/berlekamp-massey.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/berlekamp-massey.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [antileaf](https://github.com/antileaf), [Enter-tainer](https://github.com/Enter-tainer), [AntiLeaf](https://github.com/AntiLeaf), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
