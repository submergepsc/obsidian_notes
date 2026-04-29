# Hello, World! - OI Wiki

- Source: https://oi-wiki.org/lang/helloworld/

# Hello, World!

## 环境配置

工欲善其事，必先利其器．

### 集成开发环境

IDE 操作较为简单，一般入门玩家会选用 IDE 来编写代码．在竞赛中最常见的是 [Dev-C++](../../tools/editor/devcpp/)（如果考试环境是 Windows 系统，一般也会提供这一 IDE）．

### 编译器

#### Windows

推荐使用 GNU 编译器．需要去 [MinGW Distro](https://nuwen.net/mingw.html) 下载 MinGW 并安装．此外 Windows 下也可以选择 [Microsoft Visual C++ 编译器](https://docs.microsoft.com/en-us/cpp/build/projects-and-build-systems-cpp)，需要去 [Visual Studio 页面](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019) 下载安装．

#### macOS

在终端中执行：

```text 1 ``` |  ```text xcode-select \--install ```   
---|---  
  
#### Linux

使用 `g++ -v` 来检查是否安装过 `g++`．

使用如下命令可以安装：

```text 1 ``` |  ```text sudo apt update && sudo apt install g++ ```   
---|---  
  
#### 在命令行中编译代码

熟练之后也有玩家会使用更灵活的命令行来编译代码，这样就不依赖 IDE 了，而是使用自己熟悉的文本编辑器编写代码．

```text 1 ``` |  ```text g++ test.cpp -o test -lm ```   
---|---  
  
`g++` 是 C++ 语言的编译器（C 语言的编译器为 `gcc`），`-o` 用于指定可执行文件的文件名，编译选项 `-lm` 用于链接数学库 `libm`，从而使得使用 `math.h` 的代码可以正常编译运行．

注：C++ 程序不需要 `-lm` 即可正常编译运行．历年 NOI/NOIP 试题的 C++ 编译选项中都带着 `-lm`，故这里也一并加上．

## 第一份代码

通过这样一个示例程序来展开 C++ 入门之旅吧～

注：请在编写前注意开启英文输入法．

C++ 语言

```text 1 2 3 4 5 6 ``` |  ```text #include <iostream> // 引用头文件 int main () { // 定义 main 函数 std :: cout << "Hello, world!" ; // 使用标准命名空间中的 cout 函数 return 0 ; // 返回 0，结束 main 函数．编译器一般会自动加上这一行，一般可以省略 } ```   
---|---  
  
C 语言

```text 1 2 3 4 5 6 ``` |  ```text #include <stdio.h> // 引用头文件 int main () { // 定义 main 函数 printf ( "Hello, world!" ); // 输出 Hello, world! return 0 ; // 返回 0，结束 main 函数 } ```   
---|---  
  
注意：C 语言在这里仅做参考，C++ 基本兼容 C 语言，并且拥有许多新的功能，可以让选手在赛场上事半功倍．具体请见 [C++ 与其他常用语言区别](../cpp-other-langs/)

* * *

>  __本页面最近更新： 2026/1/7 08:56:54，[更新历史](https://github.com/OI-wiki/OI-wiki/commits/master/docs/lang/helloworld.md)  
>  __发现错误？想一起完善？[在 GitHub 上编辑此页！](https://oi-wiki.org/edit-landing/?ref=/lang/helloworld.md "edit.link.title")  
>  __本页面贡献者：[Ir1d](https://github.com/Ir1d), [mgt](mailto:i@margatroid.xyz), [ucSec](https://github.com/ucSec), [lihaoyu1234](https://github.com/lihaoyu1234), [cbw2007](https://github.com/cbw2007), [cmpute](https://github.com/cmpute), [Enter-tainer](https://github.com/Enter-tainer), [ouuan](mailto:1609483441@qq.com), [ouuan](https://github.com/ouuan), [Xeonacid](https://github.com/Xeonacid), [c-forrest](https://github.com/c-forrest), [CoelacanthusHex](https://github.com/CoelacanthusHex), [gavinliu266](https://github.com/gavinliu266), [H-J-Granger](https://github.com/H-J-Granger), [ksyx](https://github.com/ksyx), [NachtgeistW](https://github.com/NachtgeistW), [orzAtalod](https://github.com/orzAtalod), [Persdre](https://github.com/Persdre), [SodaCris](mailto:18463922396@163.com), [Tiphereth-A](https://github.com/Tiphereth-A), [yanboishere](https://github.com/yanboishere)  
>  __本页面的全部内容在**[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh) 和 [SATA](https://github.com/zTrix/sata-license)** 协议之条款下提供，附加条款亦可能应用
