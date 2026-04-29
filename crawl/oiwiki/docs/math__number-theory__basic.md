# 数论基础 - OI Wiki

- Source: https://oi-wiki.org/math/number-theory/basic/

# 数论基础

本文对于数论的开头部分做一个简介．

## 整除

定义

设 𝑎,𝑏 ∈𝐙a,b∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑎 ≠0a≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果 ∃𝑞 ∈𝐙∃q∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，使得 𝑏 =𝑎𝑞b=aq![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么就说 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可被 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **整除** ，记作 𝑎 ∣𝑏a∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不被 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除记作 𝑎 ∤𝑏a∤b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

整除的性质：

  * 𝑎 ∣𝑏 ⟺ −𝑎 ∣𝑏 ⟺ 𝑎 ∣ −𝑏 ⟺ |𝑎| ∣|𝑏|a∣b⟺−a∣b⟺a∣−b⟺|a|∣|b|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑎 ∣𝑏 ∧𝑏 ∣𝑐 ⟹ 𝑎 ∣𝑐a∣b∧b∣c⟹a∣c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑎 ∣𝑏 ∧𝑎 ∣𝑐 ⟺ ∀𝑥,𝑦 ∈𝐙,𝑎 ∣(𝑥𝑏 +𝑦𝑐)a∣b∧a∣c⟺∀x,y∈Z,a∣(xb+yc)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 𝑎 ∣𝑏 ∧𝑏 ∣𝑎 ⟹ 𝑏 = ±𝑎a∣b∧b∣a⟹b=±a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  * 设 𝑚 ≠0m≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑎 ∣𝑏 ⟺ 𝑚𝑎 ∣𝑚𝑏a∣b⟺ma∣mb![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 设 𝑏 ≠0b≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑎 ∣𝑏 ⟹ |𝑎| ≤|𝑏|a∣b⟹|a|≤|b|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 设 𝑎 ≠0,𝑏 =𝑞𝑎 +𝑐a≠0,b=qa+c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑎 ∣𝑏 ⟺ 𝑎 ∣𝑐a∣b⟺a∣c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

### 约数

定义

若 𝑎 ∣𝑏a∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **倍数** ，𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **约数** ．

00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是所有非 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整数的倍数．对于整数 𝑏 ≠0b≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数只有有限个．

平凡约数（平凡因数）：对于整数 𝑏 ≠0b≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，±1±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、±𝑏±b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的平凡约数．当 𝑏 = ±1b=±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 只有两个平凡约数．

对于整数 𝑏 ≠0b≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的其他约数称为真约数（真因数、非平凡约数、非平凡因数）．

约数的性质：

  * 设整数 𝑏 ≠0b≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．当 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体约数的时候，𝑏𝑑bd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也遍历 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体约数．
  * 设整数 𝑏 >0b>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则当 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 遍历 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体正约数的时候，𝑏𝑑bd![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也遍历 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的全体正约数．

在具体问题中，**如果没有特别说明，约数总是指正约数．**

## 带余数除法

余数

设 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为两个给定的整数，𝑎 ≠0a≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．设 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是一个给定的整数．那么，一定存在唯一的一对整数 𝑞q![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，满足 𝑏 =𝑞𝑎 +𝑟,𝑑 ≤𝑟 <|𝑎| +𝑑b=qa+r,d≤r<|a|+d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

无论整数 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取何值，𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 统称为余数．𝑎 ∣𝑏a∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 等价于 𝑎 ∣𝑟a∣r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

一般情况下，𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，此时等式 𝑏 =𝑞𝑎 +𝑟,0 ≤𝑟 <|𝑎|b=qa+r,0≤r<|a|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为带余数除法（带余除法）．这里的余数 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为最小非负余数．

余数往往还有两种常见取法：

  * 绝对最小余数：𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的绝对值的一半的相反数．即 𝑏 =𝑞𝑎 +𝑟, −|𝑎|2 ≤𝑟 <|𝑎| −|𝑎|2b=qa+r,−|a|2≤r<|a|−|a|2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 最小正余数：𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 取 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．即 𝑏 =𝑞𝑎 +𝑟,1 ≤𝑟 <|𝑎| +1b=qa+r,1≤r<|a|+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

带余数除法的余数只有最小非负余数．**如果没有特别说明，余数总是指最小非负余数．**

余数的性质：

  * 任一整数被正整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 除后，余数一定是且仅是 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 到 (𝑎 −1)(a−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 这 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个数中的一个．
  * 相邻的 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数被正整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 除后，恰好取到上述 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个余数．特别地，一定有且仅有一个数被 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 整除．

## 最大公约数与最小公倍数

关于公约数、公倍数、最大公约数与最小公倍数，四个名词的定义，见 [最大公约数](../gcd/)．

Warning

一些作者认为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大公约数无定义，其余作者一般将其视为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．C++ STL 的实现中采用后者，即认为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最大公约数为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)1．

最大公约数有如下性质：

  * (𝑎1,…,𝑎𝑛) =(|𝑎1|,…,|𝑎𝑛|)(a1,…,an)=(|a1|,…,|an|)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * (𝑎,𝑏) =(𝑏,𝑎)(a,b)=(b,a)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 若 𝑎 ≠0a≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 (𝑎,0) =(𝑎,𝑎) =|𝑎|(a,0)=(a,a)=|a|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * (𝑏𝑞 +𝑟,𝑏) =(𝑟,𝑏)(bq+r,b)=(r,b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * (𝑎1,…,𝑎𝑛) =((𝑎1,𝑎2),𝑎3,…,𝑎𝑛)(a1,…,an)=((a1,a2),a3,…,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而 ∀1 <𝑘 <𝑛 −1, (𝑎1,…,𝑎𝑛) =((𝑎1,…,𝑎𝑘),(𝑎𝑘+1,…,𝑎𝑛))∀1<k<n−1, (a1,…,an)=((a1,…,ak),(ak+1,…,an))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 对不全为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑎1,…,𝑎𝑛a1,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和非零整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，(𝑚𝑎1,…,𝑚𝑎𝑛) =|𝑚|(𝑎1,…,𝑎𝑛)(ma1,…,man)=|m|(a1,…,an)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 对不全为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑎1,…,𝑎𝑛a1,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 (𝑎1,…,𝑎𝑛) =𝑑(a1,…,an)=d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 (𝑎1/𝑑,…,𝑎𝑛/𝑑) =1(a1/d,…,an/d)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * (𝑎𝑛,𝑏𝑛) =(𝑎,𝑏)𝑛(an,bn)=(a,b)n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最大公约数还有如下与互素相关的性质：

  * 若 𝑏|𝑎𝑐b|ac![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 (𝑎,𝑏) =1(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑏 ∣𝑐b∣c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 若 𝑏|𝑐b|c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、𝑎|𝑐a|c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 (𝑎,𝑏) =1(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑎𝑏 ∣𝑐ab∣c![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 若 (𝑎,𝑏) =1(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 (𝑎,𝑏𝑐) =(𝑎,𝑐)(a,bc)=(a,c)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 若 (𝑎𝑖,𝑏𝑗) =1, ∀1 ≤𝑖 ≤𝑛,1 ≤𝑗 ≤𝑚(ai,bj)=1, ∀1≤i≤n,1≤j≤m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 (∏𝑖𝑎𝑖,∏𝑗𝑏𝑗) =1(∏iai,∏jbj)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．特别地，若 (𝑎,𝑏) =1(a,b)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 (𝑎𝑛,𝑏𝑚) =1(an,bm)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 对整数 𝑎1,…,𝑎𝑛a1,…,an![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 ∃𝑣 ∈𝐙, ∏𝑖𝑎𝑖 =𝑣𝑚∃v∈Z, ∏iai=vm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 (𝑎𝑖,𝑎𝑗) =1, ∀𝑖 ≠𝑗(ai,aj)=1, ∀i≠j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 ∀1 ≤𝑖 ≤𝑛, 𝑚√𝑎𝑖 ∈𝐙∀1≤i≤n, aim∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最小公倍数有如下性质：

  * [𝑎1,…,𝑎𝑛] =[|𝑎1|,…,|𝑎𝑛|][a1,…,an]=[|a1|,…,|an|]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * [𝑎,𝑏] =[𝑏,𝑎][a,b]=[b,a]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 若 𝑎 ≠0a≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 [𝑎,1] =[𝑎,𝑎] =|𝑎|[a,1]=[a,a]=|a|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 若 𝑎 ∣𝑏a∣b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 [𝑎,𝑏] =|𝑏|[a,b]=|b|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * [𝑎1,…,𝑎𝑛] =[[𝑎1,𝑎2],𝑎3,…,𝑎𝑛][a1,…,an]=[[a1,a2],a3,…,an]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而 ∀1 <𝑘 <𝑛 −1, [𝑎1,…,𝑎𝑛] =[[𝑎1,…,𝑎𝑘],[𝑎𝑘+1,…,𝑎𝑛]]∀1<k<n−1, [a1,…,an]=[[a1,…,ak],[ak+1,…,an]]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 若 𝑎𝑖 ∣𝑚, ∀1 ≤𝑖 ≤𝑛ai∣m, ∀1≤i≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 [𝑎1,…,𝑎𝑛] ∣𝑚[a1,…,an]∣m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * [𝑚𝑎1,…,𝑚𝑎𝑛] =|𝑚|[𝑎1,…,𝑎𝑛][ma1,…,man]=|m|[a1,…,an]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * [𝑎,𝑏,𝑐][𝑎𝑏,𝑏𝑐,𝑐𝑎] =[𝑎,𝑏][𝑏,𝑐][𝑐,𝑎][a,b,c][ab,bc,ca]=[a,b][b,c][c,a]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * [𝑎𝑛,𝑏𝑛] =[𝑎,𝑏]𝑛[an,bn]=[a,b]n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最大公约数和最小公倍数可以组合出很多奇妙的等式，如：

  * (𝑎,𝑏)[𝑎,𝑏] =|𝑎𝑏|(a,b)[a,b]=|ab|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * (𝑎𝑏,𝑏𝑐,𝑐𝑎)[𝑎,𝑏,𝑐] =|𝑎𝑏𝑐|(ab,bc,ca)[a,b,c]=|abc|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * (𝑎,𝑏,𝑐)2(𝑎,𝑏)(𝑏,𝑐)(𝑎,𝑐) =[𝑎,𝑏,𝑐]2[𝑎,𝑏][𝑏,𝑐][𝑎,𝑐](a,b,c)2(a,b)(b,c)(a,c)=[a,b,c]2[a,b][b,c][a,c]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这些性质均可通过定义或 唯一分解定理 证明，其中使用唯一分解定理的证明更容易理解．

### 互素

定义

若 (𝑎1,𝑎2) =1(a1,a2)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称 𝑎1a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑎2a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **互素** （**既约** ）．

若 (𝑎1,…,𝑎𝑘) =1(a1,…,ak)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称 𝑎1,…,𝑎𝑘a1,…,ak![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) **互素** （**既约** ）．

多个整数互素，不一定两两互素．例如 66![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)、1010![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 1515![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互素，但是任意两个都不互素．

互素的性质与最大公约数理论：裴蜀定理（Bézout's identity）．见 [裴蜀定理](../bezouts/)．

### 辗转相除法

辗转相除法是一种算法，也称 Euclid 算法．见 [最大公约数](../gcd/)．

## 素数与合数

关于素数的算法见 [素数](../prime/)．

定义

设整数 𝑝 ≠0, ±1p≠0,±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 除了平凡约数外没有其他约数，那么称 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **素数** （**不可约数** ）．

若整数 𝑎 ≠0, ±1a≠0,±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是素数，则称 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **合数** ．

𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 −𝑝−p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 总是同为素数或者同为合数．**如果没有特别说明，素数总是指正的素数．**

整数的因数是素数，则该素数称为该整数的素因数（素约数）．

素数与合数的简单性质：

  * 大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是合数，等价于 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可以表示为整数 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑒e![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（1 <𝑑,𝑒 <𝑎1<d,e<a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）的乘积．
  * 如果素数 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 有大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的约数 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑑 =𝑝d=p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 大于 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 一定可以表示为素数的乘积．
  * 对于合数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，一定存在素数 𝑝 ≤√𝑎p≤a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑝 ∣𝑎p∣a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 素数有无穷多个．
  * 所有大于 33![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的素数都可以表示为 6𝑛 ±16n±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的形式2．

## 算术基本定理

算术基本引理

设 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数，𝑝 ∣𝑎1𝑎2p∣a1a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么 𝑝 ∣𝑎1p∣a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑝 ∣𝑎2p∣a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 至少有一个成立．

算术基本引理的逆命题稍加修改也可以得到素数的另一种定义．

素数的另一种定义

对整数 𝑝 ≠0, ±1p≠0,±1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若对任意满足 𝑝 ∣𝑎1𝑎2p∣a1a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的整数 𝑎1,𝑎2a1,a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均有 𝑝 ∣𝑎1p∣a1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑝 ∣𝑎2p∣a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立，则称 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数．

Tip

这个定义的动机可以从 [素理想](../../algebra/ring-theory/#素理想) 中找到．

算术基本定理（唯一分解定理）

设正整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么必有表示：

𝑎=𝑝1𝑝2⋯𝑝𝑠a=p1p2⋯ps![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

其中 𝑝𝑗(1 ≤𝑗 ≤𝑠)pj(1≤j≤s)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是素数．并且在不计次序的意义下，该表示唯一．

标准素因数分解式

将上述表示中，相同的素数合并，可得：

𝑎=𝑝1𝛼1𝑝2𝛼2⋯𝑝𝑠𝛼𝑠,𝑝1<𝑝2<⋯<𝑝𝑠a=p1α1p2α2⋯psαs,p1<p2<⋯<ps![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

称为正整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的标准素因数分解式．

算术基本定理和算术基本引理，两个定理是等价的．

## 同余

定义

设整数 𝑚 ≠0m≠0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若 𝑚 ∣(𝑎 −𝑏)m∣(a−b)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **模数** （**模** ），𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同余于 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **剩余** ．记作 𝑎 ≡𝑏(mod𝑚)a≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

否则，𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不同余于 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的剩余．记作 𝑎 ≢𝑏(mod𝑚)a≢b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这样的等式，称为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的同余式，简称 **同余式** ．

根据整除的性质，上述同余式也等价于 𝑎 ≡𝑏(mod( −𝑚))a≡b(mod(−m))![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

后文中，如果没有特别说明，模数总是 **正整数** ．

式中的 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的剩余，这个概念与余数完全一致．通过限定 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的范围，相应的有 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小非负剩余、绝对最小剩余、最小正剩余．

同余的性质：

  * 同余是 [等价关系](../../order-theory/#二元关系)，即同余具有
    * 自反性：𝑎 ≡𝑎(mod𝑚)a≡a(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
    * 对称性：若 𝑎 ≡𝑏(mod𝑚)a≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑏 ≡𝑎(mod𝑚)b≡a(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
    * 传递性：若 𝑎 ≡𝑏(mod𝑚),𝑏 ≡𝑐(mod𝑚)a≡b(modm),b≡c(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑎 ≡𝑐(mod𝑚)a≡c(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 线性运算：若 𝑎,𝑏,𝑐,𝑑 ∈𝐙,𝑚 ∈𝐍∗,𝑎 ≡𝑏(mod𝑚),𝑐 ≡𝑑(mod𝑚)a,b,c,d∈Z,m∈N∗,a≡b(modm),c≡d(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 则有：
    * 𝑎 ±𝑐 ≡𝑏 ±𝑑(mod𝑚)a±c≡b±d(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
    * 𝑎 ×𝑐 ≡𝑏 ×𝑑(mod𝑚)a×c≡b×d(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 设 𝑓(𝑥) =∑𝑛𝑖=0𝑎𝑖𝑥𝑖f(x)=∑i=0naixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔(𝑥) =∑𝑛𝑖=0𝑏𝑖𝑥𝑖g(x)=∑i=0nbixi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是两个整系数多项式，𝑚 ∈𝐍∗m∈N∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑎𝑖 ≡𝑏𝑖(mod𝑚), 0 ≤𝑖 ≤𝑛ai≡bi(modm), 0≤i≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对任意整数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均有 𝑓(𝑥) ≡𝑔(𝑥)(mod𝑚)f(x)≡g(x)(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．进而若 𝑠 ≡𝑡(mod𝑚)s≡t(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑓(𝑠) ≡𝑔(𝑡)(mod𝑚)f(s)≡g(t)(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 若 𝑎,𝑏 ∈𝐙,𝑘,𝑚 ∈𝐍∗,𝑎 ≡𝑏(mod𝑚)a,b∈Z,k,m∈N∗,a≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 则 𝑎𝑘 ≡𝑏𝑘(mod𝑚𝑘)ak≡bk(modmk)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 若 𝑎,𝑏 ∈𝐙,𝑑,𝑚 ∈𝐍∗,𝑑 ∣𝑎,𝑑 ∣𝑏,𝑑 ∣𝑚a,b∈Z,d,m∈N∗,d∣a,d∣b,d∣m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则当 𝑎 ≡𝑏(mod𝑚)a≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立时，有 𝑎𝑑 ≡𝑏𝑑(mod𝑚𝑑)ad≡bd(modmd)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 若 𝑎,𝑏 ∈𝐙,𝑑,𝑚 ∈𝐍∗,𝑑 ∣𝑚a,b∈Z,d,m∈N∗,d∣m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则当 𝑎 ≡𝑏(mod𝑚)a≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立时，有 𝑎 ≡𝑏(mod𝑑)a≡b(modd)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 若 𝑎,𝑏 ∈𝐙,𝑑,𝑚 ∈𝐍∗a,b∈Z,d,m∈N∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则当 𝑎 ≡𝑏(mod𝑚)a≡b(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 成立时，有 (𝑎,𝑚) =(𝑏,𝑚)(a,m)=(b,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．若 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 能整除 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 及 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的一个，则 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 必定能整除 𝑎,𝑏a,b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的另一个．

还有性质是乘法逆元．见 [乘法逆元](../inverse/)．

## 同余类与剩余系

为方便讨论，对集合 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和元素 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们引入如下记号：

  * 𝑟 +𝐴 :={𝑟 +𝑎 :𝑎 ∈𝐴}r+A:={r+a:a∈A}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 𝑟𝐴 :={𝑟𝑎 :𝑎 ∈𝐴}rA:={ra:a∈A}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 𝐴 +𝐵 :={𝑎 +𝑏 :𝑎 ∈𝐴,𝑏 ∈𝐵}A+B:={a+b:a∈A,b∈B}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 𝐴𝐵 :={𝑎𝑏 :𝑎 ∈𝐴,𝑏 ∈𝐵}AB:={ab:a∈A,b∈B}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

同余类

对非零整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，把全体整数分成 |𝑚||m|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个两两不交的集合，且同一个集合中的任意两个数模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均同余，我们把这 |𝑚||m|![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个集合均称为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **同余类** 或 **剩余类** ．用 𝑟mod𝑚rmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示含有整数 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的同余类．

不难证明对任意非零整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，上述划分方案一定存在且唯一．

由同余类的定义可知：

  * 𝑟mod𝑚 ={𝑟 +𝑘𝑚 :𝑘 ∈𝐙}rmodm={r+km:k∈Z}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 𝑟mod𝑚 =𝑠mod𝑚 ⟺ 𝑟 ≡𝑠(mod𝑚)rmodm=smodm⟺r≡s(modm)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 对任意 𝑟,𝑠 ∈𝐙r,s∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要么 𝑟mod𝑚 =𝑠mod𝑚rmodm=smodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，要么 (𝑟mod𝑚) ∩(𝑠mod𝑚) =∅(rmodm)∩(smodm)=∅![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 若 𝑚1 ∣𝑚m1∣m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则对任意整数 𝑟r![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均有 𝑟 +𝑚𝐙 ⊆𝑟 +𝑚1𝐙r+mZ⊆r+m1Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

注意到同余是等价关系，所以同余类即为同余关系的等价类．

我们把模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的同余类全体构成的集合记为 𝐙𝑚Zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即

𝐙𝑚:={𝑟mod𝑚:0≤𝑟<𝑚}Zm:={rmodm:0≤r<m}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

不难发现：

  * 对任意整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑎 +𝐙𝑚 =𝐙𝑚a+Zm=Zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 对任意与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质的整数 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏𝐙𝑚 =𝐙𝑚bZm=Zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由 [商群](../../algebra/group-theory/#商群) 的定义可知 𝐙𝑚 =𝐙/𝑚𝐙Zm=Z/mZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以有时我们也会用 𝐙/𝑚𝐙Z/mZ![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝐙𝑚Zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

由 [抽屉原理](../../combinatorics/drawer-principle/) 可知：

  * 任取 𝑚 +1m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数，必有两个整数模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同余．
  * 存在 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个两两模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不同余的整数．

由此我们给出完全剩余系的定义：

（完全）剩余系

对 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数 𝑎1,𝑎2,…,𝑎𝑚a1,a2,…,am![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若对任意的数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有且仅有一个数 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同余，则称这 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数 𝑎1,𝑎2,…,𝑎𝑚a1,a2,…,am![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **完全剩余系** ，简称 **剩余系** ．

我们还可以定义模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的：

  * 最小非负（完全）剩余系：0,…,𝑚 −10,…,m−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 最小正（完全）剩余系：1,…,𝑚1,…,m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 绝对最小（完全）剩余系：−⌊𝑚/2⌋,…, −⌊ −𝑚/2⌋ −1−⌊m/2⌋,…,−⌊−m/2⌋−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 最大非正（完全）剩余系：−𝑚 +1,…,0−m+1,…,0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；
  * 最大负（完全）剩余系：−𝑚,…, −1−m,…,−1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

若无特殊说明，一般我们只用最小非负剩余系．

我们注意到如下命题成立：

  * 在模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的任意一个同余类中，任取两个整数 𝑎1,𝑎2a1,a2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均有 (𝑎1,𝑚) =(𝑎2,𝑚)(a1,m)=(a2,m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

考虑同余类 𝑟mod𝑚rmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 (𝑟,𝑚) =1(r,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则该同余类的所有元素均与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质，这说明我们也许可以通过类似方式得知所有与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质的整数构成的集合的结构．

既约同余类

对同余类 𝑟mod𝑚rmodm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 (𝑟,𝑚) =1(r,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则称该同余类为 **既约同余类** 或 **既约剩余类** ．

我们把模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 既约剩余类的个数记作 𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，称其为 [Euler 函数](../euler-totient/)．

我们把模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的既约同余类全体构成的集合记为 𝐙∗𝑚Zm∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即

𝐙∗𝑚:={𝑟mod𝑚:0≤𝑟<𝑚,(𝑟,𝑚)=1}Zm∗:={rmodm:0≤r<m,(r,m)=1}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)Warning

对于任意的整数 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质的整数 𝑏b![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑏𝐙∗𝑚 =𝐙∗𝑚bZm∗=Zm∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，但是 𝑎 +𝐙∗𝑚a+Zm∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不一定为 𝐙∗𝑚Zm∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．这一点与 𝐙𝑚Zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不同．

由 [抽屉原理](../../combinatorics/drawer-principle/) 可知：

  * 任取 𝜑(𝑚) +1φ(m)+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质的整数，必有两个整数模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同余．
  * 存在 𝜑(𝑚)φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个与 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质且两两模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 不同余的整数．

由此我们给出既约剩余系的定义：

既约剩余系

对 𝑡 =𝜑(𝑚)t=φ(m)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数 𝑎1,𝑎2,…,𝑎𝑡a1,a2,…,at![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，若 (𝑎𝑖,𝑚) =1, ∀1 ≤𝑖 ≤𝑡(ai,m)=1, ∀1≤i≤t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且对任意满足 (𝑥,𝑚) =1(x,m)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有且仅有一个数 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑎𝑖ai![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 同余，则称这 𝑡t![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个整数 𝑎1,𝑎2,…,𝑎𝑡a1,a2,…,at![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **既约剩余系** 、**缩剩余系** 或 **简化剩余系** ．

类似地，我们也可以定义最小非负既约剩余系等概念．

若无特殊说明，一般我们只用最小非负既约剩余系．

### 剩余系的复合

对正整数 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们有如下定理：

  * 若 𝑚 =𝑚1𝑚2, 1 ≤𝑚1,𝑚2m=m1m2, 1≤m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝑍𝑚1,𝑍𝑚2Zm1,Zm2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为模 𝑚1,𝑚2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **完全** 剩余系，则对任意与 𝑚1m1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 互质的 𝑎a![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均有：

𝑍𝑚=𝑎𝑍𝑚1+𝑚1𝑍𝑚2.Zm=aZm1+m1Zm2.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **完全** 剩余系．进而，若 𝑚 =∏𝑘𝑖=1𝑚𝑖, 1 ≤𝑚1,𝑚2,…,𝑚𝑘m=∏i=1kmi, 1≤m1,m2,…,mk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝑍𝑚1,…,𝑍𝑚𝑘Zm1,…,Zmk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为模 𝑚1,…,𝑚𝑘m1,…,mk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **完全** 剩余系，则：

𝑍𝑚=𝑘∑𝑖=1(𝑖−1∏𝑗=1𝑚𝑗)𝑍𝑚𝑖.Zm=∑i=1k(∏j=1i−1mj)Zmi.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **完全** 剩余系．

证明

只需证明对任意满足 𝑎𝑥 +𝑚1𝑦 ≡𝑎𝑥′ +𝑚1𝑦′(mod𝑚1𝑚2)ax+m1y≡ax′+m1y′(modm1m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 𝑥,𝑥′ ∈𝑍𝑚1x,x′∈Zm1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑦,𝑦′ ∈𝑍𝑚2y,y′∈Zm2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都有：

𝑎𝑥+𝑚1𝑦=𝑎𝑥′+𝑚1𝑦′.ax+m1y=ax′+m1y′.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

实际上，由 𝑚1 ∣𝑚1𝑚2m1∣m1m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，我们有 𝑎𝑥 +𝑚1𝑦 ≡𝑎𝑥′ +𝑚1𝑦′(mod𝑚1)ax+m1y≡ax′+m1y′(modm1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进而 𝑎𝑥 ≡𝑎𝑥′(mod𝑚1)ax≡ax′(modm1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 (𝑎,𝑚1) =1(a,m1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可知 𝑥 ≡𝑥′(mod𝑚1)x≡x′(modm1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，进而有 𝑥 =𝑥′x=x′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

进一步，𝑚1𝑦 ≡𝑚1𝑦′(mod𝑚1𝑚2)m1y≡m1y′(modm1m2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，则 𝑦 ≡𝑦′(mod𝑚2)y≡y′(modm2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑦 =𝑦′y=y′![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

因此，

𝑎𝑥+𝑚1𝑦=𝑎𝑥′+𝑚1𝑦′.ax+m1y=ax′+m1y′.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  * 若 𝑚 =𝑚1𝑚2, 1 ≤𝑚1,𝑚2,(𝑚1,𝑚2) =1m=m1m2, 1≤m1,m2,(m1,m2)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，令 𝑍∗𝑚1,𝑍∗𝑚2Zm1∗,Zm2∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为模 𝑚1,𝑚2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **既约** 剩余系，则：

𝑍∗𝑚=𝑚2𝑍∗𝑚1+𝑚1𝑍∗𝑚2.Zm∗=m2Zm1∗+m1Zm2∗.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **既约** 剩余系．

Tip

该定理等价于证明 Euler 函数为 积性函数．

证明

令 𝑍𝑚1,𝑍𝑚2Zm1,Zm2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 分别为模 𝑚1,𝑚2m1,m2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的完全剩余系，我们已经证明了

𝑍𝑚=𝑚2𝑍𝑚1+𝑚1𝑍𝑚2Zm=m2Zm1+m1Zm2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的完全剩余系．令 𝑀 ={𝑎 ∈𝑍𝑚 :(𝑎,𝑚) =1} ⊆𝑍𝑚M={a∈Zm:(a,m)=1}⊆Zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，显然 𝑀M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的既约剩余系，所以我们只需证明 𝑀 =𝑍∗𝑚M=Zm∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 即可．

显然 𝑍∗𝑚 ⊆𝑍𝑚Zm∗⊆Zm![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

任取 𝑚2𝑥 +𝑚1𝑦 ∈𝑀m2x+m1y∈M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑥 ∈𝑍𝑚1x∈Zm1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑦 ∈𝑍𝑚2y∈Zm2![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 (𝑚2𝑥 +𝑚1𝑦,𝑚1𝑚2) =1(m2x+m1y,m1m2)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 (𝑚1,𝑚2) =1(m1,m2)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可得

1=(𝑚2𝑥+𝑚1𝑦,𝑚1)=(𝑚2𝑥,𝑚1)=(𝑥,𝑚1),1=(m2x+m1y,m1)=(m2x,m1)=(x,m1),![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 1=(𝑚2𝑥+𝑚1𝑦,𝑚2)=(𝑚1𝑦,𝑚2)=(𝑦,𝑚2).1=(m2x+m1y,m2)=(m1y,m2)=(y,m2).![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此可得 𝑥 ∈𝑍∗𝑚1x∈Zm1∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑦 ∈𝑍∗𝑚2y∈Zm2∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑀 ⊆𝑍∗𝑚M⊆Zm∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

任取 𝑚2𝑥 +𝑚1𝑦 ∈𝑍∗𝑚m2x+m1y∈Zm∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑥 ∈𝑍∗𝑚1x∈Zm1∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑦 ∈𝑍∗𝑚2y∈Zm2∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 (𝑥,𝑚1) =1(x,m1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 (𝑦,𝑚2) =1(y,m2)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，由 (𝑚1,𝑚2) =1(m1,m2)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 可得

(𝑚2𝑥+𝑚1𝑦,𝑚1)=(𝑚2𝑥,𝑚1)=(𝑥,𝑚1)=1,(m2x+m1y,m1)=(m2x,m1)=(x,m1)=1,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) (𝑚2𝑥+𝑚1𝑦,𝑚2)=(𝑚1𝑦,𝑚2)=(𝑥,𝑚2)=1,(m2x+m1y,m2)=(m1y,m2)=(x,m2)=1,![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

因此可得 (𝑚2𝑥 +𝑚1𝑦,𝑚1𝑚2) =1(m2x+m1y,m1m2)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，即 𝑍∗𝑚 ⊆𝑀Zm∗⊆M![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

综上所述，

𝑍∗𝑚=𝑚2𝑍∗𝑚1+𝑚1𝑍∗𝑚2.Zm∗=m2Zm1∗+m1Zm2∗.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

为模 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的 **既约** 剩余系．

## 数论函数

数论函数（也称算术函数）指定义域为正整数的函数．数论函数也可以视作一个数列．

### 积性函数

定义

在数论中，若函数 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑓(1) =1f(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且 𝑓(𝑥𝑦) =𝑓(𝑥)𝑓(𝑦)f(xy)=f(x)f(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对任意互质的 𝑥,𝑦 ∈𝐍∗x,y∈N∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立，则 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **积性函数** ．

在数论中，若函数 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑓(1) =1f(1)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓(𝑥𝑦) =𝑓(𝑥)𝑓(𝑦)f(xy)=f(x)f(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对任意的 𝑥,𝑦 ∈𝐍∗x,y∈N∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立，则 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **完全积性函数** ．

#### 性质

若 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑔(𝑥)g(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 均为积性函数，则以下函数也为积性函数：

ℎ(𝑥)=𝑓(𝑥𝑝)ℎ(𝑥)=𝑓𝑝(𝑥)ℎ(𝑥)=𝑓(𝑥)𝑔(𝑥)ℎ(𝑥)=∑𝑑∣𝑥𝑓(𝑑)𝑔(𝑥𝑑)h(x)=f(xp)h(x)=fp(x)h(x)=f(x)g(x)h(x)=∑d∣xf(d)g(xd)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

对正整数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设其唯一质因数分解为 𝑥 =∏𝑝𝑘𝑖𝑖x=∏piki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为质数．

若 𝐹(𝑥)F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为积性函数，则有 𝐹(𝑥) =∏𝐹(𝑝𝑘𝑖𝑖)F(x)=∏F(piki)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

若 𝐹(𝑥)F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为完全积性函数，则有 𝐹(𝑥) =∏𝐹(𝑝𝑘𝑖𝑖) =∏𝐹(𝑝𝑖)𝑘𝑖F(x)=∏F(piki)=∏F(pi)ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 例子

  * 单位函数：𝜀(𝑛) =[𝑛 =1]ε(n)=[n=1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（完全积性）
  * 恒等函数：id𝑘⁡(𝑛) =𝑛𝑘idk⁡(n)=nk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，id1⁡(𝑛)id1⁡(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通常简记作 id⁡(𝑛)id⁡(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（完全积性）
  * 常数函数：1(𝑛) =11(n)=1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（完全积性）
  * 除数函数：𝜎𝑘(𝑛) =∑𝑑∣𝑛𝑑𝑘σk(n)=∑d∣ndk![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．𝜎0(𝑛)σ0(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通常简记作 𝑑(𝑛)d(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝜏(𝑛)τ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝜎1(𝑛)σ1(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 通常简记作 𝜎(𝑛)σ(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 欧拉函数：𝜑(𝑛) =∑𝑛𝑖=1[(𝑖,𝑛) =1]φ(n)=∑i=1n[(i,n)=1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 莫比乌斯函数：𝜇(𝑛) =⎧{ {⎨{ {⎩1𝑛=10∃𝑑>1,𝑑2∣𝑛(−1)𝜔(𝑛)otherwiseμ(n)={1n=10∃d>1,d2∣n(−1)ω(n)otherwise![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝜔(𝑛)ω(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的本质不同质因子个数．

### 加性函数

定义

在数论中，若函数 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑓(1) =0f(1)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓(𝑥𝑦) =𝑓(𝑥) +𝑓(𝑦)f(xy)=f(x)+f(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对任意互质的 𝑥,𝑦 ∈𝐍∗x,y∈N∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立，则 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **加性函数** ．

在数论中，若函数 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑓(1) =0f(1)=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 且 𝑓(𝑥𝑦) =𝑓(𝑥) +𝑓(𝑦)f(xy)=f(x)+f(y)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 对任意的 𝑥,𝑦 ∈𝐍∗x,y∈N∗![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都成立，则 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 **完全加性函数** ．

加性函数

本节中的加性函数指数论上的加性函数 (Additive function)，应与代数中的 Additive map 做区分．

#### 性质

对正整数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，设其唯一质因数分解为 𝑥 =∏𝑝𝑘𝑖𝑖x=∏piki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑝𝑖pi![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为质数．

若 𝐹(𝑥)F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为加性函数，则有 𝐹(𝑥) =∑𝐹(𝑝𝑘𝑖𝑖)F(x)=∑F(piki)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

若 𝐹(𝑥)F(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为完全加性函数，则有 𝐹(𝑥) =∑𝐹(𝑝𝑘𝑖𝑖) =∑𝐹(𝑝𝑖) ⋅𝑘𝑖F(x)=∑F(piki)=∑F(pi)⋅ki![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

#### 例子

为方便叙述，令所有质数组成的集合为 𝐏P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7).

  * 素因数分解中 𝑝p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的重数：𝜈𝑝(𝑛) =max{𝑘 ∈𝐍 :𝑝𝑘 ∣𝑛}νp(n)=max{k∈N:pk∣n}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中，𝑝 ∈𝐏p∈P![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（完全加性）
  * 所有质因子数目：Ω(𝑛) =∑𝑝∈𝐏𝜈𝑝(𝑛)Ω(n)=∑p∈Pνp(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（完全加性）
  * 相异质因子数目：𝜔(𝑛) =∑𝑝∈𝐏[𝑝 ∣𝑛]ω(n)=∑p∈P[p∣n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 所有质因子之和：𝑎0(𝑛) =∑𝑝∈𝐏𝜈𝑝(𝑛) ⋅𝑝a0(n)=∑p∈Pνp(n)⋅p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．（完全加性）
  * 相异质因子之和：𝑎1(𝑛) =∑𝑝∈𝐏[𝑝 ∣𝑛] ⋅𝑝a1(n)=∑p∈P[p∣n]⋅p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 取整函数

对于实数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，定义 **下取整函数** （floor function）和 **上取整函数** （ceiling function）分别为

⌊𝑥⌋=max{𝑘∈𝐙:𝑘≤𝑥}, ⌈𝑥⌉=min{𝑘∈𝐙:𝑘≥𝑥}.⌊x⌋=max{k∈Z:k≤x}, ⌈x⌉=min{k∈Z:k≥x}.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

利用下取整函数，一个实数可以分解为整数部分和小数部分：𝑥 =⌊𝑥⌋ +{𝑥}x=⌊x⌋+{x}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．其中，{𝑥}{x}![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的小数部分．

取整函数有如下基本性质：（𝑥 ∈𝐑, 𝑛 ∈𝐙x∈R, n∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

  * 𝑥 ∈𝐙 ⟺ 𝑥 =⌊𝑥⌋ =⌈𝑥⌉x∈Z⟺x=⌊x⌋=⌈x⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⌈𝑥⌉ −⌊𝑥⌋ =[𝑥 ∉𝐙]⌈x⌉−⌊x⌋=[x∉Z]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑥 −1 <⌊𝑥⌋ ≤𝑥 ≤⌈𝑥⌉ <𝑥 +1x−1<⌊x⌋≤x≤⌈x⌉<x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⌊ −𝑥⌋ = −⌈𝑥⌉, ⌈ −𝑥⌉ = −⌊𝑥⌋⌊−x⌋=−⌈x⌉, ⌈−x⌉=−⌊x⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⌊𝑥 +𝑛⌋ =⌊𝑥⌋ +𝑛, ⌈𝑥 +𝑛⌉ =⌈𝑥⌉ +𝑛⌊x+n⌋=⌊x⌋+n, ⌈x+n⌉=⌈x⌉+n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⌊𝑥⌋⌊x⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 ⌈𝑥⌉⌈x⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 都是关于 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的单调弱增函数．

证明关于下（上）取整函数的等式经常用到如下等价形式：（𝑥 ∈𝐑, 𝑛 ∈𝐙x∈R, n∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

  * ⌊𝑥⌋ =𝑛 ⟺ 𝑛 ≤𝑥 <𝑛 +1 ⟺ 𝑥 −1 <𝑛 ≤𝑥⌊x⌋=n⟺n≤x<n+1⟺x−1<n≤x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⌈𝑥⌉ =𝑛 ⟺ 𝑛 −1 <𝑥 ≤𝑛 ⟺ 𝑥 ≤𝑛 <𝑥 +1⌈x⌉=n⟺n−1<x≤n⟺x≤n<x+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

证明关于下（上）取整函数的不等式经常用到如下等价形式：（𝑥 ∈𝐑, 𝑛 ∈𝐙x∈R, n∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

  * 𝑥 <𝑛 ⟺ ⌊𝑥⌋ <𝑛x<n⟺⌊x⌋<n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑛 <𝑥 ⟺ 𝑛 <⌈𝑥⌉n<x⟺n<⌈x⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑥 ≤𝑛 ⟺ ⌈𝑥⌉ ≤𝑛x≤n⟺⌈x⌉≤n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑛 ≤𝑥 ⟺ 𝑛 ≤⌊𝑥⌋n≤x⟺n≤⌊x⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

涉及和、差的性质如下：（𝑥,𝑦 ∈𝐑x,y∈R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

  * ⌊𝑥⌋ +⌊𝑦⌋ ≤⌊𝑥 +𝑦⌋ ≤⌊𝑥⌋ +⌊𝑦⌋ +1⌊x⌋+⌊y⌋≤⌊x+y⌋≤⌊x⌋+⌊y⌋+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且恰有一个等号成立．
  * ⌈𝑥⌉ +⌈𝑦⌉ −1 ≤⌈𝑥 +𝑦⌉ ≤⌈𝑥⌉ +⌈𝑦⌉⌈x⌉+⌈y⌉−1≤⌈x+y⌉≤⌈x⌉+⌈y⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且恰有一个等号成立．
  * ⌊|𝑥 −𝑦|⌋ ≤|⌊𝑥⌋ −⌊𝑦⌋| ≤⌈|𝑥 −𝑦|⌉⌊|x−y|⌋≤|⌊x⌋−⌊y⌋|≤⌈|x−y|⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⌊|𝑥 −𝑦|⌋ ≤|⌈𝑥⌉ −⌈𝑦⌉| ≤⌈|𝑥 −𝑦|⌉⌊|x−y|⌋≤|⌈x⌉−⌈y⌉|≤⌈|x−y|⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

涉及商的性质如下：（𝑥 ∈𝐑, 𝑛 ∈𝐙, 𝑚 ∈𝐙+x∈R, n∈Z, m∈Z+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

  * ⌈𝑛𝑚⌉ =⌊𝑛+𝑚−1𝑚⌋, ⌊𝑛𝑚⌋ =⌈𝑛−𝑚+1𝑚⌉⌈nm⌉=⌊n+m−1m⌋, ⌊nm⌋=⌈n−m+1m⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⌊𝑥+𝑛𝑚⌋ =⌊⌊𝑥⌋+𝑛𝑚⌋, ⌈𝑥+𝑛𝑚⌉ =⌈⌈𝑥⌉+𝑛𝑚⌉⌊x+nm⌋=⌊⌊x⌋+nm⌋, ⌈x+nm⌉=⌈⌈x⌉+nm⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⌊⌊𝑥/𝑛⌋𝑚⌋ =⌊𝑥𝑛𝑚⌋, ⌈⌈𝑥/𝑛⌉𝑚⌉ =⌈𝑥𝑛𝑚⌉⌊⌊x/n⌋m⌋=⌊xnm⌋, ⌈⌈x/n⌉m⌉=⌈xnm⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 对于 𝑥 >0x>0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，有 ⌊𝑥𝑚⌋ =⌊𝑥⌋∑𝑘=1[𝑚 ∣𝑘]⌊xm⌋=∑k=1⌊x⌋[m∣k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

其中，第二条和第三条性质都可以看作是如下结论的直接推论：

  * 设 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为连续单增函数，且只要 𝑓(𝑥) ∈𝐙f(x)∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，就有 𝑥 ∈𝐙x∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，那么

⌊𝑓(𝑥)⌋=⌊𝑓(⌊𝑥⌋)⌋, ⌈𝑓(𝑥)⌉=⌈𝑓(⌈𝑥⌉)⌉.⌊f(x)⌋=⌊f(⌊x⌋)⌋, ⌈f(x)⌉=⌈f(⌈x⌉)⌉.![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 证明

由对称性，只需要证明第一个等式．如果 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是整数，那么命题显然．否则，⌊𝑥⌋ <𝑥⌊x⌋<x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和下取整函数的单调性可知，⌊𝑓(𝑥)⌋ ≥⌊𝑓(⌊𝑥⌋)⌋⌊f(x)⌋≥⌊f(⌊x⌋)⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．如果等号不成立，那么设 𝑦 =⌊𝑓(𝑥)⌋y=⌊f(x)⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，它满足 ⌊𝑓(⌊𝑥⌋)⌋ <𝑦 ≤⌊𝑓(𝑥)⌋⌊f(⌊x⌋)⌋<y≤⌊f(x)⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这等价于 𝑓(⌊𝑥⌋) <𝑦 ≤𝑓(𝑥)f(⌊x⌋)<y≤f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．由 𝑓f![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的连续性可知，存在 ⌊𝑥⌋ <𝑥0 ≤𝑥⌊x⌋<x0≤x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 使得 𝑓(𝑥0) =𝑦f(x0)=y![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．因为 𝑦 ∈𝐙y∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，所以 𝑥0 ∈𝐙x0∈Z![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，这与 ⌊𝑥⌋⌊x⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的定义矛盾．故而，等号成立，即 ⌊𝑓(𝑥)⌋ =⌊𝑓(⌊𝑥⌋)⌋⌊f(x)⌋=⌊f(⌊x⌋)⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

最后是一组关于带有取整函数的求和式的结论：（𝑥 ∈𝐑, 𝑛 ∈𝐙, 𝑚 ∈𝐙+x∈R, n∈Z, m∈Z+![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）

  * 𝑛 =⌊𝑛2⌋ +⌈𝑛2⌉n=⌊n2⌋+⌈n2⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑛 =⌊𝑛𝑚⌋ +⌊𝑛+1𝑚⌋ +⋯ +⌊𝑛+𝑚−1𝑚⌋n=⌊nm⌋+⌊n+1m⌋+⋯+⌊n+m−1m⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 𝑛 =⌈𝑛𝑚⌉ +⌈𝑛−1𝑚⌉ +⋯ +⌈𝑛−𝑚+1𝑚⌉n=⌈nm⌉+⌈n−1m⌉+⋯+⌈n−m+1m⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⌊𝑚𝑥⌋ =⌊𝑥⌋ +⌊𝑥+1𝑚⌋ +⋯ +⌊𝑥+𝑚−1𝑚⌋⌊mx⌋=⌊x⌋+⌊x+1m⌋+⋯+⌊x+m−1m⌋![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * ⌈𝑚𝑥⌉ =⌈𝑥⌉ +⌈𝑥−1𝑚⌉ +⋯ +⌈𝑥−𝑚−1𝑚⌉⌈mx⌉=⌈x⌉+⌈x−1m⌉+⋯+⌈x−m−1m⌉![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 当 𝑚 ⟂𝑛m⟂n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑚−1∑𝑘=1⌊𝑘𝑛𝑚⌋ =12(𝑛 −1)(𝑚 −1)∑k=1m−1⌊knm⌋=12(n−1)(m−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．
  * 当 𝑚 ⟂𝑛m⟂n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 时，𝑚−1∑𝑘=1⌈𝑘𝑛𝑚⌉ =12(𝑛 +1)(𝑚 −1)∑k=1m−1⌈knm⌉=12(n+1)(m−1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

这些乃至更一般的类似形式求和式的推导可以参考 [类欧几里得算法](../euclidean/) 页面．

取整函数的更多性质以及应用可以参考如下页面：

  * 取模运算：𝑛mod𝑚 =𝑛 −⌊𝑛𝑚⌋𝑚nmodm=n−⌊nm⌋m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．它可以用于 [优化整数取模运算](../mod-arithmetic/#相关算法)．
  * 利用 Gauss 引理证明 [二次互反律](../quad-residue/#二次互反律)．
  * [数论分块](../sqrt-decomposition/)，尤其是它的性质证明部分．
  * 计算阶乘中素数因子幂次的 [Legendre 公式](../factorial/#legendre-公式)．
  * [Beatty 数列](../../game-theory/impartial-game/#wythoff-游戏)、Rayleigh 定理以及 Wythoff 博弈．

## 参考资料与注释

  * 潘承洞，潘承彪．初等数论．北京大学出版社．
  * [Floor and ceiling functions - Wikipedia](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions)
  * Graham, Ronald L., Donald E. Knuth, and Oren Patashnik. "Concrete mathematics: a foundation for computer science." (1989).

* * *

  1. [std::gcd - cppreference.com](https://en.cppreference.com/w/cpp/numeric/gcd) ↩

  2. [Are all primes (past 2 and 3) of the forms 6n+1 and 6n-1?](https://primes.utm.edu/notes/faq/six.html) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/basic.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/number-theory/basic.md "edit.link.title")  
>  __本页面贡献者：[c-forrest](https://github.com/c-forrest), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [HeRaNO](https://github.com/HeRaNO), [ksyx](https://github.com/ksyx), [383494](https://github.com/383494), [buuzzing](https://github.com/buuzzing), [cr4c1an](https://github.com/cr4c1an), [Emp7iness](https://github.com/Emp7iness), [jifbt](https://github.com/jifbt), [Kaiser-Yang](https://github.com/Kaiser-Yang), [Koishilll](https://github.com/Koishilll), [Marcythm](https://github.com/Marcythm), [Qiu-Quanzhi](https://github.com/Qiu-Quanzhi), [SaisycJiang](https://github.com/SaisycJiang), [sshwy](https://github.com/sshwy), [StarryReverie](https://github.com/StarryReverie), [StudyingFather](https://github.com/StudyingFather), [Xeonacid](https://github.com/Xeonacid), [xyf007](https://github.com/xyf007)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
