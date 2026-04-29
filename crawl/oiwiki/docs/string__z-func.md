# Z 函数（扩展 KMP） - OI Wiki

- Source: https://oi-wiki.org/string/z-func/

# Z 函数（扩展 KMP）

约定：字符串下标以 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为起点．

## 定义

对于一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义函数 𝑧[𝑖]z[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑠[𝑖,𝑛 −1]s[i,n−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（即以 𝑠[𝑖]s[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开头的后缀）的最长公共前缀（LCP）的长度，则 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 被称为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **Z 函数** ．特别地，𝑧[0] =0z[0]=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

国外一般将计算该数组的算法称为 **Z Algorithm** ，而国内则称其为 **扩展 KMP** （exKMP）．

这篇文章介绍在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间复杂度内计算 Z 函数的算法以及其各种应用．

## 解释

下面若干样例展示了对于不同字符串的 Z 函数：

  * 𝑧(𝚊𝚊𝚊𝚊𝚊) =[0,4,3,2,1]z(aaaaa)=[0,4,3,2,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑧(𝚊𝚊𝚊𝚋𝚊𝚊𝚋) =[0,2,1,0,2,1,0]z(aaabaab)=[0,2,1,0,2,1,0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑧(𝚊𝚋𝚊𝚌𝚊𝚋𝚊) =[0,0,1,0,3,0,1]z(abacaba)=[0,0,1,0,3,0,1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 朴素算法

Z 函数的朴素算法复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

实现

C++Python

```text 1 2 3 4 5 6 7 ``` |  ```text vector < int > z_function_trivial ( string s ) { int n = ( int ) s . length (); vector < int > z ( n ); for ( int i = 1 ; i < n ; ++ i ) while ( i \+ z [ i ] < n && s [ z [ i ]] == s [ i \+ z [ i ]]) ++ z [ i ]; return z ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 ``` |  ```text def z_function_trivial ( s ): n = len ( s ) z = [ 0 ] * n for i in range ( 1 , n ): while i \+ z [ i ] < n and s [ z [ i ]] == s [ i \+ z [ i ]]: z [ i ] += 1 return z ```   
---|---  
  
## 线性算法

如同大多数字符串主题所介绍的算法，其关键在于，运用自动机的思想寻找限制条件下的状态转移函数，使得可以借助之前的状态来加速计算新的状态．

在该算法中，我们从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 顺次计算 𝑧[𝑖]z[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值（𝑧[0] =0z[0]=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．在计算 𝑧[𝑖]z[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的过程中，我们会利用已经计算好的 𝑧[0],…,𝑧[𝑖 −1]z[0],…,z[i−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们称区间 [𝑖,𝑖 +𝑧[𝑖] −1][i,i+z[i]−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **匹配段** ，也可以叫 Z-box．

算法的过程中我们维护右端点最靠右的匹配段．为了方便，记作 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．根据定义，𝑠[𝑙,𝑟]s[l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀．在计算 𝑧[𝑖]z[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时我们保证 𝑙 ≤𝑖l≤i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．初始时 𝑙 =𝑟 =0l=r=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

在计算 𝑧[𝑖]z[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的过程中：

  * 如果 𝑖 ≤𝑟i≤r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么根据 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义有 𝑠[𝑖,𝑟] =𝑠[𝑖 −𝑙,𝑟 −𝑙]s[i,r]=s[i−l,r−l]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此 𝑧[𝑖] ≥min(𝑧[𝑖 −𝑙],𝑟 −𝑖 +1)z[i]≥min(z[i−l],r−i+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这时：
    * 若 𝑧[𝑖 −𝑙] <𝑟 −𝑖 +1z[i−l]<r−i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑧[𝑖] =𝑧[𝑖 −𝑙]z[i]=z[i−l]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
    * 否则 𝑧[𝑖 −𝑙] ≥𝑟 −𝑖 +1z[i−l]≥r−i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这时我们令 𝑧[𝑖] =𝑟 −𝑖 +1z[i]=r−i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，然后暴力枚举下一个字符扩展 𝑧[𝑖]z[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 直到不能扩展为止．
  * 如果 𝑖 >𝑟i>r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么我们直接按照朴素算法，从 𝑠[𝑖]s[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始比较，暴力求出 𝑧[𝑖]z[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 在求出 𝑧[𝑖]z[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，如果 𝑖 +𝑧[𝑖] −1 >𝑟i+z[i]−1>r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们就需要更新 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即令 𝑙 =𝑖,𝑟 =𝑖 +𝑧[𝑖] −1l=i,r=i+z[i]−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

可以访问 [这个网站](https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm) 来看 Z 函数的模拟过程．

### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text vector < int > z_function ( string s ) { int n = ( int ) s . length (); vector < int > z ( n ); for ( int i = 1 , l = 0 , r = 0 ; i < n ; ++ i ) { if ( i <= r && z [ i \- l ] < r \- i \+ 1 ) { z [ i ] = z [ i \- l ]; } else { z [ i ] = max ( 0 , r \- i \+ 1 ); while ( i \+ z [ i ] < n && s [ z [ i ]] == s [ i \+ z [ i ]]) ++ z [ i ]; } if ( i \+ z [ i ] \- 1 > r ) l = i , r = i \+ z [ i ] \- 1 ; } return z ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text def z_function ( s ): n = len ( s ) z = [ 0 ] * n l , r = 0 , 0 for i in range ( 1 , n ): if i <= r and z [ i \- l ] < r \- i \+ 1 : z [ i ] = z [ i \- l ] else : z [ i ] = max ( 0 , r \- i \+ 1 ) while i \+ z [ i ] < n and s [ z [ i ]] == s [ i \+ z [ i ]]: z [ i ] += 1 if i \+ z [ i ] \- 1 > r : l = i r = i \+ z [ i ] \- 1 return z ```   
---|---  
  
## 复杂度分析

对于内层 `while` 循环，每次执行都会使得 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 向后移至少 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位，而 𝑟 <𝑛 −1r<n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以总共只会执行 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．

对于外层循环，只有一遍线性遍历．

总复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 应用

我们现在来考虑在若干具体情况下 Z 函数的应用．

这些应用在很大程度上同 [前缀函数](../kmp/) 的应用类似．

### 匹配所有子串

为了避免混淆，我们将 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称作 **文本** ，将 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称作 **模式** ．所给出的问题是：寻找在文本 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中模式 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有出现（occurrence）．

为了解决该问题，我们构造一个新的字符串 𝑠 =𝑝 + ⋄ +𝑡s=p+⋄+t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也即我们将 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 连接在一起，但是在中间放置了一个分割字符 ⋄⋄![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（我们将如此选取 ⋄⋄![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得其必定不出现在 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中）．

首先计算 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Z 函数．接下来，对于在区间 [0,|𝑡| −1][0,|t|−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的任意 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们考虑以 𝑡[𝑖]t[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为开头的后缀在 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的 Z 函数值 𝑘 =𝑧[𝑖 +|𝑝| +1]k=z[i+|p|+1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果 𝑘 =|𝑝|k=|p|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么我们知道有一个 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的出现位于 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个位置，否则没有 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的出现位于 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个位置．

其时间复杂度（同时也是其空间复杂度）为 𝑂(|𝑡| +|𝑝|)O(|t|+|p|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 本质不同子串数

给定一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，计算 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的本质不同子串的数目．

考虑计算增量，即在知道当前 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的本质不同子串数的情况下，计算出在 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 末尾添加一个字符后的本质不同子串数．

令 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为当前 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的本质不同子串数．我们添加一个新的字符 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的末尾．显然，会出现一些以 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结尾的新的子串（以 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结尾且之前未出现过的子串）．

设串 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑠 +𝑐s+c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的反串（反串指将原字符串的字符倒序排列形成的字符串）．我们的任务是计算有多少 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀未在 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的其他地方出现．考虑计算 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Z 函数并找到其最大值 𝑧maxzmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．则 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的长度小于等于 𝑧maxzmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀的反串在 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中是已经出现过的以 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结尾的子串．

所以，将字符 𝑐c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 添加至 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后新出现的子串数目为 |𝑡| −𝑧max|t|−zmax![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

算法时间复杂度为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

值得注意的是，我们可以用同样的方法在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内，重新计算在端点处添加一个字符或者删除一个字符（从尾或者头）后的本质不同子串数目．

### 字符串整周期

给定一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，找到其最短的整周期，即寻找一个最短的字符串 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以被若干个 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 拼接而成的字符串表示．

考虑计算 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Z 函数，则其整周期的长度为最小的 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的因数 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 𝑖 +𝑧[𝑖] =𝑛i+z[i]=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

该事实的证明同应用 [前缀函数](../kmp/) 的证明一样．

## 练习题目

  * [luogu P5410【模板】扩展 KMP/exKMP（Z 函数）](https://www.luogu.com.cn/problem/P5410)
  * [luogu P7114【NOIP2020】字符串匹配](https://www.luogu.com.cn/problem/P7114)
  * [CF126B Password](http://codeforces.com/problemset/problem/126/B)
  * [UVa # 455 Periodic Strings](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=396)
  * [UVa # 11022 String Factoring](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1963)
  * [UVa 11475 - Extend to Palindrome](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2470)
  * [Codechef - Chef and Strings](https://www.codechef.com/problems/CHSTR)
  * [Codeforces - Prefixes and Suffixes](http://codeforces.com/problemset/problem/432/D)
  * [Leetcode 2223 - Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/)

**本页面主要译自博文[Z-функция строки и её вычисление](http://e-maxx.ru/algo/z_function) 与其英文翻译版 [Z-function and its calculation](https://cp-algorithms.com/string/z-function.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/z-func.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/z-func.md "edit.link.title")  
>  __本页面贡献者：[sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [Enter-tainer](https://github.com/Enter-tainer), [LeoJacob](https://github.com/LeoJacob), [countercurrent-time](https://github.com/countercurrent-time), [H-J-Granger](https://github.com/H-J-Granger), [minghu6](https://github.com/minghu6), [NachtgeistW](https://github.com/NachtgeistW), [iamtwz](https://github.com/iamtwz), [Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [weiyong1024](https://github.com/weiyong1024), [AngelKitty](https://github.com/AngelKitty), [c-forrest](https://github.com/c-forrest), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [HeRaNO](https://github.com/HeRaNO), [Konano](https://github.com/Konano), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [mgt](mailto:i@margatroid.xyz), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [Suyun514](mailto:suyun514@qq.com), [Xeonacid](https://github.com/Xeonacid), [amlhdsan](https://github.com/amlhdsan), [Dfkuaid](https://github.com/Dfkuaid), [ethanrao](https://github.com/ethanrao), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [gi-b716](https://github.com/gi-b716), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [ouuan](https://github.com/ouuan), [Peanut-Tang](https://github.com/Peanut-Tang), [pengxurui](https://github.com/pengxurui), [shawlleyw](https://github.com/shawlleyw), [shuzhouliu](https://github.com/shuzhouliu), [SukkaW](https://github.com/SukkaW), [TrisolarisHD](mailto:orzcyand1317@gmail.com)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
