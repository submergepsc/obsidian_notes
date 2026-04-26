# 排序简介 - OI Wiki

- Source: https://oi-wiki.org/basic/sort-intro/

# 排序简介

本页面将简要介绍排序算法．

## 定义

**排序算法** （英语：Sorting algorithm）是一种将一组特定的数据按某种顺序进行排列的算法．排序算法多种多样，性质也大多不同．

## 性质

### 稳定性

稳定性是指相等的元素经过排序之后相对顺序是否发生了改变．

拥有稳定性这一特性的算法会让原本有相等键值的纪录维持相对次序，即如果一个排序算法是稳定的，当有两个相等键值的纪录 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 和 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，且在原本的列表中 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 出现在 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之前，在排序过的列表中 𝑅R![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 也将会是在 𝑆S![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之前．

基数排序、计数排序、插入排序、冒泡排序、归并排序是稳定排序．

选择排序、堆排序、快速排序、希尔排序不是稳定排序．

### 时间复杂度

主页面：[复杂度](../complexity/)

时间复杂度用来衡量一个算法的运行时间和输入规模的关系，通常用 𝑂O![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 表示．

简单计算复杂度的方法一般是统计「简单操作」的执行次数，有时候也可以直接数循环的层数来近似估计．

时间复杂度分为最优时间复杂度、平均时间复杂度和最坏时间复杂度．OI 竞赛中要考虑的一般是最坏时间复杂度，因为它代表的是算法运行水平的下界，在评测中不会出现更差的结果了．

基于比较的排序算法的时间复杂度下限是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．

当然也有不是 𝑂(𝑛log⁡𝑛)O(nlog⁡n)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的．例如，[计数排序](../counting-sort/) 的时间复杂度是 𝑂(𝑛 +𝑤)O(n+w)![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)，其中 𝑤w![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 代表输入数据的值域大小．

以下是几种排序算法的比较．

![几种排序算法的比较](./images/sort-intro-1.apng)

### 空间复杂度

与时间复杂度类似，空间复杂度用来描述算法空间消耗的规模．一般来说，空间复杂度越小，算法越好．

## 外部链接

  * [排序算法 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/sort-intro.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/sort-intro.md "edit.link.title")  
>  __本页面贡献者：[NachtgeistW](https://github.com/NachtgeistW), [Alisahhh](https://github.com/Alisahhh), [Backl1ght](https://github.com/Backl1ght), [ChungZH](https://github.com/ChungZH), [Enter-tainer](https://github.com/Enter-tainer), [Great-designer](https://github.com/Great-designer), [iamtwz](https://github.com/iamtwz), [Junyan721113](https://github.com/Junyan721113), [ouuan](https://github.com/ouuan), [partychicken](https://github.com/partychicken), [Tiphereth-A](https://github.com/Tiphereth-A)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
