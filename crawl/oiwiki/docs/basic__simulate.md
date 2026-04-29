# 模拟 - OI Wiki

- Source: https://oi-wiki.org/basic/simulate/

# 模拟

本页面将简要介绍模拟算法．

## 简介

模拟就是用计算机来模拟题目中要求的操作．

模拟题目通常具有码量大、操作多、思路繁复的特点．由于它码量大，经常会出现难以查错的情况，如果在考试中写错是相当浪费时间的．

## 技巧

写模拟题时，遵循以下的建议有可能会提升做题速度：

  * 在动手写代码之前，在草纸上尽可能地写好要实现的流程．
  * 在代码中，尽量把每个部分模块化，写成函数、结构体或类．
  * 对于一些可能重复用到的概念，可以统一转化，方便处理：如，某题给你 "YY-MM-DD 时：分" 把它抽取到一个函数，处理成秒，会减少概念混淆．
  * 调试时分块调试．模块化的好处就是可以方便的单独调某一部分．
  * 写代码的时候一定要思路清晰，不要想到什么写什么，要按照落在纸上的步骤写．

实际上，上述步骤在解决其它类型的题目时也是很有帮助的．

## 例题详解

[Climbing Worm](https://open.kattis.com/problems/climbingworm)

一只长度不计的蠕虫位于 𝑛n![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 英寸深的井的底部．它每次向上爬 𝑢u![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 英寸，但是必须休息一次才能再次向上爬．在休息的时候，它滑落了 𝑑d![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) 英寸．之后它将重复向上爬和休息的过程．蠕虫爬出井口需要至少爬多少次？如果蠕虫爬完后刚好到达井的顶部，我们也设作蠕虫已经爬出井口．

解题思路

直接使用程序模拟蠕虫爬井的过程就可以了．用一个循环重复蠕虫的爬井过程，当攀爬的长度超过或者等于井的深度时跳出．

参考代码

C++PythonJava

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` |  ```text #include <iostream> int main () { int n = 0 , u = 0 , d = 0 ; std :: cin >> u >> d >> n ; int time = 0 , dist = 0 ; while ( true ) { // 用死循环来枚举 dist += u ; time ++ ; if ( dist >= n ) break ; // 满足条件则退出死循环 dist -= d ; } std :: cout << time << '\n' ; // 输出得到的结果 return 0 ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 ``` |  ```text u , d , n = map ( int , input () . split ()) time = dist = 0 while True : # 用死循环来枚举 dist += u time += 1 if dist >= n : # 满足条件则退出死循环 break dist -= d print ( time ) # 输出得到的结果 ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text import java.util.Scanner ; public class Main { public static void main ( String [] args ) { Scanner input = new Scanner ( System . in ); int n = input . nextInt (); int u = input . nextInt (); int d = input . nextInt (); int time = 0 , dist = 0 ; while ( true ) { // 用死循环来枚举 dist += u ; time ++ ; if ( dist >= n ) { break ; // 满足条件则退出死循环 } dist -= d ; } System . out . println ( time ); // 输出得到的结果 input . close (); } } ```   
---|---  
  
## 习题

  * [「NOIP2014」生活大爆炸版石头剪刀布 - Universal Online Judge](https://uoj.ac/problem/15)
  * [「OpenJudge 3750」魔兽世界](http://bailian.openjudge.cn/practice/3750/)
  * [「SDOI2010」猪国杀 - LibreOJ](https://loj.ac/problem/2885)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/basic/simulate.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/basic/simulate.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [Tiphereth-A](https://github.com/Tiphereth-A), [H-J-Granger](https://github.com/H-J-Granger), [ksyx](https://github.com/ksyx), [leoleoasd](https://github.com/leoleoasd), [NachtgeistW](https://github.com/NachtgeistW), [ouuan](https://github.com/ouuan), [c-forrest](https://github.com/c-forrest), [ChungZH](https://github.com/ChungZH), [Enter-tainer](https://github.com/Enter-tainer), [i-yyi](https://github.com/i-yyi), [kenlig](https://github.com/kenlig), [LeiJinpeng](https://github.com/LeiJinpeng), [shawlleyw](https://github.com/shawlleyw), [shuzhouliu](https://github.com/shuzhouliu), [StudyingFather](https://github.com/StudyingFather), [WException](https://github.com/WException), [zryi2003](https://github.com/zryi2003)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
