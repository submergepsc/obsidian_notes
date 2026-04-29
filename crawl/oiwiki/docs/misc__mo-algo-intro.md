# 莫队算法简介 - OI Wiki

- Source: https://oi-wiki.org/misc/mo-algo-intro/

# 莫队算法简介

莫队算法是由莫涛提出的算法．在莫涛提出莫队算法之前，莫队算法已经在 Codeforces 的高手圈里小范围流传，但是莫涛是第一个对莫队算法进行详细归纳总结的人．莫涛提出莫队算法时，只分析了普通莫队算法，但是经过 OIer 和 ACMer 的集体智慧改造，莫队有了多种扩展版本．

莫队算法可以解决一类离线区间询问问题，适用性极为广泛．同时将其加以扩展，便能轻松处理树上路径询问以及支持修改操作．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/misc/mo-algo-intro.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/misc/mo-algo-intro.md "edit.link.title")  
>  __本页面贡献者：[countercurrent-time](https://github.com/countercurrent-time), [Ir1d](https://github.com/Ir1d), [Backl1ght](https://github.com/Backl1ght), [greyqz](https://github.com/greyqz), [MicDZ](https://github.com/MicDZ), [ouuan](https://github.com/ouuan), [StudyingFather](https://github.com/StudyingFather), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
