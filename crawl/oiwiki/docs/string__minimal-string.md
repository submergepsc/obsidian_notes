# 最小表示法 - OI Wiki

- Source: https://oi-wiki.org/string/minimal-string/

# 最小表示法

## 定义

最小表示法是用于解决字符串最小表示问题的方法．

## 字符串的最小表示

### 循环同构

当字符串 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中可以选定一个位置 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足

𝑆[𝑖⋯𝑛]+𝑆[1⋯𝑖−1]=𝑇S[i⋯n]+S[1⋯i−1]=T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

则称 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 与 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 循环同构

### 最小表示

字符串 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的最小表示为与 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 循环同构的所有字符串中字典序最小的字符串

## simple 的暴力

我们每次比较 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 开始的循环同构，把当前比较到的位置记作 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每次遇到不一样的字符时便把大的跳过，最后剩下的就是最优解．

### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text int k = 0 , i = 0 , j = 1 ; while ( k < n && i < n && j < n ) { if ( sec [( i \+ k ) % n ] == sec [( j \+ k ) % n ]) { ++ k ; } else { if ( sec [( i \+ k ) % n ] > sec [( j \+ k ) % n ]) ++ i ; else ++ j ; k = 0 ; if ( i == j ) i ++ ; } } i = min ( i , j ); ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text k , i , j = 0 , 0 , 1 while k < n and i < n and j < n : if sec [( i \+ k ) % n ] == sec [( j \+ k ) % n ]: k += 1 else : if sec [( i \+ k ) % n ] > sec [( j \+ k ) % n ]: i += 1 else : j += 1 k = 0 if i == j : i += 1 i = min ( i , j ) ```   
---|---  
  
### 解释

该实现方法随机数据下表现良好，但是可以构造特殊数据卡掉．

例如：对于 𝚊𝚊𝚊⋯𝚊𝚊𝚋aaa⋯aab![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 不难发现这个算法的复杂度退化为 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们发现，当字符串中出现多个连续重复子串时，此算法效率降低，我们考虑优化这个过程．

## 最小表示法

### 算法核心

考虑对于一对字符串 𝐴,𝐵A,B![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 它们在原字符串 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中的起始位置分别为 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 且它们的前 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 个字符均相同，即

𝑆[𝑖⋯𝑖+𝑘−1]=𝑆[𝑗⋯𝑗+𝑘−1]S[i⋯i+k−1]=S[j⋯j+k−1]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

不妨先考虑 𝑆[𝑖 +𝑘] >𝑆[𝑗 +𝑘]S[i+k]>S[j+k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的情况，我们发现起始位置下标 𝑙l![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 满足 𝑖 ≤𝑙 ≤𝑖 +𝑘i≤l≤i+k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的字符串均不能成为答案．因为对于任意一个字符串 𝑆𝑖+𝑝Si+p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（表示以 𝑖 +𝑝i+p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为起始位置的字符串，𝑝 ∈[0,𝑘]p∈[0,k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)）一定存在字符串 𝑆𝑗+𝑝Sj+p![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 比它更优．

所以我们比较时可以跳过下标 𝑙 ∈[𝑖,𝑖 +𝑘]l∈[i,i+k]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7), 直接比较 𝑆𝑖+𝑘+1Si+k+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

这样，我们就完成了对于上文暴力的优化．

### 时间复杂度

𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### 过程

  1. 初始化指针 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，𝑗j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；初始化匹配长度 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为 00![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
  2. 比较第 𝑘k![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 位的大小，根据比较结果跳转相应指针．若跳转后两个指针相同，则随意选一个加一以保证比较的两个字符串不同
  3. 重复上述过程，直到比较结束
  4. 答案为 𝑖,𝑗i,j![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中较小的一个

### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text int k = 0 , i = 0 , j = 1 ; while ( k < n && i < n && j < n ) { if ( sec [( i \+ k ) % n ] == sec [( j \+ k ) % n ]) { k ++ ; } else { sec [( i \+ k ) % n ] > sec [( j \+ k ) % n ] ? i = i \+ k \+ 1 : j = j \+ k \+ 1 ; if ( i == j ) i ++ ; k = 0 ; } } i = min ( i , j ); ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text k , i , j = 0 , 0 , 1 while k < n and i < n and j < n : if sec [( i \+ k ) % n ] == sec [( j \+ k ) % n ]: k += 1 else : if sec [( i \+ k ) % n ] > sec [( j \+ k ) % n ]: i = i \+ k \+ 1 else : j = j \+ k \+ 1 if i == j : i += 1 k = 0 i = min ( i , j ) ```   
---|---  
  
* * *

> __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/minimal-string.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/minimal-string.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [partychicken](https://github.com/partychicken), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [Early0v0](https://github.com/Early0v0), [Enter-tainer](https://github.com/Enter-tainer), [H-J-Granger](https://github.com/H-J-Granger), [iamtwz](https://github.com/iamtwz), [NachtgeistW](https://github.com/NachtgeistW), [Suyun514](mailto:suyun514@qq.com), [Xeonacid](https://github.com/Xeonacid), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [ezoixx130](https://github.com/ezoixx130), [fjzzq2002](https://github.com/fjzzq2002), [GavinZhengOI](https://github.com/GavinZhengOI), [GekkaSaori](https://github.com/GekkaSaori), [Gesrua](https://github.com/Gesrua), [Junyan721113](https://github.com/Junyan721113), [karin0](https://github.com/karin0), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [kxccc](https://github.com/kxccc), [LovelyBuggies](https://github.com/LovelyBuggies), [lychees](https://github.com/lychees), [Makkiy](https://github.com/Makkiy), [Menci](https://github.com/Menci), [mgt](mailto:i@margatroid.xyz), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [Peanut-Tang](https://github.com/Peanut-Tang), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [shawlleyw](https://github.com/shawlleyw), [sshwy](https://github.com/sshwy), [SukkaW](https://github.com/SukkaW), [Tiphereth-A](https://github.com/Tiphereth-A), [TrisolarisHD](mailto:orzcyand1317@gmail.com), [weiyong1024](https://github.com/weiyong1024)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
