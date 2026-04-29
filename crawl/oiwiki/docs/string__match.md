# 字符串匹配 - OI Wiki

- Source: https://oi-wiki.org/string/match/

# 字符串匹配

本页面将简述字符串匹配问题以及它的解法．

## 字符串匹配问题

### 定义

又称模式匹配（pattern matching）．该问题可以概括为「给定字符串 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，在主串 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中寻找子串 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)」．字符 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 称为模式串 (pattern)．

### 类型

  * 单串匹配：给定一个模式串和一个待匹配串，找出前者在后者中的所有位置．
  * 多串匹配：给定多个模式串和一个待匹配串，找出这些模式串在后者中的所有位置．
    * 出现多个待匹配串时，将它们直接连起来便可作为一个待匹配串处理．
    * 可以直接当做单串匹配，但是效率不够高．
  * 其他类型：例如匹配一个串的任意后缀，匹配多个串的任意后缀……

## 暴力做法

简称 BF (Brute Force) 算法．该算法的基本思想是从主串 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第一个字符开始和模式串 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第一个字符进行比较，若相等，则继续比较二者的后续字符；否则，模式串 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 回退到第一个字符，重新和主串 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的第二个字符进行比较．如此往复，直到 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 或 𝑇T![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 中所有字符比较完毕．

### 实现

C++Python

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` |  ```text /* * s：待匹配的主串 * t：模式串 * n：主串的长度 * m：模式串的长度 */ std :: vector < int > match ( char * s , char * t , int n , int m ) { std :: vector < int > ans ; int i , j ; for ( i = 0 ; i < n \- m \+ 1 ; i ++ ) { for ( j = 0 ; j < m ; j ++ ) { if ( s [ i \+ j ] != t [ j ]) break ; } if ( j == m ) ans . push_back ( i ); } return ans ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text def match ( s , t , n , m ): if m < 1 : return [] ans = [] for i in range ( 0 , n \- m \+ 1 ): for j in range ( 0 , m ): if s [ i \+ j ] != t [ j ]: break else : ans . append ( i ) return ans ```   
---|---  
  
### 时间复杂度

设 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为主串的长度，𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为模式串的长度．默认 𝑚 ≪𝑛m≪n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

BF 算法匹配成功时，在最好情况下，只有一趟匹配成功，此趟比较次数为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，而其余每趟不成功的匹配都发生在模式串的第一个字符，还需要 𝑛 −𝑚n−m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次比较，总比较次数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；在最坏情况下，匹配成功的趟数为 𝑛 −𝑚 +1n−m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，每趟比较次数为 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，总比较次数为 𝑚(𝑛 −𝑚 +1)m(n−m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，故时间复杂度为 𝑂(𝑚𝑛)O(mn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

BF 算法匹配失败时，在最好情况下，每趟不成功的匹配都发生在模式串的第一个字符，BF 算法要执行 𝑛 −𝑚 +1n−m+1![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次比较，时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)；在最坏情况下，每趟不成功的匹配都发生在模式串的最后一个字符，BF 算法要执行 𝑚(𝑛 −𝑚 +1)m(n−m+1)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 次比较，时间复杂度为 𝑂(𝑚𝑛)O(mn)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如果模式串有至少两个不同的字符，则 BF 算法的平均时间复杂度为 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．但是在 OI 题目中，给出的字符串一般都不是纯随机的．

## Hash 的方法

参见：[字符串哈希](../hash/)

## KMP 算法

参见：[前缀函数与 KMP 算法](../kmp/)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/string/match.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/string/match.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Xeonacid](https://github.com/Xeonacid), [Enter-tainer](https://github.com/Enter-tainer), [iamtwz](https://github.com/iamtwz), [ksyx](https://github.com/ksyx), [abc1763613206](https://github.com/abc1763613206), [f1rstmehul](https://github.com/f1rstmehul), [HeRaNO](https://github.com/HeRaNO), [karman011](https://github.com/karman011), [Menci](https://github.com/Menci), [NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [shawlleyw](https://github.com/shawlleyw), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
