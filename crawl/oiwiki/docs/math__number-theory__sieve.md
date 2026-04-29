# 筛法 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/sieve/

# 筛法

## 素数筛法

### 引入

如果我们想要知道小于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有多少个素数呢？

一个自然的想法是对于小于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的每个数进行一次质数检验．这种暴力的做法显然不能达到最优复杂度．

### 埃拉托斯特尼筛法

#### 过程

考虑这样一件事情：对于任意一个大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么它的 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 倍就是合数（𝑥 >1x>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．利用这个结论，我们可以避免很多次不必要的检测．

如果我们从小到大考虑每个数，然后同时把当前这个数的所有（比自己大的）倍数记为合数，那么运行结束的时候没有被标记的数就是素数了．

#### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text vector < int > prime ; bool is_prime [ N ]; void Eratosthenes ( int n ) { is_prime [ 0 ] = is_prime [ 1 ] = false ; for ( int i = 2 ; i <= n ; ++ i ) is_prime [ i ] = true ; for ( int i = 2 ; i <= n ; ++ i ) { if ( is_prime [ i ]) { prime . push_back ( i ); if (( long long ) i * i > n ) continue ; for ( int j = i * i ; j <= n ; j += i ) // 因为从 2 到 i - 1 的倍数我们之前筛过了，这里直接从 i // 的倍数开始，提高了运行速度 is_prime [ j ] = false ; // 是 i 的倍数的均不是素数 } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text prime = [] is_prime = [ False ] * N def Eratosthenes ( n ): is_prime [ 0 ] = is_prime [ 1 ] = False for i in range ( 2 , n \+ 1 ): is_prime [ i ] = True for i in range ( 2 , n \+ 1 ): if is_prime [ i ]: prime . append ( i ) if i * i > n : continue for j in range ( i * i , n \+ 1 , i ): is_prime [ j ] = False ```   
---|---  
  
