# 字符串哈希 - OI Wiki

- Source: https://oi-wiki.org/string/hash/

# 字符串哈希

## 定义

我们定义一个把字符串映射到整数的函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这个 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为是 Hash 函数．

我们希望这个函数 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以方便地帮我们判断两个字符串是否相等．

## Hash 的思想

Hash 的核心思想在于，将输入映射到一个值域较小、可以方便比较的范围．

Warning

这里的「值域较小」在不同情况下意义不同．

在 [哈希表](../../ds/hash/) 中，值域需要小到能够接受线性的空间与时间复杂度．

在字符串哈希中，值域需要小到能够快速比较（109109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、10181018![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是可以快速比较的）．

同时，为了降低哈希冲突率，值域也不能太小．

## 性质

具体来说，哈希函数最重要的性质可以概括为下面两条：

  1. 在 Hash 函数值不一样的时候，两个字符串一定不一样；

  2. 在 Hash 函数值一样的时候，两个字符串不一定一样（但有大概率一样，且我们当然希望它们总是一样的）．

我们将 Hash 函数值一样但原字符串不一样的现象称为哈希碰撞．

## 解释

我们需要关注的是什么？

时间复杂度和 Hash 的准确率．

通常我们采用的是多项式 Hash 的方法，对于一个长度为 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来说，我们可以这样定义多项式 Hash 函数：𝑓(𝑠) =∑𝑙𝑖=1𝑠[𝑖] ×𝑏𝑙−𝑖(mod𝑀)f(s)=∑i=1ls[i]×bl−i(modM)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．例如，对于字符串 𝑥𝑦𝑧xyz![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其哈希函数值为 𝑥𝑏2 +𝑦𝑏 +𝑧xb2+yb+z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

特别要说明的是，也有很多人使用的是另一种 Hash 函数的定义，即 𝑓(𝑠) =∑𝑙𝑖=1𝑠[𝑖] ×𝑏𝑖−1(mod𝑀)f(s)=∑i=1ls[i]×bi−1(modM)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这种定义下，同样的字符串 𝑥𝑦𝑧xyz![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的哈希值就变为了 𝑥 +𝑦𝑏 +𝑧𝑏2x+yb+zb2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 了．

显然，上面这两种哈希函数的定义函数都是可行的，但二者在之后会讲到的计算子串哈希值时所用的计算式是不同的，因此千万注意 **不要弄混了这两种不同的 Hash 方式** ．

由于前者的 Hash 定义计算更简便、使用人数更多、且可以类比为一个 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制数来帮助理解，所以本文下面所将要讨论的都是使用 𝑓(𝑠) =∑𝑙𝑖=1𝑠[𝑖] ×𝑏𝑙−𝑖(mod𝑀)f(s)=∑i=1ls[i]×bl−i(modM)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来定义的 Hash 函数．

还有，有时为了方便和扩大模数，我们在 C++ 中我们会使用 `unsigned long long` 来定义 Hash 函数的结果．由于 C++ 的特性，我们相当于把模数 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 定为 264264![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，也是一个不错的选择．

准确率会在后面讨论．

## Hash 的错误率分析

### Hash 冲突

Hash 冲突是指两个不同的字符串映射到相同的 Hash 值．

我们设 Hash 的取值空间（所有可能出现的字符串的数量）为 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，计算次数（要计算的字符串数量）为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

则 Hash 冲突的概率为：

𝑝(𝑛,𝑑)=1−𝑑!𝑑𝑛(𝑑−𝑛)!≈1−exp⁡(−𝑛(𝑛−1)2𝑑)p(n,d)=1−d!dn(d−n)!≈1−exp⁡(−n(n−1)2d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)证明

当 Hash 中每个值生成概率相同时，Hash 不冲突的概率为：

――𝑝(𝑛,𝑑)=1⋅(1−1𝑑)⋅(1−2𝑑)⋯(1−𝑛−1𝑑)p―(n,d)=1⋅(1−1d)⋅(1−2d)⋯(1−n−1d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

化简得到：

――𝑝(𝑛,𝑑)=𝑑𝑑⋅𝑑−1𝑑⋅𝑑−2𝑑⋯𝑑−𝑛+1𝑑=𝑑⋅(𝑑−1)⋅(𝑑−2)⋯(𝑑−𝑛+1)𝑑𝑛=𝑑!𝑑𝑛(𝑑−𝑛)!p―(n,d)=dd⋅d−1d⋅d−2d⋯d−n+1d=d⋅(d−1)⋅(d−2)⋯(d−n+1)dn=d!dn(d−n)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则 Hash 冲突的概率为：

𝑝(𝑛,𝑑)=1−𝑑!𝑑𝑛(𝑑−𝑛)!p(n,d)=1−d!dn(d−n)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这个公式还是太复杂了，我们进一步化简．

根据泰勒公式：

exp⁡(𝑥)=∞∑𝑘=0𝑥𝑘𝑘!=1+𝑥+𝑥22+𝑥36+𝑥424+⋯exp⁡(x)=∑k=0∞xkk!=1+x+x22+x36+x424+⋯![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

当 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为一个极小值时，exp⁡(𝑥)exp⁡(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 趋近于 1 +𝑥1+x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

将它带入 Hash 不冲突的原始公式：

――𝑝(𝑛,𝑑)≈1⋅exp⁡(−1𝑑)⋅exp⁡(−2𝑑)⋯exp⁡(−𝑛−1𝑑)p―(n,d)≈1⋅exp⁡(−1d)⋅exp⁡(−2d)⋯exp⁡(−n−1d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

化简：

――𝑝(𝑛,𝑑)≈exp⁡(−1𝑑−2𝑑−⋯−𝑛−1𝑑)=exp⁡(−𝑛(𝑛−1)2𝑑)p―(n,d)≈exp⁡(−1d−2d−⋯−n−1d)=exp⁡(−n(n−1)2d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则 Hash 冲突的概率为：

𝑝(𝑛,𝑑)≈1−exp⁡(−𝑛(𝑛−1)2𝑑)p(n,d)≈1−exp⁡(−n(n−1)2d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 卡大模数 Hash

注意到这个公式：

𝑝(𝑛,𝑑)≈1−exp⁡(−𝑛(𝑛−1)2𝑑)p(n,d)≈1−exp⁡(−n(n−1)2d)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为了卡掉 Hash，我们要满足以下条件：

  1. 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 要大于模数．
  2. 1 −𝑝(𝑑,𝑛)1−p(d,n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 要尽量小．

举个例子：

若字符集为 **大小写字母和数字** ，模数为 109 +7109+7![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时：

log62⁡109 +7 ≈6log62⁡109+7≈6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝑝(106,626) ≈0.9p(106,626)≈0.9![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

所以对于这个范围，我们随机生成 106106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个长度为 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串，它们 Hash 值相同的概率高达 90%90%![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 卡自然溢出 Hash

这种 Hash 由于模数太大，用上面的方法卡不了，所以我们需要另一种方法．

首先，这种 Hash 是形如 𝑓(𝑠) =∑𝑙𝑖=1𝑠[𝑖] ×𝑏𝑙−𝑖f(s)=∑i=1ls[i]×bl−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们根据 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来分类讨论．

#### b 为偶数

此时 𝑓(𝑠) =𝑠1 ⋅𝑏𝑙 +𝑠2 ⋅𝑏𝑙−1 +⋯ +𝑠𝑙 ⋅𝑏(mod𝑀)f(s)=s1⋅bl+s2⋅bl−1+⋯+sl⋅b(modM)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 264264![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

容易发现若 𝑙 ≥64l≥64![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑠𝑖 ⋅𝑏𝑙 ≡0(mod𝑀)si⋅bl≡0(modM)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

所以我们只要构造形如：

`aaa...a`

`baa...a`

且长度大于 6464![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串就能冲突．

#### b 为奇数

定义 !𝑠𝑖!si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为把 𝑠𝑖si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有字符反转．

例：

𝑠𝑖 =𝑎𝑏𝑎𝑎𝑏si=abaab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

!𝑠𝑖 =𝑏𝑎𝑏𝑏𝑎!si=babba![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即把 `a` 变成 `b`，把 `b` 变成 `a`．

再定义 ℎ𝑎𝑠ℎ𝑖hashi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑠𝑖si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Hash 值，!ℎ𝑎𝑠ℎ𝑖!hashi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 !𝑠𝑖!si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 Hash 值．

不断构造 𝑠𝑖 =𝑠𝑖−1 +!𝑠𝑖−1si=si−1+!si−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

𝑠12s12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 !𝑠12!s12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就是我们要的两个字符串．

推导

首先，有：

ℎ𝑎𝑠ℎ𝑖=ℎ𝑎𝑠ℎ𝑖−1⋅𝑏𝑎𝑠𝑒2𝑖−2+!ℎ𝑎𝑠ℎ𝑖−1!ℎ𝑎𝑠ℎ𝑖=!ℎ𝑎𝑠ℎ𝑖−1⋅𝑏𝑎𝑠𝑒2𝑖−2+ℎ𝑎𝑠ℎ𝑖−1hashi=hashi−1⋅base2i−2+!hashi−1!hashi=!hashi−1⋅base2i−2+hashi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

尝试相减：

ℎ𝑎𝑠ℎ𝑖−!ℎ𝑎𝑠ℎ𝑖= ℎ𝑎𝑠ℎ𝑖−1⋅𝑏𝑎𝑠𝑒2𝑖−2+!ℎ𝑎𝑠ℎ𝑖−1−(!ℎ𝑎𝑠ℎ𝑖−1⋅𝑏𝑎𝑠𝑒2𝑖−2+ℎ𝑎𝑠ℎ𝑖−1)= (ℎ𝑎𝑠ℎ𝑖−1−!ℎ𝑎𝑠ℎ𝑖−1)⋅(𝑏𝑎𝑠𝑒2𝑖−2−1)hashi−!hashi= hashi−1⋅base2i−2+!hashi−1−(!hashi−1⋅base2i−2+hashi−1)= (hashi−1−!hashi−1)⋅(base2i−2−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

发现出现了 2𝑖2i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是原式太复杂，尝试换元：

设：

𝑓𝑖=ℎ𝑎𝑠ℎ𝑖−!ℎ𝑎𝑠ℎ𝑖𝑔𝑖=𝑏𝑎𝑠𝑒2𝑖−2−1fi=hashi−!hashigi=base2i−2−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据原式得：

𝑓𝑖=𝑓𝑖−1⋅𝑔𝑖=𝑓1⋅𝑔1⋅𝑔2⋯𝑔𝑖−1fi=fi−1⋅gi=f1⋅g1⋅g2⋯gi−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因为 𝑏𝑎𝑠𝑒2𝑖−2base2i−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定是奇数，所以 𝑔𝑖gi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定是偶数．

所以：

2𝑖−1|𝑓𝑖2i−1|fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

但这样太大了，𝑖 −1 ≥64i−1≥64![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 才能卡掉，继续化简：

𝑔𝑖=𝑏𝑎𝑠𝑒2𝑖−2−1=(𝑏𝑎𝑠𝑒2𝑖−3−1)⋅(𝑏𝑎𝑠𝑒2𝑖−3+1)gi=base2i−2−1=(base2i−3−1)⋅(base2i−3+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即 𝑔𝑖gi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 𝑔𝑖−1 ⋅𝑐 (𝑐 ≡0(mod2))gi−1⋅c (c≡0(mod2))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式．

所以 2|𝑠12|s1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，4|𝑠24|s2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，……，即

2𝑖|𝑔𝑖21⋅22⋅23⋯2𝑖−1|𝑓𝑖2𝑖(𝑖−1)/2|𝑓𝑖2i|gi21⋅22⋅23⋯2i−1|fi2i(i−1)/2|fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

即当 𝑖 =12i=12![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时就可以使 264|ℎ𝑎𝑠ℎ𝑖 −!ℎ𝑎𝑠ℎ𝑖264|hashi−!hashi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 达到要求．

### 例题

[例题：BZOJ 3097 Hash Killer I](https://hydro.ac/p/bzoj-P3097)

给定一个用 **自然溢出** 实现的 Hash，要求构造一个字符串来卡掉它．

[例题：BZOJ 3097 Hash Killer II](https://hydro.ac/p/bzoj-P3098)

给定一个用 **大模数** 实现的 Hash，要求构造一个字符串来卡掉它．

[例题：洛谷 U461211 字符串 Hash（数据加强）](https://www.luogu.com.cn/problem/U461211)

给定 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符串，判断不同的字符串有多少个．

## Hash 的改进

### 多值 Hash

看了上面这么多的卡法，当然也有解决办法．

多值 Hash，就是有多个 Hash 函数，每个 Hash 函数的模数不一样，这样就能解决 Hash 冲突的问题．

判断时只要有其中一个的 Hash 值不同，就认为两个字符串不同，若 Hash 值都相同，则认为两个字符串相同．

一般来说，双值 Hash 就够用了．

### 多次询问子串哈希

单次计算一个字符串的哈希值复杂度是 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为串长，与暴力匹配没有区别，如果需要多次询问一个字符串的子串的哈希值，每次重新计算效率非常低下．

一般采取的方法是对整个字符串先预处理出每个前缀的哈希值，将哈希值看成一个 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 进制的数对 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取模的结果，这样的话每次就能快速求出子串的哈希了：

令 𝑓𝑖(𝑠)fi(s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑓(𝑠[1..𝑖])f(s[1..i])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即原串长度为 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的前缀的哈希值，那么按照定义有 𝑓𝑖(𝑠) =𝑠[1] ⋅𝑏𝑖−1 +𝑠[2] ⋅𝑏𝑖−2 +⋯ +𝑠[𝑖 −1] ⋅𝑏 +𝑠[𝑖]fi(s)=s[1]⋅bi−1+s[2]⋅bi−2+⋯+s[i−1]⋅b+s[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

现在，我们想要用类似前缀和的方式快速求出 𝑓(𝑠[𝑙..𝑟])f(s[l..r])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，按照定义有字符串 𝑠[𝑙..𝑟]s[l..r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的哈希值为 𝑓(𝑠[𝑙..𝑟]) =𝑠[𝑙] ⋅𝑏𝑟−𝑙 +𝑠[𝑙 +1] ⋅𝑏𝑟−𝑙−1 +⋯ +𝑠[𝑟 −1] ⋅𝑏 +𝑠[𝑟]f(s[l..r])=s[l]⋅br−l+s[l+1]⋅br−l−1+⋯+s[r−1]⋅b+s[r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对比观察上述两个式子，我们发现 𝑓(𝑠[𝑙..𝑟]) =𝑓𝑟(𝑠) −𝑓𝑙−1(𝑠) ×𝑏𝑟−𝑙+1f(s[l..r])=fr(s)−fl−1(s)×br−l+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立（可以手动代入验证一下），因此我们用这个式子就可以快速得到子串的哈希值．其中 𝑏𝑟−𝑙+1br−l+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的预处理出来然后 𝑂(1)O(1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的回答每次询问（当然也可以快速幂 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的回答每次询问）．

## 实现

### 模数 Hash：

注：效率较低，实际使用中不推荐．

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` |  ```text using std :: string ; constexpr int M = 1e9 \+ 7 ; constexpr int B = 233 ; using ll = long long ; int get_hash ( const string & s ) { int res = 0 ; for ( int i = 0 ; i < s . size (); ++ i ) { res = (( ll ) res * B \+ s [ i ]) % M ; } return res ; } bool cmp ( const string & s , const string & t ) { return get_hash ( s ) == get_hash ( t ); } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text M = int ( 1e9 \+ 7 ) B = 233 def get_hash ( s ): res = 0 for char in s : res = ( res * B \+ ord ( char )) % M return res def cmp ( s , t ): return get_hash ( s ) == get_hash ( t ) ```   
---|---  
  
### 双值 Hash：

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` |  ```text using ull = unsigned long long ; ull base = 131 ; ull mod1 = 212370440130137957 , mod2 = 1e9 \+ 7 ; ull get_hash1 ( std :: string s ) { int len = s . size (); ull ans = 0 ; for ( int i = 0 ; i < len ; i ++ ) ans = ( ans * base \+ ( ull ) s [ i ]) % mod1 ; return ans ; } ull get_hash2 ( std :: string s ) { int len = s . size (); ull ans = 0 ; for ( int i = 0 ; i < len ; i ++ ) ans = ( ans * base \+ ( ull ) s [ i ]) % mod2 ; return ans ; } bool cmp ( const std :: string s , const std :: string t ) { bool f1 = get_hash1 ( s ) != get_hash1 ( t ); bool f2 = get_hash2 ( s ) != get_hash2 ( t ); return f1 || f2 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text def get_hash1 ( s : str ) -> int : base = 131 mod1 = 212370440130137957 ans = 0 for char in s : ans = ( ans * base \+ ord ( char )) % mod1 return ans def get_hash2 ( s : str ) -> int : base = 131 mod2 = 1000000007 ans = 0 for char in s : ans = ( ans * base \+ ord ( char )) % mod2 return ans def cmp ( s : str , t : str ) -> bool : f1 = get_hash1 ( s ) != get_hash1 ( t ) f2 = get_hash2 ( s ) != get_hash2 ( t ) return f1 or f2 ```   
---|---  
  
## Hash 的应用

### 字符串匹配

求出模式串的哈希值后，求出文本串每个长度为模式串长度的子串的哈希值，分别与模式串的哈希值比较即可．

### 允许 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次失配的字符串匹配

问题：给定长为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的源串 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，以及长度为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的模式串 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要求查找源串中有多少子串与模式串匹配．𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 匹配，当且仅当 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑠s![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 长度相同，且最多有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个位置字符不同．其中 1 ≤𝑛,𝑚 ≤1061≤n,m≤106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，0 ≤𝑘 ≤50≤k≤5![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这道题无法使用 KMP 解决，但是可以通过哈希 + 二分来解决．

枚举所有可能匹配的子串，假设现在枚举的子串为 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，通过哈希 + 二分可以快速找到 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 第一个不同的位置．之后将 𝑠′s′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在这个失配位置及之前的部分删除掉，继续查找下一个失配位置．这样的过程最多发生 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次．

总的时间复杂度为 𝑂(𝑚 +𝑘𝑛log2⁡𝑚)O(m+knlog2⁡m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 最长回文子串

二分答案，判断是否可行时枚举回文中心（对称轴），哈希判断两侧是否相等．需要分别预处理正着和倒着的哈希值．时间复杂度 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这个问题可以使用 [manacher 算法](../manacher/) 在 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间内解决．

通过哈希同样可以 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 解决这个问题，具体方法就是记 𝑅𝑖Ri![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示以 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为结尾的最长回文的长度，那么答案就是 max𝑛𝑖=1𝑅𝑖maxi=1nRi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考虑到 𝑅𝑖 ≤𝑅𝑖−1 +2Ri≤Ri−1+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，因此我们只需要暴力从 𝑅𝑖−1 +2Ri−1+2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始递减，直到找到第一个回文即可．记变量 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示当前枚举的 𝑅𝑖Ri![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，初始时为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑧z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 在每次 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 增大的时候都会增大 22![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，之后每次暴力循环都会减少 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故暴力循环最多发生 2𝑛2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次，总的时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 最长公共子字符串

问题：给定 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个总长不超过 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非空字符串，查找所有字符串的最长公共子字符串，如果有多个，任意输出其中一个．其中 1 ≤𝑚,𝑛 ≤1061≤m,n≤106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

很显然如果存在长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最长公共子字符串，那么 𝑘 −1k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的公共子字符串也必定存在．因此我们可以二分最长公共子字符串的长度．假设现在的长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，`check(k)` 的逻辑为我们将所有所有字符串的长度为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子串分别进行哈希，将哈希值放入 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个哈希表中存储．之后求交集即可．

时间复杂度为 𝑂(𝑚 +𝑛log⁡𝑛)O(m+nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 确定字符串中不同子字符串的数量

问题：给定长为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串，仅由小写英文字母组成，查找该字符串中不同子串的数量．

为了解决这个问题，我们遍历了所有长度为 𝑙 =1,⋯,𝑛l=1,⋯,n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的子串．对于每个长度为 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们将其 Hash 值乘以相同的 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的幂次方，并存入一个数组中．数组中不同元素的数量等于字符串中长度不同的子串的数量，并此数字将添加到最终答案中．

为了方便起见，我们将使用 ℎ[𝑖]h[i]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 作为 Hash 的前缀字符，并定义 ℎ[0] =0h[0]=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` |  ```text int count_unique_substrings ( string const & s ) { int n = s . size (); constexpr static int b = 31 ; constexpr static int m = 1e9 \+ 9 ; vector < long long > b_pow ( n ); b_pow [ 0 ] = 1 ; for ( int i = 1 ; i < n ; i ++ ) b_pow [ i ] = ( b_pow [ i \- 1 ] * b ) % m ; vector < long long > h ( n \+ 1 , 0 ); for ( int i = 0 ; i < n ; i ++ ) h [ i \+ 1 ] = ( h [ i ] \+ ( s [ i ] \- 'a' \+ 1 ) * b_pow [ i ]) % m ; int cnt = 0 ; for ( int l = 1 ; l <= n ; l ++ ) { set < long long > hs ; for ( int i = 0 ; i <= n \- l ; i ++ ) { long long cur_h = ( h [ i \+ l ] \+ m \- h [ i ]) % m ; cur_h = ( cur_h * b_pow [ n \- i \- 1 ]) % m ; hs . insert ( cur_h ); } cnt += hs . size (); } return cnt ; } ```   
---|---  
  
### 例题

[CF1200E Compress Words](http://codeforces.com/contest/1200/problem/E)

给你若干个字符串，答案串初始为空．第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 步将第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符串加到答案串的后面，但是尽量地去掉重复部分（即去掉一个最长的、是原答案串的后缀、也是第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个串的前缀的字符串），求最后得到的字符串．

字符串个数不超过 105105![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，总长不超过 106106![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

题解

每次需要求最长的、是原答案串的后缀、也是第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个串的前缀的字符串．枚举这个串的长度，哈希比较即可．

当然，这道题也可以使用 [KMP 算法](../kmp/) 解决．

参考代码

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 ``` |  ```text #include <cassert> #include <cstring> #include <iostream> #include <vector> using namespace std ; constexpr int L = 1e6 \+ 5 ; constexpr int HASH_CNT = 2 ; int hashBase [ HASH_CNT ] = { 29 , 31 }; int hashMod [ HASH_CNT ] = { int ( 1e9 \+ 9 ), 998244353 }; struct StringWithHash { char s [ L ]; int ls ; int hsh [ HASH_CNT ][ L ]; int pwMod [ HASH_CNT ][ L ]; void init () { // 初始化 ls = 0 ; for ( int i = 0 ; i < HASH_CNT ; ++ i ) { hsh [ i ][ 0 ] = 0 ; pwMod [ i ][ 0 ] = 1 ; } } StringWithHash () { init (); } void extend ( char c ) { s [ ++ ls ] = c ; // 记录字符数和每一个字符 for ( int i = 0 ; i < HASH_CNT ; ++ i ) { // 双哈希的预处理 pwMod [ i ][ ls ] = 1l l * pwMod [ i ][ ls \- 1 ] * hashBase [ i ] % hashMod [ i ]; // 得到b^ls hsh [ i ][ ls ] = ( 1l l * hsh [ i ][ ls \- 1 ] * hashBase [ i ] \+ c ) % hashMod [ i ]; } } vector < int > getHash ( int l , int r ) { // 得到哈希值 vector < int > res ( HASH_CNT , 0 ); for ( int i = 0 ; i < HASH_CNT ; ++ i ) { int t = ( hsh [ i ][ r ] \- 1l l * hsh [ i ][ l \- 1 ] * pwMod [ i ][ r \- l \+ 1 ]) % hashMod [ i ]; t = ( t \+ hashMod [ i ]) % hashMod [ i ]; res [ i ] = t ; } return res ; } }; bool equal ( const vector < int > & h1 , const vector < int > & h2 ) { assert ( h1 . size () == h2 . size ()); for ( unsigned i = 0 ; i < h1 . size (); i ++ ) if ( h1 [ i ] != h2 [ i ]) return false ; return true ; } int n ; StringWithHash s , t ; char str [ L ]; void work () { int len = strlen ( str ); // 取字符串长度 t . init (); for ( int j = 0 ; j < len ; ++ j ) t . extend ( str [ j ]); int d = 0 ; for ( int j = min ( len , s . ls ); j >= 1 ; \-- j ) { if ( equal ( t . getHash ( 1 , j ), s . getHash ( s . ls \- j \+ 1 , s . ls ))) { // 比较哈希值 d = j ; break ; } } for ( int j = d ; j < len ; ++ j ) s . extend ( str [ j ]); // 更新答案数组 } int main () { cin . tie ( nullptr ) -> sync_with_stdio ( false ); cin >> n ; for ( int i = 1 ; i <= n ; ++ i ) { cin >> str ; work (); } cout << s . s \+ 1 << '\n' ; return 0 ; } ```   
---|---  
  
**本页面部分内容译自博文[строковый хеш](https://github.com/e-maxx-eng/e-maxx-eng/blob/61aff51f658644424c5e1b717f14fb7bf054ae80/src/string/string-hashing.md) 与其英文翻译版 [String Hashing](https://cp-algorithms.com/string/string-hashing.html)．其中俄文版版权协议为 Public Domain + Leave a Link；英文版版权协议为 CC-BY-SA 4.0．**

* * *

>  __本页面最近更新： 2026/2/2 11:53:55，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/hash.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/hash.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [ouuan](https://github.com/ouuan), [Tiphereth-A](https://github.com/Tiphereth-A), [1292224662](https://github.com/1292224662), [Enter-tainer](https://github.com/Enter-tainer), [Xeonacid](https://github.com/Xeonacid), [ShuYuMo2003](https://github.com/ShuYuMo2003), [c-forrest](https://github.com/c-forrest), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [mgt](mailto:i@margatroid.xyz), [taodaling](https://github.com/taodaling), [Yanjun-Zhao](https://github.com/Yanjun-Zhao), [algoriiiiithm](https://github.com/algoriiiiithm), [Chrogeek](https://github.com/Chrogeek), [GldHkkowo](https://github.com/GldHkkowo), [Haohu Shen](mailto:haohu.shen@ucalgary.ca), [HeRaNO](https://github.com/HeRaNO), [ImpleLee](https://github.com/ImpleLee), [kenlig](https://github.com/kenlig), [kevincoding03-rgb](https://github.com/kevincoding03-rgb), [Marcythm](https://github.com/Marcythm), [Menci](https://github.com/Menci), [Molmin](https://github.com/Molmin), [runnableAir](https://github.com/runnableAir), [ScrapW](https://github.com/ScrapW), [shawlleyw](https://github.com/shawlleyw), [sshwy](https://github.com/sshwy), [szdytom](https://github.com/szdytom), [tfia](https://github.com/tfia), [wangchong](mailto:wangchong756@gamil.com), [wendajiang](https://github.com/wendajiang), [xglight](https://github.com/xglight), [xiangmy21](https://github.com/xiangmy21), [zyouxam](https://github.com/zyouxam)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
