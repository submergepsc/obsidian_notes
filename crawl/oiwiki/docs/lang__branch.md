# 分支 - OI Wiki

- Source: https://oi-wiki.org/lang/branch/

# 分支

一个程序默认是按照代码的顺序执行下来的，有时我们需要选择性的执行某些语句，这时候就需要分支的功能来实现．选择合适的分支语句可以提高程序的效率．

## if 语句

### 基本 if 语句

以下是基本 if 语句的结构．

```text 1 2 3 ``` |  ```text if ( 条件 ) { 主体 ; } ```   
---|---  
  
if 语句通过对条件进行求值，若结果为真（非 0），执行语句，否则不执行．

如果主体中只有单个语句的话，花括号可以省略．

### if...else 语句

```text 1 2 3 4 5 ``` |  ```text if ( 条件 ) { 主体1 ; } else { 主体2 ; } ```   
---|---  
  
if...else 语句和 if 语句类似，else 不需要再写条件．当 if 语句的条件满足时会执行 if 里的语句，if 语句的条件不满足时会执行 else 里的语句．同样，当主体只有一条语句时，可以省略花括号．

### else if 语句

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text if ( 条件1 ) { 主体1 ; } else if ( 条件2 ) { 主体2 ; } else if ( 条件3 ) { 主体3 ; } else { 主体4 ; } ```   
---|---  
  
else if 语句是 if 和 else 的组合，对多个条件进行判断并选择不同的语句分支．在最后一条的 else 语句不需要再写条件．例如，若条件 1 为真，执行主体 1，条件 3 为真而条件 1 和条件 2 都为假，执行主体 3，所有的条件都为假才执行主体 4．

实际上，这一个语句相当于第一个 if 的 else 分句只有一个 if 语句，就将花括号省略之后放在一起了．如果条件相互之间是并列关系，这样写可以让代码的逻辑更清晰．

在逻辑上，大约相当于这一段话：

> 解一元二次方程的时候，方程的根与判别式的关系：
> 
>   * 如果 (Δ <0Δ<0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)) 方程无解；
>   * 否则，如果 (Δ =0Δ=0![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)) 方程有两个相同的实数解；
>   * 否则 方程有两个不相同的实数解；
> 

## switch 语句

```text 1 2 3 4 5 6 7 8 ``` |  ```text switch ( 选择句 ) { case 标签1 : 主体1 ; case 标签2 : 主体2 ; default : 主体3 ; } ```   
---|---  
  
switch 语句执行时，先求出选择句的值，然后根据选择句的值选择相应的标签，从标签处开始执行．其中，选择句必须是一个整数类型表达式，而标签都必须是整数类型的常量．例如：

```text 1 2 3 4 5 6 ``` |  ```text int i = 1 ; // 这里的 i 的数据类型是整型 ，满足整数类型的表达式的要求 switch ( i ) { case 1 : cout << "OI WIKI" << endl ; } ```   
---|---  
  
```text 1 2 3 4 5 6 7 8 ``` |  ```text char i = 'A' ; // 这里的 i 的数据类型是字符型 ，但 char // 也是属于整数的类型，满足整数类型的表达式的要求 switch ( i ) { case 'A' : cout << "OI WIKI" << endl ; } ```   
---|---  
  
switch 语句中还要根据需求加入 break 语句进行中断，否则在对应的 case 被选择之后接下来的所有 case 里的语句和 default 里的语句都会被运行．具体例子可看下面的示例．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` |  ```text char i = 'B' ; switch ( i ) { case 'A' : cout << "OI" << endl ; break ; case 'B' : cout << "WIKI" << endl ; default : cout << "Hello World" << endl ; } ```   
---|---  
  
以上代码运行后输出的结果为 `WIKI` 和 `Hello World`，如果不想让下面分支的语句被运行就需要 break 了，具体例子可看下面的示例．

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text char i = 'B' ; switch ( i ) { case 'A' : cout << "OI" << endl ; break ; case 'B' : cout << "WIKI" << endl ; break ; default : cout << "Hello World" << endl ; } ```   
---|---  
  
以上代码运行后输出的结果为 WIKI，因为 break 的存在，接下来的语句就不会继续被执行了．最后一个语句不需要 break，因为下面没有语句了．

处理入口编号不能重复，但可以颠倒．也就是说，入口编号的顺序不重要．各个 case（包括 default）的出现次序可任意．例如：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text char i = 'B' ; switch ( i ) { case 'B' : cout << "WIKI" << endl ; break ; default : cout << "Hello World" << endl ; break ; case 'A' : cout << "OI" << endl ; } ```   
---|---  
  
switch 的 case 分句中也可以选择性的加花括号．不过要注意的是，如果需要在 switch 语句中定义变量，花括号是必须要加的．例如：

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` |  ```text char i = 'B' ; switch ( i ) { case 'A' : { int i = 1 , j = 2 ; cout << "OI" << endl ; ans = i \+ j ; break ; } case 'B' : { int qwq = 3 ; cout << "WIKI" << endl ; ans = qwq * qwq ; break ; } default : { cout << "Hello World" << endl ; } } ```   
---|---  
  
如何理解 switch

在上文中，用了大量「case 分句」，「case 子句」等用语，实际上，在底层实现中，switch 相当于一组跳转语句．也因此，有 Duff's Device 这种奇技淫巧，希望了解的人可以自行学习．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/branch.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/lang/branch.md "edit.link.title")  
>  __本页面贡献者：[orzAtalod](https://github.com/orzAtalod), [Ir1d](https://github.com/Ir1d), [H-J-Granger](https://github.com/H-J-Granger), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [NachtgeistW](https://github.com/NachtgeistW), [CCXXXI](https://github.com/CCXXXI), [Enter-tainer](https://github.com/Enter-tainer), [mgt](mailto:i@margatroid.xyz), [AngelKitty](https://github.com/AngelKitty), [aofall](https://github.com/aofall), [cjsoft](https://github.com/cjsoft), [diauweb](https://github.com/diauweb), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [Konano](https://github.com/Konano), [ksyx](https://github.com/ksyx), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [Suyun514](mailto:suyun514@qq.com), [weiyong1024](https://github.com/weiyong1024), [billchenchina](https://github.com/billchenchina), [cbw2007](https://github.com/cbw2007), [Chrogeek](https://github.com/Chrogeek), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [ouuan](mailto:1609483441@qq.com), [Peanut-Tang](https://github.com/Peanut-Tang), [SukkaW](https://github.com/SukkaW), [Tiphereth-A](https://github.com/Tiphereth-A), [Tuffy163](https://github.com/Tuffy163)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
