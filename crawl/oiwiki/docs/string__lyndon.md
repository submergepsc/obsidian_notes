# Lyndon 分解 - OI Wiki

- Source: https://oi-wiki.org/string/lyndon/

# Lyndon 分解

## 定义

首先我们介绍 Lyndon 分解的概念．

Lyndon 串：对于字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字典序严格小于 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的所有后缀的字典序，我们称 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是简单串，或者 **Lyndon 串** ．举一些例子，`a`,`b`,`ab`,`aab`,`abb`,`ababb`,`abcd` 都是 Lyndon 串．当且仅当 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字典序严格小于它的所有非平凡的（非平凡：非空且不同于自身）循环同构串时，𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 才是 Lyndon 串．

Lyndon 分解：串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Lyndon 分解记为 𝑠 =𝑤1𝑤2⋯𝑤𝑘s=w1w2⋯wk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中所有 𝑤𝑖wi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为简单串，并且他们的字典序按照非严格单减排序，即 𝑤1 ≥𝑤2 ≥⋯ ≥𝑤𝑘w1≥w2≥⋯≥wk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．可以发现，这样的分解存在且唯一．

## Duval 算法

### 解释

Duval 可以在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内求出一个串的 Lyndon 分解．

首先我们介绍另外一个概念：如果一个字符串 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能够分解为 𝑡 =𝑤𝑤⋯――𝑤t=ww⋯w―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式，其中 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 Lyndon 串，而 ――𝑤w―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀（――𝑤w―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可能是空串），那么称 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是近似简单串（pre-simple），或者近似 Lyndon 串．一个 Lyndon 串也是近似 Lyndon 串．

Duval 算法运用了贪心的思想．算法过程中我们把串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分成三个部分 𝑠 =𝑠1𝑠2𝑠3s=s1s2s3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑠1s1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 Lyndon 串，它的 Lyndon 分解已经记录；𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个近似 Lyndon 串；𝑠3s3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是未处理的部分．

### 过程

整体描述一下，该算法每一次尝试将 𝑠3s3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的首字符添加到 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的末尾．如果 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不再是近似 Lyndon 串，那么我们就可以将 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 截出一部分前缀（即 Lyndon 分解）接在 𝑠1s1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 末尾．

