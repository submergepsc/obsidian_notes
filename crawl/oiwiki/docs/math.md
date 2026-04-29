# 数学部分简介 - OI Wiki

- Source: https://oi-wiki.org/math/

# 数学部分简介

本章介绍 OI 中可能会用到的数学知识．计算机科学与数学紧密相关，而在算法竞赛中尤其强调以数论、排列组合、概率期望、多项式为代表离散、具体的数学：其注重程序实现和现实问题，可以出现在几乎任何类别的题目中．

实际上，算法竞赛中涉及到的算法和数据结构以及自动机等也可以被认为属于数学范畴，但是这些内容被细分到诸如字符串等的具体章节加以应用背景以更好理解．本章主要介绍数学中一些基础概念、代数、数论、博弈论及概率论等知识．运用这些知识可以帮助优化其他算法和数据结构，例如：

  * 用多项式优化卷积形式的背包，来做一些字符串题．
  * 很多递推类型的题背景都是排列组合或概率期望，可以更进一步用生成函数推导和解决，以及使用基于 FFT 的分治优化算法效率．
  * 利用同余和环分析图上非简单路径在模意义下可能的权值和，并用带权并查集维护．

此外，高中数学是信息学竞赛数学的基础，学好课本上的基本概念和性质能更好地帮助学习本章内容．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/index.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/math/index.md "edit.link.title")  
>  __本页面贡献者：[hsfzLZH1](https://github.com/hsfzLZH1), [Ir1d](https://github.com/Ir1d), [sshwy](https://github.com/sshwy), [Xeonacid](https://github.com/Xeonacid), [i-yyi](https://github.com/i-yyi), [MegaOwIer](https://github.com/MegaOwIer), [Catreap](https://github.com/Catreap), [Chrogeek](https://github.com/Chrogeek), [CommonAnts](https://github.com/CommonAnts), [DCDCBigBig](https://github.com/DCDCBigBig), [Enter-tainer](https://github.com/Enter-tainer), [greyqz](https://github.com/greyqz), [ksyx](https://github.com/ksyx), [luoguyuntianming](https://github.com/luoguyuntianming), [mgt](mailto:i@margatroid.xyz), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A), [zmxqs](https://github.com/zmxqs)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
