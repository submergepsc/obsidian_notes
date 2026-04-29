# Main–Lorentz 算法 - OI Wiki

- Source: https://oi-wiki.org/string/main-lorentz/

# Main–Lorentz 算法

## 重串

### 定义

给定一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们将一个字符串连续写两遍所产生的新字符串称为 **重串 (tandem repetition)** ．下文中，为了表述精准，我们将被重复的这个字符串称为原串．换言之，一个重串等价于一对下标 (𝑖,𝑗)(i,j)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其使得 𝑠[𝑖…𝑗]s[i…j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是两个相同字符串拼接而成的．

你的目标是找出给定的字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有的重串．或者，解决一个较为简单的问题：找到字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中任意重串或者最长的一个重串．

下文的算法由 Michael Main 和 Richard J. Lorentz 在 1982 年提出．

约定

下文所有的字符串下标从 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始．

下文中，记 ――𝑠s―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的反串．如 ―――𝚊𝚋𝚌 =𝚌𝚋𝚊abc―=cba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 解释

考虑字符串 𝚊𝚌𝚊𝚋𝚊𝚋𝚊𝚎𝚎acababaee![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这个字符串包括三个重串，分别是：

  * 𝑠[2…5] =𝚊𝚋𝚊𝚋s[2…5]=abab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑠[3…6] =𝚋𝚊𝚋𝚊s[3…6]=baba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑠[7…8] =𝚎𝚎s[7…8]=ee![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

下面是另一个例子，考虑字符串 𝚊𝚋𝚊𝚊𝚋𝚊abaaba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这个字符串只有两个重串：

  * 𝑠[0…5] =𝚊𝚋𝚊𝚊𝚋𝚊s[0…5]=abaaba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑠[2…3] =𝚊𝚊s[2…3]=aa![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 重串的个数

一个长度为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串可能有高达 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个重串，一个显然的例子就是 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字母全部相同的字符串，这种情况下，只要其子串长度为偶数，这个子串就是重串．多数情况下，一个周期比较小的周期字符串会有很多重串．

但这并不影响我们在 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内计算出重串数量．因为这个算法通过某种压缩形式来表达一个重串，使得我们可以将多个重串压缩为一个．

这里有一些关于重串数量的有趣结论：

  * 如果一个重串的原串不是重串，则我们称这个重串为 **本原重串 (primitive repetition)** ．可以证明，本原重串最多有 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．
  * 如果我们把一个重串用 Crochemore 三元组 (𝑖,𝑝,𝑟)(i,p,r)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进行压缩，其中 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是重串的起始位置，𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是该重串某个循环节的长度（注意不是原串长度！），𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为这个循环节重复的次数．则某字符串的所有重串可以被 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 Crochemore 三元组表示．
  * Fibonacci 字符串定义如下：

𝑡0=𝑎,𝑡1=𝑏,𝑡𝑖=𝑡𝑖−1+𝑡𝑖−2,t0=a,t1=b,ti=ti−1+ti−2,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以发现 Fibonacci 字符串具有高度的周期性．对于长度为 𝑓𝑖fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Fibonacci 字符串 𝑡𝑖ti![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即使用 Crochemore 三元组压缩，也有 𝑂(𝑓𝑖log⁡𝑓𝑖)O(filog⁡fi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个三元组．其本原重串的数量也有 𝑂(𝑓𝑖log⁡𝑓𝑖)O(filog⁡fi)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．

## Main–Lorentz 算法

### 解释

Main–Lorentz 算法的核心思想是 **分治** ．

这个算法将字符串分为左、右两部分，首先计算完全处于字符串左部（或右部）的重串数量，然后计算起始位置在左部，终止在右部的重串数量．（下文中，我们将这种重串称为 **交叉重串** ）

计算交叉重串的数量是 Main–Lorentz 算法的关键点，我们将在下文详细探讨．

### 过程

#### 寻找交叉重串

我们记某字符串的左部为 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，右部为 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．则 𝑠 =𝑢 +𝑣s=u+v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑢,𝑣u,v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的长度大约等于 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 长度的一半．

对于任意一个重串，我们考虑其中间字符．此处我们将一个重串右半边的第一个字符称为其中间字符，换言之，若 𝑠[𝑖...𝑗]s[i...j]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为重串，则其中间字符为 𝑠[(𝑖 +𝑗 +1)/2]s[(i+j+1)/2]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果一个重串的中间字符在 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中，则称这个重串 **左偏 (left)** ，反之则称其 **右偏 (right)** ．

接下来，我们将会探讨如何找到所有的左偏重串．

我们记一个左边重串的长度为 2𝑙2l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考虑该重串第一个落入 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符（即 𝑠[|𝑢|]s[|u|]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），这个字符一定与 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的某个字符 𝑢[𝑐𝑛𝑡𝑟]u[cntr]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一致．

我们考虑固定 𝑐𝑛𝑡𝑟cntr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，并找到所有符合条件的重串．举个例子：对于字符串 𝚌 𝚊𝑐𝑛𝑡𝑟 𝚌 | 𝚊 𝚍 𝚊cacntrc|ada![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（这个 ||![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是用于分辨左右两部分的），固定 𝑐𝑛𝑡𝑟 =1cntr=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则我们可以发现重串 𝚌𝚊𝚌𝚊caca![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 符合要求．

显然，我们一旦固定了 𝑐𝑛𝑡𝑟cntr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那我们同时也固定了 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．我们一旦知道如何找到所有重串，我们就可以从 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 |𝑢| −1|u|−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 枚举 𝑐𝑛𝑡𝑟cntr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值，然后找到所有符合条件的重串．

#### 左偏重串的判定

即使固定 𝑐𝑛𝑡𝑟cntr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 后，仍然可能会有多个符合条件的重串，我们怎么找到所有符合条件的重串呢？

我们再来举一个例子，对于字符串 𝚊𝚋𝚌𝚊𝚋𝚌𝚊𝚌abcabcac![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的重串 𝑙1⏞𝚊𝑙2⏞𝚋𝑐𝑛𝑡𝑟𝚌𝑙1⏞𝚊 | 𝑙2⏞𝚋𝚌a⏞l1bcntrc⏞l2a⏞l1|bc⏞l2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们记 𝑙1l1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为该重串的首字符到 𝑠[𝑐𝑛𝑡𝑟 −1]s[cntr−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 所组成的子串的长度，记 𝑙2l2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑠[𝑐𝑛𝑡𝑟]s[cntr]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到该重串左边原串的末字符所组成的子串的长度．

于是，我们可以给出某个长度为 2𝑙 =2(𝑙1 +𝑙2) =2(|𝑢| −𝑐𝑛𝑡𝑟)2l=2(l1+l2)=2(|u|−cntr)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子串是重串的 **充分必要条件** ：

记 𝑘1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为满足 𝑢[𝑐𝑛𝑡𝑟 −𝑘1…𝑐𝑛𝑡𝑟 −1] =𝑢[|𝑢| −𝑘1…|𝑢| −1]u[cntr−k1…cntr−1]=u[|u|−k1…|u|−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大整数，记 𝑘2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为满足 𝑢[𝑐𝑛𝑡𝑟…𝑐𝑛𝑡𝑟 +𝑘2 −1] =𝑣[0…𝑘2 −1]u[cntr…cntr+k2−1]=v[0…k2−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大整数．则对于任意满足 𝑙1 ≤𝑘1l1≤k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑙2 ≤𝑘2l2≤k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二元组 (𝑙1,𝑙2)(l1,l2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们都能恰好找到一个与之对应的重串．

总结一下，即有：

  * 固定一个 𝑐𝑛𝑡𝑟cntr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 那么我们此时要找的重串长度均为 2𝑙 =2(|𝑢| −𝑐𝑛𝑡𝑟)2l=2(|u|−cntr)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．此时可能仍有多个符合条件的重串，取决于 𝑙1l1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑙2l2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的取值．
  * 计算上文提到的 𝑘1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑘2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 则所有符合条件的重串符合条件：

𝑙1+𝑙2=𝑙=|𝑢|−𝑐𝑛𝑡𝑟𝑙1≤𝑘1,𝑙2≤𝑘2.l1+l2=l=|u|−cntrl1≤k1,l2≤k2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

接下来，只需要考虑如何快速算出 𝑘1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑘2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了．借助 [Z 函数](../z-func/)，我们可以 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 计算它们：

  * 计算 𝑘1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：只需计算 ――𝑢u―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Z 函数即可．
  * 计算 𝑘2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)：只需计算 𝑣 +# +𝑢v+#+u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Z 函数即可，其中 ##![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中均没有的字符．

#### 右偏重串

计算右偏重串的方法与计算左偏重串的方法几乎一致．考虑该重串第一个落入 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符（即 𝑠[|𝑢| −1]s[|u|−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），则其一定与 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的某个字符一致，记这个字符在 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的位置为 𝑐𝑛𝑡𝑟cntr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

令 𝑘1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为满足 𝑣[𝑐𝑛𝑡𝑟 −𝑘1 +1…𝑐𝑛𝑡𝑟] =𝑢[|𝑢| −𝑘1…|𝑢| −1]v[cntr−k1+1…cntr]=u[|u|−k1…|u|−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大整数，𝑘2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为满足 𝑣[𝑐𝑛𝑡𝑟 +1…𝑐𝑛𝑡𝑟 +𝑘2] =𝑣[0…𝑘2 −1]v[cntr+1…cntr+k2]=v[0…k2−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大整数．则我们可以分别通过计算 ――𝑢 +# +――𝑣u―+#+v―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑣v![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Z 函数来得出 𝑘1k1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑘2k2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

枚举 𝑐𝑛𝑡𝑟cntr![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，用相仿的方法寻找右偏重串即可．

### 实现

Main–Lorentz 算法以四元组 (𝑐𝑛𝑡𝑟,𝑙,𝑘1,𝑘2)(cntr,l,k1,k2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式给出所有重串．如果你只需要计算重串的数量，或者只需要找到最长的一个重串，这个四元组给的信息是足够的．由 [主定理](../../basic/complexity/#主定理-master-theorem) 可得，Main–Lorentz 算法的时间复杂度为 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

请注意，如果你想通过这些四元组来找到所有重串的起始位置与终止位置，则最坏时间复杂度会达到 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．我们在下面的程序中实现了这一点，将所有重串的起始位置与终止位置存于 `repetitions` 中．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 ``` |  ```text vector < int > z_function ( string const & s ) { int n = s . size (); vector < int > z ( n ); for ( int i = 1 , l = 0 , r = 0 ; i < n ; i ++ ) { if ( i <= r ) z [ i ] = min ( r \- i \+ 1 , z [ i \- l ]); while ( i \+ z [ i ] < n && s [ z [ i ]] == s [ i \+ z [ i ]]) z [ i ] ++ ; if ( i \+ z [ i ] \- 1 > r ) { l = i ; r = i \+ z [ i ] \- 1 ; } } return z ; } int get_z ( vector < int > const & z , int i ) { if ( 0 <= i && i < ( int ) z . size ()) return z [ i ]; else return 0 ; } vector < pair < int , int >> repetitions ; void convert_to_repetitions ( int shift , bool left , int cntr , int l , int k1 , int k2 ) { for ( int l1 = max ( 1 , l \- k2 ); l1 <= min ( l , k1 ); l1 ++ ) { if ( left && l1 == l ) break ; int l2 = l \- l1 ; int pos = shift \+ ( left ? cntr \- l1 : cntr \- l \- l1 \+ 1 ); repetitions . emplace_back ( pos , pos \+ 2 * l \- 1 ); } } void find_repetitions ( string s , int shift = 0 ) { int n = s . size (); if ( n == 1 ) return ; int nu = n / 2 ; int nv = n \- nu ; string u = s . substr ( 0 , nu ); string v = s . substr ( nu ); string ru ( u . rbegin (), u . rend ()); string rv ( v . rbegin (), v . rend ()); find_repetitions ( u , shift ); find_repetitions ( v , shift \+ nu ); vector < int > z1 = z_function ( ru ); vector < int > z2 = z_function ( v \+ '#' \+ u ); vector < int > z3 = z_function ( ru \+ '#' \+ rv ); vector < int > z4 = z_function ( v ); for ( int cntr = 0 ; cntr < n ; cntr ++ ) { int l , k1 , k2 ; if ( cntr < nu ) { l = nu \- cntr ; k1 = get_z ( z1 , nu \- cntr ); k2 = get_z ( z2 , nv \+ 1 \+ cntr ); } else { l = cntr \- nu \+ 1 ; k1 = get_z ( z3 , nu \+ 1 \+ nv \- 1 \- ( cntr \- nu )); k2 = get_z ( z4 , ( cntr \- nu ) \+ 1 ); } if ( k1 \+ k2 >= l ) convert_to_repetitions ( shift , cntr < nu , cntr , l , k1 , k2 ); } } ```   
---|---  
  
**本页面主要译自博文[Поиск всех тандемных повторов в строке. Алгоритм Мейна-Лоренца](http://e-maxx.ru/algo/string_tandems) 与其英文翻译版 [Finding repetitions](https://cp-algorithms.com/string/main_lorentz.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/main-lorentz.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/main-lorentz.md "edit.link.title")  
>  __本页面贡献者：[Tiphereth-A](https://github.com/Tiphereth-A), [billchenchina](https://github.com/billchenchina), [Enter-tainer](https://github.com/Enter-tainer), [fsy-juruo](https://github.com/fsy-juruo), [HeRaNO](https://github.com/HeRaNO), [iamtwz](https://github.com/iamtwz), [ouuan](https://github.com/ouuan)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
