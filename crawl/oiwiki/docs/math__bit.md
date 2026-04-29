# 位操作 - OI Wiki

- Source: https://oi-wiki.org/math/bit/

# 位操作

位操作指的是对整数二进制表示的一元和二元操作，分为 **位运算** 和 **移位** 两类．位操作是 CPU 中最基础的一类运算，其速度往往是相当快的．

## 整数与位序列

另请参阅：[整数类型](../../lang/var/#整数类型)、[补数法](../numeral-sys/base/#补数法)

我们将只由 `0` 或 `1` 构成的长度固定的序列称为位序列．最左边的位称为最高位，最右边的位称为最低位．

计算机中用位序列表示一定范围内的整数．长度为 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位序列只有 2𝑁2N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种，所以只能和 2𝑁2N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数建立一一对应关系．这种一一对应关系可以分为两类：**有符号** 和 **无符号** ．有符号指的是对应的整数有负数，无符号指的是对应的整数全部为非负数．

  * 对于无符号的对应关系，我们可以直接将整数的二进制表示作为位序列，长度不足就在高位补 `0`．

在无符号的对应关系下，长度为 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位序列可以表示 [0,2𝑁 −1][0,2N−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的整数．

  * 对于有符号的对应关系，我们有两种表示规则：**反码** （ones' complement）和 **补码** （two's complement）．

对于非负整数来说，其表示规则和无符号的规则一致；对于负整数来说，我们将其相反数对应的位序列 **按位取反** （即将 `0` 变为 `1`，将 `1` 变为 `0`）后的结果称为反码，将反码按无符号的对应关系转为整数，然后加一，最后按无符号的对应关系转为位序列，超出原位序列长度的部分舍弃，得到的新序列称为补码．

在反码的对应关系下，长度为 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位序列可以表示 [ −2𝑁−1 +1,2𝑁−1 −1][−2N−1+1,2N−1−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的整数．

在补码的对应关系下，长度为 𝑁N![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位序列可以表示 [ −2𝑁−1,2𝑁−1 −1][−2N−1,2N−1−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 内的整数．

以 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的位序列为例：

位序列| 无符号整数| 有符号整数（反码）| 有符号整数（补码）  
---|---|---|---  
`000`| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`001`| 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`010`| 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`011`| 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`100`| 44![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −3−3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −4−4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`101`| 55![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −2−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −3−3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`110`| 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −2−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
`111`| 77![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −0−0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
  
可以看到反码的最大问题是会出现 −0−0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这个实际上不存在的「负数」，所以一般情况下我们只用补码．由于表示有符号整数时，其正负号仅由位序列的最高位决定，所以我们将这一位称为 **符号位** ．

将位序列转为整数也是容易做到的：对非负数来说不需要特别操作，对反码来说取反即可得到对应的相反数，对补码来说取反加一即可得到对应的相反数．

## 位运算

位运算指的是对位序列逐位应用某些 [布尔函数](../boolean-algebra/#布尔函数) 的运算．形式化地说，对布尔函数 𝑓 :𝐁𝑘 →𝐁f:Bk→B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，位运算即为形如

𝐹:(𝐁𝑚)𝑘→𝐁𝑚((𝑝1,1,…,𝑝𝑚,1),…,(𝑝1,𝑘,…,𝑝𝑚,𝑘))↦(𝑓(𝑝1,1,…,𝑝1,𝑘),…,𝑓(𝑝𝑚,1,…,𝑝𝑚,𝑘))F:(Bm)k→Bm((p1,1,…,pm,1),…,(p1,k,…,pm,k))↦(f(p1,1,…,p1,k),…,f(pm,1,…,pm,k))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的函数，其中 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为位序列的长度．同样的，我们一般只研究一元和二元的位运算．如无特殊说明，下文的位运算仅限于一元和二元的情况．

一般来说，我们把 **按位取反** 、**按位与** 、**按位或** 、**按位异或** 视作基本的位运算，其余的位运算均可以通过这些运算组合得到．

位运算| 数学符号表示| 对应的布尔函数| C++ 运算符| 解释  
---|---|---|---|---  
按位取反| NOTNOT![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ¬¬![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `~`| 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
按位与| ANDAND![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ∧∧![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `&`| 只有两个对应位都为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时才为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
按位或| OROR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ∨∨![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `|`| 只要两个对应位中有一个 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时就为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
按位异或| ⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、XORXOR![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| ⊕⊕![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)| `^`| 只有两个对应位不同时才为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)  
Warning

注意区分位运算与布尔函数．

例如：

  * NOT⁡01010111 =10101000NOT⁡01010111=10101000![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 01010011AND⁡00110010 =0001001001010011AND⁡00110010=00010010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 01010011OR⁡00110010 =0111001101010011OR⁡00110010=01110011![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 01010011XOR⁡00110010 =0110000101010011XOR⁡00110010=01100001![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由于上述四种位运算在运算时，各个位的运算独立，所以这四种位运算能直接继承其对应布尔函数的性质．

为方便起见，在位序列长度已知时，我们也可以直接对整数做位运算，例如：

NOT⁡5=−6,NOT⁡(−5)=4,5AND⁡6=4,5OR⁡6=7,5XOR⁡6=3.NOT⁡5=−6,NOT⁡(−5)=4,5AND⁡6=4,5OR⁡6=7,5XOR⁡6=3.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

假设 𝑥,𝑦 ≥0x,y≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们也可以将位运算用求和的方式表示：

NOT⁡𝑥=⌊log2⁡𝑥⌋∑𝑛=02𝑛((⌊𝑥2𝑛⌋mod2+1)mod2)=⌊log2⁡𝑥⌋∑𝑛=0(2⌊log2⁡𝑥⌋+1−1−𝑥)𝑥AND⁡𝑦=⌊log2⁡max{𝑥,𝑦}⌋∑𝑛=02𝑛(⌊𝑥2𝑛⌋mod2)(⌊𝑦2𝑛⌋mod2)𝑥OR⁡𝑦=⌊log2⁡max{𝑥,𝑦}⌋∑𝑛=02𝑛((⌊𝑥2𝑛⌋mod2)+(⌊𝑦2𝑛⌋mod2)−(⌊𝑥2𝑛⌋mod2)(⌊𝑦2𝑛⌋mod2))𝑥XOR⁡𝑦=⌊log2⁡max{𝑥,𝑦}⌋∑𝑛=02𝑛(((⌊𝑥2𝑛⌋mod2)+(⌊𝑦2𝑛⌋mod2))mod2)=⌊log2⁡max{𝑥,𝑦}⌋∑𝑛=02𝑛((⌊𝑥2𝑛⌋+⌊𝑦2𝑛⌋)mod2)NOT⁡x=∑n=0⌊log2⁡x⌋2n((⌊x2n⌋mod2+1)mod2)=∑n=0⌊log2⁡x⌋(2⌊log2⁡x⌋+1−1−x)xAND⁡y=∑n=0⌊log2⁡max{x,y}⌋2n(⌊x2n⌋mod2)(⌊y2n⌋mod2)xOR⁡y=∑n=0⌊log2⁡max{x,y}⌋2n((⌊x2n⌋mod2)+(⌊y2n⌋mod2)−(⌊x2n⌋mod2)(⌊y2n⌋mod2))xXOR⁡y=∑n=0⌊log2⁡max{x,y}⌋2n(((⌊x2n⌋mod2)+(⌊y2n⌋mod2))mod2)=∑n=0⌊log2⁡max{x,y}⌋2n((⌊x2n⌋+⌊y2n⌋)mod2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

在不引起歧义的情况下，下文中省略「按位」．

## 移位

另请参阅：[C++ 位操作符](../../lang/op/#位操作符)．

移位为一类将位序列「按位向左或向右移动」的二元运算，第一个参数为位序列，第二个参数一般为非负整数．向左移动称为 **左移** ，向右移动称为 **右移** ．根据对移动后的空位填充方式，可将移位操作分为 **算术移位** 、**逻辑移位** 、**循环移位** ．其中

  * 逻辑移位用 0 填充空位，
  * 算术右移用符号位填充空位，算术左移和逻辑左移相同，
  * 循环移位用溢出位填充空位．

例如对 88![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的位序列 `10 01 01 10`：

操作| 结果  
---|---  
算术左移 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位| `01 01 10 00`  
算术右移 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位| `11 10 01 01`  
逻辑左移 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位| `01 01 10 00`  
逻辑右移 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位| `00 10 01 01`  
循环左移 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位| `01 01 10 10`  
循环右移 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位| `10 10 01 01`  
  
在 C++ 中，我们用 `a << b` 表示左移，`a >> b` 表示右移，具体采用何种移位规则参见 [C++ 位操作符](../../lang/op/#位操作符)．

我们可以用如下代码实现循环移位：

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text // From <https://stackoverflow.com/a/776523/224132> #include <climits> #include <cstdint> uint32_t rotl32 ( uint32_t value , unsigned int count ) { const unsigned int mask = CHAR_BIT * sizeof ( value ) \- 1 ; count &= mask ; return ( value << count ) | ( value >> ( \- count & mask )); } uint32_t rotr32 ( uint32_t value , unsigned int count ) { const unsigned int mask = CHAR_BIT * sizeof ( value ) \- 1 ; count &= mask ; return ( value >> count ) | ( value << ( \- count & mask )); } ```   
---|---  
  
## 位操作的应用

位操作一般有三种作用：

  1. 高效地进行某些运算，代替其它低效的方式．参见 [编译优化 #强度削减](../../lang/optimizations/#强度削减-strength-reduction)．
  2. [表示集合](../binary-set/)（常用于 [状压 DP](../../dp/state/)）．
  3. 题目本来就要求进行位操作．

需要注意的是，用位操作代替其它运算方式在很多时候并不能带来太大的优化，反而会使代码变得复杂，使用时需要斟酌．

### 有关 2 的幂的应用

由于位操作针对的是二进制表示，因此可以推广出许多与 2 的整数次幂有关的应用．

将一个数乘（除）2 的非负整数次幂：

C++Python

```text 1 2 3 4 5 6 7 ``` |  ```text int mulPowerOfTwo ( int n , int m ) { // 计算 n*(2^m) return n << m ; } int divPowerOfTwo ( int n , int m ) { // 计算 n/(2^m) return n >> m ; } ```   
---|---  
  
```text 1 2 3 4 5 6 ``` |  ```text def mulPowerOfTwo ( n , m ): # 计算 n*(2^m) return n << m def divPowerOfTwo ( n , m ): # 计算 n/(2^m) return n >> m ```   
---|---  
  
Warning

我们平常写的除法是向 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取整，而这里的右移是向下取整（注意这里的区别），即当数大于等于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时两种方法等价，当数小于 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时会有区别，如：`-1 / 2` 的值为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而 `-1 >> 1` 的值为 −1−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 取绝对值

在某些机器上，效率比 `n > 0 ? n : -n` 高．

C++Python

```text 1 2 3 4 5 6 7 ``` |  ```text int Abs ( int n ) { return ( n ^ ( n >> 31 )) \- ( n >> 31 ); /* n>>31 取得 n 的符号，若 n 为正数，n>>31 等于 0，若 n 为负数，n>>31 等于 -1 若 n 为正数 n^0=n, 数不变，若 n 为负数有 n^(-1) 需要计算 n 和 -1 的补码，然后进行异或运算， 结果 n 变号并且为 n 的绝对值减 1，再减去 -1 就是绝对值 */ } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text def Abs ( n ): return ( n ^ ( n >> 31 )) \- ( n >> 31 ) """ n>>31 取得 n 的符号，若 n 为正数，n>>31 等于 0，若 n 为负数，n>>31 等于 -1 若 n 为正数 n^0=n, 数不变，若 n 为负数有 n^(-1) 需要计算 n 和 -1 的补码，然后进行异或运算， 结果 n 变号并且为 n 的绝对值减 1，再减去 -1 就是绝对值 """ ```   
---|---  
  
### 取两个数的最大/最小值

在某些机器上，效率比 `a > b ? a : b` 高．

C++Python

```text 1 2 3 4 ``` |  ```text // 如果 a >= b, (a - b) >> 31 为 0，否则为 -1 int max ( int a , int b ) { return ( b & (( a \- b ) >> 31 )) | ( a & ( ~ ( a \- b ) >> 31 )); } int min ( int a , int b ) { return ( a & (( a \- b ) >> 31 )) | ( b & ( ~ ( a \- b ) >> 31 )); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text # 如果 a >= b, (a - b) >> 31 为 0，否则为 -1 def max ( a , b ): return b & (( a \- b ) >> 31 ) | a & ( ~ ( a \- b ) >> 31 ) def min ( a , b ): return a & (( a \- b ) >> 31 ) | b & ( ~ ( a \- b ) >> 31 ) ```   
---|---  
  
### 判断两非零数符号是否相同

C++Python

```text 1 2 3 ``` |  ```text bool isSameSign ( int x , int y ) { // 有 0 的情况例外 return ( x ^ y ) >= 0 ; } ```   
---|---  
  
```text 1 2 3 ``` |  ```text # 有 0 的情况例外 def isSameSign ( x , y ): return ( x ^ y ) >= 0 ```   
---|---  
  
### 交换两个数

该方法具有局限性

这种方式只能用来交换两个整数，使用范围有限．

对于一般情况下的交换操作，推荐直接调用 `algorithm` 库中的 `std::swap` 函数．

```text 1 ``` |  ```text void swap ( int & a , int & b ) { a ^= b ^= a ^= b ; } ```   
---|---  
  
### 操作一个数的二进制位

获取一个数二进制的某一位：

C++Python

```text 1 2 ``` |  ```text // 获取 a 的第 b 位，最低位编号为 0 int getBit ( int a , int b ) { return ( a >> b ) & 1 ; } ```   
---|---  
  
```text 1 2 3 ``` |  ```text # 获取 a 的第 b 位，最低位编号为 0 def getBit ( a , b ): return ( a >> b ) & 1 ```   
---|---  
  
将一个数二进制的某一位设置为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

C++Python

```text 1 2 ``` |  ```text // 将 a 的第 b 位设置为 0 ，最低位编号为 0 int unsetBit ( int a , int b ) { return a & ~ ( 1 << b ); } ```   
---|---  
  
```text 1 2 3 ``` |  ```text # 将 a 的第 b 位设置为 0 ，最低位编号为 0 def unsetBit ( a , b ): return a & ~ ( 1 << b ) ```   
---|---  
  
将一个数二进制的某一位设置为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

C++Python

```text 1 2 ``` |  ```text // 将 a 的第 b 位设置为 1 ，最低位编号为 0 int setBit ( int a , int b ) { return a | ( 1 << b ); } ```   
---|---  
  
```text 1 2 3 ``` |  ```text # 将 a 的第 b 位设置为 1 ，最低位编号为 0 def setBit ( a , b ): return a | ( 1 << b ) ```   
---|---  
  
将一个数二进制的某一位取反：

C++Python

```text 1 2 ``` |  ```text // 将 a 的第 b 位取反 ，最低位编号为 0 int flapBit ( int a , int b ) { return a ^ ( 1 << b ); } ```   
---|---  
  
```text 1 2 3 ``` |  ```text # 将 a 的第 b 位取反 ，最低位编号为 0 def flapBit ( a , b ): return a ^ ( 1 << b ) ```   
---|---  
  
这些操作相当于将一个 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位整型变量当作一个长度为 3232![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的布尔数组．

## 汉明权重

汉明权重是一串符号中不同于（定义在其所使用的字符集上的）零符号（zero-symbol）的个数．对于一个二进制数，它的汉明权重就等于它 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数（即 `popcount`）．

求一个数的汉明权重可以循环求解：我们不断地去掉这个数在二进制下的最后一位（即右移 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位），维护一个答案变量，在除的过程中根据最低位是否为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 更新答案．

代码如下：

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // 求 x 的汉明权重 int popcount ( int x ) { int cnt = 0 ; while ( x ) { cnt += x & 1 ; x >>= 1 ; } return cnt ; } ```   
---|---  
  
求一个数的汉明权重还可以使用 `lowbit` 操作：我们将这个数不断地减去它的 `lowbit`1，直到这个数变为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

代码如下：

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text // 求 x 的汉明权重 int popcount ( int x ) { int cnt = 0 ; while ( x ) { cnt ++ ; x -= x & \- x ; } return cnt ; } ```   
---|---  
  
### 构造汉明权重递增的排列

在 [状压 DP](../../dp/state/) 中，按照 popcount 递增的顺序枚举有时可以避免重复枚举状态．这是构造汉明权重递增的排列的一大作用．

下面我们来具体探究如何在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内构造汉明权重递增的排列．

我们知道，一个汉明权重为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小的整数为 2𝑛 −12n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．只要可以在常数时间构造出一个整数汉明权重相等的后继，我们就可以通过枚举汉明权重，从 2𝑛 −12n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始不断寻找下一个数的方式，在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内构造出 0 ∼𝑛0∼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的符合要求的排列．

而找出一个数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 汉明权重相等的后继有这样的思路，以 (10110)2(10110)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为例：

  * 把 (10110)2(10110)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最右边的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向左移动，如果不能移动，移动它左边的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以此类推，得到 (11010)2(11010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 把得到的 (11010)2(11010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最后移动的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 原先的位置一直到最低位的所有 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都移到最右边．这里最后移动的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 原来在第三位，所以最后三位 010010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 要变成 001001![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得到 (11001)2(11001)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这个过程可以用位操作优化：

```text 1 2 ``` |  ```text int t = x \+ ( x & \- x ); x = t | (((( t & \- t ) / ( x & \- x )) >> 1 ) \- 1 ); ```   
---|---  
  
  * 第一个步骤中，我们把数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 加上它的 `lowbit`，在二进制表示下，就相当于把 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最右边的连续一段 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 换成它左边的一个 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如刚才提到的二进制数 (10110)2(10110)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它在加上它的 `lowbit` 后是 (11000)2(11000)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这其实得到了我们答案的前半部分．
  * 我们接下来要把答案后面的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 补齐，𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 `lowbit` 是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最右边连续一段 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最左边的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 移动后的位置，而 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 `lowbit` 则是 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最右边连续一段 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最右边的位置．还是以 (10110)2(10110)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为例，𝑡 =(11000)2t=(11000)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，lowbit⁡(𝑡) =(01000)2lowbit⁡(t)=(01000)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，lowbit⁡(𝑥) =(00010)2lowbit⁡(x)=(00010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 接下来的除法操作是这种位操作中最难理解的部分，但也是最关键的部分．我们设 **原数** 最右边连续一段 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 最高位的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在第 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位上（位数从 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始），最低位的 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在第 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 `lowbit` 等于 `1 << (r+1)`，𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 `lowbit` 等于 `1 << l`，`(((t&-t)/(x&-x))>>1)` 得到的，就是 `(1<<(r+1))/(1<<l)/2 = (1<<r)/(1<<l) = 1<<(r-l)`，在二进制表示下就是 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后面跟上 𝑟 −𝑙r−l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个零，零的个数正好等于连续 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数减去 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．举我们刚才的数为例，lowbit(t)/2lowbit(x) =(00100)2(00010)2 =(00010)2lowbit(t)/2lowbit(x)=(00100)2(00010)2=(00010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．把这个数减去 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 得到的就是我们要补全的低位，或上原来的数就可以得到答案．

所以枚举 0 ∼𝑛0∼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 按汉明权重递增的排列的完整代码为：

```text 1 2 3 4 5 6 ``` |  ```text for ( int i = 0 ; ( 1 << i ) \- 1 <= n ; i ++ ) { for ( int x = ( 1 << i ) \- 1 , t ; x <= n ; t = x \+ ( x & \- x ), x = x ? ( t | (((( t & \- t ) / ( x & \- x )) >> 1 ) \- 1 )) : ( n \+ 1 )) { // 写下需要完成的操作 } } ```   
---|---  
  
其中要注意 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特判，因为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 没有相同汉明权重的后继．

## C++ 中的相关类与函数

### GCC 内建函数

GCC 中还有一些用于位操作的内建函数：

  * `int __builtin_ffs(int x)`：返回 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制末尾最后一个 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的位置，位置的编号从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始（最低位编号为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．当 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时返回 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * `int __builtin_clz(unsigned int x)`：返回 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制的前导 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数．当 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，结果未定义．
  * `int __builtin_ctz(unsigned int x)`：返回 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制末尾连续 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数．当 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，结果未定义．
  * `int __builtin_clrsb(int x)`：当 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的符号位为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时返回 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制的前导 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数减一，否则返回 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制的前导 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数减一．
  * `int __builtin_popcount(unsigned int x)`：返回 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制中 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数．
  * `int __builtin_parity(unsigned int x)`：判断 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制中 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数的奇偶性．

这些函数都可以在函数名末尾添加 `l` 或 `ll`（如 `__builtin_popcountll`）来使参数类型变为 (`unsigned`)`long` 或 (`unsigned`)`long long`（返回值仍然是 `int` 类型）． 例如，我们有时候希望求出一个数以二为底的对数，如果不考虑 `0` 的特殊情况，就相当于这个数二进制的位数 `-1`，而一个 `N` 位整数 `n` 的二进制表示的位数可以使用 `N - __builtin_clz(n)` 表示，因此 `N - 1 - __builtin_clz(n)` 就可以求出 `n` 以二为底的对数．

由于这些函数是内建函数，经过了编译器的高度优化，运行速度十分快（有些甚至只需要一条指令）．

### 更多位数

如果需要操作的位序列非常长，可以使用 [`std::bitset`](../../lang/csl/bitset/)．

## 题目推荐

  * [Luogu P1225 黑白棋游戏](https://www.luogu.com.cn/problem/P1225)

## 参考资料与注释

  1. [位运算技巧](https://graphics.stanford.edu/~seander/bithacks.html)
  2. [Bit Operation Builtins (Using the GNU Compiler Collection (GCC))](https://gcc.gnu.org/onlinedocs/gcc/Bit-Operation-Builtins.html)
  3. [Bitwise operation - Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

* * *

  1. 一个数二进制表示从低往高的第一个 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连同后面的零，如 (1010)2(1010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 `lowbit` 是 (0010)2(0010)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，详见 [树状数组](../../ds/fenwick/)． ↩

* * *

>  __本页面最近更新： 2026/1/30 14:50:40，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/bit.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/bit.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [greyqz](https://github.com/greyqz), [Link-cute](https://github.com/Link-cute), [cjsoft](https://github.com/cjsoft), [Marcythm](https://github.com/Marcythm), [Enter-tainer](https://github.com/Enter-tainer), [ksyx](https://github.com/ksyx), [lihaoyu1234](https://github.com/lihaoyu1234), [akakw1](https://github.com/akakw1), [Anguei](https://github.com/Anguei), [aofall](https://github.com/aofall), [billchenchina](https://github.com/billchenchina), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [Dian-Jiao](https://github.com/Dian-Jiao), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [flylai](https://github.com/flylai), [Great-designer](https://github.com/Great-designer), [H-J-Granger](https://github.com/H-J-Granger), [Henry-ZHR](https://github.com/Henry-ZHR), [hhc0001](https://github.com/hhc0001), [hjsjhn](https://github.com/hjsjhn), [iamtwz](https://github.com/iamtwz), [Konano](https://github.com/Konano), [Menci](https://github.com/Menci), [MingqiHuang](mailto:hmq011212@163.com), [orzAtalod](https://github.com/orzAtalod), [PlanariaIce](https://github.com/PlanariaIce), [sakuragi1111](https://github.com/sakuragi1111), [sbofgayschool](https://github.com/sbofgayschool), [shawlleyw](https://github.com/shawlleyw), [Shen-Linwood](https://github.com/Shen-Linwood), [skippre](https://github.com/skippre), [sshwy](https://github.com/sshwy), [stevenlele](https://github.com/stevenlele), [TOMWT-qwq](https://github.com/TOMWT-qwq), [Voileexperiments](https://github.com/Voileexperiments), [Xeonacid](https://github.com/Xeonacid), [xinchengo](https://github.com/xinchengo), [ylxmf2005](https://github.com/ylxmf2005), [zhilu-tang](https://github.com/zhilu-tang), [ZnPdCo](https://github.com/ZnPdCo), [zryi2003](https://github.com/zryi2003)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
