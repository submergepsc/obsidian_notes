# Java 速成 - OI Wiki

- Source: https://oi-wiki.org/lang/java/

# Java 速成

## 关于 Java

Java 是一种广泛使用的计算机编程语言，拥有 **跨平台** 、**面向对象** 、**泛型编程** 的特性，广泛应用于企业级 Web 应用开发和移动应用开发．

## 环境安装

参见 [JDK](../../tools/compiler/#jdk)．

## 基本语法

### 主函数

Java 类似 C/C++ 语言，需要一个函数（在面向对象中，这被称为方法）作为程序执行的入口点．

Java 的主函数的格式是固定的，形如：

```text 1 2 3 4 5 ``` |  ```text class Test { public static void main ( String [] args ) { // 程序的代码 } } ```   
---|---  
  
一个打包的 Java 程序（名称一般是 `*.jar`）中可以有很多个类似的函数，但是当运行这个程序的时候，只有其中一个函数会被运行，这是定义在 `Jar` 的 `Manifest` 文件中的，在 OI 比赛中一般用不到关于它的知识．

### 注释

和 C/C++ 一样，Java 使用 `//` 和 `/* */` 分别注释单行和多行．

### 基本数据类型

类型名| 意义  
---|---  
boolean| 布尔类型  
byte| 字节类型  
char| 字符型  
double| 双精度浮点  
float| 单精度浮点  
int| 整型  
long| 长整型  
short| 短整型  
null| 空  
  
### 声明变量

```text 1 2 3 4 ``` |  ```text int a = 12 ; // 设置 a 为整数类型,并给 a 赋值为 12 String str = "Hello, OI-wiki" ; // 声明字符串变量 str char ch = 'W' ; double PI = 3.1415926 ; ```   
---|---  
  
### final 关键字

`final` 含义是这是最终的、不可更改的结果，被 `final` 修饰的变量只能被赋值一次，赋值后不再改变．

```text 1 ``` |  ```text final double PI = 3.1415926 ; ```   
---|---  
  
### 数组

```text 1 2 3 ``` |  ```text // 有十个元素的整数类型数组 // 其语法格式为 数据类型[] 变量名 = new 数据类型[数组大小] int [] ary = new int [ 10 ] ; ```   
---|---  
  
### 字符串

  * 字符串是 Java 一个内置的类．

```text 1 2 3 4 5 6 ``` |  ```text // 最为简单的构造一个字符串变量的方法如下 String a = "Hello" ; // 还可以使用字符数组构造一个字符串变量 char [] stringArray = { 'H' , 'e' , 'l' , 'l' , 'o' }; String s = new String ( stringArray ); ```   
---|---  
  
### 包和导入包

Java 中的类（`Class`）都被放在一个个包（`package`）里面．在一个包里面不允许有同名的类．在类的第一行通常要说明这个类是属于哪个包的．例如：

```text 1 ``` |  ```text package org.oi \- wiki . tutorial ; ```   
---|---  
  
包的命名规范一般是：`项目所有者的顶级域.项目所有者的二级域.项目名称`．

通过 `import` 关键字来导入不在本类所属的包下面的类．例如下面要用到的 `Scanner`：

```text 1 ``` |  ```text import java.util.Scanner ; ```   
---|---  
  
如果想要导入某包下面所有的类，只需要把这个语句最后的分号前的类名换成 `*`．

### 输入

可以通过 `Scanner` 类来处理命令行输入．

```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text package org.oiwiki.tutorial ; import java.util.Scanner ; class Test { public static void main ( String [] args ) { Scanner scan = new Scanner ( System . in ); // System.in 是输入流 int a = scan . nextInt (); double b = scan . nextDouble (); String c = scan . nextLine (); } } ```   
---|---  
  
### 输出

可以对变量进行格式化输出．

符号| 意义  
---|---  
`%f`| 浮点类型  
`%s`| 字符串类型  
`%d`| 整数类型  
`%c`| 字符类型  
  
```text 1 2 3 4 5 6 7 8 9 10 11 12 ``` |  ```text class Test { public static void main ( String [] args ) { int a = 12 ; char b = 'A' ; double s = 3.14 ; String str = "Hello world" ; System . out . printf ( "%f\n" , s ); System . out . printf ( "%d\n" , a ); System . out . printf ( "%c\n" , b ); System . out . printf ( "%s\n" , str ); } } ```   
---|---  
  
### 控制语句

Java 的流程控制语句与 C++ 是基本相同的．

#### 选择

  * if

```text 1 2 3 4 5 6 7 ``` |  ```text class Test { public static void main ( String [] args ) { if ( /* 判断条件 */ ){ // 条件成立时执行这里面的代码 } } } ```   
---|---  
  
  * if...else

```text 1 2 3 4 5 6 7 8 9 ``` |  ```text class Test { public static void main ( String [] args ) { if ( /* 判断条件 */ ) { // 条件成立时执行这里面的代码 } else { // 条件不成立时执行这里面的代码 } } } ```   
---|---  
  
  * if...else if...else

```text 1 2 3 4 5 6 7 8 9 10 11 ``` |  ```text class Test { public static void main ( String [] args ) { if ( /* 判断条件 */ ) { //判断条件成立执行这里面的代码 } else if ( /* 判断条件2 */ ) { // 判断条件2成立执行这里面的代码 } else { // 上述条件都不成立执行这里面的代码 } } } ```   
---|---  
  
  * switch...case

```text 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` |  ```text class Test { public static void main ( String [] args ) { switch ( /* 表达式 */ ){ case /* 值 1 */ : // 当表达式取得的值符合值 1 执行此段代码 break ; // 如果不加上 break 语句,会让程序按顺序往下执行直到 break case /* 值 2 */ : // 当表达式取得的值符合值 2 执行此段代码 break ; default : // 当表达式不符合上面列举的值的时候执行这里面的代码 } } } ```   
---|---  
  
#### 循环

  * for

`for` 关键字有两种使用方法，其中第一种是普通的 `for` 循环，形式如下：

```text 1 2 3 4 5 6 7 ``` |  ```text class Test { public static void main ( String [] args ) { for ( /* 初始化 */ ; /* 循环的判断条件 */ ; /* 每次循环后执行的步骤 */ ) { // 当循环的条件成立执行循环体内代码 } } } ```   
---|---  
  
第二种是类似 C++ 的 `foreach` 使用方法，用于循环数组或者集合中的数据，相当于把上一种方式中的循环变量隐藏起来了，形式如下：

```text 1 2 3 4 5 6 7 ``` |  ```text class Test { public static void main ( String [] args ) { for ( /* 元素类型X */ /* 元素名Y */ : /* 集合Z */ ) { // 这个语句块的每一次循环时，元素Y分别是集合Z中的一个元素． } } } ```   
---|---  
  
  * while

```text 1 2 3 4 5 6 7 ``` |  ```text class Test { public static void main ( String [] args ) { while ( /* 判定条件 */ ) { // 条件成立时执行循环体内代码 } } } ```   
---|---  
  
  * do...while

```text 1 2 3 4 5 6 7 ``` |  ```text class Test { public static void main ( String [] args ) { do { // 需要执行的代码 } while ( /* 循环判断条件 */ ); } } ```   
---|---  
  
## 注意事项

### 类名与文件名一致

创建 Java 源程序需要类名和文件名一致才能编译通过，否则编译器会提示找不到类．通常该文件名会在具体 OJ 中指定．

例：

`Add.java`

```text 1 2 3 4 5 ``` |  ```text class Add { public static void main ( String [] args ) { // ... } } ```   
---|---  
  
在该文件中需使用 `Add` 为类名方可编译通过．

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/java.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/lang/java.md "edit.link.title")  
>  __本页面贡献者：[jingyuexing](mailto:1941755817@qq.com), [ksyx](https://github.com/ksyx), [qyl27](https://github.com/qyl27), [Ir1d](https://github.com/Ir1d), [H-J-Granger](https://github.com/H-J-Granger), [StudyingFather](https://github.com/StudyingFather), [countercurrent-time](https://github.com/countercurrent-time), [Enter-tainer](https://github.com/Enter-tainer), [mgt](mailto:i@margatroid.xyz), [NachtgeistW](https://github.com/NachtgeistW), [billchenchina](https://github.com/billchenchina), [diauweb](https://github.com/diauweb), [Konano](https://github.com/Konano), [Suyun514](mailto:suyun514@qq.com), [Tiphereth-A](https://github.com/Tiphereth-A), [AngelKitty](https://github.com/AngelKitty), [CCXXXI](https://github.com/CCXXXI), [cjsoft](https://github.com/cjsoft), [CoelacanthusHex](https://github.com/CoelacanthusHex), [Early0v0](https://github.com/Early0v0), [ezoixx130](https://github.com/ezoixx130), [GekkaSaori](https://github.com/GekkaSaori), [LovelyBuggies](https://github.com/LovelyBuggies), [Makkiy](https://github.com/Makkiy), [minghu6](https://github.com/minghu6), [P-Y-Y](https://github.com/P-Y-Y), [PotassiumWings](https://github.com/PotassiumWings), [Qubik65536](https://github.com/Qubik65536), [SamZhangQingChuan](https://github.com/SamZhangQingChuan), [sshwy](https://github.com/sshwy), [weiyong1024](https://github.com/weiyong1024), [1804040636](https://github.com/1804040636), [clansty](https://github.com/clansty), [GavinZhengOI](https://github.com/GavinZhengOI), [Gesrua](https://github.com/Gesrua), [gtn1024](https://github.com/gtn1024), [Henry-ZHR](https://github.com/Henry-ZHR), [kxccc](https://github.com/kxccc), [lychees](https://github.com/lychees), [orzAtalod](https://github.com/orzAtalod), [Peanut-Tang](https://github.com/Peanut-Tang), [shuzhouliu](https://github.com/shuzhouliu), [SukkaW](https://github.com/SukkaW), [Xeonacid](https://github.com/Xeonacid), [yusancky](https://github.com/yusancky), [ZnPdCo](https://github.com/ZnPdCo)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
