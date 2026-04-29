# 分段打表 - OI Wiki

- Source: https://oi-wiki.org/contest/dictionary/

# 分段打表

前置知识：[分块](../../ds/decompose/)．

朴素的打表，指的是在比赛时把所有可能的输入对应的答案都计算出来并保存下来，然后在代码里开个数组把答案放里面，直接输出即可．

注意这个技巧只适用于输入的值域不大（如，输入只有一个数，而且范围很小）的问题，否则可能会导致代码过长、MLE、打表需要的时间过长等问题．

例题

规定 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 为整数 𝑥x![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的二进制表示中 11![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的个数．输入一个正整数 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)(𝑛 ≤109n≤109![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7))，输出 ∑𝑛𝑖=1𝑓2(𝑖)∑i=1nf2(i)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

如果对于每一个 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，都输出 𝑓(𝑛)f(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的话，除了可能会 MLE 外，还有可能代码超过最大代码长度限制，导致编译不通过．

我们考虑优化这个答案表．采用 [分块](../../ds/decompose/) 的思想，我们设置一个合理的步长 𝑚m![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)（这个步长一般视代码长度而定），对于第 𝑖i![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 块，计算出：

𝑛𝑖𝑚∑𝑘=𝑛𝑚(𝑖−1)+1𝑓2(𝑘)∑k=nm(i−1)+1nimf2(k)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

的值．

然后输出答案时采用分块思想处理即可．即，整块的答案用预处理的值计算，非整块的答案暴力计算．

一般来说，这样的问题对于处理单个函数值 𝑓(𝑥)f(x)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 很快，但是需要大量函数值求和（求积或某些可以快速合并的操作），枚举会超出时间限制，在找不到标准做法的情况下，分段打表是一个不错的选择．

注意事项

当上题中指数不是定值，但是范围较小，也可以考虑打表．

### 例题

[「BZOJ 3798」特殊的质数](https://hydro.ac/p/bzoj-P3798)：求 [𝑙,𝑟][l,r]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 区间内有多少个质数可以分解为两个正整数的平方和．

[「Luogu P1822」魔法指纹](https://www.luogu.com.cn/problem/P1822)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/contest/dictionary.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/contest/dictionary.md "edit.link.title")  
>  __本页面贡献者：[greyqz](https://github.com/greyqz), [Ir1d](https://github.com/Ir1d), [ouuan](https://github.com/ouuan), [HeRaNO](https://github.com/HeRaNO), [sshwy](https://github.com/sshwy), [billchenchina](https://github.com/billchenchina), [Enter-tainer](https://github.com/Enter-tainer), [Tiphereth-A](https://github.com/Tiphereth-A), [Chrogeek](https://github.com/Chrogeek), [Great-designer](https://github.com/Great-designer), [Henry-ZHR](https://github.com/Henry-ZHR), [Junyan721113](https://github.com/Junyan721113), [Macesuted](https://github.com/Macesuted), [Molmin](https://github.com/Molmin)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
