# 离线算法简介 - OI Wiki

- Source: https://oi-wiki.org/misc/offline/

# 离线算法简介

本章将介绍介绍离线算法（Offline Algorithm）的思想、常见算法及优化．

离线算法是基于「**求解前已知所有数据** 」这一假设来设计的，适用于有多组询问的题目．相对的还有 [在线算法](https://en.wikipedia.org/wiki/Online_algorithm)（Online Algorithm）．

例如 [选择排序](../../basic/selection-sort/) 必须知道数组的全局最小元素才能执行，所以是离线算法，而 [插入排序](../../basic/insertion-sort/) 可以动态接收数据进行排序，不强制要求执行前已知全部数据，所以是在线算法．

对于相同的问题，在设计难度等方面，离线算法往往优于在线算法．为了阻止选手使用离线算法，有时题目会使用「强制在线」的方式，常见的有需要前一个询问的答案才能得到下一个询问的参数（[交互题](../../contest/problems/#交互题) 与 [通信题](../../contest/problems/#通信题) 也属于此类）．

离线算法的常见思路包括将询问统一求解（如 [CDQ 分治](../cdq-divide/)）、通过一个询问的答案求出另外相似询问的答案（如 [整体二分](../parallel-binsearch/) 和 [莫队算法](../mo-algo-intro/)）等．

由于离线算法是一种思想而并不是某种具体的算法，因此它会搭配各种各样的数据结构或算法一起使用，与之相关的题目种类也更为繁杂．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/offline.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/offline.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [Oracynx](https://github.com/Oracynx)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
