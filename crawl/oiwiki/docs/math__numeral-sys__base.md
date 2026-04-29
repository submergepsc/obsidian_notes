# 进位制 - OI Wiki

- Source: https://oi-wiki.org/math/numeral-sys/base/

# 进位制

**进位制** ，又称 **进位系统** （carry system）、**进制系统** 、**位置记法** （positional notation）、**位值记数法** （place-value notation）、**位置数值系统** （positional numeral system），是一种能用有限种符号表示所有自然数的数字系统．一种进位制可以使用的符号数目称为 **基数** （radix）或 **底数** （base），基数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的进位制称为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制（𝑛 >1n>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），例如我们最常用的十进制，通常只使用 `0, 1, 2, 3, 4, 5, 6, 7, 8, 9` 这十个符号来记数．进位指的是「当一个数字的某一位达到基数时，将其置为 0 并使高一位的数加一」的操作．

一般地，我们常将一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制的数记作 (𝑎𝑘⋯𝑎1𝑎0)𝑛(ak⋯a1a0)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、(𝑎𝑘⋯𝑎1𝑎0)(𝑛)(ak⋯a1a0)(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝑎𝑘⋯𝑎1𝑎0(𝑛)ak⋯a1a0(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝑎𝑘⋯𝑎1𝑎0𝑛ak⋯a1a0n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等．若基数隐含在上下文中我们也可以省略下标．注意此处的 𝑎𝑘⋯𝑎1𝑎0ak⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 并不是 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数的乘积，而是一串序列．

对于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制数 𝑎𝑛⋯𝑎1𝑎0an⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其表示的值为 𝑎𝑛𝑘𝑛 +⋯ +𝑎1𝑘1 +𝑎0𝑘0 =∑𝑛𝑖=0𝑎𝑖𝑘𝑖ankn+⋯+a1k1+a0k0=∑i=0naiki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；对一个数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设其 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的表示为 𝑎𝑛⋯𝑎1𝑎0an⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有：

𝑎0=𝑚−𝑞0𝑘,𝑞0=𝑓(𝑚/𝑘),𝑎1=𝑞0−𝑞1𝑘,𝑞1=𝑓(𝑞0/𝑘),⋮⋮𝑎𝑛=𝑞𝑛−1−𝑞𝑛𝑘,𝑞𝑛=𝑓(𝑞𝑛−1/𝑘)=0,a0=m−q0k,q0=f(m/k),a1=q0−q1k,q1=f(q0/k),⋮⋮an=qn−1−qnk,qn=f(qn−1/k)=0,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑓(𝑥) =⌊𝑥⌋f(x)=⌊x⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下表示的长度为 ⌈log𝑘⁡(𝑛 +1)⌉⌈logk⁡(n+1)⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们一般通过添加小数点「..![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」来表示小数1、添加负号「−−![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」来表示负数、在小数末尾的一段上添加上划线表示无限循环小数等．为了方便阅读，我们可以每隔若干数位添加间隔符号（如空格、,,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、`'` 等），如 12 34512 345![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 1234512345![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在计算机中，比较常用的进位制有二进制、八进制和十六进制．

## 不同进位制间的转换

### 十进制转其他进制

这里以二进制为例来演示，其他进制的原理与其类似．

整数部分，把十进制数不断执行除 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 操作，直至商数为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，之后从下到上，取所有余数的数字，即为二进制的整数部分数字．小数部分，则用其乘 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，取其整数部分的结果，再用计算后的小数部分依此重复计算，算到小数部分全为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为止，之后从上到下，取所有计算后整数部分的数字，即为二进制的小数部分数字．

例子

将 35.2535.25![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转化为二进制数．

整数部分：

35/2=17…1,17/2=8…1,8/2=4…0,4/2=2…0,2/2=1…0,1/2=0…1.35/2=17…1,17/2=8…1,8/2=4…0,4/2=2…0,2/2=1…0,1/2=0…1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

小数部分：

0.25×2=0.5…0,0.5×2=1…1.0.25×2=0.5…0,0.5×2=1…1.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即 35.25 =(100011.01)235.25=(100011.01)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text #include <algorithm> #include <string> // only non-negative // 2 <= base && base <= 36 std :: string from_dec ( int x , int base ) { if ( x == 0 ) return "0" ; std :: string res ; while ( x ) { int r = x % base ; x /= base ; // 写法 1 res . push_back ( r < 10 ? '0' \+ r : 'A' \+ r \- 10 ); // 写法 2 // const static std::string digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // res.push_back(digits[r]); } std :: reverse ( res . begin (), res . end ()); return res ; } ```   
---|---  
  
### 其他进制转十进制

还是以二进制为例．二进制数转换为十进制数，只需将每个位的值，乘以 2𝑖2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次即可，其中 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为当前位的位数，个位的位数为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

例子

将 (11010.01)2(11010.01)2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 转换为十进制数．

(11010.01)2=+ 1×24+1×23+0×22+1×21+0×20=+ 0×2−1+1×2−2=26.25.(11010.01)2=+ 1×24+1×23+0×22+1×21+0×20=+ 0×2−1+1×2−2=26.25.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即 (11010.01)2 =(26.25)10(11010.01)2=(26.25)10![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text #include <cctype> #include <string> // only non-negative // 2 <= base && base <= 36 int to_dec ( std :: string const & s , int base ) { int res = 0 ; for ( char c : s ) { res *= base ; if ( isdigit ( c )) res += c \- '0' ; else if ( isupper ( c )) res += c \- 'A' \+ 10 ; else if ( islower ( c )) res += c \- 'a' \+ 10 ; } return res ; } ```   
---|---  
  
### 二进制/八进制/十六进制间的相互转换

一个八进制位可以用 3 个二进制位来表示（因为 23 =823=8![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），一个十六进制位可以用 4 个二进制位来表示（24 =1624=16![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），反之同理．

## 补数法

另请参阅：[反码与补码](../../bit/#整数与位序列)

**补数法** （method of complements）是用正数表示负数，使得可以用和正数加法相同的算法/电路/机械结构来计算减法的方法．补数法广泛用于计算器和计算机的设计中，用以简化结构．

对 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其 **数基补数** （radix complement，称为 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的补数）是 𝑏𝑛 −𝑎bn−a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其 **缩减数基补数** （diminished radix complement，称为 𝑏 −1b−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的补数，简称 **减补数** ）是 𝑏𝑛 −1 −𝑎bn−1−a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在二进制下，数基补数叫做 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的补数（two's complement），又叫做 **补码** ；缩减数基补数叫做 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的补数（ones' complement），又叫做 **反码** ；在十进制下，数基补数又叫做 1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的补数（ten's complement），缩减数基补数又叫做 99![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的补数（nine's complement）；其他进制以此类推．

对 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位数 𝑥,𝑦x,y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，当计算 𝑥 −𝑦x−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，我们有如下方法（若结果超过 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，则舍弃高位）：

  1. 考虑 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的减补数 𝑥′ =𝑏𝑛 −1 −𝑥x′=bn−1−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，计算 𝑥′ +𝑦 =𝑏𝑛 −1 −𝑥 +𝑦x′+y=bn−1−x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则该结果的减补数即为答案．
  2. 考虑 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的减补数 𝑦′ =𝑏𝑛 −1 −𝑦y′=bn−1−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，计算 𝑥 +𝑦′ =𝑏𝑛 −1 +𝑥 −𝑦x+y′=bn−1+x−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，直接加一即为答案．
  3. 考虑 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数基补数 𝑥′ =𝑏𝑛 −𝑥x′=bn−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，计算 𝑥′ +𝑦 =𝑏𝑛 −𝑥 +𝑦x′+y=bn−x+y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则该结果的数基补数即为答案．
  4. 考虑 𝑦y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数基补数 𝑦′ =𝑏𝑛 −𝑦y′=bn−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，计算 𝑥 +𝑦′ =𝑏𝑛 +𝑥 −𝑦x+y′=bn+x−y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此即为答案．

另外，对 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的数，我们设 𝑑 =𝑘 −1d=k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 ⋯𝑑𝑑 =:――𝑑 =∑∞𝑖=0𝑑𝑘𝑖 = −1⋯dd=:d―=∑i=0∞dki=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以对 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设其数基补数在 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的表示为 𝑎𝑛−1⋯𝑎1𝑎0an−1⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 ――𝑑𝑎𝑛−1⋯𝑎1𝑎0d―an−1⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为 ∑𝑛−1𝑖=0𝑎𝑖𝑘𝑖 +∑∞𝑖=𝑛𝑑𝑘𝑖 =𝑘𝑛 −𝑥 +( −𝑘𝑛) = −𝑥∑i=0n−1aiki+∑i=n∞dki=kn−x+(−kn)=−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这种「无限位的数」的思想可以推广为 [**𝑝 p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进数**](https://en.wikipedia.org/wiki/P-adic_number)（𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)-adic number）．

此外，我们有一个关于补数和无限循环小数的有趣定理：

Midy 定理

设 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是正整数，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是正素数，𝑎/𝑝a/p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的表示为 0.―――――𝑎1𝑎2⋯𝑎𝑙0.a1a2⋯al―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为（最短）循环节长度．若 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是偶数4，设 𝑙 =2𝑘l=2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑎1𝑎2⋯𝑎𝑘a1a2⋯ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑎𝑘+1𝑎𝑘+2⋯𝑎2𝑘ak+1ak+2⋯a2k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的减补数，即：

  * 𝑎𝑖 +𝑎𝑖+𝑘 =𝑏ai+ai+k=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 𝑎1𝑎2⋯𝑎𝑘 +𝑎𝑘+1𝑎𝑘+2⋯𝑎2𝑘 =𝑏𝑘 −1a1a2⋯ak+ak+1ak+2⋯a2k=bk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

进一步，若 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有非平凡因子 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设 𝑙 =𝑛𝑘l=nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 ∑𝑛−1𝑖=0𝑎𝑖𝑘+1𝑎𝑖𝑘+2⋯𝑎(𝑖+1)𝑘∑i=0n−1aik+1aik+2⋯a(i+1)k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑏𝑘 −1bk−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的倍数．

例子

对于 1/19 =0.――――――――――――052 631 578 947 368 421 =0.―――――032 745(8)1/19=0.052 631 578 947 368 421―=0.032 745―(8)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们有：

  * 052 631 578 +947 368 421 =999 999 999052 631 578+947 368 421=999 999 999![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 052 +631 +578 +947 +368 +421 =3 ×999052+631+578+947+368+421=3×999![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 032(8) +745(8) =777(8)032(8)+745(8)=777(8)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，
  * 03(8) +27(8) +45(8) =77(8)03(8)+27(8)+45(8)=77(8)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明

对定理中的 𝑎,𝑏,𝑝,𝑙,𝑛,𝑘a,b,p,l,n,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，不难发现 1 ≤𝑎 <𝑝1≤a<p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏 >1b>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 (𝑎,𝑝) =(𝑏,𝑝) =1(a,p)=(b,p)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对整数 0 ≤𝑖 <𝑙0≤i<l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝑓(𝑖) =𝑏𝑖 ⋅𝑎/𝑝 −⌊𝑏𝑖 ⋅𝑎/𝑝⌋f(i)=bi⋅a/p−⌊bi⋅a/p⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们有

0<𝑓(𝑖)=0.―――――――――――𝑎𝑖+1𝑎𝑖+2⋯𝑎𝑛𝑘𝑎1𝑎2⋯𝑎𝑖<1⟹0<𝑝𝑓(𝑖)<𝑝.0<f(i)=0.ai+1ai+2⋯anka1a2⋯ai―<1⟹0<pf(i)<p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

注意到 𝑝𝑓(𝑖) ∈𝐍+pf(i)∈N+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑝𝑓(𝑖) ≡𝑎𝑏𝑖(mod𝑝)pf(i)≡abi(modp)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 𝑝𝑓(𝑖) =𝑎𝑏𝑖mod𝑝pf(i)=abimodp![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

令 𝑆𝑛 =∑𝑛−1𝑖=0𝑓(𝑖𝑘) =∑𝑛−1𝑖=00.――――――――――――𝑎𝑖𝑘+1𝑎𝑖𝑘+2⋯𝑎𝑛𝑘𝑎1𝑎2⋯𝑎𝑖𝑘Sn=∑i=0n−1f(ik)=∑i=0n−10.aik+1aik+2⋯anka1a2⋯aik―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以在各个小数间「交换」若干位（例如 0.――――142857 +0.――――285714 +0.――――571428 =0.――――141414 +0.――――282828 +0.――――575757 =0.――14 +0.――28 +0.――57 =14/99 +28/99 +57/99 =10.142857―+0.285714―+0.571428―=0.141414―+0.282828―+0.575757―=0.14―+0.28―+0.57―=14/99+28/99+57/99=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），则

𝑆𝑛=𝑛−1∑𝑖=00.―――――――――𝑎𝑖𝑘+1𝑎𝑖𝑘+2⋯𝑎(𝑖+1)𝑘=𝑛−1∑𝑖=0𝑎𝑖𝑘+1𝑎𝑖𝑘+2⋯𝑎(𝑖+1)𝑘/(𝑏𝑘−1),Sn=∑i=0n−10.aik+1aik+2⋯a(i+1)k―=∑i=0n−1aik+1aik+2⋯a(i+1)k/(bk−1),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

进而

𝑝𝑆𝑛=𝑝𝑛−1∑𝑖=0𝑎𝑖𝑘+1𝑎𝑖𝑘+2⋯𝑎(𝑖+1)𝑘/(𝑏𝑘−1)=𝑛−1∑𝑖=0(𝑎𝑏𝑖𝑘mod𝑝),pSn=p∑i=0n−1aik+1aik+2⋯a(i+1)k/(bk−1)=∑i=0n−1(abikmodp),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此

𝑛−1∑𝑖=0𝑎𝑖𝑘+1𝑎𝑖𝑘+2⋯𝑎(𝑖+1)𝑘=(𝑏𝑘−1)∑𝑛−1𝑖=0(𝑎𝑏𝑖𝑘mod𝑝)𝑝.∑i=0n−1aik+1aik+2⋯a(i+1)k=(bk−1)∑i=0n−1(abikmodp)p.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若 𝑝 ∣(𝑏𝑘−1)p∣(bk−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，注意到

(𝑏𝑘−1)𝑎/𝑝=𝑎1𝑎2⋯𝑎𝑘.―――――――――――𝑎𝑘+1𝑎𝑘+2⋯𝑎𝑛𝑘𝑎1𝑎2⋯𝑎𝑘−0.――――――𝑎1𝑎2⋯𝑎𝑛𝑘,(bk−1)a/p=a1a2⋯ak.ak+1ak+2⋯anka1a2⋯ak―−0.a1a2⋯ank―,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则有 𝑎𝑘+1𝑎𝑘+2⋯𝑎𝑛𝑘𝑎1𝑎2⋯𝑎𝑘 =𝑎1𝑎2⋯𝑎𝑛𝑘ak+1ak+2⋯anka1a2⋯ak=a1a2⋯ank![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进而 𝑎1𝑎2⋯𝑎𝑘 =𝑎𝑘+1𝑎𝑘+2⋯𝑎2𝑘 =⋯ =𝑎(𝑛−1)𝑘+1𝑎(𝑛−1)𝑘+2⋯𝑎𝑛𝑘a1a2⋯ak=ak+1ak+2⋯a2k=⋯=a(n−1)k+1a(n−1)k+2⋯ank![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 0.―――――𝑎1𝑎2⋯𝑎𝑙 =0.―――――𝑎1𝑎2⋯𝑎𝑘0.a1a2⋯al―=0.a1a2⋯ak―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这与 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义矛盾，因此 𝑝 ∤(𝑏𝑘−1)p∤(bk−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

故存在正整数 𝑐 =∑𝑛−1𝑖=0(𝑎𝑏𝑖𝑘mod𝑝)𝑝c=∑i=0n−1(abikmodp)p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得

𝑛−1∑𝑖=0𝑎𝑖𝑘+1𝑎𝑖𝑘+2⋯𝑎(𝑖+1)𝑘=𝑐(𝑏𝑘−1).∑i=0n−1aik+1aik+2⋯a(i+1)k=c(bk−1).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)推论

对上述的 𝑏,𝑛,𝑘,𝑝b,n,k,p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有

𝑛−1∑𝑖=0𝑏𝑖𝑘≡0(mod𝑝).∑i=0n−1bik≡0(modp).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 广义进制系统

标准的进制系统中，基数 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是一个固定的正数，每个数位在 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种不同的符号中选取，用以表示一个非负数（不考虑小数点和负号）．实际上仍有许多记数系统和进制系统有类似的特征，但不完全符合进制系统的规定，我们把这样的记数系统称为 **广义进制系统** 或 **非标准进制系统** （Non-standard positional numeral systems）．下面介绍几种常见的广义进制系统．

### 双射记数系统

标准的进制系统并不能和其表示的数字建立双射，如 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、0101![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、001001![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示的数是相同的2，而 **双射记数系统** （bijective numeral system）可以和其表示的数字建立双射．

双射 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制（𝑘 ≥1k≥1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）使用数集 {1,2,…,𝑘}{1,2,…,k}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来唯一表示一个数，规则如下：

  1. 用空串表示 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  2. 用非空串 𝑎𝑛⋯𝑎1𝑎0an⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示数 𝑎𝑛𝑘𝑛 +⋯ +𝑎1𝑘1 +𝑎0𝑘0 =∑𝑛𝑖=0𝑎𝑖𝑘𝑖ankn+⋯+a1k1+a0k0=∑i=0naiki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对一个正数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设其双射 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的表示为 𝑎𝑛⋯𝑎1𝑎0an⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则有：

𝑎0=𝑚−𝑞0𝑘,𝑞0=𝑓(𝑚/𝑘),𝑎1=𝑞0−𝑞1𝑘,𝑞1=𝑓(𝑞0/𝑘),⋮⋮𝑎𝑛=𝑞𝑛−1−𝑞𝑛𝑘,𝑞𝑛=𝑓(𝑞𝑛−1/𝑘)=0,a0=m−q0k,q0=f(m/k),a1=q0−q1k,q1=f(q0/k),⋮⋮an=qn−1−qnk,qn=f(qn−1/k)=0,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑓(𝑥) =⌈𝑥⌉ −1f(x)=⌈x⌉−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

例如 Microsoft Excel 的列标签采用的就是双射 2626![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制．

在双射记数系统下，我们有 [一进制](https://en.wikipedia.org/wiki/Unary_numeral_system)，一进制下的非空串只由 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 构成，串的长度即为其表示的数．

类似 补数法 下的叙述，在 𝑘 >1k>1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的双射 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下，我们设 𝑑 =𝑘 −1d=k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 ⋯𝑑𝑑 =:――𝑑 =∑∞𝑖=0𝑑𝑘𝑖 = −1⋯dd=:d―=∑i=0∞dki=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进而 ――𝑑𝑘 =0d―k=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以设 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在双射 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的表示为 𝑎𝑛−1⋯𝑎1𝑎0an−1⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 ――𝑑𝑘𝑎𝑛−1⋯𝑎1𝑎0d―kan−1⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即为 −𝑥−x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

下面是双射 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制数的一些性质：

  * 长度为 𝑙 ≥0l≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数共有 𝑘𝑙kl![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种．
  * 𝑘 ≥2k≥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在双射 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下表示的长度为 ⌊log𝑘⁡(𝑛 +1)(𝑘 −1)⌋⌊logk⁡(n+1)(k−1)⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑘 ≥2k≥2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，若一个数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的表示中不含 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则其在 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的表示和在双射 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下的表示相同．

双射 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制转十进制和 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制转十进制的代码相同，下面是十进制转双射 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制的参考实现

实现

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text #include <algorithm> #include <string> // only non-negative // 1 <= base && base < 36 std :: string from_dec_bi ( int x , int base ) { std :: string res ; while ( x > 0 ) { int q = ( x \+ base \- 1 ) / base \- 1 , r = x \- q * base ; x = q ; // 写法 1 res . push_back ( r < 10 ? '0' \+ r : 'A' \+ r \- 10 ); // 写法 2 // const static std::string digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // res.push_back(digits[r]); } std :: reverse ( res . begin (), res . end ()); return res ; } ```   
---|---  
  
### 有符号位数进制

有的进位制系统允许数位中出现负数，例如 [平衡三进制](../balanced-ternary/)．

### Gray 码

主条目：[格雷码](../gray-code/)

Gray 码又叫 **循环二进制码** 或 **反射二进制码** （reflected binary code，RBC），是一种特殊的二进制数字系统，常用于数据校验中．

### 非正基数进制

我们知道对于 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制数 𝑎𝑛⋯𝑎1𝑎0an⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其表示的值为 ∑𝑛𝑖=0𝑎𝑖𝑘𝑖∑i=0naiki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们稍加修改即可定义 −𝑘−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制数 𝑎𝑛⋯𝑎1𝑎0(−𝑘)an⋯a1a0(−k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 ∑𝑛𝑖=0𝑎𝑖( −𝑘)𝑖∑i=0nai(−k)i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑎𝑛,…,𝑎1,𝑎0 ∈{0,1,…,𝑘 −1}an,…,a1,a0∈{0,1,…,k−1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．例如 12345(−10) =8265(10)12345(−10)=8265(10)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这种进制系统叫做 [**负底数进制**](https://en.wikipedia.org/wiki/Negative_base)（negative-base system）．

类似地，我们也可以定义 [**复底数进制**](https://en.wikipedia.org/wiki/Complex-base_system)（complex-base system），如 [**2 i2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制**](https://en.wikipedia.org/wiki/Quater-imaginary_base)（quater-imaginary base、quater-imaginary numeral system），我们还可以定义 [**非整数进位制**](https://en.wikipedia.org/wiki/Non-integer_base_of_numeration)（non-integer base of numeration）用于表示实数的 **𝛽 β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 展开**（𝛽β![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)-expansion）等．

### 混合基数进制

标准的进制系统中，每一个数位对应的基数都是固定的，而混合基数进制允许每一个数位对应不同的基数．混合基数进制系统最常见的应用就是计时：小时采用 2424![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制，分钟和秒采用 6060![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制．

𝑎𝑛⋯𝑎1𝑎0an⋯a1a0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制下表示的数为 ∑𝑛𝑖=0𝑎𝑖𝑏𝑖∑i=0naibi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而在混合基数进制下，其表示的数为 ∑𝑛𝑖=0𝑎𝑖∏𝑖−1𝑗=0𝑏𝑗∑i=0nai∏j=0i−1bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑏𝑗bj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑎𝑗aj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的基数．

在算法竞赛中，最常见的混合基数进制系统是 [**阶乘进制**](https://en.wikipedia.org/wiki/Factorial_number_system)（factorial number system），其中的数可以记作 𝑎𝑛⋯𝑎1𝑎0 !an⋯a1a0 !![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其表示的数为 ∑𝑛𝑖=0𝑎𝑖𝑖!∑i=0naii!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)3．阶乘进制在算法竞赛中的应用可参见 [Lehmer 码/Cantor 展开](../../permutation/#排名)．

实现（十进制转阶乘进制）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text #include <algorithm> #include <string> // only non-negative std :: string from_dec_factorial ( int x ) { if ( x == 0 ) return "0" ; std :: string res ; int base = 1 ; while ( x ) { int r = x % base ; x /= base ++ ; // 写法 1 res . push_back ( r < 10 ? '0' \+ r : 'A' \+ r \- 10 ); // 写法 2 // const static std::string digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // res.push_back(digits[r]); } std :: reverse ( res . begin (), res . end ()); return res ; } ```   
---|---  
  
实现（阶乘进制转十进制）

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text #include <cctype> #include <string> // only non-negative int to_dec_factorial ( std :: string const & s ) { int res = 0 , base = s . size (); for ( char c : s ) { res *= base \-- ; if ( isdigit ( c )) res += c \- '0' ; else if ( isupper ( c )) res += c \- 'A' \+ 10 ; else if ( islower ( c )) res += c \- 'a' \+ 10 ; } return res ; } ```   
---|---  
  
## C++ 中的实现

对于非负数，C++ 中用 `<前缀><数位><后缀>` 表示一个整数字面量，其中 `<数位>` 和 `<后缀>` 均可以为空．`<后缀>` 用于表示字面量的类型，如 `u` 或 `U` 表示该字面量为 `unsigned`、`l` 或 `L` 表示该字面量为 `long` 等．对于 `<前缀>`：

  * 当 `<前缀>` 为 `0x` 或 `0X` 时表示十六进制字面量，此时 `<数位>` 中的字符只能在 `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, A, b, B, c, C, d, D, e, E, f, F` 中选取．例如 `0x1234ABCD` 为 1234ABCD(16) =305 441 7411234ABCD(16)=305 441 741![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 当 `<前缀>` 为 `0` 时表示八进制字面量，此时 `<数位>` 中的字符只能在 `0, 1, 2, 3, 4, 5, 6, 7` 中选取．例如 `01234567` 为 1234567(8) =3423911234567(8)=342391![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；5
  * 当 `<前缀>` 为 `1`、`2`、`3`、`4`、`5`、`6`、`7`、`8` 或 `9` 时表示十进制字面量，此时 `<数位>` 中的字符只能在 `0, 1, 2, 3, 4, 5, 6, 7, 8, 9` 中选取；
  * C++14 起，当 `<前缀>` 为 `0b` 或 `0B` 时表示二进制字面量，此时 `<数位>` 中的字符只能在 `0, 1` 中选取．例如 `0b11001010` 为 11001010(2) =20211001010(2)=202![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 参考资料与注释

  * [Positional notation - Wikipedia](https://en.wikipedia.org/wiki/Positional_notation)
  * [Method of complements - Wikipedia](https://en.wikipedia.org/wiki/Method_of_complements)
  * [Non-standard positional numeral systems - Wikipedia](https://en.wikipedia.org/wiki/Non-standard_positional_numeral_systems)
  * [Bijective numeration - Wikipedia](https://en.wikipedia.org/wiki/Bijective_numeration)
  * [Midy's theorem - Wikipedia](https://en.wikipedia.org/wiki/Midy%27s_theorem)
  * [N3472 - Binary Literals in the C++ Core Language](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2012/n3472.pdf)

* * *

  1. 有的地区使用「,,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」表示小数点． ↩

  2. 我们把最高的非 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位之前的 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为 [**前导零**](https://en.wikipedia.org/wiki/Leading_zero)（leading zero）．类似地，我们可以定义 [**后导零**](https://en.wikipedia.org/wiki/Trailing_zero)（trailing zero）． ↩

  3. 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的基数是 𝑖 +1i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，0 ≤𝑎𝑖 ≤𝑖0≤ai≤i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．注意到 (𝑛 +1)! −𝑛! =𝑛 ⋅𝑛!(n+1)!−n!=n⋅n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以数在阶乘进制下的表示在去除前导零的情况下是唯一的． ↩

  4. 当 𝑎 =1a=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，在十进制下满足该条件的素数序列是 [A028416](https://oeis.org/A028416)． ↩

  5. `0` 是八进制字面量． ↩

* * *

>  __本页面最近更新： 2026/1/30 14:50:40，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/numeral-sys/base.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/numeral-sys/base.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [c-forrest](https://github.com/c-forrest), [Enter-tainer](https://github.com/Enter-tainer), [hhc0001](https://github.com/hhc0001), [Ir1d](https://github.com/Ir1d), [KingMario](https://github.com/KingMario), [ksyx](https://github.com/ksyx), [Lutra-Fs](https://github.com/Lutra-Fs), [MegaOwIer](https://github.com/MegaOwIer), [niujiaxing](https://github.com/niujiaxing), [StudyingFather](https://github.com/StudyingFather), [TOMWT-qwq](https://github.com/TOMWT-qwq), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
