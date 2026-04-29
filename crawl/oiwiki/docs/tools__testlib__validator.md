# Validator - OI Wiki

- Source: https://oi-wiki.org/tools/testlib/validator/

# Validator

前置知识：[通用](../general/)

本页面将简要介绍 validator 的概念与用法．

## 概述

Validator（中文：校验器）用于检验造好的数据的合法性．当造好一道题的数据，又担心数据不合法（不符合题目的限制条件：上溢、图不连通、不是树……）时，出题者通常会借助 validator 来检查．1

因为 Coderforces 支持 hack 功能，所以所有 Codeforces 上的题目都必须要有 validator．UOJ 也如此．[Polygon](../../polygon/) 内建了对 validator 的支持．

## 使用方法

直接在命令行输入 `./val` 即可．数据通过 stdin 输入．如果想从文件输入可 `./val < a.in`．

若数据没有问题，则什么都不会输出且返回 0；否则会输出错误信息并返回一个非 0 值．

## 提示

  * 写 validator 时，不能对被 validate 的数据做任何假设，因为它可能包含任何内容．因此，出题者要对各种不合法的情况进行判断（使用 Testlib 会大大简化这一流程）．
    * 例如，输入一个点数为 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 的树，主要工作是判断 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 是否符合范围和判断输入的是树与否．但是切不可在判断过 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 范围之后就不对接下来输入的边的起点与终点的范围进行判断，否则可能会导致 validator RE．
    * 即使不会 RE 也不应该不判断，这会导致你的报错不正确．如上例，如果不判断，报错可能会是「不是一棵树」，但是正确的报错应当是「边起点/终点不在 [1,𝑛][1,n]![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 之间」．
  * 不能对选手的读入方式做任何假设．因此，必须保证能通过 validate 的数据完全符合输入格式．
    * 例如，选手可能逐字符地读入数字，在数字与数字之间只读入一个空格．所以在编写 validator 时，数据中的每一个空白字符都要在 validator 中显式地读入（如空格和换行）．
  * 结束时不要忘记 `inf.readEof()`．
  * 如果题目开放 hack（或者说，validator 的错误信息会给别人看），请使报错信息尽量友好．
    * 读入变量时使用「项别名」．
    * 在判断使用的表达式不那么易懂时，使用 ensuref 而非 ensure．

## 示例

以下是 [CF Gym 100541A - Stock Market](https://codeforces.com/gym/100541/problem/A) 的 validator：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` |  ```text #include "testlib.h" int main ( int argc , char * argv []) { registerValidation ( argc , argv ); int testCount = inf . readInt ( 1 , 10 , "testCount" ); inf . readEoln (); for ( int i = 0 ; i < testCount ; i ++ ) { int n = inf . readInt ( 1 , 100 , "n" ); inf . readSpace (); inf . readInt ( 1 , 1000000 , "w" ); inf . readEoln (); for ( int i = 0 ; i < n ; ++ i ) { inf . readInt ( 1 , 1000 , "p_i" ); if ( i < n \- 1 ) inf . readSpace (); } inf . readEoln (); } inf . readEof (); } ```   
---|---  
  
## 外部链接

  * [Validator 的更多示例](https://github.com/MikeMirzayanov/testlib/tree/master/validators)
  * [`testlib.h` 的 GitHub 存储库 MikeMirzayanov/testlib](https://github.com/MikeMirzayanov/testlib)

## 参考资料与注释

* * *

  1. [Validators with testlib.h - Codeforces](https://codeforces.com/blog/entry/18426) ↩

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/tools/testlib/validator.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/tools/testlib/validator.md "edit.link.title")  
>  __本页面贡献者：[Xeonacid](https://github.com/Xeonacid), [abc1763613206](https://github.com/abc1763613206), [NachtgeistW](https://github.com/NachtgeistW), [CCXXXI](https://github.com/CCXXXI), [Enter-tainer](https://github.com/Enter-tainer), [fpg2012](https://github.com/fpg2012), [ouuan](mailto:1609483441@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A), [yjl9903](https://github.com/yjl9903)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
