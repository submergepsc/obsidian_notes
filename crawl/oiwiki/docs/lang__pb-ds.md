# pb_ds 简介 - OI Wiki

- Source: https://oi-wiki.org/lang/pb-ds/

# pb_ds 简介

pb_ds 库全称 Policy-Based Data Structures．

pb_ds 库封装了很多数据结构，比如哈希（Hash）表，平衡二叉树，字典树（Trie 树），堆（优先队列）等．

就像 `vector`、`set`、`map` 一样，其组件均符合 STL 的相关接口规范．部分（如优先队列）包含 STL 内对应组件的所有功能，但比 STL 功能更多．

pb_ds 只在使用 libstdc++ 为标准库的编译器下可以用．

可以使用 `begin()` 和 `end()` 来获取 `iterator` 从而遍历

可以 `increase_key`,`decrease_key` 以及删除单个元素

由于 pb_ds 库的主要内容在以下划线开头的 `__gnu_pbds` 命名空间中，在 NOI 系列活动中的合规性一直没有确定．2021 年 9 月 1 日，根据 [《关于 NOI 系列活动中编程语言使用限制的补充说明》](https://www.noi.cn/xw/2021-09-01/735729.shtml)，允许使用以下划线开头的库函数或宏（但具有明确禁止操作的库函数和宏除外），在 NOI 系列活动中使用 pb_ds 库的合规性有了文件上的依据．

**参考资料：[《C++ 的 pb_ds 库在 OI 中的应用》](https://github.com/OI-Wiki/libs/blob/master/lang/pb-ds/C%2B%2B的pb_ds库在OI中的应用.pdf)**

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/pb-ds/index.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/lang/pb-ds/index.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Xeonacid](https://github.com/Xeonacid), [HeRaNO](https://github.com/HeRaNO), [saffahyjp](https://github.com/saffahyjp), [Tiphereth-A](https://github.com/Tiphereth-A), [Enter-tainer](https://github.com/Enter-tainer), [HarryJam3](https://github.com/HarryJam3), [ouuan](https://github.com/ouuan)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
