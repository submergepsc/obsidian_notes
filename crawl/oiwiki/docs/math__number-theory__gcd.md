# 最大公约数 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/gcd/

# 最大公约数

## 定义

最大公约数即为 Greatest Common Divisor，常缩写为 gcd．

一组整数的公约数，是指同时是这组数中每一个数的约数的数．±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是任意一组整数的公约数．

一组整数的最大公约数，是指所有公约数里面最大的一个．

对不全为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将其最大公约数记为 gcd(𝑎,𝑏)gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不引起歧义时可简写为 (𝑎,𝑏)(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对不全为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑎1,…,𝑎𝑛a1,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将其最大公约数记为 gcd(𝑎1,…,𝑎𝑛)gcd(a1,…,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不引起歧义时可简写为 (𝑎1,…,𝑎𝑛)(a1,…,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最大公约数与最小公倍数的性质见 [数论基础](../basic/#最大公约数与最小公倍数)．

那么如何求最大公约数呢？我们先考虑两个数的情况．

### 欧几里得算法

#### 过程

如果我们已知两个数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如何求出二者的最大公约数呢？

不妨设 𝑎 >𝑏a>b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们发现如果 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数，那么 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是二者的最大公约数． 下面讨论不能整除的情况，即 𝑎 =𝑏 ×𝑞 +𝑟a=b×q+r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑟 <𝑏r<b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们通过证明可以得到 gcd(𝑎,𝑏) =gcd(𝑏,𝑎mod𝑏)gcd(a,b)=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，过程如下：

证明

设 𝑎 =𝑏𝑘 +𝑐a=bk+c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然有 𝑐 =𝑎mod𝑏c=amodb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 𝑑 ∣𝑎, 𝑑 ∣𝑏d∣a, d∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑐 =𝑎 −𝑏𝑘,𝑐𝑑 =𝑎𝑑 −𝑏𝑑𝑘c=a−bk,cd=ad−bdk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由右边的式子可知 𝑐𝑑cd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为整数，即 𝑑 ∣𝑐d∣c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以对于 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的公约数，它也会是 𝑏,𝑎mod𝑏b,amodb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的公约数．

反过来也需要证明：

设 𝑑 ∣𝑏, 𝑑 ∣(𝑎mod𝑏)d∣b, d∣(amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们还是可以像之前一样得到以下式子 𝑎mod𝑏𝑑 =𝑎𝑑 −𝑏𝑑𝑘, 𝑎mod𝑏𝑑 +𝑏𝑑𝑘 =𝑎𝑑amodbd=ad−bdk, amodbd+bdk=ad![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因为左边式子显然为整数，所以 𝑎𝑑ad![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也为整数，即 𝑑 ∣𝑎d∣a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑏,𝑎mod𝑏b,amodb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的公约数也是 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的公约数．

既然两式公约数都是相同的，那么最大公约数也会相同．

所以得到式子 gcd(𝑎,𝑏) =gcd(𝑏,𝑎mod𝑏)gcd(a,b)=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

既然得到了 gcd(𝑎,𝑏) =gcd(𝑏,𝑟)gcd(a,b)=gcd(b,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这里两个数的大小是不会增大的，那么我们也就得到了关于两个数的最大公约数的一个递归求法．

#### 实现

C++JavaPython

```text 1 2 3 4 5 6 7 8 ``` |  ```text // Version 1 int gcd ( int a , int b ) { if ( b == 0 ) return a ; return gcd ( b , a % b ); } // Version 2 int gcd ( int a , int b ) { return b == 0 ? a : gcd ( b , a % b ); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text // Version 1 public int gcd ( int a , int b ) { if ( b == 0 ) return a ; return gcd ( b , a % b ); } // Version 2 public int gcd ( int a , int b ) { return b == 0 ? a : gcd ( b , a % b ); } ```   
---|---  
  
```text 1 2 3 4 ``` |  ```text def gcd ( a , b ): if b == 0 : return a return gcd ( b , a % b ) ```   
---|---  
  
递归至 `b == 0`（即上一步的 `a % b == 0`）的情况再返回值即可．

根据上述递归求法，我们也可以写出一个迭代求法：

C++JavaPython

```text 1 2 3 4 5 6 7 8 ``` |  ```text int gcd ( int a , int b ) { while ( b != 0 ) { int tmp = a ; a = b ; b = tmp % b ; } return a ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text public int gcd ( int a , int b ) { while ( b != 0 ) { int tmp = a ; a = b ; b = tmp % b ; } return a ; } ```   
---|---  
  
```text 1 2 3 4 ``` |  ```text def gcd ( a , b ): while b != 0 : a , b = b , a % b return a ```   
---|---  
  
上述算法都可被称作欧几里得算法（Euclidean algorithm）．

另外，对于 C++17，我们可以使用 [`<numeric>`](https://en.cppreference.com/w/cpp/header/numeric) 头中的 [`std::gcd`](https://en.cppreference.com/w/cpp/numeric/gcd) 与 [`std::lcm`](https://en.cppreference.com/w/cpp/numeric/lcm) 来求最大公约数和最小公倍数．

注意

在部分编译器中，C++14 中可以用 `std::__gcd(a,b)` 函数来求最大公约数，但是其仅作为 `std::rotate` 的私有辅助函数．1使用该函数可能会导致预期之外的问题，故一般情况下不推荐使用．

如果两个数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 gcd(𝑎,𝑏) =1gcd(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们称 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质．

#### 性质

欧几里得算法的时间效率如何呢？下面我们证明，在输入为两个长为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制整数时，欧几里得算法的时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（换句话说，在默认 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同阶的情况下，时间复杂度为 𝑂(log⁡max(𝑎,𝑏))O(log⁡max(a,b))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．）

证明

当我们求 gcd(𝑎,𝑏)gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时候，会遇到两种情况：

  * 𝑎 <𝑏a<b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这时候 gcd(𝑎,𝑏) =gcd(𝑏,𝑎)gcd(a,b)=gcd(b,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 𝑎 ≥𝑏a≥b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这时候 gcd(𝑎,𝑏) =gcd(𝑏,𝑎mod𝑏)gcd(a,b)=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而对 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模会让 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至少折半．这意味着这一过程最多发生 𝑂(log⁡𝑎) =𝑂(𝑛)O(log⁡a)=O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．

第一种情况发生后一定会发生第二种情况，因此第一种情况的发生次数一定 **不多于** 第二种情况的发生次数．

从而我们最多递归 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次就可以得出结果．

事实上，假如我们试着用欧几里得算法去求 [斐波那契数列](../../combinatorics/fibonacci/) 相邻两项的最大公约数，会让该算法达到最坏复杂度．

### 更相减损术

大整数取模的时间复杂度较高，而加减法时间复杂度较低．针对大整数，我们可以用加减代替乘除求出最大公约数．

#### 过程

已知两数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，求 gcd(𝑎,𝑏)gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

不妨设 𝑎 ≥𝑏a≥b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 𝑎 =𝑏a=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 gcd(𝑎,𝑏) =𝑎 =𝑏gcd(a,b)=a=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)． 否则，∀𝑑 ∣𝑎,𝑑 ∣𝑏∀d∣a,d∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以证明 𝑑 ∣𝑎 −𝑏d∣a−b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此，𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **所有** 公因数都是 𝑎 −𝑏a−b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的公因数，gcd(𝑎,𝑏) =gcd(𝑎 −𝑏,𝑏)gcd(a,b)=gcd(a−b,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### Stein 算法的优化

如果 𝑎 ≫𝑏a≫b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，更相减损术的 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 复杂度将会达到最坏情况．

考虑一个优化，若 2 ∣𝑎,2 ∣𝑏2∣a,2∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，gcd(𝑎,𝑏) =2gcd(𝑎2,𝑏2)gcd(a,b)=2gcd(a2,b2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

否则，若 2 ∣𝑎2∣a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（2 ∣𝑏2∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同理），因为 2 ∣𝑏2∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况已经讨论过了，所以 2 ∤𝑏2∤b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此 gcd(𝑎,𝑏) =gcd(𝑎2,𝑏)gcd(a,b)=gcd(a2,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

优化后的算法（即 Stein 算法）时间复杂度是 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

若 2 ∣𝑎2∣a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 2 ∣𝑏2∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每次递归至少会将 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之一减半．

否则，2 ∣𝑎 −𝑏2∣a−b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，回到了上一种情况．

算法最多递归 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．

#### 实现

高精度模板见 [高精度计算](../../bignum/)．

高精度运算需实现：减法、大小比较、左移、右移（可用低精乘除代替）、二进制末位 0 的个数（可以通过判断奇偶暴力计算）．

C++

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text Big gcd ( Big a , Big b ) { if ( a == 0 ) return b ; if ( b == 0 ) return a ; // 记录a和b的公因数2出现次数，countr_zero表示二进制末位0的个数 int atimes = countr_zero ( a ); int btimes = countr_zero ( b ); int mintimes = min ( atimes , btimes ); a >>= atimes ; for (;;) { // a和b公因数中的2已经计算过了，后面不可能出现a为偶数的情况 b >>= btimes ; // 确保 a<=b if ( a > b ) swap ( a , b ); b -= a ; if ( b == 0 ) break ; btimes = countr_zero ( b ); } return a << mintimes ; } ```   
---|---  
  
上述代码参考了 [libstdc++](https://github.com/gcc-mirror/gcc/blob/1667962ae755db27965778b8c8c684c6c0c4da21/libstdc%2B%2B-v3/include/std/numeric#L173) 和 [MSVC](https://github.com/microsoft/STL/blob/9aca22477df4eed3222b4974746ee79129eb44e7/stl/inc/numeric#L591) 对 C++17 `std::gcd` 的实现．在 `unsigned int` 和 `unsigned long long` 的数据范围下，如果可以以极快的速度计算 `countr_zero`，则 Stein 算法比欧几里得算法来得快，但反之则可能比欧几里得算法慢．

关于 countr_zero

  1. gcc 有 [内建函数](../../bit/#gcc-内建函数) `__builtin_ctz`（32 位）或 `__builtin_ctzll`（64 位）可替换上述代码的 `countr_zero`；
  2. 从 C++20 开始，头文件 `<bit>` 包含了 [`std::countr_zero`](https://en.cppreference.com/w/cpp/numeric/countr_zero)；
  3. 如果不使用不在标准库的函数，又无法使用 C++20 标准，下面的代码是一种在 Word-RAM with multiplication 模型下经过预处理后 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的实现：

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text constexpr int loghash [ 64 ] = { 0 , 32 , 48 , 56 , 60 , 62 , 63 , 31 , 47 , 55 , 59 , 61 , 30 , 15 , 39 , 51 , 57 , 28 , 46 , 23 , 43 , 53 , 58 , 29 , 14 , 7 , 35 , 49 , 24 , 44 , 54 , 27 , 45 , 22 , 11 , 37 , 50 , 25 , 12 , 38 , 19 , 41 , 52 , 26 , 13 , 6 , 3 , 33 , 16 , 40 , 20 , 42 , 21 , 10 , 5 , 34 , 17 , 8 , 36 , 18 , 9 , 4 , 2 , 1 }; int countr_zero ( unsigned long long x ) { return loghash [( x & \- x ) * 0x9150D32D8EB9EFC0U i64 >> 58 ]; } ```   
---|---  
  
而对于高精度运算，如果实现方法类似 `bitset`，则搭配上述对 `countr_zero` 的实现可以在 `O(n / w)` 的时间复杂度下完成．但如果不便按二进制位拆分，则只能暴力判断最大的 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂因子，时间复杂度取决于实现．比如：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text // 以小端序实现的二进制 Big，要求能枚举每一个元素 int countr_zero ( Big a ) { int ans = 0 ; for ( auto x : a ) { if ( x != 0 ) { ans += 32 ; // 每一位数据类型的位长 } else { return ans \+ countr_zero ( x ); } } return ans ; } // 暴力计算，如需使用建议直接写进 gcd 加快常数 int countr_zero ( Big a ) { int ans = 0 ; while (( a & 1 ) == 0 ) { a >>= 1 ; ++ ans ; } return ans ; } ```   
---|---  
  
更多关于 `gcd` 实现上快慢的讨论可阅读 [Fastest way to compute the greatest common divisor](https://lemire.me/blog/2013/12/26/fastest-way-to-compute-the-greatest-common-divisor/)．

### 多个数的最大公约数

那怎么求多个数的最大公约数呢？显然答案一定是每个数的约数，那么也一定是每相邻两个数的约数．我们采用归纳法，可以证明，每次取出两个数求出答案后再放回去，不会对所需要的答案造成影响．

## 最小公倍数

接下来我们介绍如何求解最小公倍数（Least Common Multiple, LCM）．

### 定义

一组整数的公倍数，是指同时是这组数中每一个数的倍数的数．0 是任意一组整数的公倍数．

一组整数的最小公倍数，是指所有正的公倍数里面，最小的一个数．

对整数 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将其最小公倍数记为 lcm⁡(𝑎,𝑏)lcm⁡(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不引起歧义时可简写为 [𝑎,𝑏][a,b]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对整数 𝑎1,…,𝑎𝑛a1,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，将其最小公倍数记为 lcm⁡(𝑎1,…,𝑎𝑛)lcm⁡(a1,…,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不引起歧义时可简写为 [𝑎1,…,𝑎𝑛][a1,…,an]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 两个数

设 𝑎 =𝑝𝑘𝑎11𝑝𝑘𝑎22⋯𝑝𝑘𝑎𝑠𝑠a=p1ka1p2ka2⋯pskas![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏 =𝑝𝑘𝑏11𝑝𝑘𝑏22⋯𝑝𝑘𝑏𝑠𝑠b=p1kb1p2kb2⋯pskbs![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

我们发现，对于 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，二者的最大公约数等于

𝑝min(𝑘𝑎1,𝑘𝑏1)1𝑝min(𝑘𝑎2,𝑘𝑏2)2⋯𝑝min(𝑘𝑎𝑠,𝑘𝑏𝑠)𝑠p1min(ka1,kb1)p2min(ka2,kb2)⋯psmin(kas,kbs)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

最小公倍数等于

𝑝max(𝑘𝑎1,𝑘𝑏1)1𝑝max(𝑘𝑎2,𝑘𝑏2)2⋯𝑝max(𝑘𝑎𝑠,𝑘𝑏𝑠)𝑠p1max(ka1,kb1)p2max(ka2,kb2)⋯psmax(kas,kbs)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由于 𝑘𝑎 +𝑘𝑏 =max(𝑘𝑎,𝑘𝑏) +min(𝑘𝑎,𝑘𝑏)ka+kb=max(ka,kb)+min(ka,kb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以得到结论是 gcd(𝑎,𝑏) ×lcm⁡(𝑎,𝑏) =𝑎 ×𝑏gcd(a,b)×lcm⁡(a,b)=a×b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

要求两个数的最小公倍数，先求出最大公约数即可．

### 多个数

可以发现，当我们求出两个数的 gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，求最小公倍数是 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度．那么对于多个数，我们其实没有必要求一个共同的最大公约数再去处理，最直接的方法就是，当我们算出两个数的 gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，或许在求多个数的 gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时候，我们将它放入序列对后面的数继续求解，那么，我们转换一下，直接将最小公倍数放入序列即可．

## 扩展欧几里得算法

扩展欧几里得算法（Extended Euclidean algorithm, EXGCD），常用于求 𝑎𝑥 +𝑏𝑦 =gcd(𝑎,𝑏)ax+by=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一组可行解．

### 过程

设

𝑎𝑥1 +𝑏𝑦1 =gcd(𝑎,𝑏)ax1+by1=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝑏𝑥2 +(𝑎mod𝑏)𝑦2 =gcd(𝑏,𝑎mod𝑏)bx2+(amodb)y2=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由欧几里得定理可知：gcd(𝑎,𝑏) =gcd(𝑏,𝑎mod𝑏)gcd(a,b)=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以 𝑎𝑥1 +𝑏𝑦1 =𝑏𝑥2 +(𝑎mod𝑏)𝑦2ax1+by1=bx2+(amodb)y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

又因为 𝑎mod𝑏 =𝑎 −(⌊𝑎𝑏⌋ ×𝑏)amodb=a−(⌊ab⌋×b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以 𝑎𝑥1 +𝑏𝑦1 =𝑏𝑥2 +(𝑎 −(⌊𝑎𝑏⌋ ×𝑏))𝑦2ax1+by1=bx2+(a−(⌊ab⌋×b))y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝑎𝑥1 +𝑏𝑦1 =𝑎𝑦2 +𝑏𝑥2 −⌊𝑎𝑏⌋ ×𝑏𝑦2 =𝑎𝑦2 +𝑏(𝑥2 −⌊𝑎𝑏⌋𝑦2)ax1+by1=ay2+bx2−⌊ab⌋×by2=ay2+b(x2−⌊ab⌋y2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝑎 =𝑎,𝑏 =𝑏a=a,b=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑥1 =𝑦2,𝑦1 =𝑥2 −⌊𝑎𝑏⌋𝑦2x1=y2,y1=x2−⌊ab⌋y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将 𝑥2,𝑦2x2,y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不断代入递归求解直至 gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（最大公约数，下同）为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 递归 𝑥 =1,𝑦 =0x=1,y=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 回去求解．

### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text int Exgcd ( int a , int b , int & x , int & y ) { if ( ! b ) { x = 1 ; y = 0 ; return a ; } int d = Exgcd ( b , a % b , x , y ); int t = x ; x = y ; y = t \- ( a / b ) * y ; return d ; } ```   
---|---  
  
```text 1 2 3 4 5 ``` |  ```text def Exgcd ( a , b ): if b == 0 : return a , 1 , 0 d , x , y = Exgcd ( b , a % b ) return d , y , x \- ( a // b ) * y ```   
---|---  
  
函数返回的值为 gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在这个过程中计算 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

### 值域分析

𝑎𝑥 +𝑏𝑦 =gcd(𝑎,𝑏)ax+by=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解有无数个，显然其中有的解会爆 long long．  
万幸的是，若 𝑏 ≠0b≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，扩展欧几里得算法求出的可行解必有 |𝑥| ≤𝑏,|𝑦| ≤𝑎|x|≤b,|y|≤a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．  
下面给出这一性质的证明．

证明

  * gcd(𝑎,𝑏) =𝑏gcd(a,b)=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑎mod𝑏 =0amodb=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，必在下一层终止递归．  
得到 𝑥1 =0,𝑦1 =1x1=0,y1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然 𝑎,𝑏 ≥1 ≥|𝑥1|,|𝑦1|a,b≥1≥|x1|,|y1|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * gcd(𝑎,𝑏) ≠𝑏gcd(a,b)≠b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，设 |𝑥2| ≤(𝑎mod𝑏),|𝑦2| ≤𝑏|x2|≤(amodb),|y2|≤b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．  
因为 𝑥1 =𝑦2,𝑦1 =𝑥2 −⌊𝑎𝑏⌋𝑦2x1=y2,y1=x2−⌊ab⌋y2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)   
所以 |𝑥1| =|𝑦2| ≤𝑏,|𝑦1| ≤|𝑥2| +|⌊𝑎𝑏⌋𝑦2| ≤(𝑎mod𝑏) +⌊𝑎𝑏⌋|𝑦2||x1|=|y2|≤b,|y1|≤|x2|+|⌊ab⌋y2|≤(amodb)+⌊ab⌋|y2|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
≤𝑎 −⌊𝑎𝑏⌋𝑏 +⌊𝑎𝑏⌋|𝑦2| ≤𝑎 −⌊𝑎𝑏⌋(𝑏 −|𝑦2|)≤a−⌊ab⌋b+⌊ab⌋|y2|≤a−⌊ab⌋(b−|y2|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)   
𝑎mod𝑏 =𝑎 −⌊𝑎𝑏⌋𝑏 ≤𝑎 −⌊𝑎𝑏⌋(𝑏 −|𝑦2|) ≤𝑎amodb=a−⌊ab⌋b≤a−⌊ab⌋(b−|y2|)≤a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)   
因此 |𝑥1| ≤𝑏,|𝑦1| ≤𝑎|x1|≤b,|y1|≤a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立．

### 迭代法编写扩展欧几里得算法

首先，当 𝑥 =1x=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑦 =0y=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑥1 =0x1=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑦1 =1y1=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，显然有：

{𝑎𝑥+𝑏𝑦=𝑎𝑎𝑥1+𝑏𝑦1=𝑏{ax+by=aax1+by1=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

成立．

已知 𝑎mod𝑏 =𝑎 −(⌊𝑎𝑏⌋ ×𝑏)amodb=a−(⌊ab⌋×b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，下面令 𝑞 =⌊𝑎𝑏⌋q=⌊ab⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．参考迭代法求 gcd，每一轮的迭代过程可以表示为：

(𝑎,𝑏)→(𝑏,𝑎−𝑞𝑏)(a,b)→(b,a−qb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

将迭代过程中的 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替换为 𝑎𝑥 +𝑏𝑦 =𝑎ax+by=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 替换为 𝑎𝑥1 +𝑏𝑦1 =𝑏ax1+by1=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，可以得到：

{𝑎𝑥+𝑏𝑦=𝑎𝑎𝑥1+𝑏𝑦1=𝑏→{𝑎𝑥1+𝑏𝑦1=𝑏𝑎(𝑥−𝑞𝑥1)+𝑏(𝑦−𝑞𝑦1)=𝑎−𝑞𝑏{ax+by=aax1+by1=b→{ax1+by1=ba(x−qx1)+b(y−qy1)=a−qb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

据此就可以得到迭代法求 exgcd．

因为迭代的方法避免了递归，所以代码运行速度将比递归代码快一点．

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text int gcd ( int a , int b , int & x , int & y ) { x = 1 , y = 0 ; int x1 = 0 , y1 = 1 , a1 = a , b1 = b ; while ( b1 ) { int q = a1 / b1 ; tie ( x , x1 ) = make_tuple ( x1 , x \- q * x1 ); tie ( y , y1 ) = make_tuple ( y1 , y \- q * y1 ); tie ( a1 , b1 ) = make_tuple ( b1 , a1 \- q * b1 ); } return a1 ; } ```   
---|---  
  
如果你仔细观察 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏1b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，你会发现，他们在迭代版本的欧几里德算法中取值完全相同，并且以下公式无论何时（在 while 循环之前和每次迭代结束时）都是成立的：𝑥 ⋅𝑎 +𝑦 ⋅𝑏 =𝑎1x⋅a+y⋅b=a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑥1 ⋅𝑎 +𝑦1 ⋅𝑏 =𝑏1x1⋅a+y1⋅b=b1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因此，该算法肯定能正确计算出 gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后我们知道 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是要求的 gcdgcd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 𝑥 ⋅𝑎 +𝑦 ⋅𝑏 =𝑔x⋅a+y⋅b=g![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 矩阵的解释

对于正整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一次辗转相除即 gcd(𝑎,𝑏) =gcd(𝑏,𝑎mod𝑏)gcd(a,b)=gcd(b,amodb)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使用矩阵表示如

[𝑏𝑎mod𝑏]=[011−⌊𝑎/𝑏⌋][𝑎𝑏][bamodb]=[011−⌊a/b⌋][ab]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中向下取整符号 ⌊𝑐⌋⌊c⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示不大于 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大整数．我们定义变换 [𝑎𝑏] ↦[011−⌊𝑎/𝑏⌋][𝑎𝑏][ab]↦[011−⌊a/b⌋][ab]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

易发现欧几里得算法即不停应用该变换，有

[gcd(𝑎,𝑏)0]=(⋯[011−⌊𝑎/𝑏⌋][1001])[𝑎𝑏][gcd(a,b)0]=(⋯[011−⌊a/b⌋][1001])[ab]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令

[𝑥1𝑥2𝑥3𝑥4]=⋯[011−⌊𝑎/𝑏⌋][1001][x1x2x3x4]=⋯[011−⌊a/b⌋][1001]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

那么

[gcd(𝑎,𝑏)0]=[𝑥1𝑥2𝑥3𝑥4][𝑎𝑏][gcd(a,b)0]=[x1x2x3x4][ab]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

满足 𝑎 ⋅𝑥1 +𝑏 ⋅𝑥2 =gcd(𝑎,𝑏)a⋅x1+b⋅x2=gcd(a,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即扩展欧几里得算法，注意在最后乘了一个单位矩阵不会影响结果，提示我们可以在开始时维护一个 2 ×22×2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的单位矩阵编写更简洁的迭代方法如

```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text int exgcd ( int a , int b , int & x , int & y ) { int x1 = 1 , x2 = 0 , x3 = 0 , x4 = 1 ; while ( b != 0 ) { int c = a / b ; std :: tie ( x1 , x2 , x3 , x4 , a , b ) = std :: make_tuple ( x3 , x4 , x1 \- x3 * c , x2 \- x4 * c , b , a \- b * c ); } x = x1 , y = x2 ; return a ; } ```   
---|---  
  
这种表述相较于递归更简单．

## 应用

  * [10104 - Euclid Problem](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1045)
  * [GYM - (J) once upon a time](http://codeforces.com/gym/100963)
  * [UVa - 12775 - Gift Dilemma](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4628)

## 参考资料与链接

* * *

  1. [libstdc++: std Namespace Reference](https://gcc.gnu.org/onlinedocs/libstdc++/libstdc++-html-USERS-4.4/a00978.html#a2686a128df5a576cb53a1ed5f674607) ↩

* * *

>  __本页面最近更新： 2026/1/27 12:26:08，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/gcd.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/gcd.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [Enter-tainer](https://github.com/Enter-tainer), [hsfzLZH1](https://github.com/hsfzLZH1), [c-forrest](https://github.com/c-forrest), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [MegaOwIer](https://github.com/MegaOwIer), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [383494](https://github.com/383494), [i-yyi](https://github.com/i-yyi), [LuoshuiTianyi](https://github.com/LuoshuiTianyi), [mgt](mailto:i@margatroid.xyz), [untitledunrevised](https://github.com/untitledunrevised), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [Backl1ght](https://github.com/Backl1ght), [buggg-hfc](https://github.com/buggg-hfc), [FinParker](https://github.com/FinParker), [gi-b716](https://github.com/gi-b716), [Great-designer](https://github.com/Great-designer), [hhc0001](https://github.com/hhc0001), [hly1204](https://github.com/hly1204), [hsiviter](https://github.com/hsiviter), [huaruoji](mailto:43847915+huaruoji@users.noreply.github.com), [Koishilll](https://github.com/Koishilll), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [PwzXxm](https://github.com/PwzXxm), [Qubik65536](https://github.com/Qubik65536), [shawlleyw](https://github.com/shawlleyw), [tder6](https://github.com/tder6), [TOMWT-qwq](https://github.com/TOMWT-qwq), [VaneHsiung](https://github.com/VaneHsiung), [warzone-oier](https://github.com/warzone-oier), [WillHouMoe](https://github.com/WillHouMoe)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
