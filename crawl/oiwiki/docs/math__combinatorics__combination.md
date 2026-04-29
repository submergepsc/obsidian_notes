# 排列组合 - OI Wiki

- Source: https://oi-wiki.org/math/combinatorics/combination/

# 排列组合

## 引入

排列组合是组合数学中的基础．排列就是指从给定个数的元素中取出指定个数的元素进行排序；组合则是指从给定个数的元素中仅仅取出指定个数的元素，不考虑排序．排列组合的中心问题是研究给定要求的排列和组合可能出现的情况总数．排列组合与古典概率论关系密切．

在高中初等数学中，排列组合多是利用列表、枚举等方法解题．

## 加法 & 乘法原理

### 加法原理

完成一个工程可以有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类办法，𝑎𝑖(1 ≤𝑖 ≤𝑛)ai(1≤i≤n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 类方法的数目．那么完成这件事共有 𝑆 =𝑎1 +𝑎2 +⋯ +𝑎𝑛S=a1+a2+⋯+an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种不同的方法．

### 乘法原理

完成一个工程需要分 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个步骤，𝑎𝑖(1 ≤𝑖 ≤𝑛)ai(1≤i≤n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个步骤的不同方法数目．那么完成这件事共有 𝑆 =𝑎1 ×𝑎2 ×⋯ ×𝑎𝑛S=a1×a2×⋯×an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种不同的方法．

## 排列与组合基础

### 排列数

从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素中，任取 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（𝑚 ≤𝑛m≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为自然数，下同）个元素按照一定的顺序排成一列，叫做从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素中取出 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的一个排列；从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素中取出 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(𝑚 ≤𝑛m≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)) 个元素的所有排列的个数，叫做从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素中取出 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的排列数，用符号 A𝑚𝑛Anm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（或者是 P𝑚𝑛Pnm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）表示．

排列的计算公式如下：

A𝑚𝑛=𝑛(𝑛−1)(𝑛−2)⋯(𝑛−𝑚+1)=𝑛!(𝑛−𝑚)!Anm=n(n−1)(n−2)⋯(n−m+1)=n!(n−m)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

𝑛!n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的阶乘，即 6! =1 ×2 ×3 ×4 ×5 ×66!=1×2×3×4×5×6![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

公式可以这样理解：𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人选 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个来排队 (𝑚 ≤𝑛m≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))．第一个位置可以选 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，第二位置可以选 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，以此类推，第 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个（最后一个）可以选 𝑛 −𝑚 +1n−m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，得：

A𝑚𝑛=𝑛(𝑛−1)(𝑛−2)⋯(𝑛−𝑚+1)=𝑛!(𝑛−𝑚)!Anm=n(n−1)(n−2)⋯(n−m+1)=n!(n−m)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

全排列：𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人全部来排队，队长为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．第一个位置可以选 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，第二位置可以选 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，以此类推得：

A𝑛𝑛=𝑛(𝑛−1)(𝑛−2)⋯3×2×1=𝑛!Ann=n(n−1)(n−2)⋯3×2×1=n!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

全排列是排列数的一个特殊情况．

### 组合数

从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素中，任取 𝑚 ≤𝑛m≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素组成一个集合，叫做从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素中取出 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的一个组合；从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素中取出 𝑚 ≤𝑛m≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的所有组合的个数，叫做从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素中取出 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素的组合数，用符号 (𝑛𝑚)(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 来表示，读作「𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 选 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」．

组合数计算公式

(𝑛𝑚)=A𝑚𝑛𝑚!=𝑛!𝑚!(𝑛−𝑚)!(nm)=Anmm!=n!m!(n−m)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

如何理解上述公式？我们考虑 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人选 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个出来（𝑚 ≤𝑛m≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)），不排队，不在乎顺序．如果在乎顺序那么就是 A𝑚𝑛Anm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，如果不在乎那么就要除掉重复，那么重复了多少？同样选出来的 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人，他们还要「全排」得 𝑚!m!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以得：

(𝑛𝑚)×𝑚!=A𝑚𝑛(𝑛𝑚)=A𝑚𝑛𝑚!=𝑛!𝑚!(𝑛−𝑚)!(nm)×m!=Anm(nm)=Anmm!=n!m!(n−m)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

组合数也常用 C𝑚𝑛Cnm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示，即 C𝑚𝑛 =(𝑛𝑚)Cnm=(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．现在数学界普遍采用 (𝑛𝑚)(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的记号而非 C𝑚𝑛Cnm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

组合数也被称为「二项式系数」，下文二项式定理将会阐述其中的联系．

特别地，规定当 𝑚 >𝑛m>n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，A𝑚𝑛 =(𝑛𝑚) =0Anm=(nm)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 插板法

插板法（Stars and bars）是用于求一类给相同元素分组的方案数的一种技巧，也可以用于求一类线性不定方程的解的组数．

### 正整数和的数目

问题一：现有 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 **完全相同** 的元素，要求将其分为 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组，保证每组至少有一个元素，一共有多少种分法？

考虑拿 𝑘 −1k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块板子插入到 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素两两形成的 𝑛 −1n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个空里面．

因为元素是完全相同的，所以答案就是 (𝑛−1𝑘−1)(n−1k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

本质是求 𝑥1 +𝑥2 +⋯ +𝑥𝑘 =𝑛x1+x2+⋯+xk=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的正整数解的组数．

### 非负整数和的数目

问题二：如果问题变化一下，每组允许为空呢？

显然此时没法直接插板了，因为有可能出现很多块板子插到一个空里面的情况，非常不好计算．

我们考虑创造条件转化成有限制的问题一，先借 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素过来，在这 𝑛 +𝑘n+k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素形成的 𝑛 +𝑘 −1n+k−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个空里面插板，答案为

(𝑛+𝑘−1𝑘−1)=(𝑛+𝑘−1𝑛)(n+k−1k−1)=(n+k−1n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

虽然不是直接求的原问题，但这个式子就是原问题的答案，可以这么理解：

开头我们借来了 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素，用于保证每组至少有一个元素，插完板之后再把这 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个借来的元素从 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组里面拿走．因为元素是相同的，所以转化过的情况和转化前的情况可以一一对应，答案也就是相等的．

由此可以推导出插板法的公式：(𝑛+𝑘−1𝑛)(n+k−1n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

本质是求 𝑥1 +𝑥2 +⋯ +𝑥𝑘 =𝑛x1+x2+⋯+xk=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非负整数解的组数（即要求 𝑥𝑖 ≥0xi≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）．

### 不同下界整数和的数目

问题三：如果再扩展一步，要求对于第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组，至少要分到 𝑎𝑖,∑𝑎𝑖 ≤𝑛ai,∑ai≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素呢？

本质是求 𝑥1 +𝑥2 +⋯ +𝑥𝑘 =𝑛x1+x2+⋯+xk=n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的解的数目，其中 𝑥𝑖 ≥𝑎𝑖xi≥ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

类比无限制的情况，我们借 ∑𝑎𝑖∑ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素过来，保证第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组至少能分到 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个．也就是令

𝑥′𝑖=𝑥𝑖−𝑎𝑖xi′=xi−ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

得到新方程：

(𝑥′1+𝑎1)+(𝑥′2+𝑎2)+⋯+(𝑥′𝑘+𝑎𝑘)=𝑛𝑥′1+𝑥′2+⋯+𝑥′𝑘=𝑛−𝑎1−𝑎2−⋯−𝑎𝑘𝑥′1+𝑥′2+⋯+𝑥′𝑘=𝑛−∑𝑎𝑖(x1′+a1)+(x2′+a2)+⋯+(xk′+ak)=nx1′+x2′+⋯+xk′=n−a1−a2−⋯−akx1′+x2′+⋯+xk′=n−∑ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中

𝑥′𝑖≥0xi′≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

然后问题三就转化成了问题二，直接用插板法公式得到答案为

(𝑛−∑𝑎𝑖+𝑘−1𝑛−∑𝑎𝑖)(n−∑ai+k−1n−∑ai)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 不相邻的排列

1 ∼𝑛1∼n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个自然数中选 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个，这 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数中任何两个数都不相邻的组合有 (𝑛−𝑘+1𝑘)(n−k+1k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种．

## 二项式定理

在进入排列组合进阶篇之前，我们先介绍一个与组合数密切相关的定理——二项式定理．

二项式定理阐明了一个展开式的系数：

(𝑎+𝑏)𝑛=𝑛∑𝑖=0(𝑛𝑖)𝑎𝑛−𝑖𝑏𝑖(a+b)n=∑i=0n(ni)an−ibi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证明可以采用数学归纳法，利用 (𝑛𝑘) +(𝑛𝑘−1) =(𝑛+1𝑘)(nk)+(nk−1)=(n+1k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 做归纳．

二项式定理也可以很容易扩展为多项式的形式：

设 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为正整数，𝑥𝑖xi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为实数，

(𝑥1+𝑥2+⋯+𝑥𝑡)𝑛=∑满足𝑛1+⋯+𝑛𝑡=𝑛的非负整数解(𝑛𝑛1,𝑛2,⋯,𝑛𝑡)𝑥𝑛11𝑥𝑛22⋯𝑥𝑛𝑡𝑡(x1+x2+⋯+xt)n=∑满足n1+⋯+nt=n的非负整数解(nn1,n2,⋯,nt)x1n1x2n2⋯xtnt![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中的 (𝑛𝑛1,𝑛2,⋯,𝑛𝑡)(nn1,n2,⋯,nt)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是多项式系数，它的性质也很相似：

∑(𝑛𝑛1,𝑛2,⋯,𝑛𝑡)=𝑡𝑛∑(nn1,n2,⋯,nt)=tn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 排列与组合进阶篇

接下来我们介绍一些排列组合的变种．

### 多重集的排列数 | 多重组合数

请大家一定要区分 **多重组合数** 与 **多重集的组合数** ！两者是完全不同的概念！

多重集是指包含重复元素的广义集合．设 𝑆 ={𝑛1 ⋅𝑎1,𝑛2 ⋅𝑎2,⋯,𝑛𝑘 ⋅𝑎𝑘}S={n1⋅a1,n2⋅a2,⋯,nk⋅ak}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示由 𝑛1n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，…，𝑛𝑘nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组成的多重集，𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全排列个数为

𝑛!∏𝑘𝑖=1𝑛𝑖!=𝑛!𝑛1!𝑛2!⋯𝑛𝑘!n!∏i=1kni!=n!n1!n2!⋯nk!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

相当于把相同元素的排列数除掉了．具体地，你可以认为你有 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 种不一样的球，每种球的个数分别是 𝑛1,𝑛2,⋯,𝑛𝑘n1,n2,⋯,nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑛 =𝑛1 +𝑛2 +… +𝑛𝑘n=n1+n2+…+nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个球的全排列数就是 **多重集的排列数** ．多重集的排列数常被称作 **多重组合数** ．我们可以用多重组合数的符号表示上式：

(𝑛𝑛1,𝑛2,⋯,𝑛𝑘)=𝑛!∏𝑘𝑖=1𝑛𝑖!(nn1,n2,⋯,nk)=n!∏i=1kni!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

可以看出，(𝑛𝑚)(nm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价于 (𝑛𝑚,𝑛−𝑚)(nm,n−m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，只不过后者较为繁琐，因而不采用．

### 多重集的组合数 1

设 𝑆 ={𝑛1 ⋅𝑎1,𝑛2 ⋅𝑎2,⋯,𝑛𝑘 ⋅𝑎𝑘}S={n1⋅a1,n2⋅a2,⋯,nk⋅ak}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示由 𝑛1n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，…，𝑛𝑘nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组成的多重集．那么对于整数 𝑟(𝑟 <𝑛𝑖,∀𝑖 ∈[1,𝑘])r(r<ni,∀i∈[1,k])![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中选择 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素组成一个多重集的方案数就是 **多重集的组合数** ．这个问题等价于 𝑥1 +𝑥2 +⋯ +𝑥𝑘 =𝑟x1+x2+⋯+xk=r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非负整数解的数目，可以用插板法解决，答案为

(𝑟+𝑘−1𝑘−1)(r+k−1k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 多重集的组合数 2

考虑这个问题：设 𝑆 ={𝑛1 ⋅𝑎1,𝑛2 ⋅𝑎2,⋯,𝑛𝑘 ⋅𝑎𝑘,}S={n1⋅a1,n2⋅a2,⋯,nk⋅ak,}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示由 𝑛1n1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑛2n2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，…，𝑛𝑘nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个 𝑎𝑘ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 组成的多重集．那么对于正整数 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，从 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中选择 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素组成一个多重集的方案数．

这样就限制了每种元素的取的个数．同样的，我们可以把这个问题转化为带限制的线性方程求解：

∀𝑖∈[1,𝑘], 𝑥𝑖≤𝑛𝑖, 𝑘∑𝑖=1𝑥𝑖=𝑟∀i∈[1,k], xi≤ni, ∑i=1kxi=r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

于是很自然地想到了容斥原理．容斥的模型如下：

  1. 全集：𝑘∑𝑖=1𝑥𝑖 =𝑟∑i=1kxi=r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的非负整数解．
  2. 属性：𝑥𝑖 ≤𝑛𝑖xi≤ni![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

于是设满足属性 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合是 𝑆𝑖Si![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，――𝑆𝑖Si―![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示不满足属性 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合，即满足 𝑥𝑖 ≥𝑛𝑖 +1xi≥ni+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的集合（转化为上面插板法的问题三）．那么答案即为

∣𝑘⋂𝑖=1𝑆𝑖∣=|𝑈|−∣𝑘⋃𝑖=1――𝑆𝑖∣|⋂i=1kSi|=|U|−|⋃i=1kSi―|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

根据容斥原理，有：

∣𝑘⋃𝑖=1――𝑆𝑖∣=∑𝑖∣――𝑆𝑖∣−∑𝑖,𝑗∣――𝑆𝑖∩――𝑆𝑗∣+∑𝑖,𝑗,𝑘∣――𝑆𝑖∩――𝑆𝑗∩―――𝑆𝑘∣−⋯+(−1)𝑘−1∣𝑘⋂𝑖=1――𝑆𝑖∣=∑𝑖(𝑘+𝑟−𝑛𝑖−2𝑘−1)−∑𝑖,𝑗(𝑘+𝑟−𝑛𝑖−𝑛𝑗−3𝑘−1)+∑𝑖,𝑗,𝑘(𝑘+𝑟−𝑛𝑖−𝑛𝑗−𝑛𝑘−4𝑘−1)−⋯+(−1)𝑘−1(𝑘+𝑟−∑𝑘𝑖=1𝑛𝑖−𝑘−1𝑘−1)|⋃i=1kSi―|=∑i|Si―|−∑i,j|Si―∩Sj―|+∑i,j,k|Si―∩Sj―∩Sk―|−⋯+(−1)k−1|⋂i=1kSi―|=∑i(k+r−ni−2k−1)−∑i,j(k+r−ni−nj−3k−1)+∑i,j,k(k+r−ni−nj−nk−4k−1)−⋯+(−1)k−1(k+r−∑i=1kni−k−1k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

拿全集 |𝑈| =(𝑘+𝑟−1𝑘−1)|U|=(k+r−1k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 减去上式，得到多重集的组合数

𝐴𝑛𝑠=𝑘∑𝑝=0(−1)𝑝∑𝐴(𝑘+𝑟−1−∑𝐴𝑛𝐴𝑖−𝑝𝑘−1)Ans=∑p=0k(−1)p∑A(k+r−1−∑AnAi−pk−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 A 是充当枚举子集的作用，满足 |𝐴| =𝑝, 𝐴𝑖 <𝐴𝑖+1|A|=p, Ai<Ai+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 圆排列

𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个人全部来围成一圈，所有的排列数记为 Q𝑛𝑛Qnn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．考虑其中已经排好的一圈，从不同位置断开，又变成不同的队列． 所以有

Q𝑛𝑛×𝑛=A𝑛𝑛⟹Q𝑛=A𝑛𝑛𝑛=(𝑛−1)!Qnn×n=Ann⟹Qn=Annn=(n−1)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由此可知部分圆排列的公式：

Q𝑟𝑛=A𝑟𝑛𝑟=𝑛!𝑟×(𝑛−𝑟)!Qnr=Anrr=n!r×(n−r)!![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## 组合数性质 | 二项式推论

由于组合数在 OI 中十分重要，因此在此介绍一些组合数的性质．

(𝑛𝑚)=(𝑛𝑛−𝑚)(1)(1)(nm)=(nn−m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

相当于将选出的集合对全集取补集，故数值不变．（对称性）

(𝑛𝑘)=𝑛𝑘(𝑛−1𝑘−1)(2)(2)(nk)=nk(n−1k−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

由定义导出的递推式．

(𝑛𝑚)=(𝑛−1𝑚)+(𝑛−1𝑚−1)(3)(3)(nm)=(n−1m)+(n−1m−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

组合数的递推式（杨辉三角的公式表达）．我们可以利用这个式子，在 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的复杂度下推导组合数．

(𝑛0)+(𝑛1)+⋯+(𝑛𝑛)=𝑛∑𝑖=0(𝑛𝑖)=2𝑛(4)(4)(n0)+(n1)+⋯+(nn)=∑i=0n(ni)=2n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是二项式定理的特殊情况．取 𝑎 =𝑏 =1a=b=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 就得到上式．

𝑛∑𝑖=0(−1)𝑖(𝑛𝑖)=[𝑛=0](5)(5)∑i=0n(−1)i(ni)=[n=0]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

二项式定理的另一种特殊情况，可取 𝑎 =1,𝑏 = −1a=1,b=−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．式子的特殊情况是取 𝑛 =0n=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时答案为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

𝑘∑𝑖=0(𝑛𝑖)(𝑚𝑘−𝑖)=(𝑚+𝑛𝑘)(6)(6)∑i=0k(ni)(mk−i)=(m+nk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

拆组合数的式子，在处理某些数据结构题时会用到．被称为 [范德蒙恒等式](https://en.wikipedia.org/wiki/Vandermonde%27s_identity)．

𝑛∑𝑖=0(𝑛𝑖)2=(2𝑛𝑛)(7)(7)∑i=0n(ni)2=(2nn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这是 (6)(6)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的特殊情况，取 𝑛 =𝑘 =𝑚n=k=m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

𝑛∑𝑖=0𝑖(𝑛𝑖)=𝑛2𝑛−1(8)(8)∑i=0ni(ni)=n2n−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

带权和的一个式子，通过对 (4)(4)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对应的多项式函数求导可以得证．

𝑛∑𝑖=0𝑖2(𝑛𝑖)=𝑛(𝑛+1)2𝑛−2(9)(9)∑i=0ni2(ni)=n(n+1)2n−2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

与上式类似，可以通过对多项式函数求导证明．

𝑛∑𝑙=0(𝑙𝑘)=(𝑛+1𝑘+1)(10)(10)∑l=0n(lk)=(n+1k+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

通过组合分析一一考虑 𝑆 ={𝑎1,𝑎2,⋯,𝑎𝑛+1}S={a1,a2,⋯,an+1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑘 +1k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 子集数可以得证，在恒等式证明中比较常用．被称为 [朱世杰恒等式](https://en.wikipedia.org/wiki/Hockey-stick_identity)．

(𝑛𝑟)(𝑟𝑘)=(𝑛𝑘)(𝑛−𝑘𝑟−𝑘)(11)(11)(nr)(rk)=(nk)(n−kr−k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

通过定义可以证明．

𝑛∑𝑖=0(𝑛−𝑖𝑖)=𝐹𝑛+1(12)(12)∑i=0n(n−ii)=Fn+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝐹F![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是斐波那契数列．

(𝑛+𝑘𝑘)2=𝑘∑𝑗=0(𝑘𝑗)2(𝑛+2𝑘−𝑗2𝑘)(13)(13)(n+kk)2=∑j=0k(kj)2(n+2k−j2k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

通过 (6)(6)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以证明．被称为 [李善兰恒等式](https://en.wikipedia.org/wiki/Li_Shanlan_identity)．

## 二项式反演

记 𝑓𝑛fn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示恰好使用 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素形成特定结构的方案数，𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示从 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个不同元素中选出 𝑖 ≥0i≥0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个元素形成特定结构的总方案数．

若已知 𝑓𝑛fn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求 𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么显然有：

𝑔𝑛=𝑛∑𝑖=0(𝑛𝑖)𝑓𝑖gn=∑i=0n(ni)fi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

若已知 𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求 𝑓𝑛fn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么：

𝑓𝑛=𝑛∑𝑖=0(𝑛𝑖)(−1)𝑛−𝑖𝑔𝑖fn=∑i=0n(ni)(−1)n−igi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

上述已知 𝑔𝑛gn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 求 𝑓𝑛fn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的过程，就称为 **二项式反演** ．

### 证明

将反演公式的 𝑔𝑖gi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 展开得到：

𝑓𝑛=𝑛∑𝑖=0(𝑛𝑖)(−1)𝑛−𝑖[𝑖∑𝑗=0(𝑖𝑗)𝑓𝑗]=𝑛∑𝑖=0𝑖∑𝑗=0(𝑛𝑖)(𝑖𝑗)(−1)𝑛−𝑖𝑓𝑗fn=∑i=0n(ni)(−1)n−i[∑j=0i(ij)fj]=∑i=0n∑j=0i(ni)(ij)(−1)n−ifj![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

先枚举 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，再枚举 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，得到：

𝑓𝑛=𝑛∑𝑗=0𝑛∑𝑖=𝑗(𝑛𝑖)(𝑖𝑗)(−1)𝑛−𝑖𝑓𝑗=𝑛∑𝑗=0𝑓𝑗𝑛∑𝑖=𝑗(𝑛𝑖)(𝑖𝑗)(−1)𝑛−𝑖fn=∑j=0n∑i=jn(ni)(ij)(−1)n−ifj=∑j=0nfj∑i=jn(ni)(ij)(−1)n−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

使用 「组合数性质 | 二项式推论」 的公式 (11) 得到：

𝑓𝑛=𝑛∑𝑗=0𝑓𝑗𝑛∑𝑖=𝑗(𝑛𝑗)(𝑛−𝑗𝑖−𝑗)(−1)𝑛−𝑖=𝑛∑𝑗=0(𝑛𝑗)𝑓𝑗𝑛∑𝑖=𝑗(𝑛−𝑗𝑖−𝑗)(−1)𝑛−𝑖fn=∑j=0nfj∑i=jn(nj)(n−ji−j)(−1)n−i=∑j=0n(nj)fj∑i=jn(n−ji−j)(−1)n−i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

令 𝑘 =𝑖 −𝑗k=i−j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．则 𝑖 =𝑘 +𝑗i=k+j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，上式转换为：

𝑓𝑛=𝑛∑𝑗=0(𝑛𝑗)𝑓𝑗𝑛−𝑗∑𝑘=0(𝑛−𝑗𝑘)(−1)𝑛−𝑗−𝑘1𝑘fn=∑j=0n(nj)fj∑k=0n−j(n−jk)(−1)n−j−k1k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

使用 「组合数性质 | 二项式推论」 的公式 (5) 得到：

𝑓𝑛=𝑛∑𝑗=0(𝑛𝑗)𝑓𝑗[𝑛=𝑗]=𝑓𝑛fn=∑j=0n(nj)fj[n=j]=fn![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

证毕．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/combinatorics/combination.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/combinatorics/combination.md "edit.link.title")  
>  __本页面贡献者：[Zhoier](https://github.com/Zhoier), [Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [Tiphereth-A](https://github.com/Tiphereth-A), [Xeonacid](https://github.com/Xeonacid), [Great-designer](https://github.com/Great-designer), [cjsoft](https://github.com/cjsoft), [MegaOwIer](https://github.com/MegaOwIer), [Enter-tainer](https://github.com/Enter-tainer), [Marcythm](https://github.com/Marcythm), [renbaoshuo](https://github.com/renbaoshuo), [StudyingFather](https://github.com/StudyingFather), [untitledunrevised](https://github.com/untitledunrevised), [CCXXXI](https://github.com/CCXXXI), [Chrogeek](https://github.com/Chrogeek), [Early0v0](https://github.com/Early0v0), [Enonya](https://github.com/Enonya), [FFjet](https://github.com/FFjet), [Horrible120](https://github.com/Horrible120), [iamtwz](https://github.com/iamtwz), [IceySakura](https://github.com/IceySakura), [Menci](https://github.com/Menci), [opsiff](https://github.com/opsiff), [Tiger3018](https://github.com/Tiger3018), [wq-yang](https://github.com/wq-yang), [Xiaobin Ren](mailto:xbren@bupt.edu.cn), [XuYueming520](https://github.com/XuYueming520), [Yukimaikoriya](https://github.com/Yukimaikoriya), [ZXyaang](https://github.com/ZXyaang), [zyzzyh](https://github.com/zyzzyh)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