我们来更详细地解释一下算法的过程．定义一个指针 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指向 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的首字符，则 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 从 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（字符串长度）．在循环的过程中我们定义另一个指针 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指向 𝑠3s3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的首字符，指针 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指向 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中我们当前考虑的字符（意义是 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的上一个循环节中对应的字符）．我们的目标是将 𝑠[𝑗]s[j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 添加到 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的末尾，这就需要将 𝑠[𝑗]s[j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑠[𝑘]s[k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做比较：

  1. 如果 𝑠[𝑗] =𝑠[𝑘]s[j]=s[k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则将 𝑠[𝑗]s[j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 添加到 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 末尾不会影响它的近似简单性．于是我们只需要让指针 𝑗,𝑘j,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 自增（移向下一位）即可．
  2. 如果 𝑠[𝑗] >𝑠[𝑘]s[j]>s[k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑠2𝑠[𝑗]s2s[j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就变成了一个 Lyndon 串，于是我们将指针 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 自增，而让 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 指向 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的首字符，这样 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就变成了一个循环次数为 1 的新 Lyndon 串了．
  3. 如果 𝑠[𝑗] <𝑠[𝑘]s[j]<s[k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑠2𝑠[𝑗]s2s[j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就不是一个近似简单串了，那么我们就要把 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分解出它的一个 Lyndon 子串，这个 Lyndon 子串的长度将是 𝑗 −𝑘j−k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即它的一个循环节．然后把 𝑠2s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 变成分解完以后剩下的部分，继续循环下去（注意，这个情况下我们没有改变指针 𝑗,𝑘j,k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），直到循环节被截完．对于剩余部分，我们只需要将进度「回退」到剩余部分的开头即可．

### 实现

下面的代码返回串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Lyndon 分解方案．

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` |  ```text // duval_algorithm vector < string > duval ( string const & s ) { int n = s . size (), i = 0 ; vector < string > factorization ; while ( i < n ) { int j = i \+ 1 , k = i ; while ( j < n && s [ k ] <= s [ j ]) { if ( s [ k ] < s [ j ]) k = i ; else k ++ ; j ++ ; } while ( i <= k ) { factorization . push_back ( s . substr ( i , j \- k )); i += j \- k ; } } return factorization ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` |  ```text # duval_algorithm def duval ( s ): n , i = len ( s ), 0 factorization = [] while i < n : j , k = i \+ 1 , i while j < n and s [ k ] <= s [ j ]: if s [ k ] < s [ j ]: k = i else : k += 1 j += 1 while i <= k : factorization . append ( s [ i : i \+ j \- k ]) i += j \- k return factorization ```   
---|---  
  
### 复杂度分析

接下来我们证明一下这个算法的复杂度．

外层的循环次数不超过 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因为每一次 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都会增加．第二个内层循环也是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的，因为它只记录 Lyndon 分解的方案．接下来我们分析一下内层循环．很容易发现，每一次在外层循环中找到的 Lyndon 串是比我们所比较过的剩余的串要长的，因此剩余的串的长度和要小于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，于是我们最多在内层循环 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．事实上循环的总次数不超过 4𝑛 −34n−3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 最小表示法（Finding the smallest cyclic shift）

对于长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们可以通过上述算法寻找该串的最小表示法．

我们构建串 𝑠𝑠ss![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Lyndon 分解，然后寻找这个分解中的一个 Lyndon 串 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得它的起点小于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且终点大于等于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．可以很容易地使用 Lyndon 分解的性质证明，子串 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的首字符就是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小表示法的首字符，即我们沿着 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的开头往后 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符组成的串就是 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小表示法．

于是我们在分解的过程中记录每一次的近似 Lyndon 串的开头即可．

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` |  ```text // smallest_cyclic_string string min_cyclic_string ( string s ) { s += s ; int n = s . size (); int i = 0 , ans = 0 ; while ( i < n / 2 ) { ans = i ; int j = i \+ 1 , k = i ; while ( j < n && s [ k ] <= s [ j ]) { if ( s [ k ] < s [ j ]) k = i ; else k ++ ; j ++ ; } while ( i <= k ) i += j \- k ; } return s . substr ( ans , n / 2 ); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text # smallest_cyclic_string def min_cyclic_string ( s ): s += s n = len ( s ) i , ans = 0 , 0 while i < n / 2 : ans = i j , k = i \+ 1 , i while j < n and s [ k ] <= s [ j ]: if s [ k ] < s [ j ]: k = i else : k += 1 j += 1 while i <= k : i += j \- k return s [ ans : ans \+ n / 2 ] ```   
---|---  
  
## 习题

  * [UVa #719 - Glass Beads](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=660)

**本页面主要译自博文[Декомпозиция Линдона. Алгоритм Дюваля. Нахождение наименьшего циклического сдвига](http://e-maxx.ru/algo/duval_algorithm) 与其英文翻译版 [Lyndon factorization](https://cp-algorithms.com/string/lyndon_factorization.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/lyndon.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/lyndon.md "edit.link.title")  
>  __本页面贡献者：[iamtwz](https://github.com/iamtwz), [orzAtalod](https://github.com/orzAtalod), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [ksyx](https://github.com/ksyx), [Xeonacid](https://github.com/Xeonacid), [Chrogeek](https://github.com/Chrogeek), [diauweb](https://github.com/diauweb), [Enter-tainer](https://github.com/Enter-tainer), [gi-b716](https://github.com/gi-b716), [hqztrue](https://github.com/hqztrue), [Junyan721113](https://github.com/Junyan721113), [Menci](https://github.com/Menci), [shawlleyw](https://github.com/shawlleyw), [Soresen](https://github.com/Soresen), [Suyun514](mailto:suyun514@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
