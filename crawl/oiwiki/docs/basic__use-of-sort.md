# 排序应用 - OI Wiki

- Source: https://oi-wiki.org/basic/use-of-sort/

# 排序应用

本页面将简要介绍排序的用法．

## 理解数据的特点

使用排序处理数据有利于理解数据的特点，方便我们之后的分析与视觉化．像一些生活中的例子比如词典，菜单，如果不是按照一定顺序排列的话，人们想要找到自己需要的东西的时间就会大大增加．

计算机需要处理大规模的数据，排序后，人们可以根据数据的特点和需求来设计计算机的后续处理流程．

## 降低时间复杂度

使用排序预处理可以降低求解问题所需要的时间复杂度，通常是一个以空间换取时间的平衡．如果一个排序好的列表需要被多次分析的话，只需要耗费一次排序所需要的资源是很划算的，因为之后的每次分析都可以减少很多时间．

示例：检查给定数列中是否有相等的元素

考虑一个数列，你需要检查其中是否有元素相等．

一个朴素的做法是检查每一个数对，并判断这一对数是否相等．时间复杂度是 𝑂(𝑛2)O(n2)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

我们不妨先对这一列数排序，之后不难发现：如果有相等的两个数，它们一定在新数列中处于相邻的位置上．这时，只需要 𝑂(𝑛)O(n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 地扫一遍新数列了．

总的时间复杂度是排序的复杂度 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)．

## 作为查找的预处理

排序是 [二分查找](../binary/) 所要做的预处理工作．在排序后使用二分查找，可以以 𝑂(log⁡𝑛)O(log⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的时间在序列中查找指定的元素．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/use-of-sort.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/use-of-sort.md "edit.link.title")  
>  __本页面贡献者：[sshwy](https://github.com/sshwy), [Enter-tainer](https://github.com/Enter-tainer), [leoleoasd](https://github.com/leoleoasd), [NachtgeistW](https://github.com/NachtgeistW), [partychicken](https://github.com/partychicken), [Persdre](https://github.com/Persdre), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