以上为 **Eratosthenes 筛法** （埃拉托斯特尼筛法，简称埃氏筛法），时间复杂度是 𝑂(𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

现在我们就来看看推导过程：

如果每一次对数组的操作花费 1 个单位时间，则时间复杂度为：

𝑂(𝜋(𝑛)∑𝑘=1𝑛𝑝𝑘)=𝑂(𝑛𝜋(𝑛)∑𝑘=11𝑝𝑘)O(∑k=1π(n)npk)=O(n∑k=1π(n)1pk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑝𝑘pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 小的素数，𝜋(𝑛)π(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 ≤𝑛≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素数个数．∑𝜋(𝑛)𝑘=1∑k=1π(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第一层 for 循环，其中累加上界 𝜋(𝑛)π(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 `if (prime[i])` 进入 true 分支的次数；𝑛𝑝𝑘npk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示第二层 for 循环的执行次数．

根据 Mertens 第二定理，存在常数 𝐵1B1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得：

𝜋(𝑛)∑𝑘=11𝑝𝑘=log⁡log⁡𝑛+𝐵1+𝑂(1log⁡𝑛)∑k=1π(n)1pk=log⁡log⁡n+B1+O(1log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以 **Eratosthenes 筛法** 的时间复杂度为 𝑂(𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．接下来我们证明 Mertens 第二定理的弱化版本 ∑𝑘≤𝜋(𝑛)1/𝑝𝑘 =𝑂(log⁡log⁡𝑛)∑k≤π(n)1/pk=O(log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

根据 𝜋(𝑛) =Θ(𝑛/log⁡𝑛)π(n)=Θ(n/log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可知第 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个素数的大小为 Θ(𝑛log⁡𝑛)Θ(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．于是就有

𝜋(𝑛)∑𝑘=11𝑝𝑘=𝑂(𝜋(𝑛)∑𝑘=21𝑘log⁡𝑘)=𝑂(∫𝜋(𝑛)2d𝑥𝑥log⁡𝑥)=𝑂(log⁡log⁡𝜋(𝑛))=𝑂(log⁡log⁡𝑛)∑k=1π(n)1pk=O(∑k=2π(n)1klog⁡k)=O(∫2π(n)dxxlog⁡x)=O(log⁡log⁡π(n))=O(log⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当然，上面的做法效率仍然不够高效，应用下面几种方法可以稍微提高算法的执行效率．

#### 筛至平方根

显然，要找到直到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为止的所有素数，仅对不超过 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素数进行筛选就足够了．

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text vector < int > prime ; bool is_prime [ N ]; void Eratosthenes ( int n ) { is_prime [ 0 ] = is_prime [ 1 ] = false ; for ( int i = 2 ; i <= n ; ++ i ) is_prime [ i ] = true ; // i * i <= n 说明 i <= sqrt(n) for ( int i = 2 ; i * i <= n ; ++ i ) { if ( is_prime [ i ]) for ( int j = i * i ; j <= n ; j += i ) is_prime [ j ] = false ; } for ( int i = 2 ; i <= n ; ++ i ) if ( is_prime [ i ]) prime . push_back ( i ); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text prime = [] is_prime = [ False ] * N def Eratosthenes ( n ): is_prime [ 0 ] = is_prime [ 1 ] = False for i in range ( 2 , n \+ 1 ): is_prime [ i ] = True # 让 i 循环到 <= sqrt(n) for i in range ( 2 , isqrt ( n ) \+ 1 ): # `isqrt` 是 Python 3.8 新增的函数 if is_prime [ i ]: for j in range ( i * i , n \+ 1 , i ): is_prime [ j ] = False for i in range ( 2 , n \+ 1 ): if is_prime [ i ]: prime . append ( i ) ```   
---|---  
  
这种优化不会影响渐近时间复杂度，实际上重复以上证明，我们将得到 𝑛ln⁡ln⁡√𝑛 +𝑜(𝑛)nln⁡ln⁡n+o(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，根据对数的性质，它们的渐近相同，但操作次数会明显减少．

#### 只筛奇数

因为除 2 以外的偶数都是合数，所以我们可以直接跳过它们，只用关心奇数就好．

首先，这样做能让我们内存需求减半；其次，所需的操作大约也减半．

#### 减少内存的占用

我们注意到筛选时只需要 `bool` 类型的数组．`bool` 数组的一个元素一般占用 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 字节（即 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比特），但是存储一个布尔值只需要 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个比特就足够了．

我们可以使用 [位操作](../../bit/) 的相关知识，将每个布尔值压到一个比特位中，这样我们仅需使用 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比特（即 𝑛8n8![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 字节）而非 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 字节，可以显著减少内存占用．这种方式被称为「位级压缩」．

值得一提的是，存在自动执行位级压缩的数据结构，如 C++ 中的 `vector<bool>` 和 `bitset<>`．

另外，`vector<bool>` 和 `bitset<>` 对程序有常数优化，时间复杂度 𝑂(𝑛log⁡log⁡𝑛)O(nlog⁡log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的埃氏筛在使用 `bitset<>` 或 `vector<bool>` 优化后，性能甚至超过时间复杂度 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的欧拉筛．

参见 [bitset: 与埃氏筛结合](../../../lang/csl/bitset/#与埃氏筛结合)．

#### 分块筛选

由优化「筛至平方根」可知，不需要一直保留整个 `is_prime[1...n]` 数组．为了进行筛选，只保留到 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素数就足够了，即 `prime[1...sqrt(n)]`．并将整个范围分成块，每个块分别进行筛选．这样，我们就不必同时在内存中保留多个块，而且 CPU 可以更好地处理缓存．

设 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个常数，它决定了块的大小，那么我们就有了 ⌈𝑛𝑠⌉⌈ns⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个块，而块 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(𝑘 =0…⌊𝑛𝑠⌋k=0…⌊ns⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)) 包含了区间 [𝑘𝑠,𝑘𝑠 +𝑠 −1][ks,ks+s−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的数字．我们可以依次处理块，也就是说，对于每个块 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们将遍历所有质数（从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 √𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）并使用它们进行筛选．

值得注意的是，我们在处理第一个数字时需要稍微修改一下策略：首先，应保留 [1,√𝑛][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的所有的质数；第二，数字 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 应该标记为非素数．在处理最后一个块时，不应该忘记最后一个数字 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并不一定位于块的末尾．

以下实现使用块筛选来计算小于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的质数数量．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` |  ```text int count_primes ( int n ) { constexpr static int S = 10000 ; vector < int > primes ; int nsqrt = sqrt ( n ); vector < char > is_prime ( nsqrt \+ 1 , true ); for ( int i = 2 ; i <= nsqrt ; i ++ ) { if ( is_prime [ i ]) { primes . push_back ( i ); for ( int j = i * i ; j <= nsqrt ; j += i ) is_prime [ j ] = false ; } } int result = 0 ; vector < char > block ( S ); for ( int k = 0 ; k * S <= n ; k ++ ) { fill ( block . begin (), block . end (), true ); int start = k * S ; for ( int p : primes ) { int start_idx = ( start \+ p \- 1 ) / p ; int j = max ( start_idx , p ) * p \- start ; for (; j < S ; j += p ) block [ j ] = false ; } if ( k == 0 ) block [ 0 ] = block [ 1 ] = false ; for ( int i = 0 ; i < S && start \+ i <= n ; i ++ ) { if ( block [ i ]) result ++ ; } } return result ; } ```   
---|---  
  
分块筛法的渐近时间复杂度与埃氏筛法是一样的（除非块非常小），但是所需的内存将缩小为 𝑂(√𝑛 +𝑆)O(n+S)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并且有更好的缓存结果． 另一方面，对于每一对块和区间 [1,√𝑛][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的素数都要进行除法，而对于较小的块来说，这种情况要糟糕得多． 因此，在选择常数 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时要保持平衡．

块大小 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取 104104![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 105105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间，可以获得最佳的速度．

### 线性筛法

埃氏筛法仍有优化空间，它会将一个合数重复多次标记．有没有什么办法省掉无意义的步骤呢？答案是肯定的．

如果能让每个合数都只被标记一次，那么时间复杂度就可以降到 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了．

实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text vector < int > pri ; bool not_prime [ N ]; void pre ( int n ) { for ( int i = 2 ; i <= n ; ++ i ) { if ( ! not_prime [ i ]) { pri . push_back ( i ); } for ( int pri_j : pri ) { if ( i * pri_j > n ) break ; not_prime [ i * pri_j ] = true ; if ( i % pri_j == 0 ) { // i % pri_j == 0 // 换言之，i 之前被 pri_j 筛过了 // 由于 pri 里面质数是从小到大的，所以 i 乘上其他的质数的结果一定会被 // pri_j 的倍数筛掉，就不需要在这里先筛一次，所以这里直接 break // 掉就好了 break ; } } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text pri = [] not_prime = [ False ] * N def pre ( n ): for i in range ( 2 , n \+ 1 ): if not not_prime [ i ]: pri . append ( i ) for pri_j in pri : if i * pri_j > n : break not_prime [ i * pri_j ] = True if i % pri_j == 0 : """ i % pri_j == 0 换言之，i 之前被 pri_j 筛过了 由于 pri 里面质数是从小到大的，所以 i 乘上其他的质数的结果一定会被 pri_j 的倍数筛掉，就不需要在这里先筛一次，所以这里直接 break 掉就好了 """ break ```   
---|---  
  
上面的这种 **线性筛法** 也称为 **Euler 筛法** （欧拉筛法）．

Note

注意到筛法求素数的同时也得到了每个数的最小质因子．

## 筛法求欧拉函数

注意到在线性筛中，每一个合数都是被最小的质因子筛掉．比如设 𝑝1p1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小质因子，𝑛′ =𝑛𝑝1n′=np1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么线性筛的过程中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通过 𝑛′ ×𝑝1n′×p1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 筛掉．

观察线性筛的过程，我们还需要处理两个部分，下面对 𝑛′mod𝑝1n′modp1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分情况讨论．

如果 𝑛′mod𝑝1 =0n′modp1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑛′n′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 包含了 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有质因子．

𝜑(𝑛)=𝑛×𝑠∏𝑖=1𝑝𝑖−1𝑝𝑖=𝑝1×𝑛′×𝑠∏𝑖=1𝑝𝑖−1𝑝𝑖=𝑝1×𝜑(𝑛′)φ(n)=n×∏i=1spi−1pi=p1×n′×∏i=1spi−1pi=p1×φ(n′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那如果 𝑛′mod𝑝1 ≠0n′modp1≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 呢，这时 𝑛′n′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑝1p1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是互质的，根据欧拉函数性质，我们有：

𝜑(𝑛)=𝜑(𝑝1)×𝜑(𝑛′)=(𝑝1−1)×𝜑(𝑛′)φ(n)=φ(p1)×φ(n′)=(p1−1)×φ(n′)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text vector < int > pri ; bool not_prime [ N ]; int phi [ N ]; void pre ( int n ) { phi [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; i ++ ) { if ( ! not_prime [ i ]) { pri . push_back ( i ); phi [ i ] = i \- 1 ; } for ( int pri_j : pri ) { if ( i * pri_j > n ) break ; not_prime [ i * pri_j ] = true ; if ( i % pri_j == 0 ) { phi [ i * pri_j ] = phi [ i ] * pri_j ; break ; } phi [ i * pri_j ] = phi [ i ] * phi [ pri_j ]; } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text pri = [] not_prime = [ False ] * N phi = [ 0 ] * N def pre ( n ): phi [ 1 ] = 1 for i in range ( 2 , n \+ 1 ): if not not_prime [ i ]: pri . append ( i ) phi [ i ] = i \- 1 for pri_j in pri : if i * pri_j > n : break not_prime [ i * pri_j ] = True if i % pri_j == 0 : phi [ i * pri_j ] = phi [ i ] * pri_j break phi [ i * pri_j ] = phi [ i ] * phi [ pri_j ] ```   
---|---  
  
## 筛法求莫比乌斯函数

### 定义

根据莫比乌斯函数的定义，设 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个合数，𝑝1p1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小质因子，𝑛′ =𝑛𝑝1n′=np1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有：

𝜇(𝑛)=⎧{ {⎨{ {⎩0𝑛′mod𝑝1=0−𝜇(𝑛′)otherwiseμ(n)={0n′modp1=0−μ(n′)otherwise![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是质数，有 𝜇(𝑛) = −1μ(n)=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text vector < int > pri ; bool not_prime [ N ]; int mu [ N ]; void pre ( int n ) { mu [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; ++ i ) { if ( ! not_prime [ i ]) { mu [ i ] = -1 ; pri . push_back ( i ); } for ( int pri_j : pri ) { if ( i * pri_j > n ) break ; not_prime [ i * pri_j ] = true ; if ( i % pri_j == 0 ) { mu [ i * pri_j ] = 0 ; break ; } mu [ i * pri_j ] = \- mu [ i ]; } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text pri = [] not_prime = [ False ] * N mu = [ 0 ] * N def pre ( n ): mu [ 1 ] = 1 for i in range ( 2 , n \+ 1 ): if not not_prime [ i ]: pri . append ( i ) mu [ i ] = \- 1 for pri_j in pri : if i * pri_j > n : break not_prime [ i * pri_j ] = True if i % pri_j == 0 : mu [ i * pri_j ] = 0 break mu [ i * pri_j ] = \- mu [ i ] ```   
---|---  
  
## 筛法求约数个数

用 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数个数，𝑛𝑢𝑚𝑖numi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小质因子出现次数．

### 约数个数定理

定理：若 𝑛 =∏𝑚𝑖=1𝑝𝑐𝑖𝑖n=∏i=1mpici![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则 𝑑𝑖 =∏𝑚𝑖=1(𝑐𝑖 +1)di=∏i=1m(ci+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明：我们知道 𝑝𝑐𝑖𝑖pici![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数有 𝑝0𝑖,𝑝1𝑖,…,𝑝𝑐𝑖𝑖pi0,pi1,…,pici![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 共 𝑐𝑖 +1ci+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，根据乘法原理，𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数个数就是 ∏𝑚𝑖=1(𝑐𝑖 +1)∏i=1m(ci+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 实现

因为 𝑑𝑖di![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是积性函数，所以可以使用线性筛．

在这里简单介绍一下线性筛实现原理．

  1. 当 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为质数时，𝑛𝑢𝑚𝑖 ←1,𝑑𝑖 ←2numi←1,di←2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，同时设 𝑞 =⌊𝑖𝑝⌋q=⌊ip⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小质因子．
  2. 当 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的质因子时，𝑛𝑢𝑚𝑖 ←𝑛𝑢𝑚𝑞 +1,𝑑𝑖 ←𝑑𝑞𝑛𝑢𝑚𝑖 ×(𝑛𝑢𝑚𝑖 +1)numi←numq+1,di←dqnumi×(numi+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  3. 当 𝑝,𝑞p,q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质时，𝑛𝑢𝑚𝑖 ←1,𝑑𝑖 ←𝑑𝑞 ×(𝑛𝑢𝑚𝑖 +1)numi←1,di←dq×(numi+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text vector < int > pri ; bool not_prime [ N ]; int d [ N ], num [ N ]; void pre ( int n ) { d [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; ++ i ) { if ( ! not_prime [ i ]) { pri . push_back ( i ); d [ i ] = 2 ; num [ i ] = 1 ; } for ( int pri_j : pri ) { if ( i * pri_j > n ) break ; not_prime [ i * pri_j ] = true ; if ( i % pri_j == 0 ) { num [ i * pri_j ] = num [ i ] \+ 1 ; d [ i * pri_j ] = d [ i ] / num [ i * pri_j ] * ( num [ i * pri_j ] \+ 1 ); break ; } num [ i * pri_j ] = 1 ; d [ i * pri_j ] = d [ i ] * 2 ; } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text pri = [] not_prime = [ False ] * N d = [ 0 ] * N num = [ 0 ] * N def pre ( n ): d [ 1 ] = 1 for i in range ( 2 , n \+ 1 ): if not not_prime [ i ]: pri . append ( i ) d [ i ] = 2 num [ i ] = 1 for pri_j in pri : if i * pri_j > n : break not_prime [ i * pri_j ] = True if i % pri_j == 0 : num [ i * pri_j ] = num [ i ] \+ 1 d [ i * pri_j ] = d [ i ] // num [ i * pri_j ] * ( num [ i * pri_j ] \+ 1 ) break num [ i * pri_j ] = 1 d [ i * pri_j ] = d [ i ] * 2 ```   
---|---  
  
## 筛法求约数和

𝑓𝑖fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数和，𝑔𝑖gi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小质因子的 𝑝0 +𝑝1 +𝑝2 +…𝑝𝑘p0+p1+p2+…pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text vector < int > pri ; bool not_prime [ N ]; int g [ N ], f [ N ]; void pre ( int n ) { g [ 1 ] = f [ 1 ] = 1 ; for ( int i = 2 ; i <= n ; ++ i ) { if ( ! not_prime [ i ]) { pri . push_back ( i ); g [ i ] = i \+ 1 ; f [ i ] = i \+ 1 ; } for ( int pri_j : pri ) { if ( i * pri_j > n ) break ; not_prime [ i * pri_j ] = true ; if ( i % pri_j == 0 ) { g [ i * pri_j ] = g [ i ] * pri_j \+ 1 ; f [ i * pri_j ] = f [ i ] / g [ i ] * g [ i * pri_j ]; break ; } f [ i * pri_j ] = f [ i ] * f [ pri_j ]; g [ i * pri_j ] = 1 \+ pri_j ; } } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text pri = [] not_prime = [ False ] * N f = [ 0 ] * N g = [ 0 ] * N def pre ( n ): g [ 1 ] = f [ 1 ] = 1 for i in range ( 2 , n \+ 1 ): if not not_prime [ i ]: pri . append ( i ) g [ i ] = i \+ 1 f [ i ] = i \+ 1 for pri_j in pri : if i * pri_j > n : break not_prime [ i * pri_j ] = True if i % pri_j == 0 : g [ i * pri_j ] = g [ i ] * pri_j \+ 1 f [ i * pri_j ] = f [ i ] // g [ i ] * g [ i * pri_j ] break f [ i * pri_j ] = f [ i ] * f [ pri_j ] g [ i * pri_j ] = 1 \+ pri_j ```   
---|---  
  
## 一般的积性函数

假如一个 [积性函数](../basic/#积性函数) 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足：对于任意质数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和正整数 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以在关于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的低次多项式时间内计算 𝑓(𝑝𝑘)f(pk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么可以在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内筛出 𝑓(1),𝑓(2),…,𝑓(𝑛)f(1),f(2),…,f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

设合数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的质因子分解是 ∏𝑘𝑖=1𝑝𝛼𝑖𝑖∏i=1kpiαi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝1 <𝑝2 <⋯ <𝑝𝑘p1<p2<⋯<pk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为质数，我们在线性筛中记录 𝑔𝑛 =𝑝𝛼11gn=p1α1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，假如 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被 𝑥 ⋅𝑝x⋅p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 筛掉（𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是质数），那么 𝑔g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足如下递推式：

𝑔𝑛=⎧{ {⎨{ {⎩𝑔𝑥⋅𝑝𝑥mod𝑝=0𝑝otherwisegn={gx⋅pxmodp=0potherwise![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

假如 𝑛 =𝑔𝑛n=gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，说明 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是某个质数的次幂，可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；否则，𝑓(𝑛) =𝑓(𝑛𝑔𝑛) ⋅𝑓(𝑔𝑛)f(n)=f(ngn)⋅f(gn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

**本节部分内容译自博文[Решето Эратосфена](http://e-maxx.ru/algo/eratosthenes_sieve) 与其英文翻译版 [Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/27 12:26:08，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/sieve.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/sieve.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [LJFYC007](https://github.com/LJFYC007), [Xeonacid](https://github.com/Xeonacid), [H-J-Granger](https://github.com/H-J-Granger), [iamtwz](https://github.com/iamtwz), [mgt](mailto:i@margatroid.xyz), [shuzhouliu](https://github.com/shuzhouliu), [CCXXXI](https://github.com/CCXXXI), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [c-forrest](https://github.com/c-forrest), [Early0v0](https://github.com/Early0v0), [HeRaNO](https://github.com/HeRaNO), [MegaOwIer](https://github.com/MegaOwIer), [Peanut-Tang](https://github.com/Peanut-Tang), [YOYO-UIAT](https://github.com/YOYO-UIAT), [AngelKitty](https://github.com/AngelKitty), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Great-designer](https://github.com/Great-designer), [greyqz](https://github.com/greyqz), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [minghu6](https://github.com/minghu6), [Mr-Python-in-China](https://github.com/Mr-Python-in-China), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [TravorLZH](https://github.com/TravorLZH), [weilycoder](https://github.com/weilycoder), [weiyong1024](https://github.com/weiyong1024), [1804040636](https://github.com/1804040636), [383494](https://github.com/383494), [aofall](https://github.com/aofall), [CoelacanthusHex](https://github.com/CoelacanthusHex), [cubeheadsun](https://github.com/cubeheadsun), [frank-xjh](https://github.com/frank-xjh), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [hhc0001](https://github.com/hhc0001), [hqztrue](https://github.com/hqztrue), [ImpleLee](https://github.com/ImpleLee), [inkydragon](https://github.com/inkydragon), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [luojiny1](https://github.com/luojiny1), [Lutra-Fs](https://github.com/Lutra-Fs), [lychees](https://github.com/lychees), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [opsiff](https://github.com/opsiff), [partychicken](https://github.com/partychicken), [PerfectPan](https://github.com/PerfectPan), [Persdre](https://github.com/Persdre), [shawlleyw](https://github.com/shawlleyw), [StableAgOH](https://github.com/StableAgOH), [Steaunk](https://github.com/Steaunk), [SukkaW](https://github.com/SukkaW), [sunruisjtu2020](https://github.com/sunruisjtu2020), [TianKong-y](https://github.com/TianKong-y), [TOMWT-qwq](https://github.com/TOMWT-qwq), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [untitledunrevised](https://github.com/untitledunrevised), [WAAutoMaton](https://github.com/WAAutoMaton), [WineChord](https://github.com/WineChord), [wkywkyQAQ](https://github.com/wkywkyQAQ), [wood3](https://github.com/wood3), [YanWQ-monad](https://github.com/YanWQ-monad), [Yisheng Gong](mailto:yisheng_gong@onmail.com), [zhouyuyang2002](https://github.com/zhouyuyang2002), [ZnPdCo](https://github.com/ZnPdCo), [代建杉](mailto:wood3s@foxmail.com)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
