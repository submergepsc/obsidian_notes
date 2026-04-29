# Manacher - OI Wiki

- Source: https://oi-wiki.org/string/manacher/

# Manacher

## 描述

给定一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，请找到所有对 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得子串 𝑠[𝑖…𝑗]s[i…j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一个回文串．当 𝑡 =𝑡revt=trev![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，字符串 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个回文串（𝑡revtrev![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的反转字符串）．

## 解释

显然在最坏情况下可能有 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个回文串，因此似乎一眼看过去该问题并没有线性算法．

但是关于回文串的信息可用 **一种更紧凑的方式** 表达：对于每个位置 𝑖 =0…𝑛 −1i=0…n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们找出值 𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑑2[𝑖]d2[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．二者分别表示以位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心的长度为奇数和长度为偶数的回文串个数．换个角度，二者也表示了以位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心的最长回文串的半径长度（半径长度 𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑑2[𝑖]d2[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为从位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到回文串最右端位置包含的字符个数）．

举例来说，字符串 𝑠 =𝚊𝚋𝚊𝚋𝚊𝚋𝚌s=abababc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 𝑠[3] =𝑏s[3]=b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心有三个奇数长度的回文串，最长回文串半径为 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也即 𝑑1[3] =3d1[3]=3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑎 𝑑1[3]=3⏞𝑏 𝑎 𝑏𝑠3 𝑎 𝑏 𝑐a b a bs3 a b⏞d1[3]=3 c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

字符串 𝑠 =𝚌𝚋𝚊𝚊𝚋𝚍s=cbaabd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 以 𝑠[3] =𝑎s[3]=a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心有两个偶数长度的回文串，最长回文串半径为 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也即 𝑑2[3] =2d2[3]=2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：

𝑐 𝑑2[3]=2⏞𝑏 𝑎 𝑎𝑠3 𝑏 𝑑c b a as3 b⏞d2[3]=2 d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此关键思路是，如果以某个位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心，我们有一个长度为 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的回文串，那么我们有以 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心的长度为 𝑙 −2l−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑙 −4l−4![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，等等的回文串．所以 𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑑2[𝑖]d2[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 两个数组已经足够表示字符串中所有子回文串的信息．

一个令人惊讶的事实是，存在一个复杂度为线性并且足够简单的算法计算上述两个「回文性质数组」𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑑2[]d2[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．在这篇文章中我们将详细的描述该算法．

## 解法

总的来说，该问题具有多种解法：应用字符串哈希，该问题可在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内解决，而使用后缀数组和快速 LCA 该问题可在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时间内解决．

但是这里描述的算法 **压倒性** 的简单，并且在时间和空间复杂度上具有更小的常数．该算法由 **Glenn K. Manacher** 在 1975 年提出．

## 朴素算法

为了避免在之后的叙述中出现歧义，这里我们指出什么是「朴素算法」．

该算法通过下述方式工作：对每个中心位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在比较一对对应字符后，只要可能，该算法便尝试将答案加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

该算法是比较慢的：它只能在 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内计算答案．

该朴素算法的实现如下：

实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text vector < int > d1 ( n ), d2 ( n ); for ( int i = 0 ; i < n ; i ++ ) { d1 [ i ] = 1 ; while ( 0 <= i \- d1 [ i ] && i \+ d1 [ i ] < n && s [ i \- d1 [ i ]] == s [ i \+ d1 [ i ]]) { d1 [ i ] ++ ; } d2 [ i ] = 0 ; while ( 0 <= i \- d2 [ i ] \- 1 && i \+ d2 [ i ] < n && s [ i \- d2 [ i ] \- 1 ] == s [ i \+ d2 [ i ]]) { d2 [ i ] ++ ; } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 ``` |  ```text d1 = [ 0 ] * n d2 = [ 0 ] * n for i in range ( 0 , n ): d1 [ i ] = 1 while 0 <= i \- d1 [ i ] and i \+ d1 [ i ] < n and s [ i \- d1 [ i ]] == s [ i \+ d1 [ i ]]: d1 [ i ] += 1 d2 [ i ] = 0 while 0 <= i \- d2 [ i ] \- 1 and i \+ d2 [ i ] < n and s [ i \- d2 [ i ] \- 1 ] == s [ i \+ d2 [ i ]]: d2 [ i ] += 1 ```   
---|---  
  
## Manacher 算法

这里我们将只描述算法中寻找所有奇数长度子回文串的情况，即只计算 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；寻找所有偶数长度子回文串的算法（即计算数组 𝑑2[]d2[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）将只需对奇数情况下的算法进行一些小修改．

为了快速计算，我们维护已找到的最靠右的子回文串的 **边界[𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)**（即具有最大 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 值的回文串，其中 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为该回文串左右边界的位置）．初始时，我们置 𝑙 =0l=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟 = −1r=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（ _-1_ 需区别于倒序索引位置，这里可为任意负数，仅为了循环初始时方便）．

### 过程

现在假设我们要对下一个 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算 𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而之前所有 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的值已计算完毕．我们将通过下列方式计算：

  * 如果 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位于当前子回文串之外，即 𝑖 >𝑟i>r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么我们调用朴素算法．

因此我们将连续地增加 𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，同时在每一步中检查当前的子串 [𝑖 −𝑑1[𝑖]…𝑖 +𝑑1[𝑖]][i−d1[i]…i+d1[i]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示半径长度，下同）是否为一个回文串．如果我们找到了第一处对应字符不同，又或者碰到了 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的边界，则算法停止．在两种情况下我们均已计算完 𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此后，仍需记得更新 (𝑙,𝑟)(l,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

  * 现在考虑 𝑖 ≤𝑟i≤r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况．我们将尝试从已计算过的 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值中获取一些信息．首先在子回文串 (𝑙,𝑟)(l,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中反转位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即我们得到 𝑗 =𝑙 +(𝑟 −𝑖)j=l+(r−i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．现在来考察值 𝑑1[𝑗]d1[j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为位置 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对称，我们 **几乎总是** 可以置 𝑑1[𝑖] =𝑑1[𝑗]d1[i]=d1[j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．该想法的图示如下（可认为以 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心的回文串被「拷贝」至以 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心的位置上）：

… palindrome⏞¯¯¯¯¯¯¯¯¯¯¯¯¯¯⏞¯¯¯¯¯¯¯¯¯¯¯¯¯¯⏞𝑠𝑙 … 𝑠𝑗−𝑑1[𝑗]+1 … 𝑠𝑗 … 𝑠𝑗+𝑑1[𝑗]−1⏟_____⏟_____⏟palindrome … 𝑠𝑖−𝑑1[𝑗]+1 … 𝑠𝑖 … 𝑠𝑖+𝑑1[𝑗]−1⏟_____⏟_____⏟palindrome … 𝑠𝑟 …… sl … sj−d1[j]+1 … sj … sj+d1[j]−1⏟palindrome … si−d1[j]+1 … si … si+d1[j]−1⏟palindrome … sr⏞palindrome …![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然而有一个 **棘手的情况** 需要被正确处理：当「内部」的回文串到达「外部」回文串的边界时，即 𝑗 −𝑑1[𝑗] +1 ≤𝑙j−d1[j]+1≤l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（或者等价的说，𝑖 +𝑑1[𝑗] −1 ≥𝑟i+d1[j]−1≥r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．因为在「外部」回文串范围以外的对称性没有保证，因此直接置 𝑑1[𝑖] =𝑑1[𝑗]d1[i]=d1[j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 将是不正确的：我们没有足够的信息来断言在位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的回文串具有同样的长度．

实际上，为了正确处理这种情况，我们应该「截断」回文串的长度，即置 𝑑1[𝑖] =𝑟 −𝑖 +1d1[i]=r−i+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．之后我们将运行朴素算法以尝试尽可能增加 𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的值．

该种情况的图示如下（以 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心的回文串已经被截断以落在「外部」回文串内）：

… palindrome⏞¯¯¯¯¯¯¯¯⏞¯¯¯¯¯¯¯¯⏞𝑠𝑙 … 𝑠𝑗 … 𝑠𝑗+(𝑗−𝑙)⏟___⏟___⏟palindrome … 𝑠𝑖−(𝑟−𝑖) … 𝑠𝑖 … 𝑠𝑟⏟___⏟___⏟palindrome ……………⏟try moving here… sl … sj … sj+(j−l)⏟palindrome … si−(r−i) … si … sr⏟palindrome⏞palindrome ……………⏟try moving here![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

该图示显示出，尽管以 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心的回文串可能更长，以致于超出「外部」回文串，但在位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们只能利用其完全落在「外部」回文串内的部分．然而位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的答案可能比这个值更大，因此接下来我们将运行朴素算法来尝试将其扩展至「外部」回文串之外，也即标识为 "try moving here" 的区域．

最后，仍有必要提醒的是，我们应当记得在计算完每个 𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后更新值 (𝑙,𝑟)(l,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

同时，再让我们重复一遍：计算偶数长度回文串数组 𝑑2[]d2[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的算法同上述计算奇数长度回文串数组 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的算法十分类似．

## Manacher 算法的复杂度

因为在计算一个特定位置的答案时我们总会运行朴素算法，所以一眼看去该算法的时间复杂度为线性的事实并不显然．

然而更仔细的分析显示出该算法具有线性复杂度．此处我们需要指出，[计算 Z 函数的算法](../z-func/) 和该算法较为类似，并同样具有线性时间复杂度．

实际上，注意到朴素算法的每次迭代均会使 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 增加 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以及 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在算法运行过程中从不减小．这两个观察告诉我们朴素算法总共会进行 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次迭代．

Manacher 算法的另一部分显然也是线性的，因此总复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## Manacher 算法的实现

### 分类讨论

为了计算 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们有以下代码：

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text vector < int > d1 ( n ); for ( int i = 0 , l = 0 , r = -1 ; i < n ; i ++ ) { int k = ( i > r ) ? 1 : min ( d1 [ l \+ r \- i ], r \- i \+ 1 ); while ( 0 <= i \- k && i \+ k < n && s [ i \- k ] == s [ i \+ k ]) { k ++ ; } d1 [ i ] = k \-- ; if ( i \+ k > r ) { l = i \- k ; r = i \+ k ; } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text d1 = [ 0 ] * n l , r = 0 , \- 1 for i in range ( 0 , n ): k = 1 if i > r else min ( d1 [ l \+ r \- i ], r \- i \+ 1 ) while 0 <= i \- k and i \+ k < n and s [ i \- k ] == s [ i \+ k ]: k += 1 d1 [ i ] = k k -= 1 if i \+ k > r : l = i \- k r = i \+ k ```   
---|---  
  
计算 𝑑2[]d2[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的代码十分类似，但是在算术表达式上有些许不同：

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text vector < int > d2 ( n ); for ( int i = 0 , l = 0 , r = -1 ; i < n ; i ++ ) { int k = ( i > r ) ? 0 : min ( d2 [ l \+ r \- i \+ 1 ], r \- i \+ 1 ); while ( 0 <= i \- k \- 1 && i \+ k < n && s [ i \- k \- 1 ] == s [ i \+ k ]) { k ++ ; } d2 [ i ] = k \-- ; if ( i \+ k > r ) { l = i \- k \- 1 ; r = i \+ k ; } } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text d2 = [ 0 ] * n l , r = 0 , \- 1 for i in range ( 0 , n ): k = 0 if i > r else min ( d2 [ l \+ r \- i \+ 1 ], r \- i \+ 1 ) while 0 <= i \- k \- 1 and i \+ k < n and s [ i \- k \- 1 ] == s [ i \+ k ]: k += 1 d2 [ i ] = k k -= 1 if i \+ k > r : l = i \- k \- 1 r = i \+ k ```   
---|---  
  
### 统一处理

虽然在讲解过程及上述实现中我们将 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑑2[]d2[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算分开考虑，但实际上可以通过一个技巧将二者的计算统一为 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的计算．

给定一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们在其 𝑛 +1n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个空中插入分隔符 ##![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从而构造一个长度为 2𝑛 +12n+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．举例来说，对于字符串 𝑠 =𝚊𝚋𝚊𝚋𝚊𝚋𝚌s=abababc![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其对应的 𝑠′ =#𝚊#𝚋#𝚊#𝚋#𝚊#𝚋#𝚌#s′=#a#b#a#b#a#b#c#![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

对于字母间的 ##![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其实际意义为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中对应的「空」．而两端的 ##![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则是为了实现的方便．

注意到，在对 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，对于一个位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所描述的最长的子回文串必定以 ##![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 结尾（若以字母结尾，由于字母两侧必定各有一个 ##![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此可向外扩展一个得到一个更长的）．因此，对于 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中一个以字母为中心的极大子回文串，设其长度为 𝑚 +1m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则其在 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中对应一个以相应字母为中心，长度为 2𝑚 +32m+3![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极大子回文串；而对于 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中一个以空为中心的极大子回文串，设其长度为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则其在 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中对应一个以相应表示空的 ##![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为中心，长度为 2𝑚 +12m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的极大子回文串（上述两种情况下的 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为偶数，但该性质成立与否并不影响结论）．综合以上观察及少许计算后易得，在 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，𝑑1[𝑖]d1[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示在 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中以对应位置为中心的极大子回文串的 **总长度加一** ．

上述结论建立了 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑑2[]d2[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 间的关系．

由于该统一处理本质上即求 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此在得到 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，代码同上节计算 𝑑1[]d1[]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的一样．

## 练习题目

  * [UVa #11475 "Extend to Palindrome"](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2470)
  * [「国家集训队」最长双回文串](https://www.luogu.com.cn/problem/P4555)
  * [CF1326D2. Labyrinth](https://codeforces.com/contest/1326/problem/D2)

**本页面主要译自博文[Нахождение всех подпалиндромов](http://e-maxx.ru/algo/palindromes_count) 与其英文翻译版 [Finding all sub-palindromes in 𝑂(𝑁)O(N)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://cp-algorithms.com/string/manacher.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/10 01:49:06，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/manacher.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/manacher.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Enter-tainer](https://github.com/Enter-tainer), [iamtwz](https://github.com/iamtwz), [Tiphereth-A](https://github.com/Tiphereth-A), [cesonic](https://github.com/cesonic), [Henry-ZHR](https://github.com/Henry-ZHR), [Xeonacid](https://github.com/Xeonacid), [abc1763613206](https://github.com/abc1763613206), [Alisahhh](https://github.com/Alisahhh), [aofall](https://github.com/aofall), [c-forrest](https://github.com/c-forrest), [CamberLoid](https://github.com/CamberLoid), [chenhongqiao](https://github.com/chenhongqiao), [CoelacanthusHex](https://github.com/CoelacanthusHex), [fseasy](https://github.com/fseasy), [gi-b716](https://github.com/gi-b716), [HeRaNO](https://github.com/HeRaNO), [ksyx](https://github.com/ksyx), [LeoJacob](https://github.com/LeoJacob), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [ouuan](https://github.com/ouuan), [pengxurui](https://github.com/pengxurui), [Persdre](https://github.com/Persdre), [sgt57](https://github.com/sgt57), [shawlleyw](https://github.com/shawlleyw), [shuzhouliu](https://github.com/shuzhouliu), [sshwy](https://github.com/sshwy), [StudyingFather](https://github.com/StudyingFather), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [Wsuika](https://github.com/Wsuika), [XPZhen](https://github.com/XPZhen), [YurianStormrage](https://github.com/YurianStormrage)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
